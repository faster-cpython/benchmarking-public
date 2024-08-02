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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">284,862,813</td>
<td align="right">279,351,038</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,378,910</td>
<td align="right">2,424,272</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">367,884,473</td>
<td align="right">362,370,936</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,292,360</td>
<td align="right">2,324,100</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">218,108,224</td>
<td align="right">215,355,991</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">221,677,039</td>
<td align="right">218,930,805</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">232,947,885</td>
<td align="right">230,126,094</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">582,744,046</td>
<td align="right">577,273,816</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">393,472,240</td>
<td align="right">390,761,594</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">707,108,146</td>
<td align="right">704,473,960</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">84,180,275</td>
<td align="right">83,915,663</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">889,303,939</td>
<td align="right">886,587,143</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">6,621,224</td>
<td align="right">6,640,497</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,039,006,909</td>
<td align="right">1,036,281,904</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,103,787,744</td>
<td align="right">1,101,079,617</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">116,351,718</td>
<td align="right">116,080,459</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,850,341,499</td>
<td align="right">3,842,192,692</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,010,184,793</td>
<td align="right">4,002,016,656</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">6,968,141</td>
<td align="right">6,980,879</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">83,178,470</td>
<td align="right">83,318,431</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,911,107,796</td>
<td align="right">1,908,412,569</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,326,116,354</td>
<td align="right">2,322,852,672</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,287,698</td>
<td align="right">40,333,063</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,137,379,238</td>
<td align="right">3,134,609,879</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">7,571,436</td>
<td align="right">7,577,585</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">337,041,494</td>
<td align="right">336,783,202</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">244,493</td>
<td align="right">244,316</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,576,347</td>
<td align="right">17,589,000</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,287,315,384</td>
<td align="right">19,274,548,518</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,621,730</td>
<td align="right">9,628,095</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,178,361,799</td>
<td align="right">4,175,894,451</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">94,728,665</td>
<td align="right">94,673,583</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,782,273</td>
<td align="right">81,827,618</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,057,956,300</td>
<td align="right">5,055,253,722</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,002,452,960</td>
<td align="right">5,000,047,958</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">195,628,331</td>
<td align="right">195,534,722</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">392,613,497</td>
<td align="right">392,799,433</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,482,912,500</td>
<td align="right">5,480,427,822</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">258,900,764</td>
<td align="right">258,789,149</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">170,777,387</td>
<td align="right">170,847,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">75,881,959</td>
<td align="right">75,851,792</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">85,240,895</td>
<td align="right">85,273,736</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">111,137,082</td>
<td align="right">111,176,725</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">205,143,952</td>
<td align="right">205,192,895</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">106,905,115</td>
<td align="right">106,928,839</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">122,090,780</td>
<td align="right">122,066,230</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">384,583,031</td>
<td align="right">384,660,182</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">972,296,214</td>
<td align="right">972,111,115</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">435,426,431</td>
<td align="right">435,506,355</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">70,842,853</td>
<td align="right">70,855,795</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,651,722</td>
<td align="right">9,650,021</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">147,340,858</td>
<td align="right">147,316,058</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,051,458</td>
<td align="right">13,049,274</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">13,039,796</td>
<td align="right">13,037,661</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">13,047,556</td>
<td align="right">13,045,421</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,228,898,323</td>
<td align="right">1,229,097,853</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,216,120</td>
<td align="right">9,214,768</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">298,673,423</td>
<td align="right">298,714,083</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,586,930,157</td>
<td align="right">1,587,121,196</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">474,075,192</td>
<td align="right">474,130,664</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,677,101,908</td>
<td align="right">2,677,374,064</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,463,279</td>
<td align="right">53,457,947</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">291,256,181</td>
<td align="right">291,282,572</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">97,180,491</td>
<td align="right">97,189,176</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">1,470,381</td>
<td align="right">1,470,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">150,931,114</td>
<td align="right">150,919,079</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,227,435,144</td>
<td align="right">2,227,610,614</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68,003,171</td>
<td align="right">68,008,314</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,809,721</td>
<td align="right">72,814,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,998,288</td>
<td align="right">48,994,741</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">42,168,028</td>
<td align="right">42,165,158</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">290,306,021</td>
<td align="right">290,286,555</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">211,817</td>
<td align="right">211,803</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,406,628</td>
<td align="right">58,402,919</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">692,445</td>
<td align="right">692,403</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,145,536,423</td>
<td align="right">1,145,600,181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,156</td>
<td align="right">1,873,054</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,363,913,693</td>
<td align="right">1,363,840,008</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,782,521</td>
<td align="right">1,782,614</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">587,014,230</td>
<td align="right">587,044,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,925,421</td>
<td align="right">13,924,717</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">982,676,917</td>
<td align="right">982,725,689</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">188,503,030</td>
<td align="right">188,512,211</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,167,351</td>
<td align="right">78,165,004</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,305,312</td>
<td align="right">20,304,822</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">587,646,824</td>
<td align="right">587,660,573</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">33,191,732</td>
<td align="right">33,190,986</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,822,878</td>
<td align="right">1,822,839</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">64,745,740</td>
<td align="right">64,744,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">102,672,405</td>
<td align="right">102,674,438</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,386,263,539</td>
<td align="right">2,386,308,214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">329,110,770</td>
<td align="right">329,104,818</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">353,081,759</td>
<td align="right">353,075,388</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,281,161,255</td>
<td align="right">3,281,103,788</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">225,415,796</td>
<td align="right">225,419,326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">39,941,272</td>
<td align="right">39,940,657</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">398,881,055</td>
<td align="right">398,875,342</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">414,889,045</td>
<td align="right">414,894,626</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,431,221</td>
<td align="right">47,430,701</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">356,572,073</td>
<td align="right">356,568,331</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,049,030,334</td>
<td align="right">5,049,082,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">312,671,416</td>
<td align="right">312,674,621</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">622,415,050</td>
<td align="right">622,421,167</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">321,272,285</td>
<td align="right">321,269,607</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">444,741,958</td>
<td align="right">444,738,440</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,689,919</td>
<td align="right">18,689,775</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">148,276,556</td>
<td align="right">148,275,573</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">144,083,093</td>
<td align="right">144,084,002</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">350,116,512</td>
<td align="right">350,114,476</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,092,801</td>
<td align="right">83,092,434</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,613,031</td>
<td align="right">9,612,991</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,407,362</td>
<td align="right">4,407,344</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">104,677,949</td>
<td align="right">104,677,584</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">380,082,977</td>
<td align="right">380,081,684</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">278,941,351</td>
<td align="right">278,940,411</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">513,039,466</td>
<td align="right">513,037,943</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">184,206,090</td>
<td align="right">184,205,605</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">48,007,764</td>
<td align="right">48,007,885</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,710,922</td>
<td align="right">555,709,544</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">397,311,628</td>
<td align="right">397,310,728</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">104,988,640</td>
<td align="right">104,988,405</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">355,906,393</td>
<td align="right">355,905,756</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,875,572</td>
<td align="right">10,875,590</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">22,311,460</td>
<td align="right">22,311,495</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,253,159,924</td>
<td align="right">1,253,158,161</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,110,948</td>
<td align="right">91,110,829</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">143,312,568</td>
<td align="right">143,312,426</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">273,425,301</td>
<td align="right">273,425,053</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">33,292,524</td>
<td align="right">33,292,498</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,553,972</td>
<td align="right">158,553,853</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">172,973,210</td>
<td align="right">172,973,084</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">189,470,651</td>
<td align="right">189,470,524</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">31,599,594</td>
<td align="right">31,599,576</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,312,698</td>
<td align="right">233,312,589</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">72,221,094</td>
<td align="right">72,221,125</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,103,753</td>
<td align="right">216,103,842</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,613,140</td>
<td align="right">46,613,156</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">251,030,871</td>
<td align="right">251,030,957</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,048,693,833</td>
<td align="right">1,048,693,474</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">32,547,400</td>
<td align="right">32,547,392</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">44,302,700</td>
<td align="right">44,302,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">275,140,068</td>
<td align="right">275,140,046</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">326,507,454</td>
<td align="right">326,507,440</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,375</td>
<td align="right">190,039,368</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,554</td>
<td align="right">173,318,550</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">228,622,194</td>
<td align="right">228,622,190</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">65,832,030</td>
<td align="right">65,832,029</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,024,591</td>
<td align="right">402,024,585</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,216,145</td>
<td align="right">786,216,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">105,672,682</td>
<td align="right">105,672,682</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">98,885,500</td>
<td align="right">98,885,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">90,672,600</td>
<td align="right">90,672,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">90,667,460</td>
<td align="right">90,667,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,504,501</td>
<td align="right">52,504,501</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">52,179,020</td>
<td align="right">52,179,020</td>
<td align="right">0.0%</td>
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
<td align="left">CALL_STR_1</td>
<td align="right">35,125,401</td>
<td align="right">35,125,401</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">12,088,500</td>
<td align="right">12,088,500</td>
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
<td align="right">7,254,200</td>
<td align="right">7,254,200</td>
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
<td align="right">546,580</td>
<td align="right">546,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">502,660</td>
<td align="right">502,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">162,960</td>
<td align="right">162,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">150,560</td>
<td align="right">150,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">147,160</td>
<td align="right">147,160</td>
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
<td align="left">SET_ADD</td>
<td align="right">49,180</td>
<td align="right">49,180</td>
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
<td align="right">22,820</td>
<td align="right">22,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">16,007</td>
<td align="right">16,007</td>
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
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">420,432,418</td>
<td align="right">5.8%</td>
<td align="right">420,618,328</td>
<td align="right">5.8%</td>
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
<td align="right">29,500,920</td>
<td align="right">0.4%</td>
<td align="right">29,500,860</td>
<td align="right">0.4%</td>
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
<td align="right">6,825,711,397</td>
<td align="right">94.2%</td>
<td align="right">6,825,714,760</td>
<td align="right">94.2%</td>
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
<td align="right">591,500</td>
<td align="right">35.2%</td>
<td align="right">591,460</td>
<td align="right">35.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,090,499</td>
<td align="right">64.8%</td>
<td align="right">1,090,505</td>
<td align="right">64.8%</td>
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
<td align="left">or</td>
<td align="right">12,514</td>
<td align="right">1.1%</td>
<td align="right">12,530</td>
<td align="right">1.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,885</td>
<td align="right">2.7%</td>
<td align="right">29,914</td>
<td align="right">2.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">37,279</td>
<td align="right">3.4%</td>
<td align="right">37,263</td>
<td align="right">3.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">15,973</td>
<td align="right">1.5%</td>
<td align="right">15,969</td>
<td align="right">1.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">38,086</td>
<td align="right">3.5%</td>
<td align="right">38,077</td>
<td align="right">3.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,608</td>
<td align="right">0.8%</td>
<td align="right">8,606</td>
<td align="right">0.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,464</td>
<td align="right">1.0%</td>
<td align="right">10,463</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,628</td>
<td align="right">7.5%</td>
<td align="right">81,625</td>
<td align="right">7.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,606</td>
<td align="right">71.7%</td>
<td align="right">781,602</td>
<td align="right">71.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,096</td>
<td align="right">2.9%</td>
<td align="right">32,096</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,844</td>
<td align="right">0.8%</td>
<td align="right">8,844</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,528</td>
<td align="right">0.5%</td>
<td align="right">5,528</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,030</td>
<td align="right">0.5%</td>
<td align="right">5,030</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,894</td>
<td align="right">0.2%</td>
<td align="right">1,894</td>
<td align="right">0.2%</td>
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
<td align="right">416,380,838</td>
<td align="right">8.9%</td>
<td align="right">416,386,370</td>
<td align="right">8.9%</td>
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
<td align="right">1,753,473</td>
<td align="right">0.0%</td>
<td align="right">1,753,455</td>
<td align="right">0.0%</td>
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
<td align="right">4,279,190,127</td>
<td align="right">91.1%</td>
<td align="right">4,279,158,754</td>
<td align="right">91.1%</td>
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
<td align="right">148,597</td>
<td align="right">56.8%</td>
<td align="right">148,628</td>
<td align="right">56.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">113,083</td>
<td align="right">43.2%</td>
<td align="right">113,083</td>
<td align="right">43.2%</td>
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
<td align="right">30,935</td>
<td align="right">20.8%</td>
<td align="right">30,966</td>
<td align="right">20.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">44,020</td>
<td align="right">29.6%</td>
<td align="right">44,020</td>
<td align="right">29.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,318</td>
<td align="right">20.4%</td>
<td align="right">30,318</td>
<td align="right">20.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,760</td>
<td align="right">13.3%</td>
<td align="right">19,760</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">10.9%</td>
<td align="right">16,200</td>
<td align="right">10.9%</td>
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
<td align="left">list slice</td>
<td align="right">1,060</td>
<td align="right">0.7%</td>
<td align="right">1,060</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">760</td>
<td align="right">0.5%</td>
<td align="right">760</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,783,907,964</td>
<td align="right">97.2%</td>
<td align="right">10,770,062,562</td>
<td align="right">97.2%</td>
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
<td align="right">307,789,047</td>
<td align="right">2.8%</td>
<td align="right">307,457,369</td>
<td align="right">2.8%</td>
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
<td align="right">195,685,256</td>
<td align="right">1.8%</td>
<td align="right">195,623,184</td>
<td align="right">1.8%</td>
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
<td align="left">Failure</td>
<td align="right">76,862</td>
<td align="right">1.8%</td>
<td align="right">76,796</td>
<td align="right">1.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,171,065</td>
<td align="right">98.2%</td>
<td align="right">4,169,478</td>
<td align="right">98.2%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">67,942</td>
<td align="right">88.4%</td>
<td align="right">67,876</td>
<td align="right">88.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">8,440</td>
<td align="right">11.0%</td>
<td align="right">8,440</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,000</td>
<td align="right">3.9%</td>
<td align="right">3,000</td>
<td align="right">3.9%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">737,333</td>
<td align="right">0.0%</td>
<td align="right">737,989</td>
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
<td align="right">4,837,825,866</td>
<td align="right">98.0%</td>
<td align="right">4,835,120,841</td>
<td align="right">98.0%</td>
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
<td align="right">97,721,473</td>
<td align="right">2.0%</td>
<td align="right">97,730,809</td>
<td align="right">2.0%</td>
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
<td align="right">65,771</td>
<td align="right">33.5%</td>
<td align="right">65,764</td>
<td align="right">33.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">130,580</td>
<td align="right">66.5%</td>
<td align="right">130,592</td>
<td align="right">66.5%</td>
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
<td align="right">1,544</td>
<td align="right">1.2%</td>
<td align="right">1,542</td>
<td align="right">1.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,686</td>
<td align="right">8.9%</td>
<td align="right">11,700</td>
<td align="right">9.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">25,813</td>
<td align="right">19.8%</td>
<td align="right">25,786</td>
<td align="right">19.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">26,575</td>
<td align="right">20.4%</td>
<td align="right">26,599</td>
<td align="right">20.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,365</td>
<td align="right">12.5%</td>
<td align="right">16,377</td>
<td align="right">12.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,377</td>
<td align="right">11.0%</td>
<td align="right">14,368</td>
<td align="right">11.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,740</td>
<td align="right">14.4%</td>
<td align="right">18,740</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">8.2%</td>
<td align="right">10,680</td>
<td align="right">8.2%</td>
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
<td align="right">1,600</td>
<td align="right">1.2%</td>
<td align="right">1,600</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">960</td>
<td align="right">0.7%</td>
<td align="right">960</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">500</td>
<td align="right">0.4%</td>
<td align="right">500</td>
<td align="right">0.4%</td>
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
<td align="right">197,986,248</td>
<td align="right">7.7%</td>
<td align="right">197,892,669</td>
<td align="right">7.7%</td>
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
<td align="right">2,366,774,553</td>
<td align="right">92.3%</td>
<td align="right">2,366,806,187</td>
<td align="right">92.3%</td>
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
<td align="right">100,323</td>
<td align="right">63.0%</td>
<td align="right">100,293</td>
<td align="right">63.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">59,020</td>
<td align="right">37.0%</td>
<td align="right">59,020</td>
<td align="right">37.0%</td>
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
<td align="right">13,546</td>
<td align="right">13.5%</td>
<td align="right">13,514</td>
<td align="right">13.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">22,977</td>
<td align="right">22.9%</td>
<td align="right">22,979</td>
<td align="right">22.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">55,120</td>
<td align="right">54.9%</td>
<td align="right">55,120</td>
<td align="right">55.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">8,680</td>
<td align="right">8.7%</td>
<td align="right">8,680</td>
<td align="right">8.7%</td>
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
<td align="right">176,322</td>
<td align="right">0.0%</td>
<td align="right">174,418</td>
<td align="right">0.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">75,915,749</td>
<td align="right">14.1%</td>
<td align="right">75,883,802</td>
<td align="right">14.1%</td>
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
<td align="right">461,045,877</td>
<td align="right">85.8%</td>
<td align="right">461,062,454</td>
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
<td align="right">47,838</td>
<td align="right">33.6%</td>
<td align="right">47,766</td>
<td align="right">33.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">94,694</td>
<td align="right">66.4%</td>
<td align="right">94,642</td>
<td align="right">66.5%</td>
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
<td align="left">bytes</td>
<td align="right">320</td>
<td align="right">0.3%</td>
<td align="right">319</td>
<td align="right">0.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,423</td>
<td align="right">38.5%</td>
<td align="right">36,351</td>
<td align="right">38.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,148</td>
<td align="right">10.7%</td>
<td align="right">10,168</td>
<td align="right">10.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,603</td>
<td align="right">10.1%</td>
<td align="right">9,604</td>
<td align="right">10.1%</td>
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
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,480</td>
<td align="right">6.8%</td>
<td align="right">6,480</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,520</td>
<td align="right">5.8%</td>
<td align="right">5,520</td>
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
<td align="left">reversed list</td>
<td align="right">3,220</td>
<td align="right">3.4%</td>
<td align="right">3,220</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,980</td>
<td align="right">2.1%</td>
<td align="right">1,980</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,360</td>
<td align="right">1.4%</td>
<td align="right">1,360</td>
<td align="right">1.4%</td>
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
<td align="right">14,298,335,676</td>
<td align="right">92.1%</td>
<td align="right">14,282,366,383</td>
<td align="right">92.1%</td>
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
<td align="right">1,223,447,878</td>
<td align="right">7.9%</td>
<td align="right">1,223,501,418</td>
<td align="right">7.9%</td>
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
<td align="right">246,758,598</td>
<td align="right">1.6%</td>
<td align="right">246,763,071</td>
<td align="right">1.6%</td>
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
<td align="right">323,880</td>
<td align="right">0.0%</td>
<td align="right">323,880</td>
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
<td align="right">791,843</td>
<td align="right">13.2%</td>
<td align="right">791,742</td>
<td align="right">13.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,195,794</td>
<td align="right">86.8%</td>
<td align="right">5,195,600</td>
<td align="right">86.8%</td>
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
<td align="left">class attr simple</td>
<td align="right">45,506</td>
<td align="right">5.7%</td>
<td align="right">45,442</td>
<td align="right">5.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,784</td>
<td align="right">0.7%</td>
<td align="right">5,780</td>
<td align="right">0.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">54,588</td>
<td align="right">6.9%</td>
<td align="right">54,612</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">149,737</td>
<td align="right">18.9%</td>
<td align="right">149,681</td>
<td align="right">18.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">13,427</td>
<td align="right">1.7%</td>
<td align="right">13,429</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">73,027</td>
<td align="right">9.2%</td>
<td align="right">73,020</td>
<td align="right">9.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">78,007</td>
<td align="right">9.9%</td>
<td align="right">78,005</td>
<td align="right">9.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">266,967</td>
<td align="right">33.7%</td>
<td align="right">266,973</td>
<td align="right">33.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,800</td>
<td align="right">3.4%</td>
<td align="right">26,800</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">19,740</td>
<td align="right">2.5%</td>
<td align="right">19,740</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,840</td>
<td align="right">2.0%</td>
<td align="right">15,840</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,280</td>
<td align="right">1.8%</td>
<td align="right">14,280</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.5%</td>
<td align="right">12,240</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">11,360</td>
<td align="right">1.4%</td>
<td align="right">11,360</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,780</td>
<td align="right">0.4%</td>
<td align="right">2,780</td>
<td align="right">0.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,300,772,855</td>
<td align="right">99.6%</td>
<td align="right">5,298,019,956</td>
<td align="right">99.6%</td>
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
<td align="right">443,084</td>
<td align="right">0.0%</td>
<td align="right">443,245</td>
<td align="right">0.0%</td>
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
<td align="right">20,303,359</td>
<td align="right">0.4%</td>
<td align="right">20,303,267</td>
<td align="right">0.4%</td>
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
<td align="right">11,340</td>
<td align="right">0.0%</td>
<td align="right">11,340</td>
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
<td align="right">445,037</td>
<td align="right">100.0%</td>
<td align="right">444,800</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">83,635,071</td>
<td align="right">100.0%</td>
<td align="right">83,680,377</td>
<td align="right">100.0%</td>
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
<td align="right">8,127</td>
<td align="right">0.0%</td>
<td align="right">8,127</td>
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
<td align="right">7,880</td>
<td align="right">100.0%</td>
<td align="right">7,880</td>
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
<td align="right">173,284,194</td>
<td align="right">18.1%</td>
<td align="right">173,284,190</td>
<td align="right">18.1%</td>
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
<td align="right">786,185,485</td>
<td align="right">81.9%</td>
<td align="right">786,185,491</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">68,518,000</td>
<td align="right">2.5%</td>
<td align="right">68,522,622</td>
<td align="right">2.5%</td>
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
<td align="right">98,663,364</td>
<td align="right">3.6%</td>
<td align="right">98,667,875</td>
<td align="right">3.6%</td>
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
<td align="right">2,670,888,652</td>
<td align="right">96.4%</td>
<td align="right">2,670,955,858</td>
<td align="right">96.4%</td>
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
<td align="right">1,383,262</td>
<td align="right">95.1%</td>
<td align="right">1,383,355</td>
<td align="right">95.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">70,968</td>
<td align="right">4.9%</td>
<td align="right">70,968</td>
<td align="right">4.9%</td>
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
<td align="left">not managed dict</td>
<td align="right">16,728</td>
<td align="right">23.6%</td>
<td align="right">16,728</td>
<td align="right">23.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,760</td>
<td align="right">19.4%</td>
<td align="right">13,760</td>
<td align="right">19.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">10,260</td>
<td align="right">14.5%</td>
<td align="right">10,260</td>
<td align="right">14.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,580</td>
<td align="right">12.1%</td>
<td align="right">8,580</td>
<td align="right">12.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,860</td>
<td align="right">6.8%</td>
<td align="right">4,860</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,740</td>
<td align="right">6.7%</td>
<td align="right">4,740</td>
<td align="right">6.7%</td>
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
<td align="right">3,820</td>
<td align="right">5.4%</td>
<td align="right">3,820</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">2,940</td>
<td align="right">4.1%</td>
<td align="right">2,940</td>
<td align="right">4.1%</td>
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
<td align="right">818,440,666</td>
<td align="right">92.7%</td>
<td align="right">818,471,160</td>
<td align="right">92.7%</td>
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
<td align="right">64,682,141</td>
<td align="right">7.3%</td>
<td align="right">64,680,816</td>
<td align="right">7.3%</td>
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
<td align="right">52,573</td>
<td align="right">82.7%</td>
<td align="right">52,578</td>
<td align="right">82.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,026</td>
<td align="right">17.3%</td>
<td align="right">11,026</td>
<td align="right">17.3%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">10,153</td>
<td align="right">19.3%</td>
<td align="right">10,158</td>
<td align="right">19.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">33,100</td>
<td align="right">63.0%</td>
<td align="right">33,100</td>
<td align="right">63.0%</td>
<td align="right">0.0%</td>
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
<td align="left">other</td>
<td align="right">1,140</td>
<td align="right">2.2%</td>
<td align="right">1,140</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">900</td>
<td align="right">1.7%</td>
<td align="right">900</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">800</td>
<td align="right">1.5%</td>
<td align="right">800</td>
<td align="right">1.5%</td>
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
<td align="right">5,784,238,889</td>
<td align="right">95.5%</td>
<td align="right">5,776,369,712</td>
<td align="right">95.5%</td>
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
<td align="right">273,161,925</td>
<td align="right">4.5%</td>
<td align="right">273,165,122</td>
<td align="right">4.5%</td>
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
<td align="right">49,030,084</td>
<td align="right">0.8%</td>
<td align="right">49,029,598</td>
<td align="right">0.8%</td>
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
<td align="right">175,175</td>
<td align="right">13.6%</td>
<td align="right">175,092</td>
<td align="right">13.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,108,780</td>
<td align="right">86.4%</td>
<td align="right">1,108,710</td>
<td align="right">86.4%</td>
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
<td align="right">13,460</td>
<td align="right">7.7%</td>
<td align="right">13,380</td>
<td align="right">7.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,591</td>
<td align="right">2.6%</td>
<td align="right">4,587</td>
<td align="right">2.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">4,722</td>
<td align="right">2.7%</td>
<td align="right">4,724</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">14,687</td>
<td align="right">8.4%</td>
<td align="right">14,684</td>
<td align="right">8.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,378</td>
<td align="right">7.6%</td>
<td align="right">13,379</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,124</td>
<td align="right">15.5%</td>
<td align="right">27,126</td>
<td align="right">15.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">46,268</td>
<td align="right">26.4%</td>
<td align="right">46,266</td>
<td align="right">26.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">48,025</td>
<td align="right">27.4%</td>
<td align="right">48,026</td>
<td align="right">27.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,493,213,603</td>
<td align="right">100.0%</td>
<td align="right">1,487,515,297</td>
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
<td align="right">215,315</td>
<td align="right">0.0%</td>
<td align="right">215,198</td>
<td align="right">0.0%</td>
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
<td align="right">27,104</td>
<td align="right">92.9%</td>
<td align="right">27,044</td>
<td align="right">92.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,074</td>
<td align="right">7.1%</td>
<td align="right">2,074</td>
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
<td align="right">1,434</td>
<td align="right">69.1%</td>
<td align="right">1,434</td>
<td align="right">69.1%</td>
<td align="right">0.0%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">57,626,069,805</td>
<td align="right">54.6%</td>
<td align="right">57,571,681,297</td>
<td align="right">54.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">37,408,098,050</td>
<td align="right">35.5%</td>
<td align="right">37,379,663,299</td>
<td align="right">35.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,796,648,965</td>
<td align="right">9.3%</td>
<td align="right">9,793,988,408</td>
<td align="right">9.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">673,025,298</td>
<td align="right">0.6%</td>
<td align="right">672,970,739</td>
<td align="right">0.6%</td>
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
<td align="left">CALL</td>
<td align="right">307,789,047</td>
<td align="right">9.1%</td>
<td align="right">307,457,369</td>
<td align="right">9.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">197,986,248</td>
<td align="right">5.9%</td>
<td align="right">197,892,669</td>
<td align="right">5.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">420,432,418</td>
<td align="right">12.5%</td>
<td align="right">420,618,328</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">75,915,749</td>
<td align="right">2.3%</td>
<td align="right">75,883,802</td>
<td align="right">2.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">97,721,473</td>
<td align="right">2.9%</td>
<td align="right">97,730,809</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">98,663,364</td>
<td align="right">2.9%</td>
<td align="right">98,667,875</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,223,447,878</td>
<td align="right">36.3%</td>
<td align="right">1,223,501,418</td>
<td align="right">36.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">416,380,838</td>
<td align="right">12.4%</td>
<td align="right">416,386,370</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">273,161,925</td>
<td align="right">8.1%</td>
<td align="right">273,165,122</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,194</td>
<td align="right">5.1%</td>
<td align="right">173,284,190</td>
<td align="right">5.1%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">38,868,916</td>
<td align="right">5.2%</td>
<td align="right">38,793,955</td>
<td align="right">5.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,193,160</td>
<td align="right">3.4%</td>
<td align="right">25,197,782</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,947,002</td>
<td align="right">5.5%</td>
<td align="right">40,953,575</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">90,689,582</td>
<td align="right">12.1%</td>
<td align="right">90,688,685</td>
<td align="right">12.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,511,536</td>
<td align="right">3.7%</td>
<td align="right">27,511,504</td>
<td align="right">3.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,874,308</td>
<td align="right">10.4%</td>
<td align="right">77,874,377</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,874,308</td>
<td align="right">10.4%</td>
<td align="right">77,874,377</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">100,618,894</td>
<td align="right">13.4%</td>
<td align="right">100,618,939</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">73,033,136</td>
<td align="right">9.7%</td>
<td align="right">73,033,136</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,305,540</td>
<td align="right">5.8%</td>
<td align="right">43,305,540</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
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
<td align="right">5,692,830,455</td>
<td align="right">70.4%</td>
<td align="right">5,684,563,179</td>
<td align="right">70.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,377,538,699</td>
<td align="right">78.9%</td>
<td align="right">6,369,390,332</td>
<td align="right">78.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">225,112,173</td>
<td align="right">2.8%</td>
<td align="right">225,149,330</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,230,233</td>
<td align="right">10.6%</td>
<td align="right">860,156,148</td>
<td align="right">10.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,524,049,675</td>
<td align="right">18.9%</td>
<td align="right">1,524,168,530</td>
<td align="right">18.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,528,484,135</td>
<td align="right">18.9%</td>
<td align="right">1,528,602,990</td>
<td align="right">18.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,667,247</td>
<td align="right">0.9%</td>
<td align="right">71,665,390</td>
<td align="right">0.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,388,714,368</td>
<td align="right">29.6%</td>
<td align="right">2,388,759,138</td>
<td align="right">29.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,388,714,368</td>
<td align="right">29.6%</td>
<td align="right">2,388,759,138</td>
<td align="right">29.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">28,603,082</td>
<td align="right">0.4%</td>
<td align="right">28,602,787</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">527,046,962</td>
<td align="right">6.5%</td>
<td align="right">527,045,505</td>
<td align="right">6.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,380,915</td>
<td align="right">2.6%</td>
<td align="right">211,380,912</td>
<td align="right">2.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,411,640</td>
<td align="right">0.1%</td>
<td align="right">4,411,640</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">22,820</td>
<td align="right">0.0%</td>
<td align="right">22,820</td>
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
<td align="right">4,296,922</td>
<td align="right"></td>
<td align="right">3,433,242</td>
<td align="right"></td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,459,388,788</td>
<td align="right">38.4%</td>
<td align="right">6,951,757,224</td>
<td align="right">40.5%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,461,153,912</td>
<td align="right"></td>
<td align="right">6,953,521,585</td>
<td align="right"></td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">23,110,776</td>
<td align="right"></td>
<td align="right">22,042,463</td>
<td align="right"></td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,220,175,084</td>
<td align="right">60.8%</td>
<td align="right">10,087,874,588</td>
<td align="right">58.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,673,990,582</td>
<td align="right"></td>
<td align="right">10,535,952,236</td>
<td align="right"></td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,343,741,876</td>
<td align="right">61.6%</td>
<td align="right">10,211,292,377</td>
<td align="right">59.5%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">18,991,438</td>
<td align="right"></td>
<td align="right">18,784,739</td>
<td align="right"></td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">66,906,949,984</td>
<td align="right">59.1%</td>
<td align="right">66,590,387,568</td>
<td align="right">59.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,752,704</td>
<td align="right">0.6%</td>
<td align="right">103,604,091</td>
<td align="right">0.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">46,316,819,755</td>
<td align="right">40.9%</td>
<td align="right">46,257,606,122</td>
<td align="right">41.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">150,151,748</td>
<td align="right"></td>
<td align="right">150,177,472</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,113,342,433</td>
<td align="right"></td>
<td align="right">3,113,870,694</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">69,633,017,925</td>
<td align="right">53.8%</td>
<td align="right">69,644,520,041</td>
<td align="right">53.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,641,014,076</td>
<td align="right"></td>
<td align="right">2,641,334,809</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">59,904,007,913</td>
<td align="right">46.2%</td>
<td align="right">59,898,638,044</td>
<td align="right">46.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">19,814,088</td>
<td align="right">0.1%</td>
<td align="right">19,813,698</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,271,140</td>
<td align="right">2.2%</td>
<td align="right">3,271,140</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">63,860</td>
<td align="right">0.0%</td>
<td align="right">63,860</td>
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
<td align="right">18,596,020</td>
<td align="right">14,535,420,498</td>
<td align="right">0</td>
<td align="right">18,595,960</td>
<td align="right">14,468,724,583</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,940</td>
<td align="right">6,996,793,416</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,996,791,480</td>
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
<td align="right">197,897,363,530</td>
<td align="right">2,812.6%</td>
<td align="right">204,091,128,518</td>
<td align="right">2,903.4%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">822</td>
<td align="right">0.1%</td>
<td align="right">832</td>
<td align="right">0.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,183</td>
<td align="right">6.1%</td>
<td align="right">6,192</td>
<td align="right">6.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">636,152</td>
<td align="right">86.2%</td>
<td align="right">635,269</td>
<td align="right">86.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">738,026</td>
<td align="right"></td>
<td align="right">737,075</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,036,119,764</td>
<td align="right"></td>
<td align="right">7,029,485,377</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">45,671</td>
<td align="right">6.2%</td>
<td align="right">45,633</td>
<td align="right">6.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,488</td>
<td align="right">0.9%</td>
<td align="right">6,493</td>
<td align="right">0.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">101,874</td>
<td align="right">13.8%</td>
<td align="right">101,806</td>
<td align="right">13.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">438,374</td>
<td align="right">59.4%</td>
<td align="right">438,380</td>
<td align="right">59.5%</td>
<td align="right">0.0%</td>
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
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">1,300</td>
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
<td align="right">2,361</td>
<td align="right">2.3%</td>
<td align="right">2,365</td>
<td align="right">2.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">98,293</td>
<td align="right">96.5%</td>
<td align="right">98,221</td>
<td align="right">96.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">101,874</td>
<td align="right"></td>
<td align="right">101,806</td>
<td align="right"></td>
<td align="right">-0.1%</td>
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
<td align="right">4,717</td>
<td align="right">4.6%</td>
<td align="right">4,696</td>
<td align="right">4.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">19,562</td>
<td align="right">19.2%</td>
<td align="right">19,581</td>
<td align="right">19.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">32,162</td>
<td align="right">31.6%</td>
<td align="right">32,131</td>
<td align="right">31.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">24,751</td>
<td align="right">24.3%</td>
<td align="right">24,729</td>
<td align="right">24.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,146</td>
<td align="right">12.9%</td>
<td align="right">13,164</td>
<td align="right">12.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,956</td>
<td align="right">5.8%</td>
<td align="right">5,905</td>
<td align="right">5.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,420</td>
<td align="right">1.4%</td>
<td align="right">1,440</td>
<td align="right">1.4%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">160</td>
<td align="right">0.2%</td>
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
<td align="right">3,797</td>
<td align="right">3.7%</td>
<td align="right">3,796</td>
<td align="right">3.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">13,640</td>
<td align="right">13.4%</td>
<td align="right">13,619</td>
<td align="right">13.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,567</td>
<td align="right">21.2%</td>
<td align="right">21,532</td>
<td align="right">21.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">32,342</td>
<td align="right">31.7%</td>
<td align="right">32,333</td>
<td align="right">31.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">16,110</td>
<td align="right">15.8%</td>
<td align="right">16,059</td>
<td align="right">15.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,817</td>
<td align="right">7.7%</td>
<td align="right">7,802</td>
<td align="right">7.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,600</td>
<td align="right">2.6%</td>
<td align="right">2,660</td>
<td align="right">2.6%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">420</td>
<td align="right">0.4%</td>
<td align="right">420</td>
<td align="right">0.4%</td>
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
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">129,211,476</td>
<td align="right">112,718,279</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,345,726,971</td>
<td align="right">1,503,613,354</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,803,634,821</td>
<td align="right">13,125,553,169</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">13,883,872,560</td>
<td align="right">15,211,701,650</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">112,330,051</td>
<td align="right">104,076,771</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,315,700</td>
<td align="right">51,564,424</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">128,552,413</td>
<td align="right">123,025,355</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">129,747,553</td>
<td align="right">124,220,495</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">109,991,835</td>
<td align="right">107,216,217</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">333,596,661</td>
<td align="right">328,060,915</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">185,556,935</td>
<td align="right">182,685,467</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">188,084,625</td>
<td align="right">185,212,973</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">280,598,260</td>
<td align="right">277,845,795</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">325,072,183</td>
<td align="right">322,320,616</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">843,495,935</td>
<td align="right">837,961,805</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,048,690,673</td>
<td align="right">1,043,179,108</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,145,508,378</td>
<td align="right">1,140,006,037</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,245,528,878</td>
<td align="right">1,240,026,537</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,264,404,558</td>
<td align="right">1,258,902,197</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,417,280,315</td>
<td align="right">1,411,476,403</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,552,760,428</td>
<td align="right">1,547,173,550</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,667,102,163</td>
<td align="right">1,661,205,683</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,864,346,983</td>
<td align="right">1,858,595,680</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,979,339,385</td>
<td align="right">1,973,588,048</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">30,111,321</td>
<td align="right">30,025,308</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,956,402,694</td>
<td align="right">2,948,006,205</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,093,563,007</td>
<td align="right">2,088,028,078</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,106,289,241</td>
<td align="right">1,103,574,038</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,820,024,029</td>
<td align="right">2,813,926,789</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,317,609,067</td>
<td align="right">1,314,916,898</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,388,528,676</td>
<td align="right">1,385,733,079</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,378,026,561</td>
<td align="right">1,375,346,788</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,203,301,811</td>
<td align="right">3,197,592,411</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,485,402,552</td>
<td align="right">6,473,976,686</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,652,985,466</td>
<td align="right">6,641,954,742</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,874,036,898</td>
<td align="right">1,870,975,111</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">2,080,751,986</td>
<td align="right">2,077,541,468</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">232,376,693</td>
<td align="right">232,069,096</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,182,479,766</td>
<td align="right">2,179,709,509</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,122,067,638</td>
<td align="right">7,113,223,382</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,234,391,878</td>
<td align="right">2,231,633,044</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">360,496,168</td>
<td align="right">360,053,014</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">400,540,728</td>
<td align="right">400,097,574</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">184,236,963</td>
<td align="right">184,418,924</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">167,284,871</td>
<td align="right">167,442,710</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,312,775,551</td>
<td align="right">3,309,681,329</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">133,898,865</td>
<td align="right">133,774,161</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">7,108,739</td>
<td align="right">7,115,302</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,730,608,535</td>
<td align="right">5,725,337,625</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">112,102,763</td>
<td align="right">112,001,885</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,508,559,266</td>
<td align="right">6,502,788,370</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,603,943,713</td>
<td align="right">3,601,043,833</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,453,944,296</td>
<td align="right">3,451,175,175</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">140,188,212</td>
<td align="right">140,076,549</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,568,703,200</td>
<td align="right">4,565,150,096</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,739,979,245</td>
<td align="right">4,736,666,804</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,955,367,778</td>
<td align="right">4,951,943,909</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">199,529,995</td>
<td align="right">199,392,754</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">485,830,793</td>
<td align="right">485,510,583</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,228,200</td>
<td align="right">10,234,644</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">16,604,336</td>
<td align="right">16,595,153</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">541,299,447</td>
<td align="right">541,037,865</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,399,502</td>
<td align="right">78,362,716</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">342,163,904</td>
<td align="right">342,021,906</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,002,451</td>
<td align="right">88,965,532</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">93,423,003</td>
<td align="right">93,386,175</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,527,681</td>
<td align="right">93,490,852</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">947,690,097</td>
<td align="right">947,320,173</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">243,974,946</td>
<td align="right">243,900,381</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,604,980,143</td>
<td align="right">9,602,078,737</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">618,181,142</td>
<td align="right">617,995,565</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">315,098,863</td>
<td align="right">315,012,761</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">197,989,781</td>
<td align="right">197,937,885</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">686,957,245</td>
<td align="right">687,132,976</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">592,433,285</td>
<td align="right">592,289,004</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,275,111,724</td>
<td align="right">1,274,848,571</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">4,437,834</td>
<td align="right">4,437,004</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,974,925,909</td>
<td align="right">1,974,568,735</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,339,511,372</td>
<td align="right">1,339,274,250</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">874,440,317</td>
<td align="right">874,289,830</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">73,944,147</td>
<td align="right">73,955,785</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">576,722,782</td>
<td align="right">576,640,203</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">565,846,259</td>
<td align="right">565,774,425</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,794,924,648</td>
<td align="right">1,794,700,551</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">759,845,777</td>
<td align="right">759,762,883</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,181,816,085</td>
<td align="right">2,182,034,682</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">410,964,616</td>
<td align="right">410,928,169</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,013,685,424</td>
<td align="right">1,013,609,579</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">173,125,859</td>
<td align="right">173,138,116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,536,715,876</td>
<td align="right">2,536,539,561</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,320,566,961</td>
<td align="right">1,320,481,381</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">713,385,764</td>
<td align="right">713,346,019</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">790,385,633</td>
<td align="right">790,348,160</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">724,106,425</td>
<td align="right">724,073,277</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">686,654,903</td>
<td align="right">686,624,519</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,587,624</td>
<td align="right">45,585,632</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">966,554,899</td>
<td align="right">966,517,577</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,755,196</td>
<td align="right">229,763,342</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">218,010,685</td>
<td align="right">218,016,968</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,335,323</td>
<td align="right">203,329,666</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">330,488,576</td>
<td align="right">330,480,583</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,114,268,287</td>
<td align="right">1,114,244,291</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,625,414</td>
<td align="right">779,641,209</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">780,162,734</td>
<td align="right">780,178,529</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">551,216,390</td>
<td align="right">551,223,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,548,415</td>
<td align="right">733,557,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">97,575,883</td>
<td align="right">97,574,789</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">97,819,743</td>
<td align="right">97,818,649</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,318,832</td>
<td align="right">32,318,496</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">444,993</td>
<td align="right">444,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">224,505,100</td>
<td align="right">224,503,758</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,238,122,210</td>
<td align="right">1,238,128,968</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">936,674,482</td>
<td align="right">936,678,387</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">227,850,592</td>
<td align="right">227,849,688</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">382,245,456</td>
<td align="right">382,246,782</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,941</td>
<td align="right">384,636,668</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">647,417</td>
<td align="right">647,415</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">59,861,210</td>
<td align="right">59,861,050</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">588,455,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,212</td>
<td align="right">645,065,880</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">224,357,938</td>
<td align="right">224,357,497</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,353,914</td>
<td align="right">126,354,149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">423,851,227</td>
<td align="right">423,850,605</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,705,881</td>
<td align="right">909,704,608</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">263,242,180</td>
<td align="right">263,242,463</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">264,469,000</td>
<td align="right">264,469,283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,198,009</td>
<td align="right">97,197,906</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,155,349</td>
<td align="right">98,155,246</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,041,554,650</td>
<td align="right">1,041,553,681</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">22,299,320</td>
<td align="right">22,299,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">147,767,756</td>
<td align="right">147,767,633</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,257,165,553</td>
<td align="right">2,257,167,379</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,234,006,053</td>
<td align="right">2,234,007,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">55,151,968</td>
<td align="right">55,151,924</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,044,343,465</td>
<td align="right">1,044,342,695</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">61,795,600</td>
<td align="right">61,795,560</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">61,916,460</td>
<td align="right">61,916,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">959,058,279</td>
<td align="right">959,057,726</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,197,992</td>
<td align="right">101,197,940</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,912,851</td>
<td align="right">9,912,846</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">485,536,897</td>
<td align="right">485,536,697</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">108,946,888</td>
<td align="right">108,946,844</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,831,862</td>
<td align="right">101,831,830</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,818,627,312</td>
<td align="right">1,818,626,758</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">115,025,662</td>
<td align="right">115,025,628</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,645,399,482</td>
<td align="right">2,645,398,765</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,041,100</td>
<td align="right">22,041,104</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,387,038</td>
<td align="right">11,387,036</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,387,038</td>
<td align="right">11,387,036</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,367,090,077</td>
<td align="right">1,367,089,837</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,290,510</td>
<td align="right">134,290,526</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,290,510</td>
<td align="right">134,290,526</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,070,087</td>
<td align="right">35,070,085</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">409,920,740</td>
<td align="right">409,920,723</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">24,824,313</td>
<td align="right">24,824,314</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">154,174,707</td>
<td align="right">154,174,701</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,913,167</td>
<td align="right">68,913,165</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,171,706</td>
<td align="right">1,335,171,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">118,606,461</td>
<td align="right">118,606,462</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,652,558,427</td>
<td align="right">1,652,558,433</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,144,563,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,071,320</td>
<td align="right">533,071,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,717,900</td>
<td align="right">509,717,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">230,436,840</td>
<td align="right">230,436,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">213,616,660</td>
<td align="right">213,616,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,039,140</td>
<td align="right">199,039,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,548,620</td>
<td align="right">187,548,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,868,340</td>
<td align="right">149,868,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">145,314,520</td>
<td align="right">145,314,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,940,300</td>
<td align="right">144,940,300</td>
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
<td align="right">99,651,520</td>
<td align="right">99,651,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">93,666,280</td>
<td align="right">93,666,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,579,640</td>
<td align="right">80,579,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">66,194,480</td>
<td align="right">66,194,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">64,886,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">63,424,300</td>
<td align="right">63,424,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,830,020</td>
<td align="right">61,830,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">53,794,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">46,348,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">35,233,740</td>
<td align="right">35,233,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">20,499,060</td>
<td align="right">20,499,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">14,734,660</td>
<td align="right">14,734,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,693,200</td>
<td align="right">12,693,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,133,840</td>
<td align="right">8,133,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">6,583,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,659,980</td>
<td align="right">5,659,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,867,341</td>
<td align="right">4,867,341</td>
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
<td align="left">_STORE_DEREF</td>
<td align="right">3,610,440</td>
<td align="right">3,610,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,116,480</td>
<td align="right">2,116,480</td>
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
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">34,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">29,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">7,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BOX_FLOAT</td>
<td align="right"></td>
<td align="right">1,500,421,628</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNBOX_BOTH_FLOAT</td>
<td align="right"></td>
<td align="right">1,500,421,628</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNBOX_NOS_FLOAT</td>
<td align="right"></td>
<td align="right">617,234,200</td>
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
<td align="left">CALL_KW</td>
<td align="right">29,180</td>
<td align="right">28,360</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,223</td>
<td align="right">5,201</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">1,563</td>
<td align="right">1,567</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">540</td>
<td align="right">539</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,586</td>
<td align="right">6,578</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">82,613</td>
<td align="right">82,546</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40,599</td>
<td align="right">40,570</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,300</td>
<td align="right">2,301</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">32,220</td>
<td align="right">32,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,415</td>
<td align="right">2,415</td>
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
<td align="right">1,082</td>
<td align="right">1,086</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,082</td>
<td align="right">1,086</td>
<td align="right">0.4%</td>
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
<td align="right">1,880</td>
<td align="right">-1.1%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-05-23
