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
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,072</td>
<td align="right">2,272</td>
<td align="right">111.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,791,882,579</td>
<td align="right">4,257,003</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,724,902</td>
<td align="right">1,085,650</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">459,026,594</td>
<td align="right">9,328,783</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,358,406</td>
<td align="right">2,220,703</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">6,000,000</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,504,906,650</td>
<td align="right">187,037,926</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">401,289,961</td>
<td align="right">52,151,552</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,403,491,931</td>
<td align="right">184,765,405</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,585,081,341</td>
<td align="right">217,118,100</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,789,676</td>
<td align="right">101,295,661</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,275,546,453</td>
<td align="right">184,983,150</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,718,944,277</td>
<td align="right">419,233,383</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,754,455,763</td>
<td align="right">270,707,321</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,726,842</td>
<td align="right">84,014,295</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,123,696,730</td>
<td align="right">351,728,890</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">565,954,009</td>
<td align="right">94,060,607</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,482,960,455</td>
<td align="right">590,324,772</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,265,425,046</td>
<td align="right">386,940,856</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">88,979,079</td>
<td align="right">17,327,896</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">861,438,952</td>
<td align="right">167,847,715</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,809,451</td>
<td align="right">30,831,604</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,128,392</td>
<td align="right">23,287,428</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,252,080,277</td>
<td align="right">260,965,773</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">671,768,865</td>
<td align="right">140,180,633</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">690,694,337</td>
<td align="right">153,850,816</td>
<td align="right">-77.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,277,797</td>
<td align="right">76,364,204</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,694,557</td>
<td align="right">28,587,473</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,367,628</td>
<td align="right">14,818,660</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">377,603,808</td>
<td align="right">91,992,374</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">187,994,174</td>
<td align="right">45,845,797</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">940,070,406</td>
<td align="right">235,728,004</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,657,281,733</td>
<td align="right">416,677,945</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,284,139,883</td>
<td align="right">1,877,600,188</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">626,940,179</td>
<td align="right">165,795,089</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">253,095,751</td>
<td align="right">69,990,929</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,434,102,838</td>
<td align="right">953,069,501</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,531,638,603</td>
<td align="right">707,028,453</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,140,416,528</td>
<td align="right">600,106,514</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,243,768,020</td>
<td align="right">352,723,938</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,105,259,126</td>
<td align="right">599,734,435</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">77,896,787</td>
<td align="right">22,268,642</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">56,905,514</td>
<td align="right">16,420,619</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,436,387</td>
<td align="right">145,961,953</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">534,285,668</td>
<td align="right">154,984,781</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,354,432</td>
<td align="right">108,131,220</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,733,498,857</td>
<td align="right">837,265,751</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,839,323,782</td>
<td align="right">1,797,422,720</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,489,930,368</td>
<td align="right">786,051,773</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,388,297,235</td>
<td align="right">4,266,440,104</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,842,507</td>
<td align="right">2,504,368</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">352,582,586</td>
<td align="right">113,608,938</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,786,196</td>
<td align="right">24,180,684</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,731,800</td>
<td align="right">177,680,476</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,111,995,355</td>
<td align="right">3,318,327,394</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,387,231</td>
<td align="right">53,803,093</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,673,429,395</td>
<td align="right">3,628,691,178</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,040,119,448</td>
<td align="right">362,802,610</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">99,732,621</td>
<td align="right">35,102,700</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,214,839,459</td>
<td align="right">455,926,983</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">433,502,866</td>
<td align="right">163,417,621</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,357,628</td>
<td align="right">25,718,538</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">22,616,480</td>
<td align="right">8,671,647</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">261,511,041</td>
<td align="right">102,443,481</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">536,449,498</td>
<td align="right">213,959,468</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">90,430,400</td>
<td align="right">36,615,245</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,531,779,831</td>
<td align="right">3,506,976,212</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">72,974,806</td>
<td align="right">30,461,139</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">794,614,913</td>
<td align="right">331,722,887</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">2,597,140</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">780,885,858</td>
<td align="right">329,961,397</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,345,023,099</td>
<td align="right">994,300,183</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">33,492,728,795</td>
<td align="right">14,344,003,847</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,095,613,357</td>
<td align="right">482,377,041</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,366,469</td>
<td align="right">468,452,801</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,056,336,832</td>
<td align="right">476,769,075</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,537,198,335</td>
<td align="right">705,995,864</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,301,990</td>
<td align="right">60,585,922</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,888,626,507</td>
<td align="right">1,799,321,499</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">256,569,162</td>
<td align="right">121,952,757</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,022,269</td>
<td align="right">128,950,567</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,793,641</td>
<td align="right">75,503,051</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">290,125,056</td>
<td align="right">143,476,904</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">316,781,269</td>
<td align="right">158,112,081</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,628</td>
<td align="right">4,866,648</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">201,394,742</td>
<td align="right">100,987,555</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">233,988</td>
<td align="right">117,444</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">355,980,834</td>
<td align="right">179,003,829</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,466,342</td>
<td align="right">51,147,824</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">14,816</td>
<td align="right">7,744</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,542,375,590</td>
<td align="right">814,312,392</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,750,966</td>
<td align="right">941,716</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">283,088,383</td>
<td align="right">153,572,866</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,420,369,456</td>
<td align="right">1,313,664,045</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">59,159,120</td>
<td align="right">32,799,425</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">355,506,027</td>
<td align="right">197,125,384</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">774,165,329</td>
<td align="right">439,886,395</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,164,776,378</td>
<td align="right">1,801,083,305</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">116,417,392</td>
<td align="right">66,724,868</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,343,501</td>
<td align="right">4,311,179</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">801,742,447</td>
<td align="right">471,197,730</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,295,325</td>
<td align="right">103,607,626</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">132,081,818</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,358,441,959</td>
<td align="right">818,610,227</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,141</td>
<td align="right">114,765,159</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,750,039,520</td>
<td align="right">2,932,275,275</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">190,497,847</td>
<td align="right">118,256,472</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,796</td>
<td align="right">5,694,716</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">233,829,066</td>
<td align="right">149,795,142</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">485,178,873</td>
<td align="right">313,361,093</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">66,440,272</td>
<td align="right">42,929,823</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,381,489,369</td>
<td align="right">2,201,631,288</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,569,720</td>
<td align="right">161,390,188</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,519,557</td>
<td align="right">160,044,389</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">164,040,390</td>
<td align="right">108,656,313</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">75,633,047</td>
<td align="right">50,625,943</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">385,173,129</td>
<td align="right">259,848,668</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,215,858,691</td>
<td align="right">2,270,012,517</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">840,951,286</td>
<td align="right">593,782,977</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">325,922,248</td>
<td align="right">231,124,169</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,090,886</td>
<td align="right">2,192,187</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">678,226,132</td>
<td align="right">484,516,278</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,241,002,151</td>
<td align="right">4,532,704,073</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,358,969,271</td>
<td align="right">3,898,317,987</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">72,576,735</td>
<td align="right">53,588,224</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,784,319</td>
<td align="right">2,838,519</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">468,056,576</td>
<td align="right">354,388,720</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">68,562,492</td>
<td align="right">52,105,617</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,657,075</td>
<td align="right">1,262,258</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">943,020,473</td>
<td align="right">721,818,010</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">66,481,362</td>
<td align="right">51,553,291</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,122,129</td>
<td align="right">2,464,201</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">267,716,502</td>
<td align="right">212,911,901</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,171,249</td>
<td align="right">17,018,775</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,171,269</td>
<td align="right">17,018,795</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,844,496</td>
<td align="right">16,861,402</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">975,004,950</td>
<td align="right">789,947,964</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">80,979,415</td>
<td align="right">65,782,587</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">346,704,645</td>
<td align="right">283,828,860</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">335,173,463</td>
<td align="right">280,480,628</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,347,231</td>
<td align="right">350,167,053</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">115,333,162</td>
<td align="right">97,871,938</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">147,855,714</td>
<td align="right">126,111,570</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,165,319</td>
<td align="right">5,280,799</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,521,835</td>
<td align="right">60,802,948</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,097,606</td>
<td align="right">8,845,365</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">75,215,831</td>
<td align="right">66,953,071</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,705,210</td>
<td align="right">11,368,449</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">76,781</td>
<td align="right">69,551</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,587,181,425</td>
<td align="right">1,441,365,047</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">61,064,666</td>
<td align="right">55,539,634</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,356</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,098,361</td>
<td align="right">9,389,629</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,713</td>
<td align="right">31,495</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,431,052</td>
<td align="right">5,119,262</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,096,991</td>
<td align="right">148,366,821</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">463,870</td>
<td align="right">441,272</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,549</td>
<td align="right">3,389</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,112,357,370</td>
<td align="right">1,064,459,758</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,308,546</td>
<td align="right">183,868,565</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,637</td>
<td align="right">13,033</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">65,685,955</td>
<td align="right">63,683,973</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,747</td>
<td align="right">123,753,158</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">72,271,266</td>
<td align="right">70,189,817</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,515</td>
<td align="right">2,573</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,585,812</td>
<td align="right">27,947,997</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">243,303</td>
<td align="right">248,085</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,961,118</td>
<td align="right">35,547,049</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,863</td>
<td align="right">3,823</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">56,984</td>
<td align="right">56,504</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">214,345</td>
<td align="right">212,921</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,966,318</td>
<td align="right">418,145,041</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,544,199</td>
<td align="right">591,602,930</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,368</td>
<td align="right">5,359</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,658,173</td>
<td align="right">302,244,061</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,628</td>
<td align="right">72,564</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,756,412</td>
<td align="right">14,760,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,443</td>
<td align="right">41,965,283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">10,549,278</td>
<td align="right">10,549,268</td>
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
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,575</td>
<td align="right">98,575</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,850</td>
<td align="right">53,850</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
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
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">928,985,942</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">733,315,341</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,240,093,477</td>
<td align="right">87.1%</td>
<td align="right">3,743,959,378</td>
<td align="right">78.2%</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,344,092,769</td>
<td align="right">12.6%</td>
<td align="right">993,879,724</td>
<td align="right">20.7%</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">62,403,780</td>
<td align="right">0.3%</td>
<td align="right">52,173,551</td>
<td align="right">1.1%</td>
<td align="right">-16.4%</td>
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
<td align="right">913,014</td>
<td align="right">43.3%</td>
<td align="right">402,163</td>
<td align="right">28.6%</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,194,489</td>
<td align="right">56.7%</td>
<td align="right">1,002,457</td>
<td align="right">71.4%</td>
<td align="right">-16.1%</td>
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
<td align="left">subscr bytes</td>
<td align="right">22,292</td>
<td align="right">2.4%</td>
<td align="right">1,810</td>
<td align="right">0.5%</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">-81.8%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">9.4%</td>
<td align="right">16,343</td>
<td align="right">4.1%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">121,439</td>
<td align="right">13.3%</td>
<td align="right">25,835</td>
<td align="right">6.4%</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,588</td>
<td align="right">1.3%</td>
<td align="right">2,767</td>
<td align="right">0.7%</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,208</td>
<td align="right">8.1%</td>
<td align="right">18,461</td>
<td align="right">4.6%</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">114,964</td>
<td align="right">12.6%</td>
<td align="right">28,692</td>
<td align="right">7.1%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,210</td>
<td align="right">0.9%</td>
<td align="right">2,343</td>
<td align="right">0.6%</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,090</td>
<td align="right">0.1%</td>
<td align="right">333</td>
<td align="right">0.1%</td>
<td align="right">-69.4%</td>
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
<td align="right">23,516</td>
<td align="right">2.6%</td>
<td align="right">8,300</td>
<td align="right">2.1%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">42,916</td>
<td align="right">4.7%</td>
<td align="right">17,215</td>
<td align="right">4.3%</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">359</td>
<td align="right">0.0%</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,459</td>
<td align="right">4.8%</td>
<td align="right">20,822</td>
<td align="right">5.2%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,979</td>
<td align="right">3.7%</td>
<td align="right">19,835</td>
<td align="right">4.9%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">35,902</td>
<td align="right">3.9%</td>
<td align="right">21,015</td>
<td align="right">5.2%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,451</td>
<td align="right">2.1%</td>
<td align="right">11,552</td>
<td align="right">2.9%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">107,945</td>
<td align="right">11.8%</td>
<td align="right">72,756</td>
<td align="right">18.1%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,515</td>
<td align="right">0.9%</td>
<td align="right">6,194</td>
<td align="right">1.5%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">8,166</td>
<td align="right">0.9%</td>
<td align="right">6,477</td>
<td align="right">1.6%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">78,843</td>
<td align="right">8.6%</td>
<td align="right">63,001</td>
<td align="right">15.7%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">46,925</td>
<td align="right">5.1%</td>
<td align="right">37,615</td>
<td align="right">9.4%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">288</td>
<td align="right">0.1%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,336</td>
<td align="right">0.3%</td>
<td align="right">2,120</td>
<td align="right">0.5%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,163</td>
<td align="right">0.3%</td>
<td align="right">2,935</td>
<td align="right">0.7%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,115</td>
<td align="right">0.8%</td>
<td align="right">6,841</td>
<td align="right">1.7%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,036</td>
<td align="right">0.2%</td>
<td align="right">1,997</td>
<td align="right">0.5%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">1,364</td>
<td align="right">0.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,110</td>
<td align="right">0.3%</td>
<td align="right">3,130</td>
<td align="right">0.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">624</td>
<td align="right">0.1%</td>
<td align="right">626</td>
<td align="right">0.2%</td>
<td align="right">0.3%</td>
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
<td align="right">545,731,800</td>
<td align="right">100.0%</td>
<td align="right">177,680,476</td>
<td align="right">100.0%</td>
<td align="right">-67.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,105,147,453</td>
<td align="right">98.4%</td>
<td align="right">4,358,926,202</td>
<td align="right">96.8%</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">182,159,585</td>
<td align="right">1.6%</td>
<td align="right">142,193,615</td>
<td align="right">3.2%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">178,796,880</td>
<td align="right">1.6%</td>
<td align="right">139,585,280</td>
<td align="right">3.1%</td>
<td align="right">-21.9%</td>
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
<td align="right">3,605,862</td>
<td align="right">100.0%</td>
<td align="right">2,856,274</td>
<td align="right">100.0%</td>
<td align="right">-20.8%</td>
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
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">287</td>
<td align="right">196.6%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">754</td>
<td align="right">516.4%</td>
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
<td align="right">576,036</td>
<td align="right">96.6%</td>
<td align="right">576,034</td>
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
<td align="right">97.9%</td>
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
<td align="right">19,975</td>
<td align="right">100.0%</td>
<td align="right">20,373</td>
<td align="right">100.0%</td>
<td align="right">2.0%</td>
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
<td align="right">510,501,585</td>
<td align="right">10.2%</td>
<td align="right">83,904,738</td>
<td align="right">6.7%</td>
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
<td align="right">4,505,844,405</td>
<td align="right">89.8%</td>
<td align="right">1,168,137,467</td>
<td align="right">93.2%</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,270,934</td>
<td align="right">0.0%</td>
<td align="right">1,011,543</td>
<td align="right">0.1%</td>
<td align="right">-20.4%</td>
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
<td align="right">207,517</td>
<td align="right">83.4%</td>
<td align="right">91,411</td>
<td align="right">71.2%</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,409</td>
<td align="right">16.6%</td>
<td align="right">37,020</td>
<td align="right">28.8%</td>
<td align="right">-10.6%</td>
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
<td align="right">90,429</td>
<td align="right">43.6%</td>
<td align="right">4,071</td>
<td align="right">4.5%</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,834</td>
<td align="right">3.3%</td>
<td align="right">370</td>
<td align="right">0.4%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">10,446</td>
<td align="right">5.0%</td>
<td align="right">4,500</td>
<td align="right">4.9%</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,427</td>
<td align="right">21.9%</td>
<td align="right">31,385</td>
<td align="right">34.3%</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">11,306</td>
<td align="right">5.4%</td>
<td align="right">8,649</td>
<td align="right">9.5%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">196</td>
<td align="right">0.1%</td>
<td align="right">154</td>
<td align="right">0.2%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">953</td>
<td align="right">0.5%</td>
<td align="right">797</td>
<td align="right">0.9%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,324</td>
<td align="right">0.6%</td>
<td align="right">1,278</td>
<td align="right">1.4%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,776</td>
<td align="right">3.7%</td>
<td align="right">7,674</td>
<td align="right">8.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,279</td>
<td align="right">11.2%</td>
<td align="right">23,005</td>
<td align="right">25.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,898</td>
<td align="right">0.9%</td>
<td align="right">1,880</td>
<td align="right">2.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,649</td>
<td align="right">3.7%</td>
<td align="right">7,648</td>
<td align="right">8.4%</td>
<td align="right">-0.0%</td>
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
<td align="right">2,186,555,042</td>
<td align="right">93.4%</td>
<td align="right">433,396,423</td>
<td align="right">85.0%</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">153,733,489</td>
<td align="right">6.6%</td>
<td align="right">75,462,446</td>
<td align="right">14.8%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,403,587</td>
<td align="right">0.1%</td>
<td align="right">728,519</td>
<td align="right">0.1%</td>
<td align="right">-48.1%</td>
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
<td align="right">28,589</td>
<td align="right">33.0%</td>
<td align="right">16,053</td>
<td align="right">29.5%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">58,042</td>
<td align="right">67.0%</td>
<td align="right">38,295</td>
<td align="right">70.5%</td>
<td align="right">-34.0%</td>
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
<td align="right">21,455</td>
<td align="right">37.0%</td>
<td align="right">7,770</td>
<td align="right">20.3%</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,604</td>
<td align="right">25.2%</td>
<td align="right">11,264</td>
<td align="right">29.4%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,978</td>
<td align="right">18.9%</td>
<td align="right">9,077</td>
<td align="right">23.7%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,005</td>
<td align="right">19.0%</td>
<td align="right">10,184</td>
<td align="right">26.6%</td>
<td align="right">-7.5%</td>
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
<td align="right">1,504,465,794</td>
<td align="right">29.3%</td>
<td align="right">186,928,892</td>
<td align="right">13.5%</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,977,444</td>
<td align="right">3.2%</td>
<td align="right">44,186,172</td>
<td align="right">3.2%</td>
<td align="right">-73.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,472,838,394</td>
<td align="right">67.5%</td>
<td align="right">1,157,180,840</td>
<td align="right">83.3%</td>
<td align="right">-66.7%</td>
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
<td align="right">435,456</td>
<td align="right">12.3%</td>
<td align="right">103,642</td>
<td align="right">11.0%</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,099,127</td>
<td align="right">87.7%</td>
<td align="right">838,944</td>
<td align="right">89.0%</td>
<td align="right">-72.9%</td>
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
<td align="right">171,565</td>
<td align="right">39.4%</td>
<td align="right">4,151</td>
<td align="right">4.0%</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,676</td>
<td align="right">19.2%</td>
<td align="right">10,795</td>
<td align="right">10.4%</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,705</td>
<td align="right">8.0%</td>
<td align="right">5,499</td>
<td align="right">5.3%</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,284</td>
<td align="right">4.2%</td>
<td align="right">3,140</td>
<td align="right">3.0%</td>
<td align="right">-82.8%</td>
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
<td align="right">3,138</td>
<td align="right">0.7%</td>
<td align="right">866</td>
<td align="right">0.8%</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,543</td>
<td align="right">2.4%</td>
<td align="right">3,376</td>
<td align="right">3.3%</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,537</td>
<td align="right">2.4%</td>
<td align="right">3,390</td>
<td align="right">3.3%</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">533</td>
<td align="right">0.1%</td>
<td align="right">248</td>
<td align="right">0.2%</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,114</td>
<td align="right">0.7%</td>
<td align="right">1,618</td>
<td align="right">1.6%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,083</td>
<td align="right">1.4%</td>
<td align="right">4,259</td>
<td align="right">4.1%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,077</td>
<td align="right">4.2%</td>
<td align="right">12,735</td>
<td align="right">12.3%</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">69,374</td>
<td align="right">15.9%</td>
<td align="right">49,704</td>
<td align="right">48.0%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,284</td>
<td align="right">1.0%</td>
<td align="right">3,293</td>
<td align="right">3.2%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">221</td>
<td align="right">0.2%</td>
<td align="right">-15.0%</td>
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
<td align="left">string</td>
<td align="right">2,710,702</td>
<td align="right">2,710,702 / 0 !!</td>
<td align="right">1,585,754</td>
<td align="right">1,585,754 / 0 !!</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">171,694,867</td>
<td align="right">171,694,867 / 0 !!</td>
<td align="right">119,980,999</td>
<td align="right">119,980,999 / 0 !!</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,508,985</td>
<td align="right">5,508,985 / 0 !!</td>
<td align="right">4,039,306</td>
<td align="right">4,039,306 / 0 !!</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">304,488,973</td>
<td align="right">304,488,973 / 0 !!</td>
<td align="right">243,098,256</td>
<td align="right">243,098,256 / 0 !!</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,924,827</td>
<td align="right">101,924,827 / 0 !!</td>
<td align="right">84,869,766</td>
<td align="right">84,869,766 / 0 !!</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">119,408,555</td>
<td align="right">119,408,555 / 0 !!</td>
<td align="right">107,271,973</td>
<td align="right">107,271,973 / 0 !!</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,933,003</td>
<td align="right">34,933,003 / 0 !!</td>
<td align="right">34,258,256</td>
<td align="right">34,258,256 / 0 !!</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,157,203</td>
<td align="right">12,157,203 / 0 !!</td>
<td align="right">12,037,992</td>
<td align="right">12,037,992 / 0 !!</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,959,111</td>
<td align="right">341,959,111 / 0 !!</td>
<td align="right">341,360,490</td>
<td align="right">341,360,490 / 0 !!</td>
<td align="right">-0.2%</td>
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
<td align="right">11,985,648,997</td>
<td align="right">87.8%</td>
<td align="right">6,201,613,470</td>
<td align="right">86.6%</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">860,607,078</td>
<td align="right">6.3%</td>
<td align="right">488,411,178</td>
<td align="right">6.8%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">799,969,482</td>
<td align="right">5.9%</td>
<td align="right">469,803,160</td>
<td align="right">6.6%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,438,767</td>
<td align="right">0.0%</td>
<td align="right">1,005,161</td>
<td align="right">0.0%</td>
<td align="right">-30.1%</td>
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
<td align="right">16,316,574</td>
<td align="right">97.0%</td>
<td align="right">9,330,729</td>
<td align="right">95.7%</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">505,601</td>
<td align="right">3.0%</td>
<td align="right">423,360</td>
<td align="right">4.3%</td>
<td align="right">-16.3%</td>
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
<td align="right">73,627</td>
<td align="right">14.6%</td>
<td align="right">33,697</td>
<td align="right">8.0%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,102</td>
<td align="right">0.2%</td>
<td align="right">703</td>
<td align="right">0.2%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,157</td>
<td align="right">1.6%</td>
<td align="right">5,707</td>
<td align="right">1.3%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">54,639</td>
<td align="right">10.8%</td>
<td align="right">39,477</td>
<td align="right">9.3%</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,316</td>
<td align="right">1.1%</td>
<td align="right">4,064</td>
<td align="right">1.0%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,439</td>
<td align="right">4.8%</td>
<td align="right">19,508</td>
<td align="right">4.6%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,791</td>
<td align="right">3.1%</td>
<td align="right">13,691</td>
<td align="right">3.2%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,739</td>
<td align="right">0.5%</td>
<td align="right">2,378</td>
<td align="right">0.6%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">53,188</td>
<td align="right">10.5%</td>
<td align="right">47,138</td>
<td align="right">11.1%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,841</td>
<td align="right">0.4%</td>
<td align="right">1,687</td>
<td align="right">0.4%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,720</td>
<td align="right">0.3%</td>
<td align="right">1,622</td>
<td align="right">0.4%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">0.9%</td>
<td align="right">4,446</td>
<td align="right">1.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">573</td>
<td align="right">0.1%</td>
<td align="right">573</td>
<td align="right">0.1%</td>
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
<td align="right">9,220,764,767</td>
<td align="right">99.8%</td>
<td align="right">3,999,006,840</td>
<td align="right">99.6%</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">48,384</td>
<td align="right">0.0%</td>
<td align="right">47,168</td>
<td align="right">0.0%</td>
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
<td align="right">14,622,519</td>
<td align="right">0.2%</td>
<td align="right">14,622,595</td>
<td align="right">0.4%</td>
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
<td align="right">1,376</td>
<td align="right">0.0%</td>
<td align="right">1,376</td>
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
<td align="right">134,598</td>
<td align="right">100.0%</td>
<td align="right">138,433</td>
<td align="right">100.0%</td>
<td align="right">2.8%</td>
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
<td align="right">64,155,552</td>
<td align="right">100.0%</td>
<td align="right">57,731,821</td>
<td align="right">100.0%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">205</td>
<td align="right">0.0%</td>
<td align="right">203</td>
<td align="right">0.0%</td>
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
<td align="right">2,310</td>
<td align="right">100.0%</td>
<td align="right">2,370</td>
<td align="right">100.0%</td>
<td align="right">2.6%</td>
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
<td align="right">593,529,488</td>
<td align="right">82.2%</td>
<td align="right">591,588,219</td>
<td align="right">82.1%</td>
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
<td align="right">128,816,934</td>
<td align="right">17.8%</td>
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
<td align="right">114,217,389</td>
<td align="right">5.7%</td>
<td align="right">79,832,938</td>
<td align="right">5.1%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">66,396,764</td>
<td align="right">3.3%</td>
<td align="right">51,472,438</td>
<td align="right">3.3%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,812,784,830</td>
<td align="right">90.9%</td>
<td align="right">1,437,627,752</td>
<td align="right">91.6%</td>
<td align="right">-20.7%</td>
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
<td align="right">2,193,963</td>
<td align="right">98.0%</td>
<td align="right">1,547,124</td>
<td align="right">97.5%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">44,933</td>
<td align="right">2.0%</td>
<td align="right">39,528</td>
<td align="right">2.5%</td>
<td align="right">-12.0%</td>
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
<td align="right">19,647</td>
<td align="right">43.7%</td>
<td align="right">15,607</td>
<td align="right">39.5%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">5,799</td>
<td align="right">12.9%</td>
<td align="right">4,635</td>
<td align="right">11.7%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,321</td>
<td align="right">2.9%</td>
<td align="right">1,175</td>
<td align="right">3.0%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">0.9%</td>
<td align="right">379</td>
<td align="right">1.0%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">753</td>
<td align="right">1.7%</td>
<td align="right">693</td>
<td align="right">1.8%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">248,243</td>
<td align="right">552.5%</td>
<td align="right">239,826</td>
<td align="right">606.7%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,348</td>
<td align="right">7.5%</td>
<td align="right">3,442</td>
<td align="right">8.7%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,227</td>
<td align="right">16.1%</td>
<td align="right">7,207</td>
<td align="right">18.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,741</td>
<td align="right">8.3%</td>
<td align="right">3,737</td>
<td align="right">9.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">363</td>
<td align="right">0.8%</td>
<td align="right">363</td>
<td align="right">0.9%</td>
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
<td align="right">112,724,902</td>
<td align="right">100.0%</td>
<td align="right">1,085,650</td>
<td align="right">100.0%</td>
<td align="right">-99.0%</td>
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
<td align="right">700,605,771</td>
<td align="right">43.3%</td>
<td align="right">101,258,803</td>
<td align="right">32.8%</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">918,534,375</td>
<td align="right">56.7%</td>
<td align="right">207,668,605</td>
<td align="right">67.2%</td>
<td align="right">-77.4%</td>
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
<td align="right">940</td>
<td align="right">0.0%</td>
<td align="right">-57.7%</td>
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
<td align="right">181,879</td>
<td align="right">98.9%</td>
<td align="right">34,715</td>
<td align="right">94.1%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,066</td>
<td align="right">1.1%</td>
<td align="right">2,163</td>
<td align="right">5.9%</td>
<td align="right">4.7%</td>
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
<td align="right">86,545</td>
<td align="right">47.6%</td>
<td align="right">273</td>
<td align="right">0.8%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,315</td>
<td align="right">2.9%</td>
<td align="right">47</td>
<td align="right">0.1%</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,183</td>
<td align="right">10.5%</td>
<td align="right">3,323</td>
<td align="right">9.6%</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.9%</td>
<td align="right">10,483</td>
<td align="right">30.2%</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,991</td>
<td align="right">1.6%</td>
<td align="right">2,511</td>
<td align="right">7.2%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">0.9%</td>
<td align="right">1,563</td>
<td align="right">4.5%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,165</td>
<td align="right">9.4%</td>
<td align="right">16,447</td>
<td align="right">47.4%</td>
<td align="right">-4.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,728,999,010</td>
<td align="right">92.8%</td>
<td align="right">2,217,552,997</td>
<td align="right">92.5%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">255,922,017</td>
<td align="right">5.0%</td>
<td align="right">121,542,363</td>
<td align="right">5.1%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">110,683,567</td>
<td align="right">2.2%</td>
<td align="right">57,647,965</td>
<td align="right">2.4%</td>
<td align="right">-47.9%</td>
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
<td align="right">2,136,867</td>
<td align="right">78.2%</td>
<td align="right">1,137,456</td>
<td align="right">76.0%</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">596,954</td>
<td align="right">21.8%</td>
<td align="right">359,167</td>
<td align="right">24.0%</td>
<td align="right">-39.8%</td>
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
<td align="right">126,705</td>
<td align="right">21.2%</td>
<td align="right">26,551</td>
<td align="right">7.4%</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,856</td>
<td align="right">3.2%</td>
<td align="right">4,655</td>
<td align="right">1.3%</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">72,062</td>
<td align="right">12.1%</td>
<td align="right">37,633</td>
<td align="right">10.5%</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,310</td>
<td align="right">2.7%</td>
<td align="right">9,383</td>
<td align="right">2.6%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">83,575</td>
<td align="right">14.0%</td>
<td align="right">54,129</td>
<td align="right">15.1%</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,836</td>
<td align="right">43.2%</td>
<td align="right">206,220</td>
<td align="right">57.4%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,725</td>
<td align="right">1.6%</td>
<td align="right">8,693</td>
<td align="right">2.4%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,043</td>
<td align="right">1.7%</td>
<td align="right">10,061</td>
<td align="right">2.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
<td align="right">1,420</td>
<td align="right">0.4%</td>
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
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">1,237,809,996</td>
<td align="right">99.9%</td>
<td align="right">494,256,610</td>
<td align="right">99.7%</td>
<td align="right">-60.1%</td>
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
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,646,325</td>
<td align="right">0.1%</td>
<td align="right">1,251,561</td>
<td align="right">0.3%</td>
<td align="right">-24.0%</td>
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
<td align="right">929</td>
<td align="right">8.6%</td>
<td align="right">787</td>
<td align="right">7.3%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,901</td>
<td align="right">91.4%</td>
<td align="right">9,950</td>
<td align="right">92.7%</td>
<td align="right">0.5%</td>
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
<td align="right">694</td>
<td align="right">74.7%</td>
<td align="right">553</td>
<td align="right">70.3%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">99</td>
<td align="right">10.7%</td>
<td align="right">98</td>
<td align="right">12.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">14.6%</td>
<td align="right">136</td>
<td align="right">17.3%</td>
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
<td align="right">8,239,626,612</td>
<td align="right">3.9%</td>
<td align="right">2,893,136,065</td>
<td align="right">3.3%</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">78,577,244,250</td>
<td align="right">37.3%</td>
<td align="right">31,735,713,608</td>
<td align="right">36.5%</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">122,126,769,459</td>
<td align="right">58.0%</td>
<td align="right">51,373,129,929</td>
<td align="right">59.1%</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,497,533,575</td>
<td align="right">0.7%</td>
<td align="right">866,991,134</td>
<td align="right">1.0%</td>
<td align="right">-42.1%</td>
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
<td align="right">1,504,465,794</td>
<td align="right">20.6%</td>
<td align="right">186,928,892</td>
<td align="right">7.3%</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,605,771</td>
<td align="right">9.6%</td>
<td align="right">101,258,803</td>
<td align="right">4.0%</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,501,585</td>
<td align="right">7.0%</td>
<td align="right">83,904,738</td>
<td align="right">3.3%</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,731,800</td>
<td align="right">7.5%</td>
<td align="right">177,680,476</td>
<td align="right">7.0%</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,344,092,769</td>
<td align="right">32.0%</td>
<td align="right">993,879,724</td>
<td align="right">39.0%</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">255,922,017</td>
<td align="right">3.5%</td>
<td align="right">121,542,363</td>
<td align="right">4.8%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,733,489</td>
<td align="right">2.1%</td>
<td align="right">75,462,446</td>
<td align="right">3.0%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">799,969,482</td>
<td align="right">10.9%</td>
<td align="right">469,803,160</td>
<td align="right">18.4%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">178,796,880</td>
<td align="right">2.4%</td>
<td align="right">139,585,280</td>
<td align="right">5.5%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,934</td>
<td align="right">1.8%</td>
<td align="right">128,816,934</td>
<td align="right">5.1%</td>
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
<td align="right">81,896,897</td>
<td align="right">5.5%</td>
<td align="right">22,090,964</td>
<td align="right">2.5%</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">365,457,473</td>
<td align="right">24.4%</td>
<td align="right">174,001,898</td>
<td align="right">20.1%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,476,793</td>
<td align="right">3.6%</td>
<td align="right">27,359,052</td>
<td align="right">3.2%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,376,240</td>
<td align="right">3.3%</td>
<td align="right">25,451,057</td>
<td align="right">2.9%</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">264,669,917</td>
<td align="right">17.7%</td>
<td align="right">137,002,344</td>
<td align="right">15.8%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,669,232</td>
<td align="right">5.5%</td>
<td align="right">49,021,517</td>
<td align="right">5.7%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,987,984</td>
<td align="right">6.3%</td>
<td align="right">63,439,872</td>
<td align="right">7.3%</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,834,573</td>
<td align="right">5.5%</td>
<td align="right">58,635,378</td>
<td align="right">6.8%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">89,932,787</td>
<td align="right">6.0%</td>
<td align="right">68,586,180</td>
<td align="right">7.9%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,003,152</td>
<td align="right">5.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">24,730,357</td>
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
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,457</td>
<td align="right">0.1%</td>
<td align="right">2,125,982</td>
<td align="right">0.0%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,416,048,848</td>
<td align="right">81.0%</td>
<td align="right">4,380,016,147</td>
<td align="right">77.3%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">275,686,755</td>
<td align="right">4.1%</td>
<td align="right">228,168,983</td>
<td align="right">4.0%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,095,016,492</td>
<td align="right">76.2%</td>
<td align="right">4,222,552,544</td>
<td align="right">74.5%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,007,197,735</td>
<td align="right">15.1%</td>
<td align="right">869,470,893</td>
<td align="right">15.3%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,002,920,415</td>
<td align="right">15.0%</td>
<td align="right">867,341,088</td>
<td align="right">15.3%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,483,246</td>
<td align="right">3.9%</td>
<td align="right">227,867,860</td>
<td align="right">4.0%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,037,792</td>
<td align="right">1.1%</td>
<td align="right">63,680,842</td>
<td align="right">1.1%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,591,669,036</td>
<td align="right">23.8%</td>
<td align="right">1,444,485,645</td>
<td align="right">25.5%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,591,669,036</td>
<td align="right">23.8%</td>
<td align="right">1,444,485,645</td>
<td align="right">25.5%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,591,063</td>
<td align="right">0.4%</td>
<td align="right">22,760,833</td>
<td align="right">0.4%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,471,301</td>
<td align="right">8.7%</td>
<td align="right">575,014,752</td>
<td align="right">10.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,863</td>
<td align="right">0.0%</td>
<td align="right">3,823</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,898</td>
<td align="right">2.0%</td>
<td align="right">132,513,898</td>
<td align="right">2.3%</td>
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
<td align="right">27,872,084</td>
<td align="right"></td>
<td align="right">4,680,018</td>
<td align="right"></td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">84,862,300</td>
<td align="right"></td>
<td align="right">43,678,800</td>
<td align="right"></td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">57,793,004</td>
<td align="right"></td>
<td align="right">39,260,498</td>
<td align="right"></td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">306,770</td>
<td align="right">0.2%</td>
<td align="right">219,030</td>
<td align="right">0.1%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,426,342,792</td>
<td align="right"></td>
<td align="right">1,746,067,242</td>
<td align="right"></td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,362,266,499</td>
<td align="right"></td>
<td align="right">1,735,903,485</td>
<td align="right"></td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,159,597,908</td>
<td align="right"></td>
<td align="right">5,139,385,667</td>
<td align="right"></td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,484,793,010</td>
<td align="right">28.7%</td>
<td align="right">4,583,230,865</td>
<td align="right">26.7%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,562,427,916</td>
<td align="right">29.1%</td>
<td align="right">4,660,311,684</td>
<td align="right">27.1%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">24,961,377,892</td>
<td align="right">27.2%</td>
<td align="right">21,521,922,851</td>
<td align="right">26.9%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">50,150,423,792</td>
<td align="right">46.1%</td>
<td align="right">43,597,439,025</td>
<td align="right">45.4%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">39,076,719,105</td>
<td align="right">42.6%</td>
<td align="right">34,013,390,951</td>
<td align="right">42.5%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">22,996,629,649</td>
<td align="right">25.1%</td>
<td align="right">20,171,715,713</td>
<td align="right">25.2%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">31,769,178,444</td>
<td align="right">29.2%</td>
<td align="right">27,943,582,135</td>
<td align="right">29.1%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,945,940,366</td>
<td align="right">22.9%</td>
<td align="right">22,674,610,166</td>
<td align="right">23.6%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,643,377,417</td>
<td align="right">5.1%</td>
<td align="right">4,252,660,318</td>
<td align="right">5.3%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,572,428,995</td>
<td align="right">70.9%</td>
<td align="right">12,519,098,961</td>
<td align="right">72.9%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,572,576,816</td>
<td align="right"></td>
<td align="right">12,519,240,238</td>
<td align="right"></td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,612,432</td>
<td align="right"></td>
<td align="right">161,958,693</td>
<td align="right"></td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,860,587,909</td>
<td align="right">1.7%</td>
<td align="right">1,764,250,222</td>
<td align="right">1.8%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,365,270</td>
<td align="right">0.0%</td>
<td align="right">6,221,117</td>
<td align="right">0.0%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,269,636</td>
<td align="right">0.4%</td>
<td align="right">70,859,702</td>
<td align="right">0.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,404,476</td>
<td align="right">1.9%</td>
<td align="right">3,404,476</td>
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
<td align="right">364,883</td>
<td align="right">101,643,286</td>
<td align="right">9,529,890,337</td>
<td align="right">753,763,898</td>
<td align="right">766,144,605</td>
<td align="right">352,086</td>
<td align="right">68,781,546</td>
<td align="right">8,985,117,692</td>
<td align="right">732,331,653</td>
<td align="right">717,124,904</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,677,218,808</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,677,449,136</td>
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
<td align="right">0</td>
<td align="right">101</td>
<td align="right">101 / 0 !!</td>
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
<td align="right">101</td>
<td align="right">101 / 0 !!</td>
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
<td align="right">2,378</td>
<td align="right">-0.8%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-02
