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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">103,902</td>
<td align="right">6,362</td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">97,432</td>
<td align="right">6,356</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">598,421</td>
<td align="right">79,201</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">523,583</td>
<td align="right">87,443</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,756,611</td>
<td align="right">302,785</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">4,228</td>
<td align="right">751</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,718,647</td>
<td align="right">326,783</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">2,321,150</td>
<td align="right">520,401</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">945,049</td>
<td align="right">214,925</td>
<td align="right">-77.3%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">552,482</td>
<td align="right">127,695</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">885,150</td>
<td align="right">218,922</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,271,884</td>
<td align="right">821,841</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,338</td>
<td align="right">2,270</td>
<td align="right">-72.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,208,189</td>
<td align="right">655,423</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,505,720</td>
<td align="right">1,425,402</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">13,708,375</td>
<td align="right">4,495,199</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,181,141</td>
<td align="right">731,484</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,966,437</td>
<td align="right">1,340,203</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,268,488</td>
<td align="right">775,151</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,099,517</td>
<td align="right">1,407,983</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,220,248</td>
<td align="right">1,498,525</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,330,708</td>
<td align="right">477,066</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,471,821</td>
<td align="right">1,617,425</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,499,471</td>
<td align="right">1,648,619</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,550,915</td>
<td align="right">953,185</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">3,631,293</td>
<td align="right">1,368,014</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,551,377</td>
<td align="right">601,729</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,221,871</td>
<td align="right">877,248</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">25,156</td>
<td align="right">10,007</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,657,891</td>
<td align="right">2,655,693</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">16,352,197</td>
<td align="right">6,616,315</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">54,366,132</td>
<td align="right">22,430,966</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,197,611</td>
<td align="right">3,419,043</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,310,302</td>
<td align="right">1,804,995</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">5,735,871</td>
<td align="right">2,403,675</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">130,093,463</td>
<td align="right">55,443,741</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">187,149</td>
<td align="right">81,104</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,409,488</td>
<td align="right">1,050,146</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,195,240</td>
<td align="right">4,988,794</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,255,150</td>
<td align="right">2,789,679</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,876,036</td>
<td align="right">1,289,125</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,613,576</td>
<td align="right">1,171,778</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">24,006,159</td>
<td align="right">10,778,580</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,124,452</td>
<td align="right">955,057</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">644,594</td>
<td align="right">293,201</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">864,476</td>
<td align="right">395,172</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,137,377</td>
<td align="right">8,770,279</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">35,021,275</td>
<td align="right">16,050,738</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">12,859,266</td>
<td align="right">5,897,200</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">241,284</td>
<td align="right">112,349</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">4,515,112</td>
<td align="right">2,139,906</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">497,705</td>
<td align="right">237,059</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,299,669</td>
<td align="right">620,676</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">806,292</td>
<td align="right">387,682</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">12,713,608</td>
<td align="right">6,118,750</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">31,572,884</td>
<td align="right">15,246,752</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">30,946,774</td>
<td align="right">14,956,470</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,500,874</td>
<td align="right">3,630,491</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,852,546</td>
<td align="right">6,708,145</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,508,319</td>
<td align="right">1,214,925</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">22,689,854</td>
<td align="right">11,004,178</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">10,587,972</td>
<td align="right">5,136,380</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">9,222,294</td>
<td align="right">4,490,404</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">18,319,921</td>
<td align="right">8,999,617</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">341,108</td>
<td align="right">168,637</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,645,303</td>
<td align="right">2,297,313</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">519,839</td>
<td align="right">257,173</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,534,767</td>
<td align="right">759,738</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">935,297</td>
<td align="right">463,998</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">457,490</td>
<td align="right">227,284</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">681,977</td>
<td align="right">338,934</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">557,306</td>
<td align="right">277,064</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,614,164</td>
<td align="right">1,802,493</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,301,761</td>
<td align="right">649,547</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">770,351</td>
<td align="right">384,678</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">4,155</td>
<td align="right">2,075</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">4,158</td>
<td align="right">2,078</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">4,158</td>
<td align="right">2,078</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,767,807</td>
<td align="right">883,552</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">8,317</td>
<td align="right">4,157</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">54,062</td>
<td align="right">27,022</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">29,111</td>
<td align="right">14,551</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">49,906</td>
<td align="right">24,946</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">83,177</td>
<td align="right">41,577</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">33,271</td>
<td align="right">16,631</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">266,169</td>
<td align="right">133,049</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">116,449</td>
<td align="right">58,209</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">640,477</td>
<td align="right">320,157</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,867,376</td>
<td align="right">933,456</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">573,941</td>
<td align="right">286,901</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">573,941</td>
<td align="right">286,901</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">573,941</td>
<td align="right">286,901</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,451,491</td>
<td align="right">725,571</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,409,901</td>
<td align="right">704,781</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">952,411</td>
<td align="right">476,091</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">407,582</td>
<td align="right">203,742</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">203,791</td>
<td align="right">101,871</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">120,611</td>
<td align="right">60,291</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">45,749</td>
<td align="right">22,869</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">45,749</td>
<td align="right">22,869</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">45,749</td>
<td align="right">22,869</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">33,272</td>
<td align="right">16,632</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">29,113</td>
<td align="right">14,553</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">24,954</td>
<td align="right">12,474</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">24,954</td>
<td align="right">12,474</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">12,477</td>
<td align="right">6,237</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">8,318</td>
<td align="right">4,158</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">4,159</td>
<td align="right">2,079</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">4,159</td>
<td align="right">2,079</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">4,159</td>
<td align="right">2,079</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">4,159</td>
<td align="right">2,079</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,500,058</td>
<td align="right">2,249,498</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,367,182</td>
<td align="right">1,683,204</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,262,636</td>
<td align="right">1,131,114</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,845,488</td>
<td align="right">1,422,526</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">711,259</td>
<td align="right">355,578</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">470,107</td>
<td align="right">235,065</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">195,543</td>
<td align="right">97,782</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,773</td>
<td align="right">35,412</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">66,614</td>
<td align="right">33,333</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">33,342</td>
<td align="right">16,701</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">25,020</td>
<td align="right">12,539</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">20,865</td>
<td align="right">10,464</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,558</td>
<td align="right">18,836</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">12,547</td>
<td align="right">6,306</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">75,553</td>
<td align="right">38,109</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,229</td>
<td align="right">2,148</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">49,142</td>
<td align="right">25,978</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">11,243</td>
<td align="right">6,291</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">69</td>
<td align="right">68</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,116</td>
<td align="right">1,116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">536</td>
<td align="right">536</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">181</td>
<td align="right">181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">107</td>
<td align="right">107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">86</td>
<td align="right">86</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">48</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
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
<td align="right">8,267</td>
<td align="right">0.0%</td>
<td align="right">2,184</td>
<td align="right">0.0%</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,944,352</td>
<td align="right">99.9%</td>
<td align="right">18,467,712</td>
<td align="right">100.0%</td>
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
<td align="right">12,782</td>
<td align="right">0.0%</td>
<td align="right">6,432</td>
<td align="right">0.0%</td>
<td align="right">-49.7%</td>
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
<td align="right">12</td>
<td align="right">3.9%</td>
<td align="right">27</td>
<td align="right">12.6%</td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">297</td>
<td align="right">96.1%</td>
<td align="right">188</td>
<td align="right">87.4%</td>
<td align="right">-36.7%</td>
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
<td align="right">11</td>
<td align="right">91.7%</td>
<td align="right">26</td>
<td align="right">96.3%</td>
<td align="right">136.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1</td>
<td align="right">8.3%</td>
<td align="right">1</td>
<td align="right">3.7%</td>
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
<td align="right">1,451,491</td>
<td align="right">100.0%</td>
<td align="right">725,571</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
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
<td align="right">46,563,866</td>
<td align="right">97.2%</td>
<td align="right">23,274,072</td>
<td align="right">97.2%</td>
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
<td align="right">1,323,282</td>
<td align="right">2.8%</td>
<td align="right">662,517</td>
<td align="right">2.8%</td>
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
<td align="right">1,298,756</td>
<td align="right">2.7%</td>
<td align="right">650,456</td>
<td align="right">2.7%</td>
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
<td align="right">25,642</td>
<td align="right">100.0%</td>
<td align="right">13,177</td>
<td align="right">100.0%</td>
<td align="right">-48.6%</td>
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
<td align="right">43</td>
<td align="right">50.0%</td>
<td align="right">43</td>
<td align="right">50.0%</td>
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
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">43</td>
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
<td align="right">6,253,415</td>
<td align="right">29.2%</td>
<td align="right">2,788,739</td>
<td align="right">27.4%</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,134,576</td>
<td align="right">70.8%</td>
<td align="right">7,392,954</td>
<td align="right">72.6%</td>
<td align="right">-51.2%</td>
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
<td align="right">1,710</td>
<td align="right">98.6%</td>
<td align="right">915</td>
<td align="right">97.3%</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">25</td>
<td align="right">1.4%</td>
<td align="right">25</td>
<td align="right">2.7%</td>
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
<td align="right">117</td>
<td align="right">6.8%</td>
<td align="right">8</td>
<td align="right">0.9%</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">1,593</td>
<td align="right">93.2%</td>
<td align="right">907</td>
<td align="right">99.1%</td>
<td align="right">-43.1%</td>
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
<td align="right">7,203,357</td>
<td align="right">91.2%</td>
<td align="right">3,600,797</td>
<td align="right">91.2%</td>
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
<td align="right">661,297</td>
<td align="right">8.4%</td>
<td align="right">330,577</td>
<td align="right">8.4%</td>
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
<td align="right">37,446</td>
<td align="right">0.5%</td>
<td align="right">18,726</td>
<td align="right">0.5%</td>
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
<td align="left">Success</td>
<td align="right">12,492</td>
<td align="right">99.2%</td>
<td align="right">6,252</td>
<td align="right">98.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97</td>
<td align="right">0.8%</td>
<td align="right">95</td>
<td align="right">1.5%</td>
<td align="right">-2.1%</td>
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
<td align="right">47</td>
<td align="right">48.5%</td>
<td align="right">46</td>
<td align="right">48.4%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">50</td>
<td align="right">51.5%</td>
<td align="right">49</td>
<td align="right">51.6%</td>
<td align="right">-2.0%</td>
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
<td align="right">1,136,356</td>
<td align="right">33.8%</td>
<td align="right">263,615</td>
<td align="right">23.1%</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,221,156</td>
<td align="right">66.1%</td>
<td align="right">876,833</td>
<td align="right">76.9%</td>
<td align="right">-60.5%</td>
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
<td align="right">693</td>
<td align="right">96.9%</td>
<td align="right">393</td>
<td align="right">94.7%</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">22</td>
<td align="right">3.1%</td>
<td align="right">22</td>
<td align="right">5.3%</td>
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
<td align="left">dict items</td>
<td align="right">343</td>
<td align="right">49.5%</td>
<td align="right">162</td>
<td align="right">41.2%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">142</td>
<td align="right">20.5%</td>
<td align="right">75</td>
<td align="right">19.1%</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">146</td>
<td align="right">21.1%</td>
<td align="right">100</td>
<td align="right">25.4%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">60</td>
<td align="right">8.7%</td>
<td align="right">54</td>
<td align="right">13.7%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2</td>
<td align="right">0.3%</td>
<td align="right">2</td>
<td align="right">0.5%</td>
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
<td align="left">string</td>
<td align="right">1,018,955</td>
<td align="right">1,018,955 / 0 !!</td>
<td align="right">509,355</td>
<td align="right">509,355 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">395,105</td>
<td align="right">395,105 / 0 !!</td>
<td align="right">197,505</td>
<td align="right">197,505 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">382,628</td>
<td align="right">382,628 / 0 !!</td>
<td align="right">191,268</td>
<td align="right">191,268 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">12,477</td>
<td align="right">12,477 / 0 !!</td>
<td align="right">6,237</td>
<td align="right">6,237 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,477</td>
<td align="right">12,477 / 0 !!</td>
<td align="right">6,237</td>
<td align="right">6,237 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">8,318</td>
<td align="right">8,318 / 0 !!</td>
<td align="right">4,158</td>
<td align="right">4,158 / 0 !!</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,160,431</td>
<td align="right">1,160,431 / 0 !!</td>
<td align="right">580,110</td>
<td align="right">580,110 / 0 !!</td>
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
<td align="right">4,403,657</td>
<td align="right">2.6%</td>
<td align="right">1,539,999</td>
<td align="right">1.8%</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,493,958</td>
<td align="right">4.4%</td>
<td align="right">3,623,978</td>
<td align="right">4.3%</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">160,046,648</td>
<td align="right">93.1%</td>
<td align="right">78,778,537</td>
<td align="right">93.8%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">514,342</td>
<td align="right">0.3%</td>
<td align="right">257,120</td>
<td align="right">0.3%</td>
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
<td align="left">Success</td>
<td align="right">83,918</td>
<td align="right">93.2%</td>
<td align="right">29,878</td>
<td align="right">84.0%</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,094</td>
<td align="right">6.8%</td>
<td align="right">5,691</td>
<td align="right">16.0%</td>
<td align="right">-6.6%</td>
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
<td align="right">237</td>
<td align="right">3.9%</td>
<td align="right">211</td>
<td align="right">3.7%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">4,768</td>
<td align="right">78.2%</td>
<td align="right">4,437</td>
<td align="right">78.0%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">926</td>
<td align="right">15.2%</td>
<td align="right">883</td>
<td align="right">15.5%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">47</td>
<td align="right">0.8%</td>
<td align="right">46</td>
<td align="right">0.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">47</td>
<td align="right">0.8%</td>
<td align="right">46</td>
<td align="right">0.8%</td>
<td align="right">-2.1%</td>
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
<td align="right">26,565,942</td>
<td align="right">100.0%</td>
<td align="right">12,826,683</td>
<td align="right">100.0%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">228</td>
<td align="right">0.0%</td>
<td align="right">228</td>
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
<td align="right">212</td>
<td align="right">0.0%</td>
<td align="right">212</td>
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
<td align="right">312</td>
<td align="right">100.0%</td>
<td align="right">312</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">33,271</td>
<td align="right">100.0%</td>
<td align="right">16,631</td>
<td align="right">100.0%</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">2,705,230</td>
<td align="right">6.8%</td>
<td align="right">852,637</td>
<td align="right">4.4%</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">37,184,843</td>
<td align="right">93.2%</td>
<td align="right">18,644,142</td>
<td align="right">95.6%</td>
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
<td align="right">45</td>
<td align="right">0.0%</td>
<td align="right">45</td>
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
<td align="right">51,119</td>
<td align="right">100.0%</td>
<td align="right">16,305</td>
<td align="right">100.0%</td>
<td align="right">-68.1%</td>
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
<td align="right">187,149</td>
<td align="right">100.0%</td>
<td align="right">93,549</td>
<td align="right">100.0%</td>
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
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
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
<td align="right">6</td>
<td align="right">100.0%</td>
<td align="right">6</td>
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
<td align="right">3,841,395</td>
<td align="right">9.4%</td>
<td align="right">1,822,674</td>
<td align="right">9.0%</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,788,542</td>
<td align="right">90.4%</td>
<td align="right">18,321,733</td>
<td align="right">90.8%</td>
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
<td align="right">75,148</td>
<td align="right">0.2%</td>
<td align="right">37,707</td>
<td align="right">0.2%</td>
<td align="right">-49.8%</td>
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
<td align="right">72,597</td>
<td align="right">99.8%</td>
<td align="right">34,584</td>
<td align="right">99.5%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">166</td>
<td align="right">0.2%</td>
<td align="right">163</td>
<td align="right">0.5%</td>
<td align="right">-1.8%</td>
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
<td align="right">47</td>
<td align="right">28.3%</td>
<td align="right">46</td>
<td align="right">28.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">47</td>
<td align="right">28.3%</td>
<td align="right">46</td>
<td align="right">28.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">72</td>
<td align="right">43.4%</td>
<td align="right">71</td>
<td align="right">43.6%</td>
<td align="right">-1.4%</td>
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
<td align="right">4,213,126</td>
<td align="right">100.0%</td>
<td align="right">2,106,085</td>
<td align="right">100.0%</td>
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
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">11</td>
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
<td align="right">31</td>
<td align="right">100.0%</td>
<td align="right">31</td>
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
<td align="right">12,947,965</td>
<td align="right">2.1%</td>
<td align="right">5,215,157</td>
<td align="right">1.9%</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">329,914,381</td>
<td align="right">52.8%</td>
<td align="right">144,464,156</td>
<td align="right">52.8%</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">262,189,742</td>
<td align="right">41.9%</td>
<td align="right">114,823,879</td>
<td align="right">42.0%</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">19,962,224</td>
<td align="right">3.2%</td>
<td align="right">9,134,251</td>
<td align="right">3.3%</td>
<td align="right">-54.2%</td>
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
<td align="right">8,267</td>
<td align="right">0.0%</td>
<td align="right">2,184</td>
<td align="right">0.0%</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,221,156</td>
<td align="right">11.8%</td>
<td align="right">876,833</td>
<td align="right">10.1%</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,253,415</td>
<td align="right">33.2%</td>
<td align="right">2,788,739</td>
<td align="right">32.0%</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,493,958</td>
<td align="right">39.8%</td>
<td align="right">3,623,978</td>
<td align="right">41.5%</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,451,491</td>
<td align="right">7.7%</td>
<td align="right">725,571</td>
<td align="right">8.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,446</td>
<td align="right">0.2%</td>
<td align="right">18,726</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,298,756</td>
<td align="right">6.9%</td>
<td align="right">650,456</td>
<td align="right">7.5%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">75,148</td>
<td align="right">0.4%</td>
<td align="right">37,707</td>
<td align="right">0.4%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">228</td>
<td align="right">0.0%</td>
<td align="right">228</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">45</td>
<td align="right">0.0%</td>
<td align="right">45</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,322,728</td>
<td align="right">10.2%</td>
<td align="right">258,689</td>
<td align="right">5.0%</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,705,230</td>
<td align="right">20.9%</td>
<td align="right">852,637</td>
<td align="right">16.3%</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,482,197</td>
<td align="right">19.2%</td>
<td align="right">982,522</td>
<td align="right">18.8%</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,467,306</td>
<td align="right">11.3%</td>
<td align="right">685,745</td>
<td align="right">13.1%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,658,974</td>
<td align="right">12.8%</td>
<td align="right">780,775</td>
<td align="right">15.0%</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">425,751</td>
<td align="right">3.3%</td>
<td align="right">211,032</td>
<td align="right">4.0%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">648,890</td>
<td align="right">5.0%</td>
<td align="right">323,246</td>
<td align="right">6.2%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">574,149</td>
<td align="right">4.4%</td>
<td align="right">287,017</td>
<td align="right">5.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">330,667</td>
<td align="right">2.6%</td>
<td align="right">165,307</td>
<td align="right">3.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">660,981</td>
<td align="right">5.1%</td>
<td align="right">331,780</td>
<td align="right">6.4%</td>
<td align="right">-49.8%</td>
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
<td align="right">45,749</td>
<td align="right">0.1%</td>
<td align="right">22,869</td>
<td align="right">0.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">457,491</td>
<td align="right">1.3%</td>
<td align="right">228,691</td>
<td align="right">1.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,794,863</td>
<td align="right">7.7%</td>
<td align="right">1,397,103</td>
<td align="right">7.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">494,924</td>
<td align="right">1.4%</td>
<td align="right">247,404</td>
<td align="right">1.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">31,850,022</td>
<td align="right">87.6%</td>
<td align="right">15,921,376</td>
<td align="right">87.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">36,312,718</td>
<td align="right">99.9%</td>
<td align="right">18,152,231</td>
<td align="right">99.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">4,500,128</td>
<td align="right">12.4%</td>
<td align="right">2,249,567</td>
<td align="right">12.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">4,500,128</td>
<td align="right">12.4%</td>
<td align="right">2,249,567</td>
<td align="right">12.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,005,204</td>
<td align="right">11.0%</td>
<td align="right">2,002,163</td>
<td align="right">11.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,005,204</td>
<td align="right">11.0%</td>
<td align="right">2,002,163</td>
<td align="right">11.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">12,547</td>
<td align="right">0.0%</td>
<td align="right">6,306</td>
<td align="right">0.0%</td>
<td align="right">-49.7%</td>
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
<td align="right">12,586,221</td>
<td align="right">2.8%</td>
<td align="right">4,475,808</td>
<td align="right">2.0%</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">10,493,961</td>
<td align="right">2.5%</td>
<td align="right">3,779,947</td>
<td align="right">1.8%</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">199,634,868</td>
<td align="right">44.6%</td>
<td align="right">92,153,531</td>
<td align="right">41.3%</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">165,614,173</td>
<td align="right">39.1%</td>
<td align="right">76,843,318</td>
<td align="right">36.4%</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">98,622</td>
<td align="right"></td>
<td align="right">47,596</td>
<td align="right"></td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,176,051</td>
<td align="right"></td>
<td align="right">584,493</td>
<td align="right"></td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,077,883</td>
<td align="right"></td>
<td align="right">537,264</td>
<td align="right"></td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">15,016,388</td>
<td align="right"></td>
<td align="right">7,501,085</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,324,787</td>
<td align="right">39.9%</td>
<td align="right">7,658,283</td>
<td align="right">39.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">15,354,333</td>
<td align="right">40.0%</td>
<td align="right">7,673,185</td>
<td align="right">40.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">694,553</td>
<td align="right"></td>
<td align="right">347,193</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">23,024,472</td>
<td align="right"></td>
<td align="right">11,511,202</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">23,027,614</td>
<td align="right">60.0%</td>
<td align="right">11,513,826</td>
<td align="right">60.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">11,420,141</td>
<td align="right"></td>
<td align="right">5,710,187</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">27,396,307</td>
<td align="right"></td>
<td align="right">13,727,769</td>
<td align="right"></td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">29,481</td>
<td align="right">0.1%</td>
<td align="right">14,812</td>
<td align="right">0.1%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">105,037,345</td>
<td align="right">24.8%</td>
<td align="right">53,960,649</td>
<td align="right">25.5%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">92,548,716</td>
<td align="right">20.7%</td>
<td align="right">48,068,493</td>
<td align="right">21.5%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">142,318,323</td>
<td align="right">33.6%</td>
<td align="right">76,630,264</td>
<td align="right">36.3%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">142,971,411</td>
<td align="right">31.9%</td>
<td align="right">78,649,198</td>
<td align="right">35.2%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">65</td>
<td align="right">0.0%</td>
<td align="right">90</td>
<td align="right">0.0%</td>
<td align="right">38.5%</td>
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
<td align="right">651</td>
<td align="right">1,120,341</td>
<td align="right">12,432,331</td>
<td align="right">768,123</td>
<td align="right">1,243,928</td>
<td align="right">325</td>
<td align="right">558,537</td>
<td align="right">4,200,513</td>
<td align="right">103,817</td>
<td align="right">614,247</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">108</td>
<td align="right">5.1%</td>
<td align="right">10,700.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">70</td>
<td align="right">3.3%</td>
<td align="right">6,900.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">25</td>
<td align="right">1.2%</td>
<td align="right">2,400.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">217</td>
<td align="right">17.6%</td>
<td align="right">648</td>
<td align="right">30.7%</td>
<td align="right">198.6%</td>
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
<td align="right">1.7%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">513</td>
<td align="right">41.7%</td>
<td align="right">942</td>
<td align="right">44.6%</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,230</td>
<td align="right"></td>
<td align="right">2,112</td>
<td align="right"></td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">904,722,199</td>
<td align="right">14,064.0%</td>
<td align="right">547,691,525</td>
<td align="right">7,834.3%</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,432,880</td>
<td align="right"></td>
<td align="right">6,990,949</td>
<td align="right"></td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">499</td>
<td align="right">40.6%</td>
<td align="right">496</td>
<td align="right">23.5%</td>
<td align="right">-0.6%</td>
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

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1 / 0 !!</td>
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
<td align="right">433</td>
<td align="right">86.8%</td>
<td align="right">402</td>
<td align="right">81.0%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">499</td>
<td align="right"></td>
<td align="right">496</td>
<td align="right"></td>
<td align="right">-0.6%</td>
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
<td align="right">972,982</td>
<td align="right">18.2%</td>
<td align="right">790,777</td>
<td align="right">14.5%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">4,267,258</td>
<td align="right">79.7%</td>
<td align="right">4,567,639</td>
<td align="right">83.5%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">5,353,472</td>
<td align="right"></td>
<td align="right">5,472,256</td>
<td align="right"></td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">113,232</td>
<td align="right">2.1%</td>
<td align="right">113,840</td>
<td align="right">2.1%</td>
<td align="right">0.5%</td>
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
<td align="right">86,016</td>
<td align="right">1.6%</td>
<td align="right">86,016 / 0 !!</td>
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
<td align="left">127</td>
<td align="right">29.3%</td>
<td align="left">110</td>
<td align="right">27.4%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">109</td>
<td align="right">25.2%</td>
<td align="left">128</td>
<td align="right">31.8%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">132</td>
<td align="right">30.5%</td>
<td align="left">74</td>
<td align="right">18.4%</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">22</td>
<td align="right">5.1%</td>
<td align="left">65</td>
<td align="right">16.2%</td>
<td align="right">195.5%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">43</td>
<td align="right">9.9%</td>
<td align="left">25</td>
<td align="right">6.2%</td>
<td align="right">-41.9%</td>
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
<td align="left"><= 16</td>
<td align="right">42</td>
<td align="right">8.4%</td>
<td align="right">53</td>
<td align="right">10.7%</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">170</td>
<td align="right">34.1%</td>
<td align="right">13</td>
<td align="right">2.6%</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">108</td>
<td align="right">21.6%</td>
<td align="right">124</td>
<td align="right">25.0%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">69</td>
<td align="right">13.8%</td>
<td align="right">120</td>
<td align="right">24.2%</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">22</td>
<td align="right">4.4%</td>
<td align="right">87</td>
<td align="right">17.5%</td>
<td align="right">295.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">88</td>
<td align="right">17.6%</td>
<td align="right">26</td>
<td align="right">5.2%</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">52</td>
<td align="right">10.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21</td>
<td align="right">4.2%</td>
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
<td align="left"><= 16</td>
<td align="right">127</td>
<td align="right">25.5%</td>
<td align="right">57</td>
<td align="right">11.5%</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">170</td>
<td align="right">34.1%</td>
<td align="right">82</td>
<td align="right">16.5%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">69</td>
<td align="right">13.8%</td>
<td align="right">117</td>
<td align="right">23.6%</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">23</td>
<td align="right">4.6%</td>
<td align="right">67</td>
<td align="right">13.5%</td>
<td align="right">191.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">44</td>
<td align="right">8.8%</td>
<td align="right">5</td>
<td align="right">1.0%</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">50</td>
<td align="right">10.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21</td>
<td align="right">4.2%</td>
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
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">48</td>
<td align="right">30,926</td>
<td align="right">64,329.2%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">48</td>
<td align="right">29,041</td>
<td align="right">60,402.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">48</td>
<td align="right">29,041</td>
<td align="right">60,402.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">12,789</td>
<td align="right">194,589</td>
<td align="right">1,421.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">25,578</td>
<td align="right">205,789</td>
<td align="right">704.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">25,578</td>
<td align="right">197,494</td>
<td align="right">672.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">67,518</td>
<td align="right">488,560</td>
<td align="right">623.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">46,536</td>
<td align="right">246,843</td>
<td align="right">430.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">59,325</td>
<td align="right">261,726</td>
<td align="right">341.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">12,789</td>
<td align="right">29,121</td>
<td align="right">127.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">202,818</td>
<td align="right">358,862</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">202,818</td>
<td align="right">358,862</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">561,558</td>
<td align="right">282,681</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">561,558</td>
<td align="right">282,681</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">561,558</td>
<td align="right">282,681</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">561,558</td>
<td align="right">282,681</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">561,558</td>
<td align="right">282,827</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">103,031</td>
<td align="right">51,904</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">445,077</td>
<td align="right">224,469</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">445,077</td>
<td align="right">224,615</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">5,257,260</td>
<td align="right">2,679,288</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">1,572,323</td>
<td align="right">803,396</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">591,266</td>
<td align="right">312,211</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">470,655</td>
<td align="right">249,388</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">43,974</td>
<td align="right">64,330</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">4,306,528</td>
<td align="right">2,355,564</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,670,399</td>
<td align="right">2,568,161</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">3,111,382</td>
<td align="right">1,729,602</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,393,231</td>
<td align="right">2,475,684</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">65,447,307</td>
<td align="right">37,114,225</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">9,170,164</td>
<td align="right">5,223,873</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,342,008</td>
<td align="right">10,450,044</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">9,171,844</td>
<td align="right">5,226,098</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">9,171,844</td>
<td align="right">5,227,358</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">23,072,389</td>
<td align="right">13,151,069</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,585,922</td>
<td align="right">2,614,372</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">9,314,623</td>
<td align="right">5,310,599</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">9,762,700</td>
<td align="right">5,568,759</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">86,382,161</td>
<td align="right">49,344,919</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">26,181,698</td>
<td align="right">15,001,580</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">4,585,970</td>
<td align="right">2,642,090</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,825,640</td>
<td align="right">3,358,249</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">6,275,397</td>
<td align="right">3,620,030</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">7,961,440</td>
<td align="right">4,600,108</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">10,062,014</td>
<td align="right">5,852,316</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">449,757</td>
<td align="right">261,781</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">142,779</td>
<td align="right">83,105</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">14,501,224</td>
<td align="right">8,498,001</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">2,162,430</td>
<td align="right">1,269,246</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">15,415,569</td>
<td align="right">9,055,851</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">49,980</td>
<td align="right">70,560</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">49,980</td>
<td align="right">70,560</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">9,171,844</td>
<td align="right">5,398,527</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">489,051</td>
<td align="right">288,799</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">179,040,738</td>
<td align="right">105,768,793</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">5,199,356</td>
<td align="right">3,078,830</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">1,915,536</td>
<td align="right">1,143,890</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">9,271,077</td>
<td align="right">5,543,146</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">5,199,404</td>
<td align="right">3,109,756</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">5,199,404</td>
<td align="right">3,112,422</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">5,199,404</td>
<td align="right">3,112,422</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">5,199,404</td>
<td align="right">3,112,422</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">186,769,226</td>
<td align="right">112,198,763</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">3,262,402</td>
<td align="right">1,968,038</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,107,831</td>
<td align="right">670,877</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">10,457,688</td>
<td align="right">6,337,574</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">4,739,834</td>
<td align="right">2,905,479</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,120,839</td>
<td align="right">3,170,882</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">15,326,837</td>
<td align="right">9,492,809</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">4,046,711</td>
<td align="right">2,512,024</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">7,247,209</td>
<td align="right">4,568,978</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,578,582</td>
<td align="right">995,386</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">212,287</td>
<td align="right">136,971</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">212,287</td>
<td align="right">136,971</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">212,287</td>
<td align="right">136,971</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,825,784</td>
<td align="right">1,186,664</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">6,534,797</td>
<td align="right">4,251,245</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">168,357</td>
<td align="right">110,090</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">19,791,333</td>
<td align="right">13,171,959</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">162,477</td>
<td align="right">215,964</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,915,536</td>
<td align="right">1,316,392</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,017,772</td>
<td align="right">2,109,721</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">3,162,004</td>
<td align="right">2,278,254</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">568,114</td>
<td align="right">418,711</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">707,094</td>
<td align="right">530,832</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">613,434</td>
<td align="right">466,114</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">3,307,720</td>
<td align="right">2,528,043</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">580,903</td>
<td align="right">444,724</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">2,065,466</td>
<td align="right">1,633,038</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">11,690,140</td>
<td align="right">9,670,237</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">913,185</td>
<td align="right">776,159</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">296,226</td>
<td align="right">255,059</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,432,880</td>
<td align="right">6,990,949</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,432,880</td>
<td align="right">6,990,948</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">12,789</td>
<td align="right">12,460</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">861,202</td>
<td align="right">839,720</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">524,142</td>
<td align="right">512,783</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">434,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">173,772</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right"></td>
<td align="right">132,961</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right"></td>
<td align="right">64,349</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right"></td>
<td align="right">13,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">12,445</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">8,294</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right"></td>
<td align="right">4,151</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right"></td>
<td align="right">3,268</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">2,666</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">2,666</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">2,666</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">2,666</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right"></td>
<td align="right">2,666</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">2,666</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">1,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">1,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">1,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">1,910</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">1,522</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">1,406</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right"></td>
<td align="right">1,396</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right"></td>
<td align="right">1,396</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">1,333</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right"></td>
<td align="right">1,333</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right"></td>
<td align="right">1,333</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right"></td>
<td align="right">1,333</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">1,174</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">146</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">1</td>
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
<td align="right"></td>
<td align="right">64</td>
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
Stats gathered on: 2025-06-24
