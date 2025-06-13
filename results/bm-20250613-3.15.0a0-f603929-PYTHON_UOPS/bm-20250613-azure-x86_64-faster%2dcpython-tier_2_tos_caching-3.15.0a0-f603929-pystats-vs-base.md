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
<td align="left">CONVERT_VALUE</td>
<td align="right">74,958,676</td>
<td align="right">60</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,140</td>
<td align="right">63</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">52,114,074</td>
<td align="right">3,268</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,718,454</td>
<td align="right">2,340</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,286,173</td>
<td align="right">25,744</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,232,478</td>
<td align="right">250</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,796</td>
<td align="right">2,220</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,603,016</td>
<td align="right">3,325</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">17,972,383</td>
<td align="right">6,894</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">54,908,720</td>
<td align="right">26,464</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">441,321</td>
<td align="right">420</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">73,076,838</td>
<td align="right">78,120</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,347,766</td>
<td align="right">7,890</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">56,998</td>
<td align="right">131</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,864</td>
<td align="right">9</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,577</td>
<td align="right">240</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,550</td>
<td align="right">9</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,072</td>
<td align="right">3</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">268,629,587</td>
<td align="right">1,200,258</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,262,318</td>
<td align="right">7,163</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">271,728,629</td>
<td align="right">1,560,355</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,221</td>
<td align="right">89,380</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">80,287,906</td>
<td align="right">529,418</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">969,630</td>
<td align="right">6,503</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">64,366,589</td>
<td align="right">556,745</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">40,691,948</td>
<td align="right">528,379</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">2,550,451</td>
<td align="right">38,487</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">254,503,712</td>
<td align="right">4,299,977</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,149,961</td>
<td align="right">191,312</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,274,683</td>
<td align="right">1,381,513</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">162,386,111</td>
<td align="right">3,794,232</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">129,345,980</td>
<td align="right">3,383,847</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">13,034,071</td>
<td align="right">347,064</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">233,477,084</td>
<td align="right">6,481,583</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,443</td>
<td align="right">1,240,802</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">116,403,992</td>
<td align="right">3,684,591</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">457,943,766</td>
<td align="right">15,926,336</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">358,519,181</td>
<td align="right">12,632,033</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,279,323</td>
<td align="right">2,214,588</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">44,030,107</td>
<td align="right">1,615,416</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">798,533,159</td>
<td align="right">31,665,885</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">82,017,310</td>
<td align="right">3,532,862</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">874,197,308</td>
<td align="right">40,223,668</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">183,839,385</td>
<td align="right">8,533,582</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">522,186,324</td>
<td align="right">24,637,583</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">162,560,788</td>
<td align="right">7,712,161</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">65,526,177</td>
<td align="right">3,248,276</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">49,990,172</td>
<td align="right">2,579,266</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">114,765,160</td>
<td align="right">6,122,074</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">55,798,442</td>
<td align="right">3,065,230</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">373,956,451</td>
<td align="right">21,446,694</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,092,572,030</td>
<td align="right">67,676,483</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">867,170,138</td>
<td align="right">56,952,547</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,402,934</td>
<td align="right">7,583,934</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">169,303,818</td>
<td align="right">11,947,629</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,679,210</td>
<td align="right">191,755</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,641,482</td>
<td align="right">5,153,829</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">349,298,693</td>
<td align="right">26,824,252</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">604,271,149</td>
<td align="right">48,944,306</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">286,041,978</td>
<td align="right">23,430,883</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">118,543,838</td>
<td align="right">10,092,176</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">189,786,970</td>
<td align="right">16,853,297</td>
<td align="right">-91.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">538,127,136</td>
<td align="right">48,291,718</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">432,690,820</td>
<td align="right">39,834,355</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">104,795,573</td>
<td align="right">10,159,802</td>
<td align="right">-90.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">894,839,173</td>
<td align="right">89,029,070</td>
<td align="right">-90.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">641,479,631</td>
<td align="right">63,891,625</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">87,062,973</td>
<td align="right">8,680,661</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">673,171,881</td>
<td align="right">69,302,921</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,420,406,803</td>
<td align="right">148,330,105</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,076,778,643</td>
<td align="right">119,866,105</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">123,859,732</td>
<td align="right">14,534,280</td>
<td align="right">-88.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">125,748,042</td>
<td align="right">14,865,859</td>
<td align="right">-88.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">178,066,353</td>
<td align="right">21,181,040</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">214,350</td>
<td align="right">25,683</td>
<td align="right">-88.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">880,302,022</td>
<td align="right">109,396,412</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,195,069,163</td>
<td align="right">279,972,795</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">822,836,527</td>
<td align="right">105,290,306</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">202,330,252</td>
<td align="right">25,898,041</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,861,740,651</td>
<td align="right">638,057,705</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,678,005,225</td>
<td align="right">483,583,808</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">133,868,270</td>
<td align="right">17,680,755</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">37,732,689</td>
<td align="right">4,990,465</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,617,554,421</td>
<td align="right">613,658,818</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">162,027,382</td>
<td align="right">21,592,478</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">331,417,936</td>
<td align="right">44,981,910</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">69,402,913</td>
<td align="right">9,481,713</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">196,772,668</td>
<td align="right">27,376,023</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">35,963,045</td>
<td align="right">5,064,055</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">118,602,055</td>
<td align="right">16,703,045</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,859,643,520</td>
<td align="right">548,402,880</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,578,224</td>
<td align="right">2,644,756</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">243,807,768</td>
<td align="right">35,720,009</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">203,562,415</td>
<td align="right">29,833,139</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">259,742,472</td>
<td align="right">38,141,461</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">281,149,239</td>
<td align="right">41,437,790</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">468,452,801</td>
<td align="right">69,092,050</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">241,759,011</td>
<td align="right">35,719,888</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">238,375,811</td>
<td align="right">35,709,101</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">857,467,649</td>
<td align="right">129,115,947</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,054,390,043</td>
<td align="right">619,192,656</td>
<td align="right">-84.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">367,418,677</td>
<td align="right">56,124,472</td>
<td align="right">-84.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">152,289,325</td>
<td align="right">23,336,759</td>
<td align="right">-84.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">487,021,873</td>
<td align="right">74,815,792</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">15,967,479,151</td>
<td align="right">2,472,571,665</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,574</td>
<td align="right">399</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">27,120,971</td>
<td align="right">4,249,353</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">95,672,079</td>
<td align="right">15,183,058</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,569,544,290</td>
<td align="right">250,856,605</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">835,668,112</td>
<td align="right">135,714,187</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">239,372,269</td>
<td align="right">39,619,401</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,919,478,341</td>
<td align="right">322,133,198</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">86,014,864</td>
<td align="right">14,557,176</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,146,582,398</td>
<td align="right">545,919,706</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,772,405</td>
<td align="right">3,667,771</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,772,426</td>
<td align="right">3,667,793</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,407,743,651</td>
<td align="right">427,770,674</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">873,254,751</td>
<td align="right">155,788,746</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,445,657</td>
<td align="right">3,667,850</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">222,134,439</td>
<td align="right">40,287,878</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">637,396,707</td>
<td align="right">117,225,496</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">360,187,229</td>
<td align="right">66,667,336</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,970,243,429</td>
<td align="right">369,504,919</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">340,238,259</td>
<td align="right">64,005,501</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">436,933,408</td>
<td align="right">83,100,304</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,165,329</td>
<td align="right">1,180,889</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">212,873,625</td>
<td align="right">41,922,786</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,834,035</td>
<td align="right">36,014,113</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">873,532,301</td>
<td align="right">179,871,372</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">145,966,113</td>
<td align="right">30,575,386</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">115,250,208</td>
<td align="right">24,615,009</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">67,452,772</td>
<td align="right">14,427,204</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,977,554,721</td>
<td align="right">439,018,228</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">159,561,281</td>
<td align="right">35,740,828</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">34,372,295</td>
<td align="right">8,085,437</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,555,018,806</td>
<td align="right">606,935,938</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,887,030,661</td>
<td align="right">1,181,017,800</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,000,048,582</td>
<td align="right">255,908,906</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">602,500,565</td>
<td align="right">161,852,463</td>
<td align="right">-73.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">67,255,642</td>
<td align="right">18,163,621</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">51,507,100</td>
<td align="right">14,093,252</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,784,349</td>
<td align="right">1,042,171</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,359,352</td>
<td align="right">1,200,767</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,974,448</td>
<td align="right">7,705,970</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">39,277,519</td>
<td align="right">11,136,976</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">436,740,701</td>
<td align="right">137,549,701</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,995,020</td>
<td align="right">3,225,764</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">103,584,058</td>
<td align="right">33,729,479</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">103,659,396</td>
<td align="right">34,752,165</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">299,279,521</td>
<td align="right">100,378,216</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">76,368,393</td>
<td align="right">25,927,061</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,288,385</td>
<td align="right">1,857,769</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">13,028</td>
<td align="right">4,877</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,704,339</td>
<td align="right">4,782,754</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">248,086</td>
<td align="right">95,287</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">104,947,997</td>
<td align="right">41,259,382</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">10,549,274</td>
<td align="right">4,329,774</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,362</td>
<td align="right">2,216</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,082,492</td>
<td align="right">67,921,387</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">366,826,998</td>
<td align="right">161,574,087</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">225,571,477</td>
<td align="right">102,963,117</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">429,619,119</td>
<td align="right">198,745,798</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,387,011</td>
<td align="right">17,223,487</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,700</td>
<td align="right">16,866</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,090,757</td>
<td align="right">1,690,136</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,066,787,388</td>
<td align="right">604,047,331</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">171,175,315</td>
<td align="right">101,155,771</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">149,777,011</td>
<td align="right">94,539,216</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">25,335,102</td>
<td align="right">16,170,285</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,342,581</td>
<td align="right">1,519,215</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,866,865</td>
<td align="right">3,225,556</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,547,045</td>
<td align="right">24,000,304</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">118,071,625</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,749</td>
<td align="right">100,683,821</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,244,074</td>
<td align="right">236,208,449</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,602,918</td>
<td align="right">495,040,881</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">119,485,933</td>
<td align="right">101,620,103</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,439,117</td>
<td align="right">358,983,582</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">UNPACK_EX</td>
<td align="right">117,444</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,564</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,551</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,970</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">7,744</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">176</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">25</td>
<td align="right"></td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">55,486,435</td>
<td align="right">1.1%</td>
<td align="right">1,732</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,076,297,386</td>
<td align="right">21.3%</td>
<td align="right">119,824,903</td>
<td align="right">10.7%</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,929,559,572</td>
<td align="right">77.6%</td>
<td align="right">996,226,956</td>
<td align="right">89.3%</td>
<td align="right">-74.6%</td>
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
<td align="right">1,065,165</td>
<td align="right">69.7%</td>
<td align="right">5,052</td>
<td align="right">12.3%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">462,793</td>
<td align="right">30.3%</td>
<td align="right">36,176</td>
<td align="right">87.7%</td>
<td align="right">-92.2%</td>
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
<td align="left">subscr tuple slice</td>
<td align="right">107,939</td>
<td align="right">23.3%</td>
<td align="right">164</td>
<td align="right">0.5%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">16,343</td>
<td align="right">3.5%</td>
<td align="right">136</td>
<td align="right">0.4%</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,336</td>
<td align="right">0.5%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,464</td>
<td align="right">4.0%</td>
<td align="right">169</td>
<td align="right">0.5%</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">11,553</td>
<td align="right">2.5%</td>
<td align="right">158</td>
<td align="right">0.4%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,300</td>
<td align="right">1.8%</td>
<td align="right">179</td>
<td align="right">0.5%</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,194</td>
<td align="right">1.3%</td>
<td align="right">140</td>
<td align="right">0.4%</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">22,385</td>
<td align="right">4.8%</td>
<td align="right">588</td>
<td align="right">1.6%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">36,083</td>
<td align="right">7.8%</td>
<td align="right">1,597</td>
<td align="right">4.4%</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">40,933</td>
<td align="right">8.8%</td>
<td align="right">2,122</td>
<td align="right">5.9%</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21,785</td>
<td align="right">4.7%</td>
<td align="right">1,537</td>
<td align="right">4.2%</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">6,953</td>
<td align="right">1.5%</td>
<td align="right">600</td>
<td align="right">1.7%</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">0.4%</td>
<td align="right">278</td>
<td align="right">0.8%</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,862</td>
<td align="right">4.3%</td>
<td align="right">3,498</td>
<td align="right">9.7%</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">1,810</td>
<td align="right">0.4%</td>
<td align="right">460</td>
<td align="right">1.3%</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,695</td>
<td align="right">1.4%</td>
<td align="right">2,020</td>
<td align="right">5.6%</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,768</td>
<td align="right">0.6%</td>
<td align="right">987</td>
<td align="right">2.7%</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">559</td>
<td align="right">1.5%</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,350</td>
<td align="right">0.5%</td>
<td align="right">1,320</td>
<td align="right">3.6%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">25,835</td>
<td align="right">5.6%</td>
<td align="right">16,459</td>
<td align="right">45.5%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,165</td>
<td align="right">0.7%</td>
<td align="right">2,921</td>
<td align="right">8.1%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">63,013</td>
<td align="right">13.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">28,692</td>
<td align="right">6.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,130</td>
<td align="right">0.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">631</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">334</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">326</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr structtime</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">182,834,035</td>
<td align="right">100.0%</td>
<td align="right">36,014,113</td>
<td align="right">100.0%</td>
<td align="right">-80.3%</td>
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
<td align="right">150,347,215</td>
<td align="right">2.9%</td>
<td align="right">6,400,090</td>
<td align="right">0.8%</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">147,584,808</td>
<td align="right">2.8%</td>
<td align="right">6,318,400</td>
<td align="right">0.8%</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,059,714,812</td>
<td align="right">97.1%</td>
<td align="right">756,109,531</td>
<td align="right">99.1%</td>
<td align="right">-85.1%</td>
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
<td align="right">3,010,347</td>
<td align="right">100.0%</td>
<td align="right">176,915</td>
<td align="right">100.0%</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">62</td>
<td align="right">0.0%</td>
<td align="right">-57.5%</td>
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
<td align="right">44</td>
<td align="right">71.0%</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">287</td>
<td align="right">196.6%</td>
<td align="right">43</td>
<td align="right">69.4%</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">146</td>
<td align="right">100.0%</td>
<td align="right">62</td>
<td align="right">100.0%</td>
<td align="right">-57.5%</td>
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
<td align="right">574,330</td>
<td align="right">96.6%</td>
<td align="right">2,106</td>
<td align="right">43.2%</td>
<td align="right">-99.6%</td>
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
<td align="right">97.8%</td>
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
<td align="right">20,322</td>
<td align="right">100.0%</td>
<td align="right">2,771</td>
<td align="right">100.0%</td>
<td align="right">-86.4%</td>
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
<td align="right">1,263,373</td>
<td align="right">0.1%</td>
<td align="right">7,828</td>
<td align="right">0.0%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,220,511,172</td>
<td align="right">93.3%</td>
<td align="right">192,467,201</td>
<td align="right">93.0%</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">85,892,935</td>
<td align="right">6.6%</td>
<td align="right">14,538,774</td>
<td align="right">7.0%</td>
<td align="right">-83.1%</td>
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
<td align="right">103,738</td>
<td align="right">71.3%</td>
<td align="right">6,544</td>
<td align="right">35.6%</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,713</td>
<td align="right">28.7%</td>
<td align="right">11,858</td>
<td align="right">64.4%</td>
<td align="right">-71.6%</td>
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
<td align="left">baseobject</td>
<td align="right">4,519</td>
<td align="right">4.4%</td>
<td align="right">6</td>
<td align="right">0.1%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,086</td>
<td align="right">22.3%</td>
<td align="right">136</td>
<td align="right">2.1%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,095</td>
<td align="right">3.9%</td>
<td align="right">67</td>
<td align="right">1.0%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">998</td>
<td align="right">1.0%</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,905</td>
<td align="right">1.8%</td>
<td align="right">85</td>
<td align="right">1.3%</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,722</td>
<td align="right">7.4%</td>
<td align="right">390</td>
<td align="right">6.0%</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">43,293</td>
<td align="right">41.7%</td>
<td align="right">2,235</td>
<td align="right">34.2%</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,649</td>
<td align="right">8.3%</td>
<td align="right">2,544</td>
<td align="right">38.9%</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,278</td>
<td align="right">1.2%</td>
<td align="right">1,060</td>
<td align="right">16.2%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">7.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">371</td>
<td align="right">0.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">430,287,179</td>
<td align="right">83.1%</td>
<td align="right">4,970,490</td>
<td align="right">36.3%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">728,519</td>
<td align="right">0.1%</td>
<td align="right">24,000</td>
<td align="right">0.2%</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">87,018,646</td>
<td align="right">16.8%</td>
<td align="right">8,676,852</td>
<td align="right">63.4%</td>
<td align="right">-90.0%</td>
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
<td align="right">16,053</td>
<td align="right">27.6%</td>
<td align="right">575</td>
<td align="right">13.5%</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">42,017</td>
<td align="right">72.4%</td>
<td align="right">3,694</td>
<td align="right">86.5%</td>
<td align="right">-91.2%</td>
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
<td align="right">12,009</td>
<td align="right">28.6%</td>
<td align="right">495</td>
<td align="right">13.4%</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,498</td>
<td align="right">25.0%</td>
<td align="right">739</td>
<td align="right">20.0%</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">10,194</td>
<td align="right">24.3%</td>
<td align="right">1,130</td>
<td align="right">30.6%</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,316</td>
<td align="right">22.2%</td>
<td align="right">1,330</td>
<td align="right">36.0%</td>
<td align="right">-85.7%</td>
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
<td align="right">61,985,893</td>
<td align="right">4.1%</td>
<td align="right">6,289</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">202,212,876</td>
<td align="right">13.3%</td>
<td align="right">25,887,973</td>
<td align="right">8.4%</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,250,944,642</td>
<td align="right">82.6%</td>
<td align="right">282,778,248</td>
<td align="right">91.6%</td>
<td align="right">-77.4%</td>
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
<td align="right">1,174,770</td>
<td align="right">91.3%</td>
<td align="right">2,107</td>
<td align="right">20.7%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">111,981</td>
<td align="right">8.7%</td>
<td align="right">8,058</td>
<td align="right">79.3%</td>
<td align="right">-92.8%</td>
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
<td align="left">dict items</td>
<td align="right">52,273</td>
<td align="right">46.7%</td>
<td align="right">130</td>
<td align="right">1.6%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">10,857</td>
<td align="right">9.7%</td>
<td align="right">148</td>
<td align="right">1.8%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,999</td>
<td align="right">11.6%</td>
<td align="right">206</td>
<td align="right">2.6%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,184</td>
<td align="right">3.7%</td>
<td align="right">139</td>
<td align="right">1.7%</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,308</td>
<td align="right">1.2%</td>
<td align="right">124</td>
<td align="right">1.5%</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">6,420</td>
<td align="right">5.7%</td>
<td align="right">947</td>
<td align="right">11.8%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">5,157</td>
<td align="right">4.6%</td>
<td align="right">1,034</td>
<td align="right">12.8%</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,376</td>
<td align="right">3.0%</td>
<td align="right">721</td>
<td align="right">8.9%</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,978</td>
<td align="right">1.8%</td>
<td align="right">700</td>
<td align="right">8.7%</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,293</td>
<td align="right">2.9%</td>
<td align="right">1,285</td>
<td align="right">15.9%</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">260</td>
<td align="right">0.2%</td>
<td align="right">120</td>
<td align="right">1.5%</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,390</td>
<td align="right">3.0%</td>
<td align="right">2,444</td>
<td align="right">30.3%</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">5,891</td>
<td align="right">5.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">248</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="left">bytes</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
<td align="right">120</td>
<td align="right">120 / 0 !!</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">1,787,494</td>
<td align="right">1,787,494 / 0 !!</td>
<td align="right">902</td>
<td align="right">902 / 0 !!</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,415,709</td>
<td align="right">101,415,709 / 0 !!</td>
<td align="right">448,627</td>
<td align="right">448,627 / 0 !!</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,163,929</td>
<td align="right">12,163,929 / 0 !!</td>
<td align="right">154,920</td>
<td align="right">154,920 / 0 !!</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,450,885</td>
<td align="right">341,450,885 / 0 !!</td>
<td align="right">10,201,629</td>
<td align="right">10,201,629 / 0 !!</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,492,984</td>
<td align="right">5,492,984 / 0 !!</td>
<td align="right">212,519</td>
<td align="right">212,519 / 0 !!</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">171,571,746</td>
<td align="right">171,571,746 / 0 !!</td>
<td align="right">7,892,681</td>
<td align="right">7,892,681 / 0 !!</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299,401,341</td>
<td align="right">299,401,341 / 0 !!</td>
<td align="right">17,434,067</td>
<td align="right">17,434,067 / 0 !!</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">112,166,681</td>
<td align="right">112,166,681 / 0 !!</td>
<td align="right">24,720,548</td>
<td align="right">24,720,548 / 0 !!</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,532,605</td>
<td align="right">34,532,605 / 0 !!</td>
<td align="right">16,777,065</td>
<td align="right">16,777,065 / 0 !!</td>
<td align="right">-51.4%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,005,161</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">609,066,413</td>
<td align="right">7.8%</td>
<td align="right">19,644,479</td>
<td align="right">1.9%</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">520,496,259</td>
<td align="right">6.7%</td>
<td align="right">24,548,929</td>
<td align="right">2.4%</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,678,462,263</td>
<td align="right">85.5%</td>
<td align="right">964,402,524</td>
<td align="right">95.6%</td>
<td align="right">-85.6%</td>
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
<td align="right">432,345</td>
<td align="right">3.6%</td>
<td align="right">13,666</td>
<td align="right">3.1%</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,577,787</td>
<td align="right">96.4%</td>
<td align="right">428,865</td>
<td align="right">96.9%</td>
<td align="right">-96.3%</td>
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
<td align="right">23,420</td>
<td align="right">5.4%</td>
<td align="right">205</td>
<td align="right">1.5%</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,065</td>
<td align="right">0.9%</td>
<td align="right">64</td>
<td align="right">0.5%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">47,277</td>
<td align="right">10.9%</td>
<td align="right">931</td>
<td align="right">6.8%</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,839</td>
<td align="right">0.4%</td>
<td align="right">71</td>
<td align="right">0.5%</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">35,464</td>
<td align="right">8.2%</td>
<td align="right">2,490</td>
<td align="right">18.2%</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,694</td>
<td align="right">0.4%</td>
<td align="right">155</td>
<td align="right">1.1%</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">13,841</td>
<td align="right">3.2%</td>
<td align="right">1,268</td>
<td align="right">9.3%</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">39,915</td>
<td align="right">9.2%</td>
<td align="right">3,937</td>
<td align="right">28.8%</td>
<td align="right">-90.1%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">743</td>
<td align="right">0.2%</td>
<td align="right">140</td>
<td align="right">1.0%</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,447</td>
<td align="right">1.0%</td>
<td align="right">915</td>
<td align="right">6.7%</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">573</td>
<td align="right">0.1%</td>
<td align="right">160</td>
<td align="right">1.2%</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">6,976</td>
<td align="right">1.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,378</td>
<td align="right">0.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">545</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">14,622,505</td>
<td align="right">0.3%</td>
<td align="right">39,351</td>
<td align="right">0.0%</td>
<td align="right">-99.7%</td>
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
<td align="right">226</td>
<td align="right">0.0%</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,377,935,860</td>
<td align="right">99.7%</td>
<td align="right">797,256,517</td>
<td align="right">100.0%</td>
<td align="right">-81.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">51,220</td>
<td align="right">0.0%</td>
<td align="right">19,076</td>
<td align="right">0.0%</td>
<td align="right">-62.8%</td>
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
<td align="right">138,467</td>
<td align="right">100.0%</td>
<td align="right">50,035</td>
<td align="right">100.0%</td>
<td align="right">-63.9%</td>
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
<td align="right">58,889,199</td>
<td align="right">100.0%</td>
<td align="right">4,755,366</td>
<td align="right">100.0%</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">204</td>
<td align="right">0.0%</td>
<td align="right">25</td>
<td align="right">0.0%</td>
<td align="right">-87.7%</td>
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
<td align="right">2,370</td>
<td align="right">100.0%</td>
<td align="right">374</td>
<td align="right">100.0%</td>
<td align="right">-84.2%</td>
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
<td align="right">128,816,951</td>
<td align="right">17.9%</td>
<td align="right">100,658,469</td>
<td align="right">16.9%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">591,588,207</td>
<td align="right">82.1%</td>
<td align="right">495,040,881</td>
<td align="right">83.1%</td>
<td align="right">-16.3%</td>
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
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">275</td>
<td align="right">1.1%</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">25,077</td>
<td align="right">98.9%</td>
<td align="right">-27.1%</td>
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
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">637</td>
<td align="right">2.5%</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">97.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right"></td>
<td align="right"></td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">105,399,402</td>
<td align="right">6.1%</td>
<td align="right">228,410</td>
<td align="right">0.1%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">61,194,359</td>
<td align="right">3.5%</td>
<td align="right">2,191,136</td>
<td align="right">1.2%</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,575,365,304</td>
<td align="right">90.4%</td>
<td align="right">187,228,441</td>
<td align="right">98.7%</td>
<td align="right">-88.1%</td>
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
<td align="right">2,029,406</td>
<td align="right">97.9%</td>
<td align="right">21,033</td>
<td align="right">76.4%</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43,659</td>
<td align="right">2.1%</td>
<td align="right">6,493</td>
<td align="right">23.6%</td>
<td align="right">-85.1%</td>
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
<td align="left">split dict</td>
<td align="right">3,737</td>
<td align="right">8.6%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">240,691</td>
<td align="right">551.3%</td>
<td align="right">838</td>
<td align="right">12.9%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,275</td>
<td align="right">2.9%</td>
<td align="right">22</td>
<td align="right">0.3%</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,635</td>
<td align="right">10.6%</td>
<td align="right">104</td>
<td align="right">1.6%</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">747</td>
<td align="right">1.7%</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,227</td>
<td align="right">16.6%</td>
<td align="right">940</td>
<td align="right">14.5%</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">19,647</td>
<td align="right">45.0%</td>
<td align="right">3,220</td>
<td align="right">49.6%</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">379</td>
<td align="right">0.9%</td>
<td align="right">104</td>
<td align="right">1.6%</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,346</td>
<td align="right">7.7%</td>
<td align="right">1,481</td>
<td align="right">22.8%</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">363</td>
<td align="right">0.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">1,232,478</td>
<td align="right">100.0%</td>
<td align="right">250</td>
<td align="right">100.0%</td>
<td align="right">-100.0%</td>
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
<td align="right">214,271,914</td>
<td align="right">67.4%</td>
<td align="right">31,886,103</td>
<td align="right">48.6%</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">103,545,749</td>
<td align="right">32.6%</td>
<td align="right">33,720,259</td>
<td align="right">51.4%</td>
<td align="right">-67.4%</td>
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
<td align="right">2,204</td>
<td align="right">5.7%</td>
<td align="right">180</td>
<td align="right">2.0%</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">36,145</td>
<td align="right">94.3%</td>
<td align="right">9,040</td>
<td align="right">98.0%</td>
<td align="right">-75.0%</td>
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
<td align="right">273</td>
<td align="right">0.8%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,991</td>
<td align="right">8.3%</td>
<td align="right">45</td>
<td align="right">0.5%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,164</td>
<td align="right">47.5%</td>
<td align="right">1,193</td>
<td align="right">13.2%</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">3,323</td>
<td align="right">9.2%</td>
<td align="right">600</td>
<td align="right">6.6%</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">10,483</td>
<td align="right">29.0%</td>
<td align="right">5,953</td>
<td align="right">65.9%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">4.7%</td>
<td align="right">1,180</td>
<td align="right">13.1%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">162</td>
<td align="right">0.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">68</td>
<td align="right">0.8%</td>
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
<td align="right">125,238,835</td>
<td align="right">4.4%</td>
<td align="right">14,832,936</td>
<td align="right">4.0%</td>
<td align="right">-88.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,646,974,892</td>
<td align="right">93.4%</td>
<td align="right">323,986,804</td>
<td align="right">88.1%</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">60,863,833</td>
<td align="right">2.1%</td>
<td align="right">29,103,617</td>
<td align="right">7.9%</td>
<td align="right">-52.2%</td>
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
<td align="right">458,023</td>
<td align="right">27.7%</td>
<td align="right">12,742</td>
<td align="right">2.2%</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,198,051</td>
<td align="right">72.3%</td>
<td align="right">569,146</td>
<td align="right">97.8%</td>
<td align="right">-52.5%</td>
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
<td align="right">38,938</td>
<td align="right">8.5%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">51,853</td>
<td align="right">11.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">74,367</td>
<td align="right">16.2%</td>
<td align="right">2,272</td>
<td align="right">17.8%</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,059</td>
<td align="right">2.2%</td>
<td align="right">324</td>
<td align="right">2.5%</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">9,739</td>
<td align="right">2.1%</td>
<td align="right">2,595</td>
<td align="right">20.4%</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">8,710</td>
<td align="right">1.9%</td>
<td align="right">2,711</td>
<td align="right">21.3%</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,655</td>
<td align="right">1.0%</td>
<td align="right">3,300</td>
<td align="right">25.9%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,860</td>
<td align="right">56.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">1,420</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">1,251,596</td>
<td align="right">0.2%</td>
<td align="right">3,170</td>
<td align="right">0.0%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">644,122,032</td>
<td align="right">99.8%</td>
<td align="right">25,979,133</td>
<td align="right">100.0%</td>
<td align="right">-96.0%</td>
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
<td align="right">785</td>
<td align="right">7.3%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,017</td>
<td align="right">92.7%</td>
<td align="right">3,991</td>
<td align="right">99.9%</td>
<td align="right">-60.2%</td>
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
<td align="right">136</td>
<td align="right">17.3%</td>
<td align="right">2</td>
<td align="right">100.0%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">551</td>
<td align="right">70.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">12.5%</td>
<td align="right"></td>
<td align="right"></td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,045,955,731</td>
<td align="right">1.1%</td>
<td align="right">55,446,984</td>
<td align="right">0.3%</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">3,132,316,104</td>
<td align="right">3.2%</td>
<td align="right">429,636,500</td>
<td align="right">2.6%</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">57,640,487,888</td>
<td align="right">59.7%</td>
<td align="right">9,705,330,099</td>
<td align="right">58.1%</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">34,767,182,095</td>
<td align="right">36.0%</td>
<td align="right">6,508,844,068</td>
<td align="right">39.0%</td>
<td align="right">-81.3%</td>
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
<td align="left">CALL</td>
<td align="right">147,584,808</td>
<td align="right">5.4%</td>
<td align="right">6,318,400</td>
<td align="right">1.6%</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">520,496,259</td>
<td align="right">19.0%</td>
<td align="right">24,548,929</td>
<td align="right">6.3%</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">87,018,646</td>
<td align="right">3.2%</td>
<td align="right">8,676,852</td>
<td align="right">2.2%</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,076,297,386</td>
<td align="right">39.3%</td>
<td align="right">119,824,903</td>
<td align="right">30.9%</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">125,238,835</td>
<td align="right">4.6%</td>
<td align="right">14,832,936</td>
<td align="right">3.8%</td>
<td align="right">-88.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">202,212,876</td>
<td align="right">7.4%</td>
<td align="right">25,887,973</td>
<td align="right">6.7%</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">85,892,935</td>
<td align="right">3.1%</td>
<td align="right">14,538,774</td>
<td align="right">3.8%</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,834,035</td>
<td align="right">6.7%</td>
<td align="right">36,014,113</td>
<td align="right">9.3%</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">103,545,749</td>
<td align="right">3.8%</td>
<td align="right">33,720,259</td>
<td align="right">8.7%</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,951</td>
<td align="right">4.7%</td>
<td align="right">100,658,469</td>
<td align="right">26.0%</td>
<td align="right">-21.9%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">80,748,983</td>
<td align="right">7.7%</td>
<td align="right">38,077</td>
<td align="right">0.1%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">176,356,606</td>
<td align="right">16.9%</td>
<td align="right">6,673,354</td>
<td align="right">12.0%</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">219,500,145</td>
<td align="right">21.0%</td>
<td align="right">12,767,992</td>
<td align="right">23.0%</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">53,362,084</td>
<td align="right">5.1%</td>
<td align="right">3,295,827</td>
<td align="right">5.9%</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">29,486,739</td>
<td align="right">2.8%</td>
<td align="right">14,547,578</td>
<td align="right">26.2%</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">25,638,582</td>
<td align="right">2.5%</td>
<td align="right">14,548,334</td>
<td align="right">26.2%</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">89,007,734</td>
<td align="right">8.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">77,872,997</td>
<td align="right">7.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,963,039</td>
<td align="right">3.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">30,946,306</td>
<td align="right">3.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2,052,290</td>
<td align="right">3.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,025,593</td>
<td align="right">1.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">219,860</td>
<td align="right">0.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">128,507</td>
<td align="right">0.2%</td>
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
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,898</td>
<td align="right">2.0%</td>
<td align="right">2,390,986</td>
<td align="right">0.2%</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">258,591,170</td>
<td align="right">3.9%</td>
<td align="right">9,974,037</td>
<td align="right">0.7%</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">996,748,617</td>
<td align="right">15.2%</td>
<td align="right">79,618,902</td>
<td align="right">5.9%</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">998,880,743</td>
<td align="right">15.2%</td>
<td align="right">81,038,043</td>
<td align="right">6.0%</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,336,369,234</td>
<td align="right">81.3%</td>
<td align="right">617,010,654</td>
<td align="right">45.8%</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,638,873</td>
<td align="right">1.1%</td>
<td align="right">9,884,566</td>
<td align="right">0.7%</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">271,433,267</td>
<td align="right">4.1%</td>
<td align="right">38,505,332</td>
<td align="right">2.9%</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,574,031,908</td>
<td align="right">24.0%</td>
<td align="right">250,859,571</td>
<td align="right">18.6%</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,574,031,908</td>
<td align="right">24.0%</td>
<td align="right">250,859,571</td>
<td align="right">18.6%</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,986,580,040</td>
<td align="right">76.0%</td>
<td align="right">1,095,671,201</td>
<td align="right">81.4%</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">575,151,165</td>
<td align="right">8.8%</td>
<td align="right">169,821,528</td>
<td align="right">12.6%</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,551,023</td>
<td align="right">0.4%</td>
<td align="right">7,249,953</td>
<td align="right">0.5%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,262</td>
<td align="right">0.0%</td>
<td align="right">1,419,132</td>
<td align="right">0.1%</td>
<td align="right">-33.3%</td>
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
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">306,771</td>
<td align="right">0.2%</td>
<td align="right">638</td>
<td align="right">0.0%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">5,330,627</td>
<td align="right"></td>
<td align="right">15,018</td>
<td align="right"></td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">57,197,003</td>
<td align="right"></td>
<td align="right">1,606,567</td>
<td align="right"></td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">52,671,529</td>
<td align="right"></td>
<td align="right">1,607,235</td>
<td align="right"></td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,147,865,471</td>
<td align="right"></td>
<td align="right">123,451,379</td>
<td align="right"></td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,406,006,192</td>
<td align="right"></td>
<td align="right">187,844,029</td>
<td align="right"></td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,364,165</td>
<td align="right">0.0%</td>
<td align="right">503,175</td>
<td align="right">0.0%</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,560,720,837</td>
<td align="right">22.8%</td>
<td align="right">2,094,831,449</td>
<td align="right">18.3%</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">39,018,058,711</td>
<td align="right">43.1%</td>
<td align="right">3,574,281,053</td>
<td align="right">39.6%</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">22,504,217,854</td>
<td align="right">24.8%</td>
<td align="right">2,239,690,604</td>
<td align="right">24.8%</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">24,466,397,562</td>
<td align="right">27.0%</td>
<td align="right">2,536,645,657</td>
<td align="right">28.1%</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">49,806,432,450</td>
<td align="right">46.3%</td>
<td align="right">5,254,568,270</td>
<td align="right">46.0%</td>
<td align="right">-89.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,138,120</td>
<td align="right">0.4%</td>
<td align="right">8,230,924</td>
<td align="right">0.3%</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">31,297,644,715</td>
<td align="right">29.1%</td>
<td align="right">3,678,992,319</td>
<td align="right">32.2%</td>
<td align="right">-88.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,602,133,664</td>
<td align="right">5.1%</td>
<td align="right">668,946,512</td>
<td align="right">7.4%</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,104,683,775</td>
<td align="right"></td>
<td align="right">941,711,471</td>
<td align="right"></td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,340,508,154</td>
<td align="right">70.8%</td>
<td align="right">2,060,335,109</td>
<td align="right">69.5%</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,340,610,284</td>
<td align="right"></td>
<td align="right">2,060,365,745</td>
<td align="right"></td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,509,865,802</td>
<td align="right">29.2%</td>
<td align="right">902,972,157</td>
<td align="right">30.5%</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,432,363,517</td>
<td align="right">28.8%</td>
<td align="right">894,238,058</td>
<td align="right">30.2%</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,821,950,920</td>
<td align="right">1.7%</td>
<td align="right">401,594,123</td>
<td align="right">3.5%</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">173,692,544</td>
<td align="right"></td>
<td align="right">40,958,811</td>
<td align="right"></td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,404,481</td>
<td align="right">2.0%</td>
<td align="right">998,419</td>
<td align="right">2.4%</td>
<td align="right">-70.7%</td>
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
<td align="right">363,328</td>
<td align="right">100,801,512</td>
<td align="right">9,477,525,734</td>
<td align="right">752,897,551</td>
<td align="right">760,428,519</td>
<td align="right">12,598</td>
<td align="right">2,194,742</td>
<td align="right">437,627,145</td>
<td align="right">72,253,054</td>
<td align="right">10,427,429</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,681,291,008</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,681,301,508</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">180</td>
<td align="right">0.0%</td>
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
<td align="right">82</td>
<td align="right">0.0%</td>
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
<td align="right">659</td>
<td align="right">0.2%</td>
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
<td align="right">221</td>
<td align="right">0.8%</td>
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
<td align="right">1,750</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">865</td>
<td align="right">0.2%</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">27,435</td>
<td align="right">6.4%</td>
<td align="right">541</td>
<td align="right">0.6%</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">257,549,055,278</td>
<td align="right">6,466.7%</td>
<td align="right">14,037,122,772</td>
<td align="right">6,019.6%</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,982,710,746</td>
<td align="right"></td>
<td align="right">233,190,740</td>
<td align="right"></td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">228,518</td>
<td align="right">53.1%</td>
<td align="right">28,685</td>
<td align="right">30.6%</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">430,696</td>
<td align="right"></td>
<td align="right">93,736</td>
<td align="right"></td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">127,181</td>
<td align="right">29.5%</td>
<td align="right">40,988</td>
<td align="right">43.7%</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">47,382</td>
<td align="right">11.0%</td>
<td align="right">23,522</td>
<td align="right">25.1%</td>
<td align="right">-50.4%</td>
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
<td align="right">27,435</td>
<td align="right"></td>
<td align="right">541</td>
<td align="right"></td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">22,707</td>
<td align="right">82.8%</td>
<td align="right">538</td>
<td align="right">99.4%</td>
<td align="right">-97.6%</td>
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
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### JIT trace total memory histogram

<details>
<summary> JIT trace total memory histogram </summary>


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
<td align="right">1,303</td>
<td align="right">4.7%</td>
<td align="right">8</td>
<td align="right">1.5%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">736</td>
<td align="right">2.7%</td>
<td align="right">62</td>
<td align="right">11.5%</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">3,836</td>
<td align="right">14.0%</td>
<td align="right">25</td>
<td align="right">4.6%</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,317</td>
<td align="right">30.3%</td>
<td align="right">264</td>
<td align="right">48.8%</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">5,708</td>
<td align="right">20.8%</td>
<td align="right">124</td>
<td align="right">22.9%</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,285</td>
<td align="right">19.3%</td>
<td align="right">12</td>
<td align="right">2.2%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,900</td>
<td align="right">6.9%</td>
<td align="right">46</td>
<td align="right">8.5%</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">350</td>
<td align="right">1.3%</td>
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
<td align="right">754</td>
<td align="right">2.7%</td>
<td align="right">4</td>
<td align="right">0.7%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">834</td>
<td align="right">3.0%</td>
<td align="right">4</td>
<td align="right">0.7%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,872</td>
<td align="right">6.8%</td>
<td align="right">62</td>
<td align="right">11.5%</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,367</td>
<td align="right">26.9%</td>
<td align="right">178</td>
<td align="right">32.9%</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">6,707</td>
<td align="right">24.4%</td>
<td align="right">184</td>
<td align="right">34.0%</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,884</td>
<td align="right">10.5%</td>
<td align="right">57</td>
<td align="right">10.5%</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,018</td>
<td align="right">7.4%</td>
<td align="right">49</td>
<td align="right">9.1%</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">271</td>
<td align="right">1.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left"><= 4</td>
<td align="right">14,186,930</td>
<td align="right">0.4%</td>
<td align="right">185,095</td>
<td align="right">0.1%</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">132,744,325</td>
<td align="right">3.3%</td>
<td align="right">3,424,138</td>
<td align="right">1.5%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">140,545,627</td>
<td align="right">3.5%</td>
<td align="right">98,945,916</td>
<td align="right">42.4%</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">141,062,069</td>
<td align="right">3.5%</td>
<td align="right">9,986,158</td>
<td align="right">4.3%</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">133,370,033</td>
<td align="right">3.3%</td>
<td align="right">7,973,642</td>
<td align="right">3.4%</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">147,610,913</td>
<td align="right">3.7%</td>
<td align="right">3,691,769</td>
<td align="right">1.6%</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">77,258,334</td>
<td align="right">1.9%</td>
<td align="right">4,454,152</td>
<td align="right">1.9%</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">53,972,668</td>
<td align="right">1.4%</td>
<td align="right">323,004</td>
<td align="right">0.1%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">3,750,127</td>
<td align="right">0.1%</td>
<td align="right">27,399</td>
<td align="right">0.0%</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left"><= 2,048</td>
<td align="right">6,346,551</td>
<td align="right">0.2%</td>
<td align="right">3,476</td>
<td align="right">0.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left"><= 4,096</td>
<td align="right">5,945,752</td>
<td align="right">0.1%</td>
<td align="right">12,675</td>
<td align="right">0.0%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="right">193,295</td>
<td align="right">0.0%</td>
<td align="right">19,071</td>
<td align="right">0.0%</td>
<td align="right">-90.1%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="right">404,939</td>
<td align="right">0.0%</td>
<td align="right">32,668</td>
<td align="right">0.0%</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="right">65,199</td>
<td align="right">0.0%</td>
<td align="right">19,469</td>
<td align="right">0.0%</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="right">13,376</td>
<td align="right">0.0%</td>
<td align="right">10,336</td>
<td align="right">0.0%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="right">1,892</td>
<td align="right">0.0%</td>
<td align="right">6,913</td>
<td align="right">0.0%</td>
<td align="right">265.4%</td>
</tr>
<tr>
<td align="left"><= 262,144</td>
<td align="right">3,024</td>
<td align="right">0.0%</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left"><= 524,288</td>
<td align="right">129</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left"><= 1,048,576</td>
<td align="right">771</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left"><= 2,097,152</td>
<td align="right">64</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 4,194,304</td>
<td align="right">304</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left"><= 8,388,608</td>
<td align="right">376</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16,777,216</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_SET_IP</td>
<td align="right">45,375,212,290</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">40,202,232,273</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">11,108,265,467</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,878,057,981</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">7,102,352,483</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,414,126,569</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,457,953,424</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,426,660,335</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">4,068,351,997</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">4,014,376,542</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,982,710,746</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,947,970,307</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,887,160,045</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,845,486,860</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,517,773,004</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,057,066,035</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">3,050,822,804</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,863,162,347</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,851,737,576</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">2,509,407,365</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,431,415,823</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,384,459,019</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,279,229,832</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,197,747,403</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,063,781,956</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,998,262,818</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,891,253,130</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,837,717,314</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,816,293,544</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,791,873,003</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,745,076,396</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,564,697,738</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,509,761,724</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,509,474,606</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,480,071,949</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,430,532,258</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,393,017,228</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,344,196,481</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,320,322,876</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,304,768,256</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,300,682,593</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,300,682,593</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,287,980,182</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,247,590,696</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,221,157,012</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,220,200,155</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,199,881,009</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,187,668,336</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,187,016,034</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,145,196,439</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,122,327,034</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,113,617,394</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,082,097,967</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,069,219,437</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,013,166,951</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,003,771,205</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,003,641,045</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">971,358,433</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">965,968,053</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">926,478,876</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">926,464,016</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">866,418,761</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">833,231,746</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">805,129,033</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">779,668,411</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">753,138,709</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">746,004,927</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">726,451,281</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">717,377,208</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">670,429,678</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">661,730,447</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">655,176,943</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">596,488,781</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">559,072,809</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">551,155,259</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">542,683,369</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">534,009,223</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">531,566,712</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">504,412,177</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">500,059,495</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">498,439,034</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">469,930,922</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">449,749,670</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">448,805,353</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">445,741,619</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">445,741,619</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">440,628,276</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">439,980,240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">428,437,533</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">428,437,533</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">414,516,537</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">412,821,337</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">407,490,053</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">400,643,343</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">393,919,631</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">391,630,094</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">360,587,445</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">348,559,767</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">343,528,380</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">335,424,943</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">332,302,154</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">312,114,517</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">307,754,470</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">306,190,869</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">289,990,289</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">263,905,177</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">262,694,825</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">261,649,060</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">261,565,329</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">259,280,781</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">244,339,999</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">243,182,879</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">230,835,694</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">229,986,832</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">211,898,941</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">203,031,296</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">182,403,379</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">178,111,115</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">164,064,034</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">158,911,496</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">155,622,445</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">155,428,015</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">153,037,305</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">149,591,205</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">147,833,619</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">147,271,238</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">143,545,091</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">131,191,278</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">118,974,119</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">118,884,105</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">103,181,657</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">103,178,820</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">103,085,273</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">103,014,925</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">95,607,725</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">94,858,325</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,858,325</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">83,205,303</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">79,004,918</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">76,775,324</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,770,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">71,288,427</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,486</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,486</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">66,356,519</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,013,740</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">57,364,896</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">56,025,976</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">55,031,102</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,761,135</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,761,135</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">48,464,793</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">48,051,005</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,940,455</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,560</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">47,392,961</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,079</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,593,190</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">45,671,120</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">45,068,860</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,583,966</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">43,167,917</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">41,237,221</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">40,586,464</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,025,698</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">39,818,680</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">38,523,146</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">37,153,757</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">35,808,177</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">35,238,126</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">34,720,266</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">30,896,592</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">30,896,592</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">30,881,687</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">26,705,825</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">24,482,822</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">24,482,822</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">20,612,164</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">20,181,522</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,702,411</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,702,411</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">12,248,707</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">10,593,166</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">8,323,320</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">8,140,533</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">7,325,900</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">7,323,400</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,159,872</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">6,017,140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">5,266,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,107,574</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,635,678</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">4,279,396</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">3,709,046</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,253,140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,154,648</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">3,106,080</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,070,900</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,975,980</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,975,980</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,714,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,546,042</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,152,113</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">392,500</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">267,905</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">229,826</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">154,160</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">143,096</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">98,482</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">36,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">36,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">20,173</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">15,603</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">62</td>
<td align="right"></td>
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
<td align="right">23,590</td>
<td align="right">550</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right">22,980</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,817</td>
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
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,592</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
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
<td align="right">0</td>
<td align="right">-100.0%</td>
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
<td align="right">101</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
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
<td align="right">2</td>
<td align="right">-95.1%</td>
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
<td align="right">1,121</td>
<td align="right">-53.2%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-13
