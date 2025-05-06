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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">208,910,918</td>
<td align="right">739,062,250</td>
<td align="right">253.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">76,778,030</td>
<td align="right">165,290,749</td>
<td align="right">115.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">151,892,388</td>
<td align="right">304,671,567</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">1</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">8</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right">35</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,762,005</td>
<td align="right">192,036</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">121,290</td>
<td align="right">13,028</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,643,362</td>
<td align="right">274,048</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">168,083,870</td>
<td align="right">298,035,709</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">752,619</td>
<td align="right">439,500</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">407,168</td>
<td align="right">246,368</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">383,849,972</td>
<td align="right">521,331,485</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">488,800,957</td>
<td align="right">627,715,726</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">481,311,817</td>
<td align="right">606,617,376</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,684,316</td>
<td align="right">5,772,986</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">72,746,166</td>
<td align="right">59,097,465</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">822,891,333</td>
<td align="right">957,378,703</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,572,342</td>
<td align="right">3,870,866</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,496</td>
<td align="right">72,496</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">31,562,726</td>
<td align="right">36,040,099</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">448,144,505</td>
<td align="right">510,568,706</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">868,854,385</td>
<td align="right">989,624,018</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">168,049,533</td>
<td align="right">190,021,258</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">432,045,339</td>
<td align="right">378,699,427</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,431,593</td>
<td align="right">1,262,401</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">81,354,052</td>
<td align="right">73,338,311</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">171,665,262</td>
<td align="right">156,207,920</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,053,933</td>
<td align="right">9,186,183</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,815,271,909</td>
<td align="right">4,118,661,124</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,190,361,537</td>
<td align="right">2,337,799,823</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">34,193</td>
<td align="right">31,952</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">87,945,477</td>
<td align="right">93,442,185</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">46,603,196</td>
<td align="right">44,223,033</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,712,553</td>
<td align="right">4,480,299</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">582,222,256</td>
<td align="right">555,823,959</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">48,503,411</td>
<td align="right">46,332,984</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,063,821,347</td>
<td align="right">5,267,358,088</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">140,317,784</td>
<td align="right">134,752,645</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">19,459,377</td>
<td align="right">18,745,936</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">96,193,440</td>
<td align="right">99,598,153</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">124,357,485</td>
<td align="right">120,178,905</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">94,214,665</td>
<td align="right">97,193,212</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">56,423,591</td>
<td align="right">54,656,777</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">66,531,177</td>
<td align="right">64,470,534</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">24,823,439</td>
<td align="right">24,090,984</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,326,008</td>
<td align="right">10,628,019</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,156,761,297</td>
<td align="right">2,095,520,727</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">203,146,243</td>
<td align="right">208,615,215</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">88,499,652</td>
<td align="right">86,175,270</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">58,988,209</td>
<td align="right">57,448,986</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">174,698,960</td>
<td align="right">170,233,601</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,525,712</td>
<td align="right">121,549,949</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">12,905,340</td>
<td align="right">12,618,468</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">124,902,445</td>
<td align="right">122,177,488</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,590,381,727</td>
<td align="right">1,556,793,020</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">164,369,261</td>
<td align="right">160,918,517</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">949,313,442</td>
<td align="right">930,945,652</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">295,484,646</td>
<td align="right">289,837,610</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">701,340,915</td>
<td align="right">688,341,980</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">584,039,807</td>
<td align="right">573,382,473</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">114,308,517</td>
<td align="right">112,303,225</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,754,948</td>
<td align="right">1,724,728</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">612,948,281</td>
<td align="right">602,425,007</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,406,759,288</td>
<td align="right">3,348,500,134</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,501</td>
<td align="right">5,408</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">366,396,081</td>
<td align="right">360,411,197</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">108,278,211</td>
<td align="right">106,551,826</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">195,309,448</td>
<td align="right">192,211,111</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,726,949</td>
<td align="right">69,635,112</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">456,186,199</td>
<td align="right">449,309,344</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,097,069,135</td>
<td align="right">1,080,605,983</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">252,375,156</td>
<td align="right">248,623,195</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">232,753,872</td>
<td align="right">229,326,266</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">17,451,435,193</td>
<td align="right">17,706,512,931</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">243,169,639</td>
<td align="right">239,663,768</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,176,835,716</td>
<td align="right">1,193,428,229</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">344,200,715</td>
<td align="right">339,416,440</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">921,697,491</td>
<td align="right">908,905,545</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">194,646,748</td>
<td align="right">191,998,449</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">112,173,591</td>
<td align="right">110,657,422</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">69,616,048</td>
<td align="right">68,704,703</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,488,977,429</td>
<td align="right">2,457,260,336</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">927,525,008</td>
<td align="right">917,135,956</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">811,056,783</td>
<td align="right">802,124,484</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">264,778,953</td>
<td align="right">261,996,285</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">160,773,705</td>
<td align="right">159,105,420</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">273,225,751</td>
<td align="right">270,439,936</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">55,356,187</td>
<td align="right">54,801,067</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,574,352,150</td>
<td align="right">3,539,027,098</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,769,885,554</td>
<td align="right">4,722,775,243</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,109,517,676</td>
<td align="right">5,059,096,687</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,738,251</td>
<td align="right">7,665,149</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">191,982,208</td>
<td align="right">190,301,290</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,025,600</td>
<td align="right">19,852,392</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">861,215,428</td>
<td align="right">868,610,106</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,356,850</td>
<td align="right">20,183,643</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,356,870</td>
<td align="right">20,183,663</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">108,830,252</td>
<td align="right">107,936,278</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,668,395</td>
<td align="right">9,590,065</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">464,692,103</td>
<td align="right">460,964,590</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">62,210,000</td>
<td align="right">61,736,870</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">117,444</td>
<td align="right">116,559</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">848,328,616</td>
<td align="right">842,062,596</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,104,766,053</td>
<td align="right">4,077,267,559</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">815,758,226</td>
<td align="right">810,329,349</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,033,269</td>
<td align="right">30,834,189</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">238,102,768</td>
<td align="right">236,651,053</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">240,160,054</td>
<td align="right">238,701,979</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">93,357,801</td>
<td align="right">92,794,977</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,495,811</td>
<td align="right">57,156,621</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,567,490</td>
<td align="right">3,588,521</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">711,624,916</td>
<td align="right">707,617,992</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">120,109,402</td>
<td align="right">119,449,617</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,533,840,731</td>
<td align="right">1,525,664,526</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,281,700</td>
<td align="right">2,269,704</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">125,317,633</td>
<td align="right">124,683,525</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">360,118,186</td>
<td align="right">361,920,370</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">149,128,948</td>
<td align="right">148,398,229</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">366,403,806</td>
<td align="right">368,145,302</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">198,137,134</td>
<td align="right">197,207,067</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,839,400</td>
<td align="right">25,720,335</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">505,113,781</td>
<td align="right">502,817,673</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">122,776,948</td>
<td align="right">122,221,069</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">165,818,200</td>
<td align="right">165,069,804</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,610,511,364</td>
<td align="right">2,598,874,640</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,030,848,233</td>
<td align="right">2,022,089,880</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">344,080,230</td>
<td align="right">342,664,412</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">942,038,303</td>
<td align="right">938,180,406</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">153,984,191</td>
<td align="right">153,443,979</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">860,550,867</td>
<td align="right">857,950,597</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">25,631,159</td>
<td align="right">25,559,168</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,645</td>
<td align="right">2,652</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,892,882</td>
<td align="right">114,606,608</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">577,904,427</td>
<td align="right">579,267,408</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">355,780,672</td>
<td align="right">354,977,328</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,307,725,278</td>
<td align="right">2,312,272,978</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">415,921,161</td>
<td align="right">415,156,547</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">337,370,328</td>
<td align="right">336,811,990</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">413,065,193</td>
<td align="right">412,402,984</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">219,500,870</td>
<td align="right">219,151,254</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">94,137,036</td>
<td align="right">93,987,855</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">946,866,686</td>
<td align="right">948,288,520</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">265,171,492</td>
<td align="right">264,780,613</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">253,379,508</td>
<td align="right">253,022,515</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">282,181,854</td>
<td align="right">281,802,332</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,905,627</td>
<td align="right">155,730,396</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,113,715,180</td>
<td align="right">1,113,285,815</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,390,919</td>
<td align="right">418,233,839</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,401,562</td>
<td align="right">131,353,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">237,683,260</td>
<td align="right">237,601,664</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">658,710,930</td>
<td align="right">658,498,250</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">38,271,909</td>
<td align="right">38,263,415</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">13,255,129</td>
<td align="right">13,252,620</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,299</td>
<td align="right">5,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">63,721,044</td>
<td align="right">63,710,565</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,533,815</td>
<td align="right">3,533,265</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">135,670</td>
<td align="right">135,689</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">96,620,253</td>
<td align="right">96,610,818</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,956,922</td>
<td align="right">27,955,158</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,976,363</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,072,959</td>
<td align="right">35,071,129</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,484,330</td>
<td align="right">3,484,157</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,384,294</td>
<td align="right">1,384,356</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">6,152,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,351,523</td>
<td align="right">41,350,402</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,476</td>
<td align="right">5,803,324</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">81,328,651</td>
<td align="right">81,327,294</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,781,601</td>
<td align="right">184,778,757</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">55,208,384</td>
<td align="right">55,207,853</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">138,193,143</td>
<td align="right">138,194,232</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">75,304,598</td>
<td align="right">75,304,185</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,353</td>
<td align="right">35,549,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">275,717,112</td>
<td align="right">275,716,967</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,621,186</td>
<td align="right">591,621,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,491</td>
<td align="right">302,246,491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,295</td>
<td align="right">128,850,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,608</td>
<td align="right">41,964,608</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,743,126</td>
<td align="right">9,743,126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
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
<td align="left">STORE_SLICE</td>
<td align="right">1,232,478</td>
<td align="right">1,232,478</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,514</td>
<td align="right">98,514</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,501</td>
<td align="right">69,501</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,252</td>
<td align="right">57,252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,984</td>
<td align="right">53,984</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">13,935</td>
<td align="right">13,935</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,889</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,613</td>
<td align="right">3,613</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">153</td>
<td align="right">153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">36</td>
<td align="right">36</td>
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
<td align="right">55,683,867</td>
<td align="right">0.3%</td>
<td align="right">28,970,541</td>
<td align="right">0.2%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,288,493,493</td>
<td align="right">93.0%</td>
<td align="right">16,700,091,275</td>
<td align="right">93.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,176,325,618</td>
<td align="right">6.7%</td>
<td align="right">1,192,080,748</td>
<td align="right">6.7%</td>
<td align="right">1.3%</td>
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
<td align="right">492,216</td>
<td align="right">31.5%</td>
<td align="right">665,587</td>
<td align="right">35.4%</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,068,291</td>
<td align="right">68.5%</td>
<td align="right">1,215,677</td>
<td align="right">64.6%</td>
<td align="right">13.8%</td>
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
<td align="left">and int</td>
<td align="right">18,484</td>
<td align="right">3.8%</td>
<td align="right">126,611</td>
<td align="right">19.0%</td>
<td align="right">585.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">17,023</td>
<td align="right">3.5%</td>
<td align="right">94,643</td>
<td align="right">14.2%</td>
<td align="right">456.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">2,616</td>
<td align="right">0.4%</td>
<td align="right">212.9%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">156</td>
<td align="right">0.0%</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">201</td>
<td align="right">0.0%</td>
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,302</td>
<td align="right">1.7%</td>
<td align="right">12,578</td>
<td align="right">1.9%</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">85</td>
<td align="right">0.0%</td>
<td align="right">45</td>
<td align="right">0.0%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">492</td>
<td align="right">0.1%</td>
<td align="right">310</td>
<td align="right">0.0%</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">104</td>
<td align="right">0.0%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,752</td>
<td align="right">1.2%</td>
<td align="right">6,894</td>
<td align="right">1.0%</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">209</td>
<td align="right">0.0%</td>
<td align="right">169</td>
<td align="right">0.0%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,780</td>
<td align="right">4.8%</td>
<td align="right">27,807</td>
<td align="right">4.2%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">36,593</td>
<td align="right">7.4%</td>
<td align="right">42,233</td>
<td align="right">6.3%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">11,573</td>
<td align="right">2.4%</td>
<td align="right">9,992</td>
<td align="right">1.5%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,831</td>
<td align="right">1.6%</td>
<td align="right">7,034</td>
<td align="right">1.1%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">24,911</td>
<td align="right">5.1%</td>
<td align="right">25,470</td>
<td align="right">3.8%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">1,808</td>
<td align="right">0.4%</td>
<td align="right">1,848</td>
<td align="right">0.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,154</td>
<td align="right">0.6%</td>
<td align="right">3,114</td>
<td align="right">0.5%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,342</td>
<td align="right">0.5%</td>
<td align="right">2,322</td>
<td align="right">0.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">75,135</td>
<td align="right">15.3%</td>
<td align="right">74,701</td>
<td align="right">11.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,350</td>
<td align="right">0.5%</td>
<td align="right">2,343</td>
<td align="right">0.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">29,949</td>
<td align="right">6.1%</td>
<td align="right">29,873</td>
<td align="right">4.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">41,400</td>
<td align="right">8.4%</td>
<td align="right">41,302</td>
<td align="right">6.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">108,030</td>
<td align="right">21.9%</td>
<td align="right">107,945</td>
<td align="right">16.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,995</td>
<td align="right">0.4%</td>
<td align="right">1,996</td>
<td align="right">0.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,768</td>
<td align="right">0.6%</td>
<td align="right">2,767</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">28,692</td>
<td align="right">5.8%</td>
<td align="right">28,692</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">25,838</td>
<td align="right">5.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,194</td>
<td align="right">1.3%</td>
<td align="right">6,194</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,163</td>
<td align="right">0.6%</td>
<td align="right">3,163</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">624</td>
<td align="right">0.1%</td>
<td align="right">624</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">325</td>
<td align="right">0.1%</td>
<td align="right">325</td>
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
<td align="left">subscr stacksummary</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">184,781,601</td>
<td align="right">100.0%</td>
<td align="right">184,778,757</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">160,633,234</td>
<td align="right">1.4%</td>
<td align="right">159,063,945</td>
<td align="right">1.4%</td>
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
<td align="right">163,485,670</td>
<td align="right">1.5%</td>
<td align="right">162,045,973</td>
<td align="right">1.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,985,410,692</td>
<td align="right">98.5%</td>
<td align="right">10,926,610,100</td>
<td align="right">98.5%</td>
<td align="right">-0.5%</td>
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
<td align="left">Failure</td>
<td align="right">446</td>
<td align="right">0.0%</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,259,158</td>
<td align="right">100.0%</td>
<td align="right">3,228,250</td>
<td align="right">100.0%</td>
<td align="right">-0.9%</td>
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
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">146</td>
<td align="right">100.0%</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right">268</td>
<td align="right">183.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">753</td>
<td align="right">168.8%</td>
<td align="right">753</td>
<td align="right">515.8%</td>
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
<td align="right">685,347</td>
<td align="right">97.1%</td>
<td align="right">569,680</td>
<td align="right">96.6%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">584,644</td>
<td align="right">82.8%</td>
<td align="right">576,804</td>
<td align="right">97.8%</td>
<td align="right">-1.3%</td>
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
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20,467</td>
<td align="right">99.4%</td>
<td align="right">20,152</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">94,096,171</td>
<td align="right">2.0%</td>
<td align="right">97,074,409</td>
<td align="right">2.1%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,506,307,436</td>
<td align="right">97.9%</td>
<td align="right">4,476,178,335</td>
<td align="right">97.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,166,654</td>
<td align="right">0.0%</td>
<td align="right">1,171,131</td>
<td align="right">0.0%</td>
<td align="right">0.4%</td>
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
<td align="right">100,349</td>
<td align="right">71.5%</td>
<td align="right">100,694</td>
<td align="right">71.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39,960</td>
<td align="right">28.5%</td>
<td align="right">40,011</td>
<td align="right">28.4%</td>
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
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.4%</td>
<td align="right">196</td>
<td align="right">0.2%</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">9,355</td>
<td align="right">9.3%</td>
<td align="right">10,270</td>
<td align="right">10.2%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,996</td>
<td align="right">2.0%</td>
<td align="right">1,896</td>
<td align="right">1.9%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,207</td>
<td align="right">4.2%</td>
<td align="right">4,122</td>
<td align="right">4.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">37,248</td>
<td align="right">37.1%</td>
<td align="right">36,999</td>
<td align="right">36.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,767</td>
<td align="right">7.7%</td>
<td align="right">7,716</td>
<td align="right">7.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,162</td>
<td align="right">23.1%</td>
<td align="right">23,235</td>
<td align="right">23.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">371</td>
<td align="right">0.4%</td>
<td align="right">372</td>
<td align="right">0.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">5,893</td>
<td align="right">5.9%</td>
<td align="right">5,894</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">7.6%</td>
<td align="right">7,648</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,367</td>
<td align="right">1.4%</td>
<td align="right">1,367</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">979</td>
<td align="right">1.0%</td>
<td align="right">979</td>
<td align="right">1.0%</td>
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
<td align="right">88,454,475</td>
<td align="right">3.9%</td>
<td align="right">86,131,596</td>
<td align="right">3.8%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,395,959</td>
<td align="right">0.1%</td>
<td align="right">1,389,959</td>
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
<td align="right">2,189,809,223</td>
<td align="right">96.1%</td>
<td align="right">2,186,839,361</td>
<td align="right">96.1%</td>
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
<td align="left">Failure</td>
<td align="right">43,060</td>
<td align="right">60.2%</td>
<td align="right">41,631</td>
<td align="right">59.6%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,460</td>
<td align="right">39.8%</td>
<td align="right">28,266</td>
<td align="right">40.4%</td>
<td align="right">-0.7%</td>
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
<td align="right">9,969</td>
<td align="right">23.2%</td>
<td align="right">9,252</td>
<td align="right">22.2%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,199</td>
<td align="right">26.0%</td>
<td align="right">10,583</td>
<td align="right">25.4%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">12,053</td>
<td align="right">28.0%</td>
<td align="right">11,957</td>
<td align="right">28.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,839</td>
<td align="right">22.8%</td>
<td align="right">9,839</td>
<td align="right">23.6%</td>
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
<td align="right">1,312,620,797</td>
<td align="right">81.1%</td>
<td align="right">1,292,084,547</td>
<td align="right">81.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">243,037,727</td>
<td align="right">15.0%</td>
<td align="right">239,535,697</td>
<td align="right">15.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">62,023,900</td>
<td align="right">3.8%</td>
<td align="right">61,997,334</td>
<td align="right">3.9%</td>
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
<td align="right">126,302</td>
<td align="right">9.7%</td>
<td align="right">122,673</td>
<td align="right">9.5%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,175,699</td>
<td align="right">90.3%</td>
<td align="right">1,174,986</td>
<td align="right">90.5%</td>
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
<td align="left">set</td>
<td align="right">14,213</td>
<td align="right">11.3%</td>
<td align="right">12,853</td>
<td align="right">10.5%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,470</td>
<td align="right">3.5%</td>
<td align="right">4,207</td>
<td align="right">3.4%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,792</td>
<td align="right">3.0%</td>
<td align="right">3,572</td>
<td align="right">2.9%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,319</td>
<td align="right">3.4%</td>
<td align="right">4,179</td>
<td align="right">3.4%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,737</td>
<td align="right">1.4%</td>
<td align="right">1,697</td>
<td align="right">1.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">52,669</td>
<td align="right">41.7%</td>
<td align="right">51,495</td>
<td align="right">42.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,510</td>
<td align="right">5.2%</td>
<td align="right">6,391</td>
<td align="right">5.2%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">11,086</td>
<td align="right">8.8%</td>
<td align="right">10,928</td>
<td align="right">8.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">16,634</td>
<td align="right">13.2%</td>
<td align="right">16,479</td>
<td align="right">13.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">9,021</td>
<td align="right">7.1%</td>
<td align="right">9,021</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,132</td>
<td align="right">0.9%</td>
<td align="right">1,132</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">258</td>
<td align="right">0.2%</td>
<td align="right">258</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">134</td>
<td align="right">0.1%</td>
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
<td align="right">12,922,324</td>
<td align="right">12,922,324 / 0 !!</td>
<td align="right">12,139,525</td>
<td align="right">12,139,525 / 0 !!</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">6,040,815</td>
<td align="right">6,040,815 / 0 !!</td>
<td align="right">5,728,612</td>
<td align="right">5,728,612 / 0 !!</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">307,772,603</td>
<td align="right">307,772,603 / 0 !!</td>
<td align="right">302,921,803</td>
<td align="right">302,921,803 / 0 !!</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">393,552,842</td>
<td align="right">393,552,842 / 0 !!</td>
<td align="right">390,875,023</td>
<td align="right">390,875,023 / 0 !!</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">117,432,987</td>
<td align="right">117,432,987 / 0 !!</td>
<td align="right">116,782,172</td>
<td align="right">116,782,172 / 0 !!</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">102,341,348</td>
<td align="right">102,341,348 / 0 !!</td>
<td align="right">102,089,363</td>
<td align="right">102,089,363 / 0 !!</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">170,025,053</td>
<td align="right">170,025,053 / 0 !!</td>
<td align="right">169,846,273</td>
<td align="right">169,846,273 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,849,462</td>
<td align="right">34,849,462 / 0 !!</td>
<td align="right">34,813,464</td>
<td align="right">34,813,464 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,693,926</td>
<td align="right">2,693,926 / 0 !!</td>
<td align="right">2,693,926</td>
<td align="right">2,693,926 / 0 !!</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">580,458,045</td>
<td align="right">4.4%</td>
<td align="right">554,127,831</td>
<td align="right">4.2%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">704,833,760</td>
<td align="right">5.3%</td>
<td align="right">696,215,600</td>
<td align="right">5.3%</td>
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
<td align="right">12,026,157,089</td>
<td align="right">90.3%</td>
<td align="right">11,959,447,817</td>
<td align="right">90.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,262,484</td>
<td align="right">0.0%</td>
<td align="right">1,262,484</td>
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
<td align="right">497,275</td>
<td align="right">3.6%</td>
<td align="right">445,228</td>
<td align="right">3.3%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,384,755</td>
<td align="right">96.4%</td>
<td align="right">13,216,289</td>
<td align="right">96.7%</td>
<td align="right">-1.3%</td>
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
<td align="right">6,405</td>
<td align="right">1.3%</td>
<td align="right">487</td>
<td align="right">0.1%</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">163</td>
<td align="right">0.0%</td>
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">61,391</td>
<td align="right">12.3%</td>
<td align="right">47,950</td>
<td align="right">10.8%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">44,114</td>
<td align="right">8.9%</td>
<td align="right">38,063</td>
<td align="right">8.5%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,956</td>
<td align="right">1.6%</td>
<td align="right">8,773</td>
<td align="right">2.0%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">821</td>
<td align="right">0.2%</td>
<td align="right">741</td>
<td align="right">0.2%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
<td align="right">996</td>
<td align="right">0.2%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,311</td>
<td align="right">3.3%</td>
<td align="right">15,422</td>
<td align="right">3.5%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">44,859</td>
<td align="right">9.0%</td>
<td align="right">42,795</td>
<td align="right">9.6%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,208</td>
<td align="right">4.9%</td>
<td align="right">23,512</td>
<td align="right">5.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,449</td>
<td align="right">0.9%</td>
<td align="right">4,364</td>
<td align="right">1.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,897</td>
<td align="right">1.0%</td>
<td align="right">4,878</td>
<td align="right">1.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,809</td>
<td align="right">0.4%</td>
<td align="right">1,811</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,378</td>
<td align="right">0.5%</td>
<td align="right">2,378</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,778</td>
<td align="right">0.4%</td>
<td align="right">1,778</td>
<td align="right">0.4%</td>
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
<tr>
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,623,586</td>
<td align="right">0.3%</td>
<td align="right">55,996</td>
<td align="right">0.0%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,318</td>
<td align="right">0.0%</td>
<td align="right">1,142</td>
<td align="right">0.0%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,592,634,200</td>
<td align="right">99.7%</td>
<td align="right">4,554,785,945</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,574</td>
<td align="right">0.0%</td>
<td align="right">53,536</td>
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
<td align="right">139,187</td>
<td align="right">100.0%</td>
<td align="right">136,818</td>
<td align="right">100.0%</td>
<td align="right">-1.7%</td>
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
<td align="right">252</td>
<td align="right">0.0%</td>
<td align="right">255</td>
<td align="right">0.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">63,981,938</td>
<td align="right">100.0%</td>
<td align="right">63,413,968</td>
<td align="right">100.0%</td>
<td align="right">-0.9%</td>
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
<td align="right">2,393</td>
<td align="right">100.0%</td>
<td align="right">2,397</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
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
<td align="right">591,606,475</td>
<td align="right">82.1%</td>
<td align="right">591,606,542</td>
<td align="right">82.1%</td>
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
<td align="right">128,815,497</td>
<td align="right">17.9%</td>
<td align="right">128,815,497</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">72,653,707</td>
<td align="right">3.7%</td>
<td align="right">59,016,680</td>
<td align="right">3.0%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,791,678,040</td>
<td align="right">90.7%</td>
<td align="right">1,777,728,891</td>
<td align="right">91.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">111,812,977</td>
<td align="right">5.7%</td>
<td align="right">111,685,842</td>
<td align="right">5.7%</td>
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
<td align="left">Failure</td>
<td align="right">51,705</td>
<td align="right">2.3%</td>
<td align="right">42,634</td>
<td align="right">1.9%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,149,485</td>
<td align="right">97.7%</td>
<td align="right">2,144,574</td>
<td align="right">98.1%</td>
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
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">90</td>
<td align="right">0.2%</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">37</td>
<td align="right">0.1%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">423</td>
<td align="right">1.0%</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,331</td>
<td align="right">10.3%</td>
<td align="right">3,792</td>
<td align="right">8.9%</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.8%</td>
<td align="right">6,096</td>
<td align="right">14.3%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">47.3%</td>
<td align="right">19,837</td>
<td align="right">46.5%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">264,256</td>
<td align="right">511.1%</td>
<td align="right">241,502</td>
<td align="right">566.5%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,963</td>
<td align="right">9.6%</td>
<td align="right">4,763</td>
<td align="right">11.2%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">104</td>
<td align="right">0.2%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">817</td>
<td align="right">1.6%</td>
<td align="right">798</td>
<td align="right">1.9%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,345</td>
<td align="right">6.5%</td>
<td align="right">3,355</td>
<td align="right">7.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">1,665</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">360</td>
<td align="right">0.7%</td>
<td align="right">360</td>
<td align="right">0.8%</td>
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
<td align="right">1,232,478</td>
<td align="right">100.0%</td>
<td align="right">1,232,478</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">151,842,076</td>
<td align="right">14.1%</td>
<td align="right">304,584,107</td>
<td align="right">24.9%</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">921,788,806</td>
<td align="right">85.9%</td>
<td align="right">917,871,141</td>
<td align="right">75.1%</td>
<td align="right">-0.4%</td>
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
<td align="left">Failure</td>
<td align="right">48,231</td>
<td align="right">95.8%</td>
<td align="right">85,390</td>
<td align="right">97.6%</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,121</td>
<td align="right">4.2%</td>
<td align="right">2,110</td>
<td align="right">2.4%</td>
<td align="right">-0.5%</td>
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
<td align="right">10,484</td>
<td align="right">21.7%</td>
<td align="right">47,843</td>
<td align="right">56.0%</td>
<td align="right">356.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">15,163</td>
<td align="right">31.4%</td>
<td align="right">15,003</td>
<td align="right">17.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">35.9%</td>
<td align="right">17,283</td>
<td align="right">20.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,010</td>
<td align="right">6.2%</td>
<td align="right">3,010</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,662</td>
<td align="right">3.4%</td>
<td align="right">1,662</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.7%</td>
<td align="right">341</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">180</td>
<td align="right">0.4%</td>
<td align="right">180</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.1%</td>
<td align="right">68</td>
<td align="right">0.1%</td>
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
<td align="right">139,759,514</td>
<td align="right">3.0%</td>
<td align="right">134,232,365</td>
<td align="right">2.9%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">63,631,741</td>
<td align="right">1.4%</td>
<td align="right">62,995,114</td>
<td align="right">1.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,384,736,443</td>
<td align="right">95.6%</td>
<td align="right">4,366,267,155</td>
<td align="right">95.7%</td>
<td align="right">-0.4%</td>
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
<td align="right">507,277</td>
<td align="right">28.9%</td>
<td align="right">470,813</td>
<td align="right">27.6%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,249,880</td>
<td align="right">71.1%</td>
<td align="right">1,236,321</td>
<td align="right">72.4%</td>
<td align="right">-1.1%</td>
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
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">262</td>
<td align="right">0.1%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,007</td>
<td align="right">3.0%</td>
<td align="right">10,609</td>
<td align="right">2.3%</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">96,080</td>
<td align="right">18.9%</td>
<td align="right">74,463</td>
<td align="right">15.8%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">33,895</td>
<td align="right">6.7%</td>
<td align="right">27,686</td>
<td align="right">5.9%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,381</td>
<td align="right">2.6%</td>
<td align="right">11,913</td>
<td align="right">2.5%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,738</td>
<td align="right">1.9%</td>
<td align="right">9,476</td>
<td align="right">2.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">73,805</td>
<td align="right">14.5%</td>
<td align="right">72,367</td>
<td align="right">15.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,807</td>
<td align="right">51.0%</td>
<td align="right">257,852</td>
<td align="right">54.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,678</td>
<td align="right">0.9%</td>
<td align="right">4,681</td>
<td align="right">1.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,420,749</td>
<td align="right">0.1%</td>
<td align="right">1,251,718</td>
<td align="right">0.1%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,240,368,626</td>
<td align="right">99.9%</td>
<td align="right">1,232,534,809</td>
<td align="right">99.9%</td>
<td align="right">-0.6%</td>
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
<td align="right">867</td>
<td align="right">7.9%</td>
<td align="right">785</td>
<td align="right">7.3%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,057</td>
<td align="right">92.1%</td>
<td align="right">9,978</td>
<td align="right">92.7%</td>
<td align="right">-0.8%</td>
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
<td align="right">633</td>
<td align="right">73.0%</td>
<td align="right">551</td>
<td align="right">70.2%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.7%</td>
<td align="right">136</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">11.3%</td>
<td align="right">98</td>
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
<td align="right">1,164,856,040</td>
<td align="right">1.1%</td>
<td align="right">1,127,273,216</td>
<td align="right">1.1%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">3,465,527,148</td>
<td align="right">3.4%</td>
<td align="right">3,560,766,603</td>
<td align="right">3.4%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">40,926,207,416</td>
<td align="right">40.1%</td>
<td align="right">41,637,372,619</td>
<td align="right">40.1%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">56,536,061,551</td>
<td align="right">55.4%</td>
<td align="right">57,507,453,523</td>
<td align="right">55.4%</td>
<td align="right">1.7%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">151,842,076</td>
<td align="right">5.0%</td>
<td align="right">304,584,107</td>
<td align="right">9.7%</td>
<td align="right">100.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">580,458,045</td>
<td align="right">19.1%</td>
<td align="right">554,127,831</td>
<td align="right">17.6%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">139,759,514</td>
<td align="right">4.6%</td>
<td align="right">134,232,365</td>
<td align="right">4.3%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">94,096,171</td>
<td align="right">3.1%</td>
<td align="right">97,074,409</td>
<td align="right">3.1%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">88,454,475</td>
<td align="right">2.9%</td>
<td align="right">86,131,596</td>
<td align="right">2.7%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">243,037,727</td>
<td align="right">8.0%</td>
<td align="right">239,535,697</td>
<td align="right">7.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,176,325,618</td>
<td align="right">38.7%</td>
<td align="right">1,192,080,748</td>
<td align="right">37.9%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">160,633,234</td>
<td align="right">5.3%</td>
<td align="right">159,063,945</td>
<td align="right">5.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,781,601</td>
<td align="right">6.1%</td>
<td align="right">184,778,757</td>
<td align="right">5.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,497</td>
<td align="right">4.2%</td>
<td align="right">128,815,497</td>
<td align="right">4.1%</td>
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
<td align="right">82,137,201</td>
<td align="right">7.1%</td>
<td align="right">78,768,150</td>
<td align="right">7.0%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">262,768,283</td>
<td align="right">22.6%</td>
<td align="right">260,560,229</td>
<td align="right">23.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">222,032,580</td>
<td align="right">19.1%</td>
<td align="right">220,324,545</td>
<td align="right">19.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">29,968,305</td>
<td align="right">2.6%</td>
<td align="right">29,802,329</td>
<td align="right">2.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">82,704,824</td>
<td align="right">7.1%</td>
<td align="right">82,316,738</td>
<td align="right">7.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">68,353,997</td>
<td align="right">5.9%</td>
<td align="right">68,122,381</td>
<td align="right">6.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">26,715,360</td>
<td align="right">2.3%</td>
<td align="right">26,644,104</td>
<td align="right">2.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,956,335</td>
<td align="right">2.7%</td>
<td align="right">30,927,885</td>
<td align="right">2.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">92,759,638</td>
<td align="right">8.0%</td>
<td align="right">92,684,758</td>
<td align="right">8.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">30,990,170</td>
<td align="right">2.7%</td>
<td align="right">30,992,054</td>
<td align="right">2.7%</td>
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
<td align="left">Frame objects created</td>
<td align="right">70,331,300</td>
<td align="right">1.1%</td>
<td align="right">41,011,193</td>
<td align="right">0.6%</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,891,767</td>
<td align="right">0.4%</td>
<td align="right">23,998,089</td>
<td align="right">0.4%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,409,237,889</td>
<td align="right">80.9%</td>
<td align="right">5,346,679,388</td>
<td align="right">80.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,146,657,628</td>
<td align="right">77.0%</td>
<td align="right">5,092,674,908</td>
<td align="right">76.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">949,158,955</td>
<td align="right">14.2%</td>
<td align="right">941,476,618</td>
<td align="right">14.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">953,436,285</td>
<td align="right">14.3%</td>
<td align="right">945,753,948</td>
<td align="right">14.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,538,332,196</td>
<td align="right">23.0%</td>
<td align="right">1,530,155,882</td>
<td align="right">23.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,538,332,196</td>
<td align="right">23.0%</td>
<td align="right">1,530,155,882</td>
<td align="right">23.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">260,794,621</td>
<td align="right">3.9%</td>
<td align="right">259,510,665</td>
<td align="right">3.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">273,350,945</td>
<td align="right">4.1%</td>
<td align="right">272,273,491</td>
<td align="right">4.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,895,911</td>
<td align="right">8.7%</td>
<td align="right">584,401,934</td>
<td align="right">8.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,402</td>
<td align="right">2.0%</td>
<td align="right">132,513,403</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,441</td>
<td align="right">0.1%</td>
<td align="right">4,273,441</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
<td align="right">3,889</td>
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
<td align="right">434,268</td>
<td align="right">0.3%</td>
<td align="right">265,011</td>
<td align="right">0.2%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,441,240</td>
<td align="right">2.6%</td>
<td align="right">3,405,463</td>
<td align="right">2.1%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">4,832,152</td>
<td align="right"></td>
<td align="right">4,088,358</td>
<td align="right"></td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">62,106,014</td>
<td align="right"></td>
<td align="right">57,337,349</td>
<td align="right"></td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">58,082,118</td>
<td align="right"></td>
<td align="right">54,057,498</td>
<td align="right"></td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,133,802,795</td>
<td align="right"></td>
<td align="right">2,052,879,865</td>
<td align="right"></td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">4,286</td>
<td align="right">0.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">49,715,660,417</td>
<td align="right">45.0%</td>
<td align="right">48,596,432,320</td>
<td align="right">44.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">168,438,104</td>
<td align="right"></td>
<td align="right">165,246,680</td>
<td align="right"></td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">25,049,872,309</td>
<td align="right">22.7%</td>
<td align="right">24,600,983,464</td>
<td align="right">22.5%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,164,948,299</td>
<td align="right">26.0%</td>
<td align="right">23,742,823,462</td>
<td align="right">25.8%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,437,964,951</td>
<td align="right">27.7%</td>
<td align="right">5,352,894,185</td>
<td align="right">27.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,515,897,270</td>
<td align="right">28.1%</td>
<td align="right">5,430,575,315</td>
<td align="right">27.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">40,635,038,172</td>
<td align="right">43.7%</td>
<td align="right">40,033,215,164</td>
<td align="right">43.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,116,107,635</td>
<td align="right"></td>
<td align="right">6,028,188,425</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">34,509,992,204</td>
<td align="right">31.2%</td>
<td align="right">34,979,901,995</td>
<td align="right">32.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,377,614,313</td>
<td align="right"></td>
<td align="right">2,362,021,274</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,216,474,796</td>
<td align="right">1.1%</td>
<td align="right">1,223,587,447</td>
<td align="right">1.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,131,034,213</td>
<td align="right">71.9%</td>
<td align="right">14,080,726,006</td>
<td align="right">72.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,131,141,190</td>
<td align="right"></td>
<td align="right">14,080,848,850</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,508,264</td>
<td align="right">0.4%</td>
<td align="right">71,271,957</td>
<td align="right">0.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,424,055</td>
<td align="right">0.0%</td>
<td align="right">6,409,173</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">25,329,247,559</td>
<td align="right">27.2%</td>
<td align="right">25,292,164,179</td>
<td align="right">27.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,939,890,131</td>
<td align="right">3.2%</td>
<td align="right">2,936,122,569</td>
<td align="right">3.2%</td>
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
<td align="right">364,970</td>
<td align="right">102,568,902</td>
<td align="right">9,480,865,475</td>
<td align="right">747,486,671</td>
<td align="right">765,491,503</td>
<td align="right">364,569</td>
<td align="right">101,516,642</td>
<td align="right">9,509,215,250</td>
<td align="right">754,580,225</td>
<td align="right">764,368,145</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,220</td>
<td align="right">5,622,057,978</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">8,001</td>
<td align="right">4,377,552</td>
<td align="right">5,622,877,388</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">50,160</td>
<td align="right">10.9%</td>
<td align="right">88,477</td>
<td align="right">18.1%</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">260</td>
<td align="right">1.0%</td>
<td align="right">142</td>
<td align="right">0.5%</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">780</td>
<td align="right">0.2%</td>
<td align="right">690</td>
<td align="right">0.1%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">460,096</td>
<td align="right"></td>
<td align="right">489,925</td>
<td align="right"></td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">770</td>
<td align="right">0.2%</td>
<td align="right">748</td>
<td align="right">0.2%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,920,440,837</td>
<td align="right"></td>
<td align="right">4,024,379,448</td>
<td align="right"></td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">247,825,360,646</td>
<td align="right">6,321.4%</td>
<td align="right">241,905,021,538</td>
<td align="right">6,011.0%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">157,239</td>
<td align="right">34.2%</td>
<td align="right">153,702</td>
<td align="right">31.4%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">225,724</td>
<td align="right">49.1%</td>
<td align="right">221,238</td>
<td align="right">45.2%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">26,771</td>
<td align="right">5.8%</td>
<td align="right">26,306</td>
<td align="right">5.4%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">202</td>
<td align="right">0.0%</td>
<td align="right">202</td>
<td align="right">0.0%</td>
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
<td align="right">102</td>
<td align="right">0.0%</td>
<td align="right">102</td>
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
<td align="right">666</td>
<td align="right">0.1%</td>
<td align="right">666</td>
<td align="right">0.1%</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">23,203</td>
<td align="right">86.7%</td>
<td align="right">22,718</td>
<td align="right">86.4%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">26,771</td>
<td align="right"></td>
<td align="right">26,306</td>
<td align="right"></td>
<td align="right">-1.7%</td>
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
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">6,568,392</td>
<td align="right">2.1%</td>
<td align="right">6,376,976</td>
<td align="right">2.1%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">252,202,138</td>
<td align="right">81.6%</td>
<td align="right">245,290,447</td>
<td align="right">81.5%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">309,170,176</td>
<td align="right"></td>
<td align="right">300,814,336</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">50,399,646</td>
<td align="right">16.3%</td>
<td align="right">49,146,913</td>
<td align="right">16.3%</td>
<td align="right">-2.5%</td>
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
<td align="right">2,125,824</td>
<td align="right">0.7%</td>
<td align="right">2,125,824</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
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
<td align="left">4,401</td>
<td align="right">19.0%</td>
<td align="left">4,320</td>
<td align="right">19.0%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">7,243</td>
<td align="right">31.2%</td>
<td align="left">6,998</td>
<td align="right">30.8%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">7,965</td>
<td align="right">34.3%</td>
<td align="left">8,064</td>
<td align="right">35.5%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,206</td>
<td align="right">9.5%</td>
<td align="left">2,037</td>
<td align="right">9.0%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,328</td>
<td align="right">5.7%</td>
<td align="left">1,239</td>
<td align="right">5.5%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">60</td>
<td align="right">0.3%</td>
<td align="left">60</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
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
<td align="left"><= 8</td>
<td align="right">1,190</td>
<td align="right">4.4%</td>
<td align="right">1,154</td>
<td align="right">4.4%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">759</td>
<td align="right">2.8%</td>
<td align="right">652</td>
<td align="right">2.5%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,155</td>
<td align="right">15.5%</td>
<td align="right">4,192</td>
<td align="right">15.9%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,570</td>
<td align="right">32.0%</td>
<td align="right">8,303</td>
<td align="right">31.6%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">5,458</td>
<td align="right">20.4%</td>
<td align="right">5,463</td>
<td align="right">20.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,873</td>
<td align="right">18.2%</td>
<td align="right">4,928</td>
<td align="right">18.7%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,622</td>
<td align="right">6.1%</td>
<td align="right">1,470</td>
<td align="right">5.6%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">144</td>
<td align="right">0.5%</td>
<td align="right">144</td>
<td align="right">0.5%</td>
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
<td align="left"><= 4</td>
<td align="right">642</td>
<td align="right">2.4%</td>
<td align="right">606</td>
<td align="right">2.3%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">709</td>
<td align="right">2.6%</td>
<td align="right">630</td>
<td align="right">2.4%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,984</td>
<td align="right">7.4%</td>
<td align="right">1,935</td>
<td align="right">7.4%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">8,142</td>
<td align="right">30.4%</td>
<td align="right">8,020</td>
<td align="right">30.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">6,933</td>
<td align="right">25.9%</td>
<td align="right">6,796</td>
<td align="right">25.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,544</td>
<td align="right">9.5%</td>
<td align="right">2,606</td>
<td align="right">9.9%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,848</td>
<td align="right">6.9%</td>
<td align="right">1,736</td>
<td align="right">6.6%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">401</td>
<td align="right">1.5%</td>
<td align="right">389</td>
<td align="right">1.5%</td>
<td align="right">-3.0%</td>
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
<td align="left">_DEOPT</td>
<td align="right">19,447,360</td>
<td align="right">4,294,513</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">787,145</td>
<td align="right">189,904</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">53,015,503</td>
<td align="right">23,051,156</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">1,913,667</td>
<td align="right">878,307</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">168,141,049</td>
<td align="right">91,252,709</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">3,025,826</td>
<td align="right">1,744,419</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">336,499,454</td>
<td align="right">199,365,305</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,171,941,655</td>
<td align="right">712,047,609</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">706,843,593</td>
<td align="right">438,002,117</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">263,905,177</td>
<td align="right">174,465,315</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">4,263,152</td>
<td align="right">5,576,732</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">4,263,152</td>
<td align="right">5,576,732</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">374,535,033</td>
<td align="right">261,091,727</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">548,945,794</td>
<td align="right">395,986,868</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">564,794,291</td>
<td align="right">421,798,962</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">387,644</td>
<td align="right">292,742</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">26,149,658</td>
<td align="right">21,350,618</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">26,149,658</td>
<td align="right">21,350,618</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">4,791,846</td>
<td align="right">5,347,546</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">757,843,283</td>
<td align="right">670,443,098</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,801,216,947</td>
<td align="right">7,086,043,542</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,749,152,831</td>
<td align="right">1,604,395,803</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,760,478,692</td>
<td align="right">1,629,331,939</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">87,208,240</td>
<td align="right">81,161,581</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">87,208,240</td>
<td align="right">81,161,581</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">87,918,820</td>
<td align="right">81,872,161</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,384,344,898</td>
<td align="right">3,180,036,020</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,904,865,148</td>
<td align="right">3,681,162,523</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">275,288,286</td>
<td align="right">290,950,949</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,660,463,155</td>
<td align="right">2,510,876,697</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,856,604,619</td>
<td align="right">1,779,688,334</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">32,618,016</td>
<td align="right">33,931,596</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">166,496,405</td>
<td align="right">159,935,502</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,428,988,658</td>
<td align="right">2,334,270,309</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">457,763,537</td>
<td align="right">472,988,103</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">457,763,537</td>
<td align="right">472,988,103</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,900,064,934</td>
<td align="right">1,839,217,279</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,026,051,055</td>
<td align="right">3,902,801,564</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,900,993,224</td>
<td align="right">4,020,084,682</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,611,887,213</td>
<td align="right">1,563,974,053</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">37,980,653,486</td>
<td align="right">36,904,892,228</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,270,719,341</td>
<td align="right">2,207,795,141</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">42,899,253,417</td>
<td align="right">41,716,873,316</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">448,301,946</td>
<td align="right">435,952,581</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">449,096,103</td>
<td align="right">436,746,738</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">406,087,965</td>
<td align="right">394,928,580</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,920,440,837</td>
<td align="right">4,024,379,448</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,393,308,465</td>
<td align="right">1,430,233,606</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,393,483,266</td>
<td align="right">1,430,408,407</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">20,667,339</td>
<td align="right">20,159,363</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">436,348,205</td>
<td align="right">446,766,751</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">582,594,994</td>
<td align="right">596,332,540</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">875,142,869</td>
<td align="right">895,650,258</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">251,018,209</td>
<td align="right">245,167,805</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">109,179,963</td>
<td align="right">106,832,293</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">43,227,170</td>
<td align="right">44,135,833</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,225,181,635</td>
<td align="right">1,250,720,432</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">157,448,970</td>
<td align="right">154,192,635</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">91,521,913</td>
<td align="right">89,714,829</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">68,598,960</td>
<td align="right">69,912,533</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">287,073,874</td>
<td align="right">281,609,239</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">302,082,671</td>
<td align="right">296,425,170</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">139,215,350</td>
<td align="right">141,779,990</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,007,309,452</td>
<td align="right">1,025,734,151</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,094,595,001</td>
<td align="right">1,112,785,534</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,117,419,910</td>
<td align="right">1,135,472,742</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,103,376,443</td>
<td align="right">1,085,654,836</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,128,839,902</td>
<td align="right">1,146,892,647</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,153,518,293</td>
<td align="right">1,171,571,038</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,153,518,293</td>
<td align="right">1,171,571,038</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">759,461,546</td>
<td align="right">748,407,115</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,003,177,583</td>
<td align="right">1,975,565,232</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">206,339,260</td>
<td align="right">203,649,340</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">358,174,679</td>
<td align="right">353,579,033</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">571,923,755</td>
<td align="right">578,972,667</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">152,052,506</td>
<td align="right">150,274,652</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,221,198,622</td>
<td align="right">1,206,985,224</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">233,193,705</td>
<td align="right">235,749,015</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">362,689,691</td>
<td align="right">358,858,130</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">928,158,372</td>
<td align="right">918,701,414</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">928,285,992</td>
<td align="right">918,829,034</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">184,701,749</td>
<td align="right">182,907,759</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,813,766,339</td>
<td align="right">1,796,516,148</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">517,612,271</td>
<td align="right">522,372,262</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">417,053,806</td>
<td align="right">413,276,013</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,349,674,323</td>
<td align="right">4,311,450,962</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">34,917,974</td>
<td align="right">34,612,994</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">427,922,123</td>
<td align="right">424,247,672</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,955,325,735</td>
<td align="right">3,924,546,531</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">106,335,905</td>
<td align="right">105,511,828</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">469,930,789</td>
<td align="right">466,356,229</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,660,683,151</td>
<td align="right">1,648,272,369</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">77,484,437</td>
<td align="right">76,909,671</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">268,486,711</td>
<td align="right">266,580,985</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">500,024,448</td>
<td align="right">496,587,724</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,462,083,514</td>
<td align="right">1,452,180,992</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,409,219,734</td>
<td align="right">4,379,920,117</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,366,585</td>
<td align="right">3,345,438</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,589,774,379</td>
<td align="right">1,579,871,857</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,110,101,413</td>
<td align="right">1,103,897,962</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,070,951,727</td>
<td align="right">1,065,176,419</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,138,424,388</td>
<td align="right">2,126,999,500</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">612,980,114</td>
<td align="right">609,902,648</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,328,054,718</td>
<td align="right">1,321,631,862</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,670,631,249</td>
<td align="right">3,653,893,626</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">72,438,134</td>
<td align="right">72,136,506</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,943,052,402</td>
<td align="right">3,957,277,111</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">841,474,224</td>
<td align="right">838,442,217</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">231,141,085</td>
<td align="right">230,369,030</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,926,001,817</td>
<td align="right">2,917,183,803</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">34,898,714</td>
<td align="right">34,798,213</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">12,298,875</td>
<td align="right">12,263,661</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,022,749,029</td>
<td align="right">1,025,668,526</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">7,033,376,092</td>
<td align="right">7,015,143,819</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">165,823,262</td>
<td align="right">165,446,373</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,364,342,490</td>
<td align="right">2,359,099,102</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">98,167,257</td>
<td align="right">98,376,953</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,765,242,257</td>
<td align="right">3,757,304,454</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">45,464,044</td>
<td align="right">45,369,142</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">686,243,997</td>
<td align="right">685,056,007</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,257,281,347</td>
<td align="right">1,255,108,600</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">564,418,684</td>
<td align="right">565,334,819</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">3,032,790,198</td>
<td align="right">3,037,666,010</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,349,429,495</td>
<td align="right">6,358,649,757</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">825,184,083</td>
<td align="right">826,303,543</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">160,156,076</td>
<td align="right">159,943,879</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">415,636,810</td>
<td align="right">416,170,747</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">54,821,356</td>
<td align="right">54,751,030</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">505,242,548</td>
<td align="right">504,659,290</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,958,707</td>
<td align="right">10,971,352</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">9,526,946</td>
<td align="right">9,516,289</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">272,892,935</td>
<td align="right">272,591,328</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">275,283,975</td>
<td align="right">274,982,368</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,203,326,219</td>
<td align="right">1,202,023,988</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">740,831,612</td>
<td align="right">740,136,025</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">16,260,753</td>
<td align="right">16,245,918</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,047,167,550</td>
<td align="right">5,051,445,504</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">27,669,749</td>
<td align="right">27,689,016</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">22,308,393</td>
<td align="right">22,293,558</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">241,398,666</td>
<td align="right">241,558,512</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,051,402</td>
<td align="right">40,025,548</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">37,667,113</td>
<td align="right">37,645,966</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,209,843,126</td>
<td align="right">1,209,228,035</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">357,315,602</td>
<td align="right">357,464,296</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,489,976,010</td>
<td align="right">1,489,360,919</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">103,856,366</td>
<td align="right">103,815,526</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">381,533,606</td>
<td align="right">381,682,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,999,472,435</td>
<td align="right">1,998,700,655</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">272,830,605</td>
<td align="right">272,932,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">758,147,140</td>
<td align="right">757,943,856</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,211,217</td>
<td align="right">3,211,962</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">66,207,083</td>
<td align="right">66,195,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">13,243,037</td>
<td align="right">13,241,057</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">43,807,886</td>
<td align="right">43,801,786</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">19,651,166</td>
<td align="right">19,649,186</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">615,287,155</td>
<td align="right">615,226,103</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">50,342,040</td>
<td align="right">50,340,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">982,994,383</td>
<td align="right">982,973,236</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">2,650,257</td>
<td align="right">2,650,270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">6,578,007</td>
<td align="right">6,578,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">72,278,361</td>
<td align="right">72,278,261</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">32,572,440</td>
<td align="right">32,572,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,600</td>
<td align="right">47,660,580</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,600</td>
<td align="right">47,660,580</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">277,106,243</td>
<td align="right">277,106,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">277,322,303</td>
<td align="right">277,322,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,509</td>
<td align="right">70,350,499</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,509</td>
<td align="right">70,350,499</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">360,326,589</td>
<td align="right">360,326,609</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,184,069,420</td>
<td align="right">1,184,069,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">147,903,127</td>
<td align="right">147,903,125</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,345,791,817</td>
<td align="right">1,345,791,817</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">975,798,977</td>
<td align="right">975,798,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">498,487,330</td>
<td align="right">498,487,330</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">445,691,287</td>
<td align="right">445,691,287</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">445,691,287</td>
<td align="right">445,691,287</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">181,266,680</td>
<td align="right">181,266,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">146,903,277</td>
<td align="right">146,903,277</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">130,996,843</td>
<td align="right">130,996,843</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">119,055,779</td>
<td align="right">119,055,779</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,492,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">103,178,820</td>
<td align="right">103,178,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">90,286,647</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">75,133,711</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">72,564,910</td>
<td align="right">72,564,910</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,013,740</td>
<td align="right">60,013,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">54,122,020</td>
<td align="right">54,122,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,051,375</td>
<td align="right">51,051,375</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,051,375</td>
<td align="right">51,051,375</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,079</td>
<td align="right">47,071,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">43,572,660</td>
<td align="right">43,572,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">40,583,964</td>
<td align="right">40,583,964</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">39,816,180</td>
<td align="right">39,816,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">32,830,269</td>
<td align="right">32,830,269</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">24,678,391</td>
<td align="right">24,678,391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">24,678,391</td>
<td align="right">24,678,391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">20,612,184</td>
<td align="right">20,612,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">15,447,389</td>
<td align="right">15,447,389</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">13,003,060</td>
<td align="right">13,003,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_TYPE_1</td>
<td align="right">10,787,640</td>
<td align="right">10,787,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">10,787,640</td>
<td align="right">10,787,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">8,116,358</td>
<td align="right">8,116,358</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,137,792</td>
<td align="right">6,137,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">5,378,996</td>
<td align="right">5,378,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">5,140,130</td>
<td align="right">5,140,130</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,473,478</td>
<td align="right">4,473,478</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right">3,837,120</td>
<td align="right">3,837,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,976,000</td>
<td align="right">2,976,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,976,000</td>
<td align="right">2,976,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,583,782</td>
<td align="right">1,583,782</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INSERT_NULL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">93,156</td>
<td align="right">93,156</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">27,762</td>
<td align="right">27,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">26,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">15,393</td>
<td align="right">15,393</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">253</td>
<td align="right">253</td>
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
<td align="left">CALL</td>
<td align="right">1,956</td>
<td align="right">1,926</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">26,458</td>
<td align="right">26,472</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right">23,001</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">38,929</td>
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
<td align="right">100</td>
<td align="right">100</td>
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
<td align="right">100</td>
<td align="right">100</td>
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
<td align="right">2,458</td>
<td align="right">2,399</td>
<td align="right">-2.4%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-05-06
