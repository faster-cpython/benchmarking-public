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
<td align="left">CONVERT_VALUE</td>
<td align="right">23,287,428</td>
<td align="right">75,281,532</td>
<td align="right">223.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">66,073,048</td>
<td align="right">199,698,006</td>
<td align="right">202.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">29,292,593</td>
<td align="right">81,286,697</td>
<td align="right">177.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">15,294,980</td>
<td align="right">41,322,952</td>
<td align="right">170.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">62,683,281</td>
<td align="right">131,286,391</td>
<td align="right">109.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">178,363,051</td>
<td align="right">365,322,878</td>
<td align="right">104.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">5,694,716</td>
<td align="right">8,976,796</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">2,272</td>
<td align="right">1,072</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">164,409,112</td>
<td align="right">246,464,512</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">164,876,606</td>
<td align="right">244,472,366</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">163,530,809</td>
<td align="right">242,422,203</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">631,019,711</td>
<td align="right">929,287,489</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">50,626,776</td>
<td align="right">73,446,421</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">201,844,434</td>
<td align="right">282,711,542</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">473,111,400</td>
<td align="right">659,612,612</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">9,526,077</td>
<td align="right">13,189,160</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">484,814,569</td>
<td align="right">608,465,828</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">2,489,180</td>
<td align="right">3,121,759</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">95,704,446</td>
<td align="right">118,564,075</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">730,576,776</td>
<td align="right">901,477,144</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">741,367,888</td>
<td align="right">909,784,595</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,838,519</td>
<td align="right">3,472,319</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,835,640,723</td>
<td align="right">2,224,083,141</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,927,410</td>
<td align="right">3,546,406</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">51,553,675</td>
<td align="right">61,844,741</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">152,808,635</td>
<td align="right">182,579,802</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,352,122</td>
<td align="right">39,795,946</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">53,588,336</td>
<td align="right">63,882,462</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">373,448,931</td>
<td align="right">443,398,581</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,048,216</td>
<td align="right">20,170,922</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,048,237</td>
<td align="right">20,170,940</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,973,919,364</td>
<td align="right">4,674,441,143</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">16,890,844</td>
<td align="right">19,844,167</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">738,246,043</td>
<td align="right">865,325,948</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">98,073,877</td>
<td align="right">114,605,022</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">133,548,492</td>
<td align="right">154,651,143</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">72,668,158</td>
<td align="right">84,120,932</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,588,579,091</td>
<td align="right">4,120,991,565</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">969,617,669</td>
<td align="right">1,112,683,010</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">188,284,536</td>
<td align="right">215,840,696</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,085,654</td>
<td align="right">1,232,482</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">75,466,161</td>
<td align="right">85,466,874</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">390,231,475</td>
<td align="right">441,680,593</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">31,247,012</td>
<td align="right">35,355,314</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,391,055,271</td>
<td align="right">4,963,118,900</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">144,170,271</td>
<td align="right">162,624,571</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,821,610</td>
<td align="right">42,616,550</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">109,033,113</td>
<td align="right">122,103,387</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,338,221,801</td>
<td align="right">2,614,397,674</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">185,659,358</td>
<td align="right">206,707,473</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">27,758,031</td>
<td align="right">30,824,492</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">235,728,207</td>
<td align="right">261,619,981</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">790,201,552</td>
<td align="right">876,540,380</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">14,753,420,857</td>
<td align="right">16,349,317,748</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">218,471,328</td>
<td align="right">241,917,671</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">16,453,633</td>
<td align="right">18,211,866</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">62,495,537</td>
<td align="right">69,152,030</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">733,580,359</td>
<td align="right">810,301,875</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">492,461,689</td>
<td align="right">543,538,502</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">156,697,515</td>
<td align="right">172,580,519</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">486,985,984</td>
<td align="right">535,585,038</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,280,849</td>
<td align="right">5,799,275</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,391,876,974</td>
<td align="right">3,721,944,066</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">218,564,748</td>
<td align="right">238,191,638</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">266,110,775</td>
<td align="right">289,716,099</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,356</td>
<td align="right">1,476</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,300,322,341</td>
<td align="right">2,491,760,999</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,952,594,198</td>
<td align="right">3,198,062,635</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">996,341,662</td>
<td align="right">1,078,958,242</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,464,870,884</td>
<td align="right">1,584,388,521</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,856,965,955</td>
<td align="right">2,000,988,672</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">355,298,381</td>
<td align="right">382,777,741</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">807,421,451</td>
<td align="right">869,744,358</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">603,572,088</td>
<td align="right">648,942,262</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">867,708,213</td>
<td align="right">932,836,064</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,644,824,736</td>
<td align="right">4,991,516,142</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">184,300,360</td>
<td align="right">197,650,682</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">45,873,040</td>
<td align="right">49,147,736</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,206,991</td>
<td align="right">27,125,636</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">365,666,026</td>
<td align="right">391,293,165</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,328,837,216</td>
<td align="right">1,421,781,050</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">31,518</td>
<td align="right">33,697</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,338,546</td>
<td align="right">18,526,435</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">194,797,972</td>
<td align="right">207,575,992</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">609,286,570</td>
<td align="right">647,967,511</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">312,967,255</td>
<td align="right">332,190,530</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,754,700,864</td>
<td align="right">3,982,385,591</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">345,774,546</td>
<td align="right">366,234,118</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">325,114,963</td>
<td align="right">344,095,712</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">128,832,545</td>
<td align="right">136,056,202</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">8,709,222</td>
<td align="right">9,187,510</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">117,947,567</td>
<td align="right">124,086,509</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">113,697,645</td>
<td align="right">107,987,803</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">148,375,156</td>
<td align="right">155,730,791</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">843,966,906</td>
<td align="right">885,383,740</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">262,658,624</td>
<td align="right">275,212,539</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">350,475,924</td>
<td align="right">367,077,844</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,918,629,630</td>
<td align="right">2,009,423,428</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,389</td>
<td align="right">3,549</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,840,100,794</td>
<td align="right">1,926,861,249</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">108,882,899</td>
<td align="right">113,905,589</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,119,330</td>
<td align="right">5,347,863</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">972,556,128</td>
<td align="right">1,013,462,902</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">421,202,765</td>
<td align="right">438,738,480</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">153,572,119</td>
<td align="right">159,340,956</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">441,858,251</td>
<td align="right">458,133,322</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">179,132,344</td>
<td align="right">185,527,960</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">109,288,589</td>
<td align="right">112,971,256</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">102,479,868</td>
<td align="right">105,821,252</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">44,273,374</td>
<td align="right">45,687,154</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">166,231,578</td>
<td align="right">171,096,626</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">356,426,891</td>
<td align="right">366,184,393</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">90,753,038</td>
<td align="right">93,209,366</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">134,647,237</td>
<td align="right">138,256,021</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">185,228,193</td>
<td align="right">190,096,933</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">53,803,093</td>
<td align="right">55,208,411</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">42,922,434</td>
<td align="right">43,963,748</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">66,238,756</td>
<td align="right">67,842,508</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">238,888,224</td>
<td align="right">244,591,388</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,573</td>
<td align="right">2,514</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">595,898,977</td>
<td align="right">609,425,571</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">94,060,632</td>
<td align="right">96,165,279</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,220,717</td>
<td align="right">2,270,355</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">101,301,869</td>
<td align="right">103,536,184</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">423,108,023</td>
<td align="right">432,379,229</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">340,879,134</td>
<td align="right">348,293,988</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">174,505,698</td>
<td align="right">171,053,052</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">68,447,731</td>
<td align="right">69,767,776</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">33,895,786</td>
<td align="right">34,495,206</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">501,853,392</td>
<td align="right">494,930,691</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">192,696,447</td>
<td align="right">190,138,964</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,389,629</td>
<td align="right">9,507,088</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,823</td>
<td align="right">3,863</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">118,262,962</td>
<td align="right">119,450,771</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">247,781</td>
<td align="right">245,602</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">56,504</td>
<td align="right">56,984</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">212,919</td>
<td align="right">214,351</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">274,807,691</td>
<td align="right">273,045,878</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">165,127,484</td>
<td align="right">164,237,102</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,318,877</td>
<td align="right">4,334,141</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,971</td>
<td align="right">12,933</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,105,493,305</td>
<td align="right">1,108,244,893</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">128,955,515</td>
<td align="right">129,276,104</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">66,838,630</td>
<td align="right">66,991,173</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">51,179,959</td>
<td align="right">51,285,923</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">286,870,756</td>
<td align="right">287,460,752</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,358</td>
<td align="right">5,369</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">64,212,077</td>
<td align="right">64,315,952</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,958,437</td>
<td align="right">27,927,133</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">820,663,708</td>
<td align="right">821,418,147</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">123,753,240</td>
<td align="right">123,859,776</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">265,241,937</td>
<td align="right">265,399,596</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">55,539,643</td>
<td align="right">55,569,669</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,088,983</td>
<td align="right">5,091,698</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,622,483</td>
<td align="right">57,604,736</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,680,248</td>
<td align="right">9,682,326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,159,711</td>
<td align="right">418,229,083</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,260,886</td>
<td align="right">70,268,313</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,759,813</td>
<td align="right">14,758,293</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">441,429</td>
<td align="right">441,392</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,201,283</td>
<td align="right">12,202,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,720,606</td>
<td align="right">25,721,937</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,024,264</td>
<td align="right">3,024,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,428</td>
<td align="right">9,742,628</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,965,283</td>
<td align="right">41,964,443</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,262,318</td>
<td align="right">1,262,309</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">10,549,266</td>
<td align="right">10,549,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,117</td>
<td align="right">35,549,086</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">76,372,528</td>
<td align="right">76,372,555</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,619,558</td>
<td align="right">591,619,527</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">114,765,149</td>
<td align="right">114,765,155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">468,453,321</td>
<td align="right">468,453,320</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,141</td>
<td align="right">302,246,141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">145,970,793</td>
<td align="right">145,970,793</td>
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
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,140</td>
<td align="right">2,597,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,721,846</td>
<td align="right">1,721,846</td>
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
<td align="right">98,575</td>
<td align="right">98,575</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,564</td>
<td align="right">72,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,551</td>
<td align="right">69,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,850</td>
<td align="right">53,850</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">13,984</td>
<td align="right">13,984</td>
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
<td align="right">995,920,750</td>
<td align="right">5.9%</td>
<td align="right">1,078,477,595</td>
<td align="right">6.2%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,186,238</td>
<td align="right">0.3%</td>
<td align="right">55,499,198</td>
<td align="right">0.3%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,947,262,774</td>
<td align="right">93.8%</td>
<td align="right">16,237,122,041</td>
<td align="right">93.5%</td>
<td align="right">1.8%</td>
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
<td align="right">402,636</td>
<td align="right">28.7%</td>
<td align="right">463,245</td>
<td align="right">30.3%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,002,657</td>
<td align="right">71.3%</td>
<td align="right">1,064,315</td>
<td align="right">69.7%</td>
<td align="right">6.1%</td>
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
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">760.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">17,713</td>
<td align="right">4.4%</td>
<td align="right">36,109</td>
<td align="right">7.8%</td>
<td align="right">103.9%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">72,761</td>
<td align="right">18.1%</td>
<td align="right">107,942</td>
<td align="right">23.3%</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">288</td>
<td align="right">0.1%</td>
<td align="right">348</td>
<td align="right">0.1%</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">169</td>
<td align="right">0.0%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,120</td>
<td align="right">0.5%</td>
<td align="right">2,334</td>
<td align="right">0.5%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">37,617</td>
<td align="right">9.3%</td>
<td align="right">41,352</td>
<td align="right">8.9%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">2,937</td>
<td align="right">0.7%</td>
<td align="right">3,165</td>
<td align="right">0.7%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">21,007</td>
<td align="right">5.2%</td>
<td align="right">22,376</td>
<td align="right">4.8%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20,816</td>
<td align="right">5.2%</td>
<td align="right">21,791</td>
<td align="right">4.7%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,477</td>
<td align="right">1.6%</td>
<td align="right">6,693</td>
<td align="right">1.4%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">6,830</td>
<td align="right">1.7%</td>
<td align="right">6,974</td>
<td align="right">1.5%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,364</td>
<td align="right">0.3%</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,130</td>
<td align="right">0.8%</td>
<td align="right">3,110</td>
<td align="right">0.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">627</td>
<td align="right">0.2%</td>
<td align="right">625</td>
<td align="right">0.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.6%</td>
<td align="right">2,350</td>
<td align="right">0.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,832</td>
<td align="right">4.9%</td>
<td align="right">19,860</td>
<td align="right">4.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">1,810</td>
<td align="right">0.4%</td>
<td align="right">1,812</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,767</td>
<td align="right">0.7%</td>
<td align="right">2,768</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,454</td>
<td align="right">4.6%</td>
<td align="right">18,448</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,298</td>
<td align="right">2.1%</td>
<td align="right">8,299</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">11,552</td>
<td align="right">2.9%</td>
<td align="right">11,553</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">62,999</td>
<td align="right">15.6%</td>
<td align="right">62,999</td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">28,692</td>
<td align="right">7.1%</td>
<td align="right">28,692</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">25,838</td>
<td align="right">6.4%</td>
<td align="right">25,838</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">16,343</td>
<td align="right">4.1%</td>
<td align="right">16,343</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,194</td>
<td align="right">1.5%</td>
<td align="right">6,194</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">0.5%</td>
<td align="right">1,996</td>
<td align="right">0.4%</td>
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
<td align="left">and other</td>
<td align="right">335</td>
<td align="right">0.1%</td>
<td align="right">335</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="left">subscr mappingproxy</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">80</td>
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
<td align="right">179,132,344</td>
<td align="right">100.0%</td>
<td align="right">185,527,960</td>
<td align="right">100.0%</td>
<td align="right">3.6%</td>
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
<td align="right">8,603,286,348</td>
<td align="right">98.4%</td>
<td align="right">11,083,736,443</td>
<td align="right">98.6%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">143,173,832</td>
<td align="right">1.6%</td>
<td align="right">153,782,869</td>
<td align="right">1.4%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">140,547,040</td>
<td align="right">1.6%</td>
<td align="right">150,955,628</td>
<td align="right">1.3%</td>
<td align="right">7.4%</td>
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
<td align="right">2,874,427</td>
<td align="right">100.0%</td>
<td align="right">3,072,697</td>
<td align="right">100.0%</td>
<td align="right">6.9%</td>
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
<td align="right">576,034</td>
<td align="right">96.6%</td>
<td align="right">576,036</td>
<td align="right">96.6%</td>
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
<td align="right">583,374</td>
<td align="right">97.8%</td>
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
<td align="right">20,311</td>
<td align="right">100.0%</td>
<td align="right">20,271</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,011,609</td>
<td align="right">0.0%</td>
<td align="right">1,145,330</td>
<td align="right">0.0%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">90,641,876</td>
<td align="right">2.0%</td>
<td align="right">93,092,683</td>
<td align="right">2.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,404,393,437</td>
<td align="right">98.0%</td>
<td align="right">4,503,591,179</td>
<td align="right">97.9%</td>
<td align="right">2.3%</td>
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
<td align="right">93,010</td>
<td align="right">71.5%</td>
<td align="right">98,834</td>
<td align="right">71.6%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">37,026</td>
<td align="right">28.5%</td>
<td align="right">39,273</td>
<td align="right">28.4%</td>
<td align="right">6.1%</td>
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
<td align="right">154</td>
<td align="right">0.2%</td>
<td align="right">196</td>
<td align="right">0.2%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">797</td>
<td align="right">0.9%</td>
<td align="right">953</td>
<td align="right">1.0%</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">31,657</td>
<td align="right">34.0%</td>
<td align="right">36,917</td>
<td align="right">37.4%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,278</td>
<td align="right">1.4%</td>
<td align="right">1,324</td>
<td align="right">1.3%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,060</td>
<td align="right">4.4%</td>
<td align="right">4,162</td>
<td align="right">4.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">369</td>
<td align="right">0.4%</td>
<td align="right">373</td>
<td align="right">0.4%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,680</td>
<td align="right">8.3%</td>
<td align="right">7,750</td>
<td align="right">7.8%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,874</td>
<td align="right">2.0%</td>
<td align="right">1,860</td>
<td align="right">1.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">22,993</td>
<td align="right">24.7%</td>
<td align="right">23,127</td>
<td align="right">23.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">5,851</td>
<td align="right">6.3%</td>
<td align="right">5,876</td>
<td align="right">5.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,649</td>
<td align="right">9.3%</td>
<td align="right">8,648</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">8.2%</td>
<td align="right">7,648</td>
<td align="right">7.7%</td>
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
<td align="right">1,840,982,698</td>
<td align="right">96.0%</td>
<td align="right">2,185,686,629</td>
<td align="right">96.2%</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">75,425,571</td>
<td align="right">3.9%</td>
<td align="right">85,423,286</td>
<td align="right">3.8%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,389,959</td>
<td align="right">0.1%</td>
<td align="right">1,389,959</td>
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
<td align="right">38,280</td>
<td align="right">57.3%</td>
<td align="right">41,478</td>
<td align="right">59.4%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,533</td>
<td align="right">42.7%</td>
<td align="right">28,333</td>
<td align="right">40.6%</td>
<td align="right">-0.7%</td>
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
<td align="right">7,772</td>
<td align="right">20.3%</td>
<td align="right">9,649</td>
<td align="right">23.3%</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">11,267</td>
<td align="right">29.4%</td>
<td align="right">12,030</td>
<td align="right">29.0%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,185</td>
<td align="right">26.6%</td>
<td align="right">10,539</td>
<td align="right">25.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,056</td>
<td align="right">23.7%</td>
<td align="right">9,260</td>
<td align="right">22.3%</td>
<td align="right">2.3%</td>
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
<td align="right">44,179,168</td>
<td align="right">3.1%</td>
<td align="right">55,738,263</td>
<td align="right">3.6%</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">194,687,283</td>
<td align="right">13.5%</td>
<td align="right">207,460,230</td>
<td align="right">13.5%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,201,003,750</td>
<td align="right">83.4%</td>
<td align="right">1,268,096,923</td>
<td align="right">82.8%</td>
<td align="right">5.6%</td>
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
<td align="right">838,821</td>
<td align="right">88.8%</td>
<td align="right">1,056,893</td>
<td align="right">90.5%</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">105,298</td>
<td align="right">11.2%</td>
<td align="right">110,364</td>
<td align="right">9.5%</td>
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
<td align="left">seq iter</td>
<td align="right">3,139</td>
<td align="right">3.0%</td>
<td align="right">5,891</td>
<td align="right">5.3%</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">956</td>
<td align="right">0.9%</td>
<td align="right">1,216</td>
<td align="right">1.1%</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,759</td>
<td align="right">4.5%</td>
<td align="right">5,697</td>
<td align="right">5.2%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">221</td>
<td align="right">0.2%</td>
<td align="right">260</td>
<td align="right">0.2%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,501</td>
<td align="right">5.2%</td>
<td align="right">6,265</td>
<td align="right">5.7%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,618</td>
<td align="right">1.5%</td>
<td align="right">1,702</td>
<td align="right">1.5%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,731</td>
<td align="right">12.1%</td>
<td align="right">12,879</td>
<td align="right">11.7%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">10,887</td>
<td align="right">10.3%</td>
<td align="right">10,964</td>
<td align="right">9.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,047</td>
<td align="right">3.8%</td>
<td align="right">4,027</td>
<td align="right">3.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,166</td>
<td align="right">4.0%</td>
<td align="right">4,178</td>
<td align="right">3.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">49,707</td>
<td align="right">47.2%</td>
<td align="right">49,719</td>
<td align="right">45.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,497</td>
<td align="right">3.3%</td>
<td align="right">3,497</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,490</td>
<td align="right">3.3%</td>
<td align="right">3,490</td>
<td align="right">3.2%</td>
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
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">0.2%</td>
<td align="right">232</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">120,684,899</td>
<td align="right">120,684,899 / 0 !!</td>
<td align="right">171,433,937</td>
<td align="right">171,433,937 / 0 !!</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,045,632</td>
<td align="right">4,045,632 / 0 !!</td>
<td align="right">5,428,467</td>
<td align="right">5,428,467 / 0 !!</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">247,559,320</td>
<td align="right">247,559,320 / 0 !!</td>
<td align="right">301,396,393</td>
<td align="right">301,396,393 / 0 !!</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">85,267,026</td>
<td align="right">85,267,026 / 0 !!</td>
<td align="right">101,812,825</td>
<td align="right">101,812,825 / 0 !!</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111,955,996</td>
<td align="right">111,955,996 / 0 !!</td>
<td align="right">116,755,860</td>
<td align="right">116,755,860 / 0 !!</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,604,954</td>
<td align="right">2,604,954 / 0 !!</td>
<td align="right">2,693,934</td>
<td align="right">2,693,934 / 0 !!</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,651,422</td>
<td align="right">34,651,422 / 0 !!</td>
<td align="right">34,813,451</td>
<td align="right">34,813,451 / 0 !!</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,046,246</td>
<td align="right">12,046,246 / 0 !!</td>
<td align="right">12,092,310</td>
<td align="right">12,092,310 / 0 !!</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,556,271</td>
<td align="right">341,556,271 / 0 !!</td>
<td align="right">341,889,324</td>
<td align="right">341,889,324 / 0 !!</td>
<td align="right">0.1%</td>
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
<td align="right">491,507,925</td>
<td align="right">4.7%</td>
<td align="right">618,565,037</td>
<td align="right">5.4%</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">485,589,102</td>
<td align="right">4.6%</td>
<td align="right">533,896,067</td>
<td align="right">4.7%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,512,360,600</td>
<td align="right">90.7%</td>
<td align="right">10,198,152,375</td>
<td align="right">89.8%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,262,383</td>
<td align="right">0.0%</td>
<td align="right">1,262,383</td>
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
<td align="right">9,388,485</td>
<td align="right">95.7%</td>
<td align="right">11,752,037</td>
<td align="right">96.4%</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">426,309</td>
<td align="right">4.3%</td>
<td align="right">435,550</td>
<td align="right">3.6%</td>
<td align="right">2.2%</td>
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
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">19,486</td>
<td align="right">4.6%</td>
<td align="right">24,165</td>
<td align="right">5.5%</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,713</td>
<td align="right">1.3%</td>
<td align="right">6,981</td>
<td align="right">1.6%</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,689</td>
<td align="right">0.4%</td>
<td align="right">1,841</td>
<td align="right">0.4%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,622</td>
<td align="right">0.4%</td>
<td align="right">1,719</td>
<td align="right">0.4%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">34,415</td>
<td align="right">8.1%</td>
<td align="right">36,345</td>
<td align="right">8.3%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">705</td>
<td align="right">0.2%</td>
<td align="right">743</td>
<td align="right">0.2%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,280</td>
<td align="right">3.6%</td>
<td align="right">15,413</td>
<td align="right">3.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">39,479</td>
<td align="right">9.3%</td>
<td align="right">39,762</td>
<td align="right">9.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">47,774</td>
<td align="right">11.2%</td>
<td align="right">47,960</td>
<td align="right">11.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,076</td>
<td align="right">1.0%</td>
<td align="right">4,062</td>
<td align="right">0.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,446</td>
<td align="right">1.0%</td>
<td align="right">4,447</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,379</td>
<td align="right">0.6%</td>
<td align="right">2,379</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
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
<td align="right">4,267,118,679</td>
<td align="right">99.7%</td>
<td align="right">4,602,578,844</td>
<td align="right">99.7%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">47,197</td>
<td align="right">0.0%</td>
<td align="right">48,384</td>
<td align="right">0.0%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,618</td>
<td align="right">0.3%</td>
<td align="right">14,622,506</td>
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
<td align="right">137,900</td>
<td align="right">100.0%</td>
<td align="right">136,492</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">203</td>
<td align="right">0.0%</td>
<td align="right">204</td>
<td align="right">0.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">63,830,107</td>
<td align="right">100.0%</td>
<td align="right">63,860,261</td>
<td align="right">100.0%</td>
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
<td align="right">2,370</td>
<td align="right">100.0%</td>
<td align="right">2,310</td>
<td align="right">100.0%</td>
<td align="right">-2.5%</td>
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
<td align="right">591,604,847</td>
<td align="right">82.1%</td>
<td align="right">591,604,816</td>
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
<td align="right">128,816,934</td>
<td align="right">17.9%</td>
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
<td align="right">82,432,197</td>
<td align="right">4.5%</td>
<td align="right">106,794,056</td>
<td align="right">5.4%</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">51,472,951</td>
<td align="right">2.8%</td>
<td align="right">61,761,165</td>
<td align="right">3.1%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,696,481,651</td>
<td align="right">92.7%</td>
<td align="right">1,814,510,835</td>
<td align="right">91.5%</td>
<td align="right">7.0%</td>
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
<td align="right">1,595,618</td>
<td align="right">97.6%</td>
<td align="right">2,053,899</td>
<td align="right">97.9%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">39,579</td>
<td align="right">2.4%</td>
<td align="right">43,851</td>
<td align="right">2.1%</td>
<td align="right">10.8%</td>
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
<td align="right">15,607</td>
<td align="right">39.4%</td>
<td align="right">19,647</td>
<td align="right">44.8%</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,175</td>
<td align="right">3.0%</td>
<td align="right">1,321</td>
<td align="right">3.0%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">693</td>
<td align="right">1.8%</td>
<td align="right">753</td>
<td align="right">1.7%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,436</td>
<td align="right">8.7%</td>
<td align="right">3,352</td>
<td align="right">7.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,650</td>
<td align="right">11.7%</td>
<td align="right">4,715</td>
<td align="right">10.8%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">111</td>
<td align="right">0.3%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,207</td>
<td align="right">18.2%</td>
<td align="right">7,227</td>
<td align="right">16.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,737</td>
<td align="right">9.4%</td>
<td align="right">3,741</td>
<td align="right">8.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">239,826</td>
<td align="right">605.9%</td>
<td align="right">240,046</td>
<td align="right">547.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">1.1%</td>
<td align="right">423</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">363</td>
<td align="right">0.9%</td>
<td align="right">363</td>
<td align="right">0.8%</td>
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
<td align="right">1,085,654</td>
<td align="right">100.0%</td>
<td align="right">1,232,482</td>
<td align="right">100.0%</td>
<td align="right">13.5%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">940</td>
<td align="right">0.0%</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">136.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">826,808,559</td>
<td align="right">89.1%</td>
<td align="right">916,911,541</td>
<td align="right">89.9%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">101,265,010</td>
<td align="right">10.9%</td>
<td align="right">103,497,994</td>
<td align="right">10.1%</td>
<td align="right">2.2%</td>
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
<td align="right">34,716</td>
<td align="right">94.1%</td>
<td align="right">36,146</td>
<td align="right">94.5%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,163</td>
<td align="right">5.9%</td>
<td align="right">2,084</td>
<td align="right">5.5%</td>
<td align="right">-3.7%</td>
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
<td align="left">bytearray int</td>
<td align="right">47</td>
<td align="right">0.1%</td>
<td align="right">162</td>
<td align="right">0.4%</td>
<td align="right">244.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,511</td>
<td align="right">7.2%</td>
<td align="right">2,990</td>
<td align="right">8.3%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,563</td>
<td align="right">4.5%</td>
<td align="right">1,681</td>
<td align="right">4.7%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,447</td>
<td align="right">47.4%</td>
<td align="right">17,165</td>
<td align="right">47.5%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">10,484</td>
<td align="right">30.2%</td>
<td align="right">10,484</td>
<td align="right">29.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">3,323</td>
<td align="right">9.6%</td>
<td align="right">3,323</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">273</td>
<td align="right">0.8%</td>
<td align="right">273</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,940,846,662</td>
<td align="right">94.0%</td>
<td align="right">4,150,867,175</td>
<td align="right">95.4%</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">60,516,879</td>
<td align="right">1.9%</td>
<td align="right">65,367,356</td>
<td align="right">1.5%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,388,157</td>
<td align="right">4.1%</td>
<td align="right">135,536,835</td>
<td align="right">3.1%</td>
<td align="right">5.6%</td>
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
<td align="right">393,267</td>
<td align="right">24.8%</td>
<td align="right">468,793</td>
<td align="right">26.8%</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,191,335</td>
<td align="right">75.2%</td>
<td align="right">1,282,185</td>
<td align="right">73.2%</td>
<td align="right">7.6%</td>
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
<td align="right">54,142</td>
<td align="right">13.8%</td>
<td align="right">74,358</td>
<td align="right">15.9%</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">206,226</td>
<td align="right">52.4%</td>
<td align="right">257,860</td>
<td align="right">55.0%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">8,694</td>
<td align="right">2.2%</td>
<td align="right">9,384</td>
<td align="right">2.0%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">26,563</td>
<td align="right">6.8%</td>
<td align="right">27,708</td>
<td align="right">5.9%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">10,429</td>
<td align="right">2.7%</td>
<td align="right">10,848</td>
<td align="right">2.3%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">70,655</td>
<td align="right">18.0%</td>
<td align="right">72,063</td>
<td align="right">15.4%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,061</td>
<td align="right">2.6%</td>
<td align="right">10,074</td>
<td align="right">2.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,655</td>
<td align="right">1.2%</td>
<td align="right">4,656</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.4%</td>
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
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">913,305,034</td>
<td align="right">99.9%</td>
<td align="right">1,230,676,166</td>
<td align="right">99.9%</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,251,685</td>
<td align="right">0.1%</td>
<td align="right">1,251,657</td>
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
<td align="right">783</td>
<td align="right">7.3%</td>
<td align="right">795</td>
<td align="right">7.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,890</td>
<td align="right">92.7%</td>
<td align="right">9,937</td>
<td align="right">92.6%</td>
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
<td align="left">sequence</td>
<td align="right">549</td>
<td align="right">70.1%</td>
<td align="right">561</td>
<td align="right">70.6%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">17.4%</td>
<td align="right">136</td>
<td align="right">17.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">12.5%</td>
<td align="right">98</td>
<td align="right">12.3%</td>
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
<td align="right">877,203,480</td>
<td align="right">1.0%</td>
<td align="right">1,059,095,529</td>
<td align="right">1.1%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">52,713,180,038</td>
<td align="right">59.2%</td>
<td align="right">58,886,314,429</td>
<td align="right">59.7%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">32,565,540,701</td>
<td align="right">36.5%</td>
<td align="right">35,433,161,442</td>
<td align="right">36.0%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,943,849,781</td>
<td align="right">3.3%</td>
<td align="right">3,177,664,966</td>
<td align="right">3.2%</td>
<td align="right">7.9%</td>
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
<td align="right">75,425,571</td>
<td align="right">2.9%</td>
<td align="right">85,423,286</td>
<td align="right">3.1%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">485,589,102</td>
<td align="right">18.8%</td>
<td align="right">533,896,067</td>
<td align="right">19.2%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">995,920,750</td>
<td align="right">38.5%</td>
<td align="right">1,078,477,595</td>
<td align="right">38.8%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">140,547,040</td>
<td align="right">5.4%</td>
<td align="right">150,955,628</td>
<td align="right">5.4%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">194,687,283</td>
<td align="right">7.5%</td>
<td align="right">207,460,230</td>
<td align="right">7.5%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">128,388,157</td>
<td align="right">5.0%</td>
<td align="right">135,536,835</td>
<td align="right">4.9%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">179,132,344</td>
<td align="right">6.9%</td>
<td align="right">185,527,960</td>
<td align="right">6.7%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">90,641,876</td>
<td align="right">3.5%</td>
<td align="right">93,092,683</td>
<td align="right">3.3%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">101,265,010</td>
<td align="right">3.9%</td>
<td align="right">103,497,994</td>
<td align="right">3.7%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,934</td>
<td align="right">5.0%</td>
<td align="right">128,816,934</td>
<td align="right">4.6%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">63,439,872</td>
<td align="right">7.2%</td>
<td align="right">87,792,244</td>
<td align="right">8.3%</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">59,549,398</td>
<td align="right">6.8%</td>
<td align="right">81,595,930</td>
<td align="right">7.7%</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">137,567,645</td>
<td align="right">15.7%</td>
<td align="right">176,126,152</td>
<td align="right">16.6%</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">174,014,710</td>
<td align="right">19.8%</td>
<td align="right">220,513,609</td>
<td align="right">20.8%</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">22,078,793</td>
<td align="right">2.5%</td>
<td align="right">27,832,125</td>
<td align="right">2.6%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">70,170,514</td>
<td align="right">8.0%</td>
<td align="right">85,458,828</td>
<td align="right">8.1%</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">49,546,762</td>
<td align="right">5.6%</td>
<td align="right">55,002,049</td>
<td align="right">5.2%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">28,385,887</td>
<td align="right">3.2%</td>
<td align="right">30,971,671</td>
<td align="right">2.9%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">26,438,905</td>
<td align="right">3.0%</td>
<td align="right">27,807,634</td>
<td align="right">2.6%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">24,717,967</td>
<td align="right">2.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">27,828,743</td>
<td align="right">2.6%</td>
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
<td align="right">4,460,757,333</td>
<td align="right">77.1%</td>
<td align="right">5,395,162,274</td>
<td align="right">81.0%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">232,211,258</td>
<td align="right">4.0%</td>
<td align="right">274,402,786</td>
<td align="right">4.1%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,317,633,013</td>
<td align="right">74.6%</td>
<td align="right">5,071,621,247</td>
<td align="right">76.1%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">879,872,598</td>
<td align="right">15.2%</td>
<td align="right">1,000,618,835</td>
<td align="right">15.0%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">884,147,598</td>
<td align="right">15.3%</td>
<td align="right">1,004,896,155</td>
<td align="right">15.1%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">228,325,959</td>
<td align="right">3.9%</td>
<td align="right">259,056,307</td>
<td align="right">3.9%</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">63,710,217</td>
<td align="right">1.1%</td>
<td align="right">70,133,056</td>
<td align="right">1.1%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,467,991,491</td>
<td align="right">25.4%</td>
<td align="right">1,588,876,128</td>
<td align="right">23.9%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,467,991,491</td>
<td align="right">25.4%</td>
<td align="right">1,588,876,128</td>
<td align="right">23.9%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">22,767,531</td>
<td align="right">0.4%</td>
<td align="right">23,557,720</td>
<td align="right">0.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,823</td>
<td align="right">0.0%</td>
<td align="right">3,863</td>
<td align="right">0.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,271,177</td>
<td align="right">0.1%</td>
<td align="right">4,273,457</td>
<td align="right">0.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">583,843,893</td>
<td align="right">10.1%</td>
<td align="right">583,979,973</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,898</td>
<td align="right">2.3%</td>
<td align="right">132,513,898</td>
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
<td align="left">Method cache dunder hits</td>
<td align="right">1,770,185,177</td>
<td align="right"></td>
<td align="right">2,422,286,259</td>
<td align="right"></td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">40,786,563</td>
<td align="right"></td>
<td align="right">54,883,947</td>
<td align="right"></td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">44,997,523</td>
<td align="right"></td>
<td align="right">59,001,900</td>
<td align="right"></td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">1,789,245,870</td>
<td align="right"></td>
<td align="right">2,186,064,465</td>
<td align="right"></td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">219,030</td>
<td align="right">0.1%</td>
<td align="right">265,170</td>
<td align="right">0.2%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">5,205,868,446</td>
<td align="right"></td>
<td align="right">6,134,381,263</td>
<td align="right"></td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">4,646,910,117</td>
<td align="right">26.6%</td>
<td align="right">5,461,473,187</td>
<td align="right">28.6%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">4,724,012,130</td>
<td align="right">27.0%</td>
<td align="right">5,539,032,709</td>
<td align="right">29.0%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">34,463,323,925</td>
<td align="right">42.1%</td>
<td align="right">40,347,211,546</td>
<td align="right">43.6%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">29,027,115,799</td>
<td align="right">29.6%</td>
<td align="right">33,272,528,873</td>
<td align="right">30.4%</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">44,462,363,439</td>
<td align="right">45.3%</td>
<td align="right">49,729,179,506</td>
<td align="right">45.4%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">21,945,733,864</td>
<td align="right">26.8%</td>
<td align="right">24,293,859,204</td>
<td align="right">26.3%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">4,472,766</td>
<td align="right"></td>
<td align="right">4,923,522</td>
<td align="right"></td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">22,751,480,444</td>
<td align="right">27.8%</td>
<td align="right">24,823,035,251</td>
<td align="right">26.8%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,755,311,282</td>
<td align="right">3.4%</td>
<td align="right">2,993,599,300</td>
<td align="right">3.2%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">23,543,608,432</td>
<td align="right">24.0%</td>
<td align="right">25,347,022,429</td>
<td align="right">23.1%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,755,984,504</td>
<td align="right">73.0%</td>
<td align="right">13,540,235,022</td>
<td align="right">71.0%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,756,128,746</td>
<td align="right"></td>
<td align="right">13,540,363,123</td>
<td align="right"></td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,153,066,065</td>
<td align="right">1.2%</td>
<td align="right">1,205,501,299</td>
<td align="right">1.1%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">167,627,467</td>
<td align="right"></td>
<td align="right">174,214,869</td>
<td align="right"></td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,221,408</td>
<td align="right">0.0%</td>
<td align="right">6,368,913</td>
<td align="right">0.0%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">70,880,605</td>
<td align="right">0.4%</td>
<td align="right">71,190,609</td>
<td align="right">0.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,404,476</td>
<td align="right">2.0%</td>
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
<td align="right">353,044</td>
<td align="right">69,904,191</td>
<td align="right">9,043,266,899</td>
<td align="right">741,075,751</td>
<td align="right">719,807,359</td>
<td align="right">364,492</td>
<td align="right">100,737,066</td>
<td align="right">9,529,347,887</td>
<td align="right">757,466,104</td>
<td align="right">764,947,990</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,677,588,888</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,677,582,360</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">182</td>
<td align="right">0.0%</td>
<td align="right">333.3%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">102</td>
<td align="right">0.0%</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,946</td>
<td align="right">0.5%</td>
<td align="right">3,026</td>
<td align="right">0.7%</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">412</td>
<td align="right">0.1%</td>
<td align="right">591</td>
<td align="right">0.1%</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">26,955</td>
<td align="right">6.8%</td>
<td align="right">34,377</td>
<td align="right">7.7%</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">219,459,783,021</td>
<td align="right">6,338.1%</td>
<td align="right">259,514,197,523</td>
<td align="right">6,447.3%</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">200,595</td>
<td align="right">50.7%</td>
<td align="right">236,887</td>
<td align="right">53.3%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,462,525,170</td>
<td align="right"></td>
<td align="right">4,025,133,903</td>
<td align="right"></td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">395,304</td>
<td align="right"></td>
<td align="right">444,470</td>
<td align="right"></td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,659</td>
<td align="right">0.4%</td>
<td align="right">1,752</td>
<td align="right">0.4%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">120,756</td>
<td align="right">30.5%</td>
<td align="right">125,820</td>
<td align="right">28.3%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">46,956</td>
<td align="right">11.9%</td>
<td align="right">47,204</td>
<td align="right">10.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">261</td>
<td align="right">1.0%</td>
<td align="right">261</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">26,955</td>
<td align="right"></td>
<td align="right">34,377</td>
<td align="right"></td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">22,077</td>
<td align="right">81.9%</td>
<td align="right">26,919</td>
<td align="right">78.3%</td>
<td align="right">21.9%</td>
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
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">217,986,648</td>
<td align="right">80.8%</td>
<td align="right">269,875,784</td>
<td align="right">81.3%</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">269,762,560</td>
<td align="right"></td>
<td align="right">332,091,392</td>
<td align="right"></td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">5,719,712</td>
<td align="right">2.1%</td>
<td align="right">6,943,816</td>
<td align="right">2.1%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">46,056,200</td>
<td align="right">17.1%</td>
<td align="right">55,271,792</td>
<td align="right">16.6%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">18,395,136</td>
<td align="right">6.8%</td>
<td align="right">18,350,080</td>
<td align="right">5.5%</td>
<td align="right">-0.2%</td>
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
<td align="left">5,581</td>
<td align="right">25.3%</td>
<td align="left">6,760</td>
<td align="right">25.1%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">6,999</td>
<td align="right">31.7%</td>
<td align="left">8,445</td>
<td align="right">31.4%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">6,254</td>
<td align="right">28.3%</td>
<td align="left">7,623</td>
<td align="right">28.3%</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,225</td>
<td align="right">10.1%</td>
<td align="left">2,872</td>
<td align="right">10.7%</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">938</td>
<td align="right">4.2%</td>
<td align="left">1,119</td>
<td align="right">4.2%</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">80</td>
<td align="right">0.4%</td>
<td align="left">100</td>
<td align="right">0.4%</td>
<td align="right">25.0%</td>
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
<td align="right">1,300</td>
<td align="right">4.8%</td>
<td align="right">1,290</td>
<td align="right">3.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">918</td>
<td align="right">3.4%</td>
<td align="right">975</td>
<td align="right">2.8%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,289</td>
<td align="right">15.9%</td>
<td align="right">5,636</td>
<td align="right">16.4%</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,187</td>
<td align="right">30.4%</td>
<td align="right">10,270</td>
<td align="right">29.9%</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">5,199</td>
<td align="right">19.3%</td>
<td align="right">5,849</td>
<td align="right">17.0%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,146</td>
<td align="right">19.1%</td>
<td align="right">8,045</td>
<td align="right">23.4%</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,649</td>
<td align="right">6.1%</td>
<td align="right">1,942</td>
<td align="right">5.6%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">267</td>
<td align="right">1.0%</td>
<td align="right">370</td>
<td align="right">1.1%</td>
<td align="right">38.6%</td>
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
<td align="right">733</td>
<td align="right">2.7%</td>
<td align="right">723</td>
<td align="right">2.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">894</td>
<td align="right">3.3%</td>
<td align="right">917</td>
<td align="right">2.7%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,658</td>
<td align="right">9.9%</td>
<td align="right">3,425</td>
<td align="right">10.0%</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,366</td>
<td align="right">27.3%</td>
<td align="right">9,130</td>
<td align="right">26.6%</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">6,156</td>
<td align="right">22.8%</td>
<td align="right">7,470</td>
<td align="right">21.7%</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,449</td>
<td align="right">9.1%</td>
<td align="right">2,943</td>
<td align="right">8.6%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,653</td>
<td align="right">6.1%</td>
<td align="right">2,000</td>
<td align="right">5.8%</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">168</td>
<td align="right">0.6%</td>
<td align="right">311</td>
<td align="right">0.9%</td>
<td align="right">85.1%</td>
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
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">918,506</td>
<td align="right">498,439,034</td>
<td align="right">54,166.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">117,983</td>
<td align="right">6,159,872</td>
<td align="right">5,121.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,409,132</td>
<td align="right">39,821,900</td>
<td align="right">2,726.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">12,676,354</td>
<td align="right">261,500,852</td>
<td align="right">1,962.9%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">2,176,916</td>
<td align="right">40,589,684</td>
<td align="right">1,764.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,433,550</td>
<td align="right">20,612,164</td>
<td align="right">1,337.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">90,251,546</td>
<td align="right">798,910,298</td>
<td align="right">785.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">30,021,079</td>
<td align="right">245,144,435</td>
<td align="right">716.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">49,249,153</td>
<td align="right">259,280,781</td>
<td align="right">426.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">50,000,357</td>
<td align="right">259,932,645</td>
<td align="right">419.9%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">5,303,275</td>
<td align="right">24,484,725</td>
<td align="right">361.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">5,303,275</td>
<td align="right">24,484,725</td>
<td align="right">361.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">38,403,043</td>
<td align="right">132,189,336</td>
<td align="right">244.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">404,704,938</td>
<td align="right">1,083,428,503</td>
<td align="right">167.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">80,852,291</td>
<td align="right">200,302,806</td>
<td align="right">147.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">208,826,508</td>
<td align="right">499,328,667</td>
<td align="right">139.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">197,213,809</td>
<td align="right">411,932,397</td>
<td align="right">108.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">488,713,569</td>
<td align="right">1,002,770,260</td>
<td align="right">105.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">488,826,809</td>
<td align="right">1,002,971,960</td>
<td align="right">105.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">6,682,039</td>
<td align="right">13,020,108</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">179,903</td>
<td align="right">15,603</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">121,483,411</td>
<td align="right">228,505,307</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">608,017,844</td>
<td align="right">1,121,862,402</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">96,571,864</td>
<td align="right">177,053,446</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">24,643,554</td>
<td align="right">43,800,460</td>
<td align="right">77.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">192,070,404</td>
<td align="right">340,478,605</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,729,485,062</td>
<td align="right">3,059,310,965</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">196,150,743</td>
<td align="right">346,331,132</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">704,727,672</td>
<td align="right">1,216,305,577</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">782,710,272</td>
<td align="right">1,302,388,134</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">146,563,579</td>
<td align="right">242,976,559</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">795,258,363</td>
<td align="right">1,314,936,225</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">795,258,363</td>
<td align="right">1,314,936,225</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">91,303,313</td>
<td align="right">148,373,640</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">883,252,781</td>
<td align="right">1,404,918,804</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,163,545,557</td>
<td align="right">1,847,015,981</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">165,444,801</td>
<td align="right">261,874,955</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">145,657,750</td>
<td align="right">226,869,851</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">432,627,956</td>
<td align="right">664,050,057</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,553,408,521</td>
<td align="right">3,879,070,747</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">461,541,864</td>
<td align="right">672,496,943</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">602,737,018</td>
<td align="right">864,175,297</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">1,462,457,101</td>
<td align="right">2,061,699,431</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">591,121,799</td>
<td align="right">831,959,636</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">247,571,746</td>
<td align="right">338,500,721</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,861,453,046</td>
<td align="right">3,898,904,358</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,897,590</td>
<td align="right">1,243,230</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,031,777,649</td>
<td align="right">4,011,477,051</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">2,703,824,935</td>
<td align="right">3,555,810,663</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">40,758,339</td>
<td align="right">52,869,997</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">607,566,878</td>
<td align="right">783,195,663</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">568,191,683</td>
<td align="right">726,608,873</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,256,733,490</td>
<td align="right">2,861,379,344</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">433,477,165</td>
<td align="right">547,987,773</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">5,835,272,835</td>
<td align="right">7,171,529,070</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">84,643,314</td>
<td align="right">103,813,640</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,102,011,464</td>
<td align="right">11,118,011,132</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">121,814,823</td>
<td align="right">148,536,268</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,318,596,991</td>
<td align="right">1,599,871,364</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,227,614,467</td>
<td align="right">1,481,102,703</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">29,656,605</td>
<td align="right">35,698,711</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,720,625,599</td>
<td align="right">4,472,174,110</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,987,201,544</td>
<td align="right">2,386,666,124</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,448,838,092</td>
<td align="right">4,139,266,256</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">424,164,977</td>
<td align="right">504,275,684</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">262,303,007</td>
<td align="right">310,262,197</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,427,912,642</td>
<td align="right">3,990,432,159</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">468,737,208</td>
<td align="right">545,605,130</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,462,525,170</td>
<td align="right">4,025,133,903</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">39,417,040,048</td>
<td align="right">45,756,336,977</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">34,974,808,705</td>
<td align="right">40,523,285,818</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">52,206,161</td>
<td align="right">60,306,141</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">38,985,371</td>
<td align="right">45,032,700</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">340,622,522</td>
<td align="right">392,972,932</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">3,872,755,487</td>
<td align="right">4,449,354,871</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,326,199,784</td>
<td align="right">1,508,391,601</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,326,374,399</td>
<td align="right">1,508,566,216</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">39,803,587</td>
<td align="right">45,261,150</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,735,782,851</td>
<td align="right">3,060,525,322</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,314,548,267</td>
<td align="right">1,464,521,684</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">5,851,003,076</td>
<td align="right">6,483,258,584</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">921,713,685</td>
<td align="right">1,008,039,485</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">6,700,112</td>
<td align="right">7,289,860</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">694,096,795</td>
<td align="right">750,651,503</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,222,597,924</td>
<td align="right">1,320,331,149</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,060,610,883</td>
<td align="right">1,142,178,834</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">7,929,685</td>
<td align="right">7,337,377</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,438,769,328</td>
<td align="right">7,963,811,072</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">97,194,562</td>
<td align="right">102,371,332</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">159,550,636</td>
<td align="right">167,670,307</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">294,110,242</td>
<td align="right">308,197,515</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">161,981,135</td>
<td align="right">155,264,215</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">169,660,189</td>
<td align="right">176,166,082</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">148,703,874</td>
<td align="right">154,396,901</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">424,077,104</td>
<td align="right">440,197,012</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,140,979,226</td>
<td align="right">2,221,027,405</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">577,035,487</td>
<td align="right">597,053,767</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">169,744,992</td>
<td align="right">175,559,884</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,283,775,591</td>
<td align="right">1,327,495,423</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,148,998,664</td>
<td align="right">1,187,116,776</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,388,477,906</td>
<td align="right">2,458,124,681</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">321,841,081</td>
<td align="right">331,026,408</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,793,279,091</td>
<td align="right">2,872,554,525</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">65,155,967</td>
<td align="right">66,977,720</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">34,521,547</td>
<td align="right">35,476,367</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">211,418,001</td>
<td align="right">217,258,365</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">30,495,173</td>
<td align="right">31,285,073</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">383,352,144</td>
<td align="right">393,258,282</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">423,331,233</td>
<td align="right">434,026,670</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">444,620,678</td>
<td align="right">455,387,703</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">444,620,678</td>
<td align="right">455,387,703</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">74,608,089</td>
<td align="right">76,357,217</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,217,334,171</td>
<td align="right">1,244,404,297</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,808,469,529</td>
<td align="right">1,846,762,502</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">731,690,696</td>
<td align="right">742,637,643</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,324,005</td>
<td align="right">3,366,565</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">117,628,956</td>
<td align="right">118,941,387</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,782,130,827</td>
<td align="right">1,801,353,716</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,113,203,855</td>
<td align="right">1,122,934,490</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">151,782,156</td>
<td align="right">153,094,587</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,691,619</td>
<td align="right">118,700,859</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">449,877,208</td>
<td align="right">446,028,364</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">450,671,251</td>
<td align="right">446,822,407</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">642,331,269</td>
<td align="right">647,555,343</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,172,461</td>
<td align="right">5,133,148</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">20,053</td>
<td align="right">20,173</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">49,132,694</td>
<td align="right">49,308,441</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">26,717,181</td>
<td align="right">26,805,073</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">19,934,332</td>
<td align="right">19,998,850</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">7,371,654</td>
<td align="right">7,348,414</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,992,203,188</td>
<td align="right">1,998,260,997</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">439,651,395</td>
<td align="right">440,933,507</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">358,545,837</td>
<td align="right">359,568,064</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">34,592,475</td>
<td align="right">34,681,571</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">310,730,367</td>
<td align="right">311,442,064</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,199,132,886</td>
<td align="right">1,200,911,715</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">469,143,550</td>
<td align="right">469,792,122</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">37,104,317</td>
<td align="right">37,152,077</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">923,231,096</td>
<td align="right">924,298,435</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">923,245,956</td>
<td align="right">924,313,295</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">101,340,685</td>
<td align="right">101,452,885</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,534,526</td>
<td align="right">43,582,286</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,065,928,677</td>
<td align="right">1,067,053,856</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">83,399,783</td>
<td align="right">83,482,983</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">57,308,502</td>
<td align="right">57,364,897</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">2,504,830,172</td>
<td align="right">2,507,262,465</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">416,282,892</td>
<td align="right">416,676,630</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">57,138,016</td>
<td align="right">57,188,810</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">156,182,010</td>
<td align="right">156,064,121</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,223,810,183</td>
<td align="right">1,224,636,231</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">101,185,545</td>
<td align="right">101,250,085</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">101,185,545</td>
<td align="right">101,250,085</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,909,861,114</td>
<td align="right">1,910,878,516</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">975,740,854</td>
<td align="right">976,237,154</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,266,418,899</td>
<td align="right">1,267,005,888</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">45,652,380</td>
<td align="right">45,671,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,278,515,434</td>
<td align="right">2,279,372,993</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">59,999,760</td>
<td align="right">60,013,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">983,243,135</td>
<td align="right">983,035,955</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,545,565</td>
<td align="right">1,545,301</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,754,178,166</td>
<td align="right">1,754,432,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">532,331,363</td>
<td align="right">532,388,698</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">601,191,838</td>
<td align="right">601,249,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">38,306,073</td>
<td align="right">38,308,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">445,747,579</td>
<td align="right">445,757,379</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">445,747,579</td>
<td align="right">445,757,379</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,345,868,714</td>
<td align="right">1,345,863,474</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,025,890</td>
<td align="right">40,025,746</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,940,465</td>
<td align="right">47,940,442</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">48,051,015</td>
<td align="right">48,050,992</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">78,980,988</td>
<td align="right">78,980,965</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,493</td>
<td align="right">70,350,487</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,493</td>
<td align="right">70,350,487</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">768,856,688</td>
<td align="right">768,856,688</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">585,072,289</td>
<td align="right">585,072,289</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">419,919,111</td>
<td align="right">419,919,111</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">358,301,634</td>
<td align="right">358,301,634</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">263,905,177</td>
<td align="right">263,905,177</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">143,590,077</td>
<td align="right">143,590,077</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">131,031,777</td>
<td align="right">131,031,777</td>
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
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,770,000</td>
<td align="right">73,770,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">55,838,776</td>
<td align="right">55,838,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">53,395,255</td>
<td align="right">53,395,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">53,395,255</td>
<td align="right">53,395,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,560</td>
<td align="right">47,660,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,079</td>
<td align="right">47,071,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,593,190</td>
<td align="right">46,593,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">30,896,592</td>
<td align="right">30,896,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">30,896,592</td>
<td align="right">30,896,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,548,091</td>
<td align="right">12,548,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,548,091</td>
<td align="right">12,548,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">8,323,320</td>
<td align="right">8,323,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">7,953,793</td>
<td align="right">7,953,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">5,718,540</td>
<td align="right">5,718,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">5,266,200</td>
<td align="right">5,266,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,635,678</td>
<td align="right">4,635,678</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">4,208,676</td>
<td align="right">4,208,676</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">3,709,046</td>
<td align="right">3,709,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right">3,555,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,253,140</td>
<td align="right">3,253,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">3,106,080</td>
<td align="right">3,106,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,034,740</td>
<td align="right">3,034,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,975,980</td>
<td align="right">2,975,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,975,980</td>
<td align="right">2,975,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,678,400</td>
<td align="right">2,678,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">356,340</td>
<td align="right">356,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">320,873</td>
<td align="right">320,873</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">229,826</td>
<td align="right">229,826</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">143,096</td>
<td align="right">143,096</td>
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
<td align="left">_SET_ADD</td>
<td align="right">62</td>
<td align="right">62</td>
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
<td align="right">23,231</td>
<td align="right">23,670</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,787</td>
<td align="right">1,789</td>
<td align="right">0.1%</td>
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
<td align="right">101</td>
<td align="right">101</td>
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
<td align="right">101</td>
<td align="right">101</td>
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
<td align="right">2,378</td>
<td align="right">2,397</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-05
