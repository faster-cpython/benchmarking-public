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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">14,068,760</td>
<td align="right">31,411,482</td>
<td align="right">123.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">19,469,773</td>
<td align="right">39,951,185</td>
<td align="right">105.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">20,916,735</td>
<td align="right">38,283,452</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">44,361,604</td>
<td align="right">69,618,983</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,723,472</td>
<td align="right">2,690,544</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">58,934,580</td>
<td align="right">89,861,240</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">50,511,758</td>
<td align="right">75,395,001</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">88,776,620</td>
<td align="right">47,495,499</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">33,858,466</td>
<td align="right">49,110,656</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">55,038,304</td>
<td align="right">72,019,757</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,812,694</td>
<td align="right">11,599,799</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">125,738,397</td>
<td align="right">148,049,337</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">472,811</td>
<td align="right">556,221</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">109,794,578</td>
<td align="right">127,915,061</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">210,694</td>
<td align="right">178,473</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">576,042</td>
<td align="right">658,906</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">5,354,193</td>
<td align="right">6,123,640</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">13,283</td>
<td align="right">11,414</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">45,476,766</td>
<td align="right">51,699,750</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,666,925</td>
<td align="right">2,978,408</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">111,860,248</td>
<td align="right">124,810,337</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,921,051</td>
<td align="right">3,227,098</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">87,425,613</td>
<td align="right">95,906,370</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">577,274,769</td>
<td align="right">629,343,472</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,446,335</td>
<td align="right">2,661,460</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">10,117,543</td>
<td align="right">10,970,612</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">11,230,830</td>
<td align="right">12,103,746</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,639,315</td>
<td align="right">9,210,327</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,710,834</td>
<td align="right">4,950,938</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">167,042,596</td>
<td align="right">175,545,092</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,279,733</td>
<td align="right">2,387,030</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,357,954</td>
<td align="right">4,552,603</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">36,034,721</td>
<td align="right">37,553,212</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,543,663</td>
<td align="right">13,017,737</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">46,710,721</td>
<td align="right">48,464,329</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">462,001</td>
<td align="right">479,242</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,512,259</td>
<td align="right">1,566,018</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,747,096</td>
<td align="right">11,089,403</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">52,554,051</td>
<td align="right">54,169,964</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">9,981,602</td>
<td align="right">10,273,131</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">14,089,785</td>
<td align="right">14,494,307</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,685,309</td>
<td align="right">3,782,839</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,084,992</td>
<td align="right">4,187,221</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,311,922</td>
<td align="right">1,279,701</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,338,446</td>
<td align="right">1,369,335</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">118,532,723</td>
<td align="right">121,248,557</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,777,248</td>
<td align="right">3,860,680</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,366,266</td>
<td align="right">17,662,794</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">20,509,101</td>
<td align="right">20,850,292</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">16,892,328</td>
<td align="right">17,156,534</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,899,436</td>
<td align="right">1,871,780</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">162,640,915</td>
<td align="right">164,910,293</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,248,238</td>
<td align="right">1,265,479</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,334,128</td>
<td align="right">1,351,999</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">138,387,855</td>
<td align="right">140,216,334</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">30,180,138</td>
<td align="right">30,559,158</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,885,052</td>
<td align="right">2,913,901</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">9,459,634</td>
<td align="right">9,541,465</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">85,695,296</td>
<td align="right">86,436,280</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,286,440</td>
<td align="right">3,314,422</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">18,221,596</td>
<td align="right">18,376,384</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">16,287,869</td>
<td align="right">16,421,804</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">24,546,542</td>
<td align="right">24,747,035</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">8,260,282</td>
<td align="right">8,327,366</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,631,363</td>
<td align="right">4,660,852</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,575,461</td>
<td align="right">5,609,954</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,687,064</td>
<td align="right">1,697,102</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">135,787,883</td>
<td align="right">136,561,708</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,385,749</td>
<td align="right">1,393,645</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,736,118</td>
<td align="right">2,750,651</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,521,072</td>
<td align="right">4,538,313</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">17,668,510</td>
<td align="right">17,722,264</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,645,786</td>
<td align="right">6,665,862</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,206,073</td>
<td align="right">5,220,258</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,346,290</td>
<td align="right">4,356,100</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">49,887,224</td>
<td align="right">49,996,626</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,296,990</td>
<td align="right">17,327,183</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">73,913,640</td>
<td align="right">74,037,817</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,101,778</td>
<td align="right">1,103,544</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">9,990,510</td>
<td align="right">10,006,491</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">28,117,330</td>
<td align="right">28,139,013</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,943,083</td>
<td align="right">12,948,039</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">640,647</td>
<td align="right">640,556</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">767,551</td>
<td align="right">767,464</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,973</td>
<td align="right">21,975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">38,321</td>
<td align="right">38,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">53,927</td>
<td align="right">53,928</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,160,733</td>
<td align="right">8,160,652</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,115,045</td>
<td align="right">155,115,045</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,528,150</td>
<td align="right">39,528,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,864,488</td>
<td align="right">38,864,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,085,417</td>
<td align="right">38,085,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,677,579</td>
<td align="right">22,677,579</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">21,489,357</td>
<td align="right">21,489,357</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,962,922</td>
<td align="right">16,962,922</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">16,939,192</td>
<td align="right">16,939,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,050,377</td>
<td align="right">10,050,377</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,308,747</td>
<td align="right">7,308,747</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,463,656</td>
<td align="right">6,463,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,948,795</td>
<td align="right">5,948,795</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,682,855</td>
<td align="right">5,682,855</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">5,568,571</td>
<td align="right">5,568,571</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,953,173</td>
<td align="right">4,953,173</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,584,627</td>
<td align="right">4,584,627</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,468,855</td>
<td align="right">4,468,855</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,044,797</td>
<td align="right">3,044,797</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,973,710</td>
<td align="right">2,973,710</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,941,630</td>
<td align="right">2,941,630</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,687,008</td>
<td align="right">2,687,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,482,608</td>
<td align="right">2,482,608</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,020,088</td>
<td align="right">2,020,088</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,794,152</td>
<td align="right">1,794,152</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,524,955</td>
<td align="right">1,524,955</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,524,955</td>
<td align="right">1,524,955</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,515,772</td>
<td align="right">1,515,772</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,490,334</td>
<td align="right">1,490,334</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,479,752</td>
<td align="right">1,479,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,341,773</td>
<td align="right">1,341,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,280,576</td>
<td align="right">1,280,576</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,133,219</td>
<td align="right">1,133,219</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,091,629</td>
<td align="right">1,091,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">892,856</td>
<td align="right">892,856</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">833,616</td>
<td align="right">833,616</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">743,585</td>
<td align="right">743,585</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">712,414</td>
<td align="right">712,414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">554,438</td>
<td align="right">554,438</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">501,760</td>
<td align="right">501,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">345,332</td>
<td align="right">345,332</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,769</td>
<td align="right">296,769</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">266,452</td>
<td align="right">266,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">255,548</td>
<td align="right">255,548</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">247,892</td>
<td align="right">247,892</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">196,240</td>
<td align="right">196,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">192,012</td>
<td align="right">192,012</td>
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
<td align="right">152,862</td>
<td align="right">152,862</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">149,586</td>
<td align="right">149,586</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">146,468</td>
<td align="right">146,468</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">129,123</td>
<td align="right">129,123</td>
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
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">84,302</td>
<td align="right">84,302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">79,878</td>
<td align="right">79,878</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">76,982</td>
<td align="right">76,982</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">61,136</td>
<td align="right">61,136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,855</td>
<td align="right">35,855</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">32,082</td>
<td align="right">32,082</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">28,797</td>
<td align="right">28,797</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">26,362</td>
<td align="right">26,362</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">24,139</td>
<td align="right">24,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">23,613</td>
<td align="right">23,613</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">23,174</td>
<td align="right">23,174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">21,455</td>
<td align="right">21,455</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,384</td>
<td align="right">16,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,467</td>
<td align="right">11,467</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,810</td>
<td align="right">10,810</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">10,431</td>
<td align="right">10,431</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,212</td>
<td align="right">9,212</td>
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
<td align="right">8,706</td>
<td align="right">8,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4,541</td>
<td align="right">4,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,078</td>
<td align="right">3,078</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,560</td>
<td align="right">2,560</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">505</td>
<td align="right">505</td>
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
<td align="right">289</td>
<td align="right">289</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">259</td>
<td align="right">259</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">126</td>
<td align="right">126</td>
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
<td align="right">8,151,428</td>
<td align="right">40.5%</td>
<td align="right">8,151,352</td>
<td align="right">40.5%</td>
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
<td align="right">11,952,293</td>
<td align="right">59.4%</td>
<td align="right">11,952,286</td>
<td align="right">59.4%</td>
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
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">189</td>
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
<td align="right">8,708</td>
<td align="right">93.6%</td>
<td align="right">8,703</td>
<td align="right">93.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">598</td>
<td align="right">6.4%</td>
<td align="right">598</td>
<td align="right">6.4%</td>
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
<td align="left">floor divide</td>
<td align="right">126</td>
<td align="right">1.4%</td>
<td align="right">121</td>
<td align="right">1.4%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,402</td>
<td align="right">39.1%</td>
<td align="right">3,402</td>
<td align="right">39.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,349</td>
<td align="right">27.0%</td>
<td align="right">2,349</td>
<td align="right">27.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,492</td>
<td align="right">17.1%</td>
<td align="right">1,492</td>
<td align="right">17.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">535</td>
<td align="right">6.1%</td>
<td align="right">535</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">272</td>
<td align="right">3.1%</td>
<td align="right">272</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">2.6%</td>
<td align="right">229</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">116</td>
<td align="right">1.3%</td>
<td align="right">116</td>
<td align="right">1.3%</td>
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
<td align="left">true divide other</td>
<td align="right">46</td>
<td align="right">0.5%</td>
<td align="right">46</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">6</td>
<td align="right">0.1%</td>
<td align="right">6</td>
<td align="right">0.1%</td>
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
<td align="right">2,736,118</td>
<td align="right">100.0%</td>
<td align="right">2,750,651</td>
<td align="right">100.0%</td>
<td align="right">0.5%</td>
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
<td align="right">3,770,361</td>
<td align="right">9.8%</td>
<td align="right">3,853,771</td>
<td align="right">10.0%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,467,392</td>
<td align="right">84.1%</td>
<td align="right">32,467,392</td>
<td align="right">83.9%</td>
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
<td align="right">2,366,706</td>
<td align="right">6.1%</td>
<td align="right">2,366,706</td>
<td align="right">6.1%</td>
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
<td align="right">5,653</td>
<td align="right">11.0%</td>
<td align="right">5,675</td>
<td align="right">11.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">45,742</td>
<td align="right">89.0%</td>
<td align="right">45,742</td>
<td align="right">89.0%</td>
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
<td align="right">864</td>
<td align="right">15.3%</td>
<td align="right">886</td>
<td align="right">15.6%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,655</td>
<td align="right">47.0%</td>
<td align="right">2,655</td>
<td align="right">46.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">1,252</td>
<td align="right">22.1%</td>
<td align="right">1,252</td>
<td align="right">22.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">307</td>
<td align="right">5.4%</td>
<td align="right">307</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">245</td>
<td align="right">4.3%</td>
<td align="right">245</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">238</td>
<td align="right">4.2%</td>
<td align="right">238</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">92</td>
<td align="right">1.6%</td>
<td align="right">92</td>
<td align="right">1.6%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,859,186</td>
<td align="right">0.8%</td>
<td align="right">1,859,087</td>
<td align="right">0.8%</td>
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
<td align="right">1,880,289</td>
<td align="right">0.8%</td>
<td align="right">1,880,189</td>
<td align="right">0.8%</td>
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
<td align="right">239,362,408</td>
<td align="right">99.2%</td>
<td align="right">239,362,421</td>
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
<td align="right">59,424</td>
<td align="right">100.0%</td>
<td align="right">59,425</td>
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
<td align="right">400</td>
<td align="right">18.6%</td>
<td align="right">400</td>
<td align="right">18.6%</td>
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
<td align="right">1,755</td>
<td align="right">100.0%</td>
<td align="right">1,755</td>
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
<td align="right">636,765</td>
<td align="right">5.5%</td>
<td align="right">636,679</td>
<td align="right">5.5%</td>
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
<td align="right">10,929,238</td>
<td align="right">94.4%</td>
<td align="right">10,929,238</td>
<td align="right">94.4%</td>
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
<td align="right">8,049</td>
<td align="right">0.1%</td>
<td align="right">8,049</td>
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
<td align="right">2,665</td>
<td align="right">66.4%</td>
<td align="right">2,660</td>
<td align="right">66.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,348</td>
<td align="right">33.6%</td>
<td align="right">1,348</td>
<td align="right">33.6%</td>
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
<td align="right">101</td>
<td align="right">3.8%</td>
<td align="right">96</td>
<td align="right">3.6%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,804</td>
<td align="right">67.7%</td>
<td align="right">1,804</td>
<td align="right">67.8%</td>
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
<td align="left">set</td>
<td align="right">43</td>
<td align="right">1.6%</td>
<td align="right">43</td>
<td align="right">1.6%</td>
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
<td align="right">4,340,744</td>
<td align="right">27.0%</td>
<td align="right">4,350,554</td>
<td align="right">27.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,734,400</td>
<td align="right">73.0%</td>
<td align="right">11,734,400</td>
<td align="right">72.9%</td>
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
<td align="right">528</td>
<td align="right">9.5%</td>
<td align="right">528</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,018</td>
<td align="right">90.5%</td>
<td align="right">5,018</td>
<td align="right">90.5%</td>
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
<td align="left">str</td>
<td align="right">2,172</td>
<td align="right">43.3%</td>
<td align="right">2,172</td>
<td align="right">43.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,492</td>
<td align="right">29.7%</td>
<td align="right">1,492</td>
<td align="right">29.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">733</td>
<td align="right">14.6%</td>
<td align="right">733</td>
<td align="right">14.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">621</td>
<td align="right">12.4%</td>
<td align="right">621</td>
<td align="right">12.4%</td>
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
<td align="right">4,543,061</td>
<td align="right">4.3%</td>
<td align="right">20,444,924</td>
<td align="right">14.0%</td>
<td align="right">350.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">91,526,755</td>
<td align="right">86.4%</td>
<td align="right">113,502,785</td>
<td align="right">78.0%</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,806,520</td>
<td align="right">9.3%</td>
<td align="right">11,593,234</td>
<td align="right">8.0%</td>
<td align="right">18.2%</td>
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
<td align="right">86,369</td>
<td align="right">94.0%</td>
<td align="right">386,383</td>
<td align="right">98.5%</td>
<td align="right">347.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,539</td>
<td align="right">6.0%</td>
<td align="right">5,930</td>
<td align="right">1.5%</td>
<td align="right">7.1%</td>
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
<td align="left">seq iter</td>
<td align="right">1,244</td>
<td align="right">22.5%</td>
<td align="right">1,589</td>
<td align="right">26.8%</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">710</td>
<td align="right">12.8%</td>
<td align="right">732</td>
<td align="right">12.3%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,589</td>
<td align="right">28.7%</td>
<td align="right">1,612</td>
<td align="right">27.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">351</td>
<td align="right">6.3%</td>
<td align="right">352</td>
<td align="right">5.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">469</td>
<td align="right">8.5%</td>
<td align="right">469</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">465</td>
<td align="right">8.4%</td>
<td align="right">465</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">272</td>
<td align="right">4.9%</td>
<td align="right">272</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">234</td>
<td align="right">4.2%</td>
<td align="right">234</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">97</td>
<td align="right">1.8%</td>
<td align="right">97</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">61</td>
<td align="right">1.1%</td>
<td align="right">61</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">47</td>
<td align="right">0.8%</td>
<td align="right">47</td>
<td align="right">0.8%</td>
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
<td align="right">95,709,061</td>
<td align="right">28.1%</td>
<td align="right">134,990,194</td>
<td align="right">33.4%</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">197,607,351</td>
<td align="right">58.1%</td>
<td align="right">220,671,196</td>
<td align="right">54.6%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">46,250,215</td>
<td align="right">13.6%</td>
<td align="right">47,878,954</td>
<td align="right">11.8%</td>
<td align="right">3.5%</td>
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
<td align="right">57,066</td>
<td align="right">3.1%</td>
<td align="right">181,775</td>
<td align="right">6.7%</td>
<td align="right">218.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,809,154</td>
<td align="right">96.9%</td>
<td align="right">2,549,954</td>
<td align="right">93.3%</td>
<td align="right">40.9%</td>
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
<td align="right">636</td>
<td align="right">1.1%</td>
<td align="right">658</td>
<td align="right">0.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,294</td>
<td align="right">2.3%</td>
<td align="right">1,316</td>
<td align="right">0.7%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,203</td>
<td align="right">5.6%</td>
<td align="right">3,245</td>
<td align="right">1.8%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,856</td>
<td align="right">5.0%</td>
<td align="right">2,856</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">993</td>
<td align="right">1.7%</td>
<td align="right">993</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">645</td>
<td align="right">1.1%</td>
<td align="right">645</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">323</td>
<td align="right">0.6%</td>
<td align="right">323</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">115</td>
<td align="right">0.2%</td>
<td align="right">115</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">71</td>
<td align="right">0.1%</td>
<td align="right">71</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">68</td>
<td align="right">0.1%</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
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
<td align="right">209,689,427</td>
<td align="right">100.0%</td>
<td align="right">210,587,429</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,005</td>
<td align="right">0.0%</td>
<td align="right">3,006</td>
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
<td align="right">12,096</td>
<td align="right">0.0%</td>
<td align="right">12,096</td>
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
<td align="right">19,393</td>
<td align="right">100.0%</td>
<td align="right">19,394</td>
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
<td align="right">424,857</td>
<td align="right">99.9%</td>
<td align="right">424,857</td>
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
<td align="right">10,035,417</td>
<td align="right">29.8%</td>
<td align="right">10,035,417</td>
<td align="right">29.8%</td>
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
<td align="right">14,054,795</td>
<td align="right">41.7%</td>
<td align="right">14,054,795</td>
<td align="right">41.7%</td>
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
<td align="right">9,609,951</td>
<td align="right">28.5%</td>
<td align="right">9,609,951</td>
<td align="right">28.5%</td>
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
<td align="right">185,985</td>
<td align="right">95.0%</td>
<td align="right">185,985</td>
<td align="right">95.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,812</td>
<td align="right">5.0%</td>
<td align="right">9,812</td>
<td align="right">5.0%</td>
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
<td align="right">46,209</td>
<td align="right">470.9%</td>
<td align="right">170,832</td>
<td align="right">1,741.1%</td>
<td align="right">269.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">5,037</td>
<td align="right">51.3%</td>
<td align="right">5,037</td>
<td align="right">51.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,626</td>
<td align="right">26.8%</td>
<td align="right">2,626</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">643</td>
<td align="right">6.6%</td>
<td align="right">643</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">311</td>
<td align="right">3.2%</td>
<td align="right">311</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">287</td>
<td align="right">2.9%</td>
<td align="right">287</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">122</td>
<td align="right">1.2%</td>
<td align="right">122</td>
<td align="right">1.2%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">9</td>
<td align="right">0.1%</td>
<td align="right">9</td>
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
<td align="right">196,240</td>
<td align="right">100.0%</td>
<td align="right">196,240</td>
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
<td align="right">1,486,386</td>
<td align="right">14.0%</td>
<td align="right">1,486,386</td>
<td align="right">14.0%</td>
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
<td align="right">9,156,355</td>
<td align="right">86.0%</td>
<td align="right">9,156,355</td>
<td align="right">86.0%</td>
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
<td align="right">474</td>
<td align="right">12.0%</td>
<td align="right">474</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,474</td>
<td align="right">88.0%</td>
<td align="right">3,474</td>
<td align="right">88.0%</td>
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
<td align="right">2,960</td>
<td align="right">85.2%</td>
<td align="right">2,960</td>
<td align="right">85.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">342</td>
<td align="right">9.8%</td>
<td align="right">342</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">112</td>
<td align="right">3.2%</td>
<td align="right">112</td>
<td align="right">3.2%</td>
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
<td align="right">13</td>
<td align="right">0.4%</td>
<td align="right">13</td>
<td align="right">0.4%</td>
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
<td align="right">13,940,828</td>
<td align="right">7.4%</td>
<td align="right">14,345,070</td>
<td align="right">7.6%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,380,170</td>
<td align="right">2.9%</td>
<td align="right">5,450,776</td>
<td align="right">2.9%</td>
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
<td align="right">168,768,722</td>
<td align="right">89.7%</td>
<td align="right">168,735,029</td>
<td align="right">89.4%</td>
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
<td align="right">105,442</td>
<td align="right">42.1%</td>
<td align="right">106,751</td>
<td align="right">42.4%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">144,970</td>
<td align="right">57.9%</td>
<td align="right">145,250</td>
<td align="right">57.6%</td>
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
<td align="left">number</td>
<td align="right">131,622</td>
<td align="right">90.8%</td>
<td align="right">131,902</td>
<td align="right">90.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,947</td>
<td align="right">6.9%</td>
<td align="right">9,947</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,081</td>
<td align="right">1.4%</td>
<td align="right">2,081</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">905</td>
<td align="right">0.6%</td>
<td align="right">905</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">192</td>
<td align="right">0.1%</td>
<td align="right">192</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">116</td>
<td align="right">0.1%</td>
<td align="right">116</td>
<td align="right">0.1%</td>
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
<td align="right">14,605,541</td>
<td align="right">98.0%</td>
<td align="right">14,605,541</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">119,512,583</td>
<td align="right">3.5%</td>
<td align="right">174,773,240</td>
<td align="right">4.8%</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,317,063,627</td>
<td align="right">38.8%</td>
<td align="right">1,439,657,159</td>
<td align="right">39.2%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,851,331,584</td>
<td align="right">54.6%</td>
<td align="right">1,950,203,755</td>
<td align="right">53.1%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">102,375,141</td>
<td align="right">3.0%</td>
<td align="right">106,427,983</td>
<td align="right">2.9%</td>
<td align="right">4.0%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">9,806,520</td>
<td align="right">9.5%</td>
<td align="right">11,593,234</td>
<td align="right">10.8%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">46,250,215</td>
<td align="right">44.7%</td>
<td align="right">47,878,954</td>
<td align="right">44.6%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">13,940,828</td>
<td align="right">13.5%</td>
<td align="right">14,345,070</td>
<td align="right">13.4%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,770,361</td>
<td align="right">3.6%</td>
<td align="right">3,853,771</td>
<td align="right">3.6%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,736,118</td>
<td align="right">2.6%</td>
<td align="right">2,750,651</td>
<td align="right">2.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,340,744</td>
<td align="right">4.2%</td>
<td align="right">4,350,554</td>
<td align="right">4.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,859,186</td>
<td align="right">1.8%</td>
<td align="right">1,859,087</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,151,428</td>
<td align="right">7.9%</td>
<td align="right">8,151,352</td>
<td align="right">7.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,035,417</td>
<td align="right">9.7%</td>
<td align="right">10,035,417</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,486,386</td>
<td align="right">1.4%</td>
<td align="right">1,486,386</td>
<td align="right">1.4%</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,271,424</td>
<td align="right">1.9%</td>
<td align="right">10,222,863</td>
<td align="right">5.8%</td>
<td align="right">350.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,271,637</td>
<td align="right">1.9%</td>
<td align="right">10,222,061</td>
<td align="right">5.8%</td>
<td align="right">350.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">17,887,967</td>
<td align="right">15.0%</td>
<td align="right">36,392,041</td>
<td align="right">20.8%</td>
<td align="right">103.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">14,554,935</td>
<td align="right">12.2%</td>
<td align="right">23,490,049</td>
<td align="right">13.4%</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">44,472,094</td>
<td align="right">37.2%</td>
<td align="right">55,394,822</td>
<td align="right">31.7%</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,381,923</td>
<td align="right">3.7%</td>
<td align="right">4,418,128</td>
<td align="right">2.5%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,690,862</td>
<td align="right">6.4%</td>
<td align="right">7,690,802</td>
<td align="right">4.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">10,358,933</td>
<td align="right">8.7%</td>
<td align="right">10,358,933</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,554,980</td>
<td align="right">8.0%</td>
<td align="right">9,554,980</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,342,047</td>
<td align="right">2.0%</td>
<td align="right">2,342,047</td>
<td align="right">1.3%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">628,460</td>
<td align="right">0.3%</td>
<td align="right">596,239</td>
<td align="right">0.3%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">6,692,396</td>
<td align="right">3.1%</td>
<td align="right">6,629,167</td>
<td align="right">3.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,249,999</td>
<td align="right">18.4%</td>
<td align="right">40,217,778</td>
<td align="right">18.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,249,999</td>
<td align="right">18.4%</td>
<td align="right">40,217,778</td>
<td align="right">18.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">178,922,578</td>
<td align="right">81.6%</td>
<td align="right">178,922,578</td>
<td align="right">81.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,621,539</td>
<td align="right">18.1%</td>
<td align="right">39,621,539</td>
<td align="right">18.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">377</td>
<td align="right">0.0%</td>
<td align="right">377</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,619,818</td>
<td align="right">18.1%</td>
<td align="right">39,619,818</td>
<td align="right">18.1%</td>
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
<td align="right">10,484,683</td>
<td align="right">4.8%</td>
<td align="right">10,484,683</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">502,496</td>
<td align="right">0.2%</td>
<td align="right">502,496</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">18,558,143</td>
<td align="right">8.5%</td>
<td align="right">18,558,143</td>
<td align="right">8.5%</td>
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
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,068,750</td>
<td align="right">72.1%</td>
<td align="right">158,068,750</td>
<td align="right">72.1%</td>
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
<td align="left">Mortal decrefs</td>
<td align="right">1,128,267,383</td>
<td align="right">27.1%</td>
<td align="right">868,444,408</td>
<td align="right">22.3%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,272,801,391</td>
<td align="right">34.2%</td>
<td align="right">995,117,422</td>
<td align="right">28.5%</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">710,913,043</td>
<td align="right">17.1%</td>
<td align="right">622,173,276</td>
<td align="right">16.0%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">214,529,004</td>
<td align="right"></td>
<td align="right">192,494,492</td>
<td align="right"></td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">546,113,852</td>
<td align="right">13.1%</td>
<td align="right">584,046,337</td>
<td align="right">15.0%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">390,469,806</td>
<td align="right">10.5%</td>
<td align="right">408,009,614</td>
<td align="right">11.7%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,375,341,559</td>
<td align="right">37.0%</td>
<td align="right">1,433,876,960</td>
<td align="right">41.0%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">683,116,946</td>
<td align="right">18.4%</td>
<td align="right">656,479,281</td>
<td align="right">18.8%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,623,816</td>
<td align="right"></td>
<td align="right">2,552,980</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,771,868,956</td>
<td align="right">42.6%</td>
<td align="right">1,812,112,554</td>
<td align="right">46.6%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">11,625,354</td>
<td align="right"></td>
<td align="right">11,412,921</td>
<td align="right"></td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">9,003,316</td>
<td align="right"></td>
<td align="right">8,861,682</td>
<td align="right"></td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">62,118</td>
<td align="right">0.0%</td>
<td align="right">62,990</td>
<td align="right">0.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,426,421</td>
<td align="right">0.5%</td>
<td align="right">1,430,126</td>
<td align="right">0.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">158,391,292</td>
<td align="right"></td>
<td align="right">158,102,456</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">145,760,982</td>
<td align="right">51.2%</td>
<td align="right">145,675,250</td>
<td align="right">51.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">147,249,521</td>
<td align="right">51.7%</td>
<td align="right">147,168,366</td>
<td align="right">51.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">155,156,250</td>
<td align="right"></td>
<td align="right">155,227,026</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">137,344,821</td>
<td align="right">48.3%</td>
<td align="right">137,325,786</td>
<td align="right">48.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">137,302,862</td>
<td align="right"></td>
<td align="right">137,285,398</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,079,685</td>
<td align="right"></td>
<td align="right">3,079,685</td>
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
<td align="right">6,240</td>
<td align="right">13,216,729</td>
<td align="right">264,739,935</td>
<td align="right">16,131,194</td>
<td align="right">24,260,468</td>
<td align="right">6,300</td>
<td align="right">13,134,122</td>
<td align="right">261,650,695</td>
<td align="right">16,183,634</td>
<td align="right">23,996,484</td>
</tr>
<tr>
<td align="right">2</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">15,784</td>
<td align="right">62.2%</td>
<td align="right">3,181</td>
<td align="right">18.2%</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">16,257</td>
<td align="right">64.1%</td>
<td align="right">3,630</td>
<td align="right">20.8%</td>
<td align="right">-77.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">231,739,484</td>
<td align="right"></td>
<td align="right">53,955,979</td>
<td align="right"></td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">63</td>
<td align="right">0.2%</td>
<td align="right">105</td>
<td align="right">0.6%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,150,543,443</td>
<td align="right">928.0%</td>
<td align="right">924,758,580</td>
<td align="right">1,713.9%</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">9,573</td>
<td align="right">37.8%</td>
<td align="right">14,293</td>
<td align="right">81.8%</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">25,357</td>
<td align="right"></td>
<td align="right">17,474</td>
<td align="right"></td>
<td align="right">-31.1%</td>
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
<td align="right">9,573</td>
<td align="right"></td>
<td align="right">14,293</td>
<td align="right"></td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">9,552</td>
<td align="right">99.8%</td>
<td align="right">14,251</td>
<td align="right">99.7%</td>
<td align="right">49.2%</td>
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
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">50,428,731</td>
<td align="right">63.8%</td>
<td align="right">108,994,512</td>
<td align="right">69.1%</td>
<td align="right">116.1%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">8,664,248</td>
<td align="right">11.0%</td>
<td align="right">18,444,152</td>
<td align="right">11.7%</td>
<td align="right">112.9%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">77,410,304</td>
<td align="right">98.0%</td>
<td align="right">158,113,792</td>
<td align="right">100.2%</td>
<td align="right">104.3%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">79,003,648</td>
<td align="right"></td>
<td align="right">157,728,768</td>
<td align="right"></td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">19,910,669</td>
<td align="right">25.2%</td>
<td align="right">30,290,104</td>
<td align="right">19.2%</td>
<td align="right">52.1%</td>
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
<td align="left">2,730</td>
<td align="right">28.6%</td>
<td align="left">5,610</td>
<td align="right">35.2%</td>
<td align="right">105.5%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">4,924</td>
<td align="right">51.5%</td>
<td align="left">6,245</td>
<td align="right">39.2%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">1,708</td>
<td align="right">17.9%</td>
<td align="left">2,874</td>
<td align="right">18.0%</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">190</td>
<td align="right">2.0%</td>
<td align="left">624</td>
<td align="right">3.9%</td>
<td align="right">228.4%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">569</td>
<td align="right">3.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">21</td>
<td align="right">0.1%</td>
<td align="right"></td>
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
<td align="right">511</td>
<td align="right">5.3%</td>
<td align="right">770</td>
<td align="right">5.4%</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,044</td>
<td align="right">21.4%</td>
<td align="right">3,213</td>
<td align="right">22.5%</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,418</td>
<td align="right">46.2%</td>
<td align="right">6,823</td>
<td align="right">47.7%</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,347</td>
<td align="right">24.5%</td>
<td align="right">3,234</td>
<td align="right">22.6%</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">253</td>
<td align="right">2.6%</td>
<td align="right">253</td>
<td align="right">1.8%</td>
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
<td align="left"><= 8</td>
<td align="right">1,960</td>
<td align="right">20.5%</td>
<td align="right">3,771</td>
<td align="right">26.4%</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,130</td>
<td align="right">11.8%</td>
<td align="right">2,156</td>
<td align="right">15.1%</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,927</td>
<td align="right">51.5%</td>
<td align="right">6,348</td>
<td align="right">44.4%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,388</td>
<td align="right">14.5%</td>
<td align="right">1,829</td>
<td align="right">12.8%</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">147</td>
<td align="right">1.5%</td>
<td align="right">147</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
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
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,041,842</td>
<td align="right">8,405,823</td>
<td align="right">706.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">30,984,133</td>
<td align="right">57,473</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">63,625,542</td>
<td align="right">414,595</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">32,104</td>
<td align="right">1,911</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">913,716</td>
<td align="right">60,647</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">19,236</td>
<td align="right">1,995</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">19,236</td>
<td align="right">1,995</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">19,236</td>
<td align="right">1,995</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">19,236</td>
<td align="right">1,995</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,167,136</td>
<td align="right">544,057</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">20,958</td>
<td align="right">3,087</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">177,987,173</td>
<td align="right">35,261,558</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">21,626,926</td>
<td align="right">4,433,216</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">321,088</td>
<td align="right">70,035</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">220,003</td>
<td align="right">50,151</td>
<td align="right">-77.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">231,739,484</td>
<td align="right">53,955,979</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,459,923</td>
<td align="right">631,444</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">192,005</td>
<td align="right">49,324</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">33,484,542</td>
<td align="right">8,606,319</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">33,553,070</td>
<td align="right">8,669,827</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">33,333,067</td>
<td align="right">8,619,676</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">33,536,968</td>
<td align="right">8,689,642</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">34,042,533</td>
<td align="right">8,830,706</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">6,699</td>
<td align="right">1,743</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,037,875</td>
<td align="right">811,315</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">35,061,240</td>
<td align="right">9,412,406</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">4,899,264</td>
<td align="right">8,458,998</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">58,418,334</td>
<td align="right">16,094,709</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">531,422</td>
<td align="right">155,562</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">285,562</td>
<td align="right">90,913</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">285,562</td>
<td align="right">90,913</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">12,557,190</td>
<td align="right">4,054,953</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">5,396,165</td>
<td align="right">8,996,947</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">126,133</td>
<td align="right">42,723</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">203,901</td>
<td align="right">69,966</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">127,162</td>
<td align="right">43,752</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">127,099</td>
<td align="right">44,235</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">49,585,036</td>
<td align="right">18,150,225</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">49,585,036</td>
<td align="right">18,150,225</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">379,589</td>
<td align="right">139,485</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">268,850</td>
<td align="right">99,110</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,171,117</td>
<td align="right">1,241,497</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,389,000</td>
<td align="right">945,026</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,384,309</td>
<td align="right">943,533</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">227,918,743</td>
<td align="right">92,539,693</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">166,133,504</td>
<td align="right">69,439,897</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">45,177,608</td>
<td align="right">19,345,583</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">179,346</td>
<td align="right">77,117</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,341,936</td>
<td align="right">600,952</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,439,035</td>
<td align="right">1,132,330</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">34,136,836</td>
<td align="right">16,016,353</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,861,352</td>
<td align="right">1,884,511</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">105,018</td>
<td align="right">51,264</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">35,529,676</td>
<td align="right">17,374,399</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">609,699</td>
<td align="right">298,216</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">35,737,352</td>
<td align="right">17,567,228</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">608,714</td>
<td align="right">302,667</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">69,343,300</td>
<td align="right">34,561,916</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">32,264,841</td>
<td align="right">16,219,952</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,741,358</td>
<td align="right">1,383,287</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">612,901</td>
<td align="right">316,373</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">612,901</td>
<td align="right">316,373</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,789,104</td>
<td align="right">2,002,390</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">12,794,335</td>
<td align="right">6,813,285</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">771,966</td>
<td align="right">412,811</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">313,982</td>
<td align="right">169,232</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,438,000</td>
<td align="right">1,316,243</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">663,020</td>
<td align="right">366,318</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,881,129</td>
<td align="right">1,592,127</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,607,451</td>
<td align="right">1,461,421</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">67,928</td>
<td align="right">39,079</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">23,416</td>
<td align="right">13,517</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,043,459</td>
<td align="right">1,766,263</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">5,816,067</td>
<td align="right">3,441,249</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">229,754</td>
<td align="right">136,332</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">167,342</td>
<td align="right">100,258</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">15,542,258</td>
<td align="right">9,319,274</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,260,038</td>
<td align="right">1,359,714</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">205,949</td>
<td align="right">124,118</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">3,844,993</td>
<td align="right">2,321,426</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">677,355</td>
<td align="right">413,149</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,871,155</td>
<td align="right">2,977,353</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,337,476</td>
<td align="right">3,271,571</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,935,285</td>
<td align="right">2,418,308</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">236,610,639</td>
<td align="right">147,711,294</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">54,414,411</td>
<td align="right">34,084,001</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">5,245,499</td>
<td align="right">3,320,684</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,132,750</td>
<td align="right">727,552</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,051,082</td>
<td align="right">678,017</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">2,311,731</td>
<td align="right">1,524,605</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">1,048,462</td>
<td align="right">696,117</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,328,271</td>
<td align="right">1,558,824</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,311,306</td>
<td align="right">889,357</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">22,129,548</td>
<td align="right">15,589,075</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">124,935</td>
<td align="right">90,442</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">124,670</td>
<td align="right">90,266</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,092,706</td>
<td align="right">801,177</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">54,975</td>
<td align="right">40,442</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">1,159,508</td>
<td align="right">855,174</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,352,047</td>
<td align="right">1,781,035</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">910,189</td>
<td align="right">695,064</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">71,678,528</td>
<td align="right">54,905,060</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">429,892</td>
<td align="right">332,362</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">146,762</td>
<td align="right">117,273</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">101,682</td>
<td align="right">81,606</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">54,516</td>
<td align="right">44,478</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">267,932</td>
<td align="right">221,354</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">46,557</td>
<td align="right">38,661</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">319,881</td>
<td align="right">266,127</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">322,619</td>
<td align="right">268,860</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">322,619</td>
<td align="right">268,860</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">101,867</td>
<td align="right">85,886</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">77,909,910</td>
<td align="right">88,708,036</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">44,083</td>
<td align="right">48,962</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">139,082</td>
<td align="right">129,272</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">631,573</td>
<td align="right">659,229</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">470,964</td>
<td align="right">456,779</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">3,502</td>
<td align="right">3,499</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">179,580</td>
<td align="right">179,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">95,467</td>
<td align="right">95,467</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">16,317</td>
<td align="right">16,317</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,124</td>
<td align="right">6,124</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,124</td>
<td align="right">6,124</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,675</td>
<td align="right">3,675</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">3,675</td>
<td align="right">3,675</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">3,675</td>
<td align="right">3,675</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">3,546</td>
<td align="right">3,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">1,932</td>
<td align="right">1,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">1,773</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">1,773</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">1,029</td>
<td align="right">1,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,029</td>
<td align="right">1,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,029</td>
<td align="right">1,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">245</td>
<td align="right">245</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">245</td>
<td align="right">245</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">139</td>
<td align="right">139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">21</td>
<td align="right">21</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">170</td>
<td align="right">212</td>
<td align="right">24.7%</td>
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
<td align="right">22</td>
<td align="right">22</td>
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
<td align="right">23</td>
<td align="right">23</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-06
