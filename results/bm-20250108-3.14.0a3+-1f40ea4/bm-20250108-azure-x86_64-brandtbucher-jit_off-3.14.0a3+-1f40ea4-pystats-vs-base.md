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
<td align="left">SET_ADD</td>
<td align="right">1,436,308</td>
<td align="right">59,548</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">5,919,241</td>
<td align="right">1,645,921</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1,829,746</td>
<td align="right">773,585</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">107,326,786</td>
<td align="right">60,615,198</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">26,404,898</td>
<td align="right">15,695,595</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">34,916,957</td>
<td align="right">23,493,526</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">6,407,818</td>
<td align="right">4,536,169</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">3,832</td>
<td align="right">2,752</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,319,365,762</td>
<td align="right">972,651,836</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">93,113,069</td>
<td align="right">72,981,215</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">118,458,641</td>
<td align="right">93,612,902</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">119,071,617</td>
<td align="right">94,919,711</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">103,689,266</td>
<td align="right">83,641,175</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">83,383,638</td>
<td align="right">67,299,414</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">70,635,606</td>
<td align="right">57,735,795</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">83,009,331</td>
<td align="right">69,666,009</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">100,228,643</td>
<td align="right">84,423,529</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">183,516,083</td>
<td align="right">155,794,967</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">15,898,540</td>
<td align="right">13,549,216</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,909,746,887</td>
<td align="right">1,637,940,604</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">78,405,741</td>
<td align="right">68,025,308</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">965,861,588</td>
<td align="right">841,932,773</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">315,475,234</td>
<td align="right">274,997,196</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">399,466,053</td>
<td align="right">348,327,483</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">188,814,300</td>
<td align="right">168,331,348</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">69,928,287</td>
<td align="right">62,370,326</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">86,497,652</td>
<td align="right">77,226,358</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">10,025,959</td>
<td align="right">8,973,187</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">402,696,067</td>
<td align="right">363,698,644</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">586,404,831</td>
<td align="right">530,096,872</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,620,929,729</td>
<td align="right">3,292,308,098</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">192,129,735</td>
<td align="right">175,326,858</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">9,778,041</td>
<td align="right">8,976,841</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">6,941,256,461</td>
<td align="right">6,483,417,054</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">225,800,606</td>
<td align="right">211,101,548</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,432,538,005</td>
<td align="right">3,212,723,366</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,152,422,636</td>
<td align="right">1,079,522,694</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,783,086,699</td>
<td align="right">5,426,892,333</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,218,436</td>
<td align="right">9,592,166</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,341,678,280</td>
<td align="right">1,263,915,880</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">709,078,255</td>
<td align="right">668,747,560</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">551,848,942</td>
<td align="right">520,552,623</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">75,780,316</td>
<td align="right">71,561,596</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">122,674,429</td>
<td align="right">115,847,624</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">408,792,221</td>
<td align="right">386,521,464</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">399,799,862</td>
<td align="right">378,656,065</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,662,113,472</td>
<td align="right">6,309,967,469</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,095,571,676</td>
<td align="right">1,037,694,536</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">238,392,161</td>
<td align="right">225,883,565</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,088,947,761</td>
<td align="right">3,885,715,347</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">117,150,500</td>
<td align="right">111,410,710</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,203,404,756</td>
<td align="right">2,097,573,207</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,447,968,499</td>
<td align="right">1,379,585,496</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">544,470,694</td>
<td align="right">518,963,262</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,811,589,095</td>
<td align="right">1,727,126,578</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">83,489,334</td>
<td align="right">79,693,996</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,055,579,138</td>
<td align="right">5,782,534,595</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,517,979</td>
<td align="right">11,006,836</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,482,904</td>
<td align="right">20,546,098</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">101,175,115</td>
<td align="right">96,769,223</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,813,444</td>
<td align="right">20,876,638</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,813,465</td>
<td align="right">20,876,659</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">252,780,642</td>
<td align="right">242,416,359</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">254,864,611</td>
<td align="right">244,472,988</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,668,192,411</td>
<td align="right">2,559,553,572</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,025,801,197</td>
<td align="right">984,181,224</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">38,947,228,275</td>
<td align="right">37,379,344,160</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">888,356,532</td>
<td align="right">853,325,850</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,246,315,074</td>
<td align="right">3,120,716,119</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">517,524,575</td>
<td align="right">498,491,283</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,279,728,327</td>
<td align="right">2,197,230,517</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">457,824,279</td>
<td align="right">441,569,779</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">273,932,630</td>
<td align="right">264,362,084</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">331,472,351</td>
<td align="right">320,238,621</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,685,183,338</td>
<td align="right">1,629,664,701</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">37,973,331</td>
<td align="right">36,783,957</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,576,847,442</td>
<td align="right">2,499,169,103</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">200,976,103</td>
<td align="right">195,031,869</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">553,974,613</td>
<td align="right">537,667,550</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,199,729</td>
<td align="right">6,998,249</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">75,402,726</td>
<td align="right">73,338,548</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,355,465,193</td>
<td align="right">11,045,371,223</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,046,312,370</td>
<td align="right">10,746,238,615</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">530,326,968</td>
<td align="right">516,503,696</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,875,350</td>
<td align="right">1,828,667</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">838,213,836</td>
<td align="right">817,888,306</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">809,864,607</td>
<td align="right">792,776,280</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,927,232,614</td>
<td align="right">4,823,541,343</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,775,752,294</td>
<td align="right">13,495,095,770</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,188,681,707</td>
<td align="right">2,145,655,259</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">338,846,867</td>
<td align="right">332,409,643</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,203,184,911</td>
<td align="right">1,181,150,043</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">794,782,430</td>
<td align="right">781,494,039</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,611,853,448</td>
<td align="right">1,586,966,597</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">793,140</td>
<td align="right">781,020</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,498,530,373</td>
<td align="right">1,476,768,591</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,425,114,476</td>
<td align="right">1,404,576,858</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">63,156,707</td>
<td align="right">62,253,707</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">296,889,714</td>
<td align="right">292,955,636</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">375,804,290</td>
<td align="right">370,844,201</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,529,236,023</td>
<td align="right">2,496,776,267</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,276,231,254</td>
<td align="right">2,247,181,495</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">422,144,333</td>
<td align="right">416,813,531</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,826,545,491</td>
<td align="right">5,759,413,495</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">155,452,449</td>
<td align="right">153,661,776</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,391,650,609</td>
<td align="right">1,376,078,100</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,785,915,863</td>
<td align="right">2,755,700,271</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,290,097,604</td>
<td align="right">1,276,158,640</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">928,295,854</td>
<td align="right">918,401,401</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">123,765,632</td>
<td align="right">122,481,392</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,381,731,612</td>
<td align="right">2,357,198,114</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">383,098,323</td>
<td align="right">379,282,040</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">261,207,205</td>
<td align="right">258,735,054</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">360,450,424</td>
<td align="right">357,054,361</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">156,182,593</td>
<td align="right">154,850,353</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">97,957,298</td>
<td align="right">97,151,904</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">635,488,459</td>
<td align="right">630,459,734</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,767,993</td>
<td align="right">7,710,291</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,070,003,583</td>
<td align="right">1,062,566,897</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">335,738,869</td>
<td align="right">333,840,522</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,119,578,437</td>
<td align="right">1,113,279,872</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,353,466,010</td>
<td align="right">7,317,409,236</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,733,862,513</td>
<td align="right">2,720,913,726</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,764,451,392</td>
<td align="right">1,756,318,529</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">227,627,706</td>
<td align="right">226,589,023</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,083,398,400</td>
<td align="right">1,078,541,705</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,104,680</td>
<td align="right">3,115,211</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,812,583</td>
<td align="right">3,799,983</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,421,332</td>
<td align="right">181,849,892</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">702,706,550</td>
<td align="right">701,064,595</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,183,559</td>
<td align="right">6,169,863</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">404,504,929</td>
<td align="right">403,678,270</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,965,637</td>
<td align="right">35,910,430</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">90,009,790</td>
<td align="right">89,873,131</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,673</td>
<td align="right">84,553</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,663,277,371</td>
<td align="right">1,661,031,786</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,657</td>
<td align="right">33,700</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">242,605,296</td>
<td align="right">242,349,585</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">352,959,308</td>
<td align="right">352,656,300</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,497,512,036</td>
<td align="right">3,494,523,520</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">156,532,334</td>
<td align="right">156,403,081</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,200,677</td>
<td align="right">1,199,717</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">420,263,783</td>
<td align="right">419,936,770</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">403,318</td>
<td align="right">403,032</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,640,888</td>
<td align="right">127,568,748</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">510,829,290</td>
<td align="right">510,547,330</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,543,082</td>
<td align="right">593,303,459</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,261,395,424</td>
<td align="right">1,260,966,304</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,458,051</td>
<td align="right">131,417,731</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">566,286,519</td>
<td align="right">566,123,065</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">101,034,145</td>
<td align="right">101,009,468</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">76,102,820</td>
<td align="right">76,086,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,662,567</td>
<td align="right">302,607,367</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">183,186,058</td>
<td align="right">183,162,899</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,964,947</td>
<td align="right">74,955,603</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">156,820,196</td>
<td align="right">156,807,836</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,781,273</td>
<td align="right">1,781,153</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">278,058,007</td>
<td align="right">278,047,297</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,539,371</td>
<td align="right">188,535,175</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,786</td>
<td align="right">120,784</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">76,990,436</td>
<td align="right">76,991,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,758,417</td>
<td align="right">14,758,341</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,378,248</td>
<td align="right">1,053,378,248</td>
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
<td align="right">128,850,579</td>
<td align="right">128,850,579</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,162,417</td>
<td align="right">115,162,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,686,498</td>
<td align="right">112,686,498</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">100,136,760</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">9,742,713</td>
<td align="right">9,742,713</td>
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
<td align="left">CLEANUP_THROW</td>
<td align="right">98,718</td>
<td align="right">98,718</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,157</td>
<td align="right">57,157</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,670</td>
<td align="right">56,670</td>
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
<td align="right">3,624</td>
<td align="right">3,624</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,648</td>
<td align="right">2,648</td>
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
<td align="right">152</td>
<td align="right">152</td>
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
<td align="right">1,082,181,579</td>
<td align="right">12.7%</td>
<td align="right">1,077,334,958</td>
<td align="right">12.7%</td>
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
<td align="right">38,021,219</td>
<td align="right">0.4%</td>
<td align="right">37,864,271</td>
<td align="right">0.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,400,973,086</td>
<td align="right">86.8%</td>
<td align="right">7,390,880,055</td>
<td align="right">86.9%</td>
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
<td align="right">1,209,754</td>
<td align="right">62.5%</td>
<td align="right">1,199,727</td>
<td align="right">62.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">724,445</td>
<td align="right">37.5%</td>
<td align="right">721,428</td>
<td align="right">37.6%</td>
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
<td align="left">and different types</td>
<td align="right">123</td>
<td align="right">0.0%</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,410</td>
<td align="right">0.1%</td>
<td align="right">1,250</td>
<td align="right">0.1%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">7,845</td>
<td align="right">0.6%</td>
<td align="right">7,175</td>
<td align="right">0.6%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">38,100</td>
<td align="right">3.1%</td>
<td align="right">36,683</td>
<td align="right">3.1%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">177,932</td>
<td align="right">14.7%</td>
<td align="right">172,229</td>
<td align="right">14.4%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,728</td>
<td align="right">0.7%</td>
<td align="right">8,513</td>
<td align="right">0.7%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,403</td>
<td align="right">0.1%</td>
<td align="right">1,384</td>
<td align="right">0.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">34,937</td>
<td align="right">2.9%</td>
<td align="right">34,537</td>
<td align="right">2.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">43,626</td>
<td align="right">3.6%</td>
<td align="right">43,342</td>
<td align="right">3.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">176,808</td>
<td align="right">14.6%</td>
<td align="right">175,803</td>
<td align="right">14.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">19,947</td>
<td align="right">1.6%</td>
<td align="right">19,867</td>
<td align="right">1.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,975</td>
<td align="right">2.8%</td>
<td align="right">33,969</td>
<td align="right">2.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,514</td>
<td align="right">1.9%</td>
<td align="right">23,511</td>
<td align="right">2.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">580,549</td>
<td align="right">48.0%</td>
<td align="right">580,524</td>
<td align="right">48.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,488</td>
<td align="right">1.6%</td>
<td align="right">19,488</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">18,901</td>
<td align="right">1.6%</td>
<td align="right">18,901</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">1.0%</td>
<td align="right">11,587</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">0.7%</td>
<td align="right">8,203</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.2%</td>
<td align="right">2,678</td>
<td align="right">0.2%</td>
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
<td align="right">182,421,332</td>
<td align="right">100.0%</td>
<td align="right">181,849,892</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,595,173,687</td>
<td align="right">70.1%</td>
<td align="right">5,504,833,010</td>
<td align="right">70.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,381,104,073</td>
<td align="right">29.8%</td>
<td align="right">2,356,581,916</td>
<td align="right">30.0%</td>
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
<td align="right">5,928,934</td>
<td align="right">0.1%</td>
<td align="right">5,928,431</td>
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
<td align="right">619,273</td>
<td align="right">83.8%</td>
<td align="right">607,938</td>
<td align="right">83.5%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">119,915</td>
<td align="right">16.2%</td>
<td align="right">119,909</td>
<td align="right">16.5%</td>
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
<td align="left">code complex parameters</td>
<td align="right">348</td>
<td align="right">0.1%</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">52,740</td>
<td align="right">8.5%</td>
<td align="right">47,128</td>
<td align="right">7.8%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,789</td>
<td align="right">0.6%</td>
<td align="right">3,609</td>
<td align="right">0.6%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">200,421</td>
<td align="right">32.4%</td>
<td align="right">197,051</td>
<td align="right">32.4%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">195,406</td>
<td align="right">31.6%</td>
<td align="right">193,752</td>
<td align="right">31.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">28,688</td>
<td align="right">4.6%</td>
<td align="right">28,484</td>
<td align="right">4.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,488</td>
<td align="right">2.0%</td>
<td align="right">12,449</td>
<td align="right">2.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">121,418</td>
<td align="right">19.6%</td>
<td align="right">121,418</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">0.5%</td>
<td align="right">2,941</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">1,013</td>
<td align="right">0.2%</td>
<td align="right">1,013</td>
<td align="right">0.2%</td>
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
<td align="right">183,416,152</td>
<td align="right">1.6%</td>
<td align="right">155,065,293</td>
<td align="right">1.4%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,569,971,615</td>
<td align="right">98.4%</td>
<td align="right">11,072,980,949</td>
<td align="right">98.6%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">230,054</td>
<td align="right">0.0%</td>
<td align="right">230,126</td>
<td align="right">0.0%</td>
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
<td align="right">3,631,062</td>
<td align="right">100.0%</td>
<td align="right">3,097,198</td>
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
<td align="right">111,575</td>
<td align="right">15.8%</td>
<td align="right">111,575</td>
<td align="right">15.8%</td>
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
<td align="right">584,005</td>
<td align="right">82.9%</td>
<td align="right">584,005</td>
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
<td align="right">20,091</td>
<td align="right">99.4%</td>
<td align="right">20,089</td>
<td align="right">99.4%</td>
<td align="right">-0.0%</td>
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
<td align="right">1,706,192</td>
<td align="right">0.0%</td>
<td align="right">1,393,690</td>
<td align="right">0.0%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">544,209,142</td>
<td align="right">10.6%</td>
<td align="right">518,732,682</td>
<td align="right">10.3%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,584,602,490</td>
<td align="right">89.4%</td>
<td align="right">4,529,808,353</td>
<td align="right">89.7%</td>
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
<td align="left">Failure</td>
<td align="right">243,592</td>
<td align="right">83.0%</td>
<td align="right">212,619</td>
<td align="right">82.9%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">49,843</td>
<td align="right">17.0%</td>
<td align="right">43,932</td>
<td align="right">17.1%</td>
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
<td align="left">list</td>
<td align="right">1,703</td>
<td align="right">0.7%</td>
<td align="right">956</td>
<td align="right">0.4%</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">39,971</td>
<td align="right">16.4%</td>
<td align="right">23,367</td>
<td align="right">11.0%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,071</td>
<td align="right">4.1%</td>
<td align="right">7,786</td>
<td align="right">3.7%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">15,269</td>
<td align="right">6.3%</td>
<td align="right">11,998</td>
<td align="right">5.6%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">51,533</td>
<td align="right">21.2%</td>
<td align="right">45,741</td>
<td align="right">21.5%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,153</td>
<td align="right">0.9%</td>
<td align="right">1,989</td>
<td align="right">0.9%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,860</td>
<td align="right">6.1%</td>
<td align="right">13,738</td>
<td align="right">6.5%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">91,809</td>
<td align="right">37.7%</td>
<td align="right">90,860</td>
<td align="right">42.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,861</td>
<td align="right">2.8%</td>
<td align="right">6,822</td>
<td align="right">3.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">3.1%</td>
<td align="right">7,639</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,367</td>
<td align="right">0.6%</td>
<td align="right">1,367</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.1%</td>
<td align="right">356</td>
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
<td align="right">183,442,410</td>
<td align="right">7.6%</td>
<td align="right">155,733,659</td>
<td align="right">6.6%</td>
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
<td align="right">2,220,358,684</td>
<td align="right">92.3%</td>
<td align="right">2,195,971,321</td>
<td align="right">93.3%</td>
<td align="right">-1.1%</td>
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
<td align="right">71,610</td>
<td align="right">65.2%</td>
<td align="right">59,247</td>
<td align="right">60.8%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,237</td>
<td align="right">34.8%</td>
<td align="right">38,235</td>
<td align="right">39.2%</td>
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
<td align="left">tuple</td>
<td align="right">15,936</td>
<td align="right">22.3%</td>
<td align="right">11,606</td>
<td align="right">19.6%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,802</td>
<td align="right">20.7%</td>
<td align="right">11,696</td>
<td align="right">19.7%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">24,776</td>
<td align="right">34.6%</td>
<td align="right">21,380</td>
<td align="right">36.1%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">16,096</td>
<td align="right">22.5%</td>
<td align="right">14,565</td>
<td align="right">24.6%</td>
<td align="right">-9.5%</td>
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
<td align="right">3,546,351,403</td>
<td align="right">68.1%</td>
<td align="right">3,443,776,713</td>
<td align="right">67.7%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,498,084,022</td>
<td align="right">28.8%</td>
<td align="right">1,476,337,470</td>
<td align="right">29.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">165,445,292</td>
<td align="right">3.2%</td>
<td align="right">163,930,673</td>
<td align="right">3.2%</td>
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
<td align="right">441,274</td>
<td align="right">12.4%</td>
<td align="right">426,050</td>
<td align="right">12.1%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,126,497</td>
<td align="right">87.6%</td>
<td align="right">3,097,907</td>
<td align="right">87.9%</td>
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
<td align="left">reversed list</td>
<td align="right">4,368</td>
<td align="right">1.0%</td>
<td align="right">3,139</td>
<td align="right">0.7%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">24,231</td>
<td align="right">5.5%</td>
<td align="right">19,493</td>
<td align="right">4.6%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">5,319</td>
<td align="right">1.2%</td>
<td align="right">4,601</td>
<td align="right">1.1%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">37,671</td>
<td align="right">8.5%</td>
<td align="right">35,012</td>
<td align="right">8.2%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">7,188</td>
<td align="right">1.6%</td>
<td align="right">6,911</td>
<td align="right">1.6%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">71,101</td>
<td align="right">16.1%</td>
<td align="right">68,962</td>
<td align="right">16.2%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">175,001</td>
<td align="right">39.7%</td>
<td align="right">172,146</td>
<td align="right">40.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">84,548</td>
<td align="right">19.2%</td>
<td align="right">83,979</td>
<td align="right">19.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,365</td>
<td align="right">2.6%</td>
<td align="right">11,325</td>
<td align="right">2.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">14,961</td>
<td align="right">3.4%</td>
<td align="right">14,961</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,390</td>
<td align="right">0.8%</td>
<td align="right">3,390</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">734</td>
<td align="right">0.2%</td>
<td align="right">734</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right">174</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">914,621,472</td>
<td align="right">6.3%</td>
<td align="right">871,351,116</td>
<td align="right">6.3%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,692,182,224</td>
<td align="right">87.6%</td>
<td align="right">12,103,347,994</td>
<td align="right">87.5%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">886,300,568</td>
<td align="right">6.1%</td>
<td align="right">851,479,654</td>
<td align="right">6.2%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,406,360</td>
<td align="right">0.0%</td>
<td align="right">1,404,420</td>
<td align="right">0.0%</td>
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
<td align="right">17,335,358</td>
<td align="right">96.7%</td>
<td align="right">16,521,816</td>
<td align="right">96.7%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">582,809</td>
<td align="right">3.3%</td>
<td align="right">565,328</td>
<td align="right">3.3%</td>
<td align="right">-3.0%</td>
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
<td align="left">out of versions</td>
<td align="right">5,005</td>
<td align="right">0.9%</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">2,490</td>
<td align="right">0.4%</td>
<td align="right">1,640</td>
<td align="right">0.3%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">7,282</td>
<td align="right">1.2%</td>
<td align="right">6,074</td>
<td align="right">1.1%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">19,424</td>
<td align="right">3.3%</td>
<td align="right">16,593</td>
<td align="right">2.9%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,960</td>
<td align="right">0.3%</td>
<td align="right">1,800</td>
<td align="right">0.3%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">61,587</td>
<td align="right">10.6%</td>
<td align="right">57,784</td>
<td align="right">10.2%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">84,196</td>
<td align="right">14.4%</td>
<td align="right">81,836</td>
<td align="right">14.5%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">66,967</td>
<td align="right">11.5%</td>
<td align="right">66,146</td>
<td align="right">11.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,992</td>
<td align="right">0.9%</td>
<td align="right">4,952</td>
<td align="right">0.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,445</td>
<td align="right">1.1%</td>
<td align="right">6,405</td>
<td align="right">1.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">25,336</td>
<td align="right">4.3%</td>
<td align="right">25,301</td>
<td align="right">4.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,124</td>
<td align="right">1.6%</td>
<td align="right">9,124</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,729</td>
<td align="right">0.5%</td>
<td align="right">2,729</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,180</td>
<td align="right">0.2%</td>
<td align="right">1,180</td>
<td align="right">0.2%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,854</td>
<td align="right">0.0%</td>
<td align="right">1,594</td>
<td align="right">0.0%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,676,455,045</td>
<td align="right">99.8%</td>
<td align="right">9,074,789,131</td>
<td align="right">99.8%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,822</td>
<td align="right">0.0%</td>
<td align="right">53,562</td>
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
<td align="right">14,622,653</td>
<td align="right">0.2%</td>
<td align="right">14,622,716</td>
<td align="right">0.2%</td>
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
<td align="right">136,570</td>
<td align="right">100.0%</td>
<td align="right">136,411</td>
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
<td align="right">110,431,466</td>
<td align="right">100.0%</td>
<td align="right">63,730,409</td>
<td align="right">100.0%</td>
<td align="right">-42.3%</td>
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
<td align="right">2,395</td>
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
<td align="right">593,528,371</td>
<td align="right">82.2%</td>
<td align="right">593,288,748</td>
<td align="right">82.2%</td>
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
<td align="right">128,815,787</td>
<td align="right">17.8%</td>
<td align="right">128,815,787</td>
<td align="right">17.8%</td>
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
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,412</td>
<td align="right">98.1%</td>
<td align="right">34,412</td>
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
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">3,261</td>
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
<td align="right">203,729,935</td>
<td align="right">8.3%</td>
<td align="right">116,600,958</td>
<td align="right">5.7%</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,151,215,065</td>
<td align="right">88.1%</td>
<td align="right">1,849,208,943</td>
<td align="right">90.5%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">86,393,769</td>
<td align="right">3.5%</td>
<td align="right">77,133,026</td>
<td align="right">3.8%</td>
<td align="right">-10.7%</td>
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
<td align="right">3,883,915</td>
<td align="right">98.4%</td>
<td align="right">2,239,818</td>
<td align="right">97.7%</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">63,043</td>
<td align="right">1.6%</td>
<td align="right">52,760</td>
<td align="right">2.3%</td>
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
<td align="left">property</td>
<td align="right">2,894</td>
<td align="right">4.6%</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">11,722</td>
<td align="right">18.6%</td>
<td align="right">7,666</td>
<td align="right">14.5%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">437</td>
<td align="right">0.7%</td>
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">27,914</td>
<td align="right">44.3%</td>
<td align="right">24,477</td>
<td align="right">46.4%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">889</td>
<td align="right">1.4%</td>
<td align="right">810</td>
<td align="right">1.5%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,562</td>
<td align="right">8.8%</td>
<td align="right">5,322</td>
<td align="right">10.1%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">272,358</td>
<td align="right">432.0%</td>
<td align="right">271,783</td>
<td align="right">515.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,352</td>
<td align="right">5.3%</td>
<td align="right">3,346</td>
<td align="right">6.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">6,033</td>
<td align="right">9.6%</td>
<td align="right">6,033</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.2%</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.2%</td>
<td align="right">730</td>
<td align="right">1.4%</td>
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
<td align="right">112,686,498</td>
<td align="right">100.0%</td>
<td align="right">112,686,498</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">926,734,723</td>
<td align="right">56.9%</td>
<td align="right">923,175,206</td>
<td align="right">56.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">702,521,344</td>
<td align="right">43.1%</td>
<td align="right">700,880,262</td>
<td align="right">43.2%</td>
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
<td align="right">183,166</td>
<td align="right">98.9%</td>
<td align="right">182,298</td>
<td align="right">98.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,080</td>
<td align="right">1.1%</td>
<td align="right">2,075</td>
<td align="right">1.1%</td>
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
<td align="left">out of range</td>
<td align="right">1,916</td>
<td align="right">1.0%</td>
<td align="right">1,680</td>
<td align="right">0.9%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,936</td>
<td align="right">10.9%</td>
<td align="right">19,343</td>
<td align="right">10.6%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,070</td>
<td align="right">1.7%</td>
<td align="right">3,031</td>
<td align="right">1.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">86,613</td>
<td align="right">47.3%</td>
<td align="right">86,613</td>
<td align="right">47.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.7%</td>
<td align="right">48,931</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">9.5%</td>
<td align="right">17,323</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,309</td>
<td align="right">2.9%</td>
<td align="right">5,309</td>
<td align="right">2.9%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,005,520,352</td>
<td align="right">92.8%</td>
<td align="right">4,753,574,462</td>
<td align="right">92.7%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">273,231,314</td>
<td align="right">5.1%</td>
<td align="right">263,681,190</td>
<td align="right">5.1%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">115,532,955</td>
<td align="right">2.1%</td>
<td align="right">112,452,758</td>
<td align="right">2.2%</td>
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
<td align="left">Failure</td>
<td align="right">651,696</td>
<td align="right">22.6%</td>
<td align="right">631,350</td>
<td align="right">22.5%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,227,643</td>
<td align="right">77.4%</td>
<td align="right">2,169,739</td>
<td align="right">77.5%</td>
<td align="right">-2.6%</td>
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
<td align="left">dict</td>
<td align="right">22,261</td>
<td align="right">3.4%</td>
<td align="right">20,553</td>
<td align="right">3.3%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">105,146</td>
<td align="right">16.1%</td>
<td align="right">97,406</td>
<td align="right">15.4%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">14,299</td>
<td align="right">2.2%</td>
<td align="right">13,302</td>
<td align="right">2.1%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">266,628</td>
<td align="right">40.9%</td>
<td align="right">258,640</td>
<td align="right">41.0%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">78,586</td>
<td align="right">12.1%</td>
<td align="right">77,647</td>
<td align="right">12.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">133,944</td>
<td align="right">20.6%</td>
<td align="right">132,989</td>
<td align="right">21.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">10,069</td>
<td align="right">1.5%</td>
<td align="right">10,050</td>
<td align="right">1.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,921</td>
<td align="right">2.9%</td>
<td align="right">18,921</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,862,607</td>
<td align="right">0.1%</td>
<td align="right">1,816,240</td>
<td align="right">0.1%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,269,211,946</td>
<td align="right">99.9%</td>
<td align="right">1,247,538,935</td>
<td align="right">99.9%</td>
<td align="right">-1.7%</td>
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
<td align="right">1,262</td>
<td align="right">9.8%</td>
<td align="right">986</td>
<td align="right">7.9%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,561</td>
<td align="right">90.2%</td>
<td align="right">11,521</td>
<td align="right">92.1%</td>
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
<td align="left">iterator</td>
<td align="right">255</td>
<td align="right">20.2%</td>
<td align="right">136</td>
<td align="right">13.8%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">130</td>
<td align="right">10.3%</td>
<td align="right">91</td>
<td align="right">9.2%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">877</td>
<td align="right">69.5%</td>
<td align="right">759</td>
<td align="right">77.0%</td>
<td align="right">-13.5%</td>
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
<td align="right">1,631,107,409</td>
<td align="right">0.7%</td>
<td align="right">1,467,291,755</td>
<td align="right">0.7%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">82,322,342,491</td>
<td align="right">37.7%</td>
<td align="right">78,848,882,497</td>
<td align="right">37.5%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">126,257,460,966</td>
<td align="right">57.8%</td>
<td align="right">122,207,664,156</td>
<td align="right">58.1%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,084,259,454</td>
<td align="right">3.7%</td>
<td align="right">7,923,745,967</td>
<td align="right">3.8%</td>
<td align="right">-2.0%</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">183,442,410</td>
<td align="right">2.3%</td>
<td align="right">155,733,659</td>
<td align="right">2.0%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">544,209,142</td>
<td align="right">6.7%</td>
<td align="right">518,732,682</td>
<td align="right">6.6%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">886,300,568</td>
<td align="right">11.0%</td>
<td align="right">851,479,654</td>
<td align="right">10.8%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">273,231,314</td>
<td align="right">3.4%</td>
<td align="right">263,681,190</td>
<td align="right">3.3%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,498,084,022</td>
<td align="right">18.5%</td>
<td align="right">1,476,337,470</td>
<td align="right">18.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,381,104,073</td>
<td align="right">29.5%</td>
<td align="right">2,356,581,916</td>
<td align="right">29.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,082,181,579</td>
<td align="right">13.4%</td>
<td align="right">1,077,334,958</td>
<td align="right">13.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,421,332</td>
<td align="right">2.3%</td>
<td align="right">181,849,892</td>
<td align="right">2.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">702,521,344</td>
<td align="right">8.7%</td>
<td align="right">700,880,262</td>
<td align="right">8.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,787</td>
<td align="right">1.6%</td>
<td align="right">128,815,787</td>
<td align="right">1.6%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">104,985,354</td>
<td align="right">6.4%</td>
<td align="right">82,384,130</td>
<td align="right">5.6%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">291,020,090</td>
<td align="right">17.8%</td>
<td align="right">266,998,029</td>
<td align="right">18.2%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">93,167,218</td>
<td align="right">5.7%</td>
<td align="right">90,677,301</td>
<td align="right">6.2%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">96,480,949</td>
<td align="right">5.9%</td>
<td align="right">94,278,553</td>
<td align="right">6.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">56,387,861</td>
<td align="right">3.5%</td>
<td align="right">55,286,626</td>
<td align="right">3.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">371,824,174</td>
<td align="right">22.8%</td>
<td align="right">368,076,858</td>
<td align="right">25.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,752,439</td>
<td align="right">5.1%</td>
<td align="right">81,953,696</td>
<td align="right">5.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">82,607,804</td>
<td align="right">5.1%</td>
<td align="right">81,898,288</td>
<td align="right">5.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">86,914,358</td>
<td align="right">5.3%</td>
<td align="right">86,866,985</td>
<td align="right">5.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">107,199,691</td>
<td align="right">6.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">49,778,638</td>
<td align="right">3.4%</td>
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
<td align="left">Frames pushed</td>
<td align="right">5,840,706,735</td>
<td align="right">82.1%</td>
<td align="right">5,484,021,017</td>
<td align="right">81.2%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">296,156,602</td>
<td align="right">4.2%</td>
<td align="right">279,372,900</td>
<td align="right">4.1%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,423,915,452</td>
<td align="right">76.2%</td>
<td align="right">5,121,960,507</td>
<td align="right">75.8%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">995,847,661</td>
<td align="right">14.0%</td>
<td align="right">950,985,837</td>
<td align="right">14.1%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,000,125,001</td>
<td align="right">14.1%</td>
<td align="right">955,263,177</td>
<td align="right">14.1%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,689,679,825</td>
<td align="right">23.8%</td>
<td align="right">1,634,158,008</td>
<td align="right">24.2%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,689,679,825</td>
<td align="right">23.8%</td>
<td align="right">1,634,158,008</td>
<td align="right">24.2%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">25,738,644</td>
<td align="right">0.4%</td>
<td align="right">24,922,517</td>
<td align="right">0.4%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">689,554,824</td>
<td align="right">9.7%</td>
<td align="right">678,894,831</td>
<td align="right">10.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">265,399,887</td>
<td align="right">3.7%</td>
<td align="right">261,414,595</td>
<td align="right">3.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">72,259,188</td>
<td align="right">1.0%</td>
<td align="right">71,326,562</td>
<td align="right">1.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,444</td>
<td align="right">0.1%</td>
<td align="right">4,273,444</td>
<td align="right">0.1%</td>
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
<td align="right">1.9%</td>
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
<td align="left">Method cache misses</td>
<td align="right">81,848,500</td>
<td align="right"></td>
<td align="right">59,732,703</td>
<td align="right"></td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">81,495,355</td>
<td align="right"></td>
<td align="right">68,912,681</td>
<td align="right"></td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">11,635,536</td>
<td align="right"></td>
<td align="right">9,988,247</td>
<td align="right"></td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,884</td>
<td align="right">0.0%</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,474,356,824</td>
<td align="right"></td>
<td align="right">2,293,655,226</td>
<td align="right"></td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">26,850,032,988</td>
<td align="right">16.5%</td>
<td align="right">25,475,639,452</td>
<td align="right">16.3%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,056,452,665</td>
<td align="right"></td>
<td align="right">2,902,259,589</td>
<td align="right"></td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">7,847,359,048</td>
<td align="right">41.5%</td>
<td align="right">7,466,483,030</td>
<td align="right">40.7%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,840,884,828</td>
<td align="right">15.2%</td>
<td align="right">23,642,128,762</td>
<td align="right">15.2%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">7,926,059,207</td>
<td align="right">41.9%</td>
<td align="right">7,544,480,946</td>
<td align="right">41.1%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">187,432,660</td>
<td align="right"></td>
<td align="right">179,185,308</td>
<td align="right"></td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">83,007,307,601</td>
<td align="right">50.9%</td>
<td align="right">79,357,000,673</td>
<td align="right">50.9%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">92,706,654,647</td>
<td align="right">46.6%</td>
<td align="right">88,692,139,787</td>
<td align="right">46.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">8,493,633,506</td>
<td align="right"></td>
<td align="right">8,137,991,533</td>
<td align="right"></td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">34,635,531,461</td>
<td align="right">17.4%</td>
<td align="right">33,234,032,360</td>
<td align="right">17.4%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">25,059,408,809</td>
<td align="right">12.6%</td>
<td align="right">24,099,406,953</td>
<td align="right">12.6%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">28,341,807,738</td>
<td align="right">17.4%</td>
<td align="right">27,546,085,079</td>
<td align="right">17.7%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">46,597,450,424</td>
<td align="right">23.4%</td>
<td align="right">45,514,982,908</td>
<td align="right">23.8%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,551,898</td>
<td align="right">0.0%</td>
<td align="right">6,421,045</td>
<td align="right">0.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,971,128,037</td>
<td align="right">58.1%</td>
<td align="right">10,817,805,460</td>
<td align="right">58.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,971,262,599</td>
<td align="right"></td>
<td align="right">10,817,939,974</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">72,148,261</td>
<td align="right">0.4%</td>
<td align="right">71,576,871</td>
<td align="right">0.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">476,376</td>
<td align="right">0.3%</td>
<td align="right">476,016</td>
<td align="right">0.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,401</td>
<td align="right">2.4%</td>
<td align="right">4,444,161</td>
<td align="right">2.5%</td>
<td align="right">-0.0%</td>
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
<td align="right">364,908</td>
<td align="right">103,936,395</td>
<td align="right">9,812,807,908</td>
<td align="right">748,162,176</td>
<td align="right">785,515,863</td>
<td align="right">364,679</td>
<td align="right">103,496,697</td>
<td align="right">9,337,742,197</td>
<td align="right">735,446,631</td>
<td align="right">763,381,919</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,603,195,326</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,603,776,798</td>
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
<td align="right">31</td>
<td align="right">31</td>
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
<td align="right">38</td>
<td align="right">38</td>
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
<td align="right">2,496</td>
<td align="right">2,476</td>
<td align="right">-0.8%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-01-09
