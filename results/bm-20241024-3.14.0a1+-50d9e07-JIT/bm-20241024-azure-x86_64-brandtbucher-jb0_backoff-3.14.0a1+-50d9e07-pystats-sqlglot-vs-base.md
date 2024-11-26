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
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,858</td>
<td align="right">210,714</td>
<td align="right">1,538.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">39,897</td>
<td align="right">370,623</td>
<td align="right">828.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">49,184</td>
<td align="right">359,289</td>
<td align="right">630.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">195,212</td>
<td align="right">542,077</td>
<td align="right">177.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">170,017</td>
<td align="right">456,867</td>
<td align="right">168.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,646,270</td>
<td align="right">104</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,343,917</td>
<td align="right">149</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,330,233</td>
<td align="right">352</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">365,265</td>
<td align="right">2,126</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,003,380</td>
<td align="right">19,727</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,904</td>
<td align="right">31</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">63,287</td>
<td align="right">827</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,807,816</td>
<td align="right">38,269</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">8,479,872</td>
<td align="right">206,298</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,788</td>
<td align="right">252</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,747,226</td>
<td align="right">219,545</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">14,600</td>
<td align="right">724</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,629,207</td>
<td align="right">231,019</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,203,253</td>
<td align="right">319,745</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">15,819,529</td>
<td align="right">29,186,531</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">223,711</td>
<td align="right">54,233</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,046,166</td>
<td align="right">514,465</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,053</td>
<td align="right">1,027</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">36,020,211</td>
<td align="right">9,489,203</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">25,162,124</td>
<td align="right">9,621,137</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">17,071,120</td>
<td align="right">7,535,721</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,169,637</td>
<td align="right">6,102,507</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,173</td>
<td align="right">1,019</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,138,895</td>
<td align="right">35,179,445</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">21,885,755</td>
<td align="right">10,959,293</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,964,535</td>
<td align="right">3,208,835</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">12,150</td>
<td align="right">6,772</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,262,455</td>
<td align="right">719,302</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,607,101</td>
<td align="right">3,222,852</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">23,655,321</td>
<td align="right">13,605,589</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,854,428</td>
<td align="right">4,564,632</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,715,859</td>
<td align="right">3,331,610</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,847,833</td>
<td align="right">7,943,477</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,610,109</td>
<td align="right">2,219,721</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,574,385</td>
<td align="right">2,852,228</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">46,304</td>
<td align="right">28,974</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">9,108,169</td>
<td align="right">5,919,074</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,038,723</td>
<td align="right">5,987,929</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,007,494</td>
<td align="right">8,661,379</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">11,637</td>
<td align="right">15,000</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">437,931</td>
<td align="right">555,008</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">13,113</td>
<td align="right">9,655</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,267,187</td>
<td align="right">4,665,171</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,621,154</td>
<td align="right">7,024,624</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">22,482</td>
<td align="right">16,976</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,673,287</td>
<td align="right">5,809,566</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">26,665</td>
<td align="right">20,606</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,970</td>
<td align="right">10,949</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,585,625</td>
<td align="right">1,913,822</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">18,232</td>
<td align="right">15,230</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">842,411</td>
<td align="right">968,649</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,723,583</td>
<td align="right">5,383,199</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">336,682</td>
<td align="right">295,048</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">22,171</td>
<td align="right">19,431</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">191,098</td>
<td align="right">169,097</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">505,802</td>
<td align="right">448,758</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">9,494,135</td>
<td align="right">8,507,818</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,392,841</td>
<td align="right">24,609,965</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,790,225</td>
<td align="right">1,949,645</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">929,194</td>
<td align="right">848,679</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,885,894</td>
<td align="right">3,128,736</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">20,808</td>
<td align="right">19,527</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,882</td>
<td align="right">2,706</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,618,646</td>
<td align="right">3,424,936</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,256,096</td>
<td align="right">15,520,433</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">485,178</td>
<td align="right">506,336</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">34,041</td>
<td align="right">35,366</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">96,960</td>
<td align="right">93,475</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">106,935</td>
<td align="right">103,128</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">503,222</td>
<td align="right">486,403</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">42,102</td>
<td align="right">43,468</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">204,473</td>
<td align="right">197,912</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">17,373,902</td>
<td align="right">16,830,480</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">181,556</td>
<td align="right">177,302</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,956,072</td>
<td align="right">6,077,647</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">293,006</td>
<td align="right">288,742</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,901,676</td>
<td align="right">2,871,180</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">190,784</td>
<td align="right">189,120</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,247</td>
<td align="right">4,265</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,004,987</td>
<td align="right">2,996,667</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">264,600</td>
<td align="right">265,022</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">31,887</td>
<td align="right">31,924</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">45,729</td>
<td align="right">45,685</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,330,517</td>
<td align="right">11,325,489</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">2,456,469</td>
<td align="right">2,456,487</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">13,059,392</td>
<td align="right">13,059,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3,255,436</td>
<td align="right">3,255,436</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,846,277</td>
<td align="right">2,846,277</td>
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
<td align="left">FOR_ITER_GEN</td>
<td align="right">434,168</td>
<td align="right">434,168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">434,110</td>
<td align="right">434,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">360,648</td>
<td align="right">360,648</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">90,607</td>
<td align="right">90,607</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">89,736</td>
<td align="right">89,736</td>
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
<td align="left">TO_BOOL_LIST</td>
<td align="right">4,356</td>
<td align="right">4,356</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">4,292</td>
<td align="right">4,292</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,857</td>
<td align="right">1,857</td>
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
<td align="left">STORE_DEREF</td>
<td align="right">325</td>
<td align="right">325</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">209</td>
<td align="right">209</td>
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
<td align="left">TO_BOOL_INT</td>
<td align="right">113</td>
<td align="right">113</td>
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
<td align="right">35</td>
<td align="right">33.3%</td>
<td align="right">35</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">70</td>
<td align="right">66.7%</td>
<td align="right">70</td>
<td align="right">66.7%</td>
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
<td align="right">31</td>
<td align="right">100.0%</td>
<td align="right">-99.2%</td>
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
<td align="right">10,793</td>
<td align="right">2.9%</td>
<td align="right">22.5%</td>
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
<td align="right">97.0%</td>
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
<td align="right">54</td>
<td align="right">34.6%</td>
<td align="right">54</td>
<td align="right">34.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">102</td>
<td align="right">65.4%</td>
<td align="right">102</td>
<td align="right">65.4%</td>
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
<td align="right">94</td>
<td align="right">92.2%</td>
<td align="right">94</td>
<td align="right">92.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">5</td>
<td align="right">4.9%</td>
<td align="right">5</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3</td>
<td align="right">2.9%</td>
<td align="right">3</td>
<td align="right">2.9%</td>
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
<td align="right">344,190</td>
<td align="right">0.5%</td>
<td align="right">528.7%</td>
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
<td align="right">75,264,154</td>
<td align="right">99.5%</td>
<td align="right">-0.5%</td>
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
<td align="right">7,754</td>
<td align="right">100.0%</td>
<td align="right">237.3%</td>
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
<td align="right">841,333</td>
<td align="right">71.7%</td>
<td align="right">967,656</td>
<td align="right">74.5%</td>
<td align="right">15.0%</td>
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
<td align="right">25.4%</td>
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
<td align="right">959</td>
<td align="right">96.6%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">34</td>
<td align="right">3.2%</td>
<td align="right">34</td>
<td align="right">3.4%</td>
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
<td align="left">baseobject</td>
<td align="right">358</td>
<td align="right">34.3%</td>
<td align="right">314</td>
<td align="right">32.7%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">408</td>
<td align="right">39.1%</td>
<td align="right">363</td>
<td align="right">37.9%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">48</td>
<td align="right">4.6%</td>
<td align="right">52</td>
<td align="right">5.4%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">181</td>
<td align="right">17.3%</td>
<td align="right">181</td>
<td align="right">18.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">44</td>
<td align="right">4.2%</td>
<td align="right">44</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">5</td>
<td align="right">0.5%</td>
<td align="right">5</td>
<td align="right">0.5%</td>
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
<td align="right">48,938</td>
<td align="right">73.3%</td>
<td align="right">359,080</td>
<td align="right">95.3%</td>
<td align="right">633.7%</td>
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
<td align="right">3.4%</td>
<td align="right">2,279</td>
<td align="right">0.6%</td>
<td align="right">-0.3%</td>
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
<td align="right">22.9%</td>
<td align="right">15,291</td>
<td align="right">4.1%</td>
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
<td align="right">82.0%</td>
<td align="right">200</td>
<td align="right">79.4%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">52</td>
<td align="right">18.0%</td>
<td align="right">52</td>
<td align="right">20.6%</td>
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
<td align="right">237</td>
<td align="right">100.0%</td>
<td align="right">200</td>
<td align="right">100.0%</td>
<td align="right">-15.6%</td>
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
<td align="right">5,962,644</td>
<td align="right">52.1%</td>
<td align="right">3,207,655</td>
<td align="right">34.5%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,485,937</td>
<td align="right">47.9%</td>
<td align="right">6,088,988</td>
<td align="right">65.5%</td>
<td align="right">11.0%</td>
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
<td align="right">1,141</td>
<td align="right">96.7%</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39</td>
<td align="right">2.1%</td>
<td align="right">39</td>
<td align="right">3.3%</td>
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
<td align="right">46</td>
<td align="right">2.5%</td>
<td align="right">4</td>
<td align="right">0.4%</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,483</td>
<td align="right">80.1%</td>
<td align="right">836</td>
<td align="right">73.3%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">146</td>
<td align="right">7.9%</td>
<td align="right">124</td>
<td align="right">10.9%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">96</td>
<td align="right">5.2%</td>
<td align="right">96</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">48</td>
<td align="right">2.6%</td>
<td align="right">48</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">25</td>
<td align="right">1.3%</td>
<td align="right">25</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">8</td>
<td align="right">0.4%</td>
<td align="right">8</td>
<td align="right">0.7%</td>
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
<td align="right">2,137,683</td>
<td align="right">4.7%</td>
<td align="right">848,155</td>
<td align="right">1.9%</td>
<td align="right">-60.3%</td>
</tr>
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
<td align="right">3,710</td>
<td align="right">0.0%</td>
<td align="right">-42.3%</td>
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
<td align="right">100,556</td>
<td align="right">0.2%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">43,430,581</td>
<td align="right">95.1%</td>
<td align="right">43,822,190</td>
<td align="right">97.9%</td>
<td align="right">0.9%</td>
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
<td align="right">17,174</td>
<td align="right">92.9%</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,325</td>
<td align="right">3.1%</td>
<td align="right">1,303</td>
<td align="right">7.1%</td>
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
<td align="right">1,058</td>
<td align="right">79.8%</td>
<td align="right">1,037</td>
<td align="right">79.6%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">225</td>
<td align="right">17.0%</td>
<td align="right">224</td>
<td align="right">17.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">21</td>
<td align="right">1.6%</td>
<td align="right">21</td>
<td align="right">1.6%</td>
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
<td align="right">51,288,391</td>
<td align="right">100.0%</td>
<td align="right">15,644,079</td>
<td align="right">100.0%</td>
<td align="right">-69.5%</td>
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
<td align="right">263,085</td>
<td align="right">44.9%</td>
<td align="right">6.0%</td>
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
<td align="right">322,047</td>
<td align="right">55.0%</td>
<td align="right">-4.1%</td>
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
<td align="right">6,364</td>
<td align="right">100.0%</td>
<td align="right">-4.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">39,921,555</td>
<td align="right">97.8%</td>
<td align="right">40,781,598</td>
<td align="right">97.8%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">885,090</td>
<td align="right">2.2%</td>
<td align="right">876,222</td>
<td align="right">2.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">31,352</td>
<td align="right">0.1%</td>
<td align="right">31,389</td>
<td align="right">0.1%</td>
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
<td align="left">Success</td>
<td align="right">17,087</td>
<td align="right">99.3%</td>
<td align="right">16,909</td>
<td align="right">99.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">124</td>
<td align="right">0.7%</td>
<td align="right">124</td>
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
<td align="left">sequence</td>
<td align="right">118</td>
<td align="right">95.2%</td>
<td align="right">118</td>
<td align="right">95.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6</td>
<td align="right">4.8%</td>
<td align="right">6</td>
<td align="right">4.8%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">186,962,591</td>
<td align="right">38.3%</td>
<td align="right">97,244,809</td>
<td align="right">29.5%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">7,120,081</td>
<td align="right">1.5%</td>
<td align="right">4,795,060</td>
<td align="right">1.5%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">3,417,563</td>
<td align="right">0.7%</td>
<td align="right">2,395,216</td>
<td align="right">0.7%</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">290,264,946</td>
<td align="right">59.5%</td>
<td align="right">225,434,601</td>
<td align="right">68.3%</td>
<td align="right">-22.3%</td>
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
<td align="right">48,938</td>
<td align="right">0.7%</td>
<td align="right">359,080</td>
<td align="right">7.5%</td>
<td align="right">633.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,962,644</td>
<td align="right">83.9%</td>
<td align="right">3,207,655</td>
<td align="right">67.0%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,814</td>
<td align="right">0.1%</td>
<td align="right">10,793</td>
<td align="right">0.2%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">841,333</td>
<td align="right">11.8%</td>
<td align="right">967,656</td>
<td align="right">20.2%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">104,341</td>
<td align="right">1.5%</td>
<td align="right">100,556</td>
<td align="right">2.1%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">31,352</td>
<td align="right">0.4%</td>
<td align="right">31,389</td>
<td align="right">0.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">90,516</td>
<td align="right">1.3%</td>
<td align="right">90,516</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">18,511</td>
<td align="right">0.3%</td>
<td align="right">18,511</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,904</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">352</td>
<td align="right">0.0%</td>
<td align="right">352</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">303</td>
<td align="right">0.0%</td>
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
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,203</td>
<td align="right">0.2%</td>
<td align="right">131,753</td>
<td align="right">5.5%</td>
<td align="right">1,729.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">47,539</td>
<td align="right">1.4%</td>
<td align="right">212,437</td>
<td align="right">8.9%</td>
<td align="right">346.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">96,528</td>
<td align="right">2.8%</td>
<td align="right">9,070</td>
<td align="right">0.4%</td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,614,112</td>
<td align="right">47.2%</td>
<td align="right">548,882</td>
<td align="right">22.9%</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">404,157</td>
<td align="right">11.8%</td>
<td align="right">272,429</td>
<td align="right">11.4%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,886</td>
<td align="right">0.7%</td>
<td align="right">17,774</td>
<td align="right">0.7%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">335,642</td>
<td align="right">9.8%</td>
<td align="right">322,047</td>
<td align="right">13.4%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">321,884</td>
<td align="right">9.4%</td>
<td align="right">318,487</td>
<td align="right">13.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">559,822</td>
<td align="right">16.4%</td>
<td align="right">556,031</td>
<td align="right">23.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,807</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,639</td>
<td align="right">0.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">3,019,281</td>
<td align="right">5.8%</td>
<td align="right">3,014,253</td>
<td align="right">5.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,624,849</td>
<td align="right">9.0%</td>
<td align="right">4,619,821</td>
<td align="right">9.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,624,849</td>
<td align="right">9.0%</td>
<td align="right">4,619,821</td>
<td align="right">9.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">11,330,581</td>
<td align="right">22.0%</td>
<td align="right">11,325,553</td>
<td align="right">21.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">11,330,581</td>
<td align="right">22.0%</td>
<td align="right">11,325,553</td>
<td align="right">21.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">40,283,371</td>
<td align="right">78.0%</td>
<td align="right">40,288,399</td>
<td align="right">78.1%</td>
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
<td align="left">Allocations over 4 kbytes</td>
<td align="right">343</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,121</td>
<td align="right"></td>
<td align="right">1,916</td>
<td align="right"></td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">4,207,468</td>
<td align="right"></td>
<td align="right">2,835,272</td>
<td align="right"></td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">69,230,884</td>
<td align="right">9.2%</td>
<td align="right">47,692,044</td>
<td align="right">6.2%</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">203,940,325</td>
<td align="right">27.2%</td>
<td align="right">144,428,611</td>
<td align="right">18.7%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">341,357,870</td>
<td align="right">45.6%</td>
<td align="right">439,134,546</td>
<td align="right">56.9%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">346,738,024</td>
<td align="right">42.2%</td>
<td align="right">418,015,965</td>
<td align="right">48.0%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">35,984</td>
<td align="right">0.0%</td>
<td align="right">41,174</td>
<td align="right">0.0%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">144,171,613</td>
<td align="right">17.6%</td>
<td align="right">162,911,898</td>
<td align="right">18.7%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">54,641,119</td>
<td align="right">6.7%</td>
<td align="right">47,748,066</td>
<td align="right">5.5%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">275,339,245</td>
<td align="right">33.5%</td>
<td align="right">242,334,009</td>
<td align="right">27.8%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">134,723,858</td>
<td align="right">18.0%</td>
<td align="right">140,600,078</td>
<td align="right">18.2%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">465,107</td>
<td align="right"></td>
<td align="right">462,946</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">466,042</td>
<td align="right"></td>
<td align="right">464,641</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">48,563,690</td>
<td align="right"></td>
<td align="right">48,540,777</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">52,444,067</td>
<td align="right"></td>
<td align="right">52,451,763</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">52,180,184</td>
<td align="right">62.4%</td>
<td align="right">52,187,692</td>
<td align="right">62.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">52,143,857</td>
<td align="right">62.4%</td>
<td align="right">52,146,516</td>
<td align="right">62.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">31,412,450</td>
<td align="right"></td>
<td align="right">31,412,695</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">31,382,029</td>
<td align="right">37.6%</td>
<td align="right">31,382,268</td>
<td align="right">37.6%</td>
<td align="right">0.0%</td>
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
<td align="right">11,068</td>
<td align="right">101,016</td>
<td align="right">23</td>
<td align="right">10,688</td>
<td align="right">92,890</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,525</td>
<td align="right">50.2%</td>
<td align="right">16,922</td>
<td align="right">61.2%</td>
<td align="right">159.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">5,741</td>
<td align="right">44.2%</td>
<td align="right">13,319</td>
<td align="right">48.2%</td>
<td align="right">132.0%</td>
</tr>
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
<td align="right">221</td>
<td align="right">0.8%</td>
<td align="right">118.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">12,992</td>
<td align="right"></td>
<td align="right">27,653</td>
<td align="right"></td>
<td align="right">112.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">7,251</td>
<td align="right">55.8%</td>
<td align="right">14,334</td>
<td align="right">51.8%</td>
<td align="right">97.7%</td>
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
<td align="right">45</td>
<td align="right">0.2%</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">53,200,732</td>
<td align="right"></td>
<td align="right">80,270,145</td>
<td align="right"></td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">789,992,344</td>
<td align="right">1,484.9%</td>
<td align="right">1,137,826,452</td>
<td align="right">1,417.5%</td>
<td align="right">44.0%</td>
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
<td align="right">216</td>
<td align="right">0.8%</td>
<td align="right">0.9%</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">6,797</td>
<td align="right">93.7%</td>
<td align="right">14,266</td>
<td align="right">99.5%</td>
<td align="right">109.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">7,251</td>
<td align="right"></td>
<td align="right">14,334</td>
<td align="right"></td>
<td align="right">97.7%</td>
</tr>
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
<td align="right">46</td>
<td align="right">0.3%</td>
<td align="right">-58.6%</td>
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
<td align="right">199</td>
<td align="right">1.4%</td>
<td align="right">199 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">843</td>
<td align="right">11.6%</td>
<td align="right">932</td>
<td align="right">6.5%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,329</td>
<td align="right">18.3%</td>
<td align="right">3,045</td>
<td align="right">21.2%</td>
<td align="right">129.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,112</td>
<td align="right">15.3%</td>
<td align="right">5,712</td>
<td align="right">39.8%</td>
<td align="right">413.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,136</td>
<td align="right">15.7%</td>
<td align="right">3,378</td>
<td align="right">23.6%</td>
<td align="right">197.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,220</td>
<td align="right">16.8%</td>
<td align="right">802</td>
<td align="right">5.6%</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,265</td>
<td align="right">17.4%</td>
<td align="right">266</td>
<td align="right">1.9%</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">346</td>
<td align="right">4.8%</td>
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
<td align="right">545</td>
<td align="right">7.5%</td>
<td align="right">915</td>
<td align="right">6.4%</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,030</td>
<td align="right">14.2%</td>
<td align="right">888</td>
<td align="right">6.2%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,055</td>
<td align="right">14.5%</td>
<td align="right">5,068</td>
<td align="right">35.4%</td>
<td align="right">380.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,124</td>
<td align="right">15.5%</td>
<td align="right">5,494</td>
<td align="right">38.3%</td>
<td align="right">388.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,264</td>
<td align="right">17.4%</td>
<td align="right">1,439</td>
<td align="right">10.0%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,220</td>
<td align="right">16.8%</td>
<td align="right">436</td>
<td align="right">3.0%</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">430</td>
<td align="right">5.9%</td>
<td align="right">26</td>
<td align="right">0.2%</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">129</td>
<td align="right">1.8%</td>
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
<td align="left">_BUILD_MAP</td>
<td align="right">10,040</td>
<td align="right">2,779,587</td>
<td align="right">27,585.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">5,523</td>
<td align="right">1,349,291</td>
<td align="right">24,330.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">215,529</td>
<td align="right">4,597,835</td>
<td align="right">2,033.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">183,648</td>
<td align="right">2,067,072</td>
<td align="right">1,025.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">126</td>
<td align="right">1,088</td>
<td align="right">763.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">448,021</td>
<td align="right">3,430,021</td>
<td align="right">665.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">255</td>
<td align="right">1,696</td>
<td align="right">565.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">350,385</td>
<td align="right">1,473,440</td>
<td align="right">320.5%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">531,178</td>
<td align="right">2,062,879</td>
<td align="right">288.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,310,609</td>
<td align="right">4,600,405</td>
<td align="right">251.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">1,575</td>
<td align="right">5,362</td>
<td align="right">240.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">9,107,777</td>
<td align="right">27,766,847</td>
<td align="right">204.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,798,694</td>
<td align="right">8,326,375</td>
<td align="right">197.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">693</td>
<td align="right">1,974</td>
<td align="right">184.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,014,183</td>
<td align="right">7,918,539</td>
<td align="right">162.7%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,040</td>
<td align="right">23,916</td>
<td align="right">138.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">12,788,131</td>
<td align="right">29,499,180</td>
<td align="right">130.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">4,346,032</td>
<td align="right">9,987,021</td>
<td align="right">129.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">3,677,955</td>
<td align="right">8,185,275</td>
<td align="right">122.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">853,501</td>
<td align="right">1,843,831</td>
<td align="right">116.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">22,165,450</td>
<td align="right">47,707,683</td>
<td align="right">115.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,464</td>
<td align="right">5,204</td>
<td align="right">111.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,695,946</td>
<td align="right">9,724,413</td>
<td align="right">107.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">17,606,248</td>
<td align="right">36,058,559</td>
<td align="right">104.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">119,480</td>
<td align="right">305</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">662,145</td>
<td align="right">2,529</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">1,247,685</td>
<td align="right">19,193</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,247,685</td>
<td align="right">19,193</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">1,247,685</td>
<td align="right">19,193</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">437,896</td>
<td align="right">15,675</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">437,896</td>
<td align="right">15,675</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">852,550</td>
<td align="right">34,868</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">852,550</td>
<td align="right">34,868</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">10,062,911</td>
<td align="right">19,579,736</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,904,551</td>
<td align="right">5,622,586</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,904,551</td>
<td align="right">5,622,586</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">355,809</td>
<td align="right">25,083</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">355,809</td>
<td align="right">27,612</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">3,783</td>
<td align="right">420</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">3,783</td>
<td align="right">420</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">12,446,111</td>
<td align="right">22,448,109</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">13,183</td>
<td align="right">2,616</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,364,815</td>
<td align="right">9,591,472</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">78,070</td>
<td align="right">136,374</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">28,870</td>
<td align="right">7,712</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">505,199</td>
<td align="right">868,338</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">13,384,052</td>
<td align="right">22,919,451</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,867,014</td>
<td align="right">3,195,614</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">442,079</td>
<td align="right">131,937</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">14,760,042</td>
<td align="right">24,191,711</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,809,074</td>
<td align="right">6,193,323</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">4,518,564</td>
<td align="right">7,288,908</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,327,529</td>
<td align="right">3,725,717</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">216,473</td>
<td align="right">90,150</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">44,168,080</td>
<td align="right">69,352,646</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">5,684</td>
<td align="right">8,854</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">9,267,914</td>
<td align="right">14,332,152</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">17,376,230</td>
<td align="right">26,312,357</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">53,200,732</td>
<td align="right">80,270,145</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">54,536,991</td>
<td align="right">81,261,085</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">8,504,478</td>
<td align="right">12,658,192</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">4,819,919</td>
<td align="right">2,481,220</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">12,645,178</td>
<td align="right">18,412,285</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,698,420</td>
<td align="right">9,749,214</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">3,823,055</td>
<td align="right">5,545,212</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">7,354,990</td>
<td align="right">10,634,400</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,631,710</td>
<td align="right">1,620,654</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">443,821</td>
<td align="right">276,103</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">5,603,416</td>
<td align="right">3,492,766</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,236,201</td>
<td align="right">781,754</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">2,809,417</td>
<td align="right">3,795,734</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">12,893,061</td>
<td align="right">17,364,446</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">29,442,885</td>
<td align="right">39,459,896</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">70,891,884</td>
<td align="right">93,691,229</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,093,020</td>
<td align="right">1,459,770</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">44,707,774</td>
<td align="right">57,638,775</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">16,627,532</td>
<td align="right">21,361,118</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">21,493,927</td>
<td align="right">27,261,016</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">10,458,239</td>
<td align="right">13,213,228</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">11,958,310</td>
<td align="right">8,840,361</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1,336,259</td>
<td align="right">990,940</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">4,864</td>
<td align="right">6,018</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">15,032</td>
<td align="right">18,517</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">3,570,379</td>
<td align="right">4,357,456</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">443,821</td>
<td align="right">539,689</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">9,032,397</td>
<td align="right">10,915,803</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">447,958</td>
<td align="right">528,473</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,379,882</td>
<td align="right">1,996,566</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,472,599</td>
<td align="right">2,141,359</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">5,649,720</td>
<td align="right">5,040,108</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">5,649,720</td>
<td align="right">5,040,108</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,456,530</td>
<td align="right">2,192,565</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">12,239,314</td>
<td align="right">10,959,642</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,277,270</td>
<td align="right">2,060,262</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">2,234,862</td>
<td align="right">2,021,978</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">447,958</td>
<td align="right">489,592</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">25,113,437</td>
<td align="right">27,441,159</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,796,821</td>
<td align="right">4,354,641</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,052,033</td>
<td align="right">1,137,662</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,628,488</td>
<td align="right">2,414,665</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">3,957,052</td>
<td align="right">3,670,202</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,349,624</td>
<td align="right">1,261,647</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">17,586,207</td>
<td align="right">18,710,137</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">31,008</td>
<td align="right">29,029</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">3,293,738</td>
<td align="right">3,487,448</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">31,483</td>
<td align="right">30,158</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">13,043,941</td>
<td align="right">12,500,603</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,608,091</td>
<td align="right">3,462,872</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">43,295</td>
<td align="right">45,025</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">215,571</td>
<td align="right">221,822</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">48,510</td>
<td align="right">47,144</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">2,939,657</td>
<td align="right">3,002,117</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">452,032</td>
<td align="right">460,352</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">93,114</td>
<td align="right">94,778</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">408,480</td>
<td align="right">415,041</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">612,868</td>
<td align="right">619,429</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">612,868</td>
<td align="right">619,429</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">458,802</td>
<td align="right">461,804</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,494,598</td>
<td align="right">3,516,599</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">895,916</td>
<td align="right">901,422</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">2,538,289</td>
<td align="right">2,553,501</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">4,421,448</td>
<td align="right">4,447,451</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,505,255</td>
<td align="right">3,509,519</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">2,844,011</td>
<td align="right">2,847,037</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">2,396,826</td>
<td align="right">2,395,128</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">185,054</td>
<td align="right">185,098</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">5,611,689</td>
<td align="right">5,611,671</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">3,237,060</td>
<td align="right">3,237,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">1,594,263</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,335,131</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">758,651</td>
<td align="right">758,651</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">369,329</td>
<td align="right">369,329</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">346,865</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">99,308</td>
<td align="right">99,308</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">25,083</td>
<td align="right">25,083</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">10,104</td>
<td align="right">10,104</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">5,816</td>
<td align="right">5,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">2,553</td>
<td align="right">2,553</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">2,318</td>
<td align="right">2,318</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,533</td>
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
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">8,273,574</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">2,646,166</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">61,481</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">16,819</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">16,819</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right"></td>
<td align="right">9,536</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right"></td>
<td align="right">9,536</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">3,873</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right"></td>
<td align="right">1,281</td>
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
<td align="right">149</td>
<td align="right">509</td>
<td align="right">241.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">210</td>
<td align="right">394</td>
<td align="right">87.6%</td>
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
Stats gathered on: 2024-10-25
