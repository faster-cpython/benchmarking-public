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
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">66,372,730</td>
<td align="right">12,286,912</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">462,042,960</td>
<td align="right">181,727,306</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">634,819,173</td>
<td align="right">666,812,756</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,999,263,426</td>
<td align="right">2,096,565,411</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">218,393,924</td>
<td align="right">208,046,470</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,015,991,811</td>
<td align="right">6,296,102,578</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,238,041,001</td>
<td align="right">1,291,892,135</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">795,519,696</td>
<td align="right">828,796,359</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,350,515,719</td>
<td align="right">1,382,515,584</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,779,879,814</td>
<td align="right">12,877,641,144</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,447,214,265</td>
<td align="right">1,457,642,177</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">69,859,194</td>
<td align="right">70,245,095</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">6,409,750,765</td>
<td align="right">6,442,458,110</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">69,466</td>
<td align="right">69,774</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,646,267,990</td>
<td align="right">16,711,392,105</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">15,139,642</td>
<td align="right">15,087,202</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">200,104,206</td>
<td align="right">200,711,303</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">22,042,718</td>
<td align="right">22,012,836</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,119,817</td>
<td align="right">2,122,217</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">875,995,380</td>
<td align="right">876,637,063</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">10,339,338</td>
<td align="right">10,332,060</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,485,683</td>
<td align="right">10,478,585</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">83,065,636</td>
<td align="right">83,014,013</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,835,360,450</td>
<td align="right">2,833,915,477</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,258,010,451</td>
<td align="right">1,258,628,897</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">342,797,450</td>
<td align="right">342,677,144</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,827,388</td>
<td align="right">11,831,041</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">71,732,172</td>
<td align="right">71,710,995</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">11,407,596</td>
<td align="right">11,410,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1,332,923</td>
<td align="right">1,333,263</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">90,955,363</td>
<td align="right">90,934,283</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">16,907</td>
<td align="right">16,904</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">52,244,453</td>
<td align="right">52,253,531</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">129,198,213</td>
<td align="right">129,219,874</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">408,528,937</td>
<td align="right">408,462,869</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">154,636,649</td>
<td align="right">154,659,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,398,061,681</td>
<td align="right">1,397,852,419</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,472,919,654</td>
<td align="right">4,473,577,381</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">805,098,475</td>
<td align="right">804,988,804</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,769,369</td>
<td align="right">21,772,298</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">293,129,227</td>
<td align="right">293,090,450</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,783,433</td>
<td align="right">1,783,665</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">22,217,091</td>
<td align="right">22,219,939</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">22,216,944</td>
<td align="right">22,219,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">93,962,637</td>
<td align="right">93,974,175</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">99,261,201</td>
<td align="right">99,271,819</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">122,186,012</td>
<td align="right">122,173,915</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">196,080,921</td>
<td align="right">196,099,099</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">648,081,937</td>
<td align="right">648,140,687</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">77,067,400</td>
<td align="right">77,060,419</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">210,392,546</td>
<td align="right">210,410,309</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">675,001,491</td>
<td align="right">674,945,445</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">467,311,510</td>
<td align="right">467,348,267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">557,469</td>
<td align="right">557,511</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,139,474,375</td>
<td align="right">7,140,009,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,238,399,245</td>
<td align="right">4,238,084,447</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,747,898</td>
<td align="right">3,748,162</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">291,104,944</td>
<td align="right">291,084,481</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">661,314,969</td>
<td align="right">661,361,398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">637,585,535</td>
<td align="right">637,541,126</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">959,542,030</td>
<td align="right">959,608,214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">965,839,089</td>
<td align="right">965,903,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">2,026,837,186</td>
<td align="right">2,026,702,915</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">18,803,180,397</td>
<td align="right">18,804,419,505</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,108,324,807</td>
<td align="right">2,108,187,050</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">520,942,577</td>
<td align="right">520,910,181</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,073,888,319</td>
<td align="right">4,073,643,523</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">229,445,383</td>
<td align="right">229,458,871</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">451,584,460</td>
<td align="right">451,559,370</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,672,199,905</td>
<td align="right">4,671,955,479</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">251,978,023</td>
<td align="right">251,991,015</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">95,783,375</td>
<td align="right">95,787,979</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,965,435,907</td>
<td align="right">3,965,250,543</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">376,262,139</td>
<td align="right">376,244,801</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,368,701,737</td>
<td align="right">1,368,764,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">593,916,861</td>
<td align="right">593,890,271</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">44,233,374</td>
<td align="right">44,235,278</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">126,336,112</td>
<td align="right">126,341,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">8,017,124,760</td>
<td align="right">8,016,800,110</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">589,645,720</td>
<td align="right">589,669,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,398,748,624</td>
<td align="right">1,398,802,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,677,599,973</td>
<td align="right">2,677,499,043</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">626,797,135</td>
<td align="right">626,819,522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,836,524</td>
<td align="right">5,836,732</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">500,938,239</td>
<td align="right">500,955,524</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,311,710,254</td>
<td align="right">1,311,754,145</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,504,490,447</td>
<td align="right">2,504,407,478</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">844,451,755</td>
<td align="right">844,424,453</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">355,278,315</td>
<td align="right">355,289,771</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">149,767,096</td>
<td align="right">149,762,356</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">663,850,884</td>
<td align="right">663,831,231</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,166,284,297</td>
<td align="right">1,166,316,458</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,143,713,937</td>
<td align="right">2,143,772,335</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,189,971,283</td>
<td align="right">2,190,029,591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">242,284,730</td>
<td align="right">242,291,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">156,644,299</td>
<td align="right">156,648,171</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">236,285,040</td>
<td align="right">236,279,824</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,317,910,772</td>
<td align="right">1,317,881,824</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,585,293,697</td>
<td align="right">2,585,238,010</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">93,054,380</td>
<td align="right">93,052,562</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">495,404,122</td>
<td align="right">495,413,747</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,751,765,549</td>
<td align="right">1,751,799,254</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">13,861,285,489</td>
<td align="right">13,861,040,897</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">458,292,724</td>
<td align="right">458,285,299</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">469,412,370</td>
<td align="right">469,419,789</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,012,706,958</td>
<td align="right">1,012,691,034</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">18,478,015</td>
<td align="right">18,478,281</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">341,069,419</td>
<td align="right">341,073,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">445,115,189</td>
<td align="right">445,120,764</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">234,625,864</td>
<td align="right">234,628,795</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">127,633,270</td>
<td align="right">127,631,720</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,437,559,754</td>
<td align="right">1,437,542,609</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,699,591,341</td>
<td align="right">1,699,611,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">75,112,315</td>
<td align="right">75,113,132</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">229,782,636</td>
<td align="right">229,784,566</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,300,462,211</td>
<td align="right">2,300,480,754</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">345,702,160</td>
<td align="right">345,699,445</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">148,647,980</td>
<td align="right">148,649,116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,887,656,942</td>
<td align="right">4,887,620,630</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,221,265,451</td>
<td align="right">3,221,289,375</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">47,452,330,890</td>
<td align="right">47,451,987,205</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">291,818</td>
<td align="right">291,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">468,878,843</td>
<td align="right">468,881,801</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">196,259,830</td>
<td align="right">196,261,059</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">375,020,699</td>
<td align="right">375,022,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,911,663</td>
<td align="right">173,912,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">195,564,315</td>
<td align="right">195,565,438</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,382,044,300</td>
<td align="right">3,382,024,975</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">779,225,702</td>
<td align="right">779,229,862</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,460,852</td>
<td align="right">20,460,745</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,617,876</td>
<td align="right">402,619,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">556,466,472</td>
<td align="right">556,468,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">170,836,872</td>
<td align="right">170,837,562</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,848,331</td>
<td align="right">786,851,290</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">499,504,777</td>
<td align="right">499,506,422</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">211,846,861</td>
<td align="right">211,847,481</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,566,369,951</td>
<td align="right">1,566,365,642</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,133,121,467</td>
<td align="right">2,133,115,677</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">234,557,588</td>
<td align="right">234,558,179</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">361,390,309</td>
<td align="right">361,391,004</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">162,467,426</td>
<td align="right">162,467,734</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">170,077,961</td>
<td align="right">170,078,277</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,145,036,251</td>
<td align="right">1,145,038,347</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,543,252</td>
<td align="right">82,543,398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,505,933</td>
<td align="right">3,505,939</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,713,678,190</td>
<td align="right">1,713,680,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,982,450,026</td>
<td align="right">1,982,451,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">82,425,893</td>
<td align="right">82,425,939</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">282,176,020</td>
<td align="right">282,175,922</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">47,522,648</td>
<td align="right">47,522,664</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,071,546,010</td>
<td align="right">2,071,546,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">139,553,116</td>
<td align="right">139,553,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">96,820,801</td>
<td align="right">96,820,791</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,400,044</td>
<td align="right">92,400,040</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,683,684</td>
<td align="right">94,683,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,147,503,113</td>
<td align="right">3,147,503,228</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,674,627,979</td>
<td align="right">1,674,627,979</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">133,515,680</td>
<td align="right">133,515,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">87,198,800</td>
<td align="right">87,198,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">77,693,920</td>
<td align="right">77,693,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,240</td>
<td align="right">38,846,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,680</td>
<td align="right">38,845,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">14,110,700</td>
<td align="right">14,110,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">8,370,660</td>
<td align="right">8,370,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">8,205,220</td>
<td align="right">8,205,220</td>
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
<td align="left">STORE_NAME</td>
<td align="right">1,222,760</td>
<td align="right">1,222,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">1,129,440</td>
<td align="right">1,129,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">260,980</td>
<td align="right">260,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">194,500</td>
<td align="right">194,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">179,660</td>
<td align="right">179,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">158,580</td>
<td align="right">158,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">91,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">29,880</td>
<td align="right">29,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,420</td>
<td align="right">21,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,400</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,120</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,394,705,935</td>
<td align="right">86.6%</td>
<td align="right">9,459,350,932</td>
<td align="right">86.7%</td>
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
<td align="right">1,445,697,347</td>
<td align="right">13.3%</td>
<td align="right">1,445,488,108</td>
<td align="right">13.3%</td>
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
<td align="right">50,347,114</td>
<td align="right">0.5%</td>
<td align="right">50,347,095</td>
<td align="right">0.5%</td>
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
<td align="right">996,023</td>
<td align="right">36.7%</td>
<td align="right">995,971</td>
<td align="right">36.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,715,425</td>
<td align="right">63.3%</td>
<td align="right">1,715,435</td>
<td align="right">63.3%</td>
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
<td align="left">and other</td>
<td align="right">2,009</td>
<td align="right">0.1%</td>
<td align="right">2,017</td>
<td align="right">0.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">18,827</td>
<td align="right">1.1%</td>
<td align="right">18,817</td>
<td align="right">1.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">13,748</td>
<td align="right">0.8%</td>
<td align="right">13,741</td>
<td align="right">0.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">29,270</td>
<td align="right">1.7%</td>
<td align="right">29,265</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">70,915</td>
<td align="right">4.1%</td>
<td align="right">70,925</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">53,127</td>
<td align="right">3.1%</td>
<td align="right">53,123</td>
<td align="right">3.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">18,164</td>
<td align="right">1.1%</td>
<td align="right">18,163</td>
<td align="right">1.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">37,333</td>
<td align="right">2.2%</td>
<td align="right">37,335</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">217,425</td>
<td align="right">12.7%</td>
<td align="right">217,436</td>
<td align="right">12.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">29,504</td>
<td align="right">1.7%</td>
<td align="right">29,503</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">66,353</td>
<td align="right">3.9%</td>
<td align="right">66,355</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">249,231</td>
<td align="right">14.5%</td>
<td align="right">249,225</td>
<td align="right">14.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,599</td>
<td align="right">4.3%</td>
<td align="right">74,600</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">778,677</td>
<td align="right">45.4%</td>
<td align="right">778,687</td>
<td align="right">45.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">31,363</td>
<td align="right">1.8%</td>
<td align="right">31,363</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">15,440</td>
<td align="right">0.9%</td>
<td align="right">15,440</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">5,500</td>
<td align="right">0.3%</td>
<td align="right">5,500</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">3,520</td>
<td align="right">0.2%</td>
<td align="right">3,520</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
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
<td align="right">2,003,543,092</td>
<td align="right">24.3%</td>
<td align="right">2,100,821,308</td>
<td align="right">25.2%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,241,365,155</td>
<td align="right">75.7%</td>
<td align="right">6,241,396,722</td>
<td align="right">74.8%</td>
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
<td align="right">5,034,506</td>
<td align="right">0.1%</td>
<td align="right">5,034,530</td>
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
<td align="right">563,657</td>
<td align="right">74.7%</td>
<td align="right">587,457</td>
<td align="right">75.4%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">191,183</td>
<td align="right">25.3%</td>
<td align="right">191,176</td>
<td align="right">24.6%</td>
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
<td align="left">array int</td>
<td align="right">133,820</td>
<td align="right">23.7%</td>
<td align="right">157,600</td>
<td align="right">26.8%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.0%</td>
<td align="right">123</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">48,980</td>
<td align="right">8.7%</td>
<td align="right">49,000</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">74,520</td>
<td align="right">13.2%</td>
<td align="right">74,519</td>
<td align="right">12.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">264,773</td>
<td align="right">47.0%</td>
<td align="right">264,775</td>
<td align="right">45.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">35,340</td>
<td align="right">6.3%</td>
<td align="right">35,340</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">0.8%</td>
<td align="right">4,300</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">980</td>
<td align="right">0.2%</td>
<td align="right">980</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">720</td>
<td align="right">0.1%</td>
<td align="right">720</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
<td align="right">0.0%</td>
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
<td align="right">206,968,967</td>
<td align="right">1.5%</td>
<td align="right">207,023,261</td>
<td align="right">1.5%</td>
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
<td align="right">697,701,812</td>
<td align="right">4.9%</td>
<td align="right">697,764,748</td>
<td align="right">4.9%</td>
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
<td align="right">13,561,256,287</td>
<td align="right">95.1%</td>
<td align="right">13,561,636,467</td>
<td align="right">95.1%</td>
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
<td align="right">41,300</td>
<td align="right">0.0%</td>
<td align="right">41,300</td>
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
<td align="right">177,168</td>
<td align="right">3.8%</td>
<td align="right">177,234</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,494,109</td>
<td align="right">96.2%</td>
<td align="right">4,495,026</td>
<td align="right">96.2%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">164,988</td>
<td align="right">93.1%</td>
<td align="right">165,054</td>
<td align="right">93.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">11,600</td>
<td align="right">6.5%</td>
<td align="right">11,600</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,320</td>
<td align="right">1.9%</td>
<td align="right">3,320</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,100</td>
<td align="right">1.2%</td>
<td align="right">2,100</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">960</td>
<td align="right">0.5%</td>
<td align="right">960</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">580</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,402,168</td>
<td align="right">0.0%</td>
<td align="right">1,404,129</td>
<td align="right">0.0%</td>
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
<td align="right">664,854,192</td>
<td align="right">10.4%</td>
<td align="right">664,836,340</td>
<td align="right">10.4%</td>
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
<td align="right">5,756,048,329</td>
<td align="right">89.6%</td>
<td align="right">5,756,027,630</td>
<td align="right">89.6%</td>
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
<td align="right">311,089</td>
<td align="right">78.0%</td>
<td align="right">311,215</td>
<td align="right">78.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">87,771</td>
<td align="right">22.0%</td>
<td align="right">87,805</td>
<td align="right">22.0%</td>
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
<td align="left">long float</td>
<td align="right">1,560</td>
<td align="right">0.5%</td>
<td align="right">1,567</td>
<td align="right">0.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">20,320</td>
<td align="right">6.5%</td>
<td align="right">20,365</td>
<td align="right">6.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">35,097</td>
<td align="right">11.3%</td>
<td align="right">35,164</td>
<td align="right">11.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">3,288</td>
<td align="right">1.1%</td>
<td align="right">3,283</td>
<td align="right">1.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">21,185</td>
<td align="right">6.8%</td>
<td align="right">21,161</td>
<td align="right">6.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">53,469</td>
<td align="right">17.2%</td>
<td align="right">53,494</td>
<td align="right">17.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">120,570</td>
<td align="right">38.8%</td>
<td align="right">120,582</td>
<td align="right">38.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">28,760</td>
<td align="right">9.2%</td>
<td align="right">28,759</td>
<td align="right">9.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,880</td>
<td align="right">3.5%</td>
<td align="right">10,880</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">9,760</td>
<td align="right">3.1%</td>
<td align="right">9,760</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,540</td>
<td align="right">1.1%</td>
<td align="right">3,540</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,660</td>
<td align="right">0.9%</td>
<td align="right">2,660</td>
<td align="right">0.9%</td>
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
<td align="right">198,439,071</td>
<td align="right">7.4%</td>
<td align="right">198,457,236</td>
<td align="right">7.4%</td>
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
<td align="right">2,500,846,363</td>
<td align="right">92.6%</td>
<td align="right">2,500,815,597</td>
<td align="right">92.6%</td>
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
<td align="right">2,546,240</td>
<td align="right">0.1%</td>
<td align="right">2,546,240</td>
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
<td align="right">124,994</td>
<td align="right">66.5%</td>
<td align="right">125,006</td>
<td align="right">66.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">63,096</td>
<td align="right">33.5%</td>
<td align="right">63,097</td>
<td align="right">33.5%</td>
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
<td align="right">25,494</td>
<td align="right">20.4%</td>
<td align="right">25,503</td>
<td align="right">20.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">35,540</td>
<td align="right">28.4%</td>
<td align="right">35,543</td>
<td align="right">28.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">35,880</td>
<td align="right">28.7%</td>
<td align="right">35,880</td>
<td align="right">28.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">28,080</td>
<td align="right">22.5%</td>
<td align="right">28,080</td>
<td align="right">22.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,103,423,623</td>
<td align="right">72.7%</td>
<td align="right">4,136,647,715</td>
<td align="right">72.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">173,262,327</td>
<td align="right">3.1%</td>
<td align="right">173,306,231</td>
<td align="right">3.1%</td>
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
<td align="right">1,538,127,081</td>
<td align="right">27.2%</td>
<td align="right">1,538,230,497</td>
<td align="right">27.1%</td>
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
<td align="right">516,098</td>
<td align="right">13.5%</td>
<td align="right">518,153</td>
<td align="right">13.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,320,885</td>
<td align="right">86.5%</td>
<td align="right">3,321,701</td>
<td align="right">86.5%</td>
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
<td align="right">113,673</td>
<td align="right">22.0%</td>
<td align="right">115,689</td>
<td align="right">22.3%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">38,682</td>
<td align="right">7.5%</td>
<td align="right">38,708</td>
<td align="right">7.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">44,644</td>
<td align="right">8.7%</td>
<td align="right">44,649</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">220,320</td>
<td align="right">42.7%</td>
<td align="right">220,328</td>
<td align="right">42.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">30,180</td>
<td align="right">5.8%</td>
<td align="right">30,180</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">20,079</td>
<td align="right">3.9%</td>
<td align="right">20,079</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">13,020</td>
<td align="right">2.5%</td>
<td align="right">13,020</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">10,280</td>
<td align="right">2.0%</td>
<td align="right">10,280</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">7,780</td>
<td align="right">1.5%</td>
<td align="right">7,780</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">6,220</td>
<td align="right">1.2%</td>
<td align="right">6,220</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">5,680</td>
<td align="right">1.1%</td>
<td align="right">5,680</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">2,720</td>
<td align="right">0.5%</td>
<td align="right">2,720</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">2,280</td>
<td align="right">0.4%</td>
<td align="right">2,280</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">520</td>
<td align="right">0.1%</td>
<td align="right">520</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">971,627,052</td>
<td align="right">5.5%</td>
<td align="right">920,173,834</td>
<td align="right">5.2%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,397,439,514</td>
<td align="right">13.6%</td>
<td align="right">2,357,375,739</td>
<td align="right">13.4%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">303,840</td>
<td align="right">0.0%</td>
<td align="right">305,920</td>
<td align="right">0.0%</td>
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
<td align="right">15,218,229,851</td>
<td align="right">86.3%</td>
<td align="right">15,257,704,538</td>
<td align="right">86.5%</td>
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
<td align="left">Success</td>
<td align="right">19,028,168</td>
<td align="right">88.9%</td>
<td align="right">18,057,691</td>
<td align="right">88.3%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,373,635</td>
<td align="right">11.1%</td>
<td align="right">2,382,581</td>
<td align="right">11.7%</td>
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
<td align="left">shadowed</td>
<td align="right">118,368</td>
<td align="right">5.0%</td>
<td align="right">127,238</td>
<td align="right">5.3%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">7,072</td>
<td align="right">0.3%</td>
<td align="right">7,060</td>
<td align="right">0.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">21,158</td>
<td align="right">0.9%</td>
<td align="right">21,171</td>
<td align="right">0.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">82,487</td>
<td align="right">3.5%</td>
<td align="right">82,509</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">22,724</td>
<td align="right">1.0%</td>
<td align="right">22,729</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">272,813</td>
<td align="right">11.5%</td>
<td align="right">272,842</td>
<td align="right">11.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">161,134</td>
<td align="right">6.8%</td>
<td align="right">161,144</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">717,398</td>
<td align="right">30.2%</td>
<td align="right">717,424</td>
<td align="right">30.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">887,281</td>
<td align="right">37.4%</td>
<td align="right">887,264</td>
<td align="right">37.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">28,880</td>
<td align="right">1.2%</td>
<td align="right">28,880</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">20,420</td>
<td align="right">0.9%</td>
<td align="right">20,420</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">16,340</td>
<td align="right">0.7%</td>
<td align="right">16,340</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">8,000</td>
<td align="right">0.3%</td>
<td align="right">8,000</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">3,700</td>
<td align="right">0.2%</td>
<td align="right">3,700</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3,600</td>
<td align="right">0.2%</td>
<td align="right">3,600</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
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
<td align="left">property</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">427,303</td>
<td align="right">0.0%</td>
<td align="right">425,198</td>
<td align="right">0.0%</td>
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
<td align="right">20,367,517</td>
<td align="right">0.2%</td>
<td align="right">20,365,438</td>
<td align="right">0.2%</td>
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
<td align="right">11,377,446,317</td>
<td align="right">99.8%</td>
<td align="right">11,377,668,544</td>
<td align="right">99.8%</td>
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
<td align="right">9,860</td>
<td align="right">0.0%</td>
<td align="right">9,860</td>
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
<td align="right">520,638</td>
<td align="right">100.0%</td>
<td align="right">520,505</td>
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
<td align="right">86,813,534</td>
<td align="right">100.0%</td>
<td align="right">86,762,175</td>
<td align="right">100.0%</td>
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
<td align="right">8,447</td>
<td align="right">0.0%</td>
<td align="right">8,444</td>
<td align="right">0.0%</td>
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
<td align="right">8,460</td>
<td align="right">100.0%</td>
<td align="right">8,460</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,873,667</td>
<td align="right">18.1%</td>
<td align="right">173,874,666</td>
<td align="right">18.1%</td>
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
<td align="right">786,817,431</td>
<td align="right">81.9%</td>
<td align="right">786,820,390</td>
<td align="right">81.9%</td>
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
<td align="right">30,900</td>
<td align="right">0.0%</td>
<td align="right">30,900</td>
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
<td align="right">61,808</td>
<td align="right">89.7%</td>
<td align="right">61,817</td>
<td align="right">89.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,088</td>
<td align="right">10.3%</td>
<td align="right">7,089</td>
<td align="right">10.3%</td>
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
<td align="right">16,088</td>
<td align="right">26.0%</td>
<td align="right">16,097</td>
<td align="right">26.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">53.7%</td>
<td align="right">33,180</td>
<td align="right">53.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,040</td>
<td align="right">16.2%</td>
<td align="right">10,040</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">3.7%</td>
<td align="right">2,260</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">240</td>
<td align="right">0.4%</td>
<td align="right">240</td>
<td align="right">0.4%</td>
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
<td align="right">154,912,579</td>
<td align="right">5.8%</td>
<td align="right">165,847,793</td>
<td align="right">6.2%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">221,625,268</td>
<td align="right">8.3%</td>
<td align="right">232,736,194</td>
<td align="right">8.7%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,461,211,406</td>
<td align="right">91.6%</td>
<td align="right">2,450,085,399</td>
<td align="right">91.2%</td>
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
<td align="left">Failure</td>
<td align="right">106,228</td>
<td align="right">3.4%</td>
<td align="right">114,305</td>
<td align="right">3.4%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,040,277</td>
<td align="right">96.6%</td>
<td align="right">3,242,389</td>
<td align="right">96.6%</td>
<td align="right">6.6%</td>
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
<td align="left">not in dict</td>
<td align="right">11,320</td>
<td align="right">10.7%</td>
<td align="right">21,580</td>
<td align="right">18.9%</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">7,260</td>
<td align="right">6.8%</td>
<td align="right">5,080</td>
<td align="right">4.4%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,888</td>
<td align="right">9.3%</td>
<td align="right">9,885</td>
<td align="right">8.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">34,780</td>
<td align="right">32.7%</td>
<td align="right">34,780</td>
<td align="right">30.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,720</td>
<td align="right">13.9%</td>
<td align="right">14,720</td>
<td align="right">12.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">10,860</td>
<td align="right">10.2%</td>
<td align="right">10,860</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,920</td>
<td align="right">5.6%</td>
<td align="right">5,920</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">5,080</td>
<td align="right">4.8%</td>
<td align="right">5,080</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">4,760</td>
<td align="right">4.5%</td>
<td align="right">4,760</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,580</td>
<td align="right">1.5%</td>
<td align="right">1,580</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">60</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">875,718,616</td>
<td align="right">49.8%</td>
<td align="right">876,360,143</td>
<td align="right">49.8%</td>
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
<td align="right">882,772,047</td>
<td align="right">50.2%</td>
<td align="right">882,756,952</td>
<td align="right">50.2%</td>
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
<td align="right">2,900</td>
<td align="right">0.0%</td>
<td align="right">2,900</td>
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
<td align="right">262,939</td>
<td align="right">94.0%</td>
<td align="right">263,098</td>
<td align="right">94.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,725</td>
<td align="right">6.0%</td>
<td align="right">16,722</td>
<td align="right">6.0%</td>
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
<td align="left">array int</td>
<td align="right">66,080</td>
<td align="right">25.1%</td>
<td align="right">66,240</td>
<td align="right">25.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">44,059</td>
<td align="right">16.8%</td>
<td align="right">44,058</td>
<td align="right">16.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">108,760</td>
<td align="right">41.4%</td>
<td align="right">108,760</td>
<td align="right">41.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">31,140</td>
<td align="right">11.8%</td>
<td align="right">31,140</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">9,660</td>
<td align="right">3.7%</td>
<td align="right">9,660</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,240</td>
<td align="right">1.2%</td>
<td align="right">3,240</td>
<td align="right">1.2%</td>
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
<td align="right">6,000,722,428</td>
<td align="right">92.5%</td>
<td align="right">6,000,575,136</td>
<td align="right">92.5%</td>
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
<td align="right">143,730,077</td>
<td align="right">2.2%</td>
<td align="right">143,730,839</td>
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
<td align="right">485,847,400</td>
<td align="right">7.5%</td>
<td align="right">485,845,396</td>
<td align="right">7.5%</td>
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
<td align="right">660,999</td>
<td align="right">18.4%</td>
<td align="right">661,077</td>
<td align="right">18.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,923,838</td>
<td align="right">81.6%</td>
<td align="right">2,923,811</td>
<td align="right">81.6%</td>
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
<td align="left">bytearray</td>
<td align="right">1,236</td>
<td align="right">0.2%</td>
<td align="right">1,250</td>
<td align="right">0.2%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">18,647</td>
<td align="right">2.8%</td>
<td align="right">18,675</td>
<td align="right">2.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">33,893</td>
<td align="right">5.1%</td>
<td align="right">33,916</td>
<td align="right">5.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">33,500</td>
<td align="right">5.1%</td>
<td align="right">33,506</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">29,158</td>
<td align="right">4.4%</td>
<td align="right">29,162</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">103,461</td>
<td align="right">15.7%</td>
<td align="right">103,467</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">174,031</td>
<td align="right">26.3%</td>
<td align="right">174,023</td>
<td align="right">26.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">98,885</td>
<td align="right">15.0%</td>
<td align="right">98,887</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">165,168</td>
<td align="right">25.0%</td>
<td align="right">165,171</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2,600</td>
<td align="right">0.4%</td>
<td align="right">2,600</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">420</td>
<td align="right">0.1%</td>
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
<td align="right">1,751,780</td>
<td align="right">0.1%</td>
<td align="right">1,752,020</td>
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
<td align="right">1,547,765,519</td>
<td align="right">99.9%</td>
<td align="right">1,547,831,265</td>
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
<td align="right">4,240</td>
<td align="right">0.0%</td>
<td align="right">4,240</td>
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
<td align="right">2,889</td>
<td align="right">8.0%</td>
<td align="right">2,897</td>
<td align="right">8.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">33,004</td>
<td align="right">92.0%</td>
<td align="right">32,988</td>
<td align="right">91.9%</td>
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
<td align="right">1,929</td>
<td align="right">66.8%</td>
<td align="right">1,937</td>
<td align="right">66.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">580</td>
<td align="right">20.1%</td>
<td align="right">580</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">13.2%</td>
<td align="right">380</td>
<td align="right">13.1%</td>
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
<td align="right">1,710,504,092</td>
<td align="right">0.7%</td>
<td align="right">1,670,084,956</td>
<td align="right">0.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">27,420,073,358</td>
<td align="right">10.6%</td>
<td align="right">27,528,433,352</td>
<td align="right">10.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">89,137,477,687</td>
<td align="right">34.6%</td>
<td align="right">89,263,610,647</td>
<td align="right">34.6%</td>
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
<td align="right">139,408,347,597</td>
<td align="right">54.1%</td>
<td align="right">139,604,728,269</td>
<td align="right">54.1%</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">221,625,268</td>
<td align="right">2.1%</td>
<td align="right">232,736,194</td>
<td align="right">2.2%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,003,543,092</td>
<td align="right">18.7%</td>
<td align="right">2,100,821,308</td>
<td align="right">19.5%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,397,439,514</td>
<td align="right">22.4%</td>
<td align="right">2,357,375,739</td>
<td align="right">21.8%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">875,718,616</td>
<td align="right">8.2%</td>
<td align="right">876,360,143</td>
<td align="right">8.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,445,697,347</td>
<td align="right">13.5%</td>
<td align="right">1,445,488,108</td>
<td align="right">13.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">198,439,071</td>
<td align="right">1.9%</td>
<td align="right">198,457,236</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">697,701,812</td>
<td align="right">6.5%</td>
<td align="right">697,764,748</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,538,127,081</td>
<td align="right">14.3%</td>
<td align="right">1,538,230,497</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">664,854,192</td>
<td align="right">6.2%</td>
<td align="right">664,836,340</td>
<td align="right">6.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">485,847,400</td>
<td align="right">4.5%</td>
<td align="right">485,845,396</td>
<td align="right">4.5%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">354,093,915</td>
<td align="right">20.7%</td>
<td align="right">302,561,083</td>
<td align="right">18.1%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">123,432,380</td>
<td align="right">7.2%</td>
<td align="right">134,383,820</td>
<td align="right">8.0%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">66,323,040</td>
<td align="right">3.9%</td>
<td align="right">66,418,224</td>
<td align="right">4.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">86,444,996</td>
<td align="right">5.1%</td>
<td align="right">86,474,314</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">379,455,393</td>
<td align="right">22.2%</td>
<td align="right">379,527,249</td>
<td align="right">22.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">86,709,271</td>
<td align="right">5.1%</td>
<td align="right">86,723,857</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">112,146,899</td>
<td align="right">6.6%</td>
<td align="right">112,158,437</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">110,958,161</td>
<td align="right">6.5%</td>
<td align="right">110,960,451</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">67,224,146</td>
<td align="right">3.9%</td>
<td align="right">67,224,832</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">68,194,165</td>
<td align="right">4.0%</td>
<td align="right">68,193,973</td>
<td align="right">4.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">36,838,184</td>
<td align="right">0.4%</td>
<td align="right">36,845,205</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">858,606,571</td>
<td align="right">10.0%</td>
<td align="right">858,661,836</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,770,064,460</td>
<td align="right">79.1%</td>
<td align="right">6,769,698,586</td>
<td align="right">79.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,253,515,425</td>
<td align="right">73.1%</td>
<td align="right">6,253,189,813</td>
<td align="right">73.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">85,305,306</td>
<td align="right">1.0%</td>
<td align="right">85,309,371</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">176,932,256</td>
<td align="right">2.1%</td>
<td align="right">176,938,914</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">334,973,735</td>
<td align="right">3.9%</td>
<td align="right">334,982,422</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,440,175,458</td>
<td align="right">16.8%</td>
<td align="right">1,440,138,751</td>
<td align="right">16.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,445,503,778</td>
<td align="right">16.9%</td>
<td align="right">1,445,467,071</td>
<td align="right">16.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">340,274,728</td>
<td align="right">4.0%</td>
<td align="right">340,268,634</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,304,110,349</td>
<td align="right">26.9%</td>
<td align="right">2,304,128,907</td>
<td align="right">26.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,304,110,349</td>
<td align="right">26.9%</td>
<td align="right">2,304,128,907</td>
<td align="right">26.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">5,298,440</td>
<td align="right">0.1%</td>
<td align="right">5,298,440</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">29,880</td>
<td align="right">0.0%</td>
<td align="right">29,880</td>
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
<td align="left">Materialize dict (new key)</td>
<td align="right">128,160</td>
<td align="right">0.1%</td>
<td align="right">86,000</td>
<td align="right">0.0%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,264,612</td>
<td align="right"></td>
<td align="right">7,076,052</td>
<td align="right"></td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,859,703,602</td>
<td align="right"></td>
<td align="right">2,829,789,727</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,676,400,451</td>
<td align="right">47.4%</td>
<td align="right">11,740,236,365</td>
<td align="right">47.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,678,411,264</td>
<td align="right"></td>
<td align="right">11,742,247,945</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,866,565,180</td>
<td align="right">52.2%</td>
<td align="right">12,913,671,794</td>
<td align="right">52.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,976,081,308</td>
<td align="right">52.6%</td>
<td align="right">13,023,178,654</td>
<td align="right">52.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,676,364,729</td>
<td align="right"></td>
<td align="right">13,723,461,215</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">65,391,186</td>
<td align="right"></td>
<td align="right">65,571,284</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">112,664,849,061</td>
<td align="right">74.8%</td>
<td align="right">112,970,641,582</td>
<td align="right">74.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">96,656,710,822</td>
<td align="right">75.5%</td>
<td align="right">96,891,486,846</td>
<td align="right">75.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">38,007,604,253</td>
<td align="right">25.2%</td>
<td align="right">38,043,889,445</td>
<td align="right">25.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,299,747</td>
<td align="right"></td>
<td align="right">174,269,588</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">31,421,560,127</td>
<td align="right">24.5%</td>
<td align="right">31,417,896,057</td>
<td align="right">24.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">93,883,974</td>
<td align="right">0.4%</td>
<td align="right">93,874,074</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">71,669,883</td>
<td align="right"></td>
<td align="right">71,662,865</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">15,632,154</td>
<td align="right">0.1%</td>
<td align="right">15,632,786</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,414,057,665</td>
<td align="right"></td>
<td align="right">4,414,190,792</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,384,660</td>
<td align="right">1.9%</td>
<td align="right">3,384,660</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">16,480</td>
<td align="right">0.0%</td>
<td align="right">16,480 / 0 !!</td>
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
<td align="right">116,104,208</td>
<td align="right">19,627,828,567</td>
<td align="right">0</td>
<td align="right">116,111,535</td>
<td align="right">19,616,530,952</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,756,040</td>
<td align="right">6,970,260,448</td>
<td align="right">0</td>
<td align="right">10,756,040</td>
<td align="right">6,970,260,412</td>
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
<td align="right">300</td>
<td align="right">300</td>
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
<td align="right">460</td>
<td align="right">460</td>
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
<td align="right">1,820</td>
<td align="right">1,820</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-08-05
