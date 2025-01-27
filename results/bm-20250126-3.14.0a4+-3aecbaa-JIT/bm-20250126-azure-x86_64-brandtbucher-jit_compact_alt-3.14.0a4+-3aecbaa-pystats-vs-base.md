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
<td align="left">STORE_SLICE</td>
<td align="right">1,194,074</td>
<td align="right">112,189,224</td>
<td align="right">9,295.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,090,155</td>
<td align="right">60,094,367</td>
<td align="right">2,775.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">172,453,328</td>
<td align="right">3,326,376,768</td>
<td align="right">1,828.9%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,000,000</td>
<td align="right">100,136,760</td>
<td align="right">1,568.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">200,675,067</td>
<td align="right">2,206,349,710</td>
<td align="right">999.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">118,888,431</td>
<td align="right">1,252,633,198</td>
<td align="right">953.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">61,213,256</td>
<td align="right">498,620,922</td>
<td align="right">714.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">237,211,986</td>
<td align="right">1,570,530,467</td>
<td align="right">562.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">181,652,850</td>
<td align="right">1,164,479,299</td>
<td align="right">541.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">187,982,818</td>
<td align="right">1,175,201,464</td>
<td align="right">525.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">261,020,759</td>
<td align="right">1,601,996,567</td>
<td align="right">513.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">268,811,430</td>
<td align="right">1,574,074,236</td>
<td align="right">485.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">51,508,631</td>
<td align="right">268,772,242</td>
<td align="right">421.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">33,292,775</td>
<td align="right">156,225,558</td>
<td align="right">369.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">87,964,979</td>
<td align="right">382,847,842</td>
<td align="right">335.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">288,624,562</td>
<td align="right">1,250,936,712</td>
<td align="right">333.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">451,884,260</td>
<td align="right">1,873,653,259</td>
<td align="right">314.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">236,915</td>
<td align="right">922,140</td>
<td align="right">289.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">199,885,780</td>
<td align="right">767,981,628</td>
<td align="right">284.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,630,422</td>
<td align="right">470,205,475</td>
<td align="right">251.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">10,021,291</td>
<td align="right">34,964,729</td>
<td align="right">248.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">456,617,015</td>
<td align="right">1,589,105,122</td>
<td align="right">248.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">65,285,113</td>
<td align="right">188,850,464</td>
<td align="right">189.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">70,920,982</td>
<td align="right">198,502,389</td>
<td align="right">179.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,561,506,284</td>
<td align="right">4,213,404,831</td>
<td align="right">169.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">71,471,919</td>
<td align="right">192,687,332</td>
<td align="right">169.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">278,041,043</td>
<td align="right">744,059,836</td>
<td align="right">167.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">157,304,434</td>
<td align="right">416,005,943</td>
<td align="right">164.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">635,425,544</td>
<td align="right">1,672,337,272</td>
<td align="right">163.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">8,139,397</td>
<td align="right">20,621,033</td>
<td align="right">153.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">128,490,761</td>
<td align="right">319,247,775</td>
<td align="right">148.5%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">48,620,545</td>
<td align="right">116,502,959</td>
<td align="right">139.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">26,227,148</td>
<td align="right">60,078,423</td>
<td align="right">129.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">405,505,586</td>
<td align="right">920,536,899</td>
<td align="right">127.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">262,892,393</td>
<td align="right">593,252,789</td>
<td align="right">125.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">702,403,099</td>
<td align="right">1,562,793,879</td>
<td align="right">122.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">223,295,727</td>
<td align="right">477,795,069</td>
<td align="right">114.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">34,315,046</td>
<td align="right">72,060,215</td>
<td align="right">110.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">189,348,668</td>
<td align="right">382,971,684</td>
<td align="right">102.3%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">170,068,018</td>
<td align="right">57,749</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,573,100</td>
<td align="right">1,060</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">781,020</td>
<td align="right">620</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,813,998</td>
<td align="right">265,485</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,238,228</td>
<td align="right">8,839</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,553</td>
<td align="right">249</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,920</td>
<td align="right">43,581</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">392,949,467</td>
<td align="right">35,450,693</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,848,447</td>
<td align="right">360,653</td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,013,376</td>
<td align="right">1,239,828</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">614,477,006</td>
<td align="right">1,144,735,254</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">776,892,782</td>
<td align="right">108,853,743</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">206,464,103</td>
<td align="right">32,337,407</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">266,587,078</td>
<td align="right">46,570,738</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,902,674</td>
<td align="right">721,363</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">98,028,566</td>
<td align="right">18,322,536</td>
<td align="right">-81.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">372,250,213</td>
<td align="right">85,372,418</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,533</td>
<td align="right">180,830</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,464,665</td>
<td align="right">16,151,416</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_LAZY_DICT</td>
<td align="right">24,727,405</td>
<td align="right">43,389,586</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">63,177,013</td>
<td align="right">15,940,026</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">37,276,771</td>
<td align="right">10,047,113</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD_METHOD</td>
<td align="right">53,906,578</td>
<td align="right">14,576,839</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">65,396,203</td>
<td align="right">18,903,845</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">264,079,292</td>
<td align="right">78,381,177</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">229,157,895</td>
<td align="right">68,525,955</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,963,412</td>
<td align="right">1,217,314</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">57,541,515</td>
<td align="right">18,562,869</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">112,802,540</td>
<td align="right">36,394,734</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">127,347,615</td>
<td align="right">212,681,817</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">107,550,106</td>
<td align="right">179,215,297</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">79,974,423</td>
<td align="right">133,018,693</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">327,774,223</td>
<td align="right">540,489,702</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,660,142,912</td>
<td align="right">1,643,613,058</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,368</td>
<td align="right">109,387,785</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,815,135</td>
<td align="right">42,817,623</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">208,883,573</td>
<td align="right">85,781,930</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">31,650,518</td>
<td align="right">13,235,412</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,746,234,319</td>
<td align="right">5,919,276,237</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,135,470</td>
<td align="right">29,534,544</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,115,042</td>
<td align="right">1,319,069</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">322,587,416</td>
<td align="right">136,884,514</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,050,448,794</td>
<td align="right">873,205,225</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,032,275</td>
<td align="right">3,890,275</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,742,081,866</td>
<td align="right">801,729,543</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,789,332,385</td>
<td align="right">1,748,203,242</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,985,599,702</td>
<td align="right">4,593,742,184</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">69,225,051</td>
<td align="right">32,487,952</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,552,810</td>
<td align="right">4,625,023</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">712,055,691</td>
<td align="right">347,101,091</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">898,547,584</td>
<td align="right">438,461,581</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">59,875,512</td>
<td align="right">29,842,356</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,464,909,071</td>
<td align="right">2,176,076,366</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">516,660,474</td>
<td align="right">267,919,091</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">329,150,977</td>
<td align="right">173,229,815</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">480,364,376</td>
<td align="right">257,939,593</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">58,814,169</td>
<td align="right">31,663,802</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">58,596,340</td>
<td align="right">31,977,337</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">182,085,502</td>
<td align="right">99,541,393</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,956,873</td>
<td align="right">593,435,242</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,922,952</td>
<td align="right">32,730,266</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,201,440,165</td>
<td align="right">1,233,385,333</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">59,548</td>
<td align="right">33,381</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">440,593,772</td>
<td align="right">633,212,031</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">95,453,593</td>
<td align="right">54,841,830</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">313,819,027</td>
<td align="right">181,635,934</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,896</td>
<td align="right">2,317</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">169,042,544</td>
<td align="right">100,827,612</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,746,631,992</td>
<td align="right">1,668,052,536</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">226,646,962</td>
<td align="right">140,085,743</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,312,313</td>
<td align="right">29,995,243</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">94,229,519</td>
<td align="right">58,781,354</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,134,546,953</td>
<td align="right">1,333,103,686</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">114,776,774</td>
<td align="right">71,914,951</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">66,754,923</td>
<td align="right">42,061,995</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,789</td>
<td align="right">27,275,122</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,664,693</td>
<td align="right">12,210,496</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">276,786,617</td>
<td align="right">182,727,745</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">131,701,796</td>
<td align="right">88,400,171</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,677,323,649</td>
<td align="right">1,162,534,272</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">79,533,627</td>
<td align="right">55,648,906</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,363,181</td>
<td align="right">70,793,934</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">42,649,872</td>
<td align="right">31,593,963</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,956,308</td>
<td align="right">2,964,610</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">562,200,407</td>
<td align="right">425,670,766</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">299,767,524</td>
<td align="right">370,739,816</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">79,360,638</td>
<td align="right">60,631,552</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">36,195,435</td>
<td align="right">27,711,237</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">36,604,165</td>
<td align="right">28,541,703</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">21,773,890</td>
<td align="right">17,115,218</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">1,179,280,007</td>
<td align="right">936,071,523</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,046,191</td>
<td align="right">7,273,572</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">171,787,666</td>
<td align="right">138,699,320</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">254,383,402</td>
<td align="right">206,532,253</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">157,640,716</td>
<td align="right">186,338,254</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">610,006,598</td>
<td align="right">720,631,608</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">806,793,728</td>
<td align="right">931,977,706</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,876,948</td>
<td align="right">17,708,438</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,247,254,423</td>
<td align="right">15,227,185,854</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">23,563,767</td>
<td align="right">20,076,139</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,847</td>
<td align="right">5,271,777</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">27,368,715</td>
<td align="right">31,213,535</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">163,482,832</td>
<td align="right">141,642,120</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,866,911</td>
<td align="right">4,294,103</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">145,824,242</td>
<td align="right">128,846,534</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">102,525,806</td>
<td align="right">90,602,206</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,439,786</td>
<td align="right">1,279,169</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,546,408</td>
<td align="right">18,325,489</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,876,969</td>
<td align="right">18,656,050</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,650,986</td>
<td align="right">10,437,126</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">54,722,361</td>
<td align="right">49,782,332</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,036,247,851</td>
<td align="right">3,301,550,715</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,670</td>
<td align="right">51,847</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">160,320,260</td>
<td align="right">148,072,209</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">116,015,292</td>
<td align="right">124,829,405</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">174,534,121</td>
<td align="right">162,565,728</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">36,049,072</td>
<td align="right">33,706,452</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">59,426,476</td>
<td align="right">62,512,784</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">112,044,476</td>
<td align="right">106,253,160</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">139,893,049</td>
<td align="right">133,832,522</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,589,953</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">126,487,874</td>
<td align="right">122,542,976</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,626,842,025</td>
<td align="right">2,700,612,410</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">51,648,526</td>
<td align="right">50,407,299</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,316,507</td>
<td align="right">238,960,744</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,375,330</td>
<td align="right">178,126,501</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">68,226,933</td>
<td align="right">67,729,243</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">132,870,031</td>
<td align="right">133,795,563</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,619,023,928</td>
<td align="right">1,611,279,958</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,660</td>
<td align="right">33,651</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,243</td>
<td align="right">14,758,489</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,579</td>
<td align="right">128,839,285</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">130,919</td>
<td align="right">130,928</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,862</td>
<td align="right">120,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">405,463</td>
<td align="right">405,455</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,970,233,093</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">NOT_TAKEN</td>
<td align="right">18,032,228</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">CLEANUP_THROW</td>
<td align="right">98,718</td>
<td align="right">98,718</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,148</td>
<td align="right">57,148</td>
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
<td align="left">LOAD_LOCALS</td>
<td align="right">3,624</td>
<td align="right">3,624</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD</td>
<td align="right">2,518</td>
<td align="right">2,518</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">190</td>
<td align="right">190</td>
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
<td align="right">276,655,200</td>
<td align="right">3.5%</td>
<td align="right">182,645,797</td>
<td align="right">2.4%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">41,869,079</td>
<td align="right">0.5%</td>
<td align="right">38,962,749</td>
<td align="right">0.5%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,516,738,094</td>
<td align="right">95.9%</td>
<td align="right">7,492,348,373</td>
<td align="right">97.1%</td>
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
<td align="right">124,106</td>
<td align="right">13.5%</td>
<td align="right">74,718</td>
<td align="right">9.1%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">797,341</td>
<td align="right">86.5%</td>
<td align="right">742,353</td>
<td align="right">90.9%</td>
<td align="right">-6.9%</td>
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
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.7%</td>
<td align="right">2,288</td>
<td align="right">3.1%</td>
<td align="right">173.7%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">1.9%</td>
<td align="right">6,367</td>
<td align="right">8.5%</td>
<td align="right">171.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,342</td>
<td align="right">15.6%</td>
<td align="right">2,266</td>
<td align="right">3.0%</td>
<td align="right">-88.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">6,303</td>
<td align="right">5.1%</td>
<td align="right">1,465</td>
<td align="right">2.0%</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,474</td>
<td align="right">2.8%</td>
<td align="right">817</td>
<td align="right">1.1%</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.1%</td>
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,412</td>
<td align="right">4.4%</td>
<td align="right">1,968</td>
<td align="right">2.6%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1,367</td>
<td align="right">1.1%</td>
<td align="right">499</td>
<td align="right">0.7%</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">5,293</td>
<td align="right">4.3%</td>
<td align="right">1,979</td>
<td align="right">2.6%</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">1.1%</td>
<td align="right">636</td>
<td align="right">0.9%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">630</td>
<td align="right">0.5%</td>
<td align="right">296</td>
<td align="right">0.4%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">9,347</td>
<td align="right">7.5%</td>
<td align="right">4,576</td>
<td align="right">6.1%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">1.6%</td>
<td align="right">978</td>
<td align="right">1.3%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,509</td>
<td align="right">18.9%</td>
<td align="right">12,321</td>
<td align="right">16.5%</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">493</td>
<td align="right">0.4%</td>
<td align="right">304</td>
<td align="right">0.4%</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20,069</td>
<td align="right">16.2%</td>
<td align="right">12,615</td>
<td align="right">16.9%</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">3,051</td>
<td align="right">2.5%</td>
<td align="right">2,078</td>
<td align="right">2.8%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">13,456</td>
<td align="right">10.8%</td>
<td align="right">17,690</td>
<td align="right">23.7%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,718</td>
<td align="right">4.6%</td>
<td align="right">5,552</td>
<td align="right">7.4%</td>
<td align="right">-2.9%</td>
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
<td align="right">97,363,181</td>
<td align="right">100.0%</td>
<td align="right">70,793,934</td>
<td align="right">100.0%</td>
<td align="right">-27.3%</td>
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
<td align="right">451,733,345</td>
<td align="right">7.6%</td>
<td align="right">1,873,162,072</td>
<td align="right">25.6%</td>
<td align="right">314.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,825,948</td>
<td align="right">0.1%</td>
<td align="right">5,877,053</td>
<td align="right">0.1%</td>
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
<td align="right">5,470,646,791</td>
<td align="right">92.3%</td>
<td align="right">5,432,165,296</td>
<td align="right">74.3%</td>
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
<td align="right">141,677</td>
<td align="right">54.4%</td>
<td align="right">482,267</td>
<td align="right">80.1%</td>
<td align="right">240.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118,933</td>
<td align="right">45.6%</td>
<td align="right">119,565</td>
<td align="right">19.9%</td>
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
<td align="left">list slice</td>
<td align="right">7,096</td>
<td align="right">5.0%</td>
<td align="right">189,423</td>
<td align="right">39.3%</td>
<td align="right">2,569.4%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">3,677</td>
<td align="right">2.6%</td>
<td align="right">15,367</td>
<td align="right">3.2%</td>
<td align="right">317.9%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,574</td>
<td align="right">11.7%</td>
<td align="right">54,668</td>
<td align="right">11.3%</td>
<td align="right">229.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">59,700</td>
<td align="right">42.1%</td>
<td align="right">190,284</td>
<td align="right">39.5%</td>
<td align="right">218.7%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.1%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,444</td>
<td align="right">8.8%</td>
<td align="right">1,161</td>
<td align="right">0.2%</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">768</td>
<td align="right">0.5%</td>
<td align="right">194</td>
<td align="right">0.0%</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,609</td>
<td align="right">2.5%</td>
<td align="right">1,854</td>
<td align="right">0.4%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">34,775</td>
<td align="right">24.5%</td>
<td align="right">29,209</td>
<td align="right">6.1%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">65</td>
<td align="right">0.0%</td>
<td align="right">-9.7%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,186</td>
<td align="right">0.0%</td>
<td align="right">14,189</td>
<td align="right">0.0%</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">113,347,386</td>
<td align="right">1.0%</td>
<td align="right">131,630,138</td>
<td align="right">1.2%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,050,748,560</td>
<td align="right">99.0%</td>
<td align="right">10,932,573,089</td>
<td align="right">98.8%</td>
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
<td align="right">230,024</td>
<td align="right">0.0%</td>
<td align="right">230,013</td>
<td align="right">0.0%</td>
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
<td align="right">2,312,581</td>
<td align="right">100.0%</td>
<td align="right">2,657,321</td>
<td align="right">100.0%</td>
<td align="right">14.9%</td>
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
<td align="right">287</td>
<td align="right">64.3%</td>
<td align="right">287</td>
<td align="right">64.3%</td>
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
<td align="right">584,005</td>
<td align="right">82.9%</td>
<td align="right">573,706</td>
<td align="right">82.6%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">111,574</td>
<td align="right">15.8%</td>
<td align="right">111,574</td>
<td align="right">16.1%</td>
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
<td align="right">20,168</td>
<td align="right">99.4%</td>
<td align="right">19,952</td>
<td align="right">99.4%</td>
<td align="right">-1.1%</td>
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
<td align="right">87,841,361</td>
<td align="right">1.9%</td>
<td align="right">382,689,595</td>
<td align="right">7.9%</td>
<td align="right">335.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,279,929</td>
<td align="right">0.0%</td>
<td align="right">609,024</td>
<td align="right">0.0%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,516,343,649</td>
<td align="right">98.1%</td>
<td align="right">4,473,328,356</td>
<td align="right">92.1%</td>
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
<td align="left">Failure</td>
<td align="right">105,352</td>
<td align="right">71.5%</td>
<td align="right">140,076</td>
<td align="right">82.6%</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">42,094</td>
<td align="right">28.5%</td>
<td align="right">29,475</td>
<td align="right">17.4%</td>
<td align="right">-30.0%</td>
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
<td align="right">4,556</td>
<td align="right">4.3%</td>
<td align="right">87,817</td>
<td align="right">62.7%</td>
<td align="right">1,827.5%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.3%</td>
<td align="right">317</td>
<td align="right">0.2%</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,426</td>
<td align="right">6.1%</td>
<td align="right">578</td>
<td align="right">0.4%</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,380</td>
<td align="right">8.0%</td>
<td align="right">890</td>
<td align="right">0.6%</td>
<td align="right">-89.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">981</td>
<td align="right">0.9%</td>
<td align="right">294</td>
<td align="right">0.2%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,221</td>
<td align="right">1.2%</td>
<td align="right">404</td>
<td align="right">0.3%</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">929</td>
<td align="right">0.9%</td>
<td align="right">499</td>
<td align="right">0.4%</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">225</td>
<td align="right">0.2%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">213</td>
<td align="right">0.2%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">43,653</td>
<td align="right">41.4%</td>
<td align="right">28,050</td>
<td align="right">20.0%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,158</td>
<td align="right">22.0%</td>
<td align="right">14,904</td>
<td align="right">10.6%</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,715</td>
<td align="right">7.3%</td>
<td align="right">5,885</td>
<td align="right">4.2%</td>
<td align="right">-23.7%</td>
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
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
<td align="right">25,391</td>
<td align="right">0.0%</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">51,612,314</td>
<td align="right">2.3%</td>
<td align="right">50,381,613</td>
<td align="right">2.3%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,188,866,125</td>
<td align="right">97.6%</td>
<td align="right">2,167,213,030</td>
<td align="right">97.7%</td>
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
<td align="right">38,435</td>
<td align="right">53.1%</td>
<td align="right">2,712</td>
<td align="right">10.4%</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">33,951</td>
<td align="right">46.9%</td>
<td align="right">23,457</td>
<td align="right">89.6%</td>
<td align="right">-30.9%</td>
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
<td align="right">9,186</td>
<td align="right">27.1%</td>
<td align="right">4,013</td>
<td align="right">17.1%</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,738</td>
<td align="right">16.9%</td>
<td align="right">8,962</td>
<td align="right">38.2%</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,200</td>
<td align="right">33.0%</td>
<td align="right">5,681</td>
<td align="right">24.2%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,827</td>
<td align="right">23.1%</td>
<td align="right">4,801</td>
<td align="right">20.5%</td>
<td align="right">-38.7%</td>
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
<td align="right">118,788,479</td>
<td align="right">15.8%</td>
<td align="right">1,252,268,661</td>
<td align="right">36.5%</td>
<td align="right">954.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">598,658,629</td>
<td align="right">79.8%</td>
<td align="right">2,143,323,595</td>
<td align="right">62.4%</td>
<td align="right">258.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,233,381</td>
<td align="right">4.3%</td>
<td align="right">38,287,901</td>
<td align="right">1.1%</td>
<td align="right">18.8%</td>
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
<td align="right">94,875</td>
<td align="right">13.4%</td>
<td align="right">359,514</td>
<td align="right">33.1%</td>
<td align="right">278.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">613,105</td>
<td align="right">86.6%</td>
<td align="right">727,330</td>
<td align="right">66.9%</td>
<td align="right">18.6%</td>
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
<td align="right">4,495</td>
<td align="right">4.7%</td>
<td align="right">168,428</td>
<td align="right">46.8%</td>
<td align="right">3,647.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,015</td>
<td align="right">3.2%</td>
<td align="right">82,831</td>
<td align="right">23.0%</td>
<td align="right">2,647.3%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">734</td>
<td align="right">0.2%</td>
<td align="right">321.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,873</td>
<td align="right">6.2%</td>
<td align="right">21,319</td>
<td align="right">5.9%</td>
<td align="right">263.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,247</td>
<td align="right">2.4%</td>
<td align="right">7,804</td>
<td align="right">2.2%</td>
<td align="right">247.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">642</td>
<td align="right">0.2%</td>
<td align="right">96.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,567</td>
<td align="right">1.7%</td>
<td align="right">293</td>
<td align="right">0.1%</td>
<td align="right">-81.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,546</td>
<td align="right">4.8%</td>
<td align="right">1,942</td>
<td align="right">0.5%</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4,174</td>
<td align="right">4.4%</td>
<td align="right">6,556</td>
<td align="right">1.8%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">945</td>
<td align="right">1.0%</td>
<td align="right">539</td>
<td align="right">0.1%</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,771</td>
<td align="right">11.4%</td>
<td align="right">6,666</td>
<td align="right">1.9%</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,867</td>
<td align="right">3.0%</td>
<td align="right">3,309</td>
<td align="right">0.9%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">53,740</td>
<td align="right">56.6%</td>
<td align="right">58,321</td>
<td align="right">16.2%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">130</td>
<td align="right">0.0%</td>
<td align="right">-3.0%</td>
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
<td align="right">478,863,186</td>
<td align="right">3.7%</td>
<td align="right">256,707,292</td>
<td align="right">2.1%</td>
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
<td align="right">391,509,486</td>
<td align="right">3.1%</td>
<td align="right">483,225,284</td>
<td align="right">3.9%</td>
<td align="right">23.4%</td>
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
<td align="right">1,354,141</td>
<td align="right">0.0%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,944,479,163</td>
<td align="right">93.2%</td>
<td align="right">11,748,301,159</td>
<td align="right">94.1%</td>
<td align="right">-1.6%</td>
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
<td align="right">7,403,903</td>
<td align="right">95.9%</td>
<td align="right">9,132,813</td>
<td align="right">96.4%</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">318,523</td>
<td align="right">4.1%</td>
<td align="right">336,273</td>
<td align="right">3.6%</td>
<td align="right">5.6%</td>
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
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">314</td>
<td align="right">0.1%</td>
<td align="right">36</td>
<td align="right">0.0%</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">95</td>
<td align="right">0.0%</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,438</td>
<td align="right">1.4%</td>
<td align="right">1,804</td>
<td align="right">0.5%</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,340</td>
<td align="right">1.0%</td>
<td align="right">1,487</td>
<td align="right">0.4%</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">57,340</td>
<td align="right">18.0%</td>
<td align="right">26,816</td>
<td align="right">8.0%</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">38,449</td>
<td align="right">12.1%</td>
<td align="right">20,945</td>
<td align="right">6.2%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.3%</td>
<td align="right">602</td>
<td align="right">0.2%</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,582</td>
<td align="right">0.5%</td>
<td align="right">919</td>
<td align="right">0.3%</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40,821</td>
<td align="right">12.8%</td>
<td align="right">24,101</td>
<td align="right">7.2%</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,282</td>
<td align="right">1.3%</td>
<td align="right">2,562</td>
<td align="right">0.8%</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23,678</td>
<td align="right">7.4%</td>
<td align="right">15,622</td>
<td align="right">4.6%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,347</td>
<td align="right">2.3%</td>
<td align="right">6,227</td>
<td align="right">1.9%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,261</td>
<td align="right">2.0%</td>
<td align="right">6,101</td>
<td align="right">1.8%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">163</td>
<td align="right">0.1%</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">-1.8%</td>
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
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">3,624,378,043</td>
<td align="right">99.6%</td>
<td align="right">8,806,168,136</td>
<td align="right">99.8%</td>
<td align="right">143.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,594</td>
<td align="right">0.0%</td>
<td align="right">1,954</td>
<td align="right">0.0%</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,707</td>
<td align="right">0.0%</td>
<td align="right">52,189</td>
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
<td align="right">14,622,658</td>
<td align="right">0.4%</td>
<td align="right">14,622,494</td>
<td align="right">0.2%</td>
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
<td align="right">138,371</td>
<td align="right">100.0%</td>
<td align="right">136,800</td>
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

### LOAD_METHOD

<details>
<summary> specialization stats for LOAD_METHOD family </summary>

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
<td align="right">141,751,771</td>
<td align="right">51.8%</td>
<td align="right">232,684,283</td>
<td align="right">72.5%</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">131,539,183</td>
<td align="right">48.1%</td>
<td align="right">88,267,946</td>
<td align="right">27.5%</td>
<td align="right">-32.9%</td>
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
<td align="right">2,739,923</td>
<td align="right">97.1%</td>
<td align="right">4,455,210</td>
<td align="right">98.7%</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">80,426</td>
<td align="right">2.9%</td>
<td align="right">57,347</td>
<td align="right">1.3%</td>
<td align="right">-28.7%</td>
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
<td align="left">overridden</td>
<td align="right">347</td>
<td align="right">0.4%</td>
<td align="right">1,232</td>
<td align="right">2.1%</td>
<td align="right">255.0%</td>
</tr>
<tr>
<td align="left">kind 12</td>
<td align="right">332</td>
<td align="right">0.4%</td>
<td align="right">129</td>
<td align="right">0.2%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">kind 13</td>
<td align="right">321</td>
<td align="right">0.4%</td>
<td align="right">181</td>
<td align="right">0.3%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">70,578</td>
<td align="right">87.8%</td>
<td align="right">49,403</td>
<td align="right">86.1%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">kind 18</td>
<td align="right">1,628</td>
<td align="right">2.0%</td>
<td align="right">1,383</td>
<td align="right">2.4%</td>
<td align="right">-15.0%</td>
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
<td align="right">64,061,338</td>
<td align="right">100.0%</td>
<td align="right">62,678,941</td>
<td align="right">100.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">33</td>
<td align="right">0.0%</td>
<td align="right">33</td>
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
<td align="right">157</td>
<td align="right">100.0%</td>
<td align="right">157</td>
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

### LOAD_SUPER_METHOD

<details>
<summary> specialization stats for LOAD_SUPER_METHOD family </summary>

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
<td align="right">220</td>
<td align="right">8.7%</td>
<td align="right">220</td>
<td align="right">8.7%</td>
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
<td align="right">2,298</td>
<td align="right">100.0%</td>
<td align="right">2,298</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,711</td>
<td align="right">0.0%</td>
<td align="right">7,390</td>
<td align="right">0.0%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">593,288,791</td>
<td align="right">82.2%</td>
<td align="right">592,945,562</td>
<td align="right">82.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,815,787</td>
<td align="right">17.8%</td>
<td align="right">128,804,788</td>
<td align="right">17.8%</td>
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
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">522</td>
<td align="right">1.5%</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,412</td>
<td align="right">98.1%</td>
<td align="right">34,117</td>
<td align="right">98.5%</td>
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
<td align="left">list</td>
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">2,966</td>
<td align="right">8.7%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">71.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">5,959</td>
<td align="right">17.5%</td>
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
<td align="right">69,132,086</td>
<td align="right">3.4%</td>
<td align="right">32,415,824</td>
<td align="right">1.7%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">99,915,451</td>
<td align="right">4.9%</td>
<td align="right">75,569,194</td>
<td align="right">3.9%</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,859,442,700</td>
<td align="right">91.7%</td>
<td align="right">1,810,680,112</td>
<td align="right">94.4%</td>
<td align="right">-2.6%</td>
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
<td align="right">50,812</td>
<td align="right">2.6%</td>
<td align="right">30,079</td>
<td align="right">2.0%</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,926,617</td>
<td align="right">97.4%</td>
<td align="right">1,467,942</td>
<td align="right">98.0%</td>
<td align="right">-23.8%</td>
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
<td align="right">126,851</td>
<td align="right">249.6%</td>
<td align="right">226,742</td>
<td align="right">753.8%</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,954</td>
<td align="right">9.7%</td>
<td align="right">1,651</td>
<td align="right">5.5%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,098</td>
<td align="right">10.0%</td>
<td align="right">2,154</td>
<td align="right">7.2%</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">350</td>
<td align="right">1.2%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.2%</td>
<td align="right">827</td>
<td align="right">2.7%</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">57</td>
<td align="right">0.2%</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">23,917</td>
<td align="right">47.1%</td>
<td align="right">13,900</td>
<td align="right">46.2%</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">70</td>
<td align="right">0.2%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">15.1%</td>
<td align="right">4,930</td>
<td align="right">16.4%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">245</td>
<td align="right">0.8%</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.4%</td>
<td align="right">519</td>
<td align="right">1.7%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">810</td>
<td align="right">1.6%</td>
<td align="right">733</td>
<td align="right">2.4%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,352</td>
<td align="right">6.6%</td>
<td align="right">3,322</td>
<td align="right">11.0%</td>
<td align="right">-0.9%</td>
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
<td align="right">1,194,074</td>
<td align="right">100.0%</td>
<td align="right">112,189,224</td>
<td align="right">100.0%</td>
<td align="right">9,295.5%</td>
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
<td align="right">133,584,487</td>
<td align="right">12.7%</td>
<td align="right">470,083,046</td>
<td align="right">34.0%</td>
<td align="right">251.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">919,761,323</td>
<td align="right">87.3%</td>
<td align="right">912,741,429</td>
<td align="right">66.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">43,780</td>
<td align="right">95.2%</td>
<td align="right">120,322</td>
<td align="right">98.2%</td>
<td align="right">174.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,195</td>
<td align="right">4.8%</td>
<td align="right">2,147</td>
<td align="right">1.8%</td>
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
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.8%</td>
<td align="right">86,547</td>
<td align="right">71.9%</td>
<td align="right">25,280.4%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">236</td>
<td align="right">0.5%</td>
<td align="right">5,187</td>
<td align="right">4.3%</td>
<td align="right">2,097.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">502</td>
<td align="right">1.1%</td>
<td align="right">1,662</td>
<td align="right">1.4%</td>
<td align="right">231.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,703</td>
<td align="right">38.2%</td>
<td align="right">4,855</td>
<td align="right">4.0%</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,031</td>
<td align="right">6.9%</td>
<td align="right">1,432</td>
<td align="right">1.2%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">14,756</td>
<td align="right">33.7%</td>
<td align="right">13,067</td>
<td align="right">10.9%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">8,143</td>
<td align="right">18.6%</td>
<td align="right">7,504</td>
<td align="right">6.2%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">40,993,719</td>
<td align="right">0.9%</td>
<td align="right">69,212,093</td>
<td align="right">1.4%</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">102,061,285</td>
<td align="right">2.2%</td>
<td align="right">90,117,345</td>
<td align="right">1.9%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,444,719,540</td>
<td align="right">96.9%</td>
<td align="right">4,652,671,459</td>
<td align="right">96.7%</td>
<td align="right">4.7%</td>
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
<td align="right">822,116</td>
<td align="right">66.5%</td>
<td align="right">1,353,964</td>
<td align="right">75.6%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">414,364</td>
<td align="right">33.5%</td>
<td align="right">435,989</td>
<td align="right">24.4%</td>
<td align="right">5.2%</td>
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
<td align="right">16,381</td>
<td align="right">4.0%</td>
<td align="right">79,288</td>
<td align="right">18.2%</td>
<td align="right">384.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,540</td>
<td align="right">1.1%</td>
<td align="right">12,430</td>
<td align="right">2.9%</td>
<td align="right">173.8%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">262</td>
<td align="right">0.1%</td>
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">13,478</td>
<td align="right">3.3%</td>
<td align="right">2,959</td>
<td align="right">0.7%</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,619</td>
<td align="right">2.1%</td>
<td align="right">3,581</td>
<td align="right">0.8%</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,348</td>
<td align="right">3.0%</td>
<td align="right">5,996</td>
<td align="right">1.4%</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">94,086</td>
<td align="right">22.7%</td>
<td align="right">64,212</td>
<td align="right">14.7%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">5,689</td>
<td align="right">1.4%</td>
<td align="right">5,071</td>
<td align="right">1.2%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,501</td>
<td align="right">62.1%</td>
<td align="right">261,010</td>
<td align="right">59.9%</td>
<td align="right">1.4%</td>
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
<td align="left">memory view</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">3,260</td>
<td align="right">0.0%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,427,399</td>
<td align="right">0.1%</td>
<td align="right">1,267,172</td>
<td align="right">0.1%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,233,561,123</td>
<td align="right">99.9%</td>
<td align="right">1,226,413,479</td>
<td align="right">99.9%</td>
<td align="right">-0.6%</td>
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
<td align="right">866</td>
<td align="right">6.9%</td>
<td align="right">688</td>
<td align="right">5.7%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,601</td>
<td align="right">93.1%</td>
<td align="right">11,369</td>
<td align="right">94.3%</td>
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
<td align="left">sequence</td>
<td align="right">639</td>
<td align="right">73.8%</td>
<td align="right">484</td>
<td align="right">70.3%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">10.5%</td>
<td align="right">69</td>
<td align="right">10.0%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.7%</td>
<td align="right">135</td>
<td align="right">19.6%</td>
<td align="right">-0.7%</td>
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
<td align="right">2,148,757,160</td>
<td align="right">2.7%</td>
<td align="right">5,010,293,870</td>
<td align="right">5.4%</td>
<td align="right">133.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">871,457,854</td>
<td align="right">1.1%</td>
<td align="right">1,076,848,791</td>
<td align="right">1.2%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">47,291,401,597</td>
<td align="right">59.8%</td>
<td align="right">55,526,565,593</td>
<td align="right">59.4%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">28,791,272,173</td>
<td align="right">36.4%</td>
<td align="right">31,821,745,139</td>
<td align="right">34.1%</td>
<td align="right">10.5%</td>
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
<td align="right">118,788,479</td>
<td align="right">5.5%</td>
<td align="right">1,252,268,661</td>
<td align="right">25.0%</td>
<td align="right">954.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">87,841,361</td>
<td align="right">4.1%</td>
<td align="right">382,689,595</td>
<td align="right">7.6%</td>
<td align="right">335.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">451,733,345</td>
<td align="right">21.1%</td>
<td align="right">1,873,162,072</td>
<td align="right">37.4%</td>
<td align="right">314.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,584,487</td>
<td align="right">6.2%</td>
<td align="right">470,083,046</td>
<td align="right">9.4%</td>
<td align="right">251.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">478,863,186</td>
<td align="right">22.3%</td>
<td align="right">256,707,292</td>
<td align="right">5.1%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">276,655,200</td>
<td align="right">12.9%</td>
<td align="right">182,645,797</td>
<td align="right">3.6%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">131,539,183</td>
<td align="right">6.1%</td>
<td align="right">88,267,946</td>
<td align="right">1.8%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">102,061,285</td>
<td align="right">4.8%</td>
<td align="right">90,117,345</td>
<td align="right">1.8%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,787</td>
<td align="right">6.0%</td>
<td align="right">128,804,788</td>
<td align="right">2.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,363,181</td>
<td align="right">4.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">112,189,224</td>
<td align="right">2.2%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">19,289,307</td>
<td align="right">2.2%</td>
<td align="right">35,234,804</td>
<td align="right">3.3%</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">133,997,642</td>
<td align="right">15.4%</td>
<td align="right">227,092,617</td>
<td align="right">21.1%</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">195,914,984</td>
<td align="right">22.5%</td>
<td align="right">277,624,326</td>
<td align="right">25.8%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">54,162,777</td>
<td align="right">6.2%</td>
<td align="right">68,942,377</td>
<td align="right">6.4%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">78,279,157</td>
<td align="right">9.0%</td>
<td align="right">64,563,218</td>
<td align="right">6.0%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">75,251,462</td>
<td align="right">8.6%</td>
<td align="right">85,071,558</td>
<td align="right">7.9%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,238,927</td>
<td align="right">2.4%</td>
<td align="right">20,014,807</td>
<td align="right">1.9%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,872,923</td>
<td align="right">2.4%</td>
<td align="right">20,154,687</td>
<td align="right">1.9%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,429,221</td>
<td align="right">8.7%</td>
<td align="right">76,351,551</td>
<td align="right">7.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">21,600,759</td>
<td align="right">2.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">31,319,802</td>
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
<td align="left">Frame objects created</td>
<td align="right">71,636,910</td>
<td align="right">1.1%</td>
<td align="right">67,688,168</td>
<td align="right">1.0%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,455,731,600</td>
<td align="right">81.6%</td>
<td align="right">5,395,814,600</td>
<td align="right">81.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,196,436</td>
<td align="right">4.2%</td>
<td align="right">276,294,470</td>
<td align="right">4.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,062,892,224</td>
<td align="right">75.7%</td>
<td align="right">5,012,792,533</td>
<td align="right">75.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">950,963,961</td>
<td align="right">14.2%</td>
<td align="right">943,381,096</td>
<td align="right">14.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">953,096,104</td>
<td align="right">14.3%</td>
<td align="right">945,513,239</td>
<td align="right">14.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,407,242</td>
<td align="right">3.9%</td>
<td align="right">262,924,029</td>
<td align="right">4.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,623,673,549</td>
<td align="right">24.3%</td>
<td align="right">1,615,751,632</td>
<td align="right">24.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,623,673,549</td>
<td align="right">24.3%</td>
<td align="right">1,615,751,632</td>
<td align="right">24.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,100</td>
<td align="right">0.4%</td>
<td align="right">24,834,001</td>
<td align="right">0.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,577,445</td>
<td align="right">10.0%</td>
<td align="right">670,238,393</td>
<td align="right">10.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,247</td>
<td align="right">0.0%</td>
<td align="right">2,128,247</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="left">Interpreter immortal decrefs</td>
<td align="right">16,004,341,525</td>
<td align="right">8.0%</td>
<td align="right">24,744,179,071</td>
<td align="right">12.9%</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">8,557,199,634</td>
<td align="right">5.3%</td>
<td align="right">11,099,185,368</td>
<td align="right">7.1%</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">46,313,035,571</td>
<td align="right">23.1%</td>
<td align="right">57,808,144,499</td>
<td align="right">30.2%</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">83,572,137,716</td>
<td align="right">41.6%</td>
<td align="right">64,761,494,178</td>
<td align="right">33.9%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">54,910,844,563</td>
<td align="right">27.3%</td>
<td align="right">43,834,566,044</td>
<td align="right">22.9%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">34,383,310,301</td>
<td align="right">21.3%</td>
<td align="right">40,655,194,981</td>
<td align="right">26.1%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">78,474,284,496</td>
<td align="right">48.7%</td>
<td align="right">64,975,312,698</td>
<td align="right">41.7%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,166</td>
<td align="right">2.5%</td>
<td align="right">3,778,566</td>
<td align="right">2.2%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">476,016</td>
<td align="right">0.3%</td>
<td align="right">434,156</td>
<td align="right">0.3%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,222,380,515</td>
<td align="right"></td>
<td align="right">2,363,090,370</td>
<td align="right"></td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">10,869,053</td>
<td align="right"></td>
<td align="right">10,258,519</td>
<td align="right"></td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,242,959</td>
<td align="right"></td>
<td align="right">172,589,504</td>
<td align="right"></td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">39,763,979,473</td>
<td align="right">24.7%</td>
<td align="right">38,968,572,589</td>
<td align="right">25.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">69,905,179</td>
<td align="right"></td>
<td align="right">68,778,632</td>
<td align="right"></td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">59,847,387</td>
<td align="right"></td>
<td align="right">59,330,386</td>
<td align="right"></td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">7,177,192,970</td>
<td align="right">39.1%</td>
<td align="right">7,118,452,412</td>
<td align="right">39.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">7,255,139,549</td>
<td align="right">39.5%</td>
<td align="right">7,196,214,989</td>
<td align="right">39.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">7,845,548,197</td>
<td align="right"></td>
<td align="right">7,786,073,774</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,420,607</td>
<td align="right">0.0%</td>
<td align="right">6,468,252</td>
<td align="right">0.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,091,717,464</td>
<td align="right">60.5%</td>
<td align="right">11,033,341,819</td>
<td align="right">60.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,091,811,264</td>
<td align="right"></td>
<td align="right">11,033,447,090</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,931,011,047</td>
<td align="right"></td>
<td align="right">2,945,916,519</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,525,972</td>
<td align="right">0.4%</td>
<td align="right">71,294,325</td>
<td align="right">0.4%</td>
<td align="right">-0.3%</td>
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
<td align="right">363,551</td>
<td align="right">103,124,275</td>
<td align="right">9,336,751,186</td>
<td align="right">734,399,937</td>
<td align="right">762,228,197</td>
<td align="right">362,508</td>
<td align="right">101,843,018</td>
<td align="right">9,308,053,627</td>
<td align="right">737,431,479</td>
<td align="right">759,447,050</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,607,319,028</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,607,217,138</td>
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
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">492,542</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">69,568</td>
<td align="right">14.1%</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">265</td>
<td align="right">0.1%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">381,129</td>
<td align="right">77.4%</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">422,709</td>
<td align="right">85.8%</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">988</td>
<td align="right">0.2%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,104</td>
<td align="right">0.6%</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">896</td>
<td align="right">0.2%</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">501</td>
<td align="right">0.7%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,027,474,636</td>
<td align="right"></td>
<td align="right">9,168,521,092</td>
<td align="right"></td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">272,840,911,322</td>
<td align="right">3,882.5%</td>
<td align="right">312,701,972,790</td>
<td align="right">3,410.6%</td>
<td align="right">14.6%</td>
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
<td align="right">69,568</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">63,549</td>
<td align="right">91.3%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">6,049</td>
<td align="right">8.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,549</td>
<td align="right">12.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">22,009</td>
<td align="right">31.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">17,220</td>
<td align="right">24.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,945</td>
<td align="right">12.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,895</td>
<td align="right">8.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">819</td>
<td align="right">1.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">82</td>
<td align="right">0.1%</td>
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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">2,002</td>
<td align="right">2.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">8,547</td>
<td align="right">12.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">9,806</td>
<td align="right">14.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">24,261</td>
<td align="right">34.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">12,893</td>
<td align="right">18.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,341</td>
<td align="right">6.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,391</td>
<td align="right">2.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">308</td>
<td align="right">0.4%</td>
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
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,598,079</td>
<td align="right">2,107,638,388</td>
<td align="right">31,843.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">11,171,242</td>
<td align="right">3,511,537,498</td>
<td align="right">31,333.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">11,171,242</td>
<td align="right">3,510,584,601</td>
<td align="right">31,325.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right">3,840,960</td>
<td align="right">764,569,531</td>
<td align="right">19,805.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">31,135,120</td>
<td align="right">4,734,948,111</td>
<td align="right">15,107.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">31,491,440</td>
<td align="right">3,329,331,580</td>
<td align="right">10,472.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">559,470</td>
<td align="right">50,972,724</td>
<td align="right">9,010.9%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">2,615,370</td>
<td align="right">172,625,639</td>
<td align="right">6,500.4%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">1,228,800</td>
<td align="right">73,997,277</td>
<td align="right">5,921.9%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">63,256,142</td>
<td align="right">3,513,551,577</td>
<td align="right">5,454.5%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">98,482</td>
<td align="right">3,489,314</td>
<td align="right">3,443.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">123,165</td>
<td align="right">2,874,150</td>
<td align="right">2,233.6%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">97,901,643</td>
<td align="right">2,256,010,605</td>
<td align="right">2,204.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">97,901,643</td>
<td align="right">2,246,354,133</td>
<td align="right">2,194.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">23,692,642</td>
<td align="right">380,649,881</td>
<td align="right">1,506.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">25,592,949</td>
<td align="right">385,966,234</td>
<td align="right">1,408.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">25,592,949</td>
<td align="right">385,934,693</td>
<td align="right">1,408.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">217,878,693</td>
<td align="right">3,055,498,491</td>
<td align="right">1,302.4%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,202,669</td>
<td align="right">43,097,463</td>
<td align="right">1,245.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,721,878</td>
<td align="right">22,478,982</td>
<td align="right">1,205.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">1,786,835</td>
<td align="right">23,189,327</td>
<td align="right">1,197.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">9,967,628</td>
<td align="right">1,122.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">4,220,886</td>
<td align="right">985.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">7,434,163</td>
<td align="right">75,508,767</td>
<td align="right">915.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">12,408,559</td>
<td align="right">88,643,979</td>
<td align="right">614.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,149,778</td>
<td align="right">42,847,287</td>
<td align="right">596.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_METHOD_METHOD</td>
<td align="right">7,039,718</td>
<td align="right">45,902,060</td>
<td align="right">552.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">4,434,531</td>
<td align="right">26,957,461</td>
<td align="right">507.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">667,475,012</td>
<td align="right">3,627,844,725</td>
<td align="right">443.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">414,599,094</td>
<td align="right">2,107,682,844</td>
<td align="right">408.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">738,434,961</td>
<td align="right">3,696,221,519</td>
<td align="right">400.5%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">1,250,434</td>
<td align="right">6,256,873</td>
<td align="right">400.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">32,541,839</td>
<td align="right">160,670,702</td>
<td align="right">393.7%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">20,508,151</td>
<td align="right">93,062,995</td>
<td align="right">353.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">195,739,205</td>
<td align="right">863,183,516</td>
<td align="right">341.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">35,409,921</td>
<td align="right">155,225,706</td>
<td align="right">338.4%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">36,493,421</td>
<td align="right">155,479,945</td>
<td align="right">326.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,235,798,450</td>
<td align="right">34,408,411,788</td>
<td align="right">272.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,291,715,790</td>
<td align="right">4,434,975,346</td>
<td align="right">243.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">29,356,644</td>
<td align="right">75,110,406</td>
<td align="right">155.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">30,120,677</td>
<td align="right">75,152,981</td>
<td align="right">149.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">15,468,999</td>
<td align="right">35,027,415</td>
<td align="right">126.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,375,774,594</td>
<td align="right">7,637,162,386</td>
<td align="right">126.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">18,019,971</td>
<td align="right">40,746,905</td>
<td align="right">126.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">725,002,941</td>
<td align="right">1,569,431,319</td>
<td align="right">116.5%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">497,139</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">123,515,060</td>
<td align="right">582,278</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,219,140,855</td>
<td align="right">8,345,135,913</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">4,378,540,585</td>
<td align="right">8,651,058,591</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,278,080</td>
<td align="right">1,992,065</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">764,033</td>
<td align="right">43,310</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">764,033</td>
<td align="right">43,322</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,093,935</td>
<td align="right">6,001,798</td>
<td align="right">94.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">94,182,797</td>
<td align="right">182,007,689</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,087,315,571</td>
<td align="right">97,933,591</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">3,892,080</td>
<td align="right">7,355,964</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">3,892,080</td>
<td align="right">7,354,137</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">209,130,611</td>
<td align="right">394,301,937</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">504,557,241</td>
<td align="right">62,801,615</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">78,948,146</td>
<td align="right">11,042,160</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">21,250,758</td>
<td align="right">39,382,597</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,388,857,812</td>
<td align="right">222,963,809</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,220,713,010</td>
<td align="right">235,898,229</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,521,200,430</td>
<td align="right">509,705,295</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,060,242,764</td>
<td align="right">1,246,298,574</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">319,239,906</td>
<td align="right">560,540,590</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,030,397,729</td>
<td align="right">1,256,198,525</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,902,307,478</td>
<td align="right">504,810,550</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,690,915,809</td>
<td align="right">455,992,605</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,579,400</td>
<td align="right">6,151,440</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,073,959,507</td>
<td align="right">601,097,586</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,374,142,470</td>
<td align="right">399,891,795</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">765,490,744</td>
<td align="right">226,644,418</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,873,078,985</td>
<td align="right">562,421,641</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,930,233,265</td>
<td align="right">598,429,720</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">191,943,184</td>
<td align="right">60,020,986</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,927,516,241</td>
<td align="right">637,931,551</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">853,160,788</td>
<td align="right">285,357,540</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">357,606,941</td>
<td align="right">594,103,295</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,817,233,108</td>
<td align="right">2,997,974,524</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">429,326,483</td>
<td align="right">158,904,781</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">722,722,189</td>
<td align="right">1,177,607,511</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">791,448,921</td>
<td align="right">300,322,323</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">567,295,390</td>
<td align="right">231,883,329</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">72,281,603</td>
<td align="right">111,010,830</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">47,744,932</td>
<td align="right">22,762,647</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">510,086,040</td>
<td align="right">246,994,153</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,112,372,964</td>
<td align="right">1,038,347,699</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">376,098,346</td>
<td align="right">185,188,427</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_NO_DICT</td>
<td align="right">1,848,972,709</td>
<td align="right">942,625,631</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">557,419,457</td>
<td align="right">297,383,764</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">484,031,819</td>
<td align="right">262,182,985</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">484,982,159</td>
<td align="right">263,533,453</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">269,263,477</td>
<td align="right">147,347,774</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">38,540,011</td>
<td align="right">55,952,003</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">386,839,399</td>
<td align="right">560,619,892</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,456,877,501</td>
<td align="right">2,107,682,844</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">174,837,192</td>
<td align="right">252,897,987</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">94,536,125</td>
<td align="right">136,634,728</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,281,690,274</td>
<td align="right">3,272,934,608</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">545,770,423</td>
<td align="right">312,329,948</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">50,223,440</td>
<td align="right">29,339,806</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_LAZY_DICT</td>
<td align="right">50,223,440</td>
<td align="right">29,339,806</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,661,316,249</td>
<td align="right">2,330,196,572</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,483,023</td>
<td align="right">24,469,358</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">97,102,470</td>
<td align="right">59,357,302</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">8,039,832</td>
<td align="right">11,152,151</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,724,534,627</td>
<td align="right">2,391,756,184</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">579,038,740</td>
<td align="right">358,311,600</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">579,038,740</td>
<td align="right">358,720,560</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,034,675,966</td>
<td align="right">1,889,705,664</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,307,425,687</td>
<td align="right">5,258,267,833</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">311,545,082</td>
<td align="right">205,861,908</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">221,438,860</td>
<td align="right">288,325,482</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">246,442,940</td>
<td align="right">172,105,815</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,514,461,273</td>
<td align="right">3,261,346,770</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,514,370,307</td>
<td align="right">3,259,148,632</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">40,381,739</td>
<td align="right">28,738,900</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">40,382,739</td>
<td align="right">28,751,311</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">114,381,818</td>
<td align="right">81,993,704</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">285,346,375</td>
<td align="right">365,720,595</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">158,839,806</td>
<td align="right">203,163,382</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">654,424,625</td>
<td align="right">834,405,572</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">83,995,286</td>
<td align="right">107,004,474</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,292,451,827</td>
<td align="right">1,644,181,586</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">88,674,344</td>
<td align="right">112,444,943</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">753,246,596</td>
<td align="right">554,257,039</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,291,550,052</td>
<td align="right">1,631,895,472</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,649,219</td>
<td align="right">8,365,321</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">31,289,579,606</td>
<td align="right">23,357,269,194</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">425,009,536</td>
<td align="right">530,075,933</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">81,693,331</td>
<td align="right">101,205,541</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_WITH_VALUES</td>
<td align="right">1,205,467,271</td>
<td align="right">1,483,800,990</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">243,320,941</td>
<td align="right">298,932,291</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,180,047</td>
<td align="right">143,030,141</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">991,819,761</td>
<td align="right">1,210,608,594</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">92,574,051</td>
<td align="right">112,471,448</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,870,382,548</td>
<td align="right">2,245,751,649</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">107,081,228</td>
<td align="right">126,753,638</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">647,257,297</td>
<td align="right">529,650,482</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">165,623,630</td>
<td align="right">195,682,300</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">29,947,971</td>
<td align="right">24,718,282</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">29,947,971</td>
<td align="right">24,718,282</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">410,292,443</td>
<td align="right">476,007,103</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">667,420,039</td>
<td align="right">773,956,544</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">582,669,486</td>
<td align="right">675,674,628</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">103,595,549</td>
<td align="right">119,694,393</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">415,548,916</td>
<td align="right">479,576,608</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">415,548,916</td>
<td align="right">479,570,542</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">79,480,498</td>
<td align="right">89,851,817</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,562,685,127</td>
<td align="right">1,371,967,961</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,352,131,986</td>
<td align="right">1,507,273,927</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">48,642,140</td>
<td align="right">53,969,566</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">173,640,571</td>
<td align="right">192,039,633</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,908,450,628</td>
<td align="right">9,828,936,160</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">78,207,214</td>
<td align="right">86,235,086</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">48,289,055</td>
<td align="right">53,150,474</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">37,367,003</td>
<td align="right">33,626,345</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,304,301</td>
<td align="right">44,295,678</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">953,572,879</td>
<td align="right">1,044,507,120</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">71,268,749</td>
<td align="right">77,646,780</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">309,128,764</td>
<td align="right">334,616,910</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">71,268,749</td>
<td align="right">76,838,359</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">25,978,942,796</td>
<td align="right">27,864,842,172</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">170,508,734</td>
<td align="right">180,709,058</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">294,127,197</td>
<td align="right">310,951,210</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,062,820</td>
<td align="right">49,688,018</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">101,400,832</td>
<td align="right">106,947,922</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">803,471,237</td>
<td align="right">845,091,828</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,259,488</td>
<td align="right">25,347,860</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD</td>
<td align="right">171,083,172</td>
<td align="right">178,684,659</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">293,909,247</td>
<td align="right">306,657,925</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">382,568,146</td>
<td align="right">397,923,858</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">208,970,905</td>
<td align="right">216,237,660</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,444,371,401</td>
<td align="right">4,316,316,299</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">43,673,900</td>
<td align="right">44,461,277</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,644,602</td>
<td align="right">47,405,590</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,452,808,138</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,027,474,636</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">5,969,303,179</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,893,048,649</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,438,715,937</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">4,775,265,953</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,620,798,592</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,286,838,606</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,143,100,115</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,803,372,750</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,222,552,053</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,926,363,957</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,910,223,050</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,849,490,381</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,425,333,502</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,494,182,078</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,191,464,937</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,159,406,814</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,050,727,126</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,034,287,049</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,015,629,181</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">898,921,756</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">703,599,088</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">703,027,159</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">592,121,097</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">524,148,555</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">500,430,593</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">496,746,151</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">446,354,896</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">364,490,849</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">305,402,425</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">196,687,406</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">173,923,488</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">152,276,195</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">148,613,302</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">143,688,607</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">123,807,555</td>
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
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">56,439,939</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">54,541,430</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">52,084,900</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">13,165,084</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">181,915</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">67,865,890,289</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP</td>
<td align="right"></td>
<td align="right">2,991,418,031</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_NONE</td>
<td align="right"></td>
<td align="right">486,384,173</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">477,515,662</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">193,102,469</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_FOR</td>
<td align="right"></td>
<td align="right">100,178,987</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">93,154,822</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">14,673,423</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right"></td>
<td align="right">4,003,366</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right"></td>
<td align="right">1,602,339</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right"></td>
<td align="right">947,591</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">880,973</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right"></td>
<td align="right">780,400</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">574,615</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">572,808</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">380,786</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">84,304</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right"></td>
<td align="right">18,962</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right"></td>
<td align="right">1,579</td>
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
<td align="right">24,277</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,428</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">7,282</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">84</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">160</td>
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
<td align="right">160</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
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
Stats gathered on: 2025-01-27
