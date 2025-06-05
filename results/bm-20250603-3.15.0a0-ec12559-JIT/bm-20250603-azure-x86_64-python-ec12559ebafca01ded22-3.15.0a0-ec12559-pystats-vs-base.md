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
<td align="right">5,792,290,346</td>
<td align="right">5,088,983</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,724,902</td>
<td align="right">1,085,654</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">459,026,589</td>
<td align="right">9,526,077</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,358,411</td>
<td align="right">2,220,717</td>
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
<td align="right">1,504,781,592</td>
<td align="right">194,797,972</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,403,492,104</td>
<td align="right">188,284,536</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,585,080,785</td>
<td align="right">218,564,748</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,789,270</td>
<td align="right">101,301,869</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,275,545,277</td>
<td align="right">185,659,358</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,718,940,597</td>
<td align="right">421,202,765</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,754,455,779</td>
<td align="right">274,807,691</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">401,288,920</td>
<td align="right">66,073,048</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">565,955,097</td>
<td align="right">94,060,632</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,124,277,335</td>
<td align="right">356,426,891</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,482,959,993</td>
<td align="right">595,898,977</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,265,420,485</td>
<td align="right">390,231,475</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,708,264</td>
<td align="right">90,753,038</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">88,979,172</td>
<td align="right">17,338,546</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,809,448</td>
<td align="right">31,247,012</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,128,392</td>
<td align="right">23,287,428</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">861,438,992</td>
<td align="right">178,363,051</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,252,080,277</td>
<td align="right">262,658,624</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">671,962,242</td>
<td align="right">144,170,271</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,277,797</td>
<td align="right">76,372,528</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,694,557</td>
<td align="right">29,292,593</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">187,992,695</td>
<td align="right">45,873,040</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,367,628</td>
<td align="right">15,294,980</td>
<td align="right">-75.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">940,067,628</td>
<td align="right">235,728,207</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">377,689,616</td>
<td align="right">95,704,446</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,657,280,823</td>
<td align="right">423,108,023</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,284,135,074</td>
<td align="right">1,918,629,630</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">626,940,750</td>
<td align="right">166,231,578</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">690,694,457</td>
<td align="right">192,696,447</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,434,178,348</td>
<td align="right">969,617,669</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,140,429,387</td>
<td align="right">609,286,570</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">253,092,663</td>
<td align="right">72,668,158</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">56,905,342</td>
<td align="right">16,453,633</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,436,387</td>
<td align="right">145,970,793</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,531,635,765</td>
<td align="right">738,246,043</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">535,153,865</td>
<td align="right">156,697,515</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,105,599,705</td>
<td align="right">631,019,711</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,243,767,727</td>
<td align="right">373,448,931</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,548,348</td>
<td align="right">113,697,645</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,733,496,764</td>
<td align="right">843,966,906</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,490,014,443</td>
<td align="right">790,201,552</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,839,637,630</td>
<td align="right">1,856,965,955</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,389,533,973</td>
<td align="right">4,391,055,271</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,731,800</td>
<td align="right">179,132,344</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">352,582,563</td>
<td align="right">117,947,567</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,112,240,980</td>
<td align="right">3,391,876,974</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,387,231</td>
<td align="right">53,803,093</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,040,118,911</td>
<td align="right">365,666,026</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,673,431,741</td>
<td align="right">3,754,700,864</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">77,896,786</td>
<td align="right">27,758,031</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,842,507</td>
<td align="right">2,927,410</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">99,731,891</td>
<td align="right">37,821,610</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,358,101</td>
<td align="right">25,720,606</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">22,616,468</td>
<td align="right">8,709,222</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,214,828,650</td>
<td align="right">473,111,400</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,786,196</td>
<td align="right">29,206,991</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">261,982,858</td>
<td align="right">102,479,868</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">433,502,937</td>
<td align="right">174,505,698</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,531,791,931</td>
<td align="right">3,588,579,091</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">2,597,140</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,344,982,912</td>
<td align="right">996,341,662</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">795,412,021</td>
<td align="right">340,879,134</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">33,493,720,703</td>
<td align="right">14,753,420,857</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">780,741,548</td>
<td align="right">345,774,546</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,366,470</td>
<td align="right">468,453,321</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,095,842,060</td>
<td align="right">492,461,689</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">72,974,803</td>
<td align="right">33,352,122</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,056,564,420</td>
<td align="right">484,814,569</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,888,497,643</td>
<td align="right">1,835,640,723</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,537,428,511</td>
<td align="right">730,576,776</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,022,150</td>
<td align="right">128,955,515</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,301,987</td>
<td align="right">62,683,281</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">90,429,827</td>
<td align="right">44,273,374</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,972,368</td>
<td align="right">75,466,161</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">536,645,346</td>
<td align="right">266,110,775</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">233,988</td>
<td align="right">117,444</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">256,568,790</td>
<td align="right">128,832,545</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">355,896,754</td>
<td align="right">184,300,360</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,461,960</td>
<td align="right">51,179,959</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">316,781,849</td>
<td align="right">165,127,484</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">283,087,209</td>
<td align="right">153,572,119</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">201,394,706</td>
<td align="right">109,288,589</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,420,230,386</td>
<td align="right">1,328,837,216</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,542,377,660</td>
<td align="right">867,708,213</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">290,125,076</td>
<td align="right">164,409,112</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">355,505,727</td>
<td align="right">201,844,434</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">774,022,838</td>
<td align="right">441,858,251</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">59,159,110</td>
<td align="right">33,895,786</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">116,413,056</td>
<td align="right">66,838,630</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">133,548,492</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,165,029,010</td>
<td align="right">1,840,100,794</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,343,237</td>
<td align="right">4,318,877</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,358,302,635</td>
<td align="right">820,663,708</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">801,892,129</td>
<td align="right">486,985,984</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,157</td>
<td align="right">114,765,149</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">190,497,940</td>
<td align="right">118,262,962</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,750,039,013</td>
<td align="right">2,952,594,198</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,297,036</td>
<td align="right">109,033,113</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,796</td>
<td align="right">5,694,716</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">66,634,029</td>
<td align="right">42,922,434</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">233,829,357</td>
<td align="right">152,808,635</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">164,037,159</td>
<td align="right">108,882,899</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">75,634,656</td>
<td align="right">50,626,776</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">485,180,137</td>
<td align="right">325,114,963</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,569,770</td>
<td align="right">164,876,606</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,519,607</td>
<td align="right">163,530,809</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,383,160,323</td>
<td align="right">2,300,322,341</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">385,210,926</td>
<td align="right">265,241,937</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">840,951,315</td>
<td align="right">603,572,088</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,215,710,938</td>
<td align="right">2,338,221,801</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">325,947,572</td>
<td align="right">238,888,224</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">72,576,735</td>
<td align="right">53,588,336</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">678,225,478</td>
<td align="right">501,853,392</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,359,269,324</td>
<td align="right">3,973,919,364</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,241,180,612</td>
<td align="right">4,644,824,736</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,784,319</td>
<td align="right">2,838,519</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">468,052,852</td>
<td align="right">355,298,381</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,657,112</td>
<td align="right">1,262,318</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">66,481,380</td>
<td align="right">51,553,675</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">943,019,316</td>
<td align="right">733,580,359</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,122,133</td>
<td align="right">2,489,180</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,170,392</td>
<td align="right">17,048,216</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,170,412</td>
<td align="right">17,048,237</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,843,639</td>
<td align="right">16,890,844</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">267,758,754</td>
<td align="right">218,471,328</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">80,979,199</td>
<td align="right">66,238,756</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">346,700,225</td>
<td align="right">286,870,756</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">975,005,002</td>
<td align="right">807,421,451</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">68,559,460</td>
<td align="right">57,622,483</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,342,870</td>
<td align="right">350,475,924</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">115,332,004</td>
<td align="right">98,073,877</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,165,339</td>
<td align="right">5,280,849</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,521,147</td>
<td align="right">62,495,537</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">76,781</td>
<td align="right">69,551</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">61,064,648</td>
<td align="right">55,539,643</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">75,215,922</td>
<td align="right">68,447,731</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">147,898,730</td>
<td align="right">134,647,237</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,356</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,587,182,136</td>
<td align="right">1,464,870,884</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,098,361</td>
<td align="right">9,389,629</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">335,050,558</td>
<td align="right">312,967,255</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,709</td>
<td align="right">31,518</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,431,139</td>
<td align="right">5,119,330</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">14,816</td>
<td align="right">13,984</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,096,997</td>
<td align="right">148,375,156</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">463,922</td>
<td align="right">441,429</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,549</td>
<td align="right">3,389</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,096,847</td>
<td align="right">9,680,248</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,704,287</td>
<td align="right">12,201,283</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,801</td>
<td align="right">123,753,240</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">72,271,413</td>
<td align="right">70,260,886</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,502,341</td>
<td align="right">185,228,193</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,632</td>
<td align="right">12,971</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,514</td>
<td align="right">2,573</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">65,686,114</td>
<td align="right">64,212,077</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,581,400</td>
<td align="right">27,958,437</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,090,893</td>
<td align="right">3,024,264</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">243,269</td>
<td align="right">247,781</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,750,966</td>
<td align="right">1,721,846</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,961,125</td>
<td align="right">35,549,117</td>
<td align="right">-1.1%</td>
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
<td align="right">214,342</td>
<td align="right">212,919</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,112,235,782</td>
<td align="right">1,105,493,305</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,966,355</td>
<td align="right">418,159,711</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,544,206</td>
<td align="right">591,619,558</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,658,173</td>
<td align="right">302,246,141</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,364</td>
<td align="right">5,358</td>
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
<td align="right">14,756,398</td>
<td align="right">14,759,813</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,628</td>
<td align="right">9,742,428</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,443</td>
<td align="right">41,965,283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">10,549,268</td>
<td align="right">10,549,266</td>
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
<td align="right">972,556,128</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">741,367,888</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,344,052,575</td>
<td align="right">12.6%</td>
<td align="right">995,920,750</td>
<td align="right">5.9%</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">62,403,816</td>
<td align="right">0.3%</td>
<td align="right">52,186,238</td>
<td align="right">0.3%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,240,082,909</td>
<td align="right">87.1%</td>
<td align="right">15,947,262,774</td>
<td align="right">93.8%</td>
<td align="right">-1.8%</td>
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
<td align="right">913,033</td>
<td align="right">43.3%</td>
<td align="right">402,636</td>
<td align="right">28.7%</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,194,479</td>
<td align="right">56.7%</td>
<td align="right">1,002,657</td>
<td align="right">71.3%</td>
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
<td align="right">0.4%</td>
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
<td align="right">25,838</td>
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
<td align="right">74,204</td>
<td align="right">8.1%</td>
<td align="right">18,454</td>
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
<td align="right">1,097</td>
<td align="right">0.1%</td>
<td align="right">335</td>
<td align="right">0.1%</td>
<td align="right">-69.5%</td>
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
<td align="right">23,512</td>
<td align="right">2.6%</td>
<td align="right">8,298</td>
<td align="right">2.1%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">42,915</td>
<td align="right">4.7%</td>
<td align="right">17,713</td>
<td align="right">4.4%</td>
<td align="right">-58.7%</td>
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
<td align="right">20,816</td>
<td align="right">5.2%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,974</td>
<td align="right">3.7%</td>
<td align="right">19,832</td>
<td align="right">4.9%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">35,908</td>
<td align="right">3.9%</td>
<td align="right">21,007</td>
<td align="right">5.2%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,449</td>
<td align="right">2.1%</td>
<td align="right">11,552</td>
<td align="right">2.9%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">107,942</td>
<td align="right">11.8%</td>
<td align="right">72,761</td>
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
<td align="right">78,846</td>
<td align="right">8.6%</td>
<td align="right">62,999</td>
<td align="right">15.6%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">46,925</td>
<td align="right">5.1%</td>
<td align="right">37,617</td>
<td align="right">9.3%</td>
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
<td align="right">3,165</td>
<td align="right">0.3%</td>
<td align="right">2,937</td>
<td align="right">0.7%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,127</td>
<td align="right">0.8%</td>
<td align="right">6,830</td>
<td align="right">1.7%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,036</td>
<td align="right">0.2%</td>
<td align="right">1,996</td>
<td align="right">0.5%</td>
<td align="right">-2.0%</td>
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
<td align="left">subtract different types</td>
<td align="right">633</td>
<td align="right">0.1%</td>
<td align="right">627</td>
<td align="right">0.2%</td>
<td align="right">-0.9%</td>
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
<td align="left">subscr deque</td>
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
<td align="right">179,132,344</td>
<td align="right">100.0%</td>
<td align="right">-67.2%</td>
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
<td align="right">11,105,631,153</td>
<td align="right">98.4%</td>
<td align="right">8,603,286,348</td>
<td align="right">98.4%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">182,035,862</td>
<td align="right">1.6%</td>
<td align="right">143,173,832</td>
<td align="right">1.6%</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">178,675,483</td>
<td align="right">1.6%</td>
<td align="right">140,547,040</td>
<td align="right">1.6%</td>
<td align="right">-21.3%</td>
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
<td align="right">3,603,502</td>
<td align="right">100.0%</td>
<td align="right">2,874,427</td>
<td align="right">100.0%</td>
<td align="right">-20.2%</td>
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
<td align="left">init not simple</td>
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">267</td>
<td align="right">182.9%</td>
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
<td align="right">19,970</td>
<td align="right">100.0%</td>
<td align="right">20,311</td>
<td align="right">100.0%</td>
<td align="right">1.7%</td>
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
<td align="right">510,483,012</td>
<td align="right">10.2%</td>
<td align="right">90,641,876</td>
<td align="right">2.0%</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,270,942</td>
<td align="right">0.0%</td>
<td align="right">1,011,609</td>
<td align="right">0.0%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,505,841,764</td>
<td align="right">89.8%</td>
<td align="right">4,404,393,437</td>
<td align="right">98.0%</td>
<td align="right">-2.3%</td>
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
<td align="right">207,515</td>
<td align="right">83.4%</td>
<td align="right">93,010</td>
<td align="right">71.5%</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,406</td>
<td align="right">16.6%</td>
<td align="right">37,026</td>
<td align="right">28.5%</td>
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
<td align="right">90,413</td>
<td align="right">43.6%</td>
<td align="right">4,060</td>
<td align="right">4.4%</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,830</td>
<td align="right">3.3%</td>
<td align="right">369</td>
<td align="right">0.4%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">10,443</td>
<td align="right">5.0%</td>
<td align="right">5,851</td>
<td align="right">6.3%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,434</td>
<td align="right">21.9%</td>
<td align="right">31,657</td>
<td align="right">34.0%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">11,307</td>
<td align="right">5.4%</td>
<td align="right">8,649</td>
<td align="right">9.3%</td>
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
<td align="left">bool</td>
<td align="right">1,903</td>
<td align="right">0.9%</td>
<td align="right">1,874</td>
<td align="right">2.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,784</td>
<td align="right">3.8%</td>
<td align="right">7,680</td>
<td align="right">8.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,279</td>
<td align="right">11.2%</td>
<td align="right">22,993</td>
<td align="right">24.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,649</td>
<td align="right">3.7%</td>
<td align="right">7,648</td>
<td align="right">8.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">153,912,156</td>
<td align="right">6.6%</td>
<td align="right">75,425,571</td>
<td align="right">3.9%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,186,555,129</td>
<td align="right">93.4%</td>
<td align="right">1,840,982,698</td>
<td align="right">96.0%</td>
<td align="right">-15.8%</td>
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
<td align="right">1,389,959</td>
<td align="right">0.1%</td>
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
<td align="right">58,102</td>
<td align="right">67.0%</td>
<td align="right">38,280</td>
<td align="right">57.3%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,589</td>
<td align="right">33.0%</td>
<td align="right">28,533</td>
<td align="right">42.7%</td>
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
<td align="left">str</td>
<td align="right">21,455</td>
<td align="right">36.9%</td>
<td align="right">7,772</td>
<td align="right">20.3%</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,604</td>
<td align="right">25.1%</td>
<td align="right">11,267</td>
<td align="right">29.4%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,025</td>
<td align="right">19.0%</td>
<td align="right">9,056</td>
<td align="right">23.7%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,018</td>
<td align="right">19.0%</td>
<td align="right">10,185</td>
<td align="right">26.6%</td>
<td align="right">-7.6%</td>
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
<td align="right">1,504,340,631</td>
<td align="right">29.3%</td>
<td align="right">194,687,283</td>
<td align="right">13.5%</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,987,657</td>
<td align="right">3.2%</td>
<td align="right">44,179,168</td>
<td align="right">3.1%</td>
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
<td align="right">3,473,586,903</td>
<td align="right">67.5%</td>
<td align="right">1,201,003,750</td>
<td align="right">83.4%</td>
<td align="right">-65.4%</td>
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
<td align="right">435,561</td>
<td align="right">12.3%</td>
<td align="right">105,298</td>
<td align="right">11.2%</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,099,324</td>
<td align="right">87.7%</td>
<td align="right">838,821</td>
<td align="right">88.8%</td>
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
<td align="right">4,166</td>
<td align="right">4.0%</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,676</td>
<td align="right">19.2%</td>
<td align="right">10,887</td>
<td align="right">10.3%</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,701</td>
<td align="right">8.0%</td>
<td align="right">5,501</td>
<td align="right">5.2%</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,283</td>
<td align="right">4.2%</td>
<td align="right">3,139</td>
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
<td align="right">956</td>
<td align="right">0.9%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,537</td>
<td align="right">2.4%</td>
<td align="right">3,497</td>
<td align="right">3.3%</td>
<td align="right">-66.8%</td>
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
<td align="left">other</td>
<td align="right">10,543</td>
<td align="right">2.4%</td>
<td align="right">4,047</td>
<td align="right">3.8%</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">533</td>
<td align="right">0.1%</td>
<td align="right">232</td>
<td align="right">0.2%</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,114</td>
<td align="right">0.7%</td>
<td align="right">1,618</td>
<td align="right">1.5%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,068</td>
<td align="right">4.1%</td>
<td align="right">12,731</td>
<td align="right">12.1%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">69,493</td>
<td align="right">16.0%</td>
<td align="right">49,707</td>
<td align="right">47.2%</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,083</td>
<td align="right">1.4%</td>
<td align="right">4,759</td>
<td align="right">4.5%</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,284</td>
<td align="right">1.0%</td>
<td align="right">3,490</td>
<td align="right">3.3%</td>
<td align="right">-18.5%</td>
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
<td align="left">tuple</td>
<td align="right">171,931,314</td>
<td align="right">171,931,314 / 0 !!</td>
<td align="right">120,684,899</td>
<td align="right">120,684,899 / 0 !!</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,509,021</td>
<td align="right">5,509,021 / 0 !!</td>
<td align="right">4,045,632</td>
<td align="right">4,045,632 / 0 !!</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">304,488,821</td>
<td align="right">304,488,821 / 0 !!</td>
<td align="right">247,559,320</td>
<td align="right">247,559,320 / 0 !!</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,924,764</td>
<td align="right">101,924,764 / 0 !!</td>
<td align="right">85,267,026</td>
<td align="right">85,267,026 / 0 !!</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">119,408,594</td>
<td align="right">119,408,594 / 0 !!</td>
<td align="right">111,955,996</td>
<td align="right">111,955,996 / 0 !!</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,710,702</td>
<td align="right">2,710,702 / 0 !!</td>
<td align="right">2,604,954</td>
<td align="right">2,604,954 / 0 !!</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,149,540</td>
<td align="right">12,149,540 / 0 !!</td>
<td align="right">12,046,246</td>
<td align="right">12,046,246 / 0 !!</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,933,003</td>
<td align="right">34,933,003 / 0 !!</td>
<td align="right">34,651,422</td>
<td align="right">34,651,422 / 0 !!</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,959,170</td>
<td align="right">341,959,170 / 0 !!</td>
<td align="right">341,556,271</td>
<td align="right">341,556,271 / 0 !!</td>
<td align="right">-0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">860,613,466</td>
<td align="right">6.3%</td>
<td align="right">491,507,925</td>
<td align="right">4.7%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">800,119,152</td>
<td align="right">5.9%</td>
<td align="right">485,589,102</td>
<td align="right">4.6%</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,985,585,586</td>
<td align="right">87.8%</td>
<td align="right">9,512,360,600</td>
<td align="right">90.7%</td>
<td align="right">-20.6%</td>
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
<td align="right">1,262,383</td>
<td align="right">0.0%</td>
<td align="right">-12.3%</td>
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
<td align="right">16,316,665</td>
<td align="right">97.0%</td>
<td align="right">9,388,485</td>
<td align="right">95.7%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">505,667</td>
<td align="right">3.0%</td>
<td align="right">426,309</td>
<td align="right">4.3%</td>
<td align="right">-15.7%</td>
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
<td align="right">73,629</td>
<td align="right">14.6%</td>
<td align="right">34,415</td>
<td align="right">8.1%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,104</td>
<td align="right">0.2%</td>
<td align="right">705</td>
<td align="right">0.2%</td>
<td align="right">-36.1%</td>
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
<td align="right">8,155</td>
<td align="right">1.6%</td>
<td align="right">5,713</td>
<td align="right">1.3%</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">54,639</td>
<td align="right">10.8%</td>
<td align="right">39,479</td>
<td align="right">9.3%</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,320</td>
<td align="right">1.1%</td>
<td align="right">4,076</td>
<td align="right">1.0%</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,481</td>
<td align="right">4.8%</td>
<td align="right">19,486</td>
<td align="right">4.6%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,739</td>
<td align="right">0.5%</td>
<td align="right">2,379</td>
<td align="right">0.6%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">53,183</td>
<td align="right">10.5%</td>
<td align="right">47,774</td>
<td align="right">11.2%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,841</td>
<td align="right">0.4%</td>
<td align="right">1,689</td>
<td align="right">0.4%</td>
<td align="right">-8.3%</td>
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
<td align="left">class method obj</td>
<td align="right">15,819</td>
<td align="right">3.1%</td>
<td align="right">15,280</td>
<td align="right">3.6%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">0.9%</td>
<td align="right">4,446</td>
<td align="right">1.0%</td>
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
<td align="right">9,222,749,569</td>
<td align="right">99.8%</td>
<td align="right">4,267,118,679</td>
<td align="right">99.7%</td>
<td align="right">-53.7%</td>
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
<td align="right">47,197</td>
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
<td align="right">14,622,514</td>
<td align="right">0.2%</td>
<td align="right">14,622,618</td>
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
<td align="right">134,589</td>
<td align="right">100.0%</td>
<td align="right">137,900</td>
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
<td align="right">64,155,541</td>
<td align="right">100.0%</td>
<td align="right">63,830,107</td>
<td align="right">100.0%</td>
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
<td align="right">204</td>
<td align="right">0.0%</td>
<td align="right">203</td>
<td align="right">0.0%</td>
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
<td align="right">593,529,495</td>
<td align="right">82.2%</td>
<td align="right">591,604,847</td>
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
<td align="right">114,217,881</td>
<td align="right">5.7%</td>
<td align="right">82,432,197</td>
<td align="right">4.5%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">66,396,797</td>
<td align="right">3.3%</td>
<td align="right">51,472,951</td>
<td align="right">2.8%</td>
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
<td align="right">1,812,783,233</td>
<td align="right">90.9%</td>
<td align="right">1,696,481,651</td>
<td align="right">92.7%</td>
<td align="right">-6.4%</td>
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
<td align="right">2,193,970</td>
<td align="right">98.0%</td>
<td align="right">1,595,618</td>
<td align="right">97.6%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">44,918</td>
<td align="right">2.0%</td>
<td align="right">39,579</td>
<td align="right">2.4%</td>
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
<td align="left">class attr simple</td>
<td align="right">19,647</td>
<td align="right">43.7%</td>
<td align="right">15,607</td>
<td align="right">39.4%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">5,799</td>
<td align="right">12.9%</td>
<td align="right">4,650</td>
<td align="right">11.7%</td>
<td align="right">-19.8%</td>
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
<td align="right">552.7%</td>
<td align="right">239,826</td>
<td align="right">605.9%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,336</td>
<td align="right">7.4%</td>
<td align="right">3,436</td>
<td align="right">8.7%</td>
<td align="right">3.0%</td>
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
<td align="right">9.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">0.9%</td>
<td align="right">423</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
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
<td align="right">1,085,654</td>
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
<td align="right">700,605,368</td>
<td align="right">43.3%</td>
<td align="right">101,265,010</td>
<td align="right">10.9%</td>
<td align="right">-85.5%</td>
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
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">918,535,440</td>
<td align="right">56.7%</td>
<td align="right">826,808,559</td>
<td align="right">89.1%</td>
<td align="right">-10.0%</td>
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
<td align="right">181,878</td>
<td align="right">98.9%</td>
<td align="right">34,716</td>
<td align="right">94.1%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,064</td>
<td align="right">1.1%</td>
<td align="right">2,163</td>
<td align="right">5.9%</td>
<td align="right">4.8%</td>
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
<td align="right">10,484</td>
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
<td align="right">17,164</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">255,921,693</td>
<td align="right">5.0%</td>
<td align="right">128,388,157</td>
<td align="right">4.1%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">110,683,453</td>
<td align="right">2.2%</td>
<td align="right">60,516,879</td>
<td align="right">1.9%</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,728,867,851</td>
<td align="right">92.8%</td>
<td align="right">2,940,846,662</td>
<td align="right">94.0%</td>
<td align="right">-37.8%</td>
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
<td align="right">2,136,805</td>
<td align="right">78.2%</td>
<td align="right">1,191,335</td>
<td align="right">75.2%</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">596,960</td>
<td align="right">21.8%</td>
<td align="right">393,267</td>
<td align="right">24.8%</td>
<td align="right">-34.1%</td>
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
<td align="right">126,707</td>
<td align="right">21.2%</td>
<td align="right">26,563</td>
<td align="right">6.8%</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,856</td>
<td align="right">3.2%</td>
<td align="right">4,655</td>
<td align="right">1.2%</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,309</td>
<td align="right">2.7%</td>
<td align="right">10,429</td>
<td align="right">2.7%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">83,555</td>
<td align="right">14.0%</td>
<td align="right">54,142</td>
<td align="right">13.8%</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,856</td>
<td align="right">43.2%</td>
<td align="right">206,226</td>
<td align="right">52.4%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,724</td>
<td align="right">1.6%</td>
<td align="right">8,694</td>
<td align="right">2.2%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">72,063</td>
<td align="right">12.1%</td>
<td align="right">70,655</td>
<td align="right">18.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,048</td>
<td align="right">1.7%</td>
<td align="right">10,061</td>
<td align="right">2.6%</td>
<td align="right">0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,237,666,469</td>
<td align="right">99.9%</td>
<td align="right">913,305,034</td>
<td align="right">99.9%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,646,383</td>
<td align="right">0.1%</td>
<td align="right">1,251,685</td>
<td align="right">0.1%</td>
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
<td align="right">912</td>
<td align="right">8.4%</td>
<td align="right">783</td>
<td align="right">7.3%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,897</td>
<td align="right">91.6%</td>
<td align="right">9,890</td>
<td align="right">92.7%</td>
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
<td align="left">sequence</td>
<td align="right">677</td>
<td align="right">74.2%</td>
<td align="right">549</td>
<td align="right">70.1%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">99</td>
<td align="right">10.9%</td>
<td align="right">98</td>
<td align="right">12.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">14.9%</td>
<td align="right">136</td>
<td align="right">17.4%</td>
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
<td align="right">8,239,999,124</td>
<td align="right">3.9%</td>
<td align="right">2,943,849,781</td>
<td align="right">3.3%</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">78,581,537,713</td>
<td align="right">37.3%</td>
<td align="right">32,565,540,701</td>
<td align="right">36.5%</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">122,131,844,951</td>
<td align="right">58.0%</td>
<td align="right">52,713,180,038</td>
<td align="right">59.2%</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,497,426,838</td>
<td align="right">0.7%</td>
<td align="right">877,203,480</td>
<td align="right">1.0%</td>
<td align="right">-41.4%</td>
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
<td align="right">1,504,340,631</td>
<td align="right">20.6%</td>
<td align="right">194,687,283</td>
<td align="right">7.5%</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,605,368</td>
<td align="right">9.6%</td>
<td align="right">101,265,010</td>
<td align="right">3.9%</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,483,012</td>
<td align="right">7.0%</td>
<td align="right">90,641,876</td>
<td align="right">3.5%</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,731,800</td>
<td align="right">7.5%</td>
<td align="right">179,132,344</td>
<td align="right">6.9%</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,344,052,575</td>
<td align="right">32.0%</td>
<td align="right">995,920,750</td>
<td align="right">38.5%</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,912,156</td>
<td align="right">2.1%</td>
<td align="right">75,425,571</td>
<td align="right">2.9%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">255,921,693</td>
<td align="right">3.5%</td>
<td align="right">128,388,157</td>
<td align="right">5.0%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">800,119,152</td>
<td align="right">10.9%</td>
<td align="right">485,589,102</td>
<td align="right">18.8%</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">178,675,483</td>
<td align="right">2.4%</td>
<td align="right">140,547,040</td>
<td align="right">5.4%</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,934</td>
<td align="right">1.8%</td>
<td align="right">128,816,934</td>
<td align="right">5.0%</td>
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
<td align="right">81,904,291</td>
<td align="right">5.5%</td>
<td align="right">22,078,793</td>
<td align="right">2.5%</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">365,457,464</td>
<td align="right">24.4%</td>
<td align="right">174,014,710</td>
<td align="right">19.8%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">264,670,190</td>
<td align="right">17.7%</td>
<td align="right">137,567,645</td>
<td align="right">15.7%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,476,755</td>
<td align="right">3.6%</td>
<td align="right">28,385,887</td>
<td align="right">3.2%</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,376,231</td>
<td align="right">3.3%</td>
<td align="right">26,438,905</td>
<td align="right">3.0%</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,668,831</td>
<td align="right">5.5%</td>
<td align="right">49,546,762</td>
<td align="right">5.6%</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,987,984</td>
<td align="right">6.3%</td>
<td align="right">63,439,872</td>
<td align="right">7.2%</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,834,908</td>
<td align="right">5.5%</td>
<td align="right">59,549,398</td>
<td align="right">6.8%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">89,938,289</td>
<td align="right">6.0%</td>
<td align="right">70,170,514</td>
<td align="right">8.0%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,005,971</td>
<td align="right">5.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">24,717,967</td>
<td align="right">2.8%</td>
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
<td align="right">5,416,345,684</td>
<td align="right">81.0%</td>
<td align="right">4,460,757,333</td>
<td align="right">77.1%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">275,686,965</td>
<td align="right">4.1%</td>
<td align="right">232,211,258</td>
<td align="right">4.0%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,095,189,875</td>
<td align="right">76.2%</td>
<td align="right">4,317,633,013</td>
<td align="right">74.6%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,002,920,920</td>
<td align="right">15.0%</td>
<td align="right">879,872,598</td>
<td align="right">15.2%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,007,198,240</td>
<td align="right">15.1%</td>
<td align="right">884,147,598</td>
<td align="right">15.3%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,483,409</td>
<td align="right">3.9%</td>
<td align="right">228,325,959</td>
<td align="right">3.9%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,036,887</td>
<td align="right">1.1%</td>
<td align="right">63,710,217</td>
<td align="right">1.1%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,591,669,749</td>
<td align="right">23.8%</td>
<td align="right">1,467,991,491</td>
<td align="right">25.4%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,591,669,749</td>
<td align="right">23.8%</td>
<td align="right">1,467,991,491</td>
<td align="right">25.4%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,591,160</td>
<td align="right">0.4%</td>
<td align="right">22,767,531</td>
<td align="right">0.4%</td>
<td align="right">-3.5%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,471,509</td>
<td align="right">8.7%</td>
<td align="right">583,843,893</td>
<td align="right">10.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,457</td>
<td align="right">0.1%</td>
<td align="right">4,271,177</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
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
<td align="right">28,837,604</td>
<td align="right"></td>
<td align="right">4,472,766</td>
<td align="right"></td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">81,257,461</td>
<td align="right"></td>
<td align="right">44,997,523</td>
<td align="right"></td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">50,152,695,696</td>
<td align="right">46.1%</td>
<td align="right">29,027,115,799</td>
<td align="right">29.6%</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">39,078,200,165</td>
<td align="right">42.6%</td>
<td align="right">22,751,480,444</td>
<td align="right">27.8%</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,643,367,294</td>
<td align="right">5.1%</td>
<td align="right">2,755,311,282</td>
<td align="right">3.4%</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">31,767,485,811</td>
<td align="right">29.2%</td>
<td align="right">44,462,363,439</td>
<td align="right">45.3%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">24,959,099,709</td>
<td align="right">27.2%</td>
<td align="right">34,463,323,925</td>
<td align="right">42.1%</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,860,557,404</td>
<td align="right">1.7%</td>
<td align="right">1,153,066,065</td>
<td align="right">1.2%</td>
<td align="right">-38.0%</td>
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
<td align="right">2,425,553,475</td>
<td align="right"></td>
<td align="right">1,770,185,177</td>
<td align="right"></td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,366,840,944</td>
<td align="right"></td>
<td align="right">1,789,245,870</td>
<td align="right"></td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">53,222,707</td>
<td align="right"></td>
<td align="right">40,786,563</td>
<td align="right"></td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,159,928,128</td>
<td align="right"></td>
<td align="right">5,205,868,446</td>
<td align="right"></td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,484,923,477</td>
<td align="right">28.7%</td>
<td align="right">4,646,910,117</td>
<td align="right">26.6%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,562,563,059</td>
<td align="right">29.1%</td>
<td align="right">4,724,012,130</td>
<td align="right">27.0%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,573,676,726</td>
<td align="right">70.9%</td>
<td align="right">12,755,984,504</td>
<td align="right">73.0%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,573,824,634</td>
<td align="right"></td>
<td align="right">12,756,128,746</td>
<td align="right"></td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,944,339,663</td>
<td align="right">22.9%</td>
<td align="right">23,543,608,432</td>
<td align="right">24.0%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">22,993,603,786</td>
<td align="right">25.1%</td>
<td align="right">21,945,733,864</td>
<td align="right">26.8%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,612,523</td>
<td align="right"></td>
<td align="right">167,627,467</td>
<td align="right"></td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,365,261</td>
<td align="right">0.0%</td>
<td align="right">6,221,408</td>
<td align="right">0.0%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,274,321</td>
<td align="right">0.4%</td>
<td align="right">70,880,605</td>
<td align="right">0.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,404,476</td>
<td align="right">1.9%</td>
<td align="right">3,404,476</td>
<td align="right">2.0%</td>
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
<td align="right">364,837</td>
<td align="right">101,643,345</td>
<td align="right">9,530,931,688</td>
<td align="right">756,965,333</td>
<td align="right">765,041,367</td>
<td align="right">353,044</td>
<td align="right">69,904,191</td>
<td align="right">9,043,266,899</td>
<td align="right">741,075,751</td>
<td align="right">719,807,359</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,677,322,584</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,677,588,888</td>
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
Stats gathered on: 2025-06-05
