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
<td align="left">STORE_ATTR</td>
<td align="right">19</td>
<td align="right">399</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">11</td>
<td align="right">231</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">8</td>
<td align="right">168</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">7</td>
<td align="right">147</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">7</td>
<td align="right">147</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6</td>
<td align="right">126</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5</td>
<td align="right">105</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4</td>
<td align="right">84</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">3</td>
<td align="right">63</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3</td>
<td align="right">63</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1</td>
<td align="right">21</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">163</td>
<td align="right">1,323</td>
<td align="right">711.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">89</td>
<td align="right">548</td>
<td align="right">515.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">349</td>
<td align="right">1,809</td>
<td align="right">418.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">25</td>
<td align="right">105</td>
<td align="right">320.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">64</td>
<td align="right">43</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,090</td>
<td align="right">1,294</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">781</td>
<td align="right">849</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">10,143</td>
<td align="right">10,827</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,335</td>
<td align="right">2,379</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">389,489</td>
<td align="right">382,533</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,469,370</td>
<td align="right">2,431,133</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,559,954</td>
<td align="right">1,535,802</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,047,719</td>
<td align="right">1,031,518</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,170,227</td>
<td align="right">1,152,134</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">3,118,101</td>
<td align="right">3,069,945</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,471,119</td>
<td align="right">2,432,955</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,362,339</td>
<td align="right">2,325,855</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,560,993</td>
<td align="right">1,536,885</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,558,662</td>
<td align="right">1,534,590</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,305,878</td>
<td align="right">1,285,710</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,295,000</td>
<td align="right">1,275,000</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,295,000</td>
<td align="right">1,275,000</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,042,216</td>
<td align="right">1,026,120</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,041,439</td>
<td align="right">1,025,355</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">779,331</td>
<td align="right">767,295</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">520,590</td>
<td align="right">512,550</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">520,331</td>
<td align="right">512,295</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">390,313</td>
<td align="right">384,285</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">8,288</td>
<td align="right">8,160</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">5,180</td>
<td align="right">5,100</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,885</td>
<td align="right">3,825</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,108</td>
<td align="right">3,060</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,813</td>
<td align="right">1,785</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">777</td>
<td align="right">765</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">518</td>
<td align="right">510</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">518</td>
<td align="right">510</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">518</td>
<td align="right">510</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">259</td>
<td align="right">255</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">8,323,031</td>
<td align="right">8,194,490</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,603,016</td>
<td align="right">2,562,815</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,081,778</td>
<td align="right">5,003,295</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,300,764</td>
<td align="right">1,280,675</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">531,275</td>
<td align="right">523,070</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">520,656</td>
<td align="right">512,615</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">266,577</td>
<td align="right">262,460</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">265,023</td>
<td align="right">260,930</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">261,915</td>
<td align="right">257,870</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">2,603,988</td>
<td align="right">2,563,812</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">2,603,988</td>
<td align="right">2,563,812</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">2,603,988</td>
<td align="right">2,563,812</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">4,417,768</td>
<td align="right">4,349,640</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">8,101,144</td>
<td align="right">7,976,230</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,428,905</td>
<td align="right">1,406,877</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,694,965</td>
<td align="right">1,668,848</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">3,509,976</td>
<td align="right">3,455,928</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,031,411</td>
<td align="right">3,969,350</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,558,666</td>
<td align="right">1,534,674</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">658,121</td>
<td align="right">647,997</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,948,204</td>
<td align="right">1,918,236</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">12,483,389</td>
<td align="right">12,291,416</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">533,542</td>
<td align="right">525,342</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,867,401</td>
<td align="right">2,823,357</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">7,417,938</td>
<td align="right">7,304,023</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,213,943</td>
<td align="right">2,179,971</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">782,961</td>
<td align="right">770,949</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">262,598</td>
<td align="right">258,570</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,005,755</td>
<td align="right">12,806,295</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">526,550</td>
<td align="right">518,478</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,304,880</td>
<td align="right">1,284,879</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,197,257</td>
<td align="right">5,117,611</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">4,026,505</td>
<td align="right">3,964,820</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">17,053,708</td>
<td align="right">16,792,472</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,723,227</td>
<td align="right">5,635,598</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">25,036,199</td>
<td align="right">24,653,703</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,296,072</td>
<td align="right">4,230,504</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">8,726,892</td>
<td align="right">8,593,715</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">11,712,355</td>
<td align="right">11,533,711</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">18,866,844</td>
<td align="right">18,579,085</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">18,869,505</td>
<td align="right">18,581,727</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,949,771</td>
<td align="right">1,920,039</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,820,361</td>
<td align="right">4,746,856</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">100,727,423</td>
<td align="right">99,191,883</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">777,008</td>
<td align="right">765,168</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">27,888,002</td>
<td align="right">27,463,124</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">18,346,854</td>
<td align="right">18,067,368</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,767,064</td>
<td align="right">9,618,283</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">21,846,461</td>
<td align="right">21,513,828</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,830,504</td>
<td align="right">1,802,634</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,080,570</td>
<td align="right">2,048,898</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,832,512</td>
<td align="right">1,804,651</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">653,788</td>
<td align="right">643,851</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,351,737</td>
<td align="right">12,164,059</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,043,785</td>
<td align="right">1,027,965</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,762,533</td>
<td align="right">6,660,074</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">519,562</td>
<td align="right">511,698</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,557,134</td>
<td align="right">1,533,606</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">519,563</td>
<td align="right">511,719</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">519,563</td>
<td align="right">511,719</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,950,046</td>
<td align="right">1,920,630</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,733,281</td>
<td align="right">2,692,149</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,039,129</td>
<td align="right">1,023,501</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">16,683,709</td>
<td align="right">16,433,071</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,033,679</td>
<td align="right">12,837,911</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,044,118</td>
<td align="right">1,028,453</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">1,042,240</td>
<td align="right">1,026,624</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,620,828</td>
<td align="right">2,581,733</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,946,503</td>
<td align="right">1,917,482</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">786,780</td>
<td align="right">775,112</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,689,510</td>
<td align="right">1,664,478</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,216,865</td>
<td align="right">2,184,331</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,259,100</td>
<td align="right">3,211,354</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,688,571</td>
<td align="right">1,664,174</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,049,003</td>
<td align="right">1,033,863</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">782,997</td>
<td align="right">771,705</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">780,220</td>
<td align="right">769,091</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">909,144</td>
<td align="right">896,184</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">519,590</td>
<td align="right">512,286</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">648,064</td>
<td align="right">638,976</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">522,225</td>
<td align="right">514,921</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">780,943</td>
<td align="right">770,043</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">389,569</td>
<td align="right">384,213</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">264,589</td>
<td align="right">261,008</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">261,103</td>
<td align="right">257,693</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">259,627</td>
<td align="right">256,478</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">391,709</td>
<td align="right">387,681</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right"></td>
<td align="right">14,387,371</td>
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
<td align="right">12</td>
<td align="right">0.0%</td>
<td align="right">252</td>
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
<td align="right">521,897</td>
<td align="right">4.6%</td>
<td align="right">514,057</td>
<td align="right">4.6%</td>
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
<td align="right">10,934,619</td>
<td align="right">95.4%</td>
<td align="right">10,771,449</td>
<td align="right">95.4%</td>
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
<td align="right">52</td>
<td align="right">15.8%</td>
<td align="right">252</td>
<td align="right">28.5%</td>
<td align="right">384.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">277</td>
<td align="right">84.2%</td>
<td align="right">633</td>
<td align="right">71.5%</td>
<td align="right">128.5%</td>
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
<td align="left">multiply different types</td>
<td align="right">93</td>
<td align="right">33.6%</td>
<td align="right">232</td>
<td align="right">36.7%</td>
<td align="right">149.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">140</td>
<td align="right">50.5%</td>
<td align="right">337</td>
<td align="right">53.2%</td>
<td align="right">140.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">44</td>
<td align="right">15.9%</td>
<td align="right">64</td>
<td align="right">10.1%</td>
<td align="right">45.5%</td>
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
<td align="right">782,961</td>
<td align="right">100.0%</td>
<td align="right">770,949</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">48</td>
<td align="right">0.0%</td>
<td align="right">1,008</td>
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
<td align="right">74</td>
<td align="right">0.0%</td>
<td align="right">1,494</td>
<td align="right">0.0%</td>
<td align="right">1,918.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,307,623</td>
<td align="right">100.0%</td>
<td align="right">31,814,268</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">1,008</td>
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
<td align="right">323</td>
<td align="right">100.0%</td>
<td align="right">1,323</td>
<td align="right">100.0%</td>
<td align="right">309.6%</td>
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
<td align="right">2</td>
<td align="right">2 / 0 !!</td>
<td align="right">42</td>
<td align="right">42 / 0 !!</td>
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
<td align="right">3</td>
<td align="right">27.3%</td>
<td align="right">63</td>
<td align="right">27.3%</td>
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
<td align="right">8</td>
<td align="right">100.0%</td>
<td align="right">168</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">4,812,353</td>
<td align="right">94.8%</td>
<td align="right">4,739,372</td>
<td align="right">94.8%</td>
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
<td align="right">264,189</td>
<td align="right">5.2%</td>
<td align="right">260,289</td>
<td align="right">5.2%</td>
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
<td align="right">25</td>
<td align="right">6.2%</td>
<td align="right">105</td>
<td align="right">14.6%</td>
<td align="right">320.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">375</td>
<td align="right">93.8%</td>
<td align="right">614</td>
<td align="right">85.4%</td>
<td align="right">63.7%</td>
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
<td align="right">375</td>
<td align="right">100.0%</td>
<td align="right">614</td>
<td align="right">100.0%</td>
<td align="right">63.7%</td>
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
<td align="right">2,216,036</td>
<td align="right">47.3%</td>
<td align="right">2,182,452</td>
<td align="right">47.3%</td>
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
<td align="right">2,467,794</td>
<td align="right">52.7%</td>
<td align="right">2,430,522</td>
<td align="right">52.7%</td>
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
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">42</td>
<td align="right">2.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">827</td>
<td align="right">99.8%</td>
<td align="right">1,837</td>
<td align="right">97.8%</td>
<td align="right">122.1%</td>
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
<td align="right">138</td>
<td align="right">16.7%</td>
<td align="right">317</td>
<td align="right">17.3%</td>
<td align="right">129.7%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">621</td>
<td align="right">75.1%</td>
<td align="right">1,393</td>
<td align="right">75.8%</td>
<td align="right">124.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">68</td>
<td align="right">8.2%</td>
<td align="right">127</td>
<td align="right">6.9%</td>
<td align="right">86.8%</td>
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
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">336</td>
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
<td align="right">5,476,394</td>
<td align="right">87.4%</td>
<td align="right">5,392,497</td>
<td align="right">87.4%</td>
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
<td align="right">786,396</td>
<td align="right">12.6%</td>
<td align="right">774,371</td>
<td align="right">12.6%</td>
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
<td align="right">6</td>
<td align="right">1.6%</td>
<td align="right">126</td>
<td align="right">17.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">378</td>
<td align="right">98.4%</td>
<td align="right">615</td>
<td align="right">83.0%</td>
<td align="right">62.7%</td>
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
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">21</td>
<td align="right">3.4%</td>
<td align="right">950.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">45</td>
<td align="right">11.9%</td>
<td align="right">85</td>
<td align="right">13.8%</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">200</td>
<td align="right">52.9%</td>
<td align="right">318</td>
<td align="right">51.7%</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">43</td>
<td align="right">11.4%</td>
<td align="right">63</td>
<td align="right">10.2%</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">88</td>
<td align="right">23.3%</td>
<td align="right">128</td>
<td align="right">20.8%</td>
<td align="right">45.5%</td>
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
<td align="right">3,701</td>
<td align="right">3,701 / 0 !!</td>
<td align="right">3,844</td>
<td align="right">3,844 / 0 !!</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">1,036</td>
<td align="right">1,036 / 0 !!</td>
<td align="right">1,020</td>
<td align="right">1,020 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">777</td>
<td align="right">777 / 0 !!</td>
<td align="right">765</td>
<td align="right">765 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">518</td>
<td align="right">518 / 0 !!</td>
<td align="right">510</td>
<td align="right">510 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">261,332</td>
<td align="right">261,332 / 0 !!</td>
<td align="right">257,316</td>
<td align="right">257,316 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,564,111</td>
<td align="right">1,564,111 / 0 !!</td>
<td align="right">1,540,155</td>
<td align="right">1,540,155 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,037</td>
<td align="right">1,037 / 0 !!</td>
<td align="right">1,041</td>
<td align="right">1,041 / 0 !!</td>
<td align="right">0.4%</td>
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
<td align="right">24,319</td>
<td align="right">0.1%</td>
<td align="right">37,555</td>
<td align="right">0.1%</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">43,981,677</td>
<td align="right">93.1%</td>
<td align="right">43,294,684</td>
<td align="right">93.0%</td>
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
<td align="right">3,247,978</td>
<td align="right">6.9%</td>
<td align="right">3,198,857</td>
<td align="right">6.9%</td>
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
<td align="right">371</td>
<td align="right">29.7%</td>
<td align="right">1,597</td>
<td align="right">50.5%</td>
<td align="right">330.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">877</td>
<td align="right">70.3%</td>
<td align="right">1,567</td>
<td align="right">49.5%</td>
<td align="right">78.7%</td>
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
<td align="right">319</td>
<td align="right">36.4%</td>
<td align="right">697</td>
<td align="right">44.5%</td>
<td align="right">118.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">134</td>
<td align="right">15.3%</td>
<td align="right">212</td>
<td align="right">13.5%</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">134</td>
<td align="right">15.3%</td>
<td align="right">212</td>
<td align="right">13.5%</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">134</td>
<td align="right">15.3%</td>
<td align="right">212</td>
<td align="right">13.5%</td>
<td align="right">58.2%</td>
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
<td align="right">14</td>
<td align="right">0.0%</td>
<td align="right">294</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">735</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,575</td>
<td align="right">0.0%</td>
<td align="right">2,265</td>
<td align="right">0.0%</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">31,898,948</td>
<td align="right">100.0%</td>
<td align="right">31,414,731</td>
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
<td align="right">152</td>
<td align="right">100.0%</td>
<td align="right">1,050</td>
<td align="right">100.0%</td>
<td align="right">590.8%</td>
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
<td align="right">521,108</td>
<td align="right">100.0%</td>
<td align="right">513,060</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,770</td>
<td align="right">0.1%</td>
<td align="right">7,650</td>
<td align="right">0.1%</td>
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
<td align="right">12,997,985</td>
<td align="right">99.9%</td>
<td align="right">12,798,645</td>
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
<td align="right">19</td>
<td align="right">100.0%</td>
<td align="right">399</td>
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
<td align="right">1,044</td>
<td align="right">0.2%</td>
<td align="right">1,188</td>
<td align="right">0.2%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">658,128</td>
<td align="right">99.8%</td>
<td align="right">648,144</td>
<td align="right">99.8%</td>
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
<td align="right">1</td>
<td align="right">2.2%</td>
<td align="right">21</td>
<td align="right">19.8%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45</td>
<td align="right">97.8%</td>
<td align="right">85</td>
<td align="right">80.2%</td>
<td align="right">88.9%</td>
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
<td align="right">45</td>
<td align="right">100.0%</td>
<td align="right">85</td>
<td align="right">100.0%</td>
<td align="right">88.9%</td>
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
<td align="right">794</td>
<td align="right">0.0%</td>
<td align="right">828</td>
<td align="right">0.0%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,852,555</td>
<td align="right">98.3%</td>
<td align="right">14,626,127</td>
<td align="right">98.3%</td>
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
<td align="right">260,892</td>
<td align="right">1.7%</td>
<td align="right">257,123</td>
<td align="right">1.7%</td>
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
<td align="right">33</td>
<td align="right">15.6%</td>
<td align="right">252</td>
<td align="right">44.2%</td>
<td align="right">663.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">179</td>
<td align="right">84.4%</td>
<td align="right">318</td>
<td align="right">55.8%</td>
<td align="right">77.7%</td>
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
<td align="right">114</td>
<td align="right">63.7%</td>
<td align="right">233</td>
<td align="right">73.3%</td>
<td align="right">104.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">44</td>
<td align="right">24.6%</td>
<td align="right">64</td>
<td align="right">20.1%</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">11.7%</td>
<td align="right">21</td>
<td align="right">6.6%</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">1,947,541</td>
<td align="right">100.0%</td>
<td align="right">1,918,544</td>
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
<td align="right">24</td>
<td align="right">100.0%</td>
<td align="right">84</td>
<td align="right">100.0%</td>
<td align="right">250.0%</td>
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
<td align="right">35,054</td>
<td align="right">0.0%</td>
<td align="right">50,404</td>
<td align="right">0.0%</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">314,272,376</td>
<td align="right">60.9%</td>
<td align="right">323,869,250</td>
<td align="right">62.0%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">192,012,843</td>
<td align="right">37.2%</td>
<td align="right">189,070,938</td>
<td align="right">36.2%</td>
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
<td align="right">9,927,794</td>
<td align="right">1.9%</td>
<td align="right">9,785,222</td>
<td align="right">1.9%</td>
<td align="right">-1.4%</td>
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
<td align="right">14</td>
<td align="right">0.0%</td>
<td align="right">294</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">74</td>
<td align="right">0.0%</td>
<td align="right">1,494</td>
<td align="right">0.0%</td>
<td align="right">1,918.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,044</td>
<td align="right">0.0%</td>
<td align="right">1,188</td>
<td align="right">0.0%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">782,961</td>
<td align="right">9.7%</td>
<td align="right">770,949</td>
<td align="right">9.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">786,396</td>
<td align="right">9.7%</td>
<td align="right">774,371</td>
<td align="right">9.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,216,036</td>
<td align="right">27.4%</td>
<td align="right">2,182,452</td>
<td align="right">27.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,247,978</td>
<td align="right">40.2%</td>
<td align="right">3,198,857</td>
<td align="right">40.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">521,897</td>
<td align="right">6.5%</td>
<td align="right">514,057</td>
<td align="right">6.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">264,189</td>
<td align="right">3.3%</td>
<td align="right">260,289</td>
<td align="right">3.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">260,892</td>
<td align="right">3.2%</td>
<td align="right">257,123</td>
<td align="right">3.2%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">48</td>
<td align="right">0.1%</td>
<td align="right">1,008</td>
<td align="right">2.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">336</td>
<td align="right">0.7%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">14,270</td>
<td align="right">40.1%</td>
<td align="right">27,610</td>
<td align="right">54.3%</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,575</td>
<td align="right">4.4%</td>
<td align="right">2,265</td>
<td align="right">4.5%</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">519</td>
<td align="right">1.5%</td>
<td align="right">489</td>
<td align="right">1.0%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">519</td>
<td align="right">1.5%</td>
<td align="right">489</td>
<td align="right">1.0%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">7,770</td>
<td align="right">21.8%</td>
<td align="right">7,650</td>
<td align="right">15.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,049</td>
<td align="right">28.2%</td>
<td align="right">9,945</td>
<td align="right">19.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">770</td>
<td align="right">2.2%</td>
<td align="right">765</td>
<td align="right">1.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">147</td>
<td align="right">0.3%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">16,919,395</td>
<td align="right">89.7%</td>
<td align="right">16,661,074</td>
<td align="right">89.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">1,565,669</td>
<td align="right">8.3%</td>
<td align="right">1,541,769</td>
<td align="right">8.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">19,389,076</td>
<td align="right">102.8%</td>
<td align="right">19,093,614</td>
<td align="right">102.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,950,118</td>
<td align="right">10.3%</td>
<td align="right">1,920,821</td>
<td align="right">10.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,950,118</td>
<td align="right">10.3%</td>
<td align="right">1,920,821</td>
<td align="right">10.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,950,118</td>
<td align="right">10.3%</td>
<td align="right">1,920,821</td>
<td align="right">10.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,950,118</td>
<td align="right">10.3%</td>
<td align="right">1,920,821</td>
<td align="right">10.3%</td>
<td align="right">-1.5%</td>
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
<td align="right">1,653</td>
<td align="right"></td>
<td align="right">1,722</td>
<td align="right"></td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">23,987,908</td>
<td align="right"></td>
<td align="right">23,345,025</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">69,133,468</td>
<td align="right">21.3%</td>
<td align="right">67,737,590</td>
<td align="right">21.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">104,114,524</td>
<td align="right">32.1%</td>
<td align="right">102,014,674</td>
<td align="right">32.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,292,411</td>
<td align="right"></td>
<td align="right">1,268,698</td>
<td align="right"></td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">20,372,950</td>
<td align="right">46.2%</td>
<td align="right">20,039,988</td>
<td align="right">46.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,291,398</td>
<td align="right"></td>
<td align="right">1,270,603</td>
<td align="right"></td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">92,346,230</td>
<td align="right">30.5%</td>
<td align="right">90,911,881</td>
<td align="right">30.5%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">274,022</td>
<td align="right">0.6%</td>
<td align="right">269,790</td>
<td align="right">0.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,734</td>
<td align="right">0.0%</td>
<td align="right">6,630</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">518</td>
<td align="right">0.0%</td>
<td align="right">510</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">13,293,836</td>
<td align="right">4.4%</td>
<td align="right">13,090,067</td>
<td align="right">4.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">122,818,642</td>
<td align="right">40.5%</td>
<td align="right">120,938,601</td>
<td align="right">40.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,300,189</td>
<td align="right"></td>
<td align="right">1,280,289</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">20,374,038</td>
<td align="right"></td>
<td align="right">20,062,517</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">148,302,297</td>
<td align="right">45.8%</td>
<td align="right">146,037,274</td>
<td align="right">45.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">6,369,361</td>
<td align="right"></td>
<td align="right">6,272,680</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">2,347,890</td>
<td align="right">0.7%</td>
<td align="right">2,312,730</td>
<td align="right">0.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">74,435,822</td>
<td align="right">24.6%</td>
<td align="right">73,333,977</td>
<td align="right">24.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">23,712,160</td>
<td align="right">53.8%</td>
<td align="right">23,367,634</td>
<td align="right">53.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">23,431,404</td>
<td align="right">53.2%</td>
<td align="right">23,091,214</td>
<td align="right">53.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">9,667,301</td>
<td align="right"></td>
<td align="right">9,535,208</td>
<td align="right"></td>
<td align="right">-1.4%</td>
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
<td align="right">2,168,504</td>
<td align="right">41,743,448</td>
<td align="right">734,432</td>
<td align="right">2,596,972</td>
<td align="right">1,296</td>
<td align="right">2,045,733</td>
<td align="right">38,799,178</td>
<td align="right">732,098</td>
<td align="right">2,468,829</td>
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
Stats gathered on: 2025-06-27
