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
<td align="right">87,289,257</td>
<td align="right">173</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,430,142</td>
<td align="right">80,427</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,838,451</td>
<td align="right">774,340</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,386,758</td>
<td align="right">1,542,517</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,921,424</td>
<td align="right">5,883,833</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,691,852</td>
<td align="right">2,197,545</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,995,482</td>
<td align="right">2,911,921</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">11,529,612</td>
<td align="right">5,107,578</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">26,229,947</td>
<td align="right">11,629,186</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">26,240,643</td>
<td align="right">11,639,344</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">23,925,295</td>
<td align="right">10,629,157</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">12,272,276</td>
<td align="right">5,458,063</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">72,655,985</td>
<td align="right">33,312,299</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,051,785</td>
<td align="right">9,338,651</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">103,563,196</td>
<td align="right">49,451,834</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">144,304,987</td>
<td align="right">69,140,450</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">147,085,760</td>
<td align="right">70,552,799</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">390,432,602</td>
<td align="right">187,800,628</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">143,686,681</td>
<td align="right">69,420,255</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">120,531,066</td>
<td align="right">59,370,101</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,548,257</td>
<td align="right">768,127</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,558,519</td>
<td align="right">4,747,978</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,843,238</td>
<td align="right">1,412,908</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">13,599,178</td>
<td align="right">6,758,846</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">27,540,986</td>
<td align="right">13,691,607</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">81,314,272</td>
<td align="right">40,426,059</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">64,641,903</td>
<td align="right">32,137,875</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">6,205,709</td>
<td align="right">3,085,372</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">10,865,441</td>
<td align="right">5,403,347</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">105,790,583</td>
<td align="right">52,613,234</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">41,642,465</td>
<td align="right">20,710,351</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">35,572,043</td>
<td align="right">17,691,802</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,701,632</td>
<td align="right">4,825,852</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">390,851</td>
<td align="right">194,421</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">4,269,889</td>
<td align="right">2,124,104</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">4,269,333</td>
<td align="right">2,123,935</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">9,318,631</td>
<td align="right">4,635,946</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">53,564,065</td>
<td align="right">26,648,081</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,270,280</td>
<td align="right">2,124,489</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">9,060,372</td>
<td align="right">4,507,700</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,270,190</td>
<td align="right">2,124,969</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,317,185</td>
<td align="right">4,636,533</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">5,823,732</td>
<td align="right">2,898,299</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">828,929</td>
<td align="right">412,564</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">10,871,720</td>
<td align="right">5,411,042</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">388,656</td>
<td align="right">193,457</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">17,345,790</td>
<td align="right">8,634,626</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">9,323,467</td>
<td align="right">4,641,401</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,874,698</td>
<td align="right">8,901,972</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,051,151</td>
<td align="right">2,515,664</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,425,135</td>
<td align="right">709,817</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">10,879,113</td>
<td align="right">5,418,844</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">12,180,741</td>
<td align="right">6,070,107</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">6,872,949</td>
<td align="right">3,425,284</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">391,635</td>
<td align="right">195,193</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">778,633</td>
<td align="right">388,184</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">390,854</td>
<td align="right">194,865</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,843,092</td>
<td align="right">6,404,640</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,237,228</td>
<td align="right">6,604,411</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,672,429</td>
<td align="right">2,331,550</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,283,409</td>
<td align="right">2,137,797</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">39,218,947</td>
<td align="right">19,579,895</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">390,816</td>
<td align="right">195,206</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">392,552</td>
<td align="right">196,222</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">21,845,781</td>
<td align="right">10,920,575</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">22,770,500</td>
<td align="right">11,391,599</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,563,450</td>
<td align="right">782,901</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">56,314,503</td>
<td align="right">28,214,881</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">391,315</td>
<td align="right">196,078</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">28,433,396</td>
<td align="right">14,255,076</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,565,454</td>
<td align="right">784,877</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,175,484</td>
<td align="right">589,558</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">44,914,205</td>
<td align="right">22,976,535</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">406,137</td>
<td align="right">209,981</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">420</td>
<td align="right">225</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">510,078</td>
<td align="right">312,635</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">7,996</td>
<td align="right">5,290</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">180</td>
<td align="right">240</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,821</td>
<td align="right">1,896</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">3,438</td>
<td align="right">2,315</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,829</td>
<td align="right">1,234</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,855</td>
<td align="right">1,260</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,986</td>
<td align="right">2,728</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,447</td>
<td align="right">1,047</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,107</td>
<td align="right">838</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,065</td>
<td align="right">1,592</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,542</td>
<td align="right">1,267</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,542</td>
<td align="right">1,267</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,476</td>
<td align="right">2,060</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,148</td>
<td align="right">3,668</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,315</td>
<td align="right">1,106</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,153</td>
<td align="right">2,727</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">15,597</td>
<td align="right">13,722</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,302</td>
<td align="right">3,790</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,966</td>
<td align="right">4,512</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">614</td>
<td align="right">668</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,752</td>
<td align="right">3,467</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">18,141</td>
<td align="right">16,798</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,495</td>
<td align="right">2,331</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,958</td>
<td align="right">6,273</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12,562</td>
<td align="right">11,931</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">10,171</td>
<td align="right">9,701</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">17,293</td>
<td align="right">16,658</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">131,713</td>
<td align="right">128,609</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">132,534</td>
<td align="right">129,544</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">132,950</td>
<td align="right">129,953</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">129</td>
<td align="right">127</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">260</td>
<td align="right">256</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">65</td>
<td align="right">64</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">782</td>
<td align="right">770</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">196</td>
<td align="right">193</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">654</td>
<td align="right">644</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">262</td>
<td align="right">258</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,410</td>
<td align="right">3,358</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">7,345</td>
<td align="right">7,233</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">460</td>
<td align="right">453</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3,422</td>
<td align="right">3,370</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3,422</td>
<td align="right">3,370</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3,422</td>
<td align="right">3,370</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">857</td>
<td align="right">844</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">264</td>
<td align="right">260</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,558</td>
<td align="right">5,474</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">993</td>
<td align="right">978</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,858</td>
<td align="right">1,830</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">665</td>
<td align="right">655</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">466</td>
<td align="right">459</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,876</td>
<td align="right">1,848</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,443</td>
<td align="right">3,394</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">847</td>
<td align="right">835</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,559</td>
<td align="right">3,509</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,283</td>
<td align="right">1,265</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,598</td>
<td align="right">2,564</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">157</td>
<td align="right">155</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">648</td>
<td align="right">641</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">290</td>
<td align="right">287</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">638</td>
<td align="right">632</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">388</td>
<td align="right">385</td>
<td align="right">-0.8%</td>
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
<td align="right">68</td>
<td align="right">68</td>
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
<td align="left">BUILD_SLICE</td>
<td align="right">21</td>
<td align="right">21</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">42,067,250</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">1,404,032</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">765,893</td>
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
<td align="right">47,096,259</td>
<td align="right">100.0%</td>
<td align="right">23,432,885</td>
<td align="right">99.9%</td>
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
<td align="right">15,930</td>
<td align="right">0.0%</td>
<td align="right">15,248</td>
<td align="right">0.1%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">41</td>
<td align="right">0.0%</td>
<td align="right">41</td>
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
<td align="right">347</td>
<td align="right">25.5%</td>
<td align="right">367</td>
<td align="right">26.0%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,016</td>
<td align="right">74.5%</td>
<td align="right">1,043</td>
<td align="right">74.0%</td>
<td align="right">2.7%</td>
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
<td align="right">11.3%</td>
<td align="right">131</td>
<td align="right">12.6%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">347</td>
<td align="right">34.2%</td>
<td align="right">363</td>
<td align="right">34.8%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">111</td>
<td align="right">10.9%</td>
<td align="right">108</td>
<td align="right">10.4%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">311</td>
<td align="right">30.6%</td>
<td align="right">309</td>
<td align="right">29.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">130</td>
<td align="right">12.8%</td>
<td align="right">130</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">2</td>
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
<td align="right">1,858</td>
<td align="right">100.0%</td>
<td align="right">1,830</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">86,877,682</td>
<td align="right">100.0%</td>
<td align="right">43,313,573</td>
<td align="right">100.0%</td>
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
<td align="right">4,033</td>
<td align="right">0.0%</td>
<td align="right">3,970</td>
<td align="right">0.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,743</td>
<td align="right">0.0%</td>
<td align="right">5,663</td>
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
<td align="right">4,248</td>
<td align="right">100.0%</td>
<td align="right">4,580</td>
<td align="right">100.0%</td>
<td align="right">7.8%</td>
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
<td align="right">15.6%</td>
<td align="right">28</td>
<td align="right">11.7%</td>
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
<td align="right">152</td>
<td align="right">100.0%</td>
<td align="right">212</td>
<td align="right">100.0%</td>
<td align="right">39.5%</td>
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
<td align="right">709,239</td>
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
<td align="right">785,457</td>
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
<td align="right">576</td>
<td align="right">76.6%</td>
<td align="right">402</td>
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
<td align="right">76.4%</td>
<td align="right">266</td>
<td align="right">66.2%</td>
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
<td align="right">7,889,602</td>
<td align="right">100.0%</td>
<td align="right">3,290,004</td>
<td align="right">99.9%</td>
<td align="right">-58.3%</td>
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
<td align="right">3,169</td>
<td align="right">0.1%</td>
<td align="right">-1.5%</td>
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
<td align="right">335</td>
<td align="right">97.7%</td>
<td align="right">332</td>
<td align="right">97.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8</td>
<td align="right">2.3%</td>
<td align="right">8</td>
<td align="right">2.4%</td>
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
<td align="right">90</td>
<td align="right">26.9%</td>
<td align="right">89</td>
<td align="right">26.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">202</td>
<td align="right">60.3%</td>
<td align="right">200</td>
<td align="right">60.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">12.8%</td>
<td align="right">43</td>
<td align="right">13.0%</td>
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
<td align="right">15,916,753</td>
<td align="right">16.2%</td>
<td align="right">5,881,636</td>
<td align="right">12.6%</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">82,121,886</td>
<td align="right">83.8%</td>
<td align="right">40,904,406</td>
<td align="right">87.4%</td>
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
<td align="right">3,078</td>
<td align="right">0.0%</td>
<td align="right">2,178</td>
<td align="right">0.0%</td>
<td align="right">-29.2%</td>
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
<td align="right">4,584</td>
<td align="right">97.7%</td>
<td align="right">2,110</td>
<td align="right">96.0%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">110</td>
<td align="right">2.3%</td>
<td align="right">88</td>
<td align="right">4.0%</td>
<td align="right">-20.0%</td>
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
<td align="right">1,179</td>
<td align="right">25.7%</td>
<td align="right">295</td>
<td align="right">14.0%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">174</td>
<td align="right">3.8%</td>
<td align="right">67</td>
<td align="right">3.2%</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">469</td>
<td align="right">10.2%</td>
<td align="right">184</td>
<td align="right">8.7%</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,354</td>
<td align="right">29.5%</td>
<td align="right">683</td>
<td align="right">32.4%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">43</td>
<td align="right">0.9%</td>
<td align="right">22</td>
<td align="right">1.0%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1,034</td>
<td align="right">22.6%</td>
<td align="right">534</td>
<td align="right">25.3%</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">56</td>
<td align="right">1.2%</td>
<td align="right">53</td>
<td align="right">2.5%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">66</td>
<td align="right">1.4%</td>
<td align="right">65</td>
<td align="right">3.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">91</td>
<td align="right">2.0%</td>
<td align="right">90</td>
<td align="right">4.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">118</td>
<td align="right">2.6%</td>
<td align="right">117</td>
<td align="right">5.5%</td>
<td align="right">-0.8%</td>
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
<td align="right">6,078,235</td>
<td align="right">6,078,235 / 0 !!</td>
<td align="right">3,022,304</td>
<td align="right">3,022,304 / 0 !!</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">778,789</td>
<td align="right">778,789 / 0 !!</td>
<td align="right">387,801</td>
<td align="right">387,801 / 0 !!</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">4,274,228</td>
<td align="right">4,274,228 / 0 !!</td>
<td align="right">2,128,882</td>
<td align="right">2,128,882 / 0 !!</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">393,156</td>
<td align="right">393,156 / 0 !!</td>
<td align="right">197,447</td>
<td align="right">197,447 / 0 !!</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">328</td>
<td align="right">328 / 0 !!</td>
<td align="right">323</td>
<td align="right">323 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,019</td>
<td align="right">3,019 / 0 !!</td>
<td align="right">2,973</td>
<td align="right">2,973 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,853</td>
<td align="right">1,853 / 0 !!</td>
<td align="right">1,825</td>
<td align="right">1,825 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
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
<td align="right">46,410,257</td>
<td align="right">78.3%</td>
<td align="right">22,559,655</td>
<td align="right">77.9%</td>
<td align="right">-51.4%</td>
</tr>
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
<td align="right">6,398,108</td>
<td align="right">22.1%</td>
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
<td align="right">4,211</td>
<td align="right">0.0%</td>
<td align="right">4,148</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">4,652</td>
<td align="right">62.7%</td>
<td align="right">2,926</td>
<td align="right">46.2%</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,770</td>
<td align="right">37.3%</td>
<td align="right">3,409</td>
<td align="right">53.8%</td>
<td align="right">23.1%</td>
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
<td align="right">71.8%</td>
<td align="right">1,774</td>
<td align="right">60.6%</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">927</td>
<td align="right">19.9%</td>
<td align="right">774</td>
<td align="right">26.5%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">50</td>
<td align="right">1.1%</td>
<td align="right">48</td>
<td align="right">1.6%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">102</td>
<td align="right">2.2%</td>
<td align="right">100</td>
<td align="right">3.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">143</td>
<td align="right">3.1%</td>
<td align="right">141</td>
<td align="right">4.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">172,118,188</td>
<td align="right">100.0%</td>
<td align="right">83,673,471</td>
<td align="right">100.0%</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,889</td>
<td align="right">0.0%</td>
<td align="right">1,860</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">2,648</td>
<td align="right">100.0%</td>
<td align="right">3,168</td>
<td align="right">100.0%</td>
<td align="right">19.6%</td>
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
<td align="right">260</td>
<td align="right">98.5%</td>
<td align="right">-1.5%</td>
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
<td align="right">1,552</td>
<td align="right">6.3%</td>
<td align="right">-20.7%</td>
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
<td align="right">21,310</td>
<td align="right">86.0%</td>
<td align="right">-7.8%</td>
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
<td align="right">77.9%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">482</td>
<td align="right">26.9%</td>
<td align="right">423</td>
<td align="right">22.1%</td>
<td align="right">-12.2%</td>
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
<td align="right">130</td>
<td align="right">27.0%</td>
<td align="right">86</td>
<td align="right">20.3%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">330</td>
<td align="right">68.5%</td>
<td align="right">315</td>
<td align="right">74.5%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">22</td>
<td align="right">4.6%</td>
<td align="right">22</td>
<td align="right">5.2%</td>
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
<td align="right">258</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">2,125,952</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">39,578,859</td>
<td align="right">73.5%</td>
<td align="right">18,469,135</td>
<td align="right">72.2%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">683,971</td>
<td align="right">1.3%</td>
<td align="right">339,462</td>
<td align="right">1.3%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,530,654</td>
<td align="right">25.1%</td>
<td align="right">6,724,307</td>
<td align="right">26.3%</td>
<td align="right">-50.3%</td>
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
<td align="right">67,792</td>
<td align="right">83.3%</td>
<td align="right">33,707</td>
<td align="right">82.3%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,632</td>
<td align="right">16.7%</td>
<td align="right">7,232</td>
<td align="right">17.7%</td>
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
<td align="left">mapping</td>
<td align="right">65,575</td>
<td align="right">96.7%</td>
<td align="right">32,554</td>
<td align="right">96.6%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,110</td>
<td align="right">3.1%</td>
<td align="right">1,068</td>
<td align="right">3.2%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">65</td>
<td align="right">0.1%</td>
<td align="right">43</td>
<td align="right">0.1%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">0.1%</td>
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
<td align="right">11,709,869</td>
<td align="right">100.0%</td>
<td align="right">-57.7%</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">55,355,137</td>
<td align="right">2.5%</td>
<td align="right">24,901,357</td>
<td align="right">2.3%</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">731,967,673</td>
<td align="right">32.8%</td>
<td align="right">355,392,529</td>
<td align="right">32.8%</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,444,538,529</td>
<td align="right">64.7%</td>
<td align="right">701,880,976</td>
<td align="right">64.8%</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">697,233</td>
<td align="right">0.0%</td>
<td align="right">351,669</td>
<td align="right">0.0%</td>
<td align="right">-49.6%</td>
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
<td align="right">15,916,753</td>
<td align="right">36.4%</td>
<td align="right">5,881,636</td>
<td align="right">29.8%</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">13,530,654</td>
<td align="right">30.9%</td>
<td align="right">6,724,307</td>
<td align="right">34.1%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,424,383</td>
<td align="right">3.3%</td>
<td align="right">709,239</td>
<td align="right">3.6%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,835,469</td>
<td align="right">29.3%</td>
<td align="right">6,398,108</td>
<td align="right">32.4%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,958</td>
<td align="right">0.0%</td>
<td align="right">1,552</td>
<td align="right">0.0%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">15,930</td>
<td align="right">0.0%</td>
<td align="right">15,248</td>
<td align="right">0.1%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,858</td>
<td align="right">0.0%</td>
<td align="right">1,830</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,216</td>
<td align="right">0.0%</td>
<td align="right">3,169</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,743</td>
<td align="right">0.0%</td>
<td align="right">5,663</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">500</td>
<td align="right">0.0%</td>
<td align="right">500</td>
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
<td align="left">TO_BOOL_STR</td>
<td align="right">683,700</td>
<td align="right">98.1%</td>
<td align="right">339,200</td>
<td align="right">96.5%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,742</td>
<td align="right">0.2%</td>
<td align="right">895</td>
<td align="right">0.3%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191</td>
<td align="right">0.0%</td>
<td align="right">183</td>
<td align="right">0.1%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,336</td>
<td align="right">0.2%</td>
<td align="right">1,283</td>
<td align="right">0.4%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,425</td>
<td align="right">0.3%</td>
<td align="right">2,379</td>
<td align="right">0.7%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">910</td>
<td align="right">0.1%</td>
<td align="right">896</td>
<td align="right">0.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">130</td>
<td align="right">0.0%</td>
<td align="right">128</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">979</td>
<td align="right">0.1%</td>
<td align="right">964</td>
<td align="right">0.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,945</td>
<td align="right">0.6%</td>
<td align="right">3,886</td>
<td align="right">1.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,594</td>
<td align="right">0.2%</td>
<td align="right">1,577</td>
<td align="right">0.4%</td>
<td align="right">-1.1%</td>
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
<td align="right">17,066,534</td>
<td align="right">14.1%</td>
<td align="right">8,485,237</td>
<td align="right">14.1%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">99,078,317</td>
<td align="right">81.9%</td>
<td align="right">49,280,205</td>
<td align="right">81.9%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,268,390</td>
<td align="right">3.5%</td>
<td align="right">2,123,195</td>
<td align="right">3.5%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">39,219,103</td>
<td align="right">32.4%</td>
<td align="right">19,579,986</td>
<td align="right">32.5%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">21,845,939</td>
<td align="right">18.1%</td>
<td align="right">10,920,731</td>
<td align="right">18.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">21,845,939</td>
<td align="right">18.1%</td>
<td align="right">10,920,731</td>
<td align="right">18.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,779,405</td>
<td align="right">4.0%</td>
<td align="right">2,435,494</td>
<td align="right">4.0%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">510,997</td>
<td align="right">0.4%</td>
<td align="right">312,281</td>
<td align="right">0.5%</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">521</td>
<td align="right">0.0%</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,179</td>
<td align="right">0.0%</td>
<td align="right">972</td>
<td align="right">0.0%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">7,275</td>
<td align="right">0.0%</td>
<td align="right">7,165</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">431</td>
<td align="right">0.0%</td>
<td align="right">427</td>
<td align="right">0.0%</td>
<td align="right">-0.9%</td>
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
<td align="left">Mortal increfs</td>
<td align="right">259,471,817</td>
<td align="right">30.8%</td>
<td align="right">129,223,126</td>
<td align="right">30.6%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">253,397,937</td>
<td align="right">27.7%</td>
<td align="right">126,329,326</td>
<td align="right">27.6%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">26,104,176</td>
<td align="right"></td>
<td align="right">13,030,826</td>
<td align="right"></td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">2,215,997</td>
<td align="right">0.2%</td>
<td align="right">1,107,783</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">68,619,152</td>
<td align="right"></td>
<td align="right">34,339,224</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">68,621,366</td>
<td align="right">66.7%</td>
<td align="right">34,341,308</td>
<td align="right">66.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">571,770,327</td>
<td align="right">62.6%</td>
<td align="right">286,169,298</td>
<td align="right">62.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">8,858,704</td>
<td align="right"></td>
<td align="right">4,434,831</td>
<td align="right"></td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">483,079,219</td>
<td align="right">57.4%</td>
<td align="right">241,963,923</td>
<td align="right">57.3%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">40,420,078</td>
<td align="right"></td>
<td align="right">20,251,998</td>
<td align="right"></td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">12,952,702</td>
<td align="right">1.5%</td>
<td align="right">6,511,392</td>
<td align="right">1.5%</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">34,237,330</td>
<td align="right">33.3%</td>
<td align="right">17,253,039</td>
<td align="right">33.4%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">34,242,780</td>
<td align="right">33.3%</td>
<td align="right">17,257,843</td>
<td align="right">33.4%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">86,417,914</td>
<td align="right">9.5%</td>
<td align="right">43,727,649</td>
<td align="right">9.6%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">86,280,715</td>
<td align="right">10.2%</td>
<td align="right">44,539,582</td>
<td align="right">10.5%</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">552</td>
<td align="right"></td>
<td align="right">749</td>
<td align="right"></td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">2,665</td>
<td align="right"></td>
<td align="right">2,058</td>
<td align="right"></td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">2,702</td>
<td align="right">0.0%</td>
<td align="right">2,287</td>
<td align="right">0.0%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">2,748</td>
<td align="right">0.0%</td>
<td align="right">2,517</td>
<td align="right">0.0%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">6,510</td>
<td align="right"></td>
<td align="right">6,879</td>
<td align="right"></td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">7,448</td>
<td align="right"></td>
<td align="right">7,642</td>
<td align="right"></td>
<td align="right">2.6%</td>
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
<td align="right">26,888</td>
<td align="right">9,471,319</td>
<td align="right">558,403</td>
<td align="right">1,536,887</td>
<td align="right">408</td>
<td align="right">25,814</td>
<td align="right">3,356,523</td>
<td align="right">81,840</td>
<td align="right">743,582</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-18
