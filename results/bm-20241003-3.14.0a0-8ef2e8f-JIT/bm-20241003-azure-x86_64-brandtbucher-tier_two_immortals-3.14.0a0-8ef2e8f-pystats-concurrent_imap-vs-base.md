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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">1,212,805</td>
<td align="right">946,944</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,454,531</td>
<td align="right">1,923,195</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,464,219</td>
<td align="right">1,932,537</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">8,216,900</td>
<td align="right">6,444,645</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">822,782</td>
<td align="right">645,528</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,296,910</td>
<td align="right">2,588,014</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,241,926</td>
<td align="right">976,099</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,493,050</td>
<td align="right">1,961,183</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">10,808,276</td>
<td align="right">8,503,788</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,669,125</td>
<td align="right">1,314,677</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">3,342,770</td>
<td align="right">2,633,874</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,694,233</td>
<td align="right">1,339,802</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,391,370</td>
<td align="right">2,682,474</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,545,431</td>
<td align="right">2,013,391</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">849,894</td>
<td align="right">672,660</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">851,354</td>
<td align="right">674,120</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,277,771</td>
<td align="right">1,011,970</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,279,011</td>
<td align="right">1,013,088</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,557,759</td>
<td align="right">2,026,097</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,567,026</td>
<td align="right">2,035,359</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,151,430</td>
<td align="right">1,708,691</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,594,979</td>
<td align="right">2,063,308</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,606,682</td>
<td align="right">2,075,015</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">434,758</td>
<td align="right">346,159</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,760,425</td>
<td align="right">1,405,977</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">446,911</td>
<td align="right">358,284</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17,461,640</td>
<td align="right">14,005,504</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">4,952,735</td>
<td align="right">3,978,011</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,397,627</td>
<td align="right">9,181,735</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">24,906,559</td>
<td align="right">20,121,704</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,699,839</td>
<td align="right">7,839,717</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">16,248,532</td>
<td align="right">13,147,702</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">464,398</td>
<td align="right">375,799</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">19,971,911</td>
<td align="right">16,162,745</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">8,971,611</td>
<td align="right">7,288,127</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">13,379,194</td>
<td align="right">10,898,424</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,829,466</td>
<td align="right">3,120,972</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">4,326,331</td>
<td align="right">3,528,929</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">13,004,810</td>
<td align="right">10,613,011</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">486,093</td>
<td align="right">397,469</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,918,039</td>
<td align="right">2,386,532</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">9,002,013</td>
<td align="right">7,407,184</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,028,286</td>
<td align="right">4,142,652</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">9,603,831</td>
<td align="right">7,920,369</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">111,224,121</td>
<td align="right">91,910,132</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,915,076</td>
<td align="right">4,941,088</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">22,952,898</td>
<td align="right">19,230,509</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">31,704,594</td>
<td align="right">26,742,454</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">20,408,897</td>
<td align="right">17,220,834</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">36,476,233</td>
<td align="right">30,805,097</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,033,884</td>
<td align="right">3,413,588</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,758,732</td>
<td align="right">1,492,899</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">4,789,064</td>
<td align="right">4,080,224</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">6,784,932</td>
<td align="right">5,810,188</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,578,824</td>
<td align="right">4,781,623</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">16,963,086</td>
<td align="right">14,571,212</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,966,930</td>
<td align="right">1,701,149</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">29,799,261</td>
<td align="right">25,901,115</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,103,078</td>
<td align="right">9,685,470</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,431,887</td>
<td align="right">1,254,699</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">13,541,180</td>
<td align="right">12,034,736</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">854,345</td>
<td align="right">765,854</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">14,029,294</td>
<td align="right">12,608,856</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,678,321</td>
<td align="right">4,235,488</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,007,077</td>
<td align="right">918,499</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,090,237</td>
<td align="right">2,001,659</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">220</td>
<td align="right">218</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">124,531</td>
<td align="right">124,891</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">144,776</td>
<td align="right">144,936</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">250,382</td>
<td align="right">250,627</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">71,247</td>
<td align="right">71,198</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">64,469</td>
<td align="right">64,509</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">136,342</td>
<td align="right">136,418</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">80,489</td>
<td align="right">80,529</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">8,084</td>
<td align="right">8,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">18,930</td>
<td align="right">18,923</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">25,479</td>
<td align="right">25,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,206</td>
<td align="right">35,194</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">29,462</td>
<td align="right">29,472</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">548,136</td>
<td align="right">548,309</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">25,652</td>
<td align="right">25,644</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">218,698</td>
<td align="right">218,763</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">40,560</td>
<td align="right">40,572</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">24,210</td>
<td align="right">24,203</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">24,210</td>
<td align="right">24,203</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">47,005</td>
<td align="right">47,016</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">393,173</td>
<td align="right">393,239</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">37,506</td>
<td align="right">37,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,180</td>
<td align="right">17,178</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,123,687</td>
<td align="right">1,123,807</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">55,448</td>
<td align="right">55,444</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,460</td>
<td align="right">44,458</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">51,720</td>
<td align="right">51,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">625,605</td>
<td align="right">625,615</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,268,287</td>
<td align="right">2,268,315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">197,504</td>
<td align="right">197,502</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,337,380</td>
<td align="right">6,337,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">132,060</td>
<td align="right">132,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">131,360</td>
<td align="right">131,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">108,980</td>
<td align="right">108,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">97,960</td>
<td align="right">97,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">88,480</td>
<td align="right">88,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">84,980</td>
<td align="right">84,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">79,200</td>
<td align="right">79,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">71,620</td>
<td align="right">71,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">71,580</td>
<td align="right">71,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">65,800</td>
<td align="right">65,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">62,080</td>
<td align="right">62,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">59,680</td>
<td align="right">59,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">50,860</td>
<td align="right">50,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">49,000</td>
<td align="right">49,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">45,700</td>
<td align="right">45,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">38,900</td>
<td align="right">38,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">38,400</td>
<td align="right">38,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">37,480</td>
<td align="right">37,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">34,740</td>
<td align="right">34,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,400</td>
<td align="right">33,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">28,000</td>
<td align="right">28,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">26,100</td>
<td align="right">26,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">22,400</td>
<td align="right">22,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">19,280</td>
<td align="right">19,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">18,640</td>
<td align="right">18,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,160</td>
<td align="right">17,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">16,980</td>
<td align="right">16,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">15,900</td>
<td align="right">15,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">11,780</td>
<td align="right">11,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">11,780</td>
<td align="right">11,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">11,680</td>
<td align="right">11,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">11,540</td>
<td align="right">11,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">10,560</td>
<td align="right">10,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">8,320</td>
<td align="right">8,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">6,580</td>
<td align="right">6,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,400</td>
<td align="right">5,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,280</td>
<td align="right">5,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,860</td>
<td align="right">4,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">3,600</td>
<td align="right">3,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,380</td>
<td align="right">2,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,540</td>
<td align="right">1,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,220</td>
<td align="right">1,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,040</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">460</td>
<td align="right">460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">340</td>
<td align="right">340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">20</td>
<td align="right">20</td>
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
<td align="right">10,800,551</td>
<td align="right">80.7%</td>
<td align="right">8,496,630</td>
<td align="right">78.6%</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,573,806</td>
<td align="right">19.2%</td>
<td align="right">2,308,030</td>
<td align="right">21.3%</td>
<td align="right">-10.3%</td>
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
<td align="right">7,065</td>
<td align="right">91.5%</td>
<td align="right">6,498</td>
<td align="right">90.8%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">660</td>
<td align="right">8.5%</td>
<td align="right">660</td>
<td align="right">9.2%</td>
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
<td align="left">or</td>
<td align="right">1,998</td>
<td align="right">28.3%</td>
<td align="right">1,783</td>
<td align="right">27.4%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,555</td>
<td align="right">50.3%</td>
<td align="right">3,207</td>
<td align="right">49.4%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">672</td>
<td align="right">9.5%</td>
<td align="right">668</td>
<td align="right">10.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">640</td>
<td align="right">9.1%</td>
<td align="right">640</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">200</td>
<td align="right">2.8%</td>
<td align="right">200</td>
<td align="right">3.1%</td>
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
<td align="right">19,280</td>
<td align="right">100.0%</td>
<td align="right">19,280</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">1,091,702</td>
<td align="right">95.2%</td>
<td align="right">914,448</td>
<td align="right">94.3%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">54,564</td>
<td align="right">4.8%</td>
<td align="right">54,560</td>
<td align="right">5.6%</td>
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
<td align="right">300</td>
<td align="right">33.9%</td>
<td align="right">300</td>
<td align="right">33.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">584</td>
<td align="right">66.1%</td>
<td align="right">584</td>
<td align="right">66.1%</td>
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
<td align="left">buffer int</td>
<td align="right">584</td>
<td align="right">100.0%</td>
<td align="right">584</td>
<td align="right">100.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">45,909,744</td>
<td align="right">99.9%</td>
<td align="right">37,757,960</td>
<td align="right">99.9%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19,298</td>
<td align="right">0.0%</td>
<td align="right">19,298</td>
<td align="right">0.1%</td>
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
<td align="right">4,840</td>
<td align="right">0.0%</td>
<td align="right">4,840</td>
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
<td align="right">16,788</td>
<td align="right">100.0%</td>
<td align="right">16,776</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">820</td>
<td align="right">53.2%</td>
<td align="right">820</td>
<td align="right">53.2%</td>
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
<td align="right">1,275,843</td>
<td align="right">14.4%</td>
<td align="right">1,009,989</td>
<td align="right">13.4%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,568,195</td>
<td align="right">85.5%</td>
<td align="right">6,505,063</td>
<td align="right">86.5%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,400</td>
<td align="right">0.1%</td>
<td align="right">6,400</td>
<td align="right">0.1%</td>
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
<td align="right">1,414</td>
<td align="right">43.3%</td>
<td align="right">1,345</td>
<td align="right">42.0%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,854</td>
<td align="right">56.7%</td>
<td align="right">1,854</td>
<td align="right">58.0%</td>
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
<td align="left">float long</td>
<td align="right">922</td>
<td align="right">65.2%</td>
<td align="right">857</td>
<td align="right">63.7%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">172</td>
<td align="right">12.2%</td>
<td align="right">168</td>
<td align="right">12.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">320</td>
<td align="right">22.6%</td>
<td align="right">320</td>
<td align="right">23.8%</td>
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
<td align="right">3,373,984</td>
<td align="right">100.0%</td>
<td align="right">2,753,676</td>
<td align="right">100.0%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">180</td>
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
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">140</td>
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
<td align="right">8,432,128</td>
<td align="right">99.6%</td>
<td align="right">7,900,471</td>
<td align="right">99.6%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">31,640</td>
<td align="right">0.4%</td>
<td align="right">31,640</td>
<td align="right">0.4%</td>
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
<td align="right">720</td>
<td align="right">40.9%</td>
<td align="right">720</td>
<td align="right">40.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,040</td>
<td align="right">59.1%</td>
<td align="right">1,040</td>
<td align="right">59.1%</td>
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
<td align="left">itertools</td>
<td align="right">260</td>
<td align="right">25.0%</td>
<td align="right">260</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">140</td>
<td align="right">13.5%</td>
<td align="right">140</td>
<td align="right">13.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">40</td>
<td align="right">3.8%</td>
<td align="right">40</td>
<td align="right">3.8%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11,362,866</td>
<td align="right">13.0%</td>
<td align="right">9,147,550</td>
<td align="right">12.6%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">75,319,032</td>
<td align="right">86.4%</td>
<td align="right">63,002,845</td>
<td align="right">86.8%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">435,976</td>
<td align="right">0.5%</td>
<td align="right">436,332</td>
<td align="right">0.6%</td>
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
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
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
<td align="right">14,853</td>
<td align="right">35.0%</td>
<td align="right">14,305</td>
<td align="right">34.1%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">27,637</td>
<td align="right">65.0%</td>
<td align="right">27,613</td>
<td align="right">65.9%</td>
<td align="right">-0.1%</td>
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
<td align="right">4,358</td>
<td align="right">29.3%</td>
<td align="right">3,944</td>
<td align="right">27.6%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">2,294</td>
<td align="right">15.4%</td>
<td align="right">2,246</td>
<td align="right">15.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,840</td>
<td align="right">25.9%</td>
<td align="right">3,840</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,360</td>
<td align="right">9.2%</td>
<td align="right">1,360</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">580</td>
<td align="right">3.9%</td>
<td align="right">580</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">240</td>
<td align="right">1.6%</td>
<td align="right">240</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">120</td>
<td align="right">0.8%</td>
<td align="right">120</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">80</td>
<td align="right">0.5%</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">60</td>
<td align="right">0.4%</td>
<td align="right">60</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">34,481,510</td>
<td align="right">99.8%</td>
<td align="right">28,013,193</td>
<td align="right">99.8%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,624</td>
<td align="right">0.0%</td>
<td align="right">13,619</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">800</td>
<td align="right">0.0%</td>
<td align="right">800</td>
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
<td align="right">28,880</td>
<td align="right">0.1%</td>
<td align="right">28,880</td>
<td align="right">0.1%</td>
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
<td align="right">12,088</td>
<td align="right">100.0%</td>
<td align="right">12,085</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">4,537,149</td>
<td align="right">100.0%</td>
<td align="right">3,562,393</td>
<td align="right">100.0%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">260</td>
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
<td align="right">300</td>
<td align="right">100.0%</td>
<td align="right">300</td>
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
<td align="right">9,782,985</td>
<td align="right">97.4%</td>
<td align="right">8,010,745</td>
<td align="right">96.8%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">82,300</td>
<td align="right">0.8%</td>
<td align="right">82,300</td>
<td align="right">1.0%</td>
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
<td align="right">172,120</td>
<td align="right">1.7%</td>
<td align="right">172,120</td>
<td align="right">2.1%</td>
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
<td align="right">7,500</td>
<td align="right">81.0%</td>
<td align="right">7,500</td>
<td align="right">81.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,760</td>
<td align="right">19.0%</td>
<td align="right">1,760</td>
<td align="right">19.0%</td>
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
<td align="left">property</td>
<td align="right">980</td>
<td align="right">55.7%</td>
<td align="right">980</td>
<td align="right">55.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">480</td>
<td align="right">27.3%</td>
<td align="right">480</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">200</td>
<td align="right">11.4%</td>
<td align="right">200</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">100</td>
<td align="right">5.7%</td>
<td align="right">100</td>
<td align="right">5.7%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,447,504</td>
<td align="right">99.2%</td>
<td align="right">2,826,844</td>
<td align="right">99.0%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,120</td>
<td align="right">0.8%</td>
<td align="right">27,120</td>
<td align="right">0.9%</td>
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
<td align="right">300</td>
<td align="right">34.1%</td>
<td align="right">300</td>
<td align="right">34.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">580</td>
<td align="right">65.9%</td>
<td align="right">580</td>
<td align="right">65.9%</td>
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
<td align="left">py simple</td>
<td align="right">400</td>
<td align="right">69.0%</td>
<td align="right">400</td>
<td align="right">69.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">31.0%</td>
<td align="right">180</td>
<td align="right">31.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">24,166,717</td>
<td align="right">99.5%</td>
<td align="right">19,293,611</td>
<td align="right">99.4%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">119,359</td>
<td align="right">0.5%</td>
<td align="right">119,721</td>
<td align="right">0.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">880</td>
<td align="right">0.0%</td>
<td align="right">880</td>
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
<td align="right">3,060</td>
<td align="right">59.2%</td>
<td align="right">3,058</td>
<td align="right">59.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,112</td>
<td align="right">40.8%</td>
<td align="right">2,112</td>
<td align="right">40.9%</td>
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
<td align="left">mapping</td>
<td align="right">740</td>
<td align="right">35.0%</td>
<td align="right">740</td>
<td align="right">35.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">400</td>
<td align="right">18.9%</td>
<td align="right">400</td>
<td align="right">18.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">380</td>
<td align="right">18.0%</td>
<td align="right">380</td>
<td align="right">18.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">332</td>
<td align="right">15.7%</td>
<td align="right">332</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">8.5%</td>
<td align="right">180</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">80</td>
<td align="right">3.8%</td>
<td align="right">80</td>
<td align="right">3.8%</td>
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
<td align="right">3,003,009</td>
<td align="right">100.0%</td>
<td align="right">2,825,875</td>
<td align="right">100.0%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">680</td>
<td align="right">0.0%</td>
<td align="right">680</td>
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
<td align="right">540</td>
<td align="right">100.0%</td>
<td align="right">540</td>
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
<td align="right">23,898,551</td>
<td align="right">4.0%</td>
<td align="right">19,112,584</td>
<td align="right">3.8%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">203,203,695</td>
<td align="right">33.6%</td>
<td align="right">167,588,243</td>
<td align="right">33.2%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">376,749,418</td>
<td align="right">62.3%</td>
<td align="right">317,295,442</td>
<td align="right">62.9%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">649,188</td>
<td align="right">0.1%</td>
<td align="right">649,542</td>
<td align="right">0.1%</td>
<td align="right">0.1%</td>
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
<td align="right">10,800,551</td>
<td align="right">45.4%</td>
<td align="right">8,496,630</td>
<td align="right">44.7%</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,275,843</td>
<td align="right">5.4%</td>
<td align="right">1,009,989</td>
<td align="right">5.3%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,362,866</td>
<td align="right">47.7%</td>
<td align="right">9,147,550</td>
<td align="right">48.1%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">119,359</td>
<td align="right">0.5%</td>
<td align="right">119,721</td>
<td align="right">0.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">54,564</td>
<td align="right">0.2%</td>
<td align="right">54,560</td>
<td align="right">0.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">82,300</td>
<td align="right">0.3%</td>
<td align="right">82,300</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">31,640</td>
<td align="right">0.1%</td>
<td align="right">31,640</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">27,120</td>
<td align="right">0.1%</td>
<td align="right">27,120</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">19,298</td>
<td align="right">0.1%</td>
<td align="right">19,298</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">19,280</td>
<td align="right">0.1%</td>
<td align="right">19,280</td>
<td align="right">0.1%</td>
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
<td align="right">356,041</td>
<td align="right">54.8%</td>
<td align="right">356,385</td>
<td align="right">54.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">62,215</td>
<td align="right">9.6%</td>
<td align="right">62,227</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">172,120</td>
<td align="right">26.5%</td>
<td align="right">172,120</td>
<td align="right">26.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,180</td>
<td align="right">2.8%</td>
<td align="right">18,180</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,380</td>
<td align="right">1.9%</td>
<td align="right">12,380</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,700</td>
<td align="right">1.6%</td>
<td align="right">10,700</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,340</td>
<td align="right">1.0%</td>
<td align="right">6,340</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,100</td>
<td align="right">0.8%</td>
<td align="right">5,100</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,380</td>
<td align="right">0.2%</td>
<td align="right">1,380</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,060</td>
<td align="right">0.2%</td>
<td align="right">1,060</td>
<td align="right">0.2%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">986,126</td>
<td align="right">1.7%</td>
<td align="right">808,886</td>
<td align="right">1.7%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">50,579,143</td>
<td align="right">89.0%</td>
<td align="right">42,073,204</td>
<td align="right">87.0%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">43,315,523</td>
<td align="right">76.2%</td>
<td align="right">36,316,028</td>
<td align="right">75.1%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">13,009,080</td>
<td align="right">22.9%</td>
<td align="right">11,502,636</td>
<td align="right">23.8%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">13,010,520</td>
<td align="right">22.9%</td>
<td align="right">11,504,076</td>
<td align="right">23.8%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">13,546,520</td>
<td align="right">23.8%</td>
<td align="right">12,040,076</td>
<td align="right">24.9%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">13,546,520</td>
<td align="right">23.8%</td>
<td align="right">12,040,076</td>
<td align="right">24.9%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">24,570</td>
<td align="right">0.0%</td>
<td align="right">24,563</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">536,000</td>
<td align="right">0.9%</td>
<td align="right">536,000</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">980</td>
<td align="right">0.0%</td>
<td align="right">980</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">571,260</td>
<td align="right">1.0%</td>
<td align="right">571,260</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">544,820</td>
<td align="right">1.0%</td>
<td align="right">544,820</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">98,313</td>
<td align="right"></td>
<td align="right">19,602</td>
<td align="right"></td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">220,803</td>
<td align="right"></td>
<td align="right">63,888</td>
<td align="right"></td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">128,025</td>
<td align="right"></td>
<td align="right">49,797</td>
<td align="right"></td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,473,170</td>
<td align="right"></td>
<td align="right">2,764,274</td>
<td align="right"></td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">20,127,437</td>
<td align="right"></td>
<td align="right">16,217,708</td>
<td align="right"></td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">138,561,768</td>
<td align="right">15.6%</td>
<td align="right">113,131,932</td>
<td align="right">15.2%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">132,188,744</td>
<td align="right">17.1%</td>
<td align="right">108,708,793</td>
<td align="right">16.8%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">129,423,994</td>
<td align="right">16.8%</td>
<td align="right">106,838,944</td>
<td align="right">16.5%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">36,092,823</td>
<td align="right">52.9%</td>
<td align="right">29,978,671</td>
<td align="right">51.9%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">36,103,680</td>
<td align="right"></td>
<td align="right">29,989,535</td>
<td align="right"></td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">179,935,125</td>
<td align="right">20.2%</td>
<td align="right">149,588,640</td>
<td align="right">20.1%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">333,486,699</td>
<td align="right">37.5%</td>
<td align="right">278,551,110</td>
<td align="right">37.3%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">246,010,066</td>
<td align="right">31.9%</td>
<td align="right">206,404,811</td>
<td align="right">31.9%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">21,749,703</td>
<td align="right"></td>
<td align="right">18,461,161</td>
<td align="right"></td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">264,416,447</td>
<td align="right">34.2%</td>
<td align="right">224,828,399</td>
<td align="right">34.8%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">34,997,837</td>
<td align="right"></td>
<td align="right">30,036,088</td>
<td align="right"></td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">238,361,765</td>
<td align="right">26.8%</td>
<td align="right">204,800,160</td>
<td align="right">27.5%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">31,932,214</td>
<td align="right">46.8%</td>
<td align="right">27,590,950</td>
<td align="right">47.8%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">32,092,746</td>
<td align="right">47.1%</td>
<td align="right">27,751,406</td>
<td align="right">48.1%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">88,171</td>
<td align="right">0.1%</td>
<td align="right">88,087</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">72,361</td>
<td align="right">0.1%</td>
<td align="right">72,369</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">1,600</td>
<td align="right">0.0%</td>
<td align="right">1,600</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">783,549,743</td>
<td align="right">2,298.5%</td>
<td align="right">668,442,433</td>
<td align="right">2,150.9%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">34,088,937</td>
<td align="right"></td>
<td align="right">31,077,591</td>
<td align="right"></td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">608</td>
<td align="right">7.0%</td>
<td align="right">567</td>
<td align="right">6.9%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,185</td>
<td align="right">71.1%</td>
<td align="right">5,779</td>
<td align="right">70.7%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">5,886</td>
<td align="right">67.7%</td>
<td align="right">5,514</td>
<td align="right">67.5%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">8,698</td>
<td align="right"></td>
<td align="right">8,174</td>
<td align="right"></td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,204</td>
<td align="right">25.3%</td>
<td align="right">2,093</td>
<td align="right">25.6%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">41</td>
<td align="right">0.5%</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">2.4%</td>
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
<td align="right">320</td>
<td align="right">14.5%</td>
<td align="right">320</td>
<td align="right">15.3%</td>
<td align="right">0.0%</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">2,084</td>
<td align="right">94.6%</td>
<td align="right">1,973</td>
<td align="right">94.3%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,204</td>
<td align="right"></td>
<td align="right">2,093</td>
<td align="right"></td>
<td align="right">-5.0%</td>
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
<td align="right">120</td>
<td align="right">5.4%</td>
<td align="right">120</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
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
<td align="right">419</td>
<td align="right">19.0%</td>
<td align="right">397</td>
<td align="right">19.0%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">230</td>
<td align="right">10.4%</td>
<td align="right">208</td>
<td align="right">9.9%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">391</td>
<td align="right">17.7%</td>
<td align="right">367</td>
<td align="right">17.5%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">640</td>
<td align="right">29.0%</td>
<td align="right">602</td>
<td align="right">28.8%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">322</td>
<td align="right">14.6%</td>
<td align="right">322</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">182</td>
<td align="right">8.3%</td>
<td align="right">177</td>
<td align="right">8.5%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">0.9%</td>
<td align="right">20</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
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
<td align="right">166</td>
<td align="right">7.5%</td>
<td align="right">160</td>
<td align="right">7.6%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">426</td>
<td align="right">19.3%</td>
<td align="right">394</td>
<td align="right">18.8%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">57</td>
<td align="right">2.6%</td>
<td align="right">51</td>
<td align="right">2.4%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">667</td>
<td align="right">30.3%</td>
<td align="right">621</td>
<td align="right">29.7%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">425</td>
<td align="right">19.3%</td>
<td align="right">408</td>
<td align="right">19.5%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">282</td>
<td align="right">12.8%</td>
<td align="right">279</td>
<td align="right">13.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">61</td>
<td align="right">2.8%</td>
<td align="right">60</td>
<td align="right">2.9%</td>
<td align="right">-1.6%</td>
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
<td align="left">_LOAD_FAST_1</td>
<td align="right">20,971,458</td>
<td align="right">15,915,545</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">16,858,281</td>
<td align="right">12,906,155</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">399,380</td>
<td align="right">310,781</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">399,561</td>
<td align="right">310,965</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,199,685</td>
<td align="right">933,874</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,600,642</td>
<td align="right">1,246,194</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">2,000,911</td>
<td align="right">1,557,860</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">4,004,216</td>
<td align="right">3,118,065</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,201,839</td>
<td align="right">935,979</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,201,959</td>
<td align="right">936,099</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,201,959</td>
<td align="right">936,099</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,202,039</td>
<td align="right">936,179</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">6,413,084</td>
<td align="right">4,995,287</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,202,559</td>
<td align="right">936,699</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">4,410,177</td>
<td align="right">3,435,382</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,610,179</td>
<td align="right">1,255,692</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">4,029,327</td>
<td align="right">3,143,164</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">405,111</td>
<td align="right">316,486</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,216,135</td>
<td align="right">950,263</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">4,464,475</td>
<td align="right">3,489,645</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">4,064,865</td>
<td align="right">3,178,703</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">815,642</td>
<td align="right">638,390</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">3,316,706</td>
<td align="right">2,607,678</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">829,772</td>
<td align="right">652,550</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">830,302</td>
<td align="right">653,050</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,250,933</td>
<td align="right">985,054</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,250,933</td>
<td align="right">985,054</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">425,009</td>
<td align="right">336,385</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">9,433,423</td>
<td align="right">7,483,844</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">9,433,423</td>
<td align="right">7,483,844</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,233,738</td>
<td align="right">6,549,970</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">441,226</td>
<td align="right">352,629</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">11,177,574</td>
<td align="right">8,962,102</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">10,734,530</td>
<td align="right">8,607,690</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">4,944,019</td>
<td align="right">3,969,218</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">1,803,435</td>
<td align="right">1,449,068</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5,864,159</td>
<td align="right">4,712,159</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">4,512,403</td>
<td align="right">3,626,246</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,552,162</td>
<td align="right">3,665,981</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">14,163,502</td>
<td align="right">11,416,309</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">12,943,047</td>
<td align="right">10,461,726</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">12,946,387</td>
<td align="right">10,465,066</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">4,170,423</td>
<td align="right">3,372,863</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,210,063</td>
<td align="right">3,412,503</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">49,161,929</td>
<td align="right">40,062,967</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">6,861,772</td>
<td align="right">5,620,741</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">22,782,339</td>
<td align="right">18,705,340</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,513,659</td>
<td align="right">2,070,418</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,531,550</td>
<td align="right">2,088,480</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">7,688,568</td>
<td align="right">6,359,423</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">4,638,442</td>
<td align="right">3,840,926</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,579,094</td>
<td align="right">2,135,936</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">66,948,694</td>
<td align="right">55,457,020</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">4,652,803</td>
<td align="right">3,855,287</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,802,371</td>
<td align="right">5,650,429</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">2,137,588</td>
<td align="right">1,783,098</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">14,425,695</td>
<td align="right">12,071,611</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">27,870,071</td>
<td align="right">23,349,131</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,207,877</td>
<td align="right">1,853,396</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,244,120</td>
<td align="right">1,889,666</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,810,523</td>
<td align="right">1,544,707</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,104,562</td>
<td align="right">2,661,553</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,388,109</td>
<td align="right">3,767,497</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">19,970,302</td>
<td align="right">17,223,109</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,275,074</td>
<td align="right">4,566,132</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,639,238</td>
<td align="right">2,284,620</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,345,936</td>
<td align="right">1,168,757</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">1,346,456</td>
<td align="right">1,169,277</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,736,494</td>
<td align="right">2,382,075</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">17,294,615</td>
<td align="right">15,077,729</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">17,298,564</td>
<td align="right">15,081,640</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">18,361,185</td>
<td align="right">16,056,971</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">18,900,238</td>
<td align="right">16,689,589</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">5,404,886</td>
<td align="right">4,784,535</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">11,896,761</td>
<td align="right">10,567,582</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">11,896,761</td>
<td align="right">10,567,582</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">3,219,674</td>
<td align="right">2,865,125</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,427,425</td>
<td align="right">2,161,664</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">27,061,104</td>
<td align="right">24,315,675</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">902,073</td>
<td align="right">813,453</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">910,827</td>
<td align="right">822,207</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">917,033</td>
<td align="right">828,061</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">923,423</td>
<td align="right">834,827</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">925,889</td>
<td align="right">837,263</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">927,389</td>
<td align="right">838,763</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,860,056</td>
<td align="right">1,682,840</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">937,794</td>
<td align="right">849,038</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">937,794</td>
<td align="right">849,038</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,760,308</td>
<td align="right">3,405,860</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,760,308</td>
<td align="right">3,405,860</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">966,885</td>
<td align="right">878,284</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">34,088,937</td>
<td align="right">31,077,591</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">30,503,585</td>
<td align="right">27,844,524</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">34,701,259</td>
<td align="right">31,689,634</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,427,134</td>
<td align="right">4,072,710</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">8,199,405</td>
<td align="right">7,667,535</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,456,093</td>
<td align="right">1,367,473</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">7,296,630</td>
<td align="right">6,853,550</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">7,414,089</td>
<td align="right">7,060,603</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,970,940</td>
<td align="right">1,882,341</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">7,023,795</td>
<td align="right">6,757,923</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,537,960</td>
<td align="right">3,449,361</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,038</td>
<td align="right">3,993</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">3,949</td>
<td align="right">3,911</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">17,536</td>
<td align="right">17,522</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">612,322</td>
<td align="right">612,043</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">514,104</td>
<td align="right">513,931</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">531,404</td>
<td align="right">531,231</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">12,240</td>
<td align="right">12,238</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">35,658</td>
<td align="right">35,659</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">35,658</td>
<td align="right">35,659</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">5,806,800</td>
<td align="right">5,806,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,149,780</td>
<td align="right">1,149,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">1,028,780</td>
<td align="right">1,028,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,014,520</td>
<td align="right">1,014,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,008,040</td>
<td align="right">1,008,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">527,400</td>
<td align="right">527,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">506,660</td>
<td align="right">506,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">506,620</td>
<td align="right">506,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">506,580</td>
<td align="right">506,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">82,440</td>
<td align="right">82,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">78,500</td>
<td align="right">78,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">78,300</td>
<td align="right">78,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">78,260</td>
<td align="right">78,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">78,260</td>
<td align="right">78,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">43,796</td>
<td align="right">43,796</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">24,420</td>
<td align="right">24,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">16,580</td>
<td align="right">16,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">16,580</td>
<td align="right">16,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">16,100</td>
<td align="right">16,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">16,100</td>
<td align="right">16,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">15,700</td>
<td align="right">15,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">15,700</td>
<td align="right">15,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">15,700</td>
<td align="right">15,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,740</td>
<td align="right">4,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">4,460</td>
<td align="right">4,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">4,220</td>
<td align="right">4,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,500</td>
<td align="right">1,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">760</td>
<td align="right">760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_IMMORTAL</td>
<td align="right"></td>
<td align="right">1,915,228</td>
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
<td align="right">576</td>
<td align="right">575</td>
<td align="right">-0.2%</td>
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
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-04
