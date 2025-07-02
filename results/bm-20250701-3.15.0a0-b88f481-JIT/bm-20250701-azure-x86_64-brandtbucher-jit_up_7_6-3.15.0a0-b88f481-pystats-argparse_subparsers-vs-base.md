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
<td align="left">TO_BOOL_NONE</td>
<td align="right">174,108</td>
<td align="right">4,612</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">173,199</td>
<td align="right">6,199</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,444,184</td>
<td align="right">851,926</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">2,572,396</td>
<td align="right">917,315</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">682,800</td>
<td align="right">259,842</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">682,800</td>
<td align="right">259,842</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">348,462</td>
<td align="right">133,038</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">347,346</td>
<td align="right">132,945</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">813,464</td>
<td align="right">324,929</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,582,245</td>
<td align="right">707,021</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,718,256</td>
<td align="right">773,890</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,720,339</td>
<td align="right">774,990</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">856,034</td>
<td align="right">386,250</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,346,671</td>
<td align="right">1,086,738</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">18,709,962</td>
<td align="right">8,833,375</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">11,017,007</td>
<td align="right">5,243,836</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,595,668</td>
<td align="right">3,660,899</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,527,257</td>
<td align="right">1,218,690</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">3,031,083</td>
<td align="right">1,469,183</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">25,892,975</td>
<td align="right">12,615,556</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">7,855,403</td>
<td align="right">3,831,932</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,923,234</td>
<td align="right">1,914,057</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">8,126,774</td>
<td align="right">3,967,665</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,896,828</td>
<td align="right">4,351,604</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">15,541,285</td>
<td align="right">7,622,603</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">95,926,962</td>
<td align="right">47,097,011</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">11,987,201</td>
<td align="right">5,891,965</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">15,941,462</td>
<td align="right">7,859,666</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">17,728,375</td>
<td align="right">8,750,366</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">24,061,503</td>
<td align="right">11,905,925</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">382,533</td>
<td align="right">190,021</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,535,802</td>
<td align="right">764,858</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">647,847</td>
<td align="right">322,643</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">3,069,945</td>
<td align="right">1,528,953</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,325,855</td>
<td align="right">1,158,367</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,536,885</td>
<td align="right">765,429</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,534,590</td>
<td align="right">764,286</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,285,710</td>
<td align="right">640,334</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,026,120</td>
<td align="right">511,048</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,025,355</td>
<td align="right">510,667</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">767,295</td>
<td align="right">382,143</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">512,550</td>
<td align="right">255,270</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">512,295</td>
<td align="right">255,143</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">384,285</td>
<td align="right">191,389</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">8,160</td>
<td align="right">4,064</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,120</td>
<td align="right">3,048</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">5,100</td>
<td align="right">2,540</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,825</td>
<td align="right">1,905</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,060</td>
<td align="right">1,524</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,785</td>
<td align="right">889</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">765</td>
<td align="right">381</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">510</td>
<td align="right">254</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">510</td>
<td align="right">254</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">510</td>
<td align="right">254</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">255</td>
<td align="right">127</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">2,563,812</td>
<td align="right">1,276,900</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">2,563,812</td>
<td align="right">1,276,900</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">2,563,812</td>
<td align="right">1,276,900</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">4,349,640</td>
<td align="right">2,166,344</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,562,815</td>
<td align="right">1,276,414</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,406,877</td>
<td align="right">700,701</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,918,086</td>
<td align="right">955,314</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,003,295</td>
<td align="right">2,491,932</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,031,518</td>
<td align="right">513,757</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,280,675</td>
<td align="right">637,858</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,534,674</td>
<td align="right">764,370</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,969,350</td>
<td align="right">1,977,029</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,668,848</td>
<td align="right">831,215</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">525,342</td>
<td align="right">261,662</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,179,971</td>
<td align="right">1,085,827</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">770,949</td>
<td align="right">384,005</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">7,304,023</td>
<td align="right">3,638,101</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">12,806,295</td>
<td align="right">6,378,775</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">523,070</td>
<td align="right">260,541</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">512,615</td>
<td align="right">255,334</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,284,879</td>
<td align="right">640,015</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,117,611</td>
<td align="right">2,549,161</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,635,598</td>
<td align="right">2,807,181</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,920,039</td>
<td align="right">956,455</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">765,168</td>
<td align="right">381,168</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">11,533,711</td>
<td align="right">5,745,547</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">18,581,727</td>
<td align="right">9,256,537</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,048,898</td>
<td align="right">1,020,674</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">262,460</td>
<td align="right">130,747</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">260,930</td>
<td align="right">129,985</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">257,870</td>
<td align="right">128,461</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">18,067,368</td>
<td align="right">9,000,482</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,164,059</td>
<td align="right">6,059,865</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,027,965</td>
<td align="right">512,125</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">511,698</td>
<td align="right">254,930</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,533,606</td>
<td align="right">764,070</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">511,719</td>
<td align="right">254,951</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">511,719</td>
<td align="right">254,951</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,660,074</td>
<td align="right">3,318,243</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,920,630</td>
<td align="right">956,918</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,692,149</td>
<td align="right">1,341,365</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,023,501</td>
<td align="right">509,965</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">1,026,624</td>
<td align="right">511,552</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,028,453</td>
<td align="right">512,484</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,917,482</td>
<td align="right">955,519</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,581,733</td>
<td align="right">1,286,626</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,664,478</td>
<td align="right">829,534</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,184,331</td>
<td align="right">1,088,797</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">775,112</td>
<td align="right">386,373</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,211,354</td>
<td align="right">1,600,899</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,033,863</td>
<td align="right">515,463</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">771,705</td>
<td align="right">384,761</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">769,091</td>
<td align="right">383,512</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">896,184</td>
<td align="right">446,904</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">638,976</td>
<td align="right">318,720</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">770,043</td>
<td align="right">384,123</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">514,921</td>
<td align="right">256,872</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">384,213</td>
<td align="right">191,701</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">261,008</td>
<td align="right">130,256</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">257,693</td>
<td align="right">128,772</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">256,478</td>
<td align="right">128,221</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">387,681</td>
<td align="right">193,893</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,379</td>
<td align="right">1,227</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">10,827</td>
<td align="right">5,835</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">849</td>
<td align="right">465</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">680,323</td>
<td align="right">380,301</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,294</td>
<td align="right">761</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">43</td>
<td align="right">42</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">548</td>
<td align="right">547</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,809</td>
<td align="right">1,809</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,323</td>
<td align="right">1,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">399</td>
<td align="right">399</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">231</td>
<td align="right">231</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">168</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">147</td>
<td align="right">147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">147</td>
<td align="right">147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">105</td>
<td align="right">105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">105</td>
<td align="right">105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">42</td>
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
<td align="right">514,057</td>
<td align="right">4.6%</td>
<td align="right">256,137</td>
<td align="right">4.6%</td>
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
<td align="right">10,771,449</td>
<td align="right">95.4%</td>
<td align="right">5,367,671</td>
<td align="right">95.4%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">252</td>
<td align="right">0.0%</td>
<td align="right">252</td>
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
<td align="right">633</td>
<td align="right">71.5%</td>
<td align="right">504</td>
<td align="right">66.7%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">252</td>
<td align="right">28.5%</td>
<td align="right">252</td>
<td align="right">33.3%</td>
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
<td align="left">remainder</td>
<td align="right">337</td>
<td align="right">53.2%</td>
<td align="right">252</td>
<td align="right">50.0%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">232</td>
<td align="right">36.7%</td>
<td align="right">189</td>
<td align="right">37.5%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">64</td>
<td align="right">10.1%</td>
<td align="right">63</td>
<td align="right">12.5%</td>
<td align="right">-1.6%</td>
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
<td align="right">770,949</td>
<td align="right">100.0%</td>
<td align="right">384,005</td>
<td align="right">100.0%</td>
<td align="right">-50.2%</td>
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
<td align="right">31,814,268</td>
<td align="right">100.0%</td>
<td align="right">15,847,925</td>
<td align="right">100.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,494</td>
<td align="right">0.0%</td>
<td align="right">1,494</td>
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
<td align="right">1,008</td>
<td align="right">0.0%</td>
<td align="right">1,008</td>
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
<td align="right">1,323</td>
<td align="right">100.0%</td>
<td align="right">1,323</td>
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
<td align="right">42</td>
<td align="right">42 / 0 !!</td>
<td align="right">42</td>
<td align="right">42 / 0 !!</td>
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
<td align="right">63</td>
<td align="right">27.3%</td>
<td align="right">63</td>
<td align="right">27.3%</td>
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
<td align="right">168</td>
<td align="right">100.0%</td>
<td align="right">168</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,739,372</td>
<td align="right">94.8%</td>
<td align="right">2,361,131</td>
<td align="right">94.8%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">260,289</td>
<td align="right">5.2%</td>
<td align="right">129,729</td>
<td align="right">5.2%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">614</td>
<td align="right">85.4%</td>
<td align="right">422</td>
<td align="right">80.1%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">105</td>
<td align="right">14.6%</td>
<td align="right">105</td>
<td align="right">19.9%</td>
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
<td align="right">614</td>
<td align="right">100.0%</td>
<td align="right">422</td>
<td align="right">100.0%</td>
<td align="right">-31.3%</td>
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
<td align="right">2,182,452</td>
<td align="right">47.3%</td>
<td align="right">1,087,284</td>
<td align="right">47.3%</td>
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
<td align="right">2,430,522</td>
<td align="right">52.7%</td>
<td align="right">1,210,938</td>
<td align="right">52.7%</td>
<td align="right">-50.2%</td>
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
<td align="right">1,837</td>
<td align="right">97.8%</td>
<td align="right">1,471</td>
<td align="right">97.2%</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">42</td>
<td align="right">2.2%</td>
<td align="right">42</td>
<td align="right">2.8%</td>
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
<td align="right">1,393</td>
<td align="right">75.8%</td>
<td align="right">1,093</td>
<td align="right">74.3%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">127</td>
<td align="right">6.9%</td>
<td align="right">105</td>
<td align="right">7.1%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">317</td>
<td align="right">17.3%</td>
<td align="right">273</td>
<td align="right">18.6%</td>
<td align="right">-13.9%</td>
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
<td align="right">3,139,656</td>
<td align="right">80.2%</td>
<td align="right">1,117,573</td>
<td align="right">74.3%</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">774,371</td>
<td align="right">19.8%</td>
<td align="right">385,762</td>
<td align="right">25.6%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">336</td>
<td align="right">0.0%</td>
<td align="right">336</td>
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
<td align="right">615</td>
<td align="right">83.0%</td>
<td align="right">485</td>
<td align="right">79.4%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">126</td>
<td align="right">17.0%</td>
<td align="right">126</td>
<td align="right">20.6%</td>
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
<td align="left">ascii string</td>
<td align="right">63</td>
<td align="right">10.2%</td>
<td align="right">42</td>
<td align="right">8.7%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">318</td>
<td align="right">51.7%</td>
<td align="right">232</td>
<td align="right">47.8%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">85</td>
<td align="right">13.8%</td>
<td align="right">64</td>
<td align="right">13.2%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">128</td>
<td align="right">20.8%</td>
<td align="right">126</td>
<td align="right">26.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">21</td>
<td align="right">3.4%</td>
<td align="right">21</td>
<td align="right">4.3%</td>
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
<td align="left">self</td>
<td align="right">1,020</td>
<td align="right">1,020 / 0 !!</td>
<td align="right">508</td>
<td align="right">508 / 0 !!</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">765</td>
<td align="right">765 / 0 !!</td>
<td align="right">381</td>
<td align="right">381 / 0 !!</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">510</td>
<td align="right">510 / 0 !!</td>
<td align="right">254</td>
<td align="right">254 / 0 !!</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">257,316</td>
<td align="right">257,316 / 0 !!</td>
<td align="right">128,164</td>
<td align="right">128,164 / 0 !!</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,540,155</td>
<td align="right">1,540,155 / 0 !!</td>
<td align="right">767,163</td>
<td align="right">767,163 / 0 !!</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,041</td>
<td align="right">1,041 / 0 !!</td>
<td align="right">529</td>
<td align="right">529 / 0 !!</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,844</td>
<td align="right">3,844 / 0 !!</td>
<td align="right">2,051</td>
<td align="right">2,051 / 0 !!</td>
<td align="right">-46.6%</td>
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
<td align="right">43,294,684</td>
<td align="right">93.0%</td>
<td align="right">21,558,526</td>
<td align="right">93.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,198,857</td>
<td align="right">6.9%</td>
<td align="right">1,593,736</td>
<td align="right">6.9%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">37,555</td>
<td align="right">0.1%</td>
<td align="right">26,075</td>
<td align="right">0.1%</td>
<td align="right">-30.6%</td>
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
<td align="right">1,567</td>
<td align="right">49.5%</td>
<td align="right">1,181</td>
<td align="right">43.2%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,597</td>
<td align="right">50.5%</td>
<td align="right">1,554</td>
<td align="right">56.8%</td>
<td align="right">-2.7%</td>
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
<td align="left">mutable class</td>
<td align="right">212</td>
<td align="right">13.5%</td>
<td align="right">148</td>
<td align="right">12.5%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">212</td>
<td align="right">13.5%</td>
<td align="right">148</td>
<td align="right">12.5%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">212</td>
<td align="right">13.5%</td>
<td align="right">148</td>
<td align="right">12.5%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">697</td>
<td align="right">44.5%</td>
<td align="right">568</td>
<td align="right">48.1%</td>
<td align="right">-18.5%</td>
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
<td align="right">29,713,311</td>
<td align="right">100.0%</td>
<td align="right">14,640,834</td>
<td align="right">100.0%</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,265</td>
<td align="right">0.0%</td>
<td align="right">1,497</td>
<td align="right">0.0%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">294</td>
<td align="right">0.0%</td>
<td align="right">294</td>
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
<td align="right">735</td>
<td align="right">0.0%</td>
<td align="right">735</td>
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
<td align="right">1,050</td>
<td align="right">100.0%</td>
<td align="right">1,050</td>
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
<td align="right">513,060</td>
<td align="right">100.0%</td>
<td align="right">255,524</td>
<td align="right">100.0%</td>
<td align="right">-50.2%</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
<td align="right">42</td>
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
<td align="right">7,650</td>
<td align="right">0.1%</td>
<td align="right">3,810</td>
<td align="right">0.1%</td>
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
<td align="right">12,798,645</td>
<td align="right">99.9%</td>
<td align="right">6,374,965</td>
<td align="right">99.9%</td>
<td align="right">-50.2%</td>
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
<td align="right">399</td>
<td align="right">100.0%</td>
<td align="right">399</td>
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
<td align="right">648,144</td>
<td align="right">99.8%</td>
<td align="right">322,896</td>
<td align="right">99.8%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,188</td>
<td align="right">0.2%</td>
<td align="right">676</td>
<td align="right">0.2%</td>
<td align="right">-43.1%</td>
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
<td align="right">85</td>
<td align="right">80.2%</td>
<td align="right">64</td>
<td align="right">75.3%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">21</td>
<td align="right">19.8%</td>
<td align="right">21</td>
<td align="right">24.7%</td>
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
<td align="left">list slice</td>
<td align="right">85</td>
<td align="right">100.0%</td>
<td align="right">64</td>
<td align="right">100.0%</td>
<td align="right">-24.7%</td>
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
<td align="right">14,626,127</td>
<td align="right">98.3%</td>
<td align="right">7,285,966</td>
<td align="right">98.3%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">257,123</td>
<td align="right">1.7%</td>
<td align="right">128,226</td>
<td align="right">1.7%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">828</td>
<td align="right">0.0%</td>
<td align="right">444</td>
<td align="right">0.0%</td>
<td align="right">-46.4%</td>
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
<td align="right">318</td>
<td align="right">55.8%</td>
<td align="right">294</td>
<td align="right">53.8%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">252</td>
<td align="right">44.2%</td>
<td align="right">252</td>
<td align="right">46.2%</td>
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
<td align="left">tuple</td>
<td align="right">233</td>
<td align="right">73.3%</td>
<td align="right">210</td>
<td align="right">71.4%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">64</td>
<td align="right">20.1%</td>
<td align="right">63</td>
<td align="right">21.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">6.6%</td>
<td align="right">21</td>
<td align="right">7.1%</td>
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
<td align="right">1,918,544</td>
<td align="right">100.0%</td>
<td align="right">956,111</td>
<td align="right">100.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">84</td>
<td align="right">100.0%</td>
<td align="right">84</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">177,216,981</td>
<td align="right">36.5%</td>
<td align="right">86,204,722</td>
<td align="right">36.3%</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,700,910</td>
<td align="right">2.0%</td>
<td align="right">4,755,634</td>
<td align="right">2.0%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">298,200,011</td>
<td align="right">61.5%</td>
<td align="right">146,528,318</td>
<td align="right">61.7%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">50,425</td>
<td align="right">0.0%</td>
<td align="right">33,697</td>
<td align="right">0.0%</td>
<td align="right">-33.2%</td>
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
<td align="left">BINARY_SLICE</td>
<td align="right">770,949</td>
<td align="right">9.7%</td>
<td align="right">384,005</td>
<td align="right">9.7%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">774,371</td>
<td align="right">9.7%</td>
<td align="right">385,762</td>
<td align="right">9.7%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,182,452</td>
<td align="right">27.4%</td>
<td align="right">1,087,284</td>
<td align="right">27.4%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,198,857</td>
<td align="right">40.2%</td>
<td align="right">1,593,736</td>
<td align="right">40.2%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">514,057</td>
<td align="right">6.5%</td>
<td align="right">256,137</td>
<td align="right">6.5%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">260,289</td>
<td align="right">3.3%</td>
<td align="right">129,729</td>
<td align="right">3.3%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">257,123</td>
<td align="right">3.2%</td>
<td align="right">128,226</td>
<td align="right">3.2%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,188</td>
<td align="right">0.0%</td>
<td align="right">676</td>
<td align="right">0.0%</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,494</td>
<td align="right">0.0%</td>
<td align="right">1,494</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">294</td>
<td align="right">0.0%</td>
<td align="right">294</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,945</td>
<td align="right">19.5%</td>
<td align="right">4,953</td>
<td align="right">14.6%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">7,650</td>
<td align="right">15.0%</td>
<td align="right">3,810</td>
<td align="right">11.2%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">765</td>
<td align="right">1.5%</td>
<td align="right">381</td>
<td align="right">1.1%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">510</td>
<td align="right">1.0%</td>
<td align="right">254</td>
<td align="right">0.7%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">510</td>
<td align="right">1.0%</td>
<td align="right">254</td>
<td align="right">0.7%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,265</td>
<td align="right">4.4%</td>
<td align="right">1,497</td>
<td align="right">4.4%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">27,610</td>
<td align="right">54.2%</td>
<td align="right">21,122</td>
<td align="right">62.2%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,008</td>
<td align="right">2.0%</td>
<td align="right">1,008</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">336</td>
<td align="right">0.7%</td>
<td align="right">336</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">147</td>
<td align="right">0.3%</td>
<td align="right">147</td>
<td align="right">0.4%</td>
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
<td align="left">Frame objects created</td>
<td align="right">1,541,769</td>
<td align="right">8.3%</td>
<td align="right">768,009</td>
<td align="right">8.3%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">16,661,074</td>
<td align="right">89.7%</td>
<td align="right">8,299,597</td>
<td align="right">89.7%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">19,093,614</td>
<td align="right">102.8%</td>
<td align="right">9,511,656</td>
<td align="right">102.8%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,920,821</td>
<td align="right">10.3%</td>
<td align="right">957,108</td>
<td align="right">10.3%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,920,821</td>
<td align="right">10.3%</td>
<td align="right">957,108</td>
<td align="right">10.3%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,920,821</td>
<td align="right">10.3%</td>
<td align="right">957,108</td>
<td align="right">10.3%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,920,821</td>
<td align="right">10.3%</td>
<td align="right">957,108</td>
<td align="right">10.3%</td>
<td align="right">-50.2%</td>
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
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">1,270,071</td>
<td align="right"></td>
<td align="right">611,580</td>
<td align="right"></td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,272,328</td>
<td align="right"></td>
<td align="right">614,266</td>
<td align="right"></td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">116,053,711</td>
<td align="right">38.8%</td>
<td align="right">56,915,627</td>
<td align="right">38.2%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">140,066,906</td>
<td align="right">44.6%</td>
<td align="right">68,733,278</td>
<td align="right">43.9%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">20,040,009</td>
<td align="right">46.2%</td>
<td align="right">9,972,197</td>
<td align="right">46.1%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,630</td>
<td align="right">0.0%</td>
<td align="right">3,302</td>
<td align="right">0.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">510</td>
<td align="right">0.0%</td>
<td align="right">254</td>
<td align="right">0.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">13,090,067</td>
<td align="right">4.4%</td>
<td align="right">6,520,210</td>
<td align="right">4.4%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,280,289</td>
<td align="right"></td>
<td align="right">637,729</td>
<td align="right"></td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">23,345,037</td>
<td align="right"></td>
<td align="right">11,628,832</td>
<td align="right"></td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">20,062,538</td>
<td align="right"></td>
<td align="right">9,994,685</td>
<td align="right"></td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">6,273,055</td>
<td align="right"></td>
<td align="right">3,125,133</td>
<td align="right"></td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">2,312,730</td>
<td align="right">0.7%</td>
<td align="right">1,152,410</td>
<td align="right">0.7%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">73,333,051</td>
<td align="right">24.5%</td>
<td align="right">36,548,271</td>
<td align="right">24.5%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">62,942,698</td>
<td align="right">20.0%</td>
<td align="right">31,373,985</td>
<td align="right">20.1%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">23,367,844</td>
<td align="right">53.8%</td>
<td align="right">11,648,871</td>
<td align="right">53.9%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">23,091,214</td>
<td align="right">53.2%</td>
<td align="right">11,510,972</td>
<td align="right">53.2%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">270,000</td>
<td align="right">0.6%</td>
<td align="right">134,597</td>
<td align="right">0.6%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">9,533,483</td>
<td align="right"></td>
<td align="right">4,776,394</td>
<td align="right"></td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">96,481,924</td>
<td align="right">32.3%</td>
<td align="right">48,951,341</td>
<td align="right">32.9%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">108,670,031</td>
<td align="right">34.6%</td>
<td align="right">55,169,534</td>
<td align="right">35.3%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,347</td>
<td align="right"></td>
<td align="right">724</td>
<td align="right"></td>
<td align="right">-46.3%</td>
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
<td align="right">1,296</td>
<td align="right">2,045,733</td>
<td align="right">38,798,248</td>
<td align="right">731,930</td>
<td align="right">2,468,997</td>
<td align="right">656</td>
<td align="right">1,021,544</td>
<td align="right">17,774,162</td>
<td align="right">164,199</td>
<td align="right">1,232,415</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">66</td>
<td align="right">10.0%</td>
<td align="right">378</td>
<td align="right">33.3%</td>
<td align="right">472.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">660</td>
<td align="right"></td>
<td align="right">1,135</td>
<td align="right"></td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">384</td>
<td align="right">58.2%</td>
<td align="right">526</td>
<td align="right">46.3%</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">68,237,400</td>
<td align="right">8,888.9%</td>
<td align="right">46,481,302</td>
<td align="right">7,408.4%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">767,667</td>
<td align="right"></td>
<td align="right">627,414</td>
<td align="right"></td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">210</td>
<td align="right">31.8%</td>
<td align="right">231</td>
<td align="right">20.4%</td>
<td align="right">10.0%</td>
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

A potential trace is abandoned because it is too short.
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
<td align="right">210</td>
<td align="right"></td>
<td align="right">231</td>
<td align="right"></td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">210</td>
<td align="right">100.0%</td>
<td align="right">231</td>
<td align="right">100.0%</td>
<td align="right">10.0%</td>
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
<td align="right">1,757,952</td>
<td align="right">75.7%</td>
<td align="right">1,996,974</td>
<td align="right">77.4%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">48,384</td>
<td align="right">2.1%</td>
<td align="right">54,432</td>
<td align="right">2.1%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">2,322,432</td>
<td align="right"></td>
<td align="right">2,580,480</td>
<td align="right"></td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">516,096</td>
<td align="right">22.2%</td>
<td align="right">529,074</td>
<td align="right">20.5%</td>
<td align="right">2.5%</td>
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
<td align="left">126</td>
<td align="right">60.0%</td>
<td align="left">126</td>
<td align="right">54.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">63</td>
<td align="right">30.0%</td>
<td align="left">84</td>
<td align="right">36.4%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">21</td>
<td align="right">10.0%</td>
<td align="left">21</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
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
<td align="left"><= 32</td>
<td align="right">42</td>
<td align="right">20.0%</td>
<td align="right">42</td>
<td align="right">18.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">126</td>
<td align="right">60.0%</td>
<td align="right">126</td>
<td align="right">54.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">42</td>
<td align="right">20.0%</td>
<td align="right">63</td>
<td align="right">27.3%</td>
<td align="right">50.0%</td>
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
<td align="right">105</td>
<td align="right">50.0%</td>
<td align="right">105</td>
<td align="right">45.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">63</td>
<td align="right">30.0%</td>
<td align="right">84</td>
<td align="right">36.4%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">42</td>
<td align="right">20.0%</td>
<td align="right">42</td>
<td align="right">18.2%</td>
<td align="right">0.0%</td>
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
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">150</td>
<td align="right">274</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">84,378</td>
<td align="right">124,166</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">84,312</td>
<td align="right">124,060</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">84,462</td>
<td align="right">124,166</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">84,462</td>
<td align="right">124,166</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">84,462</td>
<td align="right">124,166</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">84,612</td>
<td align="right">124,272</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">41,586</td>
<td align="right">60,874</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">2,126,775</td>
<td align="right">1,261,715</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">850,710</td>
<td align="right">504,686</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">850,710</td>
<td align="right">504,686</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,701,420</td>
<td align="right">1,009,540</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">425,355</td>
<td align="right">252,385</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">425,355</td>
<td align="right">252,385</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">424,845</td>
<td align="right">252,089</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">424,845</td>
<td align="right">252,089</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">424,845</td>
<td align="right">252,089</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">850,710</td>
<td align="right">504,812</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,317,141</td>
<td align="right">817,649</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">296,505</td>
<td align="right">187,833</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">296,505</td>
<td align="right">187,833</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">592,200</td>
<td align="right">375,158</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">592,200</td>
<td align="right">375,158</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">592,200</td>
<td align="right">375,158</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">296,100</td>
<td align="right">187,579</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">296,100</td>
<td align="right">187,579</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">296,100</td>
<td align="right">187,579</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">296,100</td>
<td align="right">187,579</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1,485,240</td>
<td align="right">941,246</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">764,592</td>
<td align="right">501,894</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,399,801</td>
<td align="right">2,260,925</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">466,941</td>
<td align="right">313,217</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,803,866</td>
<td align="right">1,883,990</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,803,866</td>
<td align="right">1,883,990</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">935,322</td>
<td align="right">628,958</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">14,010,924</td>
<td align="right">9,533,068</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">12,776,982</td>
<td align="right">8,715,558</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,274,049</td>
<td align="right">878,129</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">2,252,907</td>
<td align="right">1,568,660</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">805,917</td>
<td align="right">564,088</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">805,473</td>
<td align="right">563,940</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,786,320</td>
<td align="right">1,255,442</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,786,320</td>
<td align="right">1,255,505</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">150</td>
<td align="right">106</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">150</td>
<td align="right">106</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">150</td>
<td align="right">106</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">150</td>
<td align="right">106</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">339,087</td>
<td align="right">249,277</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">339,087</td>
<td align="right">249,277</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">339,087</td>
<td align="right">249,277</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">339,087</td>
<td align="right">249,319</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">170,016</td>
<td align="right">125,216</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">170,016</td>
<td align="right">125,216</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">676,962</td>
<td align="right">499,536</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">1,441,488</td>
<td align="right">1,125,595</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">767,667</td>
<td align="right">627,414</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">767,667</td>
<td align="right">627,414</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">380,562</td>
<td align="right">311,745</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">422,259</td>
<td align="right">371,025</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">150</td>
<td align="right">148</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right"></td>
<td align="right">42</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right"></td>
<td align="right">42</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-02
