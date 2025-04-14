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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,803,245,146</td>
<td align="right">3,533,523</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,724,898</td>
<td align="right">1,232,478</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,370,308</td>
<td align="right">2,281,706</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">6,000,000</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,457,238,002</td>
<td align="right">198,438,726</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">701,026,436</td>
<td align="right">103,884,507</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,583,751,512</td>
<td align="right">237,344,497</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,403,718,067</td>
<td align="right">213,945,235</td>
<td align="right">-84.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,754,656,795</td>
<td align="right">273,491,265</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,274,625,291</td>
<td align="right">202,216,804</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,718,270,643</td>
<td align="right">438,520,567</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">566,120,161</td>
<td align="right">96,192,724</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,477,434,389</td>
<td align="right">609,536,484</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,255,459,056</td>
<td align="right">396,788,016</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,128,227,435</td>
<td align="right">377,080,892</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">506,589,969</td>
<td align="right">94,162,967</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">89,906,877</td>
<td align="right">19,469,408</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,246,175,500</td>
<td align="right">274,849,591</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,747,998</td>
<td align="right">76,792,841</td>
<td align="right">-77.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,803,354</td>
<td align="right">35,130,344</td>
<td align="right">-77.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">670,713,139</td>
<td align="right">164,069,047</td>
<td align="right">-75.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,653,803,895</td>
<td align="right">432,095,623</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,281,591,915</td>
<td align="right">2,009,087,311</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">629,951,658</td>
<td align="right">174,168,167</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">194,919,843</td>
<td align="right">54,205,967</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,606,339</td>
<td align="right">146,123,398</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">369,500,158</td>
<td align="right">107,406,428</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,405,746</td>
<td align="right">17,244,746</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">633,050,920</td>
<td align="right">192,204,467</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">375,931,186</td>
<td align="right">115,641,813</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">534,962,735</td>
<td align="right">167,776,799</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,196,612,283</td>
<td align="right">703,244,656</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,156,812</td>
<td align="right">36,938,714</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,729,882,324</td>
<td align="right">885,187,529</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">254,461,122</td>
<td align="right">83,254,060</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,113,741,808</td>
<td align="right">364,974,658</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">544,984,303</td>
<td align="right">184,724,877</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,510,871,184</td>
<td align="right">858,295,334</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,742,517,366</td>
<td align="right">1,981,191,228</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,382,445</td>
<td align="right">55,208,382</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">73,291,754</td>
<td align="right">25,631,208</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">356,680,791</td>
<td align="right">124,950,071</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">121,221,499</td>
<td align="right">42,940,737</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,008,544,036</td>
<td align="right">3,933,370,722</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,528,868,275</td>
<td align="right">908,845,014</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">61,500,611</td>
<td align="right">22,164,198</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,407,658,149</td>
<td align="right">4,910,931,092</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,683,405,957</td>
<td align="right">4,027,557,291</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,327,634,190</td>
<td align="right">501,943,587</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">859,842,952</td>
<td align="right">326,100,114</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">152,392,535</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,078,152,972</td>
<td align="right">419,550,388</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,805,891,600</td>
<td align="right">1,094,897,137</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">65,889,145</td>
<td align="right">25,839,559</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">433,385,799</td>
<td align="right">170,383,867</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">78,089,791</td>
<td align="right">31,033,272</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">266,162,189</td>
<td align="right">107,511,029</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,087,726,746</td>
<td align="right">874,153,363</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">2,597,140</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">23,426,292</td>
<td align="right">10,054,198</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">100,492,794</td>
<td align="right">43,489,897</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">810,231,685</td>
<td align="right">355,386,800</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">404,541,821</td>
<td align="right">177,722,228</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,436,108</td>
<td align="right">468,522,117</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">784,003,841</td>
<td align="right">367,185,298</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">37,014,177,161</td>
<td align="right">17,481,252,246</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,533,088</td>
<td align="right">3,567,489</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,022,058</td>
<td align="right">129,276,063</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,203,496,787</td>
<td align="right">3,573,752,691</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,253,862,668</td>
<td align="right">637,713,823</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">93,173,217</td>
<td align="right">48,508,333</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,664,378</td>
<td align="right">51,910,479</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,206,240,828</td>
<td align="right">634,831,954</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">312,519,841</td>
<td align="right">165,321,843</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">263,592,361</td>
<td align="right">141,501,722</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">546,837,279</td>
<td align="right">295,614,806</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">67,674,478</td>
<td align="right">37,377,054</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">349,117,325</td>
<td align="right">195,300,115</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,500,225,973</td>
<td align="right">840,879,960</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,798,470</td>
<td align="right">87,605,630</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">289,763,665</td>
<td align="right">163,549,852</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,874,211,598</td>
<td align="right">2,198,855,218</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">9,775</td>
<td align="right">13,935</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">57,732,290</td>
<td align="right">33,235,100</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">195,867,333</td>
<td align="right">113,647,776</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,057,739,832</td>
<td align="right">614,117,923</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">114,874,723</td>
<td align="right">66,768,770</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">771,795,409</td>
<td align="right">460,673,537</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,494,254,889</td>
<td align="right">1,490,831,369</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,181</td>
<td align="right">114,765,173</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,738,757</td>
<td align="right">4,717,220</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,378,596,902</td>
<td align="right">840,634,060</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,177,729,329</td>
<td align="right">1,964,689,831</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">190,496,551</td>
<td align="right">120,110,494</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,483,168,337</td>
<td align="right">938,282,756</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,834,979,424</td>
<td align="right">3,249,993,801</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">821,465,576</td>
<td align="right">555,908,398</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">67,603,160</td>
<td align="right">46,654,105</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,295,927</td>
<td align="right">121,383,926</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">401,639,985</td>
<td align="right">281,907,273</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">168,450,997</td>
<td align="right">118,277,551</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">485,430,314</td>
<td align="right">344,285,204</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">325,539,839</td>
<td align="right">242,825,844</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,294,700,377</td>
<td align="right">2,470,113,071</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">220,248,861</td>
<td align="right">168,106,144</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">822,418,044</td>
<td align="right">644,596,202</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,820,575</td>
<td align="right">1,431,575</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">492,763,794</td>
<td align="right">388,877,794</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">355,660,224</td>
<td align="right">282,100,666</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,182,042,070</td>
<td align="right">2,531,883,139</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,230,507,165</td>
<td align="right">4,986,471,326</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">348,220,458</td>
<td align="right">288,214,593</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">292,922,547</td>
<td align="right">249,296,822</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">94,810,816</td>
<td align="right">82,058,293</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,342,822,621</td>
<td align="right">4,643,253,375</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">72,556,228</td>
<td align="right">63,696,871</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">555,109,577</td>
<td align="right">488,304,838</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">926,824,324</td>
<td align="right">815,734,132</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">301,004,628</td>
<td align="right">266,109,845</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">415,604,279</td>
<td align="right">367,783,711</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,584,121</td>
<td align="right">10,288,614</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">949,842,302</td>
<td align="right">844,090,992</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">63,080,618</td>
<td align="right">56,987,732</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">63,324,837</td>
<td align="right">57,470,137</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">61,601,956</td>
<td align="right">56,116,710</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,798,023</td>
<td align="right">3,486,023</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">134,718,283</td>
<td align="right">125,916,185</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,668</td>
<td align="right">5,803,552</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">77,214,471</td>
<td align="right">72,748,873</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,451,098</td>
<td align="right">1,384,467</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,972,753</td>
<td align="right">20,026,352</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,303,723</td>
<td align="right">20,357,322</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,303,744</td>
<td align="right">20,357,343</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,441,421</td>
<td align="right">7,144,058</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,804</td>
<td align="right">123,859,712</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">83,615,058</td>
<td align="right">81,369,463</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">73,237,587</td>
<td align="right">71,281,901</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,777,442</td>
<td align="right">1,748,322</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">69,829,737</td>
<td align="right">70,739,113</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,385,969</td>
<td align="right">7,297,408</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,899,110</td>
<td align="right">13,760,194</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,618,198</td>
<td align="right">4,587,276</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">66,862,312</td>
<td align="right">66,500,436</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,711,142</td>
<td align="right">7,684,237</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,267,461</td>
<td align="right">155,905,625</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,503</td>
<td align="right">5,512</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,518,983,342</td>
<td align="right">1,520,429,907</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">237,901,594</td>
<td align="right">238,104,064</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">239,958,854</td>
<td align="right">240,161,346</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,944,311</td>
<td align="right">27,962,388</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,600,909</td>
<td align="right">418,391,213</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,644</td>
<td align="right">2,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,113,374,823</td>
<td align="right">1,113,582,664</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">34,177</td>
<td align="right">34,183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">752,968</td>
<td align="right">752,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">337,190,511</td>
<td align="right">337,236,731</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,417,268</td>
<td align="right">131,401,015</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">178,416,313</td>
<td align="right">178,432,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">135,697</td>
<td align="right">135,685</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,547,502</td>
<td align="right">35,549,630</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,887,921</td>
<td align="right">114,894,736</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">407,129</td>
<td align="right">407,153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,604,867</td>
<td align="right">591,621,555</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">121,291</td>
<td align="right">121,294</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,244,558</td>
<td align="right">302,246,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,761,887</td>
<td align="right">14,761,972</td>
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
<td align="right">128,850,071</td>
<td align="right">128,850,071</td>
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
<td align="right">41,964,669</td>
<td align="right">41,964,669</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">9,743,071</td>
<td align="right">9,743,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,976,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
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
<td align="left">DELETE_ATTR</td>
<td align="right">1,644,274</td>
<td align="right">1,644,274</td>
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
<td align="right">98,601</td>
<td align="right">98,601</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,496</td>
<td align="right">84,496</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,511</td>
<td align="right">69,511</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,207</td>
<td align="right">57,207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,629</td>
<td align="right">56,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,265</td>
<td align="right">5,265</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,889</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,613</td>
<td align="right">3,613</td>
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
<td align="right">153</td>
<td align="right">153</td>
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
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">1,061,730,192</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">850,714,281</td>
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
<td align="right">2,804,948,988</td>
<td align="right">15.0%</td>
<td align="right">1,094,513,034</td>
<td align="right">6.4%</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">59,002,429</td>
<td align="right">0.3%</td>
<td align="right">51,914,670</td>
<td align="right">0.3%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,816,277,627</td>
<td align="right">84.7%</td>
<td align="right">15,833,413,276</td>
<td align="right">93.2%</td>
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
<td align="right">925,584</td>
<td align="right">45.0%</td>
<td align="right">367,050</td>
<td align="right">26.9%</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,130,053</td>
<td align="right">55.0%</td>
<td align="right">996,354</td>
<td align="right">73.1%</td>
<td align="right">-11.8%</td>
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
<td align="right">115,278</td>
<td align="right">12.5%</td>
<td align="right">6,372</td>
<td align="right">1.7%</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">9.2%</td>
<td align="right">16,343</td>
<td align="right">4.5%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">2,768</td>
<td align="right">0.8%</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,212</td>
<td align="right">8.0%</td>
<td align="right">18,469</td>
<td align="right">5.0%</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">0.9%</td>
<td align="right">2,350</td>
<td align="right">0.6%</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.3%</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,512</td>
<td align="right">2.5%</td>
<td align="right">8,300</td>
<td align="right">2.3%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">350,691</td>
<td align="right">37.9%</td>
<td align="right">132,059</td>
<td align="right">36.0%</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,256</td>
<td align="right">0.1%</td>
<td align="right">489</td>
<td align="right">0.1%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,859</td>
<td align="right">4.7%</td>
<td align="right">22,134</td>
<td align="right">6.0%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">397</td>
<td align="right">0.0%</td>
<td align="right">209</td>
<td align="right">0.1%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">34,001</td>
<td align="right">3.7%</td>
<td align="right">19,867</td>
<td align="right">5.4%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">2.1%</td>
<td align="right">11,553</td>
<td align="right">3.1%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,616</td>
<td align="right">4.0%</td>
<td align="right">23,131</td>
<td align="right">6.3%</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,514</td>
<td align="right">0.9%</td>
<td align="right">6,194</td>
<td align="right">1.7%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">7,225</td>
<td align="right">0.8%</td>
<td align="right">5,752</td>
<td align="right">1.6%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">43,428</td>
<td align="right">4.7%</td>
<td align="right">36,637</td>
<td align="right">10.0%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">46,858</td>
<td align="right">5.1%</td>
<td align="right">41,361</td>
<td align="right">11.3%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,036</td>
<td align="right">0.2%</td>
<td align="right">1,996</td>
<td align="right">0.5%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">632</td>
<td align="right">0.1%</td>
<td align="right">622</td>
<td align="right">0.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,343</td>
<td align="right">0.3%</td>
<td align="right">2,341</td>
<td align="right">0.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,154</td>
<td align="right">0.3%</td>
<td align="right">3,154</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">1,969</td>
<td align="right">0.2%</td>
<td align="right">1,969</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.1%</td>
<td align="right">1,384</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">596</td>
<td align="right">0.2%</td>
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
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">61</td>
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
<td align="right">544,984,303</td>
<td align="right">100.0%</td>
<td align="right">184,724,877</td>
<td align="right">100.0%</td>
<td align="right">-66.1%</td>
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
<td align="right">177,866,705</td>
<td align="right">1.6%</td>
<td align="right">150,429,446</td>
<td align="right">1.3%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">174,743,081</td>
<td align="right">1.6%</td>
<td align="right">147,823,551</td>
<td align="right">1.3%</td>
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
<td align="right">10,962,745,479</td>
<td align="right">98.4%</td>
<td align="right">10,997,791,279</td>
<td align="right">98.6%</td>
<td align="right">0.3%</td>
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
<td align="right">3,530,307</td>
<td align="right">100.0%</td>
<td align="right">3,012,602</td>
<td align="right">100.0%</td>
<td align="right">-14.7%</td>
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
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right">267</td>
<td align="right">59.9%</td>
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
<td align="right">684,329</td>
<td align="right">97.1%</td>
<td align="right">684,331</td>
<td align="right">97.1%</td>
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
<td align="right">583,611</td>
<td align="right">82.8%</td>
<td align="right">583,611</td>
<td align="right">82.8%</td>
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
<td align="right">20,453</td>
<td align="right">99.4%</td>
<td align="right">20,454</td>
<td align="right">99.4%</td>
<td align="right">0.0%</td>
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
<td align="right">506,360,910</td>
<td align="right">10.1%</td>
<td align="right">94,044,084</td>
<td align="right">2.0%</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,434,664</td>
<td align="right">0.0%</td>
<td align="right">1,163,953</td>
<td align="right">0.0%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,500,734,353</td>
<td align="right">89.9%</td>
<td align="right">4,506,474,241</td>
<td align="right">97.9%</td>
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
<td align="right">210,862</td>
<td align="right">82.4%</td>
<td align="right">100,741</td>
<td align="right">71.6%</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">44,943</td>
<td align="right">17.6%</td>
<td align="right">39,912</td>
<td align="right">28.4%</td>
<td align="right">-11.2%</td>
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
<td align="right">90,850</td>
<td align="right">43.1%</td>
<td align="right">4,615</td>
<td align="right">4.6%</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,832</td>
<td align="right">3.2%</td>
<td align="right">370</td>
<td align="right">0.4%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">9,385</td>
<td align="right">4.5%</td>
<td align="right">5,957</td>
<td align="right">5.9%</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,503</td>
<td align="right">6.9%</td>
<td align="right">9,323</td>
<td align="right">9.3%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,694</td>
<td align="right">21.7%</td>
<td align="right">37,232</td>
<td align="right">37.0%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,473</td>
<td align="right">11.1%</td>
<td align="right">23,204</td>
<td align="right">23.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,826</td>
<td align="right">3.7%</td>
<td align="right">7,756</td>
<td align="right">7.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,985</td>
<td align="right">0.9%</td>
<td align="right">1,969</td>
<td align="right">2.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,366</td>
<td align="right">0.6%</td>
<td align="right">1,367</td>
<td align="right">1.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">3.6%</td>
<td align="right">7,648</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">944</td>
<td align="right">0.4%</td>
<td align="right">944</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.2%</td>
<td align="right">356</td>
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
<td align="right">155,736,925</td>
<td align="right">6.6%</td>
<td align="right">87,560,649</td>
<td align="right">3.8%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,065,239</td>
<td align="right">0.0%</td>
<td align="right">1,395,959</td>
<td align="right">0.1%</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,186,977,355</td>
<td align="right">93.3%</td>
<td align="right">2,189,858,052</td>
<td align="right">96.1%</td>
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
<td align="right">22,222</td>
<td align="right">27.2%</td>
<td align="right">28,462</td>
<td align="right">39.9%</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,426</td>
<td align="right">72.8%</td>
<td align="right">42,862</td>
<td align="right">60.1%</td>
<td align="right">-27.9%</td>
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
<td align="right">21,451</td>
<td align="right">36.1%</td>
<td align="right">9,625</td>
<td align="right">22.5%</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,642</td>
<td align="right">24.6%</td>
<td align="right">12,074</td>
<td align="right">28.2%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,681</td>
<td align="right">19.7%</td>
<td align="right">9,981</td>
<td align="right">23.3%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,652</td>
<td align="right">19.6%</td>
<td align="right">11,182</td>
<td align="right">26.1%</td>
<td align="right">-4.0%</td>
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
<td align="right">1,456,806,568</td>
<td align="right">28.3%</td>
<td align="right">198,320,287</td>
<td align="right">12.5%</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,534,720,481</td>
<td align="right">68.6%</td>
<td align="right">1,320,451,346</td>
<td align="right">83.5%</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,996,706</td>
<td align="right">3.2%</td>
<td align="right">61,975,007</td>
<td align="right">3.9%</td>
<td align="right">-62.2%</td>
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
<td align="right">425,847</td>
<td align="right">12.1%</td>
<td align="right">112,825</td>
<td align="right">8.8%</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,099,689</td>
<td align="right">87.9%</td>
<td align="right">1,174,784</td>
<td align="right">91.2%</td>
<td align="right">-62.1%</td>
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
<td align="right">172,124</td>
<td align="right">40.4%</td>
<td align="right">4,470</td>
<td align="right">4.0%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,640</td>
<td align="right">19.6%</td>
<td align="right">11,084</td>
<td align="right">9.8%</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,934</td>
<td align="right">8.2%</td>
<td align="right">6,439</td>
<td align="right">5.7%</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,979</td>
<td align="right">0.7%</td>
<td align="right">1,132</td>
<td align="right">1.0%</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,815</td>
<td align="right">2.5%</td>
<td align="right">4,320</td>
<td align="right">3.8%</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,246</td>
<td align="right">4.3%</td>
<td align="right">8,974</td>
<td align="right">8.0%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,144</td>
<td align="right">0.7%</td>
<td align="right">1,737</td>
<td align="right">1.5%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,437</td>
<td align="right">4.6%</td>
<td align="right">14,166</td>
<td align="right">12.6%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">67,364</td>
<td align="right">15.8%</td>
<td align="right">49,465</td>
<td align="right">43.8%</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,583</td>
<td align="right">1.1%</td>
<td align="right">3,813</td>
<td align="right">3.4%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,930</td>
<td align="right">1.6%</td>
<td align="right">6,510</td>
<td align="right">5.8%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">254</td>
<td align="right">0.1%</td>
<td align="right">254</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">819,620,728</td>
<td align="right">6.0%</td>
<td align="right">554,149,810</td>
<td align="right">4.2%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">863,444,967</td>
<td align="right">6.3%</td>
<td align="right">609,739,164</td>
<td align="right">4.6%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,006,216</td>
<td align="right">0.0%</td>
<td align="right">1,263,438</td>
<td align="right">0.0%</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,924,662,798</td>
<td align="right">87.6%</td>
<td align="right">12,103,109,128</td>
<td align="right">91.2%</td>
<td align="right">1.5%</td>
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
<td align="right">16,377,048</td>
<td align="right">96.7%</td>
<td align="right">11,590,285</td>
<td align="right">95.9%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">559,956</td>
<td align="right">3.3%</td>
<td align="right">491,357</td>
<td align="right">4.1%</td>
<td align="right">-12.3%</td>
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
<td align="right">77,375</td>
<td align="right">13.8%</td>
<td align="right">39,970</td>
<td align="right">8.1%</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,201</td>
<td align="right">0.2%</td>
<td align="right">841</td>
<td align="right">0.2%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">57,962</td>
<td align="right">10.4%</td>
<td align="right">42,919</td>
<td align="right">8.7%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,110</td>
<td align="right">1.1%</td>
<td align="right">4,896</td>
<td align="right">1.0%</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,736</td>
<td align="right">0.5%</td>
<td align="right">2,377</td>
<td align="right">0.5%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,190</td>
<td align="right">1.6%</td>
<td align="right">8,000</td>
<td align="right">1.6%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">65,778</td>
<td align="right">11.7%</td>
<td align="right">61,779</td>
<td align="right">12.6%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">25,284</td>
<td align="right">4.5%</td>
<td align="right">24,232</td>
<td align="right">4.9%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,670</td>
<td align="right">3.0%</td>
<td align="right">16,300</td>
<td align="right">3.3%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,020</td>
<td align="right">0.9%</td>
<td align="right">5,019</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.1%</td>
<td align="right">6,405</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,802</td>
<td align="right">0.3%</td>
<td align="right">1,802</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,491</td>
<td align="right">0.3%</td>
<td align="right">1,491</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
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
<td align="right">0.0%</td>
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
<td align="right">9,037,164,567</td>
<td align="right">99.8%</td>
<td align="right">4,563,279,837</td>
<td align="right">99.7%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,176</td>
<td align="right">0.0%</td>
<td align="right">53,185</td>
<td align="right">0.0%</td>
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
<td align="right">14,623,552</td>
<td align="right">0.2%</td>
<td align="right">14,623,599</td>
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
<td align="right">1,502</td>
<td align="right">0.0%</td>
<td align="right">1,502</td>
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
<td align="right">139,110</td>
<td align="right">100.0%</td>
<td align="right">139,148</td>
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
<td align="right">64,531,716</td>
<td align="right">100.0%</td>
<td align="right">64,045,369</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">251</td>
<td align="right">0.0%</td>
<td align="right">252</td>
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
<td align="right">2,393</td>
<td align="right">100.0%</td>
<td align="right">2,393</td>
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
<td align="right">591,590,156</td>
<td align="right">82.1%</td>
<td align="right">591,606,844</td>
<td align="right">82.1%</td>
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
<td align="right">128,815,273</td>
<td align="right">17.9%</td>
<td align="right">128,815,273</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">77,121,006</td>
<td align="right">3.9%</td>
<td align="right">72,656,447</td>
<td align="right">3.7%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">112,411,432</td>
<td align="right">5.7%</td>
<td align="right">106,431,873</td>
<td align="right">5.4%</td>
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
<td align="right">1,773,232,035</td>
<td align="right">90.3%</td>
<td align="right">1,795,280,212</td>
<td align="right">90.9%</td>
<td align="right">1.2%</td>
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
<td align="right">2,160,879</td>
<td align="right">97.6%</td>
<td align="right">2,047,947</td>
<td align="right">97.5%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">52,738</td>
<td align="right">2.4%</td>
<td align="right">51,697</td>
<td align="right">2.5%</td>
<td align="right">-2.0%</td>
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
<td align="right">6,005</td>
<td align="right">11.4%</td>
<td align="right">4,963</td>
<td align="right">9.6%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">271,294</td>
<td align="right">514.4%</td>
<td align="right">264,364</td>
<td align="right">511.4%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,352</td>
<td align="right">6.4%</td>
<td align="right">3,350</td>
<td align="right">6.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,317</td>
<td align="right">10.1%</td>
<td align="right">5,319</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">46.4%</td>
<td align="right">24,476</td>
<td align="right">47.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.5%</td>
<td align="right">7,666</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">814</td>
<td align="right">1.5%</td>
<td align="right">814</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">365</td>
<td align="right">0.7%</td>
<td align="right">365</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">111</td>
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
<td align="right">112,724,898</td>
<td align="right">100.0%</td>
<td align="right">1,232,478</td>
<td align="right">100.0%</td>
<td align="right">-98.9%</td>
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
<td align="right">700,842,095</td>
<td align="right">43.2%</td>
<td align="right">103,845,877</td>
<td align="right">10.1%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">922,798,732</td>
<td align="right">56.8%</td>
<td align="right">921,801,635</td>
<td align="right">89.9%</td>
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
<td align="right">182,262</td>
<td align="right">98.9%</td>
<td align="right">36,549</td>
<td align="right">94.5%</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,119</td>
<td align="right">1.1%</td>
<td align="right">2,121</td>
<td align="right">5.5%</td>
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
<td align="right">86,613</td>
<td align="right">47.5%</td>
<td align="right">341</td>
<td align="right">0.9%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,311</td>
<td align="right">2.9%</td>
<td align="right">178</td>
<td align="right">0.5%</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,343</td>
<td align="right">10.6%</td>
<td align="right">3,483</td>
<td align="right">9.5%</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.8%</td>
<td align="right">10,484</td>
<td align="right">28.7%</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,012</td>
<td align="right">1.7%</td>
<td align="right">3,011</td>
<td align="right">8.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">9.5%</td>
<td align="right">17,323</td>
<td align="right">47.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,661</td>
<td align="right">0.9%</td>
<td align="right">1,661</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.0%</td>
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
<td align="right">262,909,859</td>
<td align="right">5.2%</td>
<td align="right">140,943,224</td>
<td align="right">3.1%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">107,918,566</td>
<td align="right">2.1%</td>
<td align="right">63,625,650</td>
<td align="right">1.4%</td>
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
<td align="right">4,714,659,735</td>
<td align="right">92.7%</td>
<td align="right">4,406,196,100</td>
<td align="right">95.6%</td>
<td align="right">-6.5%</td>
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
<td align="right">2,085,583</td>
<td align="right">76.8%</td>
<td align="right">1,249,767</td>
<td align="right">71.1%</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">631,521</td>
<td align="right">23.2%</td>
<td align="right">507,510</td>
<td align="right">28.9%</td>
<td align="right">-19.6%</td>
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
<td align="right">18,878</td>
<td align="right">3.0%</td>
<td align="right">4,678</td>
<td align="right">0.9%</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">132,966</td>
<td align="right">21.1%</td>
<td align="right">33,901</td>
<td align="right">6.7%</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">20,478</td>
<td align="right">3.2%</td>
<td align="right">15,290</td>
<td align="right">3.0%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">77,675</td>
<td align="right">12.3%</td>
<td align="right">73,801</td>
<td align="right">14.5%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,977</td>
<td align="right">1.6%</td>
<td align="right">9,737</td>
<td align="right">1.9%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">97,703</td>
<td align="right">15.5%</td>
<td align="right">96,113</td>
<td align="right">18.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,306</td>
<td align="right">2.1%</td>
<td align="right">13,294</td>
<td align="right">2.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,652</td>
<td align="right">41.0%</td>
<td align="right">258,810</td>
<td align="right">51.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,809,605</td>
<td align="right">0.1%</td>
<td align="right">1,420,727</td>
<td align="right">0.1%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,238,703,838</td>
<td align="right">99.9%</td>
<td align="right">1,240,269,697</td>
<td align="right">99.9%</td>
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
<td align="right">999</td>
<td align="right">9.0%</td>
<td align="right">869</td>
<td align="right">8.0%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,051</td>
<td align="right">91.0%</td>
<td align="right">10,059</td>
<td align="right">92.0%</td>
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
<td align="left">sequence</td>
<td align="right">765</td>
<td align="right">76.6%</td>
<td align="right">635</td>
<td align="right">73.1%</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">13.6%</td>
<td align="right">136</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">9.8%</td>
<td align="right">98</td>
<td align="right">11.3%</td>
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
<td align="right">7,592,489,683</td>
<td align="right">3.6%</td>
<td align="right">2,680,680,025</td>
<td align="right">2.7%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">86,363,984,665</td>
<td align="right">41.1%</td>
<td align="right">39,594,543,461</td>
<td align="right">40.3%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">114,755,915,081</td>
<td align="right">54.6%</td>
<td align="right">54,923,473,554</td>
<td align="right">55.9%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,487,923,938</td>
<td align="right">0.7%</td>
<td align="right">1,047,463,054</td>
<td align="right">1.1%</td>
<td align="right">-29.6%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">1,456,806,568</td>
<td align="right">18.8%</td>
<td align="right">198,320,287</td>
<td align="right">7.0%</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,842,095</td>
<td align="right">9.0%</td>
<td align="right">103,845,877</td>
<td align="right">3.7%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">506,360,910</td>
<td align="right">6.5%</td>
<td align="right">94,044,084</td>
<td align="right">3.3%</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">544,984,303</td>
<td align="right">7.0%</td>
<td align="right">184,724,877</td>
<td align="right">6.5%</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,804,948,988</td>
<td align="right">36.1%</td>
<td align="right">1,094,513,034</td>
<td align="right">38.7%</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">262,909,859</td>
<td align="right">3.4%</td>
<td align="right">140,943,224</td>
<td align="right">5.0%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,736,925</td>
<td align="right">2.0%</td>
<td align="right">87,560,649</td>
<td align="right">3.1%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">819,620,728</td>
<td align="right">10.6%</td>
<td align="right">554,149,810</td>
<td align="right">19.6%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">174,743,081</td>
<td align="right">2.3%</td>
<td align="right">147,823,551</td>
<td align="right">5.2%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,273</td>
<td align="right">1.7%</td>
<td align="right">128,815,273</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,915,450</td>
<td align="right">5.5%</td>
<td align="right">30,909,584</td>
<td align="right">3.0%</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,003,861</td>
<td align="right">5.5%</td>
<td align="right">30,988,028</td>
<td align="right">3.0%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">53,569,377</td>
<td align="right">3.6%</td>
<td align="right">29,961,184</td>
<td align="right">2.9%</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">47,627,572</td>
<td align="right">3.2%</td>
<td align="right">26,705,200</td>
<td align="right">2.5%</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">368,055,714</td>
<td align="right">24.7%</td>
<td align="right">214,297,450</td>
<td align="right">20.5%</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">265,849,868</td>
<td align="right">17.9%</td>
<td align="right">175,383,728</td>
<td align="right">16.7%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,573,608</td>
<td align="right">5.5%</td>
<td align="right">55,428,632</td>
<td align="right">5.3%</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,264,414</td>
<td align="right">6.3%</td>
<td align="right">87,378,958</td>
<td align="right">8.3%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">86,055,741</td>
<td align="right">5.8%</td>
<td align="right">82,721,183</td>
<td align="right">7.9%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">84,855,074</td>
<td align="right">5.7%</td>
<td align="right">82,155,193</td>
<td align="right">7.8%</td>
<td align="right">-3.2%</td>
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
<td align="right">71,186,070</td>
<td align="right">1.1%</td>
<td align="right">70,335,447</td>
<td align="right">1.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">272,074,970</td>
<td align="right">4.1%</td>
<td align="right">273,432,958</td>
<td align="right">4.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,399,933,769</td>
<td align="right">80.9%</td>
<td align="right">5,410,110,994</td>
<td align="right">80.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,151,972,963</td>
<td align="right">77.2%</td>
<td align="right">5,160,811,391</td>
<td align="right">77.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">934,544,539</td>
<td align="right">14.0%</td>
<td align="right">935,743,774</td>
<td align="right">14.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">938,821,870</td>
<td align="right">14.1%</td>
<td align="right">940,021,105</td>
<td align="right">14.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,523,475,440</td>
<td align="right">22.8%</td>
<td align="right">1,524,922,009</td>
<td align="right">22.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,523,475,440</td>
<td align="right">22.8%</td>
<td align="right">1,524,922,009</td>
<td align="right">22.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">260,565,647</td>
<td align="right">3.9%</td>
<td align="right">260,794,308</td>
<td align="right">3.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,653,570</td>
<td align="right">8.8%</td>
<td align="right">584,900,904</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,886,590</td>
<td align="right">0.4%</td>
<td align="right">24,892,620</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,402</td>
<td align="right">2.0%</td>
<td align="right">132,513,402</td>
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
<td align="left">Mortal increfs</td>
<td align="right">24,988,293,966</td>
<td align="right">19.0%</td>
<td align="right">66,085,702,136</td>
<td align="right">48.6%</td>
<td align="right">164.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">32,624,451,213</td>
<td align="right">22.2%</td>
<td align="right">73,195,326,565</td>
<td align="right">47.9%</td>
<td align="right">124.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">78,431,905,186</td>
<td align="right">59.8%</td>
<td align="right">42,321,017,027</td>
<td align="right">31.1%</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">88,113,246,931</td>
<td align="right">59.9%</td>
<td align="right">52,525,198,438</td>
<td align="right">34.4%</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,566,960,016</td>
<td align="right">3.5%</td>
<td align="right">2,927,172,965</td>
<td align="right">2.2%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,853,044,959</td>
<td align="right">1.3%</td>
<td align="right">1,212,879,833</td>
<td align="right">0.8%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">475,949</td>
<td align="right">0.3%</td>
<td align="right">434,349</td>
<td align="right">0.3%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,216,017,942</td>
<td align="right"></td>
<td align="right">2,049,440,822</td>
<td align="right"></td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">62,239,322</td>
<td align="right"></td>
<td align="right">57,976,732</td>
<td align="right"></td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">67,661,693</td>
<td align="right"></td>
<td align="right">63,272,098</td>
<td align="right"></td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">23,258,167,317</td>
<td align="right">17.7%</td>
<td align="right">24,686,635,596</td>
<td align="right">18.1%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,576,736,555</td>
<td align="right">16.7%</td>
<td align="right">25,948,726,055</td>
<td align="right">17.0%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,227,922</td>
<td align="right"></td>
<td align="right">6,100,346</td>
<td align="right"></td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">168,614,124</td>
<td align="right"></td>
<td align="right">168,488,419</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,609,550,884</td>
<td align="right"></td>
<td align="right">6,605,482,834</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,420,919</td>
<td align="right">0.0%</td>
<td align="right">6,424,548</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,531,506</td>
<td align="right">0.4%</td>
<td align="right">71,506,309</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,930,803,654</td>
<td align="right">31.7%</td>
<td align="right">5,928,805,396</td>
<td align="right">31.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,008,756,079</td>
<td align="right">32.1%</td>
<td align="right">6,006,736,253</td>
<td align="right">32.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,709,837,013</td>
<td align="right"></td>
<td align="right">12,709,026,309</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,709,725,732</td>
<td align="right">67.9%</td>
<td align="right">12,708,921,383</td>
<td align="right">67.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,865,478,641</td>
<td align="right"></td>
<td align="right">2,865,639,619</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,443,421</td>
<td align="right">2.6%</td>
<td align="right">4,443,421</td>
<td align="right">2.6%</td>
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
<td align="right">364,646</td>
<td align="right">101,699,777</td>
<td align="right">9,590,921,533</td>
<td align="right">767,746,560</td>
<td align="right">764,152,596</td>
<td align="right">364,635</td>
<td align="right">101,087,342</td>
<td align="right">9,599,556,492</td>
<td align="right">764,233,589</td>
<td align="right">766,219,178</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,625,454,524</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,625,709,444</td>
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
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">0</td>
<td align="right">100</td>
<td align="right">100 / 0 !!</td>
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
<td align="right">100</td>
<td align="right">100 / 0 !!</td>
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
<td align="right">2,458</td>
<td align="right">2,458</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-03
