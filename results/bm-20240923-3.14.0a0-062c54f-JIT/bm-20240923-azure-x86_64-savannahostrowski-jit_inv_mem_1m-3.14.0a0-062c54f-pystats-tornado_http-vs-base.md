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
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">35,980</td>
<td align="right">143,960</td>
<td align="right">300.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">483,900</td>
<td align="right">373,418</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">601,000</td>
<td align="right">540,400</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">330,260</td>
<td align="right">325,512</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">724,681</td>
<td align="right">715,922</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,431,801</td>
<td align="right">6,489,878</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">473,462</td>
<td align="right">477,318</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">30,516</td>
<td align="right">30,764</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">340,380</td>
<td align="right">337,870</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">621,042</td>
<td align="right">616,905</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">214,298</td>
<td align="right">212,917</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">53,097</td>
<td align="right">52,760</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">85,136</td>
<td align="right">84,620</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">860,670</td>
<td align="right">855,483</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">742,322</td>
<td align="right">738,185</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,868,415</td>
<td align="right">2,852,647</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">345,916</td>
<td align="right">347,720</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">57,230</td>
<td align="right">57,471</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,849,226</td>
<td align="right">1,842,592</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">40,380</td>
<td align="right">40,523</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">847,758</td>
<td align="right">844,877</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">183,982</td>
<td align="right">183,370</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,080,472</td>
<td align="right">3,070,294</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">154,658</td>
<td align="right">155,167</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">177,100</td>
<td align="right">176,565</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">672,799</td>
<td align="right">670,851</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">190,298</td>
<td align="right">190,807</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">449,180</td>
<td align="right">450,289</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,708,701</td>
<td align="right">2,702,120</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">939,619</td>
<td align="right">937,544</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">852,772</td>
<td align="right">851,004</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">894,001</td>
<td align="right">892,177</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">459,016</td>
<td align="right">459,924</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">459,136</td>
<td align="right">460,044</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">202,357</td>
<td align="right">202,729</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,628,804</td>
<td align="right">2,633,349</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">367,423</td>
<td align="right">368,007</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">9,746,547</td>
<td align="right">9,733,368</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">425,082</td>
<td align="right">424,560</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,243,912</td>
<td align="right">14,226,743</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">691,160</td>
<td align="right">691,954</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,070,319</td>
<td align="right">1,071,492</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,962,317</td>
<td align="right">1,964,465</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,209,051</td>
<td align="right">1,207,793</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">12,585,568</td>
<td align="right">12,572,979</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,603,982</td>
<td align="right">6,597,388</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,085,256</td>
<td align="right">1,086,307</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">160,883</td>
<td align="right">161,038</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">259,536</td>
<td align="right">259,784</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">647,802</td>
<td align="right">648,396</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">204,711</td>
<td align="right">204,889</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,658,416</td>
<td align="right">3,661,397</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">65,638,340</td>
<td align="right">65,586,937</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,288,465</td>
<td align="right">2,286,789</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,986,814</td>
<td align="right">1,988,269</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">3,969,520</td>
<td align="right">3,972,212</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">12,034</td>
<td align="right">12,027</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">305,968</td>
<td align="right">306,140</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,606,067</td>
<td align="right">1,605,181</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">5,212,656</td>
<td align="right">5,215,520</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">656,563</td>
<td align="right">656,923</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">268,780</td>
<td align="right">268,923</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,922,460</td>
<td align="right">8,917,756</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">23,197,581</td>
<td align="right">23,185,836</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">7,732,372</td>
<td align="right">7,728,541</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">91,936</td>
<td align="right">91,979</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,113,744</td>
<td align="right">10,109,515</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">121,282</td>
<td align="right">121,332</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,843,591</td>
<td align="right">8,839,948</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">378,163</td>
<td align="right">378,318</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">17,363,734</td>
<td align="right">17,370,769</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">935,896</td>
<td align="right">936,235</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">220,922</td>
<td align="right">220,842</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">904,402</td>
<td align="right">904,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">530,126</td>
<td align="right">530,312</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">9,951,692</td>
<td align="right">9,948,223</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,781,205</td>
<td align="right">2,780,338</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">769,737</td>
<td align="right">769,956</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,128,962</td>
<td align="right">9,126,477</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">11,378,769</td>
<td align="right">11,376,027</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,015,440</td>
<td align="right">3,016,137</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,332,110</td>
<td align="right">1,332,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">7,581,092</td>
<td align="right">7,582,571</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,597,909</td>
<td align="right">3,598,510</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">4,825,108</td>
<td align="right">4,825,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">850,286</td>
<td align="right">850,408</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,130,786</td>
<td align="right">3,130,402</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,873,057</td>
<td align="right">1,872,976</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">327,004</td>
<td align="right">327,000</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">747,217</td>
<td align="right">747,215</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,654,260</td>
<td align="right">1,654,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">794,260</td>
<td align="right">794,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">675,720</td>
<td align="right">675,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">576,300</td>
<td align="right">576,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">565,160</td>
<td align="right">565,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">469,140</td>
<td align="right">469,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">456,000</td>
<td align="right">456,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">444,000</td>
<td align="right">444,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">399,040</td>
<td align="right">399,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">338,220</td>
<td align="right">338,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">336,820</td>
<td align="right">336,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">336,300</td>
<td align="right">336,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">325,080</td>
<td align="right">325,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">299,960</td>
<td align="right">299,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">287,940</td>
<td align="right">287,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">287,800</td>
<td align="right">287,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">277,980</td>
<td align="right">277,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">252,780</td>
<td align="right">252,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">228,620</td>
<td align="right">228,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">204,420</td>
<td align="right">204,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">191,580</td>
<td align="right">191,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">183,320</td>
<td align="right">183,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">169,320</td>
<td align="right">169,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">145,540</td>
<td align="right">145,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">121,520</td>
<td align="right">121,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">120,460</td>
<td align="right">120,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">119,980</td>
<td align="right">119,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">116,820</td>
<td align="right">116,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">108,960</td>
<td align="right">108,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">100,580</td>
<td align="right">100,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,780</td>
<td align="right">93,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">76,280</td>
<td align="right">76,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">73,200</td>
<td align="right">73,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">72,060</td>
<td align="right">72,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">72,020</td>
<td align="right">72,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">61,120</td>
<td align="right">61,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">60,580</td>
<td align="right">60,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">60,320</td>
<td align="right">60,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">60,320</td>
<td align="right">60,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">60,180</td>
<td align="right">60,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">59,980</td>
<td align="right">59,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">54,720</td>
<td align="right">54,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">48,300</td>
<td align="right">48,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">35,260</td>
<td align="right">35,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">28,780</td>
<td align="right">28,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">24,160</td>
<td align="right">24,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">24,120</td>
<td align="right">24,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">24,060</td>
<td align="right">24,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">17,140</td>
<td align="right">17,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">16,160</td>
<td align="right">16,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">13,980</td>
<td align="right">13,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">13,000</td>
<td align="right">13,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">12,140</td>
<td align="right">12,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">12,080</td>
<td align="right">12,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">12,020</td>
<td align="right">12,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">9,440</td>
<td align="right">9,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">5,940</td>
<td align="right">5,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">3,540</td>
<td align="right">3,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,320</td>
<td align="right">1,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,300</td>
<td align="right">1,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,140</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">100</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
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
<td align="right">896,099</td>
<td align="right">27.0%</td>
<td align="right">896,423</td>
<td align="right">27.0%</td>
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
<td align="right">2,415,156</td>
<td align="right">72.8%</td>
<td align="right">2,415,612</td>
<td align="right">72.8%</td>
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
<td align="right">7,343</td>
<td align="right">88.4%</td>
<td align="right">7,337</td>
<td align="right">88.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">960</td>
<td align="right">11.6%</td>
<td align="right">960</td>
<td align="right">11.6%</td>
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
<td align="right">24</td>
<td align="right">0.3%</td>
<td align="right">23</td>
<td align="right">0.3%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">442</td>
<td align="right">6.0%</td>
<td align="right">432</td>
<td align="right">5.9%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,375</td>
<td align="right">46.0%</td>
<td align="right">3,379</td>
<td align="right">46.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,222</td>
<td align="right">16.6%</td>
<td align="right">1,223</td>
<td align="right">16.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,120</td>
<td align="right">15.3%</td>
<td align="right">1,120</td>
<td align="right">15.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">880</td>
<td align="right">12.0%</td>
<td align="right">880</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">180</td>
<td align="right">2.5%</td>
<td align="right">180</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">100</td>
<td align="right">1.4%</td>
<td align="right">100</td>
<td align="right">1.4%</td>
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
<td align="right">340,380</td>
<td align="right">100.0%</td>
<td align="right">337,870</td>
<td align="right">100.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">326,740</td>
<td align="right">15.7%</td>
<td align="right">321,996</td>
<td align="right">15.5%</td>
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
<td align="right">1,788</td>
<td align="right">0.1%</td>
<td align="right">1,780</td>
<td align="right">0.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,743,746</td>
<td align="right">84.0%</td>
<td align="right">1,744,154</td>
<td align="right">84.2%</td>
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
<td align="right">2,560</td>
<td align="right">72.3%</td>
<td align="right">2,556</td>
<td align="right">72.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">980</td>
<td align="right">27.7%</td>
<td align="right">980</td>
<td align="right">27.7%</td>
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
<td align="right">2,400</td>
<td align="right">93.8%</td>
<td align="right">2,396</td>
<td align="right">93.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">160</td>
<td align="right">6.2%</td>
<td align="right">160</td>
<td align="right">6.3%</td>
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
<td align="right">260,078</td>
<td align="right">1.1%</td>
<td align="right">261,978</td>
<td align="right">1.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,525,507</td>
<td align="right">98.7%</td>
<td align="right">23,527,636</td>
<td align="right">98.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">34,000</td>
<td align="right">0.1%</td>
<td align="right">34,000</td>
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
<td align="right">26,082</td>
<td align="right">99.4%</td>
<td align="right">26,117</td>
<td align="right">99.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">160</td>
<td align="right">0.6%</td>
<td align="right">160</td>
<td align="right">0.6%</td>
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
<td align="left">out of versions</td>
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">80</td>
<td align="right">50.0%</td>
<td align="right">80</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">20</td>
<td align="right">12.5%</td>
<td align="right">20</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">20</td>
<td align="right">12.5%</td>
<td align="right">20</td>
<td align="right">12.5%</td>
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
<td align="right">820</td>
<td align="right">52.6%</td>
<td align="right">820</td>
<td align="right">52.6%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">214</td>
<td align="right">0.0%</td>
<td align="right">207</td>
<td align="right">0.0%</td>
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
<td align="right">173,430</td>
<td align="right">4.0%</td>
<td align="right">172,907</td>
<td align="right">4.0%</td>
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
<td align="right">4,158,489</td>
<td align="right">95.9%</td>
<td align="right">4,159,409</td>
<td align="right">95.9%</td>
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
<td align="right">1,770</td>
<td align="right">48.2%</td>
<td align="right">1,758</td>
<td align="right">48.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,900</td>
<td align="right">51.8%</td>
<td align="right">1,900</td>
<td align="right">51.9%</td>
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
<td align="right">150</td>
<td align="right">8.5%</td>
<td align="right">138</td>
<td align="right">7.8%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">480</td>
<td align="right">27.1%</td>
<td align="right">480</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">360</td>
<td align="right">20.3%</td>
<td align="right">360</td>
<td align="right">20.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">340</td>
<td align="right">19.2%</td>
<td align="right">340</td>
<td align="right">19.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">180</td>
<td align="right">10.2%</td>
<td align="right">180</td>
<td align="right">10.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">160</td>
<td align="right">9.0%</td>
<td align="right">160</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">60</td>
<td align="right">3.4%</td>
<td align="right">60</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">40</td>
<td align="right">2.3%</td>
<td align="right">40</td>
<td align="right">2.3%</td>
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
<td align="right">394,560</td>
<td align="right">58.2%</td>
<td align="right">394,560</td>
<td align="right">58.2%</td>
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
<td align="right">278,660</td>
<td align="right">41.1%</td>
<td align="right">278,660</td>
<td align="right">41.1%</td>
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
<td align="right">400</td>
<td align="right">8.9%</td>
<td align="right">400</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,080</td>
<td align="right">91.1%</td>
<td align="right">4,080</td>
<td align="right">91.1%</td>
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
<td align="right">2,380</td>
<td align="right">58.3%</td>
<td align="right">2,380</td>
<td align="right">58.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,200</td>
<td align="right">29.4%</td>
<td align="right">1,200</td>
<td align="right">29.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">440</td>
<td align="right">10.8%</td>
<td align="right">440</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">60</td>
<td align="right">1.5%</td>
<td align="right">60</td>
<td align="right">1.5%</td>
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
<td align="right">201,378</td>
<td align="right">22.9%</td>
<td align="right">201,552</td>
<td align="right">22.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">673,544</td>
<td align="right">76.7%</td>
<td align="right">673,964</td>
<td align="right">76.7%</td>
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
<td align="left">Failure</td>
<td align="right">2,333</td>
<td align="right">70.0%</td>
<td align="right">2,337</td>
<td align="right">70.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,000</td>
<td align="right">30.0%</td>
<td align="right">1,000</td>
<td align="right">30.0%</td>
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
<td align="left">bytes</td>
<td align="right">113</td>
<td align="right">4.8%</td>
<td align="right">117</td>
<td align="right">5.0%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,280</td>
<td align="right">54.9%</td>
<td align="right">1,280</td>
<td align="right">54.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">280</td>
<td align="right">12.0%</td>
<td align="right">280</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">200</td>
<td align="right">8.6%</td>
<td align="right">200</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">7.7%</td>
<td align="right">180</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">160</td>
<td align="right">6.9%</td>
<td align="right">160</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">120</td>
<td align="right">5.1%</td>
<td align="right">120</td>
<td align="right">5.1%</td>
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
<td align="right">610,906</td>
<td align="right">1.1%</td>
<td align="right">504,616</td>
<td align="right">0.9%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">52,591,047</td>
<td align="right">93.9%</td>
<td align="right">52,708,623</td>
<td align="right">94.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,718,699</td>
<td align="right">4.9%</td>
<td align="right">2,717,824</td>
<td align="right">4.9%</td>
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
<td align="right">54,305</td>
<td align="right">73.6%</td>
<td align="right">52,320</td>
<td align="right">72.8%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">19,506</td>
<td align="right">26.4%</td>
<td align="right">19,514</td>
<td align="right">27.2%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">7,266</td>
<td align="right">37.3%</td>
<td align="right">7,275</td>
<td align="right">37.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,280</td>
<td align="right">6.6%</td>
<td align="right">1,279</td>
<td align="right">6.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">8,020</td>
<td align="right">41.1%</td>
<td align="right">8,020</td>
<td align="right">41.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">1,220</td>
<td align="right">6.3%</td>
<td align="right">1,220</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">460</td>
<td align="right">2.4%</td>
<td align="right">460</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">380</td>
<td align="right">1.9%</td>
<td align="right">380</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">160</td>
<td align="right">0.8%</td>
<td align="right">160</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">160</td>
<td align="right">0.8%</td>
<td align="right">160</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
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
<td align="right">16,552,914</td>
<td align="right">99.8%</td>
<td align="right">16,542,851</td>
<td align="right">99.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,760</td>
<td align="right">0.1%</td>
<td align="right">14,760</td>
<td align="right">0.1%</td>
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
<td align="right">760</td>
<td align="right">0.0%</td>
<td align="right">760</td>
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
<td align="right">2,760</td>
<td align="right">0.0%</td>
<td align="right">2,760</td>
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
<td align="right">14,040</td>
<td align="right">100.0%</td>
<td align="right">14,040</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">460</td>
<td align="right">0.1%</td>
<td align="right">460</td>
<td align="right">0.1%</td>
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
<td align="right">311,560</td>
<td align="right">99.7%</td>
<td align="right">311,560</td>
<td align="right">99.7%</td>
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
<td align="right">360</td>
<td align="right">100.0%</td>
<td align="right">360</td>
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
<td align="right">336,200</td>
<td align="right">53.7%</td>
<td align="right">336,200</td>
<td align="right">53.7%</td>
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
<td align="right">287,800</td>
<td align="right">46.0%</td>
<td align="right">287,800</td>
<td align="right">46.0%</td>
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
<td align="right">200</td>
<td align="right">9.9%</td>
<td align="right">200</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,820</td>
<td align="right">90.1%</td>
<td align="right">1,820</td>
<td align="right">90.1%</td>
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
<td align="right">1,820</td>
<td align="right">100.0%</td>
<td align="right">1,820</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">585,460</td>
<td align="right">4.8%</td>
<td align="right">525,560</td>
<td align="right">4.3%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">691,940</td>
<td align="right">5.7%</td>
<td align="right">699,393</td>
<td align="right">5.7%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,917,355</td>
<td align="right">89.4%</td>
<td align="right">10,972,156</td>
<td align="right">89.8%</td>
<td align="right">0.5%</td>
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
<td align="right">8,020</td>
<td align="right">28.2%</td>
<td align="right">7,220</td>
<td align="right">25.9%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20,451</td>
<td align="right">71.8%</td>
<td align="right">20,689</td>
<td align="right">74.1%</td>
<td align="right">1.2%</td>
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
<td align="left">not in keys</td>
<td align="right">100</td>
<td align="right">1.2%</td>
<td align="right">260</td>
<td align="right">3.6%</td>
<td align="right">160.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,960</td>
<td align="right">61.8%</td>
<td align="right">4,000</td>
<td align="right">55.4%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,660</td>
<td align="right">20.7%</td>
<td align="right">1,660</td>
<td align="right">23.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">480</td>
<td align="right">6.0%</td>
<td align="right">480</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">480</td>
<td align="right">6.0%</td>
<td align="right">480</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">240</td>
<td align="right">3.0%</td>
<td align="right">240</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">100</td>
<td align="right">1.2%</td>
<td align="right">100</td>
<td align="right">1.4%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">91,880</td>
<td align="right">13.9%</td>
<td align="right">91,880</td>
<td align="right">13.9%</td>
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
<td align="right">565,400</td>
<td align="right">85.8%</td>
<td align="right">565,400</td>
<td align="right">85.8%</td>
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
<td align="right">380</td>
<td align="right">20.0%</td>
<td align="right">380</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,520</td>
<td align="right">80.0%</td>
<td align="right">1,520</td>
<td align="right">80.0%</td>
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
<td align="right">1,200</td>
<td align="right">78.9%</td>
<td align="right">1,200</td>
<td align="right">78.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">320</td>
<td align="right">21.1%</td>
<td align="right">320</td>
<td align="right">21.1%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">882,092</td>
<td align="right">6.5%</td>
<td align="right">880,267</td>
<td align="right">6.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">15,304</td>
<td align="right">0.1%</td>
<td align="right">15,324</td>
<td align="right">0.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,571,118</td>
<td align="right">93.3%</td>
<td align="right">12,573,596</td>
<td align="right">93.3%</td>
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
<td align="right">7,546</td>
<td align="right">62.0%</td>
<td align="right">7,548</td>
<td align="right">62.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,629</td>
<td align="right">38.0%</td>
<td align="right">4,630</td>
<td align="right">38.0%</td>
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
<td align="left">bytes</td>
<td align="right">623</td>
<td align="right">13.5%</td>
<td align="right">625</td>
<td align="right">13.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">501</td>
<td align="right">10.8%</td>
<td align="right">500</td>
<td align="right">10.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,205</td>
<td align="right">26.0%</td>
<td align="right">1,205</td>
<td align="right">26.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">960</td>
<td align="right">20.7%</td>
<td align="right">960</td>
<td align="right">20.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">620</td>
<td align="right">13.4%</td>
<td align="right">620</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">380</td>
<td align="right">8.2%</td>
<td align="right">380</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">340</td>
<td align="right">7.3%</td>
<td align="right">340</td>
<td align="right">7.3%</td>
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
<td align="right">1,168,988</td>
<td align="right">98.8%</td>
<td align="right">1,170,383</td>
<td align="right">98.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,920</td>
<td align="right">1.1%</td>
<td align="right">12,920</td>
<td align="right">1.1%</td>
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
<td align="right">900</td>
<td align="right">84.9%</td>
<td align="right">900</td>
<td align="right">84.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">160</td>
<td align="right">15.1%</td>
<td align="right">160</td>
<td align="right">15.1%</td>
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
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">160</td>
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
<td align="right">1,583,075</td>
<td align="right">0.5%</td>
<td align="right">1,486,134</td>
<td align="right">0.5%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">7,163,959</td>
<td align="right">2.2%</td>
<td align="right">7,093,371</td>
<td align="right">2.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">129,848,117</td>
<td align="right">40.4%</td>
<td align="right">129,950,725</td>
<td align="right">40.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">182,709,209</td>
<td align="right">56.9%</td>
<td align="right">182,588,116</td>
<td align="right">56.9%</td>
<td align="right">-0.1%</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">585,460</td>
<td align="right">8.4%</td>
<td align="right">525,560</td>
<td align="right">7.6%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">326,740</td>
<td align="right">4.7%</td>
<td align="right">321,996</td>
<td align="right">4.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">340,380</td>
<td align="right">4.9%</td>
<td align="right">337,870</td>
<td align="right">4.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">173,430</td>
<td align="right">2.5%</td>
<td align="right">172,907</td>
<td align="right">2.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">882,092</td>
<td align="right">12.6%</td>
<td align="right">880,267</td>
<td align="right">12.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">201,378</td>
<td align="right">2.9%</td>
<td align="right">201,552</td>
<td align="right">2.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">896,099</td>
<td align="right">12.8%</td>
<td align="right">896,423</td>
<td align="right">12.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,718,699</td>
<td align="right">38.8%</td>
<td align="right">2,717,824</td>
<td align="right">39.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">394,560</td>
<td align="right">5.6%</td>
<td align="right">394,560</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">336,200</td>
<td align="right">4.8%</td>
<td align="right">336,200</td>
<td align="right">4.8%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">30,897</td>
<td align="right">2.0%</td>
<td align="right">34,303</td>
<td align="right">2.3%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">26,135</td>
<td align="right">1.7%</td>
<td align="right">26,690</td>
<td align="right">1.8%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">65,495</td>
<td align="right">4.1%</td>
<td align="right">66,594</td>
<td align="right">4.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">691,920</td>
<td align="right">43.7%</td>
<td align="right">699,373</td>
<td align="right">47.1%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">42,788</td>
<td align="right">2.7%</td>
<td align="right">43,049</td>
<td align="right">2.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">283,551</td>
<td align="right">17.9%</td>
<td align="right">284,916</td>
<td align="right">19.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">125,892</td>
<td align="right">8.0%</td>
<td align="right">125,651</td>
<td align="right">8.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">124,894</td>
<td align="right">7.9%</td>
<td align="right">125,092</td>
<td align="right">8.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">110,040</td>
<td align="right">7.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">36,880</td>
<td align="right">2.3%</td>
<td align="right">36,880</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">15,857</td>
<td align="right">1.1%</td>
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
<td align="right">1,088,122</td>
<td align="right">5.3%</td>
<td align="right">1,089,868</td>
<td align="right">5.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">751,412</td>
<td align="right">3.7%</td>
<td align="right">752,009</td>
<td align="right">3.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,877,360</td>
<td align="right">23.9%</td>
<td align="right">4,880,220</td>
<td align="right">24.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,877,740</td>
<td align="right">23.9%</td>
<td align="right">4,880,600</td>
<td align="right">24.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">5,226,440</td>
<td align="right">25.7%</td>
<td align="right">5,229,300</td>
<td align="right">25.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">5,226,440</td>
<td align="right">25.7%</td>
<td align="right">5,229,300</td>
<td align="right">25.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">19,794,735</td>
<td align="right">97.2%</td>
<td align="right">19,800,401</td>
<td align="right">97.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">15,144,115</td>
<td align="right">74.3%</td>
<td align="right">15,146,921</td>
<td align="right">74.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">879,780</td>
<td align="right">4.3%</td>
<td align="right">879,923</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">348,700</td>
<td align="right">1.7%</td>
<td align="right">348,700</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">132,540</td>
<td align="right">0.7%</td>
<td align="right">132,540</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">169,480</td>
<td align="right">0.8%</td>
<td align="right">169,480</td>
<td align="right">0.8%</td>
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
<td align="right">18,089</td>
<td align="right"></td>
<td align="right">22,369</td>
<td align="right"></td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">445,965</td>
<td align="right"></td>
<td align="right">456,163</td>
<td align="right"></td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,850,478</td>
<td align="right"></td>
<td align="right">7,683,338</td>
<td align="right"></td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">432,331</td>
<td align="right"></td>
<td align="right">438,532</td>
<td align="right"></td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">81,619,226</td>
<td align="right">81,619,226 / 0 !!</td>
<td align="right">81,478,378</td>
<td align="right">81,478,378 / 0 !!</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,935,607</td>
<td align="right">56.8%</td>
<td align="right">15,917,129</td>
<td align="right">56.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,249,181</td>
<td align="right">57.9%</td>
<td align="right">16,230,966</td>
<td align="right">57.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,498,447</td>
<td align="right"></td>
<td align="right">16,480,100</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">233,263</td>
<td align="right">0.8%</td>
<td align="right">233,507</td>
<td align="right">0.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">89,383,885</td>
<td align="right">89,383,885 / 0 !!</td>
<td align="right">89,339,124</td>
<td align="right">89,339,124 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">6,638,087</td>
<td align="right"></td>
<td align="right">6,640,520</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">161,363,604</td>
<td align="right">161,363,604 / 0 !!</td>
<td align="right">161,416,826</td>
<td align="right">161,416,826 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">80,311</td>
<td align="right">0.3%</td>
<td align="right">80,330</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">179,436,216</td>
<td align="right">179,436,216 / 0 !!</td>
<td align="right">179,400,100</td>
<td align="right">179,400,100 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,884,597</td>
<td align="right"></td>
<td align="right">11,886,473</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,831,068</td>
<td align="right">42.1%</td>
<td align="right">11,832,911</td>
<td align="right">42.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,059,040</td>
<td align="right"></td>
<td align="right">1,059,040</td>
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
<td align="right">12,000</td>
<td align="right">1.1%</td>
<td align="right">12,000</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
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
<td align="right">200</td>
<td align="right">1,920</td>
<td align="right">4,378,782</td>
<td align="right">200</td>
<td align="right">1,920</td>
<td align="right">4,384,148</td>
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
<td align="right">128,766,790</td>
<td align="right">3,070.1%</td>
<td align="right">133,643,837</td>
<td align="right">3,190.5%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">274</td>
<td align="right">5.6%</td>
<td align="right">270</td>
<td align="right">5.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">3,008</td>
<td align="right">61.6%</td>
<td align="right">2,966</td>
<td align="right">61.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">2,606</td>
<td align="right">53.3%</td>
<td align="right">2,581</td>
<td align="right">53.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">4,886</td>
<td align="right"></td>
<td align="right">4,848</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,280</td>
<td align="right">46.7%</td>
<td align="right">2,267</td>
<td align="right">46.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">4,194,155</td>
<td align="right"></td>
<td align="right">4,188,833</td>
<td align="right"></td>
<td align="right">-0.1%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">20</td>
<td align="right">0.4%</td>
<td align="right">20</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="right">2,280</td>
<td align="right"></td>
<td align="right">2,267</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">2,280</td>
<td align="right">100.0%</td>
<td align="right">2,267</td>
<td align="right">100.0%</td>
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
<td align="right">48</td>
<td align="right">2.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">420</td>
<td align="right">18.4%</td>
<td align="right">414</td>
<td align="right">18.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">267</td>
<td align="right">11.7%</td>
<td align="right">248</td>
<td align="right">10.9%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">550</td>
<td align="right">24.1%</td>
<td align="right">511</td>
<td align="right">22.5%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">515</td>
<td align="right">22.6%</td>
<td align="right">557</td>
<td align="right">24.6%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">280</td>
<td align="right">12.3%</td>
<td align="right">334</td>
<td align="right">14.7%</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">120</td>
<td align="right">5.3%</td>
<td align="right">125</td>
<td align="right">5.5%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">80</td>
<td align="right">3.5%</td>
<td align="right">78</td>
<td align="right">3.4%</td>
<td align="right">-2.5%</td>
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
<td align="right">388</td>
<td align="right">17.0%</td>
<td align="right">235</td>
<td align="right">10.4%</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">180</td>
<td align="right">7.9%</td>
<td align="right">339</td>
<td align="right">15.0%</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">242</td>
<td align="right">10.6%</td>
<td align="right">222</td>
<td align="right">9.8%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">831</td>
<td align="right">36.4%</td>
<td align="right">764</td>
<td align="right">33.7%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">339</td>
<td align="right">14.9%</td>
<td align="right">383</td>
<td align="right">16.9%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">7.9%</td>
<td align="right">205</td>
<td align="right">9.0%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">80</td>
<td align="right">3.5%</td>
<td align="right">80</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">40</td>
<td align="right">1.8%</td>
<td align="right">39</td>
<td align="right">1.7%</td>
<td align="right">-2.5%</td>
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
<td align="left">_MAKE_FUNCTION</td>
<td align="right">40</td>
<td align="right">482</td>
<td align="right">1,105.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">6,374</td>
<td align="right">3,536</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">286,057</td>
<td align="right">307,436</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">140,705</td>
<td align="right">149,884</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">82,460</td>
<td align="right">87,204</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">116,800</td>
<td align="right">122,022</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">9,980</td>
<td align="right">10,422</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">188,336</td>
<td align="right">194,459</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">23,622</td>
<td align="right">24,317</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">658,833</td>
<td align="right">673,683</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">394,058</td>
<td align="right">402,709</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">188,600</td>
<td align="right">192,347</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">277,318</td>
<td align="right">282,146</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,462,466</td>
<td align="right">1,487,546</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">343,606</td>
<td align="right">349,138</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">479,677</td>
<td align="right">472,488</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">242,460</td>
<td align="right">245,850</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">311,167</td>
<td align="right">315,428</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">508,100</td>
<td align="right">514,831</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">189,960</td>
<td align="right">192,470</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">186,601</td>
<td align="right">189,028</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">327,542</td>
<td align="right">331,727</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">306,719</td>
<td align="right">310,554</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">580,783</td>
<td align="right">573,617</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">521,336</td>
<td align="right">527,653</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,048,689</td>
<td align="right">1,060,113</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">121,430</td>
<td align="right">122,722</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">211,437</td>
<td align="right">213,578</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">23,945</td>
<td align="right">24,186</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">53,462</td>
<td align="right">54,000</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">2,564,495</td>
<td align="right">2,590,153</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">410,315</td>
<td align="right">414,277</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,697,960</td>
<td align="right">2,723,044</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">255,744</td>
<td align="right">258,058</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">500,989</td>
<td align="right">505,055</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,256,207</td>
<td align="right">1,246,701</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">187,417</td>
<td align="right">188,774</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">201,129</td>
<td align="right">202,563</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">303,000</td>
<td align="right">305,042</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">313,192</td>
<td align="right">315,266</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,329,614</td>
<td align="right">1,338,129</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">78,283</td>
<td align="right">78,769</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">463,765</td>
<td align="right">466,592</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">541,131</td>
<td align="right">544,397</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">270,604</td>
<td align="right">272,185</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,404,834</td>
<td align="right">1,412,971</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">446,500</td>
<td align="right">449,018</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,100,779</td>
<td align="right">1,106,618</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">55,936</td>
<td align="right">56,218</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">543,206</td>
<td align="right">545,852</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">478,519</td>
<td align="right">480,791</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,410,542</td>
<td align="right">2,421,232</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">289,343</td>
<td align="right">290,621</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">935,002</td>
<td align="right">930,880</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">935,002</td>
<td align="right">930,880</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">210,049</td>
<td align="right">210,939</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,340,885</td>
<td align="right">1,346,434</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,720,148</td>
<td align="right">1,727,058</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,485,499</td>
<td align="right">1,491,238</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,834,925</td>
<td align="right">1,841,680</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">7,339</td>
<td align="right">7,366</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">7,339</td>
<td align="right">7,366</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">42,397</td>
<td align="right">42,242</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">42,397</td>
<td align="right">42,242</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">86,754</td>
<td align="right">86,444</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,544,578</td>
<td align="right">7,517,911</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,914,645</td>
<td align="right">1,921,400</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">44,477</td>
<td align="right">44,322</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">4,278,272</td>
<td align="right">4,291,979</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">4,278,272</td>
<td align="right">4,291,979</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,314,826</td>
<td align="right">2,321,982</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,314,826</td>
<td align="right">2,321,982</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,184,142</td>
<td align="right">2,190,742</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,301,656</td>
<td align="right">1,305,541</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,304,846</td>
<td align="right">2,311,560</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">163,951</td>
<td align="right">163,486</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,167,999</td>
<td align="right">1,171,053</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">56,420</td>
<td align="right">56,277</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">10,326,949</td>
<td align="right">10,352,183</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">65,237</td>
<td align="right">65,082</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,076,844</td>
<td align="right">2,081,235</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">89,462</td>
<td align="right">89,650</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">8,144,017</td>
<td align="right">8,161,005</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">9,064,547</td>
<td align="right">9,082,879</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">1,526,123</td>
<td align="right">1,529,161</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,526,123</td>
<td align="right">1,529,161</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">789,648</td>
<td align="right">788,111</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">233,000</td>
<td align="right">233,442</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">115,537</td>
<td align="right">115,335</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">481,768</td>
<td align="right">482,601</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">535,047</td>
<td align="right">535,961</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,684,721</td>
<td align="right">1,687,460</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">895,812</td>
<td align="right">894,363</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">707,479</td>
<td align="right">708,549</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">707,519</td>
<td align="right">708,589</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">377,858</td>
<td align="right">378,400</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">377,858</td>
<td align="right">378,400</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,017,891</td>
<td align="right">1,016,509</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">114,777</td>
<td align="right">114,622</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,380,765</td>
<td align="right">3,376,285</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,194,155</td>
<td align="right">4,188,833</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">387,474</td>
<td align="right">387,944</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">462,518</td>
<td align="right">463,060</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">462,518</td>
<td align="right">463,060</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">435,476</td>
<td align="right">435,968</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">38,570</td>
<td align="right">38,531</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,693,989</td>
<td align="right">1,692,405</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">50,510</td>
<td align="right">50,471</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">181,696</td>
<td align="right">181,560</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">278,077</td>
<td align="right">277,922</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">261,421</td>
<td align="right">261,291</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,482,182</td>
<td align="right">2,483,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">10,203</td>
<td align="right">10,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">10,203</td>
<td align="right">10,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">354,742</td>
<td align="right">354,802</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">133,397</td>
<td align="right">133,376</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">101,204</td>
<td align="right">101,206</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">4,951,580</td>
<td align="right">4,951,563</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">529,440</td>
<td align="right">529,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">243,820</td>
<td align="right">243,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">215,360</td>
<td align="right">215,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">174,000</td>
<td align="right">174,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">148,900</td>
<td align="right">148,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">105,320</td>
<td align="right">105,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">103,800</td>
<td align="right">103,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">62,220</td>
<td align="right">62,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">62,220</td>
<td align="right">62,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">59,680</td>
<td align="right">59,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">59,680</td>
<td align="right">59,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">58,560</td>
<td align="right">58,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">58,400</td>
<td align="right">58,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">58,400</td>
<td align="right">58,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">49,380</td>
<td align="right">49,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">48,700</td>
<td align="right">48,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">20,040</td>
<td align="right">20,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">11,740</td>
<td align="right">11,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">11,740</td>
<td align="right">11,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">10,700</td>
<td align="right">10,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">10,460</td>
<td align="right">10,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,380</td>
<td align="right">10,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">8,100</td>
<td align="right">8,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,060</td>
<td align="right">1,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">640</td>
<td align="right">640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">520</td>
<td align="right">520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">380</td>
<td align="right">380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">220</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right"></td>
<td align="right">4,499,387</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">1,890</td>
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
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
