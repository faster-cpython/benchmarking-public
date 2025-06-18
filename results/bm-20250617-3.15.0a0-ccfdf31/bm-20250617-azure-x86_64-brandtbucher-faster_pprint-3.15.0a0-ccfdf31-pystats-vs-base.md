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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">675,483,619</td>
<td align="right">560,344,376</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,243,760,138</td>
<td align="right">1,128,569,522</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">690,673,305</td>
<td align="right">633,094,897</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,587,146,889</td>
<td align="right">1,529,586,560</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,380,222,431</td>
<td align="right">3,264,769,550</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,887,040,006</td>
<td align="right">3,829,583,134</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,358,038,367</td>
<td align="right">5,300,600,741</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,837,919,763</td>
<td align="right">5,780,695,919</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,239,843,367</td>
<td align="right">6,182,314,974</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">232,167</td>
<td align="right">233,988</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,108,716,650</td>
<td align="right">10,051,234,439</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,671,860,784</td>
<td align="right">10,614,421,144</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">33,485,441,056</td>
<td align="right">33,428,124,492</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">76,669</td>
<td align="right">76,781</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,350</td>
<td align="right">5,357</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">463,549</td>
<td align="right">464,039</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">14,803</td>
<td align="right">14,816</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,553,244</td>
<td align="right">28,573,238</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">261,760,363</td>
<td align="right">261,645,816</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">536,441,138</td>
<td align="right">536,224,241</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">533,406,829</td>
<td align="right">533,197,076</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,332,726</td>
<td align="right">67,358,311</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">353,984,335</td>
<td align="right">353,851,011</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,497,563</td>
<td align="right">70,523,391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">334,962,364</td>
<td align="right">334,854,823</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,418,034</td>
<td align="right">190,364,924</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">840,494,592</td>
<td align="right">840,728,737</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">795,069,017</td>
<td align="right">794,850,474</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">66,513,439</td>
<td align="right">66,496,211</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">116,378,642</td>
<td align="right">116,405,169</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,688</td>
<td align="right">33,695</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">317,963,205</td>
<td align="right">318,023,243</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,430,282</td>
<td align="right">5,431,281</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,954,695</td>
<td align="right">35,961,145</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">65,675,864</td>
<td align="right">65,686,810</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,437,953</td>
<td align="right">98,453,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,812,598</td>
<td align="right">153,790,819</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,656,963</td>
<td align="right">1,657,177</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,096,557</td>
<td align="right">10,097,854</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">72,287,092</td>
<td align="right">72,296,336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,704,408</td>
<td align="right">12,705,994</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">201,369,791</td>
<td align="right">201,394,777</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,454,285</td>
<td align="right">370,410,714</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">56,899,383</td>
<td align="right">56,905,614</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">115,321,074</td>
<td align="right">115,333,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">75,632,196</td>
<td align="right">75,640,222</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">468,004,690</td>
<td align="right">468,053,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,361,229</td>
<td align="right">62,367,662</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">233,805,709</td>
<td align="right">233,829,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,682,683</td>
<td align="right">122,694,622</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,214,361,620</td>
<td align="right">1,214,471,283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,542,250,853</td>
<td align="right">1,542,381,343</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,112,129,472</td>
<td align="right">1,112,038,871</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,630</td>
<td align="right">12,631</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">346,666,986</td>
<td align="right">346,693,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,304,402</td>
<td align="right">416,335,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,358,157,534</td>
<td align="right">1,358,057,864</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">377,653,289</td>
<td align="right">377,629,053</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">256,554,405</td>
<td align="right">256,569,799</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,630,867</td>
<td align="right">510,661,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,123,986,285</td>
<td align="right">2,123,865,654</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,942,701</td>
<td align="right">419,966,414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">190,487,643</td>
<td align="right">190,498,130</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">485,158,938</td>
<td align="right">485,185,529</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,531,045,368</td>
<td align="right">2,531,182,451</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,514,133</td>
<td align="right">593,544,218</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,790,443,702</td>
<td align="right">5,790,150,332</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">401,271,085</td>
<td align="right">401,289,723</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,433,509,843</td>
<td align="right">3,433,669,309</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,420,092,824</td>
<td align="right">2,419,982,830</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">22,615,860</td>
<td align="right">22,616,814</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">80,977,796</td>
<td align="right">80,981,175</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">68,557,906</td>
<td align="right">68,560,673</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">801,824,073</td>
<td align="right">801,792,057</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,139,790,659</td>
<td align="right">2,139,875,922</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">325,969,274</td>
<td align="right">325,982,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,164,221,192</td>
<td align="right">3,164,323,737</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,056,123,867</td>
<td align="right">1,056,158,058</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">942,993,687</td>
<td align="right">943,021,206</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">861,414,444</td>
<td align="right">861,439,209</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,090,877</td>
<td align="right">3,090,964</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">352,573,871</td>
<td align="right">352,583,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,294,894</td>
<td align="right">174,299,375</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6,486,155</td>
<td align="right">6,486,314</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,265,360,906</td>
<td align="right">2,265,412,769</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,344,483,241</td>
<td align="right">2,344,536,173</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,095,411,127</td>
<td align="right">1,095,434,986</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,651,748</td>
<td align="right">302,658,186</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">75,214,752</td>
<td align="right">75,216,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">267,372,078</td>
<td align="right">267,377,571</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">773,796,039</td>
<td align="right">773,780,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">147,865,796</td>
<td align="right">147,868,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">355,610,359</td>
<td align="right">355,616,765</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,531,229,700</td>
<td align="right">8,531,379,279</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">385,165,466</td>
<td align="right">385,171,853</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,505,187,443</td>
<td align="right">1,505,162,601</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">243,206</td>
<td align="right">243,210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">214,351</td>
<td align="right">214,354</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,627</td>
<td align="right">72,628</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">164,037,838</td>
<td align="right">164,039,856</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,535,694,993</td>
<td align="right">1,535,676,265</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">59,158,601</td>
<td align="right">59,159,219</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">88,978,474</td>
<td align="right">88,979,348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">252,182,938</td>
<td align="right">252,185,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,505,268</td>
<td align="right">20,505,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,832,016</td>
<td align="right">20,832,214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,832,037</td>
<td align="right">20,832,234</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">90,542,472</td>
<td align="right">90,543,322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,275,533,696</td>
<td align="right">1,275,544,669</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,489,300,197</td>
<td align="right">2,489,279,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,718,912,768</td>
<td align="right">2,718,935,501</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">780,507,403</td>
<td align="right">780,500,966</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">187,992,183</td>
<td align="right">187,993,705</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">565,954,140</td>
<td align="right">565,958,381</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,165,325</td>
<td align="right">6,165,371</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">72,271,101</td>
<td align="right">72,271,633</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,386,421,995</td>
<td align="right">13,386,325,493</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,343,070</td>
<td align="right">7,343,121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">433,613,667</td>
<td align="right">433,616,652</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,122,125</td>
<td align="right">3,122,146</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">98,038,660</td>
<td align="right">98,039,226</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,040,228,687</td>
<td align="right">1,040,232,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">626,712,480</td>
<td align="right">626,714,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">940,058,750</td>
<td align="right">940,061,835</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,808,606</td>
<td align="right">154,809,067</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">290,124,507</td>
<td align="right">290,125,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,284,120,618</td>
<td align="right">7,284,139,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">282,063,730</td>
<td align="right">282,064,408</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,584,852,910</td>
<td align="right">1,584,856,493</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,252,077,469</td>
<td align="right">1,252,080,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,103,323,738</td>
<td align="right">2,103,328,222</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,733,490,985</td>
<td align="right">2,733,495,891</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,483,022,181</td>
<td align="right">3,483,028,318</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">66,481,373</td>
<td align="right">66,481,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,657,308,135</td>
<td align="right">1,657,310,401</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">975,004,935</td>
<td align="right">975,006,193</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,403,490,869</td>
<td align="right">1,403,492,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,519,519</td>
<td align="right">242,519,766</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,569,682</td>
<td align="right">244,569,929</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,754,454,187</td>
<td align="right">1,754,455,834</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,789,347</td>
<td align="right">700,789,910</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">671,938,186</td>
<td align="right">671,937,664</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,764</td>
<td align="right">127,568,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,503,600</td>
<td align="right">545,503,979</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,358,399</td>
<td align="right">62,358,426</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">61,064,703</td>
<td align="right">61,064,723</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">77,896,767</td>
<td align="right">77,896,786</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,750,036,054</td>
<td align="right">4,750,037,181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,215,117,195</td>
<td align="right">3,215,116,501</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">459,026,517</td>
<td align="right">459,026,610</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">10,549,274</td>
<td align="right">10,549,276</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,098,554</td>
<td align="right">271,098,596</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,096,990</td>
<td align="right">156,097,011</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,301,986</td>
<td align="right">131,301,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,436,390</td>
<td align="right">504,436,387</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,154</td>
<td align="right">188,535,155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,277,796</td>
<td align="right">340,277,797</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,366,470</td>
<td align="right">1,053,366,470</td>
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
<td align="right">158,387,232</td>
<td align="right">158,387,232</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,749</td>
<td align="right">128,851,749</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,128,392</td>
<td align="right">115,128,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,724,902</td>
<td align="right">112,724,902</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,786,196</td>
<td align="right">74,786,196</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,786,271</td>
<td align="right">71,786,271</td>
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
<td align="right">41,964,443</td>
<td align="right">41,964,443</td>
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
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,756,294</td>
<td align="right">14,756,294</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,870,921</td>
<td align="right">9,870,921</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,646</td>
<td align="right">9,742,646</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,796</td>
<td align="right">8,976,796</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">6,152,500</td>
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
<td align="left">RERAISE</td>
<td align="right">3,784,349</td>
<td align="right">3,784,349</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,749,762</td>
<td align="right">1,749,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,577</td>
<td align="right">98,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">56,999</td>
<td align="right">56,999</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,970</td>
<td align="right">53,970</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,864</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,550</td>
<td align="right">3,550</td>
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
<td align="right">2,513</td>
<td align="right">2,513</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,072</td>
<td align="right">1,072</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">176</td>
<td align="right">176</td>
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
<td align="right">25</td>
<td align="right">25</td>
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
<td align="right">2,343,553,068</td>
<td align="right">12.6%</td>
<td align="right">2,343,606,013</td>
<td align="right">12.6%</td>
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
<td align="right">16,228,049,415</td>
<td align="right">87.0%</td>
<td align="right">16,228,112,037</td>
<td align="right">87.0%</td>
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
<td align="right">71,483,620</td>
<td align="right">0.4%</td>
<td align="right">71,483,726</td>
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
<td align="left">Failure</td>
<td align="right">912,909</td>
<td align="right">40.1%</td>
<td align="right">912,899</td>
<td align="right">40.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,365,757</td>
<td align="right">59.9%</td>
<td align="right">1,365,752</td>
<td align="right">59.9%</td>
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
<td align="right">7,078</td>
<td align="right">0.8%</td>
<td align="right">7,092</td>
<td align="right">0.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">631</td>
<td align="right">0.1%</td>
<td align="right">630</td>
<td align="right">0.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,092</td>
<td align="right">0.1%</td>
<td align="right">1,091</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,521</td>
<td align="right">2.6%</td>
<td align="right">23,509</td>
<td align="right">2.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,035</td>
<td align="right">0.2%</td>
<td align="right">2,036</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,985</td>
<td align="right">3.7%</td>
<td align="right">33,974</td>
<td align="right">3.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">35,895</td>
<td align="right">3.9%</td>
<td align="right">35,906</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,219</td>
<td align="right">8.1%</td>
<td align="right">74,201</td>
<td align="right">8.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,456</td>
<td align="right">4.8%</td>
<td align="right">43,461</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">42,834</td>
<td align="right">4.7%</td>
<td align="right">42,831</td>
<td align="right">4.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">78,851</td>
<td align="right">8.6%</td>
<td align="right">78,854</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">107,940</td>
<td align="right">11.8%</td>
<td align="right">107,942</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">121,439</td>
<td align="right">13.3%</td>
<td align="right">121,439</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">114,964</td>
<td align="right">12.6%</td>
<td align="right">114,964</td>
<td align="right">12.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">9.4%</td>
<td align="right">85,543</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">46,925</td>
<td align="right">5.1%</td>
<td align="right">46,925</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">22,292</td>
<td align="right">2.4%</td>
<td align="right">22,292</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">2.1%</td>
<td align="right">19,448</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,515</td>
<td align="right">0.9%</td>
<td align="right">8,515</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">0.9%</td>
<td align="right">8,203</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">8,167</td>
<td align="right">0.9%</td>
<td align="right">8,167</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,165</td>
<td align="right">0.3%</td>
<td align="right">3,165</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,110</td>
<td align="right">0.3%</td>
<td align="right">3,110</td>
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
<td align="left">subscr string slice</td>
<td align="right">2,336</td>
<td align="right">0.3%</td>
<td align="right">2,336</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">359</td>
<td align="right">0.0%</td>
<td align="right">359</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">26</td>
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
<tr>
<td align="left">subscr deque</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">545,503,600</td>
<td align="right">100.0%</td>
<td align="right">545,503,979</td>
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
<td align="right">11,101,952,348</td>
<td align="right">98.4%</td>
<td align="right">10,987,190,916</td>
<td align="right">98.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">181,986,198</td>
<td align="right">1.6%</td>
<td align="right">181,834,382</td>
<td align="right">1.6%</td>
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
<td align="right">178,626,725</td>
<td align="right">1.6%</td>
<td align="right">178,477,760</td>
<td align="right">1.6%</td>
<td align="right">-0.1%</td>
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
<td align="right">3,602,533</td>
<td align="right">100.0%</td>
<td align="right">3,599,686</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">146</td>
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
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">146</td>
<td align="right">100.0%</td>
<td align="right">146</td>
<td align="right">100.0%</td>
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
<td align="right">574,328</td>
<td align="right">96.6%</td>
<td align="right">574,328</td>
<td align="right">96.6%</td>
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
<td align="right">581,624</td>
<td align="right">97.9%</td>
<td align="right">581,624</td>
<td align="right">97.9%</td>
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
<td align="right">19,926</td>
<td align="right">100.0%</td>
<td align="right">19,927</td>
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
<td align="right">510,405,649</td>
<td align="right">10.2%</td>
<td align="right">510,436,209</td>
<td align="right">10.2%</td>
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
<td align="right">1,270,889</td>
<td align="right">0.0%</td>
<td align="right">1,270,912</td>
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
<td align="right">4,505,608,160</td>
<td align="right">89.8%</td>
<td align="right">4,505,616,627</td>
<td align="right">89.8%</td>
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
<td align="right">41,399</td>
<td align="right">16.6%</td>
<td align="right">41,405</td>
<td align="right">16.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">207,488</td>
<td align="right">83.4%</td>
<td align="right">207,507</td>
<td align="right">83.4%</td>
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
<td align="left">bool</td>
<td align="right">1,881</td>
<td align="right">0.9%</td>
<td align="right">1,886</td>
<td align="right">0.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,298</td>
<td align="right">11.2%</td>
<td align="right">23,283</td>
<td align="right">11.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,409</td>
<td align="right">21.9%</td>
<td align="right">45,436</td>
<td align="right">21.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,762</td>
<td align="right">3.7%</td>
<td align="right">7,759</td>
<td align="right">3.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">10,483</td>
<td align="right">5.1%</td>
<td align="right">10,487</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,832</td>
<td align="right">3.3%</td>
<td align="right">6,834</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">3.7%</td>
<td align="right">7,649</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">90,414</td>
<td align="right">43.6%</td>
<td align="right">90,412</td>
<td align="right">43.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">11,307</td>
<td align="right">5.4%</td>
<td align="right">11,307</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,324</td>
<td align="right">0.6%</td>
<td align="right">1,324</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">934</td>
<td align="right">0.5%</td>
<td align="right">934</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">196</td>
<td align="right">0.1%</td>
<td align="right">196</td>
<td align="right">0.1%</td>
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
<td align="right">1,403,375</td>
<td align="right">0.1%</td>
<td align="right">1,403,587</td>
<td align="right">0.1%</td>
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
<td align="right">153,752,174</td>
<td align="right">6.6%</td>
<td align="right">153,730,410</td>
<td align="right">6.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,186,664,479</td>
<td align="right">93.4%</td>
<td align="right">2,186,668,899</td>
<td align="right">93.4%</td>
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
<td align="right">58,314</td>
<td align="right">67.1%</td>
<td align="right">58,299</td>
<td align="right">67.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,585</td>
<td align="right">32.9%</td>
<td align="right">28,589</td>
<td align="right">32.9%</td>
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
<td align="right">11,013</td>
<td align="right">18.9%</td>
<td align="right">11,004</td>
<td align="right">18.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,988</td>
<td align="right">18.8%</td>
<td align="right">10,980</td>
<td align="right">18.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,540</td>
<td align="right">24.9%</td>
<td align="right">14,542</td>
<td align="right">24.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">21,773</td>
<td align="right">37.3%</td>
<td align="right">21,773</td>
<td align="right">37.3%</td>
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
<td align="right">163,968,260</td>
<td align="right">3.2%</td>
<td align="right">163,999,388</td>
<td align="right">3.2%</td>
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
<td align="right">3,470,904,072</td>
<td align="right">67.5%</td>
<td align="right">3,470,643,175</td>
<td align="right">67.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,504,746,807</td>
<td align="right">29.3%</td>
<td align="right">1,504,720,529</td>
<td align="right">29.3%</td>
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
<td align="right">435,244</td>
<td align="right">12.3%</td>
<td align="right">436,681</td>
<td align="right">12.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,098,948</td>
<td align="right">87.7%</td>
<td align="right">3,099,538</td>
<td align="right">87.7%</td>
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
<td align="right">68,973</td>
<td align="right">15.8%</td>
<td align="right">70,431</td>
<td align="right">16.1%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,008</td>
<td align="right">4.1%</td>
<td align="right">17,977</td>
<td align="right">4.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,282</td>
<td align="right">1.0%</td>
<td align="right">4,284</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,700</td>
<td align="right">8.0%</td>
<td align="right">34,706</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,542</td>
<td align="right">2.4%</td>
<td align="right">10,543</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,675</td>
<td align="right">19.2%</td>
<td align="right">83,676</td>
<td align="right">19.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">171,565</td>
<td align="right">39.4%</td>
<td align="right">171,565</td>
<td align="right">39.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,269</td>
<td align="right">4.2%</td>
<td align="right">18,269</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,537</td>
<td align="right">2.4%</td>
<td align="right">10,537</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,083</td>
<td align="right">1.4%</td>
<td align="right">6,083</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,420</td>
<td align="right">0.8%</td>
<td align="right">3,420</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,114</td>
<td align="right">0.7%</td>
<td align="right">3,114</td>
<td align="right">0.7%</td>
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
<td align="left">tuple</td>
<td align="right">533</td>
<td align="right">0.1%</td>
<td align="right">533</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="left">set</td>
<td align="right">12,122,586</td>
<td align="right">12,122,586 / 0 !!</td>
<td align="right">12,135,548</td>
<td align="right">12,135,548 / 0 !!</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">171,490,964</td>
<td align="right">171,490,964 / 0 !!</td>
<td align="right">171,424,829</td>
<td align="right">171,424,829 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">119,369,919</td>
<td align="right">119,369,919 / 0 !!</td>
<td align="right">119,408,278</td>
<td align="right">119,408,278 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">304,453,466</td>
<td align="right">304,453,466 / 0 !!</td>
<td align="right">304,489,258</td>
<td align="right">304,489,258 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,823,200</td>
<td align="right">2,823,200 / 0 !!</td>
<td align="right">2,823,462</td>
<td align="right">2,823,462 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,508,924</td>
<td align="right">5,508,924 / 0 !!</td>
<td align="right">5,509,155</td>
<td align="right">5,509,155 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,923,177</td>
<td align="right">101,923,177 / 0 !!</td>
<td align="right">101,924,954</td>
<td align="right">101,924,954 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,932,891</td>
<td align="right">34,932,891 / 0 !!</td>
<td align="right">34,933,004</td>
<td align="right">34,933,004 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,958,869</td>
<td align="right">341,958,869 / 0 !!</td>
<td align="right">341,959,367</td>
<td align="right">341,959,367 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
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
<td align="right">11,981,960,333</td>
<td align="right">87.8%</td>
<td align="right">11,866,949,722</td>
<td align="right">87.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,436,011</td>
<td align="right">0.0%</td>
<td align="right">1,438,767</td>
<td align="right">0.0%</td>
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
<td align="right">860,551,074</td>
<td align="right">6.3%</td>
<td align="right">860,618,458</td>
<td align="right">6.4%</td>
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
<td align="right">800,051,389</td>
<td align="right">5.9%</td>
<td align="right">800,018,652</td>
<td align="right">5.9%</td>
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
<td align="right">505,661</td>
<td align="right">3.0%</td>
<td align="right">506,377</td>
<td align="right">3.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,315,455</td>
<td align="right">97.0%</td>
<td align="right">16,316,716</td>
<td align="right">97.0%</td>
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
<td align="right">5,312</td>
<td align="right">1.1%</td>
<td align="right">5,316</td>
<td align="right">1.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,158</td>
<td align="right">1.6%</td>
<td align="right">8,163</td>
<td align="right">1.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">53,191</td>
<td align="right">10.5%</td>
<td align="right">53,223</td>
<td align="right">10.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,463</td>
<td align="right">4.8%</td>
<td align="right">24,451</td>
<td align="right">4.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">73,624</td>
<td align="right">14.6%</td>
<td align="right">73,636</td>
<td align="right">14.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">54,639</td>
<td align="right">10.8%</td>
<td align="right">54,639</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,794</td>
<td align="right">3.1%</td>
<td align="right">15,794</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">0.9%</td>
<td align="right">4,448</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,739</td>
<td align="right">0.5%</td>
<td align="right">2,739</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,885</td>
<td align="right">0.4%</td>
<td align="right">1,885</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,721</td>
<td align="right">0.3%</td>
<td align="right">1,721</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,104</td>
<td align="right">0.2%</td>
<td align="right">1,104</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">573</td>
<td align="right">0.1%</td>
<td align="right">573</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">545</td>
<td align="right">0.1%</td>
<td align="right">545</td>
<td align="right">0.1%</td>
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
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">255</td>
<td align="right">0.1%</td>
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
<td align="right">9,218,090,378</td>
<td align="right">99.8%</td>
<td align="right">9,045,413,701</td>
<td align="right">99.8%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">51,816</td>
<td align="right">0.0%</td>
<td align="right">51,768</td>
<td align="right">0.0%</td>
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
<td align="right">14,622,452</td>
<td align="right">0.2%</td>
<td align="right">14,622,444</td>
<td align="right">0.2%</td>
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
<td align="right">1,376</td>
<td align="right">0.0%</td>
<td align="right">1,376</td>
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
<td align="right">134,593</td>
<td align="right">100.0%</td>
<td align="right">134,601</td>
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
<td align="right">64,155,580</td>
<td align="right">100.0%</td>
<td align="right">64,155,687</td>
<td align="right">100.0%</td>
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
<td align="right">203</td>
<td align="right">0.0%</td>
<td align="right">203</td>
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
<td align="right">2,310</td>
<td align="right">100.0%</td>
<td align="right">2,310</td>
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
<td align="right">593,499,422</td>
<td align="right">82.2%</td>
<td align="right">593,529,507</td>
<td align="right">82.2%</td>
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
<td align="right">128,816,951</td>
<td align="right">17.8%</td>
<td align="right">128,816,951</td>
<td align="right">17.8%</td>
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
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">114,206,014</td>
<td align="right">5.7%</td>
<td align="right">114,218,331</td>
<td align="right">5.7%</td>
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
<td align="right">1,812,769,404</td>
<td align="right">90.9%</td>
<td align="right">1,812,785,864</td>
<td align="right">90.9%</td>
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
<td align="right">66,396,798</td>
<td align="right">3.3%</td>
<td align="right">66,396,898</td>
<td align="right">3.3%</td>
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
<td align="right">44,910</td>
<td align="right">2.0%</td>
<td align="right">44,917</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,193,749</td>
<td align="right">98.0%</td>
<td align="right">2,193,984</td>
<td align="right">98.0%</td>
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
<td align="right">248,234</td>
<td align="right">552.7%</td>
<td align="right">248,907</td>
<td align="right">554.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,334</td>
<td align="right">7.4%</td>
<td align="right">3,340</td>
<td align="right">7.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">19,647</td>
<td align="right">43.7%</td>
<td align="right">19,647</td>
<td align="right">43.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,227</td>
<td align="right">16.1%</td>
<td align="right">7,227</td>
<td align="right">16.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">5,799</td>
<td align="right">12.9%</td>
<td align="right">5,799</td>
<td align="right">12.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,741</td>
<td align="right">8.3%</td>
<td align="right">3,741</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,321</td>
<td align="right">2.9%</td>
<td align="right">1,321</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">747</td>
<td align="right">1.7%</td>
<td align="right">747</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">0.9%</td>
<td align="right">423</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">363</td>
<td align="right">0.8%</td>
<td align="right">363</td>
<td align="right">0.8%</td>
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
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">91</td>
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
<td align="right">112,724,902</td>
<td align="right">100.0%</td>
<td align="right">112,724,902</td>
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
<td align="right">918,525,791</td>
<td align="right">56.7%</td>
<td align="right">918,539,806</td>
<td align="right">56.7%</td>
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
<td align="right">700,605,445</td>
<td align="right">43.3%</td>
<td align="right">700,606,008</td>
<td align="right">43.3%</td>
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
<td align="right">2,064</td>
<td align="right">1.1%</td>
<td align="right">2,064</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">181,878</td>
<td align="right">98.9%</td>
<td align="right">181,878</td>
<td align="right">98.9%</td>
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
<td align="right">86,545</td>
<td align="right">47.6%</td>
<td align="right">86,545</td>
<td align="right">47.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.9%</td>
<td align="right">48,931</td>
<td align="right">26.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,183</td>
<td align="right">10.5%</td>
<td align="right">19,183</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,164</td>
<td align="right">9.4%</td>
<td align="right">17,164</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,315</td>
<td align="right">2.9%</td>
<td align="right">5,315</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,991</td>
<td align="right">1.6%</td>
<td align="right">2,991</td>
<td align="right">1.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,725,910,613</td>
<td align="right">92.8%</td>
<td align="right">4,668,486,551</td>
<td align="right">92.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">110,663,053</td>
<td align="right">2.2%</td>
<td align="right">110,683,469</td>
<td align="right">2.2%</td>
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
<td align="right">255,907,337</td>
<td align="right">5.0%</td>
<td align="right">255,922,697</td>
<td align="right">5.1%</td>
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
<td align="right">2,136,465</td>
<td align="right">78.2%</td>
<td align="right">2,136,849</td>
<td align="right">78.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">596,929</td>
<td align="right">21.8%</td>
<td align="right">596,959</td>
<td align="right">21.8%</td>
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
<td align="left">set</td>
<td align="right">10,036</td>
<td align="right">1.7%</td>
<td align="right">10,054</td>
<td align="right">1.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,721</td>
<td align="right">1.6%</td>
<td align="right">9,724</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,304</td>
<td align="right">2.7%</td>
<td align="right">16,309</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">83,562</td>
<td align="right">14.0%</td>
<td align="right">83,549</td>
<td align="right">14.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">126,701</td>
<td align="right">21.2%</td>
<td align="right">126,719</td>
<td align="right">21.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,844</td>
<td align="right">43.2%</td>
<td align="right">257,843</td>
<td align="right">43.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">72,063</td>
<td align="right">12.1%</td>
<td align="right">72,063</td>
<td align="right">12.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,856</td>
<td align="right">3.2%</td>
<td align="right">18,856</td>
<td align="right">3.2%</td>
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
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,646,238</td>
<td align="right">0.1%</td>
<td align="right">1,646,447</td>
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
<td align="right">1,237,421,823</td>
<td align="right">99.9%</td>
<td align="right">1,237,425,269</td>
<td align="right">99.9%</td>
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
<td align="right">916</td>
<td align="right">8.5%</td>
<td align="right">921</td>
<td align="right">8.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,889</td>
<td align="right">91.5%</td>
<td align="right">9,889</td>
<td align="right">91.5%</td>
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
<td align="right">681</td>
<td align="right">74.3%</td>
<td align="right">686</td>
<td align="right">74.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">14.8%</td>
<td align="right">136</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">99</td>
<td align="right">10.8%</td>
<td align="right">99</td>
<td align="right">10.7%</td>
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
<td align="right">78,547,582,572</td>
<td align="right">37.3%</td>
<td align="right">78,029,541,148</td>
<td align="right">37.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">122,103,471,141</td>
<td align="right">58.0%</td>
<td align="right">121,758,652,630</td>
<td align="right">58.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,506,344,023</td>
<td align="right">0.7%</td>
<td align="right">1,506,323,748</td>
<td align="right">0.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,238,926,331</td>
<td align="right">3.9%</td>
<td align="right">8,238,971,732</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
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
<td align="right">178,626,725</td>
<td align="right">2.4%</td>
<td align="right">178,477,760</td>
<td align="right">2.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,752,174</td>
<td align="right">2.1%</td>
<td align="right">153,730,410</td>
<td align="right">2.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">255,907,337</td>
<td align="right">3.5%</td>
<td align="right">255,922,697</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,405,649</td>
<td align="right">7.0%</td>
<td align="right">510,436,209</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">800,051,389</td>
<td align="right">10.9%</td>
<td align="right">800,018,652</td>
<td align="right">10.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,343,553,068</td>
<td align="right">32.0%</td>
<td align="right">2,343,606,013</td>
<td align="right">32.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,504,746,807</td>
<td align="right">20.6%</td>
<td align="right">1,504,720,529</td>
<td align="right">20.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,605,445</td>
<td align="right">9.6%</td>
<td align="right">700,606,008</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,503,600</td>
<td align="right">7.5%</td>
<td align="right">545,503,979</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,951</td>
<td align="right">1.8%</td>
<td align="right">128,816,951</td>
<td align="right">1.8%</td>
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
<td align="right">89,886,903</td>
<td align="right">6.0%</td>
<td align="right">89,938,481</td>
<td align="right">6.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,884,354</td>
<td align="right">5.4%</td>
<td align="right">81,913,273</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,362,220</td>
<td align="right">3.3%</td>
<td align="right">49,376,295</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,824,527</td>
<td align="right">5.5%</td>
<td align="right">82,835,176</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,472,333</td>
<td align="right">3.6%</td>
<td align="right">54,476,528</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,667,089</td>
<td align="right">5.4%</td>
<td align="right">81,670,145</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">264,664,340</td>
<td align="right">17.6%</td>
<td align="right">264,672,662</td>
<td align="right">17.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,006,511</td>
<td align="right">5.4%</td>
<td align="right">82,008,720</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,987,666</td>
<td align="right">6.2%</td>
<td align="right">93,987,030</td>
<td align="right">6.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">365,459,315</td>
<td align="right">24.3%</td>
<td align="right">365,457,575</td>
<td align="right">24.3%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,002,893,399</td>
<td align="right">15.0%</td>
<td align="right">945,324,975</td>
<td align="right">14.3%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,007,170,720</td>
<td align="right">15.1%</td>
<td align="right">949,602,296</td>
<td align="right">14.3%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,591,634,510</td>
<td align="right">23.8%</td>
<td align="right">1,534,074,179</td>
<td align="right">23.1%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,591,634,510</td>
<td align="right">23.8%</td>
<td align="right">1,534,074,179</td>
<td align="right">23.1%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,415,095,918</td>
<td align="right">81.0%</td>
<td align="right">5,357,667,879</td>
<td align="right">80.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">275,667,473</td>
<td align="right">4.1%</td>
<td align="right">275,689,799</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,590,571</td>
<td align="right">0.4%</td>
<td align="right">23,591,370</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,476,535</td>
<td align="right">3.9%</td>
<td align="right">259,483,954</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,463,790</td>
<td align="right">8.7%</td>
<td align="right">584,471,883</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,093,849,450</td>
<td align="right">76.2%</td>
<td align="right">5,093,912,132</td>
<td align="right">76.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,698,544</td>
<td align="right">1.1%</td>
<td align="right">70,698,626</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,457</td>
<td align="right">0.1%</td>
<td align="right">4,273,457</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,898</td>
<td align="right">2.0%</td>
<td align="right">132,513,898</td>
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
<td align="left">Method cache hits</td>
<td align="right">2,362,695,943</td>
<td align="right"></td>
<td align="right">2,248,943,151</td>
<td align="right"></td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,765,316</td>
<td align="right"></td>
<td align="right">6,958,453</td>
<td align="right"></td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">57,289,116</td>
<td align="right"></td>
<td align="right">55,939,274</td>
<td align="right"></td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,446,854,682</td>
<td align="right"></td>
<td align="right">2,389,430,505</td>
<td align="right"></td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">63,252,304</td>
<td align="right"></td>
<td align="right">62,094,940</td>
<td align="right"></td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">24,947,678,755</td>
<td align="right">27.2%</td>
<td align="right">24,601,365,762</td>
<td align="right">27.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">31,754,509,604</td>
<td align="right">29.2%</td>
<td align="right">31,350,718,894</td>
<td align="right">29.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,643,565,996</td>
<td align="right">5.1%</td>
<td align="right">4,586,091,981</td>
<td align="right">5.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">39,069,027,781</td>
<td align="right">42.6%</td>
<td align="right">38,608,976,525</td>
<td align="right">42.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">22,957,395,691</td>
<td align="right">25.1%</td>
<td align="right">22,726,343,867</td>
<td align="right">25.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,909,861,255</td>
<td align="right">22.9%</td>
<td align="right">24,679,458,513</td>
<td align="right">22.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">50,140,253,009</td>
<td align="right">46.1%</td>
<td align="right">49,680,269,392</td>
<td align="right">46.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,571,185,778</td>
<td align="right">70.9%</td>
<td align="right">13,513,606,999</td>
<td align="right">70.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,571,298,820</td>
<td align="right"></td>
<td align="right">13,513,720,331</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,265,356</td>
<td align="right">0.4%</td>
<td align="right">71,271,810</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,860,375,437</td>
<td align="right">1.7%</td>
<td align="right">1,860,485,565</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,559,008,611</td>
<td align="right">29.1%</td>
<td align="right">5,559,250,528</td>
<td align="right">29.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,481,377,973</td>
<td align="right">28.7%</td>
<td align="right">5,481,613,436</td>
<td align="right">28.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,156,937,031</td>
<td align="right"></td>
<td align="right">6,157,144,702</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,611,660</td>
<td align="right"></td>
<td align="right">174,612,820</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,365,282</td>
<td align="right">0.0%</td>
<td align="right">6,365,282</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,404,482</td>
<td align="right">1.9%</td>
<td align="right">3,404,482</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">306,771</td>
<td align="right">0.2%</td>
<td align="right">306,771</td>
<td align="right">0.2%</td>
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
<td align="right">364,840</td>
<td align="right">102,017,796</td>
<td align="right">9,544,770,040</td>
<td align="right">759,974,420</td>
<td align="right">764,461,528</td>
<td align="right">364,845</td>
<td align="right">102,019,039</td>
<td align="right">9,526,763,897</td>
<td align="right">757,437,750</td>
<td align="right">763,809,920</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,681,053,888</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,681,046,712</td>
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
<td align="right">22,592</td>
<td align="right">22,592</td>
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
<td align="right">34</td>
<td align="right">34</td>
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
<td align="right">41</td>
<td align="right">41</td>
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
<td align="right">2,397</td>
<td align="right">2,397</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-18
