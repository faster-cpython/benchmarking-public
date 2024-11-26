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
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,879,291</td>
<td align="right">8,854,355</td>
<td align="right">128.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,321,692</td>
<td align="right">802</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">14,289,260</td>
<td align="right">9,376</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,662</td>
<td align="right">1,048</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,321,423</td>
<td align="right">18,121</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">607,165</td>
<td align="right">4,125</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,476,008</td>
<td align="right">202,405</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">22,860,472</td>
<td align="right">536,121</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">71,105</td>
<td align="right">1,715</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,608,275</td>
<td align="right">174,319</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">4,838,905</td>
<td align="right">166,927</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">52,554</td>
<td align="right">1,954</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,246,906</td>
<td align="right">271,856</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,063,691</td>
<td align="right">79,941</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,218,892</td>
<td align="right">117,642</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,029,143</td>
<td align="right">67,573</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,057,632</td>
<td align="right">79,734</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">174,994</td>
<td align="right">13,355</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,417,975</td>
<td align="right">3,013,029</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,544</td>
<td align="right">41,697</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,838,557</td>
<td align="right">1,012,330</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">74,141</td>
<td align="right">8,884</td>
<td align="right">-88.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">133,724</td>
<td align="right">16,172</td>
<td align="right">-87.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">136,879,899</td>
<td align="right">22,156,634</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,749,686</td>
<td align="right">977,979</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,780,091</td>
<td align="right">306,066</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">11,099,447</td>
<td align="right">1,973,122</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">39,951</td>
<td align="right">7,458</td>
<td align="right">-81.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">92,409,963</td>
<td align="right">167,159,734</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,196,307</td>
<td align="right">254,320</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,203</td>
<td align="right">259</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">105,016,074</td>
<td align="right">22,840,462</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">19,200,207</td>
<td align="right">4,857,734</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">3,124,246</td>
<td align="right">817,300</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">11,370,614</td>
<td align="right">3,038,494</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">3,859,267</td>
<td align="right">1,086,217</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,281,374</td>
<td align="right">370,595</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,754</td>
<td align="right">21,183</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,211,249</td>
<td align="right">1,944,348</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">237</td>
<td align="right">78</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">50,487,311</td>
<td align="right">16,876,315</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,828,270</td>
<td align="right">5,994,256</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,345,530</td>
<td align="right">483,873</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">123,552</td>
<td align="right">45,542</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,520,947</td>
<td align="right">1,007,768</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">468,372</td>
<td align="right">196,076</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,634,566</td>
<td align="right">7,843,076</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,509,509</td>
<td align="right">7,034,729</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,055,128</td>
<td align="right">456,075</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">30,773</td>
<td align="right">13,461</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">71,246,150</td>
<td align="right">31,793,265</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">136,100,728</td>
<td align="right">62,750,372</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">539,432</td>
<td align="right">250,647</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">255</td>
<td align="right">120</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,256,473</td>
<td align="right">613,094</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">622,651</td>
<td align="right">304,894</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">17,749,342</td>
<td align="right">8,718,771</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">105,666</td>
<td align="right">52,134</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,892,500</td>
<td align="right">1,432,935</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">10,918,887</td>
<td align="right">5,439,017</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">473,033,632</td>
<td align="right">235,951,601</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,263,722</td>
<td align="right">3,177,445</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">25,981,976</td>
<td align="right">13,444,489</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">32,782,877</td>
<td align="right">17,297,902</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,295</td>
<td align="right">395,081</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">139,121,687</td>
<td align="right">73,787,621</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">995,197</td>
<td align="right">534,100</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">39,065,720</td>
<td align="right">21,158,184</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">397,271</td>
<td align="right">218,067</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,600,177</td>
<td align="right">879,170</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,314,780</td>
<td align="right">728,851</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">5,310,885</td>
<td align="right">2,957,760</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,583</td>
<td align="right">1,439</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">30,956,622</td>
<td align="right">17,659,746</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">158,330,776</td>
<td align="right">90,323,629</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,946,272</td>
<td align="right">1,129,042</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,497,539</td>
<td align="right">876,160</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">113,357,355</td>
<td align="right">66,690,681</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,287,357</td>
<td align="right">2,534,143</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">97,676,996</td>
<td align="right">58,234,048</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">65,100</td>
<td align="right">39,057</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">19,307,131</td>
<td align="right">11,612,400</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,190</td>
<td align="right">1,944</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">18,302</td>
<td align="right">11,295</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,907</td>
<td align="right">470,962</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">102</td>
<td align="right">65</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">34,637,945</td>
<td align="right">22,553,837</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,719,108</td>
<td align="right">7,645,994</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">8,156,386</td>
<td align="right">5,371,155</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">40,576,206</td>
<td align="right">26,926,133</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">13,669,235</td>
<td align="right">9,086,001</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">13,253,197</td>
<td align="right">8,869,022</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">25,560,162</td>
<td align="right">17,178,567</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">7,729</td>
<td align="right">5,243</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">385,773</td>
<td align="right">261,846</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">255,756</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">7,342</td>
<td align="right">5,047</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,963,363</td>
<td align="right">1,353,935</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">12,291,380</td>
<td align="right">8,542,227</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">447</td>
<td align="right">316</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">15,526,829</td>
<td align="right">10,997,895</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">14,948,428</td>
<td align="right">10,611,539</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">17,009</td>
<td align="right">12,197</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,808,442</td>
<td align="right">2,025,905</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">529</td>
<td align="right">398</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">8,072,810</td>
<td align="right">6,238,523</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">25,654,023</td>
<td align="right">20,205,268</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,603,496</td>
<td align="right">2,070,701</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">46,202,490</td>
<td align="right">37,317,019</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">24,019,921</td>
<td align="right">19,840,642</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,310</td>
<td align="right">549,125</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,310</td>
<td align="right">549,125</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,310</td>
<td align="right">549,125</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">173,809</td>
<td align="right">201,860</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">19,444,321</td>
<td align="right">16,403,572</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,750,624</td>
<td align="right">20,282,074</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,991,352</td>
<td align="right">3,424,564</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">44,842,688</td>
<td align="right">38,554,760</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">42,970,088</td>
<td align="right">36,954,240</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,339,015</td>
<td align="right">5,455,990</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,805,208</td>
<td align="right">2,449,064</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">16,708,987</td>
<td align="right">14,594,620</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9,059</td>
<td align="right">7,924</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">8,505,541</td>
<td align="right">7,469,273</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">10,359,197</td>
<td align="right">9,219,817</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,129</td>
<td align="right">74,247</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">9,684,724</td>
<td align="right">8,751,293</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,055</td>
<td align="right">963</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,462,855</td>
<td align="right">4,142,892</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,559,343</td>
<td align="right">20,437,770</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">16,029,591</td>
<td align="right">16,838,717</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">35,562,454</td>
<td align="right">33,768,669</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">747,546</td>
<td align="right">784,995</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,503,634</td>
<td align="right">16,753,852</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">642,644</td>
<td align="right">615,774</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,452,435</td>
<td align="right">93,395,718</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">137,233,235</td>
<td align="right">131,618,159</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">259,523</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">171,141</td>
<td align="right">164,662</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,125,037</td>
<td align="right">1,086,064</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">62</td>
<td align="right">60</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,486</td>
<td align="right">161,393</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">43,967,794</td>
<td align="right">43,087,575</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">88,122</td>
<td align="right">86,571</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">176,758</td>
<td align="right">173,656</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">176,760</td>
<td align="right">173,658</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,497</td>
<td align="right">21,594,759</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">33,295,553</td>
<td align="right">32,716,717</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,621,476</td>
<td align="right">1,594,909</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,195</td>
<td align="right">18,024</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,980</td>
<td align="right">2,953</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,250</td>
<td align="right">1,233,310</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">3,960,117</td>
<td align="right">3,929,125</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,271</td>
<td align="right">24,142</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">3,595</td>
<td align="right">3,614</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,447</td>
<td align="right">1,442</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,726,920</td>
<td align="right">3,715,700</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">7,373</td>
<td align="right">7,392</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">133</td>
<td align="right">133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">92</td>
<td align="right">92</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,386,334</td>
<td align="right">37.7%</td>
<td align="right">12,116,089</td>
<td align="right">37.4%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">23,730,733</td>
<td align="right">62.2%</td>
<td align="right">20,264,933</td>
<td align="right">62.5%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">123</td>
<td align="right">0.0%</td>
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
<td align="right">18,580</td>
<td align="right">93.4%</td>
<td align="right">15,872</td>
<td align="right">92.6%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,311</td>
<td align="right">6.6%</td>
<td align="right">1,269</td>
<td align="right">7.4%</td>
<td align="right">-3.2%</td>
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
<td align="right">189</td>
<td align="right">1.0%</td>
<td align="right">8</td>
<td align="right">0.1%</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">94</td>
<td align="right">0.5%</td>
<td align="right">49</td>
<td align="right">0.3%</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">362</td>
<td align="right">1.9%</td>
<td align="right">268</td>
<td align="right">1.7%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,214</td>
<td align="right">6.5%</td>
<td align="right">902</td>
<td align="right">5.7%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">989</td>
<td align="right">5.3%</td>
<td align="right">735</td>
<td align="right">4.6%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,340</td>
<td align="right">12.6%</td>
<td align="right">1,824</td>
<td align="right">11.5%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">693</td>
<td align="right">3.7%</td>
<td align="right">555</td>
<td align="right">3.5%</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,286</td>
<td align="right">6.9%</td>
<td align="right">1,045</td>
<td align="right">6.6%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">2,644</td>
<td align="right">14.2%</td>
<td align="right">2,197</td>
<td align="right">13.8%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">571</td>
<td align="right">3.1%</td>
<td align="right">483</td>
<td align="right">3.0%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">671</td>
<td align="right">3.6%</td>
<td align="right">578</td>
<td align="right">3.6%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,087</td>
<td align="right">5.9%</td>
<td align="right">954</td>
<td align="right">6.0%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">970</td>
<td align="right">5.2%</td>
<td align="right">917</td>
<td align="right">5.8%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,876</td>
<td align="right">15.5%</td>
<td align="right">2,769</td>
<td align="right">17.4%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">213</td>
<td align="right">1.1%</td>
<td align="right">211</td>
<td align="right">1.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.8%</td>
<td align="right">154</td>
<td align="right">1.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">12.0%</td>
<td align="right">2,223</td>
<td align="right">14.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1</td>
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
<td align="right">7,342</td>
<td align="right">100.0%</td>
<td align="right">5,047</td>
<td align="right">100.0%</td>
<td align="right">-31.3%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,212</td>
<td align="right">0.0%</td>
<td align="right">3,437</td>
<td align="right">0.0%</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,803,798</td>
<td align="right">7.9%</td>
<td align="right">2,021,686</td>
<td align="right">6.8%</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,748,367</td>
<td align="right">92.1%</td>
<td align="right">27,651,009</td>
<td align="right">93.2%</td>
<td align="right">-15.6%</td>
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
<td align="right">956</td>
<td align="right">19.9%</td>
<td align="right">824</td>
<td align="right">19.3%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,860</td>
<td align="right">80.1%</td>
<td align="right">3,441</td>
<td align="right">80.7%</td>
<td align="right">-10.9%</td>
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
<td align="right">272</td>
<td align="right">7.0%</td>
<td align="right">204</td>
<td align="right">5.9%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">690</td>
<td align="right">17.9%</td>
<td align="right">551</td>
<td align="right">16.0%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">338</td>
<td align="right">8.8%</td>
<td align="right">273</td>
<td align="right">7.9%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">141</td>
<td align="right">3.7%</td>
<td align="right">119</td>
<td align="right">3.5%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,418</td>
<td align="right">62.6%</td>
<td align="right">2,293</td>
<td align="right">66.6%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">10,127</td>
<td align="right">0.0%</td>
<td align="right">6,096</td>
<td align="right">0.0%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">297,441,199</td>
<td align="right">92.8%</td>
<td align="right">281,537,520</td>
<td align="right">92.8%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">23,076,385</td>
<td align="right">7.2%</td>
<td align="right">21,879,540</td>
<td align="right">7.2%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,489</td>
<td align="right">0.0%</td>
<td align="right">8,426</td>
<td align="right">0.0%</td>
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
<td align="right">452,023</td>
<td align="right">100.0%</td>
<td align="right">429,247</td>
<td align="right">100.0%</td>
<td align="right">-5.0%</td>
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
<td align="right">13</td>
<td align="right">13 / 0 !!</td>
<td align="right">13</td>
<td align="right">13 / 0 !!</td>
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
<td align="right">2,805</td>
<td align="right">66.0%</td>
<td align="right">2,619</td>
<td align="right">64.5%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">401</td>
<td align="right">9.4%</td>
<td align="right">399</td>
<td align="right">9.8%</td>
<td align="right">-0.5%</td>
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
<td align="right">19,272,423</td>
<td align="right">27.3%</td>
<td align="right">11,585,908</td>
<td align="right">19.7%</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">375,216</td>
<td align="right">0.5%</td>
<td align="right">318,977</td>
<td align="right">0.5%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,018,257</td>
<td align="right">72.2%</td>
<td align="right">46,874,202</td>
<td align="right">79.7%</td>
<td align="right">-8.1%</td>
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
<td align="right">33,517</td>
<td align="right">80.3%</td>
<td align="right">25,414</td>
<td align="right">78.3%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,214</td>
<td align="right">19.7%</td>
<td align="right">7,049</td>
<td align="right">21.7%</td>
<td align="right">-14.2%</td>
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
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">49</td>
<td align="right">0.2%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,126</td>
<td align="right">9.3%</td>
<td align="right">1,382</td>
<td align="right">5.4%</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,090</td>
<td align="right">15.2%</td>
<td align="right">3,404</td>
<td align="right">13.4%</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">12,862</td>
<td align="right">38.4%</td>
<td align="right">9,071</td>
<td align="right">35.7%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">194</td>
<td align="right">0.6%</td>
<td align="right">243</td>
<td align="right">1.0%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">69</td>
<td align="right">0.3%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">114</td>
<td align="right">0.3%</td>
<td align="right">94</td>
<td align="right">0.4%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,244</td>
<td align="right">12.7%</td>
<td align="right">3,534</td>
<td align="right">13.9%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">22.3%</td>
<td align="right">7,390</td>
<td align="right">29.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">134</td>
<td align="right">0.4%</td>
<td align="right">134</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">44</td>
<td align="right">0.1%</td>
<td align="right">44</td>
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
<td align="right">1,342,229</td>
<td align="right">5.4%</td>
<td align="right">482,009</td>
<td align="right">2.1%</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,697</td>
<td align="right">94.6%</td>
<td align="right">22,169,469</td>
<td align="right">97.9%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">1,020</td>
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
<td align="right">3,179</td>
<td align="right">96.3%</td>
<td align="right">1,742</td>
<td align="right">93.5%</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">122</td>
<td align="right">3.7%</td>
<td align="right">122</td>
<td align="right">6.5%</td>
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
<td align="right">285</td>
<td align="right">9.0%</td>
<td align="right">111</td>
<td align="right">6.4%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,366</td>
<td align="right">43.0%</td>
<td align="right">660</td>
<td align="right">37.9%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,394</td>
<td align="right">43.9%</td>
<td align="right">859</td>
<td align="right">49.3%</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">134</td>
<td align="right">4.2%</td>
<td align="right">112</td>
<td align="right">6.4%</td>
<td align="right">-16.4%</td>
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
<td align="right">91,857</td>
<td align="right">0.2%</td>
<td align="right">18,504</td>
<td align="right">0.1%</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,280,107</td>
<td align="right">44.4%</td>
<td align="right">12,229,733</td>
<td align="right">37.4%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,544,534</td>
<td align="right">55.3%</td>
<td align="right">20,425,102</td>
<td align="right">62.5%</td>
<td align="right">-5.2%</td>
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
<td align="right">2,399</td>
<td align="right">14.6%</td>
<td align="right">1,032</td>
<td align="right">7.9%</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">14,078</td>
<td align="right">85.4%</td>
<td align="right">11,979</td>
<td align="right">92.1%</td>
<td align="right">-14.9%</td>
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
<td align="right">6,653</td>
<td align="right">47.3%</td>
<td align="right">4,876</td>
<td align="right">40.7%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,413</td>
<td align="right">17.1%</td>
<td align="right">2,226</td>
<td align="right">18.6%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">350</td>
<td align="right">2.5%</td>
<td align="right">328</td>
<td align="right">2.7%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,119</td>
<td align="right">7.9%</td>
<td align="right">1,067</td>
<td align="right">8.9%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.2%</td>
<td align="right">23</td>
<td align="right">0.2%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.2%</td>
<td align="right">28</td>
<td align="right">0.2%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,136</td>
<td align="right">15.2%</td>
<td align="right">2,091</td>
<td align="right">17.5%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">422</td>
<td align="right">3.0%</td>
<td align="right">415</td>
<td align="right">3.5%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">239</td>
<td align="right">1.7%</td>
<td align="right">236</td>
<td align="right">2.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">693</td>
<td align="right">4.9%</td>
<td align="right">689</td>
<td align="right">5.8%</td>
<td align="right">-0.6%</td>
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
<td align="right">50,430,281</td>
<td align="right">16.5%</td>
<td align="right">16,835,565</td>
<td align="right">6.4%</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">27,108,187</td>
<td align="right">8.8%</td>
<td align="right">9,578,280</td>
<td align="right">3.7%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,588</td>
<td align="right">0.0%</td>
<td align="right">8,262</td>
<td align="right">0.0%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">228,899,832</td>
<td align="right">74.7%</td>
<td align="right">235,113,766</td>
<td align="right">89.9%</td>
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
<td align="right">523,575</td>
<td align="right">92.5%</td>
<td align="right">191,272</td>
<td align="right">87.4%</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">42,657</td>
<td align="right">7.5%</td>
<td align="right">27,631</td>
<td align="right">12.6%</td>
<td align="right">-35.2%</td>
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
<td align="right">244</td>
<td align="right">0.6%</td>
<td align="right">564</td>
<td align="right">2.0%</td>
<td align="right">131.1%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,360</td>
<td align="right">5.5%</td>
<td align="right">265</td>
<td align="right">1.0%</td>
<td align="right">-88.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,223</td>
<td align="right">14.6%</td>
<td align="right">1,426</td>
<td align="right">5.2%</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,054</td>
<td align="right">7.2%</td>
<td align="right">1,125</td>
<td align="right">4.1%</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,739</td>
<td align="right">6.4%</td>
<td align="right">2,035</td>
<td align="right">7.4%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,012</td>
<td align="right">7.1%</td>
<td align="right">2,308</td>
<td align="right">8.4%</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">19,996</td>
<td align="right">46.9%</td>
<td align="right">15,764</td>
<td align="right">57.1%</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">3,866</td>
<td align="right">9.1%</td>
<td align="right">3,385</td>
<td align="right">12.3%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">142</td>
<td align="right">0.3%</td>
<td align="right">142</td>
<td align="right">0.5%</td>
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
<td align="right">208,829,942</td>
<td align="right">100.0%</td>
<td align="right">95,948,577</td>
<td align="right">100.0%</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,294</td>
<td align="right">0.0%</td>
<td align="right">1,814</td>
<td align="right">0.0%</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,602</td>
<td align="right">0.0%</td>
<td align="right">4,520</td>
<td align="right">0.0%</td>
<td align="right">-1.8%</td>
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
<td align="right">13,641</td>
<td align="right">100.0%</td>
<td align="right">13,592</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,265,858</td>
<td align="right">100.0%</td>
<td align="right">2,215,591</td>
<td align="right">100.0%</td>
<td align="right">-2.2%</td>
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
<td align="right">30</td>
<td align="right">100.0%</td>
<td align="right">30</td>
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
<td align="right">731,584</td>
<td align="right">72.0%</td>
<td align="right">385,206</td>
<td align="right">58.8%</td>
<td align="right">-47.3%</td>
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
<td align="right">1.4%</td>
<td align="right">9,875</td>
<td align="right">1.5%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">268,986</td>
<td align="right">26.5%</td>
<td align="right">258,773</td>
<td align="right">39.5%</td>
<td align="right">-3.8%</td>
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
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">165</td>
<td align="right">17.3%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
<td align="right">789</td>
<td align="right">82.7%</td>
<td align="right">-28.8%</td>
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
<td align="right">1,108</td>
<td align="right">100.0%</td>
<td align="right">789</td>
<td align="right">100.0%</td>
<td align="right">-28.8%</td>
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
<td align="right">173,679</td>
<td align="right">2.1%</td>
<td align="right">12,315</td>
<td align="right">0.2%</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">307,869</td>
<td align="right">3.7%</td>
<td align="right">248,442</td>
<td align="right">3.1%</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,902,645</td>
<td align="right">94.2%</td>
<td align="right">7,780,768</td>
<td align="right">96.7%</td>
<td align="right">-1.5%</td>
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
<td align="right">980</td>
<td align="right">14.0%</td>
<td align="right">705</td>
<td align="right">12.5%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,045</td>
<td align="right">86.0%</td>
<td align="right">4,935</td>
<td align="right">87.5%</td>
<td align="right">-18.4%</td>
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
<td align="right">302</td>
<td align="right">30.8%</td>
<td align="right">28</td>
<td align="right">4.0%</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">157</td>
<td align="right">16.0%</td>
<td align="right">156</td>
<td align="right">22.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">52.9%</td>
<td align="right">518</td>
<td align="right">73.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3</td>
<td align="right">0.3%</td>
<td align="right">3</td>
<td align="right">0.4%</td>
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
<td align="right">529</td>
<td align="right">100.0%</td>
<td align="right">398</td>
<td align="right">100.0%</td>
<td align="right">-24.8%</td>
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
<td align="right">63,565</td>
<td align="right">0.4%</td>
<td align="right">37,495</td>
<td align="right">0.3%</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,739,047</td>
<td align="right">99.6%</td>
<td align="right">13,378,323</td>
<td align="right">99.7%</td>
<td align="right">-24.6%</td>
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
<td align="right">957</td>
<td align="right">62.3%</td>
<td align="right">986</td>
<td align="right">63.1%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">578</td>
<td align="right">37.7%</td>
<td align="right">576</td>
<td align="right">36.9%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">957</td>
<td align="right">100.0%</td>
<td align="right">986</td>
<td align="right">100.0%</td>
<td align="right">3.0%</td>
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
<td align="right">9,821,291</td>
<td align="right">6.0%</td>
<td align="right">998,498</td>
<td align="right">0.7%</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">342,062</td>
<td align="right">0.2%</td>
<td align="right">248,430</td>
<td align="right">0.2%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">152,936,713</td>
<td align="right">93.8%</td>
<td align="right">149,692,627</td>
<td align="right">99.2%</td>
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
<td align="right">9,602</td>
<td align="right">41.4%</td>
<td align="right">6,178</td>
<td align="right">34.5%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,592</td>
<td align="right">58.6%</td>
<td align="right">11,748</td>
<td align="right">65.5%</td>
<td align="right">-13.6%</td>
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
<td align="right">4,829</td>
<td align="right">50.3%</td>
<td align="right">1,841</td>
<td align="right">29.8%</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">651</td>
<td align="right">6.8%</td>
<td align="right">428</td>
<td align="right">6.9%</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,252</td>
<td align="right">13.0%</td>
<td align="right">965</td>
<td align="right">15.6%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,175</td>
<td align="right">12.2%</td>
<td align="right">1,261</td>
<td align="right">20.4%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">726</td>
<td align="right">7.6%</td>
<td align="right">710</td>
<td align="right">11.5%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">9.2%</td>
<td align="right">887</td>
<td align="right">14.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.9%</td>
<td align="right">84</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,350</td>
<td align="right">0.0%</td>
<td align="right">5,229</td>
<td align="right">0.0%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,504,945</td>
<td align="right">100.0%</td>
<td align="right">82,460,816</td>
<td align="right">100.0%</td>
<td align="right">-1.3%</td>
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
<td align="right">305</td>
<td align="right">11.3%</td>
<td align="right">303</td>
<td align="right">11.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,404</td>
<td align="right">88.7%</td>
<td align="right">2,392</td>
<td align="right">88.8%</td>
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
<td align="left">sequence</td>
<td align="right">262</td>
<td align="right">85.9%</td>
<td align="right">260</td>
<td align="right">85.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.1%</td>
<td align="right">43</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">933,574,390</td>
<td align="right">31.4%</td>
<td align="right">473,065,306</td>
<td align="right">25.9%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">129,668,033</td>
<td align="right">4.4%</td>
<td align="right">73,099,639</td>
<td align="right">4.0%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">51,331,743</td>
<td align="right">1.7%</td>
<td align="right">32,313,530</td>
<td align="right">1.8%</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,854,223,784</td>
<td align="right">62.5%</td>
<td align="right">1,246,707,251</td>
<td align="right">68.3%</td>
<td align="right">-32.8%</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">173,679</td>
<td align="right">0.1%</td>
<td align="right">12,315</td>
<td align="right">0.0%</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,821,291</td>
<td align="right">7.6%</td>
<td align="right">998,498</td>
<td align="right">1.4%</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">50,430,281</td>
<td align="right">38.9%</td>
<td align="right">16,835,565</td>
<td align="right">23.1%</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,342,229</td>
<td align="right">1.0%</td>
<td align="right">482,009</td>
<td align="right">0.7%</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">63,565</td>
<td align="right">0.0%</td>
<td align="right">37,495</td>
<td align="right">0.1%</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">19,272,423</td>
<td align="right">14.9%</td>
<td align="right">11,585,908</td>
<td align="right">15.9%</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,803,798</td>
<td align="right">2.2%</td>
<td align="right">2,021,686</td>
<td align="right">2.8%</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">23,730,733</td>
<td align="right">18.3%</td>
<td align="right">20,264,933</td>
<td align="right">27.8%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,544,534</td>
<td align="right">16.6%</td>
<td align="right">20,425,102</td>
<td align="right">28.0%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.2%</td>
<td align="right">258,773</td>
<td align="right">0.4%</td>
<td align="right">-3.8%</td>
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
<td align="right">10,652,903</td>
<td align="right">20.8%</td>
<td align="right">713,141</td>
<td align="right">2.2%</td>
<td align="right">-93.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,945,984</td>
<td align="right">5.7%</td>
<td align="right">1,107,412</td>
<td align="right">3.4%</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">8,437,453</td>
<td align="right">16.4%</td>
<td align="right">3,964,666</td>
<td align="right">12.3%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,679,692</td>
<td align="right">9.1%</td>
<td align="right">3,624,985</td>
<td align="right">11.2%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">307,090</td>
<td align="right">0.6%</td>
<td align="right">248,057</td>
<td align="right">0.8%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,687,635</td>
<td align="right">9.1%</td>
<td align="right">3,786,811</td>
<td align="right">11.7%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">374,196</td>
<td align="right">0.7%</td>
<td align="right">318,009</td>
<td align="right">1.0%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,149,593</td>
<td align="right">21.7%</td>
<td align="right">10,930,556</td>
<td align="right">33.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,581</td>
<td align="right">4.1%</td>
<td align="right">2,074,345</td>
<td align="right">6.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,530</td>
<td align="right">9.9%</td>
<td align="right">5,062,843</td>
<td align="right">15.7%</td>
<td align="right">-0.8%</td>
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
<td align="right">1,008,496</td>
<td align="right">0.5%</td>
<td align="right">831,196</td>
<td align="right">0.4%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,083,219</td>
<td align="right">19.5%</td>
<td align="right">38,360,081</td>
<td align="right">19.0%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,379,446</td>
<td align="right">35.8%</td>
<td align="right">71,954,163</td>
<td align="right">35.7%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,380,231</td>
<td align="right">35.8%</td>
<td align="right">71,954,948</td>
<td align="right">35.7%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">97,635,949</td>
<td align="right">46.4%</td>
<td align="right">93,539,907</td>
<td align="right">46.4%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">97,635,949</td>
<td align="right">46.4%</td>
<td align="right">93,539,907</td>
<td align="right">46.4%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,905,623</td>
<td align="right">89.3%</td>
<td align="right">180,297,456</td>
<td align="right">89.4%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,770,256</td>
<td align="right">53.6%</td>
<td align="right">108,221,299</td>
<td align="right">53.6%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,255,718</td>
<td align="right">10.6%</td>
<td align="right">21,584,959</td>
<td align="right">10.7%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,491,134</td>
<td align="right">8.8%</td>
<td align="right">18,074,448</td>
<td align="right">9.0%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,332,127</td>
<td align="right">4.4%</td>
<td align="right">9,243,993</td>
<td align="right">4.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">348</td>
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
<td align="right">520,098,931</td>
<td align="right">10.0%</td>
<td align="right">334,342,215</td>
<td align="right">6.5%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,403,248,975</td>
<td align="right">27.0%</td>
<td align="right">962,957,569</td>
<td align="right">18.7%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,062,829,265</td>
<td align="right">39.6%</td>
<td align="right">2,619,720,929</td>
<td align="right">50.8%</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">632,508,215</td>
<td align="right">10.7%</td>
<td align="right">469,555,070</td>
<td align="right">7.8%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,125,857,494</td>
<td align="right">35.8%</td>
<td align="right">2,511,038,661</td>
<td align="right">41.7%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,795,607,270</td>
<td align="right">30.3%</td>
<td align="right">1,513,457,250</td>
<td align="right">25.1%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">142,870,849</td>
<td align="right"></td>
<td align="right">124,685,148</td>
<td align="right"></td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">774,794</td>
<td align="right"></td>
<td align="right">681,719</td>
<td align="right"></td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,377,242,248</td>
<td align="right">23.2%</td>
<td align="right">1,526,187,284</td>
<td align="right">25.4%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,795,161</td>
<td align="right"></td>
<td align="right">2,552,969</td>
<td align="right"></td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,021,830</td>
<td align="right"></td>
<td align="right">1,872,243</td>
<td align="right"></td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,275</td>
<td align="right"></td>
<td align="right">818,907</td>
<td align="right"></td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">232,262,155</td>
<td align="right">45.1%</td>
<td align="right">222,168,758</td>
<td align="right">44.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">233,069,890</td>
<td align="right">45.2%</td>
<td align="right">223,001,616</td>
<td align="right">44.5%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">245,716,314</td>
<td align="right"></td>
<td align="right">235,382,461</td>
<td align="right"></td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">262,511,657</td>
<td align="right"></td>
<td align="right">252,146,566</td>
<td align="right"></td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">799,126</td>
<td align="right">0.2%</td>
<td align="right">824,225</td>
<td align="right">0.2%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,217,197,696</td>
<td align="right">23.4%</td>
<td align="right">1,241,754,936</td>
<td align="right">24.1%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">282,467,366</td>
<td align="right">54.8%</td>
<td align="right">278,141,901</td>
<td align="right">55.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">282,499,652</td>
<td align="right"></td>
<td align="right">278,174,509</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,609</td>
<td align="right">0.0%</td>
<td align="right">8,633</td>
<td align="right">0.0%</td>
<td align="right">0.3%</td>
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
<td align="right">58,939</td>
<td align="right">48.9%</td>
<td align="right">155,192</td>
<td align="right">57.3%</td>
<td align="right">163.3%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">102</td>
<td align="right">0.2%</td>
<td align="right">256</td>
<td align="right">0.2%</td>
<td align="right">151.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,130</td>
<td align="right">0.9%</td>
<td align="right">2,809</td>
<td align="right">1.0%</td>
<td align="right">148.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">58,216</td>
<td align="right">48.3%</td>
<td align="right">139,964</td>
<td align="right">51.7%</td>
<td align="right">140.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">120,433</td>
<td align="right"></td>
<td align="right">270,776</td>
<td align="right"></td>
<td align="right">124.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">62,217</td>
<td align="right">51.7%</td>
<td align="right">130,812</td>
<td align="right">48.3%</td>
<td align="right">110.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">283,712,802</td>
<td align="right"></td>
<td align="right">455,794,646</td>
<td align="right"></td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,345</td>
<td align="right">1.1%</td>
<td align="right">2,118</td>
<td align="right">0.8%</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,299,082,100</td>
<td align="right">1,515.3%</td>
<td align="right">6,477,459,254</td>
<td align="right">1,421.1%</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">407</td>
<td align="right">0.3%</td>
<td align="right">364</td>
<td align="right">0.1%</td>
<td align="right">-10.6%</td>
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
<td align="right">55,230</td>
<td align="right">94.9%</td>
<td align="right">136,545</td>
<td align="right">97.6%</td>
<td align="right">147.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">58,216</td>
<td align="right"></td>
<td align="right">139,964</td>
<td align="right"></td>
<td align="right">140.4%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">15</td>
<td align="right">0.0%</td>
<td align="right">87.5%</td>
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
<td align="right">3,503</td>
<td align="right">2.5%</td>
<td align="right">3,503 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">5,067</td>
<td align="right">8.7%</td>
<td align="right">10,302</td>
<td align="right">7.4%</td>
<td align="right">103.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,549</td>
<td align="right">14.7%</td>
<td align="right">23,987</td>
<td align="right">17.1%</td>
<td align="right">180.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">23,703</td>
<td align="right">40.7%</td>
<td align="right">53,692</td>
<td align="right">38.4%</td>
<td align="right">126.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">13,773</td>
<td align="right">23.7%</td>
<td align="right">32,727</td>
<td align="right">23.4%</td>
<td align="right">137.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">6,382</td>
<td align="right">11.0%</td>
<td align="right">13,606</td>
<td align="right">9.7%</td>
<td align="right">113.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">742</td>
<td align="right">1.3%</td>
<td align="right">2,147</td>
<td align="right">1.5%</td>
<td align="right">189.4%</td>
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
<td align="right">3,164</td>
<td align="right">5.4%</td>
<td align="right">10,504</td>
<td align="right">7.5%</td>
<td align="right">232.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">4,435</td>
<td align="right">7.6%</td>
<td align="right">7,504</td>
<td align="right">5.4%</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">13,697</td>
<td align="right">23.5%</td>
<td align="right">42,522</td>
<td align="right">30.4%</td>
<td align="right">210.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">21,780</td>
<td align="right">37.4%</td>
<td align="right">47,747</td>
<td align="right">34.1%</td>
<td align="right">119.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,758</td>
<td align="right">18.5%</td>
<td align="right">24,034</td>
<td align="right">17.2%</td>
<td align="right">123.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,364</td>
<td align="right">2.3%</td>
<td align="right">3,788</td>
<td align="right">2.7%</td>
<td align="right">177.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">32</td>
<td align="right">0.1%</td>
<td align="right">446</td>
<td align="right">0.3%</td>
<td align="right">1,293.8%</td>
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
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,504</td>
<td align="right">1,288,192</td>
<td align="right">85,551.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">336</td>
<td align="right">174,596</td>
<td align="right">51,863.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">285</td>
<td align="right">89,160</td>
<td align="right">31,184.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,392</td>
<td align="right">290,479</td>
<td align="right">12,043.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,287</td>
<td align="right">269,474</td>
<td align="right">11,682.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">3,084</td>
<td align="right">159,443</td>
<td align="right">5,070.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">396</td>
<td align="right">14,753</td>
<td align="right">3,625.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">441,011</td>
<td align="right">10,580,257</td>
<td align="right">2,299.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">294,621</td>
<td align="right">7,047,448</td>
<td align="right">2,292.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">294,778</td>
<td align="right">7,047,764</td>
<td align="right">2,290.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">31,665</td>
<td align="right">650,305</td>
<td align="right">1,953.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">472,782</td>
<td align="right">9,273,272</td>
<td align="right">1,861.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">8,746,256</td>
<td align="right">168,983,505</td>
<td align="right">1,832.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">847</td>
<td align="right">14,049</td>
<td align="right">1,558.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">131,495</td>
<td align="right">2,088,723</td>
<td align="right">1,488.4%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">20,001</td>
<td align="right">310,896</td>
<td align="right">1,454.4%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">20,001</td>
<td align="right">310,892</td>
<td align="right">1,454.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">285,999</td>
<td align="right">4,424,079</td>
<td align="right">1,446.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">285,999</td>
<td align="right">4,401,345</td>
<td align="right">1,438.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">62</td>
<td align="right">944</td>
<td align="right">1,422.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">4,535</td>
<td align="right">65,619</td>
<td align="right">1,346.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">758,465</td>
<td align="right">10,938,764</td>
<td align="right">1,342.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">322,470</td>
<td align="right">3,051,984</td>
<td align="right">846.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">24,690</td>
<td align="right">183,966</td>
<td align="right">645.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">620,299</td>
<td align="right">4,261,048</td>
<td align="right">586.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">480,659</td>
<td align="right">3,241,378</td>
<td align="right">574.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">981,914</td>
<td align="right">6,154,755</td>
<td align="right">526.8%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">914,642</td>
<td align="right">5,371,460</td>
<td align="right">487.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">252</td>
<td align="right">1,196</td>
<td align="right">374.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">17,849</td>
<td align="right">84,343</td>
<td align="right">372.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">1,176,179</td>
<td align="right">4,287,569</td>
<td align="right">264.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">64,497</td>
<td align="right">220,103</td>
<td align="right">241.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">552</td>
<td align="right">1,798</td>
<td align="right">225.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">334,936</td>
<td align="right">1,063,857</td>
<td align="right">217.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">334,936</td>
<td align="right">1,063,857</td>
<td align="right">217.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">10,286,612</td>
<td align="right">31,699,025</td>
<td align="right">208.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">35,535,476</td>
<td align="right">105,074,198</td>
<td align="right">195.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">36,885,537</td>
<td align="right">106,261,640</td>
<td align="right">188.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">5,244,190</td>
<td align="right">13,638,950</td>
<td align="right">160.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,476,382</td>
<td align="right">3,701,568</td>
<td align="right">150.7%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">25,710,751</td>
<td align="right">61,093,437</td>
<td align="right">137.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">13,049,871</td>
<td align="right">29,961,735</td>
<td align="right">129.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">10,452,318</td>
<td align="right">23,695,659</td>
<td align="right">126.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">106,608,073</td>
<td align="right">234,309,305</td>
<td align="right">119.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">286</td>
<td align="right">622</td>
<td align="right">117.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,943,563</td>
<td align="right">14,994,791</td>
<td align="right">116.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">6,396,849</td>
<td align="right">13,775,190</td>
<td align="right">115.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">31,608,065</td>
<td align="right">67,747,381</td>
<td align="right">114.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,794,871</td>
<td align="right">8,063,651</td>
<td align="right">112.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">782,690</td>
<td align="right">1,659,527</td>
<td align="right">112.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,358,042</td>
<td align="right">21,749,789</td>
<td align="right">110.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,860,658</td>
<td align="right">8,064,803</td>
<td align="right">108.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">3,450,384</td>
<td align="right">7,125,500</td>
<td align="right">106.5%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">236,299</td>
<td align="right">487,651</td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,541,718</td>
<td align="right">5,236,020</td>
<td align="right">106.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,878,815</td>
<td align="right">7,875,857</td>
<td align="right">103.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">36,027,260</td>
<td align="right">72,975,769</td>
<td align="right">102.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">18,627,401</td>
<td align="right">37,649,592</td>
<td align="right">102.1%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">157</td>
<td align="right">316</td>
<td align="right">101.3%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">157</td>
<td align="right">316</td>
<td align="right">101.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,641,949</td>
<td align="right">3,302,168</td>
<td align="right">101.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,776</td>
<td align="right">3,568</td>
<td align="right">100.9%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,776</td>
<td align="right">3,568</td>
<td align="right">100.9%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">888</td>
<td align="right">1,784</td>
<td align="right">100.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">11,036,733</td>
<td align="right">22,106,700</td>
<td align="right">100.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">53,650,390</td>
<td align="right">21,730</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">87,841,609</td>
<td align="right">172,800,110</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">8,981,138</td>
<td align="right">17,632,871</td>
<td align="right">96.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">894,836</td>
<td align="right">38,271</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">36,519,532</td>
<td align="right">71,337,875</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">61,049,325</td>
<td align="right">119,111,980</td>
<td align="right">95.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">36,420,681</td>
<td align="right">70,921,386</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,479,160</td>
<td align="right">2,844,568</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">1,340</td>
<td align="right">2,532</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">36,137,416</td>
<td align="right">68,149,531</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,548,849</td>
<td align="right">14,213,314</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,548,849</td>
<td align="right">14,213,314</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">534,971</td>
<td align="right">996,067</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">6,023,763</td>
<td align="right">11,166,466</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">34,416,054</td>
<td align="right">63,003,199</td>
<td align="right">83.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">4,180,853</td>
<td align="right">7,397,076</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">756,301</td>
<td align="right">1,333,753</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">7,219,008</td>
<td align="right">1,731,460</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">45,915,438</td>
<td align="right">80,313,127</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">17,292,570</td>
<td align="right">29,173,875</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">6,900</td>
<td align="right">2,181</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">3,884,077</td>
<td align="right">6,533,207</td>
<td align="right">68.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">20,306,671</td>
<td align="right">34,046,707</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">11,197,729</td>
<td align="right">18,647,551</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">11,465,156</td>
<td align="right">19,070,663</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,516</td>
<td align="right">2,501</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">31,284,674</td>
<td align="right">51,246,710</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">18,858,063</td>
<td align="right">30,650,483</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,484,358</td>
<td align="right">560,215</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,484,358</td>
<td align="right">560,215</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">29,402,777</td>
<td align="right">47,390,290</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">283,712,802</td>
<td align="right">455,794,646</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">341,044</td>
<td align="right">136,137</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">156,867,139</td>
<td align="right">249,980,546</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">17,447,337</td>
<td align="right">27,394,626</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">190,957</td>
<td align="right">293,710</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">257,735,140</td>
<td align="right">394,177,269</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">315,752,285</td>
<td align="right">479,852,158</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">889</td>
<td align="right">1,331</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">21,396,133</td>
<td align="right">31,737,702</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">16,077,194</td>
<td align="right">23,375,177</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">10,900,917</td>
<td align="right">15,551,028</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">402,873,566</td>
<td align="right">563,115,880</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">18,086,739</td>
<td align="right">25,115,785</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">78,201,607</td>
<td align="right">108,259,729</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">15,567,151</td>
<td align="right">21,509,472</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,706,218</td>
<td align="right">2,343,358</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">319,187,303</td>
<td align="right">436,936,377</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">4,105</td>
<td align="right">2,604</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">76,592</td>
<td align="right">102,996</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">27,810,148</td>
<td align="right">37,375,331</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,047,919</td>
<td align="right">2,054,412</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">5,867,044</td>
<td align="right">7,669,855</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,747,350</td>
<td align="right">3,544,805</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,302,352</td>
<td align="right">1,675,136</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,264,332</td>
<td align="right">15,469,619</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">12,935,726</td>
<td align="right">16,215,677</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">12,935,726</td>
<td align="right">16,215,677</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">97,212,275</td>
<td align="right">121,766,506</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,196,848</td>
<td align="right">2,744,249</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">32,039,483</td>
<td align="right">24,057,512</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">45,674,030</td>
<td align="right">57,009,122</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">79,929,073</td>
<td align="right">99,752,593</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">48,961,766</td>
<td align="right">60,837,185</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">7,885,078</td>
<td align="right">9,786,152</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">7,398,325</td>
<td align="right">5,659,060</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">37,717,473</td>
<td align="right">46,573,908</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">7,462,004</td>
<td align="right">9,199,162</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">23,071,079</td>
<td align="right">17,703,934</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">7,982,639</td>
<td align="right">6,135,610</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">7,982,639</td>
<td align="right">6,135,610</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">3,478,149</td>
<td align="right">4,256,994</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">46,067,468</td>
<td align="right">56,248,845</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">2,384</td>
<td align="right">2,853</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">2,384</td>
<td align="right">2,853</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">30,612</td>
<td align="right">36,289</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">4,203,952</td>
<td align="right">4,971,410</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">11,564,819</td>
<td align="right">13,513,128</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">10,663,595</td>
<td align="right">8,891,644</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">286,755</td>
<td align="right">334,342</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">28,298,615</td>
<td align="right">32,727,214</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">11,417,194</td>
<td align="right">13,033,588</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">172,641,585</td>
<td align="right">196,941,375</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">34,450,763</td>
<td align="right">38,915,644</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,975,498</td>
<td align="right">5,619,808</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">317,528</td>
<td align="right">358,536</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">13,789,488</td>
<td align="right">12,061,618</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">21,081,988</td>
<td align="right">18,459,878</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">16,043,589</td>
<td align="right">14,106,290</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">671,394</td>
<td align="right">746,058</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,551,828</td>
<td align="right">20,566,407</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">25,476,479</td>
<td align="right">28,241,958</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">14,421,624</td>
<td align="right">15,835,933</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">8,209,665</td>
<td align="right">7,471,394</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">18,532,258</td>
<td align="right">20,139,036</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">2,519,583</td>
<td align="right">2,317,553</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">11,989,092</td>
<td align="right">11,048,343</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,474,245</td>
<td align="right">5,891,842</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">491,965</td>
<td align="right">529,392</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">491,965</td>
<td align="right">529,392</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">670,294</td>
<td align="right">721,059</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">40,840,348</td>
<td align="right">37,926,159</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">31,900,427</td>
<td align="right">29,683,239</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">14,196,496</td>
<td align="right">15,055,131</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">40,012,287</td>
<td align="right">37,872,408</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">862,234</td>
<td align="right">817,939</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">20,617,337</td>
<td align="right">19,647,434</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">654,278</td>
<td align="right">628,885</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">19,837,481</td>
<td align="right">20,303,073</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">132,992</td>
<td align="right">135,724</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">15,772,679</td>
<td align="right">15,470,791</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">57,754,867</td>
<td align="right">58,712,855</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">60,823,648</td>
<td align="right">61,809,514</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">1,839</td>
<td align="right">1,820</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">48,779,853</td>
<td align="right">48,350,815</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">13,413,380</td>
<td align="right">13,346,165</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">5,346</td>
<td align="right">5,327</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,848,064</td>
<td align="right">7,820,502</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">47,411,154</td>
<td align="right">47,449,730</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,515,029</td>
<td align="right">2,515,292</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,036,151</td>
<td align="right">1,036,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">937,876</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">937,678</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">925,549</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">846,539</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">846,539</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right"></td>
<td align="right">846,539</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right"></td>
<td align="right">356,520</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right"></td>
<td align="right">355,673</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">116,242</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right"></td>
<td align="right">110,749</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right"></td>
<td align="right">22,734</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">183</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">92</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">37</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right"></td>
<td align="right">7</td>
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
<td align="left">RAISE_VARARGS</td>
<td align="right">364</td>
<td align="right">638</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">10,930</td>
<td align="right">18,976</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,613</td>
<td align="right">7,993</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">278</td>
<td align="right">295</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">64</td>
<td align="right">64</td>
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
<td align="right">4</td>
<td align="right">4</td>
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
<td align="right">4</td>
<td align="right">4</td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-23
