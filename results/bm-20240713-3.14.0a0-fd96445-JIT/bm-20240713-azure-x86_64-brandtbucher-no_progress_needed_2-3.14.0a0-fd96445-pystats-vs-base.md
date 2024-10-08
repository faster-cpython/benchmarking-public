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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">485,800</td>
<td align="right">5,720,620</td>
<td align="right">1,077.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">219,468</td>
<td align="right">701,657</td>
<td align="right">219.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">54,270,955</td>
<td align="right">168,899,893</td>
<td align="right">211.2%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">4,628,872</td>
<td align="right">8,625,004</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">909,566,726</td>
<td align="right">1,540,156,940</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">20,333,898</td>
<td align="right">31,606,012</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">378,234,226</td>
<td align="right">578,649,636</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">108,591,623</td>
<td align="right">165,971,726</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,806,492</td>
<td align="right">107,214,875</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68,002,425</td>
<td align="right">98,739,801</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">42,433,744</td>
<td align="right">59,880,788</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">211,271,082</td>
<td align="right">291,690,434</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,815,465</td>
<td align="right">55,054,689</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">146,465,249</td>
<td align="right">99,271,804</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">202,175,486</td>
<td align="right">266,471,405</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">679,740,125</td>
<td align="right">892,610,505</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">404,538,568</td>
<td align="right">516,493,985</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,874,397</td>
<td align="right">2,913,299</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">46,620</td>
<td align="right">57,780</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">791,279,079</td>
<td align="right">979,131,906</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,370</td>
<td align="right">231,938,391</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">385,034,485</td>
<td align="right">468,031,601</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">194,483,450</td>
<td align="right">232,055,468</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">222,836</td>
<td align="right">185,185</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,563,364,277</td>
<td align="right">1,801,903,785</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,167,863</td>
<td align="right">267,045,147</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,297,524</td>
<td align="right">248,769,479</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,379,981,938</td>
<td align="right">3,733,514,021</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,450,734,258</td>
<td align="right">2,794,273,434</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,016,823,533</td>
<td align="right">1,157,988,691</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">386,366,035</td>
<td align="right">439,588,076</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">332,019,365</td>
<td align="right">373,425,604</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">140,536,584</td>
<td align="right">157,926,163</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">276,486,064</td>
<td align="right">310,229,216</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">366,806,199</td>
<td align="right">410,924,229</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">283,353,267</td>
<td align="right">316,398,474</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,580,514,118</td>
<td align="right">24,049,593,882</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">35,531,143</td>
<td align="right">39,578,137</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,489,307,295</td>
<td align="right">6,060,690,686</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,808,501</td>
<td align="right">35,017,682</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">23,966,865</td>
<td align="right">26,301,647</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">666,613,584</td>
<td align="right">729,480,038</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">739,557,058</td>
<td align="right">804,550,643</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,099,631,443</td>
<td align="right">4,453,893,142</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">295,222,464</td>
<td align="right">318,119,264</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,221,206,810</td>
<td align="right">6,680,619,968</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">87,803,224</td>
<td align="right">94,010,557</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,110,576,413</td>
<td align="right">1,187,014,274</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,580,110</td>
<td align="right">108,160,902</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">298,257,057</td>
<td align="right">316,024,094</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,819,086,892</td>
<td align="right">2,966,499,827</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,664,658,668</td>
<td align="right">5,958,557,397</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,644,661,655</td>
<td align="right">2,509,300,739</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,850,391</td>
<td align="right">56,537,099</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,131,545,491</td>
<td align="right">1,186,819,825</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">118,777,231</td>
<td align="right">124,477,462</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">557,041,358</td>
<td align="right">581,781,530</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">386,026,172</td>
<td align="right">402,757,759</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">21,175,493</td>
<td align="right">22,061,423</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,255,226,069</td>
<td align="right">1,304,485,890</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">942,147,494</td>
<td align="right">978,789,383</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">328,729,288</td>
<td align="right">340,169,882</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">231,221,819</td>
<td align="right">223,620,229</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">804,949,290</td>
<td align="right">831,045,696</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">421,589,954</td>
<td align="right">434,800,164</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">773,918,108</td>
<td align="right">796,652,344</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">195,651,646</td>
<td align="right">201,291,483</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,411,795,175</td>
<td align="right">1,371,995,480</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">79,279,731</td>
<td align="right">81,507,954</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">166,866,129</td>
<td align="right">171,470,489</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">162,539,697</td>
<td align="right">166,792,215</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">272,719,008</td>
<td align="right">279,829,151</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">114,868,113</td>
<td align="right">117,775,372</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,553,696</td>
<td align="right">48,638,195</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,221,949,971</td>
<td align="right">4,315,969,344</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,399,952,069</td>
<td align="right">2,349,955,819</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">215,047,513</td>
<td align="right">219,314,271</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,297,198,388</td>
<td align="right">3,362,165,451</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,591,861</td>
<td align="right">126,978,218</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">677,179,245</td>
<td align="right">690,084,030</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,877,652</td>
<td align="right">10,064,556</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">409,215,349</td>
<td align="right">416,703,757</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">318,041,043</td>
<td align="right">323,749,741</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">349,280,434</td>
<td align="right">343,045,274</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,388,590</td>
<td align="right">10,560,080</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,284,882</td>
<td align="right">93,771,063</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,290,129,139</td>
<td align="right">1,307,233,102</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">199,228,081</td>
<td align="right">201,853,876</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">639,895,780</td>
<td align="right">648,091,261</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">453,756,955</td>
<td align="right">459,201,685</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">56,521,715</td>
<td align="right">57,192,691</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">59,677,580</td>
<td align="right">60,378,415</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,101,108</td>
<td align="right">48,633,015</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">30,785,345</td>
<td align="right">30,446,324</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,872,175,209</td>
<td align="right">1,851,927,058</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">205,889,302</td>
<td align="right">208,042,036</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">137,986,057</td>
<td align="right">136,587,479</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,461,660</td>
<td align="right">7,535,860</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,175,821</td>
<td align="right">82,349,006</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,569,390</td>
<td align="right">160,142,020</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">66,953,717</td>
<td align="right">67,617,240</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">100,343,428</td>
<td align="right">101,287,069</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">486,461,360</td>
<td align="right">490,790,797</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">173,188,542</td>
<td align="right">174,419,167</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">828,544,752</td>
<td align="right">834,306,895</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,763,224</td>
<td align="right">67,165,692</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,105,988,808</td>
<td align="right">4,130,703,216</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,247,604</td>
<td align="right">62,620,384</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">901,623,105</td>
<td align="right">906,904,790</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,994,682,805</td>
<td align="right">5,961,876,263</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">481,492,919</td>
<td align="right">483,946,998</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">81,682,686</td>
<td align="right">82,094,104</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">108,507,080</td>
<td align="right">108,999,330</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">198,605,843</td>
<td align="right">199,464,125</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,612,192</td>
<td align="right">46,783,912</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,413,070</td>
<td align="right">4,428,150</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,366,385</td>
<td align="right">1,050,558,243</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">59,137,415</td>
<td align="right">58,972,193</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,525,894,943</td>
<td align="right">3,534,187,439</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,358,831</td>
<td align="right">8,376,312</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">142,537,682</td>
<td align="right">142,807,762</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,913,460</td>
<td align="right">150,193,103</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,714,481</td>
<td align="right">71,824,981</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">135,755,200</td>
<td align="right">135,939,640</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,473,436</td>
<td align="right">17,457,402</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">76,350,505</td>
<td align="right">76,416,937</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">431,589,715</td>
<td align="right">431,953,827</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,376,440</td>
<td align="right">2,374,758</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,882,803</td>
<td align="right">81,833,466</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,866,838</td>
<td align="right">403,094,983</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">49,209,196</td>
<td align="right">49,233,183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,607</td>
<td align="right">1,874,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,641,404</td>
<td align="right">3,640,603</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">485,135,654</td>
<td align="right">485,226,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,301,355</td>
<td align="right">274,339,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,885</td>
<td align="right">14,887</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,912,060</td>
<td align="right">146,894,168</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,371,141,239</td>
<td align="right">1,371,007,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,451,690</td>
<td align="right">82,457,437</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,961,863</td>
<td align="right">10,961,276</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,152,899</td>
<td align="right">21,152,258</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,160,659</td>
<td align="right">21,160,018</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,641,548</td>
<td align="right">225,648,078</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">228,048,203</td>
<td align="right">228,041,831</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,658,065</td>
<td align="right">9,658,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,694,461</td>
<td align="right">20,694,054</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,236,148</td>
<td align="right">9,236,325</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,420</td>
<td align="right">173,423</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,142,187</td>
<td align="right">91,143,732</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,739</td>
<td align="right">687,748</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,808,204</td>
<td align="right">1,808,188</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,344,783</td>
<td align="right">20,344,942</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,603,447,253</td>
<td align="right">1,603,441,096</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,950,730</td>
<td align="right">5,950,736</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,907,353</td>
<td align="right">555,906,833</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,319,328</td>
<td align="right">173,319,338</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,338,342</td>
<td align="right">233,338,353</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,024,162</td>
<td align="right">402,024,177</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,220,562</td>
<td align="right">786,220,587</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,165,100</td>
<td align="right">92,165,102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,446,940</td>
<td align="right">94,446,942</td>
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
<td align="right">12,102,480</td>
<td align="right">12,102,480</td>
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
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,240</td>
<td align="right">3,465,240</td>
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
<td align="right">657,740</td>
<td align="right">657,740</td>
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
<td align="right">436,996,138</td>
<td align="right">4.4%</td>
<td align="right">444,508,096</td>
<td align="right">4.5%</td>
<td align="right">1.7%</td>
</tr>
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
<td align="right">29,530,960</td>
<td align="right">0.3%</td>
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
<td align="right">9,428,336,550</td>
<td align="right">95.6%</td>
<td align="right">9,433,644,581</td>
<td align="right">95.5%</td>
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
<td align="right">1,122,507</td>
<td align="right">65.3%</td>
<td align="right">1,128,375</td>
<td align="right">65.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">597,624</td>
<td align="right">34.7%</td>
<td align="right">598,246</td>
<td align="right">34.6%</td>
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
<td align="left">lshift</td>
<td align="right">5,026</td>
<td align="right">0.4%</td>
<td align="right">5,769</td>
<td align="right">0.5%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,318</td>
<td align="right">4.3%</td>
<td align="right">50,767</td>
<td align="right">4.5%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">13,626</td>
<td align="right">1.2%</td>
<td align="right">14,308</td>
<td align="right">1.3%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">22,628</td>
<td align="right">2.0%</td>
<td align="right">21,711</td>
<td align="right">1.9%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,266</td>
<td align="right">2.8%</td>
<td align="right">32,296</td>
<td align="right">2.9%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,884</td>
<td align="right">0.8%</td>
<td align="right">9,085</td>
<td align="right">0.8%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">0.9%</td>
<td align="right">10,800</td>
<td align="right">1.0%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,720</td>
<td align="right">0.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,720</td>
<td align="right">0.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,407</td>
<td align="right">7.3%</td>
<td align="right">83,628</td>
<td align="right">7.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,610</td>
<td align="right">0.8%</td>
<td align="right">8,687</td>
<td align="right">0.8%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,504</td>
<td align="right">0.9%</td>
<td align="right">10,425</td>
<td align="right">0.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">48,680</td>
<td align="right">4.3%</td>
<td align="right">48,879</td>
<td align="right">4.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,548</td>
<td align="right">0.5%</td>
<td align="right">5,555</td>
<td align="right">0.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,915</td>
<td align="right">0.2%</td>
<td align="right">1,916</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,385</td>
<td align="right">2.9%</td>
<td align="right">32,374</td>
<td align="right">2.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">4,725</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,606</td>
<td align="right">69.6%</td>
<td align="right">781,610</td>
<td align="right">69.3%</td>
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
<td align="right">743,945,445</td>
<td align="right">10.8%</td>
<td align="right">808,924,623</td>
<td align="right">11.4%</td>
<td align="right">8.7%</td>
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
<td align="right">6,264,446,898</td>
<td align="right">88.6%</td>
<td align="right">1.9%</td>
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
<td align="right">4,813,092</td>
<td align="right">0.1%</td>
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
<td align="right">240,169</td>
<td align="right">56.9%</td>
<td align="right">257,505</td>
<td align="right">58.6%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,561</td>
<td align="right">43.1%</td>
<td align="right">181,607</td>
<td align="right">41.4%</td>
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
<td align="right">32,280</td>
<td align="right">12.5%</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">110,406</td>
<td align="right">46.0%</td>
<td align="right">111,340</td>
<td align="right">43.2%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">125</td>
<td align="right">0.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.2%</td>
<td align="right">5,360</td>
<td align="right">2.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">55,960</td>
<td align="right">23.3%</td>
<td align="right">56,160</td>
<td align="right">21.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,499</td>
<td align="right">12.7%</td>
<td align="right">30,600</td>
<td align="right">11.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,500</td>
<td align="right">8.1%</td>
<td align="right">19,500</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">880</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
<td align="right">0.0%</td>
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
<td align="right">26,760</td>
<td align="right">0.0%</td>
<td align="right">-7.3%</td>
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
<td align="right">183,112,649</td>
<td align="right">1.3%</td>
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
<td align="right">662,503,918</td>
<td align="right">4.6%</td>
<td align="right">664,195,541</td>
<td align="right">4.6%</td>
<td align="right">0.3%</td>
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
<td align="right">13,661,250,059</td>
<td align="right">95.3%</td>
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
<td align="right">3,947,091</td>
<td align="right">96.0%</td>
<td align="right">3,977,846</td>
<td align="right">96.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">165,422</td>
<td align="right">4.0%</td>
<td align="right">165,446</td>
<td align="right">4.0%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">155,922</td>
<td align="right">94.3%</td>
<td align="right">155,946</td>
<td align="right">94.3%</td>
<td align="right">0.0%</td>
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
<td align="right">1,333,779</td>
<td align="right">0.0%</td>
<td align="right">24.7%</td>
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
<td align="right">102,378,072</td>
<td align="right">1.6%</td>
<td align="right">1.2%</td>
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
<td align="right">6,123,275,737</td>
<td align="right">98.4%</td>
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
<td align="right">149,613</td>
<td align="right">66.3%</td>
<td align="right">161,581</td>
<td align="right">66.6%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">76,147</td>
<td align="right">33.7%</td>
<td align="right">81,195</td>
<td align="right">33.4%</td>
<td align="right">6.6%</td>
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
<td align="right">27,060</td>
<td align="right">18.1%</td>
<td align="right">33,241</td>
<td align="right">20.6%</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">42,443</td>
<td align="right">28.4%</td>
<td align="right">47,297</td>
<td align="right">29.3%</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,424</td>
<td align="right">1.0%</td>
<td align="right">1,539</td>
<td align="right">1.0%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,703</td>
<td align="right">11.2%</td>
<td align="right">17,331</td>
<td align="right">10.7%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,000</td>
<td align="right">12.7%</td>
<td align="right">19,260</td>
<td align="right">11.9%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,620</td>
<td align="right">1.1%</td>
<td align="right">1,640</td>
<td align="right">1.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,375</td>
<td align="right">9.6%</td>
<td align="right">14,283</td>
<td align="right">8.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,188</td>
<td align="right">8.1%</td>
<td align="right">12,190</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">10,680</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,580</td>
<td align="right">1.7%</td>
<td align="right">2,580</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.4%</td>
<td align="right">580</td>
<td align="right">0.4%</td>
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
<td align="right">210,412,073</td>
<td align="right">7.8%</td>
<td align="right">1.0%</td>
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
<td align="right">2,489,616,383</td>
<td align="right">92.2%</td>
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
<td align="right">2,546,240</td>
<td align="right">0.1%</td>
<td align="right">2,546,240</td>
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
<td align="right">113,728</td>
<td align="right">65.0%</td>
<td align="right">115,083</td>
<td align="right">65.3%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,120</td>
<td align="right">35.0%</td>
<td align="right">61,120</td>
<td align="right">34.7%</td>
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
<td align="right">13,940</td>
<td align="right">12.3%</td>
<td align="right">14,320</td>
<td align="right">12.4%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">56,540</td>
<td align="right">49.7%</td>
<td align="right">57,320</td>
<td align="right">49.8%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,730</td>
<td align="right">13.8%</td>
<td align="right">15,806</td>
<td align="right">13.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,518</td>
<td align="right">24.2%</td>
<td align="right">27,637</td>
<td align="right">24.0%</td>
<td align="right">0.4%</td>
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
<td align="right">2,588,403</td>
<td align="right">0.3%</td>
<td align="right">6,684,661</td>
<td align="right">0.6%</td>
<td align="right">158.3%</td>
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
<td align="right">564,764,035</td>
<td align="right">53.5%</td>
<td align="right">3.2%</td>
</tr>
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
<td align="right">490,258,122</td>
<td align="right">46.5%</td>
<td align="right">1.3%</td>
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
<td align="right">96,568</td>
<td align="right">32.9%</td>
<td align="right">173,845</td>
<td align="right">46.5%</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">196,985</td>
<td align="right">67.1%</td>
<td align="right">199,692</td>
<td align="right">53.5%</td>
<td align="right">1.4%</td>
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
<td align="left">seq iter</td>
<td align="right">3,840</td>
<td align="right">1.9%</td>
<td align="right">4,240</td>
<td align="right">2.1%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,252</td>
<td align="right">5.2%</td>
<td align="right">11,022</td>
<td align="right">5.5%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">37,173</td>
<td align="right">18.9%</td>
<td align="right">38,505</td>
<td align="right">19.3%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,285</td>
<td align="right">5.7%</td>
<td align="right">11,485</td>
<td align="right">5.8%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">615</td>
<td align="right">0.3%</td>
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,220</td>
<td align="right">2.1%</td>
<td align="right">4,200</td>
<td align="right">2.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,100</td>
<td align="right">2.6%</td>
<td align="right">5,120</td>
<td align="right">2.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,960</td>
<td align="right">53.3%</td>
<td align="right">104,960</td>
<td align="right">52.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,480</td>
<td align="right">3.3%</td>
<td align="right">6,480</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,300</td>
<td align="right">3.2%</td>
<td align="right">6,300</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,060</td>
<td align="right">2.1%</td>
<td align="right">4,060</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,720</td>
<td align="right">0.9%</td>
<td align="right">1,720</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">1,521,315,006</td>
<td align="right">8.6%</td>
<td align="right">1,590,490,206</td>
<td align="right">8.9%</td>
<td align="right">4.5%</td>
</tr>
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
<td align="right">412,873,011</td>
<td align="right">2.3%</td>
<td align="right">-1.8%</td>
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
<td align="right">16,257,681,566</td>
<td align="right">91.0%</td>
<td align="right">1.1%</td>
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
<td align="right">263,380</td>
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
<td align="right">972,024</td>
<td align="right">10.2%</td>
<td align="right">996,660</td>
<td align="right">10.6%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,539,421</td>
<td align="right">89.8%</td>
<td align="right">8,400,419</td>
<td align="right">89.4%</td>
<td align="right">-1.6%</td>
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
<td align="left">class method obj</td>
<td align="right">14,360</td>
<td align="right">1.5%</td>
<td align="right">17,660</td>
<td align="right">1.8%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">164,774</td>
<td align="right">17.0%</td>
<td align="right">175,866</td>
<td align="right">17.6%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">75,343</td>
<td align="right">7.8%</td>
<td align="right">77,786</td>
<td align="right">7.8%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">102,064</td>
<td align="right">10.5%</td>
<td align="right">103,910</td>
<td align="right">10.4%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">263,066</td>
<td align="right">27.1%</td>
<td align="right">267,299</td>
<td align="right">26.8%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,840</td>
<td align="right">0.3%</td>
<td align="right">2,880</td>
<td align="right">0.3%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,300</td>
<td align="right">1.6%</td>
<td align="right">15,440</td>
<td align="right">1.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">156,280</td>
<td align="right">16.1%</td>
<td align="right">157,521</td>
<td align="right">15.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,638</td>
<td align="right">9.0%</td>
<td align="right">87,937</td>
<td align="right">8.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,570</td>
<td align="right">0.6%</td>
<td align="right">5,572</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,880</td>
<td align="right">2.8%</td>
<td align="right">26,880</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,340</td>
<td align="right">2.1%</td>
<td align="right">20,340</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,749</td>
<td align="right">1.8%</td>
<td align="right">17,749</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.3%</td>
<td align="right">12,240</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,400</td>
<td align="right">0.6%</td>
<td align="right">5,400</td>
<td align="right">0.5%</td>
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
<td align="left">out of versions</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">340</td>
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
<td align="right">6,304,142,522</td>
<td align="right">99.7%</td>
<td align="right">7.8%</td>
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
<td align="right">436,816</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
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
<td align="right">20,319,032</td>
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
<td align="right">462,726</td>
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
<td align="right">83,720,927</td>
<td align="right">100.0%</td>
<td align="right">83,671,574</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
</tr>
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
<td align="right">7,467</td>
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
<td align="right">173,284,918</td>
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
<td align="right">786,189,927</td>
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
<td align="right">192,780,434</td>
<td align="right">6.6%</td>
<td align="right">1.2%</td>
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
<td align="right">139,055,631</td>
<td align="right">4.7%</td>
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
<td align="right">2,724,885,653</td>
<td align="right">93.4%</td>
<td align="right">2,732,182,609</td>
<td align="right">93.3%</td>
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
<td align="left">Failure</td>
<td align="right">92,028</td>
<td align="right">3.3%</td>
<td align="right">92,970</td>
<td align="right">3.3%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,726,794</td>
<td align="right">96.7%</td>
<td align="right">2,719,326</td>
<td align="right">96.7%</td>
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
<td align="left">property</td>
<td align="right">2,860</td>
<td align="right">3.1%</td>
<td align="right">3,320</td>
<td align="right">3.6%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">32,280</td>
<td align="right">35.1%</td>
<td align="right">32,740</td>
<td align="right">35.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,760</td>
<td align="right">9.5%</td>
<td align="right">8,780</td>
<td align="right">9.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,728</td>
<td align="right">10.6%</td>
<td align="right">9,730</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,960</td>
<td align="right">15.2%</td>
<td align="right">13,960</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,480</td>
<td align="right">8.1%</td>
<td align="right">7,480</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
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
<td align="left">no dict</td>
<td align="right">4,940</td>
<td align="right">5.4%</td>
<td align="right">4,940</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,780</td>
<td align="right">5.2%</td>
<td align="right">4,780</td>
<td align="right">5.1%</td>
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
<td align="right">266,925,999</td>
<td align="right">23.3%</td>
<td align="right">15.0%</td>
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
<td align="right">877,114,995</td>
<td align="right">76.7%</td>
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
<td align="right">109,144</td>
<td align="right">89.4%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,902</td>
<td align="right">11.4%</td>
<td align="right">12,904</td>
<td align="right">10.6%</td>
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
<td align="right">6,480</td>
<td align="right">6.5%</td>
<td align="right">13,180</td>
<td align="right">12.1%</td>
<td align="right">103.4%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,340</td>
<td align="right">1.3%</td>
<td align="right">1,500</td>
<td align="right">1.4%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">39,720</td>
<td align="right">39.7%</td>
<td align="right">41,881</td>
<td align="right">38.4%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,480</td>
<td align="right">1.5%</td>
<td align="right">1,520</td>
<td align="right">1.4%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,526</td>
<td align="right">7.5%</td>
<td align="right">7,643</td>
<td align="right">7.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,420</td>
<td align="right">43.4%</td>
<td align="right">43,420</td>
<td align="right">39.8%</td>
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
<td align="right">248,285,288</td>
<td align="right">3.9%</td>
<td align="right">289,719,527</td>
<td align="right">4.5%</td>
<td align="right">16.7%</td>
</tr>
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
<td align="right">59,517,419</td>
<td align="right">0.9%</td>
<td align="right">7.4%</td>
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
<td align="right">6,151,095,140</td>
<td align="right">95.5%</td>
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
<td align="left">Failure</td>
<td align="right">356,093</td>
<td align="right">22.3%</td>
<td align="right">537,413</td>
<td align="right">29.0%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,238,312</td>
<td align="right">77.7%</td>
<td align="right">1,315,947</td>
<td align="right">71.0%</td>
<td align="right">6.3%</td>
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
<td align="right">147,245</td>
<td align="right">27.4%</td>
<td align="right">2,761.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,237</td>
<td align="right">3.7%</td>
<td align="right">19,340</td>
<td align="right">3.6%</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">135,496</td>
<td align="right">38.1%</td>
<td align="right">165,115</td>
<td align="right">30.7%</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,020</td>
<td align="right">4.2%</td>
<td align="right">17,440</td>
<td align="right">3.2%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">55,260</td>
<td align="right">15.5%</td>
<td align="right">55,829</td>
<td align="right">10.4%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,168</td>
<td align="right">22.8%</td>
<td align="right">81,651</td>
<td align="right">15.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12,779</td>
<td align="right">3.6%</td>
<td align="right">12,800</td>
<td align="right">2.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">35,068</td>
<td align="right">9.8%</td>
<td align="right">35,073</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
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
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.3%</td>
<td align="right">1,040</td>
<td align="right">0.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">194,005</td>
<td align="right">0.0%</td>
<td align="right">156,361</td>
<td align="right">0.0%</td>
<td align="right">-19.4%</td>
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
<td align="right">1,558,789,164</td>
<td align="right">100.0%</td>
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
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">3,080</td>
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
<td align="right">1,855</td>
<td align="right">5.8%</td>
<td align="right">1,836</td>
<td align="right">5.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,056</td>
<td align="right">94.2%</td>
<td align="right">30,068</td>
<td align="right">94.2%</td>
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
<td align="right">380</td>
<td align="right">20.5%</td>
<td align="right">360</td>
<td align="right">19.6%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,215</td>
<td align="right">65.5%</td>
<td align="right">1,216</td>
<td align="right">66.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.0%</td>
<td align="right">260</td>
<td align="right">14.2%</td>
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
<td align="right">11,721,029,980</td>
<td align="right">9.6%</td>
<td align="right">12,714,429,824</td>
<td align="right">9.8%</td>
<td align="right">8.5%</td>
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
<td align="right">45,522,395,051</td>
<td align="right">35.2%</td>
<td align="right">6.6%</td>
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
<td align="right">70,272,889,382</td>
<td align="right">54.3%</td>
<td align="right">4.9%</td>
</tr>
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
<td align="right">917,838,927</td>
<td align="right">0.7%</td>
<td align="right">0.3%</td>
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
<td align="right">248,285,288</td>
<td align="right">4.9%</td>
<td align="right">289,719,527</td>
<td align="right">5.5%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,057,895</td>
<td align="right">4.6%</td>
<td align="right">266,925,999</td>
<td align="right">5.1%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">743,945,445</td>
<td align="right">14.8%</td>
<td align="right">808,924,623</td>
<td align="right">15.4%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,521,315,006</td>
<td align="right">30.3%</td>
<td align="right">1,590,490,206</td>
<td align="right">30.3%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">436,996,138</td>
<td align="right">8.7%</td>
<td align="right">444,508,096</td>
<td align="right">8.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">483,787,769</td>
<td align="right">9.6%</td>
<td align="right">490,258,122</td>
<td align="right">9.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">190,480,747</td>
<td align="right">3.8%</td>
<td align="right">192,780,434</td>
<td align="right">3.7%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">208,260,694</td>
<td align="right">4.1%</td>
<td align="right">210,412,073</td>
<td align="right">4.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">662,503,918</td>
<td align="right">13.2%</td>
<td align="right">664,195,541</td>
<td align="right">12.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,908</td>
<td align="right">3.5%</td>
<td align="right">173,284,918</td>
<td align="right">3.3%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,365,670</td>
<td align="right">2.7%</td>
<td align="right">30,808,425</td>
<td align="right">3.1%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">172,481,741</td>
<td align="right">17.4%</td>
<td align="right">163,691,611</td>
<td align="right">16.4%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">58,791,367</td>
<td align="right">5.9%</td>
<td align="right">56,136,827</td>
<td align="right">5.6%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">125,829,008</td>
<td align="right">12.7%</td>
<td align="right">123,178,378</td>
<td align="right">12.4%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">98,362,398</td>
<td align="right">9.9%</td>
<td align="right">97,127,730</td>
<td align="right">9.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">114,234,100</td>
<td align="right">11.5%</td>
<td align="right">113,966,087</td>
<td align="right">11.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,549,216</td>
<td align="right">3.6%</td>
<td align="right">35,595,826</td>
<td align="right">3.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,897,789</td>
<td align="right">7.8%</td>
<td align="right">77,898,029</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,897,789</td>
<td align="right">7.8%</td>
<td align="right">77,898,029</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,508</td>
<td align="right">2.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">28,425,006</td>
<td align="right">2.9%</td>
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
<td align="right">435,386,932</td>
<td align="right">5.0%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,783,963,981</td>
<td align="right">20.5%</td>
<td align="right">1,657,714,515</td>
<td align="right">19.0%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,788,410,421</td>
<td align="right">20.5%</td>
<td align="right">1,662,160,955</td>
<td align="right">19.1%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,648,977,964</td>
<td align="right">30.4%</td>
<td align="right">2,513,615,142</td>
<td align="right">28.8%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,648,977,964</td>
<td align="right">30.4%</td>
<td align="right">2,513,615,142</td>
<td align="right">28.8%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">348,464,228</td>
<td align="right">4.0%</td>
<td align="right">336,900,858</td>
<td align="right">3.9%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,064,292,819</td>
<td align="right">69.6%</td>
<td align="right">6,199,260,299</td>
<td align="right">71.2%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,567,543</td>
<td align="right">9.9%</td>
<td align="right">851,454,187</td>
<td align="right">9.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,954,292,757</td>
<td align="right">79.8%</td>
<td align="right">6,954,031,513</td>
<td align="right">79.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,401,244</td>
<td align="right">1.0%</td>
<td align="right">84,398,610</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,271</td>
<td align="right">2.0%</td>
<td align="right">175,480,520</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,015,253</td>
<td align="right">0.4%</td>
<td align="right">31,015,279</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">10,918,390</td>
<td align="right"></td>
<td align="right">10,115,297</td>
<td align="right"></td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,237,638,376</td>
<td align="right"></td>
<td align="right">3,071,991,199</td>
<td align="right"></td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">53,429,990,693</td>
<td align="right">37.2%</td>
<td align="right">56,142,595,462</td>
<td align="right">39.5%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">90,338,233,069</td>
<td align="right">62.8%</td>
<td align="right">85,917,635,859</td>
<td align="right">60.5%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">94,431,359,712</td>
<td align="right">56.7%</td>
<td align="right">91,222,981,682</td>
<td align="right">55.3%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,569,681,461</td>
<td align="right"></td>
<td align="right">4,447,472,287</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">54,207,586</td>
<td align="right"></td>
<td align="right">55,537,050</td>
<td align="right"></td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">72,153,947,970</td>
<td align="right">43.3%</td>
<td align="right">73,651,239,047</td>
<td align="right">44.7%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">94,091,431</td>
<td align="right">0.4%</td>
<td align="right">93,132,659</td>
<td align="right">0.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">61,812,756</td>
<td align="right"></td>
<td align="right">62,336,287</td>
<td align="right"></td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">14,848,228</td>
<td align="right">0.1%</td>
<td align="right">14,806,058</td>
<td align="right">0.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,823,546,309</td>
<td align="right">55.7%</td>
<td align="right">12,820,058,888</td>
<td align="right">55.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,527,829,810</td>
<td align="right"></td>
<td align="right">13,524,426,303</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,714,606,650</td>
<td align="right">55.2%</td>
<td align="right">12,712,120,171</td>
<td align="right">55.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,131,266</td>
<td align="right"></td>
<td align="right">162,103,119</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,208,402,135</td>
<td align="right"></td>
<td align="right">10,208,493,427</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,206,533,082</td>
<td align="right">44.3%</td>
<td align="right">10,206,601,638</td>
<td align="right">44.3%</td>
<td align="right">0.0%</td>
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
<td align="right">115,331,920</td>
<td align="right">19,182,793,589</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,365,028</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,303,564</td>
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,720</td>
<td align="right">0.1%</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">53.5%</td>
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
<td align="right">1,892</td>
<td align="right">0.2%</td>
<td align="right">41.3%</td>
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
<td align="right">10,815</td>
<td align="right">1.0%</td>
<td align="right">-14.0%</td>
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
<td align="right">951,441</td>
<td align="right">87.9%</td>
<td align="right">-13.5%</td>
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
<td align="right">1,082,548</td>
<td align="right"></td>
<td align="right">-11.6%</td>
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
<td align="right">6,925,412,551</td>
<td align="right"></td>
<td align="right">-9.6%</td>
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
<td align="right">54,305</td>
<td align="right">5.0%</td>
<td align="right">7.6%</td>
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
<td align="right">236,590,387,088</td>
<td align="right">3,416.3%</td>
<td align="right">-5.4%</td>
</tr>
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
<td align="right">131,107</td>
<td align="right">12.1%</td>
<td align="right">4.5%</td>
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
<td align="right">6,630</td>
<td align="right">5.1%</td>
<td align="right">4.3%</td>
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
<td align="right">477,622</td>
<td align="right">44.1%</td>
<td align="right">-3.8%</td>
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
<td align="right">140</td>
<td align="right">0.0%</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">110,723</td>
<td align="right">88.2%</td>
<td align="right">118,030</td>
<td align="right">90.0%</td>
<td align="right">6.6%</td>
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
<td align="right">131,107</td>
<td align="right"></td>
<td align="right">4.5%</td>
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
<td align="right">2,364</td>
<td align="right">1.8%</td>
<td align="right">-3.4%</td>
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
<td align="right">6,477</td>
<td align="right">4.9%</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,492</td>
<td align="right">17.1%</td>
<td align="right">22,459</td>
<td align="right">17.1%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,069</td>
<td align="right">27.9%</td>
<td align="right">36,961</td>
<td align="right">28.2%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">30,950</td>
<td align="right">24.7%</td>
<td align="right">31,728</td>
<td align="right">24.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21,164</td>
<td align="right">16.9%</td>
<td align="right">20,860</td>
<td align="right">15.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,671</td>
<td align="right">7.7%</td>
<td align="right">10,542</td>
<td align="right">8.0%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,700</td>
<td align="right">1.4%</td>
<td align="right">1,920</td>
<td align="right">1.5%</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="right">5,557</td>
<td align="right">4.2%</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">14,824</td>
<td align="right">11.8%</td>
<td align="right">15,029</td>
<td align="right">11.5%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">25,109</td>
<td align="right">20.0%</td>
<td align="right">26,695</td>
<td align="right">20.4%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">36,455</td>
<td align="right">29.0%</td>
<td align="right">38,423</td>
<td align="right">29.3%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">18,459</td>
<td align="right">14.7%</td>
<td align="right">19,386</td>
<td align="right">14.8%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,726</td>
<td align="right">7.0%</td>
<td align="right">9,500</td>
<td align="right">7.2%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,640</td>
<td align="right">2.1%</td>
<td align="right">3,040</td>
<td align="right">2.3%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">380</td>
<td align="right">0.3%</td>
<td align="right">400</td>
<td align="right">0.3%</td>
<td align="right">5.3%</td>
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
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">10,050,940</td>
<td align="right">57,251,080</td>
<td align="right">469.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">11,627,700</td>
<td align="right">59,090,580</td>
<td align="right">408.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">47,971,803</td>
<td align="right">95,235,153</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,648,680</td>
<td align="right">652,560</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">239,745,240</td>
<td align="right">80,505,785</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">2,587,460</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">101,766,723</td>
<td align="right">148,140,453</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">338,030,129</td>
<td align="right">191,914,060</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">462,537</td>
<td align="right">283,998</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,831,680</td>
<td align="right">85,265,020</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">23,620</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">30,596,970</td>
<td align="right">20,933,628</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,717,580</td>
<td align="right">18,099,000</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">193,517,411</td>
<td align="right">138,918,906</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,329,328,006</td>
<td align="right">1,701,628,564</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">274,617,103</td>
<td align="right">348,143,849</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">2,013,900</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,110</td>
<td align="right">102,910,218</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,110</td>
<td align="right">102,910,218</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">436,044,792</td>
<td align="right">534,240,184</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">297,428,675</td>
<td align="right">232,816,885</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,720</td>
<td align="right">650,000</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,027,078,726</td>
<td align="right">814,200,672</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">395,091,069</td>
<td align="right">314,599,495</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,413,551</td>
<td align="right">76,206,033</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">48,440,938</td>
<td align="right">38,753,276</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">394,178,764</td>
<td align="right">471,948,502</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">266,225,788</td>
<td align="right">318,033,298</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">514,886,812</td>
<td align="right">613,394,304</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,657,411</td>
<td align="right">78,630,613</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,324,919,691</td>
<td align="right">1,090,430,014</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,862,100</td>
<td align="right">5,661,980</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,921,150</td>
<td align="right">5,748,707</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">28,421,214</td>
<td align="right">23,811,033</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">269,595,648</td>
<td align="right">226,004,548</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">270,822,908</td>
<td align="right">227,231,808</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,695,607,728</td>
<td align="right">8,201,627,274</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,280,056,779</td>
<td align="right">1,092,203,354</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,098,637,956</td>
<td align="right">945,777,783</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">244,676,060</td>
<td align="right">211,630,940</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,966,880</td>
<td align="right">2,580,520</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">59,644,340</td>
<td align="right">51,953,540</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,853,908,949</td>
<td align="right">1,615,375,953</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">67,775,580</td>
<td align="right">59,611,680</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">457,489,248</td>
<td align="right">404,267,375</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">216,537,799</td>
<td align="right">191,711,627</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">219,066,585</td>
<td align="right">194,239,735</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,611,854,806</td>
<td align="right">1,432,571,942</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">7,009,955,553</td>
<td align="right">6,246,315,693</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,739,971,633</td>
<td align="right">3,339,623,808</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,046,287,225</td>
<td align="right">934,348,293</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">777,673,568</td>
<td align="right">694,700,942</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,275,911,478</td>
<td align="right">3,822,459,105</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,165,678,517</td>
<td align="right">2,856,641,610</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,663,392,854</td>
<td align="right">6,925,412,551</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,383,531,333</td>
<td align="right">1,251,351,670</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,819,431,072</td>
<td align="right">4,360,634,383</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,638,101</td>
<td align="right">350,222,060</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">15,659,836,248</td>
<td align="right">14,307,403,128</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,688,458,980</td>
<td align="right">4,320,090,901</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,990,831,757</td>
<td align="right">16,643,842,170</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,120,367,853</td>
<td align="right">5,669,471,889</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">121,960,451</td>
<td align="right">130,929,039</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,841,164,960</td>
<td align="right">2,640,759,695</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,189,408,152</td>
<td align="right">1,269,902,852</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,301,791,792</td>
<td align="right">1,386,694,692</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">81,660,980</td>
<td align="right">86,974,460</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,036,914,590</td>
<td align="right">2,840,876,608</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,199</td>
<td align="right">603,433,490</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">81,529,700</td>
<td align="right">86,692,740</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,322,509,992</td>
<td align="right">1,406,052,692</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,591,762</td>
<td align="right">12,287,906</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,591,762</td>
<td align="right">12,287,906</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">904,464,441</td>
<td align="right">851,253,680</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,746,465,696</td>
<td align="right">2,587,714,511</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">64,522,836</td>
<td align="right">60,877,396</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,165,636,393</td>
<td align="right">2,043,987,028</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">658,563,732</td>
<td align="right">622,051,904</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">643,762,866</td>
<td align="right">608,894,450</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">890,109,062</td>
<td align="right">842,283,763</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">60,988,920</td>
<td align="right">57,779,740</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">149,619,268</td>
<td align="right">157,489,934</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,491,231,004</td>
<td align="right">1,412,876,927</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">557,698,040</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">137,740,395</td>
<td align="right">130,627,286</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,418,307,989</td>
<td align="right">4,200,428,716</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">263,534,500</td>
<td align="right">276,319,682</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,576,454,735</td>
<td align="right">1,501,785,372</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,917,600</td>
<td align="right">3,733,160</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,580,260</td>
<td align="right">82,533,580</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">5,782,740</td>
<td align="right">5,512,660</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,682,027</td>
<td align="right">10,189,789</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,258,253,734</td>
<td align="right">5,975,829,809</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">834,115,357</td>
<td align="right">797,449,313</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">173,365,468</td>
<td align="right">180,892,657</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,282,317,776</td>
<td align="right">6,976,038,268</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">317,176,897</td>
<td align="right">304,240,665</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,685,040</td>
<td align="right">196,492,960</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">75,938,681</td>
<td align="right">72,988,065</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">39,840</td>
<td align="right">41,360</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,431,918,856</td>
<td align="right">3,303,384,958</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,186,223,262</td>
<td align="right">12,697,663,160</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,102,698,860</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,025,020</td>
<td align="right">2,914,520</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,228,648</td>
<td align="right">9,866,779</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,092,173</td>
<td align="right">33,861,512</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,816,457,228</td>
<td align="right">1,753,605,506</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">387,391,356</td>
<td align="right">400,198,003</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,718,673</td>
<td align="right">94,504,956</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,824,369,759</td>
<td align="right">6,631,219,245</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">651,580,315</td>
<td align="right">633,816,639</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,511,445</td>
<td align="right">2,579,173</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,688,754,561</td>
<td align="right">1,730,157,318</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,581,520</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,085,626,855</td>
<td align="right">2,134,682,406</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,177,300</td>
<td align="right">7,990,480</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,866,101</td>
<td align="right">31,210,972</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,963,689,584</td>
<td align="right">2,003,776,547</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,420,400,153</td>
<td align="right">1,392,062,859</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">246,294,674</td>
<td align="right">241,443,015</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,790,372,963</td>
<td align="right">1,822,931,219</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,020,261,031</td>
<td align="right">1,984,540,937</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,622,893,039</td>
<td align="right">3,561,287,144</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">52,905,300</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">67,154,944</td>
<td align="right">66,056,014</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,372,398,263</td>
<td align="right">3,317,219,189</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,025,145,254</td>
<td align="right">2,058,189,284</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">164,118,930</td>
<td align="right">161,493,739</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">800,681,643</td>
<td align="right">788,429,842</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">218,973,940</td>
<td align="right">215,682,140</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">163,092,480</td>
<td align="right">160,671,723</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">25,197,736</td>
<td align="right">24,824,956</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">395,735,798</td>
<td align="right">390,000,877</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">407,485,821</td>
<td align="right">401,761,054</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">140,275,385</td>
<td align="right">138,307,338</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,258,985,067</td>
<td align="right">2,290,193,592</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,682,494,153</td>
<td align="right">1,659,597,360</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,619,543,737</td>
<td align="right">3,573,031,546</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,997,812,905</td>
<td align="right">2,023,186,626</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,059,559,797</td>
<td align="right">1,046,523,730</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">562,750,411</td>
<td align="right">555,925,554</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,883,903,750</td>
<td align="right">1,861,073,710</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">113,127,721</td>
<td align="right">111,891,705</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">702,316,836</td>
<td align="right">709,707,777</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">45,903,980</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,187,091</td>
<td align="right">97,287,854</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,430,657,611</td>
<td align="right">2,408,781,904</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,754,409</td>
<td align="right">227,797,244</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,345,934,232</td>
<td align="right">1,334,485,778</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,550,540</td>
<td align="right">185,981,260</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">970,230,774</td>
<td align="right">962,182,640</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">198,419,844</td>
<td align="right">197,002,013</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,319,487,543</td>
<td align="right">2,302,946,073</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">102,572,237</td>
<td align="right">101,908,721</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">664,423,779</td>
<td align="right">660,166,515</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">860,839,545</td>
<td align="right">855,521,546</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,131,181,328</td>
<td align="right">1,124,206,837</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,705,220</td>
<td align="right">80,223,040</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,404,439,011</td>
<td align="right">2,390,166,824</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">972,671,738</td>
<td align="right">978,328,823</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">992,083,936</td>
<td align="right">986,336,624</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">905,547,040</td>
<td align="right">900,795,239</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">214,048,243</td>
<td align="right">213,008,578</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,328,418</td>
<td align="right">2,317,500</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">923,984,301</td>
<td align="right">919,717,540</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,152,852,636</td>
<td align="right">1,147,603,556</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">104,757,000</td>
<td align="right">105,233,680</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">321,336,639</td>
<td align="right">322,772,283</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">510,187,700</td>
<td align="right">507,960,000</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,672,988</td>
<td align="right">89,284,084</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,825,999,714</td>
<td align="right">1,818,611,104</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,697,060</td>
<td align="right">12,649,360</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">235,348,136</td>
<td align="right">234,469,676</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">554,024,588</td>
<td align="right">552,273,684</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,713,899</td>
<td align="right">90,437,310</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,508,808,218</td>
<td align="right">2,501,523,728</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,990,580</td>
<td align="right">144,588,120</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,568,217,073</td>
<td align="right">6,585,164,988</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,253,443,403</td>
<td align="right">1,250,384,120</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">126,563,832</td>
<td align="right">126,837,025</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,401,617</td>
<td align="right">96,197,583</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">893,944,320</td>
<td align="right">895,836,187</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">947,162,370</td>
<td align="right">949,144,510</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,406,979</td>
<td align="right">93,596,399</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">3,628,054</td>
<td align="right">3,621,539</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,490,447</td>
<td align="right">160,692,554</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,013,560</td>
<td align="right">532,568,000</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,602,987</td>
<td align="right">731,060,575</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,164,173</td>
<td align="right">777,615,368</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,701,493</td>
<td align="right">778,252,708</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,965,460</td>
<td align="right">154,891,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,671,620</td>
<td align="right">3,670,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,682,753</td>
<td align="right">68,658,252</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,659,960</td>
<td align="right">5,658,280</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,229,751</td>
<td align="right">97,247,594</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,402,306</td>
<td align="right">32,403,888</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,449,512</td>
<td align="right">78,449,711</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">545,860</td>
<td align="right">545,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">310,680</td>
<td align="right">310,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">29,920</td>
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
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,140</td>
<td align="right">143,586</td>
<td align="right">2,238.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,200</td>
<td align="right">9,540</td>
<td align="right">695.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,540</td>
<td align="right">17,634</td>
<td align="right">398.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">600</td>
<td align="right">1,860</td>
<td align="right">210.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">320</td>
<td align="right">700</td>
<td align="right">118.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,622</td>
<td align="right">14,062</td>
<td align="right">112.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">486,303</td>
<td align="right">190,628</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">640</td>
<td align="right">660</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">33,340</td>
<td align="right">32,740</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,661</td>
<td align="right">43,948</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,457</td>
<td align="right">2,439</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">30,500</td>
<td align="right">30,460</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,680</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">360</td>
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
<td align="right">1,109</td>
<td align="right">1,104</td>
<td align="right">-0.5%</td>
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
<td align="right">1,104</td>
<td align="right">-0.5%</td>
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
Stats gathered on: 2024-07-14
