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
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,679,206</td>
<td align="right">4,730,615</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,190,426</td>
<td align="right">13,327,476</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,471,578</td>
<td align="right">10,538,932</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,808,995</td>
<td align="right">7,843,093</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">15,232,888</td>
<td align="right">15,297,329</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">93,396,950</td>
<td align="right">93,754,567</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">38,098,730</td>
<td align="right">38,238,190</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,748,141</td>
<td align="right">4,765,278</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,739,027</td>
<td align="right">9,773,049</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">169,450,024</td>
<td align="right">169,874,942</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">48,680,731</td>
<td align="right">48,783,544</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">62,492,167</td>
<td align="right">62,623,076</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,498</td>
<td align="right">5,509</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">19,530,766</td>
<td align="right">19,564,951</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">221,339,287</td>
<td align="right">221,685,128</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">405,503,812</td>
<td align="right">406,100,281</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">94,000,369</td>
<td align="right">94,136,638</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">105,276,730</td>
<td align="right">105,428,011</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">197,694,787</td>
<td align="right">197,937,094</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">120,456,265</td>
<td align="right">120,601,404</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">88,351,121</td>
<td align="right">88,451,760</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">360,863,768</td>
<td align="right">361,266,321</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,959,377</td>
<td align="right">27,989,620</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">108,558,837</td>
<td align="right">108,673,038</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">169,938,685</td>
<td align="right">170,108,991</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">565,481,466</td>
<td align="right">566,039,820</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,867,604</td>
<td align="right">70,935,682</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">55,239,420</td>
<td align="right">55,290,094</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">393,091,014</td>
<td align="right">393,442,596</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">46,716,549</td>
<td align="right">46,755,365</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">126,569,535</td>
<td align="right">126,669,491</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">169,794,515</td>
<td align="right">169,925,742</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,644</td>
<td align="right">2,646</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">267,421,018</td>
<td align="right">267,603,925</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">34,172</td>
<td align="right">34,195</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">86,099,687</td>
<td align="right">86,151,106</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">165,859,690</td>
<td align="right">165,956,416</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">126,015,756</td>
<td align="right">126,083,056</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">570,965,890</td>
<td align="right">571,269,711</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">344,363,580</td>
<td align="right">344,522,993</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,068,167,864</td>
<td align="right">2,069,094,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">165,385,765</td>
<td align="right">165,458,453</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">858,891,207</td>
<td align="right">859,237,662</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">407,067</td>
<td align="right">407,228</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">135,642</td>
<td align="right">135,695</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">63,721,064</td>
<td align="right">63,696,824</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">290,173,253</td>
<td align="right">290,283,188</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">454,451,215</td>
<td align="right">454,615,148</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">731,092,983</td>
<td align="right">731,348,569</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">491,285,441</td>
<td align="right">491,452,167</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,005,180,512</td>
<td align="right">1,005,508,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">178,349,224</td>
<td align="right">178,293,701</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">97,197,410</td>
<td align="right">97,227,601</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,791,626,813</td>
<td align="right">3,792,783,794</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">599,309,453</td>
<td align="right">599,491,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,574,532,301</td>
<td align="right">2,575,304,772</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">953,494,439</td>
<td align="right">953,779,398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,217,249</td>
<td align="right">57,234,327</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,171,164,157</td>
<td align="right">5,172,688,783</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">295,801,586</td>
<td align="right">295,715,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">17,942,523,131</td>
<td align="right">17,947,740,468</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">818,753,777</td>
<td align="right">818,977,769</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">182,104,106</td>
<td align="right">182,153,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">112,669,900</td>
<td align="right">112,700,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">205,030,503</td>
<td align="right">205,083,438</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">699,320,197</td>
<td align="right">699,499,664</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,799,215,728</td>
<td align="right">4,800,436,677</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">573,363,900</td>
<td align="right">573,509,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,281,705</td>
<td align="right">2,282,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">619,141,415</td>
<td align="right">619,291,558</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,319,204,267</td>
<td align="right">4,320,231,106</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">149,534,829</td>
<td align="right">149,500,515</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,681,229,918</td>
<td align="right">2,681,841,571</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">951,328,191</td>
<td align="right">951,543,089</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">167,101,542</td>
<td align="right">167,065,163</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,630,683,107</td>
<td align="right">3,631,473,163</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">386,030,672</td>
<td align="right">386,114,081</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">624,772,572</td>
<td align="right">624,907,441</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">116,022,873</td>
<td align="right">115,998,282</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">84,744,625</td>
<td align="right">84,761,529</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,520,787,039</td>
<td align="right">1,521,077,259</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">56,115,688</td>
<td align="right">56,126,269</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">771,693,056</td>
<td align="right">771,834,058</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,225,886,874</td>
<td align="right">2,226,291,655</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,207,909,612</td>
<td align="right">5,208,833,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">466,011,902</td>
<td align="right">466,094,109</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,117,795,168</td>
<td align="right">2,118,159,063</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">665,160,812</td>
<td align="right">665,272,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">367,657,522</td>
<td align="right">367,711,397</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,164,633,091</td>
<td align="right">1,164,793,238</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">451,959,156</td>
<td align="right">452,020,307</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">198,653,562</td>
<td align="right">198,679,022</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,550,896,529</td>
<td align="right">2,551,219,376</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">869,208,459</td>
<td align="right">869,313,556</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">957,612,705</td>
<td align="right">957,724,491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">146,874,701</td>
<td align="right">146,891,664</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">289,542,877</td>
<td align="right">289,575,431</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">357,537,839</td>
<td align="right">357,572,537</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,444,440</td>
<td align="right">57,440,236</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">413,067,752</td>
<td align="right">413,097,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">337,565,575</td>
<td align="right">337,541,200</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,656,090,549</td>
<td align="right">3,656,353,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">237,717,416</td>
<td align="right">237,734,430</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">284,015,681</td>
<td align="right">283,995,619</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,702,196,366</td>
<td align="right">1,702,304,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">460,572,775</td>
<td align="right">460,545,902</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">121,307</td>
<td align="right">121,313</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">752,623</td>
<td align="right">752,593</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,133,560,726</td>
<td align="right">1,133,595,751</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">107,335,466</td>
<td align="right">107,338,575</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">244,970,433</td>
<td align="right">244,977,288</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,113,910,965</td>
<td align="right">1,113,886,449</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">344,272,669</td>
<td align="right">344,265,486</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,533,537</td>
<td align="right">3,533,479</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">876,843,952</td>
<td align="right">876,857,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">125,336,042</td>
<td align="right">125,334,112</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,684,398</td>
<td align="right">7,684,284</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,024,978</td>
<td align="right">20,025,258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">96,357,383</td>
<td align="right">96,356,055</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,356,228</td>
<td align="right">20,356,508</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,356,248</td>
<td align="right">20,356,528</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,761,859</td>
<td align="right">14,762,048</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,431,581</td>
<td align="right">1,431,570</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,384,314</td>
<td align="right">1,384,304</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">273,240,505</td>
<td align="right">273,238,765</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">71,282,104</td>
<td align="right">71,281,662</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">66,531,343</td>
<td align="right">66,531,040</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,839,446</td>
<td align="right">25,839,346</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">81,436,141</td>
<td align="right">81,436,421</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">934,005,315</td>
<td align="right">934,002,139</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,478</td>
<td align="right">5,803,466</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">27,664,863</td>
<td align="right">27,664,811</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,154,659</td>
<td align="right">35,154,599</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">277,635,383</td>
<td align="right">277,635,853</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">146,178,581</td>
<td align="right">146,178,738</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,389</td>
<td align="right">35,549,353</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">113,653,617</td>
<td align="right">113,653,536</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">120,109,446</td>
<td align="right">120,109,377</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">198,452,404</td>
<td align="right">198,452,293</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">133,624,097</td>
<td align="right">133,624,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,892,465</td>
<td align="right">114,892,416</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">33,227,669</td>
<td align="right">33,227,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">238,102,806</td>
<td align="right">238,102,746</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">240,160,092</td>
<td align="right">240,160,032</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">198,135,353</td>
<td align="right">198,135,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">155,090,083</td>
<td align="right">155,090,113</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">72,746,155</td>
<td align="right">72,746,144</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,781,602</td>
<td align="right">184,781,581</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">137,488,171</td>
<td align="right">137,488,157</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,053,945</td>
<td align="right">10,053,946</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">126,614,055</td>
<td align="right">126,614,067</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,905,632</td>
<td align="right">155,905,621</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,621,222</td>
<td align="right">591,621,186</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,390,974</td>
<td align="right">418,390,990</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">815,722,442</td>
<td align="right">815,722,421</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">472,774,780</td>
<td align="right">472,774,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,491</td>
<td align="right">302,246,491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">275,717,092</td>
<td align="right">275,717,092</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,401,560</td>
<td align="right">131,401,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,295</td>
<td align="right">128,850,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">81,316,759</td>
<td align="right">81,316,759</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">75,292,718</td>
<td align="right">75,292,718</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">55,208,384</td>
<td align="right">55,208,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,608</td>
<td align="right">41,964,608</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,351,511</td>
<td align="right">41,351,511</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,033,269</td>
<td align="right">31,033,269</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">9,743,078</td>
<td align="right">9,743,078</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,567,490</td>
<td align="right">3,567,490</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,484,330</td>
<td align="right">3,484,330</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,754,938</td>
<td align="right">1,754,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,643,362</td>
<td align="right">1,643,362</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,232,478</td>
<td align="right">1,232,478</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">117,444</td>
<td align="right">117,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,514</td>
<td align="right">98,514</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,496</td>
<td align="right">84,496</td>
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
<td align="right">57,238</td>
<td align="right">57,238</td>
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
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,299</td>
<td align="right">5,299</td>
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
<td align="right">120</td>
<td align="right">0.0%</td>
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
<td align="right">55,572,127</td>
<td align="right">0.3%</td>
<td align="right">55,563,924</td>
<td align="right">0.3%</td>
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
<td align="right">1,164,128,781</td>
<td align="right">6.6%</td>
<td align="right">1,164,288,821</td>
<td align="right">6.6%</td>
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
<td align="right">16,290,192,401</td>
<td align="right">93.0%</td>
<td align="right">16,291,097,509</td>
<td align="right">93.0%</td>
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
<td align="right">486,471</td>
<td align="right">31.3%</td>
<td align="right">486,527</td>
<td align="right">31.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,066,129</td>
<td align="right">68.7%</td>
<td align="right">1,066,019</td>
<td align="right">68.7%</td>
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
<td align="left">subscr deque</td>
<td align="right">151</td>
<td align="right">0.0%</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">627</td>
<td align="right">0.1%</td>
<td align="right">623</td>
<td align="right">0.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,796</td>
<td align="right">1.6%</td>
<td align="right">7,845</td>
<td align="right">1.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.5%</td>
<td align="right">2,350</td>
<td align="right">0.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">490</td>
<td align="right">0.1%</td>
<td align="right">491</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,997</td>
<td align="right">0.4%</td>
<td align="right">1,996</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,767</td>
<td align="right">0.6%</td>
<td align="right">2,768</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,863</td>
<td align="right">1.8%</td>
<td align="right">8,860</td>
<td align="right">1.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,782</td>
<td align="right">4.9%</td>
<td align="right">23,776</td>
<td align="right">4.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">12,652</td>
<td align="right">2.6%</td>
<td align="right">12,655</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">22,934</td>
<td align="right">4.7%</td>
<td align="right">22,937</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">36,589</td>
<td align="right">7.5%</td>
<td align="right">36,593</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">75,130</td>
<td align="right">15.4%</td>
<td align="right">75,137</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,475</td>
<td align="right">3.8%</td>
<td align="right">18,476</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">20,077</td>
<td align="right">4.1%</td>
<td align="right">20,076</td>
<td align="right">4.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">108,029</td>
<td align="right">22.2%</td>
<td align="right">108,029</td>
<td align="right">22.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">41,400</td>
<td align="right">8.5%</td>
<td align="right">41,400</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">30,354</td>
<td align="right">6.2%</td>
<td align="right">30,354</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">28,692</td>
<td align="right">5.9%</td>
<td align="right">28,692</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">17,023</td>
<td align="right">3.5%</td>
<td align="right">17,023</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,194</td>
<td align="right">1.3%</td>
<td align="right">6,194</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,752</td>
<td align="right">1.2%</td>
<td align="right">5,752</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,163</td>
<td align="right">0.7%</td>
<td align="right">3,163</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,154</td>
<td align="right">0.6%</td>
<td align="right">3,154</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,342</td>
<td align="right">0.5%</td>
<td align="right">2,342</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">1,808</td>
<td align="right">0.4%</td>
<td align="right">1,808</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">325</td>
<td align="right">0.1%</td>
<td align="right">325</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">209</td>
<td align="right">0.0%</td>
<td align="right">209</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">201</td>
<td align="right">0.0%</td>
<td align="right">201</td>
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
<td align="left">and different types</td>
<td align="right">85</td>
<td align="right">0.0%</td>
<td align="right">85</td>
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
<td align="right">184,781,602</td>
<td align="right">100.0%</td>
<td align="right">184,781,581</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,988,810,339</td>
<td align="right">98.5%</td>
<td align="right">10,990,345,475</td>
<td align="right">98.5%</td>
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
<td align="right">163,555,868</td>
<td align="right">1.5%</td>
<td align="right">163,534,072</td>
<td align="right">1.5%</td>
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
<td align="right">160,702,055</td>
<td align="right">1.4%</td>
<td align="right">160,680,783</td>
<td align="right">1.4%</td>
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
<td align="right">3,260,434</td>
<td align="right">100.0%</td>
<td align="right">3,260,071</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">753</td>
<td align="right">168.8%</td>
<td align="right">753</td>
<td align="right">168.8%</td>
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
<td align="right">685,346</td>
<td align="right">97.1%</td>
<td align="right">685,348</td>
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
<td align="right">584,644</td>
<td align="right">82.8%</td>
<td align="right">584,644</td>
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
<td align="right">20,485</td>
<td align="right">99.4%</td>
<td align="right">20,489</td>
<td align="right">99.4%</td>
<td align="right">0.0%</td>
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
<td align="right">1,165,919</td>
<td align="right">0.0%</td>
<td align="right">1,159,766</td>
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
<td align="right">105,155,575</td>
<td align="right">2.3%</td>
<td align="right">105,306,921</td>
<td align="right">2.3%</td>
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
<td align="right">4,506,730,292</td>
<td align="right">97.7%</td>
<td align="right">4,506,939,463</td>
<td align="right">97.7%</td>
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
<td align="right">39,930</td>
<td align="right">27.9%</td>
<td align="right">39,834</td>
<td align="right">27.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">103,028</td>
<td align="right">72.1%</td>
<td align="right">102,941</td>
<td align="right">72.1%</td>
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
<td align="left">float long</td>
<td align="right">11,651</td>
<td align="right">11.3%</td>
<td align="right">11,521</td>
<td align="right">11.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,979</td>
<td align="right">1.9%</td>
<td align="right">1,998</td>
<td align="right">1.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,203</td>
<td align="right">4.1%</td>
<td align="right">4,216</td>
<td align="right">4.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">811</td>
<td align="right">0.8%</td>
<td align="right">813</td>
<td align="right">0.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,746</td>
<td align="right">7.5%</td>
<td align="right">7,742</td>
<td align="right">7.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">37,236</td>
<td align="right">36.1%</td>
<td align="right">37,252</td>
<td align="right">36.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,159</td>
<td align="right">22.5%</td>
<td align="right">23,155</td>
<td align="right">22.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">5,892</td>
<td align="right">5.7%</td>
<td align="right">5,893</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">7.4%</td>
<td align="right">7,648</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,367</td>
<td align="right">1.3%</td>
<td align="right">1,367</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">980</td>
<td align="right">1.0%</td>
<td align="right">980</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.3%</td>
<td align="right">356</td>
<td align="right">0.3%</td>
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
<td align="right">88,305,987</td>
<td align="right">3.9%</td>
<td align="right">88,406,599</td>
<td align="right">3.9%</td>
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
<td align="right">2,190,058,091</td>
<td align="right">96.1%</td>
<td align="right">2,190,178,312</td>
<td align="right">96.1%</td>
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
<td align="right">1,395,959</td>
<td align="right">0.1%</td>
<td align="right">1,395,959</td>
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
<td align="right">43,017</td>
<td align="right">60.2%</td>
<td align="right">43,044</td>
<td align="right">60.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,460</td>
<td align="right">39.8%</td>
<td align="right">28,460</td>
<td align="right">39.8%</td>
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
<td align="right">11,177</td>
<td align="right">26.0%</td>
<td align="right">11,198</td>
<td align="right">26.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,948</td>
<td align="right">23.1%</td>
<td align="right">9,954</td>
<td align="right">23.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">12,053</td>
<td align="right">28.0%</td>
<td align="right">12,053</td>
<td align="right">28.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,839</td>
<td align="right">22.9%</td>
<td align="right">9,839</td>
<td align="right">22.9%</td>
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
<td align="right">61,944,160</td>
<td align="right">3.8%</td>
<td align="right">62,015,290</td>
<td align="right">3.8%</td>
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
<td align="right">204,909,108</td>
<td align="right">12.6%</td>
<td align="right">204,963,117</td>
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
<td align="right">1,355,920,046</td>
<td align="right">83.5%</td>
<td align="right">1,356,093,298</td>
<td align="right">83.5%</td>
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
<td align="right">115,796</td>
<td align="right">9.0%</td>
<td align="right">114,714</td>
<td align="right">8.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,174,181</td>
<td align="right">91.0%</td>
<td align="right">1,175,530</td>
<td align="right">91.1%</td>
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
<td align="left">dict items</td>
<td align="right">52,028</td>
<td align="right">44.9%</td>
<td align="right">50,946</td>
<td align="right">44.4%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,490</td>
<td align="right">5.6%</td>
<td align="right">6,470</td>
<td align="right">5.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">14,273</td>
<td align="right">12.3%</td>
<td align="right">14,298</td>
<td align="right">12.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">6,733</td>
<td align="right">5.8%</td>
<td align="right">6,730</td>
<td align="right">5.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,467</td>
<td align="right">3.9%</td>
<td align="right">4,466</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">11,085</td>
<td align="right">9.6%</td>
<td align="right">11,084</td>
<td align="right">9.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">9,021</td>
<td align="right">7.8%</td>
<td align="right">9,021</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,319</td>
<td align="right">3.7%</td>
<td align="right">4,319</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,792</td>
<td align="right">3.3%</td>
<td align="right">3,792</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,737</td>
<td align="right">1.5%</td>
<td align="right">1,737</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,132</td>
<td align="right">1.0%</td>
<td align="right">1,132</td>
<td align="right">1.0%</td>
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
<td align="right">12,918,745</td>
<td align="right">12,918,745 / 0 !!</td>
<td align="right">12,959,926</td>
<td align="right">12,959,926 / 0 !!</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">308,128,988</td>
<td align="right">308,128,988 / 0 !!</td>
<td align="right">308,300,177</td>
<td align="right">308,300,177 / 0 !!</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">170,058,873</td>
<td align="right">170,058,873 / 0 !!</td>
<td align="right">169,991,001</td>
<td align="right">169,991,001 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">393,687,689</td>
<td align="right">393,687,689 / 0 !!</td>
<td align="right">393,683,497</td>
<td align="right">393,683,497 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">6,040,819</td>
<td align="right">6,040,819 / 0 !!</td>
<td align="right">6,040,797</td>
<td align="right">6,040,797 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">117,433,092</td>
<td align="right">117,433,092 / 0 !!</td>
<td align="right">117,432,986</td>
<td align="right">117,432,986 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">102,341,381</td>
<td align="right">102,341,381 / 0 !!</td>
<td align="right">102,341,369</td>
<td align="right">102,341,369 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,849,462</td>
<td align="right">34,849,462 / 0 !!</td>
<td align="right">34,849,462</td>
<td align="right">34,849,462 / 0 !!</td>
<td align="right">0.0%</td>
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
<td align="right">563,719,856</td>
<td align="right">4.2%</td>
<td align="right">564,278,320</td>
<td align="right">4.2%</td>
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
<td align="right">781,603,818</td>
<td align="right">5.9%</td>
<td align="right">781,228,261</td>
<td align="right">5.9%</td>
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
<td align="right">11,971,366,693</td>
<td align="right">89.9%</td>
<td align="right">11,973,642,806</td>
<td align="right">89.9%</td>
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
<td align="left">Success</td>
<td align="right">14,833,244</td>
<td align="right">96.8%</td>
<td align="right">14,826,172</td>
<td align="right">96.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">493,113</td>
<td align="right">3.2%</td>
<td align="right">493,137</td>
<td align="right">3.2%</td>
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
<td align="right">4,937</td>
<td align="right">1.0%</td>
<td align="right">4,914</td>
<td align="right">1.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">45,029</td>
<td align="right">9.1%</td>
<td align="right">45,053</td>
<td align="right">9.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23,194</td>
<td align="right">4.7%</td>
<td align="right">23,182</td>
<td align="right">4.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,303</td>
<td align="right">3.3%</td>
<td align="right">16,310</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,945</td>
<td align="right">1.6%</td>
<td align="right">7,948</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40,695</td>
<td align="right">8.3%</td>
<td align="right">40,685</td>
<td align="right">8.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">61,384</td>
<td align="right">12.4%</td>
<td align="right">61,391</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.3%</td>
<td align="right">6,405</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,449</td>
<td align="right">0.9%</td>
<td align="right">4,449</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
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
<td align="left">not managed dict</td>
<td align="right">1,809</td>
<td align="right">0.4%</td>
<td align="right">1,809</td>
<td align="right">0.4%</td>
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
<td align="left">non object slot</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">821</td>
<td align="right">0.2%</td>
<td align="right">821</td>
<td align="right">0.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,717,524,230</td>
<td align="right">99.7%</td>
<td align="right">4,719,223,552</td>
<td align="right">99.7%</td>
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
<td align="right">53,887</td>
<td align="right">0.0%</td>
<td align="right">53,891</td>
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
<td align="right">14,623,513</td>
<td align="right">0.3%</td>
<td align="right">14,623,611</td>
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
<td align="right">1,473</td>
<td align="right">0.0%</td>
<td align="right">1,473</td>
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
<td align="right">139,116</td>
<td align="right">100.0%</td>
<td align="right">139,209</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">251</td>
<td align="right">0.0%</td>
<td align="right">253</td>
<td align="right">0.0%</td>
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
<td align="right">64,373,841</td>
<td align="right">100.0%</td>
<td align="right">64,562,329</td>
<td align="right">100.0%</td>
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
<td align="right">2,393</td>
<td align="right">100.0%</td>
<td align="right">2,393</td>
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
<td align="right">591,606,511</td>
<td align="right">82.1%</td>
<td align="right">591,606,475</td>
<td align="right">82.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">111,828,359</td>
<td align="right">5.7%</td>
<td align="right">111,493,712</td>
<td align="right">5.6%</td>
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
<td align="right">1,792,374,861</td>
<td align="right">90.7%</td>
<td align="right">1,793,045,760</td>
<td align="right">90.7%</td>
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
<td align="right">72,653,693</td>
<td align="right">3.7%</td>
<td align="right">72,653,681</td>
<td align="right">3.7%</td>
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
<td align="right">2,149,794</td>
<td align="right">97.7%</td>
<td align="right">2,143,460</td>
<td align="right">97.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">51,707</td>
<td align="right">2.3%</td>
<td align="right">51,709</td>
<td align="right">2.4%</td>
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
<td align="right">264,309</td>
<td align="right">511.2%</td>
<td align="right">264,329</td>
<td align="right">511.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">47.3%</td>
<td align="right">24,476</td>
<td align="right">47.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.8%</td>
<td align="right">7,666</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,331</td>
<td align="right">10.3%</td>
<td align="right">5,331</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,963</td>
<td align="right">9.6%</td>
<td align="right">4,963</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,350</td>
<td align="right">6.5%</td>
<td align="right">3,350</td>
<td align="right">6.5%</td>
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
<td align="right">817</td>
<td align="right">1.6%</td>
<td align="right">817</td>
<td align="right">1.6%</td>
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
<td align="right">360</td>
<td align="right">0.7%</td>
<td align="right">360</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">922,037,754</td>
<td align="right">85.6%</td>
<td align="right">922,155,822</td>
<td align="right">85.6%</td>
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
<td align="right">155,038,982</td>
<td align="right">14.4%</td>
<td align="right">155,039,011</td>
<td align="right">14.4%</td>
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
<td align="right">2,122</td>
<td align="right">4.1%</td>
<td align="right">2,123</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">49,019</td>
<td align="right">95.9%</td>
<td align="right">49,019</td>
<td align="right">95.8%</td>
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
<td align="right">17,323</td>
<td align="right">35.3%</td>
<td align="right">17,323</td>
<td align="right">35.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">15,163</td>
<td align="right">30.9%</td>
<td align="right">15,163</td>
<td align="right">30.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">11,272</td>
<td align="right">23.0%</td>
<td align="right">11,272</td>
<td align="right">23.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,010</td>
<td align="right">6.1%</td>
<td align="right">3,010</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,662</td>
<td align="right">3.4%</td>
<td align="right">1,662</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.7%</td>
<td align="right">341</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">180</td>
<td align="right">0.4%</td>
<td align="right">180</td>
<td align="right">0.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,470,557,434</td>
<td align="right">95.5%</td>
<td align="right">4,471,498,295</td>
<td align="right">95.5%</td>
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
<td align="right">63,617,300</td>
<td align="right">1.4%</td>
<td align="right">63,617,384</td>
<td align="right">1.4%</td>
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
<td align="right">145,618,933</td>
<td align="right">3.1%</td>
<td align="right">145,619,058</td>
<td align="right">3.1%</td>
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
<td align="right">508,689</td>
<td align="right">28.9%</td>
<td align="right">508,706</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,249,583</td>
<td align="right">71.1%</td>
<td align="right">1,249,606</td>
<td align="right">71.1%</td>
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
<td align="right">33,932</td>
<td align="right">6.7%</td>
<td align="right">33,905</td>
<td align="right">6.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">96,037</td>
<td align="right">18.9%</td>
<td align="right">96,079</td>
<td align="right">18.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,747</td>
<td align="right">1.9%</td>
<td align="right">9,743</td>
<td align="right">1.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,374</td>
<td align="right">2.6%</td>
<td align="right">13,377</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,948</td>
<td align="right">3.1%</td>
<td align="right">15,951</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">73,804</td>
<td align="right">14.5%</td>
<td align="right">73,791</td>
<td align="right">14.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,803</td>
<td align="right">50.9%</td>
<td align="right">258,816</td>
<td align="right">50.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">5,158</td>
<td align="right">1.0%</td>
<td align="right">5,158</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
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
<td align="right">1,240,578,444</td>
<td align="right">99.9%</td>
<td align="right">1,240,664,423</td>
<td align="right">99.9%</td>
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
<td align="right">1,420,744</td>
<td align="right">0.1%</td>
<td align="right">1,420,720</td>
<td align="right">0.1%</td>
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
<td align="left">Success</td>
<td align="right">10,049</td>
<td align="right">92.0%</td>
<td align="right">10,061</td>
<td align="right">92.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">868</td>
<td align="right">8.0%</td>
<td align="right">869</td>
<td align="right">8.0%</td>
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
<td align="left">sequence</td>
<td align="right">634</td>
<td align="right">73.0%</td>
<td align="right">635</td>
<td align="right">73.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.7%</td>
<td align="right">136</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">11.3%</td>
<td align="right">98</td>
<td align="right">11.3%</td>
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
<td align="right">1,241,494,363</td>
<td align="right">1.2%</td>
<td align="right">1,240,820,008</td>
<td align="right">1.2%</td>
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
<td align="right">3,433,686,016</td>
<td align="right">3.3%</td>
<td align="right">3,434,891,707</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">57,566,662,102</td>
<td align="right">55.4%</td>
<td align="right">57,582,019,065</td>
<td align="right">55.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">41,744,933,061</td>
<td align="right">40.1%</td>
<td align="right">41,755,076,108</td>
<td align="right">40.1%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">105,155,575</td>
<td align="right">3.5%</td>
<td align="right">105,306,921</td>
<td align="right">3.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">88,305,987</td>
<td align="right">3.0%</td>
<td align="right">88,406,599</td>
<td align="right">3.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">563,719,856</td>
<td align="right">18.8%</td>
<td align="right">564,278,320</td>
<td align="right">18.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">204,909,108</td>
<td align="right">6.8%</td>
<td align="right">204,963,117</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,164,128,781</td>
<td align="right">38.9%</td>
<td align="right">1,164,288,821</td>
<td align="right">38.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">160,702,055</td>
<td align="right">5.4%</td>
<td align="right">160,680,783</td>
<td align="right">5.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">145,618,933</td>
<td align="right">4.9%</td>
<td align="right">145,619,058</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">155,038,982</td>
<td align="right">5.2%</td>
<td align="right">155,039,011</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,781,602</td>
<td align="right">6.2%</td>
<td align="right">184,781,581</td>
<td align="right">6.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,497</td>
<td align="right">4.3%</td>
<td align="right">128,815,497</td>
<td align="right">4.3%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">92,774,789</td>
<td align="right">7.5%</td>
<td align="right">92,440,769</td>
<td align="right">7.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">244,927,054</td>
<td align="right">19.7%</td>
<td align="right">244,519,746</td>
<td align="right">19.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">30,956,444</td>
<td align="right">2.5%</td>
<td align="right">31,001,546</td>
<td align="right">2.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,910,321</td>
<td align="right">2.5%</td>
<td align="right">30,936,349</td>
<td align="right">2.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">78,604,292</td>
<td align="right">6.3%</td>
<td align="right">78,621,717</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">324,467,818</td>
<td align="right">26.1%</td>
<td align="right">324,480,025</td>
<td align="right">26.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">78,467,457</td>
<td align="right">6.3%</td>
<td align="right">78,464,748</td>
<td align="right">6.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">29,961,702</td>
<td align="right">2.4%</td>
<td align="right">29,961,738</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">68,228,288</td>
<td align="right">5.5%</td>
<td align="right">68,228,356</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">26,696,227</td>
<td align="right">2.2%</td>
<td align="right">26,696,222</td>
<td align="right">2.2%</td>
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
<td align="right">936,105,161</td>
<td align="right">14.0%</td>
<td align="right">936,395,573</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">940,382,491</td>
<td align="right">14.1%</td>
<td align="right">940,672,903</td>
<td align="right">14.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,412,635,987</td>
<td align="right">80.9%</td>
<td align="right">5,414,286,642</td>
<td align="right">80.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,163,304,765</td>
<td align="right">77.2%</td>
<td align="right">5,164,640,657</td>
<td align="right">77.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,525,278,500</td>
<td align="right">22.8%</td>
<td align="right">1,525,568,724</td>
<td align="right">22.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,525,278,500</td>
<td align="right">22.8%</td>
<td align="right">1,525,568,724</td>
<td align="right">22.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">273,423,272</td>
<td align="right">4.1%</td>
<td align="right">273,457,128</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,330,665</td>
<td align="right">1.1%</td>
<td align="right">70,330,983</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,891,792</td>
<td align="right">0.4%</td>
<td align="right">24,891,733</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">260,794,776</td>
<td align="right">3.9%</td>
<td align="right">260,794,475</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,896,009</td>
<td align="right">8.7%</td>
<td align="right">584,895,821</td>
<td align="right">8.7%</td>
<td align="right">-0.0%</td>
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
<td align="left">Mortal increfs</td>
<td align="right">43,338,484,532</td>
<td align="right">44.8%</td>
<td align="right">40,348,391,832</td>
<td align="right">43.3%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">52,805,378,495</td>
<td align="right">46.0%</td>
<td align="right">49,814,621,733</td>
<td align="right">45.1%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">26,008,692,636</td>
<td align="right">22.7%</td>
<td align="right">25,194,910,394</td>
<td align="right">22.8%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">51,871,077</td>
<td align="right"></td>
<td align="right">53,458,996</td>
<td align="right"></td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">57,369,030</td>
<td align="right"></td>
<td align="right">58,893,973</td>
<td align="right"></td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">25,985,691,907</td>
<td align="right">26.9%</td>
<td align="right">25,525,500,510</td>
<td align="right">27.4%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">34,729,104,093</td>
<td align="right">30.3%</td>
<td align="right">34,271,291,480</td>
<td align="right">31.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,307,065</td>
<td align="right"></td>
<td align="right">6,242,136</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">168,723,232</td>
<td align="right"></td>
<td align="right">168,860,214</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,210,958,374</td>
<td align="right"></td>
<td align="right">2,209,935,169</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,373,131,321</td>
<td align="right"></td>
<td align="right">2,373,858,319</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,943,920,320</td>
<td align="right">3.0%</td>
<td align="right">2,944,486,559</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,241,132,352</td>
<td align="right">1.1%</td>
<td align="right">1,241,368,320</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,380,283,510</td>
<td align="right">25.2%</td>
<td align="right">24,384,635,570</td>
<td align="right">26.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,117,369,466</td>
<td align="right"></td>
<td align="right">6,118,084,309</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,439,144,986</td>
<td align="right">27.7%</td>
<td align="right">5,439,682,219</td>
<td align="right">27.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,517,076,592</td>
<td align="right">28.1%</td>
<td align="right">5,517,618,519</td>
<td align="right">28.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,093,410,153</td>
<td align="right">71.9%</td>
<td align="right">14,094,608,830</td>
<td align="right">71.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,093,517,372</td>
<td align="right"></td>
<td align="right">14,094,707,653</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,508,137</td>
<td align="right">0.4%</td>
<td align="right">71,512,816</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,423,469</td>
<td align="right">0.0%</td>
<td align="right">6,423,484</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,441,240</td>
<td align="right">2.6%</td>
<td align="right">4,441,240</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">434,268</td>
<td align="right">0.3%</td>
<td align="right">434,268</td>
<td align="right">0.3%</td>
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
<td align="right">364,994</td>
<td align="right">102,382,288</td>
<td align="right">9,497,958,942</td>
<td align="right">748,438,446</td>
<td align="right">766,035,398</td>
<td align="right">364,917</td>
<td align="right">102,457,168</td>
<td align="right">9,486,320,264</td>
<td align="right">747,260,455</td>
<td align="right">766,364,293</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,220</td>
<td align="right">5,619,541,746</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,220</td>
<td align="right">5,619,542,130</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">200</td>
<td align="right">0.8%</td>
<td align="right">260</td>
<td align="right">1.0%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">796</td>
<td align="right">0.2%</td>
<td align="right">770</td>
<td align="right">0.2%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">609</td>
<td align="right">0.1%</td>
<td align="right">613</td>
<td align="right">0.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">218,236</td>
<td align="right">48.1%</td>
<td align="right">218,375</td>
<td align="right">48.1%</td>
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
<td align="right">25,107</td>
<td align="right">5.5%</td>
<td align="right">25,120</td>
<td align="right">5.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">454,043</td>
<td align="right"></td>
<td align="right">454,251</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,813,816,917</td>
<td align="right"></td>
<td align="right">3,815,370,120</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">162,887</td>
<td align="right">35.9%</td>
<td align="right">162,950</td>
<td align="right">35.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">47,611</td>
<td align="right">10.5%</td>
<td align="right">47,604</td>
<td align="right">10.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">243,711,185,360</td>
<td align="right">6,390.2%</td>
<td align="right">243,724,040,401</td>
<td align="right">6,388.0%</td>
<td align="right">0.0%</td>
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
<td align="right">62</td>
<td align="right">0.0%</td>
<td align="right">62</td>
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
<td align="right">679</td>
<td align="right">0.1%</td>
<td align="right">679</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">25,107</td>
<td align="right"></td>
<td align="right">25,120</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">21,920</td>
<td align="right">87.3%</td>
<td align="right">21,913</td>
<td align="right">87.2%</td>
<td align="right">-0.0%</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">224,206,848</td>
<td align="right">75.7%</td>
<td align="right">1,548,288</td>
<td align="right">0.6%</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">242,803,446</td>
<td align="right">82.0%</td>
<td align="right">227,370,623</td>
<td align="right">80.9%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">296,136,704</td>
<td align="right"></td>
<td align="right">281,088,000</td>
<td align="right"></td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">6,194,280</td>
<td align="right">2.1%</td>
<td align="right">6,030,128</td>
<td align="right">2.1%</td>
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
<td align="right">47,138,978</td>
<td align="right">15.9%</td>
<td align="right">47,687,249</td>
<td align="right">17.0%</td>
<td align="right">1.2%</td>
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
<td align="left">3,734</td>
<td align="right">17.0%</td>
<td align="left">4,414</td>
<td align="right">20.1%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">6,987</td>
<td align="right">31.9%</td>
<td align="left">6,750</td>
<td align="right">30.8%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">7,665</td>
<td align="right">35.0%</td>
<td align="left">7,740</td>
<td align="right">35.3%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,128</td>
<td align="right">9.7%</td>
<td align="left">1,972</td>
<td align="right">9.0%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,324</td>
<td align="right">6.0%</td>
<td align="left">997</td>
<td align="right">4.5%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">82</td>
<td align="right">0.4%</td>
<td align="left">40</td>
<td align="right">0.2%</td>
<td align="right">-51.2%</td>
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
<td align="right">1,207</td>
<td align="right">4.8%</td>
<td align="right">1,205</td>
<td align="right">4.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">732</td>
<td align="right">2.9%</td>
<td align="right">727</td>
<td align="right">2.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,018</td>
<td align="right">16.0%</td>
<td align="right">4,026</td>
<td align="right">16.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,246</td>
<td align="right">32.8%</td>
<td align="right">8,170</td>
<td align="right">32.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">5,093</td>
<td align="right">20.3%</td>
<td align="right">5,178</td>
<td align="right">20.6%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,471</td>
<td align="right">17.8%</td>
<td align="right">4,482</td>
<td align="right">17.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,236</td>
<td align="right">4.9%</td>
<td align="right">1,228</td>
<td align="right">4.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">104</td>
<td align="right">0.4%</td>
<td align="right">104</td>
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
<td align="left"><= 4</td>
<td align="right">620</td>
<td align="right">2.5%</td>
<td align="right">618</td>
<td align="right">2.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">730</td>
<td align="right">2.9%</td>
<td align="right">731</td>
<td align="right">2.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,058</td>
<td align="right">8.2%</td>
<td align="right">2,058</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,823</td>
<td align="right">31.2%</td>
<td align="right">7,770</td>
<td align="right">30.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">6,548</td>
<td align="right">26.1%</td>
<td align="right">6,548</td>
<td align="right">26.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,276</td>
<td align="right">9.1%</td>
<td align="right">2,326</td>
<td align="right">9.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,562</td>
<td align="right">6.2%</td>
<td align="right">1,563</td>
<td align="right">6.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">303</td>
<td align="right">1.2%</td>
<td align="right">299</td>
<td align="right">1.2%</td>
<td align="right">-1.3%</td>
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
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">497,360</td>
<td align="right">554,949</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">962,310</td>
<td align="right">1,049,122</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">5,515,396</td>
<td align="right">5,378,996</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">3,137,010</td>
<td align="right">3,196,091</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">72,786,480</td>
<td align="right">73,221,279</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">71,628,120</td>
<td align="right">71,950,499</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">71,628,120</td>
<td align="right">71,950,499</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">33,003,549</td>
<td align="right">32,864,089</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">37,870,653</td>
<td align="right">37,731,193</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">8,116,338</td>
<td align="right">8,140,578</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">39,644,334</td>
<td align="right">39,753,715</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">177,526,736</td>
<td align="right">177,961,726</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">116,063,892</td>
<td align="right">116,341,479</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">63,962,201</td>
<td align="right">63,828,316</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">20,688,844</td>
<td align="right">20,645,838</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">150,371,016</td>
<td align="right">150,671,788</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,472,594</td>
<td align="right">5,461,906</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">308,401,507</td>
<td align="right">308,905,818</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">55,193,171</td>
<td align="right">55,108,612</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">75,614,013</td>
<td align="right">75,725,481</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">7,683,114</td>
<td align="right">7,671,866</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">66,312,666</td>
<td align="right">66,218,745</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">44,408,906</td>
<td align="right">44,466,495</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">157,341,869</td>
<td align="right">157,144,264</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">12,331,604</td>
<td align="right">12,346,221</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">40,280,176</td>
<td align="right">40,325,317</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">162,111,970</td>
<td align="right">162,268,485</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">558,586,911</td>
<td align="right">559,102,346</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">33,405,242</td>
<td align="right">33,434,517</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">34,780,103</td>
<td align="right">34,806,838</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">556,659,935</td>
<td align="right">557,059,481</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">231,151,872</td>
<td align="right">230,992,786</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">900,958,671</td>
<td align="right">901,574,687</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">979,480,360</td>
<td align="right">980,141,517</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">345,040,300</td>
<td align="right">344,810,512</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,022,618,934</td>
<td align="right">1,023,291,342</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,047,225,812</td>
<td align="right">1,047,898,190</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,057,279,443</td>
<td align="right">1,057,951,821</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,057,279,443</td>
<td align="right">1,057,951,821</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">232,771,843</td>
<td align="right">232,906,481</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">158,361,972</td>
<td align="right">158,281,297</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">31,962,440</td>
<td align="right">31,976,807</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">364,603,624</td>
<td align="right">364,762,516</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,813,816,917</td>
<td align="right">3,815,370,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,779,036,561</td>
<td align="right">3,780,563,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">829,467,024</td>
<td align="right">829,163,250</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,129,466,428</td>
<td align="right">1,129,878,306</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">778,088,752</td>
<td align="right">778,331,499</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">410,645,939</td>
<td align="right">410,519,464</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,182,267,403</td>
<td align="right">1,181,938,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">829,468,877</td>
<td align="right">829,699,004</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">829,608,777</td>
<td align="right">829,838,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,864,616,802</td>
<td align="right">2,865,355,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">51,380,125</td>
<td align="right">51,367,505</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">12,018,658</td>
<td align="right">12,021,510</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">11,009,556</td>
<td align="right">11,007,008</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">262,143,239</td>
<td align="right">262,084,471</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,265,913,016</td>
<td align="right">6,267,252,265</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">448,811,110</td>
<td align="right">448,723,298</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">449,605,251</td>
<td align="right">449,517,439</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,752,899,441</td>
<td align="right">3,752,193,204</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,545,255</td>
<td align="right">1,545,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,997,263,987</td>
<td align="right">4,998,180,586</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,814,233,446</td>
<td align="right">2,813,755,589</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,399,885,175</td>
<td align="right">3,400,436,853</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">736,008,999</td>
<td align="right">736,123,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,802,085,615</td>
<td align="right">1,802,365,225</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,673,068,649</td>
<td align="right">3,673,634,331</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,634,519,825</td>
<td align="right">3,633,962,596</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">443,713,526</td>
<td align="right">443,649,087</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">443,713,526</td>
<td align="right">443,649,087</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">104,160,906</td>
<td align="right">104,175,571</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">105,995,545</td>
<td align="right">106,010,126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,202,775,253</td>
<td align="right">1,202,611,390</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">13,228,137</td>
<td align="right">13,229,817</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">146,228,615</td>
<td align="right">146,246,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,234,115,590</td>
<td align="right">4,234,592,368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">235,458,817</td>
<td align="right">235,433,074</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">498,770,824</td>
<td align="right">498,716,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">399,711,360</td>
<td align="right">399,753,426</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,167,792,982</td>
<td align="right">1,167,911,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,167,967,801</td>
<td align="right">1,168,086,336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,742,609,905</td>
<td align="right">7,741,892,623</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">726,320,762</td>
<td align="right">726,254,828</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,010,892,412</td>
<td align="right">1,010,804,176</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,452,096,099</td>
<td align="right">2,451,882,145</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">852,231,399</td>
<td align="right">852,157,774</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">19,636,266</td>
<td align="right">19,637,946</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">267,063,840</td>
<td align="right">267,086,654</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,740,778,890</td>
<td align="right">1,740,637,465</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">549,670,653</td>
<td align="right">549,628,986</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,117,731,332</td>
<td align="right">1,117,816,013</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">41,227,007</td>
<td align="right">41,230,095</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,882,227,623</td>
<td align="right">3,881,953,711</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,444,531,475</td>
<td align="right">1,444,632,975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,566,305,600</td>
<td align="right">1,566,407,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,097,117,488</td>
<td align="right">1,097,055,836</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">159,622,641</td>
<td align="right">159,630,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,858,581,625</td>
<td align="right">2,858,446,159</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,425,380,621</td>
<td align="right">4,425,177,214</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">264,121,820</td>
<td align="right">264,110,188</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">266,512,860</td>
<td align="right">266,501,228</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">617,099,211</td>
<td align="right">617,126,042</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">426,424,905</td>
<td align="right">426,443,245</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,663,572,764</td>
<td align="right">1,663,503,063</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,018,431,803</td>
<td align="right">2,018,516,174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,778,238,002</td>
<td align="right">1,778,312,234</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,671,539,698</td>
<td align="right">1,671,608,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,965,617,815</td>
<td align="right">3,965,462,723</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,606,006,175</td>
<td align="right">1,605,943,373</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">504,136,182</td>
<td align="right">504,155,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,988,690,453</td>
<td align="right">6,988,442,396</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">42,469,673,807</td>
<td align="right">42,471,094,310</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,085,745,626</td>
<td align="right">4,085,610,657</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">148,478,830</td>
<td align="right">148,474,008</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,291,170,124</td>
<td align="right">2,291,098,362</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,141,774,495</td>
<td align="right">2,141,713,167</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">982,995,463</td>
<td align="right">983,019,703</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,999,570,044</td>
<td align="right">1,999,614,433</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">756,496,762</td>
<td align="right">756,512,657</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">406,066,613</td>
<td align="right">406,058,868</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">506,247,840</td>
<td align="right">506,257,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,293,659,617</td>
<td align="right">1,293,679,383</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">307,798,944</td>
<td align="right">307,802,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">608,728,317</td>
<td align="right">608,734,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">397,333,352</td>
<td align="right">397,337,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,013,740</td>
<td align="right">60,013,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">179,608,470</td>
<td align="right">179,606,910</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,317,329,653</td>
<td align="right">1,317,318,799</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,062,570,844</td>
<td align="right">1,062,579,141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,075,479,655</td>
<td align="right">1,075,471,293</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,912,702,336</td>
<td align="right">1,912,713,171</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">103,892,686</td>
<td align="right">103,892,126</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">745,154,805</td>
<td align="right">745,158,175</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,051,478</td>
<td align="right">40,051,306</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">2,650,277</td>
<td align="right">2,650,267</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">2,740,907</td>
<td align="right">2,740,897</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">371,197,000</td>
<td align="right">371,198,088</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">447,432,070</td>
<td align="right">447,433,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">447,432,070</td>
<td align="right">447,433,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">13,003,000</td>
<td align="right">13,002,980</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">37,602,654,678</td>
<td align="right">37,602,705,242</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">426,073,624</td>
<td align="right">426,074,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,266,978,830</td>
<td align="right">2,266,980,981</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">73,218,810</td>
<td align="right">73,218,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">184,604,086</td>
<td align="right">184,604,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">38,477,627</td>
<td align="right">38,477,607</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">118,974,079</td>
<td align="right">118,974,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">47,613,029</td>
<td align="right">47,613,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">69,942,860</td>
<td align="right">69,942,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,197,378,428</td>
<td align="right">1,197,378,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,477,511,292</td>
<td align="right">1,477,511,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">273,269,210</td>
<td align="right">273,269,190</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">273,485,270</td>
<td align="right">273,485,250</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,495</td>
<td align="right">70,350,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,495</td>
<td align="right">70,350,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">360,326,588</td>
<td align="right">360,326,609</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">690,453,296</td>
<td align="right">690,453,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">545,748,960</td>
<td align="right">545,748,981</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">250,945,006</td>
<td align="right">250,944,998</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">131,031,865</td>
<td align="right">131,031,863</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,184,146,389</td>
<td align="right">1,184,146,405</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,345,792,897</td>
<td align="right">1,345,792,897</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">975,798,997</td>
<td align="right">975,798,997</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">735,480,741</td>
<td align="right">735,480,741</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">580,811,048</td>
<td align="right">580,811,048</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">498,487,330</td>
<td align="right">498,487,330</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">469,767,509</td>
<td align="right">469,767,509</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">383,720,121</td>
<td align="right">383,720,121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">357,582,094</td>
<td align="right">357,582,094</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">254,690,388</td>
<td align="right">254,690,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">206,340,500</td>
<td align="right">206,340,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">164,781,729</td>
<td align="right">164,781,729</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">140,461,197</td>
<td align="right">140,461,197</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">139,241,997</td>
<td align="right">139,241,997</td>
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
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">51,047,020</td>
<td align="right">51,047,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,033,355</td>
<td align="right">51,033,355</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,033,355</td>
<td align="right">51,033,355</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,079</td>
<td align="right">47,071,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">45,626,940</td>
<td align="right">45,626,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">45,626,940</td>
<td align="right">45,626,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">43,844,206</td>
<td align="right">43,844,206</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">40,595,844</td>
<td align="right">40,595,844</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">39,828,060</td>
<td align="right">39,828,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">24,484,698</td>
<td align="right">24,484,698</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">24,484,698</td>
<td align="right">24,484,698</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">20,612,184</td>
<td align="right">20,612,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">10,053,631</td>
<td align="right">10,053,631</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">10,053,631</td>
<td align="right">10,053,631</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,137,792</td>
<td align="right">6,137,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">5,769,600</td>
<td align="right">5,769,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">4,935,092</td>
<td align="right">4,935,092</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">4,935,092</td>
<td align="right">4,935,092</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,473,478</td>
<td align="right">4,473,478</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,366,585</td>
<td align="right">3,366,585</td>
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
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">1,913,667</td>
<td align="right">1,913,667</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">1,598,976</td>
<td align="right">1,598,976</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,502,102</td>
<td align="right">1,502,102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,303,010</td>
<td align="right">1,303,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">954,726</td>
<td align="right">954,726</td>
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
<td align="left">_CHECK_PEP_523</td>
<td align="right">422,120</td>
<td align="right">422,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">214,420</td>
<td align="right">214,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">183,840</td>
<td align="right">183,840</td>
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
<td align="right">1,841</td>
<td align="right">1,845</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">23,732</td>
<td align="right">23,719</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right">23,001</td>
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
<td align="right">2,458</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-05-03
