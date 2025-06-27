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
<td align="left">STORE_NAME</td>
<td align="right">258</td>
<td align="right">5,418</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">186</td>
<td align="right">3,906</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">98</td>
<td align="right">2,058</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">36</td>
<td align="right">756</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">31</td>
<td align="right">651</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">22</td>
<td align="right">462</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">21</td>
<td align="right">441</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">18</td>
<td align="right">378</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">18</td>
<td align="right">378</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">15</td>
<td align="right">315</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8</td>
<td align="right">168</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">4</td>
<td align="right">84</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">68</td>
<td align="right">1,008</td>
<td align="right">1,382.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">388</td>
<td align="right">4,185</td>
<td align="right">978.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">638</td>
<td align="right">5,532</td>
<td align="right">767.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">290</td>
<td align="right">2,187</td>
<td align="right">654.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">180</td>
<td align="right">1,260</td>
<td align="right">600.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">648</td>
<td align="right">4,421</td>
<td align="right">582.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,148</td>
<td align="right">21,168</td>
<td align="right">572.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">157</td>
<td align="right">675</td>
<td align="right">329.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,958</td>
<td align="right">25,542</td>
<td align="right">328.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">614</td>
<td align="right">2,548</td>
<td align="right">315.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,598</td>
<td align="right">9,904</td>
<td align="right">281.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,283</td>
<td align="right">3,385</td>
<td align="right">163.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">420</td>
<td align="right">1,054</td>
<td align="right">151.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">847</td>
<td align="right">2,055</td>
<td align="right">142.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,443</td>
<td align="right">7,954</td>
<td align="right">131.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,752</td>
<td align="right">8,069</td>
<td align="right">115.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,559</td>
<td align="right">6,689</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,542</td>
<td align="right">2,379</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,542</td>
<td align="right">2,379</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,876</td>
<td align="right">2,648</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">18,141</td>
<td align="right">25,049</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,855</td>
<td align="right">2,547</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">3,438</td>
<td align="right">4,666</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">993</td>
<td align="right">1,338</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">665</td>
<td align="right">895</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">466</td>
<td align="right">619</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">129</td>
<td align="right">87</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">17,293</td>
<td align="right">22,840</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,447</td>
<td align="right">1,785</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,821</td>
<td align="right">3,378</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12,562</td>
<td align="right">14,932</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,858</td>
<td align="right">2,190</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,558</td>
<td align="right">6,514</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">260</td>
<td align="right">216</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,315</td>
<td align="right">1,535</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">15,597</td>
<td align="right">18,080</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,065</td>
<td align="right">1,753</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">264</td>
<td align="right">300</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">782</td>
<td align="right">690</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,986</td>
<td align="right">4,445</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,302</td>
<td align="right">4,771</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,153</td>
<td align="right">3,485</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,829</td>
<td align="right">2,001</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">10,171</td>
<td align="right">11,036</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,495</td>
<td align="right">2,697</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3,422</td>
<td align="right">3,690</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3,422</td>
<td align="right">3,690</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3,422</td>
<td align="right">3,690</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">460</td>
<td align="right">493</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">857</td>
<td align="right">904</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">7,996</td>
<td align="right">8,273</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,966</td>
<td align="right">5,130</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,476</td>
<td align="right">2,398</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,107</td>
<td align="right">1,130</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">7,345</td>
<td align="right">7,473</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">132,950</td>
<td align="right">130,700</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">9,060,372</td>
<td align="right">8,919,528</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">778,633</td>
<td align="right">766,542</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,548,257</td>
<td align="right">1,524,233</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">26,229,947</td>
<td align="right">25,823,914</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">64,641,903</td>
<td align="right">63,641,338</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">81,314,272</td>
<td align="right">80,056,163</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">390,854</td>
<td align="right">384,810</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">10,865,441</td>
<td align="right">10,697,694</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">10,879,113</td>
<td align="right">10,711,296</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">9,318,631</td>
<td align="right">9,174,969</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">9,323,467</td>
<td align="right">9,179,751</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">41,642,465</td>
<td align="right">41,000,607</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,691,852</td>
<td align="right">5,604,138</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,270,280</td>
<td align="right">4,204,485</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">5,823,732</td>
<td align="right">5,734,034</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">12,272,276</td>
<td align="right">12,083,291</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">4,269,889</td>
<td align="right">4,204,140</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">87,289,257</td>
<td align="right">85,945,346</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">65</td>
<td align="right">64</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">103,563,196</td>
<td align="right">101,969,961</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,051,151</td>
<td align="right">4,973,482</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">27,540,986</td>
<td align="right">27,117,933</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">17,345,790</td>
<td align="right">17,079,368</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">105,790,583</td>
<td align="right">104,168,429</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">72,655,985</td>
<td align="right">71,542,318</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">120,531,066</td>
<td align="right">118,684,663</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">4,269,333</td>
<td align="right">4,203,953</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">196</td>
<td align="right">193</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">26,240,643</td>
<td align="right">25,839,070</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,701,632</td>
<td align="right">9,553,208</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">143,686,681</td>
<td align="right">141,493,818</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">392,552</td>
<td align="right">386,562</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,558,519</td>
<td align="right">9,412,682</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">21,845,781</td>
<td align="right">21,512,568</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">12,180,741</td>
<td align="right">11,994,968</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">53,564,065</td>
<td align="right">52,748,707</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">23,925,295</td>
<td align="right">23,561,260</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">144,304,987</td>
<td align="right">142,111,105</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">147,085,760</td>
<td align="right">144,850,295</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">11,529,612</td>
<td align="right">11,354,548</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">22,770,500</td>
<td align="right">22,424,920</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">390,432,602</td>
<td align="right">384,513,910</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">391,635</td>
<td align="right">385,699</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">390,851</td>
<td align="right">384,927</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">388,656</td>
<td align="right">382,766</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">35,572,043</td>
<td align="right">35,034,453</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">10,871,720</td>
<td align="right">10,707,603</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,874,698</td>
<td align="right">17,604,883</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">44,914,205</td>
<td align="right">44,237,065</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">6,872,949</td>
<td align="right">6,769,535</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,995,482</td>
<td align="right">6,890,333</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,283,409</td>
<td align="right">4,219,055</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,921,424</td>
<td align="right">15,682,594</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,270,190</td>
<td align="right">4,206,158</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,317,185</td>
<td align="right">9,177,640</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">13,599,178</td>
<td align="right">13,395,739</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">28,433,396</td>
<td align="right">28,010,448</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,051,785</td>
<td align="right">19,753,555</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">39,218,947</td>
<td align="right">38,635,844</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">56,314,503</td>
<td align="right">55,478,634</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,672,429</td>
<td align="right">4,603,280</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">6,205,709</td>
<td align="right">6,115,227</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,843,238</td>
<td align="right">2,801,880</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">390,816</td>
<td align="right">385,133</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,386,758</td>
<td align="right">4,323,590</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,838,451</td>
<td align="right">2,798,307</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">828,929</td>
<td align="right">817,359</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,237,228</td>
<td align="right">13,054,673</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,563,450</td>
<td align="right">1,541,916</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,425,135</td>
<td align="right">1,405,648</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,843,092</td>
<td align="right">12,667,977</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,430,142</td>
<td align="right">1,412,395</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,565,454</td>
<td align="right">1,547,312</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">510,078</td>
<td align="right">504,242</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">132,534</td>
<td align="right">131,071</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,175,484</td>
<td align="right">1,164,694</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,410</td>
<td align="right">3,438</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">391,315</td>
<td align="right">388,767</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">131,713</td>
<td align="right">130,963</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">406,137</td>
<td align="right">404,283</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right"></td>
<td align="right">32,135,349</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">41</td>
<td align="right">0.0%</td>
<td align="right">861</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">19,089</td>
<td align="right">0.0%</td>
<td align="right">19.8%</td>
</tr>
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
<td align="right">46,393,746</td>
<td align="right">99.9%</td>
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
<td align="left">Success</td>
<td align="right">347</td>
<td align="right">25.5%</td>
<td align="right">1,827</td>
<td align="right">48.7%</td>
<td align="right">426.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,016</td>
<td align="right">74.5%</td>
<td align="right">1,924</td>
<td align="right">51.3%</td>
<td align="right">89.4%</td>
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
<td align="left">subscr range</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">42</td>
<td align="right">2.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">347</td>
<td align="right">34.2%</td>
<td align="right">763</td>
<td align="right">39.7%</td>
<td align="right">119.9%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">115</td>
<td align="right">11.3%</td>
<td align="right">231</td>
<td align="right">12.0%</td>
<td align="right">100.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">311</td>
<td align="right">30.6%</td>
<td align="right">569</td>
<td align="right">29.6%</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">111</td>
<td align="right">10.9%</td>
<td align="right">169</td>
<td align="right">8.8%</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">130</td>
<td align="right">12.8%</td>
<td align="right">150</td>
<td align="right">7.8%</td>
<td align="right">15.4%</td>
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
<td align="right">2,190</td>
<td align="right">100.0%</td>
<td align="right">17.9%</td>
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
<td align="right">5,743</td>
<td align="right">0.0%</td>
<td align="right">17,183</td>
<td align="right">0.0%</td>
<td align="right">199.2%</td>
</tr>
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
<td align="right">85,572,182</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">3,990</td>
<td align="right">0.0%</td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right">3,990</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">12,349</td>
<td align="right">100.0%</td>
<td align="right">190.7%</td>
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
<td align="right">588</td>
<td align="right">46.7%</td>
<td align="right">2,000.0%</td>
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
<td align="right">672</td>
<td align="right">100.0%</td>
<td align="right">342.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10</td>
<td align="right">0.0%</td>
<td align="right">210</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
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
<td align="right">1,403,982</td>
<td align="right">47.5%</td>
<td align="right">-1.4%</td>
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
<td align="right">1,551,652</td>
<td align="right">52.5%</td>
<td align="right">-0.9%</td>
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
<td align="right">176</td>
<td align="right">23.4%</td>
<td align="right">756</td>
<td align="right">45.4%</td>
<td align="right">329.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">576</td>
<td align="right">76.6%</td>
<td align="right">910</td>
<td align="right">54.6%</td>
<td align="right">58.0%</td>
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
<td align="right">93</td>
<td align="right">16.1%</td>
<td align="right">233</td>
<td align="right">25.6%</td>
<td align="right">150.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">440</td>
<td align="right">76.4%</td>
<td align="right">634</td>
<td align="right">69.7%</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">7.5%</td>
<td align="right">43</td>
<td align="right">4.7%</td>
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
<td align="right">3,216</td>
<td align="right">0.0%</td>
<td align="right">5,949</td>
<td align="right">0.1%</td>
<td align="right">85.0%</td>
</tr>
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
<td align="right">7,771,789</td>
<td align="right">99.9%</td>
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
<td align="left">Success</td>
<td align="right">8</td>
<td align="right">2.3%</td>
<td align="right">168</td>
<td align="right">22.7%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">335</td>
<td align="right">97.7%</td>
<td align="right">572</td>
<td align="right">77.3%</td>
<td align="right">70.7%</td>
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
<td align="right">169</td>
<td align="right">29.5%</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">202</td>
<td align="right">60.3%</td>
<td align="right">360</td>
<td align="right">62.9%</td>
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">12.8%</td>
<td align="right">43</td>
<td align="right">7.5%</td>
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
<td align="right">3,078</td>
<td align="right">0.0%</td>
<td align="right">1,757</td>
<td align="right">0.0%</td>
<td align="right">-42.9%</td>
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
<td align="right">80,856,426</td>
<td align="right">83.8%</td>
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
<td align="right">15,916,753</td>
<td align="right">16.2%</td>
<td align="right">15,675,115</td>
<td align="right">16.2%</td>
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
<td align="left">Success</td>
<td align="right">110</td>
<td align="right">2.3%</td>
<td align="right">969</td>
<td align="right">13.0%</td>
<td align="right">780.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,584</td>
<td align="right">97.7%</td>
<td align="right">6,512</td>
<td align="right">87.0%</td>
<td align="right">42.1%</td>
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
<td align="right">56</td>
<td align="right">1.2%</td>
<td align="right">213</td>
<td align="right">3.3%</td>
<td align="right">280.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">118</td>
<td align="right">2.6%</td>
<td align="right">317</td>
<td align="right">4.9%</td>
<td align="right">168.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">91</td>
<td align="right">2.0%</td>
<td align="right">210</td>
<td align="right">3.2%</td>
<td align="right">130.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">469</td>
<td align="right">10.2%</td>
<td align="right">780</td>
<td align="right">12.0%</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">66</td>
<td align="right">1.4%</td>
<td align="right">105</td>
<td align="right">1.6%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">43</td>
<td align="right">0.9%</td>
<td align="right">63</td>
<td align="right">1.0%</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1,034</td>
<td align="right">22.6%</td>
<td align="right">1,437</td>
<td align="right">22.1%</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,179</td>
<td align="right">25.7%</td>
<td align="right">1,501</td>
<td align="right">23.0%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,354</td>
<td align="right">29.5%</td>
<td align="right">1,714</td>
<td align="right">26.3%</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">174</td>
<td align="right">3.8%</td>
<td align="right">172</td>
<td align="right">2.6%</td>
<td align="right">-1.1%</td>
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
<td align="left">string</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
<td align="right">84</td>
<td align="right">84 / 0 !!</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,853</td>
<td align="right">1,853 / 0 !!</td>
<td align="right">2,185</td>
<td align="right">2,185 / 0 !!</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,019</td>
<td align="right">3,019 / 0 !!</td>
<td align="right">3,093</td>
<td align="right">3,093 / 0 !!</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">778,789</td>
<td align="right">778,789 / 0 !!</td>
<td align="right">766,746</td>
<td align="right">766,746 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">393,156</td>
<td align="right">393,156 / 0 !!</td>
<td align="right">387,077</td>
<td align="right">387,077 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,078,235</td>
<td align="right">6,078,235 / 0 !!</td>
<td align="right">5,985,286</td>
<td align="right">5,985,286 / 0 !!</td>
<td align="right">-1.5%</td>
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
<td align="left">list</td>
<td align="right">4,274,228</td>
<td align="right">4,274,228 / 0 !!</td>
<td align="right">4,209,754</td>
<td align="right">4,209,754 / 0 !!</td>
<td align="right">-1.5%</td>
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
<td align="right">45,724,760</td>
<td align="right">78.3%</td>
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
<td align="right">12,835,469</td>
<td align="right">21.7%</td>
<td align="right">12,650,798</td>
<td align="right">21.7%</td>
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
<td align="right">4,211</td>
<td align="right">0.0%</td>
<td align="right">4,168</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">9,429</td>
<td align="right">57.3%</td>
<td align="right">240.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,652</td>
<td align="right">62.7%</td>
<td align="right">7,033</td>
<td align="right">42.7%</td>
<td align="right">51.2%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.6%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">102</td>
<td align="right">2.2%</td>
<td align="right">380</td>
<td align="right">5.4%</td>
<td align="right">272.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">50</td>
<td align="right">1.1%</td>
<td align="right">168</td>
<td align="right">2.4%</td>
<td align="right">236.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">143</td>
<td align="right">3.1%</td>
<td align="right">421</td>
<td align="right">6.0%</td>
<td align="right">194.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">927</td>
<td align="right">19.9%</td>
<td align="right">1,389</td>
<td align="right">19.7%</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">3,339</td>
<td align="right">71.8%</td>
<td align="right">4,506</td>
<td align="right">64.1%</td>
<td align="right">35.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">500</td>
<td align="right">0.0%</td>
<td align="right">10,500</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
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
<td align="right">169,502,366</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">1,900</td>
<td align="right">0.0%</td>
<td align="right">0.6%</td>
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
<td align="right">10,668</td>
<td align="right">100.0%</td>
<td align="right">302.9%</td>
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
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">42</td>
<td align="right">10.9%</td>
<td align="right">2,000.0%</td>
</tr>
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
<td align="right">300</td>
<td align="right">78.1%</td>
<td align="right">13.6%</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">4,750</td>
<td align="right">12.4%</td>
<td align="right">142.6%</td>
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
<td align="right">30,179</td>
<td align="right">78.9%</td>
<td align="right">30.6%</td>
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
<td align="right">2,772</td>
<td align="right">83.5%</td>
<td align="right">111.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">482</td>
<td align="right">26.9%</td>
<td align="right">547</td>
<td align="right">16.5%</td>
<td align="right">13.5%</td>
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
<td align="right">210</td>
<td align="right">38.4%</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">330</td>
<td align="right">68.5%</td>
<td align="right">315</td>
<td align="right">57.6%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">22</td>
<td align="right">4.6%</td>
<td align="right">22</td>
<td align="right">4.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36</td>
<td align="right">0.0%</td>
<td align="right">756</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
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
<td align="right">4,206,788</td>
<td align="right">100.0%</td>
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
<td align="left">Success</td>
<td align="right">32</td>
<td align="right">100.0%</td>
<td align="right">252</td>
<td align="right">100.0%</td>
<td align="right">687.5%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,530,654</td>
<td align="right">25.1%</td>
<td align="right">13,324,946</td>
<td align="right">25.1%</td>
<td align="right">-1.5%</td>
</tr>
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
<td align="right">38,980,193</td>
<td align="right">73.5%</td>
<td align="right">-1.5%</td>
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
<td align="right">673,802</td>
<td align="right">1.3%</td>
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
<td align="left">Success</td>
<td align="right">13,632</td>
<td align="right">16.7%</td>
<td align="right">15,472</td>
<td align="right">18.5%</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">67,792</td>
<td align="right">83.3%</td>
<td align="right">68,021</td>
<td align="right">81.5%</td>
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
<td align="left">tuple</td>
<td align="right">65</td>
<td align="right">0.1%</td>
<td align="right">105</td>
<td align="right">0.2%</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,110</td>
<td align="right">3.1%</td>
<td align="right">2,876</td>
<td align="right">4.2%</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">65,575</td>
<td align="right">96.7%</td>
<td align="right">64,998</td>
<td align="right">95.6%</td>
<td align="right">-0.9%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">444</td>
<td align="right">0.0%</td>
<td align="right">1,518</td>
<td align="right">0.0%</td>
<td align="right">241.9%</td>
</tr>
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
<td align="right">27,236,525</td>
<td align="right">100.0%</td>
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
<td align="left">Success</td>
<td align="right">124</td>
<td align="right">72.9%</td>
<td align="right">924</td>
<td align="right">89.7%</td>
<td align="right">645.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">46</td>
<td align="right">27.1%</td>
<td align="right">106</td>
<td align="right">10.3%</td>
<td align="right">130.4%</td>
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
<td align="right">106</td>
<td align="right">100.0%</td>
<td align="right">130.4%</td>
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
<td align="right">731,967,673</td>
<td align="right">32.8%</td>
<td align="right">720,850,818</td>
<td align="right">32.3%</td>
<td align="right">-1.5%</td>
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
<td align="right">686,688</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
</tr>
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
<td align="right">54,598,162</td>
<td align="right">2.4%</td>
<td align="right">-1.4%</td>
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
<td align="right">1,454,749,452</td>
<td align="right">65.2%</td>
<td align="right">0.7%</td>
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
<td align="left">LOAD_GLOBAL</td>
<td align="right">500</td>
<td align="right">0.0%</td>
<td align="right">10,500</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,743</td>
<td align="right">0.0%</td>
<td align="right">17,183</td>
<td align="right">0.0%</td>
<td align="right">199.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,958</td>
<td align="right">0.0%</td>
<td align="right">4,750</td>
<td align="right">0.0%</td>
<td align="right">142.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,216</td>
<td align="right">0.0%</td>
<td align="right">5,949</td>
<td align="right">0.0%</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">15,930</td>
<td align="right">0.0%</td>
<td align="right">19,089</td>
<td align="right">0.0%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,858</td>
<td align="right">0.0%</td>
<td align="right">2,190</td>
<td align="right">0.0%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">13,530,654</td>
<td align="right">30.9%</td>
<td align="right">13,324,946</td>
<td align="right">30.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,916,753</td>
<td align="right">36.4%</td>
<td align="right">15,675,115</td>
<td align="right">36.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,835,469</td>
<td align="right">29.3%</td>
<td align="right">12,650,798</td>
<td align="right">29.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,424,383</td>
<td align="right">3.3%</td>
<td align="right">1,403,982</td>
<td align="right">3.3%</td>
<td align="right">-1.4%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">191</td>
<td align="right">0.0%</td>
<td align="right">323</td>
<td align="right">0.0%</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,594</td>
<td align="right">0.2%</td>
<td align="right">577</td>
<td align="right">0.1%</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,425</td>
<td align="right">0.3%</td>
<td align="right">3,119</td>
<td align="right">0.5%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">979</td>
<td align="right">0.1%</td>
<td align="right">1,044</td>
<td align="right">0.2%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">910</td>
<td align="right">0.1%</td>
<td align="right">856</td>
<td align="right">0.1%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,742</td>
<td align="right">0.2%</td>
<td align="right">1,674</td>
<td align="right">0.2%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,945</td>
<td align="right">0.6%</td>
<td align="right">3,866</td>
<td align="right">0.6%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">683,700</td>
<td align="right">98.1%</td>
<td align="right">673,100</td>
<td align="right">98.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,336</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">567</td>
<td align="right">0.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">315</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">18</td>
<td align="right">0.0%</td>
<td align="right">378</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">431</td>
<td align="right">0.0%</td>
<td align="right">3,847</td>
<td align="right">0.0%</td>
<td align="right">792.6%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">7,275</td>
<td align="right">0.0%</td>
<td align="right">8,565</td>
<td align="right">0.0%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,179</td>
<td align="right">0.0%</td>
<td align="right">1,321</td>
<td align="right">0.0%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">521</td>
<td align="right">0.0%</td>
<td align="right">553</td>
<td align="right">0.0%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,268,390</td>
<td align="right">3.5%</td>
<td align="right">4,202,424</td>
<td align="right">3.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">17,066,534</td>
<td align="right">14.1%</td>
<td align="right">16,802,934</td>
<td align="right">14.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">99,078,317</td>
<td align="right">81.9%</td>
<td align="right">97,563,493</td>
<td align="right">81.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">21,845,939</td>
<td align="right">18.1%</td>
<td align="right">21,513,264</td>
<td align="right">18.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">21,845,939</td>
<td align="right">18.1%</td>
<td align="right">21,513,264</td>
<td align="right">18.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">39,219,103</td>
<td align="right">32.4%</td>
<td align="right">38,636,538</td>
<td align="right">32.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,779,405</td>
<td align="right">4.0%</td>
<td align="right">4,710,330</td>
<td align="right">4.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">510,997</td>
<td align="right">0.4%</td>
<td align="right">507,528</td>
<td align="right">0.4%</td>
<td align="right">-0.7%</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">2,702</td>
<td align="right">0.0%</td>
<td align="right">4,722</td>
<td align="right">0.0%</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,572</td>
<td align="right"></td>
<td align="right">2,732</td>
<td align="right"></td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">2,665</td>
<td align="right"></td>
<td align="right">3,885</td>
<td align="right"></td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">18,506</td>
<td align="right"></td>
<td align="right">14,628</td>
<td align="right"></td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">13,548</td>
<td align="right"></td>
<td align="right">16,372</td>
<td align="right"></td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">483,079,219</td>
<td align="right">57.4%</td>
<td align="right">475,739,163</td>
<td align="right">57.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">571,770,327</td>
<td align="right">62.6%</td>
<td align="right">563,097,921</td>
<td align="right">62.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">68,621,366</td>
<td align="right">66.7%</td>
<td align="right">67,586,158</td>
<td align="right">66.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">68,619,152</td>
<td align="right"></td>
<td align="right">67,584,819</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">259,477,926</td>
<td align="right">30.8%</td>
<td align="right">255,645,485</td>
<td align="right">30.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">12,952,702</td>
<td align="right">1.5%</td>
<td align="right">12,762,344</td>
<td align="right">1.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">40,420,034</td>
<td align="right"></td>
<td align="right">39,827,964</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">253,404,013</td>
<td align="right">27.7%</td>
<td align="right">249,702,560</td>
<td align="right">27.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">26,098,076</td>
<td align="right"></td>
<td align="right">25,721,150</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">34,237,330</td>
<td align="right">33.3%</td>
<td align="right">33,750,593</td>
<td align="right">33.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">34,242,780</td>
<td align="right">33.3%</td>
<td align="right">33,758,101</td>
<td align="right">33.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">86,436,078</td>
<td align="right">9.5%</td>
<td align="right">85,237,225</td>
<td align="right">9.5%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">2,748</td>
<td align="right">0.0%</td>
<td align="right">2,786</td>
<td align="right">0.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">86,298,853</td>
<td align="right">10.3%</td>
<td align="right">85,137,442</td>
<td align="right">10.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">8,852,684</td>
<td align="right"></td>
<td align="right">8,736,664</td>
<td align="right"></td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">2,215,997</td>
<td align="right">0.2%</td>
<td align="right">2,189,381</td>
<td align="right">0.2%</td>
<td align="right">-1.2%</td>
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
<td align="right">9,471,370</td>
<td align="right">558,403</td>
<td align="right">1,536,887</td>
<td align="right">826</td>
<td align="right">38,022</td>
<td align="right">10,208,233</td>
<td align="right">565,357</td>
<td align="right">1,579,412</td>
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
Stats gathered on: 2025-06-27
