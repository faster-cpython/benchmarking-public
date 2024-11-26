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
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">14</td>
<td align="right">271,971</td>
<td align="right">1,942,550.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">12,718</td>
<td align="right">6,030,968</td>
<td align="right">47,320.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,288</td>
<td align="right">428,972</td>
<td align="right">33,205.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">495</td>
<td align="right">131,713</td>
<td align="right">26,508.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,673</td>
<td align="right">429,363</td>
<td align="right">25,564.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,905</td>
<td align="right">390,552</td>
<td align="right">20,401.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,908</td>
<td align="right">736,409</td>
<td align="right">14,904.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,327</td>
<td align="right">132,272</td>
<td align="right">9,867.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,391</td>
<td align="right">707,852</td>
<td align="right">9,477.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,500</td>
<td align="right">132,426</td>
<td align="right">8,728.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,553</td>
<td align="right">311,409</td>
<td align="right">8,664.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,613</td>
<td align="right">148,606</td>
<td align="right">5,587.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">7,288</td>
<td align="right">315,487</td>
<td align="right">4,228.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,001</td>
<td align="right">143,824</td>
<td align="right">3,494.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,110</td>
<td align="right">406,137</td>
<td align="right">2,421.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">14,763</td>
<td align="right">287,164</td>
<td align="right">1,845.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">16,745</td>
<td align="right">289,168</td>
<td align="right">1,626.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">201,410</td>
<td align="right">1,175,492</td>
<td align="right">483.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">194,472</td>
<td align="right">1,088,506</td>
<td align="right">459.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">213,733</td>
<td align="right">954,776</td>
<td align="right">346.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">768,613</td>
<td align="right">2,675,607</td>
<td align="right">248.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">708,710</td>
<td align="right">2,246,474</td>
<td align="right">217.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,327,002</td>
<td align="right">6,653,991</td>
<td align="right">185.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">207,546</td>
<td align="right">574,811</td>
<td align="right">177.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,529,151</td>
<td align="right">6,575,190</td>
<td align="right">160.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">11,226,786</td>
<td align="right">27,483,726</td>
<td align="right">144.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">704,341</td>
<td align="right">1,723,796</td>
<td align="right">144.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,869,205</td>
<td align="right">9,323,467</td>
<td align="right">141.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,564,961</td>
<td align="right">6,090,579</td>
<td align="right">137.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">5,272,143</td>
<td align="right">12,344,240</td>
<td align="right">134.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,264,300</td>
<td align="right">5,245,752</td>
<td align="right">131.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,822,695</td>
<td align="right">17,987,920</td>
<td align="right">129.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">21,576,368</td>
<td align="right">49,598,057</td>
<td align="right">129.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,056,963</td>
<td align="right">9,318,762</td>
<td align="right">129.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,823,887</td>
<td align="right">19,824,127</td>
<td align="right">124.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,931,817</td>
<td align="right">4,270,126</td>
<td align="right">121.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">21,067,636</td>
<td align="right">46,502,758</td>
<td align="right">120.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,825,339</td>
<td align="right">12,843,086</td>
<td align="right">120.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17,057,492</td>
<td align="right">37,604,273</td>
<td align="right">120.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,392,839</td>
<td align="right">14,033,644</td>
<td align="right">119.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,358,327</td>
<td align="right">5,170,877</td>
<td align="right">119.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,319,725</td>
<td align="right">5,051,153</td>
<td align="right">117.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">155,844,154</td>
<td align="right">335,525,039</td>
<td align="right">115.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">58,217,027</td>
<td align="right">123,506,575</td>
<td align="right">112.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">58,703,576</td>
<td align="right">124,041,706</td>
<td align="right">111.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">14,947,870</td>
<td align="right">31,536,663</td>
<td align="right">111.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">3,605,839</td>
<td align="right">7,572,545</td>
<td align="right">110.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,443,444</td>
<td align="right">9,317,193</td>
<td align="right">109.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,307,681</td>
<td align="right">92,518,368</td>
<td align="right">108.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">20,928,651</td>
<td align="right">43,637,657</td>
<td align="right">108.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">13,903,877</td>
<td align="right">28,966,167</td>
<td align="right">108.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">10,855,117</td>
<td align="right">22,611,558</td>
<td align="right">108.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">10,862,071</td>
<td align="right">22,622,250</td>
<td align="right">108.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">63,890,182</td>
<td align="right">132,641,052</td>
<td align="right">107.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">12,986,570</td>
<td align="right">26,944,484</td>
<td align="right">107.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">3,152,765</td>
<td align="right">6,428,985</td>
<td align="right">103.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">10,366,099</td>
<td align="right">21,070,744</td>
<td align="right">103.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">4,747,959</td>
<td align="right">9,558,515</td>
<td align="right">101.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">40,426,059</td>
<td align="right">81,314,272</td>
<td align="right">101.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">20,710,347</td>
<td align="right">41,642,465</td>
<td align="right">101.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,825,852</td>
<td align="right">9,701,632</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,123,935</td>
<td align="right">4,269,333</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">194,549</td>
<td align="right">390,982</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">5,410,159</td>
<td align="right">10,871,720</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">709,818</td>
<td align="right">1,425,136</td>
<td align="right">100.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">5,418,844</td>
<td align="right">10,879,113</td>
<td align="right">100.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,070,094</td>
<td align="right">12,180,739</td>
<td align="right">100.7%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">194,863</td>
<td align="right">390,852</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">195,322</td>
<td align="right">391,766</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,136,133</td>
<td align="right">4,282,099</td>
<td align="right">100.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,331,465</td>
<td align="right">4,672,429</td>
<td align="right">100.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">196,219</td>
<td align="right">392,552</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">10,920,920</td>
<td align="right">21,847,414</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">195,938</td>
<td align="right">391,316</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">201,192</td>
<td align="right">396,586</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">225</td>
<td align="right">420</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">312,592</td>
<td align="right">510,074</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">5,248</td>
<td align="right">7,996</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">24</td>
<td align="right">36</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,896</td>
<td align="right">2,821</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,315</td>
<td align="right">3,438</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,234</td>
<td align="right">1,829</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">2,707</td>
<td align="right">3,986</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,260</td>
<td align="right">1,855</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">580</td>
<td align="right">845</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,047</td>
<td align="right">1,447</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,383,859</td>
<td align="right">5,947,331</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,592</td>
<td align="right">2,065</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">236</td>
<td align="right">176</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,331</td>
<td align="right">2,891</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,057</td>
<td align="right">2,476</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,641</td>
<td align="right">1,971</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">324</td>
<td align="right">388</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,106</td>
<td align="right">1,315</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">13,449,231</td>
<td align="right">15,937,590</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">13,003</td>
<td align="right">15,073</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,666</td>
<td align="right">3,146</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,046</td>
<td align="right">4,564</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">269</td>
<td align="right">300</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">292</td>
<td align="right">323</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,512</td>
<td align="right">4,966</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">16,617</td>
<td align="right">18,141</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,002</td>
<td align="right">1,092</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,467</td>
<td align="right">3,752</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">668</td>
<td align="right">614</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,013</td>
<td align="right">1,092</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">29</td>
<td align="right">31</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,201</td>
<td align="right">9,714</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,914</td>
<td align="right">12,562</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">9,675</td>
<td align="right">10,171</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,271</td>
<td align="right">5,956</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,378,402</td>
<td align="right">4,158,607</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,492</td>
<td align="right">2,598</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,441</td>
<td align="right">3,559</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,339</td>
<td align="right">3,443</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">66</td>
<td align="right">68</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,256</td>
<td align="right">1,283</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,842</td>
<td align="right">1,876</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,559</td>
<td align="right">1,586</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">843</td>
<td align="right">857</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">7,227</td>
<td align="right">7,345</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">127</td>
<td align="right">129</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">256</td>
<td align="right">260</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">64</td>
<td align="right">65</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">770</td>
<td align="right">782</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">193</td>
<td align="right">196</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">644</td>
<td align="right">654</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">258</td>
<td align="right">262</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,358</td>
<td align="right">3,410</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">453</td>
<td align="right">460</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3,370</td>
<td align="right">3,422</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3,370</td>
<td align="right">3,422</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3,370</td>
<td align="right">3,422</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">260</td>
<td align="right">264</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">978</td>
<td align="right">993</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">655</td>
<td align="right">665</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">459</td>
<td align="right">466</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">155</td>
<td align="right">157</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">632</td>
<td align="right">638</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">258</td>
<td align="right">258</td>
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
<td align="right">8,404</td>
<td align="right">39.3%</td>
<td align="right">8,949</td>
<td align="right">40.5%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,196</td>
<td align="right">57.0%</td>
<td align="right">12,379</td>
<td align="right">56.0%</td>
<td align="right">1.5%</td>
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
<td align="right">624</td>
<td align="right">100.0%</td>
<td align="right">592</td>
<td align="right">100.0%</td>
<td align="right">-5.1%</td>
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
<td align="left">add other</td>
<td align="right">131</td>
<td align="right">21.0%</td>
<td align="right">115</td>
<td align="right">19.4%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">363</td>
<td align="right">58.2%</td>
<td align="right">347</td>
<td align="right">58.6%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">129</td>
<td align="right">20.7%</td>
<td align="right">129</td>
<td align="right">21.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
<td align="right">0.2%</td>
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
<td align="right">1,559</td>
<td align="right">100.0%</td>
<td align="right">1,586</td>
<td align="right">100.0%</td>
<td align="right">1.7%</td>
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
<td align="right">23,031,013</td>
<td align="right">99.1%</td>
<td align="right">46,303,768</td>
<td align="right">99.2%</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">200,439</td>
<td align="right">0.9%</td>
<td align="right">395,823</td>
<td align="right">0.8%</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">34</td>
<td align="right">0.0%</td>
<td align="right">34</td>
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
<td align="right">191</td>
<td align="right">25.3%</td>
<td align="right">171</td>
<td align="right">22.4%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">563</td>
<td align="right">74.7%</td>
<td align="right">593</td>
<td align="right">77.6%</td>
<td align="right">5.3%</td>
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
<td align="right">146</td>
<td align="right">25.9%</td>
<td align="right">171</td>
<td align="right">28.8%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">108</td>
<td align="right">19.2%</td>
<td align="right">111</td>
<td align="right">18.7%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">309</td>
<td align="right">54.9%</td>
<td align="right">311</td>
<td align="right">52.4%</td>
<td align="right">0.6%</td>
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
<td align="right">43,312,422</td>
<td align="right">100.0%</td>
<td align="right">86,876,321</td>
<td align="right">100.0%</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,966</td>
<td align="right">0.0%</td>
<td align="right">4,029</td>
<td align="right">0.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,736</td>
<td align="right">0.0%</td>
<td align="right">1,754</td>
<td align="right">0.0%</td>
<td align="right">1.0%</td>
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
<td align="right">4,786</td>
<td align="right">100.0%</td>
<td align="right">4,394</td>
<td align="right">100.0%</td>
<td align="right">-8.2%</td>
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
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">43</td>
<td align="right">43 / 0 !!</td>
<td align="right">23</td>
<td align="right">23 / 0 !!</td>
<td align="right">-46.5%</td>
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
<td align="right">11.9%</td>
<td align="right">28</td>
<td align="right">15.9%</td>
<td align="right">0.0%</td>
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
<td align="right">709,239</td>
<td align="right">47.4%</td>
<td align="right">1,424,383</td>
<td align="right">47.6%</td>
<td align="right">100.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">785,457</td>
<td align="right">52.5%</td>
<td align="right">1,566,040</td>
<td align="right">52.4%</td>
<td align="right">99.4%</td>
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
<td align="right">403</td>
<td align="right">69.6%</td>
<td align="right">577</td>
<td align="right">76.6%</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">176</td>
<td align="right">30.4%</td>
<td align="right">176</td>
<td align="right">23.4%</td>
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
<td align="right">266</td>
<td align="right">66.0%</td>
<td align="right">440</td>
<td align="right">76.3%</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">93</td>
<td align="right">23.1%</td>
<td align="right">93</td>
<td align="right">16.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">10.7%</td>
<td align="right">43</td>
<td align="right">7.5%</td>
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
<td align="right">3,923,987</td>
<td align="right">99.9%</td>
<td align="right">7,889,604</td>
<td align="right">100.0%</td>
<td align="right">101.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,101</td>
<td align="right">0.1%</td>
<td align="right">3,216</td>
<td align="right">0.0%</td>
<td align="right">3.7%</td>
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
<td align="right">332</td>
<td align="right">100.0%</td>
<td align="right">335</td>
<td align="right">100.0%</td>
<td align="right">0.9%</td>
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
<td align="right">89</td>
<td align="right">26.8%</td>
<td align="right">90</td>
<td align="right">26.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">200</td>
<td align="right">60.2%</td>
<td align="right">202</td>
<td align="right">60.3%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">13.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,325,962</td>
<td align="right">6.7%</td>
<td align="right">6,651,753</td>
<td align="right">9.2%</td>
<td align="right">186.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,344,652</td>
<td align="right">93.3%</td>
<td align="right">65,654,028</td>
<td align="right">90.8%</td>
<td align="right">103.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,205</td>
<td align="right">0.0%</td>
<td align="right">4,615</td>
<td align="right">0.0%</td>
<td align="right">9.8%</td>
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
<td align="right">988</td>
<td align="right">91.1%</td>
<td align="right">2,146</td>
<td align="right">93.7%</td>
<td align="right">117.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">97</td>
<td align="right">8.9%</td>
<td align="right">144</td>
<td align="right">6.3%</td>
<td align="right">48.5%</td>
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
<td align="left">dict values</td>
<td align="right">12</td>
<td align="right">1.2%</td>
<td align="right">171</td>
<td align="right">8.0%</td>
<td align="right">1,325.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">76</td>
<td align="right">7.7%</td>
<td align="right">289</td>
<td align="right">13.5%</td>
<td align="right">280.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">597</td>
<td align="right">60.4%</td>
<td align="right">1,354</td>
<td align="right">63.1%</td>
<td align="right">126.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">22</td>
<td align="right">2.2%</td>
<td align="right">43</td>
<td align="right">2.0%</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">74</td>
<td align="right">7.5%</td>
<td align="right">118</td>
<td align="right">5.5%</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">94</td>
<td align="right">9.5%</td>
<td align="right">56</td>
<td align="right">2.6%</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">23</td>
<td align="right">2.3%</td>
<td align="right">24</td>
<td align="right">1.1%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">90</td>
<td align="right">9.1%</td>
<td align="right">91</td>
<td align="right">4.2%</td>
<td align="right">1.1%</td>
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
<td align="right">5,818,951</td>
<td align="right">20.0%</td>
<td align="right">12,835,469</td>
<td align="right">21.7%</td>
<td align="right">120.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,193,361</td>
<td align="right">79.9%</td>
<td align="right">46,409,989</td>
<td align="right">78.3%</td>
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
<td align="right">4,148</td>
<td align="right">0.0%</td>
<td align="right">4,211</td>
<td align="right">0.0%</td>
<td align="right">1.5%</td>
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
<td align="right">2,782</td>
<td align="right">43.3%</td>
<td align="right">4,646</td>
<td align="right">60.7%</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,648</td>
<td align="right">56.7%</td>
<td align="right">3,014</td>
<td align="right">39.3%</td>
<td align="right">-17.4%</td>
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
<td align="right">1,642</td>
<td align="right">59.0%</td>
<td align="right">3,339</td>
<td align="right">71.9%</td>
<td align="right">103.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">768</td>
<td align="right">27.6%</td>
<td align="right">921</td>
<td align="right">19.8%</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">137</td>
<td align="right">4.9%</td>
<td align="right">143</td>
<td align="right">3.1%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">48</td>
<td align="right">1.7%</td>
<td align="right">50</td>
<td align="right">1.1%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">100</td>
<td align="right">3.6%</td>
<td align="right">102</td>
<td align="right">2.2%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">71,711,019</td>
<td align="right">100.0%</td>
<td align="right">150,627,085</td>
<td align="right">100.0%</td>
<td align="right">110.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,858</td>
<td align="right">0.0%</td>
<td align="right">1,887</td>
<td align="right">0.0%</td>
<td align="right">1.6%</td>
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
<td align="right">3,166</td>
<td align="right">100.0%</td>
<td align="right">2,646</td>
<td align="right">100.0%</td>
<td align="right">-16.4%</td>
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
<td align="right">260</td>
<td align="right">98.5%</td>
<td align="right">264</td>
<td align="right">98.5%</td>
<td align="right">1.5%</td>
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
<td align="right">0.8%</td>
<td align="right">2</td>
<td align="right">0.7%</td>
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
<td align="right">1,552</td>
<td align="right">6.3%</td>
<td align="right">1,958</td>
<td align="right">7.3%</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">21,310</td>
<td align="right">86.0%</td>
<td align="right">23,107</td>
<td align="right">86.0%</td>
<td align="right">8.4%</td>
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
<td align="right">423</td>
<td align="right">22.1%</td>
<td align="right">482</td>
<td align="right">26.9%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,492</td>
<td align="right">77.9%</td>
<td align="right">1,312</td>
<td align="right">73.1%</td>
<td align="right">-12.1%</td>
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
<td align="right">86</td>
<td align="right">20.3%</td>
<td align="right">130</td>
<td align="right">27.0%</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">315</td>
<td align="right">74.5%</td>
<td align="right">330</td>
<td align="right">68.5%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">22</td>
<td align="right">5.2%</td>
<td align="right">22</td>
<td align="right">4.6%</td>
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
<td align="right">258</td>
<td align="right">100.0%</td>
<td align="right">262</td>
<td align="right">100.0%</td>
<td align="right">1.6%</td>
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
<td align="right">2,125,952</td>
<td align="right">100.0%</td>
<td align="right">4,271,765</td>
<td align="right">100.0%</td>
<td align="right">100.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">34</td>
<td align="right">0.0%</td>
<td align="right">36</td>
<td align="right">0.0%</td>
<td align="right">5.9%</td>
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
<td align="right">100.0%</td>
<td align="right">32</td>
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
<td align="right">321</td>
<td align="right">0.0%</td>
<td align="right">121,064</td>
<td align="right">0.2%</td>
<td align="right">37,614.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,269,774</td>
<td align="right">21.0%</td>
<td align="right">12,328,885</td>
<td align="right">23.6%</td>
<td align="right">134.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">19,798,594</td>
<td align="right">79.0%</td>
<td align="right">39,674,373</td>
<td align="right">76.1%</td>
<td align="right">100.4%</td>
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
<td align="right">1,536</td>
<td align="right">64.8%</td>
<td align="right">14,642</td>
<td align="right">83.0%</td>
<td align="right">853.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">834</td>
<td align="right">35.2%</td>
<td align="right">2,992</td>
<td align="right">17.0%</td>
<td align="right">258.8%</td>
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
<td align="right">387</td>
<td align="right">25.2%</td>
<td align="right">12,341</td>
<td align="right">84.3%</td>
<td align="right">3,088.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,022</td>
<td align="right">66.5%</td>
<td align="right">2,152</td>
<td align="right">14.7%</td>
<td align="right">110.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">85</td>
<td align="right">5.5%</td>
<td align="right">107</td>
<td align="right">0.7%</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">42</td>
<td align="right">2.7%</td>
<td align="right">42</td>
<td align="right">0.3%</td>
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
<td align="right">13,747,883</td>
<td align="right">100.0%</td>
<td align="right">27,660,349</td>
<td align="right">100.0%</td>
<td align="right">101.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">438</td>
<td align="right">0.0%</td>
<td align="right">444</td>
<td align="right">0.0%</td>
<td align="right">1.4%</td>
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
<td align="right">184</td>
<td align="right">80.0%</td>
<td align="right">124</td>
<td align="right">72.9%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">46</td>
<td align="right">20.0%</td>
<td align="right">46</td>
<td align="right">27.1%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">14,947</td>
<td align="right">0.0%</td>
<td align="right">136,557</td>
<td align="right">0.0%</td>
<td align="right">813.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">14,364,331</td>
<td align="right">1.9%</td>
<td align="right">33,691,876</td>
<td align="right">2.1%</td>
<td align="right">134.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">217,423,875</td>
<td align="right">29.0%</td>
<td align="right">462,783,767</td>
<td align="right">29.1%</td>
<td align="right">112.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">517,282,525</td>
<td align="right">69.1%</td>
<td align="right">1,091,706,871</td>
<td align="right">68.7%</td>
<td align="right">111.0%</td>
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
<td align="right">2,325,962</td>
<td align="right">16.2%</td>
<td align="right">6,651,753</td>
<td align="right">19.8%</td>
<td align="right">186.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">5,269,774</td>
<td align="right">36.7%</td>
<td align="right">12,328,885</td>
<td align="right">36.6%</td>
<td align="right">134.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,818,951</td>
<td align="right">40.6%</td>
<td align="right">12,835,469</td>
<td align="right">38.1%</td>
<td align="right">120.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">709,239</td>
<td align="right">4.9%</td>
<td align="right">1,424,383</td>
<td align="right">4.2%</td>
<td align="right">100.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">200,439</td>
<td align="right">1.4%</td>
<td align="right">395,823</td>
<td align="right">1.2%</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,552</td>
<td align="right">0.0%</td>
<td align="right">1,958</td>
<td align="right">0.0%</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,404</td>
<td align="right">0.1%</td>
<td align="right">8,949</td>
<td align="right">0.0%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,101</td>
<td align="right">0.0%</td>
<td align="right">3,216</td>
<td align="right">0.0%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,559</td>
<td align="right">0.0%</td>
<td align="right">1,586</td>
<td align="right">0.0%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,736</td>
<td align="right">0.0%</td>
<td align="right">1,754</td>
<td align="right">0.0%</td>
<td align="right">1.0%</td>
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
<td align="right">384</td>
<td align="right">2.5%</td>
<td align="right">1,742</td>
<td align="right">1.3%</td>
<td align="right">353.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">405</td>
<td align="right">2.6%</td>
<td align="right">707</td>
<td align="right">0.5%</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">405</td>
<td align="right">2.6%</td>
<td align="right">707</td>
<td align="right">0.5%</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,821</td>
<td align="right">24.9%</td>
<td align="right">2,873</td>
<td align="right">2.1%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,385</td>
<td align="right">15.5%</td>
<td align="right">2,431</td>
<td align="right">1.8%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">896</td>
<td align="right">5.8%</td>
<td align="right">910</td>
<td align="right">0.7%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">962</td>
<td align="right">6.3%</td>
<td align="right">977</td>
<td align="right">0.7%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,886</td>
<td align="right">25.3%</td>
<td align="right">3,945</td>
<td align="right">2.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,569</td>
<td align="right">10.2%</td>
<td align="right">1,586</td>
<td align="right">1.2%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">183</td>
<td align="right">1.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">120,787</td>
<td align="right">88.0%</td>
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
<td align="right">8,485,338</td>
<td align="right">14.1%</td>
<td align="right">17,067,727</td>
<td align="right">14.1%</td>
<td align="right">101.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">49,279,860</td>
<td align="right">81.9%</td>
<td align="right">99,076,684</td>
<td align="right">81.9%</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,123,195</td>
<td align="right">3.5%</td>
<td align="right">4,268,390</td>
<td align="right">3.5%</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">19,579,732</td>
<td align="right">32.5%</td>
<td align="right">39,218,653</td>
<td align="right">32.4%</td>
<td align="right">100.3%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">10,921,076</td>
<td align="right">18.1%</td>
<td align="right">21,847,572</td>
<td align="right">18.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">10,921,076</td>
<td align="right">18.1%</td>
<td align="right">21,847,572</td>
<td align="right">18.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">2,435,738</td>
<td align="right">4.0%</td>
<td align="right">4,779,845</td>
<td align="right">4.0%</td>
<td align="right">96.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">312,525</td>
<td align="right">0.5%</td>
<td align="right">511,437</td>
<td align="right">0.4%</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">521</td>
<td align="right">0.0%</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">972</td>
<td align="right">0.0%</td>
<td align="right">1,179</td>
<td align="right">0.0%</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">7,165</td>
<td align="right">0.0%</td>
<td align="right">7,275</td>
<td align="right">0.0%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">417</td>
<td align="right">0.0%</td>
<td align="right">421</td>
<td align="right">0.0%</td>
<td align="right">1.0%</td>
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
<td align="left">Interpreter immortal decrefs</td>
<td align="right">81,588,453</td>
<td align="right">9.6%</td>
<td align="right">176,458,541</td>
<td align="right">10.7%</td>
<td align="right">116.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">43,952,580</td>
<td align="right">6.0%</td>
<td align="right">94,339,995</td>
<td align="right">6.6%</td>
<td align="right">114.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">345,047,727</td>
<td align="right">47.3%</td>
<td align="right">721,658,459</td>
<td align="right">50.7%</td>
<td align="right">109.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">385,606,402</td>
<td align="right">45.3%</td>
<td align="right">792,657,083</td>
<td align="right">47.9%</td>
<td align="right">105.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">13,030,852</td>
<td align="right"></td>
<td align="right">26,104,005</td>
<td align="right"></td>
<td align="right">100.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">26,560,156</td>
<td align="right"></td>
<td align="right">53,100,740</td>
<td align="right"></td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">26,561,902</td>
<td align="right">49.4%</td>
<td align="right">53,102,357</td>
<td align="right">49.6%</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">30,162,318</td>
<td align="right"></td>
<td align="right">60,251,991</td>
<td align="right"></td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,434,698</td>
<td align="right"></td>
<td align="right">8,858,670</td>
<td align="right"></td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">27,161,402</td>
<td align="right">50.6%</td>
<td align="right">54,031,304</td>
<td align="right">50.4%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">27,167,463</td>
<td align="right">50.6%</td>
<td align="right">54,036,924</td>
<td align="right">50.4%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">68,748,247</td>
<td align="right">9.4%</td>
<td align="right">130,218,144</td>
<td align="right">9.2%</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">274,827,938</td>
<td align="right">32.3%</td>
<td align="right">492,586,567</td>
<td align="right">29.8%</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">109,612,679</td>
<td align="right">12.9%</td>
<td align="right">193,868,906</td>
<td align="right">11.7%</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">271,942,329</td>
<td align="right">37.3%</td>
<td align="right">476,671,358</td>
<td align="right">33.5%</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">2,058</td>
<td align="right"></td>
<td align="right">2,665</td>
<td align="right"></td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">3,542</td>
<td align="right">0.0%</td>
<td align="right">2,872</td>
<td align="right">0.0%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">662</td>
<td align="right"></td>
<td align="right">577</td>
<td align="right"></td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">2,519</td>
<td align="right">0.0%</td>
<td align="right">2,748</td>
<td align="right">0.0%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">7,337</td>
<td align="right"></td>
<td align="right">7,611</td>
<td align="right"></td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">6,683</td>
<td align="right"></td>
<td align="right">6,919</td>
<td align="right"></td>
<td align="right">3.5%</td>
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
<td align="right">428</td>
<td align="right">4,242</td>
<td align="right">7,627,700</td>
<td align="right">819</td>
<td align="right">6,123</td>
<td align="right">16,266,896</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">42</td>
<td align="right">0.8%</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,596</td>
<td align="right">31.1%</td>
<td align="right">381</td>
<td align="right">7.8%</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">836,892,492</td>
<td align="right">1,023.8%</td>
<td align="right">1,422,945,545</td>
<td align="right">1,057.8%</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">2,832</td>
<td align="right">55.2%</td>
<td align="right">4,703</td>
<td align="right">95.8%</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">81,744,748</td>
<td align="right"></td>
<td align="right">134,523,119</td>
<td align="right"></td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">67</td>
<td align="right">1.3%</td>
<td align="right">42</td>
<td align="right">0.9%</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">3,492</td>
<td align="right">68.1%</td>
<td align="right">4,529</td>
<td align="right">92.2%</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">5,130</td>
<td align="right"></td>
<td align="right">4,910</td>
<td align="right"></td>
<td align="right">-4.3%</td>
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
<td align="right">1,596</td>
<td align="right"></td>
<td align="right">381</td>
<td align="right"></td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,554</td>
<td align="right">97.4%</td>
<td align="right">381</td>
<td align="right">100.0%</td>
<td align="right">-75.5%</td>
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
<td align="right">22</td>
<td align="right">1.4%</td>
<td align="right">114</td>
<td align="right">29.9%</td>
<td align="right">418.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">272</td>
<td align="right">17.0%</td>
<td align="right">97</td>
<td align="right">25.5%</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">28</td>
<td align="right">1.8%</td>
<td align="right">21</td>
<td align="right">5.5%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">943</td>
<td align="right">59.1%</td>
<td align="right">42</td>
<td align="right">11.0%</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">158</td>
<td align="right">9.9%</td>
<td align="right">65</td>
<td align="right">17.1%</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">129</td>
<td align="right">8.1%</td>
<td align="right">42</td>
<td align="right">11.0%</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">44</td>
<td align="right">2.8%</td>
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
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">223</td>
<td align="right">14.0%</td>
<td align="right">205</td>
<td align="right">53.8%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">73</td>
<td align="right">4.6%</td>
<td align="right">27</td>
<td align="right">7.1%</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">943</td>
<td align="right">59.1%</td>
<td align="right">42</td>
<td align="right">11.0%</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">157</td>
<td align="right">9.8%</td>
<td align="right">63</td>
<td align="right">16.5%</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">27</td>
<td align="right">1.7%</td>
<td align="right">44</td>
<td align="right">11.5%</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">129</td>
<td align="right">8.1%</td>
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
<td align="left">_DEOPT</td>
<td align="right">626</td>
<td align="right">1,728</td>
<td align="right">176.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">27,759,054</td>
<td align="right">60,483,126</td>
<td align="right">117.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">27,758,909</td>
<td align="right">60,482,103</td>
<td align="right">117.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">32,838,396</td>
<td align="right">68,326,949</td>
<td align="right">108.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">34,055,856</td>
<td align="right">70,554,878</td>
<td align="right">107.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">6,305,995</td>
<td align="right">12,546,287</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">8,430,165</td>
<td align="right">16,771,847</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,250,965</td>
<td align="right">4,437,037</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,250,965</td>
<td align="right">4,437,037</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">31,938,137</td>
<td align="right">60,860,939</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">4,245,682</td>
<td align="right">8,066,351</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">4,246,084</td>
<td align="right">8,066,351</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">42,484,057</td>
<td align="right">79,765,622</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">50,403,765</td>
<td align="right">92,934,817</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">2,122,816</td>
<td align="right">3,840,917</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">2,122,816</td>
<td align="right">3,840,917</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">2,122,816</td>
<td align="right">3,840,917</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,122,906</td>
<td align="right">3,840,917</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,123,478</td>
<td align="right">3,840,917</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">10,525,867</td>
<td align="right">18,815,743</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">4,949,700</td>
<td align="right">8,796,489</td>
<td align="right">77.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">2,890,900</td>
<td align="right">5,117,203</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">2,890,908</td>
<td align="right">5,115,880</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">17,068,629</td>
<td align="right">30,068,183</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,826,745</td>
<td align="right">4,955,572</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">3,531,242</td>
<td align="right">6,181,697</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">66,400,216</td>
<td align="right">115,853,538</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,787,153</td>
<td align="right">6,605,092</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">768,113</td>
<td align="right">1,276,286</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">768,113</td>
<td align="right">1,276,286</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">768,116</td>
<td align="right">1,276,286</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">768,132</td>
<td align="right">1,276,286</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">768,135</td>
<td align="right">1,276,286</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">768,138</td>
<td align="right">1,276,286</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">768,179</td>
<td align="right">1,276,286</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,178,102</td>
<td align="right">3,618,389</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">4,631,771</td>
<td align="right">7,681,834</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">7,851,800</td>
<td align="right">13,021,923</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,025,257</td>
<td align="right">1,699,492</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">384,183</td>
<td align="right">634,809</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,325,106</td>
<td align="right">3,840,917</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">7,784,677</td>
<td align="right">12,846,340</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">901,924</td>
<td align="right">1,487,889</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">81,744,748</td>
<td align="right">134,523,119</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">81,877,605</td>
<td align="right">134,523,119</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,885,208</td>
<td align="right">7,843,823</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">6,296,956</td>
<td align="right">10,072,775</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">3,212,793</td>
<td align="right">5,115,880</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">5,528,840</td>
<td align="right">8,796,489</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">24,300,602</td>
<td align="right">38,479,492</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">703,980</td>
<td align="right">1,114,655</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">4,179,933</td>
<td align="right">6,605,092</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">706,940</td>
<td align="right">1,114,632</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">706,940</td>
<td align="right">1,114,632</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">707,120</td>
<td align="right">1,114,655</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">6,489,981</td>
<td align="right">10,072,775</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,213,455</td>
<td align="right">4,955,549</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">7,182,231</td>
<td align="right">11,044,828</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">10,475,941</td>
<td align="right">15,770,846</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">9,951,867</td>
<td align="right">14,500,719</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">35,549,391</td>
<td align="right">51,144,978</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">897,027</td>
<td align="right">1,276,286</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,702,095</td>
<td align="right">3,840,917</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,390,556</td>
<td align="right">10,283,032</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">7,775,662</td>
<td align="right">10,785,425</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">53,985,213</td>
<td align="right">74,039,288</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,281,340</td>
<td align="right">1,749,464</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,765,854</td>
<td align="right">7,840,043</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">321,223</td>
<td align="right">211,603</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">12,807,340</td>
<td align="right">16,771,847</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,407,891</td>
<td align="right">1,711,157</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">705,037</td>
<td align="right">596,502</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,720,509</td>
<td align="right">5,974,898</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,729,933</td>
<td align="right">1,658,539</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">6,147,002</td>
<td align="right">6,083,837</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">901,887</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">582,431</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">579,157</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">579,138</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">579,112</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">389,569</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">386,151</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">196,992</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">195,941</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">193,842</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">193,743</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">193,615</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">193,097</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">193,097</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">193,089</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">193,058</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">193,044</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">193,042</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">193,041</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">134,046</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">132,857</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">129,019</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">129,019</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">128,869</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">128,863</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">128,848</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">128,841</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">128,841</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">128,841</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">1,747</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">883</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">402</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">374</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">203</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">181</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">181</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">174</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">168</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">138</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">85</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">85</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">85</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">85</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">78</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">72</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">68</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">63</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">61</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">55</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">44</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">42</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">39</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">34</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">28</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">28</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">26</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">21</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">21</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">17</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">14</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">13</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">12</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">11</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">11</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">9</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">6</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">6</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">4</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">3</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">3</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">3</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">1</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">1</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">1</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">24</td>
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
Stats gathered on: 2024-11-13
