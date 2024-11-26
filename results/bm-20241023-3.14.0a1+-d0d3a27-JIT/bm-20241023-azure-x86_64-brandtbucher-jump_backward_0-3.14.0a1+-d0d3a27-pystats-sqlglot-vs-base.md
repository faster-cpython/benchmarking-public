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
<td align="right">210,690</td>
<td align="right">1,538.6%</td>
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
<td align="right">359,272</td>
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
<td align="right">170,075</td>
<td align="right">454,029</td>
<td align="right">167.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,610,108</td>
<td align="right">3,436,659</td>
<td align="right">113.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,646,270</td>
<td align="right">30</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,343,917</td>
<td align="right">95</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,330,273</td>
<td align="right">198</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">365,265</td>
<td align="right">778</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,904</td>
<td align="right">15</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,003,380</td>
<td align="right">19,572</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">63,345</td>
<td align="right">542</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,807,816</td>
<td align="right">37,832</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">14,600</td>
<td align="right">260</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">8,479,872</td>
<td align="right">206,363</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,788</td>
<td align="right">252</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">15,820,139</td>
<td align="right">31,163,467</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,747,226</td>
<td align="right">219,370</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,885,894</td>
<td align="right">5,542,228</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,629,247</td>
<td align="right">229,717</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,203,253</td>
<td align="right">321,449</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,673,345</td>
<td align="right">8,203,065</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,111</td>
<td align="right">1,012</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,046,166</td>
<td align="right">517,537</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">223,711</td>
<td align="right">57,162</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">36,020,552</td>
<td align="right">10,701,066</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">25,162,660</td>
<td align="right">9,611,823</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">46,267</td>
<td align="right">19,380</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,173</td>
<td align="right">987</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">21,886,055</td>
<td align="right">10,957,625</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">17,071,278</td>
<td align="right">8,749,252</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">12,150</td>
<td align="right">6,420</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,621,214</td>
<td align="right">8,241,428</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,964,575</td>
<td align="right">3,208,646</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,169,737</td>
<td align="right">7,315,194</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,262,455</td>
<td align="right">715,672</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,140,050</td>
<td align="right">41,196,066</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,607,141</td>
<td align="right">3,222,542</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,854,468</td>
<td align="right">4,563,377</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,715,899</td>
<td align="right">3,331,300</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,574,443</td>
<td align="right">2,851,905</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">23,655,540</td>
<td align="right">14,819,010</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">9,108,325</td>
<td align="right">5,915,846</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,038,947</td>
<td align="right">5,976,722</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">13,113</td>
<td align="right">9,281</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,847,913</td>
<td align="right">9,160,206</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">18,232</td>
<td align="right">13,278</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">438,029</td>
<td align="right">555,618</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,846,277</td>
<td align="right">3,604,928</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">11,637</td>
<td align="right">14,663</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,267,245</td>
<td align="right">4,664,926</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">22,482</td>
<td align="right">16,984</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">26,665</td>
<td align="right">20,590</td>
<td align="right">-22.8%</td>
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
<td align="right">1,913,806</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,392,942</td>
<td align="right">26,587,266</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">22,171</td>
<td align="right">18,798</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,007,534</td>
<td align="right">11,055,002</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">842,411</td>
<td align="right">968,459</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,723,583</td>
<td align="right">5,383,183</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">336,682</td>
<td align="right">295,036</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">505,802</td>
<td align="right">445,715</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">191,156</td>
<td align="right">168,776</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,256,176</td>
<td align="right">17,952,810</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">9,494,175</td>
<td align="right">8,510,708</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,790,225</td>
<td align="right">1,949,320</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">929,194</td>
<td align="right">848,651</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">106,935</td>
<td align="right">99,256</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">20,808</td>
<td align="right">19,351</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,882</td>
<td align="right">2,705</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,607</td>
<td align="right">4,347</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,618,767</td>
<td align="right">3,427,834</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">485,178</td>
<td align="right">509,453</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">96,960</td>
<td align="right">92,804</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">503,222</td>
<td align="right">486,087</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">204,473</td>
<td align="right">197,896</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">17,374,271</td>
<td align="right">16,831,023</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">181,556</td>
<td align="right">176,960</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">190,910</td>
<td align="right">186,595</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,956,072</td>
<td align="right">6,077,870</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">293,064</td>
<td align="right">288,435</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">34,104</td>
<td align="right">33,612</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,901,656</td>
<td align="right">2,870,848</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">42,165</td>
<td align="right">42,032</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,004,987</td>
<td align="right">2,996,671</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">264,600</td>
<td align="right">265,022</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">45,729</td>
<td align="right">45,685</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">31,945</td>
<td align="right">31,968</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,330,517</td>
<td align="right">11,325,349</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">2,456,829</td>
<td align="right">2,456,569</td>
<td align="right">-0.0%</td>
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
<td align="right">15</td>
<td align="right">100.0%</td>
<td align="right">-99.6%</td>
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
<td align="right">75,264,217</td>
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
<td align="right">967,468</td>
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
<td align="right">957</td>
<td align="right">96.6%</td>
<td align="right">-8.3%</td>
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
<td align="right">313</td>
<td align="right">32.7%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">408</td>
<td align="right">39.1%</td>
<td align="right">362</td>
<td align="right">37.8%</td>
<td align="right">-11.3%</td>
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
<td align="right">359,064</td>
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
<td align="right">199</td>
<td align="right">79.3%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">52</td>
<td align="right">18.0%</td>
<td align="right">52</td>
<td align="right">20.7%</td>
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
<td align="right">199</td>
<td align="right">100.0%</td>
<td align="right">-16.0%</td>
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
<td align="right">5,962,684</td>
<td align="right">52.1%</td>
<td align="right">3,207,467</td>
<td align="right">30.5%</td>
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
<td align="right">5,485,936</td>
<td align="right">47.9%</td>
<td align="right">7,305,910</td>
<td align="right">69.5%</td>
<td align="right">33.2%</td>
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
<td align="right">1,140</td>
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
<td align="right">835</td>
<td align="right">73.2%</td>
<td align="right">-43.7%</td>
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
<td align="right">96,874</td>
<td align="right">0.2%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,137,680</td>
<td align="right">4.7%</td>
<td align="right">2,000,411</td>
<td align="right">4.4%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">43,430,544</td>
<td align="right">95.1%</td>
<td align="right">43,852,705</td>
<td align="right">95.4%</td>
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
<td align="left">Failure</td>
<td align="right">1,325</td>
<td align="right">3.1%</td>
<td align="right">1,113</td>
<td align="right">2.8%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,481</td>
<td align="right">96.9%</td>
<td align="right">38,972</td>
<td align="right">97.2%</td>
<td align="right">-6.0%</td>
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
<td align="right">225</td>
<td align="right">17.0%</td>
<td align="right">181</td>
<td align="right">16.3%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">1,058</td>
<td align="right">79.8%</td>
<td align="right">890</td>
<td align="right">80.0%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">21</td>
<td align="right">1.6%</td>
<td align="right">21</td>
<td align="right">1.9%</td>
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
<td align="right">51,288,832</td>
<td align="right">100.0%</td>
<td align="right">18,014,568</td>
<td align="right">100.0%</td>
<td align="right">-64.9%</td>
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
<td align="right">263,485</td>
<td align="right">45.0%</td>
<td align="right">6.1%</td>
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
<td align="right">321,647</td>
<td align="right">54.9%</td>
<td align="right">-4.2%</td>
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
<td align="right">39,921,616</td>
<td align="right">97.8%</td>
<td align="right">40,781,711</td>
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
<td align="right">885,087</td>
<td align="right">2.2%</td>
<td align="right">876,242</td>
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
<td align="right">31,410</td>
<td align="right">0.1%</td>
<td align="right">31,433</td>
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
<td align="right">186,964,836</td>
<td align="right">38.3%</td>
<td align="right">106,924,380</td>
<td align="right">29.8%</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">7,120,179</td>
<td align="right">1.5%</td>
<td align="right">4,790,820</td>
<td align="right">1.3%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">290,268,653</td>
<td align="right">59.5%</td>
<td align="right">243,421,770</td>
<td align="right">67.9%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">3,417,977</td>
<td align="right">0.7%</td>
<td align="right">3,547,294</td>
<td align="right">1.0%</td>
<td align="right">3.8%</td>
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
<td align="right">359,064</td>
<td align="right">7.5%</td>
<td align="right">633.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,962,684</td>
<td align="right">83.8%</td>
<td align="right">3,207,467</td>
<td align="right">67.1%</td>
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
<td align="right">967,468</td>
<td align="right">20.2%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">104,341</td>
<td align="right">1.5%</td>
<td align="right">96,874</td>
<td align="right">2.0%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">31,410</td>
<td align="right">0.4%</td>
<td align="right">31,433</td>
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
<td align="right">3.7%</td>
<td align="right">1,729.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">47,539</td>
<td align="right">1.4%</td>
<td align="right">212,437</td>
<td align="right">6.0%</td>
<td align="right">346.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">404,157</td>
<td align="right">11.8%</td>
<td align="right">1,424,762</td>
<td align="right">40.2%</td>
<td align="right">252.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">96,528</td>
<td align="right">2.8%</td>
<td align="right">9,071</td>
<td align="right">0.3%</td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,614,109</td>
<td align="right">47.2%</td>
<td align="right">548,944</td>
<td align="right">15.5%</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,886</td>
<td align="right">0.7%</td>
<td align="right">17,634</td>
<td align="right">0.5%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">335,642</td>
<td align="right">9.8%</td>
<td align="right">321,647</td>
<td align="right">9.1%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">321,901</td>
<td align="right">9.4%</td>
<td align="right">318,509</td>
<td align="right">9.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">559,802</td>
<td align="right">16.4%</td>
<td align="right">556,029</td>
<td align="right">15.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">3,019,281</td>
<td align="right">5.8%</td>
<td align="right">3,014,113</td>
<td align="right">5.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,624,849</td>
<td align="right">9.0%</td>
<td align="right">4,619,681</td>
<td align="right">9.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,624,849</td>
<td align="right">9.0%</td>
<td align="right">4,619,681</td>
<td align="right">9.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">11,330,581</td>
<td align="right">22.0%</td>
<td align="right">11,325,413</td>
<td align="right">21.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">11,330,581</td>
<td align="right">22.0%</td>
<td align="right">11,325,413</td>
<td align="right">21.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">40,283,371</td>
<td align="right">78.0%</td>
<td align="right">40,288,539</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">296</td>
<td align="right"></td>
<td align="right">594</td>
<td align="right"></td>
<td align="right">100.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">343</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">4,202,007</td>
<td align="right"></td>
<td align="right">2,801,156</td>
<td align="right"></td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">69,231,223</td>
<td align="right">9.2%</td>
<td align="right">50,076,178</td>
<td align="right">6.5%</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">341,360,278</td>
<td align="right">45.6%</td>
<td align="right">424,573,688</td>
<td align="right">54.8%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">203,942,749</td>
<td align="right">27.2%</td>
<td align="right">162,105,072</td>
<td align="right">20.9%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">346,741,007</td>
<td align="right">42.2%</td>
<td align="right">411,894,364</td>
<td align="right">47.0%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">35,988</td>
<td align="right">0.0%</td>
<td align="right">41,310</td>
<td align="right">0.0%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">144,175,414</td>
<td align="right">17.6%</td>
<td align="right">164,893,572</td>
<td align="right">18.8%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">54,641,320</td>
<td align="right">6.7%</td>
<td align="right">47,744,678</td>
<td align="right">5.4%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">275,341,151</td>
<td align="right">33.5%</td>
<td align="right">251,570,782</td>
<td align="right">28.7%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">134,727,618</td>
<td align="right">18.0%</td>
<td align="right">138,217,441</td>
<td align="right">17.8%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">470,608</td>
<td align="right"></td>
<td align="right">468,302</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">470,732</td>
<td align="right"></td>
<td align="right">468,648</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">48,564,512</td>
<td align="right"></td>
<td align="right">48,542,100</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">52,180,188</td>
<td align="right">62.4%</td>
<td align="right">52,187,972</td>
<td align="right">62.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">52,444,095</td>
<td align="right"></td>
<td align="right">52,451,895</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">52,143,857</td>
<td align="right">62.4%</td>
<td align="right">52,146,662</td>
<td align="right">62.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">31,412,448</td>
<td align="right"></td>
<td align="right">31,412,737</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">31,382,029</td>
<td align="right">37.6%</td>
<td align="right">31,382,310</td>
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
<td align="right">101,002</td>
<td align="right">23</td>
<td align="right">9,995</td>
<td align="right">77,426</td>
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
<td align="right">6,522</td>
<td align="right">50.2%</td>
<td align="right">17,115</td>
<td align="right">60.9%</td>
<td align="right">162.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">5,739</td>
<td align="right">44.2%</td>
<td align="right">13,444</td>
<td align="right">47.8%</td>
<td align="right">134.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">12,994</td>
<td align="right"></td>
<td align="right">28,122</td>
<td align="right"></td>
<td align="right">116.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">7,255</td>
<td align="right">55.8%</td>
<td align="right">14,657</td>
<td align="right">52.1%</td>
<td align="right">102.0%</td>
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
<td align="right">197</td>
<td align="right">0.7%</td>
<td align="right">95.0%</td>
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
<td align="right">44</td>
<td align="right">0.2%</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">53,199,812</td>
<td align="right"></td>
<td align="right">81,403,801</td>
<td align="right"></td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">789,981,473</td>
<td align="right">1,484.9%</td>
<td align="right">1,081,800,489</td>
<td align="right">1,328.9%</td>
<td align="right">36.9%</td>
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
<td align="right">237</td>
<td align="right">0.8%</td>
<td align="right">10.7%</td>
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
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">6,801</td>
<td align="right">93.7%</td>
<td align="right">14,588</td>
<td align="right">99.5%</td>
<td align="right">114.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">7,255</td>
<td align="right"></td>
<td align="right">14,657</td>
<td align="right"></td>
<td align="right">102.0%</td>
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
<td align="right">842</td>
<td align="right">11.6%</td>
<td align="right">1,015</td>
<td align="right">6.9%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,330</td>
<td align="right">18.3%</td>
<td align="right">3,035</td>
<td align="right">20.7%</td>
<td align="right">128.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,113</td>
<td align="right">15.3%</td>
<td align="right">5,915</td>
<td align="right">40.4%</td>
<td align="right">431.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,137</td>
<td align="right">15.7%</td>
<td align="right">3,342</td>
<td align="right">22.8%</td>
<td align="right">193.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,220</td>
<td align="right">16.8%</td>
<td align="right">867</td>
<td align="right">5.9%</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,267</td>
<td align="right">17.5%</td>
<td align="right">284</td>
<td align="right">1.9%</td>
<td align="right">-77.6%</td>
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
<td align="right">851</td>
<td align="right">5.8%</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,029</td>
<td align="right">14.2%</td>
<td align="right">1,035</td>
<td align="right">7.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,056</td>
<td align="right">14.6%</td>
<td align="right">5,104</td>
<td align="right">34.8%</td>
<td align="right">383.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,125</td>
<td align="right">15.5%</td>
<td align="right">5,592</td>
<td align="right">38.2%</td>
<td align="right">397.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,265</td>
<td align="right">17.4%</td>
<td align="right">1,525</td>
<td align="right">10.4%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,221</td>
<td align="right">16.8%</td>
<td align="right">437</td>
<td align="right">3.0%</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">431</td>
<td align="right">5.9%</td>
<td align="right">44</td>
<td align="right">0.3%</td>
<td align="right">-89.8%</td>
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
<td align="right">2,780,024</td>
<td align="right">27,589.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">5,523</td>
<td align="right">1,349,345</td>
<td align="right">24,331.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">215,529</td>
<td align="right">4,597,942</td>
<td align="right">2,033.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">183,648</td>
<td align="right">2,065,368</td>
<td align="right">1,024.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">126</td>
<td align="right">1,104</td>
<td align="right">776.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">448,021</td>
<td align="right">3,430,176</td>
<td align="right">665.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">332</td>
<td align="right">1,952</td>
<td align="right">488.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">350,385</td>
<td align="right">1,473,779</td>
<td align="right">320.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">531,178</td>
<td align="right">2,059,807</td>
<td align="right">287.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">1,575</td>
<td align="right">5,736</td>
<td align="right">264.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,310,569</td>
<td align="right">4,601,660</td>
<td align="right">251.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">693</td>
<td align="right">2,150</td>
<td align="right">210.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">9,107,679</td>
<td align="right">27,776,484</td>
<td align="right">205.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,798,694</td>
<td align="right">8,326,550</td>
<td align="right">197.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,040</td>
<td align="right">24,380</td>
<td align="right">142.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">12,787,910</td>
<td align="right">30,419,927</td>
<td align="right">137.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,464</td>
<td align="right">5,837</td>
<td align="right">136.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">4,345,992</td>
<td align="right">9,960,956</td>
<td align="right">129.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">3,677,915</td>
<td align="right">8,186,693</td>
<td align="right">122.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,014,103</td>
<td align="right">6,701,810</td>
<td align="right">122.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">853,481</td>
<td align="right">1,843,397</td>
<td align="right">116.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">10,063,077</td>
<td align="right">21,189,021</td>
<td align="right">110.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,695,946</td>
<td align="right">9,728,807</td>
<td align="right">107.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">22,165,009</td>
<td align="right">45,337,957</td>
<td align="right">104.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">2,396,826</td>
<td align="right">1,012</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">119,480</td>
<td align="right">82</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">662,145</td>
<td align="right">2,545</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">17,605,987</td>
<td align="right">34,881,438</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">2,538,289</td>
<td align="right">159,401</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,349,664</td>
<td align="right">85,051</td>
<td align="right">-93.7%</td>
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
<td align="right">27,628</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">4,819,818</td>
<td align="right">503,696</td>
<td align="right">-89.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,092,980</td>
<td align="right">242,834</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,631,670</td>
<td align="right">403,484</td>
<td align="right">-84.7%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">28,870</td>
<td align="right">4,595</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1,336,548</td>
<td align="right">222,419</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">5,684</td>
<td align="right">10,272</td>
<td align="right">80.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">12,445,933</td>
<td align="right">22,450,431</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">13,183</td>
<td align="right">2,617</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">3,783</td>
<td align="right">757</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">3,783</td>
<td align="right">757</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">78,070</td>
<td align="right">139,417</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">505,199</td>
<td align="right">869,686</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,608,011</td>
<td align="right">1,029,000</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,866,974</td>
<td align="right">3,195,592</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">442,079</td>
<td align="right">131,953</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">2,234,822</td>
<td align="right">805,042</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,472,559</td>
<td align="right">924,200</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,809,034</td>
<td align="right">6,193,633</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">13,383,894</td>
<td align="right">21,705,920</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">4,518,564</td>
<td align="right">7,286,331</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,327,489</td>
<td align="right">3,727,019</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,456,510</td>
<td align="right">981,114</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">44,167,443</td>
<td align="right">70,487,832</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,796,695</td>
<td align="right">1,963,245</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">216,473</td>
<td align="right">90,338</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,364,755</td>
<td align="right">8,395,695</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">14,759,823</td>
<td align="right">22,978,221</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">9,267,856</td>
<td align="right">14,330,376</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">53,199,812</td>
<td align="right">81,403,801</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,904,531</td>
<td align="right">4,411,290</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,904,531</td>
<td align="right">4,411,290</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">17,375,963</td>
<td align="right">26,318,413</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">54,536,360</td>
<td align="right">81,626,220</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,698,196</td>
<td align="right">9,760,421</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">3,822,997</td>
<td align="right">5,545,535</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">7,354,814</td>
<td align="right">10,637,663</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">443,821</td>
<td align="right">276,255</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">5,603,358</td>
<td align="right">3,492,718</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,236,201</td>
<td align="right">779,797</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">2,809,377</td>
<td align="right">3,792,844</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">5,649,721</td>
<td align="right">3,823,170</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">5,649,721</td>
<td align="right">3,823,170</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">12,239,095</td>
<td align="right">8,563,891</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">16,627,452</td>
<td align="right">21,364,408</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">15,032</td>
<td align="right">19,188</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">12,645,080</td>
<td align="right">16,020,136</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">10,458,199</td>
<td align="right">13,213,416</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">29,442,371</td>
<td align="right">37,181,519</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">11,957,949</td>
<td align="right">8,840,279</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">13,043,435</td>
<td align="right">9,676,812</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">4,864</td>
<td align="right">6,050</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">70,890,969</td>
<td align="right">86,930,423</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">3,570,321</td>
<td align="right">4,357,811</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">443,821</td>
<td align="right">539,841</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">44,707,259</td>
<td align="right">54,028,479</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">9,032,037</td>
<td align="right">10,914,017</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">8,504,438</td>
<td align="right">10,264,593</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">447,958</td>
<td align="right">528,501</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">12,892,963</td>
<td align="right">14,973,702</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,379,842</td>
<td align="right">1,996,582</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">21,493,469</td>
<td align="right">24,868,785</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,277,230</td>
<td align="right">2,060,278</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">447,958</td>
<td align="right">489,604</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">25,113,380</td>
<td align="right">27,443,237</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,052,033</td>
<td align="right">1,138,702</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,628,448</td>
<td align="right">2,414,693</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">43,232</td>
<td align="right">46,665</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">3,956,994</td>
<td align="right">3,673,040</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">17,585,859</td>
<td align="right">18,708,690</td>
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
<td align="right">3,293,617</td>
<td align="right">3,484,550</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">92,988</td>
<td align="right">97,303</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">215,571</td>
<td align="right">221,838</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">2,939,599</td>
<td align="right">3,002,402</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">452,032</td>
<td align="right">460,348</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">408,480</td>
<td align="right">415,057</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">31,420</td>
<td align="right">31,912</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">458,802</td>
<td align="right">463,756</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">612,868</td>
<td align="right">619,445</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">612,868</td>
<td align="right">619,445</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,494,540</td>
<td align="right">3,516,920</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">895,916</td>
<td align="right">901,414</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">4,421,448</td>
<td align="right">4,447,927</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">48,447</td>
<td align="right">48,580</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,505,197</td>
<td align="right">3,509,826</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">2,843,953</td>
<td align="right">2,847,052</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">185,054</td>
<td align="right">185,098</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">5,611,329</td>
<td align="right">5,611,589</td>
<td align="right">0.0%</td>
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
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">1,247,685</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,247,685</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">1,247,685</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">852,550</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">852,550</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">758,651</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">437,896</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">437,896</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">8,273,509</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">2,646,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">61,483</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">17,135</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">17,135</td>
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
<td align="right">3,889</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right"></td>
<td align="right">1,457</td>
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
<td align="right">512</td>
<td align="right">243.6%</td>
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
Stats gathered on: 2024-10-23
