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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">752,275</td>
<td align="right">1,505,806</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,298,526</td>
<td align="right">2,597,831</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">12,476</td>
<td align="right">24,956</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">266,158</td>
<td align="right">532,398</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">29,112</td>
<td align="right">58,232</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">145,563</td>
<td align="right">291,163</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">228,743</td>
<td align="right">457,543</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">740,301</td>
<td align="right">1,480,781</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">973,206</td>
<td align="right">1,946,646</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">919,139</td>
<td align="right">1,838,499</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">365,992</td>
<td align="right">732,072</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">311,925</td>
<td align="right">623,925</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">241,222</td>
<td align="right">482,502</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">237,063</td>
<td align="right">474,183</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">224,586</td>
<td align="right">449,226</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">74,862</td>
<td align="right">149,742</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">66,544</td>
<td align="right">133,104</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">62,385</td>
<td align="right">124,785</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">54,067</td>
<td align="right">108,147</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">41,590</td>
<td align="right">83,190</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">33,272</td>
<td align="right">66,552</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">33,272</td>
<td align="right">66,552</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">33,272</td>
<td align="right">66,552</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">16,636</td>
<td align="right">33,276</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,464,450</td>
<td align="right">6,929,730</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">989,843</td>
<td align="right">1,979,923</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">723,667</td>
<td align="right">1,447,507</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,343,361</td>
<td align="right">2,687,041</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,301,771</td>
<td align="right">2,603,851</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">969,051</td>
<td align="right">1,938,331</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">969,051</td>
<td align="right">1,938,331</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">969,051</td>
<td align="right">1,938,331</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">690,397</td>
<td align="right">1,380,957</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">449,174</td>
<td align="right">898,454</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,031,437</td>
<td align="right">2,063,117</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">182,997</td>
<td align="right">366,037</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">282,815</td>
<td align="right">565,695</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">611,381</td>
<td align="right">1,222,901</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,264,354</td>
<td align="right">2,528,994</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,139,583</td>
<td align="right">2,279,423</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,555,495</td>
<td align="right">3,111,335</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">927,477</td>
<td align="right">1,855,157</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,507,932</td>
<td align="right">5,016,412</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">270,341</td>
<td align="right">540,741</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,213,704</td>
<td align="right">12,428,746</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,799,616</td>
<td align="right">9,600,257</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,532,901</td>
<td align="right">5,066,342</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,681,389</td>
<td align="right">15,364,358</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">224,594</td>
<td align="right">449,234</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">212,117</td>
<td align="right">424,277</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,901,309</td>
<td align="right">7,803,390</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,352,298</td>
<td align="right">6,705,259</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,579,842</td>
<td align="right">13,160,963</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,879,966</td>
<td align="right">3,760,288</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,720,531</td>
<td align="right">5,441,574</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,189,538</td>
<td align="right">2,379,298</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,231,132</td>
<td align="right">2,462,492</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">503,267</td>
<td align="right">1,006,627</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,850,861</td>
<td align="right">3,702,062</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">428,403</td>
<td align="right">856,883</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,027,337</td>
<td align="right">2,054,857</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,297,767</td>
<td align="right">16,596,972</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,102,828</td>
<td align="right">6,206,191</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">503,274</td>
<td align="right">1,006,634</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,988,144</td>
<td align="right">3,976,625</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">42,828,346</td>
<td align="right">85,663,889</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,372,694</td>
<td align="right">16,746,776</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">453,365</td>
<td align="right">906,805</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">906,732</td>
<td align="right">1,813,613</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">366,020</td>
<td align="right">732,100</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">103,983</td>
<td align="right">207,983</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">124,780</td>
<td align="right">249,580</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">898,418</td>
<td align="right">1,796,979</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,526,737</td>
<td align="right">7,054,033</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">10,123,890</td>
<td align="right">20,249,340</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,056,491</td>
<td align="right">2,113,132</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,600,989</td>
<td align="right">13,202,913</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,521,964</td>
<td align="right">13,044,850</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,850,882</td>
<td align="right">27,703,696</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,002,425</td>
<td align="right">2,004,986</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">74,870</td>
<td align="right">149,750</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,243,336</td>
<td align="right">12,487,502</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,534,842</td>
<td align="right">3,069,884</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,148,735</td>
<td align="right">6,297,857</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">574,012</td>
<td align="right">1,148,093</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">87,350</td>
<td align="right">174,710</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">87,350</td>
<td align="right">174,710</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,598,025</td>
<td align="right">7,196,430</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">316,132</td>
<td align="right">632,292</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">440,923</td>
<td align="right">881,884</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">445,083</td>
<td align="right">890,204</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,197,984</td>
<td align="right">2,396,066</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">203,825</td>
<td align="right">407,665</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">653,076</td>
<td align="right">1,306,197</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">465,889</td>
<td align="right">931,809</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">457,578</td>
<td align="right">915,179</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">311,995</td>
<td align="right">623,996</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">636,471</td>
<td align="right">1,272,952</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,458,610</td>
<td align="right">4,917,177</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">149,764</td>
<td align="right">299,524</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">245,451</td>
<td align="right">490,892</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">249,615</td>
<td align="right">499,215</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">137,293</td>
<td align="right">274,573</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">382,758</td>
<td align="right">765,479</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,244,038</td>
<td align="right">8,487,624</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">195,543</td>
<td align="right">391,064</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">520,063</td>
<td align="right">1,040,064</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">170,589</td>
<td align="right">341,150</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">851,291</td>
<td align="right">1,702,428</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,701</td>
<td align="right">191,381</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">657,466</td>
<td align="right">1,314,751</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">699,227</td>
<td align="right">1,398,182</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,194,578</td>
<td align="right">2,388,665</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">149,865</td>
<td align="right">299,625</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">54,138</td>
<td align="right">108,219</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">466,540</td>
<td align="right">932,516</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">275,255</td>
<td align="right">550,160</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">626,530</td>
<td align="right">1,251,996</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">41,707</td>
<td align="right">83,308</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">120,971</td>
<td align="right">241,616</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">186,089</td>
<td align="right">371,594</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">68</td>
<td align="right">69</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">437</td>
<td align="right">437</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">194</td>
<td align="right">194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">136</td>
<td align="right">136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">47</td>
<td align="right">47</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">36</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">34</td>
<td align="right">34</td>
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
<td align="right">465,838</td>
<td align="right">7.9%</td>
<td align="right">931,758</td>
<td align="right">7.9%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,419,626</td>
<td align="right">92.1%</td>
<td align="right">10,840,108</td>
<td align="right">92.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">8</td>
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
<td align="right">642</td>
<td align="right">91.5%</td>
<td align="right">698</td>
<td align="right">92.1%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">60</td>
<td align="right">8.5%</td>
<td align="right">60</td>
<td align="right">7.9%</td>
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
<td align="right">352</td>
<td align="right">54.8%</td>
<td align="right">402</td>
<td align="right">57.6%</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">95</td>
<td align="right">14.8%</td>
<td align="right">97</td>
<td align="right">13.9%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">96</td>
<td align="right">15.0%</td>
<td align="right">98</td>
<td align="right">14.0%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">99</td>
<td align="right">15.4%</td>
<td align="right">101</td>
<td align="right">14.5%</td>
<td align="right">2.0%</td>
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
<td align="right">611,381</td>
<td align="right">100.0%</td>
<td align="right">1,222,901</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
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
<td align="right">48,911</td>
<td align="right">0.3%</td>
<td align="right">98,883</td>
<td align="right">0.3%</td>
<td align="right">102.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">48,068</td>
<td align="right">0.3%</td>
<td align="right">97,088</td>
<td align="right">0.3%</td>
<td align="right">102.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,569,990</td>
<td align="right">99.7%</td>
<td align="right">31,141,777</td>
<td align="right">99.7%</td>
<td align="right">100.0%</td>
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
<td align="right">1,280</td>
<td align="right">100.0%</td>
<td align="right">2,232</td>
<td align="right">100.0%</td>
<td align="right">74.4%</td>
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
<td align="right">21</td>
<td align="right">44.7%</td>
<td align="right">21</td>
<td align="right">44.7%</td>
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
<td align="right">26</td>
<td align="right">100.0%</td>
<td align="right">26</td>
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
<td align="right">178,520</td>
<td align="right">8.5%</td>
<td align="right">357,168</td>
<td align="right">8.5%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,780,780</td>
<td align="right">85.0%</td>
<td align="right">3,561,975</td>
<td align="right">85.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">127,002</td>
<td align="right">6.1%</td>
<td align="right">253,585</td>
<td align="right">6.1%</td>
<td align="right">99.7%</td>
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
<td align="right">2,435</td>
<td align="right">24.3%</td>
<td align="right">4,741</td>
<td align="right">24.8%</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,573</td>
<td align="right">75.7%</td>
<td align="right">14,389</td>
<td align="right">75.2%</td>
<td align="right">90.0%</td>
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
<td align="right">7,573</td>
<td align="right">100.0%</td>
<td align="right">14,389</td>
<td align="right">100.0%</td>
<td align="right">90.0%</td>
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
<td align="right">1,193,673</td>
<td align="right">64.6%</td>
<td align="right">2,387,593</td>
<td align="right">64.6%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">652,999</td>
<td align="right">35.3%</td>
<td align="right">1,306,119</td>
<td align="right">35.4%</td>
<td align="right">100.0%</td>
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
<td align="right">897</td>
<td align="right">99.1%</td>
<td align="right">1,064</td>
<td align="right">99.3%</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8</td>
<td align="right">0.9%</td>
<td align="right">8</td>
<td align="right">0.7%</td>
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
<td align="right">122</td>
<td align="right">13.6%</td>
<td align="right">188</td>
<td align="right">17.7%</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">681</td>
<td align="right">75.9%</td>
<td align="right">780</td>
<td align="right">73.3%</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">94</td>
<td align="right">10.5%</td>
<td align="right">96</td>
<td align="right">9.0%</td>
<td align="right">2.1%</td>
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
<td align="right">4,267,265</td>
<td align="right">85.9%</td>
<td align="right">8,535,426</td>
<td align="right">85.9%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">698,793</td>
<td align="right">14.1%</td>
<td align="right">1,397,674</td>
<td align="right">14.1%</td>
<td align="right">100.0%</td>
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
<td align="right">425</td>
<td align="right">97.9%</td>
<td align="right">499</td>
<td align="right">98.2%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9</td>
<td align="right">2.1%</td>
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
<td align="left">enumerate</td>
<td align="right">120</td>
<td align="right">28.2%</td>
<td align="right">166</td>
<td align="right">33.3%</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">202</td>
<td align="right">47.5%</td>
<td align="right">227</td>
<td align="right">45.5%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">50</td>
<td align="right">11.8%</td>
<td align="right">52</td>
<td align="right">10.4%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">51</td>
<td align="right">12.0%</td>
<td align="right">52</td>
<td align="right">10.4%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
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
<td align="right">3,286,233</td>
<td align="right">16.0%</td>
<td align="right">6,580,416</td>
<td align="right">16.0%</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">624,075</td>
<td align="right">3.0%</td>
<td align="right">1,248,076</td>
<td align="right">3.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,669,303</td>
<td align="right">81.0%</td>
<td align="right">33,334,657</td>
<td align="right">81.0%</td>
<td align="right">100.0%</td>
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
<td align="right">62,297</td>
<td align="right">98.9%</td>
<td align="right">124,543</td>
<td align="right">99.4%</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">688</td>
<td align="right">1.1%</td>
<td align="right">702</td>
<td align="right">0.6%</td>
<td align="right">2.0%</td>
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
<td align="right">46</td>
<td align="right">6.7%</td>
<td align="right">47</td>
<td align="right">6.7%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">46</td>
<td align="right">6.7%</td>
<td align="right">47</td>
<td align="right">6.7%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">46</td>
<td align="right">6.7%</td>
<td align="right">47</td>
<td align="right">6.7%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">48</td>
<td align="right">7.0%</td>
<td align="right">49</td>
<td align="right">7.0%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">386</td>
<td align="right">56.1%</td>
<td align="right">394</td>
<td align="right">56.1%</td>
<td align="right">2.1%</td>
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
<td align="right">13,180,795</td>
<td align="right">100.0%</td>
<td align="right">26,363,840</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">26</td>
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
<td align="right">36</td>
<td align="right">0.0%</td>
<td align="right">36</td>
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
<td align="right">169</td>
<td align="right">100.0%</td>
<td align="right">169</td>
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
<td align="right">295,287</td>
<td align="right">100.0%</td>
<td align="right">590,647</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
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
<td align="right">2,217,354</td>
<td align="right">62.9%</td>
<td align="right">4,437,830</td>
<td align="right">62.9%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,309,383</td>
<td align="right">37.1%</td>
<td align="right">2,616,203</td>
<td align="right">37.1%</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
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
<td align="right">24,791</td>
<td align="right">100.0%</td>
<td align="right">49,367</td>
<td align="right">100.0%</td>
<td align="right">99.1%</td>
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
<td align="right">989,853</td>
<td align="right">94.8%</td>
<td align="right">1,979,933</td>
<td align="right">94.8%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">54,083</td>
<td align="right">5.2%</td>
<td align="right">108,163</td>
<td align="right">5.2%</td>
<td align="right">100.0%</td>
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
<td align="right">51</td>
<td align="right">92.7%</td>
<td align="right">52</td>
<td align="right">92.9%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4</td>
<td align="right">7.3%</td>
<td align="right">4</td>
<td align="right">7.1%</td>
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
<td align="right">51</td>
<td align="right">100.0%</td>
<td align="right">52</td>
<td align="right">100.0%</td>
<td align="right">2.0%</td>
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
<td align="right">89,111</td>
<td align="right">1.1%</td>
<td align="right">180,101</td>
<td align="right">1.2%</td>
<td align="right">102.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,544,588</td>
<td align="right">97.3%</td>
<td align="right">15,088,929</td>
<td align="right">97.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">120,710</td>
<td align="right">1.6%</td>
<td align="right">241,351</td>
<td align="right">1.6%</td>
<td align="right">99.9%</td>
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
<td align="right">1,716</td>
<td align="right">89.0%</td>
<td align="right">3,446</td>
<td align="right">94.1%</td>
<td align="right">100.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">213</td>
<td align="right">11.0%</td>
<td align="right">217</td>
<td align="right">5.9%</td>
<td align="right">1.9%</td>
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
<td align="right">142</td>
<td align="right">66.7%</td>
<td align="right">145</td>
<td align="right">66.8%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">50</td>
<td align="right">23.5%</td>
<td align="right">51</td>
<td align="right">23.5%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">9.9%</td>
<td align="right">21</td>
<td align="right">9.7%</td>
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
<td align="right">582,400</td>
<td align="right">100.0%</td>
<td align="right">1,164,801</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">4,861,021</td>
<td align="right">2.2%</td>
<td align="right">9,729,937</td>
<td align="right">2.2%</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">118,612,379</td>
<td align="right">53.8%</td>
<td align="right">237,243,181</td>
<td align="right">53.8%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">92,982,325</td>
<td align="right">42.2%</td>
<td align="right">185,973,784</td>
<td align="right">42.2%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">3,960,209</td>
<td align="right">1.8%</td>
<td align="right">7,916,444</td>
<td align="right">1.8%</td>
<td align="right">99.9%</td>
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
<td align="left">CALL</td>
<td align="right">48,068</td>
<td align="right">1.2%</td>
<td align="right">97,088</td>
<td align="right">1.2%</td>
<td align="right">102.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">178,520</td>
<td align="right">4.5%</td>
<td align="right">357,168</td>
<td align="right">4.5%</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">611,381</td>
<td align="right">15.3%</td>
<td align="right">1,222,901</td>
<td align="right">15.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,193,673</td>
<td align="right">29.9%</td>
<td align="right">2,387,593</td>
<td align="right">29.9%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">465,838</td>
<td align="right">11.7%</td>
<td align="right">931,758</td>
<td align="right">11.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">698,793</td>
<td align="right">17.5%</td>
<td align="right">1,397,674</td>
<td align="right">17.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">54,083</td>
<td align="right">1.4%</td>
<td align="right">108,163</td>
<td align="right">1.4%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">624,075</td>
<td align="right">15.6%</td>
<td align="right">1,248,076</td>
<td align="right">15.6%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">120,710</td>
<td align="right">3.0%</td>
<td align="right">241,351</td>
<td align="right">3.0%</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">26</td>
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
<td align="right">3,445</td>
<td align="right">0.1%</td>
<td align="right">8,003</td>
<td align="right">0.1%</td>
<td align="right">132.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">321</td>
<td align="right">0.0%</td>
<td align="right">689</td>
<td align="right">0.0%</td>
<td align="right">114.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">321</td>
<td align="right">0.0%</td>
<td align="right">689</td>
<td align="right">0.0%</td>
<td align="right">114.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">44,596</td>
<td align="right">0.9%</td>
<td align="right">90,351</td>
<td align="right">0.9%</td>
<td align="right">102.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">44,509</td>
<td align="right">0.9%</td>
<td align="right">89,744</td>
<td align="right">0.9%</td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">680,948</td>
<td align="right">14.0%</td>
<td align="right">1,368,706</td>
<td align="right">14.1%</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,605,285</td>
<td align="right">53.6%</td>
<td align="right">5,211,710</td>
<td align="right">53.6%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">45,464</td>
<td align="right">0.9%</td>
<td align="right">90,878</td>
<td align="right">0.9%</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,309,383</td>
<td align="right">26.9%</td>
<td align="right">2,616,203</td>
<td align="right">26.9%</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">127,002</td>
<td align="right">2.6%</td>
<td align="right">253,585</td>
<td align="right">2.6%</td>
<td align="right">99.7%</td>
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
<td align="right">873,406</td>
<td align="right">13.4%</td>
<td align="right">1,747,006</td>
<td align="right">13.4%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,018,634</td>
<td align="right">92.3%</td>
<td align="right">12,038,159</td>
<td align="right">92.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,609,334</td>
<td align="right">101.3%</td>
<td align="right">13,219,580</td>
<td align="right">101.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">503,350</td>
<td align="right">7.7%</td>
<td align="right">1,006,711</td>
<td align="right">7.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">503,350</td>
<td align="right">7.7%</td>
<td align="right">1,006,711</td>
<td align="right">7.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">503,350</td>
<td align="right">7.7%</td>
<td align="right">1,006,711</td>
<td align="right">7.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">503,350</td>
<td align="right">7.7%</td>
<td align="right">1,006,711</td>
<td align="right">7.7%</td>
<td align="right">100.0%</td>
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
<td align="right">38</td>
<td align="right">0.0%</td>
<td align="right">38</td>
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
<td align="left">Method cache hits</td>
<td align="right">6,047,560</td>
<td align="right"></td>
<td align="right">12,258,404</td>
<td align="right"></td>
<td align="right">102.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">1,418,086</td>
<td align="right"></td>
<td align="right">2,845,001</td>
<td align="right"></td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">11,341,850</td>
<td align="right"></td>
<td align="right">22,697,741</td>
<td align="right"></td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">40,777,393</td>
<td align="right">20.0%</td>
<td align="right">81,565,019</td>
<td align="right">20.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,385,975</td>
<td align="right">50.2%</td>
<td align="right">20,774,486</td>
<td align="right">50.2%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,452,519</td>
<td align="right">50.5%</td>
<td align="right">20,907,590</td>
<td align="right">50.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">66,544</td>
<td align="right">0.3%</td>
<td align="right">133,104</td>
<td align="right">0.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">41,590</td>
<td align="right">12.3%</td>
<td align="right">83,190</td>
<td align="right">12.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,227,241</td>
<td align="right"></td>
<td align="right">20,456,905</td>
<td align="right"></td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">336,891</td>
<td align="right"></td>
<td align="right">673,851</td>
<td align="right"></td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">29,925,125</td>
<td align="right">17.1%</td>
<td align="right">59,854,815</td>
<td align="right">17.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,227,817</td>
<td align="right">49.5%</td>
<td align="right">20,456,972</td>
<td align="right">49.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">98,744,616</td>
<td align="right">48.4%</td>
<td align="right">197,500,787</td>
<td align="right">48.4%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">84,184,462</td>
<td align="right">48.1%</td>
<td align="right">168,376,502</td>
<td align="right">48.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">34,441,018</td>
<td align="right">16.9%</td>
<td align="right">68,741,713</td>
<td align="right">16.9%</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">30,456,995</td>
<td align="right">17.4%</td>
<td align="right">60,762,692</td>
<td align="right">17.4%</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">30,451,139</td>
<td align="right">17.4%</td>
<td align="right">60,726,511</td>
<td align="right">17.4%</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">30,050,122</td>
<td align="right">14.7%</td>
<td align="right">59,909,853</td>
<td align="right">14.7%</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">309,867</td>
<td align="right"></td>
<td align="right">461,170</td>
<td align="right"></td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">315,480</td>
<td align="right"></td>
<td align="right">466,466</td>
<td align="right"></td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">8,739</td>
<td align="right"></td>
<td align="right">8,708</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">347</td>
<td align="right">702,513</td>
<td align="right">8,764,904</td>
<td align="right">54,904</td>
<td align="right">703,309</td>
<td align="right">694</td>
<td align="right">1,405,171</td>
<td align="right">17,679,792</td>
<td align="right">129,115</td>
<td align="right">1,406,962</td>
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
Stats gathered on: 2025-04-02
