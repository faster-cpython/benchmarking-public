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
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2,042</td>
<td align="right">726,694</td>
<td align="right">35,487.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">745,837</td>
<td align="right">12,358,860</td>
<td align="right">1,557.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">28,762</td>
<td align="right">214,405</td>
<td align="right">645.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">10,987</td>
<td align="right">50,456</td>
<td align="right">359.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,139,658</td>
<td align="right">3,706,741</td>
<td align="right">225.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,392,990</td>
<td align="right">3,777,480</td>
<td align="right">171.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,348,579</td>
<td align="right">3,621,376</td>
<td align="right">168.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,053,043</td>
<td align="right">2,826,092</td>
<td align="right">168.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">479,984</td>
<td align="right">1,251,392</td>
<td align="right">160.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">508</td>
<td align="right">1,265</td>
<td align="right">149.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,566,102</td>
<td align="right">3,851,834</td>
<td align="right">146.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">330,001</td>
<td align="right">793,264</td>
<td align="right">140.4%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">36,510</td>
<td align="right">86,052</td>
<td align="right">135.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,030,724</td>
<td align="right">9,381,923</td>
<td align="right">132.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">226,118</td>
<td align="right">501,655</td>
<td align="right">121.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">125,668</td>
<td align="right">260,193</td>
<td align="right">107.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">585,023</td>
<td align="right">1,190,135</td>
<td align="right">103.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">818,449</td>
<td align="right">1,650,319</td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,766,983</td>
<td align="right">3,452,302</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,137,899</td>
<td align="right">2,221,242</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,291,848</td>
<td align="right">6,230,270</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">275,982</td>
<td align="right">518,208</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,164,093</td>
<td align="right">2,172,186</td>
<td align="right">86.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,263,943</td>
<td align="right">7,546,270</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">288,738</td>
<td align="right">475,255</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,313,231</td>
<td align="right">5,319,405</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">619,195</td>
<td align="right">977,590</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,106,126</td>
<td align="right">1,744,270</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">10,623,825</td>
<td align="right">16,676,176</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">71,392</td>
<td align="right">108,829</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,398,768</td>
<td align="right">2,094,634</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">23,116,604</td>
<td align="right">12,073,711</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">5,167,338</td>
<td align="right">7,605,405</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,540,517</td>
<td align="right">2,250,655</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,076,256</td>
<td align="right">2,978,252</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,487,066</td>
<td align="right">4,840,023</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,208</td>
<td align="right">3,031</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">215,379</td>
<td align="right">295,569</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,700,998</td>
<td align="right">14,677,760</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">422,412</td>
<td align="right">577,009</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">524</td>
<td align="right">714</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,878,516</td>
<td align="right">2,548,285</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">914,403</td>
<td align="right">1,234,955</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">231,151</td>
<td align="right">310,776</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,370,183</td>
<td align="right">4,515,393</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">316,819</td>
<td align="right">422,554</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,241,241</td>
<td align="right">2,969,202</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,123,373</td>
<td align="right">1,483,092</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,429,516</td>
<td align="right">4,493,486</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">31,271,546</td>
<td align="right">40,779,056</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,769,648</td>
<td align="right">28,265,811</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">31,863,062</td>
<td align="right">41,227,243</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">13,021,521</td>
<td align="right">16,576,501</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">19,572,026</td>
<td align="right">24,739,287</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">23,345,261</td>
<td align="right">29,153,163</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">135,754,678</td>
<td align="right">168,173,483</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,536,508</td>
<td align="right">5,616,896</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">5,899,637</td>
<td align="right">7,304,505</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">955,744</td>
<td align="right">1,180,057</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,453,980</td>
<td align="right">1,793,581</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">486,722</td>
<td align="right">380,409</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">67,462</td>
<td align="right">82,001</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">8,396,140</td>
<td align="right">10,184,998</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,840,965</td>
<td align="right">9,502,208</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">23,446,314</td>
<td align="right">28,398,597</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20,992,532</td>
<td align="right">25,326,392</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">6,692,947</td>
<td align="right">8,071,714</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">41,105,409</td>
<td align="right">48,889,819</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">26,582</td>
<td align="right">31,545</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,793,462</td>
<td align="right">3,310,899</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,735,487</td>
<td align="right">2,043,766</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,448,200</td>
<td align="right">1,703,780</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">25,885,870</td>
<td align="right">30,283,151</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">194,202</td>
<td align="right">226,107</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,471,314</td>
<td align="right">2,872,669</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,730,645</td>
<td align="right">8,975,359</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">867,417</td>
<td align="right">1,006,873</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,907,251</td>
<td align="right">2,210,771</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">4,605,028</td>
<td align="right">5,332,554</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,683,365</td>
<td align="right">1,945,799</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">12,264,626</td>
<td align="right">14,090,067</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">781,262</td>
<td align="right">674,833</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,010</td>
<td align="right">4,541</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,599,502</td>
<td align="right">6,320,558</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">855,890</td>
<td align="right">964,335</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">23,274,723</td>
<td align="right">26,056,374</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">958,027</td>
<td align="right">1,066,325</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,715,289</td>
<td align="right">14,091,906</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">117,536</td>
<td align="right">129,788</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">3,933,094</td>
<td align="right">4,322,511</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">429,873</td>
<td align="right">465,934</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,344,919</td>
<td align="right">2,539,198</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">616,715</td>
<td align="right">666,621</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">10,333,125</td>
<td align="right">11,148,422</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">80,174</td>
<td align="right">86,493</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,785,490</td>
<td align="right">9,476,485</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,567,519</td>
<td align="right">2,758,966</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">38,891,932</td>
<td align="right">41,698,135</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,802,917</td>
<td align="right">1,901,653</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,178,006</td>
<td align="right">9,669,196</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">6,420,939</td>
<td align="right">6,111,437</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">284,492</td>
<td align="right">297,003</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,475,123</td>
<td align="right">1,539,155</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,668,510</td>
<td align="right">1,740,166</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,471,015</td>
<td align="right">2,574,080</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">964,691</td>
<td align="right">1,001,445</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,762,040</td>
<td align="right">2,861,144</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,898,187</td>
<td align="right">1,964,477</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,533,790</td>
<td align="right">6,758,349</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">133,809</td>
<td align="right">138,056</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">65,663</td>
<td align="right">63,848</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">947,833</td>
<td align="right">973,329</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,759,836</td>
<td align="right">1,805,428</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">804,075</td>
<td align="right">824,072</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">611,787</td>
<td align="right">626,605</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,948,324</td>
<td align="right">7,098,509</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,591,339</td>
<td align="right">1,625,580</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,471,140</td>
<td align="right">1,500,628</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,689,464</td>
<td align="right">3,762,665</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,613,122</td>
<td align="right">2,656,268</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,204,296</td>
<td align="right">1,222,473</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">41,698</td>
<td align="right">42,232</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,126</td>
<td align="right">11,268</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">164,551</td>
<td align="right">166,456</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">35,136,084</td>
<td align="right">35,530,598</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,405</td>
<td align="right">2,416</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">83,964</td>
<td align="right">84,310</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">437,069</td>
<td align="right">438,704</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">45,949,007</td>
<td align="right">46,117,856</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">281,024</td>
<td align="right">281,925</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">280,631</td>
<td align="right">281,525</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">18,923</td>
<td align="right">18,977</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,687</td>
<td align="right">5,699</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">525</td>
<td align="right">524</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">615,554</td>
<td align="right">616,452</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">582,875</td>
<td align="right">583,629</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">22,919</td>
<td align="right">22,946</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">913</td>
<td align="right">914</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,977</td>
<td align="right">2,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">4,701,949</td>
<td align="right">4,699,467</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">26,843</td>
<td align="right">26,857</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">581,003</td>
<td align="right">580,814</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,579,581</td>
<td align="right">11,582,763</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">255,323</td>
<td align="right">255,366</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,653,276</td>
<td align="right">5,653,990</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">122,607</td>
<td align="right">122,595</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">554,277</td>
<td align="right">554,227</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">56,820</td>
<td align="right">56,817</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">354,890</td>
<td align="right">354,895</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,047,175</td>
<td align="right">1,047,163</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">165,612</td>
<td align="right">165,611</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">11,717,046</td>
<td align="right">11,717,022</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">616,451</td>
<td align="right">616,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">691,626</td>
<td align="right">691,627</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,152,477</td>
<td align="right">8,152,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,495,102</td>
<td align="right">6,495,102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,284</td>
<td align="right">98,284</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">76,113</td>
<td align="right">76,113</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,427</td>
<td align="right">72,427</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,138</td>
<td align="right">56,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">42,970</td>
<td align="right">42,970</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">19,651</td>
<td align="right">19,651</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,150</td>
<td align="right">1,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,077</td>
<td align="right">1,077</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">937</td>
<td align="right">937</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">780</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">217</td>
<td align="right">217</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">205</td>
<td align="right">205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">52</td>
<td align="right">52</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">29</td>
<td align="right">29</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">10</td>
<td align="right">10</td>
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
<td align="right">314,104</td>
<td align="right">5.1%</td>
<td align="right">419,875</td>
<td align="right">6.7%</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,875,773</td>
<td align="right">94.9%</td>
<td align="right">5,875,772</td>
<td align="right">93.3%</td>
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
<td align="right">2,276</td>
<td align="right">100.0%</td>
<td align="right">2,240</td>
<td align="right">100.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">floor divide</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">91</td>
<td align="right">4.0%</td>
<td align="right">117</td>
<td align="right">5.2%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">10.1%</td>
<td align="right">191</td>
<td align="right">8.5%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">152</td>
<td align="right">6.7%</td>
<td align="right">159</td>
<td align="right">7.1%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,029</td>
<td align="right">45.2%</td>
<td align="right">991</td>
<td align="right">44.2%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">196</td>
<td align="right">8.6%</td>
<td align="right">200</td>
<td align="right">8.9%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">144</td>
<td align="right">6.3%</td>
<td align="right">145</td>
<td align="right">6.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">173</td>
<td align="right">7.6%</td>
<td align="right">173</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">120</td>
<td align="right">5.3%</td>
<td align="right">120</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">2.9%</td>
<td align="right">66</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">37</td>
<td align="right">1.6%</td>
<td align="right">37</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">10</td>
<td align="right">0.4%</td>
<td align="right">10</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
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
<td align="right">288,738</td>
<td align="right">100.0%</td>
<td align="right">475,255</td>
<td align="right">100.0%</td>
<td align="right">64.6%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">15,346</td>
<td align="right">0.1%</td>
<td align="right">31,328</td>
<td align="right">0.3%</td>
<td align="right">104.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,100,747</td>
<td align="right">9.8%</td>
<td align="right">1,738,259</td>
<td align="right">14.0%</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,117,149</td>
<td align="right">90.0%</td>
<td align="right">10,640,755</td>
<td align="right">85.7%</td>
<td align="right">5.2%</td>
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
<td align="right">1,704</td>
<td align="right">30.1%</td>
<td align="right">1,998</td>
<td align="right">30.2%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,953</td>
<td align="right">69.9%</td>
<td align="right">4,625</td>
<td align="right">69.8%</td>
<td align="right">17.0%</td>
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
<td align="right">822</td>
<td align="right">20.8%</td>
<td align="right">1,432</td>
<td align="right">31.0%</td>
<td align="right">74.2%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">636</td>
<td align="right">16.1%</td>
<td align="right">687</td>
<td align="right">14.9%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">776</td>
<td align="right">19.6%</td>
<td align="right">806</td>
<td align="right">17.4%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">33</td>
<td align="right">0.8%</td>
<td align="right">32</td>
<td align="right">0.7%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">771</td>
<td align="right">19.5%</td>
<td align="right">759</td>
<td align="right">16.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">887</td>
<td align="right">22.4%</td>
<td align="right">881</td>
<td align="right">19.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">21</td>
<td align="right">0.5%</td>
<td align="right">21</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">6</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,523,242</td>
<td align="right">9.6%</td>
<td align="right">7,650,710</td>
<td align="right">11.2%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">61,597,204</td>
<td align="right">90.4%</td>
<td align="right">60,362,054</td>
<td align="right">88.7%</td>
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
<td align="right">6,875</td>
<td align="right">0.0%</td>
<td align="right">6,882</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
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
<td align="right">154,386</td>
<td align="right">100.0%</td>
<td align="right">176,804</td>
<td align="right">100.0%</td>
<td align="right">14.5%</td>
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
<td align="right">62</td>
<td align="right">62 / 0 !!</td>
<td align="right">62</td>
<td align="right">62 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">35</td>
<td align="right">35 / 0 !!</td>
<td align="right">35</td>
<td align="right">35 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">523,188</td>
<td align="right">99.5%</td>
<td align="right">581,002</td>
<td align="right">99.6%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">556</td>
<td align="right">0.1%</td>
<td align="right">562</td>
<td align="right">0.1%</td>
<td align="right">1.1%</td>
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
<td align="right">2,547</td>
<td align="right">0.0%</td>
<td align="right">3,326</td>
<td align="right">0.0%</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">954,107</td>
<td align="right">5.3%</td>
<td align="right">1,062,284</td>
<td align="right">5.8%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,208,396</td>
<td align="right">94.7%</td>
<td align="right">17,208,607</td>
<td align="right">94.1%</td>
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
<td align="right">2,458</td>
<td align="right">61.9%</td>
<td align="right">2,579</td>
<td align="right">62.8%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,514</td>
<td align="right">38.1%</td>
<td align="right">1,529</td>
<td align="right">37.2%</td>
<td align="right">1.0%</td>
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
<td align="right">1,013</td>
<td align="right">41.2%</td>
<td align="right">1,108</td>
<td align="right">43.0%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">630</td>
<td align="right">25.6%</td>
<td align="right">655</td>
<td align="right">25.4%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">164</td>
<td align="right">6.7%</td>
<td align="right">165</td>
<td align="right">6.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">236</td>
<td align="right">9.6%</td>
<td align="right">236</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">208</td>
<td align="right">8.5%</td>
<td align="right">208</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">90</td>
<td align="right">3.7%</td>
<td align="right">90</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">51</td>
<td align="right">2.1%</td>
<td align="right">51</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">48</td>
<td align="right">2.0%</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">17</td>
<td align="right">0.7%</td>
<td align="right">17</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">1,131,155</td>
<td align="right">21.4%</td>
<td align="right">2,214,333</td>
<td align="right">34.8%</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,944</td>
<td align="right">0.5%</td>
<td align="right">26,561</td>
<td align="right">0.4%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,110,176</td>
<td align="right">77.9%</td>
<td align="right">4,112,761</td>
<td align="right">64.7%</td>
<td align="right">0.1%</td>
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
<td align="right">6,036</td>
<td align="right">100.0%</td>
<td align="right">6,198</td>
<td align="right">100.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">list</td>
<td align="right">1,158</td>
<td align="right">19.2%</td>
<td align="right">1,207</td>
<td align="right">19.5%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">512</td>
<td align="right">8.5%</td>
<td align="right">495</td>
<td align="right">8.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,152</td>
<td align="right">52.2%</td>
<td align="right">3,253</td>
<td align="right">52.5%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,214</td>
<td align="right">20.1%</td>
<td align="right">1,243</td>
<td align="right">20.1%</td>
<td align="right">2.4%</td>
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
<td align="right">1,387,539</td>
<td align="right">7.7%</td>
<td align="right">3,767,904</td>
<td align="right">14.0%</td>
<td align="right">171.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">108,237</td>
<td align="right">0.6%</td>
<td align="right">227,376</td>
<td align="right">0.8%</td>
<td align="right">110.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,574,685</td>
<td align="right">91.7%</td>
<td align="right">22,949,908</td>
<td align="right">85.1%</td>
<td align="right">38.5%</td>
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
<td align="right">4,322</td>
<td align="right">57.8%</td>
<td align="right">8,465</td>
<td align="right">61.1%</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,151</td>
<td align="right">42.2%</td>
<td align="right">5,386</td>
<td align="right">38.9%</td>
<td align="right">70.9%</td>
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
<td align="right">1,186</td>
<td align="right">27.4%</td>
<td align="right">4,258</td>
<td align="right">50.3%</td>
<td align="right">259.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">9</td>
<td align="right">0.1%</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">82</td>
<td align="right">1.9%</td>
<td align="right">146</td>
<td align="right">1.7%</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">7</td>
<td align="right">0.2%</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">61</td>
<td align="right">1.4%</td>
<td align="right">89</td>
<td align="right">1.1%</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">816</td>
<td align="right">18.9%</td>
<td align="right">1,132</td>
<td align="right">13.4%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,000</td>
<td align="right">23.1%</td>
<td align="right">1,383</td>
<td align="right">16.3%</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">444</td>
<td align="right">10.3%</td>
<td align="right">599</td>
<td align="right">7.1%</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">236</td>
<td align="right">5.5%</td>
<td align="right">306</td>
<td align="right">3.6%</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">231</td>
<td align="right">5.3%</td>
<td align="right">256</td>
<td align="right">3.0%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">228</td>
<td align="right">5.3%</td>
<td align="right">251</td>
<td align="right">3.0%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">25</td>
<td align="right">0.6%</td>
<td align="right">24</td>
<td align="right">0.3%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">22,285,589</td>
<td align="right">20.5%</td>
<td align="right">32,607,460</td>
<td align="right">26.5%</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,707,127</td>
<td align="right">8.0%</td>
<td align="right">9,396,667</td>
<td align="right">7.6%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">77,506,943</td>
<td align="right">71.4%</td>
<td align="right">80,899,015</td>
<td align="right">65.8%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">207,261</td>
<td align="right">0.2%</td>
<td align="right">207,261</td>
<td align="right">0.2%</td>
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
<td align="right">479,325</td>
<td align="right">96.9%</td>
<td align="right">675,176</td>
<td align="right">97.7%</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">15,473</td>
<td align="right">3.1%</td>
<td align="right">15,782</td>
<td align="right">2.3%</td>
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
<td align="left">module attr not found</td>
<td align="right">65</td>
<td align="right">0.4%</td>
<td align="right">71</td>
<td align="right">0.4%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">843</td>
<td align="right">5.4%</td>
<td align="right">905</td>
<td align="right">5.7%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">342</td>
<td align="right">2.2%</td>
<td align="right">366</td>
<td align="right">2.3%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,399</td>
<td align="right">22.0%</td>
<td align="right">3,627</td>
<td align="right">23.0%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">488</td>
<td align="right">3.2%</td>
<td align="right">469</td>
<td align="right">3.0%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">58</td>
<td align="right">0.4%</td>
<td align="right">59</td>
<td align="right">0.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,261</td>
<td align="right">8.1%</td>
<td align="right">1,253</td>
<td align="right">7.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,584</td>
<td align="right">10.2%</td>
<td align="right">1,588</td>
<td align="right">10.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">4,900</td>
<td align="right">31.7%</td>
<td align="right">4,911</td>
<td align="right">31.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">835</td>
<td align="right">5.4%</td>
<td align="right">835</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">1.5%</td>
<td align="right">235</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">205</td>
<td align="right">1.3%</td>
<td align="right">205</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">42,757,668</td>
<td align="right">99.9%</td>
<td align="right">53,587,741</td>
<td align="right">99.9%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,512</td>
<td align="right">0.0%</td>
<td align="right">4,462</td>
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
<td align="right">5,036</td>
<td align="right">0.0%</td>
<td align="right">5,048</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">521</td>
<td align="right">0.0%</td>
<td align="right">521</td>
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
<td align="right">17,957</td>
<td align="right">100.0%</td>
<td align="right">17,971</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
<td align="right">103</td>
<td align="right">0.0%</td>
<td align="right">102</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">719,889</td>
<td align="right">99.9%</td>
<td align="right">719,838</td>
<td align="right">99.9%</td>
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
<td align="right">422</td>
<td align="right">100.0%</td>
<td align="right">422</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,492,137</td>
<td align="right">54.9%</td>
<td align="right">6,492,137</td>
<td align="right">54.9%</td>
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
<td align="right">5,332,554</td>
<td align="right">45.1%</td>
<td align="right">5,332,554</td>
<td align="right">45.1%</td>
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
<td align="right">104</td>
<td align="right">3.5%</td>
<td align="right">104</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,861</td>
<td align="right">96.5%</td>
<td align="right">2,861</td>
<td align="right">96.5%</td>
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
<td align="right">2,058</td>
<td align="right">71.9%</td>
<td align="right">2,058</td>
<td align="right">71.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">51</td>
<td align="right">1.8%</td>
<td align="right">51</td>
<td align="right">1.8%</td>
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
<td align="right">1,197,259</td>
<td align="right">8.6%</td>
<td align="right">1,215,420</td>
<td align="right">8.7%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,959,091</td>
<td align="right">14.0%</td>
<td align="right">1,964,895</td>
<td align="right">14.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,812,238</td>
<td align="right">77.4%</td>
<td align="right">10,806,581</td>
<td align="right">77.2%</td>
<td align="right">-0.1%</td>
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
<td align="right">2,521</td>
<td align="right">5.7%</td>
<td align="right">2,537</td>
<td align="right">5.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,428</td>
<td align="right">94.3%</td>
<td align="right">41,537</td>
<td align="right">94.2%</td>
<td align="right">0.3%</td>
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
<td align="right">29</td>
<td align="right">1.2%</td>
<td align="right">31</td>
<td align="right">1.2%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">270</td>
<td align="right">10.7%</td>
<td align="right">281</td>
<td align="right">11.1%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">127</td>
<td align="right">5.0%</td>
<td align="right">130</td>
<td align="right">5.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,382</td>
<td align="right">54.8%</td>
<td align="right">1,382</td>
<td align="right">54.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">401</td>
<td align="right">15.9%</td>
<td align="right">401</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">230</td>
<td align="right">9.1%</td>
<td align="right">230</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">54</td>
<td align="right">2.1%</td>
<td align="right">54</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">8</td>
<td align="right">0.3%</td>
<td align="right">8</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
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
<td align="right">29</td>
<td align="right">100.0%</td>
<td align="right">29</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">79,409</td>
<td align="right">3.0%</td>
<td align="right">85,721</td>
<td align="right">3.2%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,587,703</td>
<td align="right">97.0%</td>
<td align="right">2,587,708</td>
<td align="right">96.8%</td>
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
<td align="right">424</td>
<td align="right">55.4%</td>
<td align="right">431</td>
<td align="right">55.8%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">341</td>
<td align="right">44.6%</td>
<td align="right">341</td>
<td align="right">44.2%</td>
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
<td align="left">bytearray int</td>
<td align="right">13</td>
<td align="right">3.1%</td>
<td align="right">20</td>
<td align="right">4.6%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">240</td>
<td align="right">56.6%</td>
<td align="right">240</td>
<td align="right">55.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">92</td>
<td align="right">21.7%</td>
<td align="right">92</td>
<td align="right">21.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">47</td>
<td align="right">11.1%</td>
<td align="right">47</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">26</td>
<td align="right">6.1%</td>
<td align="right">26</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">6</td>
<td align="right">1.4%</td>
<td align="right">6</td>
<td align="right">1.4%</td>
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
<td align="right">1,080,142</td>
<td align="right">2.7%</td>
<td align="right">2,849,271</td>
<td align="right">6.8%</td>
<td align="right">163.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">597,457</td>
<td align="right">1.5%</td>
<td align="right">612,170</td>
<td align="right">1.5%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,533,047</td>
<td align="right">95.8%</td>
<td align="right">38,487,770</td>
<td align="right">91.7%</td>
<td align="right">-0.1%</td>
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
<td align="right">27,566</td>
<td align="right">80.1%</td>
<td align="right">60,899</td>
<td align="right">89.7%</td>
<td align="right">120.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,858</td>
<td align="right">19.9%</td>
<td align="right">6,958</td>
<td align="right">10.3%</td>
<td align="right">1.5%</td>
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
<td align="right">121</td>
<td align="right">1.8%</td>
<td align="right">197</td>
<td align="right">2.8%</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">541</td>
<td align="right">7.9%</td>
<td align="right">562</td>
<td align="right">8.1%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">326</td>
<td align="right">4.8%</td>
<td align="right">328</td>
<td align="right">4.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">665</td>
<td align="right">9.7%</td>
<td align="right">666</td>
<td align="right">9.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">4,257</td>
<td align="right">62.1%</td>
<td align="right">4,257</td>
<td align="right">61.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">871</td>
<td align="right">12.7%</td>
<td align="right">871</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">50</td>
<td align="right">0.7%</td>
<td align="right">50</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">27</td>
<td align="right">0.4%</td>
<td align="right">27</td>
<td align="right">0.4%</td>
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
<td align="right">1,171</td>
<td align="right">0.0%</td>
<td align="right">725,614</td>
<td align="right">8.4%</td>
<td align="right">61,865.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,962,407</td>
<td align="right">100.0%</td>
<td align="right">7,960,889</td>
<td align="right">91.6%</td>
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
<td align="right">37</td>
<td align="right">4.2%</td>
<td align="right">246</td>
<td align="right">22.8%</td>
<td align="right">564.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">834</td>
<td align="right">95.8%</td>
<td align="right">834</td>
<td align="right">77.2%</td>
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
<td align="left">sequence</td>
<td align="right">13</td>
<td align="right">35.1%</td>
<td align="right">222</td>
<td align="right">90.2%</td>
<td align="right">1,607.7%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">24</td>
<td align="right">64.9%</td>
<td align="right">24</td>
<td align="right">9.8%</td>
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
<td align="right">32,529,504</td>
<td align="right">3.7%</td>
<td align="right">45,947,293</td>
<td align="right">4.4%</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">22,432,211</td>
<td align="right">2.6%</td>
<td align="right">28,393,750</td>
<td align="right">2.7%</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">319,645,825</td>
<td align="right">36.7%</td>
<td align="right">390,246,270</td>
<td align="right">37.3%</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">497,325,427</td>
<td align="right">57.0%</td>
<td align="right">582,698,476</td>
<td align="right">55.6%</td>
<td align="right">17.2%</td>
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
<td align="right">1,387,539</td>
<td align="right">6.2%</td>
<td align="right">3,767,904</td>
<td align="right">13.4%</td>
<td align="right">171.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,131,155</td>
<td align="right">5.1%</td>
<td align="right">2,214,333</td>
<td align="right">7.8%</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">288,738</td>
<td align="right">1.3%</td>
<td align="right">475,255</td>
<td align="right">1.7%</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,100,747</td>
<td align="right">4.9%</td>
<td align="right">1,738,259</td>
<td align="right">6.2%</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">954,107</td>
<td align="right">4.3%</td>
<td align="right">1,062,284</td>
<td align="right">3.8%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,707,127</td>
<td align="right">39.1%</td>
<td align="right">9,396,667</td>
<td align="right">33.3%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">597,457</td>
<td align="right">2.7%</td>
<td align="right">612,170</td>
<td align="right">2.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,197,259</td>
<td align="right">5.4%</td>
<td align="right">1,215,420</td>
<td align="right">4.3%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,492,137</td>
<td align="right">29.2%</td>
<td align="right">6,492,137</td>
<td align="right">23.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">314,104</td>
<td align="right">1.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">725,614</td>
<td align="right">2.6%</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">752,224</td>
<td align="right">2.3%</td>
<td align="right">2,485,939</td>
<td align="right">5.4%</td>
<td align="right">230.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,410,395</td>
<td align="right">4.3%</td>
<td align="right">2,935,716</td>
<td align="right">6.4%</td>
<td align="right">108.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">3,213,311</td>
<td align="right">9.9%</td>
<td align="right">5,124,006</td>
<td align="right">11.2%</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,187,552</td>
<td align="right">15.9%</td>
<td align="right">7,734,295</td>
<td align="right">16.8%</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,765,556</td>
<td align="right">36.2%</td>
<td align="right">15,943,935</td>
<td align="right">34.7%</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">643,474</td>
<td align="right">2.0%</td>
<td align="right">804,540</td>
<td align="right">1.8%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,628,921</td>
<td align="right">14.2%</td>
<td align="right">5,622,261</td>
<td align="right">12.2%</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">486,489</td>
<td align="right">1.5%</td>
<td align="right">540,752</td>
<td align="right">1.2%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,157,496</td>
<td align="right">3.6%</td>
<td align="right">1,259,164</td>
<td align="right">2.7%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,959,028</td>
<td align="right">6.0%</td>
<td align="right">1,964,779</td>
<td align="right">4.3%</td>
<td align="right">0.3%</td>
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
<td align="right">1,294,396</td>
<td align="right">1.9%</td>
<td align="right">1,143,541</td>
<td align="right">1.7%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">5,500,911</td>
<td align="right">7.9%</td>
<td align="right">5,397,720</td>
<td align="right">7.8%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">12,047,899</td>
<td align="right">17.4%</td>
<td align="right">11,944,748</td>
<td align="right">17.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">12,047,899</td>
<td align="right">17.4%</td>
<td align="right">11,944,748</td>
<td align="right">17.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">913</td>
<td align="right">0.0%</td>
<td align="right">914</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">390,045</td>
<td align="right">0.6%</td>
<td align="right">389,929</td>
<td align="right">0.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">57,339,722</td>
<td align="right">82.6%</td>
<td align="right">57,336,182</td>
<td align="right">82.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,160,467</td>
<td align="right">1.7%</td>
<td align="right">1,160,455</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">47,794,426</td>
<td align="right">68.9%</td>
<td align="right">47,794,013</td>
<td align="right">69.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,546,988</td>
<td align="right">9.4%</td>
<td align="right">6,547,028</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,545,842</td>
<td align="right">9.4%</td>
<td align="right">6,545,881</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">233</td>
<td align="right">0.0%</td>
<td align="right">233</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">454,264</td>
<td align="right">0.7%</td>
<td align="right">454,264</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">22</td>
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
<td align="left">Mortal decrefs</td>
<td align="right">465,367,343</td>
<td align="right">35.7%</td>
<td align="right">346,722,201</td>
<td align="right">28.2%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">489,021,429</td>
<td align="right">41.8%</td>
<td align="right">371,256,410</td>
<td align="right">33.5%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">98,708,144</td>
<td align="right">8.4%</td>
<td align="right">116,864,878</td>
<td align="right">10.5%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">214,809</td>
<td align="right"></td>
<td align="right">246,700</td>
<td align="right"></td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">362,698,980</td>
<td align="right">31.0%</td>
<td align="right">415,698,242</td>
<td align="right">37.5%</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">224,764,321</td>
<td align="right">17.2%</td>
<td align="right">193,133,743</td>
<td align="right">15.7%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">146,816,167</td>
<td align="right">11.2%</td>
<td align="right">166,714,059</td>
<td align="right">13.6%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">365,086</td>
<td align="right">0.4%</td>
<td align="right">315,633</td>
<td align="right">0.3%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,621,446</td>
<td align="right"></td>
<td align="right">1,815,568</td>
<td align="right"></td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,408,388</td>
<td align="right"></td>
<td align="right">1,570,889</td>
<td align="right"></td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">468,292,985</td>
<td align="right">35.9%</td>
<td align="right">521,679,289</td>
<td align="right">42.5%</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">219,843,376</td>
<td align="right">18.8%</td>
<td align="right">205,501,317</td>
<td align="right">18.5%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">51,851,276</td>
<td align="right"></td>
<td align="right">52,380,628</td>
<td align="right"></td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">68,001,999</td>
<td align="right">70.8%</td>
<td align="right">67,486,744</td>
<td align="right">70.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">66,703,932</td>
<td align="right"></td>
<td align="right">66,206,371</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">67,598,134</td>
<td align="right">70.3%</td>
<td align="right">67,132,461</td>
<td align="right">70.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">38,779</td>
<td align="right">0.0%</td>
<td align="right">38,650</td>
<td align="right">0.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">28,745,675</td>
<td align="right"></td>
<td align="right">28,699,199</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">28,089,528</td>
<td align="right">29.2%</td>
<td align="right">28,087,372</td>
<td align="right">29.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">28,109,938</td>
<td align="right"></td>
<td align="right">28,107,781</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">98,622</td>
<td align="right">8.9%</td>
<td align="right">98,617</td>
<td align="right">8.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,110,453</td>
<td align="right"></td>
<td align="right">1,110,449</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">4,975</td>
<td align="right">0.4%</td>
<td align="right">4,975</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<th align="right">Head Collections</th>
<th align="right">Head Objects collected</th>
<th align="right">Head Object visits</th>
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
</tr>
<tr>
<td align="right">1</td>
<td align="right">1,315</td>
<td align="right">28,721</td>
<td align="right">156,839,980</td>
<td align="right">1,326</td>
<td align="right">29,309</td>
<td align="right">178,457,164</td>
</tr>
<tr>
<td align="right">2</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,168</td>
<td align="right">1.0%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">84,014</td>
<td align="right">73.4%</td>
<td align="right">6,926</td>
<td align="right">37.9%</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">609</td>
<td align="right">0.5%</td>
<td align="right">83</td>
<td align="right">0.5%</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">114,470</td>
<td align="right"></td>
<td align="right">18,291</td>
<td align="right"></td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">36,224</td>
<td align="right">31.6%</td>
<td align="right">7,622</td>
<td align="right">41.7%</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">30,456</td>
<td align="right">26.6%</td>
<td align="right">11,365</td>
<td align="right">62.1%</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">97,123,446</td>
<td align="right"></td>
<td align="right">40,136,587</td>
<td align="right"></td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,015,975,976</td>
<td align="right">1,046.1%</td>
<td align="right">469,156,802</td>
<td align="right">1,168.9%</td>
<td align="right">-53.8%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">84,014</td>
<td align="right"></td>
<td align="right">6,926</td>
<td align="right"></td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">82,011</td>
<td align="right">97.6%</td>
<td align="right">6,926</td>
<td align="right">100.0%</td>
<td align="right">-91.6%</td>
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
</tbody>
</table>

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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">8,164</td>
<td align="right">9.7%</td>
<td align="right">1,330</td>
<td align="right">19.2%</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">16,759</td>
<td align="right">19.9%</td>
<td align="right">1,657</td>
<td align="right">23.9%</td>
<td align="right">-90.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">30,701</td>
<td align="right">36.5%</td>
<td align="right">2,281</td>
<td align="right">32.9%</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22,757</td>
<td align="right">27.1%</td>
<td align="right">1,219</td>
<td align="right">17.6%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,895</td>
<td align="right">5.8%</td>
<td align="right">419</td>
<td align="right">6.0%</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">584</td>
<td align="right">0.7%</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">154</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">3,136</td>
<td align="right">3.7%</td>
<td align="right">924</td>
<td align="right">13.3%</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">18,838</td>
<td align="right">22.4%</td>
<td align="right">1,388</td>
<td align="right">20.0%</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">10,873</td>
<td align="right">12.9%</td>
<td align="right">1,503</td>
<td align="right">21.7%</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,511</td>
<td align="right">42.3%</td>
<td align="right">2,033</td>
<td align="right">29.4%</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">12,072</td>
<td align="right">14.4%</td>
<td align="right">952</td>
<td align="right">13.7%</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,340</td>
<td align="right">1.6%</td>
<td align="right">106</td>
<td align="right">1.5%</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">240</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>

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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


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
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">389,670</td>
<td align="right">240</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">90,370</td>
<td align="right">240</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,147,636</td>
<td align="right">3,813</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,359,597</td>
<td align="right">6,531</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">465,532</td>
<td align="right">2,268</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,673,971</td>
<td align="right">11,067</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,087,935</td>
<td align="right">8,587</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">221,603</td>
<td align="right">2,478</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">341,480</td>
<td align="right">4,263</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">188,032</td>
<td align="right">2,365</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,762,424</td>
<td align="right">78,307</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">47,860</td>
<td align="right">2,268</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,367,542</td>
<td align="right">140,162</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">891,751</td>
<td align="right">76,440</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">78,792</td>
<td align="right">7,149</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">787,804</td>
<td align="right">75,726</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">791,539</td>
<td align="right">98,889</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">73,553</td>
<td align="right">9,539</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">721,032</td>
<td align="right">114,263</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">14,258,603</td>
<td align="right">2,263,185</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">586,053</td>
<td align="right">104,656</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">335,007</td>
<td align="right">60,476</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">316,656</td>
<td align="right">61,542</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,775,762</td>
<td align="right">1,442,910</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,407,336</td>
<td align="right">326,899</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">6,163,282</td>
<td align="right">1,447,034</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,407,883</td>
<td align="right">1,314,499</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">13,846,097</td>
<td align="right">3,569,633</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,285,318</td>
<td align="right">351,082</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">2,123,188</td>
<td align="right">604,548</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">2,631,960</td>
<td align="right">765,949</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">5,099,004</td>
<td align="right">1,496,948</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,422,588</td>
<td align="right">427,730</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">3,364,814</td>
<td align="right">1,022,913</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">2,473,740</td>
<td align="right">774,247</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">53,595,071</td>
<td align="right">16,977,897</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">6,392,046</td>
<td align="right">2,028,982</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">4,511,132</td>
<td align="right">1,443,599</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">2,532,512</td>
<td align="right">822,590</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">9,187,506</td>
<td align="right">3,005,144</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">3,085,777</td>
<td align="right">1,015,869</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">5,538,543</td>
<td align="right">1,952,706</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,243,801</td>
<td align="right">813,057</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">1,763,769</td>
<td align="right">652,050</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">16,105,534</td>
<td align="right">6,018,472</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">14,029,513</td>
<td align="right">5,263,746</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">2,625,750</td>
<td align="right">991,494</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">573,497</td>
<td align="right">217,458</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,173,691</td>
<td align="right">445,598</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">12,602,770</td>
<td align="right">4,835,920</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,060,065</td>
<td align="right">796,508</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">19,368,568</td>
<td align="right">7,611,744</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">4,858,215</td>
<td align="right">1,919,786</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,962,472</td>
<td align="right">1,192,572</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">6,932,717</td>
<td align="right">2,848,576</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">1,581,779</td>
<td align="right">652,050</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">97,123,446</td>
<td align="right">40,136,587</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,236,513</td>
<td align="right">512,043</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">942,202</td>
<td align="right">390,200</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,317,848</td>
<td align="right">546,441</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,366,996</td>
<td align="right">989,226</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">81,798,346</td>
<td align="right">34,534,478</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,161,213</td>
<td align="right">491,437</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,400,806</td>
<td align="right">1,024,155</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">102,432,858</td>
<td align="right">43,771,857</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">427,026</td>
<td align="right">184,485</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">16,079,733</td>
<td align="right">7,099,118</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">9,751,813</td>
<td align="right">4,308,920</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">416,813</td>
<td align="right">184,464</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">14,212,475</td>
<td align="right">6,383,725</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">654,856</td>
<td align="right">295,135</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,491,194</td>
<td align="right">2,032,548</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">7,637,552</td>
<td align="right">3,498,333</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">978,540</td>
<td align="right">449,422</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">124,392</td>
<td align="right">58,107</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,433,628</td>
<td align="right">1,608,108</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,467,398</td>
<td align="right">691,852</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">4,037,992</td>
<td align="right">1,941,366</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">9,393,427</td>
<td align="right">4,537,657</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">2,739,738</td>
<td align="right">1,334,837</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">83,990,629</td>
<td align="right">41,333,091</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">2,624,303</td>
<td align="right">1,303,554</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">7,703,538</td>
<td align="right">3,848,214</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">3,985,457</td>
<td align="right">2,044,196</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,065,290</td>
<td align="right">547,856</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">2,276,221</td>
<td align="right">1,188,243</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">56,903,187</td>
<td align="right">29,797,964</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">7,101,906</td>
<td align="right">3,816,712</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">11,972,673</td>
<td align="right">6,601,824</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">11,953,000</td>
<td align="right">6,601,824</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">3,895,723</td>
<td align="right">2,155,854</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">15,067,768</td>
<td align="right">8,417,267</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">320,222</td>
<td align="right">180,768</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">34,916,539</td>
<td align="right">19,915,456</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">2,797,279</td>
<td align="right">1,620,506</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">495,790</td>
<td align="right">301,443</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">488,442</td>
<td align="right">296,982</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">9,289,900</td>
<td align="right">5,735,561</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,664,428</td>
<td align="right">1,651,155</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,523,944</td>
<td align="right">2,186,907</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">9,279,732</td>
<td align="right">5,837,030</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">464,850</td>
<td align="right">295,599</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">5,915,527</td>
<td align="right">3,846,969</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,876,418</td>
<td align="right">3,219,244</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">6,409,471</td>
<td align="right">4,294,496</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">23,853,123</td>
<td align="right">16,053,897</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,699,343</td>
<td align="right">1,145,806</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">5,309,412</td>
<td align="right">3,635,270</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">7,138,105</td>
<td align="right">5,151,885</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,797,503</td>
<td align="right">5,022,937</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,067,045</td>
<td align="right">791,511</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,351,011</td>
<td align="right">1,013,832</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">12,167,765</td>
<td align="right">9,195,609</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">6,670,004</td>
<td align="right">5,102,491</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,576,189</td>
<td align="right">1,212,015</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,262,856</td>
<td align="right">3,421,558</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,057,809</td>
<td align="right">4,993,837</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">1,837,312</td>
<td align="right">2,146,814</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,961,681</td>
<td align="right">1,641,129</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">579,314</td>
<td align="right">506,151</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,013,511</td>
<td align="right">907,725</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">871,701</td>
<td align="right">791,511</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,738,543</td>
<td align="right">1,583,946</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">4,019,311</td>
<td align="right">3,710,760</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,046,346</td>
<td align="right">1,891,474</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,831,475</td>
<td align="right">4,544,250</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,421,028</td>
<td align="right">2,464,514</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">727,526</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">401,343</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">262,448</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">255,872</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">224,314</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">186,519</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">151,358</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">150,128</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">150,128</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">134,525</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">134,525</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">117,023</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">109,155</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">108,451</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">106,226</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">99,108</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">86,998</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">79,899</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">61,867</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">49,906</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">49,542</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">43,212</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">43,146</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">41,462</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">41,229</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">41,229</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">39,500</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">39,466</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">37,437</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">36,765</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">36,062</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">35,670</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">34,228</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">31,905</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">29,483</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">25,502</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">25,502</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">23,164</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">21,609</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">19,990</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">18,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">14,539</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">12,519</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">12,252</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">7,112</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">6,312</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">4,963</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">2,822</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">1,905</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,633</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">1,157</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">984</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">897</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">887</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">887</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">824</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">754</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">745</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">717</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">678</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">534</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">520</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">345</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">233</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">190</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">130</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">116</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">84</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">44</td>
<td align="right"></td>
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
<td align="left">CALL</td>
<td align="right">1,010</td>
<td align="right">559</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">7,336</td>
<td align="right">5,155</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">437</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">86</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2</td>
<td align="right"></td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">16</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">16</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
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
<td align="right">12</td>
<td align="right">12</td>
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
<td align="right">12</td>
<td align="right">12</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-12
