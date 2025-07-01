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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,066,073</td>
<td align="right">61,152</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">91,144</td>
<td align="right">6,997</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">518,610</td>
<td align="right">70,287</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">2,034,529</td>
<td align="right">373,814</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">551,439</td>
<td align="right">101,667</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">860,055</td>
<td align="right">174,615</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">146,076</td>
<td align="right">34,839</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,617,104</td>
<td align="right">646,800</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,441,665</td>
<td align="right">724,668</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">3,207,498</td>
<td align="right">1,037,379</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">4,143</td>
<td align="right">1,371</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,063,080</td>
<td align="right">1,549,023</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">5,411,112</td>
<td align="right">2,819,208</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,710,090</td>
<td align="right">2,534,763</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,633,493</td>
<td align="right">1,437,417</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">15,962,583</td>
<td align="right">8,736,744</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,959,717</td>
<td align="right">2,782,941</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">12,366</td>
<td align="right">6,948</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,274,117</td>
<td align="right">1,349,387</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,274,222</td>
<td align="right">1,349,492</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,643,704</td>
<td align="right">1,635,479</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,973,243</td>
<td align="right">1,883,532</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">347,954</td>
<td align="right">230,916</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,064,838</td>
<td align="right">723,399</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,431,553</td>
<td align="right">2,340,456</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,688,115</td>
<td align="right">3,266,978</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,188,730</td>
<td align="right">4,428,090</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">57,502,961</td>
<td align="right">41,227,861</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">13,493,551</td>
<td align="right">9,699,131</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,809,926</td>
<td align="right">4,966,283</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">118,959,937</td>
<td align="right">88,634,851</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,355,514</td>
<td align="right">1,018,107</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">984,753</td>
<td align="right">752,829</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">6,061,671</td>
<td align="right">4,741,170</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,560,179</td>
<td align="right">6,716,484</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,451,661</td>
<td align="right">2,740,429</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,047,968</td>
<td align="right">1,647,393</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,783,469</td>
<td align="right">1,474,186</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">30,161,781</td>
<td align="right">25,242,746</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">22,151,479</td>
<td align="right">18,549,900</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,535,258</td>
<td align="right">5,507,544</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,911,614</td>
<td align="right">2,479,287</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,530,947</td>
<td align="right">2,155,425</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">541,569</td>
<td align="right">467,943</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,742,613</td>
<td align="right">1,512,705</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">15,932,002</td>
<td align="right">13,903,362</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,044,912</td>
<td align="right">9,734,943</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">720,027</td>
<td align="right">635,964</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,713,517</td>
<td align="right">7,128,812</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">11,604,852</td>
<td align="right">10,746,164</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">18,654,771</td>
<td align="right">17,411,004</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,734,980</td>
<td align="right">6,297,663</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">7,838,047</td>
<td align="right">7,340,431</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">26,432,952</td>
<td align="right">24,914,967</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">27,356,889</td>
<td align="right">25,852,848</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,865,818</td>
<td align="right">3,672,870</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">8,598,201</td>
<td align="right">8,285,762</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">687,183</td>
<td align="right">668,850</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">16,134,086</td>
<td align="right">15,709,907</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">405,405</td>
<td align="right">401,247</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">421,785</td>
<td align="right">417,627</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,613,913</td>
<td align="right">1,601,628</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">537,069</td>
<td align="right">534,360</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">851,142</td>
<td align="right">848,433</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,732,335</td>
<td align="right">1,729,437</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">3,882,207</td>
<td align="right">3,882,207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,768,433</td>
<td align="right">2,768,433</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,743,650</td>
<td align="right">2,743,650</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,973,928</td>
<td align="right">1,973,928</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,494,570</td>
<td align="right">1,494,570</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,429,155</td>
<td align="right">1,429,155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,128,323</td>
<td align="right">1,128,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">685,988</td>
<td align="right">685,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">638,889</td>
<td align="right">638,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">630,441</td>
<td align="right">630,441</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">565,089</td>
<td align="right">565,089</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">565,089</td>
<td align="right">565,089</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">565,089</td>
<td align="right">565,089</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">483,168</td>
<td align="right">483,168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">405,543</td>
<td align="right">405,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">384,531</td>
<td align="right">384,531</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">335,859</td>
<td align="right">335,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">257,859</td>
<td align="right">257,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">241,674</td>
<td align="right">241,674</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">69,684</td>
<td align="right">69,684</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,760</td>
<td align="right">37,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">32,829</td>
<td align="right">32,829</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">28,623</td>
<td align="right">28,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">24,570</td>
<td align="right">24,570</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">24,570</td>
<td align="right">24,570</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">24,555</td>
<td align="right">24,555</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">23,889</td>
<td align="right">23,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">20,391</td>
<td align="right">20,391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">16,359</td>
<td align="right">16,359</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">12,285</td>
<td align="right">12,285</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">12,285</td>
<td align="right">12,285</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">12,285</td>
<td align="right">12,285</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">11,844</td>
<td align="right">11,844</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">10,906</td>
<td align="right">10,906</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">8,259</td>
<td align="right">8,259</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,259</td>
<td align="right">8,259</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">8,169</td>
<td align="right">8,169</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,355</td>
<td align="right">7,355</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">7,014</td>
<td align="right">7,014</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">4,095</td>
<td align="right">4,095</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">4,074</td>
<td align="right">4,074</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">4,074</td>
<td align="right">4,074</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">4,071</td>
<td align="right">4,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,247</td>
<td align="right">2,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,806</td>
<td align="right">1,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,050</td>
<td align="right">1,050</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">483</td>
<td align="right">483</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">210</td>
<td align="right">210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">69</td>
<td align="right">69</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">69</td>
<td align="right">69</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">69</td>
<td align="right">69</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">48</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">48</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
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
<td align="right">90,198</td>
<td align="right">0.2%</td>
<td align="right">6,135</td>
<td align="right">0.0%</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,264,542</td>
<td align="right">99.7%</td>
<td align="right">36,264,542</td>
<td align="right">99.9%</td>
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
<td align="right">12,565</td>
<td align="right">0.0%</td>
<td align="right">12,565</td>
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
<td align="right">232</td>
<td align="right">19.7%</td>
<td align="right">148</td>
<td align="right">13.5%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">948</td>
<td align="right">80.3%</td>
<td align="right">948</td>
<td align="right">86.5%</td>
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
<td align="right">231</td>
<td align="right">99.6%</td>
<td align="right">147</td>
<td align="right">99.3%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.7%</td>
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
<td align="right">1,429,155</td>
<td align="right">100.0%</td>
<td align="right">1,429,155</td>
<td align="right">100.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">766,075</td>
<td align="right">2.1%</td>
<td align="right">766,075</td>
<td align="right">2.1%</td>
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
<td align="right">35,666,387</td>
<td align="right">97.8%</td>
<td align="right">35,666,387</td>
<td align="right">97.8%</td>
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
<td align="right">774,740</td>
<td align="right">2.1%</td>
<td align="right">774,740</td>
<td align="right">2.1%</td>
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
<td align="right">20,509</td>
<td align="right">100.0%</td>
<td align="right">20,509</td>
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
<td align="right">525</td>
<td align="right">50.0%</td>
<td align="right">525</td>
<td align="right">50.0%</td>
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
<td align="right">525</td>
<td align="right">100.0%</td>
<td align="right">525</td>
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
<td align="right">6,531,414</td>
<td align="right">30.5%</td>
<td align="right">5,504,058</td>
<td align="right">27.5%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,872,557</td>
<td align="right">69.5%</td>
<td align="right">14,533,827</td>
<td align="right">72.5%</td>
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
<td align="right">3,361</td>
<td align="right">87.4%</td>
<td align="right">3,003</td>
<td align="right">86.1%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">483</td>
<td align="right">12.6%</td>
<td align="right">483</td>
<td align="right">13.9%</td>
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
<td align="right">316</td>
<td align="right">9.4%</td>
<td align="right">168</td>
<td align="right">5.6%</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">3,045</td>
<td align="right">90.6%</td>
<td align="right">2,835</td>
<td align="right">94.4%</td>
<td align="right">-6.9%</td>
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
<td align="right">37,149</td>
<td align="right">0.5%</td>
<td align="right">37,149</td>
<td align="right">0.5%</td>
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
<td align="right">6,940,955</td>
<td align="right">91.0%</td>
<td align="right">6,940,955</td>
<td align="right">91.0%</td>
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
<td align="right">650,861</td>
<td align="right">8.5%</td>
<td align="right">650,861</td>
<td align="right">8.5%</td>
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
<td align="right">12,559</td>
<td align="right">97.5%</td>
<td align="right">12,559</td>
<td align="right">97.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">317</td>
<td align="right">2.5%</td>
<td align="right">317</td>
<td align="right">2.5%</td>
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
<td align="right">190</td>
<td align="right">59.9%</td>
<td align="right">190</td>
<td align="right">59.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">127</td>
<td align="right">40.1%</td>
<td align="right">127</td>
<td align="right">40.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">150,219</td>
<td align="right">5.4%</td>
<td align="right">36,210</td>
<td align="right">2.2%</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,641,974</td>
<td align="right">94.6%</td>
<td align="right">1,634,066</td>
<td align="right">97.7%</td>
<td align="right">-38.1%</td>
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
<td align="right">1,625</td>
<td align="right">93.9%</td>
<td align="right">1,308</td>
<td align="right">92.6%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">105</td>
<td align="right">6.1%</td>
<td align="right">105</td>
<td align="right">7.4%</td>
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
<td align="left">enumerate</td>
<td align="right">231</td>
<td align="right">14.2%</td>
<td align="right">147</td>
<td align="right">11.2%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">676</td>
<td align="right">41.6%</td>
<td align="right">506</td>
<td align="right">38.7%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">380</td>
<td align="right">23.4%</td>
<td align="right">338</td>
<td align="right">25.8%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">316</td>
<td align="right">19.4%</td>
<td align="right">295</td>
<td align="right">22.6%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">22</td>
<td align="right">1.4%</td>
<td align="right">22</td>
<td align="right">1.7%</td>
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
<td align="left">other</td>
<td align="right">1,027,914</td>
<td align="right">1,027,914 / 0 !!</td>
<td align="right">1,027,914</td>
<td align="right">1,027,914 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">1,003,275</td>
<td align="right">1,003,275 / 0 !!</td>
<td align="right">1,003,275</td>
<td align="right">1,003,275 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">384,930</td>
<td align="right">384,930 / 0 !!</td>
<td align="right">384,930</td>
<td align="right">384,930 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">53,235</td>
<td align="right">53,235 / 0 !!</td>
<td align="right">53,235</td>
<td align="right">53,235 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,095</td>
<td align="right">4,095 / 0 !!</td>
<td align="right">4,095</td>
<td align="right">4,095 / 0 !!</td>
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
<td align="right">2,358,697</td>
<td align="right">1.5%</td>
<td align="right">921,304</td>
<td align="right">0.6%</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,684,389</td>
<td align="right">4.8%</td>
<td align="right">7,099,938</td>
<td align="right">4.6%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">150,261,790</td>
<td align="right">93.7%</td>
<td align="right">146,605,163</td>
<td align="right">94.8%</td>
<td align="right">-2.4%</td>
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
<td align="right">53,869</td>
<td align="right">73.2%</td>
<td align="right">26,754</td>
<td align="right">57.9%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">19,720</td>
<td align="right">26.8%</td>
<td align="right">19,466</td>
<td align="right">42.1%</td>
<td align="right">-1.3%</td>
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
<td align="right">443</td>
<td align="right">2.2%</td>
<td align="right">421</td>
<td align="right">2.2%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">16,594</td>
<td align="right">84.1%</td>
<td align="right">16,384</td>
<td align="right">84.2%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,661</td>
<td align="right">13.5%</td>
<td align="right">2,639</td>
<td align="right">13.6%</td>
<td align="right">-0.8%</td>
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
<td align="right">18,335,380</td>
<td align="right">99.9%</td>
<td align="right">17,039,375</td>
<td align="right">99.9%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,507</td>
<td align="right">0.0%</td>
<td align="right">3,507</td>
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
<td align="right">4,452</td>
<td align="right">0.0%</td>
<td align="right">4,452</td>
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
<td align="right">3,591</td>
<td align="right">100.0%</td>
<td align="right">3,591</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,550,901</td>
<td align="right">6.5%</td>
<td align="right">1,710,833</td>
<td align="right">4.5%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,488,882</td>
<td align="right">93.5%</td>
<td align="right">36,695,312</td>
<td align="right">95.5%</td>
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
<td align="right">903</td>
<td align="right">0.0%</td>
<td align="right">903</td>
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
<td align="right">48,999</td>
<td align="right">100.0%</td>
<td align="right">33,171</td>
<td align="right">100.0%</td>
<td align="right">-32.3%</td>
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
<td align="right">21</td>
<td align="right">0.5%</td>
<td align="right">21</td>
<td align="right">0.5%</td>
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
<td align="right">4,074</td>
<td align="right">99.0%</td>
<td align="right">4,074</td>
<td align="right">99.0%</td>
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
<td align="right">21</td>
<td align="right">100.0%</td>
<td align="right">21</td>
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
<td align="right">1,549,647</td>
<td align="right">5.1%</td>
<td align="right">1,240,770</td>
<td align="right">4.1%</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">28,953,476</td>
<td align="right">94.9%</td>
<td align="right">28,798,047</td>
<td align="right">95.8%</td>
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
<td align="right">7,461</td>
<td align="right">0.0%</td>
<td align="right">7,461</td>
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
<td align="right">32,183</td>
<td align="right">99.5%</td>
<td align="right">26,365</td>
<td align="right">99.4%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">148</td>
<td align="right">0.5%</td>
<td align="right">148</td>
<td align="right">0.6%</td>
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
<td align="right">127</td>
<td align="right">85.8%</td>
<td align="right">127</td>
<td align="right">85.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">14.2%</td>
<td align="right">21</td>
<td align="right">14.2%</td>
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
<td align="right">105</td>
<td align="right">0.0%</td>
<td align="right">105</td>
<td align="right">0.0%</td>
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
<td align="right">3,804,219</td>
<td align="right">100.0%</td>
<td align="right">3,804,219</td>
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
<td align="right">105</td>
<td align="right">100.0%</td>
<td align="right">105</td>
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
<td align="right">7,901,952</td>
<td align="right">1.4%</td>
<td align="right">5,315,652</td>
<td align="right">1.2%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">236,290,832</td>
<td align="right">42.6%</td>
<td align="right">185,612,129</td>
<td align="right">42.3%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">290,523,659</td>
<td align="right">52.3%</td>
<td align="right">230,928,953</td>
<td align="right">52.6%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">20,531,378</td>
<td align="right">3.7%</td>
<td align="right">17,426,012</td>
<td align="right">4.0%</td>
<td align="right">-15.1%</td>
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
<td align="right">90,198</td>
<td align="right">0.5%</td>
<td align="right">6,135</td>
<td align="right">0.0%</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,641,974</td>
<td align="right">13.8%</td>
<td align="right">1,634,066</td>
<td align="right">9.9%</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,531,414</td>
<td align="right">34.0%</td>
<td align="right">5,504,058</td>
<td align="right">33.4%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,684,389</td>
<td align="right">40.0%</td>
<td align="right">7,099,938</td>
<td align="right">43.1%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,429,155</td>
<td align="right">7.4%</td>
<td align="right">1,429,155</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">766,075</td>
<td align="right">4.0%</td>
<td align="right">766,075</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,149</td>
<td align="right">0.2%</td>
<td align="right">37,149</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">7,461</td>
<td align="right">0.0%</td>
<td align="right">7,461</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,507</td>
<td align="right">0.0%</td>
<td align="right">3,507</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">903</td>
<td align="right">0.0%</td>
<td align="right">903</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">911,348</td>
<td align="right">11.5%</td>
<td align="right">344,261</td>
<td align="right">6.5%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,550,901</td>
<td align="right">32.3%</td>
<td align="right">1,710,833</td>
<td align="right">32.2%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">486,782</td>
<td align="right">6.2%</td>
<td align="right">334,322</td>
<td align="right">6.3%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">764,948</td>
<td align="right">9.7%</td>
<td align="right">610,856</td>
<td align="right">11.5%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">903,255</td>
<td align="right">11.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">543,359</td>
<td align="right">6.9%</td>
<td align="right">543,359</td>
<td align="right">10.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">390,547</td>
<td align="right">4.9%</td>
<td align="right">390,547</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">378,202</td>
<td align="right">4.8%</td>
<td align="right">378,202</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">325,579</td>
<td align="right">4.1%</td>
<td align="right">325,579</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">325,282</td>
<td align="right">4.1%</td>
<td align="right">325,282</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">263,934</td>
<td align="right">5.0%</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">3,882,276</td>
<td align="right">12.6%</td>
<td align="right">3,882,276</td>
<td align="right">12.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">27,051,837</td>
<td align="right">87.4%</td>
<td align="right">27,051,837</td>
<td align="right">87.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">3,882,276</td>
<td align="right">12.6%</td>
<td align="right">3,882,276</td>
<td align="right">12.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">3,882,276</td>
<td align="right">12.6%</td>
<td align="right">3,882,276</td>
<td align="right">12.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">3,882,276</td>
<td align="right">12.6%</td>
<td align="right">3,882,276</td>
<td align="right">12.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">450,471</td>
<td align="right">1.5%</td>
<td align="right">450,471</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">69</td>
<td align="right">0.0%</td>
<td align="right">69</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,743,755</td>
<td align="right">8.9%</td>
<td align="right">2,743,755</td>
<td align="right">8.9%</td>
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
<tr>
<td align="left">Frame objects created</td>
<td align="right">12,285</td>
<td align="right">0.0%</td>
<td align="right">12,285</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">31,499,202</td>
<td align="right">101.8%</td>
<td align="right">31,499,202</td>
<td align="right">101.8%</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">362</td>
<td align="right">0.0%</td>
<td align="right">882</td>
<td align="right">0.0%</td>
<td align="right">143.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">168</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">11,508,745</td>
<td align="right">3.2%</td>
<td align="right">6,593,691</td>
<td align="right">1.8%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">14,333,663</td>
<td align="right">3.8%</td>
<td align="right">8,268,316</td>
<td align="right">2.2%</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">46,381</td>
<td align="right"></td>
<td align="right">28,350</td>
<td align="right"></td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">112,526,437</td>
<td align="right">29.9%</td>
<td align="right">134,342,725</td>
<td align="right">35.8%</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">112,560,552</td>
<td align="right">31.3%</td>
<td align="right">130,005,976</td>
<td align="right">36.3%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">175,032,187</td>
<td align="right">46.5%</td>
<td align="right">152,615,400</td>
<td align="right">40.7%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">146,605,129</td>
<td align="right">40.8%</td>
<td align="right">128,559,412</td>
<td align="right">35.9%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">341,163</td>
<td align="right"></td>
<td align="right">374,806</td>
<td align="right"></td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">74,433,868</td>
<td align="right">19.8%</td>
<td align="right">80,185,224</td>
<td align="right">21.4%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">88,737,868</td>
<td align="right">24.7%</td>
<td align="right">93,340,446</td>
<td align="right">26.0%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">386,309</td>
<td align="right"></td>
<td align="right">401,978</td>
<td align="right"></td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">24,849,906</td>
<td align="right"></td>
<td align="right">24,662,880</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">7,484,702</td>
<td align="right"></td>
<td align="right">7,502,649</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,150,351</td>
<td align="right">38.8%</td>
<td align="right">12,151,218</td>
<td align="right">38.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">11,835,258</td>
<td align="right"></td>
<td align="right">11,834,901</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,149,905</td>
<td align="right">38.8%</td>
<td align="right">12,150,168</td>
<td align="right">38.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">19,146,361</td>
<td align="right">61.2%</td>
<td align="right">19,146,498</td>
<td align="right">61.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">19,144,723</td>
<td align="right"></td>
<td align="right">19,144,615</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">647,010</td>
<td align="right"></td>
<td align="right">647,010</td>
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
<td align="right">618</td>
<td align="right">1,062,972</td>
<td align="right">12,210,348</td>
<td align="right">735,622</td>
<td align="right">1,211,641</td>
<td align="right">618</td>
<td align="right">1,062,666</td>
<td align="right">12,176,196</td>
<td align="right">739,198</td>
<td align="right">1,205,334</td>
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
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">172</td>
<td align="right">16.5%</td>
<td align="right">1,181</td>
<td align="right">29.8%</td>
<td align="right">586.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,045</td>
<td align="right"></td>
<td align="right">3,960</td>
<td align="right"></td>
<td align="right">278.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">322</td>
<td align="right">30.8%</td>
<td align="right">1,162</td>
<td align="right">29.3%</td>
<td align="right">260.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">4,358,428</td>
<td align="right"></td>
<td align="right">12,040,314</td>
<td align="right"></td>
<td align="right">176.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">551</td>
<td align="right">52.7%</td>
<td align="right">1,470</td>
<td align="right">37.1%</td>
<td align="right">166.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">747,448,789</td>
<td align="right">17,149.5%</td>
<td align="right">1,013,347,335</td>
<td align="right">8,416.3%</td>
<td align="right">35.6%</td>
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
<td align="right">105</td>
<td align="right">2.7%</td>
<td align="right">105 / 0 !!</td>
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

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">1.1%</td>
<td align="right">42 / 0 !!</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">2.1%</td>
<td align="right">84 / 0 !!</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">446</td>
<td align="right">80.9%</td>
<td align="right">1,365</td>
<td align="right">92.9%</td>
<td align="right">206.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">551</td>
<td align="right"></td>
<td align="right">1,470</td>
<td align="right"></td>
<td align="right">166.8%</td>
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
<td align="right">927,937</td>
<td align="right">14.1%</td>
<td align="right">2,854,929</td>
<td align="right">20.6%</td>
<td align="right">207.7%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">6,578,176</td>
<td align="right"></td>
<td align="right">13,848,576</td>
<td align="right"></td>
<td align="right">110.5%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">141,744</td>
<td align="right">2.2%</td>
<td align="right">297,360</td>
<td align="right">2.1%</td>
<td align="right">109.8%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">5,508,495</td>
<td align="right">83.7%</td>
<td align="right">10,696,287</td>
<td align="right">77.2%</td>
<td align="right">94.2%</td>
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
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">86,016</td>
<td align="right">0.6%</td>
<td align="right">86,016 / 0 !!</td>
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
<td align="left">86</td>
<td align="right">19.3%</td>
<td align="left">651</td>
<td align="right">47.7%</td>
<td align="right">657.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">106</td>
<td align="right">23.8%</td>
<td align="left">357</td>
<td align="right">26.2%</td>
<td align="right">236.8%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">170</td>
<td align="right">38.1%</td>
<td align="left">189</td>
<td align="right">13.8%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">21</td>
<td align="right">4.7%</td>
<td align="left">63</td>
<td align="right">4.6%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">63</td>
<td align="right">14.1%</td>
<td align="left">105</td>
<td align="right">7.7%</td>
<td align="right">66.7%</td>
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
<td align="left"><= 16</td>
<td align="right">22</td>
<td align="right">4.0%</td>
<td align="right">252</td>
<td align="right">17.1%</td>
<td align="right">1,045.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">106</td>
<td align="right">19.2%</td>
<td align="right">147</td>
<td align="right">10.0%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">108</td>
<td align="right">19.6%</td>
<td align="right">399</td>
<td align="right">27.1%</td>
<td align="right">269.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">147</td>
<td align="right">26.7%</td>
<td align="right">168</td>
<td align="right">11.4%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">2.9%</td>
<td align="right">42 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">168</td>
<td align="right">30.5%</td>
<td align="right">147</td>
<td align="right">10.0%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">294</td>
<td align="right">20.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21</td>
<td align="right">1.4%</td>
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
<td align="left"><= 16</td>
<td align="right">86</td>
<td align="right">15.6%</td>
<td align="right">336</td>
<td align="right">22.9%</td>
<td align="right">290.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">107</td>
<td align="right">19.4%</td>
<td align="right">273</td>
<td align="right">18.6%</td>
<td align="right">155.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">148</td>
<td align="right">26.9%</td>
<td align="right">273</td>
<td align="right">18.6%</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21</td>
<td align="right">3.8%</td>
<td align="right">42</td>
<td align="right">2.9%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">84</td>
<td align="right">15.2%</td>
<td align="right">105</td>
<td align="right">7.1%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">63</td>
<td align="right">4.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">252</td>
<td align="right">17.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21</td>
<td align="right">1.4%</td>
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
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">2,910</td>
<td align="right">903,777</td>
<td align="right">30,957.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,455</td>
<td align="right">451,227</td>
<td align="right">30,912.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,455</td>
<td align="right">449,778</td>
<td align="right">30,812.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,260</td>
<td align="right">112,497</td>
<td align="right">8,828.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,260</td>
<td align="right">112,497</td>
<td align="right">8,828.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">900</td>
<td align="right">72,891</td>
<td align="right">7,999.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">359,390</td>
<td align="right">996,135</td>
<td align="right">177.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,358,428</td>
<td align="right">12,040,314</td>
<td align="right">176.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,358,428</td>
<td align="right">12,040,314</td>
<td align="right">176.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">578,762</td>
<td align="right">1,571,136</td>
<td align="right">171.5%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">169,890</td>
<td align="right">399,798</td>
<td align="right">135.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">695,357</td>
<td align="right">1,470,588</td>
<td align="right">111.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">127,050</td>
<td align="right">265,167</td>
<td align="right">108.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">127,050</td>
<td align="right">265,167</td>
<td align="right">108.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">127,050</td>
<td align="right">265,167</td>
<td align="right">108.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">445,284</td>
<td align="right">867,825</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">425,481</td>
<td align="right">826,056</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">517,731</td>
<td align="right">981,603</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,003,989</td>
<td align="right">17,046,776</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">89,019</td>
<td align="right">168,252</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">425,481</td>
<td align="right">801,003</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">89,019</td>
<td align="right">162,645</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">280,413</td>
<td align="right">512,337</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">1,775,378</td>
<td align="right">3,196,515</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,836,004</td>
<td align="right">4,926,810</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,505,893</td>
<td align="right">4,264,178</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,357,859</td>
<td align="right">3,839,913</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,530,102</td>
<td align="right">2,454,832</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,604,236</td>
<td align="right">4,106,592</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">16,539,733</td>
<td align="right">25,171,914</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">5,649,528</td>
<td align="right">8,230,983</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">3,384,575</td>
<td align="right">4,918,872</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">1,530,102</td>
<td align="right">2,116,102</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,495,055</td>
<td align="right">6,212,052</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">13,445,944</td>
<td align="right">18,569,414</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">7,547,488</td>
<td align="right">10,332,879</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">4,142,313</td>
<td align="right">5,646,354</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">2,834,334</td>
<td align="right">3,861,690</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,757,406</td>
<td align="right">2,388,514</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">869,881</td>
<td align="right">1,179,164</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,087,226</td>
<td align="right">12,302,722</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">144,837,881</td>
<td align="right">195,285,248</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">4,498,914</td>
<td align="right">6,016,899</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">4,498,914</td>
<td align="right">6,016,899</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">4,498,914</td>
<td align="right">6,016,899</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">4,498,914</td>
<td align="right">6,016,899</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">4,498,914</td>
<td align="right">6,014,190</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,226,146</td>
<td align="right">1,637,993</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">140,361,920</td>
<td align="right">185,846,916</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">6,930,483</td>
<td align="right">9,029,706</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">12,588,597</td>
<td align="right">16,312,989</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">8,476,356</td>
<td align="right">10,952,025</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">13,017,359</td>
<td align="right">16,776,094</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">8,674,948</td>
<td align="right">11,163,420</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">23,077,200</td>
<td align="right">29,669,401</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">75,882,803</td>
<td align="right">96,870,246</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">8,196,279</td>
<td align="right">10,449,453</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">57,413,543</td>
<td align="right">73,021,977</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">20,357,169</td>
<td align="right">25,876,830</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">5,267,661</td>
<td align="right">6,695,367</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">4,053,630</td>
<td align="right">5,144,727</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,053,630</td>
<td align="right">5,143,341</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">8,107,260</td>
<td align="right">10,284,036</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">8,107,260</td>
<td align="right">10,282,587</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">8,107,260</td>
<td align="right">10,282,587</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">16,214,184</td>
<td align="right">20,562,528</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">8,106,924</td>
<td align="right">10,277,043</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">4,053,294</td>
<td align="right">5,136,474</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,787,350</td>
<td align="right">4,795,258</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">2,718,954</td>
<td align="right">3,404,394</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,728,295</td>
<td align="right">4,664,220</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">356,265</td>
<td align="right">443,835</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">3,695,685</td>
<td align="right">4,593,787</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">4,987,248</td>
<td align="right">6,183,030</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">356,265</td>
<td align="right">440,937</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">356,265</td>
<td align="right">440,937</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">356,265</td>
<td align="right">440,937</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">82,551</td>
<td align="right">100,884</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,556,100</td>
<td align="right">1,900,857</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">1,302,819</td>
<td align="right">1,557,675</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">471,534</td>
<td align="right">558,495</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">471,534</td>
<td align="right">555,597</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">471,534</td>
<td align="right">555,597</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">471,534</td>
<td align="right">555,597</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">471,534</td>
<td align="right">555,597</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">475,020</td>
<td align="right">559,692</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,645,561</td>
<td align="right">5,006,462</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">617,810</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">342,825</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right"></td>
<td align="right">341,439</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right"></td>
<td align="right">340,179</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right"></td>
<td align="right">340,179</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right"></td>
<td align="right">338,730</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right"></td>
<td align="right">260,085</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right"></td>
<td align="right">100,884</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right"></td>
<td align="right">23,604</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">5,418</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">5,418</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">4,158</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">4,158</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">2,898</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right"></td>
<td align="right">2,772</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right"></td>
<td align="right">2,772</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">2,709</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">2,709</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right"></td>
<td align="right">2,709</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">2,709</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right"></td>
<td align="right">2,709</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right"></td>
<td align="right">1,449</td>
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
<td align="right"></td>
<td align="right">84</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-01
