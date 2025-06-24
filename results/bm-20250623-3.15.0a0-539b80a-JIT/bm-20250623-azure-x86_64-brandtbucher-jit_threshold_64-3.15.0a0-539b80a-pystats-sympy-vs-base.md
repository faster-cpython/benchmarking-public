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
<td align="left">NOT_TAKEN</td>
<td align="right">198,593</td>
<td align="right">1,134,484</td>
<td align="right">471.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,941</td>
<td align="right">3,992</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">14,629</td>
<td align="right">8,067</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,759,216</td>
<td align="right">1,098,499</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">10,906,104</td>
<td align="right">7,568,098</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,514,204</td>
<td align="right">4,061,824</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">11,270,790</td>
<td align="right">9,042,805</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,550</td>
<td align="right">4,464</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,585,470</td>
<td align="right">1,294,412</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">9,212</td>
<td align="right">7,560</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,588,644</td>
<td align="right">2,153,140</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,474,333</td>
<td align="right">9,808,587</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">57,413,805</td>
<td align="right">49,165,569</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,585,317</td>
<td align="right">2,258,964</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">456,499</td>
<td align="right">400,777</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">57,832,562</td>
<td align="right">51,721,476</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,585,927</td>
<td align="right">4,132,974</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,484,791</td>
<td align="right">8,572,412</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">45,787,928</td>
<td align="right">41,389,498</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">22,351,155</td>
<td align="right">20,312,727</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">15,006,828</td>
<td align="right">13,719,200</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,899,591</td>
<td align="right">9,090,046</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">171,873,610</td>
<td align="right">159,299,310</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,529</td>
<td align="right">1,626,971</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">44,977,405</td>
<td align="right">41,738,246</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">55,354,897</td>
<td align="right">51,595,851</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">34,306,755</td>
<td align="right">31,987,106</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">32,098,217</td>
<td align="right">29,938,448</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">56,865,798</td>
<td align="right">53,107,449</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,490,465</td>
<td align="right">28,516,929</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">62,193,951</td>
<td align="right">58,245,195</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">23,247,582</td>
<td align="right">21,836,426</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,209</td>
<td align="right">2,067,467</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,910,963</td>
<td align="right">14,997,623</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,568,742</td>
<td align="right">14,704,069</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">18,017,125</td>
<td align="right">17,046,651</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,932,552</td>
<td align="right">8,451,825</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">44,764,461</td>
<td align="right">42,405,078</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,555,265</td>
<td align="right">1,474,361</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">51,451,116</td>
<td align="right">48,871,125</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">15,116,579</td>
<td align="right">14,441,692</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">79,528</td>
<td align="right">76,231</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">53,205,157</td>
<td align="right">51,021,600</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">15,881,542</td>
<td align="right">15,277,638</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">49,108,823</td>
<td align="right">47,322,787</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,038,343</td>
<td align="right">10,678,606</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,037</td>
<td align="right">11,648</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">62</td>
<td align="right">60</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">591</td>
<td align="right">572</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,130,481</td>
<td align="right">17,553,593</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">28,527,717</td>
<td align="right">29,432,340</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">67,315,167</td>
<td align="right">65,304,460</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">220,403,075</td>
<td align="right">213,848,580</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">144,124,840</td>
<td align="right">139,901,317</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">41,592,190</td>
<td align="right">40,385,360</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">745,351</td>
<td align="right">726,772</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">388,827</td>
<td align="right">379,223</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,594,435</td>
<td align="right">17,977,846</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,300</td>
<td align="right">1,260,638</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">85,986,838</td>
<td align="right">84,143,373</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">173,041,896</td>
<td align="right">169,387,923</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">36,902,792</td>
<td align="right">36,151,829</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">18,996,349</td>
<td align="right">19,379,631</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">13,247,370</td>
<td align="right">13,005,785</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">21,004,661</td>
<td align="right">20,622,550</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">38,717,078</td>
<td align="right">38,035,804</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,813,358</td>
<td align="right">6,696,956</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">239,255,729</td>
<td align="right">235,169,906</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">59,485,636</td>
<td align="right">58,488,900</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">44,878,276</td>
<td align="right">44,212,174</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,176,394</td>
<td align="right">4,120,916</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,856,285</td>
<td align="right">18,086,488</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,658,348</td>
<td align="right">21,382,867</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">624,173,212</td>
<td align="right">616,244,485</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">13,941,664</td>
<td align="right">13,769,310</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">39,233,185</td>
<td align="right">38,761,800</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,895,175</td>
<td align="right">59,213,302</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">48,073,996</td>
<td align="right">47,548,189</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,007</td>
<td align="right">996</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">199,135,599</td>
<td align="right">197,004,141</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">148,037,150</td>
<td align="right">146,501,324</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,418,372</td>
<td align="right">12,295,149</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">41,122</td>
<td align="right">40,759</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,221,870</td>
<td align="right">1,211,254</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,984</td>
<td align="right">2,959</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,883</td>
<td align="right">387,024</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,977,195</td>
<td align="right">5,933,598</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,645</td>
<td align="right">2,626</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">181,876,688</td>
<td align="right">180,647,049</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">43,276,238</td>
<td align="right">43,550,449</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">9,573,045</td>
<td align="right">9,512,963</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">9,662,085</td>
<td align="right">9,601,988</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,296,425</td>
<td align="right">74,865,302</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,618,033</td>
<td align="right">2,603,684</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,173</td>
<td align="right">18,081</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">17,494,885</td>
<td align="right">17,412,227</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">8,970</td>
<td align="right">9,008</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">7,105</td>
<td align="right">7,075</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,008,711</td>
<td align="right">2,000,858</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">598,535</td>
<td align="right">596,236</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">24,792,548</td>
<td align="right">24,699,375</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">33,137,871</td>
<td align="right">33,013,519</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">23,892</td>
<td align="right">23,807</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,444</td>
<td align="right">1,448</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">341,720</td>
<td align="right">340,875</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">7,924,007</td>
<td align="right">7,906,322</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,087,721</td>
<td align="right">8,070,040</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,705,486</td>
<td align="right">21,737,814</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,777,966</td>
<td align="right">9,763,757</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,743,134</td>
<td align="right">24,710,864</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,273</td>
<td align="right">175,048</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,007,590</td>
<td align="right">2,005,382</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,395</td>
<td align="right">141,287</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">89,009</td>
<td align="right">88,946</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">178,532</td>
<td align="right">178,406</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">178,534</td>
<td align="right">178,408</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">78,730,382</td>
<td align="right">78,686,108</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,631</td>
<td align="right">4,467,390</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,001,867</td>
<td align="right">4,000,133</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">172,048</td>
<td align="right">171,978</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">10,870,963</td>
<td align="right">10,867,479</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,985,357</td>
<td align="right">21,978,608</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">20,678</td>
<td align="right">20,684</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,728,104</td>
<td align="right">3,727,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,096</td>
<td align="right">83,112</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,921,018</td>
<td align="right">10,919,582</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,785,806</td>
<td align="right">6,785,036</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,301</td>
<td align="right">6,743,691</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,026,278</td>
<td align="right">6,026,810</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,524</td>
<td align="right">1,244,423</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,250</td>
<td align="right">4,497,578</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,028,989</td>
<td align="right">1,029,062</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,029,880</td>
<td align="right">1,029,953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,101</td>
<td align="right">655,147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,101</td>
<td align="right">655,147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,101</td>
<td align="right">655,147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,430</td>
<td align="right">654,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,446</td>
<td align="right">654,491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,940</td>
<td align="right">745,991</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,628,939</td>
<td align="right">18,630,195</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,589,892</td>
<td align="right">6,590,175</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,753,313</td>
<td align="right">5,753,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,788</td>
<td align="right">1,389,834</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,418,430</td>
<td align="right">2,418,504</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,541,384</td>
<td align="right">7,541,601</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,537</td>
<td align="right">427,548</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,300</td>
<td align="right">746,319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,623,035</td>
<td align="right">6,623,195</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,717</td>
<td align="right">165,713</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,329</td>
<td align="right">1,323,307</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,621</td>
<td align="right">942,636</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,031</td>
<td align="right">21,977,326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">2,995,451</td>
<td align="right">2,995,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">495,310</td>
<td align="right">495,311</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,431</td>
<td align="right">2,281,430</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,036,043</td>
<td align="right">1,036,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">372,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">270,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">133,724</td>
<td align="right">133,724</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">4,150</td>
<td align="right">4,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,679</td>
<td align="right">1,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,055</td>
<td align="right">1,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">447</td>
<td align="right">447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">394</td>
<td align="right">394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">255</td>
<td align="right">255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">133</td>
<td align="right">133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">102</td>
<td align="right">102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">92</td>
<td align="right">92</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">60,505</td>
<td align="right">0.1%</td>
<td align="right">46,153</td>
<td align="right">0.0%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">44,733,384</td>
<td align="right">38.6%</td>
<td align="right">42,375,510</td>
<td align="right">37.3%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">71,213,108</td>
<td align="right">61.4%</td>
<td align="right">71,178,606</td>
<td align="right">62.6%</td>
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
<td align="right">3,325</td>
<td align="right">10.3%</td>
<td align="right">2,993</td>
<td align="right">9.8%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">28,897</td>
<td align="right">89.7%</td>
<td align="right">27,446</td>
<td align="right">90.2%</td>
<td align="right">-5.0%</td>
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
<td align="right">422</td>
<td align="right">1.5%</td>
<td align="right">338</td>
<td align="right">1.2%</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,904</td>
<td align="right">13.5%</td>
<td align="right">3,180</td>
<td align="right">11.6%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">4,590</td>
<td align="right">15.9%</td>
<td align="right">4,106</td>
<td align="right">15.0%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,142</td>
<td align="right">7.4%</td>
<td align="right">2,046</td>
<td align="right">7.5%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">716</td>
<td align="right">2.5%</td>
<td align="right">693</td>
<td align="right">2.5%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">94</td>
<td align="right">0.3%</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">367</td>
<td align="right">1.3%</td>
<td align="right">358</td>
<td align="right">1.3%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">208</td>
<td align="right">0.7%</td>
<td align="right">211</td>
<td align="right">0.8%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">707</td>
<td align="right">2.4%</td>
<td align="right">699</td>
<td align="right">2.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,008</td>
<td align="right">3.5%</td>
<td align="right">1,017</td>
<td align="right">3.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">989</td>
<td align="right">3.4%</td>
<td align="right">982</td>
<td align="right">3.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,219</td>
<td align="right">4.2%</td>
<td align="right">1,211</td>
<td align="right">4.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">626</td>
<td align="right">2.2%</td>
<td align="right">622</td>
<td align="right">2.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">1,755</td>
<td align="right">6.1%</td>
<td align="right">1,749</td>
<td align="right">6.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,893</td>
<td align="right">10.0%</td>
<td align="right">2,885</td>
<td align="right">10.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,084</td>
<td align="right">3.8%</td>
<td align="right">1,086</td>
<td align="right">4.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">11.1%</td>
<td align="right">3,221</td>
<td align="right">11.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">7.7%</td>
<td align="right">2,225</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">570</td>
<td align="right">2.0%</td>
<td align="right">570</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.5%</td>
<td align="right">155</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr array</td>
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
<td align="right">12,037</td>
<td align="right">100.0%</td>
<td align="right">11,648</td>
<td align="right">100.0%</td>
<td align="right">-3.2%</td>
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
<td align="right">36,416,934</td>
<td align="right">11.6%</td>
<td align="right">36,805,276</td>
<td align="right">11.8%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">35,738,389</td>
<td align="right">11.4%</td>
<td align="right">36,119,351</td>
<td align="right">11.5%</td>
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
<td align="right">276,418,874</td>
<td align="right">88.4%</td>
<td align="right">276,293,512</td>
<td align="right">88.2%</td>
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
<td align="right">702,437</td>
<td align="right">100.0%</td>
<td align="right">709,732</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
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
<td align="right">3,185</td>
<td align="right">75.0%</td>
<td align="right">3,183</td>
<td align="right">74.8%</td>
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
<td align="right">2,805</td>
<td align="right">66.0%</td>
<td align="right">2,805</td>
<td align="right">66.0%</td>
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
<td align="right">1,064</td>
<td align="right">100.0%</td>
<td align="right">1,070</td>
<td align="right">100.0%</td>
<td align="right">0.6%</td>
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
<td align="right">30,451,778</td>
<td align="right">37.2%</td>
<td align="right">28,478,753</td>
<td align="right">35.6%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">412,606</td>
<td align="right">0.5%</td>
<td align="right">410,684</td>
<td align="right">0.5%</td>
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
<td align="right">51,041,320</td>
<td align="right">62.3%</td>
<td align="right">51,038,182</td>
<td align="right">63.8%</td>
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
<td align="right">37,513</td>
<td align="right">80.8%</td>
<td align="right">37,009</td>
<td align="right">80.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,903</td>
<td align="right">19.2%</td>
<td align="right">8,860</td>
<td align="right">19.3%</td>
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
<td align="left">bool</td>
<td align="right">1,463</td>
<td align="right">3.9%</td>
<td align="right">1,234</td>
<td align="right">3.3%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,465</td>
<td align="right">17.2%</td>
<td align="right">6,211</td>
<td align="right">16.8%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">135</td>
<td align="right">0.4%</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">114</td>
<td align="right">0.3%</td>
<td align="right">116</td>
<td align="right">0.3%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,237</td>
<td align="right">11.3%</td>
<td align="right">4,272</td>
<td align="right">11.5%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,205</td>
<td align="right">37.9%</td>
<td align="right">14,136</td>
<td align="right">38.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,141</td>
<td align="right">8.4%</td>
<td align="right">3,149</td>
<td align="right">8.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">19.9%</td>
<td align="right">7,480</td>
<td align="right">20.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">44</td>
<td align="right">0.1%</td>
<td align="right">44</td>
<td align="right">0.1%</td>
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
<td align="right">10,900,572</td>
<td align="right">31.7%</td>
<td align="right">7,563,420</td>
<td align="right">24.3%</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,500,438</td>
<td align="right">68.3%</td>
<td align="right">23,500,713</td>
<td align="right">75.6%</td>
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
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">1,020</td>
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
<td align="right">5,407</td>
<td align="right">97.7%</td>
<td align="right">4,553</td>
<td align="right">97.3%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">125</td>
<td align="right">2.3%</td>
<td align="right">125</td>
<td align="right">2.7%</td>
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
<td align="right">3,451</td>
<td align="right">63.8%</td>
<td align="right">2,635</td>
<td align="right">57.9%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">182</td>
<td align="right">3.4%</td>
<td align="right">159</td>
<td align="right">3.5%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">5.5%</td>
<td align="right">293</td>
<td align="right">6.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,475</td>
<td align="right">27.3%</td>
<td align="right">1,466</td>
<td align="right">32.2%</td>
<td align="right">-0.6%</td>
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
<td align="right">1,232,620</td>
<td align="right">1.1%</td>
<td align="right">894,895</td>
<td align="right">0.9%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45,735,985</td>
<td align="right">41.2%</td>
<td align="right">41,338,979</td>
<td align="right">40.0%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,054,264</td>
<td align="right">57.7%</td>
<td align="right">60,968,488</td>
<td align="right">59.0%</td>
<td align="right">-4.8%</td>
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
<td align="right">23,972</td>
<td align="right">31.9%</td>
<td align="right">17,598</td>
<td align="right">26.1%</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">51,140</td>
<td align="right">68.1%</td>
<td align="right">49,722</td>
<td align="right">73.9%</td>
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
<td align="left">list</td>
<td align="right">194</td>
<td align="right">0.4%</td>
<td align="right">150</td>
<td align="right">0.3%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,673</td>
<td align="right">5.2%</td>
<td align="right">2,440</td>
<td align="right">4.9%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">557</td>
<td align="right">1.1%</td>
<td align="right">512</td>
<td align="right">1.0%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.7%</td>
<td align="right">354</td>
<td align="right">0.7%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,339</td>
<td align="right">12.4%</td>
<td align="right">5,910</td>
<td align="right">11.9%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">38,522</td>
<td align="right">75.3%</td>
<td align="right">37,887</td>
<td align="right">76.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.5%</td>
<td align="right">756</td>
<td align="right">1.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,355</td>
<td align="right">2.6%</td>
<td align="right">1,353</td>
<td align="right">2.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">64</td>
<td align="right">0.1%</td>
<td align="right">64</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">24</td>
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
<td align="left">set</td>
<td align="right">7,185,887</td>
<td align="right">7,185,887 / 0 !!</td>
<td align="right">7,158,588</td>
<td align="right">7,158,588 / 0 !!</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">70,475</td>
<td align="right">70,475 / 0 !!</td>
<td align="right">70,501</td>
<td align="right">70,501 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">157,912</td>
<td align="right">157,912 / 0 !!</td>
<td align="right">157,939</td>
<td align="right">157,939 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,715,707</td>
<td align="right">8,715,707 / 0 !!</td>
<td align="right">8,716,099</td>
<td align="right">8,716,099 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">9,233,795</td>
<td align="right">9,233,795 / 0 !!</td>
<td align="right">9,233,892</td>
<td align="right">9,233,892 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,440,488</td>
<td align="right">9,440,488 / 0 !!</td>
<td align="right">9,440,563</td>
<td align="right">9,440,563 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,236,482</td>
<td align="right">12,236,482 / 0 !!</td>
<td align="right">12,236,550</td>
<td align="right">12,236,550 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6,028</td>
<td align="right">6,028 / 0 !!</td>
<td align="right">6,028</td>
<td align="right">6,028 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">443</td>
<td align="right">443 / 0 !!</td>
<td align="right">443</td>
<td align="right">443 / 0 !!</td>
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
<td align="right">52,697,835</td>
<td align="right">16.5%</td>
<td align="right">50,890,841</td>
<td align="right">16.3%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">206,806,498</td>
<td align="right">64.7%</td>
<td align="right">202,597,510</td>
<td align="right">64.8%</td>
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
<td align="right">59,834,924</td>
<td align="right">18.7%</td>
<td align="right">59,153,748</td>
<td align="right">18.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">1,005,140</td>
<td align="right">95.7%</td>
<td align="right">970,986</td>
<td align="right">95.6%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,035</td>
<td align="right">4.3%</td>
<td align="right">45,001</td>
<td align="right">4.4%</td>
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
<td align="left">builtin class method</td>
<td align="right">206</td>
<td align="right">0.5%</td>
<td align="right">242</td>
<td align="right">0.5%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,324</td>
<td align="right">5.2%</td>
<td align="right">2,360</td>
<td align="right">5.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,105</td>
<td align="right">6.9%</td>
<td align="right">3,057</td>
<td align="right">6.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,740</td>
<td align="right">6.1%</td>
<td align="right">2,718</td>
<td align="right">6.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">148</td>
<td align="right">0.3%</td>
<td align="right">147</td>
<td align="right">0.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,815</td>
<td align="right">15.1%</td>
<td align="right">6,770</td>
<td align="right">15.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,094</td>
<td align="right">6.9%</td>
<td align="right">3,099</td>
<td align="right">6.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,417</td>
<td align="right">47.6%</td>
<td align="right">21,419</td>
<td align="right">47.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,057</td>
<td align="right">9.0%</td>
<td align="right">4,057</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
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
<td align="right">260,465,324</td>
<td align="right">100.0%</td>
<td align="right">255,010,416</td>
<td align="right">100.0%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,601</td>
<td align="right">0.0%</td>
<td align="right">4,537</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,299</td>
<td align="right">0.0%</td>
<td align="right">1,299</td>
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
<td align="right">13,622</td>
<td align="right">100.0%</td>
<td align="right">13,594</td>
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
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,265,950</td>
<td align="right">100.0%</td>
<td align="right">2,265,943</td>
<td align="right">100.0%</td>
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
<td align="right">30</td>
<td align="right">100.0%</td>
<td align="right">30</td>
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
<td align="right">731,589</td>
<td align="right">72.0%</td>
<td align="right">731,608</td>
<td align="right">72.0%</td>
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
<td align="right">268,986</td>
<td align="right">26.5%</td>
<td align="right">268,986</td>
<td align="right">26.5%</td>
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
<td align="right">1.4%</td>
<td align="right">14,711</td>
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
<td align="left">Success</td>
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
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
<td align="left">list</td>
<td align="right">1,108</td>
<td align="right">100.0%</td>
<td align="right">1,108</td>
<td align="right">100.0%</td>
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
<td align="right">173,970</td>
<td align="right">1.9%</td>
<td align="right">173,729</td>
<td align="right">1.9%</td>
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
<td align="right">1,575,172</td>
<td align="right">17.3%</td>
<td align="right">1,576,007</td>
<td align="right">17.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,329,294</td>
<td align="right">80.7%</td>
<td align="right">7,328,700</td>
<td align="right">80.7%</td>
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
<td align="right">967</td>
<td align="right">3.1%</td>
<td align="right">983</td>
<td align="right">3.2%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">29,953</td>
<td align="right">96.9%</td>
<td align="right">29,970</td>
<td align="right">96.8%</td>
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
<td align="left">not managed dict</td>
<td align="right">294</td>
<td align="right">30.4%</td>
<td align="right">302</td>
<td align="right">30.7%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.6%</td>
<td align="right">518</td>
<td align="right">52.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">102</td>
<td align="right">10.5%</td>
<td align="right">102</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3</td>
<td align="right">0.3%</td>
<td align="right">3</td>
<td align="right">0.3%</td>
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
<td align="right">591</td>
<td align="right">100.0%</td>
<td align="right">572</td>
<td align="right">100.0%</td>
<td align="right">-3.2%</td>
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
<td align="right">2,583,196</td>
<td align="right">12.7%</td>
<td align="right">2,256,891</td>
<td align="right">11.3%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,738,844</td>
<td align="right">87.3%</td>
<td align="right">17,740,693</td>
<td align="right">88.7%</td>
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
<td align="right">1,543</td>
<td align="right">72.7%</td>
<td align="right">1,497</td>
<td align="right">72.2%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">578</td>
<td align="right">27.3%</td>
<td align="right">576</td>
<td align="right">27.8%</td>
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
<td align="right">1,543</td>
<td align="right">100.0%</td>
<td align="right">1,497</td>
<td align="right">100.0%</td>
<td align="right">-3.0%</td>
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
<td align="right">163,946,839</td>
<td align="right">94.0%</td>
<td align="right">162,765,306</td>
<td align="right">94.0%</td>
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
<td align="right">9,755,899</td>
<td align="right">5.6%</td>
<td align="right">9,741,689</td>
<td align="right">5.6%</td>
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
<td align="right">623,451</td>
<td align="right">0.4%</td>
<td align="right">623,628</td>
<td align="right">0.4%</td>
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
<td align="right">14,278</td>
<td align="right">42.9%</td>
<td align="right">14,290</td>
<td align="right">42.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,992</td>
<td align="right">57.1%</td>
<td align="right">18,982</td>
<td align="right">57.1%</td>
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
<td align="left">set</td>
<td align="right">715</td>
<td align="right">5.0%</td>
<td align="right">726</td>
<td align="right">5.1%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">722</td>
<td align="right">5.1%</td>
<td align="right">718</td>
<td align="right">5.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,266</td>
<td align="right">8.9%</td>
<td align="right">1,264</td>
<td align="right">8.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">7,991</td>
<td align="right">56.0%</td>
<td align="right">8,000</td>
<td align="right">56.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,615</td>
<td align="right">18.3%</td>
<td align="right">2,613</td>
<td align="right">18.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">6.2%</td>
<td align="right">883</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.6%</td>
<td align="right">84</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">6,273</td>
<td align="right">0.0%</td>
<td align="right">6,302</td>
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
<td align="right">83,631,433</td>
<td align="right">100.0%</td>
<td align="right">83,918,976</td>
<td align="right">100.0%</td>
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
<td align="left">Failure</td>
<td align="right">294</td>
<td align="right">10.9%</td>
<td align="right">315</td>
<td align="right">11.6%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,403</td>
<td align="right">89.1%</td>
<td align="right">2,391</td>
<td align="right">88.4%</td>
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
<td align="left">sequence</td>
<td align="right">251</td>
<td align="right">85.4%</td>
<td align="right">272</td>
<td align="right">86.3%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.6%</td>
<td align="right">43</td>
<td align="right">13.7%</td>
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
<td align="right">249,596,230</td>
<td align="right">5.8%</td>
<td align="right">235,837,568</td>
<td align="right">5.7%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,408,723,430</td>
<td align="right">32.9%</td>
<td align="right">1,359,651,320</td>
<td align="right">32.7%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,534,285,418</td>
<td align="right">59.1%</td>
<td align="right">2,473,789,470</td>
<td align="right">59.5%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">93,038,959</td>
<td align="right">2.2%</td>
<td align="right">91,267,325</td>
<td align="right">2.2%</td>
<td align="right">-1.9%</td>
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
<td align="right">10,900,572</td>
<td align="right">4.5%</td>
<td align="right">7,563,420</td>
<td align="right">3.3%</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,583,196</td>
<td align="right">1.1%</td>
<td align="right">2,256,891</td>
<td align="right">1.0%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">45,735,985</td>
<td align="right">19.0%</td>
<td align="right">41,338,979</td>
<td align="right">18.2%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,451,778</td>
<td align="right">12.7%</td>
<td align="right">28,478,753</td>
<td align="right">12.5%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">44,733,384</td>
<td align="right">18.6%</td>
<td align="right">42,375,510</td>
<td align="right">18.6%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,834,924</td>
<td align="right">24.9%</td>
<td align="right">59,153,748</td>
<td align="right">26.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,738,389</td>
<td align="right">14.9%</td>
<td align="right">36,119,351</td>
<td align="right">15.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,755,899</td>
<td align="right">4.1%</td>
<td align="right">9,741,689</td>
<td align="right">4.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">173,970</td>
<td align="right">0.1%</td>
<td align="right">173,729</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.1%</td>
<td align="right">268,986</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">12,829,510</td>
<td align="right">13.8%</td>
<td align="right">11,182,548</td>
<td align="right">12.3%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,242,611</td>
<td align="right">12.1%</td>
<td align="right">11,633,233</td>
<td align="right">12.7%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,931,428</td>
<td align="right">31.1%</td>
<td align="right">28,794,845</td>
<td align="right">31.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,208,197</td>
<td align="right">3.4%</td>
<td align="right">3,194,390</td>
<td align="right">3.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,574,393</td>
<td align="right">1.7%</td>
<td align="right">1,575,228</td>
<td align="right">1.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,151,785</td>
<td align="right">6.6%</td>
<td align="right">6,151,015</td>
<td align="right">6.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,706,614</td>
<td align="right">12.6%</td>
<td align="right">11,705,294</td>
<td align="right">12.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,523</td>
<td align="right">5.5%</td>
<td align="right">5,102,579</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,311,918</td>
<td align="right">7.9%</td>
<td align="right">7,311,989</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,574</td>
<td align="right">2.3%</td>
<td align="right">2,103,569</td>
<td align="right">2.3%</td>
<td align="right">-0.0%</td>
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
<td align="right">131,353,758</td>
<td align="right">62.5%</td>
<td align="right">131,690,397</td>
<td align="right">62.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,131,734</td>
<td align="right">19.6%</td>
<td align="right">41,086,863</td>
<td align="right">19.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,415,348</td>
<td align="right">35.9%</td>
<td align="right">75,370,922</td>
<td align="right">35.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,416,133</td>
<td align="right">35.9%</td>
<td align="right">75,371,707</td>
<td align="right">35.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">78,884,799</td>
<td align="right">37.5%</td>
<td align="right">78,840,523</td>
<td align="right">37.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">78,884,799</td>
<td align="right">37.5%</td>
<td align="right">78,840,523</td>
<td align="right">37.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,688,030</td>
<td align="right">89.3%</td>
<td align="right">187,596,987</td>
<td align="right">89.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">3,468,666</td>
<td align="right">1.6%</td>
<td align="right">3,468,816</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,347</td>
<td align="right">8.8%</td>
<td align="right">18,490,621</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,331,970</td>
<td align="right">4.4%</td>
<td align="right">9,332,046</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,174</td>
<td align="right">0.5%</td>
<td align="right">950,175</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">416</td>
<td align="right">0.0%</td>
<td align="right">416</td>
<td align="right">0.0%</td>
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
<td align="right">1,149,053</td>
<td align="right"></td>
<td align="right">978,670</td>
<td align="right"></td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">51,357,781</td>
<td align="right">1.3%</td>
<td align="right">48,414,872</td>
<td align="right">1.2%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,532,080</td>
<td align="right"></td>
<td align="right">2,670,136</td>
<td align="right"></td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,976</td>
<td align="right">0.0%</td>
<td align="right">9,193</td>
<td align="right">0.0%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,216,283,512</td>
<td align="right">35.3%</td>
<td align="right">1,241,663,851</td>
<td align="right">36.0%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,183,150,422</td>
<td align="right">34.3%</td>
<td align="right">1,159,863,926</td>
<td align="right">33.6%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,347,707,971</td>
<td align="right">34.3%</td>
<td align="right">1,373,559,633</td>
<td align="right">35.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,473,197,436</td>
<td align="right">37.5%</td>
<td align="right">1,449,339,708</td>
<td align="right">36.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">76,073,764</td>
<td align="right">2.2%</td>
<td align="right">75,021,388</td>
<td align="right">2.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,679,561</td>
<td align="right"></td>
<td align="right">3,647,200</td>
<td align="right"></td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">149,720,089</td>
<td align="right"></td>
<td align="right">150,179,348</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,055,503,984</td>
<td align="right">26.9%</td>
<td align="right">1,058,251,999</td>
<td align="right">26.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">972,549,789</td>
<td align="right">28.2%</td>
<td align="right">974,636,715</td>
<td align="right">28.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">762,819</td>
<td align="right">0.2%</td>
<td align="right">763,673</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">128,313,042</td>
<td align="right">26.6%</td>
<td align="right">128,253,065</td>
<td align="right">26.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">129,084,837</td>
<td align="right">26.8%</td>
<td align="right">129,025,931</td>
<td align="right">26.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,738,910</td>
<td align="right"></td>
<td align="right">141,680,217</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">249,099,301</td>
<td align="right"></td>
<td align="right">249,195,860</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">352,515,853</td>
<td align="right">73.2%</td>
<td align="right">352,473,797</td>
<td align="right">73.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">352,550,691</td>
<td align="right"></td>
<td align="right">352,508,632</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,231</td>
<td align="right"></td>
<td align="right">866,307</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">2</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,897</td>
<td align="right">10.1%</td>
<td align="right">9,857</td>
<td align="right">22.2%</td>
<td align="right">419.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">112</td>
<td align="right">0.6%</td>
<td align="right">387</td>
<td align="right">0.9%</td>
<td align="right">245.5%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">153</td>
<td align="right">0.8%</td>
<td align="right">375</td>
<td align="right">0.8%</td>
<td align="right">145.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,872</td>
<td align="right">9.9%</td>
<td align="right">4,454</td>
<td align="right">10.0%</td>
<td align="right">137.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">18,816</td>
<td align="right"></td>
<td align="right">44,372</td>
<td align="right"></td>
<td align="right">135.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">5,872</td>
<td align="right">31.2%</td>
<td align="right">13,459</td>
<td align="right">30.3%</td>
<td align="right">129.2%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">9,175</td>
<td align="right">48.8%</td>
<td align="right">16,602</td>
<td align="right">37.4%</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">49,375,463</td>
<td align="right"></td>
<td align="right">69,540,949</td>
<td align="right"></td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,614,179,881</td>
<td align="right">3,269.2%</td>
<td align="right">2,008,393,034</td>
<td align="right">2,888.1%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">129</td>
<td align="right">0.3%</td>
<td align="right">129 / 0 !!</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">68</td>
<td align="right">0.7%</td>
<td align="right">68 / 0 !!</td>
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
<td align="right">1,897</td>
<td align="right"></td>
<td align="right">9,857</td>
<td align="right"></td>
<td align="right">419.6%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,731</td>
<td align="right">91.2%</td>
<td align="right">8,429</td>
<td align="right">85.5%</td>
<td align="right">386.9%</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">94,208</td>
<td align="right">0.6%</td>
<td align="right">61,517,824</td>
<td align="right">82.9%</td>
<td align="right">65,200.0%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">3,490,963</td>
<td align="right">22.7%</td>
<td align="right">17,614,916</td>
<td align="right">23.7%</td>
<td align="right">404.6%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">15,360,000</td>
<td align="right"></td>
<td align="right">74,211,328</td>
<td align="right"></td>
<td align="right">383.1%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">11,518,845</td>
<td align="right">75.0%</td>
<td align="right">54,943,236</td>
<td align="right">74.0%</td>
<td align="right">377.0%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">350,192</td>
<td align="right">2.3%</td>
<td align="right">1,653,176</td>
<td align="right">2.2%</td>
<td align="right">372.1%</td>
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
<td align="left">493</td>
<td align="right">28.5%</td>
<td align="left">2,571</td>
<td align="right">30.5%</td>
<td align="right">421.5%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">848</td>
<td align="right">49.0%</td>
<td align="left">3,740</td>
<td align="right">44.4%</td>
<td align="right">341.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">345</td>
<td align="right">19.9%</td>
<td align="left">1,792</td>
<td align="right">21.3%</td>
<td align="right">419.4%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">45</td>
<td align="right">2.6%</td>
<td align="left">326</td>
<td align="right">3.9%</td>
<td align="right">624.4%</td>
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
<td align="right">67</td>
<td align="right">3.5%</td>
<td align="right">574</td>
<td align="right">5.8%</td>
<td align="right">756.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">223</td>
<td align="right">11.8%</td>
<td align="right">1,432</td>
<td align="right">14.5%</td>
<td align="right">542.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">390</td>
<td align="right">20.6%</td>
<td align="right">1,371</td>
<td align="right">13.9%</td>
<td align="right">251.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">830</td>
<td align="right">43.8%</td>
<td align="right">4,031</td>
<td align="right">40.9%</td>
<td align="right">385.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">321</td>
<td align="right">16.9%</td>
<td align="right">1,714</td>
<td align="right">17.4%</td>
<td align="right">434.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">45</td>
<td align="right">2.4%</td>
<td align="right">605</td>
<td align="right">6.1%</td>
<td align="right">1,244.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">21</td>
<td align="right">1.1%</td>
<td align="right">130</td>
<td align="right">1.3%</td>
<td align="right">519.0%</td>
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
<td align="right">45</td>
<td align="right">2.4%</td>
<td align="right">568</td>
<td align="right">5.8%</td>
<td align="right">1,162.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">130</td>
<td align="right">6.9%</td>
<td align="right">796</td>
<td align="right">8.1%</td>
<td align="right">512.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">181</td>
<td align="right">9.5%</td>
<td align="right">978</td>
<td align="right">9.9%</td>
<td align="right">440.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">924</td>
<td align="right">48.7%</td>
<td align="right">3,527</td>
<td align="right">35.8%</td>
<td align="right">281.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">192</td>
<td align="right">10.1%</td>
<td align="right">1,620</td>
<td align="right">16.4%</td>
<td align="right">743.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">238</td>
<td align="right">12.5%</td>
<td align="right">811</td>
<td align="right">8.2%</td>
<td align="right">240.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">1.1%</td>
<td align="right">129</td>
<td align="right">1.3%</td>
<td align="right">514.3%</td>
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
<td align="left">_COMPARE_OP</td>
<td align="right">1,286</td>
<td align="right">1,900,889</td>
<td align="right">147,714.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">7,664</td>
<td align="right">2,497,434</td>
<td align="right">32,486.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">28,192</td>
<td align="right">550,582</td>
<td align="right">1,853.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">479,967</td>
<td align="right">1,682.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">28,192</td>
<td align="right">463,829</td>
<td align="right">1,545.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">8,561</td>
<td align="right">133,651</td>
<td align="right">1,461.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">52,447</td>
<td align="right">713,026</td>
<td align="right">1,259.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">73,352</td>
<td align="right">988,548</td>
<td align="right">1,247.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">144,184</td>
<td align="right">1,792,278</td>
<td align="right">1,143.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">128,958</td>
<td align="right">1,524,200</td>
<td align="right">1,081.9%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,166</td>
<td align="right">60,990</td>
<td align="right">1,080.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">283,254</td>
<td align="right">3,326,316</td>
<td align="right">1,074.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">45,128</td>
<td align="right">526,862</td>
<td align="right">1,067.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">45,128</td>
<td align="right">526,862</td>
<td align="right">1,067.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">5,306</td>
<td align="right">60,822</td>
<td align="right">1,046.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">35,660</td>
<td align="right">381,939</td>
<td align="right">971.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">90,320</td>
<td align="right">900,574</td>
<td align="right">897.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">18,228</td>
<td align="right">135,075</td>
<td align="right">641.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">174,242</td>
<td align="right">1,037,451</td>
<td align="right">495.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,096</td>
<td align="right">18,224</td>
<td align="right">488.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,384</td>
<td align="right">25,652</td>
<td align="right">247.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,072,551</td>
<td align="right">3,274,416</td>
<td align="right">205.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,278,748</td>
<td align="right">3,903,023</td>
<td align="right">205.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,278,748</td>
<td align="right">3,903,023</td>
<td align="right">205.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">3,159,428</td>
<td align="right">9,322,597</td>
<td align="right">195.1%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,437,889</td>
<td align="right">3,925,080</td>
<td align="right">173.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,437,889</td>
<td align="right">3,925,080</td>
<td align="right">173.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,437,889</td>
<td align="right">3,925,080</td>
<td align="right">173.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,437,889</td>
<td align="right">3,873,251</td>
<td align="right">169.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,089,181</td>
<td align="right">8,023,594</td>
<td align="right">159.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">272,856</td>
<td align="right">705,252</td>
<td align="right">158.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">1,437,889</td>
<td align="right">3,637,737</td>
<td align="right">153.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">2,040,956</td>
<td align="right">5,123,360</td>
<td align="right">151.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">5,392,961</td>
<td align="right">12,807,727</td>
<td align="right">137.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,078,895</td>
<td align="right">2,533,714</td>
<td align="right">134.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">833,316</td>
<td align="right">1,896,472</td>
<td align="right">127.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">5,924,764</td>
<td align="right">11,884,154</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,060,711</td>
<td align="right">2,031,112</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,489,505</td>
<td align="right">4,675,608</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">1,038,997</td>
<td align="right">1,910,638</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">1,038,997</td>
<td align="right">1,910,482</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">10,171,466</td>
<td align="right">18,316,581</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,286</td>
<td align="right">2,177</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,391,040</td>
<td align="right">3,982,088</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">3,340,640</td>
<td align="right">5,501,763</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,308,890</td>
<td align="right">5,449,043</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">21,523,073</td>
<td align="right">33,849,691</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">6,521,198</td>
<td align="right">9,781,801</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">2,117,815</td>
<td align="right">3,044,454</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,695,291</td>
<td align="right">2,424,274</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">9,881,491</td>
<td align="right">14,015,220</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">2,279,123</td>
<td align="right">3,224,126</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">2,888,400</td>
<td align="right">4,068,531</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">49,375,463</td>
<td align="right">69,540,949</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">49,375,463</td>
<td align="right">69,489,149</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,878,868</td>
<td align="right">5,423,186</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,567,853</td>
<td align="right">2,172,091</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,567,853</td>
<td align="right">2,172,091</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">5,198,825</td>
<td align="right">7,147,292</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,828,629</td>
<td align="right">2,503,735</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">3,186,680</td>
<td align="right">4,360,299</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">13,603,601</td>
<td align="right">18,215,198</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">6,746,317</td>
<td align="right">8,888,339</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,168,941</td>
<td align="right">2,808,429</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">7,404,641</td>
<td align="right">9,518,971</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">10,901,646</td>
<td align="right">13,982,516</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">3,350,452</td>
<td align="right">4,238,141</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">89,582,273</td>
<td align="right">111,402,419</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">24,552,984</td>
<td align="right">30,320,312</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,202,579</td>
<td align="right">3,948,383</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">11,842,500</td>
<td align="right">14,570,317</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">6,571,075</td>
<td align="right">8,029,717</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,618,348</td>
<td align="right">1,966,360</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">335,937,999</td>
<td align="right">406,887,650</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,209,502</td>
<td align="right">2,635,059</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">1,062,578</td>
<td align="right">1,264,253</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">302,233,317</td>
<td align="right">359,336,082</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,125,156</td>
<td align="right">2,508,303</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">5,037,101</td>
<td align="right">5,926,305</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">7,684,078</td>
<td align="right">9,020,316</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,125,156</td>
<td align="right">2,485,122</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">31,088,347</td>
<td align="right">35,989,829</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">6,284,426</td>
<td align="right">7,250,418</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">26,846,841</td>
<td align="right">30,921,032</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">26,846,841</td>
<td align="right">30,893,447</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">35,960,360</td>
<td align="right">40,810,673</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">80,313,440</td>
<td align="right">91,078,692</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">4,040,143</td>
<td align="right">4,566,790</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">25,998,628</td>
<td align="right">29,336,082</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,449,404</td>
<td align="right">2,740,605</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">6,129,265</td>
<td align="right">6,774,108</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">26,119,811</td>
<td align="right">28,613,225</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,325,246</td>
<td align="right">9,115,092</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">12,121,268</td>
<td align="right">13,242,866</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">12,121,268</td>
<td align="right">13,242,866</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">29,727,981</td>
<td align="right">32,191,704</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">17,907,726</td>
<td align="right">19,360,370</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">26,119,811</td>
<td align="right">28,144,385</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">22,438,675</td>
<td align="right">23,980,377</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">5,071,993</td>
<td align="right">5,347,653</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,763,661</td>
<td align="right">1,855,161</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,066,687</td>
<td align="right">5,308,393</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,763,661</td>
<td align="right">1,841,763</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,437,889</td>
<td align="right">1,499,195</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,437,889</td>
<td align="right">1,498,938</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">40,206,810</td>
<td align="right">41,861,470</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">26,124,922</td>
<td align="right">27,135,426</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">12,360,922</td>
<td align="right">11,961,058</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">1,437,889</td>
<td align="right">1,480,419</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,437,889</td>
<td align="right">1,480,419</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,437,889</td>
<td align="right">1,480,419</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,437,889</td>
<td align="right">1,480,419</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">32,537,659</td>
<td align="right">32,623,671</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,790,925</td>
<td align="right">15,811,773</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,513,496</td>
<td align="right">2,514,647</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right"></td>
<td align="right">2,441,413</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right"></td>
<td align="right">2,434,603</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right"></td>
<td align="right">2,426,142</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">1,156,173</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">326,371</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">127,694</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">127,551</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">48,026</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right"></td>
<td align="right">33,506</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right"></td>
<td align="right">27,648</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right"></td>
<td align="right">16,390</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">14,939</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">14,217</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right"></td>
<td align="right">10,821</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">9,604</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right"></td>
<td align="right">8,127</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">7,968</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right"></td>
<td align="right">7,931</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">6,990</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right"></td>
<td align="right">6,562</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">4,949</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">3,969</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">3,774</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">3,308</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">2,878</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right"></td>
<td align="right">2,816</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">2,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right"></td>
<td align="right">2,572</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">2,292</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">2,292</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">2,216</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right"></td>
<td align="right">1,864</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right"></td>
<td align="right">1,652</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right">1,524</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_TUPLE_1</td>
<td align="right"></td>
<td align="right">1,437</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right"></td>
<td align="right">1,437</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right"></td>
<td align="right">1,159</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">1,115</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right">1,086</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">845</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">719</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">656</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">410</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">389</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">333</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">270</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">106</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">105</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right"></td>
<td align="right">88</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">82</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right"></td>
<td align="right">82</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">82</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right"></td>
<td align="right">67</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">63</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right"></td>
<td align="right">41</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right"></td>
<td align="right">41</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">19</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right"></td>
<td align="right">19</td>
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
<td align="left">SEND</td>
<td align="right">21</td>
<td align="right">66</td>
<td align="right">214.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">565</td>
<td align="right">1,723</td>
<td align="right">205.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,480</td>
<td align="right">3,393</td>
<td align="right">129.3%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">238</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-24
