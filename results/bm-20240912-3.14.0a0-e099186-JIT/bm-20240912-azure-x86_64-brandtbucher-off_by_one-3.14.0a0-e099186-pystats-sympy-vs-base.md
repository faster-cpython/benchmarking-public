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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">51,945,467</td>
<td align="right">44,143,204</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">117,210,149</td>
<td align="right">123,856,034</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">434,192</td>
<td align="right">409,950</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">189,424</td>
<td align="right">179,501</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">180,122,793</td>
<td align="right">172,668,985</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,094,425</td>
<td align="right">39,810,203</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">940</td>
<td align="right">920</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">3,600</td>
<td align="right">3,540</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">41,393</td>
<td align="right">40,844</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">76,340</td>
<td align="right">75,340</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">591,742,367</td>
<td align="right">584,194,447</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">22,668,152</td>
<td align="right">22,385,116</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">21,352,869</td>
<td align="right">21,581,936</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,980,074</td>
<td align="right">23,206,076</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">16,321,531</td>
<td align="right">16,165,763</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">14,521,946</td>
<td align="right">14,383,703</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">26,826,091</td>
<td align="right">27,074,540</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,919,097</td>
<td align="right">1,905,875</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">43,045,582</td>
<td align="right">43,317,863</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">11,480</td>
<td align="right">11,420</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,506,198</td>
<td align="right">3,488,218</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,850,216</td>
<td align="right">3,830,931</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,081,669</td>
<td align="right">4,062,101</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">101,060</td>
<td align="right">100,600</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">39,676</td>
<td align="right">39,848</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33,833,218</td>
<td align="right">33,687,365</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,760</td>
<td align="right">4,740</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">121,615,029</td>
<td align="right">122,118,894</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">49,997</td>
<td align="right">50,179</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">72,160</td>
<td align="right">71,900</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">29,311,706</td>
<td align="right">29,207,277</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,355,193</td>
<td align="right">22,281,465</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">140,707,881</td>
<td align="right">140,259,300</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">10,542,298</td>
<td align="right">10,508,766</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">22,510</td>
<td align="right">22,571</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">232,459</td>
<td align="right">231,910</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">54,931,583</td>
<td align="right">54,808,075</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,638,829</td>
<td align="right">3,630,983</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">197,146,116</td>
<td align="right">196,724,934</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">64,757,706</td>
<td align="right">64,893,769</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">126,130,288</td>
<td align="right">126,378,589</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">840,826</td>
<td align="right">839,234</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">168,592,845</td>
<td align="right">168,894,718</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">170,560,678</td>
<td align="right">170,272,945</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">92,651,842</td>
<td align="right">92,783,338</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">93,880</td>
<td align="right">93,754</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">244,881</td>
<td align="right">244,553</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">55,892,422</td>
<td align="right">55,966,575</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">51,050,971</td>
<td align="right">51,115,099</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">54,922,680</td>
<td align="right">54,977,216</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">7,414,530</td>
<td align="right">7,407,344</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">139,180</td>
<td align="right">139,060</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">119,244</td>
<td align="right">119,144</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">1,204</td>
<td align="right">1,203</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,030,186</td>
<td align="right">2,031,866</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">22,983,493</td>
<td align="right">22,964,728</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">10,023,333</td>
<td align="right">10,031,244</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">23,930,337</td>
<td align="right">23,911,466</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">27,184,486</td>
<td align="right">27,163,428</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,340,231</td>
<td align="right">1,339,232</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,615,267</td>
<td align="right">3,612,747</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">39,215,106</td>
<td align="right">39,188,140</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">119,058</td>
<td align="right">119,130</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">3,445,072</td>
<td align="right">3,443,007</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,450,564</td>
<td align="right">2,449,106</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">227,611</td>
<td align="right">227,480</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">41,797,017</td>
<td align="right">41,773,801</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">44,715,980</td>
<td align="right">44,692,518</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">142,511</td>
<td align="right">142,437</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,518,450</td>
<td align="right">1,517,692</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">4,008</td>
<td align="right">4,006</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,841,351</td>
<td align="right">2,839,935</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,515,229</td>
<td align="right">1,514,482</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">49,711,115</td>
<td align="right">49,735,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">165,203</td>
<td align="right">165,127</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">906,533</td>
<td align="right">906,947</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">906,533</td>
<td align="right">906,947</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">906,533</td>
<td align="right">906,947</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,679,030</td>
<td align="right">1,678,265</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">769,294</td>
<td align="right">768,946</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,352,364</td>
<td align="right">2,351,419</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">411,790</td>
<td align="right">411,948</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,870,070</td>
<td align="right">1,870,772</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">5,333,882</td>
<td align="right">5,331,892</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,450,186</td>
<td align="right">1,449,718</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,349,022</td>
<td align="right">1,349,394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">210,380</td>
<td align="right">210,322</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">122,242,773</td>
<td align="right">122,209,535</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,842,138</td>
<td align="right">4,840,913</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">19,021,273</td>
<td align="right">19,025,389</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">181,848</td>
<td align="right">181,810</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,095,562</td>
<td align="right">3,094,917</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,564,066</td>
<td align="right">16,560,826</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,027,429</td>
<td align="right">5,026,483</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">532,240</td>
<td align="right">532,144</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">21,656,000</td>
<td align="right">21,652,143</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,045,967</td>
<td align="right">5,045,112</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,628,009</td>
<td align="right">2,628,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">13,209,634</td>
<td align="right">13,207,510</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,768</td>
<td align="right">12,766</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,592,093</td>
<td align="right">1,591,875</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,388,295</td>
<td align="right">1,388,118</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">23,538,717</td>
<td align="right">23,535,799</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">42,260,652</td>
<td align="right">42,255,442</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">20,030,614</td>
<td align="right">20,028,226</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">19,733,641</td>
<td align="right">19,735,957</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,054,772</td>
<td align="right">16,052,908</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,181,915</td>
<td align="right">1,182,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">530,706</td>
<td align="right">530,761</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">887,770</td>
<td align="right">887,858</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">262,586</td>
<td align="right">262,561</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">9,430,479</td>
<td align="right">9,429,626</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">532,765</td>
<td align="right">532,719</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,784,196</td>
<td align="right">1,784,045</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">178,043,952</td>
<td align="right">178,058,095</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">7,231,045</td>
<td align="right">7,230,522</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">24,831,045</td>
<td align="right">24,832,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,582,390</td>
<td align="right">2,582,204</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">32,967,521</td>
<td align="right">32,969,724</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,624,375</td>
<td align="right">10,623,666</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">12,328,564</td>
<td align="right">12,327,765</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,312,372</td>
<td align="right">3,312,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">30,656,797</td>
<td align="right">30,655,103</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,028,520</td>
<td align="right">1,028,464</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">5,719,510</td>
<td align="right">5,719,203</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,098,305</td>
<td align="right">2,098,194</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">28,012,216</td>
<td align="right">28,013,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">17,002,255</td>
<td align="right">17,001,487</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,572,567</td>
<td align="right">1,572,513</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">18,576,503</td>
<td align="right">18,575,983</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,847,012</td>
<td align="right">4,847,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,491,122</td>
<td align="right">7,490,931</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,607,991</td>
<td align="right">8,607,802</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">867,370</td>
<td align="right">867,386</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">543,653</td>
<td align="right">543,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,118,638</td>
<td align="right">1,118,651</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">4,746,266</td>
<td align="right">4,746,214</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">13,187,815</td>
<td align="right">13,187,957</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,656,052</td>
<td align="right">12,655,949</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">25,266,570</td>
<td align="right">25,266,396</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">14,540,828</td>
<td align="right">14,540,733</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,135,739</td>
<td align="right">8,135,702</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,958,396</td>
<td align="right">8,958,430</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">8,206,807</td>
<td align="right">8,206,836</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">13,978,371</td>
<td align="right">13,978,347</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">519,360</td>
<td align="right">519,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">442,840</td>
<td align="right">442,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">282,600</td>
<td align="right">282,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">282,560</td>
<td align="right">282,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">233,080</td>
<td align="right">233,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">140,940</td>
<td align="right">140,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">117,080</td>
<td align="right">117,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">63,800</td>
<td align="right">63,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">47,548</td>
<td align="right">47,548</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">19,260</td>
<td align="right">19,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">3,100</td>
<td align="right">3,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">2,660</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,540</td>
<td align="right">2,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,040</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,840</td>
<td align="right">1,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
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
<td align="right">29,256,771</td>
<td align="right">60.8%</td>
<td align="right">29,152,321</td>
<td align="right">60.7%</td>
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
<td align="right">18,838,107</td>
<td align="right">39.1%</td>
<td align="right">18,840,210</td>
<td align="right">39.2%</td>
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
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">120</td>
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
<td align="right">6,704</td>
<td align="right">12.2%</td>
<td align="right">6,696</td>
<td align="right">12.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">48,231</td>
<td align="right">87.8%</td>
<td align="right">48,260</td>
<td align="right">87.8%</td>
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
<td align="left">lshift</td>
<td align="right">226</td>
<td align="right">0.5%</td>
<td align="right">224</td>
<td align="right">0.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,742</td>
<td align="right">14.0%</td>
<td align="right">6,782</td>
<td align="right">14.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">376</td>
<td align="right">0.8%</td>
<td align="right">378</td>
<td align="right">0.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">5,840</td>
<td align="right">12.1%</td>
<td align="right">5,820</td>
<td align="right">12.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,183</td>
<td align="right">2.5%</td>
<td align="right">1,187</td>
<td align="right">2.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,817</td>
<td align="right">3.8%</td>
<td align="right">1,821</td>
<td align="right">3.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,841</td>
<td align="right">8.0%</td>
<td align="right">3,845</td>
<td align="right">8.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">2,051</td>
<td align="right">4.3%</td>
<td align="right">2,052</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,144</td>
<td align="right">19.0%</td>
<td align="right">9,140</td>
<td align="right">18.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,521</td>
<td align="right">5.2%</td>
<td align="right">2,522</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,824</td>
<td align="right">7.9%</td>
<td align="right">3,823</td>
<td align="right">7.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,700</td>
<td align="right">7.7%</td>
<td align="right">3,700</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,854</td>
<td align="right">5.9%</td>
<td align="right">2,854</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,120</td>
<td align="right">4.4%</td>
<td align="right">2,120</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">1,108</td>
<td align="right">2.3%</td>
<td align="right">1,108</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">582</td>
<td align="right">1.2%</td>
<td align="right">582</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">300</td>
<td align="right">0.6%</td>
<td align="right">300</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
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
<td align="right">532,765</td>
<td align="right">100.0%</td>
<td align="right">532,719</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">3,488,392</td>
<td align="right">7.5%</td>
<td align="right">3,470,437</td>
<td align="right">7.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,927</td>
<td align="right">0.0%</td>
<td align="right">14,934</td>
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
<td align="right">42,687,035</td>
<td align="right">92.4%</td>
<td align="right">42,695,053</td>
<td align="right">92.4%</td>
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
<td align="right">10,334</td>
<td align="right">57.3%</td>
<td align="right">10,310</td>
<td align="right">57.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,712</td>
<td align="right">42.7%</td>
<td align="right">7,711</td>
<td align="right">42.8%</td>
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
<td align="left">buffer int</td>
<td align="right">1,200</td>
<td align="right">11.6%</td>
<td align="right">1,220</td>
<td align="right">11.8%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,152</td>
<td align="right">69.2%</td>
<td align="right">7,108</td>
<td align="right">68.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,960</td>
<td align="right">19.0%</td>
<td align="right">1,960</td>
<td align="right">19.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">29,752,479</td>
<td align="right">7.2%</td>
<td align="right">29,926,954</td>
<td align="right">7.2%</td>
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
<td align="right">385,078,464</td>
<td align="right">92.8%</td>
<td align="right">385,055,147</td>
<td align="right">92.7%</td>
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
<td align="right">167,508</td>
<td align="right">0.0%</td>
<td align="right">167,510</td>
<td align="right">0.0%</td>
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
<td align="right">21,800</td>
<td align="right">0.0%</td>
<td align="right">21,800</td>
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
<td align="right">659,957</td>
<td align="right">100.0%</td>
<td align="right">663,224</td>
<td align="right">100.0%</td>
<td align="right">0.5%</td>
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
<td align="right">260</td>
<td align="right">260 / 0 !!</td>
<td align="right">260</td>
<td align="right">260 / 0 !!</td>
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
<td align="right">7,984</td>
<td align="right">48.8%</td>
<td align="right">7,984</td>
<td align="right">48.8%</td>
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
<td align="right">3,580</td>
<td align="right">21.9%</td>
<td align="right">3,580</td>
<td align="right">21.9%</td>
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
<td align="right">22,595,428</td>
<td align="right">25.3%</td>
<td align="right">22,312,363</td>
<td align="right">25.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">465,611</td>
<td align="right">0.5%</td>
<td align="right">467,568</td>
<td align="right">0.5%</td>
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
<td align="right">66,066,997</td>
<td align="right">74.1%</td>
<td align="right">66,007,709</td>
<td align="right">74.3%</td>
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
<td align="right">18,208</td>
<td align="right">22.4%</td>
<td align="right">18,236</td>
<td align="right">22.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">63,096</td>
<td align="right">77.6%</td>
<td align="right">63,133</td>
<td align="right">77.6%</td>
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
<td align="left">bool</td>
<td align="right">417</td>
<td align="right">0.7%</td>
<td align="right">411</td>
<td align="right">0.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">16,225</td>
<td align="right">25.7%</td>
<td align="right">16,284</td>
<td align="right">25.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,920</td>
<td align="right">15.7%</td>
<td align="right">9,908</td>
<td align="right">15.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,862</td>
<td align="right">20.4%</td>
<td align="right">12,852</td>
<td align="right">20.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">12,152</td>
<td align="right">19.3%</td>
<td align="right">12,158</td>
<td align="right">19.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,320</td>
<td align="right">16.4%</td>
<td align="right">10,320</td>
<td align="right">16.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">220</td>
<td align="right">0.3%</td>
<td align="right">220</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,907,965</td>
<td align="right">6.0%</td>
<td align="right">1,894,795</td>
<td align="right">6.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,686,108</td>
<td align="right">93.9%</td>
<td align="right">29,687,038</td>
<td align="right">94.0%</td>
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
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">1,200</td>
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
<td align="right">9,892</td>
<td align="right">88.9%</td>
<td align="right">9,840</td>
<td align="right">88.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,240</td>
<td align="right">11.1%</td>
<td align="right">1,240</td>
<td align="right">11.2%</td>
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
<td align="left">list</td>
<td align="right">940</td>
<td align="right">9.5%</td>
<td align="right">900</td>
<td align="right">9.1%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,556</td>
<td align="right">35.9%</td>
<td align="right">3,524</td>
<td align="right">35.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">5,116</td>
<td align="right">51.7%</td>
<td align="right">5,136</td>
<td align="right">52.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">280</td>
<td align="right">2.8%</td>
<td align="right">280</td>
<td align="right">2.8%</td>
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
<td align="right">113,433</td>
<td align="right">0.2%</td>
<td align="right">116,424</td>
<td align="right">0.2%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">21,983,757</td>
<td align="right">44.6%</td>
<td align="right">21,954,354</td>
<td align="right">44.6%</td>
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
<td align="right">27,137,773</td>
<td align="right">55.1%</td>
<td align="right">27,116,667</td>
<td align="right">55.1%</td>
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
<td align="right">14,019</td>
<td align="right">28.8%</td>
<td align="right">14,087</td>
<td align="right">28.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,705</td>
<td align="right">71.2%</td>
<td align="right">34,747</td>
<td align="right">71.2%</td>
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
<td align="left">set</td>
<td align="right">4,005</td>
<td align="right">11.5%</td>
<td align="right">3,991</td>
<td align="right">11.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">16,378</td>
<td align="right">47.2%</td>
<td align="right">16,430</td>
<td align="right">47.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,462</td>
<td align="right">10.0%</td>
<td align="right">3,466</td>
<td align="right">10.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,720</td>
<td align="right">13.6%</td>
<td align="right">4,720</td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,960</td>
<td align="right">5.6%</td>
<td align="right">1,960</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,840</td>
<td align="right">5.3%</td>
<td align="right">1,840</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,400</td>
<td align="right">4.0%</td>
<td align="right">1,400</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">780</td>
<td align="right">2.2%</td>
<td align="right">780</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">80</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">33,216,584</td>
<td align="right">8.6%</td>
<td align="right">31,544,498</td>
<td align="right">8.2%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">286,581,839</td>
<td align="right">74.5%</td>
<td align="right">289,903,977</td>
<td align="right">75.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">64,542,646</td>
<td align="right">16.8%</td>
<td align="right">64,678,510</td>
<td align="right">16.7%</td>
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
<td align="right">22,500</td>
<td align="right">0.0%</td>
<td align="right">22,500</td>
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
<td align="right">710,878</td>
<td align="right">85.4%</td>
<td align="right">679,394</td>
<td align="right">84.8%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">121,886</td>
<td align="right">14.6%</td>
<td align="right">122,083</td>
<td align="right">15.2%</td>
<td align="right">0.2%</td>
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
<td align="right">59,460</td>
<td align="right">48.8%</td>
<td align="right">59,615</td>
<td align="right">48.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">11,714</td>
<td align="right">9.6%</td>
<td align="right">11,734</td>
<td align="right">9.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">9,262</td>
<td align="right">7.6%</td>
<td align="right">9,274</td>
<td align="right">7.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,907</td>
<td align="right">7.3%</td>
<td align="right">8,916</td>
<td align="right">7.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">7,743</td>
<td align="right">6.4%</td>
<td align="right">7,744</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">14,880</td>
<td align="right">12.2%</td>
<td align="right">14,880</td>
<td align="right">12.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4,800</td>
<td align="right">3.9%</td>
<td align="right">4,800</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">880</td>
<td align="right">0.7%</td>
<td align="right">880</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">265,086,714</td>
<td align="right">99.9%</td>
<td align="right">264,927,066</td>
<td align="right">99.9%</td>
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
<td align="right">90,019</td>
<td align="right">0.0%</td>
<td align="right">90,016</td>
<td align="right">0.0%</td>
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
<td align="right">20,380</td>
<td align="right">0.0%</td>
<td align="right">20,380</td>
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
<td align="right">91,989</td>
<td align="right">100.0%</td>
<td align="right">91,954</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">604</td>
<td align="right">0.0%</td>
<td align="right">603</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,996,031</td>
<td align="right">100.0%</td>
<td align="right">2,996,172</td>
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
<td align="right">600</td>
<td align="right">100.0%</td>
<td align="right">600</td>
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
<td align="right">999,160</td>
<td align="right">67.8%</td>
<td align="right">999,144</td>
<td align="right">67.8%</td>
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
<td align="right">439,720</td>
<td align="right">29.9%</td>
<td align="right">439,720</td>
<td align="right">29.9%</td>
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
<td align="right">30,640</td>
<td align="right">2.1%</td>
<td align="right">30,640</td>
<td align="right">2.1%</td>
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
<td align="right">620</td>
<td align="right">16.8%</td>
<td align="right">620</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,060</td>
<td align="right">83.2%</td>
<td align="right">3,060</td>
<td align="right">83.2%</td>
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
<td align="left">list</td>
<td align="right">3,060</td>
<td align="right">100.0%</td>
<td align="right">3,060</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">426,066</td>
<td align="right">3.5%</td>
<td align="right">425,720</td>
<td align="right">3.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,175,418</td>
<td align="right">93.0%</td>
<td align="right">11,179,880</td>
<td align="right">93.0%</td>
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
<td align="right">402,986</td>
<td align="right">3.4%</td>
<td align="right">403,144</td>
<td align="right">3.4%</td>
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
<td align="right">12,972</td>
<td align="right">77.8%</td>
<td align="right">12,972</td>
<td align="right">77.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,704</td>
<td align="right">22.2%</td>
<td align="right">3,704</td>
<td align="right">22.2%</td>
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
<td align="left">class attr simple</td>
<td align="right">1,960</td>
<td align="right">52.9%</td>
<td align="right">1,960</td>
<td align="right">52.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,444</td>
<td align="right">39.0%</td>
<td align="right">1,444</td>
<td align="right">39.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">240</td>
<td align="right">6.5%</td>
<td align="right">240</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">60</td>
<td align="right">1.6%</td>
<td align="right">60</td>
<td align="right">1.6%</td>
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
<td align="right">940</td>
<td align="right">100.0%</td>
<td align="right">920</td>
<td align="right">100.0%</td>
<td align="right">-2.1%</td>
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
<td align="right">183,867</td>
<td align="right">0.8%</td>
<td align="right">173,936</td>
<td align="right">0.8%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">22,622,056</td>
<td align="right">99.2%</td>
<td align="right">22,627,002</td>
<td align="right">99.2%</td>
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
<td align="right">2,833</td>
<td align="right">51.0%</td>
<td align="right">2,843</td>
<td align="right">51.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,724</td>
<td align="right">49.0%</td>
<td align="right">2,722</td>
<td align="right">48.9%</td>
<td align="right">-0.1%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">2,833</td>
<td align="right">100.0%</td>
<td align="right">2,843</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
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
<td align="right">196,679,803</td>
<td align="right">93.8%</td>
<td align="right">196,889,681</td>
<td align="right">93.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">440,011</td>
<td align="right">0.2%</td>
<td align="right">440,148</td>
<td align="right">0.2%</td>
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
<td align="right">12,580,670</td>
<td align="right">6.0%</td>
<td align="right">12,580,598</td>
<td align="right">6.0%</td>
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
<td align="right">22,756</td>
<td align="right">27.6%</td>
<td align="right">22,728</td>
<td align="right">27.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">59,738</td>
<td align="right">72.4%</td>
<td align="right">59,732</td>
<td align="right">72.4%</td>
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
<td align="left">dict</td>
<td align="right">2,080</td>
<td align="right">9.1%</td>
<td align="right">2,060</td>
<td align="right">9.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,634</td>
<td align="right">7.2%</td>
<td align="right">1,646</td>
<td align="right">7.2%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">3,509</td>
<td align="right">15.4%</td>
<td align="right">3,498</td>
<td align="right">15.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,440</td>
<td align="right">6.3%</td>
<td align="right">1,438</td>
<td align="right">6.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,793</td>
<td align="right">47.4%</td>
<td align="right">10,786</td>
<td align="right">47.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">3,260</td>
<td align="right">14.3%</td>
<td align="right">3,260</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
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
<td align="right">27,516</td>
<td align="right">0.0%</td>
<td align="right">27,690</td>
<td align="right">0.0%</td>
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
<td align="right">105,735,096</td>
<td align="right">100.0%</td>
<td align="right">105,880,957</td>
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
<td align="left">Failure</td>
<td align="right">776</td>
<td align="right">6.4%</td>
<td align="right">778</td>
<td align="right">6.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,384</td>
<td align="right">93.6%</td>
<td align="right">11,380</td>
<td align="right">93.6%</td>
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
<td align="right">716</td>
<td align="right">92.3%</td>
<td align="right">718</td>
<td align="right">92.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">60</td>
<td align="right">7.7%</td>
<td align="right">60</td>
<td align="right">7.7%</td>
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
<td align="right">64,485,031</td>
<td align="right">1.7%</td>
<td align="right">62,992,166</td>
<td align="right">1.7%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,194,492,695</td>
<td align="right">32.0%</td>
<td align="right">1,179,738,983</td>
<td align="right">31.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">164,079,238</td>
<td align="right">4.4%</td>
<td align="right">163,765,748</td>
<td align="right">4.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,311,199,631</td>
<td align="right">61.9%</td>
<td align="right">2,310,317,673</td>
<td align="right">62.2%</td>
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
<td align="right">22,595,428</td>
<td align="right">13.8%</td>
<td align="right">22,312,363</td>
<td align="right">13.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,907,965</td>
<td align="right">1.2%</td>
<td align="right">1,894,795</td>
<td align="right">1.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,488,392</td>
<td align="right">2.1%</td>
<td align="right">3,470,437</td>
<td align="right">2.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">29,256,771</td>
<td align="right">17.9%</td>
<td align="right">29,152,321</td>
<td align="right">17.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">64,542,646</td>
<td align="right">39.5%</td>
<td align="right">64,678,510</td>
<td align="right">39.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">27,137,773</td>
<td align="right">16.6%</td>
<td align="right">27,116,667</td>
<td align="right">16.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">402,986</td>
<td align="right">0.2%</td>
<td align="right">403,144</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">532,765</td>
<td align="right">0.3%</td>
<td align="right">532,719</td>
<td align="right">0.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,580,670</td>
<td align="right">7.7%</td>
<td align="right">12,580,598</td>
<td align="right">7.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">439,720</td>
<td align="right">0.3%</td>
<td align="right">439,720</td>
<td align="right">0.3%</td>
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
<td align="right">14,012,773</td>
<td align="right">21.7%</td>
<td align="right">12,287,571</td>
<td align="right">19.5%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">14,347,924</td>
<td align="right">22.3%</td>
<td align="right">14,577,336</td>
<td align="right">23.1%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,548,850</td>
<td align="right">14.8%</td>
<td align="right">9,654,665</td>
<td align="right">15.3%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,407,697</td>
<td align="right">8.4%</td>
<td align="right">5,348,658</td>
<td align="right">8.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,162,961</td>
<td align="right">9.6%</td>
<td align="right">6,108,710</td>
<td align="right">9.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">464,011</td>
<td align="right">0.7%</td>
<td align="right">465,968</td>
<td align="right">0.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,669,067</td>
<td align="right">5.7%</td>
<td align="right">3,675,997</td>
<td align="right">5.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">425,086</td>
<td align="right">0.7%</td>
<td align="right">424,740</td>
<td align="right">0.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,661,158</td>
<td align="right">4.1%</td>
<td align="right">2,661,191</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">6,512,226</td>
<td align="right">10.1%</td>
<td align="right">6,512,214</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">29,115,545</td>
<td align="right">10.7%</td>
<td align="right">29,341,479</td>
<td align="right">10.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">126,373,185</td>
<td align="right">46.3%</td>
<td align="right">126,620,937</td>
<td align="right">46.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">126,373,185</td>
<td align="right">46.3%</td>
<td align="right">126,620,937</td>
<td align="right">46.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">146,406,320</td>
<td align="right">53.7%</td>
<td align="right">146,304,532</td>
<td align="right">53.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">1,365,894</td>
<td align="right">0.5%</td>
<td align="right">1,365,030</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">52,805,850</td>
<td align="right">19.4%</td>
<td align="right">52,825,923</td>
<td align="right">19.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">243,347,602</td>
<td align="right">89.2%</td>
<td align="right">243,267,528</td>
<td align="right">89.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">97,250,340</td>
<td align="right">35.7%</td>
<td align="right">97,272,158</td>
<td align="right">35.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">97,257,640</td>
<td align="right">35.7%</td>
<td align="right">97,279,458</td>
<td align="right">35.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">23,782,907</td>
<td align="right">8.7%</td>
<td align="right">23,783,836</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">11,824,676</td>
<td align="right">4.3%</td>
<td align="right">11,825,081</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">6,960</td>
<td align="right">0.0%</td>
<td align="right">6,960</td>
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
<td align="right">1,105,296</td>
<td align="right"></td>
<td align="right">1,406,708</td>
<td align="right"></td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">4,916,194</td>
<td align="right"></td>
<td align="right">5,240,255</td>
<td align="right"></td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">193,514,842</td>
<td align="right"></td>
<td align="right">190,551,613</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">2,666,038,816</td>
<td align="right">2,666,038,816 / 0 !!</td>
<td align="right">2,690,270,557</td>
<td align="right">2,690,270,557 / 0 !!</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">3,814,872</td>
<td align="right"></td>
<td align="right">3,837,455</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">2,755,887,217</td>
<td align="right">2,755,887,217 / 0 !!</td>
<td align="right">2,771,537,104</td>
<td align="right">2,771,537,104 / 0 !!</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">1,790,531,295</td>
<td align="right">1,790,531,295 / 0 !!</td>
<td align="right">1,781,045,726</td>
<td align="right">1,781,045,726 / 0 !!</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,065,497</td>
<td align="right">0.2%</td>
<td align="right">1,061,099</td>
<td align="right">0.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">337,716,714</td>
<td align="right"></td>
<td align="right">336,869,044</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">2,275,196,533</td>
<td align="right">2,275,196,533 / 0 !!</td>
<td align="right">2,274,286,710</td>
<td align="right">2,274,286,710 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,392,810</td>
<td align="right"></td>
<td align="right">1,393,072</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">364,778,873</td>
<td align="right"></td>
<td align="right">364,769,506</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">364,539,796</td>
<td align="right">55.4%</td>
<td align="right">364,530,437</td>
<td align="right">55.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">291,882,273</td>
<td align="right">44.4%</td>
<td align="right">291,889,653</td>
<td align="right">44.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">292,972,230</td>
<td align="right">44.6%</td>
<td align="right">292,975,212</td>
<td align="right">44.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">306,897,550</td>
<td align="right"></td>
<td align="right">306,898,096</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">24,460</td>
<td align="right">0.0%</td>
<td align="right">24,460</td>
<td align="right">0.0%</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">2,166</td>
<td align="right">2.4%</td>
<td align="right">2,588</td>
<td align="right">2.8%</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">313</td>
<td align="right">1.0%</td>
<td align="right">354</td>
<td align="right">1.0%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">242</td>
<td align="right">0.3%</td>
<td align="right">264</td>
<td align="right">0.3%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">32,113</td>
<td align="right">36.1%</td>
<td align="right">34,377</td>
<td align="right">36.8%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">52,688</td>
<td align="right">59.3%</td>
<td align="right">55,391</td>
<td align="right">59.3%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">88,852</td>
<td align="right"></td>
<td align="right">93,363</td>
<td align="right"></td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">56,739</td>
<td align="right">63.9%</td>
<td align="right">58,986</td>
<td align="right">63.2%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">370,299,253</td>
<td align="right"></td>
<td align="right">379,972,319</td>
<td align="right"></td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">5,313,086,408</td>
<td align="right">1,434.8%</td>
<td align="right">5,378,206,869</td>
<td align="right">1,415.4%</td>
<td align="right">1.2%</td>
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">280</td>
<td align="right">0.3%</td>
<td align="right">280</td>
<td align="right">0.3%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">32,113</td>
<td align="right"></td>
<td align="right">34,377</td>
<td align="right"></td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">30,494</td>
<td align="right">95.0%</td>
<td align="right">32,520</td>
<td align="right">94.6%</td>
<td align="right">6.6%</td>
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
<td align="right">160</td>
<td align="right">0.5%</td>
<td align="right">160</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
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
<td align="right">541</td>
<td align="right">1.7%</td>
<td align="right">548</td>
<td align="right">1.6%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">4,086</td>
<td align="right">12.7%</td>
<td align="right">4,394</td>
<td align="right">12.8%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">4,342</td>
<td align="right">13.5%</td>
<td align="right">4,732</td>
<td align="right">13.8%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">12,371</td>
<td align="right">38.5%</td>
<td align="right">13,183</td>
<td align="right">38.3%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">7,850</td>
<td align="right">24.4%</td>
<td align="right">8,232</td>
<td align="right">23.9%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,783</td>
<td align="right">8.7%</td>
<td align="right">3,148</td>
<td align="right">9.2%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">140</td>
<td align="right">0.4%</td>
<td align="right">140</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="right">4,106</td>
<td align="right">12.8%</td>
<td align="right">4,403</td>
<td align="right">12.8%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,390</td>
<td align="right">7.4%</td>
<td align="right">2,606</td>
<td align="right">7.6%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,202</td>
<td align="right">25.5%</td>
<td align="right">8,774</td>
<td align="right">25.5%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">10,020</td>
<td align="right">31.2%</td>
<td align="right">10,563</td>
<td align="right">30.7%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">5,216</td>
<td align="right">16.2%</td>
<td align="right">5,594</td>
<td align="right">16.3%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">520</td>
<td align="right">1.6%</td>
<td align="right">540</td>
<td align="right">1.6%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">3,765</td>
<td align="right">238</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">3,765</td>
<td align="right">238</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">32,196,470</td>
<td align="right">40,147,913</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">280</td>
<td align="right">320</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">320</td>
<td align="right">360</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">63,191,792</td>
<td align="right">70,882,767</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">12,543,943</td>
<td align="right">13,803,888</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">3,560</td>
<td align="right">3,880</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">18,438,651</td>
<td align="right">19,725,500</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">144,817,957</td>
<td align="right">152,655,385</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,900,454</td>
<td align="right">2,749,171</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">219,328,059</td>
<td align="right">230,723,682</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">26,754,177</td>
<td align="right">28,128,295</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">30,763,079</td>
<td align="right">32,117,232</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">42,601,601</td>
<td align="right">40,984,246</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">24,567,338</td>
<td align="right">25,451,894</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">17,702,941</td>
<td align="right">18,306,396</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">36,831,318</td>
<td align="right">38,025,715</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">54,643,961</td>
<td align="right">52,966,847</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">45,139,045</td>
<td align="right">46,420,692</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">45,298,333</td>
<td align="right">46,580,554</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">370,299,253</td>
<td align="right">379,972,319</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">5,287,217</td>
<td align="right">5,424,823</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">343,159,545</td>
<td align="right">351,458,591</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">6,934,691</td>
<td align="right">7,091,575</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">6,420</td>
<td align="right">6,560</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">3,080</td>
<td align="right">3,140</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">3,080</td>
<td align="right">3,140</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">14,861,045</td>
<td align="right">15,146,585</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,767,100</td>
<td align="right">16,052,574</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">15,767,100</td>
<td align="right">16,052,574</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">6,188,640</td>
<td align="right">6,292,970</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,220</td>
<td align="right">1,240</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">1,220</td>
<td align="right">1,240</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">16,211,390</td>
<td align="right">16,457,634</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">5,760</td>
<td align="right">5,840</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">5,748,572</td>
<td align="right">5,814,211</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">3,900</td>
<td align="right">3,940</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">8,160</td>
<td align="right">8,240</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">110,600,015</td>
<td align="right">111,682,359</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">13,483,635</td>
<td align="right">13,360,281</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">20,606,252</td>
<td align="right">20,418,578</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">12,585,721</td>
<td align="right">12,471,437</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">9,898,793</td>
<td align="right">9,810,002</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,222,888</td>
<td align="right">2,242,593</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">74,917,664</td>
<td align="right">74,284,955</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">7,800</td>
<td align="right">7,860</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">14,860</td>
<td align="right">14,960</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">63,958,959</td>
<td align="right">64,357,945</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">15,040,597</td>
<td align="right">14,946,884</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">134,622,839</td>
<td align="right">133,808,080</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">50,101,240</td>
<td align="right">49,807,262</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">23,181,783</td>
<td align="right">23,316,519</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">24,308,844</td>
<td align="right">24,448,578</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">30,080</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">26,443,210</td>
<td align="right">26,579,973</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">57,915,092</td>
<td align="right">58,198,888</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">60,121,678</td>
<td align="right">60,415,893</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">35,847,324</td>
<td align="right">36,011,264</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">341,516</td>
<td align="right">343,055</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">58,774,676</td>
<td align="right">59,034,705</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,680</td>
<td align="right">13,740</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">31,960</td>
<td align="right">32,100</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">338,436</td>
<td align="right">339,915</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">268,362</td>
<td align="right">269,475</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">711,330</td>
<td align="right">714,236</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">20,594,081</td>
<td align="right">20,513,740</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">20,560</td>
<td align="right">20,640</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">20,560</td>
<td align="right">20,640</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">346,698</td>
<td align="right">348,004</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">97,568</td>
<td align="right">97,902</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">536,849,140</td>
<td align="right">538,678,801</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">47,680</td>
<td align="right">47,840</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">57,005,171</td>
<td align="right">56,818,559</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">36,660</td>
<td align="right">36,780</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">18,429,541</td>
<td align="right">18,369,539</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">3,238,333</td>
<td align="right">3,248,589</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">969,070</td>
<td align="right">966,011</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">40,000</td>
<td align="right">40,120</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">40,000</td>
<td align="right">40,120</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">52,819,883</td>
<td align="right">52,970,784</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">36,260</td>
<td align="right">36,360</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">54,718,942</td>
<td align="right">54,869,776</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">62,126,643</td>
<td align="right">62,295,894</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">106,660</td>
<td align="right">106,920</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">78,339,363</td>
<td align="right">78,522,205</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">10,204,708</td>
<td align="right">10,227,477</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">114,386</td>
<td align="right">114,134</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">83,917,278</td>
<td align="right">84,100,329</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">115,192,090</td>
<td align="right">115,430,886</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">441,650</td>
<td align="right">442,537</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">441,650</td>
<td align="right">442,537</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">15,530,849</td>
<td align="right">15,500,699</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">107,732,835</td>
<td align="right">107,931,873</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">67,474,044</td>
<td align="right">67,350,775</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">57,325,528</td>
<td align="right">57,221,135</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">21,599,642</td>
<td align="right">21,638,805</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,894,574</td>
<td align="right">1,891,163</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">67,180</td>
<td align="right">67,300</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">10,972,495</td>
<td align="right">10,991,853</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">42,413,389</td>
<td align="right">42,486,587</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">268,440</td>
<td align="right">268,880</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">14,376,634</td>
<td align="right">14,400,165</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">44,902,662</td>
<td align="right">44,969,818</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">413,620</td>
<td align="right">414,220</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">413,620</td>
<td align="right">414,220</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">4,449,005</td>
<td align="right">4,455,399</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">943,873</td>
<td align="right">945,209</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">231,245,916</td>
<td align="right">231,550,139</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">61,720</td>
<td align="right">61,800</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">52,324,352</td>
<td align="right">52,257,116</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">82,627</td>
<td align="right">82,733</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">854,560</td>
<td align="right">855,600</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">20,899,299</td>
<td align="right">20,924,190</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">17,974,464</td>
<td align="right">17,953,120</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">418,540</td>
<td align="right">419,000</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">20,966,892</td>
<td align="right">20,945,133</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">852,199</td>
<td align="right">853,075</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">617,260</td>
<td align="right">617,820</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">658,678</td>
<td align="right">659,254</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">658,678</td>
<td align="right">659,254</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">189,120</td>
<td align="right">189,280</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,226,880</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">185,058</td>
<td align="right">185,199</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">6,117,621</td>
<td align="right">6,121,820</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">5,929,572</td>
<td align="right">5,933,615</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,985,172</td>
<td align="right">3,987,804</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">36,769,917</td>
<td align="right">36,793,902</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,466,546</td>
<td align="right">1,467,466</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,317,420</td>
<td align="right">1,318,220</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">968,377</td>
<td align="right">968,963</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">5,570,519</td>
<td align="right">5,573,866</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">271,145</td>
<td align="right">271,299</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,824,926</td>
<td align="right">4,827,646</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,833,778</td>
<td align="right">1,834,790</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">7,570,823</td>
<td align="right">7,574,883</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,909,025</td>
<td align="right">2,907,490</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">860,243</td>
<td align="right">860,693</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">39,280</td>
<td align="right">39,300</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">10,463,948</td>
<td align="right">10,468,959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">5,185,160</td>
<td align="right">5,187,616</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,295,280</td>
<td align="right">2,296,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">9,495,324</td>
<td align="right">9,499,608</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">14,856,973</td>
<td align="right">14,862,705</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">13,206,702</td>
<td align="right">13,211,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">3,015,486</td>
<td align="right">3,016,618</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">10,563,186</td>
<td align="right">10,566,945</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">10,789,970</td>
<td align="right">10,793,611</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">10,789,970</td>
<td align="right">10,793,611</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">18,113,484</td>
<td align="right">18,119,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">24,155,428</td>
<td align="right">24,163,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">1,837,105</td>
<td align="right">1,837,670</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">4,520,323</td>
<td align="right">4,521,713</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">25,113,948</td>
<td align="right">25,121,591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">6,087,981</td>
<td align="right">6,089,758</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,675,809</td>
<td align="right">9,678,542</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,675,809</td>
<td align="right">9,678,542</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">9,962,649</td>
<td align="right">9,965,462</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">19,952,764</td>
<td align="right">19,957,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">15,275,915</td>
<td align="right">15,279,626</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">18,236,850</td>
<td align="right">18,232,568</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">460,541</td>
<td align="right">460,646</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,488,115</td>
<td align="right">1,488,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">41,125,654</td>
<td align="right">41,117,899</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">30,256,866</td>
<td align="right">30,262,383</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">26,479,184</td>
<td align="right">26,474,801</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">3,150,816</td>
<td align="right">3,151,336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">432,240,271</td>
<td align="right">432,174,517</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,932,855</td>
<td align="right">1,933,146</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">25,419,354</td>
<td align="right">25,423,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">7,758,743</td>
<td align="right">7,757,856</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">26,033,025</td>
<td align="right">26,035,974</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">27,952,016</td>
<td align="right">27,949,337</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">8,731,078</td>
<td align="right">8,731,715</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">906,055</td>
<td align="right">905,989</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,890,809</td>
<td align="right">1,890,925</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">51,383,575</td>
<td align="right">51,386,319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">1,201,220</td>
<td align="right">1,201,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">18,702,203</td>
<td align="right">18,702,958</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">16,858,338</td>
<td align="right">16,858,566</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">4,317,978</td>
<td align="right">4,317,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">446,180</td>
<td align="right">446,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">49,740</td>
<td align="right">49,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">11,920</td>
<td align="right">11,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">11,040</td>
<td align="right">11,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,540</td>
<td align="right">2,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">180</td>
<td align="right">180</td>
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
<td align="left">SEND</td>
<td align="right">60</td>
<td align="right">80</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,864</td>
<td align="right">4,056</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">7,080</td>
<td align="right">7,180</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20</td>
<td align="right">20</td>
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
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
