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
<td align="right">6,653,675</td>
<td align="right">648,804</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">536,581</td>
<td align="right">110,588</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">908,139</td>
<td align="right">191,323</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">743,485</td>
<td align="right">226,954</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">726,468</td>
<td align="right">239,705</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">2,360,994</td>
<td align="right">785,071</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,689,402</td>
<td align="right">565,042</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,443,548</td>
<td align="right">826,665</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,783,155</td>
<td align="right">624,305</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,977,820</td>
<td align="right">1,789,066</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,387,427</td>
<td align="right">527,852</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">759,591</td>
<td align="right">293,408</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,370,289</td>
<td align="right">947,252</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">206,383</td>
<td align="right">82,479</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,158,447</td>
<td align="right">2,570,772</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">619,196</td>
<td align="right">263,086</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,261,887</td>
<td align="right">969,267</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,263,160</td>
<td align="right">547,121</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">3,731,360</td>
<td align="right">1,643,004</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">470,535</td>
<td align="right">209,301</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,995,563</td>
<td align="right">1,795,874</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">16,469,292</td>
<td align="right">7,406,937</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,583,819</td>
<td align="right">1,175,049</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">16,617,944</td>
<td align="right">7,591,448</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,399,707</td>
<td align="right">2,483,548</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">27,490,576</td>
<td align="right">12,711,661</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,422,321</td>
<td align="right">3,904,554</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,101,345</td>
<td align="right">6,134,348</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,509,538</td>
<td align="right">1,181,971</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">12,944,498</td>
<td align="right">6,154,075</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">20,093,564</td>
<td align="right">9,628,768</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">85,004,881</td>
<td align="right">40,793,471</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,526,401</td>
<td align="right">4,579,773</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,333,130</td>
<td align="right">5,943,593</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">5,027,366</td>
<td align="right">2,437,346</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,879,353</td>
<td align="right">2,376,227</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">3,046,268</td>
<td align="right">1,492,548</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,246,166</td>
<td align="right">7,480,840</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,824,355</td>
<td align="right">897,992</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">545,920</td>
<td align="right">270,425</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">7,743,358</td>
<td align="right">3,852,808</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">6,876,418</td>
<td align="right">3,424,280</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">891,542</td>
<td align="right">444,344</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">6,249,409</td>
<td align="right">3,116,546</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">899,829</td>
<td align="right">449,124</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,039,049</td>
<td align="right">1,018,820</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,436,371</td>
<td align="right">718,153</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,304,639</td>
<td align="right">652,636</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,799,661</td>
<td align="right">901,218</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,141,070</td>
<td align="right">3,576,506</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,964,691</td>
<td align="right">985,013</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,577,854</td>
<td align="right">1,294,285</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">404,529</td>
<td align="right">203,134</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,059,715</td>
<td align="right">6,562,808</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">875,100</td>
<td align="right">440,551</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,494,231</td>
<td align="right">752,275</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,213,493</td>
<td align="right">611,009</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">627,428</td>
<td align="right">315,946</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,087,399</td>
<td align="right">1,555,309</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">24,764</td>
<td align="right">12,476</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">528,302</td>
<td align="right">266,158</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">57,784</td>
<td align="right">29,112</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">288,923</td>
<td align="right">145,563</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">454,023</td>
<td align="right">228,743</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">1,469,389</td>
<td align="right">740,301</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,931,670</td>
<td align="right">973,206</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">726,440</td>
<td align="right">365,992</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">619,125</td>
<td align="right">311,925</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">478,790</td>
<td align="right">241,222</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">445,770</td>
<td align="right">224,586</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">148,590</td>
<td align="right">74,862</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">132,080</td>
<td align="right">66,544</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">123,825</td>
<td align="right">62,385</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">107,315</td>
<td align="right">54,067</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">82,550</td>
<td align="right">41,590</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">66,040</td>
<td align="right">33,272</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">66,040</td>
<td align="right">33,272</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">66,040</td>
<td align="right">33,272</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">33,020</td>
<td align="right">16,636</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,666,369</td>
<td align="right">1,343,361</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,923,419</td>
<td align="right">969,051</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,923,419</td>
<td align="right">969,051</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,923,419</td>
<td align="right">969,051</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,370,333</td>
<td align="right">690,397</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,047,245</td>
<td align="right">1,031,437</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">363,221</td>
<td align="right">182,997</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">561,343</td>
<td align="right">282,815</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,840,885</td>
<td align="right">927,477</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">445,778</td>
<td align="right">224,594</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">421,013</td>
<td align="right">212,117</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">998,883</td>
<td align="right">503,267</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,673,582</td>
<td align="right">1,850,861</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">850,291</td>
<td align="right">428,403</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">998,890</td>
<td align="right">503,274</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,999,774</td>
<td align="right">3,526,737</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">247,660</td>
<td align="right">124,780</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,096,876</td>
<td align="right">1,056,491</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,989,562</td>
<td align="right">1,002,425</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">148,598</td>
<td align="right">74,870</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,391,438</td>
<td align="right">6,243,336</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,139,261</td>
<td align="right">574,012</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">173,366</td>
<td align="right">87,350</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">173,366</td>
<td align="right">87,350</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">883,356</td>
<td align="right">445,083</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,377,634</td>
<td align="right">1,197,984</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,296,149</td>
<td align="right">653,076</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">924,641</td>
<td align="right">465,889</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">297,220</td>
<td align="right">149,764</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">487,116</td>
<td align="right">245,451</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">495,375</td>
<td align="right">249,615</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">272,461</td>
<td align="right">137,293</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">388,056</td>
<td align="right">195,543</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,032,064</td>
<td align="right">520,063</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">338,526</td>
<td align="right">170,589</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">189,909</td>
<td align="right">95,701</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">297,310</td>
<td align="right">149,854</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">107,386</td>
<td align="right">54,138</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,242,372</td>
<td align="right">626,530</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">181,860</td>
<td align="right">91,745</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">82,668</td>
<td align="right">41,707</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">239,760</td>
<td align="right">120,971</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">368,658</td>
<td align="right">186,089</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">69</td>
<td align="right">68</td>
<td align="right">-1.4%</td>
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
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">1,420,534</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">1,140,867</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">198,938</td>
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
<td align="right">742,960</td>
<td align="right">9.9%</td>
<td align="right">226,522</td>
<td align="right">6.3%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,728,053</td>
<td align="right">90.0%</td>
<td align="right">3,389,812</td>
<td align="right">93.7%</td>
<td align="right">-49.6%</td>
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
<td align="right">497</td>
<td align="right">94.7%</td>
<td align="right">404</td>
<td align="right">93.5%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28</td>
<td align="right">5.3%</td>
<td align="right">28</td>
<td align="right">6.5%</td>
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
<td align="right">401</td>
<td align="right">80.7%</td>
<td align="right">309</td>
<td align="right">76.5%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">96</td>
<td align="right">19.3%</td>
<td align="right">95</td>
<td align="right">23.5%</td>
<td align="right">-1.0%</td>
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
<td align="right">1,213,493</td>
<td align="right">100.0%</td>
<td align="right">611,009</td>
<td align="right">100.0%</td>
<td align="right">-49.6%</td>
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
<td align="right">4,028,663</td>
<td align="right">95.7%</td>
<td align="right">2,029,814</td>
<td align="right">95.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">181,630</td>
<td align="right">4.3%</td>
<td align="right">91,518</td>
<td align="right">4.3%</td>
<td align="right">-49.6%</td>
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
<td align="right">198</td>
<td align="right">86.1%</td>
<td align="right">195</td>
<td align="right">85.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">32</td>
<td align="right">13.9%</td>
<td align="right">32</td>
<td align="right">14.1%</td>
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
<td align="left">string slice</td>
<td align="right">98</td>
<td align="right">49.5%</td>
<td align="right">96</td>
<td align="right">49.2%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">100</td>
<td align="right">50.5%</td>
<td align="right">99</td>
<td align="right">50.8%</td>
<td align="right">-1.0%</td>
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
<td align="right">98,131</td>
<td align="right">0.3%</td>
<td align="right">48,911</td>
<td align="right">0.3%</td>
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
<td align="right">96,350</td>
<td align="right">0.3%</td>
<td align="right">48,068</td>
<td align="right">0.3%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">30,902,195</td>
<td align="right">99.7%</td>
<td align="right">15,569,990</td>
<td align="right">99.7%</td>
<td align="right">-49.6%</td>
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
<td align="right">2,218</td>
<td align="right">100.0%</td>
<td align="right">1,280</td>
<td align="right">100.0%</td>
<td align="right">-42.3%</td>
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
<td align="right">354,347</td>
<td align="right">8.5%</td>
<td align="right">178,520</td>
<td align="right">8.5%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,534,594</td>
<td align="right">85.1%</td>
<td align="right">1,780,780</td>
<td align="right">85.0%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">251,684</td>
<td align="right">6.1%</td>
<td align="right">127,002</td>
<td align="right">6.1%</td>
<td align="right">-49.5%</td>
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
<td align="right">4,701</td>
<td align="right">24.8%</td>
<td align="right">2,435</td>
<td align="right">24.3%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">14,275</td>
<td align="right">75.2%</td>
<td align="right">7,573</td>
<td align="right">75.7%</td>
<td align="right">-46.9%</td>
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
<td align="right">14,275</td>
<td align="right">100.0%</td>
<td align="right">7,573</td>
<td align="right">100.0%</td>
<td align="right">-46.9%</td>
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
<td align="right">2,369,225</td>
<td align="right">64.6%</td>
<td align="right">946,393</td>
<td align="right">59.1%</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,296,071</td>
<td align="right">35.4%</td>
<td align="right">652,999</td>
<td align="right">40.8%</td>
<td align="right">-49.6%</td>
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
<td align="right">1,056</td>
<td align="right">99.2%</td>
<td align="right">851</td>
<td align="right">99.1%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8</td>
<td align="right">0.8%</td>
<td align="right">8</td>
<td align="right">0.9%</td>
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
<td align="right">186</td>
<td align="right">17.6%</td>
<td align="right">79</td>
<td align="right">9.3%</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">774</td>
<td align="right">73.3%</td>
<td align="right">678</td>
<td align="right">79.7%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">96</td>
<td align="right">9.1%</td>
<td align="right">94</td>
<td align="right">11.0%</td>
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
<td align="right">8,469,762</td>
<td align="right">85.9%</td>
<td align="right">3,155,422</td>
<td align="right">85.7%</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,386,922</td>
<td align="right">14.1%</td>
<td align="right">527,461</td>
<td align="right">14.3%</td>
<td align="right">-62.0%</td>
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
<td align="right">496</td>
<td align="right">98.2%</td>
<td align="right">382</td>
<td align="right">97.7%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9</td>
<td align="right">1.8%</td>
<td align="right">9</td>
<td align="right">2.3%</td>
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
<td align="right">164</td>
<td align="right">33.1%</td>
<td align="right">78</td>
<td align="right">20.4%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">227</td>
<td align="right">45.8%</td>
<td align="right">201</td>
<td align="right">52.6%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">51</td>
<td align="right">10.3%</td>
<td align="right">50</td>
<td align="right">13.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">52</td>
<td align="right">10.5%</td>
<td align="right">51</td>
<td align="right">13.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">33,078,231</td>
<td align="right">81.0%</td>
<td align="right">16,165,009</td>
<td align="right">80.5%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,529,775</td>
<td align="right">16.0%</td>
<td align="right">3,286,233</td>
<td align="right">16.4%</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,238,476</td>
<td align="right">3.0%</td>
<td align="right">624,075</td>
<td align="right">3.1%</td>
<td align="right">-49.6%</td>
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
<td align="right">123,588</td>
<td align="right">99.4%</td>
<td align="right">62,297</td>
<td align="right">98.9%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">700</td>
<td align="right">0.6%</td>
<td align="right">688</td>
<td align="right">1.1%</td>
<td align="right">-1.7%</td>
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
<td align="right">392</td>
<td align="right">56.0%</td>
<td align="right">386</td>
<td align="right">56.1%</td>
<td align="right">-1.5%</td>
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
<td align="right">26,161,024</td>
<td align="right">100.0%</td>
<td align="right">12,697,120</td>
<td align="right">100.0%</td>
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
<td align="right">586,103</td>
<td align="right">100.0%</td>
<td align="right">295,287</td>
<td align="right">100.0%</td>
<td align="right">-49.6%</td>
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
<td align="right">4,403,697</td>
<td align="right">62.9%</td>
<td align="right">2,217,354</td>
<td align="right">62.9%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,596,077</td>
<td align="right">37.1%</td>
<td align="right">1,309,383</td>
<td align="right">37.1%</td>
<td align="right">-49.6%</td>
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
<td align="right">48,996</td>
<td align="right">100.0%</td>
<td align="right">24,791</td>
<td align="right">100.0%</td>
<td align="right">-49.4%</td>
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
<td align="right">1,964,701</td>
<td align="right">94.8%</td>
<td align="right">989,853</td>
<td align="right">94.8%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">107,331</td>
<td align="right">5.2%</td>
<td align="right">54,083</td>
<td align="right">5.2%</td>
<td align="right">-49.6%</td>
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
<td align="right">4</td>
<td align="right">7.3%</td>
<td align="right">4</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">51</td>
<td align="right">92.7%</td>
<td align="right">51</td>
<td align="right">92.7%</td>
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
<td align="right">51</td>
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
<td align="right">178,732</td>
<td align="right">1.2%</td>
<td align="right">89,111</td>
<td align="right">1.1%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,972,833</td>
<td align="right">97.3%</td>
<td align="right">7,544,588</td>
<td align="right">97.3%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">239,495</td>
<td align="right">1.6%</td>
<td align="right">120,710</td>
<td align="right">1.6%</td>
<td align="right">-49.6%</td>
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
<td align="right">3,421</td>
<td align="right">94.0%</td>
<td align="right">1,716</td>
<td align="right">89.0%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">217</td>
<td align="right">6.0%</td>
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
<td align="right">1,155,841</td>
<td align="right">100.0%</td>
<td align="right">582,400</td>
<td align="right">100.0%</td>
<td align="right">-49.6%</td>
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
<td align="right">7,855,485</td>
<td align="right">1.8%</td>
<td align="right">3,393,295</td>
<td align="right">1.6%</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">184,543,133</td>
<td align="right">42.2%</td>
<td align="right">85,385,369</td>
<td align="right">41.1%</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">235,467,612</td>
<td align="right">53.8%</td>
<td align="right">114,115,879</td>
<td align="right">54.9%</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">9,655,125</td>
<td align="right">2.2%</td>
<td align="right">4,860,874</td>
<td align="right">2.3%</td>
<td align="right">-49.7%</td>
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
<td align="right">742,960</td>
<td align="right">9.4%</td>
<td align="right">226,522</td>
<td align="right">6.6%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,386,922</td>
<td align="right">17.5%</td>
<td align="right">527,461</td>
<td align="right">15.4%</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,369,225</td>
<td align="right">29.9%</td>
<td align="right">946,393</td>
<td align="right">27.6%</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">96,350</td>
<td align="right">1.2%</td>
<td align="right">48,068</td>
<td align="right">1.4%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,213,493</td>
<td align="right">15.3%</td>
<td align="right">611,009</td>
<td align="right">17.8%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">354,347</td>
<td align="right">4.5%</td>
<td align="right">178,520</td>
<td align="right">5.2%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">181,630</td>
<td align="right">2.3%</td>
<td align="right">91,518</td>
<td align="right">2.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">107,331</td>
<td align="right">1.4%</td>
<td align="right">54,083</td>
<td align="right">1.6%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,238,476</td>
<td align="right">15.6%</td>
<td align="right">624,075</td>
<td align="right">18.2%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">239,495</td>
<td align="right">3.0%</td>
<td align="right">120,710</td>
<td align="right">3.5%</td>
<td align="right">-49.6%</td>
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
<td align="left">RESUME</td>
<td align="right">666</td>
<td align="right">0.0%</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">666</td>
<td align="right">0.0%</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">7,950</td>
<td align="right">0.1%</td>
<td align="right">3,445</td>
<td align="right">0.1%</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">89,668</td>
<td align="right">0.9%</td>
<td align="right">44,596</td>
<td align="right">0.9%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">89,058</td>
<td align="right">0.9%</td>
<td align="right">44,509</td>
<td align="right">0.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,358,171</td>
<td align="right">14.1%</td>
<td align="right">680,948</td>
<td align="right">14.0%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,171,604</td>
<td align="right">53.6%</td>
<td align="right">2,605,285</td>
<td align="right">53.6%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">90,179</td>
<td align="right">0.9%</td>
<td align="right">45,464</td>
<td align="right">0.9%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,596,077</td>
<td align="right">26.9%</td>
<td align="right">1,309,383</td>
<td align="right">26.9%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">251,684</td>
<td align="right">2.6%</td>
<td align="right">127,002</td>
<td align="right">2.6%</td>
<td align="right">-49.5%</td>
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
<td align="right">1,733,566</td>
<td align="right">13.4%</td>
<td align="right">873,406</td>
<td align="right">13.4%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">11,945,551</td>
<td align="right">92.3%</td>
<td align="right">6,018,634</td>
<td align="right">92.3%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">13,117,884</td>
<td align="right">101.3%</td>
<td align="right">6,609,334</td>
<td align="right">101.3%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">998,967</td>
<td align="right">7.7%</td>
<td align="right">503,350</td>
<td align="right">7.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">998,967</td>
<td align="right">7.7%</td>
<td align="right">503,350</td>
<td align="right">7.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">998,967</td>
<td align="right">7.7%</td>
<td align="right">503,350</td>
<td align="right">7.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">998,967</td>
<td align="right">7.7%</td>
<td align="right">503,350</td>
<td align="right">7.7%</td>
<td align="right">-49.6%</td>
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
<td align="left">Interpreter immortal increfs</td>
<td align="right">59,394,364</td>
<td align="right">17.1%</td>
<td align="right">28,115,130</td>
<td align="right">15.9%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">80,937,583</td>
<td align="right">20.0%</td>
<td align="right">38,598,173</td>
<td align="right">18.6%</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">167,081,199</td>
<td align="right">48.2%</td>
<td align="right">79,829,663</td>
<td align="right">45.1%</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">195,981,367</td>
<td align="right">48.5%</td>
<td align="right">96,296,448</td>
<td align="right">46.5%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">22,977</td>
<td align="right"></td>
<td align="right">34,664</td>
<td align="right"></td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,808,581</td>
<td align="right"></td>
<td align="right">1,391,966</td>
<td align="right"></td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">12,238,569</td>
<td align="right"></td>
<td align="right">6,078,189</td>
<td align="right"></td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">22,516,098</td>
<td align="right"></td>
<td align="right">11,336,370</td>
<td align="right"></td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">20,614,526</td>
<td align="right">50.2%</td>
<td align="right">10,385,764</td>
<td align="right">50.2%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">82,550</td>
<td align="right">12.3%</td>
<td align="right">41,590</td>
<td align="right">12.3%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">20,299,651</td>
<td align="right"></td>
<td align="right">10,227,359</td>
<td align="right"></td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">20,746,606</td>
<td align="right">50.5%</td>
<td align="right">10,452,651</td>
<td align="right">50.5%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">668,667</td>
<td align="right"></td>
<td align="right">336,891</td>
<td align="right"></td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">20,299,735</td>
<td align="right">49.5%</td>
<td align="right">10,228,050</td>
<td align="right">49.5%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">132,080</td>
<td align="right">0.3%</td>
<td align="right">66,866</td>
<td align="right">0.3%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">60,202,772</td>
<td align="right">17.4%</td>
<td align="right">32,243,535</td>
<td align="right">18.2%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">59,395,470</td>
<td align="right">14.7%</td>
<td align="right">33,370,107</td>
<td align="right">16.1%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">68,140,159</td>
<td align="right">16.8%</td>
<td align="right">38,840,662</td>
<td align="right">18.8%</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">60,230,798</td>
<td align="right">17.4%</td>
<td align="right">36,768,704</td>
<td align="right">20.8%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">383,142</td>
<td align="right"></td>
<td align="right">279,238</td>
<td align="right"></td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">400,181</td>
<td align="right"></td>
<td align="right">308,377</td>
<td align="right"></td>
<td align="right">-22.9%</td>
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
<td align="right">688</td>
<td align="right">1,393,541</td>
<td align="right">17,385,200</td>
<td align="right">109,611</td>
<td align="right">1,394,438</td>
<td align="right">347</td>
<td align="right">702,334</td>
<td align="right">8,761,312</td>
<td align="right">53,508</td>
<td align="right">703,815</td>
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
Stats gathered on: 2025-02-06
