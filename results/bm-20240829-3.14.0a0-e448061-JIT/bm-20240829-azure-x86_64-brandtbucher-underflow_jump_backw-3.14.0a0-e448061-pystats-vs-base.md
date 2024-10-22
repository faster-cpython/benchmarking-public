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
<td align="right">402,564,525</td>
<td align="right">196,144</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">338,864,978</td>
<td align="right">774,774</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,288</td>
<td align="right">8,948</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">331,693,283</td>
<td align="right">876,003</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,142,793</td>
<td align="right">234,513</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">60,308,098</td>
<td align="right">174,479</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">275,147,318</td>
<td align="right">1,409,177</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,053,113,336</td>
<td align="right">6,345,482</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">107,218,522</td>
<td align="right">891,677</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">62,053,943</td>
<td align="right">521,935</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,461,963</td>
<td align="right">738,021</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">304,922,595</td>
<td align="right">2,904,571</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,744,106</td>
<td align="right">40,950</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">71,261,716</td>
<td align="right">818,505</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">137,085,052</td>
<td align="right">1,855,092</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">298,283,270</td>
<td align="right">4,102,506</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,031,285,831</td>
<td align="right">16,435,402</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,603,414</td>
<td align="right">58,907</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,641</td>
<td align="right">1,561</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">43,448,680</td>
<td align="right">767,019</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">158,450,808</td>
<td align="right">2,832,271</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,479,810</td>
<td align="right">2,883,654</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">44,067,851</td>
<td align="right">978,073</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,088,467</td>
<td align="right">495,405</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">33,173,255</td>
<td align="right">856,385</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,521,763</td>
<td align="right">203,103</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,419,552</td>
<td align="right">47,727</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,340,743</td>
<td align="right">394,523</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">221,400,401</td>
<td align="right">8,836,759</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">65,676,271</td>
<td align="right">2,914,287</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">260,960,041</td>
<td align="right">12,111,050</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,893,250</td>
<td align="right">136,636</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">36,478,010</td>
<td align="right">1,761,012</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,614,254,290</td>
<td align="right">136,530,196</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">528,859,441</td>
<td align="right">28,505,593</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">53,710,832</td>
<td align="right">3,029,814</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">735,481,162</td>
<td align="right">42,995,308</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">457,084,498</td>
<td align="right">26,979,298</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,411,926,233</td>
<td align="right">152,490,465</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">187,856,852</td>
<td align="right">12,610,043</td>
<td align="right">-93.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">91,866,985</td>
<td align="right">6,320,656</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,643,979,302</td>
<td align="right">254,002,504</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,477,730</td>
<td align="right">325,150</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">207,686,382</td>
<td align="right">15,421,171</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">370,559,846</td>
<td align="right">27,854,135</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">763,776</td>
<td align="right">57,791</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">120,124,718</td>
<td align="right">9,650,810</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">99,173,424</td>
<td align="right">8,011,585</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">720,751</td>
<td align="right">58,670</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">120,698,504</td>
<td align="right">10,360,097</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">108,046,843</td>
<td align="right">9,390,472</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">56,641,245</td>
<td align="right">5,043,615</td>
<td align="right">-91.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">733,649,077</td>
<td align="right">67,989,925</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,636,240,538</td>
<td align="right">152,702,510</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">226,426,021</td>
<td align="right">21,670,359</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,323,663</td>
<td align="right">9,965,492</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">556,842,266</td>
<td align="right">53,879,104</td>
<td align="right">-90.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">332,686,658</td>
<td align="right">33,264,674</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">33,835,153</td>
<td align="right">3,433,667</td>
<td align="right">-89.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">103,158,635</td>
<td align="right">10,473,823</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">93,340,658</td>
<td align="right">9,538,245</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">190,830,471</td>
<td align="right">19,556,070</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">522,935,351</td>
<td align="right">54,630,821</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">562,528,781</td>
<td align="right">62,112,363</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">154,270,242</td>
<td align="right">17,319,345</td>
<td align="right">-88.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">525,480,978</td>
<td align="right">60,479,221</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">78,591,655</td>
<td align="right">9,155,715</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,777,894,577</td>
<td align="right">449,796,918</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,034,244</td>
<td align="right">4,401,166</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">90,973,084</td>
<td align="right">11,498,682</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">135,281,115</td>
<td align="right">17,260,754</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">8,530,886</td>
<td align="right">1,088,534</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">365,127,701</td>
<td align="right">48,295,864</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,258,213</td>
<td align="right">1,521,271</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">430,189,182</td>
<td align="right">58,454,075</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,334,424,505</td>
<td align="right">603,711,260</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">340,692,953</td>
<td align="right">47,710,539</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,422,676</td>
<td align="right">1,478,347</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">197,213,586</td>
<td align="right">28,307,094</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,826,826,040</td>
<td align="right">262,904,408</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">392,395,523</td>
<td align="right">58,053,398</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">153,076,055</td>
<td align="right">23,601,854</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,082,879</td>
<td align="right">28,139,226</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">806,281,916</td>
<td align="right">125,984,075</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">14,953,270</td>
<td align="right">2,407,142</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">182,862,020</td>
<td align="right">30,141,092</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">50,028,630</td>
<td align="right">8,446,912</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">52,704,415</td>
<td align="right">9,024,046</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">255,207,852</td>
<td align="right">43,902,205</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,732,605</td>
<td align="right">1,503,824</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">56,050,360</td>
<td align="right">10,295,712</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,166,081</td>
<td align="right">49,406,175</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,596,128,128</td>
<td align="right">897,743,338</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">355,320,855</td>
<td align="right">71,476,439</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,592,928,677</td>
<td align="right">3,162,621,287</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">150,193,462</td>
<td align="right">31,267,119</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">220,106,779</td>
<td align="right">45,931,535</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">251,207,037</td>
<td align="right">52,901,254</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,558,824</td>
<td align="right">12,186,654</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,973,118,292</td>
<td align="right">423,994,785</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,945,743</td>
<td align="right">5,253,781</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">100,288,460</td>
<td align="right">21,730,614</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">197,308,884</td>
<td align="right">43,443,654</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">27,478,592</td>
<td align="right">6,088,272</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,251,014</td>
<td align="right">65,899,562</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,806</td>
<td align="right">6,526</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,470</td>
<td align="right">41,318</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">203,724,397</td>
<td align="right">49,111,790</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,445,404</td>
<td align="right">11,647,311</td>
<td align="right">-75.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">178,551,511</td>
<td align="right">44,214,475</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">88,069,983</td>
<td align="right">22,218,110</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,016,371</td>
<td align="right">31,358,247</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,348,190,925</td>
<td align="right">342,769,094</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,706,676,774</td>
<td align="right">964,107,752</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">238,807,069</td>
<td align="right">64,664,814</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">85,127,967</td>
<td align="right">24,824,227</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,037,959</td>
<td align="right">2,754,269</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">474,369,545</td>
<td align="right">146,992,349</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">52,159,512</td>
<td align="right">16,936,201</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">348,929,787</td>
<td align="right">121,672,355</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,215,258,838</td>
<td align="right">780,564,535</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">189,687,578</td>
<td align="right">67,968,693</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,629,760,470</td>
<td align="right">1,663,456,610</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,104,162</td>
<td align="right">148,997,005</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">58,873,294</td>
<td align="right">22,037,054</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">224,007</td>
<td align="right">86,902</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">822,173,045</td>
<td align="right">321,497,489</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">16,246,056</td>
<td align="right">6,553,936</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">64,986,063</td>
<td align="right">26,952,019</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">920</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">40,340</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,995,982</td>
<td align="right">5,561,611</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">618,272,599</td>
<td align="right">316,173,944</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">551,620</td>
<td align="right">292,960</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">74,062,926</td>
<td align="right">39,837,877</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,430,073,494</td>
<td align="right">3,493,757,734</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">36,668,601</td>
<td align="right">20,864,327</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,859,343,325</td>
<td align="right">1,641,278,549</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,372,096,510</td>
<td align="right">790,440,097</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">44,848,991</td>
<td align="right">26,573,186</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">170,740,817</td>
<td align="right">103,743,893</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">525,287</td>
<td align="right">349,583</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">951,446,591</td>
<td align="right">664,601,395</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">141,987,269</td>
<td align="right">100,546,811</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,489,413</td>
<td align="right">50,961,898</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,417,344</td>
<td align="right">67,705,034</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">134,320,418</td>
<td align="right">98,190,950</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">53,177,386</td>
<td align="right">40,312,516</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">27,949,499</td>
<td align="right">21,629,726</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,768,286</td>
<td align="right">14,709,272</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,210,011</td>
<td align="right">10,987,140</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">147,000,844</td>
<td align="right">126,889,983</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">276,932,946</td>
<td align="right">314,323,331</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,856</td>
<td align="right">19,296</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">43,628,260</td>
<td align="right">39,577,468</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">410,179,948</td>
<td align="right">385,022,276</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,062</td>
<td align="right">1,122</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,387,074</td>
<td align="right">20,188,355</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">58,580</td>
<td align="right">55,653</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">102,115,621</td>
<td align="right">98,539,203</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">651,872</td>
<td align="right">637,892</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">29,709</td>
<td align="right">29,089</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,407,121</td>
<td align="right">196,740,649</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,259,182,194</td>
<td align="right">2,244,956,087</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">268,685</td>
<td align="right">268,231</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,259,182</td>
<td align="right">1,257,979</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">70,944,737</td>
<td align="right">70,922,130</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,167</td>
<td align="right">15,170</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,586,959</td>
<td align="right">3,586,505</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">66,760</td>
<td align="right">66,766</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,395,415</td>
<td align="right">21,394,421</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,081,104</td>
<td align="right">21,080,312</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,353,558</td>
<td align="right">20,352,928</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,830,247</td>
<td align="right">5,830,311</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,399,214</td>
<td align="right">173,400,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">77,693,920</td>
<td align="right">77,693,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,240</td>
<td align="right">38,846,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,680</td>
<td align="right">38,845,680</td>
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
<td align="left">CLEANUP_THROW</td>
<td align="right">157,711</td>
<td align="right">157,711</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16,120</td>
<td align="right">16,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">423</td>
<td align="right">423</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">241</td>
<td align="right">241</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">140</td>
<td align="right">140</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">369,401,569</td>
<td align="right">3.8%</td>
<td align="right">27,434,511</td>
<td align="right">0.3%</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,480,870</td>
<td align="right">0.3%</td>
<td align="right">10,218,271</td>
<td align="right">0.1%</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,403,446,726</td>
<td align="right">95.9%</td>
<td align="right">9,391,788,415</td>
<td align="right">99.6%</td>
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
<td align="left">Failure</td>
<td align="right">1,116,292</td>
<td align="right">65.1%</td>
<td align="right">377,809</td>
<td align="right">61.7%</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">598,065</td>
<td align="right">34.9%</td>
<td align="right">234,535</td>
<td align="right">38.3%</td>
<td align="right">-60.8%</td>
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
<td align="left">multiply different types</td>
<td align="right">81,923</td>
<td align="right">7.3%</td>
<td align="right">184,034</td>
<td align="right">48.7%</td>
<td align="right">124.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,608</td>
<td align="right">70.0%</td>
<td align="right">1,809</td>
<td align="right">0.5%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">31,310</td>
<td align="right">2.8%</td>
<td align="right">4,971</td>
<td align="right">1.3%</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">49,299</td>
<td align="right">4.4%</td>
<td align="right">88,339</td>
<td align="right">23.4%</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">8,249</td>
<td align="right">0.7%</td>
<td align="right">2,134</td>
<td align="right">0.6%</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,805</td>
<td align="right">1.0%</td>
<td align="right">4,176</td>
<td align="right">1.1%</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,742</td>
<td align="right">0.9%</td>
<td align="right">3,829</td>
<td align="right">1.0%</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">6,805</td>
<td align="right">0.6%</td>
<td align="right">2,866</td>
<td align="right">0.8%</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">401</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">47,061</td>
<td align="right">4.2%</td>
<td align="right">23,717</td>
<td align="right">6.3%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,620</td>
<td align="right">0.5%</td>
<td align="right">3,007</td>
<td align="right">0.8%</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,395</td>
<td align="right">1.3%</td>
<td align="right">7,917</td>
<td align="right">2.1%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,272</td>
<td align="right">2.8%</td>
<td align="right">19,876</td>
<td align="right">5.3%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,830</td>
<td align="right">0.3%</td>
<td align="right">3,611</td>
<td align="right">1.0%</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">20,124</td>
<td align="right">1.8%</td>
<td align="right">15,485</td>
<td align="right">4.1%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,471</td>
<td align="right">0.8%</td>
<td align="right">6,605</td>
<td align="right">1.7%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,963</td>
<td align="right">0.3%</td>
<td align="right">2,343</td>
<td align="right">0.6%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,580</td>
<td align="right">0.2%</td>
<td align="right">2,058</td>
<td align="right">0.5%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">834</td>
<td align="right">0.1%</td>
<td align="right">832</td>
<td align="right">0.2%</td>
<td align="right">-0.2%</td>
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
<td align="right">474,099,725</td>
<td align="right">7.1%</td>
<td align="right">146,816,856</td>
<td align="right">2.3%</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,792,351</td>
<td align="right">0.1%</td>
<td align="right">4,727,527</td>
<td align="right">0.1%</td>
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
<td align="right">6,201,993,890</td>
<td align="right">92.8%</td>
<td align="right">6,182,043,461</td>
<td align="right">97.6%</td>
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
<td align="right">178,219</td>
<td align="right">49.5%</td>
<td align="right">84,088</td>
<td align="right">31.8%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,562</td>
<td align="right">50.5%</td>
<td align="right">180,179</td>
<td align="right">68.2%</td>
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
<td align="left">array int</td>
<td align="right">26,640</td>
<td align="right">14.9%</td>
<td align="right">3,320</td>
<td align="right">3.9%</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">220</td>
<td align="right">0.3%</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,330</td>
<td align="right">12.0%</td>
<td align="right">7,093</td>
<td align="right">8.4%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">58,326</td>
<td align="right">32.7%</td>
<td align="right">25,205</td>
<td align="right">30.0%</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">940</td>
<td align="right">0.5%</td>
<td align="right">600</td>
<td align="right">0.7%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">65,338</td>
<td align="right">36.7%</td>
<td align="right">42,944</td>
<td align="right">51.1%</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">320</td>
<td align="right">0.2%</td>
<td align="right">220</td>
<td align="right">0.3%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">125</td>
<td align="right">0.1%</td>
<td align="right">86</td>
<td align="right">0.1%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">2.4%</td>
<td align="right">4,300</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
<td align="right">32,060</td>
<td align="right">0.0%</td>
<td align="right">22,260</td>
<td align="right">0.0%</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">150,934,445</td>
<td align="right">1.1%</td>
<td align="right">115,554,330</td>
<td align="right">0.9%</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,498,584,766</td>
<td align="right">98.9%</td>
<td align="right">13,466,749,097</td>
<td align="right">99.1%</td>
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
<td align="right">716,679</td>
<td align="right">0.0%</td>
<td align="right">715,430</td>
<td align="right">0.0%</td>
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
<td align="left">Success</td>
<td align="right">3,422,578</td>
<td align="right">100.0%</td>
<td align="right">2,750,083</td>
<td align="right">100.0%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">363</td>
<td align="right">0.0%</td>
<td align="right">363</td>
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
<td align="left">init not inline values</td>
<td align="right">2,829</td>
<td align="right">779.3%</td>
<td align="right">2,829</td>
<td align="right">779.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,003</td>
<td align="right">551.8%</td>
<td align="right">2,003</td>
<td align="right">551.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">921</td>
<td align="right">253.7%</td>
<td align="right">921</td>
<td align="right">253.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">363</td>
<td align="right">100.0%</td>
<td align="right">363</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">435,240</td>
<td align="right">86.7%</td>
<td align="right">126,880</td>
<td align="right">65.5%</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,415</td>
<td align="right">7.3%</td>
<td align="right">36,417</td>
<td align="right">18.8%</td>
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
<td align="right">103,107,638</td>
<td align="right">1.8%</td>
<td align="right">9,841,589</td>
<td align="right">0.2%</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,249,139</td>
<td align="right">0.0%</td>
<td align="right">173,454</td>
<td align="right">0.0%</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,722,094,276</td>
<td align="right">98.2%</td>
<td align="right">5,711,517,573</td>
<td align="right">99.8%</td>
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
<td align="right">160,993</td>
<td align="right">67.3%</td>
<td align="right">69,460</td>
<td align="right">54.7%</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">78,249</td>
<td align="right">32.7%</td>
<td align="right">57,510</td>
<td align="right">45.3%</td>
<td align="right">-26.5%</td>
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
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">6.6%</td>
<td align="right">1,600</td>
<td align="right">2.3%</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,524</td>
<td align="right">9.0%</td>
<td align="right">3,194</td>
<td align="right">4.6%</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">29,783</td>
<td align="right">18.5%</td>
<td align="right">6,858</td>
<td align="right">9.9%</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,189</td>
<td align="right">11.9%</td>
<td align="right">8,790</td>
<td align="right">12.7%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,060</td>
<td align="right">1.9%</td>
<td align="right">1,420</td>
<td align="right">2.0%</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">48,512</td>
<td align="right">30.1%</td>
<td align="right">24,629</td>
<td align="right">35.5%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,086</td>
<td align="right">7.5%</td>
<td align="right">6,651</td>
<td align="right">9.6%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,720</td>
<td align="right">1.7%</td>
<td align="right">1,580</td>
<td align="right">2.3%</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,439</td>
<td align="right">10.8%</td>
<td align="right">12,001</td>
<td align="right">17.3%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,550</td>
<td align="right">1.0%</td>
<td align="right">1,227</td>
<td align="right">1.8%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">1,060</td>
<td align="right">1.5%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">490</td>
<td align="right">0.3%</td>
<td align="right">450</td>
<td align="right">0.6%</td>
<td align="right">-8.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,546,180</td>
<td align="right">0.1%</td>
<td align="right">40,940</td>
<td align="right">0.0%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,584,086</td>
<td align="right">1.4%</td>
<td align="right">20,802,779</td>
<td align="right">0.8%</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,486,718,666</td>
<td align="right">98.4%</td>
<td align="right">2,433,792,901</td>
<td align="right">99.1%</td>
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
<td align="left">Success</td>
<td align="right">61,139</td>
<td align="right">46.2%</td>
<td align="right">13,859</td>
<td align="right">22.2%</td>
<td align="right">-77.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">71,336</td>
<td align="right">53.8%</td>
<td align="right">48,429</td>
<td align="right">77.8%</td>
<td align="right">-32.1%</td>
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
<td align="right">27,578</td>
<td align="right">38.7%</td>
<td align="right">17,409</td>
<td align="right">35.9%</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,470</td>
<td align="right">20.3%</td>
<td align="right">9,529</td>
<td align="right">19.7%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">13,982</td>
<td align="right">19.6%</td>
<td align="right">9,381</td>
<td align="right">19.4%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,306</td>
<td align="right">21.5%</td>
<td align="right">12,110</td>
<td align="right">25.0%</td>
<td align="right">-20.9%</td>
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
<td align="right">73,913,641</td>
<td align="right">12.0%</td>
<td align="right">39,709,203</td>
<td align="right">11.1%</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">534,037,689</td>
<td align="right">86.9%</td>
<td align="right">313,795,086</td>
<td align="right">87.6%</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,746,723</td>
<td align="right">1.1%</td>
<td align="right">4,725,699</td>
<td align="right">1.3%</td>
<td align="right">-30.0%</td>
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
<td align="right">175,722</td>
<td align="right">63.6%</td>
<td align="right">137,492</td>
<td align="right">63.2%</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">100,558</td>
<td align="right">36.4%</td>
<td align="right">80,140</td>
<td align="right">36.8%</td>
<td align="right">-20.3%</td>
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
<td align="left">ascii string</td>
<td align="right">2,467</td>
<td align="right">2.5%</td>
<td align="right">1,120</td>
<td align="right">1.4%</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,981</td>
<td align="right">4.0%</td>
<td align="right">5,700</td>
<td align="right">7.1%</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,602</td>
<td align="right">7.6%</td>
<td align="right">4,942</td>
<td align="right">6.2%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,565</td>
<td align="right">6.5%</td>
<td align="right">4,806</td>
<td align="right">6.0%</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">2,724</td>
<td align="right">2.7%</td>
<td align="right">2,004</td>
<td align="right">2.5%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,775</td>
<td align="right">36.6%</td>
<td align="right">27,795</td>
<td align="right">34.7%</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,071</td>
<td align="right">11.0%</td>
<td align="right">8,534</td>
<td align="right">10.6%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,222</td>
<td align="right">5.2%</td>
<td align="right">4,034</td>
<td align="right">5.0%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,956</td>
<td align="right">4.9%</td>
<td align="right">4,156</td>
<td align="right">5.2%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.3%</td>
<td align="right">240</td>
<td align="right">0.3%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">10,798</td>
<td align="right">10.7%</td>
<td align="right">9,259</td>
<td align="right">11.6%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,737</td>
<td align="right">6.7%</td>
<td align="right">6,229</td>
<td align="right">7.8%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">620</td>
<td align="right">0.6%</td>
<td align="right">581</td>
<td align="right">0.7%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">740</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">1,288,800</td>
<td align="right">0.0%</td>
<td align="right">99,340</td>
<td align="right">0.0%</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">558,709,619</td>
<td align="right">3.4%</td>
<td align="right">60,849,749</td>
<td align="right">0.4%</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">341,162,049</td>
<td align="right">2.1%</td>
<td align="right">163,143,157</td>
<td align="right">1.1%</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,374,610,351</td>
<td align="right">94.4%</td>
<td align="right">14,936,638,279</td>
<td align="right">98.5%</td>
<td align="right">-2.8%</td>
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
<td align="right">9,748,220</td>
<td align="right">95.4%</td>
<td align="right">4,046,717</td>
<td align="right">93.9%</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">473,308</td>
<td align="right">4.6%</td>
<td align="right">265,120</td>
<td align="right">6.1%</td>
<td align="right">-44.0%</td>
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
<td align="left">expected error</td>
<td align="right">5,300</td>
<td align="right">1.1%</td>
<td align="right">1,352</td>
<td align="right">0.5%</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,992</td>
<td align="right">3.8%</td>
<td align="right">7,828</td>
<td align="right">3.0%</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,964</td>
<td align="right">0.6%</td>
<td align="right">1,364</td>
<td align="right">0.5%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">88,006</td>
<td align="right">18.6%</td>
<td align="right">41,849</td>
<td align="right">15.8%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">32,253</td>
<td align="right">6.8%</td>
<td align="right">15,562</td>
<td align="right">5.9%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">84,351</td>
<td align="right">17.8%</td>
<td align="right">42,655</td>
<td align="right">16.1%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">62</td>
<td align="right">0.0%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">31,279</td>
<td align="right">6.6%</td>
<td align="right">16,706</td>
<td align="right">6.3%</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">20,880</td>
<td align="right">4.4%</td>
<td align="right">12,180</td>
<td align="right">4.6%</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">11,000</td>
<td align="right">2.3%</td>
<td align="right">6,460</td>
<td align="right">2.4%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,425</td>
<td align="right">1.1%</td>
<td align="right">3,239</td>
<td align="right">1.2%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">2,755</td>
<td align="right">0.6%</td>
<td align="right">1,792</td>
<td align="right">0.7%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">138,634</td>
<td align="right">29.3%</td>
<td align="right">90,625</td>
<td align="right">34.2%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.2%</td>
<td align="right">760</td>
<td align="right">0.3%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">15,331</td>
<td align="right">3.2%</td>
<td align="right">10,695</td>
<td align="right">4.0%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2,543</td>
<td align="right">0.5%</td>
<td align="right">1,856</td>
<td align="right">0.7%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
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
<td align="right">4,492,950,151</td>
<td align="right">99.5%</td>
<td align="right">565,788,720</td>
<td align="right">96.5%</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">394,374</td>
<td align="right">0.0%</td>
<td align="right">395,223</td>
<td align="right">0.1%</td>
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
<td align="right">19,893,761</td>
<td align="right">0.4%</td>
<td align="right">19,893,457</td>
<td align="right">3.4%</td>
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
<td align="right">9,236</td>
<td align="right">0.0%</td>
<td align="right">9,236</td>
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
<td align="right">465,604</td>
<td align="right">100.0%</td>
<td align="right">465,267</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">86,169,022</td>
<td align="right">100.0%</td>
<td align="right">84,849,207</td>
<td align="right">100.0%</td>
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
<td align="right">7,626</td>
<td align="right">0.0%</td>
<td align="right">7,629</td>
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
<td align="right">7,541</td>
<td align="right">100.0%</td>
<td align="right">7,541</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">30,643</td>
<td align="right">0.0%</td>
<td align="right">29,603</td>
<td align="right">0.0%</td>
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
<td align="right">173,334,483</td>
<td align="right">18.1%</td>
<td align="right">173,335,265</td>
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
<td align="right">786,232,550</td>
<td align="right">81.9%</td>
<td align="right">786,232,775</td>
<td align="right">81.9%</td>
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
<td align="right">5,557</td>
<td align="right">8.5%</td>
<td align="right">5,537</td>
<td align="right">8.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,734</td>
<td align="right">91.5%</td>
<td align="right">59,854</td>
<td align="right">91.5%</td>
<td align="right">0.2%</td>
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
<td align="right">10,020</td>
<td align="right">16.8%</td>
<td align="right">10,140</td>
<td align="right">16.9%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">55.5%</td>
<td align="right">33,180</td>
<td align="right">55.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,268</td>
<td align="right">23.9%</td>
<td align="right">14,268</td>
<td align="right">23.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
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
<td align="right">111,394,440</td>
<td align="right">4.3%</td>
<td align="right">24,034,695</td>
<td align="right">1.0%</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">44,667,152</td>
<td align="right">1.7%</td>
<td align="right">26,413,928</td>
<td align="right">1.1%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,463,383,025</td>
<td align="right">94.0%</td>
<td align="right">2,451,906,777</td>
<td align="right">98.0%</td>
<td align="right">-0.5%</td>
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
<td align="right">2,204,796</td>
<td align="right">96.7%</td>
<td align="right">557,250</td>
<td align="right">91.2%</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">76,051</td>
<td align="right">3.3%</td>
<td align="right">53,691</td>
<td align="right">8.8%</td>
<td align="right">-29.4%</td>
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
<td align="right">9,776</td>
<td align="right">12.9%</td>
<td align="right">4,097</td>
<td align="right">7.6%</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">31,884</td>
<td align="right">41.9%</td>
<td align="right">20,724</td>
<td align="right">38.6%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,505</td>
<td align="right">9.9%</td>
<td align="right">5,565</td>
<td align="right">10.4%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,185</td>
<td align="right">4.2%</td>
<td align="right">2,405</td>
<td align="right">4.5%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">2,160</td>
<td align="right">2.8%</td>
<td align="right">1,760</td>
<td align="right">3.3%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,383</td>
<td align="right">11.0%</td>
<td align="right">6,863</td>
<td align="right">12.8%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,075</td>
<td align="right">6.7%</td>
<td align="right">4,194</td>
<td align="right">7.8%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">780</td>
<td align="right">1.0%</td>
<td align="right">700</td>
<td align="right">1.3%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">804</td>
<td align="right">1.1%</td>
<td align="right">764</td>
<td align="right">1.4%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,439</td>
<td align="right">8.5%</td>
<td align="right">6,559</td>
<td align="right">12.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">60</td>
<td align="right">0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,900</td>
<td align="right">0.0%</td>
<td align="right">1,060</td>
<td align="right">0.0%</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">93,337,109</td>
<td align="right">9.6%</td>
<td align="right">67,642,892</td>
<td align="right">7.3%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">875,265,881</td>
<td align="right">90.4%</td>
<td align="right">863,242,000</td>
<td align="right">92.7%</td>
<td align="right">-1.4%</td>
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
<td align="right">66,905</td>
<td align="right">83.3%</td>
<td align="right">48,828</td>
<td align="right">78.5%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,370</td>
<td align="right">16.7%</td>
<td align="right">13,334</td>
<td align="right">21.5%</td>
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
<td align="right">6,722</td>
<td align="right">10.0%</td>
<td align="right">20,605</td>
<td align="right">42.2%</td>
<td align="right">206.5%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">14,280</td>
<td align="right">21.3%</td>
<td align="right">2,800</td>
<td align="right">5.7%</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">42,263</td>
<td align="right">63.2%</td>
<td align="right">22,443</td>
<td align="right">46.0%</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,520</td>
<td align="right">2.3%</td>
<td align="right">1,040</td>
<td align="right">2.1%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">640</td>
<td align="right">1.0%</td>
<td align="right">540</td>
<td align="right">1.1%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,480</td>
<td align="right">2.2%</td>
<td align="right">1,400</td>
<td align="right">2.9%</td>
<td align="right">-5.4%</td>
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
<td align="right">158,042,552</td>
<td align="right">2.7%</td>
<td align="right">2,580,210</td>
<td align="right">0.0%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,569,146</td>
<td align="right">0.4%</td>
<td align="right">9,637,876</td>
<td align="right">0.2%</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,761,506,622</td>
<td align="right">96.9%</td>
<td align="right">5,266,212,624</td>
<td align="right">99.8%</td>
<td align="right">-8.6%</td>
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
<td align="right">210,520</td>
<td align="right">24.3%</td>
<td align="right">55,009</td>
<td align="right">12.8%</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">656,479</td>
<td align="right">75.7%</td>
<td align="right">375,402</td>
<td align="right">87.2%</td>
<td align="right">-42.8%</td>
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
<td align="right">82,867</td>
<td align="right">39.4%</td>
<td align="right">12,244</td>
<td align="right">22.3%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">19,076</td>
<td align="right">9.1%</td>
<td align="right">2,994</td>
<td align="right">5.4%</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">24,181</td>
<td align="right">11.5%</td>
<td align="right">4,502</td>
<td align="right">8.2%</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">37,227</td>
<td align="right">17.7%</td>
<td align="right">8,911</td>
<td align="right">16.2%</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,145</td>
<td align="right">7.7%</td>
<td align="right">6,524</td>
<td align="right">11.9%</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,749</td>
<td align="right">0.8%</td>
<td align="right">863</td>
<td align="right">1.6%</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">180</td>
<td align="right">0.3%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">7,332</td>
<td align="right">3.5%</td>
<td align="right">4,261</td>
<td align="right">7.7%</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">14,911</td>
<td align="right">7.1%</td>
<td align="right">9,274</td>
<td align="right">16.9%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">683</td>
<td align="right">0.3%</td>
<td align="right">502</td>
<td align="right">0.9%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,009</td>
<td align="right">2.9%</td>
<td align="right">4,754</td>
<td align="right">8.6%</td>
<td align="right">-20.9%</td>
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
<td align="right">191,651</td>
<td align="right">0.0%</td>
<td align="right">54,872</td>
<td align="right">0.0%</td>
<td align="right">-71.4%</td>
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
<td align="right">1,060</td>
<td align="right">0.0%</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,529,565,662</td>
<td align="right">100.0%</td>
<td align="right">1,342,592,093</td>
<td align="right">100.0%</td>
<td align="right">-12.2%</td>
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
<td align="right">1,861</td>
<td align="right">5.7%</td>
<td align="right">1,543</td>
<td align="right">4.8%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,535</td>
<td align="right">94.3%</td>
<td align="right">30,507</td>
<td align="right">95.2%</td>
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
<td align="left">other</td>
<td align="right">380</td>
<td align="right">20.4%</td>
<td align="right">220</td>
<td align="right">14.3%</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">267</td>
<td align="right">14.3%</td>
<td align="right">227</td>
<td align="right">14.7%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,214</td>
<td align="right">65.2%</td>
<td align="right">1,096</td>
<td align="right">71.0%</td>
<td align="right">-9.7%</td>
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
<td align="right">30,485,411,275</td>
<td align="right">34.1%</td>
<td align="right">4,813,399,726</td>
<td align="right">19.7%</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">7,550,697,959</td>
<td align="right">8.5%</td>
<td align="right">1,814,555,235</td>
<td align="right">7.4%</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">50,587,976,422</td>
<td align="right">56.7%</td>
<td align="right">17,531,029,732</td>
<td align="right">71.6%</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">673,946,986</td>
<td align="right">0.8%</td>
<td align="right">333,015,004</td>
<td align="right">1.4%</td>
<td align="right">-50.6%</td>
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
<td align="right">369,401,569</td>
<td align="right">17.5%</td>
<td align="right">27,434,511</td>
<td align="right">4.6%</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,107,638</td>
<td align="right">4.9%</td>
<td align="right">9,841,589</td>
<td align="right">1.7%</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">558,709,619</td>
<td align="right">26.5%</td>
<td align="right">60,849,749</td>
<td align="right">10.2%</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">474,099,725</td>
<td align="right">22.5%</td>
<td align="right">146,816,856</td>
<td align="right">24.6%</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">73,913,641</td>
<td align="right">3.5%</td>
<td align="right">39,709,203</td>
<td align="right">6.7%</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">36,584,086</td>
<td align="right">1.7%</td>
<td align="right">20,802,779</td>
<td align="right">3.5%</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">44,667,152</td>
<td align="right">2.1%</td>
<td align="right">26,413,928</td>
<td align="right">4.4%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,337,109</td>
<td align="right">4.4%</td>
<td align="right">67,642,892</td>
<td align="right">11.3%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,334,483</td>
<td align="right">8.2%</td>
<td align="right">173,335,265</td>
<td align="right">29.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">158,042,552</td>
<td align="right">7.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">19,893,457</td>
<td align="right">3.3%</td>
<td align="right"></td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">87,518,876</td>
<td align="right">13.0%</td>
<td align="right">23,410,547</td>
<td align="right">7.0%</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">89,298,741</td>
<td align="right">13.2%</td>
<td align="right">38,925,725</td>
<td align="right">11.7%</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,508,653</td>
<td align="right">6.0%</td>
<td align="right">19,628,870</td>
<td align="right">5.9%</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">134,218,764</td>
<td align="right">19.9%</td>
<td align="right">86,257,982</td>
<td align="right">25.9%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">80,483,460</td>
<td align="right">11.9%</td>
<td align="right">53,716,370</td>
<td align="right">16.1%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,497,345</td>
<td align="right">4.1%</td>
<td align="right">27,080,077</td>
<td align="right">8.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,105,372</td>
<td align="right">2.7%</td>
<td align="right">18,140,461</td>
<td align="right">5.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">38,012,121</td>
<td align="right">5.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">23,851,898</td>
<td align="right">3.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,177,240</td>
<td align="right">3.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">11,301,093</td>
<td align="right">3.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">8,462,575</td>
<td align="right">2.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">6,250,980</td>
<td align="right">1.9%</td>
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
<td align="right">4,418,272</td>
<td align="right">0.1%</td>
<td align="right">2,658,092</td>
<td align="right">0.0%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,755,923</td>
<td align="right">1.0%</td>
<td align="right">83,525,064</td>
<td align="right">1.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,168,181,787</td>
<td align="right">73.2%</td>
<td align="right">6,109,496,149</td>
<td align="right">73.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,680,527,455</td>
<td align="right">79.2%</td>
<td align="right">6,629,926,525</td>
<td align="right">79.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,411,014,891</td>
<td align="right">16.7%</td>
<td align="right">1,401,873,603</td>
<td align="right">16.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,262,999,398</td>
<td align="right">26.8%</td>
<td align="right">2,248,772,568</td>
<td align="right">26.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,262,999,398</td>
<td align="right">26.8%</td>
<td align="right">2,248,772,568</td>
<td align="right">26.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">333,949,713</td>
<td align="right">4.0%</td>
<td align="right">331,875,029</td>
<td align="right">4.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">851,984,507</td>
<td align="right">10.1%</td>
<td align="right">846,898,965</td>
<td align="right">10.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,406,566,490</td>
<td align="right">16.7%</td>
<td align="right">1,399,185,482</td>
<td align="right">16.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">30,129</td>
<td align="right">0.0%</td>
<td align="right">30,029</td>
<td align="right">0.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,644,565</td>
<td align="right">3.9%</td>
<td align="right">331,697,973</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,097,811</td>
<td align="right">0.4%</td>
<td align="right">31,097,973</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,501</td>
<td align="right">2.1%</td>
<td align="right">175,480,822</td>
<td align="right">2.1%</td>
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
<td align="right">41,210,052,013</td>
<td align="right">41,210,052,013 / 0 !!</td>
<td align="right">15,158,817,925</td>
<td align="right">15,158,817,925 / 0 !!</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">96,509,508,823</td>
<td align="right">96,509,508,823 / 0 !!</td>
<td align="right">133,618,404,101</td>
<td align="right">133,618,404,101 / 0 !!</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">56,365,676,905</td>
<td align="right">56,365,676,905 / 0 !!</td>
<td align="right">37,899,730,906</td>
<td align="right">37,899,730,906 / 0 !!</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">103,859,174,619</td>
<td align="right">103,859,174,619 / 0 !!</td>
<td align="right">133,514,789,338</td>
<td align="right">133,514,789,338 / 0 !!</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,300</td>
<td align="right">1.4%</td>
<td align="right">2,972,700</td>
<td align="right">1.3%</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">62,000,011</td>
<td align="right"></td>
<td align="right">56,961,449</td>
<td align="right"></td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">68,609,788</td>
<td align="right"></td>
<td align="right">63,977,816</td>
<td align="right"></td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,600,348</td>
<td align="right"></td>
<td align="right">8,014,229</td>
<td align="right"></td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,543,478,346</td>
<td align="right"></td>
<td align="right">2,409,861,427</td>
<td align="right"></td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">235,988,948</td>
<td align="right"></td>
<td align="right">229,265,704</td>
<td align="right"></td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,773,781,686</td>
<td align="right">52.1%</td>
<td align="right">12,902,222,105</td>
<td align="right">52.4%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,882,111,556</td>
<td align="right">52.5%</td>
<td align="right">13,010,719,645</td>
<td align="right">52.8%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,582,829,430</td>
<td align="right"></td>
<td align="right">13,710,936,392</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,711,387,511</td>
<td align="right"></td>
<td align="right">3,683,421,508</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">92,968,938</td>
<td align="right">0.4%</td>
<td align="right">93,138,569</td>
<td align="right">0.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,635,338,910</td>
<td align="right"></td>
<td align="right">11,619,977,650</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,633,462,021</td>
<td align="right">47.5%</td>
<td align="right">11,618,110,472</td>
<td align="right">47.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">15,360,932</td>
<td align="right">0.1%</td>
<td align="right">15,358,971</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">240,283</td>
<td align="right">0.1%</td>
<td align="right">240,283</td>
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
<td align="right">112,267,788</td>
<td align="right">19,369,638,285</td>
<td align="right">0</td>
<td align="right">112,307,377</td>
<td align="right">19,409,373,669</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,644,844</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,973,507,280</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">8,280</td>
<td align="right">4.7%</td>
<td align="right">27,682</td>
<td align="right">5.6%</td>
<td align="right">234.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">177,313</td>
<td align="right">19.8%</td>
<td align="right">491,667</td>
<td align="right">52.1%</td>
<td align="right">177.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,002</td>
<td align="right">0.1%</td>
<td align="right">2,680</td>
<td align="right">0.3%</td>
<td align="right">167.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">9,432,209,759</td>
<td align="right"></td>
<td align="right">20,497,171,449</td>
<td align="right"></td>
<td align="right">117.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">649,917</td>
<td align="right">72.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,899</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">301,300,380,982</td>
<td align="right">3,194.4%</td>
<td align="right">435,840,075,335</td>
<td align="right">2,126.3%</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">715,606</td>
<td align="right">80.0%</td>
<td align="right">451,599</td>
<td align="right">47.9%</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,581</td>
<td align="right">0.4%</td>
<td align="right">2,966</td>
<td align="right">0.3%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">894,818</td>
<td align="right"></td>
<td align="right">943,286</td>
<td align="right"></td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">12,084</td>
<td align="right">1.4%</td>
<td align="right">12,046</td>
<td align="right">1.3%</td>
<td align="right">-0.3%</td>
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
<td align="right">165,554</td>
<td align="right">93.4%</td>
<td align="right">474,053</td>
<td align="right">96.4%</td>
<td align="right">186.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">177,313</td>
<td align="right"></td>
<td align="right">491,667</td>
<td align="right"></td>
<td align="right">177.3%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,600</td>
<td align="right">1.5%</td>
<td align="right">7,058</td>
<td align="right">1.4%</td>
<td align="right">171.5%</td>
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
<td align="right">741</td>
<td align="right">0.2%</td>
<td align="right">741 / 0 !!</td>
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
<td align="right">3,694</td>
<td align="right">2.1%</td>
<td align="right">15,641</td>
<td align="right">3.2%</td>
<td align="right">323.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">22,781</td>
<td align="right">12.8%</td>
<td align="right">46,397</td>
<td align="right">9.4%</td>
<td align="right">103.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20,875</td>
<td align="right">11.8%</td>
<td align="right">85,783</td>
<td align="right">17.4%</td>
<td align="right">310.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">47,871</td>
<td align="right">27.0%</td>
<td align="right">185,571</td>
<td align="right">37.7%</td>
<td align="right">287.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">40,521</td>
<td align="right">22.9%</td>
<td align="right">110,275</td>
<td align="right">22.4%</td>
<td align="right">172.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">23,867</td>
<td align="right">13.5%</td>
<td align="right">39,579</td>
<td align="right">8.0%</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">14,544</td>
<td align="right">8.2%</td>
<td align="right">7,361</td>
<td align="right">1.5%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,800</td>
<td align="right">1.6%</td>
<td align="right">760</td>
<td align="right">0.2%</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">360</td>
<td align="right">0.2%</td>
<td align="right">300</td>
<td align="right">0.1%</td>
<td align="right">-16.7%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">700.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">20,030</td>
<td align="right">11.3%</td>
<td align="right">22,212</td>
<td align="right">4.5%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,551</td>
<td align="right">9.3%</td>
<td align="right">66,334</td>
<td align="right">13.5%</td>
<td align="right">300.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">30,531</td>
<td align="right">17.2%</td>
<td align="right">145,590</td>
<td align="right">29.6%</td>
<td align="right">376.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">50,136</td>
<td align="right">28.3%</td>
<td align="right">160,156</td>
<td align="right">32.6%</td>
<td align="right">219.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">29,412</td>
<td align="right">16.6%</td>
<td align="right">64,198</td>
<td align="right">13.1%</td>
<td align="right">118.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,514</td>
<td align="right">7.6%</td>
<td align="right">13,400</td>
<td align="right">2.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,660</td>
<td align="right">2.6%</td>
<td align="right">1,623</td>
<td align="right">0.3%</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">700</td>
<td align="right">0.4%</td>
<td align="right">380</td>
<td align="right">0.1%</td>
<td align="right">-45.7%</td>
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
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">1,205,925</td>
<td align="right">14,606.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,885</td>
<td align="right">182,852,869</td>
<td align="right">11,743.7%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">10,164</td>
<td align="right">672,378</td>
<td align="right">6,515.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,084,240</td>
<td align="right">58,806,268</td>
<td align="right">2,721.5%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">7,869,568</td>
<td align="right">220,433,213</td>
<td align="right">2,701.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">370,525</td>
<td align="right">9,085,099</td>
<td align="right">2,352.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">2,104,763</td>
<td align="right">38,657,162</td>
<td align="right">1,736.7%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,468,651</td>
<td align="right">89,378,182</td>
<td align="right">1,281.7%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">785,055</td>
<td align="right">8,706,438</td>
<td align="right">1,009.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">6,776,827</td>
<td align="right">72,629,000</td>
<td align="right">971.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">937,895</td>
<td align="right">8,337,787</td>
<td align="right">789.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">936,365,537</td>
<td align="right">8,093,939,127</td>
<td align="right">764.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">4,785,180</td>
<td align="right">40,914,688</td>
<td align="right">755.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">5,709,160</td>
<td align="right">47,149,619</td>
<td align="right">725.9%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,942,620</td>
<td align="right">23,470,136</td>
<td align="right">697.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">11,163,200</td>
<td align="right">81,310,522</td>
<td align="right">628.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,303,714</td>
<td align="right">9,187,974</td>
<td align="right">604.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">60,921,091</td>
<td align="right">333,715,612</td>
<td align="right">447.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">238,358,782</td>
<td align="right">1,281,242,965</td>
<td align="right">437.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,427,900</td>
<td align="right">499,622,943</td>
<td align="right">412.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,076,388,923</td>
<td align="right">5,332,291,146</td>
<td align="right">395.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">49,870,456</td>
<td align="right">240,582,924</td>
<td align="right">382.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">51,304,796</td>
<td align="right">244,060,344</td>
<td align="right">375.7%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,842,060</td>
<td align="right">7,786,720</td>
<td align="right">322.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">27,150,708</td>
<td align="right">111,657,635</td>
<td align="right">311.3%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,154,420</td>
<td align="right">40,876,964</td>
<td align="right">302.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,431,296</td>
<td align="right">37,846,084</td>
<td align="right">301.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">114,754,074</td>
<td align="right">442,480,989</td>
<td align="right">285.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">204,905,296</td>
<td align="right">767,427,116</td>
<td align="right">274.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">12,712,504</td>
<td align="right">47,116,600</td>
<td align="right">270.6%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">32,293,752</td>
<td align="right">117,567,597</td>
<td align="right">264.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,280,004</td>
<td align="right">192,858,957</td>
<td align="right">255.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,275,764</td>
<td align="right">192,839,653</td>
<td align="right">255.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,640,211</td>
<td align="right">8,665,935</td>
<td align="right">228.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">48,047,215</td>
<td align="right">147,356,492</td>
<td align="right">206.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,111,754,393</td>
<td align="right">6,327,956,622</td>
<td align="right">199.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">278,686,103</td>
<td align="right">819,615,936</td>
<td align="right">194.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">40,300,048</td>
<td align="right">109,880,659</td>
<td align="right">172.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">40,985,468</td>
<td align="right">111,079,664</td>
<td align="right">171.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">209,960,769</td>
<td align="right">536,959,914</td>
<td align="right">155.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,122,658,448</td>
<td align="right">2,809,004,877</td>
<td align="right">150.2%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">45,570,023</td>
<td align="right">107,308,315</td>
<td align="right">135.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">45,570,023</td>
<td align="right">107,308,315</td>
<td align="right">135.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,309,832</td>
<td align="right">208,826,263</td>
<td align="right">131.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,994,660</td>
<td align="right">4,577,799</td>
<td align="right">129.5%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">420</td>
<td align="right">940</td>
<td align="right">123.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">139,676,556</td>
<td align="right">310,419,683</td>
<td align="right">122.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">39,076,060</td>
<td align="right">85,817,127</td>
<td align="right">119.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,241,400</td>
<td align="right">4,904,248</td>
<td align="right">118.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">9,432,209,759</td>
<td align="right">20,497,171,449</td>
<td align="right">117.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">49,699,380</td>
<td align="right">107,599,708</td>
<td align="right">116.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">115,238,934</td>
<td align="right">242,027,483</td>
<td align="right">110.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">110,269,454</td>
<td align="right">231,317,989</td>
<td align="right">109.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">475,047,261</td>
<td align="right">968,409,678</td>
<td align="right">103.9%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">962,920</td>
<td align="right">1,932,105</td>
<td align="right">100.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,626,064</td>
<td align="right">1,377,930</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">36,583,000</td>
<td align="right">71,605,966</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,065,198,609</td>
<td align="right">2,045,257,700</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">166,049,961</td>
<td align="right">318,461,924</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,713,031,331</td>
<td align="right">3,269,568,568</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">247,072,356</td>
<td align="right">466,080,832</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">891,713,662</td>
<td align="right">1,679,073,130</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">39,233,233</td>
<td align="right">73,683,019</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">290,692,085</td>
<td align="right">542,232,481</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,183,355,126</td>
<td align="right">15,211,059,403</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">92,412,707</td>
<td align="right">170,554,877</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">41,253,593</td>
<td align="right">75,927,560</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">576,272,661</td>
<td align="right">1,050,351,150</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">219,954,795</td>
<td align="right">399,724,532</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,894,060</td>
<td align="right">88,632,221</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,894,060</td>
<td align="right">88,632,221</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">388,236,039</td>
<td align="right">699,722,821</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,398,739,180</td>
<td align="right">4,294,390,463</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">200,142,092</td>
<td align="right">356,322,294</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,462,298,225</td>
<td align="right">4,383,561,605</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">44,058,042</td>
<td align="right">9,774,748</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">44,061,602</td>
<td align="right">9,816,733</td>
<td align="right">-77.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">153,210,727</td>
<td align="right">36,141,386</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,145,062,479</td>
<td align="right">3,780,169,755</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,133,029,652</td>
<td align="right">5,485,187,791</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">707,669,498</td>
<td align="right">1,230,107,811</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">8,195,840</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">962,920</td>
<td align="right">1,662,745</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,218,999,035</td>
<td align="right">14,183,207,744</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,587,500</td>
<td align="right">9,632,992</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">703,070,472</td>
<td align="right">1,197,297,381</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,287,646,922</td>
<td align="right">3,878,514,673</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">709,493,219</td>
<td align="right">1,200,759,638</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">452,354,489</td>
<td align="right">751,280,039</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,776,769,171</td>
<td align="right">2,916,454,576</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,413,790,191</td>
<td align="right">5,598,509,283</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,810,249,921</td>
<td align="right">6,237,104,352</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">3,362,936,711</td>
<td align="right">5,486,266,575</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,618,713,155</td>
<td align="right">2,637,582,887</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">924,918,454</td>
<td align="right">1,494,691,076</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,756,619,371</td>
<td align="right">2,832,896,651</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">160,127,395</td>
<td align="right">256,341,468</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">917,546,025</td>
<td align="right">1,468,835,214</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">107,936,249</td>
<td align="right">169,468,406</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,649,463,161</td>
<td align="right">5,690,484,620</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">697,977,658</td>
<td align="right">1,074,750,387</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">702,781,818</td>
<td align="right">1,080,690,037</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">797,202,387</td>
<td align="right">1,225,249,045</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,936,694,929</td>
<td align="right">12,170,369,249</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">898,300,429</td>
<td align="right">1,376,835,101</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,561,764,436</td>
<td align="right">5,452,531,505</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">489,820</td>
<td align="right">748,480</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">122,707,543</td>
<td align="right">187,471,893</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">228,516,684</td>
<td align="right">348,574,017</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">305,989,398</td>
<td align="right">459,856,708</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,183,374,371</td>
<td align="right">592,876,116</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">162,208,144</td>
<td align="right">242,836,317</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">353,753,017</td>
<td align="right">520,129,880</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">8,445,156,796</td>
<td align="right">12,247,209,895</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,826,179,766</td>
<td align="right">5,533,446,856</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">210,378,782</td>
<td align="right">117,290,099</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">155,220,170</td>
<td align="right">223,641,995</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">130,183,353</td>
<td align="right">187,484,947</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">74,216,157</td>
<td align="right">106,569,569</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">622,669,738</td>
<td align="right">887,944,780</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,102,252</td>
<td align="right">736,861,343</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">359,288,787</td>
<td align="right">510,098,627</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">57,765,800</td>
<td align="right">81,290,003</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,420,036,091</td>
<td align="right">3,384,638,086</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,619,349,265</td>
<td align="right">2,249,684,940</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">847,863,072</td>
<td align="right">1,175,389,064</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,951,640</td>
<td align="right">9,635,552</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,567,700</td>
<td align="right">45,113,808</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,018,699</td>
<td align="right">53,604,408</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">25,336,425,548</td>
<td align="right">34,880,193,108</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">5,472,895</td>
<td align="right">7,522,809</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">985,071,238</td>
<td align="right">1,350,032,711</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">181,469,202</td>
<td align="right">114,407,558</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,744,938,250</td>
<td align="right">20,159,784,544</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">376,020</td>
<td align="right">508,175</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">125,369,780</td>
<td align="right">168,459,539</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,082,746,573</td>
<td align="right">1,448,223,276</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">879,797,758</td>
<td align="right">1,174,566,577</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,365,961,034</td>
<td align="right">8,351,656,759</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,413,619,239</td>
<td align="right">1,852,987,646</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">121,101,396</td>
<td align="right">158,582,130</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">68,863,002</td>
<td align="right">90,107,114</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">341,961,176</td>
<td align="right">446,398,728</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">991,343,737</td>
<td align="right">1,279,565,657</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,947,788,445</td>
<td align="right">2,511,777,722</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">351,212,423</td>
<td align="right">452,706,181</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">11,445,900</td>
<td align="right">14,694,435</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,071,491,684</td>
<td align="right">1,373,359,205</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,405,542,033</td>
<td align="right">5,632,409,595</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,364,112,300</td>
<td align="right">3,008,440,096</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">21,070,493,105</td>
<td align="right">26,787,249,062</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,557,249,657</td>
<td align="right">3,230,631,133</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,670,451,879</td>
<td align="right">7,136,264,434</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">167,924,929</td>
<td align="right">210,606,597</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,332,317,854</td>
<td align="right">1,670,578,238</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,156,491,394</td>
<td align="right">1,446,635,016</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">25,246,820</td>
<td align="right">19,035,712</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,232,020</td>
<td align="right">433,663,363</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">952,135,942</td>
<td align="right">1,177,576,690</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,049,856,630</td>
<td align="right">1,295,208,176</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">67,610,140</td>
<td align="right">83,266,549</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">366,309,287</td>
<td align="right">448,278,629</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,289,989</td>
<td align="right">118,799,612</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">236,468,671</td>
<td align="right">286,842,872</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">394,814,562</td>
<td align="right">477,960,811</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,241,889</td>
<td align="right">117,353,386</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">112,666,344</td>
<td align="right">89,466,290</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">530,143,303</td>
<td align="right">637,982,437</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,617,520,810</td>
<td align="right">1,945,536,596</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">676,913,769</td>
<td align="right">812,002,023</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,905,604</td>
<td align="right">7,128,527</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">166,996,855</td>
<td align="right">197,413,717</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">556,437,781</td>
<td align="right">653,770,383</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,884,415,707</td>
<td align="right">5,725,128,372</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,731,396,602</td>
<td align="right">4,357,146,367</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,436,926</td>
<td align="right">37,872,125</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,713,956,979</td>
<td align="right">1,998,903,014</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,699,893,829</td>
<td align="right">1,978,408,222</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">281,309,822</td>
<td align="right">327,258,506</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,821,109,334</td>
<td align="right">2,111,300,698</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">658,816,803</td>
<td align="right">763,586,997</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">961,404,862</td>
<td align="right">1,113,549,960</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">394,254,521</td>
<td align="right">452,684,232</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,739,351</td>
<td align="right">234,772,326</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,401,858</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,143,984,920</td>
<td align="right">1,304,798,280</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">242,849,697</td>
<td align="right">276,951,237</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,254,344,736</td>
<td align="right">5,989,284,802</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,478,801,318</td>
<td align="right">1,683,105,508</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,344,480,866</td>
<td align="right">1,518,608,800</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">99,691,960</td>
<td align="right">112,543,350</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">10,339,855,502</td>
<td align="right">11,670,145,795</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,265,959,537</td>
<td align="right">1,422,844,810</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,439,954</td>
<td align="right">676,433,589</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">24,662</td>
<td align="right">27,589</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,939,009,314</td>
<td align="right">4,399,891,634</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">566,894,220</td>
<td align="right">626,719,593</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,331,739</td>
<td align="right">75,518,353</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,313,759,885</td>
<td align="right">2,537,476,684</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,224,686,354</td>
<td align="right">2,431,784,721</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,871,063,615</td>
<td align="right">2,605,301,128</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,247,637,332</td>
<td align="right">11,157,405,734</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">57,016,988</td>
<td align="right">62,017,844</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">532,993,906</td>
<td align="right">578,755,644</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,625,840,004</td>
<td align="right">3,937,123,939</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">721,026,612</td>
<td align="right">763,928,909</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,035,326,593</td>
<td align="right">3,210,897,834</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">84,053,160</td>
<td align="right">88,091,545</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,905,400</td>
<td align="right">162,224,060</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">782,483,423</td>
<td align="right">818,240,476</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">780,841,995</td>
<td align="right">816,227,272</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,484,235</td>
<td align="right">814,595,752</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,730,972,596</td>
<td align="right">4,935,116,742</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,377,462,304</td>
<td align="right">2,460,631,489</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">760,095,394</td>
<td align="right">786,667,041</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,081,911,595</td>
<td align="right">2,153,811,568</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,391,402,480</td>
<td align="right">2,473,404,171</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">597,220</td>
<td align="right">608,720</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">580,643,900</td>
<td align="right">590,891,692</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,006,381</td>
<td align="right">82,340,353</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,043,323</td>
<td align="right">742,793,629</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,316,575,890</td>
<td align="right">1,309,593,196</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">555,929,442</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">253,107,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">2,679,230</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">90,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_UPDATE</td>
<td align="right"></td>
<td align="right">21,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_LOCALS</td>
<td align="right"></td>
<td align="right">2,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FROM_DICT_OR_DEREF</td>
<td align="right"></td>
<td align="right">1,280</td>
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
<td align="left">CALL</td>
<td align="right">19,115</td>
<td align="right">117,168</td>
<td align="right">513.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,020</td>
<td align="right">3,840</td>
<td align="right">276.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">60</td>
<td align="right">222</td>
<td align="right">270.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,115</td>
<td align="right">75,862</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">36,000</td>
<td align="right">40,159</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right"></td>
<td align="right">9,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right"></td>
<td align="right">397</td>
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
<td align="right">1,151</td>
<td align="right">1,371</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,151</td>
<td align="right">1,371</td>
<td align="right">19.1%</td>
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
<td align="right">460</td>
<td align="right">460</td>
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
<td align="right">1,801</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
