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
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,075,021</td>
<td align="right">4,722,754</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">45,149,737</td>
<td align="right">48,769,358</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">68,856,418</td>
<td align="right">70,934,347</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">229,770,036</td>
<td align="right">235,510,906</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,704</td>
<td align="right">2,644</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">144,214,999</td>
<td align="right">147,402,054</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,350,157</td>
<td align="right">63,721,100</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,036,028</td>
<td align="right">13,305,790</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">456,835,978</td>
<td align="right">464,800,400</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">194,643,332</td>
<td align="right">197,775,173</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">122,206,197</td>
<td align="right">124,161,786</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,400,694</td>
<td align="right">105,744,069</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">286,780,347</td>
<td align="right">290,278,027</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,851,255,292</td>
<td align="right">3,894,898,613</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">123,381,332</td>
<td align="right">124,710,945</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">163,023,834</td>
<td align="right">164,714,346</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">113,399,211</td>
<td align="right">114,555,478</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">270,857,774</td>
<td align="right">273,570,302</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,504,031</td>
<td align="right">10,606,614</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,166,204</td>
<td align="right">7,234,553</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">274,184,168</td>
<td align="right">276,795,168</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,319,610</td>
<td align="right">7,388,008</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">92,443,849</td>
<td align="right">93,284,778</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">766,588,499</td>
<td align="right">773,154,262</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">871,597,231</td>
<td align="right">879,002,763</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,633,933,558</td>
<td align="right">3,662,947,929</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">72,181,116</td>
<td align="right">72,746,294</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,029,563,105</td>
<td align="right">1,037,543,929</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,038,488,198</td>
<td align="right">1,046,200,698</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,728,921</td>
<td align="right">4,762,362</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">197,700,535</td>
<td align="right">199,062,770</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">566,598,917</td>
<td align="right">570,289,228</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">857,907,009</td>
<td align="right">863,375,140</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">397,121,676</td>
<td align="right">399,629,777</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,377,927,698</td>
<td align="right">4,404,946,271</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">127,795,958</td>
<td align="right">128,582,016</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">244,358,426</td>
<td align="right">245,852,243</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">93,648,821</td>
<td align="right">94,213,232</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">164,485,091</td>
<td align="right">165,456,280</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,479,146</td>
<td align="right">57,807,397</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">107,382,577</td>
<td align="right">107,988,223</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">282,465,252</td>
<td align="right">284,048,454</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">54,908,693</td>
<td align="right">55,208,384</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">409,367</td>
<td align="right">407,213</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">125,331,169</td>
<td align="right">125,956,405</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">359,319,323</td>
<td align="right">361,090,400</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">18,480,830,094</td>
<td align="right">18,571,192,945</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">74,959,696</td>
<td align="right">75,310,732</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,284,942,033</td>
<td align="right">5,308,251,490</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">80,954,802</td>
<td align="right">81,305,838</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">62,335,014</td>
<td align="right">62,603,297</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">272,541,144</td>
<td align="right">273,713,930</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,171,916</td>
<td align="right">41,347,434</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">403,220,507</td>
<td align="right">404,896,175</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">293,344,159</td>
<td align="right">294,555,664</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">287,661,798</td>
<td align="right">288,834,588</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">202,004,443</td>
<td align="right">202,819,768</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">574,690,812</td>
<td align="right">576,909,500</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">96,133,309</td>
<td align="right">96,488,101</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,789,623,254</td>
<td align="right">1,796,227,702</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">227,493,287</td>
<td align="right">228,303,188</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,206,342,943</td>
<td align="right">1,210,519,455</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">19,491,911</td>
<td align="right">19,559,241</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,610,816,896</td>
<td align="right">2,619,733,660</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">829,217,306</td>
<td align="right">832,003,499</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,344,009,561</td>
<td align="right">2,351,773,652</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,171,230</td>
<td align="right">184,777,605</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">935,211,283</td>
<td align="right">938,228,628</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">251,544,680</td>
<td align="right">252,333,347</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,882,109,518</td>
<td align="right">4,896,857,020</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">171,274,690</td>
<td align="right">171,780,870</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,329,802,098</td>
<td align="right">5,344,730,005</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">86,330,358</td>
<td align="right">86,560,685</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,589,246,799</td>
<td align="right">2,595,895,486</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">46,658,538</td>
<td align="right">46,771,634</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">336,720,579</td>
<td align="right">337,531,993</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,244,963,026</td>
<td align="right">1,247,830,656</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,093,331,843</td>
<td align="right">2,098,069,876</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,280,254,555</td>
<td align="right">2,285,125,881</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">242,746,062</td>
<td align="right">243,262,779</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,680,781,355</td>
<td align="right">2,686,479,504</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">597,934,754</td>
<td align="right">599,188,970</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,932,381,458</td>
<td align="right">3,939,659,372</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">792,517,904</td>
<td align="right">793,957,661</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">957,808,444</td>
<td align="right">959,292,747</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">429,971,773</td>
<td align="right">430,633,140</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">702,278,581</td>
<td align="right">703,321,229</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">344,748,458</td>
<td align="right">345,207,713</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">56,106,778</td>
<td align="right">56,033,873</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">510,427,803</td>
<td align="right">511,088,441</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">166,905,790</td>
<td align="right">166,693,527</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">661,222,513</td>
<td align="right">662,062,112</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">612,799,917</td>
<td align="right">613,536,484</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">86,041,862</td>
<td align="right">86,143,279</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">108,348,919</td>
<td align="right">108,468,672</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">617,975,457</td>
<td align="right">618,646,050</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">745,032,789</td>
<td align="right">745,785,911</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">174,089,628</td>
<td align="right">174,261,627</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">492,288,463</td>
<td align="right">492,758,927</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,279,619</td>
<td align="right">2,281,713</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">493,572,483</td>
<td align="right">494,021,255</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">958,029,013</td>
<td align="right">958,827,177</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">365,710,984</td>
<td align="right">366,013,428</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">115,690,867</td>
<td align="right">115,785,532</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">237,926,646</td>
<td align="right">238,102,961</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">239,982,523</td>
<td align="right">240,160,244</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,113,065,956</td>
<td align="right">1,113,877,376</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,500</td>
<td align="right">5,504</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,948,525</td>
<td align="right">27,963,864</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">344,279,926</td>
<td align="right">344,461,195</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,520,260,642</td>
<td align="right">1,521,032,652</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">203,750,931</td>
<td align="right">203,853,594</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">869,704,966</td>
<td align="right">870,124,134</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,565,892</td>
<td align="right">3,567,530</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">474,922,764</td>
<td align="right">475,129,801</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">38,247,326</td>
<td align="right">38,263,181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">121,328</td>
<td align="right">121,286</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">34,198</td>
<td align="right">34,187</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">178,348,318</td>
<td align="right">178,404,798</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">161,019,227</td>
<td align="right">161,065,570</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,197,599</td>
<td align="right">57,182,607</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">174,812,296</td>
<td align="right">174,845,842</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">752,303</td>
<td align="right">752,422</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">28,879,669</td>
<td align="right">28,884,211</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">97,914,823</td>
<td align="right">97,930,103</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">112,791,982</td>
<td align="right">112,807,574</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,384,154</td>
<td align="right">1,384,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">55,372,197</td>
<td align="right">55,378,021</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,763,373</td>
<td align="right">14,761,970</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,069,880</td>
<td align="right">35,072,966</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">81,503,784</td>
<td align="right">81,497,679</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,431,566</td>
<td align="right">1,431,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,533,250</td>
<td align="right">3,533,435</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,838,109</td>
<td align="right">25,839,428</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,899,576</td>
<td align="right">155,905,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">413,784,822</td>
<td align="right">413,800,351</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">94,861,378</td>
<td align="right">94,864,875</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,684,103</td>
<td align="right">7,684,279</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">135,671</td>
<td align="right">135,673</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,053,918</td>
<td align="right">10,054,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">815,716,985</td>
<td align="right">815,723,367</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,024,941</td>
<td align="right">20,025,095</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,356,209</td>
<td align="right">20,356,363</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,356,189</td>
<td align="right">20,356,342</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,458</td>
<td align="right">5,803,498</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">66,527,293</td>
<td align="right">66,527,729</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">71,428,885</td>
<td align="right">71,429,293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">369,619,487</td>
<td align="right">369,621,066</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">273,238,025</td>
<td align="right">273,239,042</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">120,109,306</td>
<td align="right">120,109,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">33,224,335</td>
<td align="right">33,224,408</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,643,422</td>
<td align="right">1,643,419</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,462</td>
<td align="right">35,549,414</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">198,119,855</td>
<td align="right">198,119,624</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">154,813,968</td>
<td align="right">154,814,093</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,892,402</td>
<td align="right">114,892,469</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">126,614,055</td>
<td align="right">126,614,095</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">172,534,341</td>
<td align="right">172,534,304</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,621,296</td>
<td align="right">591,621,248</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,390,955</td>
<td align="right">418,390,928</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">138,160,190</td>
<td align="right">138,160,193</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,401,564</td>
<td align="right">131,401,562</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">504,639,440</td>
<td align="right">504,639,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,521</td>
<td align="right">302,246,521</td>
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
<td align="right">128,850,305</td>
<td align="right">128,850,305</td>
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
<td align="right">41,964,610</td>
<td align="right">41,964,610</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,033,269</td>
<td align="right">31,033,269</td>
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
<td align="right">9,743,044</td>
<td align="right">9,743,044</td>
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
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,484,368</td>
<td align="right">3,484,368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,755,411</td>
<td align="right">1,755,411</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,232,478</td>
<td align="right">1,232,478</td>
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
<td align="right">98,514</td>
<td align="right">98,514</td>
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
<td align="right">69,497</td>
<td align="right">69,497</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,195</td>
<td align="right">57,195</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,981</td>
<td align="right">53,981</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">13,935</td>
<td align="right">13,935</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,299</td>
<td align="right">5,299</td>
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
<td align="right">36</td>
<td align="right">36</td>
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
<td align="right">1,244,535,383</td>
<td align="right">7.3%</td>
<td align="right">1,247,403,423</td>
<td align="right">7.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,813,571,633</td>
<td align="right">92.4%</td>
<td align="right">15,830,969,093</td>
<td align="right">92.4%</td>
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
<td align="right">56,830,298</td>
<td align="right">0.3%</td>
<td align="right">56,826,959</td>
<td align="right">0.3%</td>
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
<td align="right">406,450</td>
<td align="right">27.2%</td>
<td align="right">407,058</td>
<td align="right">27.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,090,066</td>
<td align="right">72.8%</td>
<td align="right">1,088,981</td>
<td align="right">72.8%</td>
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
<td align="left">xor</td>
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">209</td>
<td align="right">0.1%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">303</td>
<td align="right">0.1%</td>
<td align="right">325</td>
<td align="right">0.1%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">145</td>
<td align="right">0.0%</td>
<td align="right">148</td>
<td align="right">0.0%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,685</td>
<td align="right">1.9%</td>
<td align="right">7,835</td>
<td align="right">1.9%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">40,983</td>
<td align="right">10.1%</td>
<td align="right">41,400</td>
<td align="right">10.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,174</td>
<td align="right">0.8%</td>
<td align="right">3,154</td>
<td align="right">0.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">494</td>
<td align="right">0.1%</td>
<td align="right">492</td>
<td align="right">0.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">627</td>
<td align="right">0.2%</td>
<td align="right">628</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">1,806</td>
<td align="right">0.4%</td>
<td align="right">1,808</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,501</td>
<td align="right">4.6%</td>
<td align="right">18,481</td>
<td align="right">4.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">6,884</td>
<td align="right">1.7%</td>
<td align="right">6,889</td>
<td align="right">1.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">1,969</td>
<td align="right">0.5%</td>
<td align="right">1,970</td>
<td align="right">0.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">29,939</td>
<td align="right">7.4%</td>
<td align="right">29,950</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">11,294</td>
<td align="right">2.8%</td>
<td align="right">11,297</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">36,632</td>
<td align="right">9.0%</td>
<td align="right">36,638</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">75,135</td>
<td align="right">18.5%</td>
<td align="right">75,146</td>
<td align="right">18.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">25,942</td>
<td align="right">6.4%</td>
<td align="right">25,939</td>
<td align="right">6.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,779</td>
<td align="right">5.9%</td>
<td align="right">23,780</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">30,354</td>
<td align="right">7.5%</td>
<td align="right">30,354</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">28,692</td>
<td align="right">7.1%</td>
<td align="right">28,692</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">17,023</td>
<td align="right">4.2%</td>
<td align="right">17,023</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">15,432</td>
<td align="right">3.8%</td>
<td align="right">15,432</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">7,754</td>
<td align="right">1.9%</td>
<td align="right">7,754</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,752</td>
<td align="right">1.4%</td>
<td align="right">5,752</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,767</td>
<td align="right">0.7%</td>
<td align="right">2,767</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.6%</td>
<td align="right">2,343</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,342</td>
<td align="right">0.6%</td>
<td align="right">2,342</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">0.5%</td>
<td align="right">1,996</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">836</td>
<td align="right">0.2%</td>
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
<td align="right">201</td>
<td align="right">0.0%</td>
<td align="right">201</td>
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
<td align="left">subscr stacksummary</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">184,171,230</td>
<td align="right">100.0%</td>
<td align="right">184,777,605</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">162,014,565</td>
<td align="right">1.5%</td>
<td align="right">165,157,332</td>
<td align="right">1.5%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">159,190,019</td>
<td align="right">1.4%</td>
<td align="right">162,273,448</td>
<td align="right">1.5%</td>
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
<td align="right">10,969,644,604</td>
<td align="right">98.5%</td>
<td align="right">10,987,538,068</td>
<td align="right">98.5%</td>
<td align="right">0.2%</td>
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
<td align="right">3,233,467</td>
<td align="right">100.0%</td>
<td align="right">3,290,651</td>
<td align="right">100.0%</td>
<td align="right">1.8%</td>
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
<td align="right">685,057</td>
<td align="right">97.1%</td>
<td align="right">685,057</td>
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
<td align="right">584,357</td>
<td align="right">82.8%</td>
<td align="right">584,357</td>
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
<td align="right">20,508</td>
<td align="right">99.4%</td>
<td align="right">20,466</td>
<td align="right">99.4%</td>
<td align="right">-0.2%</td>
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
<td align="right">104,279,514</td>
<td align="right">2.3%</td>
<td align="right">105,622,893</td>
<td align="right">2.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,156,493</td>
<td align="right">0.0%</td>
<td align="right">1,160,077</td>
<td align="right">0.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,493,455,708</td>
<td align="right">97.7%</td>
<td align="right">4,506,909,711</td>
<td align="right">97.7%</td>
<td align="right">0.3%</td>
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
<td align="right">40,080</td>
<td align="right">28.1%</td>
<td align="right">39,838</td>
<td align="right">27.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">102,720</td>
<td align="right">71.9%</td>
<td align="right">103,029</td>
<td align="right">72.1%</td>
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
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">356</td>
<td align="right">0.3%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,321</td>
<td align="right">1.3%</td>
<td align="right">1,367</td>
<td align="right">1.3%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,975</td>
<td align="right">1.9%</td>
<td align="right">2,001</td>
<td align="right">1.9%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,736</td>
<td align="right">7.5%</td>
<td align="right">7,825</td>
<td align="right">7.6%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,159</td>
<td align="right">4.0%</td>
<td align="right">4,201</td>
<td align="right">4.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">37,088</td>
<td align="right">36.1%</td>
<td align="right">37,237</td>
<td align="right">36.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">11,560</td>
<td align="right">11.3%</td>
<td align="right">11,518</td>
<td align="right">11.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">810</td>
<td align="right">0.8%</td>
<td align="right">811</td>
<td align="right">0.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,198</td>
<td align="right">22.6%</td>
<td align="right">23,172</td>
<td align="right">22.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">5,930</td>
<td align="right">5.8%</td>
<td align="right">5,932</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">7.4%</td>
<td align="right">7,648</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">961</td>
<td align="right">0.9%</td>
<td align="right">961</td>
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
<td align="right">93,602,147</td>
<td align="right">4.1%</td>
<td align="right">94,166,644</td>
<td align="right">4.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,186,572,788</td>
<td align="right">95.8%</td>
<td align="right">2,190,159,495</td>
<td align="right">95.8%</td>
<td align="right">0.2%</td>
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
<td align="right">1,395,959</td>
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
<td align="left">Success</td>
<td align="right">28,659</td>
<td align="right">39.2%</td>
<td align="right">28,459</td>
<td align="right">39.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">44,358</td>
<td align="right">60.8%</td>
<td align="right">44,472</td>
<td align="right">61.0%</td>
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
<td align="left">other</td>
<td align="right">9,947</td>
<td align="right">22.4%</td>
<td align="right">9,982</td>
<td align="right">22.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,142</td>
<td align="right">25.1%</td>
<td align="right">11,178</td>
<td align="right">25.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,070</td>
<td align="right">31.7%</td>
<td align="right">14,113</td>
<td align="right">31.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,199</td>
<td align="right">20.7%</td>
<td align="right">9,199</td>
<td align="right">20.7%</td>
<td align="right">0.0%</td>
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
<td align="right">242,615,462</td>
<td align="right">14.3%</td>
<td align="right">243,130,573</td>
<td align="right">14.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,390,409,822</td>
<td align="right">82.0%</td>
<td align="right">1,391,838,468</td>
<td align="right">82.0%</td>
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
<td align="right">62,000,267</td>
<td align="right">3.7%</td>
<td align="right">62,026,557</td>
<td align="right">3.7%</td>
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
<td align="right">125,026</td>
<td align="right">9.6%</td>
<td align="right">126,626</td>
<td align="right">9.7%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,175,222</td>
<td align="right">90.4%</td>
<td align="right">1,175,723</td>
<td align="right">90.3%</td>
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
<td align="left">reversed list</td>
<td align="right">1,673</td>
<td align="right">1.3%</td>
<td align="right">1,737</td>
<td align="right">1.4%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">50,512</td>
<td align="right">40.4%</td>
<td align="right">52,003</td>
<td align="right">41.1%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,470</td>
<td align="right">3.6%</td>
<td align="right">4,428</td>
<td align="right">3.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">14,195</td>
<td align="right">11.4%</td>
<td align="right">14,297</td>
<td align="right">11.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,339</td>
<td align="right">3.5%</td>
<td align="right">4,319</td>
<td align="right">3.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">16,631</td>
<td align="right">13.3%</td>
<td align="right">16,637</td>
<td align="right">13.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">11,086</td>
<td align="right">8.9%</td>
<td align="right">11,085</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">9,967</td>
<td align="right">8.0%</td>
<td align="right">9,967</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,510</td>
<td align="right">5.2%</td>
<td align="right">6,510</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,792</td>
<td align="right">3.0%</td>
<td align="right">3,792</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,132</td>
<td align="right">0.9%</td>
<td align="right">1,132</td>
<td align="right">0.9%</td>
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
<td align="left">map</td>
<td align="right">258</td>
<td align="right">0.2%</td>
<td align="right">258</td>
<td align="right">0.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,898,595,254</td>
<td align="right">89.7%</td>
<td align="right">11,680,473,393</td>
<td align="right">89.5%</td>
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
<td align="right">564,834,692</td>
<td align="right">4.3%</td>
<td align="right">568,527,870</td>
<td align="right">4.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">793,450,008</td>
<td align="right">6.0%</td>
<td align="right">793,907,075</td>
<td align="right">6.1%</td>
<td align="right">0.1%</td>
</tr>
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
<td align="right">1,262,484</td>
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
<td align="right">492,991</td>
<td align="right">3.2%</td>
<td align="right">494,161</td>
<td align="right">3.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,060,859</td>
<td align="right">96.8%</td>
<td align="right">15,065,329</td>
<td align="right">96.8%</td>
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
<td align="left">method</td>
<td align="right">40,158</td>
<td align="right">8.1%</td>
<td align="right">40,752</td>
<td align="right">8.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,783</td>
<td align="right">0.4%</td>
<td align="right">1,809</td>
<td align="right">0.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,898</td>
<td align="right">1.0%</td>
<td align="right">4,931</td>
<td align="right">1.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">44,802</td>
<td align="right">9.1%</td>
<td align="right">45,045</td>
<td align="right">9.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">61,347</td>
<td align="right">12.4%</td>
<td align="right">61,429</td>
<td align="right">12.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,213</td>
<td align="right">4.9%</td>
<td align="right">24,226</td>
<td align="right">4.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,314</td>
<td align="right">3.3%</td>
<td align="right">16,309</td>
<td align="right">3.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,950</td>
<td align="right">1.6%</td>
<td align="right">7,952</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">0.9%</td>
<td align="right">4,449</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
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
<td align="right">2,378</td>
<td align="right">0.5%</td>
<td align="right">2,378</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,778</td>
<td align="right">0.4%</td>
<td align="right">1,778</td>
<td align="right">0.4%</td>
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
<td align="left">builtin class method</td>
<td align="right">821</td>
<td align="right">0.2%</td>
<td align="right">821</td>
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
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">255</td>
<td align="right">0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,583</td>
<td align="right">0.0%</td>
<td align="right">53,150</td>
<td align="right">0.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,766,787,103</td>
<td align="right">99.7%</td>
<td align="right">4,780,441,322</td>
<td align="right">99.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,623,554</td>
<td align="right">0.3%</td>
<td align="right">14,623,568</td>
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
<td align="right">1,479</td>
<td align="right">0.0%</td>
<td align="right">1,479</td>
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
<td align="right">140,594</td>
<td align="right">100.0%</td>
<td align="right">139,177</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">64,161,654</td>
<td align="right">100.0%</td>
<td align="right">64,533,583</td>
<td align="right">100.0%</td>
<td align="right">0.6%</td>
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
<td align="right">251</td>
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
<td align="right">2,453</td>
<td align="right">100.0%</td>
<td align="right">2,393</td>
<td align="right">100.0%</td>
<td align="right">-2.4%</td>
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
<td align="right">591,606,585</td>
<td align="right">82.1%</td>
<td align="right">591,606,537</td>
<td align="right">82.1%</td>
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
<td align="right">128,815,507</td>
<td align="right">17.9%</td>
<td align="right">128,815,507</td>
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
<td align="right">72,087,376</td>
<td align="right">3.7%</td>
<td align="right">72,653,831</td>
<td align="right">3.7%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,783,461,454</td>
<td align="right">90.6%</td>
<td align="right">1,790,867,427</td>
<td align="right">90.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">111,808,679</td>
<td align="right">5.7%</td>
<td align="right">111,814,692</td>
<td align="right">5.7%</td>
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
<td align="right">51,590</td>
<td align="right">2.3%</td>
<td align="right">51,712</td>
<td align="right">2.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,150,834</td>
<td align="right">97.7%</td>
<td align="right">2,149,566</td>
<td align="right">97.7%</td>
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
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.1%</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,898</td>
<td align="right">9.5%</td>
<td align="right">4,963</td>
<td align="right">9.6%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,346</td>
<td align="right">6.5%</td>
<td align="right">3,354</td>
<td align="right">6.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,327</td>
<td align="right">10.3%</td>
<td align="right">5,331</td>
<td align="right">10.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">264,133</td>
<td align="right">512.0%</td>
<td align="right">264,194</td>
<td align="right">510.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">47.4%</td>
<td align="right">24,476</td>
<td align="right">47.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.9%</td>
<td align="right">7,666</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">817</td>
<td align="right">1.6%</td>
<td align="right">817</td>
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
<td align="right">1,232,478</td>
<td align="right">100.0%</td>
<td align="right">1,232,478</td>
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
<td align="right">920,405,341</td>
<td align="right">85.6%</td>
<td align="right">922,126,391</td>
<td align="right">85.6%</td>
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
<td align="right">154,762,806</td>
<td align="right">14.4%</td>
<td align="right">154,763,050</td>
<td align="right">14.4%</td>
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
<td align="right">2,242</td>
<td align="right">4.4%</td>
<td align="right">2,123</td>
<td align="right">4.2%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">48,960</td>
<td align="right">95.6%</td>
<td align="right">48,960</td>
<td align="right">95.8%</td>
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
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">35.4%</td>
<td align="right">17,323</td>
<td align="right">35.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">15,163</td>
<td align="right">31.0%</td>
<td align="right">15,163</td>
<td align="right">31.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">11,212</td>
<td align="right">22.9%</td>
<td align="right">11,212</td>
<td align="right">22.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,010</td>
<td align="right">6.1%</td>
<td align="right">3,010</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,662</td>
<td align="right">3.4%</td>
<td align="right">1,662</td>
<td align="right">3.4%</td>
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
<td align="left">bytearray int</td>
<td align="right">181</td>
<td align="right">0.4%</td>
<td align="right">181</td>
<td align="right">0.4%</td>
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
<td align="right">143,655,344</td>
<td align="right">3.1%</td>
<td align="right">146,842,061</td>
<td align="right">3.1%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,491,905,123</td>
<td align="right">95.6%</td>
<td align="right">4,502,770,454</td>
<td align="right">95.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">63,914,560</td>
<td align="right">1.4%</td>
<td align="right">63,940,422</td>
<td align="right">1.4%</td>
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
<td align="right">508,175</td>
<td align="right">28.8%</td>
<td align="right">509,009</td>
<td align="right">28.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,255,737</td>
<td align="right">71.2%</td>
<td align="right">1,255,712</td>
<td align="right">71.2%</td>
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
<td align="left">sequence</td>
<td align="right">9,057</td>
<td align="right">1.8%</td>
<td align="right">9,731</td>
<td align="right">1.9%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,885</td>
<td align="right">3.1%</td>
<td align="right">15,945</td>
<td align="right">3.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">73,716</td>
<td align="right">14.5%</td>
<td align="right">73,786</td>
<td align="right">14.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,385</td>
<td align="right">2.6%</td>
<td align="right">13,391</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">33,930</td>
<td align="right">6.7%</td>
<td align="right">33,915</td>
<td align="right">6.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">96,061</td>
<td align="right">18.9%</td>
<td align="right">96,084</td>
<td align="right">18.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">5,457</td>
<td align="right">1.1%</td>
<td align="right">5,458</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,798</td>
<td align="right">50.9%</td>
<td align="right">258,813</td>
<td align="right">50.8%</td>
<td align="right">0.0%</td>
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
<td align="right">1,239,843,730</td>
<td align="right">99.9%</td>
<td align="right">1,240,630,456</td>
<td align="right">99.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,420,705</td>
<td align="right">0.1%</td>
<td align="right">1,420,806</td>
<td align="right">0.1%</td>
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
<td align="right">872</td>
<td align="right">8.0%</td>
<td align="right">870</td>
<td align="right">8.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,069</td>
<td align="right">92.0%</td>
<td align="right">10,049</td>
<td align="right">92.0%</td>
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
<td align="right">638</td>
<td align="right">73.2%</td>
<td align="right">636</td>
<td align="right">73.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.6%</td>
<td align="right">136</td>
<td align="right">15.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">11.2%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">43,050,574,064</td>
<td align="right">40.4%</td>
<td align="right">43,250,132,258</td>
<td align="right">40.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,954,549,954</td>
<td align="right">2.8%</td>
<td align="right">2,967,887,551</td>
<td align="right">2.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">59,315,179,255</td>
<td align="right">55.7%</td>
<td align="right">59,534,241,372</td>
<td align="right">55.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,253,379,661</td>
<td align="right">1.2%</td>
<td align="right">1,257,038,653</td>
<td align="right">1.2%</td>
<td align="right">0.3%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">143,655,344</td>
<td align="right">4.6%</td>
<td align="right">146,842,061</td>
<td align="right">4.7%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">159,190,019</td>
<td align="right">5.1%</td>
<td align="right">162,273,448</td>
<td align="right">5.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,279,514</td>
<td align="right">3.4%</td>
<td align="right">105,622,893</td>
<td align="right">3.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">564,834,692</td>
<td align="right">18.2%</td>
<td align="right">568,527,870</td>
<td align="right">18.2%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">93,602,147</td>
<td align="right">3.0%</td>
<td align="right">94,166,644</td>
<td align="right">3.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,171,230</td>
<td align="right">5.9%</td>
<td align="right">184,777,605</td>
<td align="right">5.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,244,535,383</td>
<td align="right">40.0%</td>
<td align="right">1,247,403,423</td>
<td align="right">39.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">242,615,462</td>
<td align="right">7.8%</td>
<td align="right">243,130,573</td>
<td align="right">7.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">154,762,806</td>
<td align="right">5.0%</td>
<td align="right">154,763,050</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,507</td>
<td align="right">4.1%</td>
<td align="right">128,815,507</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">68,498,074</td>
<td align="right">5.5%</td>
<td align="right">69,861,566</td>
<td align="right">5.6%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,929,732</td>
<td align="right">2.5%</td>
<td align="right">30,948,739</td>
<td align="right">2.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">30,066,578</td>
<td align="right">2.4%</td>
<td align="right">30,079,935</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">30,993,140</td>
<td align="right">2.5%</td>
<td align="right">31,000,423</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">82,702,719</td>
<td align="right">6.6%</td>
<td align="right">82,687,259</td>
<td align="right">6.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">92,759,381</td>
<td align="right">7.4%</td>
<td align="right">92,760,893</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">26,900,731</td>
<td align="right">2.1%</td>
<td align="right">26,900,950</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,097,220</td>
<td align="right">6.5%</td>
<td align="right">82,096,865</td>
<td align="right">6.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">248,029,571</td>
<td align="right">19.8%</td>
<td align="right">248,029,963</td>
<td align="right">19.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">325,336,792</td>
<td align="right">26.0%</td>
<td align="right">325,336,874</td>
<td align="right">25.9%</td>
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
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,149,808,593</td>
<td align="right">77.2%</td>
<td align="right">5,164,572,988</td>
<td align="right">77.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,399,282,296</td>
<td align="right">80.9%</td>
<td align="right">5,414,183,428</td>
<td align="right">80.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">273,207,568</td>
<td align="right">4.1%</td>
<td align="right">273,450,273</td>
<td align="right">4.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">935,578,882</td>
<td align="right">14.0%</td>
<td align="right">936,350,670</td>
<td align="right">14.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">939,856,212</td>
<td align="right">14.1%</td>
<td align="right">940,628,000</td>
<td align="right">14.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,524,752,116</td>
<td align="right">22.8%</td>
<td align="right">1,525,524,129</td>
<td align="right">22.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,524,752,116</td>
<td align="right">22.8%</td>
<td align="right">1,525,524,129</td>
<td align="right">22.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">260,787,495</td>
<td align="right">3.9%</td>
<td align="right">260,795,049</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,891,646</td>
<td align="right">0.4%</td>
<td align="right">24,891,990</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,330,679</td>
<td align="right">1.1%</td>
<td align="right">70,330,733</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,895,904</td>
<td align="right">8.8%</td>
<td align="right">584,896,129</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,441</td>
<td align="right">0.1%</td>
<td align="right">4,273,441</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">8,087,184</td>
<td align="right"></td>
<td align="right">7,742,166</td>
<td align="right"></td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">60,768,378</td>
<td align="right"></td>
<td align="right">60,499,811</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">26,410,590,776</td>
<td align="right">27.4%</td>
<td align="right">26,521,033,971</td>
<td align="right">27.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">35,045,492,037</td>
<td align="right">30.6%</td>
<td align="right">35,179,284,769</td>
<td align="right">30.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">168,386,060</td>
<td align="right"></td>
<td align="right">168,838,764</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,204,173,659</td>
<td align="right"></td>
<td align="right">2,209,890,823</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,325,027,230</td>
<td align="right">25.2%</td>
<td align="right">24,370,547,314</td>
<td align="right">25.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">25,944,264,504</td>
<td align="right">22.7%</td>
<td align="right">25,986,942,771</td>
<td align="right">22.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,392,428</td>
<td align="right">0.4%</td>
<td align="right">71,507,911</td>
<td align="right">0.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,241,085,681</td>
<td align="right">1.1%</td>
<td align="right">1,243,035,529</td>
<td align="right">1.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">55,374,078</td>
<td align="right"></td>
<td align="right">55,453,670</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,510,334,284</td>
<td align="right">28.1%</td>
<td align="right">5,517,021,721</td>
<td align="right">28.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,432,523,821</td>
<td align="right">27.7%</td>
<td align="right">5,439,091,471</td>
<td align="right">27.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,110,820,567</td>
<td align="right"></td>
<td align="right">6,118,092,196</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,080,880,577</td>
<td align="right"></td>
<td align="right">14,095,309,712</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,080,773,195</td>
<td align="right">71.9%</td>
<td align="right">14,095,169,109</td>
<td align="right">71.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">42,706,627,377</td>
<td align="right">44.3%</td>
<td align="right">42,750,136,989</td>
<td align="right">44.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,957,004,374</td>
<td align="right">3.1%</td>
<td align="right">2,959,882,484</td>
<td align="right">3.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,373,156,212</td>
<td align="right"></td>
<td align="right">2,375,360,806</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">52,266,820,884</td>
<td align="right">45.6%</td>
<td align="right">52,304,530,180</td>
<td align="right">45.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,418,035</td>
<td align="right">0.0%</td>
<td align="right">6,422,339</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,441,243</td>
<td align="right">2.6%</td>
<td align="right">4,441,243</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">434,265</td>
<td align="right">0.3%</td>
<td align="right">434,265</td>
<td align="right">0.3%</td>
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
<td align="right">364,097</td>
<td align="right">101,559,103</td>
<td align="right">9,436,605,074</td>
<td align="right">745,510,970</td>
<td align="right">762,815,031</td>
<td align="right">364,584</td>
<td align="right">102,125,658</td>
<td align="right">9,445,873,552</td>
<td align="right">745,517,930</td>
<td align="right">764,020,088</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,610,014,928</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,610,014,028</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">772</td>
<td align="right">0.2%</td>
<td align="right">788</td>
<td align="right">0.2%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">183,988</td>
<td align="right">39.0%</td>
<td align="right">185,182</td>
<td align="right">39.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">471,333</td>
<td align="right"></td>
<td align="right">472,806</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">209,818</td>
<td align="right">44.5%</td>
<td align="right">210,082</td>
<td align="right">44.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">233,319,870,555</td>
<td align="right">6,271.5%</td>
<td align="right">233,038,548,498</td>
<td align="right">6,261.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">25,052</td>
<td align="right">5.3%</td>
<td align="right">25,035</td>
<td align="right">5.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">52,273</td>
<td align="right">11.1%</td>
<td align="right">52,305</td>
<td align="right">11.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,720,305,408</td>
<td align="right"></td>
<td align="right">3,721,687,610</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">202</td>
<td align="right">0.0%</td>
<td align="right">202</td>
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
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">666</td>
<td align="right">0.1%</td>
<td align="right">666</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">673</td>
<td align="right">0.1%</td>
<td align="right">673</td>
<td align="right">0.1%</td>
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
<td align="right">200</td>
<td align="right">0.8%</td>
<td align="right">200</td>
<td align="right">0.8%</td>
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
<td align="right">21,621</td>
<td align="right">86.3%</td>
<td align="right">21,507</td>
<td align="right">85.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">25,052</td>
<td align="right"></td>
<td align="right">25,035</td>
<td align="right"></td>
<td align="right">-0.1%</td>
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
<td align="right">45,540,030</td>
<td align="right">15.6%</td>
<td align="right">44,296,150</td>
<td align="right">15.4%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">228,151,296</td>
<td align="right">78.0%</td>
<td align="right">224,129,024</td>
<td align="right">78.0%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">292,462,592</td>
<td align="right"></td>
<td align="right">287,424,512</td>
<td align="right"></td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">240,717,914</td>
<td align="right">82.3%</td>
<td align="right">236,983,610</td>
<td align="right">82.5%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">6,204,648</td>
<td align="right">2.1%</td>
<td align="right">6,144,752</td>
<td align="right">2.1%</td>
<td align="right">-1.0%</td>
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
<td align="left">3,510</td>
<td align="right">16.2%</td>
<td align="left">3,663</td>
<td align="right">17.0%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">7,160</td>
<td align="right">33.1%</td>
<td align="left">7,148</td>
<td align="right">33.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">7,300</td>
<td align="right">33.8%</td>
<td align="left">7,074</td>
<td align="right">32.9%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,370</td>
<td align="right">11.0%</td>
<td align="left">2,344</td>
<td align="right">10.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,139</td>
<td align="right">5.3%</td>
<td align="left">1,176</td>
<td align="right">5.5%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">142</td>
<td align="right">0.7%</td>
<td align="left">102</td>
<td align="right">0.5%</td>
<td align="right">-28.2%</td>
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
<td align="right">979</td>
<td align="right">3.9%</td>
<td align="right">987</td>
<td align="right">3.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">710</td>
<td align="right">2.8%</td>
<td align="right">823</td>
<td align="right">3.3%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,200</td>
<td align="right">16.8%</td>
<td align="right">4,202</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,234</td>
<td align="right">32.9%</td>
<td align="right">8,103</td>
<td align="right">32.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,916</td>
<td align="right">19.6%</td>
<td align="right">4,912</td>
<td align="right">19.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,740</td>
<td align="right">18.9%</td>
<td align="right">4,738</td>
<td align="right">18.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,089</td>
<td align="right">4.3%</td>
<td align="right">1,086</td>
<td align="right">4.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">184</td>
<td align="right">0.7%</td>
<td align="right">184</td>
<td align="right">0.7%</td>
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
<td align="right">999</td>
<td align="right">4.0%</td>
<td align="right">1,007</td>
<td align="right">4.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">124</td>
<td align="right">0.5%</td>
<td align="right">237</td>
<td align="right">0.9%</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,176</td>
<td align="right">8.7%</td>
<td align="right">2,225</td>
<td align="right">8.9%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,843</td>
<td align="right">31.3%</td>
<td align="right">7,651</td>
<td align="right">30.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">6,469</td>
<td align="right">25.8%</td>
<td align="right">6,425</td>
<td align="right">25.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,442</td>
<td align="right">9.7%</td>
<td align="right">2,290</td>
<td align="right">9.1%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,209</td>
<td align="right">4.8%</td>
<td align="right">1,395</td>
<td align="right">5.6%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">359</td>
<td align="right">1.4%</td>
<td align="right">277</td>
<td align="right">1.1%</td>
<td align="right">-22.8%</td>
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
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">66,779,420</td>
<td align="right">810,407,185</td>
<td align="right">1,113.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">58,349,671</td>
<td align="right">338,101,535</td>
<td align="right">479.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,968,393</td>
<td align="right">4,056,204</td>
<td align="right">106.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,992,130,666</td>
<td align="right">9,992,619,937</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">3,960,254,000</td>
<td align="right">65,680</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">736,845,997</td>
<td align="right">65,720</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">816,006,559</td>
<td align="right">91,216,550</td>
<td align="right">-88.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">887,481,434</td>
<td align="right">144,446,662</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">273,530,164</td>
<td align="right">49,805,540</td>
<td align="right">-81.8%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">756,226</td>
<td align="right">957,401</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">442,486</td>
<td align="right">545,946</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">214,420</td>
<td align="right">262,174</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">262,153,803</td>
<td align="right">245,755,518</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">2,352,466</td>
<td align="right">2,457,398</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,223,442,835</td>
<td align="right">1,185,923,155</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">7,691,368</td>
<td align="right">7,812,794</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,480,848</td>
<td align="right">5,554,520</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">59,384,164</td>
<td align="right">59,963,503</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">69,061,693</td>
<td align="right">69,677,816</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">362,812,553</td>
<td align="right">359,589,731</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">7,878,682</td>
<td align="right">7,939,855</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">37,092,354</td>
<td align="right">37,346,951</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">35,784,330,505</td>
<td align="right">36,018,751,308</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">40,003,541,637</td>
<td align="right">40,240,281,951</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">143,884,574</td>
<td align="right">144,475,818</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">12,310,511</td>
<td align="right">12,359,373</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">10,186,897</td>
<td align="right">10,223,691</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">34,088,302</td>
<td align="right">34,204,050</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">30,003,242</td>
<td align="right">29,904,662</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">33,363,165</td>
<td align="right">33,460,882</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">58,579,041</td>
<td align="right">58,750,206</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,700,293,351</td>
<td align="right">2,693,666,574</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">156,022,071</td>
<td align="right">156,395,867</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">162,286,512</td>
<td align="right">162,660,121</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">45,518,886</td>
<td align="right">45,622,346</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">262,095,984</td>
<td align="right">261,546,151</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">20,688,842</td>
<td align="right">20,731,849</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">901,109,898</td>
<td align="right">902,786,923</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">901,292,796</td>
<td align="right">902,969,821</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,123,139,144</td>
<td align="right">1,125,093,491</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">75,739,208</td>
<td align="right">75,608,754</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,819,817,202</td>
<td align="right">1,816,737,392</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">344,483,237</td>
<td align="right">344,967,003</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">230,694,347</td>
<td align="right">231,004,132</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">368,701,201</td>
<td align="right">369,184,967</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">394,672,350</td>
<td align="right">395,185,224</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">300,605,615</td>
<td align="right">300,950,304</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">162,045,793</td>
<td align="right">162,225,993</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">62,027,398</td>
<td align="right">62,094,861</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">796,211,842</td>
<td align="right">797,062,551</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">221,557,163</td>
<td align="right">221,783,554</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">157,149,579</td>
<td align="right">157,304,217</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">349,876,403</td>
<td align="right">350,200,037</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,049,980,176</td>
<td align="right">1,049,191,181</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">157,493,978</td>
<td align="right">157,611,159</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">448,945,261</td>
<td align="right">449,269,707</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">450,412,327</td>
<td align="right">450,736,773</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">899,717,594</td>
<td align="right">900,310,598</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">925,120,772</td>
<td align="right">925,713,765</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">925,120,772</td>
<td align="right">925,713,765</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,256,608,880</td>
<td align="right">1,257,345,806</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">734,041,855</td>
<td align="right">734,460,952</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">734,171,655</td>
<td align="right">734,590,752</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">474,626,868</td>
<td align="right">474,897,194</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,144,839,759</td>
<td align="right">3,146,569,471</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">262,650,153</td>
<td align="right">262,774,378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">104,139,848</td>
<td align="right">104,188,701</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,893,158,078</td>
<td align="right">6,896,192,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">686,919,630</td>
<td align="right">687,206,525</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">549,890,125</td>
<td align="right">550,111,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,715,167,602</td>
<td align="right">1,715,831,692</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,428,456,402</td>
<td align="right">1,429,005,188</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,720,305,408</td>
<td align="right">3,721,687,610</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,710,118,258</td>
<td align="right">3,711,463,666</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,556,110,907</td>
<td align="right">1,556,659,693</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">352,355,161</td>
<td align="right">352,479,386</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,140,567,129</td>
<td align="right">6,142,661,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,064,872,089</td>
<td align="right">1,065,231,601</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,378,974,575</td>
<td align="right">3,380,108,413</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,224,155,238</td>
<td align="right">2,224,893,230</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">505,315,647</td>
<td align="right">505,481,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,196,978,022</td>
<td align="right">1,197,364,271</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">264,544,843</td>
<td align="right">264,628,121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,097,554,464</td>
<td align="right">1,097,889,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">460,423,599</td>
<td align="right">460,561,798</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,420,261,721</td>
<td align="right">2,420,974,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">1,957,882,042</td>
<td align="right">1,958,453,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,528,027,111</td>
<td align="right">3,528,973,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,477,965,046</td>
<td align="right">1,478,351,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,763,441,269</td>
<td align="right">2,764,140,721</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,559,329,080</td>
<td align="right">1,559,715,778</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">502,260,511</td>
<td align="right">502,379,373</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">740,847,962</td>
<td align="right">740,676,099</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">418,995,810</td>
<td align="right">419,091,513</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">60,544,010</td>
<td align="right">60,556,229</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,398,483</td>
<td align="right">1,398,232</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">405,652,240</td>
<td align="right">405,721,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,333,902,062</td>
<td align="right">4,334,590,284</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">231,255,478</td>
<td align="right">231,292,123</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,659,041,572</td>
<td align="right">1,659,304,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">729,061,141</td>
<td align="right">729,154,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">612,948,343</td>
<td align="right">612,870,856</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,678,177,800</td>
<td align="right">3,678,627,569</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">813,159,273</td>
<td align="right">813,257,058</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,300,814,222</td>
<td align="right">1,300,966,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,884,674,191</td>
<td align="right">3,885,109,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,665,722,069</td>
<td align="right">1,665,890,304</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,071,219,492</td>
<td align="right">1,071,327,466</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,176,032,730</td>
<td align="right">4,175,631,697</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">604,530,712</td>
<td align="right">604,584,106</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,734,581,739</td>
<td align="right">1,734,723,121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,999,480,956</td>
<td align="right">1,999,627,524</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">747,420,234</td>
<td align="right">747,469,098</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">39,302,951</td>
<td align="right">39,300,635</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,011,095,751</td>
<td align="right">1,011,144,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,722,257,799</td>
<td align="right">7,722,381,172</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,855,711,997</td>
<td align="right">3,855,766,869</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,051,402</td>
<td align="right">40,051,786</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,922,072</td>
<td align="right">1,922,061</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">2,012,702</td>
<td align="right">2,012,691</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,689,804,170</td>
<td align="right">1,689,808,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,146,640,435</td>
<td align="right">3,146,644,721</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">67,947,131</td>
<td align="right">67,947,203</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">67,947,131</td>
<td align="right">67,947,203</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">496,807,850</td>
<td align="right">496,807,326</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">68,657,691</td>
<td align="right">68,657,763</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">273,746,224</td>
<td align="right">273,746,346</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">59,718,355</td>
<td align="right">59,718,344</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,489</td>
<td align="right">70,350,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,489</td>
<td align="right">70,350,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">171,253,991</td>
<td align="right">171,253,980</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,651,357,556</td>
<td align="right">2,651,357,628</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">252,256,115</td>
<td align="right">252,256,117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">148,465,064</td>
<td align="right">148,465,063</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">184,591,829</td>
<td align="right">184,591,828</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">687,284,556</td>
<td align="right">687,284,555</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,224,950,083</td>
<td align="right">2,224,950,083</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,348,014,607</td>
<td align="right">1,348,014,607</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,182,096,629</td>
<td align="right">1,182,096,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,157,768,383</td>
<td align="right">1,157,768,383</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">985,238,793</td>
<td align="right">985,238,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">977,989,247</td>
<td align="right">977,989,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">681,110,981</td>
<td align="right">681,110,981</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">548,796,668</td>
<td align="right">548,796,668</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">546,024,923</td>
<td align="right">546,024,923</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">498,487,330</td>
<td align="right">498,487,330</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">469,637,442</td>
<td align="right">469,637,442</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">425,725,446</td>
<td align="right">425,725,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">425,725,446</td>
<td align="right">425,725,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">405,430,323</td>
<td align="right">405,430,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">360,330,603</td>
<td align="right">360,330,603</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">348,554,161</td>
<td align="right">348,554,161</td>
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
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">206,356,260</td>
<td align="right">206,356,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">161,516,189</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">140,461,197</td>
<td align="right">140,461,197</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">139,450,026</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">131,031,945</td>
<td align="right">131,031,945</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">119,055,799</td>
<td align="right">119,055,799</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,492,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">103,891,386</td>
<td align="right">103,891,386</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">103,178,820</td>
<td align="right">103,178,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">98,412,957</td>
<td align="right">98,412,957</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">72,544,302</td>
<td align="right">72,544,302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,013,740</td>
<td align="right">60,013,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">52,198,435</td>
<td align="right">52,198,435</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">52,198,435</td>
<td align="right">52,198,435</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">50,375,000</td>
<td align="right">50,375,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">47,122,225</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,079</td>
<td align="right">47,071,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">44,407,420</td>
<td align="right">44,407,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">44,407,420</td>
<td align="right">44,407,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">43,842,906</td>
<td align="right">43,842,906</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">40,586,144</td>
<td align="right">40,586,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">39,818,360</td>
<td align="right">39,818,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">37,706,453</td>
<td align="right">37,706,453</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">32,839,369</td>
<td align="right">32,839,369</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">24,483,458</td>
<td align="right">24,483,458</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">24,483,458</td>
<td align="right">24,483,458</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">23,732,161</td>
<td align="right">23,732,161</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">20,612,184</td>
<td align="right">20,612,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">19,637,866</td>
<td align="right">19,637,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">13,229,737</td>
<td align="right">13,229,737</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,973,034</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">8,251,711</td>
<td align="right">8,251,711</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">8,251,711</td>
<td align="right">8,251,711</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">8,116,338</td>
<td align="right">8,116,338</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,137,792</td>
<td align="right">6,137,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">5,360,689</td>
<td align="right">5,360,689</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,650,796</td>
<td align="right">4,650,796</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,473,478</td>
<td align="right">4,473,478</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,366,545</td>
<td align="right">3,366,545</td>
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
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">2,972,592</td>
<td align="right">2,972,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">2,972,592</td>
<td align="right">2,972,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">2,159,367</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,404,690</td>
<td align="right">1,404,690</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">954,726</td>
<td align="right">954,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">574,810</td>
<td align="right">574,810</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">446,880</td>
<td align="right">446,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">255,096</td>
<td align="right">255,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">183,840</td>
<td align="right">183,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">93,156</td>
<td align="right">93,156</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">65,780</td>
<td align="right">65,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">27,762</td>
<td align="right">27,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">26,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">15,393</td>
<td align="right">15,393</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">253</td>
<td align="right">253</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">23,769</td>
<td align="right">23,797</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,583</td>
<td align="right">6,581</td>
<td align="right">-0.0%</td>
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
<td align="right">100</td>
<td align="right">100</td>
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
<td align="right">100</td>
<td align="right">100</td>
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
<td align="right">2,458</td>
<td align="right">2,458</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-24
