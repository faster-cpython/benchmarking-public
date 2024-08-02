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
<td align="left">UNARY_INVERT</td>
<td align="right">1,565,036</td>
<td align="right">2,350,758</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67,886,629</td>
<td align="right">38,875,761</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,037,450</td>
<td align="right">117,335,145</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">2,226,681</td>
<td align="right">1,471,256</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,713,119</td>
<td align="right">2,280,321</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,693,939</td>
<td align="right">54,878,281</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">127,275,293</td>
<td align="right">114,886,580</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">6,164,485</td>
<td align="right">6,609,916</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">42,546,957</td>
<td align="right">40,102,012</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,167,529</td>
<td align="right">9,618,737</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">6,664,843</td>
<td align="right">6,961,597</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,826,345,242</td>
<td align="right">4,665,841,081</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">414,054,569</td>
<td align="right">404,053,329</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">32,318,110</td>
<td align="right">31,604,067</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">39,482,456</td>
<td align="right">40,271,713</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">195,333,234</td>
<td align="right">191,739,027</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,394,138,585</td>
<td align="right">1,368,901,819</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">107,725,660</td>
<td align="right">105,986,140</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">7,497,103</td>
<td align="right">7,610,099</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">106,503,187</td>
<td align="right">105,040,185</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">167,104,328</td>
<td align="right">169,315,119</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">278,711,747</td>
<td align="right">275,420,940</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">83,957,042</td>
<td align="right">84,842,666</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">429,493,949</td>
<td align="right">425,106,142</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,672,118,764</td>
<td align="right">2,645,221,046</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">80,972,119</td>
<td align="right">81,759,309</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">500,740</td>
<td align="right">505,540</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">213,894</td>
<td align="right">211,881</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">71,513,048</td>
<td align="right">70,843,279</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">25,861,339,084</td>
<td align="right">25,621,585,072</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">144,720,875</td>
<td align="right">143,529,660</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">417,971,655</td>
<td align="right">414,722,271</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">953,052,650</td>
<td align="right">946,002,578</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">117,920,433</td>
<td align="right">117,056,813</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">164,080</td>
<td align="right">162,960</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">5,155,650</td>
<td align="right">5,190,020</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">190,270,207</td>
<td align="right">191,492,675</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">76,323,077</td>
<td align="right">75,866,012</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,211,525,422</td>
<td align="right">6,175,066,064</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">513,629,521</td>
<td align="right">516,642,718</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">323,157,876</td>
<td align="right">321,296,391</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,089,393</td>
<td align="right">53,390,909</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,623,088</td>
<td align="right">78,192,385</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,194,090</td>
<td align="right">65,832,325</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">328,927,428</td>
<td align="right">327,266,988</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">49,171,254</td>
<td align="right">49,395,449</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">116,363,295</td>
<td align="right">115,835,096</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">99,327,420</td>
<td align="right">98,885,500</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">6,551,222,428</td>
<td align="right">6,522,577,060</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,246,340,411</td>
<td align="right">6,219,749,478</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,726,181</td>
<td align="right">52,506,181</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">106,117,022</td>
<td align="right">105,676,062</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">170,087,374</td>
<td align="right">170,743,096</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,617,535,031</td>
<td align="right">6,592,036,508</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">430,235,853</td>
<td align="right">428,594,755</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,800,848,042</td>
<td align="right">4,782,574,979</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,585,387</td>
<td align="right">9,619,928</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,214,622,090</td>
<td align="right">1,210,351,889</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">210,158,509</td>
<td align="right">209,422,880</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,149,627,468</td>
<td align="right">1,145,750,505</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,599,937,480</td>
<td align="right">1,594,580,753</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">395,740,860</td>
<td align="right">394,454,813</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">313,691,983</td>
<td align="right">312,674,519</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,424,496,534</td>
<td align="right">3,413,864,365</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">234,435,527</td>
<td align="right">233,725,780</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">415,360,962</td>
<td align="right">414,227,164</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,703,367,484</td>
<td align="right">1,698,752,231</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">400,107,628</td>
<td align="right">399,072,128</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">90,894,340</td>
<td align="right">90,673,780</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">90,899,460</td>
<td align="right">90,678,900</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">144,864,104</td>
<td align="right">144,523,869</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,785,334,598</td>
<td align="right">1,781,223,391</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">146,780</td>
<td align="right">147,100</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">431,294,396</td>
<td align="right">432,192,683</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">301,393,620</td>
<td align="right">302,019,354</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">473,108,476</td>
<td align="right">474,080,809</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,619,412,876</td>
<td align="right">4,610,049,484</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">830,400,689</td>
<td align="right">832,033,185</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">480,098,864</td>
<td align="right">480,884,275</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">933,898,709</td>
<td align="right">935,375,909</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,737,722,745</td>
<td align="right">3,732,331,360</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">329,423,424</td>
<td align="right">328,988,921</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">150,706,294</td>
<td align="right">150,892,072</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">110,978,561</td>
<td align="right">111,112,128</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">290,928,911</td>
<td align="right">291,249,129</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">590,331,032</td>
<td align="right">590,979,975</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">362,205,961</td>
<td align="right">361,809,225</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">689,075,629</td>
<td align="right">688,395,846</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,800,692,104</td>
<td align="right">3,797,022,155</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">13,028,779</td>
<td align="right">13,040,705</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">13,036,539</td>
<td align="right">13,048,465</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,041,335</td>
<td align="right">13,052,983</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">336,183,681</td>
<td align="right">335,901,449</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,097,201,761</td>
<td align="right">4,093,936,484</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,913,573,732</td>
<td align="right">2,915,792,915</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">94,669,848</td>
<td align="right">94,602,255</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">29,879,621</td>
<td align="right">29,859,261</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,783,621</td>
<td align="right">1,784,822</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">122,156,075</td>
<td align="right">122,078,450</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,967,405</td>
<td align="right">48,996,897</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">215,973,826</td>
<td align="right">216,103,440</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,373,130</td>
<td align="right">58,405,470</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,121,736,310</td>
<td align="right">1,122,324,864</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">316,449,677</td>
<td align="right">316,291,182</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">416,469,724</td>
<td align="right">416,265,167</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">266,559,666</td>
<td align="right">266,434,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,298,150,941</td>
<td align="right">3,296,629,331</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,017,105,796</td>
<td align="right">1,016,684,525</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">404,673,545</td>
<td align="right">404,838,561</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">89,262,849</td>
<td align="right">89,298,252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">321,711,688</td>
<td align="right">321,815,849</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,135,806,353</td>
<td align="right">1,136,167,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">620,140,439</td>
<td align="right">619,958,436</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,213,934</td>
<td align="right">9,216,616</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">147,333,859</td>
<td align="right">147,293,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">293,961,542</td>
<td align="right">293,882,483</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,675,936</td>
<td align="right">18,680,950</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,649,394</td>
<td align="right">9,651,939</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">22,317,887</td>
<td align="right">22,323,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">278,871,255</td>
<td align="right">278,936,685</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,428,251</td>
<td align="right">47,437,864</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">766,637,147</td>
<td align="right">766,493,734</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,364,300,293</td>
<td align="right">1,364,074,493</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">64,928,558</td>
<td align="right">64,938,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,086,292</td>
<td align="right">83,096,828</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">16,067</td>
<td align="right">16,065</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,335,092,375</td>
<td align="right">2,334,843,038</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">184,358,712</td>
<td align="right">184,377,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">244,572</td>
<td align="right">244,547</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">48,018,678</td>
<td align="right">48,014,108</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">693,998</td>
<td align="right">693,937</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">72,218,099</td>
<td align="right">72,224,386</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">356,559,005</td>
<td align="right">356,588,217</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,407,188</td>
<td align="right">4,407,494</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">188,500,696</td>
<td align="right">188,513,503</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,111,600</td>
<td align="right">58,107,661</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">451,190,424</td>
<td align="right">451,219,406</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,106,830</td>
<td align="right">91,112,131</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">891,743,389</td>
<td align="right">891,691,751</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,897,473</td>
<td align="right">10,897,133</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,923</td>
<td align="right">1,873,979</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">250,994,197</td>
<td align="right">251,000,397</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,698,937</td>
<td align="right">555,710,751</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">104,684,384</td>
<td align="right">104,686,522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">330,346,707</td>
<td align="right">330,352,775</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">32,555,018</td>
<td align="right">32,555,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">33,301,362</td>
<td align="right">33,301,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">123,542,321</td>
<td align="right">123,542,961</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,925,298,334</td>
<td align="right">1,925,307,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,310,788</td>
<td align="right">20,310,695</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">148,275,484</td>
<td align="right">148,274,830</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">325,120,155</td>
<td align="right">325,119,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">175,140,453</td>
<td align="right">175,140,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,615,620</td>
<td align="right">46,615,636</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,216,940</td>
<td align="right">786,216,956</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,313,413</td>
<td align="right">233,313,411</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,026,448</td>
<td align="right">402,026,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">228,622,192</td>
<td align="right">228,622,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,321,072</td>
<td align="right">173,321,072</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">52,179,040</td>
<td align="right">52,179,040</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">12,088,440</td>
<td align="right">12,088,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">8,000,960</td>
<td align="right">8,000,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,254,180</td>
<td align="right">7,254,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,464,720</td>
<td align="right">3,464,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">2,995,200</td>
<td align="right">2,995,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">719,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">546,420</td>
<td align="right">546,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">151,180</td>
<td align="right">151,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">94,160</td>
<td align="right">94,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">89,680</td>
<td align="right">89,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">49,180</td>
<td align="right">49,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">26,960</td>
<td align="right">26,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">22,820</td>
<td align="right">22,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,020</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,000</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">900</td>
<td align="right">900</td>
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
<td align="right">0.4%</td>
<td align="right">20,454,680</td>
<td align="right">0.2%</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">541,416,243</td>
<td align="right">6.5%</td>
<td align="right">535,641,606</td>
<td align="right">6.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,725,743,511</td>
<td align="right">93.4%</td>
<td align="right">7,691,164,304</td>
<td align="right">93.5%</td>
<td align="right">-0.4%</td>
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
<td align="right">592,397</td>
<td align="right">34.6%</td>
<td align="right">421,723</td>
<td align="right">29.0%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,121,801</td>
<td align="right">65.4%</td>
<td align="right">1,034,069</td>
<td align="right">71.0%</td>
<td align="right">-7.8%</td>
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
<td align="right">38,038</td>
<td align="right">3.4%</td>
<td align="right">23,112</td>
<td align="right">2.2%</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">91,086</td>
<td align="right">8.1%</td>
<td align="right">64,984</td>
<td align="right">6.3%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,607</td>
<td align="right">69.7%</td>
<td align="right">734,129</td>
<td align="right">71.0%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">0.9%</td>
<td align="right">10,320</td>
<td align="right">1.0%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,463</td>
<td align="right">0.9%</td>
<td align="right">10,744</td>
<td align="right">1.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">12,068</td>
<td align="right">1.1%</td>
<td align="right">12,366</td>
<td align="right">1.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,031</td>
<td align="right">2.6%</td>
<td align="right">29,512</td>
<td align="right">2.9%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">12,964</td>
<td align="right">1.2%</td>
<td align="right">12,944</td>
<td align="right">1.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,030</td>
<td align="right">0.4%</td>
<td align="right">5,026</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">15,964</td>
<td align="right">1.4%</td>
<td align="right">15,975</td>
<td align="right">1.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">43,880</td>
<td align="right">3.9%</td>
<td align="right">43,910</td>
<td align="right">4.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,893</td>
<td align="right">0.2%</td>
<td align="right">1,892</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,609</td>
<td align="right">0.8%</td>
<td align="right">8,607</td>
<td align="right">0.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,096</td>
<td align="right">2.9%</td>
<td align="right">32,096</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">15,508</td>
<td align="right">1.4%</td>
<td align="right">15,508</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">5,220</td>
<td align="right">0.5%</td>
<td align="right">5,220</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">4,724</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,600</td>
<td align="right">0.2%</td>
<td align="right">2,600</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
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
<td align="right">419,460,988</td>
<td align="right">8.8%</td>
<td align="right">416,212,556</td>
<td align="right">8.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,355,898,277</td>
<td align="right">91.2%</td>
<td align="right">4,342,248,402</td>
<td align="right">91.2%</td>
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
<td align="right">1,752,349</td>
<td align="right">0.0%</td>
<td align="right">1,752,170</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">149,733</td>
<td align="right">56.9%</td>
<td align="right">148,604</td>
<td align="right">56.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">113,283</td>
<td align="right">43.1%</td>
<td align="right">113,281</td>
<td align="right">43.3%</td>
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
<td align="left">buffer slice</td>
<td align="right">860</td>
<td align="right">0.6%</td>
<td align="right">780</td>
<td align="right">0.5%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,120</td>
<td align="right">0.7%</td>
<td align="right">1,080</td>
<td align="right">0.7%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">44,880</td>
<td align="right">30.0%</td>
<td align="right">44,020</td>
<td align="right">29.6%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,397</td>
<td align="right">20.3%</td>
<td align="right">30,257</td>
<td align="right">20.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">30,972</td>
<td align="right">20.7%</td>
<td align="right">30,963</td>
<td align="right">20.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,760</td>
<td align="right">13.2%</td>
<td align="right">19,760</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">10.8%</td>
<td align="right">16,200</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,320</td>
<td align="right">3.6%</td>
<td align="right">5,320</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">205,842,923</td>
<td align="right">1.6%</td>
<td align="right">203,564,911</td>
<td align="right">1.6%</td>
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
<td align="right">317,764,943</td>
<td align="right">2.5%</td>
<td align="right">315,001,652</td>
<td align="right">2.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,338,465,281</td>
<td align="right">97.5%</td>
<td align="right">12,325,847,556</td>
<td align="right">97.5%</td>
<td align="right">-0.1%</td>
</tr>
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
<td align="right">28,860</td>
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
<td align="right">4,364,735</td>
<td align="right">98.3%</td>
<td align="right">4,321,705</td>
<td align="right">98.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">76,540</td>
<td align="right">1.7%</td>
<td align="right">76,650</td>
<td align="right">1.7%</td>
<td align="right">0.1%</td>
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
<td align="left">wrong number arguments</td>
<td align="right">8,340</td>
<td align="right">10.9%</td>
<td align="right">8,380</td>
<td align="right">10.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">67,720</td>
<td align="right">88.5%</td>
<td align="right">67,790</td>
<td align="right">88.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,100</td>
<td align="right">4.1%</td>
<td align="right">3,100</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">580</td>
<td align="right">0.8%</td>
<td align="right">580</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">480</td>
<td align="right">0.6%</td>
<td align="right">480</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">200</td>
<td align="right">0.3%</td>
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
<td align="right">127,818,906</td>
<td align="right">2.2%</td>
<td align="right">115,425,493</td>
<td align="right">2.0%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">749,378</td>
<td align="right">0.0%</td>
<td align="right">741,119</td>
<td align="right">0.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,771,851,580</td>
<td align="right">97.8%</td>
<td align="right">5,756,648,364</td>
<td align="right">98.0%</td>
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
<td align="right">138,920</td>
<td align="right">67.5%</td>
<td align="right">135,525</td>
<td align="right">67.0%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">66,845</td>
<td align="right">32.5%</td>
<td align="right">66,681</td>
<td align="right">33.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">14,323</td>
<td align="right">10.3%</td>
<td align="right">11,482</td>
<td align="right">8.5%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,080</td>
<td align="right">0.8%</td>
<td align="right">960</td>
<td align="right">0.7%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">500</td>
<td align="right">0.4%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">26,343</td>
<td align="right">19.0%</td>
<td align="right">26,047</td>
<td align="right">19.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,824</td>
<td align="right">8.5%</td>
<td align="right">11,736</td>
<td align="right">8.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,700</td>
<td align="right">13.5%</td>
<td align="right">18,640</td>
<td align="right">13.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,543</td>
<td align="right">1.1%</td>
<td align="right">1,545</td>
<td align="right">1.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">20,504</td>
<td align="right">14.8%</td>
<td align="right">20,530</td>
<td align="right">15.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">26,423</td>
<td align="right">19.0%</td>
<td align="right">26,445</td>
<td align="right">19.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">14,160</td>
<td align="right">10.2%</td>
<td align="right">14,160</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,740</td>
<td align="right">1.3%</td>
<td align="right">1,740</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,740</td>
<td align="right">1.3%</td>
<td align="right">1,740</td>
<td align="right">1.3%</td>
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
<td align="right">236,782,916</td>
<td align="right">9.1%</td>
<td align="right">236,073,580</td>
<td align="right">9.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,370,434,897</td>
<td align="right">90.9%</td>
<td align="right">2,366,773,449</td>
<td align="right">90.9%</td>
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
<td align="right">2,517,260</td>
<td align="right">0.1%</td>
<td align="right">2,517,260</td>
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
<td align="right">110,834</td>
<td align="right">65.2%</td>
<td align="right">110,421</td>
<td align="right">65.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">59,037</td>
<td align="right">34.8%</td>
<td align="right">59,039</td>
<td align="right">34.8%</td>
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
<td align="right">23,342</td>
<td align="right">21.1%</td>
<td align="right">23,100</td>
<td align="right">20.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">16,780</td>
<td align="right">15.1%</td>
<td align="right">16,660</td>
<td align="right">15.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">13,572</td>
<td align="right">12.2%</td>
<td align="right">13,521</td>
<td align="right">12.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">57,140</td>
<td align="right">51.6%</td>
<td align="right">57,140</td>
<td align="right">51.7%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,791</td>
<td align="right">0.0%</td>
<td align="right">168,687</td>
<td align="right">0.0%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">76,345,057</td>
<td align="right">14.2%</td>
<td align="right">75,892,954</td>
<td align="right">14.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">460,664,000</td>
<td align="right">85.8%</td>
<td align="right">460,917,786</td>
<td align="right">85.8%</td>
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
<td align="left">Success</td>
<td align="right">47,683</td>
<td align="right">33.6%</td>
<td align="right">47,757</td>
<td align="right">33.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">94,128</td>
<td align="right">66.4%</td>
<td align="right">93,988</td>
<td align="right">66.3%</td>
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
<td align="left">reversed list</td>
<td align="right">3,320</td>
<td align="right">3.5%</td>
<td align="right">3,220</td>
<td align="right">3.4%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">319</td>
<td align="right">0.3%</td>
<td align="right">320</td>
<td align="right">0.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,460</td>
<td align="right">6.9%</td>
<td align="right">6,480</td>
<td align="right">6.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,146</td>
<td align="right">10.8%</td>
<td align="right">10,132</td>
<td align="right">10.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,359</td>
<td align="right">38.6%</td>
<td align="right">36,311</td>
<td align="right">38.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,564</td>
<td align="right">10.2%</td>
<td align="right">9,565</td>
<td align="right">10.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,720</td>
<td align="right">8.2%</td>
<td align="right">7,720</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,300</td>
<td align="right">7.8%</td>
<td align="right">7,300</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,420</td>
<td align="right">5.8%</td>
<td align="right">5,420</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,840</td>
<td align="right">4.1%</td>
<td align="right">3,840</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,540</td>
<td align="right">1.6%</td>
<td align="right">1,540</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,360</td>
<td align="right">1.4%</td>
<td align="right">1,360</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">560</td>
<td align="right">0.6%</td>
<td align="right">560</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.2%</td>
<td align="right">220</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,036,940,630</td>
<td align="right">92.9%</td>
<td align="right">17,976,702,539</td>
<td align="right">92.9%</td>
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
<td align="right">1,376,493,027</td>
<td align="right">7.1%</td>
<td align="right">1,376,867,743</td>
<td align="right">7.1%</td>
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
<td align="right">246,715,088</td>
<td align="right">1.3%</td>
<td align="right">246,728,440</td>
<td align="right">1.3%</td>
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
<td align="right">323,880</td>
<td align="right">0.0%</td>
<td align="right">323,880</td>
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
<td align="right">829,857</td>
<td align="right">13.8%</td>
<td align="right">829,582</td>
<td align="right">13.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,198,557</td>
<td align="right">86.2%</td>
<td align="right">5,198,806</td>
<td align="right">86.2%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">5,658</td>
<td align="right">0.7%</td>
<td align="right">5,782</td>
<td align="right">0.7%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,249</td>
<td align="right">10.5%</td>
<td align="right">86,179</td>
<td align="right">10.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">54,069</td>
<td align="right">6.5%</td>
<td align="right">54,445</td>
<td align="right">6.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,360</td>
<td align="right">1.7%</td>
<td align="right">14,440</td>
<td align="right">1.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">19,940</td>
<td align="right">2.4%</td>
<td align="right">19,840</td>
<td align="right">2.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,700</td>
<td align="right">3.2%</td>
<td align="right">26,800</td>
<td align="right">3.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,200</td>
<td align="right">1.5%</td>
<td align="right">12,240</td>
<td align="right">1.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,720</td>
<td align="right">1.9%</td>
<td align="right">15,680</td>
<td align="right">1.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">13,346</td>
<td align="right">1.6%</td>
<td align="right">13,324</td>
<td align="right">1.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">45,284</td>
<td align="right">5.5%</td>
<td align="right">45,356</td>
<td align="right">5.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">266,745</td>
<td align="right">32.1%</td>
<td align="right">266,994</td>
<td align="right">32.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">73,065</td>
<td align="right">8.8%</td>
<td align="right">73,006</td>
<td align="right">8.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">179,541</td>
<td align="right">21.6%</td>
<td align="right">179,516</td>
<td align="right">21.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">11,380</td>
<td align="right">1.4%</td>
<td align="right">11,380</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,840</td>
<td align="right">0.3%</td>
<td align="right">2,840</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
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
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
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
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">453,996</td>
<td align="right">0.0%</td>
<td align="right">456,704</td>
<td align="right">0.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,503,845,497</td>
<td align="right">99.7%</td>
<td align="right">7,512,638,184</td>
<td align="right">99.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,317,385</td>
<td align="right">0.3%</td>
<td align="right">20,320,041</td>
<td align="right">0.3%</td>
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
<td align="right">11,460</td>
<td align="right">0.0%</td>
<td align="right">11,460</td>
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
<td align="right">447,399</td>
<td align="right">100.0%</td>
<td align="right">447,358</td>
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
<td align="right">86,157,689</td>
<td align="right">100.0%</td>
<td align="right">86,979,169</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,167</td>
<td align="right">0.0%</td>
<td align="right">8,165</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">7,900</td>
<td align="right">100.0%</td>
<td align="right">7,900</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">786,186,280</td>
<td align="right">81.9%</td>
<td align="right">786,186,296</td>
<td align="right">81.9%</td>
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
<td align="right">173,286,712</td>
<td align="right">18.1%</td>
<td align="right">173,286,712</td>
<td align="right">18.1%</td>
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
<td align="right">5,420</td>
<td align="right">8.3%</td>
<td align="right">5,420</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
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
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">9,960</td>
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
<td align="right">99,411,351</td>
<td align="right">2.7%</td>
<td align="right">98,681,850</td>
<td align="right">2.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,554,803,098</td>
<td align="right">97.2%</td>
<td align="right">3,547,520,607</td>
<td align="right">97.3%</td>
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
<td align="right">68,549,149</td>
<td align="right">1.9%</td>
<td align="right">68,533,180</td>
<td align="right">1.9%</td>
<td align="right">-0.0%</td>
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
<td align="right">71,528</td>
<td align="right">4.9%</td>
<td align="right">71,288</td>
<td align="right">4.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,384,380</td>
<td align="right">95.1%</td>
<td align="right">1,384,109</td>
<td align="right">95.1%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">8,740</td>
<td align="right">12.2%</td>
<td align="right">8,580</td>
<td align="right">12.0%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">2,980</td>
<td align="right">4.2%</td>
<td align="right">2,940</td>
<td align="right">4.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,840</td>
<td align="right">19.3%</td>
<td align="right">13,760</td>
<td align="right">19.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">10,220</td>
<td align="right">14.3%</td>
<td align="right">10,260</td>
<td align="right">14.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">16,728</td>
<td align="right">23.4%</td>
<td align="right">16,728</td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,940</td>
<td align="right">6.9%</td>
<td align="right">4,940</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,860</td>
<td align="right">6.8%</td>
<td align="right">4,860</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,360</td>
<td align="right">6.1%</td>
<td align="right">4,360</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3,940</td>
<td align="right">5.5%</td>
<td align="right">3,940</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">800</td>
<td align="right">1.1%</td>
<td align="right">800</td>
<td align="right">1.1%</td>
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
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">851,579,101</td>
<td align="right">92.9%</td>
<td align="right">850,265,718</td>
<td align="right">92.9%</td>
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
<td align="right">64,864,755</td>
<td align="right">7.1%</td>
<td align="right">64,874,763</td>
<td align="right">7.1%</td>
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
<td align="right">52,760</td>
<td align="right">82.7%</td>
<td align="right">52,838</td>
<td align="right">82.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,043</td>
<td align="right">17.3%</td>
<td align="right">11,041</td>
<td align="right">17.3%</td>
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
<td align="left">out of range</td>
<td align="right">780</td>
<td align="right">1.5%</td>
<td align="right">800</td>
<td align="right">1.5%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,120</td>
<td align="right">2.1%</td>
<td align="right">1,140</td>
<td align="right">2.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">10,160</td>
<td align="right">19.3%</td>
<td align="right">10,178</td>
<td align="right">19.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">33,160</td>
<td align="right">62.9%</td>
<td align="right">33,180</td>
<td align="right">62.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">12.3%</td>
<td align="right">6,480</td>
<td align="right">12.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,040</td>
<td align="right">2.0%</td>
<td align="right">1,040</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">527,892,796</td>
<td align="right">7.0%</td>
<td align="right">528,650,963</td>
<td align="right">7.1%</td>
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
<td align="right">6,960,100,422</td>
<td align="right">92.9%</td>
<td align="right">6,951,129,501</td>
<td align="right">92.9%</td>
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
<td align="right">49,141,984</td>
<td align="right">0.7%</td>
<td align="right">49,114,437</td>
<td align="right">0.7%</td>
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
<td align="right">236,528</td>
<td align="right">17.5%</td>
<td align="right">236,734</td>
<td align="right">17.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,111,524</td>
<td align="right">82.5%</td>
<td align="right">1,111,015</td>
<td align="right">82.4%</td>
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
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.6%</td>
<td align="right">1,740</td>
<td align="right">0.7%</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">14,640</td>
<td align="right">6.2%</td>
<td align="right">14,520</td>
<td align="right">6.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">14,726</td>
<td align="right">6.2%</td>
<td align="right">14,690</td>
<td align="right">6.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,353</td>
<td align="right">5.6%</td>
<td align="right">13,377</td>
<td align="right">5.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,216</td>
<td align="right">11.5%</td>
<td align="right">27,261</td>
<td align="right">11.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,618</td>
<td align="right">2.0%</td>
<td align="right">4,613</td>
<td align="right">1.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">42,428</td>
<td align="right">17.9%</td>
<td align="right">42,469</td>
<td align="right">17.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">48,020</td>
<td align="right">20.3%</td>
<td align="right">48,001</td>
<td align="right">20.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">68,607</td>
<td align="right">29.0%</td>
<td align="right">68,603</td>
<td align="right">29.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.4%</td>
<td align="right">1,040</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">420</td>
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
<td align="right">1,530,002,967</td>
<td align="right">100.0%</td>
<td align="right">1,530,211,286</td>
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
<td align="right">215,355</td>
<td align="right">0.0%</td>
<td align="right">215,339</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">2,073</td>
<td align="right">7.1%</td>
<td align="right">2,072</td>
<td align="right">7.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">27,144</td>
<td align="right">92.9%</td>
<td align="right">27,136</td>
<td align="right">92.9%</td>
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
<td align="left">sequence</td>
<td align="right">1,433</td>
<td align="right">69.1%</td>
<td align="right">1,432</td>
<td align="right">69.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">18.3%</td>
<td align="right">380</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">12.5%</td>
<td align="right">260</td>
<td align="right">12.5%</td>
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
<td align="right">683,292,349</td>
<td align="right">0.5%</td>
<td align="right">671,936,834</td>
<td align="right">0.5%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">50,497,471,027</td>
<td align="right">37.6%</td>
<td align="right">50,094,337,881</td>
<td align="right">37.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">70,215,419,934</td>
<td align="right">52.3%</td>
<td align="right">69,867,333,574</td>
<td align="right">52.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">12,781,863,416</td>
<td align="right">9.5%</td>
<td align="right">12,732,030,948</td>
<td align="right">9.5%</td>
<td align="right">-0.4%</td>
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
<td align="right">127,818,906</td>
<td align="right">3.2%</td>
<td align="right">115,425,493</td>
<td align="right">2.9%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">541,416,243</td>
<td align="right">13.6%</td>
<td align="right">535,641,606</td>
<td align="right">13.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">317,764,943</td>
<td align="right">8.0%</td>
<td align="right">315,001,652</td>
<td align="right">8.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">419,460,988</td>
<td align="right">10.5%</td>
<td align="right">416,212,556</td>
<td align="right">10.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">99,411,351</td>
<td align="right">2.5%</td>
<td align="right">98,681,850</td>
<td align="right">2.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">76,345,057</td>
<td align="right">1.9%</td>
<td align="right">75,892,954</td>
<td align="right">1.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">236,782,916</td>
<td align="right">5.9%</td>
<td align="right">236,073,580</td>
<td align="right">6.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">527,892,796</td>
<td align="right">13.3%</td>
<td align="right">528,650,963</td>
<td align="right">13.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,376,493,027</td>
<td align="right">34.6%</td>
<td align="right">1,376,867,743</td>
<td align="right">34.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,286,712</td>
<td align="right">4.4%</td>
<td align="right">173,286,712</td>
<td align="right">4.4%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">100,730,061</td>
<td align="right">13.2%</td>
<td align="right">98,424,796</td>
<td align="right">13.1%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">38,933,921</td>
<td align="right">5.1%</td>
<td align="right">39,011,715</td>
<td align="right">5.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,206,169</td>
<td align="right">3.3%</td>
<td align="right">25,192,120</td>
<td align="right">3.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">100,600,426</td>
<td align="right">13.2%</td>
<td align="right">100,619,626</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">73,012,616</td>
<td align="right">9.6%</td>
<td align="right">73,016,740</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,962,926</td>
<td align="right">5.4%</td>
<td align="right">40,960,810</td>
<td align="right">5.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,323,660</td>
<td align="right">5.7%</td>
<td align="right">43,321,740</td>
<td align="right">5.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,874,851</td>
<td align="right">10.2%</td>
<td align="right">77,874,586</td>
<td align="right">10.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,874,851</td>
<td align="right">10.2%</td>
<td align="right">77,874,586</td>
<td align="right">10.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,511,497</td>
<td align="right">3.6%</td>
<td align="right">27,511,571</td>
<td align="right">3.7%</td>
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
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,312,387,798</td>
<td align="right">68.4%</td>
<td align="right">6,304,014,977</td>
<td align="right">68.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">2,051,314,504</td>
<td align="right">22.2%</td>
<td align="right">2,053,419,887</td>
<td align="right">22.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">2,055,748,964</td>
<td align="right">22.3%</td>
<td align="right">2,057,854,347</td>
<td align="right">22.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">475,172,323</td>
<td align="right">5.1%</td>
<td align="right">475,626,027</td>
<td align="right">5.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">7,524,229,564</td>
<td align="right">81.5%</td>
<td align="right">7,518,080,610</td>
<td align="right">81.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,916,022,903</td>
<td align="right">31.6%</td>
<td align="right">2,918,242,647</td>
<td align="right">31.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,916,022,903</td>
<td align="right">31.6%</td>
<td align="right">2,918,242,647</td>
<td align="right">31.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,657,654</td>
<td align="right">0.8%</td>
<td align="right">71,670,109</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,273,939</td>
<td align="right">9.3%</td>
<td align="right">860,388,300</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">590,983,017</td>
<td align="right">6.4%</td>
<td align="right">591,006,263</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">28,604,632</td>
<td align="right">0.3%</td>
<td align="right">28,605,712</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,380,872</td>
<td align="right">2.3%</td>
<td align="right">211,380,984</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,411,640</td>
<td align="right">0.0%</td>
<td align="right">4,411,640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">22,820</td>
<td align="right">0.0%</td>
<td align="right">22,820</td>
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
<td align="right">3,324,371</td>
<td align="right"></td>
<td align="right">3,655,404</td>
<td align="right"></td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">29,081,738</td>
<td align="right"></td>
<td align="right">28,456,207</td>
<td align="right"></td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">32,221,055</td>
<td align="right"></td>
<td align="right">31,929,043</td>
<td align="right"></td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">58,888,380,749</td>
<td align="right">46.0%</td>
<td align="right">58,415,572,067</td>
<td align="right">45.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">73,628,020,861</td>
<td align="right">50.5%</td>
<td align="right">73,167,615,205</td>
<td align="right">50.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">69,123,513,731</td>
<td align="right">54.0%</td>
<td align="right">69,405,100,764</td>
<td align="right">54.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">72,094,508,239</td>
<td align="right">49.5%</td>
<td align="right">72,379,629,425</td>
<td align="right">49.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,872,924,508</td>
<td align="right">37.7%</td>
<td align="right">6,898,032,105</td>
<td align="right">37.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,874,735,366</td>
<td align="right"></td>
<td align="right">6,899,807,972</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">19,751,650</td>
<td align="right">0.1%</td>
<td align="right">19,815,304</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">149,918,154</td>
<td align="right"></td>
<td align="right">150,146,538</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,842,164</td>
<td align="right">0.6%</td>
<td align="right">103,744,524</td>
<td align="right">0.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,239,053,787</td>
<td align="right">61.6%</td>
<td align="right">11,228,774,135</td>
<td align="right">61.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,362,647,601</td>
<td align="right">62.3%</td>
<td align="right">11,352,333,963</td>
<td align="right">62.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">11,712,009,023</td>
<td align="right"></td>
<td align="right">11,701,468,568</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,656,184,742</td>
<td align="right"></td>
<td align="right">2,657,321,503</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,219,022,633</td>
<td align="right"></td>
<td align="right">4,220,309,965</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,271,180</td>
<td align="right">2.2%</td>
<td align="right">3,271,180</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">63,920</td>
<td align="right">0.0%</td>
<td align="right">63,920</td>
<td align="right">0.0%</td>
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
<td align="right">19,263,360</td>
<td align="right">14,481,225,685</td>
<td align="right">0</td>
<td align="right">18,587,580</td>
<td align="right">14,472,141,048</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">7,052,530,544</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">7,056,289,296</td>
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,724</td>
<td align="right">0.9%</td>
<td align="right">8,626</td>
<td align="right">1.2%</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">680</td>
<td align="right">0.1%</td>
<td align="right">821</td>
<td align="right">0.1%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">45,342</td>
<td align="right">6.1%</td>
<td align="right">45,738</td>
<td align="right">6.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">197,864,357,853</td>
<td align="right">2,805.8%</td>
<td align="right">196,205,990,537</td>
<td align="right">2,787.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,320</td>
<td align="right">6.3%</td>
<td align="right">6,268</td>
<td align="right">6.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">440,072</td>
<td align="right">59.6%</td>
<td align="right">441,090</td>
<td align="right">59.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,052,030,664</td>
<td align="right"></td>
<td align="right">7,040,138,683</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">637,866</td>
<td align="right">86.3%</td>
<td align="right">638,779</td>
<td align="right">86.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">101,055</td>
<td align="right">13.7%</td>
<td align="right">100,930</td>
<td align="right">13.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">738,921</td>
<td align="right"></td>
<td align="right">739,709</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,320</td>
<td align="right">0.2%</td>
<td align="right">1,320</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,380</td>
<td align="right">2.4%</td>
<td align="right">2,464</td>
<td align="right">2.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">97,455</td>
<td align="right">96.4%</td>
<td align="right">97,246</td>
<td align="right">96.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">101,055</td>
<td align="right"></td>
<td align="right">100,930</td>
<td align="right"></td>
<td align="right">-0.1%</td>
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
<td align="right">4,618</td>
<td align="right">4.6%</td>
<td align="right">4,601</td>
<td align="right">4.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">19,549</td>
<td align="right">19.3%</td>
<td align="right">18,914</td>
<td align="right">18.7%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">32,128</td>
<td align="right">31.8%</td>
<td align="right">24,881</td>
<td align="right">24.7%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">24,593</td>
<td align="right">24.3%</td>
<td align="right">27,902</td>
<td align="right">27.6%</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">12,748</td>
<td align="right">12.6%</td>
<td align="right">15,273</td>
<td align="right">15.1%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,919</td>
<td align="right">5.9%</td>
<td align="right">7,379</td>
<td align="right">7.3%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,340</td>
<td align="right">1.3%</td>
<td align="right">1,760</td>
<td align="right">1.7%</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">220</td>
<td align="right">0.2%</td>
<td align="right">37.5%</td>
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
<td align="right">3,738</td>
<td align="right">3.7%</td>
<td align="right">3,761</td>
<td align="right">3.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">13,619</td>
<td align="right">13.5%</td>
<td align="right">13,579</td>
<td align="right">13.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,448</td>
<td align="right">21.2%</td>
<td align="right">17,589</td>
<td align="right">17.4%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">32,158</td>
<td align="right">31.8%</td>
<td align="right">29,669</td>
<td align="right">29.4%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">15,871</td>
<td align="right">15.7%</td>
<td align="right">20,073</td>
<td align="right">19.9%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,681</td>
<td align="right">7.6%</td>
<td align="right">8,635</td>
<td align="right">8.6%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,520</td>
<td align="right">2.5%</td>
<td align="right">3,400</td>
<td align="right">3.4%</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">420</td>
<td align="right">0.4%</td>
<td align="right">540</td>
<td align="right">0.5%</td>
<td align="right">28.6%</td>
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
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">168,024,180</td>
<td align="right">158.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,543,809,959</td>
<td align="right">1,285,357,107</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">779,818,805</td>
<td align="right">423,396,627</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">59,932,296</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">67,378,216</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">213,616,900</td>
<td align="right">164,181,600</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,376,579,748</td>
<td align="right">1,077,450,341</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">953,916,585</td>
<td align="right">806,898,663</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,412,274,200</td>
<td align="right">1,218,851,215</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,732,660</td>
<td align="right">22,299,320</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">108,946,791</td>
<td align="right">122,529,073</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">693,021,671</td>
<td align="right">623,364,852</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">112,664,108</td>
<td align="right">123,774,208</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,116,480</td>
<td align="right">2,310,100</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">109,954,401</td>
<td align="right">119,426,761</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">400,417,746</td>
<td align="right">366,563,415</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,183,412,092</td>
<td align="right">2,000,438,345</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,692,400</td>
<td align="right">843,602,203</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,068,492</td>
<td align="right">605,160,194</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,549,860</td>
<td align="right">1,212,791,480</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">63,297,168</td>
<td align="right">59,828,999</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,354,518</td>
<td align="right">11,936,947</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,354,518</td>
<td align="right">11,936,947</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,269,819,826</td>
<td align="right">2,384,511,879</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,296,663,606</td>
<td align="right">2,407,753,099</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,006,791,515</td>
<td align="right">1,044,700,313</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">100,741,179</td>
<td align="right">97,141,234</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">100,985,299</td>
<td align="right">97,385,354</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,069,714</td>
<td align="right">33,847,163</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,940</td>
<td align="right">395,745,863</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">412,003,423</td>
<td align="right">422,090,589</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">576,387,742</td>
<td align="right">588,041,622</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,152,031,526</td>
<td align="right">1,174,934,511</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,693,312,236</td>
<td align="right">6,822,936,415</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">872,260,413</td>
<td align="right">888,467,358</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,252,079,926</td>
<td align="right">1,274,989,011</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,270,568,506</td>
<td align="right">1,293,753,251</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">112,297,118</td>
<td align="right">114,213,855</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">331,497,409</td>
<td align="right">326,028,092</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">724,070,332</td>
<td align="right">735,811,810</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,995,479</td>
<td align="right">7,108,358</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,818,687,156</td>
<td align="right">2,861,758,647</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,671,816,548</td>
<td align="right">1,694,979,704</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">266,488,322</td>
<td align="right">263,046,045</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">267,715,142</td>
<td align="right">264,272,865</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,870,718,186</td>
<td align="right">1,892,531,577</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,937,531</td>
<td align="right">10,049,053</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,986,059,142</td>
<td align="right">2,007,532,930</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,804,278,686</td>
<td align="right">1,823,709,777</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,136,883,597</td>
<td align="right">7,212,408,276</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">594,001,440</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">186,240,377</td>
<td align="right">184,549,252</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,319,591,685</td>
<td align="right">1,330,850,901</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,522,499,907</td>
<td align="right">6,575,688,770</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">168,871,776</td>
<td align="right">167,511,712</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">61,351,100</td>
<td align="right">61,839,320</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,737,540,101</td>
<td align="right">5,692,220,624</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">61,237,200</td>
<td align="right">61,703,140</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,873,534,962</td>
<td align="right">1,859,599,136</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,206,912,124</td>
<td align="right">3,226,207,975</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">172,901,604</td>
<td align="right">171,916,270</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,182,771,641</td>
<td align="right">2,193,650,972</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">30,103,210</td>
<td align="right">29,956,015</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">13,843,402,220</td>
<td align="right">13,904,832,113</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,753,207,808</td>
<td align="right">11,795,604,420</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">765,311,297</td>
<td align="right">762,632,697</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,050,310,370</td>
<td align="right">1,046,778,167</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">225,199,422</td>
<td align="right">224,492,115</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,444,698,246</td>
<td align="right">3,455,058,050</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">73,721,330</td>
<td align="right">73,940,789</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">115,374,216</td>
<td align="right">115,034,613</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">29,840</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,341,173,793</td>
<td align="right">1,337,738,445</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,962,581,408</td>
<td align="right">4,950,850,138</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">232,297,125</td>
<td align="right">231,783,806</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,573,700,234</td>
<td align="right">4,563,694,925</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">565,248,258</td>
<td align="right">564,069,053</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">360,373,186</td>
<td align="right">359,635,483</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,979,877,175</td>
<td align="right">1,976,239,220</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,751,676,669</td>
<td align="right">4,743,907,387</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,650,239,284</td>
<td align="right">2,646,787,870</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">24,792,655</td>
<td align="right">24,822,954</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,346,052,653</td>
<td align="right">1,344,458,957</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,875,012</td>
<td align="right">4,869,620</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">129,064,729</td>
<td align="right">129,204,155</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">169,270,806</td>
<td align="right">169,096,303</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">171,803,346</td>
<td align="right">171,628,763</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">542,202,399</td>
<td align="right">541,668,840</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,126,976</td>
<td align="right">202,940,537</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">20,517,860</td>
<td align="right">20,499,060</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">551,408,389</td>
<td align="right">550,904,781</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,413,438</td>
<td align="right">134,290,958</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,413,438</td>
<td align="right">134,290,958</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,445,806</td>
<td align="right">126,331,212</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,847,740</td>
<td align="right">61,901,440</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,039,091,059</td>
<td align="right">1,038,257,290</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,386,063,840</td>
<td align="right">1,384,978,421</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">712,952,418</td>
<td align="right">713,477,755</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,612,011,938</td>
<td align="right">9,618,889,274</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">243,726,152</td>
<td align="right">243,552,194</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,096,765,197</td>
<td align="right">2,095,431,500</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,538,110</td>
<td align="right">45,566,618</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">485,499,956</td>
<td align="right">485,197,068</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,551,273,443</td>
<td align="right">1,550,409,681</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">35,252,540</td>
<td align="right">35,233,740</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">133,753,389</td>
<td align="right">133,689,606</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,316,631,119</td>
<td align="right">1,317,230,729</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">315,070,246</td>
<td align="right">314,926,805</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">16,606,026</td>
<td align="right">16,613,287</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,281,485</td>
<td align="right">779,610,807</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">445,198</td>
<td align="right">445,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">146,425,607</td>
<td align="right">146,367,203</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,105,547,465</td>
<td align="right">1,105,919,464</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,652,798,047</td>
<td align="right">1,652,282,211</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,320,219</td>
<td align="right">733,537,403</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">118,379,682</td>
<td align="right">118,346,750</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,940,263,457</td>
<td align="right">2,939,602,301</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,228,356,692</td>
<td align="right">2,227,863,110</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,007,422,954</td>
<td align="right">1,007,644,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,134,080</td>
<td align="right">8,132,320</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">342,055,932</td>
<td align="right">341,991,066</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">966,694,293</td>
<td align="right">966,517,270</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">198,202,879</td>
<td align="right">198,168,277</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">217,935,111</td>
<td align="right">217,972,508</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,114,185,769</td>
<td align="right">1,114,372,664</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">129,511,603</td>
<td align="right">129,532,430</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">128,316,783</td>
<td align="right">128,337,290</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,610,440</td>
<td align="right">3,609,940</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">6,582,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,274,712,029</td>
<td align="right">1,274,544,916</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,958,840</td>
<td align="right">144,940,040</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">333,579,925</td>
<td align="right">333,541,053</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">936,564,898</td>
<td align="right">936,670,561</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">154,019,990</td>
<td align="right">154,003,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">843,045,309</td>
<td align="right">843,122,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,237,738,516</td>
<td align="right">1,237,835,531</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">2,089,449,256</td>
<td align="right">2,089,288,545</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">618,183,850</td>
<td align="right">618,226,311</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,416,484,274</td>
<td align="right">6,416,889,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,659,680</td>
<td align="right">5,660,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,339,434,108</td>
<td align="right">1,339,361,651</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">147,768,739</td>
<td align="right">147,760,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">4,437,918</td>
<td align="right">4,437,684</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,759,083</td>
<td align="right">229,770,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,603,217,799</td>
<td align="right">3,603,382,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">280,850,033</td>
<td align="right">280,838,635</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,318,790</td>
<td align="right">32,317,522</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">330,496,142</td>
<td align="right">330,507,770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,719,340</td>
<td align="right">509,703,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,832,037</td>
<td align="right">101,828,949</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,696,220</td>
<td align="right">12,695,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">224,637,144</td>
<td align="right">224,630,816</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">686,574,234</td>
<td align="right">686,555,054</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">592,435,763</td>
<td align="right">592,451,729</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">93,670,740</td>
<td align="right">93,668,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">145,316,240</td>
<td align="right">145,312,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">382,061,069</td>
<td align="right">382,053,289</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">409,588,287</td>
<td align="right">409,580,114</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,260,809,096</td>
<td align="right">3,260,744,830</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">55,151,871</td>
<td align="right">55,150,857</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,552,680</td>
<td align="right">187,549,440</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,366,953,155</td>
<td align="right">1,366,931,622</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">198,827,979</td>
<td align="right">198,831,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">957,248,268</td>
<td align="right">957,233,872</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">790,293,630</td>
<td align="right">790,304,849</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">485,544,179</td>
<td align="right">485,538,312</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,387,083</td>
<td align="right">78,386,232</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,515,156</td>
<td align="right">93,514,200</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">219,072,476</td>
<td align="right">219,070,648</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,283,720</td>
<td align="right">54,283,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,580,380</td>
<td align="right">80,579,760</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,816,480,658</td>
<td align="right">1,816,467,483</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">63,419,660</td>
<td align="right">63,419,280</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">88,989,715</td>
<td align="right">88,989,185</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">230,441,900</td>
<td align="right">230,440,800</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,041,860</td>
<td align="right">22,041,780</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">93,410,418</td>
<td align="right">93,410,121</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,032,620</td>
<td align="right">533,031,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,197,370</td>
<td align="right">97,197,582</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,156,010</td>
<td align="right">98,156,222</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,199,232</td>
<td align="right">101,199,114</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">423,778,101</td>
<td align="right">423,777,651</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,912,848</td>
<td align="right">9,912,852</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,039,100</td>
<td align="right">199,039,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,870,774</td>
<td align="right">68,870,763</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,868,360</td>
<td align="right">149,868,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">99,651,520</td>
<td align="right">99,651,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">66,194,480</td>
<td align="right">66,194,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">14,734,660</td>
<td align="right">14,734,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,625,240</td>
<td align="right">4,625,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,943,300</td>
<td align="right">1,943,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,889,580</td>
<td align="right">1,889,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,543,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,160</td>
<td align="right">821,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">647,416</td>
<td align="right">647,416</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">543,660</td>
<td align="right">543,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">71,760</td>
<td align="right">71,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">34,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">7,620</td>
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
<td align="left">BEFORE_WITH</td>
<td align="right">1,487</td>
<td align="right">1,502</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">82,830</td>
<td align="right">82,222</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,417</td>
<td align="right">2,400</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">4,981</td>
<td align="right">4,960</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,592</td>
<td align="right">6,578</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40,590</td>
<td align="right">40,545</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">32,220</td>
<td align="right">32,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">29,080</td>
<td align="right">29,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,221</td>
<td align="right">2,221</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,660</td>
<td align="right">1,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,340</td>
<td align="right">1,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">540</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">260</td>
<td align="right">260</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,080</td>
<td align="right">1,084</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,080</td>
<td align="right">1,084</td>
<td align="right">0.4%</td>
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
<td align="right">240</td>
<td align="right">240</td>
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
<td align="right">360</td>
<td align="right">360</td>
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
<td align="right">1,900</td>
<td align="right">1,900</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-05-10
