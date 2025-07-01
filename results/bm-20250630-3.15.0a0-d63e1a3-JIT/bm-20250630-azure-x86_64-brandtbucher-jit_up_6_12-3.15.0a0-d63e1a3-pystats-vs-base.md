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
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,315,340</td>
<td align="right">504,205</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">114,350,367</td>
<td align="right">76,994,960</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,265,188</td>
<td align="right">956,279</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">52,075,598</td>
<td align="right">39,547,518</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,349,805</td>
<td align="right">1,033,846</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">85,283,939</td>
<td align="right">66,741,534</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">207,957,783</td>
<td align="right">170,156,494</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">96,653,286</td>
<td align="right">80,186,312</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,807,102</td>
<td align="right">2,368,676</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">220,246,698</td>
<td align="right">186,822,558</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,354,001</td>
<td align="right">2,876,344</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">369,954,636</td>
<td align="right">321,697,523</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">94,311,927</td>
<td align="right">82,582,872</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">57,327,364</td>
<td align="right">50,432,809</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">449,939,615</td>
<td align="right">396,793,073</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">111,699,135</td>
<td align="right">100,016,616</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">197,567,460</td>
<td align="right">178,097,032</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">126,964,760</td>
<td align="right">114,610,250</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">37,070,159</td>
<td align="right">33,467,396</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,099,922,867</td>
<td align="right">995,271,098</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">42,025,370</td>
<td align="right">38,300,874</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">14,297,526</td>
<td align="right">13,085,500</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">182,621,912</td>
<td align="right">167,160,092</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,840,180</td>
<td align="right">2,604,900</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,542,876</td>
<td align="right">167,773,761</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">77,863,075</td>
<td align="right">71,806,647</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,035,674,002</td>
<td align="right">1,882,378,162</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">164,689,544</td>
<td align="right">152,509,919</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">163,945,034</td>
<td align="right">152,038,063</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">431,759,287</td>
<td align="right">401,102,856</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">957,654,786</td>
<td align="right">891,604,528</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">49,734,678</td>
<td align="right">46,391,884</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">907,099,296</td>
<td align="right">846,607,933</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">178,177,806</td>
<td align="right">166,501,454</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">78,915</td>
<td align="right">73,770</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">709,897,881</td>
<td align="right">665,272,500</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">27,571,619</td>
<td align="right">25,838,999</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">96,871,386</td>
<td align="right">91,043,903</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">373,881,548</td>
<td align="right">351,556,181</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,090,483,630</td>
<td align="right">1,025,817,727</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">624,059,745</td>
<td align="right">587,386,500</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">11,163,960</td>
<td align="right">10,509,311</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">209,837,953</td>
<td align="right">197,642,047</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">910,283,530</td>
<td align="right">859,054,404</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,562,154</td>
<td align="right">99,670,034</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">148,537,414</td>
<td align="right">140,418,653</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">220,719,607</td>
<td align="right">209,491,957</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,544,932</td>
<td align="right">5,264,799</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">383,888,736</td>
<td align="right">365,134,147</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,877,728,302</td>
<td align="right">16,065,387,315</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">852,853,951</td>
<td align="right">892,544,511</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,088,363,503</td>
<td align="right">4,857,168,025</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">42,727,340</td>
<td align="right">40,788,661</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">127,900,098</td>
<td align="right">122,157,107</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">149,217,724</td>
<td align="right">142,747,365</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">352,815,775</td>
<td align="right">337,524,911</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">37,576,131</td>
<td align="right">36,078,710</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,387,602,242</td>
<td align="right">3,252,938,156</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">467,975,397</td>
<td align="right">449,624,003</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,245,700</td>
<td align="right">6,003,780</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,516,861</td>
<td align="right">4,342,601</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">658,003,425</td>
<td align="right">632,838,049</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,729,160</td>
<td align="right">9,377,530</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">19,387,660</td>
<td align="right">18,704,174</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">919,629,220</td>
<td align="right">887,361,262</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">878,207,320</td>
<td align="right">847,704,665</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">274,430,759</td>
<td align="right">265,034,006</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">124,153,260</td>
<td align="right">119,953,379</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,154,551,351</td>
<td align="right">4,015,856,309</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">472,408,781</td>
<td align="right">456,931,944</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">134,670,752</td>
<td align="right">130,317,063</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">281,033,223</td>
<td align="right">271,972,784</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">168,432,590</td>
<td align="right">163,059,285</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,560,932</td>
<td align="right">9,261,834</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,191,708,326</td>
<td align="right">4,062,203,436</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">55,469,573</td>
<td align="right">53,768,370</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">173,731,396</td>
<td align="right">168,457,155</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">924,067,033</td>
<td align="right">896,593,767</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">119,116,381</td>
<td align="right">115,614,885</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">264,958,212</td>
<td align="right">257,337,063</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">927,739,606</td>
<td align="right">901,190,834</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">560,164</td>
<td align="right">544,244</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">424,197,537</td>
<td align="right">413,039,201</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,278,437</td>
<td align="right">47,063,680</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,049,994,079</td>
<td align="right">1,999,181,756</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,529,308,299</td>
<td align="right">1,491,606,770</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">77,451,619</td>
<td align="right">75,571,603</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,338,476,900</td>
<td align="right">2,282,344,940</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">279,175,484</td>
<td align="right">272,527,804</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">124,871,671</td>
<td align="right">121,940,759</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">462,070,383</td>
<td align="right">451,653,588</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,745,426,082</td>
<td align="right">3,663,252,024</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">179,363,972</td>
<td align="right">175,447,157</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">207,570,809</td>
<td align="right">203,192,247</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,023,632,559</td>
<td align="right">1,980,993,755</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">52,652,481</td>
<td align="right">51,591,833</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">69,035,271</td>
<td align="right">67,666,388</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,880,262</td>
<td align="right">61,993,671</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">297,390,974</td>
<td align="right">291,990,457</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">137,139,376</td>
<td align="right">134,714,491</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">255,013,031</td>
<td align="right">259,432,264</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">508,784,561</td>
<td align="right">500,140,007</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">246,747,882</td>
<td align="right">242,566,697</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">115,592,511</td>
<td align="right">113,667,771</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">561,252,265</td>
<td align="right">552,205,933</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,713,139,684</td>
<td align="right">4,637,421,168</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,664,671,264</td>
<td align="right">2,623,410,522</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,001,033</td>
<td align="right">25,602,048</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,531,045,079</td>
<td align="right">2,493,112,253</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">112,289,889</td>
<td align="right">110,661,864</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,041,508</td>
<td align="right">30,594,688</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">64,309,172</td>
<td align="right">63,411,591</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">811,093,912</td>
<td align="right">800,000,227</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">71,659,486</td>
<td align="right">70,725,934</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,739,597</td>
<td align="right">61,020,775</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">558,504,350</td>
<td align="right">552,365,067</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">833,067,438</td>
<td align="right">824,615,674</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">81,470,442</td>
<td align="right">80,677,357</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">384,319,805</td>
<td align="right">380,581,558</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">283,417,966</td>
<td align="right">280,710,548</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,055,566,867</td>
<td align="right">5,008,249,526</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">70,308,077</td>
<td align="right">69,660,381</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">75,115,545</td>
<td align="right">74,553,231</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,445,686</td>
<td align="right">41,135,491</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">256,775,015</td>
<td align="right">254,865,572</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">621,768,803</td>
<td align="right">617,347,711</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,136,625,291</td>
<td align="right">1,129,082,270</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">120,446,284</td>
<td align="right">119,762,798</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">141,371,283</td>
<td align="right">140,624,564</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">672,358,104</td>
<td align="right">668,997,274</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,184,173</td>
<td align="right">123,576,181</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">71,145,807</td>
<td align="right">70,824,467</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">372,813,493</td>
<td align="right">371,133,439</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">346,654,349</td>
<td align="right">345,092,264</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,715,231</td>
<td align="right">10,672,921</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">368,501,623</td>
<td align="right">367,193,248</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">21,535,496</td>
<td align="right">21,602,417</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">292,970,077</td>
<td align="right">292,347,553</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,450,765</td>
<td align="right">3,446,291</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">262,522,015</td>
<td align="right">262,827,931</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">68,512,998</td>
<td align="right">68,480,557</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,599,289</td>
<td align="right">190,516,049</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">332,127,556</td>
<td align="right">332,264,449</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,107,626,231</td>
<td align="right">1,107,762,992</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">69,833,463</td>
<td align="right">69,824,903</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">92,081</td>
<td align="right">92,087</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,439,741</td>
<td align="right">28,440,987</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,147,679</td>
<td align="right">21,147,071</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,423,284</td>
<td align="right">21,422,676</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,423,305</td>
<td align="right">21,422,697</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">13,523,652</td>
<td align="right">13,523,886</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,100,401</td>
<td align="right">3,100,358</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,576,539</td>
<td align="right">1,576,519</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">323,893</td>
<td align="right">323,889</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,680,537</td>
<td align="right">6,680,603</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">333,541</td>
<td align="right">333,538</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,540,620,411</td>
<td align="right">1,540,614,828</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,682,739</td>
<td align="right">114,682,924</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">15,619,526</td>
<td align="right">15,619,501</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,279,017</td>
<td align="right">6,279,007</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">11,838,596</td>
<td align="right">11,838,586</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,925,954</td>
<td align="right">35,925,981</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,705,679</td>
<td align="right">418,705,635</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">241,369,152</td>
<td align="right">241,369,174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">243,419,240</td>
<td align="right">243,419,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,078,481</td>
<td align="right">155,078,490</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,462,202</td>
<td align="right">591,462,229</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,552,075</td>
<td align="right">302,552,075</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,636,886</td>
<td align="right">172,636,886</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,310,545</td>
<td align="right">129,310,545</td>
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
<td align="right">41,858,530</td>
<td align="right">41,858,530</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,660</td>
<td align="right">29,134,660</td>
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
<td align="right">8,951,274</td>
<td align="right">8,951,274</td>
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
<td align="left">RERAISE</td>
<td align="right">4,130,887</td>
<td align="right">4,130,887</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">2,332,004</td>
<td align="right">2,332,004</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">120,759</td>
<td align="right">120,759</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">115,623</td>
<td align="right">115,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">106,196</td>
<td align="right">106,196</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">74,319</td>
<td align="right">74,319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">73,792</td>
<td align="right">73,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">50,315</td>
<td align="right">50,315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">23,410</td>
<td align="right">23,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">19,258</td>
<td align="right">19,258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,158</td>
<td align="right">14,158</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,959</td>
<td align="right">5,959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">3,696</td>
<td align="right">3,696</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,709</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,776</td>
<td align="right">1,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">725</td>
<td align="right">725</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
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
<td align="right">1,089,672,394</td>
<td align="right">6.3%</td>
<td align="right">1,025,057,322</td>
<td align="right">5.9%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">65,513,558</td>
<td align="right">0.4%</td>
<td align="right">69,266,149</td>
<td align="right">0.4%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,139,704,256</td>
<td align="right">93.3%</td>
<td align="right">16,136,392,108</td>
<td align="right">93.6%</td>
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
<td align="right">653,866</td>
<td align="right">32.0%</td>
<td align="right">603,159</td>
<td align="right">29.2%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,391,549</td>
<td align="right">68.0%</td>
<td align="right">1,462,294</td>
<td align="right">70.8%</td>
<td align="right">5.1%</td>
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
<td align="left">and int</td>
<td align="right">29,721</td>
<td align="right">4.5%</td>
<td align="right">11,289</td>
<td align="right">1.9%</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">15,181</td>
<td align="right">2.3%</td>
<td align="right">11,457</td>
<td align="right">1.9%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">5,212</td>
<td align="right">0.8%</td>
<td align="right">4,032</td>
<td align="right">0.7%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">25,123</td>
<td align="right">3.8%</td>
<td align="right">20,623</td>
<td align="right">3.4%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">39,645</td>
<td align="right">6.1%</td>
<td align="right">33,702</td>
<td align="right">5.6%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">15,139</td>
<td align="right">2.3%</td>
<td align="right">13,491</td>
<td align="right">2.2%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">5,350</td>
<td align="right">0.8%</td>
<td align="right">4,864</td>
<td align="right">0.8%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">56,721</td>
<td align="right">8.7%</td>
<td align="right">52,025</td>
<td align="right">8.6%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">33,181</td>
<td align="right">5.1%</td>
<td align="right">30,831</td>
<td align="right">5.1%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">3,093</td>
<td align="right">0.5%</td>
<td align="right">2,890</td>
<td align="right">0.5%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">59,119</td>
<td align="right">9.0%</td>
<td align="right">55,620</td>
<td align="right">9.2%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">15,464</td>
<td align="right">2.4%</td>
<td align="right">14,596</td>
<td align="right">2.4%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">588</td>
<td align="right">0.1%</td>
<td align="right">567</td>
<td align="right">0.1%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">16,575</td>
<td align="right">2.5%</td>
<td align="right">16,007</td>
<td align="right">2.7%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">8,464</td>
<td align="right">1.3%</td>
<td align="right">8,296</td>
<td align="right">1.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,181</td>
<td align="right">0.8%</td>
<td align="right">5,081</td>
<td align="right">0.8%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">28,112</td>
<td align="right">4.3%</td>
<td align="right">27,583</td>
<td align="right">4.6%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,784</td>
<td align="right">7.5%</td>
<td align="right">47,873</td>
<td align="right">7.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">4,237</td>
<td align="right">0.6%</td>
<td align="right">4,197</td>
<td align="right">0.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">71,308</td>
<td align="right">10.9%</td>
<td align="right">70,702</td>
<td align="right">11.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">29,084</td>
<td align="right">4.4%</td>
<td align="right">28,916</td>
<td align="right">4.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,417</td>
<td align="right">0.2%</td>
<td align="right">1,411</td>
<td align="right">0.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,953</td>
<td align="right">1.7%</td>
<td align="right">10,933</td>
<td align="right">1.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,041</td>
<td align="right">0.2%</td>
<td align="right">1,042</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">109,863</td>
<td align="right">16.8%</td>
<td align="right">109,821</td>
<td align="right">18.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">5,634</td>
<td align="right">0.9%</td>
<td align="right">5,634</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,765</td>
<td align="right">0.6%</td>
<td align="right">3,765</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,756</td>
<td align="right">0.4%</td>
<td align="right">2,756</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">1,207</td>
<td align="right">0.2%</td>
<td align="right">1,207</td>
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
<td align="right">560</td>
<td align="right">0.1%</td>
<td align="right">560</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">343</td>
<td align="right">0.1%</td>
<td align="right">343</td>
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
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
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
<td align="right">182,542,876</td>
<td align="right">100.0%</td>
<td align="right">167,773,761</td>
<td align="right">100.0%</td>
<td align="right">-8.1%</td>
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
<td align="right">163,291,096</td>
<td align="right">1.5%</td>
<td align="right">164,410,308</td>
<td align="right">1.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">161,190,588</td>
<td align="right">1.5%</td>
<td align="right">162,288,607</td>
<td align="right">1.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,948,151,433</td>
<td align="right">98.5%</td>
<td align="right">10,949,859,336</td>
<td align="right">98.5%</td>
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
<td align="right">6,720</td>
<td align="right">0.0%</td>
<td align="right">6,720</td>
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
<td align="right">3,676,881</td>
<td align="right">100.0%</td>
<td align="right">3,698,054</td>
<td align="right">100.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">166</td>
<td align="right">0.0%</td>
<td align="right">166</td>
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
<td align="right">3,414</td>
<td align="right">2,056.6%</td>
<td align="right">3,414</td>
<td align="right">2,056.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">947</td>
<td align="right">570.5%</td>
<td align="right">947</td>
<td align="right">570.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">166</td>
<td align="right">100.0%</td>
<td align="right">166</td>
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
<td align="right">685,038</td>
<td align="right">91.8%</td>
<td align="right">685,038</td>
<td align="right">91.8%</td>
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
<td align="right">640,338</td>
<td align="right">85.8%</td>
<td align="right">640,338</td>
<td align="right">85.8%</td>
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
<td align="right">61,496</td>
<td align="right">100.0%</td>
<td align="right">61,496</td>
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
<td align="right">96,636,766</td>
<td align="right">2.1%</td>
<td align="right">90,810,979</td>
<td align="right">2.0%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,317,091</td>
<td align="right">0.0%</td>
<td align="right">1,308,312</td>
<td align="right">0.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,500,056,897</td>
<td align="right">97.9%</td>
<td align="right">4,499,357,249</td>
<td align="right">98.0%</td>
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
<td align="right">169,282</td>
<td align="right">65.4%</td>
<td align="right">167,584</td>
<td align="right">65.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">89,711</td>
<td align="right">34.6%</td>
<td align="right">89,552</td>
<td align="right">34.8%</td>
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
<td align="left">set</td>
<td align="right">1,244</td>
<td align="right">0.7%</td>
<td align="right">1,162</td>
<td align="right">0.7%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,848</td>
<td align="right">1.7%</td>
<td align="right">2,681</td>
<td align="right">1.6%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">12,209</td>
<td align="right">7.2%</td>
<td align="right">11,801</td>
<td align="right">7.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">15,628</td>
<td align="right">9.2%</td>
<td align="right">15,142</td>
<td align="right">9.0%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,394</td>
<td align="right">7.3%</td>
<td align="right">12,228</td>
<td align="right">7.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">62,979</td>
<td align="right">37.2%</td>
<td align="right">62,603</td>
<td align="right">37.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">8,883</td>
<td align="right">5.2%</td>
<td align="right">8,841</td>
<td align="right">5.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,339</td>
<td align="right">16.1%</td>
<td align="right">27,393</td>
<td align="right">16.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">19,251</td>
<td align="right">11.4%</td>
<td align="right">19,226</td>
<td align="right">11.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,151</td>
<td align="right">1.9%</td>
<td align="right">3,151</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">2,842</td>
<td align="right">1.7%</td>
<td align="right">2,842</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">514</td>
<td align="right">0.3%</td>
<td align="right">514</td>
<td align="right">0.3%</td>
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
<td align="right">94,191,901</td>
<td align="right">4.1%</td>
<td align="right">82,466,231</td>
<td align="right">3.6%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,177,558,546</td>
<td align="right">95.8%</td>
<td align="right">2,177,557,720</td>
<td align="right">96.3%</td>
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
<td align="right">1,043,801</td>
<td align="right">0.0%</td>
<td align="right">1,043,801</td>
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
<td align="right">104,336</td>
<td align="right">74.7%</td>
<td align="right">100,951</td>
<td align="right">74.1%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">35,271</td>
<td align="right">25.3%</td>
<td align="right">35,271</td>
<td align="right">25.9%</td>
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
<td align="right">18,063</td>
<td align="right">17.3%</td>
<td align="right">16,957</td>
<td align="right">16.8%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">23,849</td>
<td align="right">22.9%</td>
<td align="right">23,037</td>
<td align="right">22.8%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">31,479</td>
<td align="right">30.2%</td>
<td align="right">30,567</td>
<td align="right">30.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">30,945</td>
<td align="right">29.7%</td>
<td align="right">30,390</td>
<td align="right">30.1%</td>
<td align="right">-1.8%</td>
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
<td align="right">219,979,742</td>
<td align="right">13.5%</td>
<td align="right">186,577,957</td>
<td align="right">12.2%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,341,351,150</td>
<td align="right">82.6%</td>
<td align="right">1,278,815,147</td>
<td align="right">83.7%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">62,660,171</td>
<td align="right">3.9%</td>
<td align="right">61,329,051</td>
<td align="right">4.0%</td>
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
<td align="left">Failure</td>
<td align="right">207,398</td>
<td align="right">14.3%</td>
<td align="right">184,955</td>
<td align="right">13.2%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,241,392</td>
<td align="right">85.7%</td>
<td align="right">1,216,390</td>
<td align="right">86.8%</td>
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
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">14,829</td>
<td align="right">7.2%</td>
<td align="right">9,961</td>
<td align="right">5.4%</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,183</td>
<td align="right">0.6%</td>
<td align="right">805</td>
<td align="right">0.4%</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,577</td>
<td align="right">9.0%</td>
<td align="right">14,452</td>
<td align="right">7.8%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,646</td>
<td align="right">1.8%</td>
<td align="right">3,014</td>
<td align="right">1.6%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">18,890</td>
<td align="right">9.1%</td>
<td align="right">16,269</td>
<td align="right">8.8%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,042</td>
<td align="right">5.3%</td>
<td align="right">9,766</td>
<td align="right">5.3%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">10,336</td>
<td align="right">5.0%</td>
<td align="right">9,229</td>
<td align="right">5.0%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,675</td>
<td align="right">2.7%</td>
<td align="right">5,167</td>
<td align="right">2.8%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">1,159</td>
<td align="right">0.6%</td>
<td align="right">1,076</td>
<td align="right">0.6%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">78,599</td>
<td align="right">37.9%</td>
<td align="right">73,428</td>
<td align="right">39.7%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">17,570</td>
<td align="right">8.5%</td>
<td align="right">16,513</td>
<td align="right">8.9%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">7,926</td>
<td align="right">3.8%</td>
<td align="right">7,634</td>
<td align="right">4.1%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">11,401</td>
<td align="right">5.5%</td>
<td align="right">11,258</td>
<td align="right">6.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,496</td>
<td align="right">2.2%</td>
<td align="right">4,455</td>
<td align="right">2.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,829</td>
<td align="right">0.9%</td>
<td align="right">1,828</td>
<td align="right">1.0%</td>
<td align="right">-0.1%</td>
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
<td align="left">tuple</td>
<td align="right">173,347,660</td>
<td align="right">173,347,660 / 0 !!</td>
<td align="right">173,246,006</td>
<td align="right">173,246,006 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,372,891</td>
<td align="right">12,372,891 / 0 !!</td>
<td align="right">12,371,669</td>
<td align="right">12,371,669 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,649,325</td>
<td align="right">5,649,325 / 0 !!</td>
<td align="right">5,649,313</td>
<td align="right">5,649,313 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">305,510,719</td>
<td align="right">305,510,719 / 0 !!</td>
<td align="right">305,510,465</td>
<td align="right">305,510,465 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">336,990,206</td>
<td align="right">336,990,206 / 0 !!</td>
<td align="right">336,989,975</td>
<td align="right">336,989,975 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,671,555</td>
<td align="right">101,671,555 / 0 !!</td>
<td align="right">101,671,502</td>
<td align="right">101,671,502 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">116,484,574</td>
<td align="right">116,484,574 / 0 !!</td>
<td align="right">116,484,625</td>
<td align="right">116,484,625 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,205,175</td>
<td align="right">34,205,175 / 0 !!</td>
<td align="right">34,205,175</td>
<td align="right">34,205,175 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,297,294</td>
<td align="right">2,297,294 / 0 !!</td>
<td align="right">2,297,294</td>
<td align="right">2,297,294 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">814,329</td>
<td align="right">814,329 / 0 !!</td>
<td align="right">814,329</td>
<td align="right">814,329 / 0 !!</td>
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
<td align="right">645,871,089</td>
<td align="right">5.6%</td>
<td align="right">660,792,851</td>
<td align="right">5.8%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">555,790,065</td>
<td align="right">4.8%</td>
<td align="right">549,682,924</td>
<td align="right">4.8%</td>
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
<td align="right">10,322,429,880</td>
<td align="right">89.6%</td>
<td align="right">10,239,860,106</td>
<td align="right">89.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,133,675</td>
<td align="right">0.0%</td>
<td align="right">1,133,675</td>
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
<td align="right">12,793,776</td>
<td align="right">94.3%</td>
<td align="right">13,074,961</td>
<td align="right">94.5%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">766,906</td>
<td align="right">5.7%</td>
<td align="right">763,188</td>
<td align="right">5.5%</td>
<td align="right">-0.5%</td>
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
<td align="right">78,458</td>
<td align="right">10.2%</td>
<td align="right">77,003</td>
<td align="right">10.1%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,856</td>
<td align="right">0.4%</td>
<td align="right">2,814</td>
<td align="right">0.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">41,197</td>
<td align="right">5.4%</td>
<td align="right">41,800</td>
<td align="right">5.5%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">4,327</td>
<td align="right">0.6%</td>
<td align="right">4,267</td>
<td align="right">0.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">76,204</td>
<td align="right">9.9%</td>
<td align="right">75,174</td>
<td align="right">9.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,673</td>
<td align="right">0.2%</td>
<td align="right">1,653</td>
<td align="right">0.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">15,083</td>
<td align="right">2.0%</td>
<td align="right">14,903</td>
<td align="right">2.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4,745</td>
<td align="right">0.6%</td>
<td align="right">4,703</td>
<td align="right">0.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">12,303</td>
<td align="right">1.6%</td>
<td align="right">12,223</td>
<td align="right">1.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">30,642</td>
<td align="right">4.0%</td>
<td align="right">30,461</td>
<td align="right">4.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">138,884</td>
<td align="right">18.1%</td>
<td align="right">138,202</td>
<td align="right">18.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">21,886</td>
<td align="right">2.9%</td>
<td align="right">21,865</td>
<td align="right">2.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">9,020</td>
<td align="right">1.2%</td>
<td align="right">9,020</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,092</td>
<td align="right">0.1%</td>
<td align="right">1,092</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">1,021</td>
<td align="right">0.1%</td>
<td align="right">1,021</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">106</td>
<td align="right">0.0%</td>
<td align="right">106</td>
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
<td align="right">4,680,322,846</td>
<td align="right">99.7%</td>
<td align="right">4,604,932,377</td>
<td align="right">99.7%</td>
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
<td align="right">15,098,961</td>
<td align="right">0.3%</td>
<td align="right">15,098,946</td>
<td align="right">0.3%</td>
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
<td align="right">5,094</td>
<td align="right">0.0%</td>
<td align="right">5,094</td>
<td align="right">0.0%</td>
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
<td align="right">302,514</td>
<td align="right">0.0%</td>
<td align="right">302,514</td>
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
<td align="right">525,508</td>
<td align="right">100.0%</td>
<td align="right">525,498</td>
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
<td align="right">67,201,443</td>
<td align="right">100.0%</td>
<td align="right">67,201,389</td>
<td align="right">100.0%</td>
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
<td align="right">6,988</td>
<td align="right">0.0%</td>
<td align="right">6,988</td>
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
<td align="right">7,170</td>
<td align="right">100.0%</td>
<td align="right">7,170</td>
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
<td align="right">591,434,781</td>
<td align="right">82.1%</td>
<td align="right">591,434,808</td>
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
<td align="right">129,260,570</td>
<td align="right">17.9%</td>
<td align="right">129,260,570</td>
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
<td align="right">27,421</td>
<td align="right">0.0%</td>
<td align="right">27,421</td>
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
<td align="right">4,554</td>
<td align="right">9.0%</td>
<td align="right">4,554</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,927</td>
<td align="right">91.0%</td>
<td align="right">45,927</td>
<td align="right">91.0%</td>
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
<td align="right">25,040</td>
<td align="right">54.5%</td>
<td align="right">25,040</td>
<td align="right">54.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,693</td>
<td align="right">21.1%</td>
<td align="right">9,693</td>
<td align="right">21.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,073</td>
<td align="right">19.8%</td>
<td align="right">9,073</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,121</td>
<td align="right">4.6%</td>
<td align="right">2,121</td>
<td align="right">4.6%</td>
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
<td align="right">121,306,811</td>
<td align="right">6.1%</td>
<td align="right">118,520,806</td>
<td align="right">5.9%</td>
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
<td align="right">61,527,711</td>
<td align="right">3.1%</td>
<td align="right">60,809,503</td>
<td align="right">3.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,812,242,980</td>
<td align="right">90.8%</td>
<td align="right">1,814,976,438</td>
<td align="right">91.0%</td>
<td align="right">0.2%</td>
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
<td align="right">2,395,070</td>
<td align="right">95.9%</td>
<td align="right">2,342,391</td>
<td align="right">95.9%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">101,541</td>
<td align="right">4.1%</td>
<td align="right">100,927</td>
<td align="right">4.1%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">8,313</td>
<td align="right">8.2%</td>
<td align="right">7,704</td>
<td align="right">7.6%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">310,943</td>
<td align="right">306.2%</td>
<td align="right">310,475</td>
<td align="right">307.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">11,039</td>
<td align="right">10.9%</td>
<td align="right">11,035</td>
<td align="right">10.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">43,627</td>
<td align="right">43.0%</td>
<td align="right">43,626</td>
<td align="right">43.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">14,124</td>
<td align="right">13.9%</td>
<td align="right">14,124</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">7,974</td>
<td align="right">7.9%</td>
<td align="right">7,974</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">7,044</td>
<td align="right">6.9%</td>
<td align="right">7,044</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,088</td>
<td align="right">3.0%</td>
<td align="right">3,088</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,823</td>
<td align="right">1.8%</td>
<td align="right">1,823</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">631</td>
<td align="right">0.6%</td>
<td align="right">631</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">603</td>
<td align="right">0.6%</td>
<td align="right">603</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">273</td>
<td align="right">0.3%</td>
<td align="right">273</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">251</td>
<td align="right">0.2%</td>
<td align="right">251</td>
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
<td align="right">1,349,805</td>
<td align="right">100.0%</td>
<td align="right">1,033,846</td>
<td align="right">100.0%</td>
<td align="right">-23.4%</td>
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
<td align="right">105,467,002</td>
<td align="right">10.3%</td>
<td align="right">99,577,379</td>
<td align="right">9.8%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">914,511,045</td>
<td align="right">89.7%</td>
<td align="right">914,504,210</td>
<td align="right">90.2%</td>
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
<td align="right">2,160</td>
<td align="right">0.0%</td>
<td align="right">2,160</td>
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
<td align="right">79,984</td>
<td align="right">84.0%</td>
<td align="right">77,487</td>
<td align="right">83.6%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,208</td>
<td align="right">16.0%</td>
<td align="right">15,208</td>
<td align="right">16.4%</td>
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
<td align="left">array slice</td>
<td align="right">168</td>
<td align="right">0.2%</td>
<td align="right">126</td>
<td align="right">0.2%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">850</td>
<td align="right">1.1%</td>
<td align="right">682</td>
<td align="right">0.9%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,174</td>
<td align="right">20.2%</td>
<td align="right">14,667</td>
<td align="right">18.9%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">2,282</td>
<td align="right">2.9%</td>
<td align="right">2,098</td>
<td align="right">2.7%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,909</td>
<td align="right">9.9%</td>
<td align="right">7,313</td>
<td align="right">9.4%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">45,076</td>
<td align="right">56.4%</td>
<td align="right">45,076</td>
<td align="right">58.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,465</td>
<td align="right">5.6%</td>
<td align="right">4,465</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,060</td>
<td align="right">3.8%</td>
<td align="right">3,060</td>
<td align="right">3.9%</td>
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
<td align="right">136,350,544</td>
<td align="right">3.1%</td>
<td align="right">133,891,518</td>
<td align="right">3.1%</td>
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
<td align="right">4,188,193,923</td>
<td align="right">95.3%</td>
<td align="right">4,139,528,768</td>
<td align="right">95.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">71,625,985</td>
<td align="right">1.6%</td>
<td align="right">72,131,656</td>
<td align="right">1.7%</td>
<td align="right">0.7%</td>
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
<td align="right">564,865</td>
<td align="right">26.5%</td>
<td align="right">599,040</td>
<td align="right">27.5%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,569,587</td>
<td align="right">73.5%</td>
<td align="right">1,579,070</td>
<td align="right">72.5%</td>
<td align="right">0.6%</td>
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
<td align="right">80,050</td>
<td align="right">14.2%</td>
<td align="right">115,067</td>
<td align="right">19.2%</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">6,816</td>
<td align="right">1.2%</td>
<td align="right">6,356</td>
<td align="right">1.1%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">11,602</td>
<td align="right">2.1%</td>
<td align="right">11,497</td>
<td align="right">1.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">18,579</td>
<td align="right">3.3%</td>
<td align="right">18,436</td>
<td align="right">3.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">86,823</td>
<td align="right">15.4%</td>
<td align="right">86,677</td>
<td align="right">14.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,930</td>
<td align="right">3.5%</td>
<td align="right">19,911</td>
<td align="right">3.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">81,561</td>
<td align="right">14.4%</td>
<td align="right">81,581</td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,442</td>
<td align="right">45.6%</td>
<td align="right">257,453</td>
<td align="right">43.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">622</td>
<td align="right">0.1%</td>
<td align="right">622</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
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
<td align="right">1,275,710</td>
<td align="right">0.1%</td>
<td align="right">464,952</td>
<td align="right">0.0%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,240,929,579</td>
<td align="right">99.9%</td>
<td align="right">1,241,052,997</td>
<td align="right">100.0%</td>
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
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">2,660</td>
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
<td align="right">2,473</td>
<td align="right">6.2%</td>
<td align="right">2,096</td>
<td align="right">5.3%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">37,197</td>
<td align="right">93.8%</td>
<td align="right">37,197</td>
<td align="right">94.7%</td>
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
<td align="left">sequence</td>
<td align="right">1,779</td>
<td align="right">71.9%</td>
<td align="right">1,402</td>
<td align="right">66.9%</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">378</td>
<td align="right">15.3%</td>
<td align="right">378</td>
<td align="right">18.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">316</td>
<td align="right">12.8%</td>
<td align="right">316</td>
<td align="right">15.1%</td>
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
<td align="right">3,257,946,368</td>
<td align="right">3.2%</td>
<td align="right">3,102,182,091</td>
<td align="right">3.2%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">36,448,705,546</td>
<td align="right">36.1%</td>
<td align="right">35,215,903,574</td>
<td align="right">36.1%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">60,098,417,259</td>
<td align="right">59.5%</td>
<td align="right">58,093,090,100</td>
<td align="right">59.5%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,133,769,264</td>
<td align="right">1.1%</td>
<td align="right">1,149,935,430</td>
<td align="right">1.2%</td>
<td align="right">1.4%</td>
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
<td align="right">219,979,742</td>
<td align="right">7.7%</td>
<td align="right">186,577,957</td>
<td align="right">6.9%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">94,191,901</td>
<td align="right">3.3%</td>
<td align="right">82,466,231</td>
<td align="right">3.0%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,542,876</td>
<td align="right">6.4%</td>
<td align="right">167,773,761</td>
<td align="right">6.2%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">96,636,766</td>
<td align="right">3.4%</td>
<td align="right">90,810,979</td>
<td align="right">3.4%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,089,672,394</td>
<td align="right">38.2%</td>
<td align="right">1,025,057,322</td>
<td align="right">37.9%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,467,002</td>
<td align="right">3.7%</td>
<td align="right">99,577,379</td>
<td align="right">3.7%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">136,350,544</td>
<td align="right">4.8%</td>
<td align="right">133,891,518</td>
<td align="right">4.9%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">555,790,065</td>
<td align="right">19.5%</td>
<td align="right">549,682,924</td>
<td align="right">20.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">161,190,588</td>
<td align="right">5.7%</td>
<td align="right">162,288,607</td>
<td align="right">6.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,260,570</td>
<td align="right">4.5%</td>
<td align="right">129,260,570</td>
<td align="right">4.8%</td>
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
<td align="right">62,304,809</td>
<td align="right">5.5%</td>
<td align="right">66,464,820</td>
<td align="right">5.8%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">82,085,095</td>
<td align="right">7.2%</td>
<td align="right">84,965,084</td>
<td align="right">7.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">78,871,265</td>
<td align="right">7.0%</td>
<td align="right">81,145,983</td>
<td align="right">7.1%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">103,205,504</td>
<td align="right">9.1%</td>
<td align="right">100,516,664</td>
<td align="right">8.7%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">238,585,082</td>
<td align="right">21.0%</td>
<td align="right">244,424,203</td>
<td align="right">21.3%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">31,344,721</td>
<td align="right">2.8%</td>
<td align="right">30,637,732</td>
<td align="right">2.7%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">188,926,271</td>
<td align="right">16.7%</td>
<td align="right">193,120,318</td>
<td align="right">16.8%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">31,233,202</td>
<td align="right">2.8%</td>
<td align="right">30,609,071</td>
<td align="right">2.7%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">33,621,454</td>
<td align="right">3.0%</td>
<td align="right">34,277,243</td>
<td align="right">3.0%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">31,597,052</td>
<td align="right">2.8%</td>
<td align="right">31,473,782</td>
<td align="right">2.7%</td>
<td align="right">-0.4%</td>
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
<td align="right">5,412,593,406</td>
<td align="right">81.0%</td>
<td align="right">5,412,430,305</td>
<td align="right">81.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">274,287,383</td>
<td align="right">4.1%</td>
<td align="right">274,282,079</td>
<td align="right">4.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,547,793</td>
<td align="right">1.1%</td>
<td align="right">71,547,200</td>
<td align="right">1.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">956,853,359</td>
<td align="right">14.3%</td>
<td align="right">956,847,790</td>
<td align="right">14.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">961,127,596</td>
<td align="right">14.4%</td>
<td align="right">961,122,027</td>
<td align="right">14.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,133,642,506</td>
<td align="right">76.9%</td>
<td align="right">5,133,621,872</td>
<td align="right">76.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,545,305,421</td>
<td align="right">23.1%</td>
<td align="right">1,545,299,832</td>
<td align="right">23.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,545,305,421</td>
<td align="right">23.1%</td>
<td align="right">1,545,299,832</td>
<td align="right">23.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,808,724</td>
<td align="right">0.4%</td>
<td align="right">23,808,683</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,534,148</td>
<td align="right">3.9%</td>
<td align="right">259,534,016</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,177,825</td>
<td align="right">8.7%</td>
<td align="right">584,177,805</td>
<td align="right">8.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,223,922</td>
<td align="right">0.1%</td>
<td align="right">4,223,922</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">50,315</td>
<td align="right">0.0%</td>
<td align="right">50,315</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">131,916,029</td>
<td align="right">2.0%</td>
<td align="right">131,916,029</td>
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
<td align="right">5,413,778</td>
<td align="right"></td>
<td align="right">6,404,107</td>
<td align="right"></td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">59,944,917</td>
<td align="right"></td>
<td align="right">61,924,916</td>
<td align="right"></td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,222,621,787</td>
<td align="right">1.2%</td>
<td align="right">1,185,977,126</td>
<td align="right">1.1%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,959,789,714</td>
<td align="right">3.2%</td>
<td align="right">2,872,832,507</td>
<td align="right">3.1%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">55,219,901</td>
<td align="right"></td>
<td align="right">56,212,088</td>
<td align="right"></td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">25,058,718,317</td>
<td align="right">27.4%</td>
<td align="right">24,623,037,137</td>
<td align="right">26.9%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">33,450,943,535</td>
<td align="right">31.7%</td>
<td align="right">33,014,515,724</td>
<td align="right">31.2%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">39,457,744,597</td>
<td align="right">43.1%</td>
<td align="right">39,951,791,871</td>
<td align="right">43.6%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">48,749,828,742</td>
<td align="right">46.1%</td>
<td align="right">49,245,006,513</td>
<td align="right">46.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,097,666,436</td>
<td align="right"></td>
<td align="right">2,114,130,229</td>
<td align="right"></td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,107,028,623</td>
<td align="right">26.3%</td>
<td align="right">24,183,671,277</td>
<td align="right">26.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">22,223,934,265</td>
<td align="right">21.0%</td>
<td align="right">22,266,841,844</td>
<td align="right">21.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,604,905</td>
<td align="right">0.0%</td>
<td align="right">6,611,385</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,369,279,297</td>
<td align="right"></td>
<td align="right">2,371,053,673</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,699,735</td>
<td align="right">0.4%</td>
<td align="right">71,749,782</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,110,276,873</td>
<td align="right"></td>
<td align="right">6,110,707,305</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,453,235,141</td>
<td align="right"></td>
<td align="right">13,452,687,630</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,451,523,783</td>
<td align="right">70.8%</td>
<td align="right">13,450,979,990</td>
<td align="right">70.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,473,463,657</td>
<td align="right">28.8%</td>
<td align="right">5,473,403,882</td>
<td align="right">28.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,551,768,297</td>
<td align="right">29.2%</td>
<td align="right">5,551,765,049</td>
<td align="right">29.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">177,375,775</td>
<td align="right"></td>
<td align="right">177,375,783</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,639,155</td>
<td align="right">2.1%</td>
<td align="right">3,639,155</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">336,748</td>
<td align="right">0.2%</td>
<td align="right">336,748</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,383</td>
<td align="right">0.0%</td>
<td align="right">4,383</td>
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
<td align="right">366,958</td>
<td align="right">93,688,569</td>
<td align="right">9,728,604,736</td>
<td align="right">813,026,789</td>
<td align="right">753,520,155</td>
<td align="right">366,910</td>
<td align="right">94,071,153</td>
<td align="right">9,776,332,626</td>
<td align="right">817,051,870</td>
<td align="right">755,955,848</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,934</td>
<td align="right">4,310,180</td>
<td align="right">5,666,441,612</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,934</td>
<td align="right">4,310,180</td>
<td align="right">5,666,446,592</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">601</td>
<td align="right">1.7%</td>
<td align="right">4,022</td>
<td align="right">4.2%</td>
<td align="right">569.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">929</td>
<td align="right">0.2%</td>
<td align="right">364.5%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">182</td>
<td align="right">0.0%</td>
<td align="right">843</td>
<td align="right">0.1%</td>
<td align="right">363.2%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">848</td>
<td align="right">0.2%</td>
<td align="right">2,616</td>
<td align="right">0.4%</td>
<td align="right">208.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">36,288</td>
<td align="right">8.2%</td>
<td align="right">95,730</td>
<td align="right">16.4%</td>
<td align="right">163.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">3,185</td>
<td align="right">0.7%</td>
<td align="right">5,498</td>
<td align="right">0.9%</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">133,907</td>
<td align="right">30.4%</td>
<td align="right">205,197</td>
<td align="right">35.2%</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,339</td>
<td align="right">0.3%</td>
<td align="right">2,001</td>
<td align="right">0.3%</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">440,652</td>
<td align="right"></td>
<td align="right">582,628</td>
<td align="right"></td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">223,409</td>
<td align="right">50.7%</td>
<td align="right">234,018</td>
<td align="right">40.2%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">246,170,805,405</td>
<td align="right">6,387.5%</td>
<td align="right">253,733,077,412</td>
<td align="right">6,490.2%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,853,951,237</td>
<td align="right"></td>
<td align="right">3,909,478,325</td>
<td align="right"></td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">46,848</td>
<td align="right">10.6%</td>
<td align="right">46,754</td>
<td align="right">8.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">30,661</td>
<td align="right">84.5%</td>
<td align="right">84,884</td>
<td align="right">88.7%</td>
<td align="right">176.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">36,288</td>
<td align="right"></td>
<td align="right">95,730</td>
<td align="right"></td>
<td align="right">163.8%</td>
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
<td align="right">83</td>
<td align="right">0.1%</td>
<td align="right">83 / 0 !!</td>
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
<td align="right">65,955,637</td>
<td align="right">16.0%</td>
<td align="right">184,447,030</td>
<td align="right">16.8%</td>
<td align="right">179.7%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">8,681,176</td>
<td align="right">2.1%</td>
<td align="right">23,457,344</td>
<td align="right">2.1%</td>
<td align="right">170.2%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">411,242,496</td>
<td align="right"></td>
<td align="right">1,100,816,384</td>
<td align="right"></td>
<td align="right">167.7%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">336,605,683</td>
<td align="right">81.9%</td>
<td align="right">892,912,010</td>
<td align="right">81.1%</td>
<td align="right">165.3%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">4,169,728</td>
<td align="right">1.0%</td>
<td align="right">4,681,728</td>
<td align="right">0.4%</td>
<td align="right">12.3%</td>
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
<td align="left">6,721</td>
<td align="right">21.9%</td>
<td align="left">11,018</td>
<td align="right">13.0%</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">9,538</td>
<td align="right">31.1%</td>
<td align="left">33,764</td>
<td align="right">39.8%</td>
<td align="right">254.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">8,470</td>
<td align="right">27.6%</td>
<td align="left">26,336</td>
<td align="right">31.0%</td>
<td align="right">210.9%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">4,081</td>
<td align="right">13.3%</td>
<td align="left">10,502</td>
<td align="right">12.4%</td>
<td align="right">157.3%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,691</td>
<td align="right">5.5%</td>
<td align="left">2,744</td>
<td align="right">3.2%</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">160</td>
<td align="right">0.5%</td>
<td align="left">520</td>
<td align="right">0.6%</td>
<td align="right">225.0%</td>
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
<td align="right">1,423</td>
<td align="right">3.9%</td>
<td align="right">1,782</td>
<td align="right">1.9%</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,481</td>
<td align="right">4.1%</td>
<td align="right">1,941</td>
<td align="right">2.0%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,422</td>
<td align="right">14.9%</td>
<td align="right">12,111</td>
<td align="right">12.7%</td>
<td align="right">123.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,375</td>
<td align="right">28.6%</td>
<td align="right">37,446</td>
<td align="right">39.1%</td>
<td align="right">260.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,395</td>
<td align="right">20.4%</td>
<td align="right">21,628</td>
<td align="right">22.6%</td>
<td align="right">192.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,994</td>
<td align="right">19.3%</td>
<td align="right">15,266</td>
<td align="right">15.9%</td>
<td align="right">118.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,691</td>
<td align="right">7.4%</td>
<td align="right">4,187</td>
<td align="right">4.4%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">507</td>
<td align="right">1.4%</td>
<td align="right">1,369</td>
<td align="right">1.4%</td>
<td align="right">170.0%</td>
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
<td align="right">800</td>
<td align="right">2.2%</td>
<td align="right">1,135</td>
<td align="right">1.2%</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,120</td>
<td align="right">3.1%</td>
<td align="right">1,275</td>
<td align="right">1.3%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,653</td>
<td align="right">7.3%</td>
<td align="right">3,330</td>
<td align="right">3.5%</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">10,072</td>
<td align="right">27.8%</td>
<td align="right">32,532</td>
<td align="right">34.0%</td>
<td align="right">223.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,433</td>
<td align="right">23.2%</td>
<td align="right">28,427</td>
<td align="right">29.7%</td>
<td align="right">237.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,222</td>
<td align="right">11.6%</td>
<td align="right">12,039</td>
<td align="right">12.6%</td>
<td align="right">185.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,831</td>
<td align="right">7.8%</td>
<td align="right">4,937</td>
<td align="right">5.2%</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">530</td>
<td align="right">1.5%</td>
<td align="right">1,209</td>
<td align="right">1.3%</td>
<td align="right">128.1%</td>
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
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,796</td>
<td align="right">306,978</td>
<td align="right">1,045.6%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">23,212</td>
<td align="right">212,285</td>
<td align="right">814.5%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">1,302</td>
<td align="right">6,447</td>
<td align="right">395.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">3,220,144</td>
<td align="right">15,574,651</td>
<td align="right">383.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">13,260,066</td>
<td align="right">50,615,310</td>
<td align="right">281.7%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">158,441</td>
<td align="right">510,071</td>
<td align="right">221.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">382,725</td>
<td align="right">1,193,472</td>
<td align="right">211.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,508,076</td>
<td align="right">3,587,089</td>
<td align="right">137.9%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,914,560</td>
<td align="right">11,116,220</td>
<td align="right">126.2%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">288,400</td>
<td align="right">597,309</td>
<td align="right">107.1%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">857,440</td>
<td align="right">1,512,089</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">185,682</td>
<td align="right">53,070</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">63,538</td>
<td align="right">106,030</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">91,976,259</td>
<td align="right">143,154,595</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,976,259</td>
<td align="right">143,154,595</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">92,672,199</td>
<td align="right">144,186,575</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">85,608</td>
<td align="right">118,053</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">339,011,007</td>
<td align="right">464,996,552</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,220,780</td>
<td align="right">2,107,360</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,310,575</td>
<td align="right">1,631,918</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">49,788,325</td>
<td align="right">60,222,263</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">49,788,325</td>
<td align="right">60,222,263</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">61,688,088</td>
<td align="right">73,306,613</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">69,818,132</td>
<td align="right">82,045,063</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">30,032,954</td>
<td align="right">35,186,650</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">333,680</td>
<td align="right">276,480</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,321,086</td>
<td align="right">5,039,277</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,890,144</td>
<td align="right">3,367,801</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">75,120</td>
<td align="right">64,262</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">25,999,567</td>
<td align="right">29,718,412</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">115,502,589</td>
<td align="right">130,839,137</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,001,870</td>
<td align="right">5,649,512</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">37,697,295</td>
<td align="right">42,518,037</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">148,138,116</td>
<td align="right">166,528,509</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">4,961,160</td>
<td align="right">5,572,464</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">11,571,606</td>
<td align="right">12,997,415</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">7,374,659</td>
<td align="right">8,272,240</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">106,388,800</td>
<td align="right">118,916,880</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">641,796,101</td>
<td align="right">717,350,457</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">162,702,378</td>
<td align="right">181,448,023</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">166,103,292</td>
<td align="right">184,745,389</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">6,956,010</td>
<td align="right">7,684,278</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">200,489,676</td>
<td align="right">221,368,289</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">486,650,286</td>
<td align="right">535,508,577</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">111,244,816</td>
<td align="right">122,336,744</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">198,111,777</td>
<td align="right">217,582,443</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,425,395,783</td>
<td align="right">1,563,912,620</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,425,772,334</td>
<td align="right">1,564,091,850</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,115,165</td>
<td align="right">47,295,968</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">34,957,410</td>
<td align="right">31,589,510</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">6,614,520</td>
<td align="right">7,250,500</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">142,536,503</td>
<td align="right">155,265,250</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">116,173,764</td>
<td align="right">126,546,558</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,678,400</td>
<td align="right">2,907,980</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">227,548,352</td>
<td align="right">246,673,077</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">295,017,830</td>
<td align="right">319,134,861</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">41,429,630</td>
<td align="right">44,772,337</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">278,554,136</td>
<td align="right">300,421,291</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">565,765,041</td>
<td align="right">609,816,640</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,001,422</td>
<td align="right">12,934,958</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,001,422</td>
<td align="right">12,934,958</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">45,824,616</td>
<td align="right">49,324,900</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">153,190,275</td>
<td align="right">164,669,343</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">149,494,909</td>
<td align="right">160,651,033</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,313,820</td>
<td align="right">3,549,100</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">3,922,208</td>
<td align="right">4,187,611</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,012,080</td>
<td align="right">3,210,504</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">11,508,290</td>
<td align="right">10,771,208</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">23,550,310</td>
<td align="right">25,047,728</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">23,550,310</td>
<td align="right">25,047,728</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,052,929</td>
<td align="right">6,431,547</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,822,600</td>
<td align="right">2,996,920</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,822,600</td>
<td align="right">2,996,920</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">338,666,797</td>
<td align="right">359,438,001</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">107,112,198</td>
<td align="right">113,671,558</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">36,763,718</td>
<td align="right">39,007,418</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">18,771,684</td>
<td align="right">19,903,384</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">314,923,603</td>
<td align="right">333,398,179</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">73,836,596</td>
<td align="right">78,137,165</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">73,369,959</td>
<td align="right">77,449,810</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">256,380,769</td>
<td align="right">270,101,961</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,863,459,040</td>
<td align="right">8,267,926,515</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,241,707,913</td>
<td align="right">1,305,414,866</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">296,755,796</td>
<td align="right">311,978,506</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">43,982,703</td>
<td align="right">46,179,920</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">553,034,326</td>
<td align="right">580,315,215</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">444,050,141</td>
<td align="right">465,590,132</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">541,777,961</td>
<td align="right">566,939,728</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,978,645,153</td>
<td align="right">4,162,747,395</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">252,435,301</td>
<td align="right">264,110,829</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">399,379,185</td>
<td align="right">417,763,889</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">317,001,818</td>
<td align="right">331,256,146</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">644,193,077</td>
<td align="right">672,643,962</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,953,138,076</td>
<td align="right">3,083,549,485</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">234,976,012</td>
<td align="right">245,316,477</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">34,713,627</td>
<td align="right">36,233,954</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">701,495,336</td>
<td align="right">732,108,666</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,416,888,642</td>
<td align="right">1,478,690,755</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">42,106,940</td>
<td align="right">43,941,247</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">412,052,824</td>
<td align="right">429,975,730</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,833,921,008</td>
<td align="right">3,999,730,724</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,546,104,524</td>
<td align="right">1,481,181,901</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">357,814,305</td>
<td align="right">372,583,420</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">966,635,522</td>
<td align="right">1,005,740,142</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">966,500,562</td>
<td align="right">1,005,207,351</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,249,948,372</td>
<td align="right">1,298,999,225</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,249,948,372</td>
<td align="right">1,298,999,225</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,237,946,950</td>
<td align="right">1,286,064,267</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,295,551,573</td>
<td align="right">1,344,768,601</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">29,768,070</td>
<td align="right">30,895,819</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">29,768,070</td>
<td align="right">30,895,819</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">35,341,207,748</td>
<td align="right">36,676,121,080</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">100,976,530</td>
<td align="right">104,755,078</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">144,004,730</td>
<td align="right">149,374,691</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,864,801,136</td>
<td align="right">1,933,483,292</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,065,840</td>
<td align="right">48,798,460</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">467,890,537</td>
<td align="right">484,350,682</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,172,826,339</td>
<td align="right">1,213,915,633</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">55,460,483</td>
<td align="right">57,399,418</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">452,628,380</td>
<td align="right">468,086,575</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">452,628,380</td>
<td align="right">468,086,575</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">461,592,496</td>
<td align="right">477,164,020</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,798,940,417</td>
<td align="right">1,858,737,876</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">431,668,601</td>
<td align="right">445,917,206</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">453,847,045</td>
<td align="right">468,788,312</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,794,882,981</td>
<td align="right">1,853,828,597</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">399,613,664</td>
<td align="right">412,487,263</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">808,811,386</td>
<td align="right">834,522,951</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,790,704,815</td>
<td align="right">2,878,250,697</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">40,370,578,180</td>
<td align="right">41,632,203,393</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,549,838</td>
<td align="right">121,152,598</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,450,393,988</td>
<td align="right">3,554,314,578</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,991,098,869</td>
<td align="right">7,199,375,257</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">188,493,771</td>
<td align="right">194,089,158</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,769,162,246</td>
<td align="right">3,878,336,298</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,476,152</td>
<td align="right">48,846,204</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,154,167,843</td>
<td align="right">2,215,776,149</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,075,674,646</td>
<td align="right">1,105,718,427</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,394,828</td>
<td align="right">48,704,427</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">10,961,242,711</td>
<td align="right">11,257,882,359</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,034,320</td>
<td align="right">74,944,400</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">757,567,708</td>
<td align="right">777,258,731</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">390,330,773</td>
<td align="right">400,334,346</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,205,621,742</td>
<td align="right">1,236,278,423</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,350,347,856</td>
<td align="right">1,384,653,592</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">66,306,036</td>
<td align="right">64,635,599</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,243,616,102</td>
<td align="right">2,296,209,890</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,876,523,140</td>
<td align="right">2,943,670,423</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">1,339,808,206</td>
<td align="right">1,370,632,785</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">352,930,430</td>
<td align="right">361,049,291</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,193,684</td>
<td align="right">47,255,644</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_INT</td>
<td align="right">17,372,080</td>
<td align="right">17,769,580</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">236,844,758</td>
<td align="right">242,244,494</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,016,106,830</td>
<td align="right">2,058,782,478</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">39,464,124</td>
<td align="right">40,257,209</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">180,319,232</td>
<td align="right">183,858,099</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,220,887,308</td>
<td align="right">1,244,653,358</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">168,158,180</td>
<td align="right">171,428,463</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">136,640,971</td>
<td align="right">139,070,927</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,139,612,007</td>
<td align="right">1,159,795,863</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">642,383,174</td>
<td align="right">653,541,406</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">528,091,463</td>
<td align="right">537,034,420</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">521,771,141</td>
<td align="right">530,336,835</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,348,454,898</td>
<td align="right">4,417,879,561</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">19,960,962</td>
<td align="right">20,271,157</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,818,970,615</td>
<td align="right">3,877,676,530</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">249,694,147</td>
<td align="right">253,522,175</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">2,473,111,819</td>
<td align="right">2,510,721,344</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">43,824,341</td>
<td align="right">43,165,934</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">846,845,553</td>
<td align="right">859,441,778</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">38,871,924</td>
<td align="right">39,434,238</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,853,951,237</td>
<td align="right">3,909,478,325</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">406,927,868</td>
<td align="right">412,748,663</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,110,691,604</td>
<td align="right">1,125,841,709</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,308,759,629</td>
<td align="right">6,394,393,079</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,831,083,876</td>
<td align="right">2,867,834,453</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">952,750,306</td>
<td align="right">965,092,075</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,002,700,616</td>
<td align="right">1,015,165,037</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,454,808,392</td>
<td align="right">2,484,914,754</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">971,534,463</td>
<td align="right">983,134,216</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">54,918,418</td>
<td align="right">55,541,151</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT__NO_DECREF_INPUTS</td>
<td align="right">460,952,104</td>
<td align="right">465,981,207</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">494,105,970</td>
<td align="right">499,296,970</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">39,305,461</td>
<td align="right">39,704,173</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">427,994,534</td>
<td align="right">432,312,448</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,401,747,121</td>
<td align="right">4,445,770,410</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">593,441,283</td>
<td align="right">599,330,728</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">69,571,394</td>
<td align="right">70,254,830</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">69,571,394</td>
<td align="right">70,254,830</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,342,629,585</td>
<td align="right">2,365,592,872</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">143,855,102</td>
<td align="right">145,256,935</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,167,276,662</td>
<td align="right">1,178,505,193</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">46,728,468</td>
<td align="right">47,175,287</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">966,661,248</td>
<td align="right">975,776,528</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,913,472,764</td>
<td align="right">3,946,052,572</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right">769,932,725</td>
<td align="right">776,092,403</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">138,186,716</td>
<td align="right">137,151,086</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">59,546,900</td>
<td align="right">59,985,324</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right">1,557,554,920</td>
<td align="right">1,568,275,331</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,010,421,801</td>
<td align="right">1,017,277,470</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">3,003,700</td>
<td align="right">3,023,860</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT__NO_DECREF_INPUTS</td>
<td align="right">71,532,780</td>
<td align="right">71,992,800</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">254,794,593</td>
<td align="right">256,282,799</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,341,749,232</td>
<td align="right">1,349,370,518</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">169,036,781</td>
<td align="right">169,888,957</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">911,622,888</td>
<td align="right">915,824,781</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,468,813,756</td>
<td align="right">1,475,461,434</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">36,367,438</td>
<td align="right">36,210,701</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">485,933,658</td>
<td align="right">487,991,567</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">911,622,888</td>
<td align="right">915,418,693</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,052,114,763</td>
<td align="right">1,056,493,516</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,195,783,677</td>
<td align="right">1,199,418,364</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,376,320</td>
<td align="right">111,692,279</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">440,119,735</td>
<td align="right">441,331,749</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">440,119,735</td>
<td align="right">441,331,749</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">225,785,209</td>
<td align="right">226,393,195</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">93,891,060</td>
<td align="right">94,132,980</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">735,007,110</td>
<td align="right">736,687,151</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">749,042,877</td>
<td align="right">750,577,992</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,171,220</td>
<td align="right">3,164,900</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">202,428,941</td>
<td align="right">202,041,827</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">35,266,120</td>
<td align="right">35,199,158</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">55,264,815</td>
<td align="right">55,167,995</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,294,340,277</td>
<td align="right">1,293,414,493</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">746,285,386</td>
<td align="right">746,535,024</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,997,705,814</td>
<td align="right">1,998,365,881</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">150,369,864</td>
<td align="right">150,322,894</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right"></td>
<td align="right">19,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right"></td>
<td align="right">19,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">15,876</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_UNICODE</td>
<td align="right"></td>
<td align="right">10,433</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_TYPE_1</td>
<td align="right"></td>
<td align="right">4,700</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">4,466</td>
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
<td align="right">23,356</td>
<td align="right">26,247</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,728</td>
<td align="right">1,836</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">22,981</td>
<td align="right">23,083</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right"></td>
<td align="right">21</td>
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
<td align="right">401</td>
<td align="right">708</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">401</td>
<td align="right">708</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,239</td>
<td align="right">22,239</td>
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
<td align="right">714</td>
<td align="right">714</td>
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
<td align="right">901</td>
<td align="right">901</td>
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
<td align="right">2,337</td>
<td align="right">2,337</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-01
