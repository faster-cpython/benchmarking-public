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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,834,163</td>
<td align="right">12,929,841</td>
<td align="right">356.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,548,257</td>
<td align="right">4,094</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">1,546,023</td>
<td align="right">4,095</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">828,667</td>
<td align="right">4,958</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">64,640,710</td>
<td align="right">642,357</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,563,450</td>
<td align="right">19,107</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,565,454</td>
<td align="right">21,096</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">66,987,660</td>
<td align="right">1,072,011</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">142,125</td>
<td align="right">12,837</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">146,226</td>
<td align="right">16,781</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">81,314,272</td>
<td align="right">12,659,515</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">84,451,588</td>
<td align="right">15,610,918</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">101,133,787</td>
<td align="right">28,180,939</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">2,862,774</td>
<td align="right">862,163</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">119,247,150</td>
<td align="right">43,169,730</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,554,535</td>
<td align="right">710,619</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">9,060,370</td>
<td align="right">4,264,996</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,102,848</td>
<td align="right">1,478,802</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,842,976</td>
<td align="right">1,412,684</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,425,136</td>
<td align="right">709,853</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">778,633</td>
<td align="right">388,209</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">10,984,136</td>
<td align="right">6,384,430</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,175,498</td>
<td align="right">731,525</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">6,205,709</td>
<td align="right">3,883,710</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,558,515</td>
<td align="right">6,048,115</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">10,865,572</td>
<td align="right">6,963,824</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">23,395,784</td>
<td align="right">15,155,561</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">23,406,480</td>
<td align="right">15,165,790</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">27,540,986</td>
<td align="right">17,982,771</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">176</td>
<td align="right">236</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">138,899,032</td>
<td align="right">98,089,107</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">35,572,043</td>
<td align="right">25,398,165</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">5,823,732</td>
<td align="right">4,201,030</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">11,661,938</td>
<td align="right">8,426,276</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">13,599,526</td>
<td align="right">9,862,312</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">28,429,799</td>
<td align="right">20,646,506</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,447</td>
<td align="right">1,052</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">396,090,879</td>
<td align="right">291,389,364</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">10,871,720</td>
<td align="right">8,011,287</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">99,444,988</td>
<td align="right">73,668,854</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">53,564,451</td>
<td align="right">40,170,576</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">139,568,995</td>
<td align="right">105,743,460</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">141,679,904</td>
<td align="right">108,018,695</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">6,872,425</td>
<td align="right">5,245,926</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">22,770,236</td>
<td align="right">17,390,251</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">53,446,104</td>
<td align="right">40,908,645</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21,357,070</td>
<td align="right">16,355,100</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,711,300</td>
<td align="right">4,409,018</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">21,846,964</td>
<td align="right">16,898,863</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">44,885,873</td>
<td align="right">35,094,107</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,986</td>
<td align="right">3,129</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">3,438</td>
<td align="right">2,713</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">7,996</td>
<td align="right">6,344</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">10,246,823</td>
<td align="right">8,177,692</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">41,642,465</td>
<td align="right">33,451,398</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">39,218,947</td>
<td align="right">31,673,531</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,408,065</td>
<td align="right">3,564,109</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,821</td>
<td align="right">2,293</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">17,350,312</td>
<td align="right">14,363,139</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">390,831</td>
<td align="right">325,127</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">4,269,889</td>
<td align="right">3,554,106</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,270,280</td>
<td align="right">3,554,494</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">390,982</td>
<td align="right">325,461</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,701,632</td>
<td align="right">8,076,372</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">9,318,762</td>
<td align="right">7,757,644</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">4,269,333</td>
<td align="right">3,554,200</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,270,190</td>
<td align="right">3,555,111</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,317,193</td>
<td align="right">7,756,972</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">9,323,467</td>
<td align="right">7,762,232</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,874,561</td>
<td align="right">14,882,889</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,051,153</td>
<td align="right">4,205,974</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">390,552</td>
<td align="right">325,214</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">392,552</td>
<td align="right">326,885</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">391,766</td>
<td align="right">326,237</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,843,087</td>
<td align="right">10,697,014</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,237,228</td>
<td align="right">11,025,724</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,282,099</td>
<td align="right">3,566,737</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,672,429</td>
<td align="right">3,892,036</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">391,315</td>
<td align="right">326,230</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,146</td>
<td align="right">3,666</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">406,113</td>
<td align="right">340,514</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">406,137</td>
<td align="right">340,617</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">845</td>
<td align="right">711</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">420</td>
<td align="right">355</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,315</td>
<td align="right">1,112</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">510,074</td>
<td align="right">443,063</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,829</td>
<td align="right">1,629</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,855</td>
<td align="right">1,655</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,561</td>
<td align="right">4,071</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,065</td>
<td align="right">1,856</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,891</td>
<td align="right">2,616</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,542</td>
<td align="right">1,404</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,542</td>
<td align="right">1,404</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">614</td>
<td align="right">668</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">15,073</td>
<td align="right">13,800</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,971</td>
<td align="right">1,826</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,476</td>
<td align="right">2,332</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,956</td>
<td align="right">6,289</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">12,180,739</td>
<td align="right">11,530,574</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">10,171</td>
<td align="right">9,751</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">18,141</td>
<td align="right">17,433</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,966</td>
<td align="right">4,790</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12,562</td>
<td align="right">12,151</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">65</td>
<td align="right">64</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">993</td>
<td align="right">978</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">665</td>
<td align="right">658</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">196</td>
<td align="right">194</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">300</td>
<td align="right">297</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">654</td>
<td align="right">648</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">460</td>
<td align="right">456</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">466</td>
<td align="right">462</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,283</td>
<td align="right">1,272</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">7,345</td>
<td align="right">7,286</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">129</td>
<td align="right">128</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">260</td>
<td align="right">258</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">782</td>
<td align="right">776</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">262</td>
<td align="right">260</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,410</td>
<td align="right">3,384</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3,422</td>
<td align="right">3,396</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3,422</td>
<td align="right">3,396</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3,422</td>
<td align="right">3,396</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">264</td>
<td align="right">262</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,559</td>
<td align="right">3,534</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">128,903</td>
<td align="right">129,741</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">129,465</td>
<td align="right">130,296</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,876</td>
<td align="right">1,864</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">129,619</td>
<td align="right">130,445</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">157</td>
<td align="right">156</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">323</td>
<td align="right">321</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">175</td>
<td align="right">174</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,443</td>
<td align="right">3,424</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,598</td>
<td align="right">2,585</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,752</td>
<td align="right">3,770</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">638</td>
<td align="right">635</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">857</td>
<td align="right">853</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,452</td>
<td align="right">1,446</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,586</td>
<td align="right">1,580</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">10,879,113</td>
<td align="right">10,879,104</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">388</td>
<td align="right">388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">258</td>
<td align="right">258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">186</td>
<td align="right">186</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">98</td>
<td align="right">98</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">70</td>
<td align="right">70</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">36</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">31</td>
<td align="right">31</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">22</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">18</td>
<td align="right">18</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">18</td>
<td align="right">18</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE_KNOWN</td>
<td align="right"></td>
<td align="right">48,710,936</td>
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
<td align="right">46,316,333</td>
<td align="right">99.1%</td>
<td align="right">37,344,954</td>
<td align="right">99.1%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">404,586</td>
<td align="right">0.9%</td>
<td align="right">338,939</td>
<td align="right">0.9%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
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
<td align="right">343</td>
<td align="right">22.5%</td>
<td align="right">363</td>
<td align="right">23.0%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,184</td>
<td align="right">77.5%</td>
<td align="right">1,212</td>
<td align="right">77.0%</td>
<td align="right">2.4%</td>
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
<td align="left">add other</td>
<td align="right">115</td>
<td align="right">9.7%</td>
<td align="right">132</td>
<td align="right">10.9%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">347</td>
<td align="right">29.3%</td>
<td align="right">364</td>
<td align="right">30.0%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">111</td>
<td align="right">9.4%</td>
<td align="right">109</td>
<td align="right">9.0%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">171</td>
<td align="right">14.4%</td>
<td align="right">169</td>
<td align="right">13.9%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">311</td>
<td align="right">26.3%</td>
<td align="right">309</td>
<td align="right">25.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">129</td>
<td align="right">10.9%</td>
<td align="right">129</td>
<td align="right">10.6%</td>
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
<td align="right">1,586</td>
<td align="right">100.0%</td>
<td align="right">1,580</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">86,876,771</td>
<td align="right">100.0%</td>
<td align="right">68,798,300</td>
<td align="right">100.0%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,029</td>
<td align="right">0.0%</td>
<td align="right">3,996</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,739</td>
<td align="right">0.0%</td>
<td align="right">5,698</td>
<td align="right">0.0%</td>
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
<td align="left">Success</td>
<td align="right">4,246</td>
<td align="right">100.0%</td>
<td align="right">4,587</td>
<td align="right">100.0%</td>
<td align="right">8.0%</td>
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
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">2,000.0%</td>
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
<td align="right">28</td>
<td align="right">15.9%</td>
<td align="right">28</td>
<td align="right">11.9%</td>
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
<td align="right">148</td>
<td align="right">100.0%</td>
<td align="right">208</td>
<td align="right">100.0%</td>
<td align="right">40.5%</td>
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
<td align="right">1,424,383</td>
<td align="right">47.6%</td>
<td align="right">709,274</td>
<td align="right">47.4%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,566,040</td>
<td align="right">52.4%</td>
<td align="right">785,717</td>
<td align="right">52.5%</td>
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
<td align="right">10</td>
<td align="right">0.0%</td>
<td align="right">10</td>
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
<td align="right">577</td>
<td align="right">76.6%</td>
<td align="right">403</td>
<td align="right">69.6%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">176</td>
<td align="right">23.4%</td>
<td align="right">176</td>
<td align="right">30.4%</td>
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
<td align="left">different types</td>
<td align="right">440</td>
<td align="right">76.3%</td>
<td align="right">266</td>
<td align="right">66.0%</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">93</td>
<td align="right">16.1%</td>
<td align="right">93</td>
<td align="right">23.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">7.5%</td>
<td align="right">43</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,889,604</td>
<td align="right">100.0%</td>
<td align="right">5,614,295</td>
<td align="right">99.9%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,216</td>
<td align="right">0.0%</td>
<td align="right">3,191</td>
<td align="right">0.1%</td>
<td align="right">-0.8%</td>
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
<td align="right">8</td>
<td align="right">2.3%</td>
<td align="right">8</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">335</td>
<td align="right">97.7%</td>
<td align="right">335</td>
<td align="right">97.7%</td>
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
<td align="left">str</td>
<td align="right">202</td>
<td align="right">60.3%</td>
<td align="right">202</td>
<td align="right">60.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">90</td>
<td align="right">26.9%</td>
<td align="right">90</td>
<td align="right">26.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">12.8%</td>
<td align="right">43</td>
<td align="right">12.8%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,954</td>
<td align="right">0.0%</td>
<td align="right">267,598</td>
<td align="right">0.4%</td>
<td align="right">3,264.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11,657,822</td>
<td align="right">12.4%</td>
<td align="right">8,423,003</td>
<td align="right">11.7%</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">82,254,096</td>
<td align="right">87.6%</td>
<td align="right">63,277,778</td>
<td align="right">87.9%</td>
<td align="right">-23.1%</td>
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
<td align="right">207</td>
<td align="right">4.9%</td>
<td align="right">5,032</td>
<td align="right">61.3%</td>
<td align="right">2,330.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,024</td>
<td align="right">95.1%</td>
<td align="right">3,180</td>
<td align="right">38.7%</td>
<td align="right">-21.0%</td>
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
<td align="left">itertools</td>
<td align="right">492</td>
<td align="right">12.2%</td>
<td align="right">105</td>
<td align="right">3.3%</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">43</td>
<td align="right">1.1%</td>
<td align="right">22</td>
<td align="right">0.7%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,354</td>
<td align="right">33.6%</td>
<td align="right">1,117</td>
<td align="right">35.1%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1,846</td>
<td align="right">45.9%</td>
<td align="right">1,651</td>
<td align="right">51.9%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">56</td>
<td align="right">1.4%</td>
<td align="right">53</td>
<td align="right">1.7%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">118</td>
<td align="right">2.9%</td>
<td align="right">117</td>
<td align="right">3.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">91</td>
<td align="right">2.3%</td>
<td align="right">91</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">24</td>
<td align="right">0.6%</td>
<td align="right">24</td>
<td align="right">0.8%</td>
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
<td align="right">12,835,469</td>
<td align="right">21.7%</td>
<td align="right">10,689,334</td>
<td align="right">21.4%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">46,409,989</td>
<td align="right">78.3%</td>
<td align="right">39,317,922</td>
<td align="right">78.6%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,211</td>
<td align="right">0.0%</td>
<td align="right">4,181</td>
<td align="right">0.0%</td>
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
<td align="left">Success</td>
<td align="right">2,770</td>
<td align="right">37.3%</td>
<td align="right">3,410</td>
<td align="right">45.6%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,647</td>
<td align="right">62.7%</td>
<td align="right">4,070</td>
<td align="right">54.4%</td>
<td align="right">-12.4%</td>
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
<td align="left">class method obj</td>
<td align="right">3,339</td>
<td align="right">71.9%</td>
<td align="right">2,816</td>
<td align="right">69.2%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">922</td>
<td align="right">19.8%</td>
<td align="right">874</td>
<td align="right">21.5%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">50</td>
<td align="right">1.1%</td>
<td align="right">48</td>
<td align="right">1.2%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">102</td>
<td align="right">2.2%</td>
<td align="right">100</td>
<td align="right">2.5%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">143</td>
<td align="right">3.1%</td>
<td align="right">142</td>
<td align="right">3.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">167,996,907</td>
<td align="right">100.0%</td>
<td align="right">126,388,106</td>
<td align="right">100.0%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,887</td>
<td align="right">0.0%</td>
<td align="right">1,860</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">500</td>
<td align="right">0.0%</td>
<td align="right">500</td>
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
<td align="right">2,646</td>
<td align="right">100.0%</td>
<td align="right">3,166</td>
<td align="right">100.0%</td>
<td align="right">19.7%</td>
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
<td align="right">264</td>
<td align="right">98.5%</td>
<td align="right">262</td>
<td align="right">98.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">2</td>
<td align="right">0.8%</td>
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
<td align="right">2</td>
<td align="right">100.0%</td>
<td align="right">2</td>
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
<td align="right">1,958</td>
<td align="right">7.3%</td>
<td align="right">1,813</td>
<td align="right">7.0%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,107</td>
<td align="right">86.0%</td>
<td align="right">22,223</td>
<td align="right">85.5%</td>
<td align="right">-3.8%</td>
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
<td align="right">1,312</td>
<td align="right">73.1%</td>
<td align="right">1,492</td>
<td align="right">76.2%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">482</td>
<td align="right">26.9%</td>
<td align="right">465</td>
<td align="right">23.8%</td>
<td align="right">-3.5%</td>
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
<td align="right">330</td>
<td align="right">68.5%</td>
<td align="right">315</td>
<td align="right">67.7%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">130</td>
<td align="right">27.0%</td>
<td align="right">128</td>
<td align="right">27.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">22</td>
<td align="right">4.6%</td>
<td align="right">22</td>
<td align="right">4.7%</td>
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
<td align="right">262</td>
<td align="right">100.0%</td>
<td align="right">260</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">4,271,765</td>
<td align="right">100.0%</td>
<td align="right">3,555,970</td>
<td align="right">100.0%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36</td>
<td align="right">0.0%</td>
<td align="right">36</td>
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
<td align="right">32</td>
<td align="right">94.1%</td>
<td align="right">32</td>
<td align="right">94.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2</td>
<td align="right">5.9%</td>
<td align="right">2</td>
<td align="right">5.9%</td>
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
<td align="left">out of range</td>
<td align="right">2</td>
<td align="right">100.0%</td>
<td align="right">2</td>
<td align="right">100.0%</td>
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
<td align="right">683,975</td>
<td align="right">1.3%</td>
<td align="right">2,121</td>
<td align="right">0.0%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">39,578,594</td>
<td align="right">73.5%</td>
<td align="right">28,249,572</td>
<td align="right">74.1%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,530,914</td>
<td align="right">25.1%</td>
<td align="right">9,858,642</td>
<td align="right">25.9%</td>
<td align="right">-27.1%</td>
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
<td align="right">67,878</td>
<td align="right">83.3%</td>
<td align="right">2,837</td>
<td align="right">76.6%</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,635</td>
<td align="right">16.7%</td>
<td align="right">869</td>
<td align="right">23.4%</td>
<td align="right">-93.6%</td>
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
<td align="right">65,575</td>
<td align="right">96.6%</td>
<td align="right">883</td>
<td align="right">31.1%</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,152</td>
<td align="right">3.2%</td>
<td align="right">1,804</td>
<td align="right">63.6%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">109</td>
<td align="right">0.2%</td>
<td align="right">108</td>
<td align="right">3.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">1.5%</td>
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
<td align="right">27,660,349</td>
<td align="right">100.0%</td>
<td align="right">18,038,368</td>
<td align="right">100.0%</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">444</td>
<td align="right">0.0%</td>
<td align="right">438</td>
<td align="right">0.0%</td>
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
<td align="left">Success</td>
<td align="right">124</td>
<td align="right">72.9%</td>
<td align="right">184</td>
<td align="right">80.0%</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">46</td>
<td align="right">27.1%</td>
<td align="right">46</td>
<td align="right">20.0%</td>
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
<td align="left">iterator</td>
<td align="right">46</td>
<td align="right">100.0%</td>
<td align="right">46</td>
<td align="right">100.0%</td>
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
<td align="right">769,231,027</td>
<td align="right">35.5%</td>
<td align="right">484,479,700</td>
<td align="right">34.9%</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,357,767,662</td>
<td align="right">62.6%</td>
<td align="right">858,504,167</td>
<td align="right">61.9%</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">702,100</td>
<td align="right">0.0%</td>
<td align="right">535,616</td>
<td align="right">0.0%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">39,954,925</td>
<td align="right">1.8%</td>
<td align="right">42,715,561</td>
<td align="right">3.1%</td>
<td align="right">6.9%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">1,424,383</td>
<td align="right">3.6%</td>
<td align="right">709,274</td>
<td align="right">1.7%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">11,657,822</td>
<td align="right">29.2%</td>
<td align="right">8,423,003</td>
<td align="right">19.7%</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">13,530,914</td>
<td align="right">33.9%</td>
<td align="right">9,858,642</td>
<td align="right">23.1%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,835,469</td>
<td align="right">32.2%</td>
<td align="right">10,689,334</td>
<td align="right">25.0%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">404,586</td>
<td align="right">1.0%</td>
<td align="right">338,939</td>
<td align="right">0.8%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,958</td>
<td align="right">0.0%</td>
<td align="right">1,813</td>
<td align="right">0.0%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,216</td>
<td align="right">0.0%</td>
<td align="right">3,191</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,739</td>
<td align="right">0.0%</td>
<td align="right">5,698</td>
<td align="right">0.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,586</td>
<td align="right">0.0%</td>
<td align="right">1,580</td>
<td align="right">0.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">500</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">12,650,944</td>
<td align="right">29.6%</td>
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
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,742</td>
<td align="right">0.2%</td>
<td align="right">258,070</td>
<td align="right">48.2%</td>
<td align="right">14,714.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">683,700</td>
<td align="right">97.4%</td>
<td align="right">1,855</td>
<td align="right">0.3%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,212</td>
<td align="right">0.9%</td>
<td align="right">9,528</td>
<td align="right">1.8%</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">181</td>
<td align="right">0.0%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">977</td>
<td align="right">0.1%</td>
<td align="right">962</td>
<td align="right">0.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">910</td>
<td align="right">0.1%</td>
<td align="right">898</td>
<td align="right">0.2%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,586</td>
<td align="right">0.2%</td>
<td align="right">1,569</td>
<td align="right">0.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,945</td>
<td align="right">0.6%</td>
<td align="right">3,915</td>
<td align="right">0.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,431</td>
<td align="right">0.3%</td>
<td align="right">2,415</td>
<td align="right">0.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">130</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE_KNOWN</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">255,691</td>
<td align="right">47.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">17,067,727</td>
<td align="right">14.1%</td>
<td align="right">12,902,354</td>
<td align="right">13.8%</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">99,077,134</td>
<td align="right">81.9%</td>
<td align="right">76,457,141</td>
<td align="right">81.9%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">21,847,122</td>
<td align="right">18.1%</td>
<td align="right">16,899,020</td>
<td align="right">18.1%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">21,847,122</td>
<td align="right">18.1%</td>
<td align="right">16,899,020</td>
<td align="right">18.1%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">39,219,103</td>
<td align="right">32.4%</td>
<td align="right">31,673,622</td>
<td align="right">33.9%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,268,390</td>
<td align="right">3.5%</td>
<td align="right">3,553,325</td>
<td align="right">3.8%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,779,395</td>
<td align="right">4.0%</td>
<td align="right">3,996,666</td>
<td align="right">4.3%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">510,987</td>
<td align="right">0.4%</td>
<td align="right">443,323</td>
<td align="right">0.5%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">521</td>
<td align="right">0.0%</td>
<td align="right">455</td>
<td align="right">0.0%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,179</td>
<td align="right">0.0%</td>
<td align="right">1,105</td>
<td align="right">0.0%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">421</td>
<td align="right">0.0%</td>
<td align="right">417</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">7,275</td>
<td align="right">0.0%</td>
<td align="right">7,220</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">18</td>
<td align="right">0.0%</td>
<td align="right">18</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left">Method cache collisions</td>
<td align="right">7,740</td>
<td align="right"></td>
<td align="right">31,280</td>
<td align="right"></td>
<td align="right">304.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">8,660</td>
<td align="right"></td>
<td align="right">32,066</td>
<td align="right"></td>
<td align="right">270.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">89,288,160</td>
<td align="right">6.0%</td>
<td align="right">130,695,675</td>
<td align="right">10.8%</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">267,555,755</td>
<td align="right">17.9%</td>
<td align="right">157,199,413</td>
<td align="right">13.0%</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">41,197,265</td>
<td align="right"></td>
<td align="right">28,575,507</td>
<td align="right"></td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">72,114,140</td>
<td align="right"></td>
<td align="right">52,599,818</td>
<td align="right"></td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">72,116,323</td>
<td align="right">67.3%</td>
<td align="right">52,601,996</td>
<td align="right">67.3%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">35,015,338</td>
<td align="right">32.7%</td>
<td align="right">25,577,535</td>
<td align="right">32.7%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">35,020,792</td>
<td align="right">32.7%</td>
<td align="right">25,582,809</td>
<td align="right">32.7%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">829,736,596</td>
<td align="right">65.4%</td>
<td align="right">634,236,066</td>
<td align="right">61.4%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">862,866,695</td>
<td align="right">57.6%</td>
<td align="right">668,106,423</td>
<td align="right">55.2%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">818</td>
<td align="right"></td>
<td align="right">988</td>
<td align="right"></td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">126,201,304</td>
<td align="right">9.9%</td>
<td align="right">101,191,286</td>
<td align="right">9.8%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">88,297,217</td>
<td align="right">7.0%</td>
<td align="right">71,243,471</td>
<td align="right">6.9%</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">8,858,595</td>
<td align="right"></td>
<td align="right">7,296,860</td>
<td align="right"></td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">26,102,957</td>
<td align="right"></td>
<td align="right">21,721,796</td>
<td align="right"></td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">2,665</td>
<td align="right"></td>
<td align="right">2,327</td>
<td align="right"></td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">278,845,418</td>
<td align="right">18.6%</td>
<td align="right">255,375,683</td>
<td align="right">21.1%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">2,706</td>
<td align="right">0.0%</td>
<td align="right">2,610</td>
<td align="right">0.0%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">2,748</td>
<td align="right">0.0%</td>
<td align="right">2,664</td>
<td align="right">0.0%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">225,085,167</td>
<td align="right">17.7%</td>
<td align="right">225,904,856</td>
<td align="right">21.9%</td>
<td align="right">0.4%</td>
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
<td align="right">799</td>
<td align="right">26,899</td>
<td align="right">9,284,165</td>
<td align="right">557,148</td>
<td align="right">1,522,986</td>
<td align="right">409</td>
<td align="right">26,776</td>
<td align="right">3,254,833</td>
<td align="right">89,945</td>
<td align="right">733,238</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">1,258</td>
<td align="right">18.4%</td>
<td align="right">62,800.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">1,318</td>
<td align="right">19.2%</td>
<td align="right">32,850.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">4,118,211</td>
<td align="right"></td>
<td align="right">58,464,911</td>
<td align="right"></td>
<td align="right">1,319.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">117,128,057</td>
<td align="right">2,844.1%</td>
<td align="right">853,244,667</td>
<td align="right">1,459.4%</td>
<td align="right">628.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">15,801</td>
<td align="right">74.3%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">21,273</td>
<td align="right"></td>
<td align="right">6,850</td>
<td align="right"></td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">5,468</td>
<td align="right">25.7%</td>
<td align="right">5,532</td>
<td align="right">80.8%</td>
<td align="right">1.2%</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">53</td>
<td align="right">0.8%</td>
<td align="right">53 / 0 !!</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">4</td>
<td align="right"></td>
<td align="right">1,318</td>
<td align="right"></td>
<td align="right">32,850.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">4</td>
<td align="right">100.0%</td>
<td align="right">64</td>
<td align="right">4.9%</td>
<td align="right">1,500.0%</td>
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
<td align="right">1,254</td>
<td align="right">95.1%</td>
<td align="right">1,254 / 0 !!</td>
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
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">7,168</td>
<td align="right">13.5%</td>
<td align="right">54,200</td>
<td align="right">15.2%</td>
<td align="right">656.1%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">38,031</td>
<td align="right">71.4%</td>
<td align="right">273,482</td>
<td align="right">76.7%</td>
<td align="right">619.1%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">53,248</td>
<td align="right"></td>
<td align="right">356,352</td>
<td align="right"></td>
<td align="right">569.2%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">8,049</td>
<td align="right">15.1%</td>
<td align="right">28,670</td>
<td align="right">8.0%</td>
<td align="right">256.2%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">258,048</td>
<td align="right">484.6%</td>
<td align="right">32,768</td>
<td align="right">9.2%</td>
<td align="right">-87.3%</td>
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
<td align="left"><= 8,192</td>
<td align="left">2</td>
<td align="right">50.0%</td>
<td align="left">2</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">1</td>
<td align="right">25.0%</td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">1</td>
<td align="right">25.0%</td>
<td align="left">3</td>
<td align="right">4.7%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 4,096</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">58</td>
<td align="right">90.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">1</td>
<td align="right">1.6%</td>
<td align="right"></td>
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
<td align="left"><= 64</td>
<td align="right">2</td>
<td align="right">50.0%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2</td>
<td align="right">50.0%</td>
<td align="right">3</td>
<td align="right">0.2%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">5</td>
<td align="right">0.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">54</td>
<td align="right">4.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,255</td>
<td align="right">95.2%</td>
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
<td align="left"><= 32</td>
<td align="right">2</td>
<td align="right">50.0%</td>
<td align="right">43</td>
<td align="right">3.3%</td>
<td align="right">2,050.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1</td>
<td align="right">25.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1</td>
<td align="right">25.0%</td>
<td align="right">3</td>
<td align="right">0.2%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">17</td>
<td align="right">1.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right"></td>
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
<td align="left">_PUSH_NULL</td>
<td align="right">2,807</td>
<td align="right">3,054,801</td>
<td align="right">108,728.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,807</td>
<td align="right">892,381</td>
<td align="right">31,691.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,807</td>
<td align="right">764,937</td>
<td align="right">27,151.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,283,916</td>
<td align="right">49,859,037</td>
<td align="right">3,783.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,283,916</td>
<td align="right">49,859,037</td>
<td align="right">3,783.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,839,780</td>
<td align="right">81,717,447</td>
<td align="right">2,777.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,118,211</td>
<td align="right">58,464,911</td>
<td align="right">1,319.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,118,211</td>
<td align="right">58,464,785</td>
<td align="right">1,319.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">4,121,018</td>
<td align="right">58,465,815</td>
<td align="right">1,318.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">12,096,330</td>
<td align="right">96,369,419</td>
<td align="right">696.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,236,158</td>
<td align="right">54,306,228</td>
<td align="right">559.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">19,649</td>
<td align="right">6,328</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,807</td>
<td align="right">904</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">2,807</td>
<td align="right">904</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">2,807</td>
<td align="right">904</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,807</td>
<td align="right">904</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,807</td>
<td align="right">904</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">2,807</td>
<td align="right">904</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">2,807</td>
<td align="right">904</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,807</td>
<td align="right">904</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">2,810</td>
<td align="right">905</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">2,810</td>
<td align="right">905</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">1,283,916</td>
<td align="right">697,702</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,283,916</td>
<td align="right">697,702</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,283,916</td>
<td align="right">697,702</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,283,916</td>
<td align="right">697,702</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,283,916</td>
<td align="right">697,702</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">1,283,916</td>
<td align="right">697,702</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">1,283,916</td>
<td align="right">697,702</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,283,916</td>
<td align="right">697,702</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">1,283,916</td>
<td align="right">697,702</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,283,916</td>
<td align="right">697,702</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,283,916</td>
<td align="right">697,702</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">4,121,015</td>
<td align="right">5,859,147</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">1,283,916</td>
<td align="right">825,146</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">11,070,321</td>
<td align="right">7,899,602</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,283,916</td>
<td align="right">946,342</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,834,163</td>
<td align="right">2,168,066</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">2,834,163</td>
<td align="right">2,168,066</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,572,185</td>
<td align="right">3,055,139</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,283,916</td>
<td align="right">1,461,735</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,121,015</td>
<td align="right">3,694,492</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">4,118,208</td>
<td align="right">3,693,588</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,542,012</td>
<td align="right">11,572,585</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,288,140</td>
<td align="right">1,402,173</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">12,096,330</td>
<td align="right">11,384,780</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,401,995</td>
<td align="right">5,089,301</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FOR_ITER_GEN</td>
<td align="right"></td>
<td align="right">54,901,001</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FOR_ITER_GEN_FUNCTION</td>
<td align="right"></td>
<td align="right">54,900,143</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FOR_ITER_GEN_OFFSET</td>
<td align="right"></td>
<td align="right">54,899,450</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right"></td>
<td align="right">49,158,974</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right"></td>
<td align="right">48,397,302</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right"></td>
<td align="right">1,140,117</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right"></td>
<td align="right">891,477</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">764,033</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">764,033</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">764,033</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right"></td>
<td align="right">764,033</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right"></td>
<td align="right">764,033</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right"></td>
<td align="right">764,033</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right"></td>
<td align="right">764,033</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">764,033</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right"></td>
<td align="right">761,798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right"></td>
<td align="right">761,798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">127,444</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">63,721</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">126</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-18
