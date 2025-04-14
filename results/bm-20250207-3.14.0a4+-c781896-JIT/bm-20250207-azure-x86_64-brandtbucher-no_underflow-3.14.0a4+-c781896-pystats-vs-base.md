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
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">207,639</td>
<td align="right">1,751,802</td>
<td align="right">743.7%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">27,991,418</td>
<td align="right">70,611,890</td>
<td align="right">152.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">54,635,115</td>
<td align="right">131,401,322</td>
<td align="right">140.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">365,501,272</td>
<td align="right">697,610,529</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">34,046,122</td>
<td align="right">62,543,995</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">324,114,886</td>
<td align="right">594,116,830</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,068,865</td>
<td align="right">15,554,184</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">643,913,005</td>
<td align="right">1,091,345,477</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">163,627,501</td>
<td align="right">259,228,695</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">323,704,764</td>
<td align="right">507,541,792</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">325,391,960</td>
<td align="right">504,639,440</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">651,528,245</td>
<td align="right">954,952,601</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">526,250,877</td>
<td align="right">743,154,551</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">194,346,331</td>
<td align="right">273,276,998</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">482,590,713</td>
<td align="right">676,892,117</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">71,389,840</td>
<td align="right">96,630,448</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,256,825,695</td>
<td align="right">828,956,509</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">131,187,714</td>
<td align="right">170,413,692</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">163,769,395</td>
<td align="right">204,787,541</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">218,060,674</td>
<td align="right">267,067,735</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">521,917,870</td>
<td align="right">635,657,788</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">453,378,206</td>
<td align="right">547,950,334</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">203,371,144</td>
<td align="right">244,777,362</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,117,431</td>
<td align="right">9,742,691</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">99,223,695</td>
<td align="right">118,894,354</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">377,539,337</td>
<td align="right">447,024,727</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">317,518,186</td>
<td align="right">374,706,175</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">121,217,608</td>
<td align="right">142,544,653</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">751,638,660</td>
<td align="right">881,726,421</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">321,348,836</td>
<td align="right">372,889,202</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">121,542,383</td>
<td align="right">140,044,909</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">40,136,534</td>
<td align="right">45,944,919</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,602,633,046</td>
<td align="right">5,263,430,132</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">240,841,993</td>
<td align="right">275,153,302</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,560,434</td>
<td align="right">3,911,637</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,869,354</td>
<td align="right">4,197,304</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">38,186,179</td>
<td align="right">43,419,207</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">44,928,203</td>
<td align="right">50,867,618</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">872,331,417</td>
<td align="right">967,855,103</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,904,612,733</td>
<td align="right">2,104,432,152</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,219,276,824</td>
<td align="right">3,532,137,079</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,833,018,724</td>
<td align="right">4,200,635,832</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">188,748,158</td>
<td align="right">205,919,565</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">28,061,628</td>
<td align="right">30,543,492</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">156,832,784</td>
<td align="right">169,983,721</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">116,937,588</td>
<td align="right">126,614,011</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">217,487,895</td>
<td align="right">235,297,822</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">140,696,657</td>
<td align="right">151,526,035</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,938,193,823</td>
<td align="right">19,284,324,728</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">226,752,203</td>
<td align="right">241,809,824</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">783,847,233</td>
<td align="right">831,573,088</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">377,330,701</td>
<td align="right">398,658,947</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">88,690,242</td>
<td align="right">93,531,769</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">102,981,607</td>
<td align="right">108,513,860</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,131,041,876</td>
<td align="right">4,348,831,304</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">172,836,517</td>
<td align="right">181,917,433</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">95,151,896</td>
<td align="right">99,993,408</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">91,802,652</td>
<td align="right">96,271,713</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">262,066,094</td>
<td align="right">274,802,235</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">121,482,713</td>
<td align="right">127,202,561</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,395,106,057</td>
<td align="right">2,497,242,248</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">949,228,826</td>
<td align="right">988,334,681</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">124,246,483</td>
<td align="right">129,234,184</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">281,027,777</td>
<td align="right">291,986,891</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">149,491,269</td>
<td align="right">154,852,375</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,527,328,012</td>
<td align="right">2,611,664,085</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">418,690,143</td>
<td align="right">432,458,257</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">496,814,409</td>
<td align="right">513,044,979</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">195,777,357</td>
<td align="right">201,897,964</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">656,748,510</td>
<td align="right">676,184,694</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">73,437,315</td>
<td align="right">71,335,308</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">351,468,781</td>
<td align="right">361,397,945</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">332,171,848</td>
<td align="right">340,738,866</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">92,982,225</td>
<td align="right">95,353,227</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,250,408,933</td>
<td align="right">2,307,790,047</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">864,178,771</td>
<td align="right">886,070,112</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">355,255,386</td>
<td align="right">364,043,436</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">32,307,251</td>
<td align="right">33,100,707</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">177,437,868</td>
<td align="right">181,690,281</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">124,221,176</td>
<td align="right">127,170,075</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">574,371,605</td>
<td align="right">587,696,275</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">14,459,188</td>
<td align="right">14,123,848</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,648</td>
<td align="right">2,708</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">239,373,629</td>
<td align="right">234,423,308</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">115,506,444</td>
<td align="right">117,892,915</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">478,917,505</td>
<td align="right">488,806,858</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,093,238,676</td>
<td align="right">1,112,761,539</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,819,764</td>
<td align="right">10,626,728</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">288,641,978</td>
<td align="right">293,493,031</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">34,384,503</td>
<td align="right">34,931,914</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">71,074,641</td>
<td align="right">72,152,073</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,615,146,827</td>
<td align="right">2,652,642,778</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">682,390,173</td>
<td align="right">692,114,571</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">118,276,259</td>
<td align="right">119,866,084</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,784,797,875</td>
<td align="right">3,833,266,542</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">396,253,031</td>
<td align="right">401,156,792</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">57,598,539</td>
<td align="right">58,262,614</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">172,395,909</td>
<td align="right">174,143,844</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">36,931,884</td>
<td align="right">36,581,592</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,136,267</td>
<td align="right">9,052,716</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,545,353</td>
<td align="right">9,461,783</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,809,841</td>
<td align="right">4,768,000</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">43,483,063</td>
<td align="right">43,132,771</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">159,814,461</td>
<td align="right">158,547,790</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">22,438,217</td>
<td align="right">22,262,661</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">422,855,923</td>
<td align="right">426,069,493</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">949,504,529</td>
<td align="right">955,853,810</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">807,445,737</td>
<td align="right">812,205,623</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,918,880</td>
<td align="right">60,579,570</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">93,816,931</td>
<td align="right">94,319,770</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,360,301,459</td>
<td align="right">5,388,636,876</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">229,513,355</td>
<td align="right">228,356,201</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">403,347</td>
<td align="right">405,283</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">19,678,584</td>
<td align="right">19,594,208</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">58,174,163</td>
<td align="right">57,974,230</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">273,449,875</td>
<td align="right">272,516,227</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,322,398,518</td>
<td align="right">2,330,255,436</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">474,680,371</td>
<td align="right">476,043,580</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">86,694,854</td>
<td align="right">86,456,294</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,625,723,507</td>
<td align="right">1,630,124,566</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,762,774,670</td>
<td align="right">1,767,397,689</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,128,380</td>
<td align="right">48,020,528</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">108,567,678</td>
<td align="right">108,354,312</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">86,281,437</td>
<td align="right">86,155,700</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">138,359,004</td>
<td align="right">138,160,175</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,897,338,514</td>
<td align="right">4,903,612,906</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,282,262</td>
<td align="right">2,280,178</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,319,533</td>
<td align="right">180,467,027</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,843,306</td>
<td align="right">57,800,189</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,331,019</td>
<td align="right">242,154,812</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,387,648</td>
<td align="right">244,210,035</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,946,628</td>
<td align="right">101,012,031</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">891,813,562</td>
<td align="right">891,318,252</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,700</td>
<td align="right">33,717</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">172,616,230</td>
<td align="right">172,534,334</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,133</td>
<td align="right">5,131</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">174,900,066</td>
<td align="right">174,858,105</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">133,093</td>
<td align="right">133,123</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,817</td>
<td align="right">120,796</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,560,550</td>
<td align="right">26,556,032</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">61,264,902</td>
<td align="right">61,274,867</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,040,064,636</td>
<td align="right">1,039,908,115</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,680</td>
<td align="right">773,580</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">508,757,814</td>
<td align="right">508,803,890</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,439,855</td>
<td align="right">1,439,743</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,172,878</td>
<td align="right">67,167,908</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,758,734</td>
<td align="right">14,759,676</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,048,704</td>
<td align="right">3,048,534</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">156,037,000</td>
<td align="right">156,030,950</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">71,494,772</td>
<td align="right">71,495,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">81,166,969</td>
<td align="right">81,165,870</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">19,916,051</td>
<td align="right">19,915,845</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,246,534</td>
<td align="right">20,246,328</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,246,555</td>
<td align="right">20,246,349</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,196,387</td>
<td align="right">5,196,428</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,824</td>
<td align="right">5,803,792</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,094,665</td>
<td align="right">10,094,613</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">112,765,379</td>
<td align="right">112,765,001</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,194,076</td>
<td align="right">1,194,078</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,920</td>
<td align="right">1,645,921</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,713,027</td>
<td align="right">419,712,802</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">29,023,508</td>
<td align="right">29,023,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,303,416</td>
<td align="right">593,303,416</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,900</td>
<td align="right">302,607,900</td>
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
<td align="right">128,851,678</td>
<td align="right">128,851,678</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">53,629,016</td>
<td align="right">53,629,016</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,793</td>
<td align="right">41,964,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,911,015</td>
<td align="right">35,911,015</td>
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
<td align="right">8,976,841</td>
<td align="right">8,976,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">6,152,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
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
<td align="left">RERAISE</td>
<td align="right">3,488,296</td>
<td align="right">3,488,296</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">781,020</td>
<td align="right">781,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,734</td>
<td align="right">98,734</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,552</td>
<td align="right">84,552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">59,727</td>
<td align="right">59,727</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,147</td>
<td align="right">57,147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,770</td>
<td align="right">56,770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,546</td>
<td align="right">17,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,321</td>
<td align="right">5,321</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,896</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,620</td>
<td align="right">3,620</td>
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
<td align="right">151</td>
<td align="right">151</td>
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
<td align="right">453,186,284</td>
<td align="right">5.6%</td>
<td align="right">547,735,235</td>
<td align="right">6.6%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,644,883,004</td>
<td align="right">93.8%</td>
<td align="right">7,638,636,287</td>
<td align="right">92.7%</td>
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
<td align="right">51,025,581</td>
<td align="right">0.6%</td>
<td align="right">51,018,531</td>
<td align="right">0.6%</td>
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
<td align="right">183,393</td>
<td align="right">15.9%</td>
<td align="right">206,505</td>
<td align="right">17.5%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">971,240</td>
<td align="right">84.1%</td>
<td align="right">971,173</td>
<td align="right">82.5%</td>
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
<td align="left">remainder</td>
<td align="right">17,896</td>
<td align="right">9.8%</td>
<td align="right">36,637</td>
<td align="right">17.7%</td>
<td align="right">104.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21,860</td>
<td align="right">11.9%</td>
<td align="right">25,899</td>
<td align="right">12.5%</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">209</td>
<td align="right">0.1%</td>
<td align="right">189</td>
<td align="right">0.1%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,477</td>
<td align="right">12.8%</td>
<td align="right">23,755</td>
<td align="right">11.5%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,154</td>
<td align="right">1.7%</td>
<td align="right">3,174</td>
<td align="right">1.5%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">633</td>
<td align="right">0.3%</td>
<td align="right">631</td>
<td align="right">0.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">494</td>
<td align="right">0.3%</td>
<td align="right">495</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,462</td>
<td align="right">10.1%</td>
<td align="right">18,495</td>
<td align="right">9.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">29,924</td>
<td align="right">16.3%</td>
<td align="right">29,944</td>
<td align="right">14.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,342</td>
<td align="right">1.3%</td>
<td align="right">2,343</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">11,299</td>
<td align="right">6.2%</td>
<td align="right">11,300</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">17,023</td>
<td align="right">9.3%</td>
<td align="right">17,023</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">15,432</td>
<td align="right">8.4%</td>
<td align="right">15,432</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">7,753</td>
<td align="right">4.2%</td>
<td align="right">7,753</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,752</td>
<td align="right">3.1%</td>
<td align="right">5,752</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,767</td>
<td align="right">1.5%</td>
<td align="right">2,767</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">1.1%</td>
<td align="right">1,996</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.8%</td>
<td align="right">1,384</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.5%</td>
<td align="right">836</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">597</td>
<td align="right">0.3%</td>
<td align="right">597</td>
<td align="right">0.3%</td>
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
<td align="right">121,542,383</td>
<td align="right">100.0%</td>
<td align="right">140,044,909</td>
<td align="right">100.0%</td>
<td align="right">15.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">526,082,724</td>
<td align="right">8.7%</td>
<td align="right">742,932,413</td>
<td align="right">11.9%</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,494,019,809</td>
<td align="right">91.2%</td>
<td align="right">5,491,962,810</td>
<td align="right">88.0%</td>
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
<td align="right">5,827,967</td>
<td align="right">0.1%</td>
<td align="right">5,827,814</td>
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
<td align="right">159,874</td>
<td align="right">57.5%</td>
<td align="right">212,919</td>
<td align="right">64.2%</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118,014</td>
<td align="right">42.5%</td>
<td align="right">118,954</td>
<td align="right">35.8%</td>
<td align="right">0.8%</td>
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
<td align="right">62,873</td>
<td align="right">39.3%</td>
<td align="right">110,307</td>
<td align="right">51.8%</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">792</td>
<td align="right">0.5%</td>
<td align="right">948</td>
<td align="right">0.4%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">35,272</td>
<td align="right">22.1%</td>
<td align="right">40,897</td>
<td align="right">19.2%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">3,936</td>
<td align="right">2.5%</td>
<td align="right">3,823</td>
<td align="right">1.8%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">7,581</td>
<td align="right">4.7%</td>
<td align="right">7,521</td>
<td align="right">3.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,446</td>
<td align="right">7.8%</td>
<td align="right">12,449</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">30,333</td>
<td align="right">19.0%</td>
<td align="right">30,333</td>
<td align="right">14.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,607</td>
<td align="right">2.3%</td>
<td align="right">3,607</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">1.8%</td>
<td align="right">2,941</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">139,717,554</td>
<td align="right">1.2%</td>
<td align="right">137,631,655</td>
<td align="right">1.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">137,312,457</td>
<td align="right">1.2%</td>
<td align="right">135,265,991</td>
<td align="right">1.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,111,672,671</td>
<td align="right">98.8%</td>
<td align="right">11,110,939,441</td>
<td align="right">98.8%</td>
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
<td align="right">22,186</td>
<td align="right">0.0%</td>
<td align="right">22,186</td>
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
<td align="right">2,807,998</td>
<td align="right">100.0%</td>
<td align="right">2,770,501</td>
<td align="right">100.0%</td>
<td align="right">-1.3%</td>
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
<td align="left">init not python</td>
<td align="right">287</td>
<td align="right">64.3%</td>
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right">-7.0%</td>
</tr>
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
<td align="right">684,422</td>
<td align="right">97.1%</td>
<td align="right">684,422</td>
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
<td align="right">583,846</td>
<td align="right">82.9%</td>
<td align="right">583,846</td>
<td align="right">82.9%</td>
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
<td align="right">20,121</td>
<td align="right">99.4%</td>
<td align="right">20,100</td>
<td align="right">99.4%</td>
<td align="right">-0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,169,305</td>
<td align="right">0.0%</td>
<td align="right">1,157,708</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,528,897,673</td>
<td align="right">97.6%</td>
<td align="right">4,516,132,941</td>
<td align="right">97.6%</td>
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
<td align="right">108,445,803</td>
<td align="right">2.3%</td>
<td align="right">108,232,385</td>
<td align="right">2.3%</td>
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
<td align="right">103,982</td>
<td align="right">72.3%</td>
<td align="right">103,711</td>
<td align="right">72.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39,763</td>
<td align="right">27.7%</td>
<td align="right">39,863</td>
<td align="right">27.8%</td>
<td align="right">0.3%</td>
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
<td align="right">356</td>
<td align="right">0.3%</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,367</td>
<td align="right">1.3%</td>
<td align="right">1,321</td>
<td align="right">1.3%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">11,800</td>
<td align="right">11.3%</td>
<td align="right">11,616</td>
<td align="right">11.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,602</td>
<td align="right">4.4%</td>
<td align="right">4,553</td>
<td align="right">4.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,979</td>
<td align="right">1.9%</td>
<td align="right">1,972</td>
<td align="right">1.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,718</td>
<td align="right">7.4%</td>
<td align="right">7,705</td>
<td align="right">7.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,158</td>
<td align="right">22.3%</td>
<td align="right">23,190</td>
<td align="right">22.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">802</td>
<td align="right">0.8%</td>
<td align="right">801</td>
<td align="right">0.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">37,024</td>
<td align="right">35.6%</td>
<td align="right">37,046</td>
<td align="right">35.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,553</td>
<td align="right">6.3%</td>
<td align="right">6,550</td>
<td align="right">6.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.3%</td>
<td align="right">7,639</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">984</td>
<td align="right">0.9%</td>
<td align="right">984</td>
<td align="right">0.9%</td>
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
<td align="right">71,348,910</td>
<td align="right">3.1%</td>
<td align="right">96,583,174</td>
<td align="right">4.2%</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,193,808,265</td>
<td align="right">96.8%</td>
<td align="right">2,192,438,895</td>
<td align="right">95.7%</td>
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
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
<td align="right">1,916,987</td>
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
<td align="right">38,869</td>
<td align="right">50.4%</td>
<td align="right">45,013</td>
<td align="right">53.9%</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,235</td>
<td align="right">49.6%</td>
<td align="right">38,435</td>
<td align="right">46.1%</td>
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
<td align="left">list</td>
<td align="right">7,857</td>
<td align="right">20.2%</td>
<td align="right">14,075</td>
<td align="right">31.3%</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,166</td>
<td align="right">28.7%</td>
<td align="right">11,099</td>
<td align="right">24.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,827</td>
<td align="right">25.3%</td>
<td align="right">9,807</td>
<td align="right">21.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,019</td>
<td align="right">25.8%</td>
<td align="right">10,032</td>
<td align="right">22.3%</td>
<td align="right">0.1%</td>
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
<td align="right">872,893,637</td>
<td align="right">77.1%</td>
<td align="right">1,262,810,194</td>
<td align="right">80.8%</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">203,255,734</td>
<td align="right">18.0%</td>
<td align="right">244,646,116</td>
<td align="right">15.7%</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">55,525,142</td>
<td align="right">4.9%</td>
<td align="right">55,541,544</td>
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
<td align="right">110,355</td>
<td align="right">9.5%</td>
<td align="right">126,200</td>
<td align="right">10.7%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,052,538</td>
<td align="right">90.5%</td>
<td align="right">1,052,829</td>
<td align="right">89.3%</td>
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
<td align="right">2,513</td>
<td align="right">2.3%</td>
<td align="right">4,330</td>
<td align="right">3.4%</td>
<td align="right">72.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">7,086</td>
<td align="right">6.4%</td>
<td align="right">11,120</td>
<td align="right">8.8%</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,656</td>
<td align="right">4.2%</td>
<td align="right">6,531</td>
<td align="right">5.2%</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,825</td>
<td align="right">2.6%</td>
<td align="right">3,771</td>
<td align="right">3.0%</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">6,923</td>
<td align="right">6.3%</td>
<td align="right">8,629</td>
<td align="right">6.8%</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,858</td>
<td align="right">10.7%</td>
<td align="right">13,032</td>
<td align="right">10.3%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">49,331</td>
<td align="right">44.7%</td>
<td align="right">53,632</td>
<td align="right">42.5%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,529</td>
<td align="right">1.4%</td>
<td align="right">1,465</td>
<td align="right">1.2%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,400</td>
<td align="right">1.3%</td>
<td align="right">1,359</td>
<td align="right">1.1%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">16,502</td>
<td align="right">15.0%</td>
<td align="right">16,608</td>
<td align="right">13.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,537</td>
<td align="right">4.1%</td>
<td align="right">4,528</td>
<td align="right">3.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">734</td>
<td align="right">0.7%</td>
<td align="right">734</td>
<td align="right">0.6%</td>
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
<td align="left">callable</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">134</td>
<td align="right">0.1%</td>
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
<td align="right">572,614,054</td>
<td align="right">4.2%</td>
<td align="right">585,931,767</td>
<td align="right">4.4%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">788,289,485</td>
<td align="right">5.8%</td>
<td align="right">803,304,733</td>
<td align="right">6.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,129,259,474</td>
<td align="right">89.9%</td>
<td align="right">12,065,570,983</td>
<td align="right">89.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,404,473</td>
<td align="right">0.0%</td>
<td align="right">1,404,473</td>
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
<td align="right">14,955,071</td>
<td align="right">96.8%</td>
<td align="right">15,242,163</td>
<td align="right">96.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">492,076</td>
<td align="right">3.2%</td>
<td align="right">495,590</td>
<td align="right">3.1%</td>
<td align="right">0.7%</td>
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
<td align="right">23,411</td>
<td align="right">4.8%</td>
<td align="right">24,990</td>
<td align="right">5.0%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,561</td>
<td align="right">3.2%</td>
<td align="right">16,265</td>
<td align="right">3.3%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">42,758</td>
<td align="right">8.7%</td>
<td align="right">44,440</td>
<td align="right">9.0%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,110</td>
<td align="right">1.0%</td>
<td align="right">4,948</td>
<td align="right">1.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,801</td>
<td align="right">0.4%</td>
<td align="right">1,775</td>
<td align="right">0.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">44,705</td>
<td align="right">9.1%</td>
<td align="right">44,115</td>
<td align="right">8.9%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,583</td>
<td align="right">0.3%</td>
<td align="right">1,584</td>
<td align="right">0.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60,517</td>
<td align="right">12.3%</td>
<td align="right">60,491</td>
<td align="right">12.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,087</td>
<td align="right">1.0%</td>
<td align="right">5,086</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,945</td>
<td align="right">1.6%</td>
<td align="right">7,944</td>
<td align="right">1.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.3%</td>
<td align="right">6,405</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,369</td>
<td align="right">0.5%</td>
<td align="right">2,369</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.2%</td>
<td align="right">1,092</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">820</td>
<td align="right">0.2%</td>
<td align="right">820</td>
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
<td align="right">4,593,275,333</td>
<td align="right">99.7%</td>
<td align="right">4,829,912,721</td>
<td align="right">99.7%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,132</td>
<td align="right">0.0%</td>
<td align="right">52,588</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,691</td>
<td align="right">0.3%</td>
<td align="right">14,622,698</td>
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
<td align="right">1,508</td>
<td align="right">0.0%</td>
<td align="right">1,508</td>
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
<td align="right">136,812</td>
<td align="right">100.0%</td>
<td align="right">137,747</td>
<td align="right">100.0%</td>
<td align="right">0.7%</td>
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
<td align="right">64,633,198</td>
<td align="right">100.0%</td>
<td align="right">64,171,966</td>
<td align="right">100.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">253</td>
<td align="right">0.0%</td>
<td align="right">253</td>
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
<td align="right">2,395</td>
<td align="right">100.0%</td>
<td align="right">2,455</td>
<td align="right">100.0%</td>
<td align="right">2.5%</td>
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
<td align="right">128,816,907</td>
<td align="right">17.8%</td>
<td align="right">128,816,907</td>
<td align="right">17.8%</td>
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
<td align="right">593,288,705</td>
<td align="right">82.2%</td>
<td align="right">593,288,705</td>
<td align="right">82.2%</td>
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
<td align="right">651</td>
<td align="right">1.9%</td>
<td align="right">651</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,392</td>
<td align="right">98.1%</td>
<td align="right">34,392</td>
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
<td align="right">71.1%</td>
<td align="right">24,440</td>
<td align="right">71.1%</td>
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
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">732</td>
<td align="right">2.1%</td>
<td align="right">732</td>
<td align="right">2.1%</td>
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
<td align="right">70,982,590</td>
<td align="right">3.5%</td>
<td align="right">72,058,513</td>
<td align="right">3.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,849,883,034</td>
<td align="right">90.9%</td>
<td align="right">1,842,288,823</td>
<td align="right">90.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">114,574,486</td>
<td align="right">5.6%</td>
<td align="right">114,594,557</td>
<td align="right">5.6%</td>
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
<td align="right">51,299</td>
<td align="right">2.3%</td>
<td align="right">51,585</td>
<td align="right">2.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,201,890</td>
<td align="right">97.7%</td>
<td align="right">2,203,463</td>
<td align="right">97.7%</td>
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
<td align="left">property</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">1,619</td>
<td align="right">3.1%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,076</td>
<td align="right">46.9%</td>
<td align="right">24,476</td>
<td align="right">47.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,978</td>
<td align="right">9.7%</td>
<td align="right">4,924</td>
<td align="right">9.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,322</td>
<td align="right">10.4%</td>
<td align="right">5,298</td>
<td align="right">10.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,344</td>
<td align="right">6.5%</td>
<td align="right">3,354</td>
<td align="right">6.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">741</td>
<td align="right">1.4%</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">262,010</td>
<td align="right">510.8%</td>
<td align="right">262,398</td>
<td align="right">508.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.9%</td>
<td align="right">7,666</td>
<td align="right">14.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">810</td>
<td align="right">1.6%</td>
<td align="right">810</td>
<td align="right">1.6%</td>
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
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">361</td>
<td align="right">0.7%</td>
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
<td align="right">1,194,076</td>
<td align="right">100.0%</td>
<td align="right">1,194,078</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">149,441,546</td>
<td align="right">13.9%</td>
<td align="right">154,801,223</td>
<td align="right">14.4%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">922,239,138</td>
<td align="right">86.1%</td>
<td align="right">921,174,253</td>
<td align="right">85.6%</td>
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
<td align="left">Success</td>
<td align="right">2,074</td>
<td align="right">4.2%</td>
<td align="right">2,197</td>
<td align="right">4.3%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">47,689</td>
<td align="right">95.8%</td>
<td align="right">48,995</td>
<td align="right">95.7%</td>
<td align="right">2.7%</td>
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
<td align="right">501</td>
<td align="right">1.1%</td>
<td align="right">1,681</td>
<td align="right">3.4%</td>
<td align="right">235.5%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">156</td>
<td align="right">0.3%</td>
<td align="right">176</td>
<td align="right">0.4%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,905</td>
<td align="right">6.1%</td>
<td align="right">3,031</td>
<td align="right">6.2%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">11,232</td>
<td align="right">23.6%</td>
<td align="right">11,212</td>
<td align="right">22.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">36.3%</td>
<td align="right">17,323</td>
<td align="right">35.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">15,163</td>
<td align="right">31.8%</td>
<td align="right">15,163</td>
<td align="right">30.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.7%</td>
<td align="right">341</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.1%</td>
<td align="right">68</td>
<td align="right">0.1%</td>
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
<td align="right">120,753,714</td>
<td align="right">2.5%</td>
<td align="right">142,008,597</td>
<td align="right">3.0%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">62,111,026</td>
<td align="right">1.3%</td>
<td align="right">64,933,476</td>
<td align="right">1.4%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,574,234,113</td>
<td align="right">96.1%</td>
<td align="right">4,573,394,229</td>
<td align="right">95.7%</td>
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
<td align="right">414,304</td>
<td align="right">25.4%</td>
<td align="right">486,037</td>
<td align="right">27.6%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,220,017</td>
<td align="right">74.6%</td>
<td align="right">1,273,695</td>
<td align="right">72.4%</td>
<td align="right">4.4%</td>
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
<td align="right">8,975</td>
<td align="right">2.2%</td>
<td align="right">73,715</td>
<td align="right">15.2%</td>
<td align="right">721.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">6,365</td>
<td align="right">1.5%</td>
<td align="right">9,111</td>
<td align="right">1.9%</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,548</td>
<td align="right">3.0%</td>
<td align="right">13,326</td>
<td align="right">2.7%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">5,278</td>
<td align="right">1.3%</td>
<td align="right">5,457</td>
<td align="right">1.1%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,675</td>
<td align="right">3.8%</td>
<td align="right">15,961</td>
<td align="right">3.3%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">255,991</td>
<td align="right">61.8%</td>
<td align="right">258,816</td>
<td align="right">53.3%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">95,897</td>
<td align="right">23.1%</td>
<td align="right">96,063</td>
<td align="right">19.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,689</td>
<td align="right">2.8%</td>
<td align="right">11,702</td>
<td align="right">2.4%</td>
<td align="right">0.1%</td>
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
<td align="right">1,237,520,864</td>
<td align="right">99.9%</td>
<td align="right">1,246,818,253</td>
<td align="right">99.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,427,493</td>
<td align="right">0.1%</td>
<td align="right">1,427,423</td>
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
<td align="left">Success</td>
<td align="right">11,581</td>
<td align="right">93.1%</td>
<td align="right">11,541</td>
<td align="right">93.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">861</td>
<td align="right">6.9%</td>
<td align="right">859</td>
<td align="right">6.9%</td>
<td align="right">-0.2%</td>
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
<td align="right">634</td>
<td align="right">73.6%</td>
<td align="right">632</td>
<td align="right">73.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.8%</td>
<td align="right">136</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">10.6%</td>
<td align="right">91</td>
<td align="right">10.6%</td>
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
<td align="right">2,547,426,406</td>
<td align="right">2.6%</td>
<td align="right">2,984,931,254</td>
<td align="right">2.8%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">39,997,577,044</td>
<td align="right">40.3%</td>
<td align="right">42,859,584,093</td>
<td align="right">40.4%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">55,483,900,901</td>
<td align="right">55.9%</td>
<td align="right">59,053,841,539</td>
<td align="right">55.6%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,220,945,891</td>
<td align="right">1.2%</td>
<td align="right">1,236,712,919</td>
<td align="right">1.2%</td>
<td align="right">1.3%</td>
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
<td align="left">BINARY_SUBSCR</td>
<td align="right">526,082,724</td>
<td align="right">19.6%</td>
<td align="right">742,932,413</td>
<td align="right">23.8%</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">453,186,284</td>
<td align="right">16.9%</td>
<td align="right">547,735,235</td>
<td align="right">17.6%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">203,255,734</td>
<td align="right">7.6%</td>
<td align="right">244,646,116</td>
<td align="right">7.8%</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">120,753,714</td>
<td align="right">4.5%</td>
<td align="right">142,008,597</td>
<td align="right">4.6%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">121,542,383</td>
<td align="right">4.5%</td>
<td align="right">140,044,909</td>
<td align="right">4.5%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">149,441,546</td>
<td align="right">5.6%</td>
<td align="right">154,801,223</td>
<td align="right">5.0%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">572,614,054</td>
<td align="right">21.4%</td>
<td align="right">585,931,767</td>
<td align="right">18.8%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">137,312,457</td>
<td align="right">5.1%</td>
<td align="right">135,265,991</td>
<td align="right">4.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">108,445,803</td>
<td align="right">4.0%</td>
<td align="right">108,232,385</td>
<td align="right">3.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,907</td>
<td align="right">4.8%</td>
<td align="right">128,816,907</td>
<td align="right">4.1%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">82,181,509</td>
<td align="right">6.7%</td>
<td align="right">88,085,724</td>
<td align="right">7.1%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">80,871,299</td>
<td align="right">6.6%</td>
<td align="right">85,132,116</td>
<td align="right">6.9%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">26,371,536</td>
<td align="right">2.2%</td>
<td align="right">27,603,866</td>
<td align="right">2.2%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">29,138,169</td>
<td align="right">2.4%</td>
<td align="right">30,051,262</td>
<td align="right">2.4%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">243,316,842</td>
<td align="right">19.9%</td>
<td align="right">245,834,224</td>
<td align="right">19.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">69,579,856</td>
<td align="right">5.7%</td>
<td align="right">68,862,852</td>
<td align="right">5.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">326,623,835</td>
<td align="right">26.7%</td>
<td align="right">328,996,356</td>
<td align="right">26.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">27,695,978</td>
<td align="right">2.3%</td>
<td align="right">27,720,912</td>
<td align="right">2.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">27,751,294</td>
<td align="right">2.3%</td>
<td align="right">27,742,372</td>
<td align="right">2.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">92,936,375</td>
<td align="right">7.6%</td>
<td align="right">92,958,396</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
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
<td align="right">3,558,377</td>
<td align="right">0.1%</td>
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">674,387,078</td>
<td align="right">10.0%</td>
<td align="right">678,918,394</td>
<td align="right">10.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,630,216,912</td>
<td align="right">24.2%</td>
<td align="right">1,634,617,969</td>
<td align="right">24.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,630,216,912</td>
<td align="right">24.2%</td>
<td align="right">1,634,617,969</td>
<td align="right">24.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,100,831,459</td>
<td align="right">75.8%</td>
<td align="right">5,108,408,012</td>
<td align="right">75.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,478,969,893</td>
<td align="right">81.4%</td>
<td align="right">5,471,182,749</td>
<td align="right">81.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,589,056</td>
<td align="right">4.2%</td>
<td align="right">279,327,189</td>
<td align="right">4.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">952,267,561</td>
<td align="right">14.1%</td>
<td align="right">951,422,237</td>
<td align="right">14.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">955,829,834</td>
<td align="right">14.2%</td>
<td align="right">955,699,575</td>
<td align="right">14.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,414,897</td>
<td align="right">3.9%</td>
<td align="right">261,407,340</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,612</td>
<td align="right">0.4%</td>
<td align="right">24,922,396</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,792,074</td>
<td align="right">1.1%</td>
<td align="right">70,791,974</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,139</td>
<td align="right">2.0%</td>
<td align="right">132,513,139</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">8,095,603</td>
<td align="right"></td>
<td align="right">8,998,707</td>
<td align="right"></td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">66,634,922</td>
<td align="right"></td>
<td align="right">72,414,321</td>
<td align="right"></td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">59,346,837</td>
<td align="right"></td>
<td align="right">64,223,721</td>
<td align="right"></td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">11,968,277,598</td>
<td align="right">7.6%</td>
<td align="right">12,764,278,356</td>
<td align="right">8.1%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">67,406,259,925</td>
<td align="right">42.6%</td>
<td align="right">63,969,069,734</td>
<td align="right">40.7%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">43,303,401,314</td>
<td align="right">27.3%</td>
<td align="right">45,395,559,414</td>
<td align="right">28.9%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">75,179,953,765</td>
<td align="right">37.9%</td>
<td align="right">71,668,808,950</td>
<td align="right">36.5%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">52,584,976,878</td>
<td align="right">26.5%</td>
<td align="right">54,759,807,095</td>
<td align="right">27.9%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">19,935,688,076</td>
<td align="right">10.1%</td>
<td align="right">20,695,876,242</td>
<td align="right">10.5%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">50,624,071,998</td>
<td align="right">25.5%</td>
<td align="right">49,399,260,506</td>
<td align="right">25.1%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">35,728,029,045</td>
<td align="right">22.6%</td>
<td align="right">34,975,635,631</td>
<td align="right">22.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,721,784</td>
<td align="right"></td>
<td align="right">179,203,833</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,541,232</td>
<td align="right">0.4%</td>
<td align="right">71,430,337</td>
<td align="right">0.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,263,211,459</td>
<td align="right"></td>
<td align="right">2,261,179,180</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,682,919,374</td>
<td align="right"></td>
<td align="right">6,688,814,325</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,423,136</td>
<td align="right">0.0%</td>
<td align="right">6,418,678</td>
<td align="right">0.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,415,959,709</td>
<td align="right">67.1%</td>
<td align="right">12,422,797,598</td>
<td align="right">67.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,416,046,634</td>
<td align="right"></td>
<td align="right">12,422,879,239</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,015,350,052</td>
<td align="right">32.5%</td>
<td align="right">6,017,478,259</td>
<td align="right">32.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,093,314,420</td>
<td align="right">32.9%</td>
<td align="right">6,095,327,274</td>
<td align="right">32.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,903,051,377</td>
<td align="right"></td>
<td align="right">2,903,710,438</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,172</td>
<td align="right">2.5%</td>
<td align="right">4,444,172</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">434,416</td>
<td align="right">0.2%</td>
<td align="right">434,416</td>
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
<td align="right">364,890</td>
<td align="right">102,522,614</td>
<td align="right">9,572,820,902</td>
<td align="right">756,890,042</td>
<td align="right">766,170,679</td>
<td align="right">364,759</td>
<td align="right">102,449,566</td>
<td align="right">9,558,879,471</td>
<td align="right">757,243,822</td>
<td align="right">764,994,925</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,608,301,612</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,608,306,592</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">253,412</td>
<td align="right">57.1%</td>
<td align="right">47,605</td>
<td align="right">10.6%</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">4,768,448,356</td>
<td align="right"></td>
<td align="right">3,815,347,506</td>
<td align="right"></td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">38,982</td>
<td align="right">8.8%</td>
<td align="right">31,505</td>
<td align="right">7.0%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">823</td>
<td align="right">0.2%</td>
<td align="right">747</td>
<td align="right">0.2%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">226,921,178,134</td>
<td align="right">4,758.8%</td>
<td align="right">210,293,245,337</td>
<td align="right">5,511.8%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">691</td>
<td align="right">0.2%</td>
<td align="right">673</td>
<td align="right">0.1%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">212,722</td>
<td align="right">48.0%</td>
<td align="right">217,440</td>
<td align="right">48.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">150,908</td>
<td align="right">34.0%</td>
<td align="right">153,551</td>
<td align="right">34.1%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">443,522</td>
<td align="right"></td>
<td align="right">450,321</td>
<td align="right"></td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,161</td>
<td align="right">0.7%</td>
<td align="right">3,121</td>
<td align="right">0.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">220</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="right">280</td>
<td align="right">0.7%</td>
<td align="right">280</td>
<td align="right">0.9%</td>
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
<td align="right">33,808</td>
<td align="right">86.7%</td>
<td align="right">26,895</td>
<td align="right">85.4%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">38,982</td>
<td align="right"></td>
<td align="right">31,505</td>
<td align="right"></td>
<td align="right">-19.2%</td>
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
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">70,341,249</td>
<td align="right">18.1%</td>
<td align="right">55,576,380</td>
<td align="right">16.8%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">310,788,096</td>
<td align="right">80.0%</td>
<td align="right">263,335,936</td>
<td align="right">79.6%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">388,714,496</td>
<td align="right"></td>
<td align="right">330,625,024</td>
<td align="right"></td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">47,176,280</td>
<td align="right">12.1%</td>
<td align="right">40,638,952</td>
<td align="right">12.3%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">271,196,967</td>
<td align="right">69.8%</td>
<td align="right">234,409,692</td>
<td align="right">70.9%</td>
<td align="right">-13.6%</td>
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
<td align="left">8,701</td>
<td align="right">25.7%</td>
<td align="left">5,140</td>
<td align="right">19.1%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">11,291</td>
<td align="right">33.4%</td>
<td align="left">9,628</td>
<td align="right">35.8%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">9,932</td>
<td align="right">29.4%</td>
<td align="left">8,583</td>
<td align="right">31.9%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,658</td>
<td align="right">7.9%</td>
<td align="left">2,448</td>
<td align="right">9.1%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">938</td>
<td align="right">2.8%</td>
<td align="left">892</td>
<td align="right">3.3%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">288</td>
<td align="right">0.9%</td>
<td align="left">204</td>
<td align="right">0.8%</td>
<td align="right">-29.2%</td>
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
<td align="right">2,984</td>
<td align="right">7.7%</td>
<td align="right">1,012</td>
<td align="right">3.2%</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">3,364</td>
<td align="right">8.6%</td>
<td align="right">1,976</td>
<td align="right">6.3%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">11,813</td>
<td align="right">30.3%</td>
<td align="right">10,119</td>
<td align="right">32.1%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,220</td>
<td align="right">26.2%</td>
<td align="right">8,383</td>
<td align="right">26.6%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">6,371</td>
<td align="right">16.3%</td>
<td align="right">5,711</td>
<td align="right">18.1%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,500</td>
<td align="right">9.0%</td>
<td align="right">3,660</td>
<td align="right">11.6%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">648</td>
<td align="right">1.7%</td>
<td align="right">562</td>
<td align="right">1.8%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">82</td>
<td align="right">0.2%</td>
<td align="right">82</td>
<td align="right">0.3%</td>
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
<td align="right">1,139</td>
<td align="right">2.9%</td>
<td align="right">1,005</td>
<td align="right">3.2%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,796</td>
<td align="right">7.2%</td>
<td align="right">439</td>
<td align="right">1.4%</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">5,757</td>
<td align="right">14.8%</td>
<td align="right">4,499</td>
<td align="right">14.3%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">12,256</td>
<td align="right">31.4%</td>
<td align="right">10,688</td>
<td align="right">33.9%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,307</td>
<td align="right">21.3%</td>
<td align="right">7,006</td>
<td align="right">22.2%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,653</td>
<td align="right">6.8%</td>
<td align="right">2,488</td>
<td align="right">7.9%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">652</td>
<td align="right">1.7%</td>
<td align="right">606</td>
<td align="right">1.9%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">248</td>
<td align="right">0.6%</td>
<td align="right">164</td>
<td align="right">0.5%</td>
<td align="right">-33.9%</td>
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
<td align="left">_DELETE_SUBSCR</td>
<td align="right">76,782,406</td>
<td align="right">16,402</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,628,879</td>
<td align="right">143,314</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">10,631,286</td>
<td align="right">954,726</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,364,028</td>
<td align="right">261,631</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">37,790,915</td>
<td align="right">7,922,158</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">90,376,686</td>
<td align="right">19,636,186</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">168,346,636</td>
<td align="right">71,159,722</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">15,713,653</td>
<td align="right">7,251,947</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">1,760</td>
<td align="right">2,640</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">481,984,963</td>
<td align="right">250,514,530</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">10,105,170</td>
<td align="right">5,291,779</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">726,696,775</td>
<td align="right">422,741,666</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">456,877,955</td>
<td align="right">273,433,568</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">486,827,631</td>
<td align="right">307,778,971</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">11,771,317</td>
<td align="right">7,596,068</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">59,924,063</td>
<td align="right">40,930,143</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">83,352,667</td>
<td align="right">57,738,052</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">6,122,956</td>
<td align="right">4,463,596</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,150,728</td>
<td align="right">4,508,518</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">362,099,118</td>
<td align="right">267,095,744</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">718,346,905</td>
<td align="right">532,445,832</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">728,044,148</td>
<td align="right">548,796,668</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">20,481,951</td>
<td align="right">15,671,261</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">20,506,777</td>
<td align="right">15,693,399</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,430,817,412</td>
<td align="right">1,099,439,362</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,515,796,837</td>
<td align="right">1,166,635,348</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,874,647</td>
<td align="right">3,521,807</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,757,752,799</td>
<td align="right">3,805,394,620</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,768,448,356</td>
<td align="right">3,815,347,506</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,226,051,716</td>
<td align="right">1,818,291,686</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">665,614</td>
<td align="right">543,862</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,808,219,910</td>
<td align="right">1,478,239,213</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">62,304,645</td>
<td align="right">51,484,013</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,935,657,835</td>
<td align="right">1,605,178,138</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,600,682,092</td>
<td align="right">1,328,951,130</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">1,124,571</td>
<td align="right">940,376</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">145,574,262</td>
<td align="right">124,181,421</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">4,537,154,305</td>
<td align="right">3,875,317,234</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">34,097,163</td>
<td align="right">29,313,009</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">7,188,168,528</td>
<td align="right">6,239,197,028</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">41,184,875</td>
<td align="right">35,995,386</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">309,852,971</td>
<td align="right">270,825,893</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,830,604,403</td>
<td align="right">1,611,076,073</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">700,249,440</td>
<td align="right">623,592,474</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">440,077,664</td>
<td align="right">392,819,209</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">49,166,389</td>
<td align="right">43,887,786</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">935,276,115</td>
<td align="right">836,430,015</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">185,187,886</td>
<td align="right">165,678,303</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,352,800,196</td>
<td align="right">7,506,472,122</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,985,311</td>
<td align="right">5,386,108</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">182,405,879</td>
<td align="right">164,754,276</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">466,787,522</td>
<td align="right">425,642,502</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">466,787,522</td>
<td align="right">425,642,502</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,032,817,794</td>
<td align="right">942,240,377</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,032,834,200</td>
<td align="right">942,256,806</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">7,693,982,732</td>
<td align="right">7,020,022,759</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">163,474,031</td>
<td align="right">149,317,217</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">8,831,844</td>
<td align="right">8,067,811</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">275,451,599</td>
<td align="right">252,057,508</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">43,946,994</td>
<td align="right">40,229,849</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,798,234,217</td>
<td align="right">4,398,272,741</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">600,261,143</td>
<td align="right">550,309,834</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">441,436,197</td>
<td align="right">405,348,183</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">382,478,861</td>
<td align="right">351,356,452</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,298,082,651</td>
<td align="right">1,193,491,293</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">91,028,595</td>
<td align="right">83,955,439</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,028,595</td>
<td align="right">83,955,439</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">91,245,487</td>
<td align="right">84,156,879</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">23,700,061,080</td>
<td align="right">21,927,107,809</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,804,137,324</td>
<td align="right">1,670,071,557</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">333,140,689</td>
<td align="right">309,145,188</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,991,854,616</td>
<td align="right">2,778,953,210</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">10,695,294</td>
<td align="right">9,952,623</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">794,579,699</td>
<td align="right">741,046,789</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">293,392,172</td>
<td align="right">273,688,351</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">293,608,232</td>
<td align="right">273,904,411</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">27,730,283,585</td>
<td align="right">25,921,945,309</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">47,301,507</td>
<td align="right">44,340,997</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">4,146,097,270</td>
<td align="right">3,892,758,862</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,865,949,808</td>
<td align="right">2,691,243,824</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,937,147,545</td>
<td align="right">2,766,471,857</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">46,893,820</td>
<td align="right">44,407,420</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">46,893,820</td>
<td align="right">44,407,420</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">5,700,187</td>
<td align="right">5,406,978</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">72,455,099</td>
<td align="right">68,856,866</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">61,690,612</td>
<td align="right">58,771,613</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">8,432,458,089</td>
<td align="right">8,069,888,860</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,893,386,602</td>
<td align="right">3,726,026,650</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">215,478,490</td>
<td align="right">206,587,871</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">2,075,564</td>
<td align="right">2,159,367</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,338,068,180</td>
<td align="right">2,243,857,022</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">3,657,004,595</td>
<td align="right">3,524,597,494</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">57,671,545</td>
<td align="right">55,640,935</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">58,488,025</td>
<td align="right">56,457,415</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">761,069,810</td>
<td align="right">735,336,605</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">188,262,283</td>
<td align="right">182,049,291</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,826,690,600</td>
<td align="right">2,734,936,771</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">719,550,329</td>
<td align="right">696,604,789</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">24,864,963</td>
<td align="right">24,072,518</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">24,864,963</td>
<td align="right">24,072,518</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,307,801,290</td>
<td align="right">1,268,555,199</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">165,192,785</td>
<td align="right">160,427,225</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">234,633,747</td>
<td align="right">228,203,530</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">501,448,941</td>
<td align="right">487,978,786</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">524,883,979</td>
<td align="right">510,795,122</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">194,626,038</td>
<td align="right">189,900,157</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,513,985,974</td>
<td align="right">1,477,962,995</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,986,705,142</td>
<td align="right">3,894,317,604</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">985,891,177</td>
<td align="right">965,097,625</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">985,891,177</td>
<td align="right">965,097,625</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">278,354</td>
<td align="right">283,793</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,709,925,374</td>
<td align="right">2,659,413,821</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">924,677,445</td>
<td align="right">908,225,463</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">46,527,226</td>
<td align="right">45,735,257</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,086,946,475</td>
<td align="right">1,068,843,879</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">753,135,919</td>
<td align="right">740,931,350</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">753,334,539</td>
<td align="right">741,138,110</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,185,950,802</td>
<td align="right">1,167,419,245</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,586,284,306</td>
<td align="right">3,531,841,838</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">265,946,741</td>
<td align="right">261,992,140</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">578,689,345</td>
<td align="right">570,178,860</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">458,757,693</td>
<td align="right">452,068,697</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,417,485,998</td>
<td align="right">4,353,470,255</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">566,949</td>
<td align="right">558,864</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">566,949</td>
<td align="right">558,864</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">459,854,134</td>
<td align="right">453,376,536</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">870,507,151</td>
<td align="right">858,859,999</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">705,834,412</td>
<td align="right">696,590,353</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,768,941,841</td>
<td align="right">1,745,912,365</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,400,820,772</td>
<td align="right">4,346,012,129</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">944,536,781</td>
<td align="right">933,169,905</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,694,491,342</td>
<td align="right">1,675,724,832</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">63,817,911</td>
<td align="right">63,144,762</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">63,817,911</td>
<td align="right">63,144,762</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">474,322,246</td>
<td align="right">469,498,669</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">551,384,488</td>
<td align="right">546,024,742</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">60,483,284</td>
<td align="right">59,919,494</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">498,588,288</td>
<td align="right">494,163,539</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,074,792,340</td>
<td align="right">1,065,392,677</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">70,230,470</td>
<td align="right">69,629,859</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">41,077,716</td>
<td align="right">41,386,136</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">3,992,429,325</td>
<td align="right">3,963,747,151</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">371,228,631</td>
<td align="right">368,785,312</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">501,708,644</td>
<td align="right">498,487,330</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">682,097,629</td>
<td align="right">678,019,525</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">1,319,687</td>
<td align="right">1,326,740</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">138,719,287</td>
<td align="right">139,452,050</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,241,868,613</td>
<td align="right">2,231,622,095</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,714,904,178</td>
<td align="right">1,708,033,413</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">50,176,180</td>
<td align="right">50,375,000</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">230,384,990</td>
<td align="right">229,631,480</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,955,150,168</td>
<td align="right">3,942,695,147</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">21,543,837</td>
<td align="right">21,608,423</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,167,773</td>
<td align="right">1,171,126</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">815,681,600</td>
<td align="right">813,852,637</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">987,066,709</td>
<td align="right">985,287,829</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,419,720,172</td>
<td align="right">2,423,849,522</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">167,487,511</td>
<td align="right">167,764,798</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,009,764,022</td>
<td align="right">1,008,150,061</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">165,651,672</td>
<td align="right">165,902,480</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">119,351,973</td>
<td align="right">119,191,899</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,188,143,590</td>
<td align="right">1,186,573,411</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">140,137,134</td>
<td align="right">140,295,423</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">409,989,425</td>
<td align="right">409,553,786</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">508,330,275</td>
<td align="right">507,798,338</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">98,330,997</td>
<td align="right">98,412,957</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">343,435,550</td>
<td align="right">343,160,148</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">221,809,886</td>
<td align="right">221,635,802</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,347,189,351</td>
<td align="right">1,346,390,638</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,398,736</td>
<td align="right">1,397,955</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">9,750,994</td>
<td align="right">9,745,617</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">9,750,994</td>
<td align="right">9,745,617</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">15,704,991</td>
<td align="right">15,696,505</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">12,454,274</td>
<td align="right">12,448,897</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">162,692,988</td>
<td align="right">162,744,989</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,739,133</td>
<td align="right">40,741,843</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">78,197,254</td>
<td align="right">78,196,510</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">78,965,038</td>
<td align="right">78,964,294</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,313</td>
<td align="right">70,350,484</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,313</td>
<td align="right">70,350,484</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">39,798,841</td>
<td align="right">39,798,879</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">101,559,430</td>
<td align="right">101,559,490</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">409,331,650</td>
<td align="right">409,331,650</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">329,788,034</td>
<td align="right">329,788,034</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">254,690,388</td>
<td align="right">254,690,388</td>
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
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,013,180</td>
<td align="right">60,013,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,063,339</td>
<td align="right">47,063,339</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">40,775,190</td>
<td align="right">40,775,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">8,067,811</td>
<td align="right">8,067,811</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,137,792</td>
<td align="right">6,137,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,976,000</td>
<td align="right">2,976,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,976,000</td>
<td align="right">2,976,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">2,703,280</td>
<td align="right">2,703,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">764,033</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">764,033</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">127,444</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">27,762</td>
<td align="right">27,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">263</td>
<td align="right">263</td>
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
<td align="left">CALL</td>
<td align="right">2,462</td>
<td align="right">2,086</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">24,023</td>
<td align="right">23,853</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right">23,001</td>
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
<td align="right">120</td>
<td align="right">120</td>
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
<td align="right">120</td>
<td align="right">120</td>
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
<td align="right">2,476</td>
<td align="right">2,476</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-08
