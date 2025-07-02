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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">3,448,706</td>
<td align="right">875,199</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,026,423</td>
<td align="right">311,856</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,699,838</td>
<td align="right">1,215,977</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">157,436</td>
<td align="right">55,530</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">79,076</td>
<td align="right">29,511</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">523,813</td>
<td align="right">200,618</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">398,502</td>
<td align="right">153,699</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,856,768</td>
<td align="right">749,393</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">531,229</td>
<td align="right">215,103</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,932,734</td>
<td align="right">789,302</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,909,505</td>
<td align="right">781,600</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">454,889</td>
<td align="right">187,072</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,150,794</td>
<td align="right">485,142</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,809,743</td>
<td align="right">1,192,513</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">417,909</td>
<td align="right">178,836</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,256,636</td>
<td align="right">543,501</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,339,271</td>
<td align="right">579,411</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,392,747</td>
<td align="right">3,673,601</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">733,363</td>
<td align="right">323,511</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,591,096</td>
<td align="right">6,898,359</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">241,694</td>
<td align="right">107,436</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,101,320</td>
<td align="right">935,537</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,179,967</td>
<td align="right">983,241</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,275,847</td>
<td align="right">576,415</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">946,078</td>
<td align="right">432,669</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">962,663</td>
<td align="right">440,916</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">893,533</td>
<td align="right">410,844</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,233,308</td>
<td align="right">573,600</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">7,408,415</td>
<td align="right">3,462,062</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">609,174</td>
<td align="right">284,823</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">14,941,475</td>
<td align="right">6,993,806</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">13,093,533</td>
<td align="right">6,146,493</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">698,225</td>
<td align="right">328,881</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,080,636</td>
<td align="right">1,451,164</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,550,749</td>
<td align="right">5,463,414</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">11,883,019</td>
<td align="right">5,685,692</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">25,282,416</td>
<td align="right">12,135,160</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,462,600</td>
<td align="right">702,932</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">11,321,895</td>
<td align="right">5,441,523</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">919,093</td>
<td align="right">442,281</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">74,586,272</td>
<td align="right">35,908,895</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,033,804</td>
<td align="right">2,433,984</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">4,986,850</td>
<td align="right">2,416,052</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,593,306</td>
<td align="right">3,678,874</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,811,555</td>
<td align="right">878,829</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">6,422,587</td>
<td align="right">3,118,554</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,999,430</td>
<td align="right">972,432</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,722,170</td>
<td align="right">840,825</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">972,563</td>
<td align="right">475,503</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,081,319</td>
<td align="right">1,022,874</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,561,788</td>
<td align="right">2,244,728</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,156,176</td>
<td align="right">1,558,032</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,491,650</td>
<td align="right">1,725,567</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,100,582</td>
<td align="right">4,004,094</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">24,495,694</td>
<td align="right">12,108,315</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,955,441</td>
<td align="right">966,861</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,918,430</td>
<td align="right">949,872</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">12,566,075</td>
<td align="right">6,237,561</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">369,227</td>
<td align="right">183,909</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,652,647</td>
<td align="right">2,819,347</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">24,552</td>
<td align="right">12,264</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,482,875</td>
<td align="right">740,772</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">818,722</td>
<td align="right">409,122</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">57,316</td>
<td align="right">28,644</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">450,463</td>
<td align="right">225,183</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">278,473</td>
<td align="right">139,209</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">712,596</td>
<td align="right">356,244</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">991,111</td>
<td align="right">495,495</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">851,864</td>
<td align="right">425,880</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">720,808</td>
<td align="right">360,360</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">614,325</td>
<td align="right">307,125</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">475,078</td>
<td align="right">237,510</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">442,314</td>
<td align="right">221,130</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">147,438</td>
<td align="right">73,710</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">131,056</td>
<td align="right">65,520</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">122,865</td>
<td align="right">61,425</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">106,483</td>
<td align="right">53,235</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">81,910</td>
<td align="right">40,950</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">65,528</td>
<td align="right">32,760</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">49,146</td>
<td align="right">24,570</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">40,955</td>
<td align="right">20,475</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,425,255</td>
<td align="right">712,551</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,645,777</td>
<td align="right">1,322,769</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,785,708</td>
<td align="right">892,779</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,359,769</td>
<td align="right">679,833</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,137,956</td>
<td align="right">1,068,900</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,589,138</td>
<td align="right">794,514</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,589,138</td>
<td align="right">794,514</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,589,138</td>
<td align="right">794,514</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">360,425</td>
<td align="right">180,201</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,138,619</td>
<td align="right">569,274</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">876,507</td>
<td align="right">438,234</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,449,961</td>
<td align="right">724,968</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">630,777</td>
<td align="right">315,384</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">557,051</td>
<td align="right">278,523</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">483,339</td>
<td align="right">241,674</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">7,586,115</td>
<td align="right">3,793,249</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">385,047</td>
<td align="right">192,534</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,277,982</td>
<td align="right">1,639,329</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">442,482</td>
<td align="right">221,298</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">893,197</td>
<td align="right">446,733</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">147,501</td>
<td align="right">73,773</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,144,879</td>
<td align="right">6,074,475</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">950,702</td>
<td align="right">475,566</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">991,699</td>
<td align="right">496,083</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,040,791</td>
<td align="right">1,020,885</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,286,960</td>
<td align="right">643,824</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">721,312</td>
<td align="right">360,864</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">204,943</td>
<td align="right">102,543</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">991,930</td>
<td align="right">496,314</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">245,940</td>
<td align="right">123,060</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,648,656</td>
<td align="right">1,825,719</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">147,606</td>
<td align="right">73,878</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">172,242</td>
<td align="right">86,226</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">172,242</td>
<td align="right">86,226</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">295,716</td>
<td align="right">148,113</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">492,972</td>
<td align="right">247,212</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">271,290</td>
<td align="right">136,122</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">189,317</td>
<td align="right">95,046</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">107,176</td>
<td align="right">53,844</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">444,925</td>
<td align="right">223,531</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">338,792</td>
<td align="right">170,268</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,240,506</td>
<td align="right">624,382</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">239,542</td>
<td align="right">120,673</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">82,946</td>
<td align="right">41,985</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">895,024</td>
<td align="right">717,001</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">48</td>
<td align="right">47</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,719</td>
<td align="right">3,719</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,172</td>
<td align="right">2,172</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">945</td>
<td align="right">945</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">819</td>
<td align="right">819</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">336</td>
<td align="right">336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">315</td>
<td align="right">315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">210</td>
<td align="right">210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">168</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">147</td>
<td align="right">147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">105</td>
<td align="right">105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">21</td>
<td align="right">21</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,222,936</td>
<td align="right">94.9%</td>
<td align="right">4,114,646</td>
<td align="right">94.8%</td>
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
<td align="right">442,882</td>
<td align="right">5.1%</td>
<td align="right">221,698</td>
<td align="right">5.1%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">273</td>
<td align="right">0.0%</td>
<td align="right">273</td>
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
<td align="right">1,623</td>
<td align="right">78.6%</td>
<td align="right">1,413</td>
<td align="right">76.2%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">441</td>
<td align="right">21.4%</td>
<td align="right">441</td>
<td align="right">23.8%</td>
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
<td align="left">multiply different types</td>
<td align="right">316</td>
<td align="right">19.5%</td>
<td align="right">274</td>
<td align="right">19.4%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">969</td>
<td align="right">59.7%</td>
<td align="right">843</td>
<td align="right">59.7%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">338</td>
<td align="right">20.8%</td>
<td align="right">296</td>
<td align="right">20.9%</td>
<td align="right">-12.4%</td>
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
<td align="right">962,663</td>
<td align="right">100.0%</td>
<td align="right">440,916</td>
<td align="right">100.0%</td>
<td align="right">-54.2%</td>
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
<td align="right">98,239</td>
<td align="right">0.3%</td>
<td align="right">49,019</td>
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
<td align="right">28,328,196</td>
<td align="right">99.6%</td>
<td align="right">14,167,447</td>
<td align="right">99.6%</td>
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
<td align="right">97,836</td>
<td align="right">0.3%</td>
<td align="right">49,554</td>
<td align="right">0.3%</td>
<td align="right">-49.3%</td>
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
<td align="right">4,122</td>
<td align="right">100.0%</td>
<td align="right">3,184</td>
<td align="right">100.0%</td>
<td align="right">-22.8%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">420</td>
<td align="right">44.4%</td>
<td align="right">420</td>
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
<td align="right">353,507</td>
<td align="right">9.0%</td>
<td align="right">175,562</td>
<td align="right">9.0%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,295,971</td>
<td align="right">84.2%</td>
<td align="right">1,649,216</td>
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
<td align="right">248,760</td>
<td align="right">6.4%</td>
<td align="right">125,436</td>
<td align="right">6.4%</td>
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
<td align="right">15,321</td>
<td align="right">75.3%</td>
<td align="right">7,931</td>
<td align="right">75.2%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,028</td>
<td align="right">24.7%</td>
<td align="right">2,622</td>
<td align="right">24.8%</td>
<td align="right">-47.9%</td>
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
<td align="right">15,321</td>
<td align="right">100.0%</td>
<td align="right">7,931</td>
<td align="right">100.0%</td>
<td align="right">-48.2%</td>
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
<td align="right">2,097,505</td>
<td align="right">60.0%</td>
<td align="right">932,169</td>
<td align="right">57.1%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,393,226</td>
<td align="right">39.9%</td>
<td align="right">696,906</td>
<td align="right">42.7%</td>
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
<td align="right">3,647</td>
<td align="right">95.6%</td>
<td align="right">3,200</td>
<td align="right">95.0%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">168</td>
<td align="right">4.4%</td>
<td align="right">168</td>
<td align="right">5.0%</td>
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
<td align="right">296</td>
<td align="right">8.1%</td>
<td align="right">254</td>
<td align="right">7.9%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">2,930</td>
<td align="right">80.3%</td>
<td align="right">2,568</td>
<td align="right">80.2%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">421</td>
<td align="right">11.5%</td>
<td align="right">378</td>
<td align="right">11.8%</td>
<td align="right">-10.2%</td>
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
<td align="right">5,411,027</td>
<td align="right">74.4%</td>
<td align="right">1,946,214</td>
<td align="right">72.2%</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,854,474</td>
<td align="right">25.5%</td>
<td align="right">747,501</td>
<td align="right">27.7%</td>
<td align="right">-59.7%</td>
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
<td align="right">2,065</td>
<td align="right">90.0%</td>
<td align="right">1,663</td>
<td align="right">87.9%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">229</td>
<td align="right">10.0%</td>
<td align="right">229</td>
<td align="right">12.1%</td>
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
<td align="right">275</td>
<td align="right">13.3%</td>
<td align="right">190</td>
<td align="right">11.4%</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">442</td>
<td align="right">21.4%</td>
<td align="right">357</td>
<td align="right">21.5%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">884</td>
<td align="right">42.8%</td>
<td align="right">715</td>
<td align="right">43.0%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">231</td>
<td align="right">11.2%</td>
<td align="right">189</td>
<td align="right">11.4%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">211</td>
<td align="right">10.2%</td>
<td align="right">190</td>
<td align="right">11.4%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">22</td>
<td align="right">1.1%</td>
<td align="right">22</td>
<td align="right">1.3%</td>
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
<td align="right">139,247</td>
<td align="right">139,247 / 0 !!</td>
<td align="right">69,615</td>
<td align="right">69,615 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">106,483</td>
<td align="right">106,483 / 0 !!</td>
<td align="right">53,235</td>
<td align="right">53,235 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">106,483</td>
<td align="right">106,483 / 0 !!</td>
<td align="right">53,235</td>
<td align="right">53,235 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">434,165</td>
<td align="right">434,165 / 0 !!</td>
<td align="right">217,077</td>
<td align="right">217,077 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">221,199</td>
<td align="right">221,199 / 0 !!</td>
<td align="right">110,607</td>
<td align="right">110,607 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,671,363</td>
<td align="right">1,671,363 / 0 !!</td>
<td align="right">835,779</td>
<td align="right">835,779 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">401,701</td>
<td align="right">401,701 / 0 !!</td>
<td align="right">200,996</td>
<td align="right">200,996 / 0 !!</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,477,902</td>
<td align="right">16.9%</td>
<td align="right">2,755,369</td>
<td align="right">14.5%</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,232,143</td>
<td align="right">3.2%</td>
<td align="right">617,742</td>
<td align="right">3.3%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">30,681,391</td>
<td align="right">79.9%</td>
<td align="right">15,559,248</td>
<td align="right">82.2%</td>
<td align="right">-49.3%</td>
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
<td align="right">124,688</td>
<td align="right">98.2%</td>
<td align="right">54,645</td>
<td align="right">96.4%</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,341</td>
<td align="right">1.8%</td>
<td align="right">2,047</td>
<td align="right">3.6%</td>
<td align="right">-12.6%</td>
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
<td align="right">127</td>
<td align="right">5.4%</td>
<td align="right">106</td>
<td align="right">5.2%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">127</td>
<td align="right">5.4%</td>
<td align="right">106</td>
<td align="right">5.2%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">127</td>
<td align="right">5.4%</td>
<td align="right">106</td>
<td align="right">5.2%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,412</td>
<td align="right">60.3%</td>
<td align="right">1,244</td>
<td align="right">60.8%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">189</td>
<td align="right">8.1%</td>
<td align="right">168</td>
<td align="right">8.2%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">21</td>
<td align="right">1.0%</td>
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
<td align="right">23,202,079</td>
<td align="right">100.0%</td>
<td align="right">11,124,380</td>
<td align="right">100.0%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">567</td>
<td align="right">0.0%</td>
<td align="right">567</td>
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
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,835</td>
<td align="right">0.0%</td>
<td align="right">2,835</td>
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
<td align="right">1,668</td>
<td align="right">100.0%</td>
<td align="right">1,668</td>
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
<td align="right">581,519</td>
<td align="right">100.0%</td>
<td align="right">290,703</td>
<td align="right">99.9%</td>
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
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
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
<td align="right">2,576,134</td>
<td align="right">34.0%</td>
<td align="right">1,286,191</td>
<td align="right">33.9%</td>
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
<td align="right">5,009,981</td>
<td align="right">66.0%</td>
<td align="right">2,507,184</td>
<td align="right">66.1%</td>
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
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">189</td>
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
<td align="right">49,072</td>
<td align="right">100.0%</td>
<td align="right">24,652</td>
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
<td align="right">1,974,241</td>
<td align="right">94.9%</td>
<td align="right">987,105</td>
<td align="right">94.8%</td>
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
<td align="right">106,840</td>
<td align="right">5.1%</td>
<td align="right">53,529</td>
<td align="right">5.1%</td>
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
<td align="left">Failure</td>
<td align="right">231</td>
<td align="right">68.8%</td>
<td align="right">210</td>
<td align="right">66.7%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">105</td>
<td align="right">31.2%</td>
<td align="right">105</td>
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
<td align="left">list slice</td>
<td align="right">231</td>
<td align="right">100.0%</td>
<td align="right">210</td>
<td align="right">100.0%</td>
<td align="right">-9.1%</td>
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
<td align="right">176,569</td>
<td align="right">1.3%</td>
<td align="right">87,612</td>
<td align="right">1.3%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,296,928</td>
<td align="right">97.0%</td>
<td align="right">6,622,865</td>
<td align="right">97.0%</td>
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
<td align="right">238,218</td>
<td align="right">1.7%</td>
<td align="right">119,433</td>
<td align="right">1.7%</td>
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
<td align="right">3,915</td>
<td align="right">84.5%</td>
<td align="right">2,230</td>
<td align="right">77.9%</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">716</td>
<td align="right">15.5%</td>
<td align="right">632</td>
<td align="right">22.1%</td>
<td align="right">-11.7%</td>
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
<td align="right">484</td>
<td align="right">67.6%</td>
<td align="right">421</td>
<td align="right">66.6%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">211</td>
<td align="right">29.5%</td>
<td align="right">190</td>
<td align="right">30.1%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">2.9%</td>
<td align="right">21</td>
<td align="right">3.3%</td>
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
<td align="right">1,148,280</td>
<td align="right">100.0%</td>
<td align="right">574,839</td>
<td align="right">99.9%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">126</td>
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
<td align="right">210</td>
<td align="right">100.0%</td>
<td align="right">210</td>
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
<td align="right">9,581,731</td>
<td align="right">2.4%</td>
<td align="right">4,307,369</td>
<td align="right">2.2%</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">10,410,901</td>
<td align="right">2.6%</td>
<td align="right">4,791,487</td>
<td align="right">2.5%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">141,425,587</td>
<td align="right">35.1%</td>
<td align="right">66,324,740</td>
<td align="right">34.6%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">241,200,052</td>
<td align="right">59.9%</td>
<td align="right">116,520,824</td>
<td align="right">60.7%</td>
<td align="right">-51.7%</td>
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
<td align="right">1,854,474</td>
<td align="right">25.1%</td>
<td align="right">747,501</td>
<td align="right">22.3%</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,097,505</td>
<td align="right">28.4%</td>
<td align="right">932,169</td>
<td align="right">27.7%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">962,663</td>
<td align="right">13.0%</td>
<td align="right">440,916</td>
<td align="right">13.1%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">353,507</td>
<td align="right">4.8%</td>
<td align="right">175,562</td>
<td align="right">5.2%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">442,882</td>
<td align="right">6.0%</td>
<td align="right">221,698</td>
<td align="right">6.6%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">106,840</td>
<td align="right">1.4%</td>
<td align="right">53,529</td>
<td align="right">1.6%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,232,143</td>
<td align="right">16.7%</td>
<td align="right">617,742</td>
<td align="right">18.4%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">238,218</td>
<td align="right">3.2%</td>
<td align="right">119,433</td>
<td align="right">3.6%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">97,836</td>
<td align="right">1.3%</td>
<td align="right">49,554</td>
<td align="right">1.5%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">567</td>
<td align="right">0.0%</td>
<td align="right">567</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,135,717</td>
<td align="right">53.6%</td>
<td align="right">2,083,444</td>
<td align="right">48.4%</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">7,897</td>
<td align="right">0.1%</td>
<td align="right">3,392</td>
<td align="right">0.1%</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">88,194</td>
<td align="right">0.9%</td>
<td align="right">43,558</td>
<td align="right">1.0%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">88,249</td>
<td align="right">0.9%</td>
<td align="right">43,928</td>
<td align="right">1.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,576,134</td>
<td align="right">26.9%</td>
<td align="right">1,286,191</td>
<td align="right">29.9%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,342,185</td>
<td align="right">14.0%</td>
<td align="right">671,925</td>
<td align="right">15.6%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">248,760</td>
<td align="right">2.6%</td>
<td align="right">125,436</td>
<td align="right">2.9%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">90,300</td>
<td align="right">0.9%</td>
<td align="right">45,585</td>
<td align="right">1.1%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,835</td>
<td align="right">0.0%</td>
<td align="right">2,835</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">683</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">336</td>
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
<td align="left">Frame objects created</td>
<td align="right">1,400,997</td>
<td align="right">11.0%</td>
<td align="right">700,581</td>
<td align="right">11.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">11,701,445</td>
<td align="right">92.2%</td>
<td align="right">5,852,352</td>
<td align="right">92.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">12,865,813</td>
<td align="right">101.4%</td>
<td align="right">6,435,087</td>
<td align="right">101.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">992,126</td>
<td align="right">7.8%</td>
<td align="right">496,509</td>
<td align="right">7.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">992,126</td>
<td align="right">7.8%</td>
<td align="right">496,509</td>
<td align="right">7.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">992,126</td>
<td align="right">7.8%</td>
<td align="right">496,509</td>
<td align="right">7.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">992,126</td>
<td align="right">7.8%</td>
<td align="right">496,509</td>
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
<td align="right">882</td>
<td align="right">0.0%</td>
<td align="right">882</td>
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
<td align="left">Allocations over 4 kbytes</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">13,344,644</td>
<td align="right"></td>
<td align="right">6,377,617</td>
<td align="right"></td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">111,135,376</td>
<td align="right">47.5%</td>
<td align="right">53,635,397</td>
<td align="right">45.9%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">84,718,420</td>
<td align="right">38.9%</td>
<td align="right">40,904,062</td>
<td align="right">37.6%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">10,512,921</td>
<td align="right">4.8%</td>
<td align="right">5,103,063</td>
<td align="right">4.7%</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">56,333,107</td>
<td align="right">24.1%</td>
<td align="right">27,891,756</td>
<td align="right">23.9%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">61,402,323</td>
<td align="right">28.2%</td>
<td align="right">30,486,292</td>
<td align="right">28.0%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">17,977,772</td>
<td align="right"></td>
<td align="right">8,948,142</td>
<td align="right"></td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,162,568</td>
<td align="right"></td>
<td align="right">1,579,349</td>
<td align="right"></td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">81,910</td>
<td align="right">12.3%</td>
<td align="right">40,950</td>
<td align="right">12.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">17,661,649</td>
<td align="right"></td>
<td align="right">8,830,713</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">17,661,103</td>
<td align="right">51.8%</td>
<td align="right">8,831,219</td>
<td align="right">51.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">16,332,240</td>
<td align="right">47.9%</td>
<td align="right">8,167,167</td>
<td align="right">47.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,463,574</td>
<td align="right">48.2%</td>
<td align="right">8,233,761</td>
<td align="right">48.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">663,723</td>
<td align="right"></td>
<td align="right">331,947</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,950,497</td>
<td align="right">0.8%</td>
<td align="right">975,685</td>
<td align="right">0.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">131,313</td>
<td align="right">0.4%</td>
<td align="right">66,552</td>
<td align="right">0.4%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">61,092,945</td>
<td align="right">28.1%</td>
<td align="right">32,316,992</td>
<td align="right">29.7%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">64,552,753</td>
<td align="right">27.6%</td>
<td align="right">34,427,486</td>
<td align="right">29.4%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">383,624</td>
<td align="right"></td>
<td align="right">224,723</td>
<td align="right"></td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">365,944</td>
<td align="right"></td>
<td align="right">216,313</td>
<td align="right"></td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">26,106</td>
<td align="right"></td>
<td align="right">15,939</td>
<td align="right"></td>
<td align="right">-38.9%</td>
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
<td align="right">746</td>
<td align="right">1,519,533</td>
<td align="right">19,894,034</td>
<td align="right">106,043</td>
<td align="right">1,523,969</td>
<td align="right">363</td>
<td align="right">735,915</td>
<td align="right">9,658,443</td>
<td align="right">49,458</td>
<td align="right">741,547</td>
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
<td align="right">46</td>
<td align="right">7.6%</td>
<td align="right">1,370</td>
<td align="right">33.5%</td>
<td align="right">2,878.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">604</td>
<td align="right"></td>
<td align="right">4,092</td>
<td align="right"></td>
<td align="right">577.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">152</td>
<td align="right">25.2%</td>
<td align="right">993</td>
<td align="right">24.3%</td>
<td align="right">553.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">42</td>
<td align="right">7.0%</td>
<td align="right">188</td>
<td align="right">4.6%</td>
<td align="right">347.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">406</td>
<td align="right">67.2%</td>
<td align="right">1,729</td>
<td align="right">42.3%</td>
<td align="right">325.9%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">43</td>
<td align="right">7.1%</td>
<td align="right">147</td>
<td align="right">3.6%</td>
<td align="right">241.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">978,932</td>
<td align="right"></td>
<td align="right">2,020,840</td>
<td align="right"></td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">23,719,435</td>
<td align="right">2,423.0%</td>
<td align="right">42,576,339</td>
<td align="right">2,106.9%</td>
<td align="right">79.5%</td>
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
<td align="right">406</td>
<td align="right"></td>
<td align="right">1,729</td>
<td align="right"></td>
<td align="right">325.9%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">279</td>
<td align="right">68.7%</td>
<td align="right">1,180</td>
<td align="right">68.2%</td>
<td align="right">322.9%</td>
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
<td align="right">513,165</td>
<td align="right">16.7%</td>
<td align="right">2,319,248</td>
<td align="right">19.2%</td>
<td align="right">351.9%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">3,063,808</td>
<td align="right"></td>
<td align="right">12,083,200</td>
<td align="right"></td>
<td align="right">294.4%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">67,256</td>
<td align="right">2.2%</td>
<td align="right">261,632</td>
<td align="right">2.2%</td>
<td align="right">289.0%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">2,483,387</td>
<td align="right">81.1%</td>
<td align="right">9,502,320</td>
<td align="right">78.6%</td>
<td align="right">282.6%</td>
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
<td align="left"><= 4,096</td>
<td align="left">44</td>
<td align="right">15.8%</td>
<td align="left">232</td>
<td align="right">19.7%</td>
<td align="right">427.3%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">148</td>
<td align="right">53.0%</td>
<td align="left">484</td>
<td align="right">41.0%</td>
<td align="right">227.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">45</td>
<td align="right">16.1%</td>
<td align="left">380</td>
<td align="right">32.2%</td>
<td align="right">744.4%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">42</td>
<td align="right">15.1%</td>
<td align="left">84</td>
<td align="right">7.1%</td>
<td align="right">100.0%</td>
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
<td align="left"><= 8</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">64</td>
<td align="right">3.7%</td>
<td align="right">6,300.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">3.6%</td>
<td align="right">63 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">64</td>
<td align="right">15.8%</td>
<td align="right">168</td>
<td align="right">9.7%</td>
<td align="right">162.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">129</td>
<td align="right">31.8%</td>
<td align="right">548</td>
<td align="right">31.7%</td>
<td align="right">324.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">190</td>
<td align="right">46.8%</td>
<td align="right">739</td>
<td align="right">42.7%</td>
<td align="right">288.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">22</td>
<td align="right">5.4%</td>
<td align="right">147</td>
<td align="right">8.5%</td>
<td align="right">568.2%</td>
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
<td align="left"><= 8</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">84</td>
<td align="right">4.9%</td>
<td align="right">8,300.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">22</td>
<td align="right">5.4%</td>
<td align="right">84</td>
<td align="right">4.9%</td>
<td align="right">281.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">169</td>
<td align="right">41.6%</td>
<td align="right">441</td>
<td align="right">25.5%</td>
<td align="right">160.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">3</td>
<td align="right">0.7%</td>
<td align="right">317</td>
<td align="right">18.3%</td>
<td align="right">10,466.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">84</td>
<td align="right">20.7%</td>
<td align="right">232</td>
<td align="right">13.4%</td>
<td align="right">176.2%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">22</td>
<td align="right">1.3%</td>
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
<td align="left">_GET_ITER</td>
<td align="right">5</td>
<td align="right">89,380</td>
<td align="right">1,787,500.0%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">581</td>
<td align="right">212,881</td>
<td align="right">36,540.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">762</td>
<td align="right">177,538</td>
<td align="right">23,199.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">762</td>
<td align="right">177,538</td>
<td align="right">23,199.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">1,998</td>
<td align="right">99,876</td>
<td align="right">4,898.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">812</td>
<td align="right">37,527</td>
<td align="right">4,521.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">1,998</td>
<td align="right">90,636</td>
<td align="right">4,436.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,186</td>
<td align="right">51,072</td>
<td align="right">4,206.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">812</td>
<td align="right">30,786</td>
<td align="right">3,691.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">7,189</td>
<td align="right">176,630</td>
<td align="right">2,356.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">3,571</td>
<td align="right">47,670</td>
<td align="right">1,234.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">3,571</td>
<td align="right">47,628</td>
<td align="right">1,233.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">57,354</td>
<td align="right">698,382</td>
<td align="right">1,117.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">57,354</td>
<td align="right">698,382</td>
<td align="right">1,117.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">70,727</td>
<td align="right">488,271</td>
<td align="right">590.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">97,022</td>
<td align="right">576,259</td>
<td align="right">493.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">17,921</td>
<td align="right">86,062</td>
<td align="right">380.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">132,221</td>
<td align="right">591,543</td>
<td align="right">347.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">70,727</td>
<td align="right">292,551</td>
<td align="right">313.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">54,484</td>
<td align="right">207,794</td>
<td align="right">281.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">18,595</td>
<td align="right">70,917</td>
<td align="right">281.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">18,595</td>
<td align="right">70,854</td>
<td align="right">281.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">18,595</td>
<td align="right">70,854</td>
<td align="right">281.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">7,189</td>
<td align="right">27,237</td>
<td align="right">278.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">29,435</td>
<td align="right">99,498</td>
<td align="right">238.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">29,435</td>
<td align="right">99,498</td>
<td align="right">238.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">115,066</td>
<td align="right">324,513</td>
<td align="right">182.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">96,648</td>
<td align="right">263,554</td>
<td align="right">172.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">590,320</td>
<td align="right">1,559,529</td>
<td align="right">164.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">21,539</td>
<td align="right">54,558</td>
<td align="right">153.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">21,539</td>
<td align="right">54,558</td>
<td align="right">153.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">134,265</td>
<td align="right">337,827</td>
<td align="right">151.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">64,724</td>
<td align="right">139,146</td>
<td align="right">115.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">64,724</td>
<td align="right">139,146</td>
<td align="right">115.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">64,724</td>
<td align="right">139,146</td>
<td align="right">115.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">64,724</td>
<td align="right">139,146</td>
<td align="right">115.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">978,932</td>
<td align="right">2,020,840</td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">978,932</td>
<td align="right">2,020,840</td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">1,215,615</td>
<td align="right">2,363,665</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">106,581</td>
<td align="right">204,225</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">28,700</td>
<td align="right">54,831</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">14,350</td>
<td align="right">27,405</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">28,700</td>
<td align="right">54,684</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">14,350</td>
<td align="right">27,342</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">14,350</td>
<td align="right">27,342</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">14,350</td>
<td align="right">27,342</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">400,922</td>
<td align="right">744,395</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">4,663,839</td>
<td align="right">8,095,785</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">3,783,928</td>
<td align="right">6,486,593</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">183,663</td>
<td align="right">309,666</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">160,813</td>
<td align="right">260,169</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">100,723</td>
<td align="right">151,851</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">284,931</td>
<td align="right">423,738</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">236,683</td>
<td align="right">342,825</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">351,258</td>
<td align="right">496,674</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">1,360,169</td>
<td align="right">1,908,041</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">708,075</td>
<td align="right">988,309</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">708,075</td>
<td align="right">988,288</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">477,143</td>
<td align="right">655,607</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">77,881</td>
<td align="right">52,395</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">233,643</td>
<td align="right">157,395</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">233,643</td>
<td align="right">157,395</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">77,881</td>
<td align="right">52,542</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">110,186</td>
<td align="right">137,718</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">127,076</td>
<td align="right">103,908</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">63,538</td>
<td align="right">51,954</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">63,538</td>
<td align="right">51,954</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">63,538</td>
<td align="right">51,954</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">63,538</td>
<td align="right">52,017</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">63,538</td>
<td align="right">52,017</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">92,259</td>
<td align="right">106,617</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">251,599</td>
<td align="right">286,738</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">127,076</td>
<td align="right">110,880</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">127,076</td>
<td align="right">110,880</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">127,076</td>
<td align="right">110,880</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">127,076</td>
<td align="right">110,880</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">424,278</td>
<td align="right">475,986</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">234,829</td>
<td align="right">208,257</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">234,829</td>
<td align="right">208,257</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">234,829</td>
<td align="right">208,257</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">534,303</td>
<td align="right">593,901</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">387,748</td>
<td align="right">346,206</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">18,590</td>
<td align="right">20,076</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">18,590</td>
<td align="right">20,034</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">18,590</td>
<td align="right">20,034</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">18,590</td>
<td align="right">20,034</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">18,590</td>
<td align="right">20,034</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">63,538</td>
<td align="right">58,863</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">63,538</td>
<td align="right">58,863</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">96,471</td>
<td align="right">90,804</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">254,152</td>
<td align="right">243,936</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">77,888</td>
<td align="right">79,359</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">155,776</td>
<td align="right">158,655</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">77,888</td>
<td align="right">79,296</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right"></td>
<td align="right">219,891</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">202,566</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right"></td>
<td align="right">86,099</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right">36,225</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right"></td>
<td align="right">30,177</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right"></td>
<td align="right">27,573</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right"></td>
<td align="right">27,510</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right"></td>
<td align="right">24,906</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right"></td>
<td align="right">18,207</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">18,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right"></td>
<td align="right">18,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right"></td>
<td align="right">18,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">8,946</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right"></td>
<td align="right">6,909</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right"></td>
<td align="right">6,909</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right"></td>
<td align="right">6,846</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right"></td>
<td align="right">210</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right"></td>
<td align="right">147</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">147</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">126</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">63</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">63</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right"></td>
<td align="right">63</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right"></td>
<td align="right">63</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">63</td>
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
<td align="right"></td>
<td align="right">42</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right"></td>
<td align="right">21</td>
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
Stats gathered on: 2025-07-02
