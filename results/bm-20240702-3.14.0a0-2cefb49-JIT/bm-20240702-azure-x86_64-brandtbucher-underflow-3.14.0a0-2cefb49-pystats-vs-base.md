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
<td align="left">UNARY_NOT</td>
<td align="right">8,357,552</td>
<td align="right">36,884,037</td>
<td align="right">341.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">81,682,682</td>
<td align="right">1,486,747</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">334,209,893</td>
<td align="right">31,930,420</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,411,421</td>
<td align="right">727,306</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68,000,940</td>
<td align="right">17,927,990</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">118,740,764</td>
<td align="right">32,403,629</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">294,705,193</td>
<td align="right">87,123,345</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">49,289,802</td>
<td align="right">16,693,880</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,763,227</td>
<td align="right">22,740,130</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">66,953,723</td>
<td align="right">23,113,166</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,264,258</td>
<td align="right">31,834,351</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">146,449,176</td>
<td align="right">56,276,170</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,101,356</td>
<td align="right">18,863,817</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,461,660</td>
<td align="right">3,047,800</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,636,927</td>
<td align="right">43,362,565</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">59,218,322</td>
<td align="right">26,586,643</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,588,899</td>
<td align="right">57,648,772</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,362</td>
<td align="right">88,203,381</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">79,282,163</td>
<td align="right">37,525,242</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">214,581,775</td>
<td align="right">102,051,709</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">803,777,427</td>
<td align="right">388,238,856</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">404,145,744</td>
<td align="right">195,642,635</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,804,991</td>
<td align="right">38,076,213</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">222,980</td>
<td align="right">119,207</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">114,863,042</td>
<td align="right">61,790,133</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">210,432,688</td>
<td align="right">115,885,324</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">386,018,873</td>
<td align="right">216,413,935</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">298,250,253</td>
<td align="right">178,355,262</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">385,609,250</td>
<td align="right">232,965,847</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,371,101,062</td>
<td align="right">831,618,945</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">440,300</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,142,641</td>
<td align="right">56,491,808</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">173,188,709</td>
<td align="right">109,819,486</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,247,916</td>
<td align="right">40,388,610</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">87,769,033</td>
<td align="right">56,959,952</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">230,664,610</td>
<td align="right">150,049,809</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,877,686</td>
<td align="right">6,484,830</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,420</td>
<td align="right">115,832</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,098,269,674</td>
<td align="right">2,759,233,571</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,808,661</td>
<td align="right">21,562,901</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">24,142,297</td>
<td align="right">16,405,828</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">100,345,617</td>
<td align="right">68,258,196</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,385,176</td>
<td align="right">7,166,276</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,451,701</td>
<td align="right">57,171,534</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">194,479,637</td>
<td align="right">135,126,866</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">636,688,192</td>
<td align="right">442,614,884</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">21,172,796</td>
<td align="right">14,795,804</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">409,256,905</td>
<td align="right">288,809,282</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">76,286,312</td>
<td align="right">53,952,895</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,104,613,021</td>
<td align="right">2,926,027,035</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,672,300,496</td>
<td align="right">4,098,418,091</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,550,970</td>
<td align="right">34,528,716</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,399,820,452</td>
<td align="right">1,758,363,370</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,294,945,073</td>
<td align="right">2,434,083,225</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">140,540,021</td>
<td align="right">104,142,106</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,410,665,281</td>
<td align="right">1,047,509,350</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">135,755,200</td>
<td align="right">100,973,856</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">142,537,682</td>
<td align="right">106,089,338</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,714,481</td>
<td align="right">53,632,713</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">42,435,517</td>
<td align="right">31,902,554</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">30,785,532</td>
<td align="right">23,249,162</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">199,227,492</td>
<td align="right">150,501,884</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,871,088,879</td>
<td align="right">1,420,627,810</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">108,592,655</td>
<td align="right">84,062,579</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">35,526,971</td>
<td align="right">27,647,514</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">4,716,218</td>
<td align="right">3,721,131</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">907,886,373</td>
<td align="right">719,657,234</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,222,743,681</td>
<td align="right">4,997,005,411</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">828,627,866</td>
<td align="right">672,596,461</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,240,444,558</td>
<td align="right">3,449,944,720</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,611,089,010</td>
<td align="right">17,623,027,133</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">162,000,736</td>
<td align="right">133,436,840</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">201,453,046</td>
<td align="right">165,967,118</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">59,677,580</td>
<td align="right">49,226,221</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">378,229,624</td>
<td align="right">313,047,026</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">366,813,344</td>
<td align="right">304,597,740</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,016,771,133</td>
<td align="right">846,926,818</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">677,180,472</td>
<td align="right">565,304,231</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,451,032,886</td>
<td align="right">2,046,336,091</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">348,124,146</td>
<td align="right">291,962,349</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,489,106,446</td>
<td align="right">4,610,708,297</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">195,635,477</td>
<td align="right">165,543,749</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">739,592,456</td>
<td align="right">627,040,317</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,525,743,769</td>
<td align="right">2,996,884,958</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">283,352,996</td>
<td align="right">241,296,476</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">452,636,213</td>
<td align="right">386,580,797</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">331,590,179</td>
<td align="right">287,039,367</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">485,240</td>
<td align="right">421,840</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,259,834,825</td>
<td align="right">1,098,442,534</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">901,814,696</td>
<td align="right">787,409,012</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,109,786,915</td>
<td align="right">972,081,406</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,998,854,364</td>
<td align="right">5,262,480,641</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,818,198,454</td>
<td align="right">2,491,550,833</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,137,025,674</td>
<td align="right">1,005,813,403</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">942,143,708</td>
<td align="right">833,871,051</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">318,139,618</td>
<td align="right">283,536,955</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">679,742,740</td>
<td align="right">608,849,566</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">138,058,623</td>
<td align="right">124,419,665</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">666,565,497</td>
<td align="right">602,205,394</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,819,132</td>
<td align="right">36,923,675</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,568,258,883</td>
<td align="right">1,418,900,332</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">431,663,764</td>
<td align="right">392,541,155</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">385,202,810</td>
<td align="right">350,430,369</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,105,024</td>
<td align="right">84,016,209</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,913,558</td>
<td align="right">137,556,116</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,947,810</td>
<td align="right">370,535,467</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,872,699</td>
<td align="right">75,402,946</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,365,472</td>
<td align="right">2,205,512</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">556,449,862</td>
<td align="right">520,004,281</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">198,600,474</td>
<td align="right">185,764,712</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">20,422,358</td>
<td align="right">19,204,238</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">486,450,449</td>
<td align="right">457,539,731</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">56,501,392</td>
<td align="right">53,258,212</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">791,276,282</td>
<td align="right">746,654,343</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">219,498</td>
<td align="right">207,579</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">272,673,961</td>
<td align="right">257,875,837</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,373,998,061</td>
<td align="right">4,137,676,189</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">54,270,958</td>
<td align="right">51,498,981</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">276,487,304</td>
<td align="right">289,337,848</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,866,729</td>
<td align="right">3,693,320</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">166,847,458</td>
<td align="right">159,477,746</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,297,223</td>
<td align="right">207,440,336</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,910,919</td>
<td align="right">140,981,345</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">421,590,441</td>
<td align="right">406,417,191</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,850,607</td>
<td align="right">51,968,108</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,569,243</td>
<td align="right">153,078,620</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,290,129,590</td>
<td align="right">1,249,187,444</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,152,174</td>
<td align="right">20,515,029</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,024,186</td>
<td align="right">392,932,029</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,168,547</td>
<td align="right">227,955,482</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,584</td>
<td align="right">1,842,867</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">773,991,890</td>
<td align="right">762,321,374</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,466,248</td>
<td align="right">17,212,062</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">205,801,317</td>
<td align="right">203,171,778</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">481,502,567</td>
<td align="right">477,952,730</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,612,128</td>
<td align="right">46,426,132</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,644,791,915</td>
<td align="right">2,654,860,249</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">108,507,865</td>
<td align="right">108,199,257</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,380,686</td>
<td align="right">1,044,789,517</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,165,260</td>
<td align="right">91,941,500</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,447,100</td>
<td align="right">94,223,340</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">228,049,185</td>
<td align="right">227,775,946</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,641,564</td>
<td align="right">225,438,790</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,603,445,886</td>
<td align="right">1,602,293,189</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,958</td>
<td align="right">687,708</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,229,348</td>
<td align="right">274,301,582</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,693,789</td>
<td align="right">20,697,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,659,148</td>
<td align="right">9,657,288</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,159,934</td>
<td align="right">21,163,948</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,961,784</td>
<td align="right">10,959,869</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,237,103</td>
<td align="right">9,235,609</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,809,121</td>
<td align="right">1,808,858</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">484,955,459</td>
<td align="right">484,912,077</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,884</td>
<td align="right">14,885</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,639,873</td>
<td align="right">3,639,961</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,950,802</td>
<td align="right">5,950,716</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,906,038</td>
<td align="right">555,910,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,344,679</td>
<td align="right">20,344,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,338,310</td>
<td align="right">233,338,346</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,220,538</td>
<td align="right">786,220,512</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,319,344</td>
<td align="right">173,319,340</td>
<td align="right">-0.0%</td>
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
<td align="left">SET_ADD</td>
<td align="right">46,620</td>
<td align="right">46,620</td>
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
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
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
<td align="right">0.3%</td>
<td align="right">20,045,820</td>
<td align="right">0.2%</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">437,037,758</td>
<td align="right">4.4%</td>
<td align="right">307,446,774</td>
<td align="right">3.2%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,428,332,621</td>
<td align="right">95.6%</td>
<td align="right">9,402,558,013</td>
<td align="right">96.8%</td>
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
<td align="right">597,564</td>
<td align="right">34.7%</td>
<td align="right">419,183</td>
<td align="right">29.8%</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,122,503</td>
<td align="right">65.3%</td>
<td align="right">989,145</td>
<td align="right">70.2%</td>
<td align="right">-11.9%</td>
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
<td align="right">48,678</td>
<td align="right">4.3%</td>
<td align="right">21,753</td>
<td align="right">2.2%</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,026</td>
<td align="right">0.4%</td>
<td align="right">2,546</td>
<td align="right">0.3%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,402</td>
<td align="right">7.3%</td>
<td align="right">53,923</td>
<td align="right">5.5%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,534</td>
<td align="right">0.5%</td>
<td align="right">3,725</td>
<td align="right">0.4%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,321</td>
<td align="right">4.3%</td>
<td align="right">35,524</td>
<td align="right">3.6%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,722</td>
<td align="right">0.4%</td>
<td align="right">3,664</td>
<td align="right">0.4%</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,882</td>
<td align="right">0.8%</td>
<td align="right">6,904</td>
<td align="right">0.7%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">13,623</td>
<td align="right">1.2%</td>
<td align="right">10,622</td>
<td align="right">1.1%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">0.9%</td>
<td align="right">9,220</td>
<td align="right">0.9%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,420</td>
<td align="right">0.2%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,264</td>
<td align="right">2.8%</td>
<td align="right">28,264</td>
<td align="right">2.9%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,607</td>
<td align="right">69.6%</td>
<td align="right">733,970</td>
<td align="right">74.2%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,388</td>
<td align="right">2.9%</td>
<td align="right">30,511</td>
<td align="right">3.1%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,500</td>
<td align="right">0.9%</td>
<td align="right">10,130</td>
<td align="right">1.0%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">22,652</td>
<td align="right">2.0%</td>
<td align="right">22,412</td>
<td align="right">2.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,657</td>
<td align="right">0.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,918</td>
<td align="right">0.2%</td>
<td align="right">1,912</td>
<td align="right">0.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,606</td>
<td align="right">0.8%</td>
<td align="right">8,588</td>
<td align="right">0.9%</td>
<td align="right">-0.2%</td>
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
<td align="right">743,980,833</td>
<td align="right">10.8%</td>
<td align="right">631,458,215</td>
<td align="right">9.3%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,149,784,073</td>
<td align="right">89.2%</td>
<td align="right">6,133,119,321</td>
<td align="right">90.7%</td>
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
<td align="right">4,810,131</td>
<td align="right">0.1%</td>
<td align="right">4,808,946</td>
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
<td align="right">240,202</td>
<td align="right">57.0%</td>
<td align="right">209,507</td>
<td align="right">53.6%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,552</td>
<td align="right">43.0%</td>
<td align="right">181,541</td>
<td align="right">46.4%</td>
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
<td align="left">buffer int</td>
<td align="right">30,499</td>
<td align="right">12.7%</td>
<td align="right">19,100</td>
<td align="right">9.1%</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">55,960</td>
<td align="right">23.3%</td>
<td align="right">40,580</td>
<td align="right">19.4%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">6.7%</td>
<td align="right">13,220</td>
<td align="right">6.3%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.2%</td>
<td align="right">5,000</td>
<td align="right">2.4%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
<td align="right">1,100</td>
<td align="right">0.5%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">122</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">110,441</td>
<td align="right">46.0%</td>
<td align="right">109,983</td>
<td align="right">52.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,500</td>
<td align="right">8.1%</td>
<td align="right">19,500</td>
<td align="right">9.3%</td>
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
<td align="right">22,460</td>
<td align="right">0.0%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">181,260,247</td>
<td align="right">1.3%</td>
<td align="right">147,360,570</td>
<td align="right">1.0%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">662,107,381</td>
<td align="right">4.6%</td>
<td align="right">628,803,747</td>
<td align="right">4.4%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,665,861,215</td>
<td align="right">95.4%</td>
<td align="right">13,680,259,543</td>
<td align="right">95.6%</td>
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
<td align="right">3,942,967</td>
<td align="right">96.0%</td>
<td align="right">3,303,598</td>
<td align="right">95.2%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">165,358</td>
<td align="right">4.0%</td>
<td align="right">165,302</td>
<td align="right">4.8%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">155,858</td>
<td align="right">94.3%</td>
<td align="right">155,802</td>
<td align="right">94.3%</td>
<td align="right">-0.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">101,191,248</td>
<td align="right">1.6%</td>
<td align="right">69,099,184</td>
<td align="right">1.1%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,071,565</td>
<td align="right">0.0%</td>
<td align="right">1,056,468</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,122,643,303</td>
<td align="right">98.4%</td>
<td align="right">6,105,337,078</td>
<td align="right">98.9%</td>
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
<td align="right">149,731</td>
<td align="right">66.3%</td>
<td align="right">139,598</td>
<td align="right">64.8%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">76,203</td>
<td align="right">33.7%</td>
<td align="right">75,882</td>
<td align="right">35.2%</td>
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
<td align="left">float long</td>
<td align="right">14,377</td>
<td align="right">9.6%</td>
<td align="right">8,847</td>
<td align="right">6.3%</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.4%</td>
<td align="right">480</td>
<td align="right">0.3%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,600</td>
<td align="right">1.7%</td>
<td align="right">2,220</td>
<td align="right">1.6%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">840</td>
<td align="right">0.6%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,020</td>
<td align="right">12.7%</td>
<td align="right">17,720</td>
<td align="right">12.7%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,184</td>
<td align="right">8.1%</td>
<td align="right">11,516</td>
<td align="right">8.2%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,693</td>
<td align="right">11.1%</td>
<td align="right">15,855</td>
<td align="right">11.4%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,428</td>
<td align="right">1.0%</td>
<td align="right">1,384</td>
<td align="right">1.0%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">42,519</td>
<td align="right">28.4%</td>
<td align="right">41,742</td>
<td align="right">29.9%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,070</td>
<td align="right">18.1%</td>
<td align="right">26,694</td>
<td align="right">19.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">10,680</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,620</td>
<td align="right">1.1%</td>
<td align="right">1,620</td>
<td align="right">1.2%</td>
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
<td align="right">208,172,737</td>
<td align="right">7.7%</td>
<td align="right">205,519,154</td>
<td align="right">7.6%</td>
<td align="right">-1.3%</td>
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
<td align="right">2,517,680</td>
<td align="right">0.1%</td>
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
<td align="right">2,489,645,383</td>
<td align="right">92.3%</td>
<td align="right">2,485,230,782</td>
<td align="right">92.4%</td>
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
<td align="left">Failure</td>
<td align="right">113,700</td>
<td align="right">65.0%</td>
<td align="right">109,764</td>
<td align="right">64.5%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,120</td>
<td align="right">35.0%</td>
<td align="right">60,540</td>
<td align="right">35.5%</td>
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
<td align="left">tuple</td>
<td align="right">27,499</td>
<td align="right">24.2%</td>
<td align="right">24,940</td>
<td align="right">22.7%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">13,940</td>
<td align="right">12.3%</td>
<td align="right">13,338</td>
<td align="right">12.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,721</td>
<td align="right">13.8%</td>
<td align="right">15,106</td>
<td align="right">13.8%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">56,540</td>
<td align="right">49.7%</td>
<td align="right">56,380</td>
<td align="right">51.4%</td>
<td align="right">-0.3%</td>
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
<td align="right">547,174,277</td>
<td align="right">53.1%</td>
<td align="right">428,908,073</td>
<td align="right">47.2%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,588,465</td>
<td align="right">0.3%</td>
<td align="right">2,559,309</td>
<td align="right">0.3%</td>
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
<td align="right">483,797,468</td>
<td align="right">46.9%</td>
<td align="right">480,221,266</td>
<td align="right">52.8%</td>
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
<td align="left">Failure</td>
<td align="right">197,004</td>
<td align="right">67.1%</td>
<td align="right">194,778</td>
<td align="right">67.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">96,560</td>
<td align="right">32.9%</td>
<td align="right">95,995</td>
<td align="right">33.0%</td>
<td align="right">-0.6%</td>
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
<td align="left">set</td>
<td align="right">10,293</td>
<td align="right">5.2%</td>
<td align="right">9,494</td>
<td align="right">4.9%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,840</td>
<td align="right">1.9%</td>
<td align="right">3,620</td>
<td align="right">1.9%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,060</td>
<td align="right">2.1%</td>
<td align="right">3,840</td>
<td align="right">2.0%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,100</td>
<td align="right">2.6%</td>
<td align="right">4,980</td>
<td align="right">2.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,291</td>
<td align="right">5.7%</td>
<td align="right">11,043</td>
<td align="right">5.7%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">37,142</td>
<td align="right">18.9%</td>
<td align="right">36,581</td>
<td align="right">18.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,300</td>
<td align="right">3.2%</td>
<td align="right">6,260</td>
<td align="right">3.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,220</td>
<td align="right">2.1%</td>
<td align="right">4,200</td>
<td align="right">2.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">618</td>
<td align="right">0.3%</td>
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,960</td>
<td align="right">53.3%</td>
<td align="right">104,960</td>
<td align="right">53.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,480</td>
<td align="right">3.3%</td>
<td align="right">6,480</td>
<td align="right">3.3%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">320,000</td>
<td align="right">0.0%</td>
<td align="right">146,440</td>
<td align="right">0.0%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">419,073,273</td>
<td align="right">2.4%</td>
<td align="right">316,991,669</td>
<td align="right">1.8%</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,519,370,478</td>
<td align="right">8.6%</td>
<td align="right">1,281,559,980</td>
<td align="right">7.4%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,088,193,665</td>
<td align="right">91.3%</td>
<td align="right">15,919,567,735</td>
<td align="right">92.5%</td>
<td align="right">-1.0%</td>
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
<td align="right">8,517,409</td>
<td align="right">89.8%</td>
<td align="right">6,592,125</td>
<td align="right">87.7%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">972,301</td>
<td align="right">10.2%</td>
<td align="right">920,970</td>
<td align="right">12.3%</td>
<td align="right">-5.3%</td>
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
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,755</td>
<td align="right">1.8%</td>
<td align="right">13,826</td>
<td align="right">1.5%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,303</td>
<td align="right">9.0%</td>
<td align="right">78,236</td>
<td align="right">8.5%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">263,182</td>
<td align="right">27.1%</td>
<td align="right">242,971</td>
<td align="right">26.4%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,840</td>
<td align="right">1.6%</td>
<td align="right">14,657</td>
<td align="right">1.6%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,380</td>
<td align="right">1.5%</td>
<td align="right">13,520</td>
<td align="right">1.5%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">102,088</td>
<td align="right">10.5%</td>
<td align="right">96,017</td>
<td align="right">10.4%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,582</td>
<td align="right">0.6%</td>
<td align="right">5,260</td>
<td align="right">0.6%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,880</td>
<td align="right">2.8%</td>
<td align="right">25,460</td>
<td align="right">2.8%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,840</td>
<td align="right">0.3%</td>
<td align="right">2,700</td>
<td align="right">0.3%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">164,798</td>
<td align="right">16.9%</td>
<td align="right">158,981</td>
<td align="right">17.3%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">75,378</td>
<td align="right">7.8%</td>
<td align="right">74,086</td>
<td align="right">8.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,340</td>
<td align="right">2.1%</td>
<td align="right">20,033</td>
<td align="right">2.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">156,135</td>
<td align="right">16.1%</td>
<td align="right">155,503</td>
<td align="right">16.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.3%</td>
<td align="right">12,240</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,400</td>
<td align="right">0.6%</td>
<td align="right">5,400</td>
<td align="right">0.6%</td>
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
<td align="right">5,847,306,104</td>
<td align="right">99.6%</td>
<td align="right">4,658,265,993</td>
<td align="right">99.6%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">438,602</td>
<td align="right">0.0%</td>
<td align="right">436,515</td>
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
<td align="right">20,320,609</td>
<td align="right">0.3%</td>
<td align="right">20,318,624</td>
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
<td align="right">462,672</td>
<td align="right">100.0%</td>
<td align="right">462,611</td>
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
<td align="right">83,711,740</td>
<td align="right">100.0%</td>
<td align="right">83,551,337</td>
<td align="right">100.0%</td>
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
<td align="right">7,464</td>
<td align="right">0.0%</td>
<td align="right">7,465</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">786,189,878</td>
<td align="right">81.9%</td>
<td align="right">786,189,852</td>
<td align="right">81.9%</td>
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
<td align="right">173,284,924</td>
<td align="right">18.1%</td>
<td align="right">173,284,920</td>
<td align="right">18.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">139,438,393</td>
<td align="right">4.8%</td>
<td align="right">124,649,968</td>
<td align="right">4.3%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">190,470,433</td>
<td align="right">6.5%</td>
<td align="right">174,080,900</td>
<td align="right">6.0%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,724,899,622</td>
<td align="right">93.4%</td>
<td align="right">2,724,704,314</td>
<td align="right">93.9%</td>
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
<td align="right">2,726,543</td>
<td align="right">96.7%</td>
<td align="right">2,447,610</td>
<td align="right">96.5%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">92,024</td>
<td align="right">3.3%</td>
<td align="right">89,566</td>
<td align="right">3.5%</td>
<td align="right">-2.7%</td>
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
<td align="left">no dict</td>
<td align="right">4,940</td>
<td align="right">5.4%</td>
<td align="right">4,638</td>
<td align="right">5.2%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,760</td>
<td align="right">9.5%</td>
<td align="right">8,260</td>
<td align="right">9.2%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">2,860</td>
<td align="right">3.1%</td>
<td align="right">2,720</td>
<td align="right">3.0%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,960</td>
<td align="right">15.2%</td>
<td align="right">13,394</td>
<td align="right">15.0%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">32,280</td>
<td align="right">35.1%</td>
<td align="right">31,326</td>
<td align="right">35.0%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,724</td>
<td align="right">10.6%</td>
<td align="right">9,728</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,480</td>
<td align="right">8.1%</td>
<td align="right">7,480</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,320</td>
<td align="right">6.9%</td>
<td align="right">6,320</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,780</td>
<td align="right">5.2%</td>
<td align="right">4,780</td>
<td align="right">5.3%</td>
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
<td align="right">232,058,579</td>
<td align="right">20.9%</td>
<td align="right">227,847,583</td>
<td align="right">20.7%</td>
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
<td align="right">877,148,402</td>
<td align="right">79.1%</td>
<td align="right">875,158,346</td>
<td align="right">79.3%</td>
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
<td align="right">99,964</td>
<td align="right">88.6%</td>
<td align="right">97,897</td>
<td align="right">88.4%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,904</td>
<td align="right">11.4%</td>
<td align="right">12,902</td>
<td align="right">11.6%</td>
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
<td align="right">1,480</td>
<td align="right">1.5%</td>
<td align="right">1,380</td>
<td align="right">1.4%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">6.5%</td>
<td align="right">6,120</td>
<td align="right">6.3%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">39,720</td>
<td align="right">39.7%</td>
<td align="right">38,200</td>
<td align="right">39.0%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,524</td>
<td align="right">7.5%</td>
<td align="right">7,437</td>
<td align="right">7.6%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,420</td>
<td align="right">43.4%</td>
<td align="right">43,420</td>
<td align="right">44.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,340</td>
<td align="right">1.3%</td>
<td align="right">1,340</td>
<td align="right">1.4%</td>
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
<td align="right">248,282,880</td>
<td align="right">3.9%</td>
<td align="right">183,978,722</td>
<td align="right">3.0%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">55,397,668</td>
<td align="right">0.9%</td>
<td align="right">50,334,249</td>
<td align="right">0.8%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,101,008,207</td>
<td align="right">96.1%</td>
<td align="right">5,935,422,585</td>
<td align="right">97.0%</td>
<td align="right">-2.7%</td>
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
<td align="right">1,238,323</td>
<td align="right">77.7%</td>
<td align="right">1,143,103</td>
<td align="right">77.1%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">356,102</td>
<td align="right">22.3%</td>
<td align="right">339,290</td>
<td align="right">22.9%</td>
<td align="right">-4.7%</td>
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
<td align="right">13,239</td>
<td align="right">3.7%</td>
<td align="right">6,570</td>
<td align="right">1.9%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.4%</td>
<td align="right">1,156</td>
<td align="right">0.3%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,164</td>
<td align="right">22.8%</td>
<td align="right">73,446</td>
<td align="right">21.6%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,150</td>
<td align="right">1.4%</td>
<td align="right">4,924</td>
<td align="right">1.5%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">55,263</td>
<td align="right">15.5%</td>
<td align="right">53,980</td>
<td align="right">15.9%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12,779</td>
<td align="right">3.6%</td>
<td align="right">12,626</td>
<td align="right">3.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,020</td>
<td align="right">4.2%</td>
<td align="right">14,860</td>
<td align="right">4.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">35,076</td>
<td align="right">9.8%</td>
<td align="right">34,803</td>
<td align="right">10.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">135,491</td>
<td align="right">38.0%</td>
<td align="right">135,465</td>
<td align="right">39.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.3%</td>
<td align="right">1,040</td>
<td align="right">0.3%</td>
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
<td align="right">194,158</td>
<td align="right">0.0%</td>
<td align="right">90,459</td>
<td align="right">0.0%</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,558,397,337</td>
<td align="right">100.0%</td>
<td align="right">1,406,446,799</td>
<td align="right">100.0%</td>
<td align="right">-9.8%</td>
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
<td align="right">1,858</td>
<td align="right">5.8%</td>
<td align="right">1,772</td>
<td align="right">5.6%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,044</td>
<td align="right">94.2%</td>
<td align="right">30,056</td>
<td align="right">94.4%</td>
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
<td align="right">300</td>
<td align="right">16.9%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,218</td>
<td align="right">65.6%</td>
<td align="right">1,212</td>
<td align="right">68.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.0%</td>
<td align="right">260</td>
<td align="right">14.7%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">67,016,614,557</td>
<td align="right">54.8%</td>
<td align="right">53,982,094,588</td>
<td align="right">53.9%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">914,059,576</td>
<td align="right">0.7%</td>
<td align="right">748,696,054</td>
<td align="right">0.7%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">42,719,005,476</td>
<td align="right">34.9%</td>
<td align="right">35,444,174,262</td>
<td align="right">35.4%</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,717,789,320</td>
<td align="right">9.6%</td>
<td align="right">9,967,429,182</td>
<td align="right">10.0%</td>
<td align="right">-14.9%</td>
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
<td align="right">437,037,758</td>
<td align="right">8.7%</td>
<td align="right">307,446,774</td>
<td align="right">7.0%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">248,282,880</td>
<td align="right">4.9%</td>
<td align="right">183,978,722</td>
<td align="right">4.2%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,519,370,478</td>
<td align="right">30.3%</td>
<td align="right">1,281,559,980</td>
<td align="right">29.2%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">743,980,833</td>
<td align="right">14.8%</td>
<td align="right">631,458,215</td>
<td align="right">14.4%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">190,470,433</td>
<td align="right">3.8%</td>
<td align="right">174,080,900</td>
<td align="right">4.0%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">662,107,381</td>
<td align="right">13.2%</td>
<td align="right">628,803,747</td>
<td align="right">14.3%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,058,579</td>
<td align="right">4.6%</td>
<td align="right">227,847,583</td>
<td align="right">5.2%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">208,172,737</td>
<td align="right">4.1%</td>
<td align="right">205,519,154</td>
<td align="right">4.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">483,797,468</td>
<td align="right">9.6%</td>
<td align="right">480,221,266</td>
<td align="right">11.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,924</td>
<td align="right">3.5%</td>
<td align="right">173,284,920</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">171,950,543</td>
<td align="right">17.3%</td>
<td align="right">114,546,320</td>
<td align="right">13.9%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,547,164</td>
<td align="right">3.6%</td>
<td align="right">25,553,980</td>
<td align="right">3.1%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">98,381,121</td>
<td align="right">9.9%</td>
<td align="right">70,824,021</td>
<td align="right">8.6%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">58,788,733</td>
<td align="right">5.9%</td>
<td align="right">46,192,250</td>
<td align="right">5.6%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">125,645,656</td>
<td align="right">12.7%</td>
<td align="right">108,819,607</td>
<td align="right">13.2%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">114,222,140</td>
<td align="right">11.5%</td>
<td align="right">99,514,619</td>
<td align="right">12.0%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,897,432</td>
<td align="right">7.9%</td>
<td align="right">77,898,220</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,897,432</td>
<td align="right">7.9%</td>
<td align="right">77,898,220</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,485</td>
<td align="right">2.8%</td>
<td align="right">27,496,517</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,366,082</td>
<td align="right">2.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">25,112,272</td>
<td align="right">3.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">348,547,153</td>
<td align="right">4.0%</td>
<td align="right">356,194,127</td>
<td align="right">4.1%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,784,047,052</td>
<td align="right">20.5%</td>
<td align="right">1,794,223,791</td>
<td align="right">20.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,788,493,492</td>
<td align="right">20.5%</td>
<td align="right">1,798,670,231</td>
<td align="right">20.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">550,012,131</td>
<td align="right">6.3%</td>
<td align="right">552,766,761</td>
<td align="right">6.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,064,096,131</td>
<td align="right">69.6%</td>
<td align="right">6,037,772,813</td>
<td align="right">69.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,649,106,694</td>
<td align="right">30.4%</td>
<td align="right">2,659,227,083</td>
<td align="right">30.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,649,106,694</td>
<td align="right">30.4%</td>
<td align="right">2,659,227,083</td>
<td align="right">30.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,954,179,303</td>
<td align="right">79.8%</td>
<td align="right">6,938,500,721</td>
<td align="right">79.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,613,202</td>
<td align="right">9.9%</td>
<td align="right">860,556,852</td>
<td align="right">9.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,397,352</td>
<td align="right">1.0%</td>
<td align="right">84,401,636</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,015,817</td>
<td align="right">0.4%</td>
<td align="right">31,015,208</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,249</td>
<td align="right">2.0%</td>
<td align="right">175,480,326</td>
<td align="right">2.0%</td>
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
<td align="left">Interpreter increfs</td>
<td align="right">53,466,309,268</td>
<td align="right">37.2%</td>
<td align="right">43,869,695,898</td>
<td align="right">30.3%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">90,290,811,638</td>
<td align="right">62.8%</td>
<td align="right">101,026,065,807</td>
<td align="right">69.7%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">54,231,476</td>
<td align="right"></td>
<td align="right">59,993,917</td>
<td align="right"></td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">72,192,141,394</td>
<td align="right">43.3%</td>
<td align="right">65,417,874,999</td>
<td align="right">39.0%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">94,383,329,472</td>
<td align="right">56.7%</td>
<td align="right">102,444,790,662</td>
<td align="right">61.0%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">67,760,584</td>
<td align="right"></td>
<td align="right">72,854,727</td>
<td align="right"></td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">16,845,198</td>
<td align="right"></td>
<td align="right">16,169,121</td>
<td align="right"></td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,237,475,217</td>
<td align="right"></td>
<td align="right">3,278,650,192</td>
<td align="right"></td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,715,281,163</td>
<td align="right">55.2%</td>
<td align="right">12,850,912,160</td>
<td align="right">55.4%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,824,203,345</td>
<td align="right">55.7%</td>
<td align="right">12,959,745,427</td>
<td align="right">55.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,529,066,281</td>
<td align="right"></td>
<td align="right">13,663,812,458</td>
<td align="right"></td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,126,366</td>
<td align="right"></td>
<td align="right">161,802,568</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,206,246,789</td>
<td align="right">44.3%</td>
<td align="right">10,216,871,533</td>
<td align="right">44.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,208,147,271</td>
<td align="right"></td>
<td align="right">10,218,745,388</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">94,073,978</td>
<td align="right">0.4%</td>
<td align="right">93,988,969</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,563,373,921</td>
<td align="right"></td>
<td align="right">4,566,137,096</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">14,848,204</td>
<td align="right">0.1%</td>
<td align="right">14,844,298</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,306,920</td>
<td align="right">2.0%</td>
<td align="right">3,306,920</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">113,940</td>
<td align="right">0.1%</td>
<td align="right">113,940</td>
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
<td align="right">115,475,440</td>
<td align="right">19,131,077,303</td>
<td align="right">0</td>
<td align="right">114,795,680</td>
<td align="right">19,135,058,966</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,334,252</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,339,108</td>
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
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">214.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">494,994</td>
<td align="right">40.4%</td>
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
<td align="right">50,489</td>
<td align="right">4.1%</td>
<td align="right">95,404</td>
<td align="right">9.0%</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,337</td>
<td align="right">0.1%</td>
<td align="right">2,126</td>
<td align="right">0.2%</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">125,781</td>
<td align="right">10.3%</td>
<td align="right">191,033</td>
<td align="right">18.1%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">12,568</td>
<td align="right">1.0%</td>
<td align="right">15,762</td>
<td align="right">1.5%</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,098,358</td>
<td align="right">89.7%</td>
<td align="right">863,479</td>
<td align="right">81.9%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,658,491,963</td>
<td align="right"></td>
<td align="right">9,152,531,134</td>
<td align="right"></td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">249,868,283,340</td>
<td align="right">3,262.6%</td>
<td align="right">291,202,331,324</td>
<td align="right">3,181.7%</td>
<td align="right">16.5%</td>
</tr>
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
<td align="right">1,980</td>
<td align="right">0.2%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,224,139</td>
<td align="right"></td>
<td align="right">1,054,512</td>
<td align="right"></td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,348</td>
<td align="right">5.0%</td>
<td align="right">7,136</td>
<td align="right">3.7%</td>
<td align="right">12.4%</td>
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
<td align="right">125,781</td>
<td align="right"></td>
<td align="right">191,033</td>
<td align="right"></td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">110,933</td>
<td align="right">88.2%</td>
<td align="right">163,399</td>
<td align="right">85.5%</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,443</td>
<td align="right">1.9%</td>
<td align="right">2,451</td>
<td align="right">1.3%</td>
<td align="right">0.3%</td>
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
<td align="right">5,298</td>
<td align="right">4.2%</td>
<td align="right">14,511</td>
<td align="right">7.6%</td>
<td align="right">173.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,573</td>
<td align="right">17.2%</td>
<td align="right">32,597</td>
<td align="right">17.1%</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,251</td>
<td align="right">28.0%</td>
<td align="right">49,323</td>
<td align="right">25.8%</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">30,857</td>
<td align="right">24.5%</td>
<td align="right">48,132</td>
<td align="right">25.2%</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21,219</td>
<td align="right">16.9%</td>
<td align="right">26,611</td>
<td align="right">13.9%</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,723</td>
<td align="right">7.7%</td>
<td align="right">16,442</td>
<td align="right">8.6%</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,700</td>
<td align="right">1.4%</td>
<td align="right">2,897</td>
<td align="right">1.5%</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">520</td>
<td align="right">0.3%</td>
<td align="right">225.0%</td>
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
<td align="right">4,138</td>
<td align="right">3.3%</td>
<td align="right">2,697</td>
<td align="right">1.4%</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">14,802</td>
<td align="right">11.8%</td>
<td align="right">29,771</td>
<td align="right">15.6%</td>
<td align="right">101.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">25,257</td>
<td align="right">20.1%</td>
<td align="right">37,709</td>
<td align="right">19.7%</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">36,427</td>
<td align="right">29.0%</td>
<td align="right">49,476</td>
<td align="right">25.9%</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">18,509</td>
<td align="right">14.7%</td>
<td align="right">25,599</td>
<td align="right">13.4%</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,760</td>
<td align="right">7.0%</td>
<td align="right">12,814</td>
<td align="right">6.7%</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,660</td>
<td align="right">2.1%</td>
<td align="right">4,493</td>
<td align="right">2.4%</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">380</td>
<td align="right">0.3%</td>
<td align="right">840</td>
<td align="right">0.4%</td>
<td align="right">121.1%</td>
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
<td align="right">29,920</td>
<td align="right">6,339,533</td>
<td align="right">21,088.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">153,338,802</td>
<td align="right">9,832.3%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">648,779</td>
<td align="right">8,414.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,922,920</td>
<td align="right">56,351,792</td>
<td align="right">1,044.7%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,671,620</td>
<td align="right">38,321,874</td>
<td align="right">943.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">10,050,940</td>
<td align="right">100,170,671</td>
<td align="right">896.6%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,917,600</td>
<td align="right">38,253,184</td>
<td align="right">876.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">11,627,720</td>
<td align="right">101,852,371</td>
<td align="right">775.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">262,399,640</td>
<td align="right">2,231,006,759</td>
<td align="right">750.2%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">5,782,740</td>
<td align="right">41,785,324</td>
<td align="right">622.6%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,025,020</td>
<td align="right">20,883,908</td>
<td align="right">590.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">464,415</td>
<td align="right">2,966,602</td>
<td align="right">538.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">13,166,200</td>
<td align="right">385.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,227,105</td>
<td align="right">35,692,914</td>
<td align="right">249.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">67,792,420</td>
<td align="right">231,789,429</td>
<td align="right">241.9%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,092,198</td>
<td align="right">98,461,204</td>
<td align="right">180.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">907,921,574</td>
<td align="right">2,521,216,916</td>
<td align="right">177.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">126,546,234</td>
<td align="right">331,203,428</td>
<td align="right">161.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">47,971,827</td>
<td align="right">119,715,372</td>
<td align="right">149.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,717,560</td>
<td align="right">63,744,800</td>
<td align="right">147.9%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,533,432</td>
<td align="right">5,391,895</td>
<td align="right">112.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">601,140</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">25,197,744</td>
<td align="right">45,228,930</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">101,766,747</td>
<td align="right">178,283,192</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">75,936,345</td>
<td align="right">128,131,455</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">801,164,005</td>
<td align="right">1,348,375,080</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,659,960</td>
<td align="right">9,284,488</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">113,122,590</td>
<td align="right">184,775,174</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">338,027,898</td>
<td align="right">550,330,204</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">81,592,680</td>
<td align="right">132,303,352</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">81,702,400</td>
<td align="right">132,449,119</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">264,980,681</td>
<td align="right">411,465,747</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">266,207,941</td>
<td align="right">412,694,309</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,862,100</td>
<td align="right">10,486,628</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,713,332</td>
<td align="right">139,711,410</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">173,883,327</td>
<td align="right">256,925,142</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">39,840</td>
<td align="right">21,040</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,421,185,031</td>
<td align="right">2,070,786,388</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,652,185</td>
<td align="right">128,462,901</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">102,572,236</td>
<td align="right">146,412,794</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,490,837,241</td>
<td align="right">2,119,347,321</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,429,774</td>
<td align="right">111,098,770</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,682,778</td>
<td align="right">40,132,850</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,177,320</td>
<td align="right">11,569,699</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,414,870</td>
<td align="right">134,542,959</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">150,145,075</td>
<td align="right">211,653,190</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,658,730</td>
<td align="right">134,803,619</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,690,398,961</td>
<td align="right">2,372,033,319</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">163,092,540</td>
<td align="right">228,485,492</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,025,666,874</td>
<td align="right">2,828,789,140</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,964,176,769</td>
<td align="right">2,713,805,375</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">947,129,059</td>
<td align="right">1,308,109,729</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">407,352,702</td>
<td align="right">562,289,483</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,790,342,787</td>
<td align="right">2,456,937,797</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,086,114,050</td>
<td align="right">2,860,331,092</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,387,369</td>
<td align="right">126,091,606</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">317,179,580</td>
<td align="right">427,946,618</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">394,141,934</td>
<td align="right">530,545,586</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,381,935</td>
<td align="right">128,866,899</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">212,710,464</td>
<td align="right">283,720,269</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,578,500,794</td>
<td align="right">2,102,226,088</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">458,247,341</td>
<td align="right">600,875,771</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,990,580</td>
<td align="right">188,633,120</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">164,119,758</td>
<td align="right">212,843,899</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,412,648,438</td>
<td align="right">3,068,236,405</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,190,140,867</td>
<td align="right">1,505,460,604</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,994,596,737</td>
<td align="right">22,653,770,145</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,386,341,118</td>
<td align="right">3,003,787,225</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">28,421,210</td>
<td align="right">35,755,982</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,620,206,295</td>
<td align="right">4,545,671,986</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,323,249,487</td>
<td align="right">1,660,027,301</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,302,521,727</td>
<td align="right">1,630,927,751</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">563,253,712</td>
<td align="right">700,755,758</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,802,948,951</td>
<td align="right">8,416,428,687</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">395,595,992</td>
<td align="right">489,146,994</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">30,588,139</td>
<td align="right">37,669,410</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">194,356,520</td>
<td align="right">239,117,704</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,426,781,855</td>
<td align="right">4,214,813,456</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,720</td>
<td align="right">1,007,700</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,326,679,010</td>
<td align="right">1,623,879,500</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,340,453,587</td>
<td align="right">1,639,333,580</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,166,678,013</td>
<td align="right">3,853,736,253</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">395,766,495</td>
<td align="right">481,542,329</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,746,337,424</td>
<td align="right">3,340,203,375</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,276,455,267</td>
<td align="right">8,802,005,021</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">658,505,649</td>
<td align="right">793,459,556</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">274,498,649</td>
<td align="right">330,598,957</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,835,900</td>
<td align="right">74,403,213</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">121,960,461</td>
<td align="right">146,548,897</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">884,396,088</td>
<td align="right">1,062,605,529</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,046,701,297</td>
<td align="right">1,254,118,569</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">972,069,275</td>
<td align="right">1,164,376,685</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,658,491,963</td>
<td align="right">9,152,531,134</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">310,680</td>
<td align="right">368,268</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,152,854,888</td>
<td align="right">1,359,367,180</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,119,605,245</td>
<td align="right">7,180,301,377</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">60,988,920</td>
<td align="right">71,230,540</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">216,982,949</td>
<td align="right">252,370,707</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">219,513,205</td>
<td align="right">254,902,582</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,015,825,824</td>
<td align="right">2,336,931,194</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,685,040</td>
<td align="right">236,984,838</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">697,369,158</td>
<td align="right">796,483,406</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,059,561,191</td>
<td align="right">1,208,101,108</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">266,229,464</td>
<td align="right">303,104,659</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,713,871</td>
<td align="right">103,072,942</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,131,167,091</td>
<td align="right">1,283,299,942</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">435,925,196</td>
<td align="right">494,477,557</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">860,552,563</td>
<td align="right">974,801,681</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">834,115,332</td>
<td align="right">941,853,581</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">67,154,995</td>
<td align="right">75,788,614</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">15,663,608,008</td>
<td align="right">17,667,183,246</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,383,961,517</td>
<td align="right">1,555,255,757</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,683,011,511</td>
<td align="right">1,886,711,499</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">924,450,130</td>
<td align="right">1,036,210,066</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">64,522,284</td>
<td align="right">72,230,153</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,185,920,039</td>
<td align="right">14,744,573,961</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">297,705,572</td>
<td align="right">332,311,011</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">104,767,940</td>
<td align="right">116,909,347</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,742,287,559</td>
<td align="right">4,175,498,826</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">904,464,414</td>
<td align="right">1,008,991,945</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">514,767,036</td>
<td align="right">573,333,363</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">246,294,981</td>
<td align="right">273,586,860</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,809,679</td>
<td align="right">35,056,887</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,829,219,785</td>
<td align="right">2,015,449,774</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,252,646,628</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">59,644,340</td>
<td align="right">65,171,240</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">137,782,897</td>
<td align="right">150,485,470</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,584,100</td>
<td align="right">94,458,660</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">893,721,072</td>
<td align="right">974,079,332</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,255,054,792</td>
<td align="right">6,813,141,162</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">58,567,820</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">239,754,893</td>
<td align="right">218,621,054</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,638,074</td>
<td align="right">417,300,904</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,688,399,516</td>
<td align="right">5,083,197,513</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">510,187,700</td>
<td align="right">551,501,740</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">218,973,940</td>
<td align="right">236,646,320</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,037,852,163</td>
<td align="right">3,282,126,167</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,165,627,940</td>
<td align="right">2,339,621,618</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,849,005,499</td>
<td align="right">1,988,893,991</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,330,974,065</td>
<td align="right">2,506,345,610</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">48,459,599</td>
<td align="right">52,063,242</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,819,434,084</td>
<td align="right">5,173,143,030</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">7,006,297,041</td>
<td align="right">6,512,063,458</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,329,334</td>
<td align="right">2,492,338</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,611,485,654</td>
<td align="right">1,724,081,002</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,696,159,857</td>
<td align="right">10,351,671,292</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,027,076,433</td>
<td align="right">1,096,091,640</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,187,201</td>
<td align="right">104,518,113</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,335</td>
<td align="right">142,750,930</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,335</td>
<td align="right">142,750,930</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,229,861</td>
<td align="right">103,159,345</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,171</td>
<td align="right">683,619,746</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">553,867,554</td>
<td align="right">585,236,952</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">3,628,062</td>
<td align="right">3,830,830</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,253,951,572</td>
<td align="right">1,322,657,709</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,418,374,871</td>
<td align="right">4,660,178,029</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">619,477,485</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">235,347,921</td>
<td align="right">247,156,187</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,490,371</td>
<td align="right">168,465,856</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">777,658,264</td>
<td align="right">812,503,980</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">387,261,850</td>
<td align="right">404,069,022</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,966,880</td>
<td align="right">3,095,631</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">321,279,671</td>
<td align="right">334,990,918</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">198,417,421</td>
<td align="right">206,615,990</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">664,882,748</td>
<td align="right">691,523,841</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,698,177</td>
<td align="right">807,934,121</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,160,857</td>
<td align="right">807,331,421</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,940</td>
<td align="right">6,822,779</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,280,057,960</td>
<td align="right">1,324,421,515</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,366,919,175</td>
<td align="right">3,483,529,663</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">992,082,796</td>
<td align="right">1,026,250,573</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,816,269,139</td>
<td align="right">1,878,319,859</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,591,672</td>
<td align="right">11,959,205</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,591,672</td>
<td align="right">11,956,785</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,270,476,662</td>
<td align="right">4,396,056,775</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,682,017</td>
<td align="right">10,989,411</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,623,729,195</td>
<td align="right">3,727,707,110</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,965,460</td>
<td align="right">159,379,320</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,841,142,041</td>
<td align="right">2,905,962,339</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">972,689,965</td>
<td align="right">994,048,760</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">140,317,419</td>
<td align="right">142,804,051</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,648,680</td>
<td align="right">4,729,880</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,319,550,051</td>
<td align="right">2,351,350,180</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,259,037,890</td>
<td align="right">2,288,202,735</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">651,198,990</td>
<td align="right">659,600,562</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,997,861,167</td>
<td align="right">2,020,119,308</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,749,503</td>
<td align="right">232,264,133</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,550,540</td>
<td align="right">189,434,308</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">244,676,060</td>
<td align="right">246,278,129</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">643,762,527</td>
<td align="right">647,973,651</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,601,060</td>
<td align="right">735,485,032</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,883,906,419</td>
<td align="right">1,893,102,777</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,098,164,256</td>
<td align="right">1,100,790,146</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,080,100</td>
<td align="right">534,189,320</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,508,973,019</td>
<td align="right">2,513,840,287</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,561,839,761</td>
<td align="right">6,574,190,390</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">46,415,300</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,705,220</td>
<td align="right">80,714,471</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,403,284</td>
<td align="right">32,402,318</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,697,060</td>
<td align="right">12,696,980</td>
<td align="right">-0.0%</td>
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
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">34,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">538,734,493</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">9,092,151</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">30,963</td>
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
<td align="left">IMPORT_NAME</td>
<td align="right">2,457</td>
<td align="right">4,795</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,200</td>
<td align="right">1,997</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">640</td>
<td align="right">960</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">540</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,221</td>
<td align="right">9,303</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,540</td>
<td align="right">5,141</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">30,640</td>
<td align="right">43,962</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">620</td>
<td align="right">820</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">320</td>
<td align="right">420</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,618</td>
<td align="right">8,416</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">486,640</td>
<td align="right">554,917</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,641</td>
<td align="right">48,479</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">33,340</td>
<td align="right">34,091</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,680</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right"></td>
<td align="right">289</td>
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
<td align="right">1,105</td>
<td align="right">1,106</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,105</td>
<td align="right">1,106</td>
<td align="right">0.1%</td>
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
Stats gathered on: 2024-07-03
