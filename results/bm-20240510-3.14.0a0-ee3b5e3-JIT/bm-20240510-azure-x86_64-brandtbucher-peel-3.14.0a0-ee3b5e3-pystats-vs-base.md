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
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">1,470,285</td>
<td align="right">2,227,445</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,592,600</td>
<td align="right">2,314,937</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67,890,563</td>
<td align="right">38,870,545</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,037,447</td>
<td align="right">117,335,148</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,730,812</td>
<td align="right">2,254,780</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,697,798</td>
<td align="right">54,873,156</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,477,658</td>
<td align="right">10,307,067</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">126,400,695</td>
<td align="right">115,726,525</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">6,176,099</td>
<td align="right">6,593,906</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">40,064,997</td>
<td align="right">42,533,907</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">6,671,418</td>
<td align="right">6,949,773</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">49,180</td>
<td align="right">50,900</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">404,005,731</td>
<td align="right">414,027,632</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,802,041,163</td>
<td align="right">4,690,021,666</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">31,596,046</td>
<td align="right">32,321,451</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">161,940</td>
<td align="right">164,980</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">39,498,178</td>
<td align="right">40,225,881</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">195,333,144</td>
<td align="right">191,740,754</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">116,497,576</td>
<td align="right">118,454,346</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">142,957,749</td>
<td align="right">145,334,461</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">105,984,232</td>
<td align="right">107,726,320</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">70,626,164</td>
<td align="right">71,749,298</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">166,949,928</td>
<td align="right">169,474,371</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">105,031,377</td>
<td align="right">106,505,124</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">7,500,785</td>
<td align="right">7,605,550</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">424,680,112</td>
<td align="right">429,991,188</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">275,392,836</td>
<td align="right">278,725,925</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">83,962,724</td>
<td align="right">84,929,389</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">211,791</td>
<td align="right">213,978</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">169,544,149</td>
<td align="right">171,285,631</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,387,166,247</td>
<td align="right">1,373,000,424</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">497,863</td>
<td align="right">502,660</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">110,532,036</td>
<td align="right">111,540,322</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">80,997,036</td>
<td align="right">81,720,537</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">326,729,334</td>
<td align="right">329,467,358</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">414,745,110</td>
<td align="right">418,046,096</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">945,801,887</td>
<td align="right">953,229,001</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">5,155,198</td>
<td align="right">5,190,031</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">430,355,594</td>
<td align="right">433,222,394</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">321,165,880</td>
<td align="right">323,301,327</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">190,270,137</td>
<td align="right">191,492,786</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,326,107,175</td>
<td align="right">2,340,242,006</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">324,124,499</td>
<td align="right">326,090,445</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,162,941</td>
<td align="right">78,634,512</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,208,894,183</td>
<td align="right">1,216,100,871</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">513,654,570</td>
<td align="right">516,600,664</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,132,779,125</td>
<td align="right">1,139,246,606</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">144,289,929</td>
<td align="right">145,087,944</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">65,832,343</td>
<td align="right">66,194,098</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,144,511,824</td>
<td align="right">1,150,752,635</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,101,084</td>
<td align="right">53,385,126</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,778,316,433</td>
<td align="right">1,787,795,835</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">315,545,057</td>
<td align="right">317,203,224</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">686,957,818</td>
<td align="right">690,481,955</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">75,958,555</td>
<td align="right">76,341,446</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">428,441,623</td>
<td align="right">430,427,554</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">328,516,982</td>
<td align="right">330,029,796</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">98,881,660</td>
<td align="right">99,331,260</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">829,369,602</td>
<td align="right">833,012,988</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">398,720,300</td>
<td align="right">400,441,740</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,501,661</td>
<td align="right">52,727,421</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">479,258,885</td>
<td align="right">481,303,220</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">105,667,962</td>
<td align="right">106,118,522</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">49,178,890</td>
<td align="right">49,385,297</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,662,825,178</td>
<td align="right">2,651,759,376</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,697,587,220</td>
<td align="right">1,704,590,089</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">618,825,363</td>
<td align="right">621,334,897</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">312,558,743</td>
<td align="right">313,793,994</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">188,510,257</td>
<td align="right">189,247,591</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">25,789,454,412</td>
<td align="right">25,689,025,033</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">209,395,638</td>
<td align="right">210,195,565</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,580,073</td>
<td align="right">9,615,605</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">335,450,541</td>
<td align="right">336,616,069</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,088,407,399</td>
<td align="right">4,102,608,075</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,594,896,404</td>
<td align="right">1,600,188,965</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,183,069,082</td>
<td align="right">6,203,312,125</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">290,624,717</td>
<td align="right">291,536,455</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">933,484,587</td>
<td align="right">936,360,588</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">301,240,593</td>
<td align="right">302,168,518</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">6,527,154,884</td>
<td align="right">6,546,976,952</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">472,872,231</td>
<td align="right">474,213,860</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">414,206,117</td>
<td align="right">415,344,778</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">90,664,420</td>
<td align="right">90,891,380</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">90,669,540</td>
<td align="right">90,896,500</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,730,785,436</td>
<td align="right">3,739,835,304</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">321,428,529</td>
<td align="right">322,196,048</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">146,780</td>
<td align="right">147,100</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,225,044,766</td>
<td align="right">6,238,414,059</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">394,724,258</td>
<td align="right">395,538,653</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">404,387,435</td>
<td align="right">405,221,385</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,294,076,799</td>
<td align="right">3,300,627,156</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">233,864,636</td>
<td align="right">234,320,549</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">590,236,633</td>
<td align="right">591,139,432</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,016,100,078</td>
<td align="right">1,017,618,619</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">266,303,041</td>
<td align="right">266,669,309</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,121,279,224</td>
<td align="right">1,122,700,638</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">361,780,899</td>
<td align="right">362,230,376</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">150,693,291</td>
<td align="right">150,879,704</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,612,019,979</td>
<td align="right">4,617,518,955</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">49,017,636</td>
<td align="right">48,963,372</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,597,373</td>
<td align="right">216,831,647</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">94,709,670</td>
<td align="right">94,607,832</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,673,219</td>
<td align="right">18,692,374</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,796,930,684</td>
<td align="right">3,800,685,497</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">13,026,162</td>
<td align="right">13,038,547</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">13,033,921</td>
<td align="right">13,046,307</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,420,869,843</td>
<td align="right">3,417,689,272</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,038,274</td>
<td align="right">13,050,249</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">244,542</td>
<td align="right">244,765</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,607,943,844</td>
<td align="right">6,602,107,864</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,422,963</td>
<td align="right">58,372,077</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,913,390,324</td>
<td align="right">2,915,861,926</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">29,852,233</td>
<td align="right">29,875,681</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,363,641,020</td>
<td align="right">1,364,712,093</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,791,827,669</td>
<td align="right">4,788,586,984</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">416,396,219</td>
<td align="right">416,670,445</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">22,329,617</td>
<td align="right">22,342,837</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">122,051,255</td>
<td align="right">122,121,171</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,647,607</td>
<td align="right">9,653,112</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,212,173</td>
<td align="right">9,217,299</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">766,363,674</td>
<td align="right">766,753,051</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">89,260,273</td>
<td align="right">89,300,330</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,781,481</td>
<td align="right">1,782,275</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">16,043</td>
<td align="right">16,050</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,875,529</td>
<td align="right">10,879,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,426,902</td>
<td align="right">47,440,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">278,871,046</td>
<td align="right">278,938,007</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">48,010,463</td>
<td align="right">48,021,770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,103,839</td>
<td align="right">58,116,352</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">147,332,114</td>
<td align="right">147,301,170</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">692,496</td>
<td align="right">692,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">891,646,876</td>
<td align="right">891,793,844</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">356,591,275</td>
<td align="right">356,537,725</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">293,952,478</td>
<td align="right">293,912,358</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,079,785</td>
<td align="right">83,090,745</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">184,357,357</td>
<td align="right">184,381,569</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">451,239,463</td>
<td align="right">451,188,562</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">64,929,550</td>
<td align="right">64,936,654</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">72,217,869</td>
<td align="right">72,224,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">116,138,692</td>
<td align="right">116,148,538</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,407,054</td>
<td align="right">4,407,424</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,106,071</td>
<td align="right">91,111,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,918</td>
<td align="right">1,873,831</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">104,675,132</td>
<td align="right">104,679,443</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">330,344,304</td>
<td align="right">330,357,713</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">250,973,959</td>
<td align="right">250,981,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,308,772</td>
<td align="right">20,309,279</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">32,547,038</td>
<td align="right">32,547,796</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">33,292,200</td>
<td align="right">33,292,930</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,698,291</td>
<td align="right">555,710,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,925,267,021</td>
<td align="right">1,925,290,885</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">123,542,261</td>
<td align="right">123,542,901</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,613,148</td>
<td align="right">46,613,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">175,140,239</td>
<td align="right">175,140,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">148,275,830</td>
<td align="right">148,275,751</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,313,194</td>
<td align="right">233,313,267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,216,123</td>
<td align="right">786,216,230</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">52,179,014</td>
<td align="right">52,179,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,638</td>
<td align="right">173,318,636</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">228,622,198</td>
<td align="right">228,622,196</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,024,637</td>
<td align="right">402,024,634</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,460</td>
<td align="right">38,846,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,760</td>
<td align="right">38,845,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">12,088,360</td>
<td align="right">12,088,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">8,000,960</td>
<td align="right">8,000,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,254,180</td>
<td align="right">7,254,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,464,680</td>
<td align="right">3,464,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">2,995,200</td>
<td align="right">2,995,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">719,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">546,220</td>
<td align="right">546,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">150,560</td>
<td align="right">150,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">94,160</td>
<td align="right">94,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">90,000</td>
<td align="right">90,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">25,780</td>
<td align="right">25,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">22,800</td>
<td align="right">22,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,020</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,000</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">80</td>
<td align="right">80</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,500,920</td>
<td align="right">0.4%</td>
<td align="right">20,454,680</td>
<td align="right">0.2%</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">541,441,514</td>
<td align="right">6.6%</td>
<td align="right">535,599,305</td>
<td align="right">6.5%</td>
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
<td align="right">7,720,197,467</td>
<td align="right">93.4%</td>
<td align="right">7,696,690,037</td>
<td align="right">93.5%</td>
<td align="right">-0.3%</td>
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
<td align="right">592,293</td>
<td align="right">34.6%</td>
<td align="right">421,795</td>
<td align="right">29.0%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,121,683</td>
<td align="right">65.4%</td>
<td align="right">1,034,244</td>
<td align="right">71.0%</td>
<td align="right">-7.8%</td>
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
<td align="left">add different types</td>
<td align="right">38,041</td>
<td align="right">3.4%</td>
<td align="right">23,134</td>
<td align="right">2.2%</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">90,964</td>
<td align="right">8.1%</td>
<td align="right">64,946</td>
<td align="right">6.3%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,611</td>
<td align="right">69.7%</td>
<td align="right">734,127</td>
<td align="right">71.0%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">0.9%</td>
<td align="right">10,320</td>
<td align="right">1.0%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,462</td>
<td align="right">0.9%</td>
<td align="right">10,744</td>
<td align="right">1.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">12,101</td>
<td align="right">1.1%</td>
<td align="right">12,368</td>
<td align="right">1.2%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,077</td>
<td align="right">2.6%</td>
<td align="right">29,527</td>
<td align="right">2.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">15,917</td>
<td align="right">1.4%</td>
<td align="right">16,012</td>
<td align="right">1.5%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,024</td>
<td align="right">0.4%</td>
<td align="right">5,034</td>
<td align="right">0.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">43,861</td>
<td align="right">3.9%</td>
<td align="right">43,944</td>
<td align="right">4.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">12,942</td>
<td align="right">1.2%</td>
<td align="right">12,966</td>
<td align="right">1.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">15,494</td>
<td align="right">1.4%</td>
<td align="right">15,522</td>
<td align="right">1.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,603</td>
<td align="right">0.8%</td>
<td align="right">8,613</td>
<td align="right">0.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,722</td>
<td align="right">0.4%</td>
<td align="right">4,726</td>
<td align="right">0.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,896</td>
<td align="right">0.2%</td>
<td align="right">1,897</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,088</td>
<td align="right">2.9%</td>
<td align="right">32,104</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">5,220</td>
<td align="right">0.5%</td>
<td align="right">5,220</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">2,640</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


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
<td align="right">416,237,114</td>
<td align="right">8.7%</td>
<td align="right">419,537,037</td>
<td align="right">8.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,341,945,379</td>
<td align="right">91.2%</td>
<td align="right">4,356,098,152</td>
<td align="right">91.2%</td>
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
<td align="right">1,753,810</td>
<td align="right">0.0%</td>
<td align="right">1,754,029</td>
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
<td align="right">148,575</td>
<td align="right">56.8%</td>
<td align="right">149,834</td>
<td align="right">57.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">113,231</td>
<td align="right">43.2%</td>
<td align="right">113,254</td>
<td align="right">43.0%</td>
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
<td align="left">buffer slice</td>
<td align="right">780</td>
<td align="right">0.5%</td>
<td align="right">860</td>
<td align="right">0.6%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,080</td>
<td align="right">0.7%</td>
<td align="right">1,120</td>
<td align="right">0.7%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">122</td>
<td align="right">0.1%</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">44,000</td>
<td align="right">29.6%</td>
<td align="right">44,920</td>
<td align="right">30.0%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,218</td>
<td align="right">20.3%</td>
<td align="right">30,437</td>
<td align="right">20.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">30,995</td>
<td align="right">20.9%</td>
<td align="right">30,991</td>
<td align="right">20.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,760</td>
<td align="right">13.3%</td>
<td align="right">19,760</td>
<td align="right">13.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">10.9%</td>
<td align="right">16,200</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,320</td>
<td align="right">3.6%</td>
<td align="right">5,320</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
<td align="right">203,227,882</td>
<td align="right">1.6%</td>
<td align="right">206,178,846</td>
<td align="right">1.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">314,975,017</td>
<td align="right">2.5%</td>
<td align="right">317,879,667</td>
<td align="right">2.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,317,797,747</td>
<td align="right">97.5%</td>
<td align="right">12,346,280,380</td>
<td align="right">97.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">28,860</td>
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
<td align="right">4,315,117</td>
<td align="right">98.3%</td>
<td align="right">4,370,945</td>
<td align="right">98.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">76,440</td>
<td align="right">1.7%</td>
<td align="right">76,772</td>
<td align="right">1.7%</td>
<td align="right">0.4%</td>
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
<td align="left">wrong number arguments</td>
<td align="right">8,340</td>
<td align="right">10.9%</td>
<td align="right">8,380</td>
<td align="right">10.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">67,620</td>
<td align="right">88.5%</td>
<td align="right">67,912</td>
<td align="right">88.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,100</td>
<td align="right">4.1%</td>
<td align="right">3,100</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">580</td>
<td align="right">0.8%</td>
<td align="right">580</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">480</td>
<td align="right">0.6%</td>
<td align="right">480</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">200</td>
<td align="right">0.3%</td>
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
<td align="right">126,937,226</td>
<td align="right">2.2%</td>
<td align="right">116,276,142</td>
<td align="right">2.0%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">741,470</td>
<td align="right">0.0%</td>
<td align="right">752,735</td>
<td align="right">0.0%</td>
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
<td align="right">5,755,274,552</td>
<td align="right">97.8%</td>
<td align="right">5,773,159,367</td>
<td align="right">98.0%</td>
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
<td align="right">138,343</td>
<td align="right">67.5%</td>
<td align="right">136,283</td>
<td align="right">67.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">66,596</td>
<td align="right">32.5%</td>
<td align="right">66,835</td>
<td align="right">32.9%</td>
<td align="right">0.4%</td>
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
<td align="right">14,325</td>
<td align="right">10.4%</td>
<td align="right">11,485</td>
<td align="right">8.4%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">960</td>
<td align="right">0.7%</td>
<td align="right">1,080</td>
<td align="right">0.8%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">500</td>
<td align="right">0.4%</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">25,962</td>
<td align="right">18.8%</td>
<td align="right">26,427</td>
<td align="right">19.4%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,746</td>
<td align="right">8.5%</td>
<td align="right">11,822</td>
<td align="right">8.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,720</td>
<td align="right">13.5%</td>
<td align="right">18,780</td>
<td align="right">13.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,543</td>
<td align="right">1.1%</td>
<td align="right">1,545</td>
<td align="right">1.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">26,493</td>
<td align="right">19.2%</td>
<td align="right">26,510</td>
<td align="right">19.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">20,554</td>
<td align="right">14.9%</td>
<td align="right">20,554</td>
<td align="right">15.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">14,160</td>
<td align="right">10.2%</td>
<td align="right">14,160</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,740</td>
<td align="right">1.3%</td>
<td align="right">1,740</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,640</td>
<td align="right">1.2%</td>
<td align="right">1,640</td>
<td align="right">1.2%</td>
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
<td align="right">2,366,184,953</td>
<td align="right">90.9%</td>
<td align="right">2,370,986,338</td>
<td align="right">90.9%</td>
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
<td align="right">236,212,445</td>
<td align="right">9.1%</td>
<td align="right">236,668,003</td>
<td align="right">9.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,517,260</td>
<td align="right">0.1%</td>
<td align="right">2,517,260</td>
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
<td align="right">110,434</td>
<td align="right">65.2%</td>
<td align="right">110,787</td>
<td align="right">65.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">59,017</td>
<td align="right">34.8%</td>
<td align="right">59,019</td>
<td align="right">34.8%</td>
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
<td align="right">23,096</td>
<td align="right">20.9%</td>
<td align="right">23,343</td>
<td align="right">21.1%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">16,660</td>
<td align="right">15.1%</td>
<td align="right">16,780</td>
<td align="right">15.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">13,538</td>
<td align="right">12.3%</td>
<td align="right">13,524</td>
<td align="right">12.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">57,140</td>
<td align="right">51.7%</td>
<td align="right">57,140</td>
<td align="right">51.6%</td>
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
<td align="right">176,215</td>
<td align="right">0.0%</td>
<td align="right">163,021</td>
<td align="right">0.0%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">459,437,361</td>
<td align="right">85.8%</td>
<td align="right">462,147,849</td>
<td align="right">85.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">75,992,608</td>
<td align="right">14.2%</td>
<td align="right">76,362,653</td>
<td align="right">14.2%</td>
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
<td align="left">Success</td>
<td align="right">47,882</td>
<td align="right">33.7%</td>
<td align="right">47,684</td>
<td align="right">33.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">94,280</td>
<td align="right">66.3%</td>
<td align="right">94,130</td>
<td align="right">66.4%</td>
<td align="right">-0.2%</td>
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
<td align="left">reversed list</td>
<td align="right">3,220</td>
<td align="right">3.4%</td>
<td align="right">3,320</td>
<td align="right">3.5%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,540</td>
<td align="right">38.8%</td>
<td align="right">36,308</td>
<td align="right">38.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,194</td>
<td align="right">10.8%</td>
<td align="right">10,155</td>
<td align="right">10.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">320</td>
<td align="right">0.3%</td>
<td align="right">319</td>
<td align="right">0.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,460</td>
<td align="right">6.9%</td>
<td align="right">6,480</td>
<td align="right">6.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,566</td>
<td align="right">10.1%</td>
<td align="right">9,568</td>
<td align="right">10.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,720</td>
<td align="right">8.2%</td>
<td align="right">7,720</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,300</td>
<td align="right">7.7%</td>
<td align="right">7,300</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,420</td>
<td align="right">5.7%</td>
<td align="right">5,420</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,840</td>
<td align="right">4.1%</td>
<td align="right">3,840</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,540</td>
<td align="right">1.6%</td>
<td align="right">1,540</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,380</td>
<td align="right">1.5%</td>
<td align="right">1,380</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">560</td>
<td align="right">0.6%</td>
<td align="right">560</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.2%</td>
<td align="right">220</td>
<td align="right">0.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,962,276,306</td>
<td align="right">92.9%</td>
<td align="right">18,051,334,684</td>
<td align="right">92.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,373,439,536</td>
<td align="right">7.1%</td>
<td align="right">1,379,953,965</td>
<td align="right">7.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">246,686,167</td>
<td align="right">1.3%</td>
<td align="right">246,737,953</td>
<td align="right">1.3%</td>
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
<td align="right">320,700</td>
<td align="right">0.0%</td>
<td align="right">320,700</td>
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
<td align="right">828,014</td>
<td align="right">13.7%</td>
<td align="right">831,906</td>
<td align="right">13.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,197,742</td>
<td align="right">86.3%</td>
<td align="right">5,198,688</td>
<td align="right">86.2%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">5,658</td>
<td align="right">0.7%</td>
<td align="right">5,778</td>
<td align="right">0.7%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">85,824</td>
<td align="right">10.4%</td>
<td align="right">87,522</td>
<td align="right">10.5%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">19,820</td>
<td align="right">2.4%</td>
<td align="right">19,960</td>
<td align="right">2.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">54,260</td>
<td align="right">6.6%</td>
<td align="right">54,628</td>
<td align="right">6.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,380</td>
<td align="right">1.7%</td>
<td align="right">14,460</td>
<td align="right">1.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">45,184</td>
<td align="right">5.5%</td>
<td align="right">45,425</td>
<td align="right">5.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">13,309</td>
<td align="right">1.6%</td>
<td align="right">13,377</td>
<td align="right">1.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,700</td>
<td align="right">3.2%</td>
<td align="right">26,800</td>
<td align="right">3.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,200</td>
<td align="right">1.5%</td>
<td align="right">12,240</td>
<td align="right">1.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">266,539</td>
<td align="right">32.2%</td>
<td align="right">267,266</td>
<td align="right">32.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,760</td>
<td align="right">1.9%</td>
<td align="right">15,720</td>
<td align="right">1.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">72,983</td>
<td align="right">8.8%</td>
<td align="right">73,096</td>
<td align="right">8.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">179,397</td>
<td align="right">21.7%</td>
<td align="right">179,634</td>
<td align="right">21.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">11,380</td>
<td align="right">1.4%</td>
<td align="right">11,380</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,860</td>
<td align="right">0.3%</td>
<td align="right">2,860</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">451,163</td>
<td align="right">0.0%</td>
<td align="right">455,974</td>
<td align="right">0.0%</td>
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
<td align="right">7,490,979,847</td>
<td align="right">99.7%</td>
<td align="right">7,538,024,440</td>
<td align="right">99.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,312,988</td>
<td align="right">0.3%</td>
<td align="right">20,318,038</td>
<td align="right">0.3%</td>
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
<td align="right">11,300</td>
<td align="right">0.0%</td>
<td align="right">11,300</td>
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
<td align="right">446,947</td>
<td align="right">100.0%</td>
<td align="right">447,215</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
<td align="right">86,182,154</td>
<td align="right">100.0%</td>
<td align="right">86,940,408</td>
<td align="right">100.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,143</td>
<td align="right">0.0%</td>
<td align="right">8,150</td>
<td align="right">0.0%</td>
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
<td align="right">7,900</td>
<td align="right">100.0%</td>
<td align="right">7,900</td>
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

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NONE family </summary>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NOT_NONE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


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
<td align="right">786,185,463</td>
<td align="right">81.9%</td>
<td align="right">786,185,570</td>
<td align="right">81.9%</td>
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
<td align="right">173,284,278</td>
<td align="right">18.1%</td>
<td align="right">173,284,276</td>
<td align="right">18.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">30,660</td>
<td align="right">0.0%</td>
<td align="right">30,660</td>
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
<td align="right">5,420</td>
<td align="right">8.3%</td>
<td align="right">5,420</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
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
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">55.7%</td>
<td align="right">33,180</td>
<td align="right">55.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,240</td>
<td align="right">23.9%</td>
<td align="right">14,240</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,220</td>
<td align="right">3.7%</td>
<td align="right">2,220</td>
<td align="right">3.7%</td>
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
<td align="right">98,657,359</td>
<td align="right">2.7%</td>
<td align="right">99,374,830</td>
<td align="right">2.7%</td>
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
<td align="right">3,546,221,630</td>
<td align="right">97.3%</td>
<td align="right">3,555,986,460</td>
<td align="right">97.2%</td>
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
<td align="right">68,516,286</td>
<td align="right">1.9%</td>
<td align="right">68,508,774</td>
<td align="right">1.9%</td>
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
<td align="left">Failure</td>
<td align="right">71,204</td>
<td align="right">4.9%</td>
<td align="right">71,772</td>
<td align="right">4.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,383,769</td>
<td align="right">95.1%</td>
<td align="right">1,383,623</td>
<td align="right">95.1%</td>
<td align="right">-0.0%</td>
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
<td align="right">2,840</td>
<td align="right">4.0%</td>
<td align="right">3,080</td>
<td align="right">4.3%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,580</td>
<td align="right">12.0%</td>
<td align="right">8,740</td>
<td align="right">12.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,840</td>
<td align="right">6.8%</td>
<td align="right">4,880</td>
<td align="right">6.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,760</td>
<td align="right">19.3%</td>
<td align="right">13,840</td>
<td align="right">19.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">10,220</td>
<td align="right">14.4%</td>
<td align="right">10,260</td>
<td align="right">14.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">16,724</td>
<td align="right">23.5%</td>
<td align="right">16,732</td>
<td align="right">23.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,020</td>
<td align="right">7.1%</td>
<td align="right">5,020</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,360</td>
<td align="right">6.1%</td>
<td align="right">4,360</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3,940</td>
<td align="right">5.5%</td>
<td align="right">3,940</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">800</td>
<td align="right">1.1%</td>
<td align="right">800</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>


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
<td align="right">849,698,517</td>
<td align="right">92.9%</td>
<td align="right">852,104,778</td>
<td align="right">92.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">64,865,751</td>
<td align="right">7.1%</td>
<td align="right">64,872,766</td>
<td align="right">7.1%</td>
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
<td align="right">52,760</td>
<td align="right">82.7%</td>
<td align="right">52,841</td>
<td align="right">82.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,039</td>
<td align="right">17.3%</td>
<td align="right">11,047</td>
<td align="right">17.3%</td>
<td align="right">0.1%</td>
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
<td align="right">780</td>
<td align="right">1.5%</td>
<td align="right">800</td>
<td align="right">1.5%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,120</td>
<td align="right">2.1%</td>
<td align="right">1,140</td>
<td align="right">2.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">10,160</td>
<td align="right">19.3%</td>
<td align="right">10,181</td>
<td align="right">19.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">33,160</td>
<td align="right">62.9%</td>
<td align="right">33,180</td>
<td align="right">62.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">12.3%</td>
<td align="right">6,480</td>
<td align="right">12.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,040</td>
<td align="right">2.0%</td>
<td align="right">1,040</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">527,097,988</td>
<td align="right">7.1%</td>
<td align="right">529,178,963</td>
<td align="right">7.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,947,093,422</td>
<td align="right">92.9%</td>
<td align="right">6,962,857,546</td>
<td align="right">92.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,191,817</td>
<td align="right">0.7%</td>
<td align="right">49,230,094</td>
<td align="right">0.7%</td>
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
<td align="right">240,346</td>
<td align="right">17.8%</td>
<td align="right">241,174</td>
<td align="right">17.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,112,368</td>
<td align="right">82.2%</td>
<td align="right">1,113,177</td>
<td align="right">82.2%</td>
<td align="right">0.1%</td>
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
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.6%</td>
<td align="right">1,740</td>
<td align="right">0.7%</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">14,480</td>
<td align="right">6.0%</td>
<td align="right">14,600</td>
<td align="right">6.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,593</td>
<td align="right">1.9%</td>
<td align="right">4,627</td>
<td align="right">1.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">48,000</td>
<td align="right">20.0%</td>
<td align="right">48,182</td>
<td align="right">20.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,667</td>
<td align="right">5.7%</td>
<td align="right">13,715</td>
<td align="right">5.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">14,677</td>
<td align="right">6.1%</td>
<td align="right">14,727</td>
<td align="right">6.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,175</td>
<td align="right">11.3%</td>
<td align="right">27,234</td>
<td align="right">11.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">46,231</td>
<td align="right">19.2%</td>
<td align="right">46,274</td>
<td align="right">19.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">68,603</td>
<td align="right">28.5%</td>
<td align="right">68,615</td>
<td align="right">28.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.4%</td>
<td align="right">1,040</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">420</td>
<td align="right">0.2%</td>
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
<td align="right">215,346</td>
<td align="right">0.0%</td>
<td align="right">215,524</td>
<td align="right">0.0%</td>
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
<td align="right">1,529,684,991</td>
<td align="right">100.0%</td>
<td align="right">1,530,508,597</td>
<td align="right">100.0%</td>
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
<td align="right">27,120</td>
<td align="right">92.9%</td>
<td align="right">27,164</td>
<td align="right">92.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,076</td>
<td align="right">7.1%</td>
<td align="right">2,077</td>
<td align="right">7.1%</td>
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
<td align="right">1,436</td>
<td align="right">69.2%</td>
<td align="right">1,437</td>
<td align="right">69.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">18.3%</td>
<td align="right">380</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">12.5%</td>
<td align="right">260</td>
<td align="right">12.5%</td>
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
<td align="right">680,668,350</td>
<td align="right">0.5%</td>
<td align="right">674,658,621</td>
<td align="right">0.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">50,368,610,944</td>
<td align="right">37.6%</td>
<td align="right">50,220,593,393</td>
<td align="right">37.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">12,739,460,628</td>
<td align="right">9.5%</td>
<td align="right">12,775,272,778</td>
<td align="right">9.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">70,036,667,436</td>
<td align="right">52.3%</td>
<td align="right">70,032,180,180</td>
<td align="right">52.4%</td>
<td align="right">-0.0%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">126,937,226</td>
<td align="right">3.2%</td>
<td align="right">116,276,142</td>
<td align="right">2.9%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">541,441,514</td>
<td align="right">13.6%</td>
<td align="right">535,599,305</td>
<td align="right">13.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">314,975,017</td>
<td align="right">7.9%</td>
<td align="right">317,879,667</td>
<td align="right">8.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">416,237,114</td>
<td align="right">10.5%</td>
<td align="right">419,537,037</td>
<td align="right">10.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">98,657,359</td>
<td align="right">2.5%</td>
<td align="right">99,374,830</td>
<td align="right">2.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">75,992,608</td>
<td align="right">1.9%</td>
<td align="right">76,362,653</td>
<td align="right">1.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,373,439,536</td>
<td align="right">34.6%</td>
<td align="right">1,379,953,965</td>
<td align="right">34.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">527,097,988</td>
<td align="right">13.3%</td>
<td align="right">529,178,963</td>
<td align="right">13.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">236,212,445</td>
<td align="right">6.0%</td>
<td align="right">236,668,003</td>
<td align="right">6.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,278</td>
<td align="right">4.4%</td>
<td align="right">173,284,276</td>
<td align="right">4.4%</td>
<td align="right">-0.0%</td>
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
<td align="right">98,417,149</td>
<td align="right">13.0%</td>
<td align="right">100,736,403</td>
<td align="right">13.4%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,201,018</td>
<td align="right">3.3%</td>
<td align="right">25,191,594</td>
<td align="right">3.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,952,049</td>
<td align="right">5.4%</td>
<td align="right">40,966,293</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">100,617,010</td>
<td align="right">13.3%</td>
<td align="right">100,626,476</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">73,008,652</td>
<td align="right">9.6%</td>
<td align="right">73,014,616</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">38,980,846</td>
<td align="right">5.1%</td>
<td align="right">38,979,089</td>
<td align="right">5.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,295,968</td>
<td align="right">5.7%</td>
<td align="right">43,297,880</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,511,579</td>
<td align="right">3.6%</td>
<td align="right">27,511,663</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,874,700</td>
<td align="right">10.3%</td>
<td align="right">77,874,595</td>
<td align="right">10.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,874,700</td>
<td align="right">10.3%</td>
<td align="right">77,874,595</td>
<td align="right">10.3%</td>
<td align="right">-0.0%</td>
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
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,297,800,318</td>
<td align="right">68.4%</td>
<td align="right">6,318,387,388</td>
<td align="right">68.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">7,509,905,918</td>
<td align="right">81.5%</td>
<td align="right">7,532,117,372</td>
<td align="right">81.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">474,955,901</td>
<td align="right">5.2%</td>
<td align="right">475,808,497</td>
<td align="right">5.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">2,051,098,018</td>
<td align="right">22.3%</td>
<td align="right">2,053,540,046</td>
<td align="right">22.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">2,055,532,438</td>
<td align="right">22.3%</td>
<td align="right">2,057,974,466</td>
<td align="right">22.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,915,840,830</td>
<td align="right">31.6%</td>
<td align="right">2,918,312,597</td>
<td align="right">31.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,915,840,830</td>
<td align="right">31.6%</td>
<td align="right">2,918,312,597</td>
<td align="right">31.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,654,539</td>
<td align="right">0.8%</td>
<td align="right">71,666,497</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">590,973,810</td>
<td align="right">6.4%</td>
<td align="right">591,017,065</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">28,601,759</td>
<td align="right">0.3%</td>
<td align="right">28,603,543</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,308,392</td>
<td align="right">9.3%</td>
<td align="right">860,338,131</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,380,983</td>
<td align="right">2.3%</td>
<td align="right">211,380,841</td>
<td align="right">2.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,411,620</td>
<td align="right">0.0%</td>
<td align="right">4,411,620</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">22,800</td>
<td align="right">0.0%</td>
<td align="right">22,800</td>
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
<td align="right">4,330,334</td>
<td align="right"></td>
<td align="right">4,212,451</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">68,984,232,612</td>
<td align="right">54.0%</td>
<td align="right">69,531,185,094</td>
<td align="right">54.3%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">71,962,687,994</td>
<td align="right">49.5%</td>
<td align="right">72,490,128,020</td>
<td align="right">49.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,867,883,528</td>
<td align="right"></td>
<td align="right">6,906,646,252</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,866,108,741</td>
<td align="right">37.7%</td>
<td align="right">6,904,835,484</td>
<td align="right">37.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">24,063,183</td>
<td align="right"></td>
<td align="right">23,931,281</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">149,692,832</td>
<td align="right"></td>
<td align="right">150,348,720</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">19,745,718</td>
<td align="right">0.1%</td>
<td align="right">19,820,843</td>
<td align="right">0.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,660,773,180</td>
<td align="right"></td>
<td align="right">2,669,660,403</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">58,742,942,848</td>
<td align="right">46.0%</td>
<td align="right">58,548,298,255</td>
<td align="right">45.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">11,695,314,946</td>
<td align="right"></td>
<td align="right">11,717,990,930</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,346,609,361</td>
<td align="right">62.3%</td>
<td align="right">11,368,120,800</td>
<td align="right">62.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,223,154,188</td>
<td align="right">61.6%</td>
<td align="right">11,244,430,310</td>
<td align="right">61.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">73,454,712,638</td>
<td align="right">50.5%</td>
<td align="right">73,336,324,828</td>
<td align="right">50.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,709,455</td>
<td align="right">0.6%</td>
<td align="right">103,869,647</td>
<td align="right">0.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,216,709,782</td>
<td align="right"></td>
<td align="right">4,220,074,872</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">19,917,537</td>
<td align="right"></td>
<td align="right">19,903,214</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,271,100</td>
<td align="right">2.2%</td>
<td align="right">3,271,100</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">63,880</td>
<td align="right">0.0%</td>
<td align="right">63,880</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">18,591,788</td>
<td align="right">14,455,315,360</td>
<td align="right">0</td>
<td align="right">19,267,460</td>
<td align="right">14,478,210,360</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,753,920</td>
<td align="right">7,058,820,148</td>
<td align="right">0</td>
<td align="right">10,753,920</td>
<td align="right">7,064,790,764</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">685</td>
<td align="right">0.1%</td>
<td align="right">810</td>
<td align="right">0.1%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">438,423</td>
<td align="right">59.5%</td>
<td align="right">442,230</td>
<td align="right">59.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,300</td>
<td align="right">6.2%</td>
<td align="right">6,247</td>
<td align="right">6.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">635,784</td>
<td align="right">86.3%</td>
<td align="right">640,935</td>
<td align="right">86.4%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">45,528</td>
<td align="right">6.2%</td>
<td align="right">45,876</td>
<td align="right">6.2%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">736,755</td>
<td align="right"></td>
<td align="right">742,202</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,745</td>
<td align="right">0.9%</td>
<td align="right">6,787</td>
<td align="right">0.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">197,599,725,577</td>
<td align="right">2,809.6%</td>
<td align="right">196,371,324,518</td>
<td align="right">2,783.5%</td>
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
<td align="right">7,033,045,789</td>
<td align="right"></td>
<td align="right">7,054,852,756</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">100,971</td>
<td align="right">13.7%</td>
<td align="right">101,267</td>
<td align="right">13.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
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
<td align="right">1,280</td>
<td align="right">0.2%</td>
<td align="right">1,280</td>
<td align="right">0.2%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,380</td>
<td align="right">2.4%</td>
<td align="right">2,463</td>
<td align="right">2.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">100,971</td>
<td align="right"></td>
<td align="right">101,267</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">97,371</td>
<td align="right">96.4%</td>
<td align="right">97,584</td>
<td align="right">96.4%</td>
<td align="right">0.2%</td>
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
<td align="right">4,554</td>
<td align="right">4.5%</td>
<td align="right">4,518</td>
<td align="right">4.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">19,538</td>
<td align="right">19.4%</td>
<td align="right">18,952</td>
<td align="right">18.7%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">32,377</td>
<td align="right">32.1%</td>
<td align="right">23,632</td>
<td align="right">23.3%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">24,326</td>
<td align="right">24.1%</td>
<td align="right">27,834</td>
<td align="right">27.5%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">12,819</td>
<td align="right">12.7%</td>
<td align="right">16,561</td>
<td align="right">16.4%</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,857</td>
<td align="right">5.8%</td>
<td align="right">7,369</td>
<td align="right">7.3%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,340</td>
<td align="right">1.3%</td>
<td align="right">2,221</td>
<td align="right">2.2%</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">180</td>
<td align="right">0.2%</td>
<td align="right">12.5%</td>
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
<td align="right">3,674</td>
<td align="right">3.6%</td>
<td align="right">3,678</td>
<td align="right">3.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">13,615</td>
<td align="right">13.5%</td>
<td align="right">13,650</td>
<td align="right">13.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,612</td>
<td align="right">21.4%</td>
<td align="right">16,629</td>
<td align="right">16.4%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">32,077</td>
<td align="right">31.8%</td>
<td align="right">29,210</td>
<td align="right">28.8%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">15,833</td>
<td align="right">15.7%</td>
<td align="right">21,166</td>
<td align="right">20.9%</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,600</td>
<td align="right">7.5%</td>
<td align="right">8,970</td>
<td align="right">8.9%</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,540</td>
<td align="right">2.5%</td>
<td align="right">3,620</td>
<td align="right">3.6%</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">420</td>
<td align="right">0.4%</td>
<td align="right">661</td>
<td align="right">0.7%</td>
<td align="right">57.4%</td>
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
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">168,024,180</td>
<td align="right">158.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">72,648,358</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,540,630,273</td>
<td align="right">1,287,680,362</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">80,094,278</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">779,827,248</td>
<td align="right">421,536,046</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,116,480</td>
<td align="right">3,033,380</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">213,616,640</td>
<td align="right">161,037,180</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">108,946,812</td>
<td align="right">135,245,183</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,376,127,378</td>
<td align="right">1,057,721,761</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">954,373,250</td>
<td align="right">766,736,537</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">22,299,340</td>
<td align="right">25,732,680</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,415,465,678</td>
<td align="right">1,204,245,323</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,183,260,625</td>
<td align="right">1,933,328,570</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">112,098,915</td>
<td align="right">124,326,928</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">689,585,642</td>
<td align="right">624,964,071</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">109,953,578</td>
<td align="right">119,437,172</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">400,405,817</td>
<td align="right">366,609,928</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,265,820,853</td>
<td align="right">2,438,564,655</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,242,410,533</td>
<td align="right">2,411,890,195</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,692,480</td>
<td align="right">843,602,269</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,210</td>
<td align="right">605,158,927</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,549,860</td>
<td align="right">1,212,791,480</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">59,849,615</td>
<td align="right">63,248,514</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,354,584</td>
<td align="right">11,937,025</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,354,584</td>
<td align="right">11,937,025</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">33,060</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,006,295,931</td>
<td align="right">1,045,173,581</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,069,716</td>
<td align="right">33,847,191</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">97,304,350</td>
<td align="right">100,571,176</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">97,548,470</td>
<td align="right">100,815,296</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">410,596,255</td>
<td align="right">423,496,242</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,657,866,657</td>
<td align="right">6,859,688,063</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,940</td>
<td align="right">395,745,869</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,152,732,495</td>
<td align="right">1,177,044,366</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">577,724,159</td>
<td align="right">589,496,386</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,252,821,615</td>
<td align="right">1,277,133,486</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,271,319,575</td>
<td align="right">1,295,907,066</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">873,945,789</td>
<td align="right">889,934,583</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,493,532,108</td>
<td align="right">6,606,069,004</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">112,295,025</td>
<td align="right">114,216,057</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">723,998,357</td>
<td align="right">735,763,793</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,801,448,977</td>
<td align="right">1,829,233,276</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,821,281,305</td>
<td align="right">2,863,835,425</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,999,266</td>
<td align="right">7,103,109</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,671,642,565</td>
<td align="right">1,695,940,466</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,871,481,272</td>
<td align="right">1,845,116,062</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,870,628,622</td>
<td align="right">1,895,317,521</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">263,045,504</td>
<td align="right">266,488,629</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">264,272,324</td>
<td align="right">267,715,449</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,985,269,277</td>
<td align="right">2,011,001,943</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,129,643,291</td>
<td align="right">7,219,666,282</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,941,386</td>
<td align="right">10,043,781</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,318,932,441</td>
<td align="right">1,332,009,181</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">594,001,420</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">114,673,915</td>
<td align="right">115,717,682</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">327,417,307</td>
<td align="right">330,190,912</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,203,377,079</td>
<td align="right">3,229,578,680</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">61,350,400</td>
<td align="right">61,851,380</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">61,236,880</td>
<td align="right">61,715,580</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">185,652,683</td>
<td align="right">187,047,077</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">2,080,847,852</td>
<td align="right">2,094,629,381</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">13,834,493,123</td>
<td align="right">13,918,204,942</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">172,901,620</td>
<td align="right">171,897,986</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">761,841,430</td>
<td align="right">766,054,600</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,182,073,271</td>
<td align="right">2,193,843,701</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,748,060,979</td>
<td align="right">11,802,612,786</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,132,768</td>
<td align="right">202,221,101</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">30,099,010</td>
<td align="right">29,980,006</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,444,969,284</td>
<td align="right">3,457,593,758</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,046,772,519</td>
<td align="right">1,050,241,292</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,720,716,895</td>
<td align="right">5,702,345,693</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">224,128,876</td>
<td align="right">224,804,750</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">29,840</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">73,726,684</td>
<td align="right">73,923,041</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,337,731,556</td>
<td align="right">1,341,178,147</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">128,984,126</td>
<td align="right">129,290,539</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,741,957,227</td>
<td align="right">4,752,069,773</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">168,988,058</td>
<td align="right">169,339,376</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">565,162,549</td>
<td align="right">564,059,334</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">197,867,612</td>
<td align="right">198,234,987</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">16,625,054</td>
<td align="right">16,595,832</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">232,287,042</td>
<td align="right">231,880,464</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,976,358,303</td>
<td align="right">1,979,768,281</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">133,832,527</td>
<td align="right">133,613,544</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">360,361,257</td>
<td align="right">359,776,516</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,952,197,937</td>
<td align="right">4,960,223,375</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,608,579,510</td>
<td align="right">9,622,470,005</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,564,240,237</td>
<td align="right">4,570,504,632</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">550,790,191</td>
<td align="right">551,506,384</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,646,789,572</td>
<td align="right">2,650,215,007</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">24,792,658</td>
<td align="right">24,822,559</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">133,596,528</td>
<td align="right">133,756,392</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">133,596,528</td>
<td align="right">133,756,392</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,877,000</td>
<td align="right">4,872,037</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,384,809,547</td>
<td align="right">1,386,119,219</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">20,499,060</td>
<td align="right">20,517,860</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">541,656,418</td>
<td align="right">542,143,102</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,847,400</td>
<td align="right">61,901,420</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,324,468</td>
<td align="right">126,433,939</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,316,325,323</td>
<td align="right">1,317,399,164</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">714,313,533</td>
<td align="right">714,881,434</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">146,406,599</td>
<td align="right">146,293,017</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,038,255,168</td>
<td align="right">1,039,023,666</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">198,819,442</td>
<td align="right">198,697,755</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">168,958,908</td>
<td align="right">168,859,695</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">171,487,929</td>
<td align="right">171,388,876</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">35,233,740</td>
<td align="right">35,252,540</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,105,403,740</td>
<td align="right">1,105,974,189</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,367,810</td>
<td align="right">78,407,692</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,551,267,954</td>
<td align="right">1,550,481,429</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">217,878,082</td>
<td align="right">217,988,209</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">341,873,628</td>
<td align="right">342,044,222</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">88,970,077</td>
<td align="right">89,010,872</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">485,504,855</td>
<td align="right">485,290,360</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">93,391,265</td>
<td align="right">93,431,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,495,955</td>
<td align="right">93,535,887</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,289,928</td>
<td align="right">779,590,466</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">226,598,859</td>
<td align="right">226,516,158</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">315,070,211</td>
<td align="right">314,955,785</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,938,724,084</td>
<td align="right">2,939,751,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,227,725,870</td>
<td align="right">2,228,471,708</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">333,502,590</td>
<td align="right">333,602,427</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,652,304,982</td>
<td align="right">1,652,778,568</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,345,147,561</td>
<td align="right">1,344,784,683</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,324,983</td>
<td align="right">733,522,485</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,134,060</td>
<td align="right">8,132,040</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,339,505,035</td>
<td align="right">1,339,174,478</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">966,566,959</td>
<td align="right">966,802,594</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">118,371,568</td>
<td align="right">118,343,467</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">129,506,303</td>
<td align="right">129,536,455</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">128,311,463</td>
<td align="right">128,341,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,734,553</td>
<td align="right">229,784,065</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,114,168,240</td>
<td align="right">1,114,374,243</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">592,452,579</td>
<td align="right">592,343,963</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">243,642,160</td>
<td align="right">243,599,469</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">4,437,405</td>
<td align="right">4,436,679</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,610,440</td>
<td align="right">3,609,940</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">6,582,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,940,020</td>
<td align="right">144,958,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">154,019,186</td>
<td align="right">154,000,187</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,095,340,779</td>
<td align="right">2,095,598,515</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">936,562,730</td>
<td align="right">936,669,811</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">444,935</td>
<td align="right">444,985</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,237,704,114</td>
<td align="right">1,237,839,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">843,039,861</td>
<td align="right">843,132,031</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,274,708,581</td>
<td align="right">1,274,605,274</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,695,720</td>
<td align="right">12,694,760</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,599,597</td>
<td align="right">45,603,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">790,266,545</td>
<td align="right">790,322,478</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,260,783,064</td>
<td align="right">3,260,565,114</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,603,025,688</td>
<td align="right">3,603,251,698</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,659,680</td>
<td align="right">5,660,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">147,752,805</td>
<td align="right">147,744,747</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,319,138</td>
<td align="right">32,317,708</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,007,109,032</td>
<td align="right">1,007,152,506</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,719,340</td>
<td align="right">509,697,940</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">330,504,699</td>
<td align="right">330,491,123</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">93,668,040</td>
<td align="right">93,671,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,288,768</td>
<td align="right">54,286,740</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,912,850</td>
<td align="right">9,912,539</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,832,010</td>
<td align="right">101,828,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,416,473,678</td>
<td align="right">6,416,661,303</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,552,660</td>
<td align="right">187,547,900</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">280,841,867</td>
<td align="right">280,835,173</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">485,553,873</td>
<td align="right">485,543,463</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">618,151,905</td>
<td align="right">618,140,024</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,366,939,504</td>
<td align="right">1,366,913,920</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">219,056,993</td>
<td align="right">219,052,949</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">55,151,892</td>
<td align="right">55,150,905</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">63,421,300</td>
<td align="right">63,420,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">382,059,142</td>
<td align="right">382,055,194</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">230,441,900</td>
<td align="right">230,440,220</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,870,776</td>
<td align="right">68,870,291</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,579,820</td>
<td align="right">80,580,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">957,554,216</td>
<td align="right">957,548,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">145,318,660</td>
<td align="right">145,317,980</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,041,708</td>
<td align="right">22,041,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,197,681</td>
<td align="right">97,197,413</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,156,241</td>
<td align="right">98,155,973</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">423,778,513</td>
<td align="right">423,779,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,032,620</td>
<td align="right">533,031,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,816,465,456</td>
<td align="right">1,816,461,062</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">409,583,133</td>
<td align="right">409,582,384</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">647,419</td>
<td align="right">647,418</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,198,030</td>
<td align="right">101,197,927</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">686,558,880</td>
<td align="right">686,558,211</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,038,860</td>
<td align="right">199,038,780</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,868,360</td>
<td align="right">149,868,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">99,814,800</td>
<td align="right">99,814,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">66,194,480</td>
<td align="right">66,194,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">14,734,660</td>
<td align="right">14,734,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,625,240</td>
<td align="right">4,625,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,943,300</td>
<td align="right">1,943,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,889,580</td>
<td align="right">1,889,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,543,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,160</td>
<td align="right">821,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">543,660</td>
<td align="right">543,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">71,760</td>
<td align="right">71,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">7,620</td>
<td align="right">0.0%</td>
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
<td align="left">CALL_LIST_APPEND</td>
<td align="right">4,982</td>
<td align="right">5,074</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">1,500</td>
<td align="right">1,526</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">82,060</td>
<td align="right">82,971</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,140</td>
<td align="right">2,160</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,537</td>
<td align="right">6,589</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,414</td>
<td align="right">2,400</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40,590</td>
<td align="right">40,554</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">32,220</td>
<td align="right">32,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">29,100</td>
<td align="right">29,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,660</td>
<td align="right">1,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,340</td>
<td align="right">1,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">540</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">260</td>
<td align="right">260</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,080</td>
<td align="right">1,085</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,080</td>
<td align="right">1,085</td>
<td align="right">0.5%</td>
</tr>
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
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
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
<td align="right">360</td>
<td align="right">360</td>
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
<td align="right">1,900</td>
<td align="right">1,900</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-05-11
