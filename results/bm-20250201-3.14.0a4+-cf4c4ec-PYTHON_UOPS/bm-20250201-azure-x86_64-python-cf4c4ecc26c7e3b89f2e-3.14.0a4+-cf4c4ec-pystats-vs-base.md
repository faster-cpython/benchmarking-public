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
<td align="right">5,759,789,905</td>
<td align="right">3,997,134</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,686,498</td>
<td align="right">1,194,074</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,370,333</td>
<td align="right">2,089,321</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">6,000,000</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,476,606,791</td>
<td align="right">118,735,491</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">630,577,594</td>
<td align="right">51,869,874</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,720,974,685</td>
<td align="right">260,345,587</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,756,318,075</td>
<td align="right">188,282,645</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,198,216,131</td>
<td align="right">238,424,311</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">566,122,909</td>
<td align="right">70,306,515</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,404,615,365</td>
<td align="right">178,772,588</td>
<td align="right">-87.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,780,917</td>
<td align="right">236,754</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">195,031,942</td>
<td align="right">26,363,869</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">497,366,067</td>
<td align="right">67,774,182</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,494,526,312</td>
<td align="right">480,044,924</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,146,393,893</td>
<td align="right">295,899,733</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,937,554</td>
<td align="right">58,235,959</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,247,988,121</td>
<td align="right">317,902,229</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,587,006,538</td>
<td align="right">225,222,923</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,276,199,800</td>
<td align="right">186,915,864</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,789,171</td>
<td align="right">58,634,193</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">519,112,452</td>
<td align="right">88,359,700</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,662,974,075</td>
<td align="right">292,383,825</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">701,064,341</td>
<td align="right">133,626,196</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,357,255,669</td>
<td align="right">481,802,073</td>
<td align="right">-79.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">89,951,925</td>
<td align="right">18,826,525</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,762,983</td>
<td align="right">71,710,721</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,260,966,304</td>
<td align="right">267,365,171</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">156,807,836</td>
<td align="right">33,292,776</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,318,197,310</td>
<td align="right">1,604,218,822</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,756,175,140</td>
<td align="right">636,242,971</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">669,088,245</td>
<td align="right">156,316,412</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,699,945,434</td>
<td align="right">402,085,310</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,850,357</td>
<td align="right">36,876,309</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,436,108</td>
<td align="right">251,869,800</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">379,267,078</td>
<td align="right">93,747,060</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">537,414,470</td>
<td align="right">136,209,045</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">259,913,703</td>
<td align="right">66,186,043</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,079,535,786</td>
<td align="right">275,044,190</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,038,062,295</td>
<td align="right">266,203,528</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,783,775,247</td>
<td align="right">1,491,143,773</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,417,724</td>
<td align="right">34,314,938</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">225,868,851</td>
<td align="right">61,539,947</td>
<td align="right">-72.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,560,185,132</td>
<td align="right">698,431,645</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,116,894,083</td>
<td align="right">307,152,195</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,536,919,127</td>
<td align="right">708,324,470</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,047,576,793</td>
<td align="right">3,114,533,440</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,493,521,458</td>
<td align="right">3,859,374,566</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">441,847,562</td>
<td align="right">126,555,238</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">781,571,936</td>
<td align="right">224,819,784</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,735,235,140</td>
<td align="right">3,164,603,538</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">357,331,134</td>
<td align="right">106,076,065</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">918,381,496</td>
<td align="right">272,947,402</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,620,498</td>
<td align="right">153,442,403</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,775,139</td>
<td align="right">17,826,188</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">76,086,856</td>
<td align="right">23,563,767</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,162,417</td>
<td align="right">36,614,787</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,955,606</td>
<td align="right">24,299,914</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,910,947</td>
<td align="right">11,706,004</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,022,155</td>
<td align="right">92,717,902</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,303,349</td>
<td align="right">206,464,013</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,481,380</td>
<td align="right">42,660,466</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,253,697</td>
<td align="right">21,773,878</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">520,453,922</td>
<td align="right">182,571,678</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,210,791,361</td>
<td align="right">443,273,555</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">37,487,050,585</td>
<td align="right">13,846,915,832</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,766,707</td>
<td align="right">57,661,459</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">211,102,954</td>
<td align="right">79,975,151</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">792,853,616</td>
<td align="right">302,282,205</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">93,848,896</td>
<td align="right">36,046,669</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,813</td>
<td align="right">49,176,178</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">264,381,530</td>
<td align="right">102,691,872</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,299,690</td>
<td align="right">26,873,043</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">816,719,369</td>
<td align="right">326,361,943</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,097,887,122</td>
<td align="right">852,110,511</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">813,887,045</td>
<td align="right">330,621,215</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">389,144,912</td>
<td align="right">160,180,492</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">403,677,995</td>
<td align="right">169,311,137</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">2,585,080</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">6,510,608,789</td>
<td align="right">2,759,295,689</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,561,584</td>
<td align="right">31,250,482</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">23,493,567</td>
<td align="right">10,290,971</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">320,337,894</td>
<td align="right">145,315,027</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">288,759,674</td>
<td align="right">131,387,567</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,380,040,829</td>
<td align="right">628,840,924</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">79,693,934</td>
<td align="right">36,340,903</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">57,318,891</td>
<td align="right">26,530,152</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,535,688,367</td>
<td align="right">715,093,135</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">364,111,931</td>
<td align="right">170,863,560</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">242,354,480</td>
<td align="right">114,836,835</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">332,410,096</td>
<td align="right">158,974,668</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,264,270,639</td>
<td align="right">610,692,605</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,872,791,605</td>
<td align="right">1,907,947,247</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,691</td>
<td align="right">4,866,911</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,749,561</td>
<td align="right">3,929,205</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,487,108,895</td>
<td align="right">1,265,984,454</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,852,955,840</td>
<td align="right">2,486,630,720</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,850,148</td>
<td align="right">96,482,913</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">292,955,674</td>
<td align="right">157,643,062</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">175,327,308</td>
<td align="right">94,519,385</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,637,957,069</td>
<td align="right">901,833,354</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,212,751,400</td>
<td align="right">1,790,483,038</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">168,569,480</td>
<td align="right">95,894,650</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">15,697,660</td>
<td align="right">8,983,062</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">115,828,271</td>
<td align="right">68,210,030</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,311,492,424</td>
<td align="right">3,860,219,949</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">183,157,318</td>
<td align="right">112,042,654</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,989,785</td>
<td align="right">61,666,954</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">331,405,598</td>
<td align="right">207,542,165</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">226,948,060</td>
<td align="right">142,180,831</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">852,734,644</td>
<td align="right">535,765,746</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">842,216,808</td>
<td align="right">538,583,338</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">984,978,105</td>
<td align="right">631,580,234</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,349,149,908</td>
<td align="right">2,168,466,348</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">320,799,911</td>
<td align="right">209,789,075</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">498,509,789</td>
<td align="right">328,952,903</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">94,959,296</td>
<td align="right">65,385,762</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6,998,249</td>
<td align="right">4,823,139</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">69,729,033</td>
<td align="right">48,619,886</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">503,654,486</td>
<td align="right">362,575,305</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,177,160,527</td>
<td align="right">2,291,694,033</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,115,245</td>
<td align="right">2,283,042</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,171</td>
<td align="right">139,893,028</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">569,056,647</td>
<td align="right">423,166,153</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">156,403,095</td>
<td align="right">119,379,820</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">76,988,317</td>
<td align="right">58,922,360</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,828,750</td>
<td align="right">1,439,814</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">972,652,131</td>
<td align="right">776,891,936</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">138,662,584</td>
<td align="right">111,759,715</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">99,391,853</td>
<td align="right">81,655,424</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,475,103</td>
<td align="right">212,203,978</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,428,421,435</td>
<td align="right">4,800,607,566</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">63,890,791</td>
<td align="right">56,704,419</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,660,536</td>
<td align="right">4,206,110</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">77,226,794</td>
<td align="right">69,841,615</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">73,147,932</td>
<td align="right">66,803,165</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,671,423</td>
<td align="right">8,882,506</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">348,740,387</td>
<td align="right">320,301,943</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,052,005</td>
<td align="right">8,361,350</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,798,885</td>
<td align="right">392,937,459</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">83,647,120</td>
<td align="right">79,641,339</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">73,338,948</td>
<td align="right">70,135,755</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,800,296</td>
<td align="right">3,954,636</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,360,800</td>
<td align="right">10,919,985</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,113,277,760</td>
<td align="right">1,071,996,537</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,648</td>
<td align="right">2,708</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,902,238</td>
<td align="right">13,660,550</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">170,068,018</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,418,474</td>
<td align="right">239,409,436</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,630,332,504</td>
<td align="right">1,616,275,009</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">68,026,101</td>
<td align="right">67,480,085</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">403,034</td>
<td align="right">405,555</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,713,574</td>
<td align="right">179,794,365</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">61,047,600</td>
<td align="right">60,879,473</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">101,012,059</td>
<td align="right">100,816,104</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,137</td>
<td align="right">5,129</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,722</td>
<td align="right">33,682</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,759</td>
<td align="right">120,860</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">133,122</td>
<td align="right">133,057</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,669</td>
<td align="right">773,545</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,758,190</td>
<td align="right">14,760,185</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,546,689</td>
<td align="right">20,546,039</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,877,172</td>
<td align="right">20,876,522</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,877,193</td>
<td align="right">20,876,543</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,905</td>
<td align="right">6,169,867</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,921</td>
<td align="right">1,645,920</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,899</td>
<td align="right">302,607,899</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,677</td>
<td align="right">128,851,677</td>
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
<td align="right">41,964,793</td>
<td align="right">41,964,793</td>
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
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">2,013,452,738</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">171,564,975</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">17,925,453</td>
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
<td align="right">7,641,566,589</td>
<td align="right">89.8%</td>
<td align="right">1,458,620,474</td>
<td align="right">79.3%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">813,470,254</td>
<td align="right">9.6%</td>
<td align="right">330,459,455</td>
<td align="right">18.0%</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,095,049</td>
<td align="right">0.6%</td>
<td align="right">51,010,289</td>
<td align="right">2.8%</td>
<td align="right">-3.9%</td>
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
<td align="right">408,234</td>
<td align="right">28.8%</td>
<td align="right">153,166</td>
<td align="right">13.6%</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,010,299</td>
<td align="right">71.2%</td>
<td align="right">971,019</td>
<td align="right">86.4%</td>
<td align="right">-3.9%</td>
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
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">21.0%</td>
<td align="right">17,023</td>
<td align="right">11.1%</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,517</td>
<td align="right">5.8%</td>
<td align="right">5,455</td>
<td align="right">3.6%</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">2.8%</td>
<td align="right">2,847</td>
<td align="right">1.9%</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,221</td>
<td align="right">18.2%</td>
<td align="right">18,456</td>
<td align="right">12.0%</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">2.0%</td>
<td align="right">2,343</td>
<td align="right">1.5%</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.7%</td>
<td align="right">836</td>
<td align="right">0.5%</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">4.8%</td>
<td align="right">6,572</td>
<td align="right">4.3%</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,255</td>
<td align="right">0.3%</td>
<td align="right">493</td>
<td align="right">0.3%</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">43,338</td>
<td align="right">10.6%</td>
<td align="right">17,771</td>
<td align="right">11.6%</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,796</td>
<td align="right">10.7%</td>
<td align="right">20,064</td>
<td align="right">13.1%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">399</td>
<td align="right">0.1%</td>
<td align="right">189</td>
<td align="right">0.1%</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,513</td>
<td align="right">2.1%</td>
<td align="right">4,213</td>
<td align="right">2.8%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,975</td>
<td align="right">8.3%</td>
<td align="right">19,841</td>
<td align="right">13.0%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,626</td>
<td align="right">9.0%</td>
<td align="right">23,467</td>
<td align="right">15.3%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">7,225</td>
<td align="right">1.8%</td>
<td align="right">5,718</td>
<td align="right">3.7%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,035</td>
<td align="right">0.5%</td>
<td align="right">1,995</td>
<td align="right">1.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">637</td>
<td align="right">0.2%</td>
<td align="right">625</td>
<td align="right">0.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,154</td>
<td align="right">0.8%</td>
<td align="right">3,174</td>
<td align="right">2.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">1,384</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">597</td>
<td align="right">0.1%</td>
<td align="right">597</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">83</td>
<td align="right">0.1%</td>
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
<td align="right">181,850,148</td>
<td align="right">100.0%</td>
<td align="right">96,482,913</td>
<td align="right">100.0%</td>
<td align="right">-46.9%</td>
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
<td align="right">5,504,907,105</td>
<td align="right">70.0%</td>
<td align="right">1,073,952,859</td>
<td align="right">68.8%</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,356,639,490</td>
<td align="right">30.0%</td>
<td align="right">481,643,561</td>
<td align="right">30.8%</td>
<td align="right">-79.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,928,439</td>
<td align="right">0.1%</td>
<td align="right">5,824,971</td>
<td align="right">0.4%</td>
<td align="right">-1.7%</td>
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
<td align="right">607,919</td>
<td align="right">83.5%</td>
<td align="right">149,274</td>
<td align="right">55.7%</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">119,911</td>
<td align="right">16.5%</td>
<td align="right">118,913</td>
<td align="right">44.3%</td>
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
<td align="left">list slice</td>
<td align="right">193,731</td>
<td align="right">31.9%</td>
<td align="right">7,097</td>
<td align="right">4.8%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">28,488</td>
<td align="right">4.7%</td>
<td align="right">3,672</td>
<td align="right">2.5%</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">121,418</td>
<td align="right">20.0%</td>
<td align="right">24,070</td>
<td align="right">16.1%</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">197,054</td>
<td align="right">32.4%</td>
<td align="right">59,547</td>
<td align="right">39.9%</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">47,128</td>
<td align="right">7.8%</td>
<td align="right">35,034</td>
<td align="right">23.5%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">1,012</td>
<td align="right">0.2%</td>
<td align="right">768</td>
<td align="right">0.5%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,445</td>
<td align="right">2.0%</td>
<td align="right">12,443</td>
<td align="right">8.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,609</td>
<td align="right">0.6%</td>
<td align="right">3,609</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">0.5%</td>
<td align="right">2,941</td>
<td align="right">2.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,117,027,574</td>
<td align="right">98.6%</td>
<td align="right">4,326,687,455</td>
<td align="right">97.1%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">155,057,416</td>
<td align="right">1.4%</td>
<td align="right">128,356,421</td>
<td align="right">2.9%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">230,114</td>
<td align="right">0.0%</td>
<td align="right">230,030</td>
<td align="right">0.0%</td>
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
<td align="right">3,097,146</td>
<td align="right">100.0%</td>
<td align="right">2,595,879</td>
<td align="right">100.0%</td>
<td align="right">-16.2%</td>
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
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right">287</td>
<td align="right">64.3%</td>
<td align="right">7.5%</td>
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
<td align="right">111,573</td>
<td align="right">15.8%</td>
<td align="right">111,573</td>
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
<td align="right">583,846</td>
<td align="right">82.9%</td>
<td align="right">583,846</td>
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
<td align="right">20,063</td>
<td align="right">99.4%</td>
<td align="right">20,164</td>
<td align="right">99.4%</td>
<td align="right">0.5%</td>
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
<td align="right">518,881,070</td>
<td align="right">10.3%</td>
<td align="right">88,235,797</td>
<td align="right">8.1%</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,530,283,877</td>
<td align="right">89.7%</td>
<td align="right">1,000,072,534</td>
<td align="right">91.8%</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,432,972</td>
<td align="right">0.0%</td>
<td align="right">1,286,388</td>
<td align="right">0.1%</td>
<td align="right">-10.2%</td>
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
<td align="right">213,441</td>
<td align="right">82.7%</td>
<td align="right">105,650</td>
<td align="right">71.5%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">44,654</td>
<td align="right">17.3%</td>
<td align="right">42,206</td>
<td align="right">28.5%</td>
<td align="right">-5.5%</td>
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
<td align="right">90,849</td>
<td align="right">42.6%</td>
<td align="right">4,555</td>
<td align="right">4.3%</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,821</td>
<td align="right">3.2%</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,999</td>
<td align="right">0.9%</td>
<td align="right">938</td>
<td align="right">0.9%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">11,953</td>
<td align="right">5.6%</td>
<td align="right">6,430</td>
<td align="right">6.1%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,521</td>
<td align="right">6.8%</td>
<td align="right">8,634</td>
<td align="right">8.2%</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,367</td>
<td align="right">0.6%</td>
<td align="right">1,221</td>
<td align="right">1.2%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.2%</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,774</td>
<td align="right">21.4%</td>
<td align="right">43,688</td>
<td align="right">41.4%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,004</td>
<td align="right">0.5%</td>
<td align="right">984</td>
<td align="right">0.9%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,777</td>
<td align="right">3.6%</td>
<td align="right">7,696</td>
<td align="right">7.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,381</td>
<td align="right">11.0%</td>
<td align="right">23,171</td>
<td align="right">21.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">3.6%</td>
<td align="right">7,639</td>
<td align="right">7.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,196,248,650</td>
<td align="right">93.3%</td>
<td align="right">312,920,896</td>
<td align="right">84.0%</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">155,705,394</td>
<td align="right">6.6%</td>
<td align="right">57,623,755</td>
<td align="right">15.5%</td>
<td align="right">-63.0%</td>
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
<td align="right">0.5%</td>
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
<td align="right">59,252</td>
<td align="right">60.8%</td>
<td align="right">35,443</td>
<td align="right">48.0%</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,235</td>
<td align="right">39.2%</td>
<td align="right">38,435</td>
<td align="right">52.0%</td>
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
<td align="left">str</td>
<td align="right">21,380</td>
<td align="right">36.1%</td>
<td align="right">9,166</td>
<td align="right">25.9%</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,566</td>
<td align="right">24.6%</td>
<td align="right">7,196</td>
<td align="right">20.3%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,704</td>
<td align="right">19.8%</td>
<td align="right">7,881</td>
<td align="right">22.2%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,602</td>
<td align="right">19.6%</td>
<td align="right">11,200</td>
<td align="right">31.6%</td>
<td align="right">-3.5%</td>
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
<td align="right">1,476,171,611</td>
<td align="right">29.0%</td>
<td align="right">118,633,655</td>
<td align="right">18.0%</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,444,568,577</td>
<td align="right">67.7%</td>
<td align="right">508,889,983</td>
<td align="right">77.1%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,994,098</td>
<td align="right">3.2%</td>
<td align="right">32,450,082</td>
<td align="right">4.9%</td>
<td align="right">-80.2%</td>
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
<td align="right">3,099,129</td>
<td align="right">87.8%</td>
<td align="right">617,174</td>
<td align="right">86.4%</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">430,109</td>
<td align="right">12.2%</td>
<td align="right">96,774</td>
<td align="right">13.6%</td>
<td align="right">-77.5%</td>
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
<td align="right">172,146</td>
<td align="right">40.0%</td>
<td align="right">4,495</td>
<td align="right">4.6%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,979</td>
<td align="right">19.5%</td>
<td align="right">3,015</td>
<td align="right">3.1%</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,997</td>
<td align="right">8.1%</td>
<td align="right">5,893</td>
<td align="right">6.1%</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,325</td>
<td align="right">2.6%</td>
<td align="right">2,247</td>
<td align="right">2.3%</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">734</td>
<td align="right">0.2%</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">-76.3%</td>
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
<td align="left">reversed list</td>
<td align="right">3,139</td>
<td align="right">0.7%</td>
<td align="right">945</td>
<td align="right">1.0%</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,261</td>
<td align="right">4.2%</td>
<td align="right">6,164</td>
<td align="right">6.4%</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,390</td>
<td align="right">0.8%</td>
<td align="right">1,547</td>
<td align="right">1.6%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,504</td>
<td align="right">4.5%</td>
<td align="right">10,738</td>
<td align="right">11.1%</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,601</td>
<td align="right">1.1%</td>
<td align="right">2,867</td>
<td align="right">3.0%</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,911</td>
<td align="right">1.6%</td>
<td align="right">4,546</td>
<td align="right">4.7%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">69,725</td>
<td align="right">16.2%</td>
<td align="right">53,682</td>
<td align="right">55.5%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">-23.0%</td>
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
<td align="right">12,174,414,550</td>
<td align="right">87.6%</td>
<td align="right">5,604,922,651</td>
<td align="right">82.6%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">850,888,077</td>
<td align="right">6.1%</td>
<td align="right">534,139,199</td>
<td align="right">7.9%</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">871,353,483</td>
<td align="right">6.3%</td>
<td align="right">647,066,085</td>
<td align="right">9.5%</td>
<td align="right">-25.7%</td>
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
<td align="left">Failure</td>
<td align="right">565,640</td>
<td align="right">3.3%</td>
<td align="right">355,770</td>
<td align="right">2.8%</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,521,736</td>
<td align="right">96.7%</td>
<td align="right">12,295,251</td>
<td align="right">97.2%</td>
<td align="right">-25.6%</td>
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
<td align="right">81,386</td>
<td align="right">14.4%</td>
<td align="right">41,117</td>
<td align="right">11.6%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">58,015</td>
<td align="right">10.3%</td>
<td align="right">38,479</td>
<td align="right">10.8%</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,180</td>
<td align="right">0.2%</td>
<td align="right">854</td>
<td align="right">0.2%</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,144</td>
<td align="right">1.1%</td>
<td align="right">5,030</td>
<td align="right">1.4%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,130</td>
<td align="right">1.6%</td>
<td align="right">7,935</td>
<td align="right">2.2%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,633</td>
<td align="right">2.9%</td>
<td align="right">14,537</td>
<td align="right">4.1%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,729</td>
<td align="right">0.5%</td>
<td align="right">2,403</td>
<td align="right">0.7%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,802</td>
<td align="right">0.3%</td>
<td align="right">1,608</td>
<td align="right">0.5%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">66,166</td>
<td align="right">11.7%</td>
<td align="right">60,053</td>
<td align="right">16.9%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">25,289</td>
<td align="right">4.5%</td>
<td align="right">23,852</td>
<td align="right">6.7%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,584</td>
<td align="right">0.3%</td>
<td align="right">1,582</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,088</td>
<td align="right">0.9%</td>
<td align="right">5,087</td>
<td align="right">1.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.1%</td>
<td align="right">6,405</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.2%</td>
<td align="right">1,092</td>
<td align="right">0.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,132,871,988</td>
<td align="right">99.8%</td>
<td align="right">3,659,557,562</td>
<td align="right">99.6%</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,167</td>
<td align="right">0.0%</td>
<td align="right">52,559</td>
<td align="right">0.0%</td>
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
<td align="right">14,622,687</td>
<td align="right">0.2%</td>
<td align="right">14,622,654</td>
<td align="right">0.4%</td>
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
<td align="right">136,272</td>
<td align="right">100.0%</td>
<td align="right">138,300</td>
<td align="right">100.0%</td>
<td align="right">1.5%</td>
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
<td align="right">64,162,845</td>
<td align="right">100.0%</td>
<td align="right">63,162,515</td>
<td align="right">100.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">593,288,638</td>
<td align="right">82.2%</td>
<td align="right">206,449,302</td>
<td align="right">61.6%</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,816,906</td>
<td align="right">17.8%</td>
<td align="right">128,816,906</td>
<td align="right">38.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,850,005,428</td>
<td align="right">90.5%</td>
<td align="right">1,301,541,527</td>
<td align="right">87.5%</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">77,133,458</td>
<td align="right">3.8%</td>
<td align="right">69,748,491</td>
<td align="right">4.7%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">116,601,649</td>
<td align="right">5.7%</td>
<td align="right">115,907,484</td>
<td align="right">7.8%</td>
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
<td align="right">52,760</td>
<td align="right">2.3%</td>
<td align="right">50,969</td>
<td align="right">2.2%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,239,840</td>
<td align="right">97.7%</td>
<td align="right">2,228,341</td>
<td align="right">97.8%</td>
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
<td align="left">other</td>
<td align="right">272,068</td>
<td align="right">515.7%</td>
<td align="right">135,543</td>
<td align="right">265.9%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">6,033</td>
<td align="right">11.4%</td>
<td align="right">4,954</td>
<td align="right">9.7%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">699</td>
<td align="right">1.4%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,322</td>
<td align="right">10.1%</td>
<td align="right">5,098</td>
<td align="right">10.0%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">1,619</td>
<td align="right">3.2%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">46.4%</td>
<td align="right">24,076</td>
<td align="right">47.2%</td>
<td align="right">-1.6%</td>
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
<td align="left">not managed dict</td>
<td align="right">3,346</td>
<td align="right">6.3%</td>
<td align="right">3,348</td>
<td align="right">6.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.5%</td>
<td align="right">7,666</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">810</td>
<td align="right">1.5%</td>
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
<td align="right">112,686,498</td>
<td align="right">100.0%</td>
<td align="right">1,194,074</td>
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
<td align="right">700,880,003</td>
<td align="right">43.1%</td>
<td align="right">133,580,260</td>
<td align="right">43.1%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">923,451,823</td>
<td align="right">56.8%</td>
<td align="right">176,380,360</td>
<td align="right">56.9%</td>
<td align="right">-80.9%</td>
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
<td align="right">182,300</td>
<td align="right">98.9%</td>
<td align="right">43,779</td>
<td align="right">95.2%</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,078</td>
<td align="right">1.1%</td>
<td align="right">2,197</td>
<td align="right">4.8%</td>
<td align="right">5.7%</td>
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
<td align="right">0.8%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,309</td>
<td align="right">2.9%</td>
<td align="right">236</td>
<td align="right">0.5%</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.8%</td>
<td align="right">8,142</td>
<td align="right">18.6%</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">0.9%</td>
<td align="right">501</td>
<td align="right">1.1%</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,343</td>
<td align="right">10.6%</td>
<td align="right">14,756</td>
<td align="right">33.7%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">9.5%</td>
<td align="right">16,703</td>
<td align="right">38.2%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,032</td>
<td align="right">1.7%</td>
<td align="right">3,032</td>
<td align="right">6.9%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">112,464,528</td>
<td align="right">2.2%</td>
<td align="right">40,958,194</td>
<td align="right">1.6%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">263,700,382</td>
<td align="right">5.2%</td>
<td align="right">102,228,575</td>
<td align="right">4.1%</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,742,074,209</td>
<td align="right">92.6%</td>
<td align="right">2,349,732,477</td>
<td align="right">94.2%</td>
<td align="right">-50.4%</td>
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
<td align="right">2,169,920</td>
<td align="right">77.5%</td>
<td align="right">821,437</td>
<td align="right">66.5%</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">631,650</td>
<td align="right">22.5%</td>
<td align="right">413,171</td>
<td align="right">33.5%</td>
<td align="right">-34.6%</td>
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
<td align="right">77,658</td>
<td align="right">12.3%</td>
<td align="right">8,635</td>
<td align="right">2.1%</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">132,980</td>
<td align="right">21.1%</td>
<td align="right">16,387</td>
<td align="right">4.0%</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,878</td>
<td align="right">3.0%</td>
<td align="right">4,597</td>
<td align="right">1.1%</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">10,053</td>
<td align="right">1.6%</td>
<td align="right">5,538</td>
<td align="right">1.3%</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">20,552</td>
<td align="right">3.3%</td>
<td align="right">13,480</td>
<td align="right">3.3%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,323</td>
<td align="right">2.1%</td>
<td align="right">12,363</td>
<td align="right">3.0%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">97,682</td>
<td align="right">15.5%</td>
<td align="right">94,094</td>
<td align="right">22.8%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,638</td>
<td align="right">40.9%</td>
<td align="right">256,191</td>
<td align="right">62.0%</td>
<td align="right">-0.9%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,247,616,564</td>
<td align="right">99.9%</td>
<td align="right">396,216,542</td>
<td align="right">99.6%</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,816,321</td>
<td align="right">0.1%</td>
<td align="right">1,427,430</td>
<td align="right">0.4%</td>
<td align="right">-21.4%</td>
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
<td align="right">988</td>
<td align="right">7.9%</td>
<td align="right">863</td>
<td align="right">6.9%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,521</td>
<td align="right">92.1%</td>
<td align="right">11,601</td>
<td align="right">93.1%</td>
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
<td align="left">sequence</td>
<td align="right">761</td>
<td align="right">77.0%</td>
<td align="right">636</td>
<td align="right">73.7%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">13.8%</td>
<td align="right">136</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">9.2%</td>
<td align="right">91</td>
<td align="right">10.5%</td>
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
<td align="right">7,658,537,677</td>
<td align="right">3.6%</td>
<td align="right">2,162,363,153</td>
<td align="right">2.7%</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">86,725,287,330</td>
<td align="right">41.1%</td>
<td align="right">30,239,815,005</td>
<td align="right">37.7%</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">115,388,009,820</td>
<td align="right">54.6%</td>
<td align="right">46,727,057,892</td>
<td align="right">58.3%</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,482,627,818</td>
<td align="right">0.7%</td>
<td align="right">1,025,590,988</td>
<td align="right">1.3%</td>
<td align="right">-30.8%</td>
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
<td align="right">1,476,171,611</td>
<td align="right">19.3%</td>
<td align="right">118,633,655</td>
<td align="right">5.5%</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">518,881,070</td>
<td align="right">6.8%</td>
<td align="right">88,235,797</td>
<td align="right">4.1%</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,880,003</td>
<td align="right">9.2%</td>
<td align="right">133,580,260</td>
<td align="right">6.2%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,356,639,490</td>
<td align="right">30.8%</td>
<td align="right">481,643,561</td>
<td align="right">22.3%</td>
<td align="right">-79.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">263,700,382</td>
<td align="right">3.4%</td>
<td align="right">102,228,575</td>
<td align="right">4.7%</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">813,470,254</td>
<td align="right">10.6%</td>
<td align="right">330,459,455</td>
<td align="right">15.3%</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,850,148</td>
<td align="right">2.4%</td>
<td align="right">96,482,913</td>
<td align="right">4.5%</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">850,888,077</td>
<td align="right">11.1%</td>
<td align="right">534,139,199</td>
<td align="right">24.7%</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,705,394</td>
<td align="right">2.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,906</td>
<td align="right">1.7%</td>
<td align="right">128,816,906</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">69,748,491</td>
<td align="right">3.2%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">368,081,973</td>
<td align="right">24.8%</td>
<td align="right">255,269,563</td>
<td align="right">24.9%</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">266,997,716</td>
<td align="right">18.0%</td>
<td align="right">188,324,541</td>
<td align="right">18.4%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">90,679,818</td>
<td align="right">6.1%</td>
<td align="right">75,714,566</td>
<td align="right">7.4%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">82,382,239</td>
<td align="right">5.6%</td>
<td align="right">69,071,946</td>
<td align="right">6.7%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">86,869,082</td>
<td align="right">5.9%</td>
<td align="right">74,460,459</td>
<td align="right">7.3%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,279,957</td>
<td align="right">6.4%</td>
<td align="right">94,274,265</td>
<td align="right">9.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,019,741</td>
<td align="right">5.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,896,097</td>
<td align="right">5.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">55,296,348</td>
<td align="right">3.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,780,810</td>
<td align="right">3.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">24,421,702</td>
<td align="right">2.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21,597,684</td>
<td align="right">2.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21,238,328</td>
<td align="right">2.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20,872,852</td>
<td align="right">2.0%</td>
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
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">2,128,247</td>
<td align="right">0.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,122,803,017</td>
<td align="right">75.8%</td>
<td align="right">5,017,309,709</td>
<td align="right">75.6%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,485,532,905</td>
<td align="right">81.2%</td>
<td align="right">5,404,451,314</td>
<td align="right">81.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">678,890,256</td>
<td align="right">10.0%</td>
<td align="right">670,613,087</td>
<td align="right">10.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,634,825,909</td>
<td align="right">24.2%</td>
<td align="right">1,620,922,748</td>
<td align="right">24.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,634,825,909</td>
<td align="right">24.2%</td>
<td align="right">1,620,922,748</td>
<td align="right">24.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">955,935,653</td>
<td align="right">14.1%</td>
<td align="right">950,309,661</td>
<td align="right">14.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,453,106</td>
<td align="right">4.1%</td>
<td align="right">278,109,363</td>
<td align="right">4.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,327,052</td>
<td align="right">1.1%</td>
<td align="right">71,632,691</td>
<td align="right">1.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">951,658,315</td>
<td align="right">14.1%</td>
<td align="right">948,177,518</td>
<td align="right">14.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,414,681</td>
<td align="right">3.9%</td>
<td align="right">261,407,014</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,717</td>
<td align="right">0.4%</td>
<td align="right">24,922,181</td>
<td align="right">0.4%</td>
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
<td align="left">Method cache misses</td>
<td align="right">64,705,762</td>
<td align="right"></td>
<td align="right">59,342,992</td>
<td align="right"></td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">27,496,851,000</td>
<td align="right">17.8%</td>
<td align="right">25,440,988,563</td>
<td align="right">16.1%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">79,640,773,165</td>
<td align="right">51.5%</td>
<td align="right">85,592,358,396</td>
<td align="right">54.2%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">71,238,249</td>
<td align="right"></td>
<td align="right">66,076,992</td>
<td align="right"></td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">89,051,196,598</td>
<td align="right">46.5%</td>
<td align="right">94,502,100,346</td>
<td align="right">47.6%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,288,532,955</td>
<td align="right"></td>
<td align="right">2,173,549,378</td>
<td align="right"></td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">45,511,950,648</td>
<td align="right">23.8%</td>
<td align="right">47,292,505,680</td>
<td align="right">23.8%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,339,551</td>
<td align="right"></td>
<td align="right">7,541,037</td>
<td align="right"></td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,502,047</td>
<td align="right"></td>
<td align="right">174,900,363</td>
<td align="right"></td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,439,129,634</td>
<td align="right"></td>
<td align="right">12,265,722,296</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,438,997,867</td>
<td align="right">67.1%</td>
<td align="right">12,265,624,424</td>
<td align="right">66.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">25,402,079,502</td>
<td align="right">16.4%</td>
<td align="right">25,072,772,020</td>
<td align="right">15.9%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">21,979,807,381</td>
<td align="right">14.2%</td>
<td align="right">21,698,222,308</td>
<td align="right">13.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">23,841,929,624</td>
<td align="right">12.5%</td>
<td align="right">23,633,393,031</td>
<td align="right">11.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,028,545,390</td>
<td align="right">32.5%</td>
<td align="right">5,990,887,885</td>
<td align="right">32.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,106,542,625</td>
<td align="right">32.9%</td>
<td align="right">6,068,824,542</td>
<td align="right">33.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,700,541,627</td>
<td align="right"></td>
<td align="right">6,660,382,623</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,906,496,893</td>
<td align="right"></td>
<td align="right">2,897,300,243</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,576,074</td>
<td align="right">0.4%</td>
<td align="right">71,516,936</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,421,161</td>
<td align="right">0.0%</td>
<td align="right">6,419,721</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">33,078,071,573</td>
<td align="right">17.3%</td>
<td align="right">33,071,040,708</td>
<td align="right">16.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,171</td>
<td align="right">2.5%</td>
<td align="right">4,444,171</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">476,016</td>
<td align="right">0.3%</td>
<td align="right">476,016</td>
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
<td align="right">365,610</td>
<td align="right">103,645,126</td>
<td align="right">9,516,180,584</td>
<td align="right">745,611,402</td>
<td align="right">766,748,625</td>
<td align="right">364,686</td>
<td align="right">103,276,582</td>
<td align="right">9,562,392,903</td>
<td align="right">756,975,749</td>
<td align="right">765,555,721</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,607,147,860</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,607,430,290</td>
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
<td align="right">160</td>
<td align="right">160 / 0 !!</td>
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
<td align="right">160</td>
<td align="right">160 / 0 !!</td>
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
Stats gathered on: 2025-02-03
