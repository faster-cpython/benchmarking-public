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
<td align="left">DELETE_NAME</td>
<td align="right">25</td>
<td align="right">725</td>
<td align="right">2,800.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">56,999</td>
<td align="right">1,553,607</td>
<td align="right">2,625.7%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">176</td>
<td align="right">3,696</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,355</td>
<td align="right">92,080</td>
<td align="right">1,619.5%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,864</td>
<td align="right">50,315</td>
<td align="right">1,202.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,690</td>
<td align="right">324,222</td>
<td align="right">862.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,628</td>
<td align="right">106,194</td>
<td align="right">740.9%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,550</td>
<td align="right">23,410</td>
<td align="right">559.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">243,192</td>
<td align="right">1,577,826</td>
<td align="right">548.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,513</td>
<td align="right">14,157</td>
<td align="right">463.4%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,072</td>
<td align="right">5,959</td>
<td align="right">455.9%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">14,816</td>
<td align="right">24,160</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">214,351</td>
<td align="right">333,538</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,970</td>
<td align="right">74,319</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,749,762</td>
<td align="right">2,332,004</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">463,971</td>
<td align="right">582,117</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,646</td>
<td align="right">12,021,399</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,577</td>
<td align="right">120,759</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,776</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">76,781</td>
<td align="right">87,161</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">10,549,274</td>
<td align="right">11,838,586</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,122,138</td>
<td align="right">3,463,430</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,784,349</td>
<td align="right">4,130,887</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,097,200</td>
<td align="right">10,782,834</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,705,220</td>
<td align="right">13,525,234</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">65,686,399</td>
<td align="right">69,577,983</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">75,637,654</td>
<td align="right">80,094,332</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,756,294</td>
<td align="right">15,620,407</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">325,993,684</td>
<td align="right">344,883,500</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">61,064,708</td>
<td align="right">64,101,034</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">66,606,613</td>
<td align="right">69,264,622</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">80,980,812</td>
<td align="right">84,084,997</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">66,481,431</td>
<td align="right">68,996,271</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,431,257</td>
<td align="right">5,629,256</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">59,159,201</td>
<td align="right">61,294,100</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,505,066</td>
<td align="right">21,199,139</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,831,814</td>
<td align="right">21,474,744</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,831,835</td>
<td align="right">21,474,765</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,657,112</td>
<td align="right">1,703,991</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">975,006,114</td>
<td align="right">1,002,372,783</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">201,394,654</td>
<td align="right">206,153,720</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">233,988</td>
<td align="right">228,525</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,521,577</td>
<td align="right">72,074,188</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">773,946,524</td>
<td align="right">790,070,176</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">840,727,381</td>
<td align="right">857,602,848</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">801,872,145</td>
<td align="right">817,682,015</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">780,666,198</td>
<td align="right">795,661,243</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,165,349</td>
<td align="right">6,279,043</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,297,902</td>
<td align="right">177,464,831</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">675,544,471</td>
<td align="right">687,757,733</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,560,926</td>
<td align="right">29,049,284</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,628</td>
<td align="right">73,854</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">468,039,339</td>
<td align="right">475,467,396</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,709</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">261,915,422</td>
<td align="right">265,917,900</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,535,795,692</td>
<td align="right">1,558,806,036</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">187,992,808</td>
<td align="right">190,729,528</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,584,856,062</td>
<td align="right">1,607,518,969</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">795,303,354</td>
<td align="right">806,374,710</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,886,364</td>
<td align="right">155,955,986</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">72,296,391</td>
<td align="right">73,257,691</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6,486,314</td>
<td align="right">6,569,395</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">690,694,646</td>
<td align="right">699,369,132</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,275,544,215</td>
<td align="right">1,260,923,295</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">401,289,477</td>
<td align="right">396,864,991</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,403,492,195</td>
<td align="right">1,388,371,836</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">147,892,973</td>
<td align="right">149,477,671</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,505,336,778</td>
<td align="right">1,489,362,636</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">116,392,657</td>
<td align="right">117,601,455</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,961,152</td>
<td align="right">36,327,146</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">459,026,601</td>
<td align="right">454,424,338</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,128,392</td>
<td align="right">113,987,469</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">267,401,724</td>
<td align="right">270,033,794</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,657,310,166</td>
<td align="right">1,641,008,827</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,489,326,267</td>
<td align="right">2,513,207,864</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,587,183,966</td>
<td align="right">1,601,756,606</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">233,829,281</td>
<td align="right">235,905,011</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,718,920,406</td>
<td align="right">2,695,064,822</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">626,713,232</td>
<td align="right">632,106,315</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,301,986</td>
<td align="right">130,184,901</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,380,923,342</td>
<td align="right">3,409,616,539</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">354,079,282</td>
<td align="right">357,031,668</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,750,041,003</td>
<td align="right">4,788,569,901</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,503,979</td>
<td align="right">541,095,431</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,441,500</td>
<td align="right">99,213,421</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,887,369,850</td>
<td align="right">3,917,693,598</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,733,496,669</td>
<td align="right">2,713,088,500</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">90,542,890</td>
<td align="right">91,203,861</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,358,175</td>
<td align="right">66,871,957</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,277,797</td>
<td align="right">337,891,733</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,520,906</td>
<td align="right">367,936,325</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,214,453,198</td>
<td align="right">1,206,224,417</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,358,364,135</td>
<td align="right">5,393,406,385</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,097,008</td>
<td align="right">155,082,705</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,243,768,863</td>
<td align="right">1,235,886,201</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">346,680,044</td>
<td align="right">348,835,607</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">861,439,082</td>
<td align="right">856,102,752</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,099,148</td>
<td align="right">269,426,756</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">164,037,848</td>
<td align="right">165,022,827</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,483,026,808</td>
<td align="right">3,462,226,080</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,103,508,082</td>
<td align="right">2,115,928,446</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,531,176,263</td>
<td align="right">2,516,275,459</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,240,280,801</td>
<td align="right">6,275,821,596</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,344,505,238</td>
<td align="right">2,331,158,542</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">533,686,381</td>
<td align="right">536,662,715</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,436,387</td>
<td align="right">501,632,713</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">352,583,623</td>
<td align="right">350,666,454</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">68,563,586</td>
<td align="right">68,198,201</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,139,887,488</td>
<td align="right">2,151,111,112</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">75,216,119</td>
<td align="right">75,607,134</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,284,135,354</td>
<td align="right">7,248,043,279</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">56,905,435</td>
<td align="right">57,187,003</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">98,039,041</td>
<td align="right">98,486,058</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,124,195,241</td>
<td align="right">2,114,926,930</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,040,232,565</td>
<td align="right">1,035,785,770</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">385,183,924</td>
<td align="right">386,818,521</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">252,184,651</td>
<td align="right">253,227,743</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">377,678,038</td>
<td align="right">376,127,086</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">355,618,491</td>
<td align="right">354,206,870</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,164,456,111</td>
<td align="right">3,176,738,780</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,366,470</td>
<td align="right">1,049,376,789</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">256,569,694</td>
<td align="right">255,628,848</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,749</td>
<td align="right">129,310,545</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,519,739</td>
<td align="right">241,661,549</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,569,902</td>
<td align="right">243,711,643</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,648,260</td>
<td align="right">508,934,473</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,754,455,820</td>
<td align="right">1,748,729,453</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">72,271,502</td>
<td align="right">72,503,702</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,090,907</td>
<td align="right">3,100,421</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,796</td>
<td align="right">8,951,274</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,215,289,661</td>
<td align="right">3,224,311,079</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,108,944,225</td>
<td align="right">10,081,230,697</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,694,622</td>
<td align="right">122,369,056</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,420,174,333</td>
<td align="right">2,426,496,815</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,443</td>
<td align="right">41,858,530</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">565,955,562</td>
<td align="right">564,543,120</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,433,703,212</td>
<td align="right">3,442,141,964</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,838,461,396</td>
<td align="right">5,824,118,753</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,789,321</td>
<td align="right">699,148,560</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,387,013,397</td>
<td align="right">13,356,066,805</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">940,059,214</td>
<td align="right">942,168,590</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,322,673</td>
<td align="right">417,255,926</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">282,064,088</td>
<td align="right">282,660,316</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">536,598,180</td>
<td align="right">535,504,328</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,786,196</td>
<td align="right">74,637,453</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">33,486,781,574</td>
<td align="right">33,549,077,292</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,531,359,222</td>
<td align="right">8,545,895,058</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,870,921</td>
<td align="right">9,887,601</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,475,002</td>
<td align="right">190,768,080</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,367,662</td>
<td align="right">62,274,486</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">77,896,786</td>
<td align="right">77,785,489</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,786,271</td>
<td align="right">71,683,831</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">318,021,803</td>
<td align="right">317,591,676</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">485,184,250</td>
<td align="right">485,756,119</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,252,080,295</td>
<td align="right">1,253,524,487</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,542,376,293</td>
<td align="right">1,544,009,516</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,658,186</td>
<td align="right">302,953,279</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,809,066</td>
<td align="right">154,673,090</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,265,400,369</td>
<td align="right">2,263,468,068</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">672,047,566</td>
<td align="right">671,475,195</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">190,498,000</td>
<td align="right">190,658,649</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">433,615,993</td>
<td align="right">433,968,401</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">290,125,212</td>
<td align="right">289,898,833</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,672,278,396</td>
<td align="right">10,679,499,901</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">943,020,466</td>
<td align="right">943,615,230</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">115,332,892</td>
<td align="right">115,394,723</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,966,361</td>
<td align="right">420,185,417</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,387,232</td>
<td align="right">158,464,398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,156</td>
<td align="right">188,626,814</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">335,056,797</td>
<td align="right">335,211,463</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,343,118</td>
<td align="right">7,346,057</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">22,616,520</td>
<td align="right">22,624,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,544,225</td>
<td align="right">593,343,100</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,760</td>
<td align="right">127,610,456</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">88,979,218</td>
<td align="right">89,008,115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,636,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,112,241,312</td>
<td align="right">1,111,963,985</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">6,154,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,358,246,739</td>
<td align="right">1,357,946,895</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,056,276,498</td>
<td align="right">1,056,104,560</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,095,553,868</td>
<td align="right">1,095,375,741</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,358,412</td>
<td align="right">62,354,016</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,790,921,557</td>
<td align="right">5,791,126,896</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,724,902</td>
<td align="right">112,726,125</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right">29,134,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">100,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">29,134,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right"></td>
<td align="right">4,955,680,734</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right"></td>
<td align="right">80</td>
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
<td align="right">71,525,201</td>
<td align="right">0.4%</td>
<td align="right">71,994,290</td>
<td align="right">0.4%</td>
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
<td align="right">16,228,079,956</td>
<td align="right">87.0%</td>
<td align="right">16,123,594,158</td>
<td align="right">87.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,343,575,087</td>
<td align="right">12.6%</td>
<td align="right">2,329,928,394</td>
<td align="right">12.6%</td>
<td align="right">-0.6%</td>
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
<td align="right">912,886</td>
<td align="right">40.0%</td>
<td align="right">1,072,704</td>
<td align="right">41.5%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,366,542</td>
<td align="right">60.0%</td>
<td align="right">1,513,871</td>
<td align="right">58.5%</td>
<td align="right">10.8%</td>
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
<td align="left">subscr enumdict</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">343</td>
<td align="right">0.0%</td>
<td align="right">697.7%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">384.6%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">279.6%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,336</td>
<td align="right">0.3%</td>
<td align="right">8,485</td>
<td align="right">0.8%</td>
<td align="right">263.2%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">1,207</td>
<td align="right">0.1%</td>
<td align="right">246.8%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">631</td>
<td align="right">0.1%</td>
<td align="right">1,417</td>
<td align="right">0.1%</td>
<td align="right">124.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">8,167</td>
<td align="right">0.9%</td>
<td align="right">17,983</td>
<td align="right">1.7%</td>
<td align="right">120.2%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,090</td>
<td align="right">0.8%</td>
<td align="right">15,491</td>
<td align="right">1.4%</td>
<td align="right">118.5%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">359</td>
<td align="right">0.0%</td>
<td align="right">754</td>
<td align="right">0.1%</td>
<td align="right">110.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,035</td>
<td align="right">0.2%</td>
<td align="right">4,257</td>
<td align="right">0.4%</td>
<td align="right">109.2%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">900</td>
<td align="right">0.1%</td>
<td align="right">104.5%</td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">2,756</td>
<td align="right">0.3%</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.3%</td>
<td align="right">4,915</td>
<td align="right">0.5%</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,110</td>
<td align="right">0.3%</td>
<td align="right">5,634</td>
<td align="right">0.5%</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">35,901</td>
<td align="right">3.9%</td>
<td align="right">62,273</td>
<td align="right">5.8%</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,094</td>
<td align="right">0.1%</td>
<td align="right">1,760</td>
<td align="right">0.2%</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,515</td>
<td align="right">0.9%</td>
<td align="right">13,134</td>
<td align="right">1.2%</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">42,830</td>
<td align="right">4.7%</td>
<td align="right">63,127</td>
<td align="right">5.9%</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">46,925</td>
<td align="right">5.1%</td>
<td align="right">64,472</td>
<td align="right">6.0%</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">0.9%</td>
<td align="right">11,021</td>
<td align="right">1.0%</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,457</td>
<td align="right">4.8%</td>
<td align="right">56,700</td>
<td align="right">5.3%</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,513</td>
<td align="right">2.6%</td>
<td align="right">29,807</td>
<td align="right">2.8%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,955</td>
<td align="right">3.7%</td>
<td align="right">41,977</td>
<td align="right">3.9%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">14,050</td>
<td align="right">1.3%</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,165</td>
<td align="right">0.3%</td>
<td align="right">3,765</td>
<td align="right">0.4%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">2.1%</td>
<td align="right">22,723</td>
<td align="right">2.1%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">22,292</td>
<td align="right">2.4%</td>
<td align="right">25,632</td>
<td align="right">2.4%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">78,858</td>
<td align="right">8.6%</td>
<td align="right">87,244</td>
<td align="right">8.1%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">121,439</td>
<td align="right">13.3%</td>
<td align="right">126,579</td>
<td align="right">11.8%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,208</td>
<td align="right">8.1%</td>
<td align="right">71,158</td>
<td align="right">6.6%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">9.4%</td>
<td align="right">88,203</td>
<td align="right">8.2%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">107,942</td>
<td align="right">11.8%</td>
<td align="right">109,884</td>
<td align="right">10.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">114,964</td>
<td align="right">12.6%</td>
<td align="right">114,008</td>
<td align="right">10.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">subscr structtime</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">545,503,979</td>
<td align="right">100.0%</td>
<td align="right">541,095,431</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">189,012,689</td>
<td align="right">1.7%</td>
<td align="right">2,220,183.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">178,681,917</td>
<td align="right">1.6%</td>
<td align="right">186,427,461</td>
<td align="right">1.7%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">182,042,447</td>
<td align="right">1.6%</td>
<td align="right">189,012,689</td>
<td align="right">1.7%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,102,645,703</td>
<td align="right">98.4%</td>
<td align="right">11,089,544,784</td>
<td align="right">98.3%</td>
<td align="right">-0.1%</td>
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
<td align="right">3,603,576</td>
<td align="right">100.0%</td>
<td align="right">4,162,888</td>
<td align="right">100.0%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">166</td>
<td align="right">0.0%</td>
<td align="right">13.7%</td>
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
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">3,414</td>
<td align="right">2,056.6%</td>
<td align="right">352.8%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">947</td>
<td align="right">570.5%</td>
<td align="right">254.7%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">146</td>
<td align="right">100.0%</td>
<td align="right">166</td>
<td align="right">100.0%</td>
<td align="right">13.7%</td>
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
<td align="right">574,328</td>
<td align="right">96.6%</td>
<td align="right">685,038</td>
<td align="right">91.8%</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">581,624</td>
<td align="right">97.9%</td>
<td align="right">640,338</td>
<td align="right">85.8%</td>
<td align="right">10.1%</td>
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
<td align="right">640,338</td>
<td align="right">85.8%</td>
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
<td align="right">19,924</td>
<td align="right">100.0%</td>
<td align="right">61,494</td>
<td align="right">100.0%</td>
<td align="right">208.6%</td>
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
<td align="right">1,270,904</td>
<td align="right">0.0%</td>
<td align="right">1,331,709</td>
<td align="right">0.0%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">510,423,070</td>
<td align="right">10.2%</td>
<td align="right">508,598,380</td>
<td align="right">10.1%</td>
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
<td align="right">4,505,616,983</td>
<td align="right">89.8%</td>
<td align="right">4,507,902,574</td>
<td align="right">89.8%</td>
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
<td align="right">41,392</td>
<td align="right">16.6%</td>
<td align="right">89,982</td>
<td align="right">24.9%</td>
<td align="right">117.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">207,467</td>
<td align="right">83.4%</td>
<td align="right">270,756</td>
<td align="right">75.1%</td>
<td align="right">30.5%</td>
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
<td align="right">934</td>
<td align="right">0.5%</td>
<td align="right">3,151</td>
<td align="right">1.2%</td>
<td align="right">237.4%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">196</td>
<td align="right">0.1%</td>
<td align="right">514</td>
<td align="right">0.2%</td>
<td align="right">162.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,759</td>
<td align="right">3.7%</td>
<td align="right">19,304</td>
<td align="right">7.1%</td>
<td align="right">148.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,324</td>
<td align="right">0.6%</td>
<td align="right">2,842</td>
<td align="right">1.0%</td>
<td align="right">114.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">10,484</td>
<td align="right">5.1%</td>
<td align="right">20,951</td>
<td align="right">7.7%</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,886</td>
<td align="right">0.9%</td>
<td align="right">2,841</td>
<td align="right">1.0%</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,416</td>
<td align="right">21.9%</td>
<td align="right">64,814</td>
<td align="right">23.9%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">11,307</td>
<td align="right">5.5%</td>
<td align="right">14,692</td>
<td align="right">5.4%</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,271</td>
<td align="right">11.2%</td>
<td align="right">27,723</td>
<td align="right">10.2%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,649</td>
<td align="right">3.7%</td>
<td align="right">9,030</td>
<td align="right">3.3%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,831</td>
<td align="right">3.3%</td>
<td align="right">7,645</td>
<td align="right">2.8%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">90,410</td>
<td align="right">43.6%</td>
<td align="right">97,249</td>
<td align="right">35.9%</td>
<td align="right">7.6%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,403,587</td>
<td align="right">0.1%</td>
<td align="right">1,382,577</td>
<td align="right">0.1%</td>
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
<td align="right">153,825,919</td>
<td align="right">6.6%</td>
<td align="right">155,820,822</td>
<td align="right">6.7%</td>
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
<td align="right">2,186,668,226</td>
<td align="right">93.4%</td>
<td align="right">2,181,315,277</td>
<td align="right">93.3%</td>
<td align="right">-0.2%</td>
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
<td align="right">58,335</td>
<td align="right">67.1%</td>
<td align="right">119,474</td>
<td align="right">74.1%</td>
<td align="right">104.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,589</td>
<td align="right">32.9%</td>
<td align="right">41,663</td>
<td align="right">25.9%</td>
<td align="right">45.7%</td>
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
<td align="right">11,016</td>
<td align="right">18.9%</td>
<td align="right">31,408</td>
<td align="right">26.3%</td>
<td align="right">185.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">21,773</td>
<td align="right">37.3%</td>
<td align="right">42,067</td>
<td align="right">35.2%</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,542</td>
<td align="right">24.9%</td>
<td align="right">26,275</td>
<td align="right">22.0%</td>
<td align="right">80.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,004</td>
<td align="right">18.9%</td>
<td align="right">19,724</td>
<td align="right">16.5%</td>
<td align="right">79.2%</td>
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
<td align="right">164,003,534</td>
<td align="right">3.2%</td>
<td align="right">162,051,566</td>
<td align="right">3.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,504,894,128</td>
<td align="right">29.3%</td>
<td align="right">1,488,781,020</td>
<td align="right">28.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,471,340,364</td>
<td align="right">67.5%</td>
<td align="right">3,493,040,039</td>
<td align="right">67.9%</td>
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
<td align="left">Failure</td>
<td align="right">437,261</td>
<td align="right">12.4%</td>
<td align="right">522,032</td>
<td align="right">14.3%</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,099,612</td>
<td align="right">87.6%</td>
<td align="right">3,116,740</td>
<td align="right">85.7%</td>
<td align="right">0.6%</td>
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
<td align="left">map</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">1,159</td>
<td align="right">0.2%</td>
<td align="right">345.8%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">533</td>
<td align="right">0.1%</td>
<td align="right">2,124</td>
<td align="right">0.4%</td>
<td align="right">298.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,284</td>
<td align="right">1.0%</td>
<td align="right">8,667</td>
<td align="right">1.7%</td>
<td align="right">102.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,083</td>
<td align="right">1.4%</td>
<td align="right">11,904</td>
<td align="right">2.3%</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,114</td>
<td align="right">0.7%</td>
<td align="right">5,583</td>
<td align="right">1.1%</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right">2,065</td>
<td align="right">0.4%</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,543</td>
<td align="right">2.4%</td>
<td align="right">17,169</td>
<td align="right">3.3%</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,420</td>
<td align="right">0.8%</td>
<td align="right">5,519</td>
<td align="right">1.1%</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">70,965</td>
<td align="right">16.2%</td>
<td align="right">96,138</td>
<td align="right">18.4%</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,707</td>
<td align="right">7.9%</td>
<td align="right">46,814</td>
<td align="right">9.0%</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,269</td>
<td align="right">4.2%</td>
<td align="right">24,379</td>
<td align="right">4.7%</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,022</td>
<td align="right">4.1%</td>
<td align="right">23,619</td>
<td align="right">4.5%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,537</td>
<td align="right">2.4%</td>
<td align="right">12,435</td>
<td align="right">2.4%</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,676</td>
<td align="right">19.1%</td>
<td align="right">89,124</td>
<td align="right">17.1%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">171,565</td>
<td align="right">39.2%</td>
<td align="right">175,073</td>
<td align="right">33.5%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">5,509,119</td>
<td align="right">5,509,119 / 0 !!</td>
<td align="right">5,663,016</td>
<td align="right">5,663,016 / 0 !!</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,120,635</td>
<td align="right">12,120,635 / 0 !!</td>
<td align="right">12,384,179</td>
<td align="right">12,384,179 / 0 !!</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
<td align="right">814,329</td>
<td align="right">814,329 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,933,004</td>
<td align="right">34,933,004 / 0 !!</td>
<td align="right">34,406,741</td>
<td align="right">34,406,741 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,959,219</td>
<td align="right">341,959,219 / 0 !!</td>
<td align="right">337,002,333</td>
<td align="right">337,002,333 / 0 !!</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">304,488,904</td>
<td align="right">304,488,904 / 0 !!</td>
<td align="right">307,873,372</td>
<td align="right">307,873,372 / 0 !!</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">171,559,240</td>
<td align="right">171,559,240 / 0 !!</td>
<td align="right">173,199,029</td>
<td align="right">173,199,029 / 0 !!</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,823,462</td>
<td align="right">2,823,462 / 0 !!</td>
<td align="right">2,815,298</td>
<td align="right">2,815,298 / 0 !!</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,924,887</td>
<td align="right">101,924,887 / 0 !!</td>
<td align="right">101,786,208</td>
<td align="right">101,786,208 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">119,408,267</td>
<td align="right">119,408,267 / 0 !!</td>
<td align="right">119,431,236</td>
<td align="right">119,431,236 / 0 !!</td>
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
<td align="right">1,438,767</td>
<td align="right">0.0%</td>
<td align="right">1,557,821</td>
<td align="right">0.0%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">800,099,395</td>
<td align="right">5.9%</td>
<td align="right">814,878,795</td>
<td align="right">5.9%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">860,619,085</td>
<td align="right">6.3%</td>
<td align="right">873,315,731</td>
<td align="right">6.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,982,380,100</td>
<td align="right">87.8%</td>
<td align="right">12,019,528,833</td>
<td align="right">87.7%</td>
<td align="right">0.3%</td>
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
<td align="right">505,703</td>
<td align="right">3.0%</td>
<td align="right">840,355</td>
<td align="right">4.7%</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,316,801</td>
<td align="right">97.0%</td>
<td align="right">17,085,383</td>
<td align="right">95.3%</td>
<td align="right">4.7%</td>
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
<td align="left">class attr simple</td>
<td align="right">1,885</td>
<td align="right">0.4%</td>
<td align="right">21,886</td>
<td align="right">2.6%</td>
<td align="right">1,061.1%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">1,092</td>
<td align="right">0.1%</td>
<td align="right">328.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">573</td>
<td align="right">0.1%</td>
<td align="right">1,673</td>
<td align="right">0.2%</td>
<td align="right">192.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,104</td>
<td align="right">0.2%</td>
<td align="right">3,192</td>
<td align="right">0.4%</td>
<td align="right">189.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">53,210</td>
<td align="right">10.5%</td>
<td align="right">147,387</td>
<td align="right">17.5%</td>
<td align="right">177.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,312</td>
<td align="right">1.1%</td>
<td align="right">13,506</td>
<td align="right">1.6%</td>
<td align="right">154.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,721</td>
<td align="right">0.3%</td>
<td align="right">4,327</td>
<td align="right">0.5%</td>
<td align="right">151.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">106</td>
<td align="right">0.0%</td>
<td align="right">130.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">0.9%</td>
<td align="right">9,020</td>
<td align="right">1.1%</td>
<td align="right">102.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,156</td>
<td align="right">1.6%</td>
<td align="right">16,244</td>
<td align="right">1.9%</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,801</td>
<td align="right">3.1%</td>
<td align="right">31,046</td>
<td align="right">3.7%</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">545</td>
<td align="right">0.1%</td>
<td align="right">1,021</td>
<td align="right">0.1%</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,739</td>
<td align="right">0.5%</td>
<td align="right">5,081</td>
<td align="right">0.6%</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,475</td>
<td align="right">4.8%</td>
<td align="right">42,666</td>
<td align="right">5.1%</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">54,639</td>
<td align="right">10.8%</td>
<td align="right">91,783</td>
<td align="right">10.9%</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">73,632</td>
<td align="right">14.6%</td>
<td align="right">113,380</td>
<td align="right">13.5%</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">-20.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">51,820</td>
<td align="right">0.0%</td>
<td align="right">303,522</td>
<td align="right">0.0%</td>
<td align="right">485.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,376</td>
<td align="right">0.0%</td>
<td align="right">5,094</td>
<td align="right">0.0%</td>
<td align="right">270.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,459</td>
<td align="right">0.2%</td>
<td align="right">15,099,423</td>
<td align="right">0.2%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,219,332,918</td>
<td align="right">99.8%</td>
<td align="right">9,233,431,770</td>
<td align="right">99.8%</td>
<td align="right">0.2%</td>
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
<td align="right">134,588</td>
<td align="right">100.0%</td>
<td align="right">525,927</td>
<td align="right">100.0%</td>
<td align="right">290.8%</td>
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
<td align="right">203</td>
<td align="right">0.0%</td>
<td align="right">6,987</td>
<td align="right">0.0%</td>
<td align="right">3,341.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,155,615</td>
<td align="right">100.0%</td>
<td align="right">67,201,455</td>
<td align="right">100.0%</td>
<td align="right">4.7%</td>
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
<td align="right">2,310</td>
<td align="right">100.0%</td>
<td align="right">7,170</td>
<td align="right">100.0%</td>
<td align="right">210.4%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,711</td>
<td align="right">0.0%</td>
<td align="right">27,421</td>
<td align="right">0.0%</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,816,951</td>
<td align="right">17.8%</td>
<td align="right">129,260,570</td>
<td align="right">17.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">593,529,514</td>
<td align="right">82.2%</td>
<td align="right">593,315,679</td>
<td align="right">82.1%</td>
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
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">4,554</td>
<td align="right">9.0%</td>
<td align="right">591.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">45,927</td>
<td align="right">91.0%</td>
<td align="right">33.5%</td>
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
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">9,693</td>
<td align="right">21.1%</td>
<td align="right">197.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right">2,121</td>
<td align="right">4.6%</td>
<td align="right">182.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">9,073</td>
<td align="right">19.8%</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">25,040</td>
<td align="right">54.5%</td>
<td align="right">2.5%</td>
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
<td align="right">114,218,313</td>
<td align="right">5.7%</td>
<td align="right">126,292,313</td>
<td align="right">6.2%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">66,396,848</td>
<td align="right">3.3%</td>
<td align="right">68,781,472</td>
<td align="right">3.4%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,812,785,063</td>
<td align="right">90.9%</td>
<td align="right">1,828,646,974</td>
<td align="right">90.4%</td>
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
<td align="left">Failure</td>
<td align="right">44,918</td>
<td align="right">2.0%</td>
<td align="right">104,454</td>
<td align="right">4.0%</td>
<td align="right">132.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,193,978</td>
<td align="right">98.0%</td>
<td align="right">2,489,264</td>
<td align="right">96.0%</td>
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
<td align="left">not in keys</td>
<td align="right">747</td>
<td align="right">1.7%</td>
<td align="right">7,044</td>
<td align="right">6.7%</td>
<td align="right">843.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">631</td>
<td align="right">0.6%</td>
<td align="right">468.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">363</td>
<td align="right">0.8%</td>
<td align="right">1,823</td>
<td align="right">1.7%</td>
<td align="right">402.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,344</td>
<td align="right">7.4%</td>
<td align="right">11,043</td>
<td align="right">10.6%</td>
<td align="right">230.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">273</td>
<td align="right">0.3%</td>
<td align="right">190.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">251</td>
<td align="right">0.2%</td>
<td align="right">175.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,321</td>
<td align="right">2.9%</td>
<td align="right">3,088</td>
<td align="right">3.0%</td>
<td align="right">133.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">19,647</td>
<td align="right">43.7%</td>
<td align="right">43,626</td>
<td align="right">41.8%</td>
<td align="right">122.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,741</td>
<td align="right">8.3%</td>
<td align="right">7,974</td>
<td align="right">7.6%</td>
<td align="right">113.2%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,227</td>
<td align="right">16.1%</td>
<td align="right">14,124</td>
<td align="right">13.5%</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">5,799</td>
<td align="right">12.9%</td>
<td align="right">9,321</td>
<td align="right">8.9%</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">0.9%</td>
<td align="right">603</td>
<td align="right">0.6%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">248,234</td>
<td align="right">552.6%</td>
<td align="right">319,820</td>
<td align="right">306.2%</td>
<td align="right">28.8%</td>
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
<td align="right">112,724,902</td>
<td align="right">100.0%</td>
<td align="right">112,726,125</td>
<td align="right">100.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">918,536,965</td>
<td align="right">56.7%</td>
<td align="right">915,207,414</td>
<td align="right">56.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">700,605,419</td>
<td align="right">43.3%</td>
<td align="right">698,908,506</td>
<td align="right">43.3%</td>
<td align="right">-0.2%</td>
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
<td align="right">2,064</td>
<td align="right">1.1%</td>
<td align="right">15,206</td>
<td align="right">6.3%</td>
<td align="right">636.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">181,878</td>
<td align="right">98.9%</td>
<td align="right">224,888</td>
<td align="right">93.7%</td>
<td align="right">23.6%</td>
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
<td align="right">17,164</td>
<td align="right">9.4%</td>
<td align="right">45,076</td>
<td align="right">20.0%</td>
<td align="right">162.6%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">168</td>
<td align="right">0.1%</td>
<td align="right">147.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">0.9%</td>
<td align="right">3,060</td>
<td align="right">1.4%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,315</td>
<td align="right">2.9%</td>
<td align="right">8,875</td>
<td align="right">3.9%</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,991</td>
<td align="right">1.6%</td>
<td align="right">4,465</td>
<td align="right">2.0%</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,183</td>
<td align="right">10.5%</td>
<td align="right">23,849</td>
<td align="right">10.6%</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.9%</td>
<td align="right">53,621</td>
<td align="right">23.8%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">86,545</td>
<td align="right">47.6%</td>
<td align="right">85,774</td>
<td align="right">38.1%</td>
<td align="right">-0.9%</td>
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
<td align="right">110,683,097</td>
<td align="right">2.2%</td>
<td align="right">115,049,778</td>
<td align="right">2.2%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,726,271,111</td>
<td align="right">92.8%</td>
<td align="right">4,759,078,485</td>
<td align="right">92.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">255,922,592</td>
<td align="right">5.0%</td>
<td align="right">254,757,522</td>
<td align="right">5.0%</td>
<td align="right">-0.5%</td>
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
<td align="right">2,136,866</td>
<td align="right">78.2%</td>
<td align="right">2,389,132</td>
<td align="right">78.7%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">596,942</td>
<td align="right">21.8%</td>
<td align="right">647,062</td>
<td align="right">21.3%</td>
<td align="right">8.4%</td>
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
<td align="left">memory view</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,045</td>
<td align="right">1.7%</td>
<td align="right">19,952</td>
<td align="right">3.1%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">622</td>
<td align="right">0.1%</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,307</td>
<td align="right">2.7%</td>
<td align="right">24,002</td>
<td align="right">3.7%</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,724</td>
<td align="right">1.6%</td>
<td align="right">11,996</td>
<td align="right">1.9%</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">83,512</td>
<td align="right">14.0%</td>
<td align="right">95,795</td>
<td align="right">14.8%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">72,063</td>
<td align="right">12.1%</td>
<td align="right">81,581</td>
<td align="right">12.6%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,856</td>
<td align="right">3.2%</td>
<td align="right">20,936</td>
<td align="right">3.2%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">126,748</td>
<td align="right">21.2%</td>
<td align="right">133,292</td>
<td align="right">20.6%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,845</td>
<td align="right">43.2%</td>
<td align="right">257,446</td>
<td align="right">39.8%</td>
<td align="right">-0.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,646,394</td>
<td align="right">0.1%</td>
<td align="right">1,664,277</td>
<td align="right">0.1%</td>
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
<td align="right">1,237,590,713</td>
<td align="right">99.9%</td>
<td align="right">1,249,286,523</td>
<td align="right">99.9%</td>
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
<td align="right">9,889</td>
<td align="right">91.6%</td>
<td align="right">37,193</td>
<td align="right">93.6%</td>
<td align="right">276.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">909</td>
<td align="right">8.4%</td>
<td align="right">2,561</td>
<td align="right">6.4%</td>
<td align="right">181.7%</td>
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
<td align="right">99</td>
<td align="right">10.9%</td>
<td align="right">398</td>
<td align="right">15.5%</td>
<td align="right">302.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">674</td>
<td align="right">74.1%</td>
<td align="right">1,847</td>
<td align="right">72.1%</td>
<td align="right">174.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.0%</td>
<td align="right">316</td>
<td align="right">12.3%</td>
<td align="right">132.4%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">122,108,965,215</td>
<td align="right">58.0%</td>
<td align="right">127,241,024,774</td>
<td align="right">59.0%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,506,577,731</td>
<td align="right">0.7%</td>
<td align="right">1,541,569,925</td>
<td align="right">0.7%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,239,395,468</td>
<td align="right">3.9%</td>
<td align="right">8,224,397,748</td>
<td align="right">3.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">78,552,145,286</td>
<td align="right">37.3%</td>
<td align="right">78,639,145,998</td>
<td align="right">36.5%</td>
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
<td align="left">CALL</td>
<td align="right">178,681,917</td>
<td align="right">2.4%</td>
<td align="right">186,427,461</td>
<td align="right">2.6%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">800,099,395</td>
<td align="right">10.9%</td>
<td align="right">814,878,795</td>
<td align="right">11.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,825,919</td>
<td align="right">2.1%</td>
<td align="right">155,820,822</td>
<td align="right">2.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,504,894,128</td>
<td align="right">20.6%</td>
<td align="right">1,488,781,020</td>
<td align="right">20.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,503,979</td>
<td align="right">7.5%</td>
<td align="right">541,095,431</td>
<td align="right">7.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,343,575,087</td>
<td align="right">32.0%</td>
<td align="right">2,329,928,394</td>
<td align="right">31.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">255,922,592</td>
<td align="right">3.5%</td>
<td align="right">254,757,522</td>
<td align="right">3.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,423,070</td>
<td align="right">7.0%</td>
<td align="right">508,598,380</td>
<td align="right">7.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,951</td>
<td align="right">1.8%</td>
<td align="right">129,260,570</td>
<td align="right">1.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,605,419</td>
<td align="right">9.6%</td>
<td align="right">698,908,506</td>
<td align="right">9.6%</td>
<td align="right">-0.2%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,987,666</td>
<td align="right">6.2%</td>
<td align="right">105,769,620</td>
<td align="right">6.9%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,376,176</td>
<td align="right">3.3%</td>
<td align="right">52,989,251</td>
<td align="right">3.4%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,670,270</td>
<td align="right">5.4%</td>
<td align="right">84,910,464</td>
<td align="right">5.5%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">89,935,858</td>
<td align="right">6.0%</td>
<td align="right">92,225,300</td>
<td align="right">6.0%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,834,831</td>
<td align="right">5.5%</td>
<td align="right">84,800,464</td>
<td align="right">5.5%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,912,897</td>
<td align="right">5.4%</td>
<td align="right">80,906,896</td>
<td align="right">5.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,013,242</td>
<td align="right">5.4%</td>
<td align="right">81,062,422</td>
<td align="right">5.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,476,432</td>
<td align="right">3.6%</td>
<td align="right">55,099,190</td>
<td align="right">3.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">365,459,423</td>
<td align="right">24.3%</td>
<td align="right">369,444,824</td>
<td align="right">24.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">264,671,856</td>
<td align="right">17.6%</td>
<td align="right">266,332,675</td>
<td align="right">17.3%</td>
<td align="right">0.6%</td>
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
<td align="right">3,864</td>
<td align="right">0.0%</td>
<td align="right">50,315</td>
<td align="right">0.0%</td>
<td align="right">1,202.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,002,922,546</td>
<td align="right">15.0%</td>
<td align="right">1,017,269,378</td>
<td align="right">15.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,007,199,867</td>
<td align="right">15.1%</td>
<td align="right">1,021,543,615</td>
<td align="right">15.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,698,282</td>
<td align="right">1.1%</td>
<td align="right">71,599,190</td>
<td align="right">1.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,457</td>
<td align="right">0.1%</td>
<td align="right">4,223,922</td>
<td align="right">0.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,591,227</td>
<td align="right">0.4%</td>
<td align="right">23,847,507</td>
<td align="right">0.4%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,591,671,587</td>
<td align="right">23.8%</td>
<td align="right">1,606,441,618</td>
<td align="right">23.9%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,591,671,587</td>
<td align="right">23.8%</td>
<td align="right">1,606,441,618</td>
<td align="right">23.9%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,415,419,390</td>
<td align="right">81.0%</td>
<td align="right">5,451,076,306</td>
<td align="right">81.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,898</td>
<td align="right">2.0%</td>
<td align="right">131,916,029</td>
<td align="right">2.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">275,687,879</td>
<td align="right">4.1%</td>
<td align="right">276,911,548</td>
<td align="right">4.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,094,268,080</td>
<td align="right">76.2%</td>
<td align="right">5,116,381,795</td>
<td align="right">76.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,483,601</td>
<td align="right">3.9%</td>
<td align="right">260,167,466</td>
<td align="right">3.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,471,720</td>
<td align="right">8.7%</td>
<td align="right">584,898,003</td>
<td align="right">8.7%</td>
<td align="right">0.1%</td>
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
<td align="left">Materialize dict (new key)</td>
<td align="right">306,771</td>
<td align="right">0.2%</td>
<td align="right">336,748</td>
<td align="right">0.2%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">53,859,443</td>
<td align="right"></td>
<td align="right">57,630,314</td>
<td align="right"></td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,404,482</td>
<td align="right">1.9%</td>
<td align="right">3,639,155</td>
<td align="right">2.0%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">59,998,263</td>
<td align="right"></td>
<td align="right">63,837,944</td>
<td align="right"></td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,365,283</td>
<td align="right">0.0%</td>
<td align="right">6,599,859</td>
<td align="right">0.0%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,366,216,214</td>
<td align="right"></td>
<td align="right">2,418,245,761</td>
<td align="right"></td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,612,733</td>
<td align="right"></td>
<td align="right">177,776,746</td>
<td align="right"></td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">22,954,639,697</td>
<td align="right">25.1%</td>
<td align="right">23,122,065,327</td>
<td align="right">25.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,268,492</td>
<td align="right">0.4%</td>
<td align="right">71,728,263</td>
<td align="right">0.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,559,298,472</td>
<td align="right">29.1%</td>
<td align="right">5,593,172,616</td>
<td align="right">29.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,481,664,697</td>
<td align="right">28.7%</td>
<td align="right">5,514,844,494</td>
<td align="right">28.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,940,507</td>
<td align="right"></td>
<td align="right">6,902,025</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,447,138,403</td>
<td align="right"></td>
<td align="right">2,459,403,063</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">4,383</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,571,878,224</td>
<td align="right">70.9%</td>
<td align="right">13,517,087,785</td>
<td align="right">70.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,571,991,462</td>
<td align="right"></td>
<td align="right">13,518,797,612</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">39,071,285,847</td>
<td align="right">42.6%</td>
<td align="right">39,222,628,002</td>
<td align="right">42.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,907,814,455</td>
<td align="right">22.9%</td>
<td align="right">24,998,077,426</td>
<td align="right">23.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">50,143,229,286</td>
<td align="right">46.1%</td>
<td align="right">50,291,101,659</td>
<td align="right">46.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">24,946,698,535</td>
<td align="right">27.2%</td>
<td align="right">25,012,365,075</td>
<td align="right">27.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,643,664,441</td>
<td align="right">5.1%</td>
<td align="right">4,654,090,416</td>
<td align="right">5.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,860,435,744</td>
<td align="right">1.7%</td>
<td align="right">1,864,268,004</td>
<td align="right">1.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">31,753,727,728</td>
<td align="right">29.2%</td>
<td align="right">31,731,116,281</td>
<td align="right">29.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,157,304,209</td>
<td align="right"></td>
<td align="right">6,153,456,285</td>
<td align="right"></td>
<td align="right">-0.1%</td>
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
<td align="right">364,854</td>
<td align="right">102,019,039</td>
<td align="right">9,532,982,198</td>
<td align="right">758,453,501</td>
<td align="right">763,950,608</td>
<td align="right">367,270</td>
<td align="right">94,736,173</td>
<td align="right">9,779,227,724</td>
<td align="right">818,424,640</td>
<td align="right">756,014,896</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,681,093,428</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,934</td>
<td align="right">4,310,180</td>
<td align="right">5,666,277,928</td>
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
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">41</td>
<td align="right">901</td>
<td align="right">2,097.6%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">34</td>
<td align="right">714</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,592</td>
<td align="right">22,239</td>
<td align="right">-1.6%</td>
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
<td align="right">2,397</td>
<td align="right">2,337</td>
<td align="right">-2.5%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-27
