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
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">262,727,380</td>
<td align="right">17,338,948</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">5,694,716</td>
<td align="right">1,386,916</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">237,304,302</td>
<td align="right">59,233,339</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">23,304,832</td>
<td align="right">6,571,808</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,030,372</td>
<td align="right">2,833,920</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">219,584,203</td>
<td align="right">66,903,927</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,144</td>
<td align="right">886,004</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">274,808,044</td>
<td align="right">94,710,621</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">796,008,458</td>
<td align="right">310,984,298</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,545,875</td>
<td align="right">2,181,165</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">64,315,267</td>
<td align="right">26,254,738</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">29,331,002</td>
<td align="right">12,597,992</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">50,776,628</td>
<td align="right">21,957,607</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">15,324,677</td>
<td align="right">6,914,302</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,466,393</td>
<td align="right">2,050,347</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">53,588,827</td>
<td align="right">28,145,630</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">9,526,061</td>
<td align="right">5,085,237</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,304,343</td>
<td align="right">15,971,731</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">175,186,557</td>
<td align="right">98,757,211</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">975,868,561</td>
<td align="right">605,101,434</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">16,597,327</td>
<td align="right">10,631,589</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">153,671,508</td>
<td align="right">99,288,225</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">119,084,811</td>
<td align="right">78,291,167</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">742,745,694</td>
<td align="right">495,571,146</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,948,398</td>
<td align="right">2,003,444</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">51,635,298</td>
<td align="right">35,898,424</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">365,751,045</td>
<td align="right">255,392,170</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">486,224,020</td>
<td align="right">339,658,982</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">596,356,056</td>
<td align="right">420,511,336</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,375,236</td>
<td align="right">23,899,434</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">66,380,047</td>
<td align="right">47,673,297</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">156,744,095</td>
<td align="right">112,897,223</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">476,157,520</td>
<td align="right">344,905,076</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">220,887,142</td>
<td align="right">160,738,190</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">6,495</td>
<td align="right">8,235</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,851,191</td>
<td align="right">2,103,431</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,409,247,022</td>
<td align="right">3,278,932,339</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">179,170,442</td>
<td align="right">133,482,057</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,400,079,144</td>
<td align="right">2,562,698,227</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">810,624,515</td>
<td align="right">618,299,761</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,764,347,339</td>
<td align="right">2,880,554,896</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">423,211,359</td>
<td align="right">324,135,075</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">31,319,438</td>
<td align="right">24,124,597</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">185,419,090</td>
<td align="right">142,844,590</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,310,331,619</td>
<td align="right">1,793,137,882</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,847,800,800</td>
<td align="right">1,444,483,900</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">361,058,648</td>
<td align="right">282,759,881</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">102,933,608</td>
<td align="right">81,386,748</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">492,604,214</td>
<td align="right">389,638,524</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">98,083,062</td>
<td align="right">77,726,052</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">348,373,683</td>
<td align="right">276,714,622</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,838,749,365</td>
<td align="right">1,460,893,719</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,965,533,560</td>
<td align="right">2,362,292,257</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">633,380,698</td>
<td align="right">506,882,137</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">396,237,821</td>
<td align="right">318,010,675</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,065,889</td>
<td align="right">13,709,362</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,065,909</td>
<td align="right">13,709,383</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">266,156,566</td>
<td align="right">215,506,986</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,601,641,805</td>
<td align="right">2,925,477,336</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,921,243,677</td>
<td align="right">1,560,700,493</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">494,044,205</td>
<td align="right">401,342,899</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">16,904,293</td>
<td align="right">13,734,487</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">68,498,826</td>
<td align="right">55,714,741</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">145,138,451</td>
<td align="right">118,372,042</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">109,438,121</td>
<td align="right">89,548,421</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">135,630,819</td>
<td align="right">111,092,001</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">185,756,907</td>
<td align="right">153,039,068</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">604,032,675</td>
<td align="right">498,931,210</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">156,853,674</td>
<td align="right">129,610,913</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">741,626,136</td>
<td align="right">613,084,689</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">14,802,479,723</td>
<td align="right">12,239,875,508</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,993,331,525</td>
<td align="right">3,318,658,558</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">357,703,146</td>
<td align="right">297,517,484</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">95,804,540</td>
<td align="right">79,790,659</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">202,055,534</td>
<td align="right">168,827,841</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">62,750,871</td>
<td align="right">52,670,063</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,861,662,562</td>
<td align="right">1,564,938,221</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">101,323,135</td>
<td align="right">85,217,443</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,333,806,012</td>
<td align="right">1,123,892,564</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">846,151,136</td>
<td align="right">717,338,349</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">996,982,352</td>
<td align="right">850,308,404</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">27,766,519</td>
<td align="right">23,695,386</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,085,654</td>
<td align="right">933,214</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">43,319,969</td>
<td align="right">37,480,289</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">66,528,405</td>
<td align="right">57,571,653</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">443,170,229</td>
<td align="right">384,071,092</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">94,059,746</td>
<td align="right">82,280,555</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">188,551,916</td>
<td align="right">164,967,915</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">38,751,194</td>
<td align="right">33,917,665</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">110,010,413</td>
<td align="right">96,431,593</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">325,509,564</td>
<td align="right">285,381,387</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">44,929,453</td>
<td align="right">39,398,951</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">374,072,664</td>
<td align="right">328,509,252</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,285,044</td>
<td align="right">4,651,526</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">350,491,346</td>
<td align="right">309,692,126</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,668,296,807</td>
<td align="right">4,130,259,623</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">75,094,302</td>
<td align="right">67,123,430</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,560,534</td>
<td align="right">15,715,751</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">178,449,429</td>
<td align="right">160,059,135</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,353,714,151</td>
<td align="right">2,115,656,392</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">50,620,623</td>
<td align="right">45,629,088</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">109,066,769</td>
<td align="right">98,492,050</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">421,435,873</td>
<td align="right">381,749,851</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">146,094,435</td>
<td align="right">133,716,377</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">166,191,032</td>
<td align="right">152,407,343</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">62,985,590</td>
<td align="right">57,816,763</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">266,546,444</td>
<td align="right">245,880,420</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">76,690,033</td>
<td align="right">70,939,393</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">317,789,656</td>
<td align="right">294,609,880</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">91,262,042</td>
<td align="right">84,658,321</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">736,111,721</td>
<td align="right">683,133,304</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">195,950,630</td>
<td align="right">182,044,999</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">239,386,399</td>
<td align="right">223,504,798</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">615,203,630</td>
<td align="right">574,410,781</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">468,522,077</td>
<td align="right">439,492,844</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">346,964,049</td>
<td align="right">326,450,781</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,720,505</td>
<td align="right">24,280,227</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">192,680,214</td>
<td align="right">182,593,418</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">75,612,871</td>
<td align="right">71,739,716</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">129,431,922</td>
<td align="right">123,076,543</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">867,731,089</td>
<td align="right">828,627,911</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,356</td>
<td align="right">1,296</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">164,452,987</td>
<td align="right">157,276,089</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">113,727,890</td>
<td align="right">109,005,041</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">114,765,185</td>
<td align="right">110,062,660</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">33,973,066</td>
<td align="right">32,584,493</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,241,535</td>
<td align="right">3,364,290</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">31,971</td>
<td align="right">30,770</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">187,184,693</td>
<td align="right">180,987,172</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">984,390,505</td>
<td align="right">952,501,457</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,443,064</td>
<td align="right">13,876,762</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">148,375,149</td>
<td align="right">143,639,643</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,630,172</td>
<td align="right">56,152,095</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,426</td>
<td align="right">3,346</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">13,153</td>
<td align="right">12,874</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">56,449,811</td>
<td align="right">57,555,629</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,220,702</td>
<td align="right">2,179,642</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">118,262,816</td>
<td align="right">116,309,669</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">503,864,244</td>
<td align="right">495,663,016</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">252,365</td>
<td align="right">248,673</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">128,955,681</td>
<td align="right">127,132,730</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,472,065,523</td>
<td align="right">1,451,716,057</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">123,753,233</td>
<td align="right">122,216,157</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">53,803,093</td>
<td align="right">53,172,413</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,926,884</td>
<td align="right">10,033,396</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">166,602,714</td>
<td align="right">165,040,491</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">133,549,177</td>
<td align="right">132,319,292</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,447,761</td>
<td align="right">12,554,678</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">164,932,386</td>
<td align="right">163,524,631</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">276,267</td>
<td align="right">274,324</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,864</td>
<td align="right">3,844</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,268</td>
<td align="right">57,028</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">287,808,666</td>
<td align="right">288,697,804</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,141</td>
<td align="right">301,326,615</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">163,586,585</td>
<td align="right">163,139,910</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">733,591,995</td>
<td align="right">731,623,092</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,110,729,248</td>
<td align="right">1,107,835,755</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">66,884,069</td>
<td align="right">66,729,043</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">51,212,331</td>
<td align="right">51,114,290</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,456</td>
<td align="right">5,466</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,089,900</td>
<td align="right">5,085,867</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,262,386</td>
<td align="right">1,262,082</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,961,273</td>
<td align="right">27,955,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,164,522</td>
<td align="right">418,100,423</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">441,342</td>
<td align="right">441,279</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,763,054</td>
<td align="right">14,761,227</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">821,805,815</td>
<td align="right">821,723,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,365,793</td>
<td align="right">70,362,279</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,965,411</td>
<td align="right">41,966,731</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,633</td>
<td align="right">9,742,533</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,048,027</td>
<td align="right">3,047,996</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">8,709,159</td>
<td align="right">8,709,092</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,098</td>
<td align="right">35,549,081</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,619,539</td>
<td align="right">591,619,522</td>
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
<td align="right">128,851,732</td>
<td align="right">128,851,732</td>
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
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
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
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,721,848</td>
<td align="right">1,721,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">117,444</td>
<td align="right">117,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,575</td>
<td align="right">98,575</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,564</td>
<td align="right">72,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,551</td>
<td align="right">69,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,850</td>
<td align="right">53,850</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">13,984</td>
<td align="right">13,984</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,641</td>
<td align="right">2,641</td>
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
<td align="right">996,560,354</td>
<td align="right">5.9%</td>
<td align="right">849,979,502</td>
<td align="right">5.1%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,213,747</td>
<td align="right">0.3%</td>
<td align="right">46,098,176</td>
<td align="right">0.3%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,953,848,401</td>
<td align="right">93.8%</td>
<td align="right">15,869,421,661</td>
<td align="right">94.7%</td>
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
<td align="right">403,462</td>
<td align="right">28.7%</td>
<td align="right">311,237</td>
<td align="right">26.0%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,003,442</td>
<td align="right">71.3%</td>
<td align="right">887,268</td>
<td align="right">74.0%</td>
<td align="right">-11.6%</td>
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
<td align="right">11,552</td>
<td align="right">2.9%</td>
<td align="right">3,772</td>
<td align="right">1.2%</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">72,758</td>
<td align="right">18.0%</td>
<td align="right">24,879</td>
<td align="right">8.0%</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,293</td>
<td align="right">2.1%</td>
<td align="right">4,756</td>
<td align="right">1.5%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">37,617</td>
<td align="right">9.3%</td>
<td align="right">23,497</td>
<td align="right">7.5%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">21,075</td>
<td align="right">5.2%</td>
<td align="right">14,789</td>
<td align="right">4.8%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">18,005</td>
<td align="right">4.5%</td>
<td align="right">13,156</td>
<td align="right">4.2%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.6%</td>
<td align="right">1,863</td>
<td align="right">0.6%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21,004</td>
<td align="right">5.2%</td>
<td align="right">18,085</td>
<td align="right">5.8%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,130</td>
<td align="right">0.8%</td>
<td align="right">2,827</td>
<td align="right">0.9%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,477</td>
<td align="right">1.6%</td>
<td align="right">6,077</td>
<td align="right">2.0%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">16,343</td>
<td align="right">4.1%</td>
<td align="right">15,343</td>
<td align="right">4.9%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">25,838</td>
<td align="right">6.4%</td>
<td align="right">24,268</td>
<td align="right">7.8%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,120</td>
<td align="right">0.5%</td>
<td align="right">2,000</td>
<td align="right">0.6%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,364</td>
<td align="right">0.3%</td>
<td align="right">1,304</td>
<td align="right">0.4%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">107</td>
<td align="right">0.0%</td>
<td align="right">103</td>
<td align="right">0.0%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,830</td>
<td align="right">4.9%</td>
<td align="right">19,126</td>
<td align="right">6.1%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,767</td>
<td align="right">0.7%</td>
<td align="right">2,727</td>
<td align="right">0.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,194</td>
<td align="right">1.5%</td>
<td align="right">6,134</td>
<td align="right">2.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">330</td>
<td align="right">0.1%</td>
<td align="right">332</td>
<td align="right">0.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,016</td>
<td align="right">1.7%</td>
<td align="right">6,986</td>
<td align="right">2.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">289</td>
<td align="right">0.1%</td>
<td align="right">288</td>
<td align="right">0.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">625</td>
<td align="right">0.2%</td>
<td align="right">623</td>
<td align="right">0.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">28,692</td>
<td align="right">7.1%</td>
<td align="right">28,612</td>
<td align="right">9.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">1,814</td>
<td align="right">0.4%</td>
<td align="right">1,810</td>
<td align="right">0.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,469</td>
<td align="right">4.6%</td>
<td align="right">18,487</td>
<td align="right">5.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">63,003</td>
<td align="right">15.6%</td>
<td align="right">63,006</td>
<td align="right">20.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">2,935</td>
<td align="right">0.7%</td>
<td align="right">2,935</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">0.5%</td>
<td align="right">1,996</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">836</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">157</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">149</td>
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
<td align="left">and different types</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">5</td>
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
<td align="right">179,170,442</td>
<td align="right">100.0%</td>
<td align="right">133,482,057</td>
<td align="right">100.0%</td>
<td align="right">-25.5%</td>
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
<td align="right">143,353,894</td>
<td align="right">1.6%</td>
<td align="right">135,704,106</td>
<td align="right">1.6%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">140,724,875</td>
<td align="right">1.6%</td>
<td align="right">133,219,065</td>
<td align="right">1.6%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,620,254,152</td>
<td align="right">98.4%</td>
<td align="right">8,342,857,280</td>
<td align="right">98.4%</td>
<td align="right">-3.2%</td>
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
<td align="right">2,881,238</td>
<td align="right">100.0%</td>
<td align="right">2,733,568</td>
<td align="right">100.0%</td>
<td align="right">-5.1%</td>
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
<td align="left">init not simple</td>
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">594</td>
<td align="right">406.8%</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">247</td>
<td align="right">169.2%</td>
<td align="right">-7.5%</td>
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
<td align="right">576,076</td>
<td align="right">96.6%</td>
<td align="right">576,078</td>
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
<td align="right">583,374</td>
<td align="right">97.8%</td>
<td align="right">583,374</td>
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
<td align="right">20,451</td>
<td align="right">100.0%</td>
<td align="right">20,170</td>
<td align="right">100.0%</td>
<td align="right">-1.4%</td>
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
<td align="right">91,149,524</td>
<td align="right">2.0%</td>
<td align="right">84,548,481</td>
<td align="right">1.9%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,036,555</td>
<td align="right">0.0%</td>
<td align="right">1,023,109</td>
<td align="right">0.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,407,777,517</td>
<td align="right">97.9%</td>
<td align="right">4,394,130,340</td>
<td align="right">98.1%</td>
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
<td align="right">94,107</td>
<td align="right">71.4%</td>
<td align="right">91,661</td>
<td align="right">71.1%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">37,748</td>
<td align="right">28.6%</td>
<td align="right">37,294</td>
<td align="right">28.9%</td>
<td align="right">-1.2%</td>
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
<td align="right">838</td>
<td align="right">0.9%</td>
<td align="right">718</td>
<td align="right">0.8%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">9,400</td>
<td align="right">10.0%</td>
<td align="right">8,088</td>
<td align="right">8.8%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,080</td>
<td align="right">4.3%</td>
<td align="right">3,802</td>
<td align="right">4.1%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">31,820</td>
<td align="right">33.8%</td>
<td align="right">31,264</td>
<td align="right">34.1%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">5,854</td>
<td align="right">6.2%</td>
<td align="right">5,791</td>
<td align="right">6.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">372</td>
<td align="right">0.4%</td>
<td align="right">369</td>
<td align="right">0.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,640</td>
<td align="right">8.1%</td>
<td align="right">7,588</td>
<td align="right">8.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,883</td>
<td align="right">2.0%</td>
<td align="right">1,889</td>
<td align="right">2.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,095</td>
<td align="right">24.5%</td>
<td align="right">23,028</td>
<td align="right">25.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,323</td>
<td align="right">1.4%</td>
<td align="right">1,322</td>
<td align="right">1.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">8.1%</td>
<td align="right">7,648</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">154</td>
<td align="right">0.2%</td>
<td align="right">154</td>
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
<td align="right">75,572,193</td>
<td align="right">3.9%</td>
<td align="right">71,701,526</td>
<td align="right">3.8%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,842,155,797</td>
<td align="right">96.0%</td>
<td align="right">1,814,560,465</td>
<td align="right">96.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,389,959</td>
<td align="right">0.1%</td>
<td align="right">1,389,907</td>
<td align="right">0.1%</td>
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
<td align="right">38,360</td>
<td align="right">57.3%</td>
<td align="right">35,992</td>
<td align="right">55.9%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,541</td>
<td align="right">42.7%</td>
<td align="right">28,421</td>
<td align="right">44.1%</td>
<td align="right">-0.4%</td>
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
<td align="right">11,267</td>
<td align="right">29.4%</td>
<td align="right">10,188</td>
<td align="right">28.3%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,094</td>
<td align="right">23.7%</td>
<td align="right">8,563</td>
<td align="right">23.8%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">7,772</td>
<td align="right">20.3%</td>
<td align="right">7,392</td>
<td align="right">20.5%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,227</td>
<td align="right">26.7%</td>
<td align="right">9,849</td>
<td align="right">27.4%</td>
<td align="right">-3.7%</td>
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
<td align="right">44,183,392</td>
<td align="right">3.0%</td>
<td align="right">29,060,286</td>
<td align="right">2.2%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,212,156,703</td>
<td align="right">83.5%</td>
<td align="right">1,117,898,089</td>
<td align="right">84.1%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">195,838,916</td>
<td align="right">13.5%</td>
<td align="right">181,937,392</td>
<td align="right">13.7%</td>
<td align="right">-7.1%</td>
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
<td align="right">838,952</td>
<td align="right">88.8%</td>
<td align="right">553,618</td>
<td align="right">84.4%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">106,271</td>
<td align="right">11.2%</td>
<td align="right">102,159</td>
<td align="right">15.6%</td>
<td align="right">-3.9%</td>
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
<td align="left">ascii string</td>
<td align="right">956</td>
<td align="right">0.9%</td>
<td align="right">717</td>
<td align="right">0.7%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,762</td>
<td align="right">4.5%</td>
<td align="right">3,582</td>
<td align="right">3.5%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,619</td>
<td align="right">1.5%</td>
<td align="right">1,841</td>
<td align="right">1.8%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,140</td>
<td align="right">3.0%</td>
<td align="right">2,720</td>
<td align="right">2.7%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,665</td>
<td align="right">5.3%</td>
<td align="right">5,024</td>
<td align="right">4.9%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,167</td>
<td align="right">3.9%</td>
<td align="right">3,979</td>
<td align="right">3.9%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,779</td>
<td align="right">12.0%</td>
<td align="right">12,238</td>
<td align="right">12.0%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">50,153</td>
<td align="right">47.2%</td>
<td align="right">49,124</td>
<td align="right">48.1%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,567</td>
<td align="right">3.4%</td>
<td align="right">3,609</td>
<td align="right">3.5%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">10,885</td>
<td align="right">10.2%</td>
<td align="right">10,765</td>
<td align="right">10.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,497</td>
<td align="right">3.3%</td>
<td align="right">3,477</td>
<td align="right">3.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,211</td>
<td align="right">4.0%</td>
<td align="right">4,213</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">0.2%</td>
<td align="right">232</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">221</td>
<td align="right">0.2%</td>
<td align="right">221</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">90</td>
<td align="right">0.1%</td>
<td align="right">90</td>
<td align="right">0.1%</td>
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
<td align="left">generator</td>
<td align="right">85,275,392</td>
<td align="right">85,275,392 / 0 !!</td>
<td align="right">64,903,557</td>
<td align="right">64,903,557 / 0 !!</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,049,799</td>
<td align="right">4,049,799 / 0 !!</td>
<td align="right">3,273,352</td>
<td align="right">3,273,352 / 0 !!</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">120,862,094</td>
<td align="right">120,862,094 / 0 !!</td>
<td align="right">104,682,680</td>
<td align="right">104,682,680 / 0 !!</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">249,102,797</td>
<td align="right">249,102,797 / 0 !!</td>
<td align="right">224,716,667</td>
<td align="right">224,716,667 / 0 !!</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,604,985</td>
<td align="right">2,604,985 / 0 !!</td>
<td align="right">2,496,632</td>
<td align="right">2,496,632 / 0 !!</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111,977,360</td>
<td align="right">111,977,360 / 0 !!</td>
<td align="right">108,781,107</td>
<td align="right">108,781,107 / 0 !!</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,055,082</td>
<td align="right">12,055,082 / 0 !!</td>
<td align="right">11,935,843</td>
<td align="right">11,935,843 / 0 !!</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,680,084</td>
<td align="right">341,680,084 / 0 !!</td>
<td align="right">341,714,390</td>
<td align="right">341,714,390 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,651,422</td>
<td align="right">34,651,422 / 0 !!</td>
<td align="right">34,650,122</td>
<td align="right">34,650,122 / 0 !!</td>
<td align="right">-0.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">492,011,975</td>
<td align="right">4.7%</td>
<td align="right">315,252,316</td>
<td align="right">3.2%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">491,195,869</td>
<td align="right">4.7%</td>
<td align="right">388,603,937</td>
<td align="right">4.0%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,540,465,683</td>
<td align="right">90.6%</td>
<td align="right">9,061,688,714</td>
<td align="right">92.8%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,262,389</td>
<td align="right">0.0%</td>
<td align="right">1,262,389</td>
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
<td align="right">9,402,241</td>
<td align="right">95.6%</td>
<td align="right">6,096,977</td>
<td align="right">93.7%</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">433,291</td>
<td align="right">4.4%</td>
<td align="right">409,895</td>
<td align="right">6.3%</td>
<td align="right">-5.4%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">19,539</td>
<td align="right">4.5%</td>
<td align="right">13,325</td>
<td align="right">3.3%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">6,391</td>
<td align="right">1.5%</td>
<td align="right">4,808</td>
<td align="right">1.2%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">40,786</td>
<td align="right">9.4%</td>
<td align="right">32,504</td>
<td align="right">7.9%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">35,999</td>
<td align="right">8.3%</td>
<td align="right">30,594</td>
<td align="right">7.5%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,667</td>
<td align="right">0.4%</td>
<td align="right">1,569</td>
<td align="right">0.4%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,334</td>
<td align="right">3.5%</td>
<td align="right">15,131</td>
<td align="right">3.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">47,866</td>
<td align="right">11.0%</td>
<td align="right">47,325</td>
<td align="right">11.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,886</td>
<td align="right">1.1%</td>
<td align="right">4,909</td>
<td align="right">1.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">1.0%</td>
<td align="right">4,448</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,379</td>
<td align="right">0.5%</td>
<td align="right">2,379</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,647</td>
<td align="right">0.4%</td>
<td align="right">1,647</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,033</td>
<td align="right">0.2%</td>
<td align="right">1,033</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">703</td>
<td align="right">0.2%</td>
<td align="right">703</td>
<td align="right">0.2%</td>
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
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">4,281,824,311</td>
<td align="right">99.7%</td>
<td align="right">3,489,529,740</td>
<td align="right">99.6%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">47,425</td>
<td align="right">0.0%</td>
<td align="right">45,905</td>
<td align="right">0.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,623,435</td>
<td align="right">0.3%</td>
<td align="right">14,623,333</td>
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
<td align="right">1,381</td>
<td align="right">0.0%</td>
<td align="right">1,381</td>
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
<td align="right">140,330</td>
<td align="right">100.0%</td>
<td align="right">138,565</td>
<td align="right">100.0%</td>
<td align="right">-1.3%</td>
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
<td align="right">65,058,340</td>
<td align="right">100.0%</td>
<td align="right">65,611,550</td>
<td align="right">100.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">216</td>
<td align="right">0.0%</td>
<td align="right">216</td>
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
<td align="right">2,425</td>
<td align="right">100.0%</td>
<td align="right">2,425</td>
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
<td align="right">591,604,828</td>
<td align="right">82.1%</td>
<td align="right">591,604,811</td>
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
<td align="right">128,816,934</td>
<td align="right">17.9%</td>
<td align="right">128,816,934</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">82,596,182</td>
<td align="right">4.5%</td>
<td align="right">41,893,292</td>
<td align="right">2.4%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">51,552,829</td>
<td align="right">2.8%</td>
<td align="right">35,823,957</td>
<td align="right">2.0%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,699,932,209</td>
<td align="right">92.7%</td>
<td align="right">1,688,384,640</td>
<td align="right">95.6%</td>
<td align="right">-0.7%</td>
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
<td align="right">1,599,666</td>
<td align="right">97.5%</td>
<td align="right">831,660</td>
<td align="right">96.2%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40,336</td>
<td align="right">2.5%</td>
<td align="right">32,670</td>
<td align="right">3.8%</td>
<td align="right">-19.0%</td>
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
<td align="right">15,813</td>
<td align="right">39.2%</td>
<td align="right">9,773</td>
<td align="right">29.9%</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">704</td>
<td align="right">1.7%</td>
<td align="right">504</td>
<td align="right">1.5%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,781</td>
<td align="right">9.4%</td>
<td align="right">2,821</td>
<td align="right">8.6%</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,519</td>
<td align="right">3.8%</td>
<td align="right">1,419</td>
<td align="right">4.3%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,207</td>
<td align="right">17.9%</td>
<td align="right">6,847</td>
<td align="right">21.0%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,650</td>
<td align="right">11.5%</td>
<td align="right">4,691</td>
<td align="right">14.4%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,446</td>
<td align="right">8.5%</td>
<td align="right">3,422</td>
<td align="right">10.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">241,128</td>
<td align="right">597.8%</td>
<td align="right">240,296</td>
<td align="right">735.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">1.0%</td>
<td align="right">423</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">365</td>
<td align="right">0.9%</td>
<td align="right">365</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">94</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">91</td>
<td align="right">0.3%</td>
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
<td align="right">1,085,654</td>
<td align="right">100.0%</td>
<td align="right">933,214</td>
<td align="right">100.0%</td>
<td align="right">-14.0%</td>
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
<td align="right">101,286,071</td>
<td align="right">10.9%</td>
<td align="right">85,186,361</td>
<td align="right">9.6%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">828,043,016</td>
<td align="right">89.1%</td>
<td align="right">804,822,097</td>
<td align="right">90.4%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">940</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">Failure</td>
<td align="right">34,903</td>
<td align="right">94.1%</td>
<td align="right">29,037</td>
<td align="right">93.4%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,181</td>
<td align="right">5.9%</td>
<td align="right">2,045</td>
<td align="right">6.6%</td>
<td align="right">-6.2%</td>
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
<td align="left">list slice</td>
<td align="right">2,511</td>
<td align="right">7.2%</td>
<td align="right">851</td>
<td align="right">2.9%</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">10,484</td>
<td align="right">30.0%</td>
<td align="right">8,298</td>
<td align="right">28.6%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">1.0%</td>
<td align="right">301</td>
<td align="right">1.0%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,566</td>
<td align="right">47.5%</td>
<td align="right">14,726</td>
<td align="right">50.7%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,563</td>
<td align="right">4.5%</td>
<td align="right">1,423</td>
<td align="right">4.9%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">3,323</td>
<td align="right">9.5%</td>
<td align="right">3,323</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">47</td>
<td align="right">0.1%</td>
<td align="right">47</td>
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
<td align="right">60,712,178</td>
<td align="right">1.9%</td>
<td align="right">52,687,125</td>
<td align="right">1.8%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,948,205,070</td>
<td align="right">93.9%</td>
<td align="right">2,698,188,633</td>
<td align="right">93.9%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,986,143</td>
<td align="right">4.1%</td>
<td align="right">122,748,863</td>
<td align="right">4.3%</td>
<td align="right">-4.8%</td>
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
<td align="right">394,166</td>
<td align="right">24.8%</td>
<td align="right">276,844</td>
<td align="right">21.0%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,195,500</td>
<td align="right">75.2%</td>
<td align="right">1,043,379</td>
<td align="right">79.0%</td>
<td align="right">-12.7%</td>
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
<td align="right">26,677</td>
<td align="right">6.8%</td>
<td align="right">4,566</td>
<td align="right">1.6%</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">54,384</td>
<td align="right">13.8%</td>
<td align="right">31,199</td>
<td align="right">11.3%</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">206,224</td>
<td align="right">52.3%</td>
<td align="right">136,072</td>
<td align="right">49.2%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">262</td>
<td align="right">0.1%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">10,430</td>
<td align="right">2.6%</td>
<td align="right">10,046</td>
<td align="right">3.6%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">70,981</td>
<td align="right">18.0%</td>
<td align="right">69,629</td>
<td align="right">25.2%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">8,840</td>
<td align="right">2.2%</td>
<td align="right">8,830</td>
<td align="right">3.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,067</td>
<td align="right">2.6%</td>
<td align="right">10,059</td>
<td align="right">3.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,677</td>
<td align="right">1.2%</td>
<td align="right">4,677</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.4%</td>
<td align="right">1,420</td>
<td align="right">0.5%</td>
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
<td align="right">915,486,128</td>
<td align="right">99.9%</td>
<td align="right">892,277,697</td>
<td align="right">99.9%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,251,635</td>
<td align="right">0.1%</td>
<td align="right">1,251,600</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">10,001</td>
<td align="right">92.7%</td>
<td align="right">9,702</td>
<td align="right">92.6%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">790</td>
<td align="right">7.3%</td>
<td align="right">780</td>
<td align="right">7.4%</td>
<td align="right">-1.3%</td>
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
<td align="right">556</td>
<td align="right">70.4%</td>
<td align="right">546</td>
<td align="right">70.0%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">17.2%</td>
<td align="right">136</td>
<td align="right">17.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">12.4%</td>
<td align="right">98</td>
<td align="right">12.6%</td>
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
<td align="right">878,304,020</td>
<td align="right">1.0%</td>
<td align="right">623,909,528</td>
<td align="right">0.8%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">52,923,574,850</td>
<td align="right">59.2%</td>
<td align="right">43,124,085,996</td>
<td align="right">58.6%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">32,696,320,072</td>
<td align="right">36.6%</td>
<td align="right">27,367,048,509</td>
<td align="right">37.2%</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,954,248,096</td>
<td align="right">3.3%</td>
<td align="right">2,503,479,773</td>
<td align="right">3.4%</td>
<td align="right">-15.3%</td>
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
<td align="left">BINARY_SLICE</td>
<td align="right">179,170,442</td>
<td align="right">6.9%</td>
<td align="right">133,482,057</td>
<td align="right">6.0%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">491,195,869</td>
<td align="right">18.9%</td>
<td align="right">388,603,937</td>
<td align="right">17.4%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">101,286,071</td>
<td align="right">3.9%</td>
<td align="right">85,186,361</td>
<td align="right">3.8%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">996,560,354</td>
<td align="right">38.4%</td>
<td align="right">849,979,502</td>
<td align="right">38.1%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">91,149,524</td>
<td align="right">3.5%</td>
<td align="right">84,548,481</td>
<td align="right">3.8%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">195,838,916</td>
<td align="right">7.5%</td>
<td align="right">181,937,392</td>
<td align="right">8.1%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">140,724,875</td>
<td align="right">5.4%</td>
<td align="right">133,219,065</td>
<td align="right">6.0%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">75,572,193</td>
<td align="right">2.9%</td>
<td align="right">71,701,526</td>
<td align="right">3.2%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">128,986,143</td>
<td align="right">5.0%</td>
<td align="right">122,748,863</td>
<td align="right">5.5%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,934</td>
<td align="right">5.0%</td>
<td align="right">128,816,934</td>
<td align="right">5.8%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">63,600,567</td>
<td align="right">7.2%</td>
<td align="right">22,915,307</td>
<td align="right">3.7%</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">59,549,214</td>
<td align="right">6.8%</td>
<td align="right">30,487,698</td>
<td align="right">4.9%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">174,364,503</td>
<td align="right">19.8%</td>
<td align="right">101,557,195</td>
<td align="right">16.3%</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">137,614,666</td>
<td align="right">15.7%</td>
<td align="right">88,803,006</td>
<td align="right">14.2%</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">70,162,933</td>
<td align="right">8.0%</td>
<td align="right">49,568,417</td>
<td align="right">7.9%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">28,461,740</td>
<td align="right">3.2%</td>
<td align="right">24,475,813</td>
<td align="right">3.9%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">49,548,253</td>
<td align="right">5.6%</td>
<td align="right">46,153,616</td>
<td align="right">7.4%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">26,557,208</td>
<td align="right">3.0%</td>
<td align="right">24,829,016</td>
<td align="right">4.0%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">24,725,131</td>
<td align="right">2.8%</td>
<td align="right">24,723,261</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">22,073,155</td>
<td align="right">2.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20,872,888</td>
<td align="right">3.3%</td>
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
<td align="right">63,727,983</td>
<td align="right">1.1%</td>
<td align="right">58,465,229</td>
<td align="right">1.0%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,208,861</td>
<td align="right">0.4%</td>
<td align="right">22,210,352</td>
<td align="right">0.4%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,335,438,811</td>
<td align="right">74.6%</td>
<td align="right">4,177,224,322</td>
<td align="right">74.2%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">4,480,568,477</td>
<td align="right">77.1%</td>
<td align="right">4,324,337,552</td>
<td align="right">76.8%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">228,782,109</td>
<td align="right">3.9%</td>
<td align="right">221,263,246</td>
<td align="right">3.9%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">886,644,493</td>
<td align="right">15.3%</td>
<td align="right">865,896,099</td>
<td align="right">15.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">890,919,550</td>
<td align="right">15.3%</td>
<td align="right">870,169,996</td>
<td align="right">15.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">232,557,982</td>
<td align="right">4.0%</td>
<td align="right">227,916,391</td>
<td align="right">4.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,475,190,486</td>
<td align="right">25.4%</td>
<td align="right">1,454,272,222</td>
<td align="right">25.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,475,190,486</td>
<td align="right">25.4%</td>
<td align="right">1,454,272,222</td>
<td align="right">25.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
<td align="right">3,844</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,270,936</td>
<td align="right">10.1%</td>
<td align="right">584,102,226</td>
<td align="right">10.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,271,193</td>
<td align="right">0.1%</td>
<td align="right">4,270,053</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,901</td>
<td align="right">2.3%</td>
<td align="right">132,513,901</td>
<td align="right">2.4%</td>
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
<td align="right">37,731,918</td>
<td align="right"></td>
<td align="right">20,290,620</td>
<td align="right"></td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">41,445,328</td>
<td align="right"></td>
<td align="right">23,012,624</td>
<td align="right"></td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">3,976,184</td>
<td align="right"></td>
<td align="right">2,768,228</td>
<td align="right"></td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">219,028</td>
<td align="right">0.1%</td>
<td align="right">157,888</td>
<td align="right">0.1%</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">1,799,545,017</td>
<td align="right"></td>
<td align="right">1,498,696,792</td>
<td align="right"></td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">22,837,721,598</td>
<td align="right">27.8%</td>
<td align="right">19,666,685,013</td>
<td align="right">24.9%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,153,770,990</td>
<td align="right">1.2%</td>
<td align="right">1,004,338,157</td>
<td align="right">1.1%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">29,135,016,687</td>
<td align="right">29.6%</td>
<td align="right">26,447,037,554</td>
<td align="right">27.8%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,759,979,773</td>
<td align="right">3.4%</td>
<td align="right">2,511,207,905</td>
<td align="right">3.2%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">1,779,125,944</td>
<td align="right"></td>
<td align="right">1,672,196,099</td>
<td align="right"></td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">4,657,728,361</td>
<td align="right">26.4%</td>
<td align="right">4,506,076,031</td>
<td align="right">26.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">5,217,793,071</td>
<td align="right"></td>
<td align="right">5,048,863,047</td>
<td align="right"></td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">4,734,950,757</td>
<td align="right">26.9%</td>
<td align="right">4,582,919,884</td>
<td align="right">26.5%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,264,982</td>
<td align="right">0.0%</td>
<td align="right">6,079,481</td>
<td align="right">0.0%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">34,517,953,375</td>
<td align="right">42.0%</td>
<td align="right">35,512,632,907</td>
<td align="right">44.9%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">21,980,455,124</td>
<td align="right">26.8%</td>
<td align="right">21,348,796,080</td>
<td align="right">27.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">168,653,072</td>
<td align="right"></td>
<td align="right">164,047,243</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">23,580,085,117</td>
<td align="right">24.0%</td>
<td align="right">22,978,963,082</td>
<td align="right">24.1%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,899,985,445</td>
<td align="right"></td>
<td align="right">12,741,228,819</td>
<td align="right"></td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,899,839,861</td>
<td align="right">73.1%</td>
<td align="right">12,741,118,210</td>
<td align="right">73.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">44,521,676,281</td>
<td align="right">45.2%</td>
<td align="right">44,769,465,601</td>
<td align="right">47.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">70,957,414</td>
<td align="right">0.4%</td>
<td align="right">70,764,372</td>
<td align="right">0.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,405,116</td>
<td align="right">2.0%</td>
<td align="right">3,405,116</td>
<td align="right">2.1%</td>
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
<td align="right">353,083</td>
<td align="right">69,904,835</td>
<td align="right">8,973,122,872</td>
<td align="right">727,424,721</td>
<td align="right">718,903,523</td>
<td align="right">339,467</td>
<td align="right">31,379,035</td>
<td align="right">8,412,505,153</td>
<td align="right">714,457,546</td>
<td align="right">665,987,112</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,677,454,908</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,677,441,480</td>
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">225</td>
<td align="right">0.1%</td>
<td align="right">257.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">202,136</td>
<td align="right">50.7%</td>
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
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,947</td>
<td align="right">0.5%</td>
<td align="right">749</td>
<td align="right">0.2%</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">122,057</td>
<td align="right">30.6%</td>
<td align="right">158,899</td>
<td align="right">48.2%</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">261</td>
<td align="right">1.0%</td>
<td align="right">321</td>
<td align="right">1.3%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">398,393</td>
<td align="right"></td>
<td align="right">329,340</td>
<td align="right"></td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">219,590,687,082</td>
<td align="right">6,340.0%</td>
<td align="right">245,381,563,892</td>
<td align="right">6,490.8%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">431</td>
<td align="right">0.1%</td>
<td align="right">475</td>
<td align="right">0.1%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,463,571,032</td>
<td align="right"></td>
<td align="right">3,780,425,445</td>
<td align="right"></td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">47,117</td>
<td align="right">11.8%</td>
<td align="right">50,977</td>
<td align="right">15.5%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">27,041</td>
<td align="right">6.8%</td>
<td align="right">25,400</td>
<td align="right">7.7%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,676</td>
<td align="right">0.4%</td>
<td align="right">1,684</td>
<td align="right">0.5%</td>
<td align="right">0.5%</td>
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
<td align="right">27,041</td>
<td align="right"></td>
<td align="right">25,400</td>
<td align="right"></td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">22,153</td>
<td align="right">81.9%</td>
<td align="right">21,990</td>
<td align="right">86.6%</td>
<td align="right">-0.7%</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">18,313,216</td>
<td align="right">6.7%</td>
<td align="right">1,007,616</td>
<td align="right">0.3%</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">220,147,934</td>
<td align="right">80.9%</td>
<td align="right">266,925,869</td>
<td align="right">83.6%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">272,183,296</td>
<td align="right"></td>
<td align="right">319,455,232</td>
<td align="right"></td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">5,769,648</td>
<td align="right">2.1%</td>
<td align="right">6,645,424</td>
<td align="right">2.1%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">46,265,714</td>
<td align="right">17.0%</td>
<td align="right">45,883,939</td>
<td align="right">14.4%</td>
<td align="right">-0.8%</td>
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
<td align="left">5,562</td>
<td align="right">25.1%</td>
<td align="left">4,805</td>
<td align="right">21.9%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">7,019</td>
<td align="right">31.7%</td>
<td align="left">6,149</td>
<td align="right">28.0%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">6,280</td>
<td align="right">28.3%</td>
<td align="left">6,203</td>
<td align="right">28.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,247</td>
<td align="right">10.1%</td>
<td align="left">2,991</td>
<td align="right">13.6%</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">965</td>
<td align="right">4.4%</td>
<td align="left">1,619</td>
<td align="right">7.4%</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">80</td>
<td align="right">0.4%</td>
<td align="left">223</td>
<td align="right">1.0%</td>
<td align="right">178.8%</td>
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
<td align="right">1,298</td>
<td align="right">4.8%</td>
<td align="right">1,385</td>
<td align="right">5.5%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">896</td>
<td align="right">3.3%</td>
<td align="right">966</td>
<td align="right">3.8%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,320</td>
<td align="right">16.0%</td>
<td align="right">3,341</td>
<td align="right">13.2%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,192</td>
<td align="right">30.3%</td>
<td align="right">6,409</td>
<td align="right">25.2%</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">5,224</td>
<td align="right">19.3%</td>
<td align="right">5,833</td>
<td align="right">23.0%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,168</td>
<td align="right">19.1%</td>
<td align="right">3,444</td>
<td align="right">13.6%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,676</td>
<td align="right">6.2%</td>
<td align="right">3,449</td>
<td align="right">13.6%</td>
<td align="right">105.8%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">267</td>
<td align="right">1.0%</td>
<td align="right">573</td>
<td align="right">2.3%</td>
<td align="right">114.6%</td>
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
<td align="right">731</td>
<td align="right">2.7%</td>
<td align="right">881</td>
<td align="right">3.5%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">891</td>
<td align="right">3.3%</td>
<td align="right">697</td>
<td align="right">2.7%</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,650</td>
<td align="right">9.8%</td>
<td align="right">2,287</td>
<td align="right">9.0%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,380</td>
<td align="right">27.3%</td>
<td align="right">5,948</td>
<td align="right">23.4%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">6,181</td>
<td align="right">22.9%</td>
<td align="right">5,866</td>
<td align="right">23.1%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,463</td>
<td align="right">9.1%</td>
<td align="right">3,627</td>
<td align="right">14.3%</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,675</td>
<td align="right">6.2%</td>
<td align="right">2,217</td>
<td align="right">8.7%</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">182</td>
<td align="right">0.7%</td>
<td align="right">467</td>
<td align="right">1.8%</td>
<td align="right">156.6%</td>
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
<td align="left">_MAKE_CELL</td>
<td align="right">144,386</td>
<td align="right">38,152,529</td>
<td align="right">26,324.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">117,983</td>
<td align="right">19,196,663</td>
<td align="right">16,170.7%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">3,294,419</td>
<td align="right">12,132.4%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">179,903</td>
<td align="right">9,744,249</td>
<td align="right">5,316.4%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">677,888</td>
<td align="right">8,362,243</td>
<td align="right">1,133.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">6,713,427</td>
<td align="right">64,799,296</td>
<td align="right">865.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">5,718,540</td>
<td align="right">37,034,140</td>
<td align="right">547.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">39,279,673</td>
<td align="right">163,826,653</td>
<td align="right">317.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">7,991,793</td>
<td align="right">31,046,819</td>
<td align="right">288.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">39,831,068</td>
<td align="right">123,882,689</td>
<td align="right">211.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">7,783,149</td>
<td align="right">23,717,976</td>
<td align="right">204.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">29,719,286</td>
<td align="right">90,469,692</td>
<td align="right">204.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,583,956</td>
<td align="right">16,794,706</td>
<td align="right">200.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">7,953,793</td>
<td align="right">23,045,110</td>
<td align="right">189.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">101,740,528</td>
<td align="right">249,135,156</td>
<td align="right">144.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">101,585,388</td>
<td align="right">245,969,326</td>
<td align="right">142.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">101,585,388</td>
<td align="right">245,969,326</td>
<td align="right">142.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,548,091</td>
<td align="right">29,522,389</td>
<td align="right">135.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,548,091</td>
<td align="right">29,522,389</td>
<td align="right">135.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">27,042,203</td>
<td align="right">61,528,748</td>
<td align="right">127.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">40,460,443</td>
<td align="right">89,981,637</td>
<td align="right">122.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,678,400</td>
<td align="right">5,945,887</td>
<td align="right">122.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">433,020,859</td>
<td align="right">953,425,576</td>
<td align="right">120.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">83,399,783</td>
<td align="right">179,275,741</td>
<td align="right">115.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">34,521,547</td>
<td align="right">74,007,761</td>
<td align="right">114.4%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,975,980</td>
<td align="right">5,433,580</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,975,980</td>
<td align="right">5,433,580</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,635,678</td>
<td align="right">8,441,303</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">30,021,049</td>
<td align="right">50,505,415</td>
<td align="right">68.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">424,614,758</td>
<td align="right">707,249,930</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">609,257,681</td>
<td align="right">966,762,954</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">706,244,570</td>
<td align="right">1,083,421,176</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right">5,266,500</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,983,993</td>
<td align="right">2,930,313</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">796,826,107</td>
<td align="right">1,163,963,976</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">796,826,107</td>
<td align="right">1,163,963,976</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">197,253,092</td>
<td align="right">286,746,491</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">784,278,016</td>
<td align="right">1,134,441,587</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">404,684,245</td>
<td align="right">581,862,890</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">294,820,200</td>
<td align="right">422,416,330</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,940,440</td>
<td align="right">68,254,020</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">3,709,046</td>
<td align="right">5,152,486</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,165,756,879</td>
<td align="right">1,613,055,933</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">2,706,669,192</td>
<td align="right">3,684,855,825</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">462,143,821</td>
<td align="right">619,927,984</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">50,000,356</td>
<td align="right">66,403,758</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">147,055,567</td>
<td align="right">194,414,819</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,329,303,582</td>
<td align="right">1,754,317,919</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,329,483,214</td>
<td align="right">1,754,497,152</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">169,970,805</td>
<td align="right">223,977,751</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,731,038,613</td>
<td align="right">2,250,462,040</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">489,688,795</td>
<td align="right">636,541,142</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">489,802,035</td>
<td align="right">636,541,142</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">165,936,688</td>
<td align="right">214,770,607</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">608,464,989</td>
<td align="right">785,119,613</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,560</td>
<td align="right">60,989,708</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,452,835,418</td>
<td align="right">4,386,829,803</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">8,323,320</td>
<td align="right">10,548,460</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">433,516,421</td>
<td align="right">545,338,162</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">75,010,522</td>
<td align="right">94,249,812</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">78,980,963</td>
<td align="right">99,091,264</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">975,741,736</td>
<td align="right">1,218,390,288</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">118,803,098</td>
<td align="right">148,132,003</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">20,041,856</td>
<td align="right">24,890,388</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">49,132,694</td>
<td align="right">60,695,375</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,113,750,711</td>
<td align="right">1,368,989,332</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">6,700,112</td>
<td align="right">8,209,592</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">1,463,129,475</td>
<td align="right">1,789,813,920</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">57,567,413</td>
<td align="right">70,051,013</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">884,793,676</td>
<td align="right">1,061,272,058</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">52,258,341</td>
<td align="right">42,180,620</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">153,039,303</td>
<td align="right">182,490,461</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">12,783,849</td>
<td align="right">15,224,569</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,324,005</td>
<td align="right">3,956,139</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">440,121,418</td>
<td align="right">523,587,364</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">156,877,166</td>
<td align="right">186,059,964</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">983,244,017</td>
<td align="right">1,155,830,812</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">262,313,214</td>
<td align="right">308,162,928</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">41,116,362</td>
<td align="right">48,098,726</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,989,390,753</td>
<td align="right">2,318,956,560</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">694,097,677</td>
<td align="right">808,640,865</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">98,098,601</td>
<td align="right">113,471,830</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">731,839,989</td>
<td align="right">845,268,856</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">322,789,526</td>
<td align="right">372,529,351</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">38,306,073</td>
<td align="right">44,131,480</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,227,614,467</td>
<td align="right">1,407,711,933</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,556,350,669</td>
<td align="right">2,928,704,890</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,257,371,505</td>
<td align="right">2,562,242,772</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">642,331,269</td>
<td align="right">725,416,136</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">591,130,589</td>
<td align="right">665,960,408</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,721,384,970</td>
<td align="right">4,191,710,870</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">145,755,849</td>
<td align="right">163,741,893</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">170,042,198</td>
<td align="right">149,686,948</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">5,303,275</td>
<td align="right">5,929,555</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">5,303,275</td>
<td align="right">5,929,555</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,909,803,319</td>
<td align="right">2,131,948,692</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">90,282,923</td>
<td align="right">100,392,282</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,345,868,714</td>
<td align="right">1,494,758,315</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">358,521,878</td>
<td align="right">397,929,117</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,266,418,901</td>
<td align="right">1,403,691,699</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,061,195,789</td>
<td align="right">1,174,915,539</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">39,440,814,914</td>
<td align="right">43,616,369,817</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">34,996,829,071</td>
<td align="right">38,644,852,727</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,141,584,372</td>
<td align="right">2,358,378,922</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">148,987,967</td>
<td align="right">164,004,457</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">5,560,502</td>
<td align="right">5,007,925</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">53,395,255</td>
<td align="right">58,562,655</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,105,399,123</td>
<td align="right">9,962,989,195</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">53,395,255</td>
<td align="right">58,422,275</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,428,874,103</td>
<td align="right">3,745,600,731</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,463,571,032</td>
<td align="right">3,780,425,445</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">310,730,342</td>
<td align="right">337,165,925</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">161,981,135</td>
<td align="right">174,707,728</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,223,810,183</td>
<td align="right">1,319,888,940</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">121,884,246</td>
<td align="right">130,874,969</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,737,325,890</td>
<td align="right">2,930,479,748</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">419,919,993</td>
<td align="right">448,011,999</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,808,674,834</td>
<td align="right">1,927,617,674</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,770,000</td>
<td align="right">78,472,524</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">90,810,039</td>
<td align="right">96,442,032</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">55,838,776</td>
<td align="right">59,145,595</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,793,678,934</td>
<td align="right">2,958,552,094</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">469,041,941</td>
<td align="right">496,638,582</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">568,620,157</td>
<td align="right">601,598,241</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">383,450,243</td>
<td align="right">405,096,829</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,534,526</td>
<td align="right">45,974,226</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,409,132</td>
<td align="right">1,331,496</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">5,852,494,984</td>
<td align="right">6,166,596,509</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">208,827,224</td>
<td align="right">219,566,547</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">30,896,592</td>
<td align="right">32,408,278</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">30,896,592</td>
<td align="right">32,408,278</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">121,790,865</td>
<td align="right">127,667,815</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">3,873,776,427</td>
<td align="right">4,059,104,835</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">30,495,173</td>
<td align="right">31,893,655</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">585,073,171</td>
<td align="right">611,424,984</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,199,132,886</td>
<td align="right">1,251,175,791</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">602,897,187</td>
<td align="right">628,815,532</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,992,273,267</td>
<td align="right">2,076,027,768</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,754,931,293</td>
<td align="right">1,825,943,428</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,782,792,530</td>
<td align="right">1,852,101,387</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">96,571,866</td>
<td align="right">100,206,178</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,025,554</td>
<td align="right">41,465,798</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">2,176,916</td>
<td align="right">2,099,280</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">358,301,634</td>
<td align="right">370,724,898</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,319,706,163</td>
<td align="right">1,275,625,765</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">37,104,317</td>
<td align="right">38,335,197</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,315,657,439</td>
<td align="right">1,275,283,721</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">192,648,203</td>
<td align="right">197,974,549</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,438,787,850</td>
<td align="right">7,635,901,553</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">65,207,763</td>
<td align="right">63,572,483</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">921,766,149</td>
<td align="right">944,858,902</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">469,143,550</td>
<td align="right">480,508,482</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">45,813,318</td>
<td align="right">46,895,733</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">577,035,507</td>
<td align="right">590,533,122</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,863,923,843</td>
<td align="right">2,929,486,016</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">768,857,570</td>
<td align="right">786,332,767</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">263,905,177</td>
<td align="right">269,814,574</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,222,983,427</td>
<td align="right">1,197,221,398</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">2,504,834,956</td>
<td align="right">2,547,131,604</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">211,745,927</td>
<td align="right">208,310,152</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,031,907,323</td>
<td align="right">3,080,767,766</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,217,714,843</td>
<td align="right">1,236,281,918</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">131,031,777</td>
<td align="right">132,998,837</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">416,282,834</td>
<td align="right">422,354,366</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">601,196,603</td>
<td align="right">609,325,028</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,278,515,434</td>
<td align="right">2,306,868,099</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">160,398,151</td>
<td align="right">162,350,526</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">143,590,077</td>
<td align="right">145,315,475</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">49,249,153</td>
<td align="right">49,836,403</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">81,255,858</td>
<td align="right">80,292,622</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">247,851,902</td>
<td align="right">250,709,171</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,148,998,666</td>
<td align="right">1,160,898,699</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">452,206,029</td>
<td align="right">456,879,516</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">57,605,753</td>
<td align="right">57,027,873</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">229,826</td>
<td align="right">232,052</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">451,080,786</td>
<td align="right">455,439,798</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,065,964,786</td>
<td align="right">1,076,220,797</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">923,250,740</td>
<td align="right">932,039,341</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">424,469,708</td>
<td align="right">420,453,185</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">923,235,880</td>
<td align="right">930,346,759</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">196,728,502</td>
<td align="right">198,053,468</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,487</td>
<td align="right">70,804,078</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,487</td>
<td align="right">70,804,078</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,691,619</td>
<td align="right">118,393,819</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">5,839,840,845</td>
<td align="right">5,871,201,199</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,283,792,869</td>
<td align="right">1,276,912,543</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">103,178,820</td>
<td align="right">103,567,160</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">34,676,876</td>
<td align="right">34,804,661</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">341,036,296</td>
<td align="right">342,050,541</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">423,331,251</td>
<td align="right">424,537,557</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">444,620,696</td>
<td align="right">445,799,660</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">444,620,696</td>
<td align="right">445,799,660</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,388,923,952</td>
<td align="right">2,386,171,064</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">4,208,676</td>
<td align="right">4,212,015</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">24,643,554</td>
<td align="right">24,660,923</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">532,683,636</td>
<td align="right">533,031,028</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">84,643,314</td>
<td align="right">84,660,683</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,545,507</td>
<td align="right">1,545,266</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">445,747,579</td>
<td align="right">445,758,207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">445,747,579</td>
<td align="right">445,758,207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,593,190</td>
<td align="right">46,594,283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">48,050,990</td>
<td align="right">48,052,099</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,433,550</td>
<td align="right">1,433,532</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,253,140</td>
<td align="right">3,253,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,492,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">59,999,760</td>
<td align="right">59,999,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,079</td>
<td align="right">47,071,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">3,106,080</td>
<td align="right">3,106,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,034,740</td>
<td align="right">3,034,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">918,506</td>
<td align="right">918,506</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">356,340</td>
<td align="right">356,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">27,762</td>
<td align="right">27,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">20,053</td>
<td align="right">20,053</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLER_INSTR_PTR</td>
<td align="right"></td>
<td align="right">532,969,894</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLER_FUNCTION_VERSION</td>
<td align="right"></td>
<td align="right">398,191,254</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">50,837,738</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right"></td>
<td align="right">14,763,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_TUPLE_1</td>
<td align="right"></td>
<td align="right">3,267,487</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">919,526</td>
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
<td align="left">CALL</td>
<td align="right">1,810</td>
<td align="right">2,593</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">23,367</td>
<td align="right">25,790</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right">23,001</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">660</td>
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
<td align="right">101</td>
<td align="right">161</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">101</td>
<td align="right">161</td>
<td align="right">59.4%</td>
</tr>
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
<td align="right">2,420</td>
<td align="right">2,420</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-05-29
