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
<td align="left">CLEANUP_THROW</td>
<td align="right">98,514</td>
<td align="right">496</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,496</td>
<td align="right">12,071</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,497</td>
<td align="right">21,571</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,820,431</td>
<td align="right">575,538</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,437,957</td>
<td align="right">3,076,784</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">36</td>
<td align="right">16</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,495,567</td>
<td align="right">3,873,763</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">752,266</td>
<td align="right">395,896</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,450,846</td>
<td align="right">937,092</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,509</td>
<td align="right">3,797</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,194</td>
<td align="right">41,466</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,947,102</td>
<td align="right">20,887,747</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,889</td>
<td align="right">2,930</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">83,590,635</td>
<td align="right">63,274,253</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,443</td>
<td align="right">27,151,260</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">68,476,417</td>
<td align="right">52,303,438</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,644</td>
<td align="right">2,021</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">153</td>
<td align="right">117</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">23,452,781</td>
<td align="right">18,030,147</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,711,143</td>
<td align="right">6,026,785</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,299</td>
<td align="right">4,240</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">135,666</td>
<td align="right">110,079</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,718,955</td>
<td align="right">3,972,667</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,905,648</td>
<td align="right">60,108,836</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">34,174</td>
<td align="right">28,999</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,796,368</td>
<td align="right">3,265,232</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">407,116</td>
<td align="right">361,907</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">61,829,191</td>
<td align="right">54,968,190</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,643,428</td>
<td align="right">1,482,762</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,194,227</td>
<td align="right">60,690,676</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,822,526</td>
<td align="right">141,353,634</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">135,076,779</td>
<td align="right">123,588,656</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,613</td>
<td align="right">3,326</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,784,530</td>
<td align="right">1,643,320</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">337,256,950</td>
<td align="right">310,916,961</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">786,180,659</td>
<td align="right">724,978,742</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">67,544,265</td>
<td align="right">62,383,416</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">493,650,650</td>
<td align="right">456,190,038</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">773,928,169</td>
<td align="right">715,392,640</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,683,684</td>
<td align="right">91,280,295</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">114,973,730</td>
<td align="right">106,371,950</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,150,804,574</td>
<td align="right">1,066,663,599</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,560</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,891,830</td>
<td align="right">107,911,450</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">95,077,043</td>
<td align="right">89,327,706</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">65,890,722</td>
<td align="right">62,273,769</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">325,932,436</td>
<td align="right">308,393,981</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,994,671</td>
<td align="right">19,872,262</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,305</td>
<td align="right">122,113,015</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">546,809,113</td>
<td align="right">519,357,091</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,792,112</td>
<td align="right">166,198,974</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,325,920</td>
<td align="right">20,277,708</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,325,939</td>
<td align="right">20,277,729</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">354,092,973</td>
<td align="right">336,698,822</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">827,732,677</td>
<td align="right">787,388,654</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">348,540,707</td>
<td align="right">332,403,086</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">14,111,536</td>
<td align="right">13,458,728</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,823,364</td>
<td align="right">11,276,798</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">178,511,012</td>
<td align="right">170,493,868</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">415,705,449</td>
<td align="right">397,410,580</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">825,304,546</td>
<td align="right">792,391,854</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">73,272,372</td>
<td align="right">70,368,791</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">63,364,211</td>
<td align="right">60,907,893</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">93,404,473</td>
<td align="right">89,835,505</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">168,628,628</td>
<td align="right">162,326,992</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,770,519</td>
<td align="right">7,490,655</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,198,743,692</td>
<td align="right">2,123,583,377</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">556,440,825</td>
<td align="right">538,161,552</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">314,229,754</td>
<td align="right">304,028,075</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">100,780,237</td>
<td align="right">97,691,225</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,524</td>
<td align="right">5,981,971</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">121,283</td>
<td align="right">117,627</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,059,048,808</td>
<td align="right">1,027,174,661</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">436,849,034</td>
<td align="right">423,884,691</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">257,121,413</td>
<td align="right">249,541,458</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,380,144,743</td>
<td align="right">1,341,849,849</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">511,560,198</td>
<td align="right">497,391,184</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,521</td>
<td align="right">293,954,463</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,444,183</td>
<td align="right">55,877,534</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">533,200,664</td>
<td align="right">518,837,957</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,099,835,171</td>
<td align="right">2,044,363,977</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">402,693,813</td>
<td align="right">392,560,348</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,304,124,677</td>
<td align="right">3,221,219,693</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,882,635,147</td>
<td align="right">3,786,375,827</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">305,798,359</td>
<td align="right">298,262,846</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,521,521,122</td>
<td align="right">1,485,015,842</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">201,791,694</td>
<td align="right">197,005,929</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">221,724,097</td>
<td align="right">216,598,540</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,250,913,649</td>
<td align="right">6,107,102,925</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,363,290,037</td>
<td align="right">5,241,133,404</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">57,852,923</td>
<td align="right">56,670,007</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,113,602,749</td>
<td align="right">1,090,956,103</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,497,124,658</td>
<td align="right">2,446,426,147</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,206,861,465</td>
<td align="right">1,182,436,873</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,543,132,643</td>
<td align="right">1,511,927,616</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">355,810,204</td>
<td align="right">348,681,239</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">77,220,693</td>
<td align="right">75,695,459</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">72,404,047</td>
<td align="right">71,004,841</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,188,661,694</td>
<td align="right">3,131,171,422</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,328,232,409</td>
<td align="right">1,304,949,340</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,808,943,397</td>
<td align="right">5,708,130,950</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">637,246,618</td>
<td align="right">626,386,582</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">292,918,352</td>
<td align="right">287,957,364</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,750,735,469</td>
<td align="right">5,656,415,308</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">810,437,569</td>
<td align="right">797,205,215</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">72,577,918</td>
<td align="right">71,411,231</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">13,935</td>
<td align="right">13,720</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">121,925,262</td>
<td align="right">120,134,270</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">61,976,258</td>
<td align="right">61,069,764</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">34,206,643,460</td>
<td align="right">33,710,825,194</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,218,815,402</td>
<td align="right">7,114,315,412</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,712,690,418</td>
<td align="right">10,561,262,869</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,114,450,815</td>
<td align="right">1,098,977,741</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">671,599,577</td>
<td align="right">662,433,938</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,528,911,330</td>
<td align="right">2,494,467,793</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">566,125,100</td>
<td align="right">558,452,261</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">263,696,816</td>
<td align="right">260,231,620</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,079,202,863</td>
<td align="right">9,952,778,683</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">194,983,591</td>
<td align="right">192,554,086</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">369,678,360</td>
<td align="right">365,188,522</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,422,041,872</td>
<td align="right">13,267,895,140</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">290,855,177</td>
<td align="right">287,644,016</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,939,616,658</td>
<td align="right">2,907,729,295</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">950,455,936</td>
<td align="right">940,340,824</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,460,854,563</td>
<td align="right">1,446,026,803</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">265,950,008</td>
<td align="right">263,372,166</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">946,762,777</td>
<td align="right">937,696,088</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,615,847</td>
<td align="right">414,728,120</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,621,277</td>
<td align="right">586,236,179</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">375,868,268</td>
<td align="right">372,530,072</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,531,860,661</td>
<td align="right">2,510,005,636</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,610</td>
<td align="right">41,603,679</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,806,505,652</td>
<td align="right">2,782,492,274</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,737,222,125</td>
<td align="right">2,714,911,779</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,134,600,856</td>
<td align="right">2,117,604,242</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,584,374,866</td>
<td align="right">1,572,348,083</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,262,457,914</td>
<td align="right">2,246,031,520</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">356,978,612</td>
<td align="right">354,470,026</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,189,000,538</td>
<td align="right">3,166,770,596</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">89,969,732</td>
<td align="right">89,348,117</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,838,164,684</td>
<td align="right">4,805,034,727</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">490,745,192</td>
<td align="right">487,449,980</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,719,218,617</td>
<td align="right">2,701,488,086</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">630,033,186</td>
<td align="right">625,980,365</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">238,190,255</td>
<td align="right">236,772,007</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">240,247,538</td>
<td align="right">238,825,714</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,078,702,520</td>
<td align="right">1,072,528,501</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,853,435</td>
<td align="right">7,808,756</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,275,285,611</td>
<td align="right">1,268,499,083</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,404,085,188</td>
<td align="right">1,396,809,289</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,288,653,670</td>
<td align="right">7,254,711,617</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">861,643,244</td>
<td align="right">857,750,937</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">190,501,404</td>
<td align="right">189,827,944</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,715</td>
<td align="right">127,135,117</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,852,348</td>
<td align="right">154,381,791</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">701,026,214</td>
<td align="right">698,960,130</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,022,098</td>
<td align="right">270,226,142</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">78,104,349</td>
<td align="right">77,897,074</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">939,204,403</td>
<td align="right">936,739,135</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,761,870</td>
<td align="right">14,724,151</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">404,600,372</td>
<td align="right">403,605,753</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,501,394,445</td>
<td align="right">1,497,751,803</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,957,873</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,657,376,284</td>
<td align="right">1,653,885,769</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,484,115,136</td>
<td align="right">3,476,832,432</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,370,319</td>
<td align="right">62,263,550</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,162,372</td>
<td align="right">114,980,805</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,755,351,468</td>
<td align="right">1,753,092,411</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,719,465</td>
<td align="right">545,099,608</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,743,044</td>
<td align="right">9,734,995</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,190</td>
<td align="right">188,393,416</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,416,961</td>
<td align="right">131,331,240</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,829,859</td>
<td align="right">340,647,832</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,271,696</td>
<td align="right">156,217,684</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,251,965,649</td>
<td align="right">1,251,652,050</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,635,145</td>
<td align="right">504,573,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,387,203</td>
<td align="right">158,373,127</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">73,291,751</td>
<td align="right">73,290,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">6,152,485</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,724,898</td>
<td align="right">112,724,681</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,436,107</td>
<td align="right">1,053,436,105</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">100,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
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
<td align="left">UNPACK_EX</td>
<td align="right">117,444</td>
<td align="right">117,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,981</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
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
<td align="right">2,805,560,097</td>
<td align="right">15.0%</td>
<td align="right">2,781,575,869</td>
<td align="right">14.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">59,044,517</td>
<td align="right">0.3%</td>
<td align="right">58,749,579</td>
<td align="right">0.3%</td>
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
<td align="right">15,836,262,293</td>
<td align="right">84.7%</td>
<td align="right">15,773,522,938</td>
<td align="right">84.7%</td>
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
<td align="left">Failure</td>
<td align="right">925,359</td>
<td align="right">45.0%</td>
<td align="right">899,915</td>
<td align="right">44.5%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,130,838</td>
<td align="right">55.0%</td>
<td align="right">1,121,558</td>
<td align="right">55.5%</td>
<td align="right">-0.8%</td>
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
<td align="left">subtract different types</td>
<td align="right">627</td>
<td align="right">0.1%</td>
<td align="right">287</td>
<td align="right">0.0%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,993</td>
<td align="right">0.9%</td>
<td align="right">4,130</td>
<td align="right">0.5%</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,035</td>
<td align="right">0.2%</td>
<td align="right">1,233</td>
<td align="right">0.1%</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,344</td>
<td align="right">0.3%</td>
<td align="right">1,623</td>
<td align="right">0.2%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">399</td>
<td align="right">0.0%</td>
<td align="right">282</td>
<td align="right">0.0%</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,154</td>
<td align="right">0.3%</td>
<td align="right">2,503</td>
<td align="right">0.3%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">1,971</td>
<td align="right">0.2%</td>
<td align="right">1,572</td>
<td align="right">0.2%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.3%</td>
<td align="right">2,137</td>
<td align="right">0.2%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">7,225</td>
<td align="right">0.8%</td>
<td align="right">5,989</td>
<td align="right">0.7%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,247</td>
<td align="right">0.1%</td>
<td align="right">1,052</td>
<td align="right">0.1%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,514</td>
<td align="right">0.9%</td>
<td align="right">7,654</td>
<td align="right">0.9%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.1%</td>
<td align="right">1,254</td>
<td align="right">0.1%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">46,972</td>
<td align="right">5.1%</td>
<td align="right">43,078</td>
<td align="right">4.8%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">325</td>
<td align="right">0.0%</td>
<td align="right">303</td>
<td align="right">0.0%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,631</td>
<td align="right">4.0%</td>
<td align="right">34,274</td>
<td align="right">3.8%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">0.9%</td>
<td align="right">7,710</td>
<td align="right">0.9%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,209</td>
<td align="right">8.0%</td>
<td align="right">70,308</td>
<td align="right">7.8%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">147</td>
<td align="right">0.0%</td>
<td align="right">142</td>
<td align="right">0.0%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,512</td>
<td align="right">2.5%</td>
<td align="right">22,921</td>
<td align="right">2.5%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">79,324</td>
<td align="right">8.6%</td>
<td align="right">77,495</td>
<td align="right">8.6%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,853</td>
<td align="right">4.7%</td>
<td align="right">43,087</td>
<td align="right">4.8%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">43,423</td>
<td align="right">4.7%</td>
<td align="right">42,814</td>
<td align="right">4.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">115,299</td>
<td align="right">12.5%</td>
<td align="right">114,472</td>
<td align="right">12.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,967</td>
<td align="right">3.7%</td>
<td align="right">33,745</td>
<td align="right">3.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">2.1%</td>
<td align="right">19,433</td>
<td align="right">2.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">9.2%</td>
<td align="right">85,540</td>
<td align="right">9.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">121,439</td>
<td align="right">13.1%</td>
<td align="right">121,438</td>
<td align="right">13.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">114,964</td>
<td align="right">12.4%</td>
<td align="right">114,964</td>
<td align="right">12.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">22,288</td>
<td align="right">2.4%</td>
<td align="right">22,288</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">561</td>
<td align="right">0.1%</td>
<td align="right">561</td>
<td align="right">0.1%</td>
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
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr stacksummary</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">545,719,465</td>
<td align="right">100.0%</td>
<td align="right">545,099,608</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">178,542,721</td>
<td align="right">1.6%</td>
<td align="right">152,251,905</td>
<td align="right">1.4%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">175,406,255</td>
<td align="right">1.6%</td>
<td align="right">149,598,681</td>
<td align="right">1.4%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,988,224,560</td>
<td align="right">98.4%</td>
<td align="right">10,821,167,663</td>
<td align="right">98.6%</td>
<td align="right">-1.5%</td>
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
<td align="right">3,543,136</td>
<td align="right">100.0%</td>
<td align="right">3,014,685</td>
<td align="right">100.0%</td>
<td align="right">-14.9%</td>
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
<td align="right">690</td>
<td align="right">154.7%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right">246</td>
<td align="right">55.2%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">566</td>
<td align="right">126.9%</td>
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
<td align="right">584,357</td>
<td align="right">82.8%</td>
<td align="right">8,857</td>
<td align="right">7.0%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">685,057</td>
<td align="right">97.1%</td>
<td align="right">119,491</td>
<td align="right">94.5%</td>
<td align="right">-82.6%</td>
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
<td align="right">20,463</td>
<td align="right">99.4%</td>
<td align="right">6,873</td>
<td align="right">98.3%</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">1.7%</td>
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
<td align="right">1,459,290</td>
<td align="right">0.0%</td>
<td align="right">1,299,518</td>
<td align="right">0.0%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">511,329,999</td>
<td align="right">10.2%</td>
<td align="right">497,181,284</td>
<td align="right">10.0%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,508,672,891</td>
<td align="right">89.8%</td>
<td align="right">4,474,353,760</td>
<td align="right">90.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">45,399</td>
<td align="right">17.6%</td>
<td align="right">39,972</td>
<td align="right">17.1%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">212,010</td>
<td align="right">82.4%</td>
<td align="right">194,168</td>
<td align="right">82.9%</td>
<td align="right">-8.4%</td>
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
<td align="left">bool</td>
<td align="right">2,020</td>
<td align="right">1.0%</td>
<td align="right">775</td>
<td align="right">0.4%</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,809</td>
<td align="right">3.7%</td>
<td align="right">5,416</td>
<td align="right">2.8%</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,004</td>
<td align="right">0.5%</td>
<td align="right">724</td>
<td align="right">0.4%</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,370</td>
<td align="right">11.0%</td>
<td align="right">17,451</td>
<td align="right">9.0%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.2%</td>
<td align="right">312</td>
<td align="right">0.2%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">15,028</td>
<td align="right">7.1%</td>
<td align="right">13,751</td>
<td align="right">7.1%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,736</td>
<td align="right">21.6%</td>
<td align="right">42,037</td>
<td align="right">21.6%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">10,389</td>
<td align="right">4.9%</td>
<td align="right">9,666</td>
<td align="right">5.0%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">90,449</td>
<td align="right">42.7%</td>
<td align="right">88,488</td>
<td align="right">45.6%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">3.6%</td>
<td align="right">7,486</td>
<td align="right">3.9%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,834</td>
<td align="right">3.2%</td>
<td align="right">6,695</td>
<td align="right">3.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,367</td>
<td align="right">0.6%</td>
<td align="right">1,367</td>
<td align="right">0.7%</td>
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
<td align="right">155,761,017</td>
<td align="right">6.6%</td>
<td align="right">141,303,715</td>
<td align="right">6.1%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,395,959</td>
<td align="right">0.1%</td>
<td align="right">1,368,378</td>
<td align="right">0.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,190,804,543</td>
<td align="right">93.3%</td>
<td align="right">2,175,608,724</td>
<td align="right">93.8%</td>
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
<td align="right">59,393</td>
<td align="right">67.6%</td>
<td align="right">48,619</td>
<td align="right">64.2%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,459</td>
<td align="right">32.4%</td>
<td align="right">27,132</td>
<td align="right">35.8%</td>
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
<td align="left">tuple</td>
<td align="right">11,657</td>
<td align="right">19.6%</td>
<td align="right">7,424</td>
<td align="right">15.3%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,661</td>
<td align="right">19.6%</td>
<td align="right">7,993</td>
<td align="right">16.4%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,623</td>
<td align="right">24.6%</td>
<td align="right">13,236</td>
<td align="right">27.2%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">21,452</td>
<td align="right">36.1%</td>
<td align="right">19,966</td>
<td align="right">41.1%</td>
<td align="right">-6.9%</td>
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
<td align="right">3,535,250,461</td>
<td align="right">68.5%</td>
<td align="right">3,416,594,724</td>
<td align="right">68.0%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,460,422,658</td>
<td align="right">28.3%</td>
<td align="right">1,445,635,419</td>
<td align="right">28.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,984,031</td>
<td align="right">3.2%</td>
<td align="right">162,723,936</td>
<td align="right">3.2%</td>
<td align="right">-0.8%</td>
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
<td align="right">426,323</td>
<td align="right">12.1%</td>
<td align="right">387,671</td>
<td align="right">11.2%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,099,444</td>
<td align="right">87.9%</td>
<td align="right">3,073,854</td>
<td align="right">88.8%</td>
<td align="right">-0.8%</td>
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
<td align="right">67,440</td>
<td align="right">15.8%</td>
<td align="right">34,907</td>
<td align="right">9.0%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,447</td>
<td align="right">4.6%</td>
<td align="right">10,219</td>
<td align="right">2.6%</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right">130</td>
<td align="right">0.0%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,562</td>
<td align="right">1.1%</td>
<td align="right">3,646</td>
<td align="right">0.9%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,930</td>
<td align="right">1.6%</td>
<td align="right">5,786</td>
<td align="right">1.5%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,147</td>
<td align="right">0.7%</td>
<td align="right">2,865</td>
<td align="right">0.7%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,999</td>
<td align="right">8.2%</td>
<td align="right">32,407</td>
<td align="right">8.4%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,814</td>
<td align="right">2.5%</td>
<td align="right">10,437</td>
<td align="right">2.7%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">258</td>
<td align="right">0.1%</td>
<td align="right">251</td>
<td align="right">0.1%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,153</td>
<td align="right">0.7%</td>
<td align="right">3,111</td>
<td align="right">0.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">172,124</td>
<td align="right">40.4%</td>
<td align="right">170,254</td>
<td align="right">43.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right">1,212</td>
<td align="right">0.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,793</td>
<td align="right">19.7%</td>
<td align="right">83,223</td>
<td align="right">21.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,259</td>
<td align="right">4.3%</td>
<td align="right">18,243</td>
<td align="right">4.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">10,479</td>
<td align="right">2.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">501</td>
<td align="right">0.1%</td>
<td align="right"></td>
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
<td align="right">1,262,484</td>
<td align="right">0.0%</td>
<td align="right">1,063,703</td>
<td align="right">0.0%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">865,748,410</td>
<td align="right">6.3%</td>
<td align="right">816,141,457</td>
<td align="right">6.1%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">825,886,663</td>
<td align="right">6.0%</td>
<td align="right">785,717,715</td>
<td align="right">5.8%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,015,389,308</td>
<td align="right">87.6%</td>
<td align="right">11,836,012,230</td>
<td align="right">88.1%</td>
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
<td align="right">561,336</td>
<td align="right">3.3%</td>
<td align="right">459,944</td>
<td align="right">2.9%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,420,701</td>
<td align="right">96.7%</td>
<td align="right">15,456,768</td>
<td align="right">97.1%</td>
<td align="right">-5.9%</td>
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
<td align="right">1,778</td>
<td align="right">0.3%</td>
<td align="right">303</td>
<td align="right">0.1%</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,156</td>
<td align="right">1.1%</td>
<td align="right">3,653</td>
<td align="right">0.8%</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,181</td>
<td align="right">0.2%</td>
<td align="right">791</td>
<td align="right">0.2%</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,738</td>
<td align="right">0.5%</td>
<td align="right">2,085</td>
<td align="right">0.5%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">66,138</td>
<td align="right">11.8%</td>
<td align="right">50,784</td>
<td align="right">11.0%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,129</td>
<td align="right">1.6%</td>
<td align="right">7,556</td>
<td align="right">1.6%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,658</td>
<td align="right">3.0%</td>
<td align="right">14,102</td>
<td align="right">3.1%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">163</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">25,254</td>
<td align="right">4.5%</td>
<td align="right">21,693</td>
<td align="right">4.7%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
<td align="right">944</td>
<td align="right">0.2%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">58,075</td>
<td align="right">10.3%</td>
<td align="right">54,107</td>
<td align="right">11.8%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,810</td>
<td align="right">0.3%</td>
<td align="right">1,701</td>
<td align="right">0.4%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">77,634</td>
<td align="right">13.8%</td>
<td align="right">74,448</td>
<td align="right">16.2%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,450</td>
<td align="right">0.8%</td>
<td align="right">4,334</td>
<td align="right">0.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.1%</td>
<td align="right">6,363</td>
<td align="right">1.4%</td>
<td align="right">-0.7%</td>
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
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,479</td>
<td align="right">0.0%</td>
<td align="right">992</td>
<td align="right">0.0%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,151</td>
<td align="right">0.0%</td>
<td align="right">43,192</td>
<td align="right">0.0%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,054,806,995</td>
<td align="right">99.8%</td>
<td align="right">8,877,591,809</td>
<td align="right">99.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,623,539</td>
<td align="right">0.2%</td>
<td align="right">14,615,229</td>
<td align="right">0.2%</td>
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
<td align="right">139,106</td>
<td align="right">100.0%</td>
<td align="right">109,563</td>
<td align="right">100.0%</td>
<td align="right">-21.2%</td>
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
<td align="right">251</td>
<td align="right">0.0%</td>
<td align="right">96</td>
<td align="right">0.0%</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,815,057</td>
<td align="right">100.0%</td>
<td align="right">61,844,985</td>
<td align="right">100.0%</td>
<td align="right">-4.6%</td>
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
<td align="right">1,925</td>
<td align="right">100.0%</td>
<td align="right">-19.6%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,711</td>
<td align="right">0.0%</td>
<td align="right">9,124</td>
<td align="right">0.0%</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,815,507</td>
<td align="right">17.9%</td>
<td align="right">122,081,423</td>
<td align="right">17.2%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">591,606,566</td>
<td align="right">82.1%</td>
<td align="right">586,227,055</td>
<td align="right">82.8%</td>
<td align="right">-0.9%</td>
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
<td align="right">463</td>
<td align="right">1.5%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">31,288</td>
<td align="right">98.5%</td>
<td align="right">-9.1%</td>
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
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">940</td>
<td align="right">3.0%</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">5,908</td>
<td align="right">18.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">78.1%</td>
<td align="right">0.0%</td>
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
<td align="right">113,737,797</td>
<td align="right">5.7%</td>
<td align="right">110,755,641</td>
<td align="right">5.6%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">77,127,189</td>
<td align="right">3.9%</td>
<td align="right">75,610,610</td>
<td align="right">3.9%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,792,457,757</td>
<td align="right">90.4%</td>
<td align="right">1,776,239,144</td>
<td align="right">90.5%</td>
<td align="right">-0.9%</td>
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
<td align="right">52,753</td>
<td align="right">2.4%</td>
<td align="right">48,699</td>
<td align="right">2.2%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,185,784</td>
<td align="right">97.6%</td>
<td align="right">2,125,086</td>
<td align="right">97.8%</td>
<td align="right">-2.8%</td>
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
<td align="right">3,350</td>
<td align="right">6.4%</td>
<td align="right">1,764</td>
<td align="right">3.6%</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">272,247</td>
<td align="right">516.1%</td>
<td align="right">208,476</td>
<td align="right">428.1%</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">311</td>
<td align="right">0.6%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">1,435</td>
<td align="right">2.9%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">817</td>
<td align="right">1.5%</td>
<td align="right">707</td>
<td align="right">1.5%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,331</td>
<td align="right">10.1%</td>
<td align="right">4,713</td>
<td align="right">9.7%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">103</td>
<td align="right">0.2%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.5%</td>
<td align="right">7,226</td>
<td align="right">14.8%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">46.4%</td>
<td align="right">23,707</td>
<td align="right">48.7%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">6,007</td>
<td align="right">11.4%</td>
<td align="right">5,989</td>
<td align="right">12.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">741</td>
<td align="right">1.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">729</td>
<td align="right">1.5%</td>
<td align="right">-0.1%</td>
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
<td align="right">112,724,681</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">923,101,492</td>
<td align="right">56.8%</td>
<td align="right">912,920,067</td>
<td align="right">56.6%</td>
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
<td align="right">700,841,865</td>
<td align="right">43.2%</td>
<td align="right">698,778,071</td>
<td align="right">43.4%</td>
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
<td align="right">2,123</td>
<td align="right">1.2%</td>
<td align="right">1,363</td>
<td align="right">0.7%</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">182,266</td>
<td align="right">98.8%</td>
<td align="right">180,736</td>
<td align="right">99.3%</td>
<td align="right">-0.8%</td>
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
<td align="right">19,343</td>
<td align="right">10.6%</td>
<td align="right">18,005</td>
<td align="right">10.0%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,011</td>
<td align="right">1.7%</td>
<td align="right">2,919</td>
<td align="right">1.6%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,662</td>
<td align="right">0.9%</td>
<td align="right">1,614</td>
<td align="right">0.9%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,314</td>
<td align="right">2.9%</td>
<td align="right">5,295</td>
<td align="right">2.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,324</td>
<td align="right">9.5%</td>
<td align="right">17,316</td>
<td align="right">9.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">86,613</td>
<td align="right">47.5%</td>
<td align="right">86,588</td>
<td align="right">47.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.8%</td>
<td align="right">48,931</td>
<td align="right">27.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">68</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">110,036,583</td>
<td align="right">2.2%</td>
<td align="right">105,609,809</td>
<td align="right">2.1%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,734,808,453</td>
<td align="right">92.7%</td>
<td align="right">4,623,748,327</td>
<td align="right">92.7%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">263,014,242</td>
<td align="right">5.1%</td>
<td align="right">259,580,507</td>
<td align="right">5.2%</td>
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
<td align="right">2,125,480</td>
<td align="right">77.1%</td>
<td align="right">2,028,748</td>
<td align="right">76.8%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">631,589</td>
<td align="right">22.9%</td>
<td align="right">614,110</td>
<td align="right">23.2%</td>
<td align="right">-2.8%</td>
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
<td align="right">13,380</td>
<td align="right">2.1%</td>
<td align="right">7,136</td>
<td align="right">1.2%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">97,667</td>
<td align="right">15.5%</td>
<td align="right">92,477</td>
<td align="right">15.1%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">20,482</td>
<td align="right">3.2%</td>
<td align="right">19,803</td>
<td align="right">3.2%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">77,680</td>
<td align="right">12.3%</td>
<td align="right">76,195</td>
<td align="right">12.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">132,986</td>
<td align="right">21.1%</td>
<td align="right">130,558</td>
<td align="right">21.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,990</td>
<td align="right">1.6%</td>
<td align="right">9,924</td>
<td align="right">1.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">380</td>
<td align="right">0.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,640</td>
<td align="right">41.0%</td>
<td align="right">257,305</td>
<td align="right">41.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,878</td>
<td align="right">3.0%</td>
<td align="right">18,828</td>
<td align="right">3.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
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
<td align="right">1,809,465</td>
<td align="right">0.1%</td>
<td align="right">568,116</td>
<td align="right">0.0%</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,240,895,160</td>
<td align="right">99.9%</td>
<td align="right">1,181,258,243</td>
<td align="right">100.0%</td>
<td align="right">-4.8%</td>
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
<td align="right">997</td>
<td align="right">9.0%</td>
<td align="right">388</td>
<td align="right">5.2%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,049</td>
<td align="right">91.0%</td>
<td align="right">7,114</td>
<td align="right">94.8%</td>
<td align="right">-29.2%</td>
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
<td align="right">763</td>
<td align="right">76.5%</td>
<td align="right">200</td>
<td align="right">51.5%</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">13.6%</td>
<td align="right">90</td>
<td align="right">23.2%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">9.8%</td>
<td align="right">98</td>
<td align="right">25.3%</td>
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
<td align="right">1,494,756,406</td>
<td align="right">0.7%</td>
<td align="right">1,409,115,698</td>
<td align="right">0.7%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">7,608,827,351</td>
<td align="right">3.6%</td>
<td align="right">7,485,258,306</td>
<td align="right">3.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">114,922,124,062</td>
<td align="right">54.6%</td>
<td align="right">113,098,207,667</td>
<td align="right">54.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">86,623,307,596</td>
<td align="right">41.1%</td>
<td align="right">85,288,049,472</td>
<td align="right">41.1%</td>
<td align="right">-1.5%</td>
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
<td align="right">175,406,255</td>
<td align="right">2.3%</td>
<td align="right">149,598,681</td>
<td align="right">2.0%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,761,017</td>
<td align="right">2.0%</td>
<td align="right">141,303,715</td>
<td align="right">1.9%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,507</td>
<td align="right">1.7%</td>
<td align="right">122,081,423</td>
<td align="right">1.6%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">825,886,663</td>
<td align="right">10.6%</td>
<td align="right">785,717,715</td>
<td align="right">10.3%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">511,329,999</td>
<td align="right">6.6%</td>
<td align="right">497,181,284</td>
<td align="right">6.5%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">263,014,242</td>
<td align="right">3.4%</td>
<td align="right">259,580,507</td>
<td align="right">3.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,460,422,658</td>
<td align="right">18.8%</td>
<td align="right">1,445,635,419</td>
<td align="right">18.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,805,560,097</td>
<td align="right">36.1%</td>
<td align="right">2,781,575,869</td>
<td align="right">36.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,841,865</td>
<td align="right">9.0%</td>
<td align="right">698,778,071</td>
<td align="right">9.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,719,465</td>
<td align="right">7.0%</td>
<td align="right">545,099,608</td>
<td align="right">7.1%</td>
<td align="right">-0.1%</td>
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
<td align="right">87,387,500</td>
<td align="right">5.8%</td>
<td align="right">77,636,641</td>
<td align="right">5.5%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,896,287</td>
<td align="right">5.5%</td>
<td align="right">74,696,426</td>
<td align="right">5.3%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">48,534,764</td>
<td align="right">3.2%</td>
<td align="right">45,150,525</td>
<td align="right">3.2%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">266,108,012</td>
<td align="right">17.8%</td>
<td align="right">249,994,988</td>
<td align="right">17.7%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">85,592,537</td>
<td align="right">5.7%</td>
<td align="right">82,367,398</td>
<td align="right">5.8%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,231,153</td>
<td align="right">6.3%</td>
<td align="right">92,494,234</td>
<td align="right">6.6%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">368,060,206</td>
<td align="right">24.6%</td>
<td align="right">362,389,944</td>
<td align="right">25.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,422,487</td>
<td align="right">3.6%</td>
<td align="right">53,783,654</td>
<td align="right">3.8%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,901,715</td>
<td align="right">5.5%</td>
<td align="right">81,251,980</td>
<td align="right">5.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,004,921</td>
<td align="right">5.5%</td>
<td align="right">81,419,078</td>
<td align="right">5.8%</td>
<td align="right">-0.7%</td>
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
<td align="right">3,889</td>
<td align="right">0.0%</td>
<td align="right">2,930</td>
<td align="right">0.0%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,891,701</td>
<td align="right">0.4%</td>
<td align="right">22,044,509</td>
<td align="right">0.3%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">273,455,670</td>
<td align="right">4.1%</td>
<td align="right">257,502,538</td>
<td align="right">3.9%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">936,839,520</td>
<td align="right">14.0%</td>
<td align="right">903,625,117</td>
<td align="right">13.8%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">941,116,850</td>
<td align="right">14.1%</td>
<td align="right">907,900,664</td>
<td align="right">13.9%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">260,794,480</td>
<td align="right">3.9%</td>
<td align="right">254,449,919</td>
<td align="right">3.9%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,169,942,820</td>
<td align="right">77.2%</td>
<td align="right">5,044,492,892</td>
<td align="right">77.2%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,526,012,596</td>
<td align="right">22.8%</td>
<td align="right">1,489,177,832</td>
<td align="right">22.8%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,526,012,596</td>
<td align="right">22.8%</td>
<td align="right">1,489,177,832</td>
<td align="right">22.8%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,420,404,418</td>
<td align="right">81.0%</td>
<td align="right">5,292,015,141</td>
<td align="right">81.0%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,204,765</td>
<td align="right">1.1%</td>
<td align="right">69,680,071</td>
<td align="right">1.1%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,895,746</td>
<td align="right">8.7%</td>
<td align="right">581,277,168</td>
<td align="right">8.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,441</td>
<td align="right">0.1%</td>
<td align="right">4,272,617</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,402</td>
<td align="right">2.0%</td>
<td align="right">132,512,960</td>
<td align="right">2.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">5,766,396</td>
<td align="right"></td>
<td align="right">4,978,887</td>
<td align="right"></td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">52,755,409</td>
<td align="right"></td>
<td align="right">56,382,377</td>
<td align="right"></td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,240,970,965</td>
<td align="right"></td>
<td align="right">2,124,607,871</td>
<td align="right"></td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">25,503,638,300</td>
<td align="right">27.5%</td>
<td align="right">24,241,454,062</td>
<td align="right">27.0%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,872,832,153</td>
<td align="right"></td>
<td align="right">2,730,699,109</td>
<td align="right"></td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">57,717,682</td>
<td align="right"></td>
<td align="right">60,560,644</td>
<td align="right"></td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,104,733,081</td>
<td align="right"></td>
<td align="right">13,446,677,803</td>
<td align="right"></td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,104,612,808</td>
<td align="right">71.8%</td>
<td align="right">13,446,617,729</td>
<td align="right">71.3%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,871,176,642</td>
<td align="right">1.7%</td>
<td align="right">1,794,490,270</td>
<td align="right">1.7%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">51,745,351,167</td>
<td align="right">47.0%</td>
<td align="right">49,766,005,980</td>
<td align="right">46.7%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">22,800,708,644</td>
<td align="right">24.6%</td>
<td align="right">22,142,478,754</td>
<td align="right">24.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">31,779,105,847</td>
<td align="right">28.9%</td>
<td align="right">30,939,453,818</td>
<td align="right">29.0%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,605,545,215</td>
<td align="right">22.4%</td>
<td align="right">24,034,218,943</td>
<td align="right">22.6%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,441,243</td>
<td align="right">2.6%</td>
<td align="right">4,344,903</td>
<td align="right">2.6%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">39,792,649,594</td>
<td align="right">42.9%</td>
<td align="right">38,965,604,471</td>
<td align="right">43.4%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,448,741,050</td>
<td align="right">27.8%</td>
<td align="right">5,343,372,069</td>
<td align="right">28.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,526,719,329</td>
<td align="right">28.2%</td>
<td align="right">5,420,330,966</td>
<td align="right">28.7%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,127,392,652</td>
<td align="right"></td>
<td align="right">6,018,919,869</td>
<td align="right"></td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,582,743,846</td>
<td align="right">4.9%</td>
<td align="right">4,506,450,155</td>
<td align="right">5.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">169,165,832</td>
<td align="right"></td>
<td align="right">166,824,347</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,558,525</td>
<td align="right">0.4%</td>
<td align="right">70,582,408</td>
<td align="right">0.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">475,865</td>
<td align="right">0.3%</td>
<td align="right">471,009</td>
<td align="right">0.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,419,754</td>
<td align="right">0.0%</td>
<td align="right">6,376,489</td>
<td align="right">0.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">365,036</td>
<td align="right">102,388,306</td>
<td align="right">9,467,805,104</td>
<td align="right">745,083,115</td>
<td align="right">764,535,477</td>
<td align="right">363,712</td>
<td align="right">102,298,422</td>
<td align="right">9,406,486,553</td>
<td align="right">736,321,446</td>
<td align="right">762,279,090</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,608,591,668</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,608,585,896</td>
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
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">30</td>
<td align="right">22</td>
<td align="right">-26.7%</td>
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
<td align="right">29</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,629</td>
<td align="right">22,592</td>
<td align="right">-0.2%</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">2,458</td>
<td align="right">2,395</td>
<td align="right">-2.6%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-16
