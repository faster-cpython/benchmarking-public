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
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,432,340</td>
<td align="right">3,920,964</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">43,051,757</td>
<td align="right">46,412,063</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">67,847,893</td>
<td align="right">69,707,118</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">133,383,267</td>
<td align="right">136,650,515</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">233,653,329</td>
<td align="right">239,341,632</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,642</td>
<td align="right">2,581</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,512,010</td>
<td align="right">63,882,953</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">384,036,717</td>
<td align="right">391,934,785</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">186,482,361</td>
<td align="right">190,091,598</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">120,162,427</td>
<td align="right">122,141,631</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,172,032,304</td>
<td align="right">3,213,463,584</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">263,167,420</td>
<td align="right">266,324,236</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">92,655,017</td>
<td align="right">93,749,636</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,721,828</td>
<td align="right">13,567,710</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">56,957,514</td>
<td align="right">57,584,334</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">111,963,962</td>
<td align="right">113,120,172</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">272,629,207</td>
<td align="right">275,341,735</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">270,398,930</td>
<td align="right">273,021,995</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,361,223</td>
<td align="right">61,926,369</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">252,373</td>
<td align="right">250,089</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">781,898,211</td>
<td align="right">788,535,642</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,307,520</td>
<td align="right">125,332,438</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">925,115,173</td>
<td align="right">932,690,860</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">880,537,027</td>
<td align="right">887,709,595</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">162,323,150</td>
<td align="right">163,635,134</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">866,927,674</td>
<td align="right">873,273,649</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,709,846</td>
<td align="right">1,721,848</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">107,222,247</td>
<td align="right">107,964,230</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">214,668,226</td>
<td align="right">216,121,375</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,108,252,559</td>
<td align="right">4,135,035,066</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,969,837,012</td>
<td align="right">3,993,990,142</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">864,140,679</td>
<td align="right">869,173,813</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,260,616</td>
<td align="right">10,201,070</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">281,327,633</td>
<td align="right">282,905,683</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">54,908,720</td>
<td align="right">55,208,411</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">74,922,960</td>
<td align="right">75,273,996</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,652,680,084</td>
<td align="right">16,729,683,994</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">164,573,206</td>
<td align="right">165,332,890</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">243,846,699</td>
<td align="right">244,968,922</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">607,091,015</td>
<td align="right">609,877,298</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">205,905,860</td>
<td align="right">206,813,943</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">80,949,130</td>
<td align="right">81,300,166</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,516,113</td>
<td align="right">4,496,797</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,177,131</td>
<td align="right">41,352,649</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,963,236,994</td>
<td align="right">4,983,841,956</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">114,654,878</td>
<td align="right">115,122,079</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">13,143,130</td>
<td align="right">13,192,574</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,996,673</td>
<td align="right">9,959,091</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">95,809,048</td>
<td align="right">96,163,079</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">85,091,901</td>
<td align="right">85,405,986</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">138,776,165</td>
<td align="right">139,273,746</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">369,828,328</td>
<td align="right">371,096,341</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,022,473,060</td>
<td align="right">1,025,977,244</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">13,157</td>
<td align="right">13,113</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">929,801,314</td>
<td align="right">932,907,191</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">540,041,523</td>
<td align="right">541,832,663</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">259,388,527</td>
<td align="right">260,241,940</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">185,028,403</td>
<td align="right">185,634,778</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">446,559,281</td>
<td align="right">447,942,371</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,420,174,564</td>
<td align="right">1,424,535,230</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,515,745</td>
<td align="right">12,478,343</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">163,450,851</td>
<td align="right">163,002,026</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,928,689,923</td>
<td align="right">1,933,812,945</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">56,753,320</td>
<td align="right">56,604,435</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,221,715,837</td>
<td align="right">2,227,543,200</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">67,821,301</td>
<td align="right">67,999,018</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,717,829</td>
<td align="right">9,742,833</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">242,889,562</td>
<td align="right">243,498,064</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">288,949,600</td>
<td align="right">289,663,828</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,076,915,410</td>
<td align="right">1,079,530,517</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">383,451,004</td>
<td align="right">384,378,580</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,496,462,977</td>
<td align="right">2,502,462,922</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">198,127,638</td>
<td align="right">198,581,737</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,008,034,074</td>
<td align="right">2,012,279,856</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,004,463,509</td>
<td align="right">5,014,853,396</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,685,491,916</td>
<td align="right">4,695,078,552</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,817,854</td>
<td align="right">18,779,500</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">44,465,558</td>
<td align="right">44,377,300</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,002,836,556</td>
<td align="right">2,006,457,406</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">18,395,260</td>
<td align="right">18,365,181</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">336,234,828</td>
<td align="right">336,778,655</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">87,136,107</td>
<td align="right">87,002,821</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">173,452,875</td>
<td align="right">173,701,628</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">661,987,945</td>
<td align="right">662,825,767</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">649,196,489</td>
<td align="right">649,968,324</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,730,930,356</td>
<td align="right">3,735,249,079</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,575,930,749</td>
<td align="right">2,578,724,444</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">575,497,221</td>
<td align="right">576,116,964</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,268,257</td>
<td align="right">2,270,349</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">106,550,554</td>
<td align="right">106,461,927</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,963,906</td>
<td align="right">27,940,821</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">76,794,618</td>
<td align="right">76,736,922</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">911,502,539</td>
<td align="right">912,168,157</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,301,023</td>
<td align="right">242,477,386</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,350,484</td>
<td align="right">244,528,253</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">192,051,313</td>
<td align="right">191,915,305</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">438,786,661</td>
<td align="right">439,091,565</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">196,178,242</td>
<td align="right">196,310,036</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">443,891,134</td>
<td align="right">444,172,104</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">354,775,658</td>
<td align="right">354,988,298</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">666,446,896</td>
<td align="right">666,841,187</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">882,191,433</td>
<td align="right">882,707,474</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">368,788,168</td>
<td align="right">369,003,817</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">200,398,952</td>
<td align="right">200,514,039</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">344,571,393</td>
<td align="right">344,765,076</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">39,892,484</td>
<td align="right">39,914,742</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">34,166</td>
<td align="right">34,147</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,462</td>
<td align="right">5,459</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,112,638,314</td>
<td align="right">1,113,249,384</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">183,687,744</td>
<td align="right">183,587,706</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">609,628,905</td>
<td align="right">609,943,801</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">246,381,333</td>
<td align="right">246,508,430</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">432,273,642</td>
<td align="right">432,481,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,565,756</td>
<td align="right">3,567,394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">51,352,311</td>
<td align="right">51,329,207</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">879,249,050</td>
<td align="right">879,643,625</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">43,529,993</td>
<td align="right">43,544,923</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">67,070,567</td>
<td align="right">67,047,707</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">171,569,783</td>
<td align="right">171,513,528</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">822,701,281</td>
<td align="right">822,480,493</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,418,734</td>
<td align="right">35,427,828</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">440,629</td>
<td align="right">440,738</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">459,144,769</td>
<td align="right">459,245,082</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">173,268,894</td>
<td align="right">173,232,045</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">27,218,398</td>
<td align="right">27,222,956</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">146,129,192</td>
<td align="right">146,109,715</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,762,980</td>
<td align="right">14,761,424</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">53,867,694</td>
<td align="right">53,872,947</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">154,265,818</td>
<td align="right">154,251,657</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">69,832,724</td>
<td align="right">69,826,839</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">118,557,616</td>
<td align="right">118,566,333</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">365,620,712</td>
<td align="right">365,645,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">73,590,227</td>
<td align="right">73,594,825</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">497,319,659</td>
<td align="right">497,350,322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">288,520,411</td>
<td align="right">288,538,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,047,965</td>
<td align="right">3,048,147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">367,126,209</td>
<td align="right">367,104,339</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,720,513</td>
<td align="right">25,721,978</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,091,692</td>
<td align="right">5,091,956</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,774,291</td>
<td align="right">5,774,571</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,262,374</td>
<td align="right">1,262,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,724,710</td>
<td align="right">155,730,774</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,591,917,840</td>
<td align="right">1,591,872,912</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">277,684</td>
<td align="right">277,687</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,187,367</td>
<td align="right">9,187,461</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">64,420,292</td>
<td align="right">64,420,888</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,611,855</td>
<td align="right">114,612,832</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">810,304,609</td>
<td align="right">810,311,366</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,456</td>
<td align="right">5,803,494</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,372,935</td>
<td align="right">70,373,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">119,450,470</td>
<td align="right">119,450,738</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">19,857,349</td>
<td align="right">19,857,308</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,188,345</td>
<td align="right">20,188,304</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,188,324</td>
<td align="right">20,188,284</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">34,572,391</td>
<td align="right">34,572,459</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">123,859,626</td>
<td align="right">123,859,739</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">103,557,324</td>
<td align="right">103,557,231</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">129,276,030</td>
<td align="right">129,275,996</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,234,111</td>
<td align="right">418,234,082</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,353,967</td>
<td align="right">131,353,972</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">114,765,175</td>
<td align="right">114,765,173</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,619,534</td>
<td align="right">591,619,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">468,522,077</td>
<td align="right">468,522,077</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,141</td>
<td align="right">302,246,141</td>
<td align="right">0.0%</td>
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
<td align="left">DELETE_FAST</td>
<td align="right">41,964,571</td>
<td align="right">41,964,571</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,093</td>
<td align="right">35,549,093</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">30,832,979</td>
<td align="right">30,832,979</td>
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
<td align="left">RERAISE</td>
<td align="right">3,484,991</td>
<td align="right">3,484,991</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,144</td>
<td align="right">2,597,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,232,482</td>
<td align="right">1,232,482</td>
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
<td align="left">STORE_NAME</td>
<td align="right">57,748</td>
<td align="right">57,748</td>
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
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,295</td>
<td align="right">5,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,904</td>
<td align="right">3,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,586</td>
<td align="right">3,586</td>
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
<td align="right">1,076,433,261</td>
<td align="right">6.2%</td>
<td align="right">1,079,048,876</td>
<td align="right">6.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,229,586,406</td>
<td align="right">93.5%</td>
<td align="right">16,244,487,845</td>
<td align="right">93.5%</td>
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
<td align="right">55,515,913</td>
<td align="right">0.3%</td>
<td align="right">55,521,259</td>
<td align="right">0.3%</td>
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
<td align="right">463,466</td>
<td align="right">30.3%</td>
<td align="right">464,041</td>
<td align="right">30.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,065,928</td>
<td align="right">69.7%</td>
<td align="right">1,064,954</td>
<td align="right">69.7%</td>
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
<td align="left">xor</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">169</td>
<td align="right">0.0%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">327</td>
<td align="right">0.1%</td>
<td align="right">349</td>
<td align="right">0.1%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">329</td>
<td align="right">0.1%</td>
<td align="right">335</td>
<td align="right">0.1%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,035</td>
<td align="right">1.5%</td>
<td align="right">7,140</td>
<td align="right">1.5%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">40,935</td>
<td align="right">8.8%</td>
<td align="right">41,352</td>
<td align="right">8.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,130</td>
<td align="right">0.7%</td>
<td align="right">3,110</td>
<td align="right">0.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">624</td>
<td align="right">0.1%</td>
<td align="right">626</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,349</td>
<td align="right">0.5%</td>
<td align="right">2,343</td>
<td align="right">0.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">1,814</td>
<td align="right">0.4%</td>
<td align="right">1,816</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,291</td>
<td align="right">1.8%</td>
<td align="right">8,300</td>
<td align="right">1.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,447</td>
<td align="right">4.0%</td>
<td align="right">18,466</td>
<td align="right">4.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,768</td>
<td align="right">0.6%</td>
<td align="right">2,767</td>
<td align="right">0.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,849</td>
<td align="right">4.3%</td>
<td align="right">19,855</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">22,440</td>
<td align="right">4.8%</td>
<td align="right">22,444</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">63,009</td>
<td align="right">13.6%</td>
<td align="right">63,000</td>
<td align="right">13.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">11,553</td>
<td align="right">2.5%</td>
<td align="right">11,552</td>
<td align="right">2.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">36,400</td>
<td align="right">7.9%</td>
<td align="right">36,403</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21,969</td>
<td align="right">4.7%</td>
<td align="right">21,968</td>
<td align="right">4.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">107,940</td>
<td align="right">23.3%</td>
<td align="right">107,938</td>
<td align="right">23.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">28,692</td>
<td align="right">6.2%</td>
<td align="right">28,692</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">25,838</td>
<td align="right">5.6%</td>
<td align="right">25,838</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">16,343</td>
<td align="right">3.5%</td>
<td align="right">16,343</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,693</td>
<td align="right">1.4%</td>
<td align="right">6,693</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,194</td>
<td align="right">1.3%</td>
<td align="right">6,194</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,163</td>
<td align="right">0.7%</td>
<td align="right">3,163</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,334</td>
<td align="right">0.5%</td>
<td align="right">2,334</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,995</td>
<td align="right">0.4%</td>
<td align="right">1,995</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">836</td>
<td align="right">0.2%</td>
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
<td align="left">subscr deque</td>
<td align="right">107</td>
<td align="right">0.0%</td>
<td align="right">107</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">80</td>
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
<td align="right">185,028,403</td>
<td align="right">100.0%</td>
<td align="right">185,634,778</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">151,045,128</td>
<td align="right">1.3%</td>
<td align="right">153,665,614</td>
<td align="right">1.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">148,270,828</td>
<td align="right">1.3%</td>
<td align="right">150,841,804</td>
<td align="right">1.3%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,089,129,471</td>
<td align="right">98.7%</td>
<td align="right">11,101,771,463</td>
<td align="right">98.6%</td>
<td align="right">0.1%</td>
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
<td align="right">3,026,527</td>
<td align="right">100.0%</td>
<td align="right">3,073,753</td>
<td align="right">100.0%</td>
<td align="right">1.6%</td>
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
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">267</td>
<td align="right">182.9%</td>
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
<td align="right">576,079</td>
<td align="right">96.6%</td>
<td align="right">576,077</td>
<td align="right">96.6%</td>
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
<td align="right">20,452</td>
<td align="right">100.0%</td>
<td align="right">20,410</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">92,537,270</td>
<td align="right">2.0%</td>
<td align="right">93,631,719</td>
<td align="right">2.0%</td>
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
<td align="right">1,154,794</td>
<td align="right">0.0%</td>
<td align="right">1,166,363</td>
<td align="right">0.0%</td>
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
<td align="right">4,494,315,597</td>
<td align="right">98.0%</td>
<td align="right">4,507,141,980</td>
<td align="right">97.9%</td>
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
<td align="right">99,302</td>
<td align="right">71.3%</td>
<td align="right">99,809</td>
<td align="right">71.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">40,030</td>
<td align="right">28.7%</td>
<td align="right">39,920</td>
<td align="right">28.6%</td>
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
<td align="left">long float</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">196</td>
<td align="right">0.2%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,323</td>
<td align="right">1.3%</td>
<td align="right">1,369</td>
<td align="right">1.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,105</td>
<td align="right">4.1%</td>
<td align="right">4,165</td>
<td align="right">4.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">9,265</td>
<td align="right">9.3%</td>
<td align="right">9,382</td>
<td align="right">9.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,607</td>
<td align="right">7.7%</td>
<td align="right">7,702</td>
<td align="right">7.7%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">374</td>
<td align="right">0.4%</td>
<td align="right">371</td>
<td align="right">0.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">36,906</td>
<td align="right">37.2%</td>
<td align="right">37,073</td>
<td align="right">37.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,866</td>
<td align="right">1.9%</td>
<td align="right">1,865</td>
<td align="right">1.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">5,877</td>
<td align="right">5.9%</td>
<td align="right">5,875</td>
<td align="right">5.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,163</td>
<td align="right">23.3%</td>
<td align="right">23,169</td>
<td align="right">23.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">7.7%</td>
<td align="right">7,648</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">994</td>
<td align="right">1.0%</td>
<td align="right">994</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">85,048,139</td>
<td align="right">3.7%</td>
<td align="right">85,362,394</td>
<td align="right">3.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,183,716,973</td>
<td align="right">96.2%</td>
<td align="right">2,186,967,731</td>
<td align="right">96.2%</td>
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
<td align="right">1,389,959</td>
<td align="right">0.1%</td>
<td align="right">1,389,959</td>
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
<td align="left">Success</td>
<td align="right">28,539</td>
<td align="right">40.8%</td>
<td align="right">28,339</td>
<td align="right">40.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">41,446</td>
<td align="right">59.2%</td>
<td align="right">41,476</td>
<td align="right">59.4%</td>
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
<td align="left">other</td>
<td align="right">9,303</td>
<td align="right">22.4%</td>
<td align="right">9,262</td>
<td align="right">22.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">11,947</td>
<td align="right">28.8%</td>
<td align="right">11,990</td>
<td align="right">28.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,547</td>
<td align="right">25.4%</td>
<td align="right">10,575</td>
<td align="right">25.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,649</td>
<td align="right">23.3%</td>
<td align="right">9,649</td>
<td align="right">23.3%</td>
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
<td align="right">196,064,224</td>
<td align="right">12.7%</td>
<td align="right">196,195,727</td>
<td align="right">12.7%</td>
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
<td align="right">1,291,632,897</td>
<td align="right">83.7%</td>
<td align="right">1,292,463,735</td>
<td align="right">83.7%</td>
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
<td align="right">55,887,504</td>
<td align="right">3.6%</td>
<td align="right">55,901,680</td>
<td align="right">3.6%</td>
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
<td align="right">108,532</td>
<td align="right">9.3%</td>
<td align="right">108,828</td>
<td align="right">9.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,059,803</td>
<td align="right">90.7%</td>
<td align="right">1,060,066</td>
<td align="right">90.7%</td>
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
<td align="left">reversed list</td>
<td align="right">1,639</td>
<td align="right">1.5%</td>
<td align="right">1,703</td>
<td align="right">1.6%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">50,256</td>
<td align="right">46.3%</td>
<td align="right">50,544</td>
<td align="right">46.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,208</td>
<td align="right">3.9%</td>
<td align="right">4,191</td>
<td align="right">3.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,936</td>
<td align="right">11.9%</td>
<td align="right">12,887</td>
<td align="right">11.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,163</td>
<td align="right">3.8%</td>
<td align="right">4,167</td>
<td align="right">3.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,564</td>
<td align="right">3.3%</td>
<td align="right">3,567</td>
<td align="right">3.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,529</td>
<td align="right">6.0%</td>
<td align="right">6,532</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">6,468</td>
<td align="right">6.0%</td>
<td align="right">6,467</td>
<td align="right">5.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">10,964</td>
<td align="right">10.1%</td>
<td align="right">10,965</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">5,892</td>
<td align="right">5.4%</td>
<td align="right">5,892</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,236</td>
<td align="right">1.1%</td>
<td align="right">1,236</td>
<td align="right">1.1%</td>
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
<td align="left">map</td>
<td align="right">260</td>
<td align="right">0.2%</td>
<td align="right">260</td>
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
<td align="left">set</td>
<td align="right">12,138,501</td>
<td align="right">12,138,501 / 0 !!</td>
<td align="right">12,110,620</td>
<td align="right">12,110,620 / 0 !!</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">116,655,469</td>
<td align="right">116,655,469 / 0 !!</td>
<td align="right">116,791,339</td>
<td align="right">116,791,339 / 0 !!</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">302,796,691</td>
<td align="right">302,796,691 / 0 !!</td>
<td align="right">303,094,761</td>
<td align="right">303,094,761 / 0 !!</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">171,610,026</td>
<td align="right">171,610,026 / 0 !!</td>
<td align="right">171,442,829</td>
<td align="right">171,442,829 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">390,766,639</td>
<td align="right">390,766,639 / 0 !!</td>
<td align="right">390,868,624</td>
<td align="right">390,868,624 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">102,090,382</td>
<td align="right">102,090,382 / 0 !!</td>
<td align="right">102,092,402</td>
<td align="right">102,092,402 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,730,051</td>
<td align="right">5,730,051 / 0 !!</td>
<td align="right">5,730,116</td>
<td align="right">5,730,116 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,813,451</td>
<td align="right">34,813,451 / 0 !!</td>
<td align="right">34,813,451</td>
<td align="right">34,813,451 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,693,965</td>
<td align="right">2,693,965 / 0 !!</td>
<td align="right">2,693,965</td>
<td align="right">2,693,965 / 0 !!</td>
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
<td align="right">11,908,984,940</td>
<td align="right">91.1%</td>
<td align="right">10,227,620,709</td>
<td align="right">89.8%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">538,337,705</td>
<td align="right">4.1%</td>
<td align="right">540,132,160</td>
<td align="right">4.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">617,401,997</td>
<td align="right">4.7%</td>
<td align="right">618,107,439</td>
<td align="right">5.4%</td>
<td align="right">0.1%</td>
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
<td align="left">Failure</td>
<td align="right">441,844</td>
<td align="right">3.6%</td>
<td align="right">442,662</td>
<td align="right">3.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,738,803</td>
<td align="right">96.4%</td>
<td align="right">11,747,959</td>
<td align="right">96.4%</td>
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
<td align="left">method</td>
<td align="right">37,369</td>
<td align="right">8.5%</td>
<td align="right">37,945</td>
<td align="right">8.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,738</td>
<td align="right">0.4%</td>
<td align="right">1,764</td>
<td align="right">0.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,861</td>
<td align="right">1.1%</td>
<td align="right">4,909</td>
<td align="right">1.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,451</td>
<td align="right">3.5%</td>
<td align="right">15,483</td>
<td align="right">3.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">41,075</td>
<td align="right">9.3%</td>
<td align="right">41,135</td>
<td align="right">9.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,237</td>
<td align="right">5.5%</td>
<td align="right">24,208</td>
<td align="right">5.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">1.0%</td>
<td align="right">4,449</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">48,001</td>
<td align="right">10.9%</td>
<td align="right">48,010</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,658</td>
<td align="right">1.7%</td>
<td align="right">7,658</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,379</td>
<td align="right">0.5%</td>
<td align="right">2,379</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,799</td>
<td align="right">0.4%</td>
<td align="right">1,799</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,033</td>
<td align="right">0.2%</td>
<td align="right">1,033</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">741</td>
<td align="right">0.2%</td>
<td align="right">741</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">47,985</td>
<td align="right">0.0%</td>
<td align="right">48,552</td>
<td align="right">0.0%</td>
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
<td align="right">4,609,129,078</td>
<td align="right">99.7%</td>
<td align="right">4,618,749,344</td>
<td align="right">99.7%</td>
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
<td align="right">14,623,313</td>
<td align="right">0.3%</td>
<td align="right">14,623,260</td>
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
<td align="right">140,378</td>
<td align="right">100.0%</td>
<td align="right">138,875</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">217</td>
<td align="right">0.0%</td>
<td align="right">216</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">65,471,594</td>
<td align="right">100.0%</td>
<td align="right">65,260,185</td>
<td align="right">100.0%</td>
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
<td align="left">Success</td>
<td align="right">2,425</td>
<td align="right">100.0%</td>
<td align="right">2,365</td>
<td align="right">100.0%</td>
<td align="right">-2.5%</td>
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
<td align="right">128,816,934</td>
<td align="right">17.9%</td>
<td align="right">128,816,934</td>
<td align="right">17.9%</td>
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
<td align="right">591,604,823</td>
<td align="right">82.1%</td>
<td align="right">591,604,823</td>
<td align="right">82.1%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">61,274,628</td>
<td align="right">3.1%</td>
<td align="right">61,841,072</td>
<td align="right">3.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,811,912,043</td>
<td align="right">91.5%</td>
<td align="right">1,818,257,487</td>
<td align="right">91.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">106,964,632</td>
<td align="right">5.4%</td>
<td align="right">106,971,902</td>
<td align="right">5.4%</td>
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
<td align="right">44,484</td>
<td align="right">2.1%</td>
<td align="right">44,586</td>
<td align="right">2.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,059,434</td>
<td align="right">97.9%</td>
<td align="right">2,058,203</td>
<td align="right">97.9%</td>
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
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.6%</td>
<td align="right">1,665</td>
<td align="right">3.7%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,650</td>
<td align="right">10.5%</td>
<td align="right">4,715</td>
<td align="right">10.6%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,354</td>
<td align="right">7.5%</td>
<td align="right">3,342</td>
<td align="right">7.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,781</td>
<td align="right">8.5%</td>
<td align="right">3,785</td>
<td align="right">8.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">241,371</td>
<td align="right">542.6%</td>
<td align="right">241,386</td>
<td align="right">541.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">19,853</td>
<td align="right">44.6%</td>
<td align="right">19,853</td>
<td align="right">44.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,227</td>
<td align="right">16.2%</td>
<td align="right">7,227</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">764</td>
<td align="right">1.7%</td>
<td align="right">764</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">1.0%</td>
<td align="right">423</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">365</td>
<td align="right">0.8%</td>
<td align="right">365</td>
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
<td align="right">1,232,482</td>
<td align="right">100.0%</td>
<td align="right">1,232,482</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">916,893,418</td>
<td align="right">89.9%</td>
<td align="right">918,253,624</td>
<td align="right">89.9%</td>
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
<td align="right">103,518,812</td>
<td align="right">10.1%</td>
<td align="right">103,518,839</td>
<td align="right">10.1%</td>
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
<td align="left">Success</td>
<td align="right">2,220</td>
<td align="right">5.8%</td>
<td align="right">2,100</td>
<td align="right">5.5%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">36,332</td>
<td align="right">94.2%</td>
<td align="right">36,332</td>
<td align="right">94.5%</td>
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
<td align="right">17,283</td>
<td align="right">47.6%</td>
<td align="right">17,283</td>
<td align="right">47.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">10,484</td>
<td align="right">28.9%</td>
<td align="right">10,484</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">3,323</td>
<td align="right">9.1%</td>
<td align="right">3,323</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,990</td>
<td align="right">8.2%</td>
<td align="right">2,990</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">4.6%</td>
<td align="right">1,681</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.9%</td>
<td align="right">341</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">162</td>
<td align="right">0.4%</td>
<td align="right">162</td>
<td align="right">0.4%</td>
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
<td align="right">132,863,398</td>
<td align="right">3.1%</td>
<td align="right">136,129,862</td>
<td align="right">3.1%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,151,463,577</td>
<td align="right">95.4%</td>
<td align="right">4,159,231,059</td>
<td align="right">95.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">65,597,427</td>
<td align="right">1.5%</td>
<td align="right">65,628,551</td>
<td align="right">1.5%</td>
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
<td align="right">468,287</td>
<td align="right">26.7%</td>
<td align="right">469,643</td>
<td align="right">26.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,287,542</td>
<td align="right">73.3%</td>
<td align="right">1,287,531</td>
<td align="right">73.3%</td>
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
<td align="right">8,853</td>
<td align="right">1.9%</td>
<td align="right">9,528</td>
<td align="right">2.0%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">71,775</td>
<td align="right">15.3%</td>
<td align="right">72,384</td>
<td align="right">15.4%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">10,775</td>
<td align="right">2.3%</td>
<td align="right">10,846</td>
<td align="right">2.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">27,788</td>
<td align="right">5.9%</td>
<td align="right">27,819</td>
<td align="right">5.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">74,622</td>
<td align="right">15.9%</td>
<td align="right">74,584</td>
<td align="right">15.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,677</td>
<td align="right">1.0%</td>
<td align="right">4,678</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,067</td>
<td align="right">2.1%</td>
<td align="right">10,066</td>
<td align="right">2.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,844</td>
<td align="right">55.1%</td>
<td align="right">257,852</td>
<td align="right">54.9%</td>
<td align="right">0.0%</td>
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
<td align="right">1,232,437,325</td>
<td align="right">99.9%</td>
<td align="right">1,232,649,016</td>
<td align="right">99.9%</td>
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
<td align="right">1,251,588</td>
<td align="right">0.1%</td>
<td align="right">1,251,676</td>
<td align="right">0.1%</td>
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
<td align="right">798</td>
<td align="right">7.3%</td>
<td align="right">789</td>
<td align="right">7.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,068</td>
<td align="right">92.7%</td>
<td align="right">10,040</td>
<td align="right">92.7%</td>
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
<td align="right">564</td>
<td align="right">70.7%</td>
<td align="right">555</td>
<td align="right">70.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">17.0%</td>
<td align="right">136</td>
<td align="right">17.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">12.3%</td>
<td align="right">98</td>
<td align="right">12.4%</td>
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
<td align="right">35,444,891,998</td>
<td align="right">36.0%</td>
<td align="right">35,586,855,652</td>
<td align="right">36.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">58,827,300,644</td>
<td align="right">59.7%</td>
<td align="right">59,030,250,198</td>
<td align="right">59.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">3,196,087,271</td>
<td align="right">3.2%</td>
<td align="right">3,207,088,541</td>
<td align="right">3.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,055,771,320</td>
<td align="right">1.1%</td>
<td align="right">1,059,167,354</td>
<td align="right">1.1%</td>
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
<td align="right">132,863,398</td>
<td align="right">4.8%</td>
<td align="right">136,129,862</td>
<td align="right">4.9%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">148,270,828</td>
<td align="right">5.4%</td>
<td align="right">150,841,804</td>
<td align="right">5.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">92,537,270</td>
<td align="right">3.3%</td>
<td align="right">93,631,719</td>
<td align="right">3.4%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">85,048,139</td>
<td align="right">3.1%</td>
<td align="right">85,362,394</td>
<td align="right">3.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">538,337,705</td>
<td align="right">19.5%</td>
<td align="right">540,132,160</td>
<td align="right">19.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">185,028,403</td>
<td align="right">6.7%</td>
<td align="right">185,634,778</td>
<td align="right">6.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,076,433,261</td>
<td align="right">38.9%</td>
<td align="right">1,079,048,876</td>
<td align="right">38.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">196,064,224</td>
<td align="right">7.1%</td>
<td align="right">196,195,727</td>
<td align="right">7.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">103,518,812</td>
<td align="right">3.7%</td>
<td align="right">103,518,839</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,934</td>
<td align="right">4.7%</td>
<td align="right">128,816,934</td>
<td align="right">4.6%</td>
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
<td align="right">53,602,705</td>
<td align="right">5.1%</td>
<td align="right">54,966,541</td>
<td align="right">5.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">27,902,218</td>
<td align="right">2.6%</td>
<td align="right">27,914,912</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">31,069,071</td>
<td align="right">2.9%</td>
<td align="right">31,082,305</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">85,441,190</td>
<td align="right">8.1%</td>
<td align="right">85,451,879</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">27,907,897</td>
<td align="right">2.6%</td>
<td align="right">27,909,373</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">87,966,727</td>
<td align="right">8.3%</td>
<td align="right">87,968,239</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">27,958,057</td>
<td align="right">2.6%</td>
<td align="right">27,958,232</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">81,597,986</td>
<td align="right">7.7%</td>
<td align="right">81,598,488</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">174,188,527</td>
<td align="right">16.5%</td>
<td align="right">174,188,750</td>
<td align="right">16.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">221,897,079</td>
<td align="right">21.0%</td>
<td align="right">221,897,056</td>
<td align="right">20.9%</td>
<td align="right">-0.0%</td>
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
<td align="right">4,262,472</td>
<td align="right">0.1%</td>
<td align="right">4,273,473</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,080,196,316</td>
<td align="right">76.1%</td>
<td align="right">5,090,156,967</td>
<td align="right">76.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,406,744,876</td>
<td align="right">81.0%</td>
<td align="right">5,416,224,811</td>
<td align="right">81.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">274,663,260</td>
<td align="right">4.1%</td>
<td align="right">274,803,900</td>
<td align="right">4.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,007,802,803</td>
<td align="right">15.1%</td>
<td align="right">1,007,678,544</td>
<td align="right">15.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,340,211</td>
<td align="right">8.8%</td>
<td align="right">584,408,536</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,012,069,179</td>
<td align="right">15.2%</td>
<td align="right">1,011,955,921</td>
<td align="right">15.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,503,323</td>
<td align="right">3.9%</td>
<td align="right">259,511,086</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,596,409,390</td>
<td align="right">23.9%</td>
<td align="right">1,596,364,457</td>
<td align="right">23.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,596,409,390</td>
<td align="right">23.9%</td>
<td align="right">1,596,364,457</td>
<td align="right">23.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,998,835</td>
<td align="right">0.4%</td>
<td align="right">23,999,174</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,150,589</td>
<td align="right">1.1%</td>
<td align="right">70,150,445</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,904</td>
<td align="right">0.0%</td>
<td align="right">3,904</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,901</td>
<td align="right">2.0%</td>
<td align="right">132,513,901</td>
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
<td align="left">Method cache misses</td>
<td align="right">53,623,670</td>
<td align="right"></td>
<td align="right">58,799,950</td>
<td align="right"></td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,599,626</td>
<td align="right"></td>
<td align="right">6,911,664</td>
<td align="right"></td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">60,416,477</td>
<td align="right"></td>
<td align="right">64,904,768</td>
<td align="right"></td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">24,550,854,310</td>
<td align="right">26.5%</td>
<td align="right">24,642,211,986</td>
<td align="right">26.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">33,549,936,482</td>
<td align="right">30.4%</td>
<td align="right">33,656,656,524</td>
<td align="right">30.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,369,894,197</td>
<td align="right">26.3%</td>
<td align="right">24,407,812,652</td>
<td align="right">26.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,164,791</td>
<td align="right">0.4%</td>
<td align="right">71,269,528</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,220,394,566</td>
<td align="right">1.1%</td>
<td align="right">1,221,989,981</td>
<td align="right">1.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">25,393,332,059</td>
<td align="right">23.0%</td>
<td align="right">25,426,424,108</td>
<td align="right">23.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,545,785,870</td>
<td align="right">28.2%</td>
<td align="right">5,550,592,358</td>
<td align="right">28.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,468,213,044</td>
<td align="right">27.8%</td>
<td align="right">5,472,910,412</td>
<td align="right">27.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,191,685,223</td>
<td align="right"></td>
<td align="right">2,189,825,047</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,144,002,612</td>
<td align="right"></td>
<td align="right">6,148,217,303</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,408,035</td>
<td align="right">0.0%</td>
<td align="right">6,412,418</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,150,384,570</td>
<td align="right"></td>
<td align="right">14,158,826,027</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,150,273,630</td>
<td align="right">71.8%</td>
<td align="right">14,158,697,983</td>
<td align="right">71.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,997,329,402</td>
<td align="right">3.2%</td>
<td align="right">2,999,012,982</td>
<td align="right">3.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">40,813,860,936</td>
<td align="right">44.0%</td>
<td align="right">40,827,942,292</td>
<td align="right">44.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">175,336,433</td>
<td align="right"></td>
<td align="right">175,365,289</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">50,140,390,237</td>
<td align="right">45.5%</td>
<td align="right">50,148,471,532</td>
<td align="right">45.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,428,899,285</td>
<td align="right"></td>
<td align="right">2,429,174,507</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,405,116</td>
<td align="right">1.9%</td>
<td align="right">3,405,116</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">265,168</td>
<td align="right">0.2%</td>
<td align="right">265,168</td>
<td align="right">0.2%</td>
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
<td align="right">364,011</td>
<td align="right">101,233,194</td>
<td align="right">9,456,134,876</td>
<td align="right">749,256,086</td>
<td align="right">761,578,478</td>
<td align="right">364,530</td>
<td align="right">101,520,109</td>
<td align="right">9,460,370,556</td>
<td align="right">748,547,276</td>
<td align="right">762,685,276</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,675,849,812</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,675,857,612</td>
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
<td align="right">605</td>
<td align="right">0.1%</td>
<td align="right">627</td>
<td align="right">0.1%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">126,073</td>
<td align="right">28.2%</td>
<td align="right">127,118</td>
<td align="right">28.4%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">258,069,710,361</td>
<td align="right">6,432.4%</td>
<td align="right">257,060,146,039</td>
<td align="right">6,407.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">446,826</td>
<td align="right"></td>
<td align="right">447,881</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,754</td>
<td align="right">0.4%</td>
<td align="right">1,751</td>
<td align="right">0.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">34,455</td>
<td align="right">7.7%</td>
<td align="right">34,511</td>
<td align="right">7.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">47,330</td>
<td align="right">10.6%</td>
<td align="right">47,307</td>
<td align="right">10.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">238,786</td>
<td align="right">53.4%</td>
<td align="right">238,763</td>
<td align="right">53.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">4,012,032,949</td>
<td align="right"></td>
<td align="right">4,011,703,737</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">182</td>
<td align="right">0.0%</td>
<td align="right">182</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">2,926</td>
<td align="right">0.7%</td>
<td align="right">2,926</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
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
<td align="right">0.8%</td>
<td align="right">261</td>
<td align="right">0.8%</td>
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
<td align="right">27,328</td>
<td align="right">79.3%</td>
<td align="right">27,270</td>
<td align="right">79.0%</td>
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
<td align="right">34,455</td>
<td align="right"></td>
<td align="right">34,511</td>
<td align="right"></td>
<td align="right">0.2%</td>
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
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">280,783,771</td>
<td align="right">81.3%</td>
<td align="right">276,509,078</td>
<td align="right">81.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">345,268,224</td>
<td align="right"></td>
<td align="right">340,697,088</td>
<td align="right"></td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">18,178,048</td>
<td align="right">5.3%</td>
<td align="right">18,014,208</td>
<td align="right">5.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">7,339,648</td>
<td align="right">2.1%</td>
<td align="right">7,285,864</td>
<td align="right">2.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">57,144,805</td>
<td align="right">16.6%</td>
<td align="right">56,902,146</td>
<td align="right">16.7%</td>
<td align="right">-0.4%</td>
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
<td align="left">6,063</td>
<td align="right">22.2%</td>
<td align="left">6,090</td>
<td align="right">22.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">8,853</td>
<td align="right">32.4%</td>
<td align="left">9,055</td>
<td align="right">33.2%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">8,356</td>
<td align="right">30.6%</td>
<td align="left">8,212</td>
<td align="right">30.1%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,573</td>
<td align="right">9.4%</td>
<td align="left">2,626</td>
<td align="right">9.6%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,383</td>
<td align="right">5.1%</td>
<td align="left">1,187</td>
<td align="right">4.4%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">100</td>
<td align="right">0.4%</td>
<td align="left">100</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="right">1,305</td>
<td align="right">3.8%</td>
<td align="right">1,307</td>
<td align="right">3.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">850</td>
<td align="right">2.5%</td>
<td align="right">968</td>
<td align="right">2.8%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,707</td>
<td align="right">16.6%</td>
<td align="right">5,701</td>
<td align="right">16.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,508</td>
<td align="right">30.5%</td>
<td align="right">10,452</td>
<td align="right">30.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">5,951</td>
<td align="right">17.3%</td>
<td align="right">5,950</td>
<td align="right">17.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">7,806</td>
<td align="right">22.7%</td>
<td align="right">7,801</td>
<td align="right">22.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,958</td>
<td align="right">5.7%</td>
<td align="right">1,962</td>
<td align="right">5.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">370</td>
<td align="right">1.1%</td>
<td align="right">370</td>
<td align="right">1.1%</td>
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
<td align="left"><= 4</td>
<td align="right">738</td>
<td align="right">2.1%</td>
<td align="right">740</td>
<td align="right">2.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">849</td>
<td align="right">2.5%</td>
<td align="right">962</td>
<td align="right">2.8%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">3,265</td>
<td align="right">9.5%</td>
<td align="right">3,314</td>
<td align="right">9.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">9,399</td>
<td align="right">27.3%</td>
<td align="right">9,411</td>
<td align="right">27.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">7,798</td>
<td align="right">22.6%</td>
<td align="right">7,586</td>
<td align="right">22.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,958</td>
<td align="right">8.6%</td>
<td align="right">2,935</td>
<td align="right">8.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,940</td>
<td align="right">5.6%</td>
<td align="right">2,017</td>
<td align="right">5.8%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">381</td>
<td align="right">1.1%</td>
<td align="right">305</td>
<td align="right">0.9%</td>
<td align="right">-19.9%</td>
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
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">114,155,056</td>
<td align="right">1,123,865,437</td>
<td align="right">884.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">954,953,847</td>
<td align="right">356,340</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">272,508,221</td>
<td align="right">3,106,080</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,560</td>
<td align="right">3,253,140</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,851,399,104</td>
<td align="right">11,121,301,152</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,166,363,504</td>
<td align="right">177,097,043</td>
<td align="right">-84.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,229,446,240</td>
<td align="right">219,283,584</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">72,133,697</td>
<td align="right">45,887,637</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,653,150,440</td>
<td align="right">1,244,467,483</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">1,067,908,160</td>
<td align="right">924,303,090</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">878,731</td>
<td align="right">764,994</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">258,134,434</td>
<td align="right">241,609,486</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,958,975,521</td>
<td align="right">1,910,771,554</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">2,544,700,429</td>
<td align="right">2,507,168,579</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">5,670,309</td>
<td align="right">5,607,603</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">41,820,095</td>
<td align="right">41,383,266</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,391,785</td>
<td align="right">5,335,556</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">20,106,368</td>
<td align="right">19,998,850</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">39,081,042,273</td>
<td align="right">39,254,036,644</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">33,045,985</td>
<td align="right">32,902,280</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">44,276,369,615</td>
<td align="right">44,450,364,085</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">771,680,613</td>
<td align="right">768,857,570</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">147,381,211</td>
<td align="right">147,900,400</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">262,381,078</td>
<td align="right">261,524,526</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">28,236,883</td>
<td align="right">28,153,456</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">120,710,609</td>
<td align="right">120,374,170</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,051,258,261</td>
<td align="right">3,059,747,648</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">3,063,702,947</td>
<td align="right">3,055,893,620</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">7,738,886</td>
<td align="right">7,757,214</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">154,988,615</td>
<td align="right">154,629,062</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">4,173,010,765</td>
<td align="right">4,163,975,562</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">12,723,354</td>
<td align="right">12,697,845</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">154,509,375</td>
<td align="right">154,202,211</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">228,508,437</td>
<td align="right">228,114,976</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">341,821,263</td>
<td align="right">341,273,104</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">369,228,924</td>
<td align="right">368,680,765</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">34,404,628</td>
<td align="right">34,353,632</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,528,926</td>
<td align="right">5,536,642</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">45,436,809</td>
<td align="right">45,374,103</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">103,873,342</td>
<td align="right">103,734,993</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">168,733,395</td>
<td align="right">168,525,149</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">447,091,136</td>
<td align="right">446,553,996</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">448,534,942</td>
<td align="right">447,997,802</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,084,812,237</td>
<td align="right">1,083,538,950</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">57,769,005</td>
<td align="right">57,704,825</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">832,281,900</td>
<td align="right">833,070,352</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">333,631,856</td>
<td align="right">333,325,676</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,223,153,365</td>
<td align="right">1,224,274,714</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">411,244,985</td>
<td align="right">411,621,229</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,509,889,264</td>
<td align="right">1,511,005,353</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,510,068,896</td>
<td align="right">1,511,184,985</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">76,615,955</td>
<td align="right">76,667,007</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">34,840,447</td>
<td align="right">34,817,338</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">736,570,212</td>
<td align="right">736,126,062</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">156,942,265</td>
<td align="right">156,849,573</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">308,751,850</td>
<td align="right">308,588,802</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,882,202,777</td>
<td align="right">3,880,233,154</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">564,625,085</td>
<td align="right">564,348,274</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,389,060,935</td>
<td align="right">2,387,897,621</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">440,990,245</td>
<td align="right">440,778,203</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,123,332,009</td>
<td align="right">1,122,796,325</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">339,426,739</td>
<td align="right">339,274,562</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">176,098,966</td>
<td align="right">176,020,136</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,296,690,445</td>
<td align="right">1,297,210,035</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">58,384,728</td>
<td align="right">58,362,620</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,219,418,513</td>
<td align="right">1,218,966,200</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">673,350,485</td>
<td align="right">673,107,049</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">504,734,136</td>
<td align="right">504,554,839</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,306,864,423</td>
<td align="right">1,306,412,148</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,319,412,514</td>
<td align="right">1,318,960,239</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,319,412,514</td>
<td align="right">1,318,960,239</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,200,515,022</td>
<td align="right">1,200,911,715</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,266,619,201</td>
<td align="right">1,267,005,888</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">38,303,420</td>
<td align="right">38,314,032</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,480,729,653</td>
<td align="right">1,481,126,346</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,004,826,358</td>
<td align="right">1,004,574,200</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,005,055,758</td>
<td align="right">1,004,803,600</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">105,638,004</td>
<td align="right">105,612,483</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,852,886,528</td>
<td align="right">1,852,450,348</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">43,815,036</td>
<td align="right">43,825,036</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,755,185,692</td>
<td align="right">1,754,832,396</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,469,427,249</td>
<td align="right">4,468,616,655</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,629,318,684</td>
<td align="right">3,628,720,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,459,667,261</td>
<td align="right">2,460,051,343</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,142,932,848</td>
<td align="right">1,142,762,308</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,067,901,782</td>
<td align="right">2,068,185,939</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">245,148,219</td>
<td align="right">245,180,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">664,540,523</td>
<td align="right">664,456,662</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">532,793,231</td>
<td align="right">532,727,662</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">67,072,128</td>
<td align="right">67,064,123</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,494,180,790</td>
<td align="right">1,494,016,231</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">200,321,931</td>
<td align="right">200,343,933</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,623,152,615</td>
<td align="right">1,622,988,056</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">103,828,216</td>
<td align="right">103,838,216</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">310,293,936</td>
<td align="right">310,266,133</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">863,719,144</td>
<td align="right">863,644,215</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">4,011,548,989</td>
<td align="right">4,011,886,258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">226,986,948</td>
<td align="right">226,968,205</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,012,032,949</td>
<td align="right">4,011,703,737</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,977,172,329</td>
<td align="right">3,976,866,226</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,864,311,910</td>
<td align="right">2,864,097,481</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">260,525,474</td>
<td align="right">260,507,721</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,452,133,210</td>
<td align="right">4,452,383,782</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">7,173,173,393</td>
<td align="right">7,173,575,097</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,802,176,578</td>
<td align="right">1,802,082,253</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,346,191,222</td>
<td align="right">1,346,125,877</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">392,976,902</td>
<td align="right">392,958,159</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">416,657,376</td>
<td align="right">416,676,883</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,998,492,846</td>
<td align="right">1,998,416,293</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,067,132,660</td>
<td align="right">1,067,094,968</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">726,964,002</td>
<td align="right">726,987,632</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">548,011,061</td>
<td align="right">547,993,256</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">798,863,085</td>
<td align="right">798,837,573</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,545,515</td>
<td align="right">1,545,555</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">601,221,417</td>
<td align="right">601,209,229</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">393,012,356</td>
<td align="right">393,006,555</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">924,300,400</td>
<td align="right">924,288,230</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,846,997,306</td>
<td align="right">1,846,974,389</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,221,661,935</td>
<td align="right">2,221,639,000</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,025,486</td>
<td align="right">40,025,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,471,700,210</td>
<td align="right">6,471,755,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,900,834,195</td>
<td align="right">3,900,859,646</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,992,229,404</td>
<td align="right">7,992,252,030</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,007,725,322</td>
<td align="right">1,007,722,528</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">176,728,025</td>
<td align="right">176,727,665</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,940,415</td>
<td align="right">47,940,453</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">48,050,965</td>
<td align="right">48,051,003</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">78,980,938</td>
<td align="right">78,980,976</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">499,092,964</td>
<td align="right">499,093,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">101,635,779</td>
<td align="right">101,635,761</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">101,635,779</td>
<td align="right">101,635,761</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">101,839,479</td>
<td align="right">101,839,461</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">311,428,917</td>
<td align="right">311,428,955</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,492</td>
<td align="right">70,350,486</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,492</td>
<td align="right">70,350,486</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">148,541,741</td>
<td align="right">148,541,743</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,872,957,194</td>
<td align="right">2,872,957,176</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,110,554,207</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,279,292,730</td>
<td align="right">2,279,292,730</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,345,747,554</td>
<td align="right">1,345,747,554</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,224,636,230</td>
<td align="right">1,224,636,230</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,187,119,480</td>
<td align="right">1,187,119,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">982,981,357</td>
<td align="right">982,981,357</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">976,177,596</td>
<td align="right">976,177,596</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">809,781,769</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">681,989,457</td>
<td align="right">681,989,457</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">646,998,023</td>
<td align="right">646,998,023</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">597,053,787</td>
<td align="right">597,053,787</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">585,073,171</td>
<td align="right">585,073,171</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">498,487,103</td>
<td align="right">498,487,103</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">469,792,122</td>
<td align="right">469,792,122</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">455,387,721</td>
<td align="right">455,387,721</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">455,387,721</td>
<td align="right">455,387,721</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">445,753,959</td>
<td align="right">445,753,959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">445,753,959</td>
<td align="right">445,753,959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">434,026,688</td>
<td align="right">434,026,688</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">419,919,993</td>
<td align="right">419,919,993</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">359,475,385</td>
<td align="right">359,475,385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">358,301,634</td>
<td align="right">358,301,634</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">263,905,177</td>
<td align="right">263,905,177</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">259,316,734</td>
<td align="right">259,316,734</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">179,606,886</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">169,308,989</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">155,264,215</td>
<td align="right">155,264,215</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">143,590,077</td>
<td align="right">143,590,077</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">131,031,817</td>
<td align="right">131,031,817</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">118,700,859</td>
<td align="right">118,700,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,492,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">103,178,820</td>
<td align="right">103,178,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">83,482,983</td>
<td align="right">83,482,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,770,000</td>
<td align="right">73,770,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">61,669,521</td>
<td align="right">61,669,521</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,013,180</td>
<td align="right">60,013,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">55,838,776</td>
<td align="right">55,838,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">53,395,255</td>
<td align="right">53,395,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">53,395,255</td>
<td align="right">53,395,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">49,872,511</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">49,308,441</td>
<td align="right">49,308,441</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,560</td>
<td align="right">47,660,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,079</td>
<td align="right">47,071,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,593,190</td>
<td align="right">46,593,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,582,286</td>
<td align="right">43,582,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">40,614,624</td>
<td align="right">40,614,624</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">39,846,840</td>
<td align="right">39,846,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">37,152,077</td>
<td align="right">37,152,077</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">35,379,527</td>
<td align="right">35,379,527</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">31,188,233</td>
<td align="right">31,188,233</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">30,896,592</td>
<td align="right">30,896,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">30,896,592</td>
<td align="right">30,896,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">24,484,641</td>
<td align="right">24,484,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">24,484,641</td>
<td align="right">24,484,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">20,612,164</td>
<td align="right">20,612,164</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,548,091</td>
<td align="right">12,548,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,548,091</td>
<td align="right">12,548,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">11,165,748</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">8,323,320</td>
<td align="right">8,323,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">7,953,793</td>
<td align="right">7,953,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">7,289,860</td>
<td align="right">7,289,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,159,872</td>
<td align="right">6,159,872</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">5,718,540</td>
<td align="right">5,718,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,635,678</td>
<td align="right">4,635,678</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">4,208,676</td>
<td align="right">4,208,676</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">3,709,046</td>
<td align="right">3,709,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right">3,555,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,366,565</td>
<td align="right">3,366,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,034,740</td>
<td align="right">3,034,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,975,980</td>
<td align="right">2,975,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,975,980</td>
<td align="right">2,975,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,678,400</td>
<td align="right">2,678,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">2,351,667</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,329,634</td>
<td align="right">1,329,634</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">229,826</td>
<td align="right">229,826</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">143,096</td>
<td align="right">143,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">27,762</td>
<td align="right">27,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">26,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">20,173</td>
<td align="right">20,173</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">15,603</td>
<td align="right">15,603</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_CALL_TWO_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,285</td>
<td align="right">9,285</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right"></td>
<td align="right">1,407,387,258</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right"></td>
<td align="right">259,907,176</td>
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
<td align="right">23,863</td>
<td align="right">23,841</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right">23,001</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,824</td>
<td align="right">1,824</td>
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
<td align="right">101</td>
<td align="right">101</td>
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
<td align="right">101</td>
<td align="right">101</td>
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
<td align="right">2,439</td>
<td align="right">2,439</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-05-21
