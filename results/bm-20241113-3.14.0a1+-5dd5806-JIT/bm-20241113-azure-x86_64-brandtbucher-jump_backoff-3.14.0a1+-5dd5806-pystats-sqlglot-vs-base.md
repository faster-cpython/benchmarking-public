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
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">209</td>
<td align="right">87,043</td>
<td align="right">41,547.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">325</td>
<td align="right">22,279</td>
<td align="right">6,755.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">22,482</td>
<td align="right">906,512</td>
<td align="right">3,932.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">18,232</td>
<td align="right">469,768</td>
<td align="right">2,476.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,858</td>
<td align="right">279,440</td>
<td align="right">2,073.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">113</td>
<td align="right">2,431</td>
<td align="right">2,051.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">46,264</td>
<td align="right">969,155</td>
<td align="right">1,994.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">293,048</td>
<td align="right">3,780,411</td>
<td align="right">1,190.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">168,345</td>
<td align="right">1,121,223</td>
<td align="right">566.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">38,189</td>
<td align="right">253,137</td>
<td align="right">562.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">47,476</td>
<td align="right">279,132</td>
<td align="right">487.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">181,556</td>
<td align="right">904,455</td>
<td align="right">398.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,307</td>
<td align="right">21,324</td>
<td align="right">395.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">26,665</td>
<td align="right">115,921</td>
<td align="right">334.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,970</td>
<td align="right">36,935</td>
<td align="right">311.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">191,134</td>
<td align="right">786,131</td>
<td align="right">311.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">438,009</td>
<td align="right">1,728,919</td>
<td align="right">294.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,173</td>
<td align="right">7,037</td>
<td align="right">223.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,089</td>
<td align="right">12,093</td>
<td align="right">195.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">223,711</td>
<td align="right">594,712</td>
<td align="right">165.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">31,923</td>
<td align="right">76,622</td>
<td align="right">140.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">4,292</td>
<td align="right">10,108</td>
<td align="right">135.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">336,682</td>
<td align="right">778,697</td>
<td align="right">131.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">63,323</td>
<td align="right">145,967</td>
<td align="right">130.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">45,729</td>
<td align="right">100,793</td>
<td align="right">120.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">42,102</td>
<td align="right">90,612</td>
<td align="right">115.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">363,557</td>
<td align="right">714,140</td>
<td align="right">96.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">34,041</td>
<td align="right">65,524</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,256,187</td>
<td align="right">2,353,282</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">189,833</td>
<td align="right">326,904</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">14,600</td>
<td align="right">24,640</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">4,356</td>
<td align="right">6,909</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">204,473</td>
<td align="right">318,718</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,329,035</td>
<td align="right">636,502</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,035,859</td>
<td align="right">13,640,484</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">929,194</td>
<td align="right">1,371,209</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">5,586,619</td>
<td align="right">7,949,958</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,663,658</td>
<td align="right">6,609,487</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,901,656</td>
<td align="right">4,091,828</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">9,105,342</td>
<td align="right">12,413,918</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,613,767</td>
<td align="right">7,495,435</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">11,637</td>
<td align="right">15,420</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">190,784</td>
<td align="right">242,276</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">15,815,311</td>
<td align="right">11,974,768</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,628,009</td>
<td align="right">1,250,545</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,882,478</td>
<td align="right">3,441,115</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">25,153,087</td>
<td align="right">29,986,049</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,044,458</td>
<td align="right">2,435,657</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,608,871</td>
<td align="right">1,313,317</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">841,557</td>
<td align="right">982,997</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,568,308</td>
<td align="right">2,989,776</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">434,168</td>
<td align="right">503,828</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,118,456</td>
<td align="right">83,299,800</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,003,380</td>
<td align="right">3,451,093</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,004,987</td>
<td align="right">3,451,076</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">96,960</td>
<td align="right">110,144</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,583,917</td>
<td align="right">1,798,865</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">505,802</td>
<td align="right">573,246</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">21,874,120</td>
<td align="right">24,651,730</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">13,113</td>
<td align="right">14,688</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">22,171</td>
<td align="right">24,635</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">17,060,870</td>
<td align="right">18,788,815</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,618,682</td>
<td align="right">3,980,753</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">89,736</td>
<td align="right">97,992</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,996,613</td>
<td align="right">14,119,380</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,568,153</td>
<td align="right">4,949,894</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,203,253</td>
<td align="right">2,384,738</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">36,003,015</td>
<td align="right">38,959,719</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,720,167</td>
<td align="right">5,106,848</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">28,511,155</td>
<td align="right">26,351,162</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,843,730</td>
<td align="right">11,944,153</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">9,492,936</td>
<td align="right">8,911,664</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">12,150</td>
<td align="right">12,864</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">485,178</td>
<td align="right">512,935</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,252,910</td>
<td align="right">17,141,382</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,789,371</td>
<td align="right">1,886,120</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,154,728</td>
<td align="right">13,785,737</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">23,638,803</td>
<td align="right">24,671,250</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,851,523</td>
<td align="right">7,511,751</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,857</td>
<td align="right">1,920</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">20,808</td>
<td align="right">21,501</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,963,338</td>
<td align="right">5,827,715</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,712,954</td>
<td align="right">5,584,545</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">195,211</td>
<td align="right">199,567</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,604,196</td>
<td align="right">5,512,592</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">106,935</td>
<td align="right">108,370</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">2,456,529</td>
<td align="right">2,473,546</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">360,648</td>
<td align="right">362,688</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,747,226</td>
<td align="right">5,777,938</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,807,816</td>
<td align="right">2,817,856</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,343,917</td>
<td align="right">1,347,697</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3,255,436</td>
<td align="right">3,262,048</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">264,600</td>
<td align="right">265,022</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,846,277</td>
<td align="right">2,847,283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">17,374,090</td>
<td align="right">17,369,424</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">13,059,392</td>
<td align="right">13,059,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,330,517</td>
<td align="right">11,330,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">8,479,872</td>
<td align="right">8,479,872</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,646,270</td>
<td align="right">2,646,270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">2,452,224</td>
<td align="right">2,452,224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">2,452,224</td>
<td align="right">2,452,224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">503,222</td>
<td align="right">503,222</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">434,110</td>
<td align="right">434,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">90,607</td>
<td align="right">90,607</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">57,781</td>
<td align="right">57,781</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">27,136</td>
<td align="right">27,136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">18,616</td>
<td align="right">18,616</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,788</td>
<td align="right">9,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,904</td>
<td align="right">3,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,882</td>
<td align="right">2,882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,584</td>
<td align="right">1,584</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,026</td>
<td align="right">1,026</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">959</td>
<td align="right">959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">368</td>
<td align="right">368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">142</td>
<td align="right">142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">48</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
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
<td align="right">18,511</td>
<td align="right">11.8%</td>
<td align="right">18,511</td>
<td align="right">11.8%</td>
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
<td align="right">137,649</td>
<td align="right">88.1%</td>
<td align="right">137,649</td>
<td align="right">88.1%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">70</td>
<td align="right">100.0%</td>
<td align="right">70</td>
<td align="right">100.0%</td>
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
<td align="left">add other</td>
<td align="right">49</td>
<td align="right">70.0%</td>
<td align="right">49</td>
<td align="right">70.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21</td>
<td align="right">30.0%</td>
<td align="right">21</td>
<td align="right">30.0%</td>
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
<td align="right">3,904</td>
<td align="right">100.0%</td>
<td align="right">3,904</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,814</td>
<td align="right">2.4%</td>
<td align="right">36,693</td>
<td align="right">9.3%</td>
<td align="right">316.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">358,706</td>
<td align="right">97.5%</td>
<td align="right">358,706</td>
<td align="right">90.6%</td>
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
<td align="right">192</td>
<td align="right">0.1%</td>
<td align="right">192</td>
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
<td align="right">102</td>
<td align="right">65.4%</td>
<td align="right">188</td>
<td align="right">77.7%</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">54</td>
<td align="right">34.6%</td>
<td align="right">54</td>
<td align="right">22.3%</td>
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
<td align="left">out of range</td>
<td align="right">3</td>
<td align="right">2.9%</td>
<td align="right">45</td>
<td align="right">23.9%</td>
<td align="right">1,400.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">5</td>
<td align="right">4.9%</td>
<td align="right">49</td>
<td align="right">26.1%</td>
<td align="right">880.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">94</td>
<td align="right">92.2%</td>
<td align="right">94</td>
<td align="right">50.0%</td>
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
<td align="right">54,742</td>
<td align="right">0.1%</td>
<td align="right">428,068</td>
<td align="right">0.6%</td>
<td align="right">682.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">75,641,690</td>
<td align="right">99.9%</td>
<td align="right">75,102,779</td>
<td align="right">99.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">352</td>
<td align="right">0.0%</td>
<td align="right">352</td>
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
<td align="right">2,299</td>
<td align="right">100.0%</td>
<td align="right">9,354</td>
<td align="right">100.0%</td>
<td align="right">306.9%</td>
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
<td align="left">init not inline values</td>
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
<td align="right">14</td>
<td align="right">29.2%</td>
<td align="right">14</td>
<td align="right">29.2%</td>
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
<td align="right">840,479</td>
<td align="right">71.7%</td>
<td align="right">981,849</td>
<td align="right">74.7%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">330,546</td>
<td align="right">28.2%</td>
<td align="right">330,546</td>
<td align="right">25.2%</td>
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
<td align="right">1,044</td>
<td align="right">96.8%</td>
<td align="right">1,114</td>
<td align="right">97.0%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">34</td>
<td align="right">3.2%</td>
<td align="right">34</td>
<td align="right">3.0%</td>
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
<td align="left">string</td>
<td align="right">5</td>
<td align="right">0.5%</td>
<td align="right">50</td>
<td align="right">4.5%</td>
<td align="right">900.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">48</td>
<td align="right">4.6%</td>
<td align="right">31</td>
<td align="right">2.8%</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">358</td>
<td align="right">34.3%</td>
<td align="right">400</td>
<td align="right">35.9%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">408</td>
<td align="right">39.1%</td>
<td align="right">408</td>
<td align="right">36.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">181</td>
<td align="right">17.3%</td>
<td align="right">181</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">44</td>
<td align="right">4.2%</td>
<td align="right">44</td>
<td align="right">3.9%</td>
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
<td align="right">47,230</td>
<td align="right">72.6%</td>
<td align="right">278,938</td>
<td align="right">94.0%</td>
<td align="right">490.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,284</td>
<td align="right">23.5%</td>
<td align="right">15,284</td>
<td align="right">5.2%</td>
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
<td align="right">2,286</td>
<td align="right">3.5%</td>
<td align="right">2,286</td>
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
<td align="left">Failure</td>
<td align="right">237</td>
<td align="right">100.0%</td>
<td align="right">185</td>
<td align="right">100.0%</td>
<td align="right">-21.9%</td>
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
<td align="left">tuple</td>
<td align="right">237</td>
<td align="right">100.0%</td>
<td align="right">185</td>
<td align="right">100.0%</td>
<td align="right">-21.9%</td>
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
<td align="right">5,484,699</td>
<td align="right">47.9%</td>
<td align="right">5,303,390</td>
<td align="right">47.6%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,961,447</td>
<td align="right">52.1%</td>
<td align="right">5,825,861</td>
<td align="right">52.3%</td>
<td align="right">-2.3%</td>
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
<td align="right">1,852</td>
<td align="right">97.9%</td>
<td align="right">1,815</td>
<td align="right">97.9%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39</td>
<td align="right">2.1%</td>
<td align="right">39</td>
<td align="right">2.1%</td>
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
<td align="right">8</td>
<td align="right">0.4%</td>
<td align="right">96</td>
<td align="right">5.3%</td>
<td align="right">1,100.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">25</td>
<td align="right">1.3%</td>
<td align="right">46</td>
<td align="right">2.5%</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">48</td>
<td align="right">2.6%</td>
<td align="right">31</td>
<td align="right">1.7%</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">96</td>
<td align="right">5.2%</td>
<td align="right">84</td>
<td align="right">4.6%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,483</td>
<td align="right">80.1%</td>
<td align="right">1,364</td>
<td align="right">75.2%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">146</td>
<td align="right">7.9%</td>
<td align="right">148</td>
<td align="right">8.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">46</td>
<td align="right">2.5%</td>
<td align="right">46</td>
<td align="right">2.5%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,425</td>
<td align="right">0.0%</td>
<td align="right">305,249</td>
<td align="right">0.6%</td>
<td align="right">4,651.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,138,023</td>
<td align="right">4.7%</td>
<td align="right">3,356,158</td>
<td align="right">7.1%</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">104,341</td>
<td align="right">0.2%</td>
<td align="right">105,734</td>
<td align="right">0.2%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">43,500,653</td>
<td align="right">95.1%</td>
<td align="right">43,791,373</td>
<td align="right">92.7%</td>
<td align="right">0.7%</td>
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
<td align="right">41,481</td>
<td align="right">96.9%</td>
<td align="right">64,478</td>
<td align="right">97.9%</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,325</td>
<td align="right">3.1%</td>
<td align="right">1,367</td>
<td align="right">2.1%</td>
<td align="right">3.2%</td>
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
<td align="right">1,058</td>
<td align="right">79.8%</td>
<td align="right">1,100</td>
<td align="right">80.5%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">225</td>
<td align="right">17.0%</td>
<td align="right">225</td>
<td align="right">16.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">21</td>
<td align="right">1.6%</td>
<td align="right">21</td>
<td align="right">1.5%</td>
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
<td align="right">51,393,816</td>
<td align="right">100.0%</td>
<td align="right">53,552,180</td>
<td align="right">100.0%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">303</td>
<td align="right">0.0%</td>
<td align="right">303</td>
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
<td align="right">1,692</td>
<td align="right">0.0%</td>
<td align="right">1,692</td>
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
<td align="right">767</td>
<td align="right">100.0%</td>
<td align="right">767</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">8,068,158</td>
<td align="right">100.0%</td>
<td align="right">8,068,158</td>
<td align="right">100.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">248,230</td>
<td align="right">42.5%</td>
<td align="right">242,854</td>
<td align="right">41.4%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">335,642</td>
<td align="right">57.4%</td>
<td align="right">342,677</td>
<td align="right">58.5%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">44</td>
<td align="right">0.0%</td>
<td align="right">44</td>
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
<td align="right">6,637</td>
<td align="right">100.0%</td>
<td align="right">6,763</td>
<td align="right">100.0%</td>
<td align="right">1.9%</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">230,783</td>
<td align="right">100.0%</td>
<td align="right">230,783</td>
<td align="right">100.0%</td>
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
<td align="right">1</td>
<td align="right">100.0%</td>
<td align="right">1</td>
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
<td align="right">885,086</td>
<td align="right">2.2%</td>
<td align="right">2,493,891</td>
<td align="right">5.7%</td>
<td align="right">181.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">31,388</td>
<td align="right">0.1%</td>
<td align="right">76,098</td>
<td align="right">0.2%</td>
<td align="right">142.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">39,915,327</td>
<td align="right">97.8%</td>
<td align="right">41,006,575</td>
<td align="right">94.1%</td>
<td align="right">2.7%</td>
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
<td align="right">17,087</td>
<td align="right">99.3%</td>
<td align="right">47,447</td>
<td align="right">99.8%</td>
<td align="right">177.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">124</td>
<td align="right">0.7%</td>
<td align="right">113</td>
<td align="right">0.2%</td>
<td align="right">-8.9%</td>
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
<td align="right">6</td>
<td align="right">4.8%</td>
<td align="right">11</td>
<td align="right">9.7%</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">118</td>
<td align="right">95.2%</td>
<td align="right">102</td>
<td align="right">90.3%</td>
<td align="right">-13.6%</td>
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
<td align="right">90,516</td>
<td align="right">0.7%</td>
<td align="right">90,516</td>
<td align="right">0.7%</td>
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
<td align="right">13,040,940</td>
<td align="right">99.3%</td>
<td align="right">13,040,940</td>
<td align="right">99.3%</td>
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
<td align="right">40</td>
<td align="right">44.0%</td>
<td align="right">40</td>
<td align="right">44.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">51</td>
<td align="right">56.0%</td>
<td align="right">51</td>
<td align="right">56.0%</td>
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
<td align="left">other</td>
<td align="right">51</td>
<td align="right">100.0%</td>
<td align="right">51</td>
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
<td align="right">3,417,920</td>
<td align="right">0.7%</td>
<td align="right">6,625,182</td>
<td align="right">1.2%</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">192,442,710</td>
<td align="right">39.3%</td>
<td align="right">224,175,822</td>
<td align="right">41.5%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">286,837,479</td>
<td align="right">58.6%</td>
<td align="right">302,352,454</td>
<td align="right">55.9%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">7,116,358</td>
<td align="right">1.5%</td>
<td align="right">7,427,930</td>
<td align="right">1.4%</td>
<td align="right">4.4%</td>
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
<td align="right">47,230</td>
<td align="right">0.7%</td>
<td align="right">278,938</td>
<td align="right">3.8%</td>
<td align="right">490.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,814</td>
<td align="right">0.1%</td>
<td align="right">36,693</td>
<td align="right">0.5%</td>
<td align="right">316.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">31,388</td>
<td align="right">0.4%</td>
<td align="right">76,098</td>
<td align="right">1.0%</td>
<td align="right">142.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">840,479</td>
<td align="right">11.8%</td>
<td align="right">981,849</td>
<td align="right">13.2%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,961,447</td>
<td align="right">83.9%</td>
<td align="right">5,825,861</td>
<td align="right">78.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">104,341</td>
<td align="right">1.5%</td>
<td align="right">105,734</td>
<td align="right">1.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">90,516</td>
<td align="right">1.3%</td>
<td align="right">90,516</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">18,511</td>
<td align="right">0.3%</td>
<td align="right">18,511</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,904</td>
<td align="right">0.1%</td>
<td align="right">3,904</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">352</td>
<td align="right">0.0%</td>
<td align="right">352</td>
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
<td align="right">1,807</td>
<td align="right">0.1%</td>
<td align="right">279,132</td>
<td align="right">4.2%</td>
<td align="right">15,347.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,203</td>
<td align="right">0.2%</td>
<td align="right">182,368</td>
<td align="right">2.8%</td>
<td align="right">2,431.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">47,539</td>
<td align="right">1.4%</td>
<td align="right">245,700</td>
<td align="right">3.7%</td>
<td align="right">416.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">96,528</td>
<td align="right">2.8%</td>
<td align="right">395,352</td>
<td align="right">6.0%</td>
<td align="right">309.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">321,900</td>
<td align="right">9.4%</td>
<td align="right">860,813</td>
<td align="right">13.0%</td>
<td align="right">167.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">559,802</td>
<td align="right">16.4%</td>
<td align="right">1,352,516</td>
<td align="right">20.4%</td>
<td align="right">141.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,613,160</td>
<td align="right">47.2%</td>
<td align="right">2,525,566</td>
<td align="right">38.1%</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">335,642</td>
<td align="right">9.8%</td>
<td align="right">342,677</td>
<td align="right">5.2%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">405,449</td>
<td align="right">11.9%</td>
<td align="right">412,354</td>
<td align="right">6.2%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,886</td>
<td align="right">0.7%</td>
<td align="right">22,886</td>
<td align="right">0.3%</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">11,330,581</td>
<td align="right">22.0%</td>
<td align="right">11,330,581</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">40,283,371</td>
<td align="right">78.0%</td>
<td align="right">40,283,371</td>
<td align="right">78.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">11,330,581</td>
<td align="right">22.0%</td>
<td align="right">11,330,581</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,624,849</td>
<td align="right">9.0%</td>
<td align="right">4,624,849</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">6,705,732</td>
<td align="right">13.0%</td>
<td align="right">6,705,732</td>
<td align="right">13.0%</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,624,849</td>
<td align="right">9.0%</td>
<td align="right">4,624,849</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
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
<td align="right">1,587,200</td>
<td align="right">3.1%</td>
<td align="right">1,587,200</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">25,664</td>
<td align="right">0.0%</td>
<td align="right">25,664</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">3,019,281</td>
<td align="right">5.8%</td>
<td align="right">3,019,281</td>
<td align="right">5.8%</td>
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
<tr>
<td align="left">Frame objects created</td>
<td align="right">192</td>
<td align="right">0.0%</td>
<td align="right">192</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">33,168,832</td>
<td align="right">64.3%</td>
<td align="right">33,168,832</td>
<td align="right">64.3%</td>
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
<td align="right">2,727</td>
<td align="right"></td>
<td align="right">3,381</td>
<td align="right"></td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">54,638,744</td>
<td align="right">6.6%</td>
<td align="right">62,572,628</td>
<td align="right">7.8%</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">758</td>
<td align="right">0.0%</td>
<td align="right">861</td>
<td align="right">0.0%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">344,574,793</td>
<td align="right">46.4%</td>
<td align="right">304,046,343</td>
<td align="right">41.9%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">203,836,977</td>
<td align="right">27.4%</td>
<td align="right">227,018,872</td>
<td align="right">31.3%</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">349,924,534</td>
<td align="right">42.5%</td>
<td align="right">313,015,918</td>
<td align="right">39.0%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">144,176,758</td>
<td align="right">17.5%</td>
<td align="right">132,698,009</td>
<td align="right">16.5%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">59,563,479</td>
<td align="right">8.0%</td>
<td align="right">63,882,489</td>
<td align="right">8.8%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">275,264,998</td>
<td align="right">33.4%</td>
<td align="right">294,821,369</td>
<td align="right">36.7%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">35,637</td>
<td align="right">0.0%</td>
<td align="right">33,392</td>
<td align="right">0.0%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">4,168,711</td>
<td align="right"></td>
<td align="right">4,393,929</td>
<td align="right"></td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">134,740,717</td>
<td align="right">18.1%</td>
<td align="right">131,047,064</td>
<td align="right">18.1%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">48,562,120</td>
<td align="right"></td>
<td align="right">48,846,648</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">471,908</td>
<td align="right"></td>
<td align="right">470,831</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">474,367</td>
<td align="right"></td>
<td align="right">473,846</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">52,443,124</td>
<td align="right"></td>
<td align="right">52,437,856</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">52,180,232</td>
<td align="right">62.4%</td>
<td align="right">52,177,020</td>
<td align="right">62.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">52,143,837</td>
<td align="right">62.4%</td>
<td align="right">52,142,767</td>
<td align="right">62.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">31,382,010</td>
<td align="right">37.6%</td>
<td align="right">31,381,909</td>
<td align="right">37.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">31,412,315</td>
<td align="right"></td>
<td align="right">31,412,214</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">16,704</td>
<td align="right"></td>
<td align="right">16,704</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
<td align="right">23</td>
<td align="right">10,688</td>
<td align="right">92,858</td>
<td align="right">23</td>
<td align="right">10,372</td>
<td align="right">88,658</td>
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">101</td>
<td align="right">0.8%</td>
<td align="right">219</td>
<td align="right">2.7%</td>
<td align="right">116.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">325</td>
<td align="right">2.5%</td>
<td align="right">567</td>
<td align="right">7.1%</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">7,260</td>
<td align="right">55.8%</td>
<td align="right">3,706</td>
<td align="right">46.3%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">13,020</td>
<td align="right"></td>
<td align="right">8,005</td>
<td align="right"></td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">53,695,240</td>
<td align="right"></td>
<td align="right">38,611,133</td>
<td align="right"></td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,590</td>
<td align="right">50.6%</td>
<td align="right">4,797</td>
<td align="right">59.9%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">5,760</td>
<td align="right">44.2%</td>
<td align="right">4,299</td>
<td align="right">53.7%</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">792,334,525</td>
<td align="right">1,475.6%</td>
<td align="right">632,216,284</td>
<td align="right">1,637.4%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">214</td>
<td align="right">1.6%</td>
<td align="right">194</td>
<td align="right">2.4%</td>
<td align="right">-9.3%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">111</td>
<td align="right">1.5%</td>
<td align="right">21</td>
<td align="right">0.6%</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">7,260</td>
<td align="right"></td>
<td align="right">3,706</td>
<td align="right"></td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">6,806</td>
<td align="right">93.7%</td>
<td align="right">3,643</td>
<td align="right">98.3%</td>
<td align="right">-46.5%</td>
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
<td align="right">889</td>
<td align="right">12.2%</td>
<td align="right">725</td>
<td align="right">19.6%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,329</td>
<td align="right">18.3%</td>
<td align="right">281</td>
<td align="right">7.6%</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,113</td>
<td align="right">15.3%</td>
<td align="right">726</td>
<td align="right">19.6%</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,136</td>
<td align="right">15.6%</td>
<td align="right">347</td>
<td align="right">9.4%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,201</td>
<td align="right">16.5%</td>
<td align="right">533</td>
<td align="right">14.4%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,265</td>
<td align="right">17.4%</td>
<td align="right">926</td>
<td align="right">25.0%</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">327</td>
<td align="right">4.5%</td>
<td align="right">168</td>
<td align="right">4.5%</td>
<td align="right">-48.6%</td>
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
<td align="right">413</td>
<td align="right">5.7%</td>
<td align="right">449</td>
<td align="right">12.1%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,208</td>
<td align="right">16.6%</td>
<td align="right">557</td>
<td align="right">15.0%</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,055</td>
<td align="right">14.5%</td>
<td align="right">297</td>
<td align="right">8.0%</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,126</td>
<td align="right">15.5%</td>
<td align="right">604</td>
<td align="right">16.3%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,348</td>
<td align="right">18.6%</td>
<td align="right">218</td>
<td align="right">5.9%</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,265</td>
<td align="right">17.4%</td>
<td align="right">909</td>
<td align="right">24.5%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">243</td>
<td align="right">3.3%</td>
<td align="right">567</td>
<td align="right">15.3%</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">148</td>
<td align="right">2.0%</td>
<td align="right">42</td>
<td align="right">1.1%</td>
<td align="right">-71.6%</td>
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
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,505,213</td>
<td align="right">17,850</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">443,821</td>
<td align="right">4,620</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">443,821</td>
<td align="right">4,620</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">183,648</td>
<td align="right">2,163</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">452,032</td>
<td align="right">5,943</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">448,021</td>
<td align="right">5,943</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">895,916</td>
<td align="right">11,886</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">447,958</td>
<td align="right">5,943</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">447,958</td>
<td align="right">5,943</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">458,802</td>
<td align="right">7,266</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">28,870</td>
<td align="right">1,113</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">43,295</td>
<td align="right">1,848</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">31,008</td>
<td align="right">3,129</td>
<td align="right">-89.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">15,032</td>
<td align="right">1,848</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">25,083</td>
<td align="right">3,129</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">99,308</td>
<td align="right">12,474</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">78,070</td>
<td align="right">12,285</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">10,104</td>
<td align="right">1,848</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">532,886</td>
<td align="right">141,687</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">506,907</td>
<td align="right">156,324</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,701,284</td>
<td align="right">2,096,659</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">482,316</td>
<td align="right">150,990</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">482,316</td>
<td align="right">150,990</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">5,523</td>
<td align="right">1,743</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">941,390</td>
<td align="right">303,996</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">941,390</td>
<td align="right">303,996</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">252</td>
<td align="right">85</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">217,327</td>
<td align="right">75,957</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">216,383</td>
<td align="right">75,978</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,242,469</td>
<td align="right">468,034</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">1,296,375</td>
<td align="right">504,420</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,296,375</td>
<td align="right">504,420</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">1,296,375</td>
<td align="right">504,420</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">357,517</td>
<td align="right">142,569</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">357,517</td>
<td align="right">142,569</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">665,561</td>
<td align="right">278,880</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">13,183</td>
<td align="right">5,796</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">93,114</td>
<td align="right">41,622</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,317,364</td>
<td align="right">595,882</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">853,479</td>
<td align="right">394,785</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">443,787</td>
<td align="right">212,079</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">267,159</td>
<td align="right">132,552</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">29,450,800</td>
<td align="right">15,023,889</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">4,657,677</td>
<td align="right">6,817,670</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">7,357,795</td>
<td align="right">4,172,635</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">5,603,380</td>
<td align="right">3,269,601</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">215,571</td>
<td align="right">126,315</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">17,384,107</td>
<td align="right">10,237,630</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,055,469</td>
<td align="right">636,149</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,868,212</td>
<td align="right">2,560,682</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">119,480</td>
<td align="right">75,285</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">5,133,878</td>
<td align="right">3,255,102</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">9,524,133</td>
<td align="right">6,306,455</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">44,491,235</td>
<td align="right">29,846,033</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">9,268,605</td>
<td align="right">6,298,289</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,802,955</td>
<td align="right">3,299,421</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,612,765</td>
<td align="right">4,706,483</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,018,286</td>
<td align="right">3,917,863</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">185,054</td>
<td align="right">129,990</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">10,082,817</td>
<td align="right">7,126,727</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">53,695,240</td>
<td align="right">38,611,133</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">55,031,176</td>
<td align="right">39,856,719</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">12,129,603</td>
<td align="right">8,811,683</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,313,514</td>
<td align="right">1,653,286</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,094,218</td>
<td align="right">2,629,142</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">3,958,724</td>
<td align="right">3,005,846</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">44,696,590</td>
<td align="right">34,008,310</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">25,119,757</td>
<td align="right">19,306,048</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">2,810,616</td>
<td align="right">3,391,888</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">2,236,913</td>
<td align="right">2,696,594</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">4,421,448</td>
<td align="right">3,539,345</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">12,657,731</td>
<td align="right">10,141,074</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">70,891,521</td>
<td align="right">57,168,226</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">612,868</td>
<td align="right">498,623</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">612,868</td>
<td align="right">498,623</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,494,562</td>
<td align="right">2,899,565</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">8,945,518</td>
<td align="right">7,430,435</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,328,727</td>
<td align="right">2,706,191</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,329,547</td>
<td align="right">4,508,357</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">12,244,303</td>
<td align="right">10,387,991</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">3,381,481</td>
<td align="right">3,877,963</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">22,171,720</td>
<td align="right">19,141,632</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">408,480</td>
<td align="right">353,534</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,279,321</td>
<td align="right">2,585,462</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,940,249</td>
<td align="right">2,553,569</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,940,249</td>
<td align="right">2,553,569</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,474,650</td>
<td align="right">2,796,827</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">13,394,302</td>
<td align="right">11,666,357</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">17,533,415</td>
<td align="right">15,309,503</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">4,518,500</td>
<td align="right">3,967,810</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">21,506,420</td>
<td align="right">18,903,086</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">3,293,702</td>
<td align="right">2,931,631</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">16,056,809</td>
<td align="right">14,299,145</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,382,901</td>
<td align="right">2,640,923</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">12,734,031</td>
<td align="right">11,417,740</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">3,570,343</td>
<td align="right">3,206,286</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">3,829,287</td>
<td align="right">3,447,546</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">13,043,079</td>
<td align="right">11,851,470</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,335,987</td>
<td align="right">1,222,420</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1,335,936</td>
<td align="right">1,245,586</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">16,637,612</td>
<td align="right">15,671,210</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,635,470</td>
<td align="right">2,782,416</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">2,568,222</td>
<td align="right">2,426,950</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">17,586,037</td>
<td align="right">16,642,724</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">5,650,958</td>
<td align="right">5,946,512</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">5,650,958</td>
<td align="right">5,946,512</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">9,203,753</td>
<td align="right">8,765,015</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">14,770,292</td>
<td align="right">14,107,528</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">1,596,546</td>
<td align="right">1,529,545</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">3,679,152</td>
<td align="right">3,524,925</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,630,539</td>
<td align="right">2,529,371</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">2,939,621</td>
<td align="right">2,856,977</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,811,979</td>
<td align="right">3,903,583</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,492,228</td>
<td align="right">2,547,626</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">3,237,060</td>
<td align="right">3,167,400</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">369,329</td>
<td align="right">362,717</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,695,946</td>
<td align="right">4,629,168</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">2,538,269</td>
<td align="right">2,503,957</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">4,157,611</td>
<td align="right">4,102,890</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">10,459,436</td>
<td align="right">10,595,022</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">346,866</td>
<td align="right">342,510</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,798,694</td>
<td align="right">2,767,982</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">350,385</td>
<td align="right">351,875</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">5,611,629</td>
<td align="right">5,594,612</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">2,843,975</td>
<td align="right">2,835,971</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">758,651</td>
<td align="right">757,645</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">48,510</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">31,483</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">10,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">5,816</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">5,684</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">4,864</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">3,783</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">3,783</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">2,553</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,464</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,464</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">2,318</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">1,575</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,533</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">693</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">422</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">422</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">126</td>
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
<td align="right">210</td>
<td align="right">42</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">149</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-14
