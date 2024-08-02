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
<td align="right">36,564,975</td>
<td align="right">337.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">81,682,682</td>
<td align="right">1,469,643</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,451,701</td>
<td align="right">2,402,419</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">135,755,200</td>
<td align="right">4,988,362</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">142,537,682</td>
<td align="right">8,824,104</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,714,481</td>
<td align="right">5,146,855</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">334,209,893</td>
<td align="right">30,648,360</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,411,421</td>
<td align="right">549,561</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,906,038</td>
<td align="right">77,978,733</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">283,352,996</td>
<td align="right">41,632,628</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">294,705,193</td>
<td align="right">62,826,239</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">153,900</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">118,740,764</td>
<td align="right">29,594,774</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68,000,940</td>
<td align="right">17,918,204</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">89,960</td>
<td align="right">25,800</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">49,289,802</td>
<td align="right">16,232,992</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,763,227</td>
<td align="right">22,740,133</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">66,953,723</td>
<td align="right">23,081,783</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,101,356</td>
<td align="right">17,465,192</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">146,449,176</td>
<td align="right">55,257,264</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,264,258</td>
<td align="right">31,426,747</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,636,927</td>
<td align="right">41,063,771</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,461,660</td>
<td align="right">3,047,800</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">214,581,775</td>
<td align="right">92,344,838</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">59,218,322</td>
<td align="right">26,057,850</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,588,899</td>
<td align="right">56,877,376</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">404,145,744</td>
<td align="right">184,523,362</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">803,777,427</td>
<td align="right">367,640,416</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">79,282,163</td>
<td align="right">36,459,845</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,362</td>
<td align="right">88,200,700</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,016,771,133</td>
<td align="right">484,501,273</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">385,202,810</td>
<td align="right">189,369,167</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">222,980</td>
<td align="right">112,685</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,804,991</td>
<td align="right">38,074,026</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">386,018,873</td>
<td align="right">203,854,783</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">114,863,042</td>
<td align="right">61,035,087</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,877,686</td>
<td align="right">5,269,514</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">210,432,688</td>
<td align="right">115,040,488</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,371,101,062</td>
<td align="right">785,908,740</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,672,300,496</td>
<td align="right">3,327,341,612</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">298,250,253</td>
<td align="right">178,204,138</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">385,609,250</td>
<td align="right">230,535,461</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,105,024</td>
<td align="right">55,551,038</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,104,613,021</td>
<td align="right">2,507,060,142</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,142,641</td>
<td align="right">56,174,572</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">100,345,617</td>
<td align="right">62,179,945</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">230,664,610</td>
<td align="right">143,137,829</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">87,769,033</td>
<td align="right">54,826,326</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,098,269,674</td>
<td align="right">2,583,137,024</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">173,188,709</td>
<td align="right">109,820,872</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,247,916</td>
<td align="right">40,105,918</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">138,058,623</td>
<td align="right">92,079,338</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,420</td>
<td align="right">115,841</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,947,810</td>
<td align="right">269,487,712</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">24,142,297</td>
<td align="right">16,242,522</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,808,661</td>
<td align="right">21,562,861</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,385,176</td>
<td align="right">7,053,626</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,818,198,454</td>
<td align="right">1,916,579,263</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">76,286,312</td>
<td align="right">52,194,834</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">409,256,905</td>
<td align="right">280,670,301</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">42,435,517</td>
<td align="right">29,151,272</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,410,665,281</td>
<td align="right">972,956,871</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">194,479,637</td>
<td align="right">134,747,209</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">636,688,192</td>
<td align="right">442,095,614</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">21,172,796</td>
<td align="right">14,716,862</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">108,592,655</td>
<td align="right">75,668,879</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,399,820,452</td>
<td align="right">1,676,632,961</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">942,143,708</td>
<td align="right">672,473,641</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,525,743,769</td>
<td align="right">2,517,441,334</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,294,945,073</td>
<td align="right">2,364,028,915</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,550,970</td>
<td align="right">34,180,125</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">828,627,866</td>
<td align="right">598,832,791</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">677,180,472</td>
<td align="right">495,249,164</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">35,526,971</td>
<td align="right">26,136,412</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">318,139,618</td>
<td align="right">234,806,616</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">140,540,021</td>
<td align="right">103,926,032</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,871,088,879</td>
<td align="right">1,392,870,290</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,611,089,010</td>
<td align="right">16,160,435,842</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">30,785,532</td>
<td align="right">23,178,590</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">199,227,492</td>
<td align="right">150,455,458</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,451,032,886</td>
<td align="right">1,853,374,097</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,612,128</td>
<td align="right">35,561,700</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">201,453,046</td>
<td align="right">154,758,964</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">907,886,373</td>
<td align="right">700,554,003</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,998,854,364</td>
<td align="right">4,637,461,943</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,819,132</td>
<td align="right">31,665,435</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,222,743,681</td>
<td align="right">4,831,208,784</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,489,106,446</td>
<td align="right">4,278,804,628</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">4,716,218</td>
<td align="right">3,719,414</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">195,635,477</td>
<td align="right">155,861,922</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,240,444,558</td>
<td align="right">3,379,275,375</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">348,124,146</td>
<td align="right">280,307,780</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">378,229,624</td>
<td align="right">308,341,723</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">162,000,736</td>
<td align="right">132,481,438</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">331,590,179</td>
<td align="right">271,825,613</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">366,813,344</td>
<td align="right">301,210,513</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">59,677,580</td>
<td align="right">49,188,570</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">739,592,456</td>
<td align="right">626,918,138</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">773,991,890</td>
<td align="right">663,964,018</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,109,786,915</td>
<td align="right">960,631,785</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">901,814,696</td>
<td align="right">781,562,009</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,259,834,825</td>
<td align="right">1,092,421,483</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">485,240</td>
<td align="right">421,840</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">679,742,740</td>
<td align="right">596,584,046</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">452,636,213</td>
<td align="right">397,434,263</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,568,258,883</td>
<td align="right">1,381,563,872</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,137,025,674</td>
<td align="right">1,002,304,315</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">666,565,497</td>
<td align="right">604,280,352</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">431,663,764</td>
<td align="right">391,563,120</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,297,223</td>
<td align="right">196,320,319</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">272,673,961</td>
<td align="right">249,463,612</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,913,558</td>
<td align="right">137,510,663</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,365,472</td>
<td align="right">2,174,719</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,872,699</td>
<td align="right">75,361,503</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">791,276,282</td>
<td align="right">729,194,475</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">20,422,358</td>
<td align="right">18,844,869</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">198,600,474</td>
<td align="right">184,065,839</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">486,450,449</td>
<td align="right">452,716,660</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">556,449,862</td>
<td align="right">518,080,377</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,024,186</td>
<td align="right">374,538,273</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">56,501,392</td>
<td align="right">52,885,004</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,373,998,061</td>
<td align="right">4,108,369,044</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,866,729</td>
<td align="right">3,651,966</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">219,498</td>
<td align="right">207,464</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">54,270,958</td>
<td align="right">51,299,386</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,290,129,590</td>
<td align="right">1,229,217,514</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">166,847,458</td>
<td align="right">159,311,713</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">276,487,304</td>
<td align="right">288,710,950</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">421,590,441</td>
<td align="right">404,129,104</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,910,919</td>
<td align="right">140,905,573</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,850,607</td>
<td align="right">51,819,558</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,569,243</td>
<td align="right">153,079,995</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,152,174</td>
<td align="right">20,515,144</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,168,547</td>
<td align="right">227,904,108</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,584</td>
<td align="right">1,842,838</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,466,248</td>
<td align="right">17,182,148</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">205,801,317</td>
<td align="right">202,511,642</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,961,784</td>
<td align="right">10,807,114</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">481,502,567</td>
<td align="right">477,897,897</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,641,564</td>
<td align="right">224,335,951</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,644,791,915</td>
<td align="right">2,657,697,734</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,380,686</td>
<td align="right">1,042,733,441</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">108,507,865</td>
<td align="right">108,138,749</td>
<td align="right">-0.3%</td>
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
<td align="right">227,771,815</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,603,445,886</td>
<td align="right">1,602,288,815</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,639,873</td>
<td align="right">3,637,271</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,958</td>
<td align="right">687,763</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">484,955,459</td>
<td align="right">484,822,258</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,884</td>
<td align="right">14,888</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,809,121</td>
<td align="right">1,808,828</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,693,789</td>
<td align="right">20,697,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,159,934</td>
<td align="right">21,163,089</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,229,348</td>
<td align="right">274,265,069</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,659,148</td>
<td align="right">9,658,008</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,237,103</td>
<td align="right">9,236,151</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,950,802</td>
<td align="right">5,950,742</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,344,679</td>
<td align="right">20,344,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,338,310</td>
<td align="right">233,338,348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,319,344</td>
<td align="right">173,319,338</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,220,538</td>
<td align="right">786,220,523</td>
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
<td align="right">299,311,508</td>
<td align="right">3.1%</td>
<td align="right">-31.5%</td>
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
<td align="right">9,402,434,891</td>
<td align="right">96.9%</td>
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
<td align="right">419,234</td>
<td align="right">29.8%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,122,503</td>
<td align="right">65.3%</td>
<td align="right">985,379</td>
<td align="right">70.2%</td>
<td align="right">-12.2%</td>
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
<td align="right">21,773</td>
<td align="right">2.2%</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,026</td>
<td align="right">0.4%</td>
<td align="right">2,551</td>
<td align="right">0.3%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,402</td>
<td align="right">7.3%</td>
<td align="right">53,873</td>
<td align="right">5.5%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,534</td>
<td align="right">0.5%</td>
<td align="right">3,715</td>
<td align="right">0.4%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,321</td>
<td align="right">4.3%</td>
<td align="right">34,535</td>
<td align="right">3.5%</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">13,623</td>
<td align="right">1.2%</td>
<td align="right">10,487</td>
<td align="right">1.1%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,882</td>
<td align="right">0.8%</td>
<td align="right">6,865</td>
<td align="right">0.7%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,722</td>
<td align="right">0.4%</td>
<td align="right">3,665</td>
<td align="right">0.4%</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">0.9%</td>
<td align="right">8,762</td>
<td align="right">0.9%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,264</td>
<td align="right">2.8%</td>
<td align="right">27,852</td>
<td align="right">2.8%</td>
<td align="right">-10.9%</td>
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
<td align="left">remainder</td>
<td align="right">22,652</td>
<td align="right">2.0%</td>
<td align="right">21,049</td>
<td align="right">2.1%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,607</td>
<td align="right">69.6%</td>
<td align="right">733,958</td>
<td align="right">74.5%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,388</td>
<td align="right">2.9%</td>
<td align="right">30,504</td>
<td align="right">3.1%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,500</td>
<td align="right">0.9%</td>
<td align="right">10,063</td>
<td align="right">1.0%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,606</td>
<td align="right">0.8%</td>
<td align="right">8,339</td>
<td align="right">0.8%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,654</td>
<td align="right">0.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,918</td>
<td align="right">0.2%</td>
<td align="right">1,914</td>
<td align="right">0.2%</td>
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
<td align="right">631,335,562</td>
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
<td align="right">6,132,874,166</td>
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
<td align="right">4,808,203</td>
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
<td align="right">209,251</td>
<td align="right">53.5%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,552</td>
<td align="right">43.0%</td>
<td align="right">181,528</td>
<td align="right">46.5%</td>
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
<td align="right">40,460</td>
<td align="right">19.3%</td>
<td align="right">-27.7%</td>
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
<td align="right">125</td>
<td align="right">0.1%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">110,441</td>
<td align="right">46.0%</td>
<td align="right">109,846</td>
<td align="right">52.5%</td>
<td align="right">-0.5%</td>
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
<td align="right">20,080</td>
<td align="right">0.0%</td>
<td align="right">-30.4%</td>
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
<td align="right">141,341,514</td>
<td align="right">1.0%</td>
<td align="right">-22.0%</td>
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
<td align="right">622,808,325</td>
<td align="right">4.4%</td>
<td align="right">-5.9%</td>
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
<td align="right">13,685,416,685</td>
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
<td align="right">3,190,167</td>
<td align="right">95.1%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">165,358</td>
<td align="right">4.0%</td>
<td align="right">165,280</td>
<td align="right">4.9%</td>
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
<td align="right">155,780</td>
<td align="right">94.3%</td>
<td align="right">-0.1%</td>
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
<td align="right">62,958,816</td>
<td align="right">1.0%</td>
<td align="right">-37.8%</td>
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
<td align="right">987,484</td>
<td align="right">0.0%</td>
<td align="right">-7.8%</td>
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
<td align="right">6,105,571,631</td>
<td align="right">99.0%</td>
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
<td align="right">134,082</td>
<td align="right">64.3%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">76,203</td>
<td align="right">33.7%</td>
<td align="right">74,531</td>
<td align="right">35.7%</td>
<td align="right">-2.2%</td>
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
<td align="right">8,906</td>
<td align="right">6.6%</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.4%</td>
<td align="right">480</td>
<td align="right">0.4%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,600</td>
<td align="right">1.7%</td>
<td align="right">2,220</td>
<td align="right">1.7%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,184</td>
<td align="right">8.1%</td>
<td align="right">10,561</td>
<td align="right">7.9%</td>
<td align="right">-13.3%</td>
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
<td align="left">big int</td>
<td align="right">27,070</td>
<td align="right">18.1%</td>
<td align="right">23,834</td>
<td align="right">17.8%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,693</td>
<td align="right">11.1%</td>
<td align="right">14,733</td>
<td align="right">11.0%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,020</td>
<td align="right">12.7%</td>
<td align="right">17,520</td>
<td align="right">13.1%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,428</td>
<td align="right">1.0%</td>
<td align="right">1,387</td>
<td align="right">1.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">42,519</td>
<td align="right">28.4%</td>
<td align="right">41,301</td>
<td align="right">30.8%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">10,680</td>
<td align="right">8.0%</td>
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
<td align="right">204,859,674</td>
<td align="right">7.6%</td>
<td align="right">-1.6%</td>
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
<td align="right">2,485,207,506</td>
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
<td align="right">109,109</td>
<td align="right">64.3%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,120</td>
<td align="right">35.0%</td>
<td align="right">60,539</td>
<td align="right">35.7%</td>
<td align="right">-1.0%</td>
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
<td align="right">24,855</td>
<td align="right">22.8%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">13,940</td>
<td align="right">12.3%</td>
<td align="right">12,960</td>
<td align="right">11.9%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,721</td>
<td align="right">13.8%</td>
<td align="right">14,914</td>
<td align="right">13.7%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">56,540</td>
<td align="right">49.7%</td>
<td align="right">56,380</td>
<td align="right">51.7%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,588,465</td>
<td align="right">0.3%</td>
<td align="right">134,749</td>
<td align="right">0.0%</td>
<td align="right">-94.8%</td>
</tr>
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
<td align="right">417,953,330</td>
<td align="right">46.6%</td>
<td align="right">-23.6%</td>
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
<td align="right">477,787,610</td>
<td align="right">53.3%</td>
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
<td align="right">96,560</td>
<td align="right">32.9%</td>
<td align="right">50,257</td>
<td align="right">20.5%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">197,004</td>
<td align="right">67.1%</td>
<td align="right">194,779</td>
<td align="right">79.5%</td>
<td align="right">-1.1%</td>
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
<td align="right">9,482</td>
<td align="right">4.9%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,060</td>
<td align="right">2.1%</td>
<td align="right">3,820</td>
<td align="right">2.0%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,840</td>
<td align="right">1.9%</td>
<td align="right">3,640</td>
<td align="right">1.9%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,291</td>
<td align="right">5.7%</td>
<td align="right">10,966</td>
<td align="right">5.6%</td>
<td align="right">-2.9%</td>
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
<td align="left">dict items</td>
<td align="right">37,142</td>
<td align="right">18.9%</td>
<td align="right">36,653</td>
<td align="right">18.8%</td>
<td align="right">-1.3%</td>
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
<td align="left">dict values</td>
<td align="right">4,220</td>
<td align="right">2.1%</td>
<td align="right">4,220</td>
<td align="right">2.2%</td>
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
<td align="left">bytes</td>
<td align="right">618</td>
<td align="right">0.3%</td>
<td align="right">618</td>
<td align="right">0.3%</td>
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
<td align="right">143,100</td>
<td align="right">0.0%</td>
<td align="right">-55.3%</td>
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
<td align="right">295,374,901</td>
<td align="right">1.7%</td>
<td align="right">-29.5%</td>
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
<td align="right">1,249,020,807</td>
<td align="right">7.3%</td>
<td align="right">-17.8%</td>
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
<td align="right">15,881,454,780</td>
<td align="right">92.7%</td>
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
<td align="left">Success</td>
<td align="right">8,517,409</td>
<td align="right">89.8%</td>
<td align="right">6,184,405</td>
<td align="right">88.5%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">972,301</td>
<td align="right">10.2%</td>
<td align="right">801,474</td>
<td align="right">11.5%</td>
<td align="right">-17.6%</td>
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
<td align="right">156,135</td>
<td align="right">16.1%</td>
<td align="right">43,097</td>
<td align="right">5.4%</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,755</td>
<td align="right">1.8%</td>
<td align="right">13,768</td>
<td align="right">1.7%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,303</td>
<td align="right">9.0%</td>
<td align="right">78,012</td>
<td align="right">9.7%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">263,182</td>
<td align="right">27.1%</td>
<td align="right">239,923</td>
<td align="right">29.9%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">102,088</td>
<td align="right">10.5%</td>
<td align="right">95,371</td>
<td align="right">11.9%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,880</td>
<td align="right">2.8%</td>
<td align="right">25,200</td>
<td align="right">3.1%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,582</td>
<td align="right">0.6%</td>
<td align="right">5,240</td>
<td align="right">0.7%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,380</td>
<td align="right">1.5%</td>
<td align="right">13,500</td>
<td align="right">1.7%</td>
<td align="right">-6.1%</td>
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
<td align="right">156,819</td>
<td align="right">19.6%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,840</td>
<td align="right">1.6%</td>
<td align="right">15,143</td>
<td align="right">1.9%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">75,378</td>
<td align="right">7.8%</td>
<td align="right">73,074</td>
<td align="right">9.1%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,340</td>
<td align="right">2.1%</td>
<td align="right">19,947</td>
<td align="right">2.5%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.3%</td>
<td align="right">12,240</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,400</td>
<td align="right">0.6%</td>
<td align="right">5,400</td>
<td align="right">0.7%</td>
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
<td align="right">0.1%</td>
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
<td align="right">4,395,292,637</td>
<td align="right">99.5%</td>
<td align="right">-24.8%</td>
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
<td align="right">438,610</td>
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
<td align="right">20,320,609</td>
<td align="right">0.3%</td>
<td align="right">20,320,753</td>
<td align="right">0.5%</td>
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
<td align="right">462,650</td>
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
<td align="right">83,520,531</td>
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
<td align="right">7,468</td>
<td align="right">0.0%</td>
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
<td align="right">173,284,924</td>
<td align="right">18.1%</td>
<td align="right">173,284,918</td>
<td align="right">18.1%</td>
<td align="right">-0.0%</td>
</tr>
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
<td align="right">786,189,863</td>
<td align="right">81.9%</td>
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
<td align="right">122,215,432</td>
<td align="right">4.2%</td>
<td align="right">-12.4%</td>
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
<td align="right">171,543,881</td>
<td align="right">5.9%</td>
<td align="right">-9.9%</td>
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
<td align="right">2,722,160,926</td>
<td align="right">94.0%</td>
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
<td align="left">Success</td>
<td align="right">2,726,543</td>
<td align="right">96.7%</td>
<td align="right">2,401,728</td>
<td align="right">96.4%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">92,024</td>
<td align="right">3.3%</td>
<td align="right">89,381</td>
<td align="right">3.6%</td>
<td align="right">-2.9%</td>
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
<td align="right">4,640</td>
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
<td align="right">13,329</td>
<td align="right">14.9%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">32,280</td>
<td align="right">35.1%</td>
<td align="right">31,222</td>
<td align="right">34.9%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,780</td>
<td align="right">5.2%</td>
<td align="right">4,760</td>
<td align="right">5.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,724</td>
<td align="right">10.6%</td>
<td align="right">9,730</td>
<td align="right">10.9%</td>
<td align="right">0.1%</td>
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
<td align="right">227,796,374</td>
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
<td align="right">875,027,339</td>
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
<td align="right">97,728</td>
<td align="right">88.3%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,904</td>
<td align="right">11.4%</td>
<td align="right">12,906</td>
<td align="right">11.7%</td>
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
<td align="right">38,080</td>
<td align="right">39.0%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,524</td>
<td align="right">7.5%</td>
<td align="right">7,388</td>
<td align="right">7.6%</td>
<td align="right">-1.8%</td>
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
<td align="right">181,169,117</td>
<td align="right">3.0%</td>
<td align="right">-27.0%</td>
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
<td align="right">47,857,216</td>
<td align="right">0.8%</td>
<td align="right">-13.6%</td>
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
<td align="right">5,922,129,471</td>
<td align="right">97.0%</td>
<td align="right">-2.9%</td>
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
<td align="right">1,096,427</td>
<td align="right">76.4%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">356,102</td>
<td align="right">22.3%</td>
<td align="right">338,881</td>
<td align="right">23.6%</td>
<td align="right">-4.8%</td>
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
<td align="right">6,545</td>
<td align="right">1.9%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.4%</td>
<td align="right">1,157</td>
<td align="right">0.3%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,164</td>
<td align="right">22.8%</td>
<td align="right">73,220</td>
<td align="right">21.6%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,150</td>
<td align="right">1.4%</td>
<td align="right">4,937</td>
<td align="right">1.5%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">55,263</td>
<td align="right">15.5%</td>
<td align="right">53,958</td>
<td align="right">15.9%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12,779</td>
<td align="right">3.6%</td>
<td align="right">12,590</td>
<td align="right">3.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,020</td>
<td align="right">4.2%</td>
<td align="right">14,820</td>
<td align="right">4.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">35,076</td>
<td align="right">9.8%</td>
<td align="right">34,808</td>
<td align="right">10.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">135,491</td>
<td align="right">38.0%</td>
<td align="right">135,386</td>
<td align="right">40.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">83,939</td>
<td align="right">0.0%</td>
<td align="right">-56.8%</td>
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
<td align="right">1,230,532,398</td>
<td align="right">100.0%</td>
<td align="right">-21.0%</td>
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
<td align="right">1,754</td>
<td align="right">5.5%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,044</td>
<td align="right">94.2%</td>
<td align="right">30,072</td>
<td align="right">94.5%</td>
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
<td align="right">380</td>
<td align="right">20.5%</td>
<td align="right">280</td>
<td align="right">16.0%</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,218</td>
<td align="right">65.6%</td>
<td align="right">1,214</td>
<td align="right">69.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.0%</td>
<td align="right">260</td>
<td align="right">14.8%</td>
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
<td align="right">49,136,389,705</td>
<td align="right">53.4%</td>
<td align="right">-26.7%</td>
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
<td align="right">32,966,956,162</td>
<td align="right">35.8%</td>
<td align="right">-22.8%</td>
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
<td align="right">713,656,390</td>
<td align="right">0.8%</td>
<td align="right">-21.9%</td>
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
<td align="right">9,231,852,960</td>
<td align="right">10.0%</td>
<td align="right">-21.2%</td>
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
<td align="right">299,311,508</td>
<td align="right">6.9%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">248,282,880</td>
<td align="right">4.9%</td>
<td align="right">181,169,117</td>
<td align="right">4.2%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,519,370,478</td>
<td align="right">30.3%</td>
<td align="right">1,249,020,807</td>
<td align="right">28.9%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">743,980,833</td>
<td align="right">14.8%</td>
<td align="right">631,335,562</td>
<td align="right">14.6%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">190,470,433</td>
<td align="right">3.8%</td>
<td align="right">171,543,881</td>
<td align="right">4.0%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">662,107,381</td>
<td align="right">13.2%</td>
<td align="right">622,808,325</td>
<td align="right">14.4%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,058,579</td>
<td align="right">4.6%</td>
<td align="right">227,796,374</td>
<td align="right">5.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">208,172,737</td>
<td align="right">4.1%</td>
<td align="right">204,859,674</td>
<td align="right">4.7%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">483,797,468</td>
<td align="right">9.6%</td>
<td align="right">477,787,610</td>
<td align="right">11.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,924</td>
<td align="right">3.5%</td>
<td align="right">173,284,918</td>
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
<td align="right">113,305,762</td>
<td align="right">14.3%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">98,381,121</td>
<td align="right">9.9%</td>
<td align="right">64,923,258</td>
<td align="right">8.2%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,547,164</td>
<td align="right">3.6%</td>
<td align="right">24,714,440</td>
<td align="right">3.1%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">58,788,733</td>
<td align="right">5.9%</td>
<td align="right">41,306,598</td>
<td align="right">5.2%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">125,645,656</td>
<td align="right">12.7%</td>
<td align="right">98,157,704</td>
<td align="right">12.4%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">114,222,140</td>
<td align="right">11.5%</td>
<td align="right">98,267,101</td>
<td align="right">12.4%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,897,432</td>
<td align="right">7.9%</td>
<td align="right">77,898,141</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,897,432</td>
<td align="right">7.9%</td>
<td align="right">77,898,141</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,485</td>
<td align="right">2.8%</td>
<td align="right">27,496,582</td>
<td align="right">3.5%</td>
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
<td align="right">23,925,201</td>
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
<td align="right">358,815,088</td>
<td align="right">4.1%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,784,047,052</td>
<td align="right">20.5%</td>
<td align="right">1,797,028,187</td>
<td align="right">20.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,788,493,492</td>
<td align="right">20.5%</td>
<td align="right">1,801,474,627</td>
<td align="right">20.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">550,012,131</td>
<td align="right">6.3%</td>
<td align="right">552,988,786</td>
<td align="right">6.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,064,096,131</td>
<td align="right">69.6%</td>
<td align="right">6,034,403,611</td>
<td align="right">69.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,649,106,694</td>
<td align="right">30.4%</td>
<td align="right">2,662,062,150</td>
<td align="right">30.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,649,106,694</td>
<td align="right">30.4%</td>
<td align="right">2,662,062,150</td>
<td align="right">30.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,954,179,303</td>
<td align="right">79.8%</td>
<td align="right">6,937,935,961</td>
<td align="right">79.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,613,202</td>
<td align="right">9.9%</td>
<td align="right">860,587,523</td>
<td align="right">9.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,397,352</td>
<td align="right">1.0%</td>
<td align="right">84,398,926</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,015,817</td>
<td align="right">0.4%</td>
<td align="right">31,015,329</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,249</td>
<td align="right">2.0%</td>
<td align="right">175,480,443</td>
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
<td align="right">42,176,087,538</td>
<td align="right">28.7%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">90,290,811,638</td>
<td align="right">62.8%</td>
<td align="right">104,990,657,547</td>
<td align="right">71.3%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">94,383,329,472</td>
<td align="right">56.7%</td>
<td align="right">106,385,280,056</td>
<td align="right">62.5%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">72,192,141,394</td>
<td align="right">43.3%</td>
<td align="right">63,923,095,158</td>
<td align="right">37.5%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">16,845,198</td>
<td align="right"></td>
<td align="right">15,454,850</td>
<td align="right"></td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">54,231,476</td>
<td align="right"></td>
<td align="right">57,254,818</td>
<td align="right"></td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,715,281,163</td>
<td align="right">55.2%</td>
<td align="right">13,026,036,852</td>
<td align="right">55.8%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">67,760,584</td>
<td align="right"></td>
<td align="right">69,404,685</td>
<td align="right"></td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,824,203,345</td>
<td align="right">55.7%</td>
<td align="right">13,134,867,962</td>
<td align="right">56.2%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,237,475,217</td>
<td align="right"></td>
<td align="right">3,315,005,475</td>
<td align="right"></td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,529,066,281</td>
<td align="right"></td>
<td align="right">13,838,874,128</td>
<td align="right"></td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,126,366</td>
<td align="right"></td>
<td align="right">161,785,246</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,206,246,789</td>
<td align="right">44.3%</td>
<td align="right">10,216,409,426</td>
<td align="right">43.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,208,147,271</td>
<td align="right"></td>
<td align="right">10,218,287,974</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">94,073,978</td>
<td align="right">0.4%</td>
<td align="right">93,986,562</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,563,373,921</td>
<td align="right"></td>
<td align="right">4,566,997,164</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">14,848,204</td>
<td align="right">0.1%</td>
<td align="right">14,844,548</td>
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
<td align="right">114,823,520</td>
<td align="right">19,151,323,918</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,334,252</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,358,944</td>
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
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">185.7%</td>
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
<td align="right">2,978</td>
<td align="right">0.3%</td>
<td align="right">122.7%</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">125,781</td>
<td align="right">10.3%</td>
<td align="right">222,904</td>
<td align="right">21.4%</td>
<td align="right">77.2%</td>
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
<td align="right">11,285,067,622</td>
<td align="right"></td>
<td align="right">47.4%</td>
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
<td align="right">17,469</td>
<td align="right">1.7%</td>
<td align="right">39.0%</td>
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
<td align="right">2,260</td>
<td align="right">0.2%</td>
<td align="right">31.4%</td>
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
<td align="right">34,729</td>
<td align="right">3.3%</td>
<td align="right">-31.2%</td>
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
<td align="right">817,945</td>
<td align="right">78.6%</td>
<td align="right">-25.5%</td>
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
<td align="right">306,897,878,071</td>
<td align="right">2,719.5%</td>
<td align="right">22.8%</td>
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
<td align="right">1,040,849</td>
<td align="right"></td>
<td align="right">-15.0%</td>
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
<td align="right">7,236</td>
<td align="right">3.2%</td>
<td align="right">14.0%</td>
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
<td align="right">222,904</td>
<td align="right"></td>
<td align="right">77.2%</td>
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
<td align="right">194,731</td>
<td align="right">87.4%</td>
<td align="right">75.5%</td>
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
<td align="right">2,444</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
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
<td align="right">740</td>
<td align="right">0.3%</td>
<td align="right">740 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">5,298</td>
<td align="right">4.2%</td>
<td align="right">28,043</td>
<td align="right">12.6%</td>
<td align="right">429.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,573</td>
<td align="right">17.2%</td>
<td align="right">37,331</td>
<td align="right">16.7%</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,251</td>
<td align="right">28.0%</td>
<td align="right">54,671</td>
<td align="right">24.5%</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">30,857</td>
<td align="right">24.5%</td>
<td align="right">52,187</td>
<td align="right">23.4%</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21,219</td>
<td align="right">16.9%</td>
<td align="right">27,359</td>
<td align="right">12.3%</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,723</td>
<td align="right">7.7%</td>
<td align="right">18,975</td>
<td align="right">8.5%</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,700</td>
<td align="right">1.4%</td>
<td align="right">3,158</td>
<td align="right">1.4%</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">440</td>
<td align="right">0.2%</td>
<td align="right">175.0%</td>
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
<td align="right">740</td>
<td align="right">0.3%</td>
<td align="right">740 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">4,138</td>
<td align="right">3.3%</td>
<td align="right">8,492</td>
<td align="right">3.8%</td>
<td align="right">105.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">14,802</td>
<td align="right">11.8%</td>
<td align="right">39,574</td>
<td align="right">17.8%</td>
<td align="right">167.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">25,257</td>
<td align="right">20.1%</td>
<td align="right">42,703</td>
<td align="right">19.2%</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">36,427</td>
<td align="right">29.0%</td>
<td align="right">55,066</td>
<td align="right">24.7%</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">18,509</td>
<td align="right">14.7%</td>
<td align="right">28,367</td>
<td align="right">12.7%</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,760</td>
<td align="right">7.0%</td>
<td align="right">13,911</td>
<td align="right">6.2%</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,660</td>
<td align="right">2.1%</td>
<td align="right">4,998</td>
<td align="right">2.2%</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">380</td>
<td align="right">0.3%</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">131.6%</td>
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
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">329,091,768</td>
<td align="right">21,216.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">6,350,200</td>
<td align="right">21,123.9%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">647,805</td>
<td align="right">8,401.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,917,600</td>
<td align="right">134,238,678</td>
<td align="right">3,326.6%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">5,782,740</td>
<td align="right">139,050,558</td>
<td align="right">2,304.6%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,025,020</td>
<td align="right">69,369,766</td>
<td align="right">2,193.2%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,720</td>
<td align="right">11,872,148</td>
<td align="right">1,344.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,922,920</td>
<td align="right">56,760,340</td>
<td align="right">1,053.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">262,399,640</td>
<td align="right">2,863,228,671</td>
<td align="right">991.2%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,671,620</td>
<td align="right">38,639,367</td>
<td align="right">952.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">10,050,940</td>
<td align="right">101,175,983</td>
<td align="right">906.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">11,627,720</td>
<td align="right">102,869,549</td>
<td align="right">784.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">464,415</td>
<td align="right">3,074,876</td>
<td align="right">562.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">13,204,198</td>
<td align="right">386.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,227,105</td>
<td align="right">37,466,093</td>
<td align="right">266.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">67,792,420</td>
<td align="right">231,813,760</td>
<td align="right">241.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">907,921,574</td>
<td align="right">2,967,403,586</td>
<td align="right">226.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,092,198</td>
<td align="right">98,459,857</td>
<td align="right">180.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">887,540</td>
<td align="right">175.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">126,546,234</td>
<td align="right">333,841,498</td>
<td align="right">163.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">47,971,827</td>
<td align="right">119,743,515</td>
<td align="right">149.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,717,560</td>
<td align="right">63,652,980</td>
<td align="right">147.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,381,935</td>
<td align="right">229,887,714</td>
<td align="right">138.5%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,533,432</td>
<td align="right">5,539,230</td>
<td align="right">118.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">25,197,744</td>
<td align="right">45,402,522</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,421,185,031</td>
<td align="right">2,557,609,897</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">81,702,400</td>
<td align="right">144,713,177</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">81,592,680</td>
<td align="right">143,718,484</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">101,766,747</td>
<td align="right">178,328,235</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">801,164,005</td>
<td align="right">1,369,624,973</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">75,936,345</td>
<td align="right">128,859,948</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">338,027,898</td>
<td align="right">568,838,348</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,659,960</td>
<td align="right">9,454,503</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">121,960,461</td>
<td align="right">201,317,955</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">113,122,590</td>
<td align="right">184,894,039</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">317,179,580</td>
<td align="right">497,981,603</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">264,980,681</td>
<td align="right">414,340,910</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,177,320</td>
<td align="right">12,785,177</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">407,352,702</td>
<td align="right">635,932,936</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">266,207,941</td>
<td align="right">415,573,297</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,713,332</td>
<td align="right">139,896,507</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">173,883,327</td>
<td align="right">263,957,914</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,490,837,241</td>
<td align="right">2,214,228,467</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,690,398,961</td>
<td align="right">2,505,120,639</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,658,491,963</td>
<td align="right">11,285,067,622</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,652,185</td>
<td align="right">129,382,705</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,025,666,874</td>
<td align="right">2,916,752,113</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,086,114,050</td>
<td align="right">3,003,526,021</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">947,129,059</td>
<td align="right">1,359,160,584</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">102,572,236</td>
<td align="right">146,444,174</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,964,176,769</td>
<td align="right">2,802,231,246</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,429,774</td>
<td align="right">111,532,972</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,790,342,787</td>
<td align="right">2,538,331,536</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,682,778</td>
<td align="right">40,447,760</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,414,870</td>
<td align="right">134,526,051</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,658,730</td>
<td align="right">134,774,611</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">163,092,540</td>
<td align="right">229,133,850</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,578,500,794</td>
<td align="right">2,207,164,091</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">30,588,139</td>
<td align="right">42,707,491</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,862,100</td>
<td align="right">9,458,863</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">212,710,464</td>
<td align="right">292,952,804</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">394,141,934</td>
<td align="right">536,679,585</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">3,628,062</td>
<td align="right">4,933,666</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,387,369</td>
<td align="right">126,593,845</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,165,627,940</td>
<td align="right">2,901,460,409</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,994,596,737</td>
<td align="right">24,089,697,035</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">39,840</td>
<td align="right">26,426</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">834,115,332</td>
<td align="right">1,103,207,452</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">150,145,075</td>
<td align="right">198,357,368</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">194,356,520</td>
<td align="right">256,598,588</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,835,900</td>
<td align="right">81,523,456</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">458,247,341</td>
<td align="right">603,306,001</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">563,253,712</td>
<td align="right">740,809,942</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,190,140,867</td>
<td align="right">1,565,170,456</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,323,249,487</td>
<td align="right">1,722,794,193</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,990,580</td>
<td align="right">188,633,120</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,302,521,727</td>
<td align="right">1,692,508,915</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">164,119,758</td>
<td align="right">212,890,238</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,412,648,438</td>
<td align="right">3,119,076,829</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,620,206,295</td>
<td align="right">4,638,620,289</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,386,341,118</td>
<td align="right">3,054,530,649</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,802,948,951</td>
<td align="right">8,665,584,398</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,326,679,010</td>
<td align="right">1,689,061,419</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,746,337,424</td>
<td align="right">3,485,713,419</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">28,421,210</td>
<td align="right">35,905,394</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,426,781,855</td>
<td align="right">4,320,961,868</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,166,678,013</td>
<td align="right">3,968,766,394</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">777,658,264</td>
<td align="right">973,532,341</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">658,505,649</td>
<td align="right">816,141,275</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">395,595,992</td>
<td align="right">489,963,527</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,276,455,267</td>
<td align="right">9,011,445,724</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,340,453,587</td>
<td align="right">1,640,615,660</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">395,766,495</td>
<td align="right">484,327,886</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,119,605,245</td>
<td align="right">7,466,763,450</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">884,396,088</td>
<td align="right">1,074,070,458</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,046,701,297</td>
<td align="right">1,265,150,181</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,152,854,888</td>
<td align="right">1,393,232,286</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">274,498,649</td>
<td align="right">330,611,791</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,742,287,559</td>
<td align="right">4,496,768,818</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">972,069,275</td>
<td align="right">1,165,731,626</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,418,374,871</td>
<td align="right">5,286,890,099</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">310,680</td>
<td align="right">368,259</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">198,417,421</td>
<td align="right">234,978,522</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">15,663,608,008</td>
<td align="right">18,397,853,704</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,131,167,091</td>
<td align="right">1,325,372,307</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">216,982,949</td>
<td align="right">254,150,576</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">219,513,205</td>
<td align="right">256,681,388</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,015,825,824</td>
<td align="right">2,356,376,181</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">60,988,920</td>
<td align="right">71,230,580</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,696,159,857</td>
<td align="right">11,257,134,273</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,685,040</td>
<td align="right">237,162,744</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">697,369,158</td>
<td align="right">808,005,225</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,037,852,163</td>
<td align="right">3,518,360,076</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">297,705,572</td>
<td align="right">343,790,500</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">137,782,897</td>
<td align="right">158,895,567</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,255,054,792</td>
<td align="right">7,188,027,589</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,059,561,191</td>
<td align="right">1,216,216,971</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,383,961,517</td>
<td align="right">1,587,876,986</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">266,229,464</td>
<td align="right">304,803,566</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">321,279,671</td>
<td align="right">367,294,889</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">7,006,297,041</td>
<td align="right">8,006,360,856</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">860,552,563</td>
<td align="right">980,488,348</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,713,871</td>
<td align="right">103,118,116</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,683,011,511</td>
<td align="right">1,911,008,627</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">435,925,196</td>
<td align="right">494,672,892</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">67,154,995</td>
<td align="right">76,126,953</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">924,450,130</td>
<td align="right">1,045,916,837</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,185,920,039</td>
<td align="right">14,917,443,802</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,335</td>
<td align="right">151,796,810</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,335</td>
<td align="right">151,796,810</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">893,721,072</td>
<td align="right">1,009,750,312</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">218,973,940</td>
<td align="right">246,097,723</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">64,522,284</td>
<td align="right">72,481,319</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">104,767,940</td>
<td align="right">117,677,059</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">246,294,981</td>
<td align="right">275,620,280</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">904,464,414</td>
<td align="right">1,009,036,150</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,809,679</td>
<td align="right">35,380,387</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,584,100</td>
<td align="right">95,969,847</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">514,767,036</td>
<td align="right">570,444,610</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,688,399,516</td>
<td align="right">5,191,316,510</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">244,676,060</td>
<td align="right">270,376,369</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,829,219,785</td>
<td align="right">2,016,655,640</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">48,459,599</td>
<td align="right">53,340,354</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,849,005,499</td>
<td align="right">2,025,845,331</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,819,434,084</td>
<td align="right">5,278,546,931</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,966,880</td>
<td align="right">3,249,179</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,252,649,306</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">59,644,340</td>
<td align="right">65,173,740</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,080,100</td>
<td align="right">582,331,121</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">58,584,720</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">239,754,893</td>
<td align="right">219,342,414</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,638,074</td>
<td align="right">417,298,734</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">992,082,796</td>
<td align="right">1,074,960,409</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">510,187,700</td>
<td align="right">552,559,168</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,330,974,065</td>
<td align="right">2,522,192,294</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,027,076,433</td>
<td align="right">1,108,352,448</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,561,839,761</td>
<td align="right">7,065,736,156</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,329,334</td>
<td align="right">2,504,792</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,611,485,654</td>
<td align="right">1,724,041,978</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">553,867,554</td>
<td align="right">590,923,093</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,187,201</td>
<td align="right">104,588,539</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,229,861</td>
<td align="right">103,232,605</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,171</td>
<td align="right">683,622,961</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">387,261,850</td>
<td align="right">409,938,865</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">235,347,921</td>
<td align="right">248,854,553</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,883,906,419</td>
<td align="right">1,991,398,669</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,253,951,572</td>
<td align="right">1,323,302,580</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">619,482,881</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,490,371</td>
<td align="right">168,536,384</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,280,057,960</td>
<td align="right">1,341,880,199</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,591,672</td>
<td align="right">12,110,606</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,591,672</td>
<td align="right">12,105,286</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">664,882,748</td>
<td align="right">692,416,510</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,698,177</td>
<td align="right">809,315,529</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,160,857</td>
<td align="right">808,712,829</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,270,476,662</td>
<td align="right">4,429,852,895</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,940</td>
<td align="right">6,824,495</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,366,919,175</td>
<td align="right">3,487,034,622</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">972,689,965</td>
<td align="right">1,007,331,833</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,682,017</td>
<td align="right">11,050,121</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,816,269,139</td>
<td align="right">1,876,069,757</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,623,729,195</td>
<td align="right">3,729,989,058</td>
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
<td align="right">2,910,621,642</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,319,550,051</td>
<td align="right">2,370,372,678</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">140,317,419</td>
<td align="right">143,261,059</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,259,037,890</td>
<td align="right">2,303,466,844</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,648,680</td>
<td align="right">4,729,880</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,997,861,167</td>
<td align="right">2,031,634,458</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">651,198,990</td>
<td align="right">659,402,882</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,749,503</td>
<td align="right">232,488,122</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,550,540</td>
<td align="right">189,432,974</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,601,060</td>
<td align="right">736,836,551</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">643,762,527</td>
<td align="right">648,125,611</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,403,284</td>
<td align="right">32,555,864</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,508,973,019</td>
<td align="right">2,513,494,814</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">46,421,480</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,098,164,256</td>
<td align="right">1,096,912,363</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,705,220</td>
<td align="right">80,714,597</td>
<td align="right">0.0%</td>
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
<td align="right">584,477,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">27,485,904</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">31,002</td>
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
<td align="left">SEND</td>
<td align="right">33,340</td>
<td align="right">159,028</td>
<td align="right">377.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">320</td>
<td align="right">1,160</td>
<td align="right">262.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,457</td>
<td align="right">5,807</td>
<td align="right">136.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">700</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,200</td>
<td align="right">2,279</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">640</td>
<td align="right">1,060</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">30,640</td>
<td align="right">47,615</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,221</td>
<td align="right">9,518</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,540</td>
<td align="right">5,260</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">620</td>
<td align="right">860</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,618</td>
<td align="right">8,613</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">486,640</td>
<td align="right">568,855</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,641</td>
<td align="right">49,053</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,680</td>
<td align="right">1,660</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right"></td>
<td align="right">396</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right"></td>
<td align="right">20</td>
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
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,105</td>
<td align="right">1,105</td>
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
<td align="right">1,105</td>
<td align="right">1,105</td>
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
