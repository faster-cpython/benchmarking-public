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
<td align="left">JUMP_BACKWARD</td>
<td align="right">415,446</td>
<td align="right">224,425</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,481,469</td>
<td align="right">930,360</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">8,893,125</td>
<td align="right">6,349,865</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,437,684</td>
<td align="right">6,953,131</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">14,338,248</td>
<td align="right">16,074,862</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">11,839,131</td>
<td align="right">10,473,209</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">14,326,985</td>
<td align="right">12,827,539</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">14,055,773</td>
<td align="right">12,786,424</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">38,971,131</td>
<td align="right">35,647,413</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">15,622,312</td>
<td align="right">14,468,950</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,625,694</td>
<td align="right">6,011,236</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,886,387</td>
<td align="right">1,767,899</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">35,511,436</td>
<td align="right">33,607,808</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,223,487</td>
<td align="right">1,159,813</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,522,531</td>
<td align="right">1,600,558</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,327,924</td>
<td align="right">3,167,431</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,073,347</td>
<td align="right">28,675,537</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12,003,329</td>
<td align="right">11,474,951</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">90,635,126</td>
<td align="right">86,818,879</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,997,954</td>
<td align="right">7,267,360</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">96,036,933</td>
<td align="right">92,654,689</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">14,302,412</td>
<td align="right">13,824,050</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,679,151</td>
<td align="right">5,513,735</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,493,776</td>
<td align="right">1,450,410</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">14,713,383</td>
<td align="right">14,289,909</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">960,761</td>
<td align="right">934,818</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">71,617</td>
<td align="right">69,725</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">104,860,556</td>
<td align="right">102,118,661</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">446,771,462</td>
<td align="right">435,699,321</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,849,360</td>
<td align="right">2,779,527</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,451,655</td>
<td align="right">4,345,719</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">81,802,654</td>
<td align="right">80,053,222</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">27,961,177</td>
<td align="right">27,392,584</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,680,180</td>
<td align="right">8,503,839</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">24,561,742</td>
<td align="right">24,085,421</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">23,836</td>
<td align="right">24,288</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,513,782</td>
<td align="right">2,467,435</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">325,955</td>
<td align="right">320,340</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,246,658</td>
<td align="right">37,595,172</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,486,258</td>
<td align="right">3,429,679</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,151,184</td>
<td align="right">3,101,146</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">128,647,355</td>
<td align="right">126,739,778</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">117,304,353</td>
<td align="right">115,709,350</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">80,694,840</td>
<td align="right">79,606,226</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">55,764,447</td>
<td align="right">56,457,100</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">111,213,602</td>
<td align="right">109,899,842</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,287,193</td>
<td align="right">4,242,998</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,050,908</td>
<td align="right">2,031,610</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">134,523</td>
<td align="right">133,263</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,710,590</td>
<td align="right">3,677,769</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,016,178</td>
<td align="right">11,916,996</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">116,366,721</td>
<td align="right">117,244,946</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">1,214,462</td>
<td align="right">1,205,339</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">9,638,952</td>
<td align="right">9,569,518</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">4,620,130</td>
<td align="right">4,590,526</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,371,546</td>
<td align="right">6,411,855</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">115,142</td>
<td align="right">114,460</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">31,199,200</td>
<td align="right">31,343,687</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">449,955</td>
<td align="right">451,776</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,198,369</td>
<td align="right">1,203,121</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,386,969</td>
<td align="right">1,382,013</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">5,321,303</td>
<td align="right">5,304,541</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,674,239</td>
<td align="right">18,618,542</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">673,262</td>
<td align="right">671,324</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">605,798</td>
<td align="right">604,313</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,220,244</td>
<td align="right">4,211,152</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,789,123</td>
<td align="right">20,747,315</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,001,646</td>
<td align="right">2,005,583</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">544,878</td>
<td align="right">543,890</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">549,732</td>
<td align="right">548,757</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">67,305,493</td>
<td align="right">67,194,529</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,872,326</td>
<td align="right">2,876,810</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">61,421,629</td>
<td align="right">61,334,111</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">10,930,695</td>
<td align="right">10,945,273</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,317,256</td>
<td align="right">2,314,243</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,284,290</td>
<td align="right">1,282,736</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,536,244</td>
<td align="right">1,538,065</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">5,937,617</td>
<td align="right">5,930,617</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,348,241</td>
<td align="right">3,344,364</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">42,719,883</td>
<td align="right">42,768,684</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">753,072</td>
<td align="right">753,852</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,625,443</td>
<td align="right">7,633,306</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">543,029</td>
<td align="right">543,555</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,989,836</td>
<td align="right">2,987,170</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,497,737</td>
<td align="right">1,496,425</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">129,991,130</td>
<td align="right">129,882,371</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,251,629</td>
<td align="right">39,283,270</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,513,801</td>
<td align="right">4,517,125</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,175,766</td>
<td align="right">1,176,523</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">4,144,181</td>
<td align="right">4,141,727</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,880,575</td>
<td align="right">9,875,194</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">24,357,827</td>
<td align="right">24,345,228</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">813,565</td>
<td align="right">813,232</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">3,282,047</td>
<td align="right">3,283,319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,457,651</td>
<td align="right">4,459,113</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,720,481</td>
<td align="right">1,721,038</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,951</td>
<td align="right">21,958</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,975,882</td>
<td align="right">5,977,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">38,368</td>
<td align="right">38,375</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,325,459</td>
<td align="right">8,324,036</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">140,101</td>
<td align="right">140,081</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">630,431</td>
<td align="right">630,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,913,513</td>
<td align="right">4,912,825</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">191,956</td>
<td align="right">191,936</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">266,451</td>
<td align="right">266,454</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">741,867</td>
<td align="right">741,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,066,761</td>
<td align="right">155,067,287</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,526,673</td>
<td align="right">39,526,673</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,864,488</td>
<td align="right">38,864,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,677,584</td>
<td align="right">22,677,584</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,288,773</td>
<td align="right">7,288,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,883,722</td>
<td align="right">5,883,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,646,559</td>
<td align="right">5,646,559</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,973,717</td>
<td align="right">2,973,717</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,908,515</td>
<td align="right">2,908,515</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,687,006</td>
<td align="right">2,687,006</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,522,465</td>
<td align="right">1,522,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,522,465</td>
<td align="right">1,522,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,477,262</td>
<td align="right">1,477,262</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,265,648</td>
<td align="right">1,265,648</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,131,337</td>
<td align="right">1,131,337</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,089,000</td>
<td align="right">1,089,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,055,894</td>
<td align="right">1,055,894</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">751,029</td>
<td align="right">751,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">482,628</td>
<td align="right">482,628</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">472,489</td>
<td align="right">472,489</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">341,498</td>
<td align="right">341,498</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,769</td>
<td align="right">296,769</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">254,220</td>
<td align="right">254,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">243,703</td>
<td align="right">243,703</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">219,438</td>
<td align="right">219,438</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">162,506</td>
<td align="right">162,506</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">158,405</td>
<td align="right">158,405</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">151,664</td>
<td align="right">151,664</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">146,469</td>
<td align="right">146,469</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">136,443</td>
<td align="right">136,443</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">129,127</td>
<td align="right">129,127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">117,056</td>
<td align="right">117,056</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">84,414</td>
<td align="right">84,414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">76,798</td>
<td align="right">76,798</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,860</td>
<td align="right">35,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">32,107</td>
<td align="right">32,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">28,799</td>
<td align="right">28,799</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,977</td>
<td align="right">25,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">20,885</td>
<td align="right">20,885</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20,197</td>
<td align="right">20,197</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,384</td>
<td align="right">16,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">15,139</td>
<td align="right">15,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">12,210</td>
<td align="right">12,210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,663</td>
<td align="right">10,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,205</td>
<td align="right">9,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,706</td>
<td align="right">8,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,559</td>
<td align="right">8,559</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4,541</td>
<td align="right">4,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">3,213</td>
<td align="right">3,213</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,081</td>
<td align="right">3,081</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,908</td>
<td align="right">2,908</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,240</td>
<td align="right">2,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,091</td>
<td align="right">2,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1,344</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">346</td>
<td align="right">346</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">302</td>
<td align="right">302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">259</td>
<td align="right">259</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">143</td>
<td align="right">143</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">117</td>
<td align="right">117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">115</td>
<td align="right">115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">10</td>
<td align="right">10</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">9</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">7</td>
<td align="right">7</td>
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
<td align="right">6,362,308</td>
<td align="right">37.0%</td>
<td align="right">6,402,625</td>
<td align="right">37.1%</td>
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
<td align="right">10,829,404</td>
<td align="right">63.0%</td>
<td align="right">10,829,404</td>
<td align="right">62.8%</td>
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
<td align="right">8,649</td>
<td align="right">100.0%</td>
<td align="right">8,641</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">floor divide</td>
<td align="right">121</td>
<td align="right">1.4%</td>
<td align="right">134</td>
<td align="right">1.6%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,006</td>
<td align="right">34.8%</td>
<td align="right">2,985</td>
<td align="right">34.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,376</td>
<td align="right">27.5%</td>
<td align="right">2,376</td>
<td align="right">27.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,492</td>
<td align="right">17.3%</td>
<td align="right">1,492</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">844</td>
<td align="right">9.8%</td>
<td align="right">844</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">251</td>
<td align="right">2.9%</td>
<td align="right">251</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">2.6%</td>
<td align="right">229</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">184</td>
<td align="right">2.1%</td>
<td align="right">184</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">66</td>
<td align="right">0.8%</td>
<td align="right">66</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.8%</td>
<td align="right">66</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8</td>
<td align="right">0.1%</td>
<td align="right">8</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
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
<td align="right">2,050,908</td>
<td align="right">100.0%</td>
<td align="right">2,031,610</td>
<td align="right">100.0%</td>
<td align="right">-0.9%</td>
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
<td align="right">3,341,108</td>
<td align="right">8.8%</td>
<td align="right">3,337,231</td>
<td align="right">8.7%</td>
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
<td align="right">2,363,147</td>
<td align="right">6.2%</td>
<td align="right">2,363,041</td>
<td align="right">6.2%</td>
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
<td align="right">32,467,765</td>
<td align="right">85.0%</td>
<td align="right">32,467,750</td>
<td align="right">85.0%</td>
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
<td align="right">45,676</td>
<td align="right">88.6%</td>
<td align="right">45,674</td>
<td align="right">88.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,900</td>
<td align="right">11.4%</td>
<td align="right">5,900</td>
<td align="right">11.4%</td>
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
<td align="left">string slice</td>
<td align="right">1,270</td>
<td align="right">21.5%</td>
<td align="right">1,271</td>
<td align="right">21.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,974</td>
<td align="right">50.4%</td>
<td align="right">2,973</td>
<td align="right">50.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">775</td>
<td align="right">13.1%</td>
<td align="right">775</td>
<td align="right">13.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">307</td>
<td align="right">5.2%</td>
<td align="right">307</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">245</td>
<td align="right">4.2%</td>
<td align="right">245</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">238</td>
<td align="right">4.0%</td>
<td align="right">238</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">91</td>
<td align="right">1.5%</td>
<td align="right">91</td>
<td align="right">1.5%</td>
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
<td align="right">1,801,066</td>
<td align="right">0.7%</td>
<td align="right">1,794,841</td>
<td align="right">0.7%</td>
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
<td align="right">14,174</td>
<td align="right">0.0%</td>
<td align="right">14,178</td>
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
<td align="right">239,411,460</td>
<td align="right">99.2%</td>
<td align="right">239,419,294</td>
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
<td align="left">Success</td>
<td align="right">59,721</td>
<td align="right">100.0%</td>
<td align="right">59,606</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
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
<td align="left">init not simple</td>
<td align="right">424</td>
<td align="right">424 / 0 !!</td>
<td align="right">424</td>
<td align="right">424 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">24</td>
<td align="right">24 / 0 !!</td>
<td align="right">24</td>
<td align="right">24 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3</td>
<td align="right">3 / 0 !!</td>
<td align="right">3</td>
<td align="right">3 / 0 !!</td>
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
<td align="right">336</td>
<td align="right">15.6%</td>
<td align="right">336</td>
<td align="right">15.6%</td>
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
<td align="right">64</td>
<td align="right">3.0%</td>
<td align="right">64</td>
<td align="right">3.0%</td>
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
<td align="right">626,551</td>
<td align="right">5.4%</td>
<td align="right">626,627</td>
<td align="right">5.4%</td>
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
<td align="right">10,925,783</td>
<td align="right">94.5%</td>
<td align="right">10,925,783</td>
<td align="right">94.5%</td>
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
<td align="right">7,941</td>
<td align="right">0.1%</td>
<td align="right">7,941</td>
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
<td align="right">2,660</td>
<td align="right">66.4%</td>
<td align="right">2,673</td>
<td align="right">66.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,349</td>
<td align="right">33.6%</td>
<td align="right">1,349</td>
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
<td align="left">big int</td>
<td align="right">99</td>
<td align="right">3.7%</td>
<td align="right">112</td>
<td align="right">4.2%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,823</td>
<td align="right">68.5%</td>
<td align="right">1,823</td>
<td align="right">68.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">258</td>
<td align="right">9.7%</td>
<td align="right">258</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">256</td>
<td align="right">9.6%</td>
<td align="right">256</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">157</td>
<td align="right">5.9%</td>
<td align="right">157</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">23</td>
<td align="right">0.9%</td>
<td align="right">23</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">3,481,025</td>
<td align="right">22.9%</td>
<td align="right">3,424,467</td>
<td align="right">22.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,731,432</td>
<td align="right">77.1%</td>
<td align="right">11,731,432</td>
<td align="right">77.4%</td>
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
<td align="right">4,705</td>
<td align="right">100.0%</td>
<td align="right">4,684</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">tuple</td>
<td align="right">1,443</td>
<td align="right">30.7%</td>
<td align="right">1,422</td>
<td align="right">30.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,972</td>
<td align="right">41.9%</td>
<td align="right">1,972</td>
<td align="right">42.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">733</td>
<td align="right">15.6%</td>
<td align="right">733</td>
<td align="right">15.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">557</td>
<td align="right">11.8%</td>
<td align="right">557</td>
<td align="right">11.9%</td>
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
<td align="right">2,331,427</td>
<td align="right">3.0%</td>
<td align="right">2,739,603</td>
<td align="right">3.5%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,324,097</td>
<td align="right">4.3%</td>
<td align="right">3,163,605</td>
<td align="right">4.1%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">71,445,768</td>
<td align="right">92.7%</td>
<td align="right">71,691,280</td>
<td align="right">92.4%</td>
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
<td align="right">44,626</td>
<td align="right">93.3%</td>
<td align="right">52,320</td>
<td align="right">94.3%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,191</td>
<td align="right">6.7%</td>
<td align="right">3,190</td>
<td align="right">5.7%</td>
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
<td align="left">zip</td>
<td align="right">220</td>
<td align="right">6.9%</td>
<td align="right">239</td>
<td align="right">7.5%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,052</td>
<td align="right">33.0%</td>
<td align="right">1,027</td>
<td align="right">32.2%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">838</td>
<td align="right">26.3%</td>
<td align="right">843</td>
<td align="right">26.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">314</td>
<td align="right">9.8%</td>
<td align="right">314</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">275</td>
<td align="right">8.6%</td>
<td align="right">275</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">180</td>
<td align="right">5.6%</td>
<td align="right">180</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">142</td>
<td align="right">4.5%</td>
<td align="right">142</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">76</td>
<td align="right">2.4%</td>
<td align="right">76</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">54</td>
<td align="right">1.7%</td>
<td align="right">54</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">25</td>
<td align="right">0.8%</td>
<td align="right">25</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15</td>
<td align="right">0.5%</td>
<td align="right">15</td>
<td align="right">0.5%</td>
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
<td align="right">29,757,205</td>
<td align="right">9.8%</td>
<td align="right">28,359,527</td>
<td align="right">9.3%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">65,346,256</td>
<td align="right">21.5%</td>
<td align="right">62,750,835</td>
<td align="right">20.5%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">207,915,794</td>
<td align="right">68.5%</td>
<td align="right">213,966,180</td>
<td align="right">70.1%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">64,389</td>
<td align="right">0.0%</td>
<td align="right">64,389</td>
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
<td align="right">9,390</td>
<td align="right">0.6%</td>
<td align="right">9,024</td>
<td align="right">0.6%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,537,885</td>
<td align="right">99.4%</td>
<td align="right">1,489,185</td>
<td align="right">99.4%</td>
<td align="right">-3.2%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">2,023</td>
<td align="right">21.5%</td>
<td align="right">1,656</td>
<td align="right">18.4%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">279</td>
<td align="right">3.0%</td>
<td align="right">280</td>
<td align="right">3.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,965</td>
<td align="right">31.6%</td>
<td align="right">2,965</td>
<td align="right">32.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,049</td>
<td align="right">11.2%</td>
<td align="right">1,049</td>
<td align="right">11.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">993</td>
<td align="right">10.6%</td>
<td align="right">993</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">645</td>
<td align="right">6.9%</td>
<td align="right">645</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">530</td>
<td align="right">5.6%</td>
<td align="right">530</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">115</td>
<td align="right">1.2%</td>
<td align="right">115</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">70</td>
<td align="right">0.7%</td>
<td align="right">70</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">69</td>
<td align="right">0.7%</td>
<td align="right">69</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6</td>
<td align="right">0.1%</td>
<td align="right">6</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">166,270,044</td>
<td align="right">100.0%</td>
<td align="right">163,440,631</td>
<td align="right">100.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,998</td>
<td align="right">0.0%</td>
<td align="right">3,002</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">57</td>
<td align="right">0.0%</td>
<td align="right">57</td>
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
<td align="right">12,141</td>
<td align="right">0.0%</td>
<td align="right">12,141</td>
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
<td align="right">19,380</td>
<td align="right">100.0%</td>
<td align="right">19,383</td>
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
<td align="right">50</td>
<td align="right">0.0%</td>
<td align="right">50</td>
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
<td align="right">424,859</td>
<td align="right">99.9%</td>
<td align="right">424,859</td>
<td align="right">99.9%</td>
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
<td align="right">209</td>
<td align="right">100.0%</td>
<td align="right">209</td>
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
<td align="right">4,490</td>
<td align="right">29.2%</td>
<td align="right">4,490</td>
<td align="right">29.2%</td>
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
<td align="right">10,810</td>
<td align="right">70.4%</td>
<td align="right">10,810</td>
<td align="right">70.4%</td>
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
<td align="right">4</td>
<td align="right">7.8%</td>
<td align="right">4</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">47</td>
<td align="right">92.2%</td>
<td align="right">47</td>
<td align="right">92.2%</td>
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
<td align="right">47</td>
<td align="right">100.0%</td>
<td align="right">47</td>
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
<td align="right">8,665,569</td>
<td align="right">26.8%</td>
<td align="right">8,489,273</td>
<td align="right">26.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,550,851</td>
<td align="right">29.5%</td>
<td align="right">9,522,504</td>
<td align="right">29.7%</td>
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
<td align="right">14,098,376</td>
<td align="right">43.6%</td>
<td align="right">14,079,618</td>
<td align="right">43.9%</td>
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
<td align="right">9,462</td>
<td align="right">4.9%</td>
<td align="right">9,417</td>
<td align="right">4.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">184,869</td>
<td align="right">95.1%</td>
<td align="right">184,324</td>
<td align="right">95.1%</td>
<td align="right">-0.3%</td>
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
<td align="right">4,736</td>
<td align="right">50.1%</td>
<td align="right">4,691</td>
<td align="right">49.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,626</td>
<td align="right">27.8%</td>
<td align="right">2,626</td>
<td align="right">27.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">989</td>
<td align="right">10.5%</td>
<td align="right">989</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">643</td>
<td align="right">6.8%</td>
<td align="right">643</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">308</td>
<td align="right">3.3%</td>
<td align="right">308</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">1.0%</td>
<td align="right">94</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">53</td>
<td align="right">0.6%</td>
<td align="right">53</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8</td>
<td align="right">0.1%</td>
<td align="right">8</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">115,142</td>
<td align="right">100.0%</td>
<td align="right">114,460</td>
<td align="right">100.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">1,477,524</td>
<td align="right">13.9%</td>
<td align="right">926,544</td>
<td align="right">9.2%</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,156,354</td>
<td align="right">86.1%</td>
<td align="right">9,156,354</td>
<td align="right">90.8%</td>
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
<td align="right">3,471</td>
<td align="right">88.0%</td>
<td align="right">3,342</td>
<td align="right">87.6%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">474</td>
<td align="right">12.0%</td>
<td align="right">474</td>
<td align="right">12.4%</td>
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
<td align="right">341</td>
<td align="right">9.8%</td>
<td align="right">212</td>
<td align="right">6.3%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,960</td>
<td align="right">85.3%</td>
<td align="right">2,960</td>
<td align="right">88.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">113</td>
<td align="right">3.3%</td>
<td align="right">113</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">47</td>
<td align="right">1.4%</td>
<td align="right">47</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">10</td>
<td align="right">0.3%</td>
<td align="right">10</td>
<td align="right">0.3%</td>
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
<td align="right">3,791,731</td>
<td align="right">2.1%</td>
<td align="right">3,683,007</td>
<td align="right">2.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11,908,585</td>
<td align="right">6.5%</td>
<td align="right">11,812,160</td>
<td align="right">6.4%</td>
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
<td align="right">168,667,386</td>
<td align="right">91.4%</td>
<td align="right">168,527,688</td>
<td align="right">91.5%</td>
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
<td align="right">75,455</td>
<td align="right">42.1%</td>
<td align="right">73,427</td>
<td align="right">42.1%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">103,624</td>
<td align="right">57.9%</td>
<td align="right">100,847</td>
<td align="right">57.9%</td>
<td align="right">-2.7%</td>
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
<td align="left">number</td>
<td align="right">90,029</td>
<td align="right">86.9%</td>
<td align="right">87,253</td>
<td align="right">86.5%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,160</td>
<td align="right">2.1%</td>
<td align="right">2,159</td>
<td align="right">2.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,949</td>
<td align="right">9.6%</td>
<td align="right">9,949</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,073</td>
<td align="right">1.0%</td>
<td align="right">1,073</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">213</td>
<td align="right">0.2%</td>
<td align="right">213</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">107</td>
<td align="right">0.1%</td>
<td align="right">107</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">93</td>
<td align="right">0.1%</td>
<td align="right">93</td>
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
<td align="right">296,270</td>
<td align="right">2.0%</td>
<td align="right">296,270</td>
<td align="right">2.0%</td>
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
<td align="right">14,605,532</td>
<td align="right">98.0%</td>
<td align="right">14,605,532</td>
<td align="right">98.0%</td>
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
<td align="right">402</td>
<td align="right">80.6%</td>
<td align="right">402</td>
<td align="right">80.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97</td>
<td align="right">19.4%</td>
<td align="right">97</td>
<td align="right">19.4%</td>
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
<td align="right">74</td>
<td align="right">76.3%</td>
<td align="right">74</td>
<td align="right">76.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">23</td>
<td align="right">23.7%</td>
<td align="right">23</td>
<td align="right">23.7%</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">71,945,603</td>
<td align="right">2.7%</td>
<td align="right">69,520,644</td>
<td align="right">2.6%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">85,209,133</td>
<td align="right">3.2%</td>
<td align="right">82,878,418</td>
<td align="right">3.1%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,589,358,047</td>
<td align="right">58.9%</td>
<td align="right">1,560,786,230</td>
<td align="right">58.9%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">950,381,461</td>
<td align="right">35.2%</td>
<td align="right">937,709,409</td>
<td align="right">35.4%</td>
<td align="right">-1.3%</td>
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
<td align="right">1,477,524</td>
<td align="right">2.1%</td>
<td align="right">926,544</td>
<td align="right">1.3%</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,324,097</td>
<td align="right">4.7%</td>
<td align="right">3,163,605</td>
<td align="right">4.6%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">29,757,205</td>
<td align="right">41.7%</td>
<td align="right">28,359,527</td>
<td align="right">41.1%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,665,569</td>
<td align="right">12.1%</td>
<td align="right">8,489,273</td>
<td align="right">12.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,481,025</td>
<td align="right">4.9%</td>
<td align="right">3,424,467</td>
<td align="right">5.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,050,908</td>
<td align="right">2.9%</td>
<td align="right">2,031,610</td>
<td align="right">2.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">11,908,585</td>
<td align="right">16.7%</td>
<td align="right">11,812,160</td>
<td align="right">17.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,362,308</td>
<td align="right">8.9%</td>
<td align="right">6,402,625</td>
<td align="right">9.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,341,108</td>
<td align="right">4.7%</td>
<td align="right">3,337,231</td>
<td align="right">4.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">626,551</td>
<td align="right">0.9%</td>
<td align="right">626,627</td>
<td align="right">0.9%</td>
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
<td align="right">4,836,384</td>
<td align="right">5.7%</td>
<td align="right">3,518,999</td>
<td align="right">4.2%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,164,916</td>
<td align="right">1.4%</td>
<td align="right">1,369,711</td>
<td align="right">1.7%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,166,511</td>
<td align="right">1.4%</td>
<td align="right">1,369,892</td>
<td align="right">1.7%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">8,492,602</td>
<td align="right">10.0%</td>
<td align="right">9,636,819</td>
<td align="right">11.6%</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">10,595,265</td>
<td align="right">12.4%</td>
<td align="right">9,458,259</td>
<td align="right">11.4%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">31,441,885</td>
<td align="right">36.9%</td>
<td align="right">30,066,235</td>
<td align="right">36.3%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,078,699</td>
<td align="right">3.6%</td>
<td align="right">2,981,549</td>
<td align="right">3.6%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,448,018</td>
<td align="right">11.1%</td>
<td align="right">9,548,630</td>
<td align="right">11.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,509,605</td>
<td align="right">11.2%</td>
<td align="right">9,484,726</td>
<td align="right">11.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,338,581</td>
<td align="right">2.7%</td>
<td align="right">2,338,475</td>
<td align="right">2.8%</td>
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
<td align="right">18,708,020</td>
<td align="right">8.5%</td>
<td align="right">18,057,060</td>
<td align="right">8.2%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,781,048</td>
<td align="right">18.1%</td>
<td align="right">39,129,562</td>
<td align="right">17.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,782,771</td>
<td align="right">18.1%</td>
<td align="right">39,131,285</td>
<td align="right">17.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,650,501</td>
<td align="right">18.5%</td>
<td align="right">40,000,836</td>
<td align="right">18.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,650,501</td>
<td align="right">18.5%</td>
<td align="right">40,000,836</td>
<td align="right">18.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">178,753,024</td>
<td align="right">81.5%</td>
<td align="right">179,404,510</td>
<td align="right">81.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">867,730</td>
<td align="right">0.4%</td>
<td align="right">869,551</td>
<td align="right">0.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">7,047,752</td>
<td align="right">3.2%</td>
<td align="right">7,049,779</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,049,019</td>
<td align="right">72.0%</td>
<td align="right">158,049,545</td>
<td align="right">72.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">379</td>
<td align="right">0.0%</td>
<td align="right">379</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">10,484,588</td>
<td align="right">4.8%</td>
<td align="right">10,484,588</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">502,497</td>
<td align="right">0.2%</td>
<td align="right">502,497</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">88</td>
<td align="right">0.0%</td>
<td align="right">88</td>
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
<td align="left">Method cache misses</td>
<td align="right">8,203,146</td>
<td align="right"></td>
<td align="right">8,783,558</td>
<td align="right"></td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">9,334,288</td>
<td align="right"></td>
<td align="right">9,859,202</td>
<td align="right"></td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,133,566</td>
<td align="right"></td>
<td align="right">1,078,074</td>
<td align="right"></td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">287,844,078</td>
<td align="right">7.3%</td>
<td align="right">281,595,464</td>
<td align="right">7.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,504,807,366</td>
<td align="right">34.4%</td>
<td align="right">1,531,818,389</td>
<td align="right">35.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,650,845,939</td>
<td align="right">41.9%</td>
<td align="right">1,678,822,559</td>
<td align="right">42.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">438,415,181</td>
<td align="right">10.0%</td>
<td align="right">431,843,560</td>
<td align="right">9.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,189,809,553</td>
<td align="right">30.2%</td>
<td align="right">1,173,089,222</td>
<td align="right">29.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,586,615,672</td>
<td align="right">36.3%</td>
<td align="right">1,571,463,495</td>
<td align="right">35.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,584,050</td>
<td align="right">0.5%</td>
<td align="right">1,597,619</td>
<td align="right">0.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">201,087,042</td>
<td align="right"></td>
<td align="right">199,474,490</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">815,155,426</td>
<td align="right">20.7%</td>
<td align="right">820,303,522</td>
<td align="right">20.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">155,943,114</td>
<td align="right"></td>
<td align="right">155,267,877</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">251,680,604</td>
<td align="right"></td>
<td align="right">252,182,443</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">62,031</td>
<td align="right">0.0%</td>
<td align="right">62,154</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">840,245,926</td>
<td align="right">19.2%</td>
<td align="right">841,094,250</td>
<td align="right">19.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">242,423,009</td>
<td align="right">74.3%</td>
<td align="right">242,479,405</td>
<td align="right">74.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">240,776,928</td>
<td align="right">73.8%</td>
<td align="right">240,819,632</td>
<td align="right">73.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">83,851,233</td>
<td align="right"></td>
<td align="right">83,849,123</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">83,866,942</td>
<td align="right">25.7%</td>
<td align="right">83,866,699</td>
<td align="right">25.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,079,690</td>
<td align="right"></td>
<td align="right">3,079,690</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">997,148</td>
<td align="right">32.4%</td>
<td align="right">997,148</td>
<td align="right">32.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">98,881</td>
<td align="right">3.2%</td>
<td align="right">98,881</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
<td align="right">1,344</td>
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
<td align="right">6,278</td>
<td align="right">12,276,198</td>
<td align="right">371,829,163</td>
<td align="right">6,238</td>
<td align="right">12,514,013</td>
<td align="right">372,682,029</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">34</td>
<td align="right">0.0%</td>
<td align="right">10</td>
<td align="right">0.0%</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">3,554</td>
<td align="right">1.1%</td>
<td align="right">2,977</td>
<td align="right">0.9%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">100,844</td>
<td align="right">30.4%</td>
<td align="right">109,696</td>
<td align="right">31.8%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,341</td>
<td align="right">0.4%</td>
<td align="right">1,232</td>
<td align="right">0.4%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">135,450</td>
<td align="right">40.8%</td>
<td align="right">144,912</td>
<td align="right">42.0%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">3,898,068,513</td>
<td align="right">970.2%</td>
<td align="right">4,090,600,410</td>
<td align="right">999.3%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">331,864</td>
<td align="right"></td>
<td align="right">345,265</td>
<td align="right"></td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">231,020</td>
<td align="right">69.6%</td>
<td align="right">235,569</td>
<td align="right">68.2%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">401,798,982</td>
<td align="right"></td>
<td align="right">409,337,303</td>
<td align="right"></td>
<td align="right">1.9%</td>
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
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">149</td>
<td align="right">0.0%</td>
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
<td align="right">222,450</td>
<td align="right">96.3%</td>
<td align="right">235,513</td>
<td align="right">100.0%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">231,020</td>
<td align="right"></td>
<td align="right">235,569</td>
<td align="right"></td>
<td align="right">2.0%</td>
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
<td align="right">56</td>
<td align="right">0.0%</td>
<td align="right">56</td>
<td align="right">0.0%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,593</td>
<td align="right">7.2%</td>
<td align="right">16,878</td>
<td align="right">7.2%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">60,018</td>
<td align="right">26.0%</td>
<td align="right">60,580</td>
<td align="right">25.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">87,171</td>
<td align="right">37.7%</td>
<td align="right">92,466</td>
<td align="right">39.3%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">50,576</td>
<td align="right">21.9%</td>
<td align="right">51,366</td>
<td align="right">21.8%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">16,317</td>
<td align="right">7.1%</td>
<td align="right">13,916</td>
<td align="right">5.9%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">345</td>
<td align="right">0.1%</td>
<td align="right">363</td>
<td align="right">0.2%</td>
<td align="right">5.2%</td>
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
<td align="right">1,704</td>
<td align="right">0.7%</td>
<td align="right">1,687</td>
<td align="right">0.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">49,742</td>
<td align="right">21.5%</td>
<td align="right">22,299</td>
<td align="right">9.5%</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">48,419</td>
<td align="right">21.0%</td>
<td align="right">74,533</td>
<td align="right">31.6%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">92,188</td>
<td align="right">39.9%</td>
<td align="right">99,567</td>
<td align="right">42.3%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">28,022</td>
<td align="right">12.1%</td>
<td align="right">33,785</td>
<td align="right">14.3%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,330</td>
<td align="right">1.0%</td>
<td align="right">3,579</td>
<td align="right">1.5%</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">45</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
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
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">904</td>
<td align="right">4,356,983</td>
<td align="right">481,867.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">904</td>
<td align="right">4,356,983</td>
<td align="right">481,867.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">188,426</td>
<td align="right">739,406</td>
<td align="right">292.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">203,209</td>
<td align="right">443,922</td>
<td align="right">118.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,992,004</td>
<td align="right">3,839,210</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">3,249,191</td>
<td align="right">6,128,647</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">76,823,595</td>
<td align="right">13,681,803</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">4,056,672</td>
<td align="right">6,599,932</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">342,433</td>
<td align="right">147,323</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">11,186,798</td>
<td align="right">5,572,117</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,860,599</td>
<td align="right">1,499,204</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">3,715,356</td>
<td align="right">4,984,705</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,116,095</td>
<td align="right">2,794,621</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">124,062</td>
<td align="right">155,465</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">5,730,562</td>
<td align="right">7,096,484</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">8,258</td>
<td align="right">10,150</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">23,984,892</td>
<td align="right">29,198,619</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">12,014</td>
<td align="right">14,621</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">50,640,433</td>
<td align="right">41,962,835</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,384,088</td>
<td align="right">1,606,944</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">5,626,686</td>
<td align="right">6,466,483</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">189,290,578</td>
<td align="right">215,266,072</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,707,524</td>
<td align="right">4,185,886</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,707,524</td>
<td align="right">4,185,886</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">21,807,033</td>
<td align="right">24,456,333</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">13,020,576</td>
<td align="right">14,555,374</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,807,849</td>
<td align="right">4,233,821</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,065,830</td>
<td align="right">1,184,318</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">4,935,859</td>
<td align="right">5,464,237</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">69,727,343</td>
<td align="right">76,982,929</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">606,489</td>
<td align="right">664,931</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">13,949,036</td>
<td align="right">15,283,105</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">18,207,607</td>
<td align="right">19,762,747</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">4,534,846</td>
<td align="right">4,912,262</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">6,615,973</td>
<td align="right">7,140,717</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">27,068,250</td>
<td align="right">29,186,280</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">18,063</td>
<td align="right">19,375</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">69,112</td>
<td align="right">64,360</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">27,178,162</td>
<td align="right">28,905,969</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">10,356,097</td>
<td align="right">10,953,549</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">994,288</td>
<td align="right">1,050,846</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">63,350</td>
<td align="right">60,026</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">27,971,388</td>
<td align="right">29,410,525</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">71,512,925</td>
<td align="right">67,953,639</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,414,467</td>
<td align="right">1,484,300</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">55,148,381</td>
<td align="right">57,849,457</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,986,941</td>
<td align="right">12,555,538</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">29,633,574</td>
<td align="right">30,965,298</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">758,306</td>
<td align="right">791,127</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">11,785,966</td>
<td align="right">11,280,534</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">81,541,875</td>
<td align="right">84,914,959</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">125,406</td>
<td align="right">130,445</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">125,406</td>
<td align="right">130,445</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">75,123,867</td>
<td align="right">72,240,397</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">50,861,890</td>
<td align="right">52,769,612</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">45,456,066</td>
<td align="right">47,114,386</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,575,869</td>
<td align="right">1,633,348</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">155,283</td>
<td align="right">160,898</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">155,283</td>
<td align="right">160,898</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">226,040,153</td>
<td align="right">233,687,691</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">930,174</td>
<td align="right">960,824</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">40,052,008</td>
<td align="right">41,352,693</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,469,892</td>
<td align="right">15,949,964</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">122,245</td>
<td align="right">125,890</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,306,279</td>
<td align="right">2,369,953</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">121,169,437</td>
<td align="right">124,480,235</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">309,787,637</td>
<td align="right">317,940,993</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">15,107,364</td>
<td align="right">15,503,838</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">736,477</td>
<td align="right">755,775</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">57,226</td>
<td align="right">58,716</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,938,103</td>
<td align="right">1,988,141</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">26,284,693</td>
<td align="right">26,957,800</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">3,120,997</td>
<td align="right">3,042,970</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">3,120,997</td>
<td align="right">3,042,970</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">26,351,032</td>
<td align="right">27,005,082</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">39,274,342</td>
<td align="right">40,197,943</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">95,817,912</td>
<td align="right">98,055,247</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">324,405,503</td>
<td align="right">331,815,334</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">3,089,437</td>
<td align="right">3,159,642</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">1,075,617</td>
<td align="right">1,100,035</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,714,961</td>
<td align="right">2,775,441</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">34,151,017</td>
<td align="right">33,458,364</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">3,664,284</td>
<td align="right">3,736,778</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,947,058</td>
<td align="right">12,700,153</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">401,798,982</td>
<td align="right">409,337,303</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">321,789</td>
<td align="right">327,586</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">82,668</td>
<td align="right">81,206</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">4,899,170</td>
<td align="right">4,983,867</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">413,584,948</td>
<td align="right">420,617,837</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">44,319,872</td>
<td align="right">43,593,100</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,539,697</td>
<td align="right">6,645,633</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">302,523</td>
<td align="right">307,376</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">43,103</td>
<td align="right">43,791</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,562,996</td>
<td align="right">8,689,510</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">7,429,115</td>
<td align="right">7,537,658</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">29,976,132</td>
<td align="right">29,547,445</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,878,449</td>
<td align="right">2,838,208</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">354,599</td>
<td align="right">359,555</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">805,859</td>
<td align="right">814,982</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">806,428</td>
<td align="right">815,551</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,055,231</td>
<td align="right">9,154,962</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">5,104,288</td>
<td align="right">5,159,985</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">66,837,234</td>
<td align="right">66,181,707</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">387,066</td>
<td align="right">383,448</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">809,830</td>
<td align="right">816,830</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">81,098</td>
<td align="right">81,780</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">13,816,066</td>
<td align="right">13,932,116</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">969,321</td>
<td align="right">976,828</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">684,944</td>
<td align="right">679,711</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">684,944</td>
<td align="right">679,711</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">74,692</td>
<td align="right">74,135</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">61,501</td>
<td align="right">61,049</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">559,008</td>
<td align="right">563,004</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">48,227</td>
<td align="right">48,558</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,452,019</td>
<td align="right">1,461,831</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,809,394</td>
<td align="right">7,860,938</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">78,992,945</td>
<td align="right">79,486,982</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,891,995</td>
<td align="right">2,909,498</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">19,729,250</td>
<td align="right">19,840,214</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,606,018</td>
<td align="right">1,614,972</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">178,992</td>
<td align="right">179,967</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">8,517,481</td>
<td align="right">8,563,828</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">3,106,327</td>
<td align="right">3,123,089</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">225,917</td>
<td align="right">226,977</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">179,322</td>
<td align="right">178,565</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">242,427</td>
<td align="right">243,379</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,025,131</td>
<td align="right">2,017,268</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">5,133,692</td>
<td align="right">5,115,417</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,274,999</td>
<td align="right">1,271,062</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,558,595</td>
<td align="right">5,544,017</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,506,549</td>
<td align="right">1,502,864</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">577,796</td>
<td align="right">576,518</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">814,033</td>
<td align="right">815,518</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,479,097</td>
<td align="right">2,483,595</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,726</td>
<td align="right">1,723</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">50,680,966</td>
<td align="right">50,600,673</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,553,787</td>
<td align="right">1,556,241</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">38,457,278</td>
<td align="right">38,397,087</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">21,767,395</td>
<td align="right">21,735,754</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">73,302,594</td>
<td align="right">73,200,114</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">73,243,197</td>
<td align="right">73,140,825</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">83,080</td>
<td align="right">82,969</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,811,457</td>
<td align="right">4,806,823</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">5,520,001</td>
<td align="right">5,515,131</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,696,636</td>
<td align="right">1,697,896</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,696,636</td>
<td align="right">1,697,896</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,687,405</td>
<td align="right">2,689,343</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,748,475</td>
<td align="right">2,749,898</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">41,341,817</td>
<td align="right">41,352,693</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">10,720,785</td>
<td align="right">10,720,266</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">458,845</td>
<td align="right">458,865</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">508,213</td>
<td align="right">508,233</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">3,058,612</td>
<td align="right">3,058,612</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">2,287,448</td>
<td align="right">2,287,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,705,429</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">1,482,938</td>
<td align="right">1,482,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,466,784</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">82,615</td>
<td align="right">82,615</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">65,111</td>
<td align="right">65,111</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">38,288</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">36,304</td>
<td align="right">36,304</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">33,140</td>
<td align="right">33,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,507</td>
<td align="right">29,507</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,507</td>
<td align="right">29,507</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">29,298</td>
<td align="right">29,298</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">28,553</td>
<td align="right">28,553</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">19,984</td>
<td align="right">19,984</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,223</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">16,930</td>
<td align="right">16,930</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">14,961</td>
<td align="right">14,961</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">14,961</td>
<td align="right">14,961</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">13,144</td>
<td align="right">13,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">11,589</td>
<td align="right">11,589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">11,403</td>
<td align="right">11,403</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">11,004</td>
<td align="right">11,004</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">10,270</td>
<td align="right">10,270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">9,006</td>
<td align="right">9,006</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">7,214</td>
<td align="right">7,214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">5,230</td>
<td align="right">5,230</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">3,844</td>
<td align="right">3,844</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">3,071</td>
<td align="right">3,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,638</td>
<td align="right">2,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_WITH_SPEC</td>
<td align="right">2,417</td>
<td align="right">2,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">2,327</td>
<td align="right">2,327</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">1,886</td>
<td align="right">1,886</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,481</td>
<td align="right">1,481</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">1,334</td>
<td align="right">1,334</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,282</td>
<td align="right">1,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,282</td>
<td align="right">1,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">608</td>
<td align="right">608</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">184</td>
<td align="right">184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">147</td>
<td align="right">147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">147</td>
<td align="right">147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">42</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">7</td>
<td align="right">7</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">77,029,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right"></td>
<td align="right">64,331,406</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">6,700,581</td>
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
<td align="left">CALL</td>
<td align="right">1,283</td>
<td align="right">1,221</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">4,591</td>
<td align="right">4,497</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">127</td>
<td align="right">127</td>
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
<td align="right">23</td>
<td align="right">23</td>
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
<td align="right">24</td>
<td align="right">24</td>
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
<td align="right">8</td>
<td align="right">8</td>
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
<td align="right">8</td>
<td align="right">8</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-18
