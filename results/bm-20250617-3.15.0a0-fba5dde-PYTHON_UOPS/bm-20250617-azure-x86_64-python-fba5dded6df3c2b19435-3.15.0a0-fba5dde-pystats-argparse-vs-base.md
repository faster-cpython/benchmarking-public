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
<td align="right">5,515,642</td>
<td align="right">432,536</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">698,885</td>
<td align="right">223,129</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">324,447</td>
<td align="right">120,102</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,405,975</td>
<td align="right">576,620</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,597,316</td>
<td align="right">672,281</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,475,677</td>
<td align="right">1,954,695</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,388,704</td>
<td align="right">1,083,605</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">773,667</td>
<td align="right">359,025</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,047,222</td>
<td align="right">973,347</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,813,613</td>
<td align="right">878,970</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">26,489,122</td>
<td align="right">12,877,517</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">15,598,754</td>
<td align="right">7,589,151</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,279,423</td>
<td align="right">1,111,821</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">13,651,940</td>
<td align="right">6,661,453</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,726,762</td>
<td align="right">4,284,824</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,717,197</td>
<td align="right">2,316,369</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">550,160</td>
<td align="right">270,425</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,021,114</td>
<td align="right">5,909,016</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,224,334</td>
<td align="right">2,571,684</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,610,663</td>
<td align="right">1,777,458</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,354,520</td>
<td align="right">4,121,970</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">76,803,830</td>
<td align="right">37,964,743</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">25,224,352</td>
<td align="right">12,472,038</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">7,620,372</td>
<td align="right">3,769,827</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,006,601</td>
<td align="right">498,411</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">12,886,789</td>
<td align="right">6,387,419</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">6,597,341</td>
<td align="right">3,270,511</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,314,751</td>
<td align="right">652,636</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,004,879</td>
<td align="right">997,489</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">11,555,749</td>
<td align="right">5,749,743</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">407,665</td>
<td align="right">203,134</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,888,448</td>
<td align="right">7,928,909</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,006,611</td>
<td align="right">502,879</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,505,806</td>
<td align="right">752,275</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">990,031</td>
<td align="right">494,618</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,306,087</td>
<td align="right">652,560</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">632,292</td>
<td align="right">315,946</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">5,082,980</td>
<td align="right">2,540,342</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">765,479</td>
<td align="right">382,572</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,948,949</td>
<td align="right">974,124</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,272,952</td>
<td align="right">636,285</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,219,482</td>
<td align="right">1,609,376</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">24,956</td>
<td align="right">12,476</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,745,488</td>
<td align="right">3,872,151</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">831,882</td>
<td align="right">415,882</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">58,232</td>
<td align="right">29,112</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">457,543</td>
<td align="right">228,743</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">282,845</td>
<td align="right">141,405</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">723,752</td>
<td align="right">361,832</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,946,646</td>
<td align="right">973,206</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,006,599</td>
<td align="right">503,239</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">732,072</td>
<td align="right">365,992</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">623,925</td>
<td align="right">311,925</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">540,735</td>
<td align="right">270,335</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">482,502</td>
<td align="right">241,222</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">449,226</td>
<td align="right">224,586</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">149,742</td>
<td align="right">74,862</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">133,104</td>
<td align="right">66,544</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">124,785</td>
<td align="right">62,385</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">108,147</td>
<td align="right">54,067</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">83,190</td>
<td align="right">41,590</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">66,552</td>
<td align="right">33,272</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">49,914</td>
<td align="right">24,954</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,595</td>
<td align="right">20,795</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,447,507</td>
<td align="right">723,667</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,687,041</td>
<td align="right">1,343,361</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,380,957</td>
<td align="right">690,397</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,171,264</td>
<td align="right">1,085,504</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,613,890</td>
<td align="right">806,850</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,613,890</td>
<td align="right">806,850</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,613,890</td>
<td align="right">806,850</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">366,037</td>
<td align="right">182,997</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">565,695</td>
<td align="right">282,815</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,963,304</td>
<td align="right">981,544</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">449,234</td>
<td align="right">224,594</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">424,277</td>
<td align="right">212,117</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">906,789</td>
<td align="right">453,349</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">149,745</td>
<td align="right">74,865</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,741,058</td>
<td align="right">2,870,255</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">12,071,177</td>
<td align="right">6,035,016</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">965,030</td>
<td align="right">482,470</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,006,627</td>
<td align="right">503,267</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">732,096</td>
<td align="right">366,016</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,128,050</td>
<td align="right">1,563,889</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,838,563</td>
<td align="right">919,203</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">7,702,913</td>
<td align="right">3,851,137</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">906,805</td>
<td align="right">453,365</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,813,613</td>
<td align="right">906,732</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">207,983</td>
<td align="right">103,983</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,006,638</td>
<td align="right">503,278</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">249,580</td>
<td align="right">124,780</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,327,743</td>
<td align="right">1,663,742</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,113,132</td>
<td align="right">1,056,491</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,472,538</td>
<td align="right">736,217</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,029,943</td>
<td align="right">1,014,902</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">149,750</td>
<td align="right">74,870</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,329,441</td>
<td align="right">6,164,315</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,853,590</td>
<td align="right">1,426,708</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,156,412</td>
<td align="right">578,171</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">174,710</td>
<td align="right">87,350</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">174,710</td>
<td align="right">87,350</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">890,204</td>
<td align="right">445,083</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,306,197</td>
<td align="right">653,076</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">931,809</td>
<td align="right">465,889</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,071,625</td>
<td align="right">1,035,783</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">640,634</td>
<td align="right">320,313</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">299,524</td>
<td align="right">149,764</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">490,892</td>
<td align="right">245,451</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">499,212</td>
<td align="right">249,612</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">274,574</td>
<td align="right">137,294</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,702,603</td>
<td align="right">1,851,396</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">391,064</td>
<td align="right">195,543</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,040,064</td>
<td align="right">520,063</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">191,381</td>
<td align="right">95,701</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,486,134</td>
<td align="right">743,157</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">341,220</td>
<td align="right">170,660</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">166,486</td>
<td align="right">83,285</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">108,221</td>
<td align="right">54,140</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,252,013</td>
<td align="right">626,547</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">449,799</td>
<td align="right">225,149</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">83,307</td>
<td align="right">41,706</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">241,616</td>
<td align="right">120,971</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">371,592</td>
<td align="right">186,087</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">69</td>
<td align="right">68</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">439</td>
<td align="right">439</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">45</td>
<td align="right">45</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">39</td>
<td align="right">39</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">36</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">10</td>
<td align="right">10</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">7</td>
<td align="right">7</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">5</td>
<td align="right">5</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">1,865,220</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">377,383</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">42,566</td>
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
<td align="right">8,344,442</td>
<td align="right">94.9%</td>
<td align="right">4,045,459</td>
<td align="right">94.7%</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">449,254</td>
<td align="right">5.1%</td>
<td align="right">224,614</td>
<td align="right">5.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">13</td>
<td align="right">0.0%</td>
<td align="right">13</td>
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
<td align="right">485</td>
<td align="right">88.8%</td>
<td align="right">475</td>
<td align="right">88.6%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61</td>
<td align="right">11.2%</td>
<td align="right">61</td>
<td align="right">11.4%</td>
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
<td align="right">290</td>
<td align="right">59.8%</td>
<td align="right">284</td>
<td align="right">59.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">97</td>
<td align="right">20.0%</td>
<td align="right">95</td>
<td align="right">20.0%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">98</td>
<td align="right">20.2%</td>
<td align="right">96</td>
<td align="right">20.2%</td>
<td align="right">-2.0%</td>
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
<td align="right">1,006,611</td>
<td align="right">100.0%</td>
<td align="right">502,879</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
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
<td align="right">98,883</td>
<td align="right">0.3%</td>
<td align="right">48,911</td>
<td align="right">0.3%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">28,762,539</td>
<td align="right">99.7%</td>
<td align="right">14,228,922</td>
<td align="right">99.7%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">97,092</td>
<td align="right">0.3%</td>
<td align="right">48,072</td>
<td align="right">0.3%</td>
<td align="right">-50.5%</td>
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
<td align="right">2,230</td>
<td align="right">100.0%</td>
<td align="right">1,278</td>
<td align="right">100.0%</td>
<td align="right">-42.7%</td>
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
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
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
<td align="right">20</td>
<td align="right">44.4%</td>
<td align="right">20</td>
<td align="right">44.4%</td>
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
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">25</td>
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
<td align="right">357,167</td>
<td align="right">9.0%</td>
<td align="right">178,519</td>
<td align="right">9.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,345,681</td>
<td align="right">84.3%</td>
<td align="right">1,672,646</td>
<td align="right">84.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">253,585</td>
<td align="right">6.4%</td>
<td align="right">127,002</td>
<td align="right">6.4%</td>
<td align="right">-49.9%</td>
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
<td align="right">4,740</td>
<td align="right">24.8%</td>
<td align="right">2,434</td>
<td align="right">24.3%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">14,388</td>
<td align="right">75.2%</td>
<td align="right">7,572</td>
<td align="right">75.7%</td>
<td align="right">-47.4%</td>
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
<td align="right">14,388</td>
<td align="right">100.0%</td>
<td align="right">7,572</td>
<td align="right">100.0%</td>
<td align="right">-47.4%</td>
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
<td align="right">2,387,593</td>
<td align="right">62.8%</td>
<td align="right">1,082,625</td>
<td align="right">60.6%</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,414,266</td>
<td align="right">37.2%</td>
<td align="right">701,545</td>
<td align="right">39.3%</td>
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
<td align="left">Failure</td>
<td align="right">1,103</td>
<td align="right">99.3%</td>
<td align="right">972</td>
<td align="right">99.2%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8</td>
<td align="right">0.7%</td>
<td align="right">8</td>
<td align="right">0.8%</td>
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
<td align="right">125</td>
<td align="right">11.3%</td>
<td align="right">100</td>
<td align="right">10.3%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">882</td>
<td align="right">80.0%</td>
<td align="right">778</td>
<td align="right">80.0%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">96</td>
<td align="right">8.7%</td>
<td align="right">94</td>
<td align="right">9.7%</td>
<td align="right">-2.1%</td>
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
<td align="right">6,480,633</td>
<td align="right">76.0%</td>
<td align="right">2,830,368</td>
<td align="right">74.4%</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,046,556</td>
<td align="right">24.0%</td>
<td align="right">972,842</td>
<td align="right">25.6%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">16</td>
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
<td align="right">657</td>
<td align="right">98.6%</td>
<td align="right">496</td>
<td align="right">98.2%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9</td>
<td align="right">1.4%</td>
<td align="right">9</td>
<td align="right">1.8%</td>
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
<td align="right">158</td>
<td align="right">24.0%</td>
<td align="right">72</td>
<td align="right">14.5%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">166</td>
<td align="right">25.3%</td>
<td align="right">120</td>
<td align="right">24.2%</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">227</td>
<td align="right">34.6%</td>
<td align="right">201</td>
<td align="right">40.5%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">52</td>
<td align="right">7.9%</td>
<td align="right">50</td>
<td align="right">10.1%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">52</td>
<td align="right">7.9%</td>
<td align="right">51</td>
<td align="right">10.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2</td>
<td align="right">0.3%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
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
<td align="left">enumerate</td>
<td align="right">141,423</td>
<td align="right">141,423 / 0 !!</td>
<td align="right">70,703</td>
<td align="right">70,703 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">108,147</td>
<td align="right">108,147 / 0 !!</td>
<td align="right">54,067</td>
<td align="right">54,067 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">108,147</td>
<td align="right">108,147 / 0 !!</td>
<td align="right">54,067</td>
<td align="right">54,067 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">440,909</td>
<td align="right">440,909 / 0 !!</td>
<td align="right">220,429</td>
<td align="right">220,429 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">224,615</td>
<td align="right">224,615 / 0 !!</td>
<td align="right">112,295</td>
<td align="right">112,295 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,697,095</td>
<td align="right">1,697,095 / 0 !!</td>
<td align="right">848,455</td>
<td align="right">848,455 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">407,714</td>
<td align="right">407,714 / 0 !!</td>
<td align="right">203,873</td>
<td align="right">203,873 / 0 !!</td>
<td align="right">-50.0%</td>
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
<td align="right">31,155,071</td>
<td align="right">79.9%</td>
<td align="right">15,436,489</td>
<td align="right">79.8%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,580,416</td>
<td align="right">16.9%</td>
<td align="right">3,286,233</td>
<td align="right">17.0%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,248,084</td>
<td align="right">3.2%</td>
<td align="right">624,083</td>
<td align="right">3.2%</td>
<td align="right">-50.0%</td>
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
<td align="right">124,551</td>
<td align="right">99.4%</td>
<td align="right">62,305</td>
<td align="right">98.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">703</td>
<td align="right">0.6%</td>
<td align="right">689</td>
<td align="right">1.1%</td>
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
<td align="left">mutable class</td>
<td align="right">47</td>
<td align="right">6.7%</td>
<td align="right">46</td>
<td align="right">6.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">47</td>
<td align="right">6.7%</td>
<td align="right">46</td>
<td align="right">6.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">47</td>
<td align="right">6.7%</td>
<td align="right">46</td>
<td align="right">6.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">49</td>
<td align="right">7.0%</td>
<td align="right">48</td>
<td align="right">7.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">394</td>
<td align="right">56.0%</td>
<td align="right">386</td>
<td align="right">56.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
<td align="right">23,626,791</td>
<td align="right">100.0%</td>
<td align="right">11,784,624</td>
<td align="right">100.0%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27</td>
<td align="right">0.0%</td>
<td align="right">27</td>
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
<td align="right">35</td>
<td align="right">0.0%</td>
<td align="right">35</td>
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
<td align="right">135</td>
<td align="right">0.0%</td>
<td align="right">135</td>
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
<td align="right">590,647</td>
<td align="right">100.0%</td>
<td align="right">295,287</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
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
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">5</td>
<td align="right">100.0%</td>
<td align="right">5</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,086,710</td>
<td align="right">66.0%</td>
<td align="right">2,541,754</td>
<td align="right">66.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,616,203</td>
<td align="right">34.0%</td>
<td align="right">1,309,383</td>
<td align="right">34.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
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
<td align="right">49,370</td>
<td align="right">100.0%</td>
<td align="right">24,794</td>
<td align="right">100.0%</td>
<td align="right">-49.8%</td>
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
<td align="right">2,004,889</td>
<td align="right">94.9%</td>
<td align="right">997,499</td>
<td align="right">94.9%</td>
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
<td align="right">108,164</td>
<td align="right">5.1%</td>
<td align="right">54,084</td>
<td align="right">5.1%</td>
<td align="right">-50.0%</td>
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
<td align="right">52</td>
<td align="right">91.2%</td>
<td align="right">51</td>
<td align="right">91.1%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5</td>
<td align="right">8.8%</td>
<td align="right">5</td>
<td align="right">8.9%</td>
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
<td align="right">52</td>
<td align="right">100.0%</td>
<td align="right">51</td>
<td align="right">100.0%</td>
<td align="right">-1.9%</td>
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
<td align="right">13,500,000</td>
<td align="right">97.0%</td>
<td align="right">6,579,090</td>
<td align="right">96.9%</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">180,101</td>
<td align="right">1.3%</td>
<td align="right">89,111</td>
<td align="right">1.3%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">241,351</td>
<td align="right">1.7%</td>
<td align="right">120,710</td>
<td align="right">1.8%</td>
<td align="right">-50.0%</td>
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
<td align="right">3,446</td>
<td align="right">94.1%</td>
<td align="right">1,716</td>
<td align="right">89.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">217</td>
<td align="right">5.9%</td>
<td align="right">213</td>
<td align="right">11.0%</td>
<td align="right">-1.8%</td>
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
<td align="right">145</td>
<td align="right">66.8%</td>
<td align="right">142</td>
<td align="right">66.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">51</td>
<td align="right">23.5%</td>
<td align="right">50</td>
<td align="right">23.5%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">9.7%</td>
<td align="right">21</td>
<td align="right">9.9%</td>
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
<td align="right">1,164,801</td>
<td align="right">100.0%</td>
<td align="right">582,214</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
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
<td align="right">10,994,586</td>
<td align="right">2.6%</td>
<td align="right">5,337,372</td>
<td align="right">2.6%</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">147,439,056</td>
<td align="right">35.5%</td>
<td align="right">72,156,262</td>
<td align="right">35.2%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">247,543,017</td>
<td align="right">59.5%</td>
<td align="right">122,649,631</td>
<td align="right">59.8%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">9,730,049</td>
<td align="right">2.3%</td>
<td align="right">4,861,150</td>
<td align="right">2.4%</td>
<td align="right">-50.0%</td>
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
<td align="right">2,387,593</td>
<td align="right">30.1%</td>
<td align="right">1,082,625</td>
<td align="right">28.4%</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,046,556</td>
<td align="right">25.8%</td>
<td align="right">972,842</td>
<td align="right">25.5%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">97,092</td>
<td align="right">1.2%</td>
<td align="right">48,072</td>
<td align="right">1.3%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,006,611</td>
<td align="right">12.7%</td>
<td align="right">502,879</td>
<td align="right">13.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">357,167</td>
<td align="right">4.5%</td>
<td align="right">178,519</td>
<td align="right">4.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">449,254</td>
<td align="right">5.7%</td>
<td align="right">224,614</td>
<td align="right">5.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">108,164</td>
<td align="right">1.4%</td>
<td align="right">54,084</td>
<td align="right">1.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,248,084</td>
<td align="right">15.7%</td>
<td align="right">624,083</td>
<td align="right">16.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">241,351</td>
<td align="right">3.0%</td>
<td align="right">120,710</td>
<td align="right">3.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">27</td>
<td align="right">0.0%</td>
<td align="right">27</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">8,003</td>
<td align="right">0.1%</td>
<td align="right">3,445</td>
<td align="right">0.1%</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">90,351</td>
<td align="right">0.9%</td>
<td align="right">44,596</td>
<td align="right">0.9%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">89,744</td>
<td align="right">0.9%</td>
<td align="right">44,509</td>
<td align="right">0.9%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">697</td>
<td align="right">0.0%</td>
<td align="right">346</td>
<td align="right">0.0%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">697</td>
<td align="right">0.0%</td>
<td align="right">346</td>
<td align="right">0.0%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,368,706</td>
<td align="right">14.1%</td>
<td align="right">680,948</td>
<td align="right">14.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,211,710</td>
<td align="right">53.6%</td>
<td align="right">2,605,285</td>
<td align="right">53.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">90,878</td>
<td align="right">0.9%</td>
<td align="right">45,464</td>
<td align="right">0.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,616,203</td>
<td align="right">26.9%</td>
<td align="right">1,309,383</td>
<td align="right">26.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">253,585</td>
<td align="right">2.6%</td>
<td align="right">127,002</td>
<td align="right">2.6%</td>
<td align="right">-49.9%</td>
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
<td align="right">1,422,565</td>
<td align="right">11.0%</td>
<td align="right">711,205</td>
<td align="right">11.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">11,880,094</td>
<td align="right">92.2%</td>
<td align="right">5,939,609</td>
<td align="right">92.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">13,061,519</td>
<td align="right">101.4%</td>
<td align="right">6,530,313</td>
<td align="right">101.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,006,715</td>
<td align="right">7.8%</td>
<td align="right">503,354</td>
<td align="right">7.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,006,715</td>
<td align="right">7.8%</td>
<td align="right">503,354</td>
<td align="right">7.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,006,715</td>
<td align="right">7.8%</td>
<td align="right">503,354</td>
<td align="right">7.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,006,715</td>
<td align="right">7.8%</td>
<td align="right">503,354</td>
<td align="right">7.8%</td>
<td align="right">-50.0%</td>
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
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">8,134</td>
<td align="right"></td>
<td align="right">17,926</td>
<td align="right"></td>
<td align="right">120.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">467,164</td>
<td align="right"></td>
<td align="right">198,314</td>
<td align="right"></td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">472,872</td>
<td align="right"></td>
<td align="right">213,331</td>
<td align="right"></td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,228,152</td>
<td align="right"></td>
<td align="right">1,600,118</td>
<td align="right"></td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">18,284,945</td>
<td align="right"></td>
<td align="right">9,110,038</td>
<td align="right"></td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">64,702,143</td>
<td align="right">27.1%</td>
<td align="right">32,241,378</td>
<td align="right">27.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">59,382,462</td>
<td align="right">24.9%</td>
<td align="right">29,614,899</td>
<td align="right">24.8%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">61,190,429</td>
<td align="right">27.8%</td>
<td align="right">30,565,754</td>
<td align="right">27.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">62,282,556</td>
<td align="right">28.3%</td>
<td align="right">31,121,042</td>
<td align="right">28.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">17,933,527</td>
<td align="right"></td>
<td align="right">8,964,579</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">17,934,178</td>
<td align="right">51.8%</td>
<td align="right">8,965,548</td>
<td align="right">51.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">83,190</td>
<td align="right">12.3%</td>
<td align="right">41,590</td>
<td align="right">12.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">673,851</td>
<td align="right"></td>
<td align="right">336,891</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">112,897,588</td>
<td align="right">47.2%</td>
<td align="right">56,446,733</td>
<td align="right">47.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">86,027,496</td>
<td align="right">39.1%</td>
<td align="right">43,013,415</td>
<td align="right">39.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">16,584,032</td>
<td align="right">47.9%</td>
<td align="right">8,292,031</td>
<td align="right">47.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,978,748</td>
<td align="right">0.8%</td>
<td align="right">989,382</td>
<td align="right">0.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,717,136</td>
<td align="right">48.2%</td>
<td align="right">8,358,768</td>
<td align="right">48.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">10,799,863</td>
<td align="right">4.9%</td>
<td align="right">5,400,576</td>
<td align="right">4.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">133,104</td>
<td align="right">0.4%</td>
<td align="right">66,716</td>
<td align="right">0.4%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">13,450,369</td>
<td align="right"></td>
<td align="right">6,758,032</td>
<td align="right"></td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">758</td>
<td align="right">1,550,273</td>
<td align="right">20,409,149</td>
<td align="right">125,716</td>
<td align="right">1,552,302</td>
<td align="right">369</td>
<td align="right">754,651</td>
<td align="right">9,860,346</td>
<td align="right">52,172</td>
<td align="right">755,202</td>
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
Stats gathered on: 2025-06-18
