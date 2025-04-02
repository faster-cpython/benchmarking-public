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
<td align="left">UNPACK_EX</td>
<td align="right">781,020</td>
<td align="right">117,444</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,546</td>
<td align="right">13,935</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">76,988,247</td>
<td align="right">68,707,845</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,485,960</td>
<td align="right">3,797,960</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">75,783</td>
<td align="right">69,511</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">77,368,255</td>
<td align="right">72,320,004</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,642</td>
<td align="right">6,169,720</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,641,205,637</td>
<td align="right">1,544,775,888</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,436,096</td>
<td align="right">7,853,438</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">19,913,969</td>
<td align="right">20,849,322</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,244,967</td>
<td align="right">21,180,320</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,244,947</td>
<td align="right">21,180,299</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,402,620</td>
<td align="right">8,977,136</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,131</td>
<td align="right">5,362</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">211,084,946</td>
<td align="right">201,828,770</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">57,168,545</td>
<td align="right">59,536,290</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">15,696,913</td>
<td align="right">15,109,814</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,614,869</td>
<td align="right">4,444,445</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">73,083,541</td>
<td align="right">70,533,904</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">978,753,941</td>
<td align="right">946,773,227</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">69,465,601</td>
<td align="right">67,422,892</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,781,914</td>
<td align="right">13,379,364</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">772,780</td>
<td align="right">752,961</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">320,016,796</td>
<td align="right">312,949,787</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,048,351</td>
<td align="right">3,114,859</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,299,621</td>
<td align="right">65,891,208</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">319,964,553</td>
<td align="right">314,540,579</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">841,379,934</td>
<td align="right">827,253,707</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,748,401</td>
<td align="right">1,777,530</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,718</td>
<td align="right">34,273</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,181,855</td>
<td align="right">10,999,389</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">519,017,411</td>
<td align="right">511,257,959</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">498,234,048</td>
<td align="right">490,827,293</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">403,084</td>
<td align="right">408,622</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">151</td>
<td align="right">153</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">613,302,895</td>
<td align="right">605,864,148</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">259,137,028</td>
<td align="right">255,997,148</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">850,914,956</td>
<td align="right">840,967,086</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">362,518,624</td>
<td align="right">358,330,355</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">441,286,891</td>
<td align="right">436,219,407</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">226,805,798</td>
<td align="right">224,234,881</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,837,956</td>
<td align="right">72,578,476</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,558,376,936</td>
<td align="right">2,532,297,541</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">794,257,614</td>
<td align="right">786,219,842</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,909,805</td>
<td align="right">35,549,673</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">781,296,353</td>
<td align="right">774,004,937</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">133,116</td>
<td align="right">134,205</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">99,822,131</td>
<td align="right">100,634,076</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,472,111,629</td>
<td align="right">1,460,939,403</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,093,413,053</td>
<td align="right">2,078,201,870</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,760,047</td>
<td align="right">57,353,146</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,260,512,864</td>
<td align="right">1,251,960,913</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,427,851,306</td>
<td align="right">5,392,669,912</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,345,828,456</td>
<td align="right">3,324,189,310</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">115,707,789</td>
<td align="right">114,963,244</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">154,918,570</td>
<td align="right">155,901,994</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,212,484,364</td>
<td align="right">3,192,653,677</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,312,564,582</td>
<td align="right">6,274,613,568</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,145,269,710</td>
<td align="right">2,133,042,650</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,245,104,424</td>
<td align="right">2,232,809,485</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">37,462,739,403</td>
<td align="right">37,258,858,547</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,870,755,714</td>
<td align="right">3,849,735,887</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">72,893,420</td>
<td align="right">73,273,097</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,966,161</td>
<td align="right">8,919,619</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">62,690,169</td>
<td align="right">62,365,653</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,262,591,328</td>
<td align="right">1,256,291,488</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,745</td>
<td align="right">121,332</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">815,430,156</td>
<td align="right">811,501,208</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,782,040,165</td>
<td align="right">5,755,580,088</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,126,718</td>
<td align="right">154,828,624</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,036,669,762</td>
<td align="right">1,031,957,930</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,728,452,420</td>
<td align="right">10,679,855,216</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,211,826,517</td>
<td align="right">1,206,497,945</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,231,994</td>
<td align="right">61,961,443</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,441,023</td>
<td align="right">121,913,872</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,627,604,129</td>
<td align="right">1,620,599,406</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,179,234,138</td>
<td align="right">3,166,043,077</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">568,757,255</td>
<td align="right">566,531,067</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,754,939,451</td>
<td align="right">2,744,529,557</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">502,390,334</td>
<td align="right">500,572,224</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">246,206,236</td>
<td align="right">245,330,966</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">94,673,539</td>
<td align="right">95,008,461</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">918,183,417</td>
<td align="right">914,937,150</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">388,440,825</td>
<td align="right">387,103,768</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,444,765</td>
<td align="right">67,216,972</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,662,823,173</td>
<td align="right">1,657,376,365</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,117,237,252</td>
<td align="right">1,113,739,217</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">287,972,846</td>
<td align="right">287,099,564</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">264,244,074</td>
<td align="right">263,476,228</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,466,303</td>
<td align="right">180,939,105</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,494,211,007</td>
<td align="right">3,484,115,429</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,700,760</td>
<td align="right">7,678,574</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,303,049</td>
<td align="right">591,621,572</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,828,736</td>
<td align="right">1,823,676</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,843,577</td>
<td align="right">415,697,017</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">667,342,199</td>
<td align="right">665,590,378</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,712,095</td>
<td align="right">418,615,353</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">981,112,176</td>
<td align="right">983,576,665</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">175,226,733</td>
<td align="right">174,795,399</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">6,505,287,770</td>
<td align="right">6,489,827,831</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">537,372,490</td>
<td align="right">538,638,242</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,036,969</td>
<td align="right">156,396,533</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,759,948,520</td>
<td align="right">5,746,809,931</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">167,721,657</td>
<td align="right">168,089,892</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">405,487,003</td>
<td align="right">404,602,111</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">63,646,843</td>
<td align="right">63,510,295</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,476,539</td>
<td align="right">369,813,929</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">23,493,127</td>
<td align="right">23,453,159</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,841,489</td>
<td align="right">98,690,049</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,698,391,024</td>
<td align="right">1,700,962,539</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">349,751,079</td>
<td align="right">349,229,688</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">244,369,408</td>
<td align="right">244,006,518</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,484,398,849</td>
<td align="right">13,464,388,357</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">246,425,974</td>
<td align="right">246,063,088</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,314,739,545</td>
<td align="right">7,305,154,954</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,534,606,443</td>
<td align="right">2,531,467,979</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">519,877,599</td>
<td align="right">519,245,788</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,295,449</td>
<td align="right">62,370,330</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,606,849</td>
<td align="right">302,246,650</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,197,924,482</td>
<td align="right">2,195,430,077</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,152</td>
<td align="right">57,215</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">331,010,384</td>
<td align="right">330,683,545</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">101,013,908</td>
<td align="right">100,917,200</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,380,578,288</td>
<td align="right">1,379,282,886</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,047,693,709</td>
<td align="right">11,037,437,489</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,621</td>
<td align="right">3,618</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">89,859,109</td>
<td align="right">89,787,293</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,720,855,053</td>
<td align="right">2,719,038,170</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,552</td>
<td align="right">84,496</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,437,923</td>
<td align="right">180,330,824</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,844,393,927</td>
<td align="right">4,846,961,347</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">630,304,335</td>
<td align="right">630,606,748</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,717,642</td>
<td align="right">340,563,496</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,115,382,209</td>
<td align="right">1,115,864,779</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,756,110,982</td>
<td align="right">1,755,354,852</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,483,880,497</td>
<td align="right">2,482,955,648</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,534,715,249</td>
<td align="right">1,534,161,646</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">92,825,934</td>
<td align="right">92,859,235</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,275,608,759</td>
<td align="right">1,275,204,653</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">78,127,835</td>
<td align="right">78,104,354</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">356,233,745</td>
<td align="right">356,337,196</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,129,138</td>
<td align="right">115,162,430</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,758,308</td>
<td align="right">14,762,483</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">270,947,204</td>
<td align="right">271,022,065</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">223,498,987</td>
<td align="right">223,554,886</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">331,966,412</td>
<td align="right">332,038,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,586,429,326</td>
<td align="right">1,586,089,382</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,078,492,497</td>
<td align="right">1,078,721,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,605,301</td>
<td align="right">504,551,034</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,404,134,434</td>
<td align="right">1,403,996,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">137,244,968</td>
<td align="right">137,258,098</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,171,338,755</td>
<td align="right">3,171,072,676</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">701,010,540</td>
<td align="right">701,064,451</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">379,235,348</td>
<td align="right">379,259,978</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">83,601,640</td>
<td align="right">83,606,424</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">183,114,867</td>
<td align="right">183,122,443</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">292,913,171</td>
<td align="right">292,922,479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">194,819,633</td>
<td align="right">194,822,986</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">77,223,254</td>
<td align="right">77,223,659</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,669</td>
<td align="right">9,742,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">566,125,897</td>
<td align="right">566,124,589</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,081</td>
<td align="right">128,850,117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,824</td>
<td align="right">127,568,803</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,955,614</td>
<td align="right">74,955,607</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,417,278</td>
<td align="right">131,417,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,436,108</td>
<td align="right">1,053,436,107</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,191</td>
<td align="right">188,535,191</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">156,807,836</td>
<td align="right">156,807,836</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,686,498</td>
<td align="right">112,686,498</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">100,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,671</td>
<td align="right">41,964,671</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right">29,134,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">29,134,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,976,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">6,152,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,644,310</td>
<td align="right">1,644,310</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,608</td>
<td align="right">98,608</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,624</td>
<td align="right">56,624</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,265</td>
<td align="right">5,265</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,897</td>
<td align="right">3,897</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,646</td>
<td align="right">2,646</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">42</td>
<td align="right">42</td>
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
<td align="right">13,143,796,836</td>
<td align="right">80.3%</td>
<td align="right">13,118,714,154</td>
<td align="right">80.2%</td>
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
<td align="right">59,001,051</td>
<td align="right">0.4%</td>
<td align="right">58,921,715</td>
<td align="right">0.4%</td>
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
<td align="right">3,170,305,809</td>
<td align="right">19.4%</td>
<td align="right">3,170,037,810</td>
<td align="right">19.4%</td>
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
<td align="right">1,129,780</td>
<td align="right">52.6%</td>
<td align="right">1,128,536</td>
<td align="right">52.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,016,135</td>
<td align="right">47.4%</td>
<td align="right">1,016,105</td>
<td align="right">47.4%</td>
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
<td align="left">subscr</td>
<td align="right">351,006</td>
<td align="right">34.5%</td>
<td align="right">349,269</td>
<td align="right">34.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">630</td>
<td align="right">0.1%</td>
<td align="right">632</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,256</td>
<td align="right">0.1%</td>
<td align="right">1,254</td>
<td align="right">0.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">43,376</td>
<td align="right">4.3%</td>
<td align="right">43,424</td>
<td align="right">4.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,969</td>
<td align="right">3.3%</td>
<td align="right">33,945</td>
<td align="right">3.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,830</td>
<td align="right">4.3%</td>
<td align="right">43,860</td>
<td align="right">4.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">3,607</td>
<td align="right">0.4%</td>
<td align="right">3,609</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,037</td>
<td align="right">0.2%</td>
<td align="right">2,036</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">12,452</td>
<td align="right">1.2%</td>
<td align="right">12,456</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">7,223</td>
<td align="right">0.7%</td>
<td align="right">7,225</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,191</td>
<td align="right">7.3%</td>
<td align="right">74,202</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">193,731</td>
<td align="right">19.1%</td>
<td align="right">193,754</td>
<td align="right">19.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,513</td>
<td align="right">0.8%</td>
<td align="right">8,514</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,510</td>
<td align="right">2.3%</td>
<td align="right">23,511</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,612</td>
<td align="right">3.6%</td>
<td align="right">36,613</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">8.4%</td>
<td align="right">85,543</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">47,024</td>
<td align="right">4.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">1.9%</td>
<td align="right">19,448</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">1.1%</td>
<td align="right">11,587</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">0.8%</td>
<td align="right">8,203</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,154</td>
<td align="right">0.3%</td>
<td align="right">3,154</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.3%</td>
<td align="right">2,678</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.1%</td>
<td align="right">1,384</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">597</td>
<td align="right">0.1%</td>
<td align="right">597</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">399</td>
<td align="right">0.0%</td>
<td align="right">399</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or int</td>
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
<td align="right">181,466,303</td>
<td align="right">100.0%</td>
<td align="right">180,939,105</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
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
<td align="right">154,978,941</td>
<td align="right">1.4%</td>
<td align="right">154,202,401</td>
<td align="right">1.4%</td>
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
<td align="right">152,285,871</td>
<td align="right">1.4%</td>
<td align="right">151,525,553</td>
<td align="right">1.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,113,140,154</td>
<td align="right">98.6%</td>
<td align="right">11,066,489,808</td>
<td align="right">98.6%</td>
<td align="right">-0.4%</td>
</tr>
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
<td align="right">8,513</td>
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
<td align="right">3,095,708</td>
<td align="right">100.0%</td>
<td align="right">3,085,024</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">446</td>
<td align="right">0.0%</td>
<td align="right">446</td>
<td align="right">0.0%</td>
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
<td align="left">init not simple</td>
<td align="right">752</td>
<td align="right">168.6%</td>
<td align="right">752</td>
<td align="right">168.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right">267</td>
<td align="right">59.9%</td>
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
<td align="right">684,442</td>
<td align="right">97.1%</td>
<td align="right">684,591</td>
<td align="right">97.1%</td>
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
<td align="right">583,856</td>
<td align="right">82.9%</td>
<td align="right">583,856</td>
<td align="right">82.8%</td>
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
<td align="right">20,039</td>
<td align="right">99.4%</td>
<td align="right">20,477</td>
<td align="right">99.4%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">0.6%</td>
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
<td align="right">1,291,341</td>
<td align="right">0.0%</td>
<td align="right">1,367,567</td>
<td align="right">0.0%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">518,793,128</td>
<td align="right">10.3%</td>
<td align="right">511,029,114</td>
<td align="right">10.2%</td>
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
<td align="right">4,528,612,627</td>
<td align="right">89.7%</td>
<td align="right">4,517,786,563</td>
<td align="right">89.8%</td>
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
<td align="right">42,081</td>
<td align="right">16.9%</td>
<td align="right">43,671</td>
<td align="right">17.2%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">206,371</td>
<td align="right">83.1%</td>
<td align="right">210,655</td>
<td align="right">82.8%</td>
<td align="right">2.1%</td>
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
<td align="right">38,965</td>
<td align="right">18.9%</td>
<td align="right">45,790</td>
<td align="right">21.7%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">11,949</td>
<td align="right">5.8%</td>
<td align="right">10,412</td>
<td align="right">4.9%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,230</td>
<td align="right">6.9%</td>
<td align="right">13,235</td>
<td align="right">6.3%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,024</td>
<td align="right">0.5%</td>
<td align="right">1,004</td>
<td align="right">0.5%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,029</td>
<td align="right">1.0%</td>
<td align="right">2,007</td>
<td align="right">1.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,767</td>
<td align="right">3.8%</td>
<td align="right">7,784</td>
<td align="right">3.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,820</td>
<td align="right">3.3%</td>
<td align="right">6,832</td>
<td align="right">3.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">3.7%</td>
<td align="right">7,648</td>
<td align="right">3.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,370</td>
<td align="right">11.3%</td>
<td align="right">23,357</td>
<td align="right">11.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">90,855</td>
<td align="right">44.0%</td>
<td align="right">90,863</td>
<td align="right">43.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,367</td>
<td align="right">0.7%</td>
<td align="right">1,367</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.2%</td>
<td align="right">356</td>
<td align="right">0.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
<td align="right">1,395,959</td>
<td align="right">0.1%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">154,857,353</td>
<td align="right">6.6%</td>
<td align="right">155,840,497</td>
<td align="right">6.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,195,480,886</td>
<td align="right">93.3%</td>
<td align="right">2,190,178,300</td>
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
<td align="left">Success</td>
<td align="right">38,233</td>
<td align="right">39.3%</td>
<td align="right">28,464</td>
<td align="right">32.4%</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,158</td>
<td align="right">60.7%</td>
<td align="right">59,376</td>
<td align="right">67.6%</td>
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
<td align="left">list</td>
<td align="right">14,561</td>
<td align="right">24.6%</td>
<td align="right">14,643</td>
<td align="right">24.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">21,281</td>
<td align="right">36.0%</td>
<td align="right">21,380</td>
<td align="right">36.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,596</td>
<td align="right">19.6%</td>
<td align="right">11,648</td>
<td align="right">19.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,720</td>
<td align="right">19.8%</td>
<td align="right">11,705</td>
<td align="right">19.7%</td>
<td align="right">-0.1%</td>
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
<td align="right">1,471,676,089</td>
<td align="right">28.9%</td>
<td align="right">1,460,506,202</td>
<td align="right">28.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,447,787,938</td>
<td align="right">67.8%</td>
<td align="right">3,445,995,126</td>
<td align="right">68.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">164,019,605</td>
<td align="right">3.2%</td>
<td align="right">164,010,907</td>
<td align="right">3.2%</td>
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
<td align="right">430,477</td>
<td align="right">12.2%</td>
<td align="right">428,016</td>
<td align="right">12.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,099,603</td>
<td align="right">87.8%</td>
<td align="right">3,099,554</td>
<td align="right">87.9%</td>
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
<td align="left">ascii string</td>
<td align="right">3,390</td>
<td align="right">0.8%</td>
<td align="right">3,153</td>
<td align="right">0.7%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">71,088</td>
<td align="right">16.5%</td>
<td align="right">69,077</td>
<td align="right">16.1%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,911</td>
<td align="right">1.6%</td>
<td align="right">6,954</td>
<td align="right">1.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,601</td>
<td align="right">1.1%</td>
<td align="right">4,583</td>
<td align="right">1.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,556</td>
<td align="right">4.5%</td>
<td align="right">19,498</td>
<td align="right">4.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,139</td>
<td align="right">0.7%</td>
<td align="right">3,147</td>
<td align="right">0.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,954</td>
<td align="right">19.5%</td>
<td align="right">83,794</td>
<td align="right">19.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,825</td>
<td align="right">2.5%</td>
<td align="right">10,816</td>
<td align="right">2.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,970</td>
<td align="right">8.1%</td>
<td align="right">34,949</td>
<td align="right">8.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">172,123</td>
<td align="right">40.0%</td>
<td align="right">172,125</td>
<td align="right">40.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,269</td>
<td align="right">4.2%</td>
<td align="right">18,269</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">254</td>
<td align="right">0.1%</td>
<td align="right">254</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right">174</td>
<td align="right">0.0%</td>
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
<td align="right">1,378,316</td>
<td align="right">0.0%</td>
<td align="right">1,263,385</td>
<td align="right">0.0%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">849,070,959</td>
<td align="right">6.1%</td>
<td align="right">839,117,522</td>
<td align="right">6.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,166,814,111</td>
<td align="right">87.6%</td>
<td align="right">12,032,417,987</td>
<td align="right">87.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">868,020,080</td>
<td align="right">6.3%</td>
<td align="right">865,911,926</td>
<td align="right">6.3%</td>
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
<td align="right">16,458,777</td>
<td align="right">96.7%</td>
<td align="right">16,423,516</td>
<td align="right">96.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">564,295</td>
<td align="right">3.3%</td>
<td align="right">564,065</td>
<td align="right">3.3%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">6,140</td>
<td align="right">1.1%</td>
<td align="right">6,058</td>
<td align="right">1.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,200</td>
<td align="right">0.2%</td>
<td align="right">1,206</td>
<td align="right">0.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">57,872</td>
<td align="right">10.3%</td>
<td align="right">57,614</td>
<td align="right">10.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,633</td>
<td align="right">2.9%</td>
<td align="right">16,676</td>
<td align="right">3.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,729</td>
<td align="right">0.5%</td>
<td align="right">2,736</td>
<td align="right">0.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">81,340</td>
<td align="right">14.4%</td>
<td align="right">81,519</td>
<td align="right">14.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.2%</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">66,580</td>
<td align="right">11.8%</td>
<td align="right">66,524</td>
<td align="right">11.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,801</td>
<td align="right">0.3%</td>
<td align="right">1,802</td>
<td align="right">0.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,167</td>
<td align="right">1.6%</td>
<td align="right">9,172</td>
<td align="right">1.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">25,262</td>
<td align="right">4.5%</td>
<td align="right">25,268</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,087</td>
<td align="right">0.9%</td>
<td align="right">5,088</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.1%</td>
<td align="right">6,405</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,513</td>
<td align="right">0.3%</td>
<td align="right">1,513</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.0%</td>
<td align="right">235</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">163</td>
<td align="right">0.0%</td>
<td align="right">163</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">53,190</td>
<td align="right">0.0%</td>
<td align="right">53,875</td>
<td align="right">0.0%</td>
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
<td align="right">9,127,815,431</td>
<td align="right">99.8%</td>
<td align="right">9,079,715,523</td>
<td align="right">99.8%</td>
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
<td align="right">14,622,690</td>
<td align="right">0.2%</td>
<td align="right">14,623,790</td>
<td align="right">0.2%</td>
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
<td align="right">1,508</td>
<td align="right">0.0%</td>
<td align="right">1,508</td>
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
<td align="right">136,381</td>
<td align="right">100.0%</td>
<td align="right">139,471</td>
<td align="right">100.0%</td>
<td align="right">2.3%</td>
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
<td align="right">65,738,520</td>
<td align="right">100.0%</td>
<td align="right">65,480,512</td>
<td align="right">100.0%</td>
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
<td align="right">252</td>
<td align="right">0.0%</td>
<td align="right">252</td>
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
<td align="right">2,394</td>
<td align="right">100.0%</td>
<td align="right">2,394</td>
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
<td align="right">593,288,338</td>
<td align="right">82.2%</td>
<td align="right">591,606,861</td>
<td align="right">82.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,815,291</td>
<td align="right">17.8%</td>
<td align="right">128,815,319</td>
<td align="right">17.9%</td>
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
<td align="right">14,711</td>
<td align="right">0.0%</td>
<td align="right">14,711</td>
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
<td align="right">651</td>
<td align="right">1.9%</td>
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
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
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right">752</td>
<td align="right">2.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,853,567,735</td>
<td align="right">90.6%</td>
<td align="right">1,825,558,157</td>
<td align="right">90.5%</td>
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
<td align="right">115,275,223</td>
<td align="right">5.6%</td>
<td align="right">113,768,576</td>
<td align="right">5.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">77,129,938</td>
<td align="right">3.8%</td>
<td align="right">77,130,101</td>
<td align="right">3.8%</td>
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
<td align="right">2,214,892</td>
<td align="right">97.7%</td>
<td align="right">2,186,478</td>
<td align="right">97.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">52,744</td>
<td align="right">2.3%</td>
<td align="right">52,743</td>
<td align="right">2.4%</td>
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
<td align="left">not managed dict</td>
<td align="right">3,346</td>
<td align="right">6.3%</td>
<td align="right">3,350</td>
<td align="right">6.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">270,935</td>
<td align="right">513.7%</td>
<td align="right">270,879</td>
<td align="right">513.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">46.4%</td>
<td align="right">24,476</td>
<td align="right">46.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.5%</td>
<td align="right">7,666</td>
<td align="right">14.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">6,012</td>
<td align="right">11.4%</td>
<td align="right">6,012</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,322</td>
<td align="right">10.1%</td>
<td align="right">5,322</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">811</td>
<td align="right">1.5%</td>
<td align="right">811</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
<td align="right">112,686,498</td>
<td align="right">100.0%</td>
<td align="right">112,686,498</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">922,357,422</td>
<td align="right">56.8%</td>
<td align="right">922,459,565</td>
<td align="right">56.8%</td>
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
<td align="right">700,826,206</td>
<td align="right">43.2%</td>
<td align="right">700,880,069</td>
<td align="right">43.2%</td>
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
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">2,220</td>
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
<td align="right">2,075</td>
<td align="right">1.1%</td>
<td align="right">2,121</td>
<td align="right">1.2%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">182,299</td>
<td align="right">98.9%</td>
<td align="right">182,301</td>
<td align="right">98.8%</td>
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
<td align="right">3,031</td>
<td align="right">1.7%</td>
<td align="right">3,032</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">9.5%</td>
<td align="right">17,324</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">86,613</td>
<td align="right">47.5%</td>
<td align="right">86,613</td>
<td align="right">47.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.8%</td>
<td align="right">48,931</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,343</td>
<td align="right">10.6%</td>
<td align="right">19,343</td>
<td align="right">10.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,309</td>
<td align="right">2.9%</td>
<td align="right">5,309</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">0.9%</td>
<td align="right">1,681</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">68</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">112,359,783</td>
<td align="right">2.2%</td>
<td align="right">110,031,800</td>
<td align="right">2.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,735,727,520</td>
<td align="right">92.6%</td>
<td align="right">4,700,272,574</td>
<td align="right">92.6%</td>
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
<td align="right">263,562,973</td>
<td align="right">5.2%</td>
<td align="right">262,794,047</td>
<td align="right">5.2%</td>
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
<td align="right">2,167,969</td>
<td align="right">77.4%</td>
<td align="right">2,125,107</td>
<td align="right">77.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">631,594</td>
<td align="right">22.6%</td>
<td align="right">631,470</td>
<td align="right">22.9%</td>
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
<td align="left">sequence</td>
<td align="right">10,053</td>
<td align="right">1.6%</td>
<td align="right">10,011</td>
<td align="right">1.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">20,551</td>
<td align="right">3.3%</td>
<td align="right">20,481</td>
<td align="right">3.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,283</td>
<td align="right">2.1%</td>
<td align="right">13,301</td>
<td align="right">2.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">132,987</td>
<td align="right">21.1%</td>
<td align="right">132,929</td>
<td align="right">21.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">97,664</td>
<td align="right">15.5%</td>
<td align="right">97,696</td>
<td align="right">15.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">77,652</td>
<td align="right">12.3%</td>
<td align="right">77,645</td>
<td align="right">12.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,640</td>
<td align="right">41.0%</td>
<td align="right">258,643</td>
<td align="right">41.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,878</td>
<td align="right">3.0%</td>
<td align="right">18,878</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">0.0%</td>
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
<td align="right">1,249,075,105</td>
<td align="right">99.9%</td>
<td align="right">1,240,973,678</td>
<td align="right">99.9%</td>
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
<td align="right">1,816,301</td>
<td align="right">0.1%</td>
<td align="right">1,811,134</td>
<td align="right">0.1%</td>
<td align="right">-0.3%</td>
</tr>
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
<td align="right">3,700</td>
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
<td align="right">992</td>
<td align="right">7.9%</td>
<td align="right">1,003</td>
<td align="right">7.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,523</td>
<td align="right">92.1%</td>
<td align="right">11,619</td>
<td align="right">92.1%</td>
<td align="right">0.8%</td>
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
<td align="right">91</td>
<td align="right">9.2%</td>
<td align="right">98</td>
<td align="right">9.8%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">765</td>
<td align="right">77.1%</td>
<td align="right">769</td>
<td align="right">76.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">13.7%</td>
<td align="right">136</td>
<td align="right">13.6%</td>
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
<td align="right">1,477,646,231</td>
<td align="right">0.7%</td>
<td align="right">1,470,395,261</td>
<td align="right">0.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">86,697,870,050</td>
<td align="right">41.0%</td>
<td align="right">86,272,435,293</td>
<td align="right">41.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">7,650,895,590</td>
<td align="right">3.6%</td>
<td align="right">7,621,497,935</td>
<td align="right">3.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">115,439,766,803</td>
<td align="right">54.6%</td>
<td align="right">114,998,177,821</td>
<td align="right">54.7%</td>
<td align="right">-0.4%</td>
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
<td align="right">518,793,128</td>
<td align="right">6.7%</td>
<td align="right">511,029,114</td>
<td align="right">6.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">849,070,959</td>
<td align="right">10.9%</td>
<td align="right">839,117,522</td>
<td align="right">10.8%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,471,676,089</td>
<td align="right">18.9%</td>
<td align="right">1,460,506,202</td>
<td align="right">18.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">154,857,353</td>
<td align="right">2.0%</td>
<td align="right">155,840,497</td>
<td align="right">2.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">152,285,871</td>
<td align="right">2.0%</td>
<td align="right">151,525,553</td>
<td align="right">2.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">263,562,973</td>
<td align="right">3.4%</td>
<td align="right">262,794,047</td>
<td align="right">3.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,466,303</td>
<td align="right">2.3%</td>
<td align="right">180,939,105</td>
<td align="right">2.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,170,305,809</td>
<td align="right">40.7%</td>
<td align="right">3,170,037,810</td>
<td align="right">40.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,826,206</td>
<td align="right">9.0%</td>
<td align="right">700,880,069</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,291</td>
<td align="right">1.7%</td>
<td align="right">128,815,319</td>
<td align="right">1.7%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">90,673,020</td>
<td align="right">6.1%</td>
<td align="right">87,397,553</td>
<td align="right">5.9%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,766,324</td>
<td align="right">3.4%</td>
<td align="right">48,564,807</td>
<td align="right">3.3%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">55,251,781</td>
<td align="right">3.7%</td>
<td align="right">54,401,832</td>
<td align="right">3.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">86,866,092</td>
<td align="right">5.9%</td>
<td align="right">85,607,842</td>
<td align="right">5.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">92,955,862</td>
<td align="right">6.3%</td>
<td align="right">94,262,682</td>
<td align="right">6.4%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">365,470,123</td>
<td align="right">24.7%</td>
<td align="right">368,072,121</td>
<td align="right">25.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">82,321,341</td>
<td align="right">5.6%</td>
<td align="right">81,950,892</td>
<td align="right">5.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">266,301,637</td>
<td align="right">18.0%</td>
<td align="right">266,134,715</td>
<td align="right">18.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,930,179</td>
<td align="right">5.5%</td>
<td align="right">81,923,011</td>
<td align="right">5.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,012,031</td>
<td align="right">5.5%</td>
<td align="right">82,010,501</td>
<td align="right">5.6%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,424,355</td>
<td align="right">4.1%</td>
<td align="right">276,058,366</td>
<td align="right">4.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,484,642,299</td>
<td align="right">81.1%</td>
<td align="right">5,449,790,268</td>
<td align="right">81.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,126,649,164</td>
<td align="right">75.9%</td>
<td align="right">5,094,556,834</td>
<td align="right">75.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">948,822,948</td>
<td align="right">14.0%</td>
<td align="right">943,869,395</td>
<td align="right">14.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">953,100,287</td>
<td align="right">14.1%</td>
<td align="right">948,146,735</td>
<td align="right">14.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,632,095,780</td>
<td align="right">24.1%</td>
<td align="right">1,625,091,091</td>
<td align="right">24.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,632,095,780</td>
<td align="right">24.1%</td>
<td align="right">1,625,091,091</td>
<td align="right">24.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,789,958</td>
<td align="right">1.0%</td>
<td align="right">71,062,809</td>
<td align="right">1.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">678,995,493</td>
<td align="right">10.0%</td>
<td align="right">676,944,356</td>
<td align="right">10.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,412,082</td>
<td align="right">3.9%</td>
<td align="right">260,685,995</td>
<td align="right">3.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,921,224</td>
<td align="right">0.4%</td>
<td align="right">24,892,787</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">4,273,443</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,897</td>
<td align="right">0.0%</td>
<td align="right">3,897</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,402</td>
<td align="right">2.0%</td>
<td align="right">132,513,402</td>
<td align="right">2.0%</td>
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
<td align="left">Method cache misses</td>
<td align="right">71,319,402</td>
<td align="right"></td>
<td align="right">59,838,192</td>
<td align="right"></td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">78,445,866</td>
<td align="right"></td>
<td align="right">67,131,107</td>
<td align="right"></td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">434,343</td>
<td align="right">0.2%</td>
<td align="right">475,943</td>
<td align="right">0.3%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,933,213</td>
<td align="right"></td>
<td align="right">8,096,854</td>
<td align="right"></td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,905,192,672</td>
<td align="right"></td>
<td align="right">2,874,776,679</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">79,615,979,235</td>
<td align="right">51.6%</td>
<td align="right">79,214,129,350</td>
<td align="right">51.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">89,009,003,628</td>
<td align="right">46.5%</td>
<td align="right">88,562,868,512</td>
<td align="right">46.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">21,962,265,614</td>
<td align="right">14.2%</td>
<td align="right">21,857,680,939</td>
<td align="right">14.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">25,275,421,311</td>
<td align="right">16.4%</td>
<td align="right">25,156,612,916</td>
<td align="right">16.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,274,138,732</td>
<td align="right"></td>
<td align="right">2,264,425,016</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">23,821,673,194</td>
<td align="right">12.5%</td>
<td align="right">23,725,421,526</td>
<td align="right">12.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,015,735,565</td>
<td align="right">32.5%</td>
<td align="right">5,993,534,494</td>
<td align="right">32.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,093,673,839</td>
<td align="right">32.9%</td>
<td align="right">6,071,510,878</td>
<td align="right">32.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">32,956,908,579</td>
<td align="right">17.2%</td>
<td align="right">32,838,504,165</td>
<td align="right">17.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,039,414</td>
<td align="right"></td>
<td align="right">178,418,018</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">27,475,017,789</td>
<td align="right">17.8%</td>
<td align="right">27,382,993,103</td>
<td align="right">17.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,686,278,010</td>
<td align="right"></td>
<td align="right">6,664,520,684</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">45,486,112,061</td>
<td align="right">23.8%</td>
<td align="right">45,358,934,047</td>
<td align="right">23.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,431,011,237</td>
<td align="right">67.1%</td>
<td align="right">12,405,396,468</td>
<td align="right">67.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,431,108,865</td>
<td align="right"></td>
<td align="right">12,405,496,641</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,517,367</td>
<td align="right">0.4%</td>
<td align="right">71,555,528</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,420,907</td>
<td align="right">0.0%</td>
<td align="right">6,420,856</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,443,359</td>
<td align="right">2.5%</td>
<td align="right">4,443,360</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
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
<td align="right">365,393</td>
<td align="right">102,601,494</td>
<td align="right">9,550,686,301</td>
<td align="right">757,529,297</td>
<td align="right">764,970,842</td>
<td align="right">365,128</td>
<td align="right">102,419,298</td>
<td align="right">9,567,803,852</td>
<td align="right">757,851,190</td>
<td align="right">765,958,140</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,438</td>
<td align="right">5,601,646,604</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,438</td>
<td align="right">5,631,251,086</td>
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
<td align="right">22,629</td>
<td align="right">22,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">30</td>
<td align="right">30</td>
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
<td align="right">37</td>
<td align="right">37</td>
<td align="right">0.0%</td>
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
<td align="right">2,476</td>
<td align="right">2,479</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-02
