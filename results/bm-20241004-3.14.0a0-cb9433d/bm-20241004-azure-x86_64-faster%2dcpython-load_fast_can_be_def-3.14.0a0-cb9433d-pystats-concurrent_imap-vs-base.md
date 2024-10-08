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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">368,790</td>
<td align="right">978,700</td>
<td align="right">165.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,780,782</td>
<td align="right">9,880,354</td>
<td align="right">161.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,403,156</td>
<td align="right">3,640,389</td>
<td align="right">159.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">342,857</td>
<td align="right">885,973</td>
<td align="right">158.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">901,055</td>
<td align="right">2,325,038</td>
<td align="right">158.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,091,144</td>
<td align="right">13,127,489</td>
<td align="right">157.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">775,187</td>
<td align="right">1,996,051</td>
<td align="right">157.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,162,657</td>
<td align="right">2,992,760</td>
<td align="right">157.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">259,928</td>
<td align="right">666,438</td>
<td align="right">156.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,440,096</td>
<td align="right">3,686,369</td>
<td align="right">156.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,346,696</td>
<td align="right">3,390,221</td>
<td align="right">151.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,342,537</td>
<td align="right">3,377,632</td>
<td align="right">151.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,488,296</td>
<td align="right">3,734,969</td>
<td align="right">151.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">269,968</td>
<td align="right">676,478</td>
<td align="right">150.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,242,977</td>
<td align="right">3,092,280</td>
<td align="right">148.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">429,715</td>
<td align="right">1,056,266</td>
<td align="right">145.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">574,215</td>
<td align="right">1,389,954</td>
<td align="right">142.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">289,946</td>
<td align="right">698,920</td>
<td align="right">141.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">433,446</td>
<td align="right">1,044,101</td>
<td align="right">140.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">291,406</td>
<td align="right">700,380</td>
<td align="right">140.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">435,315</td>
<td align="right">1,045,876</td>
<td align="right">140.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">91</td>
<td align="right">218</td>
<td align="right">139.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">157,511</td>
<td align="right">361,811</td>
<td align="right">129.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">476,507</td>
<td align="right">1,090,309</td>
<td align="right">128.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,568,002</td>
<td align="right">14,817,039</td>
<td align="right">125.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">174,148</td>
<td align="right">386,272</td>
<td align="right">121.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">169,164</td>
<td align="right">373,699</td>
<td align="right">120.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">170,380</td>
<td align="right">373,752</td>
<td align="right">119.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,022,795</td>
<td align="right">13,179,117</td>
<td align="right">118.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,271,024</td>
<td align="right">22,369,483</td>
<td align="right">117.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,905,159</td>
<td align="right">4,143,510</td>
<td align="right">117.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,493,371</td>
<td align="right">29,302,311</td>
<td align="right">117.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">6,367,365</td>
<td align="right">13,604,914</td>
<td align="right">113.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,032,301</td>
<td align="right">4,279,291</td>
<td align="right">110.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">12,819,308</td>
<td align="right">26,614,226</td>
<td align="right">107.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,551,655</td>
<td align="right">13,549,393</td>
<td align="right">106.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,025,761</td>
<td align="right">6,148,649</td>
<td align="right">103.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,394,335</td>
<td align="right">2,825,438</td>
<td align="right">102.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,842,990</td>
<td align="right">7,758,587</td>
<td align="right">101.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,569,678</td>
<td align="right">7,061,938</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,470,078</td>
<td align="right">2,896,539</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,248,945</td>
<td align="right">8,348,235</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,065,543</td>
<td align="right">535,980</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">25,013,823</td>
<td align="right">48,167,497</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,503,643</td>
<td align="right">4,782,775</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,352,552</td>
<td align="right">2,573,330</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,238,926</td>
<td align="right">6,148,706</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">180</td>
<td align="right">340</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,946,191</td>
<td align="right">5,488,299</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">788,639</td>
<td align="right">1,449,769</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">8,013,259</td>
<td align="right">14,650,538</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">79,179,473</td>
<td align="right">16,349,752</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,980,537</td>
<td align="right">10,503,940</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">323,974</td>
<td align="right">565,625</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">16,978,045</td>
<td align="right">29,488,181</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">906,854</td>
<td align="right">1,524,913</td>
<td align="right">68.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,251,451</td>
<td align="right">2,097,582</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">8,864,020</td>
<td align="right">14,831,582</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">29,513,910</td>
<td align="right">49,356,155</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,849,318</td>
<td align="right">22,843,836</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">20,262,610</td>
<td align="right">32,954,673</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,385,973</td>
<td align="right">8,723,663</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,365,234</td>
<td align="right">2,195,132</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">19,263,572</td>
<td align="right">30,548,205</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">8,465,382</td>
<td align="right">12,824,290</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,065,540</td>
<td align="right">12,181,200</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,653,321</td>
<td align="right">2,476,971</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,512,890</td>
<td align="right">5,179,208</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,723,726</td>
<td align="right">5,380,569</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,721,153</td>
<td align="right">12,214,658</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">44,888</td>
<td align="right">62,661</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">118,788</td>
<td align="right">160,648</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,350,042</td>
<td align="right">1,774,242</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,414,476</td>
<td align="right">8,403,477</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">29,440</td>
<td align="right">38,400</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">797,834</td>
<td align="right">1,019,328</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">35,860</td>
<td align="right">45,700</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">41,220</td>
<td align="right">50,900</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">124,695</td>
<td align="right">152,775</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">7,221</td>
<td align="right">8,731</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">16,075,322</td>
<td align="right">19,146,503</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">880</td>
<td align="right">1,040</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,251,250</td>
<td align="right">1,473,314</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">71,007</td>
<td align="right">80,532</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,926,902</td>
<td align="right">4,366,782</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">17,983</td>
<td align="right">19,574</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">23,183</td>
<td align="right">24,854</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">23,183</td>
<td align="right">24,854</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,780</td>
<td align="right">5,100</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">108,280</td>
<td align="right">113,240</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">57,160</td>
<td align="right">59,720</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">21,440</td>
<td align="right">22,400</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">86,200</td>
<td align="right">90,040</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">86,200</td>
<td align="right">90,040</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">750,936</td>
<td align="right">783,166</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">95,160</td>
<td align="right">97,960</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">47,800</td>
<td align="right">49,000</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">32,460</td>
<td align="right">33,260</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">69,900</td>
<td align="right">71,580</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">69,940</td>
<td align="right">71,620</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">16,700</td>
<td align="right">17,100</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,121,981</td>
<td align="right">1,148,236</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">27,399</td>
<td align="right">28,000</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,880</td>
<td align="right">19,280</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">62,680</td>
<td align="right">63,960</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">236,531</td>
<td align="right">241,298</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">86,739</td>
<td align="right">88,480</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">36,760</td>
<td align="right">37,480</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,163,100</td>
<td align="right">1,183,860</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">553,228</td>
<td align="right">562,864</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">107,300</td>
<td align="right">109,060</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">43,771</td>
<td align="right">44,458</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">61,240</td>
<td align="right">62,200</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">525,740</td>
<td align="right">533,980</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,241,220</td>
<td align="right">6,337,380</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">5,730,320</td>
<td align="right">5,818,480</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">78,000</td>
<td align="right">79,200</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">10,400</td>
<td align="right">10,560</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,200</td>
<td align="right">5,280</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,056,307</td>
<td align="right">1,072,552</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">15,660</td>
<td align="right">15,900</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">83,700</td>
<td align="right">84,980</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,320</td>
<td align="right">5,400</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">11,380</td>
<td align="right">11,540</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,241,064</td>
<td align="right">2,268,333</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">25,860</td>
<td align="right">26,100</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">130,280</td>
<td align="right">131,480</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">130,860</td>
<td align="right">132,060</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,053,600</td>
<td align="right">1,062,240</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">38,780</td>
<td align="right">39,020</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">25,571</td>
<td align="right">25,655</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,115</td>
<td align="right">35,213</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">571,260</td>
<td align="right">572,460</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,823,420</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">18,640</td>
<td align="right">18,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">9,180</td>
<td align="right">9,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">8,320</td>
<td align="right">8,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,860</td>
<td align="right">4,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,420</td>
<td align="right">2,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,540</td>
<td align="right">1,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,220</td>
<td align="right">1,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">500</td>
<td align="right">500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_DEFERRED</td>
<td align="right"></td>
<td align="right">185,738,759</td>
<td align="right"></td>
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
<td align="right">210,262</td>
<td align="right">3.0%</td>
<td align="right">570,072</td>
<td align="right">3.5%</td>
<td align="right">171.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,072,697</td>
<td align="right">71.5%</td>
<td align="right">13,086,681</td>
<td align="right">80.1%</td>
<td align="right">158.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,796,520</td>
<td align="right">25.3%</td>
<td align="right">2,630,856</td>
<td align="right">16.1%</td>
<td align="right">46.4%</td>
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
<td align="right">4,636</td>
<td align="right">20.7%</td>
<td align="right">11,428</td>
<td align="right">22.2%</td>
<td align="right">146.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">17,769</td>
<td align="right">79.3%</td>
<td align="right">40,128</td>
<td align="right">77.8%</td>
<td align="right">125.8%</td>
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
<td align="right">12,444</td>
<td align="right">70.0%</td>
<td align="right">32,755</td>
<td align="right">81.6%</td>
<td align="right">163.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,548</td>
<td align="right">8.7%</td>
<td align="right">2,291</td>
<td align="right">5.7%</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">140</td>
<td align="right">0.8%</td>
<td align="right">200</td>
<td align="right">0.5%</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2,959</td>
<td align="right">16.7%</td>
<td align="right">4,147</td>
<td align="right">10.3%</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">678</td>
<td align="right">3.8%</td>
<td align="right">735</td>
<td align="right">1.8%</td>
<td align="right">8.4%</td>
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
<td align="right">18,880</td>
<td align="right">100.0%</td>
<td align="right">19,280</td>
<td align="right">100.0%</td>
<td align="right">2.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">520,688</td>
<td align="right">48.5%</td>
<td align="right">935,358</td>
<td align="right">62.4%</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">552,201</td>
<td align="right">51.4%</td>
<td align="right">561,791</td>
<td align="right">37.5%</td>
<td align="right">1.7%</td>
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
<td align="right">727</td>
<td align="right">70.8%</td>
<td align="right">773</td>
<td align="right">72.0%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">300</td>
<td align="right">29.2%</td>
<td align="right">300</td>
<td align="right">28.0%</td>
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
<td align="left">buffer int</td>
<td align="right">727</td>
<td align="right">100.0%</td>
<td align="right">773</td>
<td align="right">100.0%</td>
<td align="right">6.3%</td>
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
<td align="right">19,687,858</td>
<td align="right">99.8%</td>
<td align="right">38,732,672</td>
<td align="right">99.9%</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,100</td>
<td align="right">0.0%</td>
<td align="right">5,580</td>
<td align="right">0.0%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19,273</td>
<td align="right">0.1%</td>
<td align="right">19,307</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
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
<td align="right">16,722</td>
<td align="right">100.0%</td>
<td align="right">16,786</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
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
<td align="right">820</td>
<td align="right">53.2%</td>
<td align="right">820</td>
<td align="right">53.2%</td>
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
<td align="right">124,966</td>
<td align="right">2.7%</td>
<td align="right">328,512</td>
<td align="right">4.1%</td>
<td align="right">162.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">424,658</td>
<td align="right">9.2%</td>
<td align="right">1,047,147</td>
<td align="right">13.1%</td>
<td align="right">146.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,072,975</td>
<td align="right">88.0%</td>
<td align="right">6,633,601</td>
<td align="right">82.7%</td>
<td align="right">62.9%</td>
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
<td align="right">3,297</td>
<td align="right">44.7%</td>
<td align="right">7,346</td>
<td align="right">48.1%</td>
<td align="right">122.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,087</td>
<td align="right">55.3%</td>
<td align="right">7,940</td>
<td align="right">51.9%</td>
<td align="right">94.3%</td>
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
<td align="right">2,859</td>
<td align="right">86.7%</td>
<td align="right">6,851</td>
<td align="right">93.3%</td>
<td align="right">139.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">138</td>
<td align="right">4.2%</td>
<td align="right">175</td>
<td align="right">2.4%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">300</td>
<td align="right">9.1%</td>
<td align="right">320</td>
<td align="right">4.4%</td>
<td align="right">6.7%</td>
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
<td align="right">1,396,755</td>
<td align="right">100.0%</td>
<td align="right">2,827,858</td>
<td align="right">100.0%</td>
<td align="right">102.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">180</td>
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
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">140</td>
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
<td align="right">14,663,477</td>
<td align="right">92.7%</td>
<td align="right">19,721,906</td>
<td align="right">94.3%</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,160,760</td>
<td align="right">7.3%</td>
<td align="right">1,181,420</td>
<td align="right">5.7%</td>
<td align="right">1.8%</td>
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
<td align="right">1,640</td>
<td align="right">70.1%</td>
<td align="right">1,720</td>
<td align="right">70.5%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">700</td>
<td align="right">29.9%</td>
<td align="right">720</td>
<td align="right">29.5%</td>
<td align="right">2.9%</td>
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
<td align="left">callable</td>
<td align="right">200</td>
<td align="right">12.2%</td>
<td align="right">220</td>
<td align="right">12.8%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">340</td>
<td align="right">20.7%</td>
<td align="right">360</td>
<td align="right">20.9%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">460</td>
<td align="right">28.0%</td>
<td align="right">480</td>
<td align="right">27.9%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">460</td>
<td align="right">28.0%</td>
<td align="right">480</td>
<td align="right">27.9%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">140</td>
<td align="right">8.5%</td>
<td align="right">140</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">40</td>
<td align="right">2.4%</td>
<td align="right">40</td>
<td align="right">2.3%</td>
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
<td align="right">5,989,781</td>
<td align="right">13.8%</td>
<td align="right">13,143,530</td>
<td align="right">16.3%</td>
<td align="right">119.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,840,347</td>
<td align="right">85.1%</td>
<td align="right">66,955,599</td>
<td align="right">83.1%</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">450,446</td>
<td align="right">1.0%</td>
<td align="right">462,979</td>
<td align="right">0.6%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
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
<td align="right">13,179</td>
<td align="right">32.1%</td>
<td align="right">15,682</td>
<td align="right">35.8%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">27,835</td>
<td align="right">67.9%</td>
<td align="right">28,126</td>
<td align="right">64.2%</td>
<td align="right">1.0%</td>
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
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">0.8%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,201</td>
<td align="right">24.3%</td>
<td align="right">4,400</td>
<td align="right">28.1%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">60</td>
<td align="right">0.5%</td>
<td align="right">80</td>
<td align="right">0.5%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,200</td>
<td align="right">9.1%</td>
<td align="right">1,360</td>
<td align="right">8.7%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">2,368</td>
<td align="right">18.0%</td>
<td align="right">2,652</td>
<td align="right">16.9%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">560</td>
<td align="right">4.2%</td>
<td align="right">620</td>
<td align="right">4.0%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,924</td>
<td align="right">29.8%</td>
<td align="right">4,305</td>
<td align="right">27.5%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">220</td>
<td align="right">1.7%</td>
<td align="right">240</td>
<td align="right">1.5%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">60</td>
<td align="right">0.5%</td>
<td align="right">60</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">20,016,466</td>
<td align="right">99.7%</td>
<td align="right">42,822,824</td>
<td align="right">99.9%</td>
<td align="right">113.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,560</td>
<td align="right">0.1%</td>
<td align="right">28,880</td>
<td align="right">0.1%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,595</td>
<td align="right">0.1%</td>
<td align="right">13,629</td>
<td align="right">0.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">800</td>
<td align="right">0.0%</td>
<td align="right">800</td>
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
<td align="right">12,036</td>
<td align="right">100.0%</td>
<td align="right">12,086</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
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
<td align="right">1,432,596</td>
<td align="right">100.0%</td>
<td align="right">3,678,789</td>
<td align="right">100.0%</td>
<td align="right">156.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">260</td>
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
<td align="right">300</td>
<td align="right">100.0%</td>
<td align="right">300</td>
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
<td align="right">4,113,005</td>
<td align="right">94.1%</td>
<td align="right">8,221,815</td>
<td align="right">96.9%</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">80,700</td>
<td align="right">1.8%</td>
<td align="right">82,300</td>
<td align="right">1.0%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">171,800</td>
<td align="right">3.9%</td>
<td align="right">172,120</td>
<td align="right">2.0%</td>
<td align="right">0.2%</td>
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
<td align="right">1,620</td>
<td align="right">17.8%</td>
<td align="right">1,760</td>
<td align="right">19.0%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,499</td>
<td align="right">82.2%</td>
<td align="right">7,500</td>
<td align="right">81.0%</td>
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
<td align="left">overridden</td>
<td align="right">80</td>
<td align="right">4.9%</td>
<td align="right">100</td>
<td align="right">5.7%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">880</td>
<td align="right">54.3%</td>
<td align="right">980</td>
<td align="right">55.7%</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">460</td>
<td align="right">28.4%</td>
<td align="right">480</td>
<td align="right">27.3%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">200</td>
<td align="right">12.3%</td>
<td align="right">200</td>
<td align="right">11.4%</td>
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
<td align="right">1,470,078</td>
<td align="right">98.2%</td>
<td align="right">2,896,539</td>
<td align="right">99.0%</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">26,560</td>
<td align="right">1.8%</td>
<td align="right">27,120</td>
<td align="right">0.9%</td>
<td align="right">2.1%</td>
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
<td align="right">540</td>
<td align="right">64.4%</td>
<td align="right">580</td>
<td align="right">65.9%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">299</td>
<td align="right">35.6%</td>
<td align="right">300</td>
<td align="right">34.1%</td>
<td align="right">0.3%</td>
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
<td align="right">160</td>
<td align="right">29.6%</td>
<td align="right">180</td>
<td align="right">31.0%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">380</td>
<td align="right">70.4%</td>
<td align="right">400</td>
<td align="right">69.0%</td>
<td align="right">5.3%</td>
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
<td align="right">8,643,790</td>
<td align="right">91.5%</td>
<td align="right">19,884,590</td>
<td align="right">95.1%</td>
<td align="right">130.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">792,349</td>
<td align="right">8.4%</td>
<td align="right">1,013,602</td>
<td align="right">4.8%</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">880</td>
<td align="right">0.0%</td>
<td align="right">880</td>
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
<td align="right">2,428</td>
<td align="right">44.3%</td>
<td align="right">2,666</td>
<td align="right">46.6%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,057</td>
<td align="right">55.7%</td>
<td align="right">3,060</td>
<td align="right">53.4%</td>
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
<td align="left">bytes</td>
<td align="right">60</td>
<td align="right">2.5%</td>
<td align="right">80</td>
<td align="right">3.0%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">160</td>
<td align="right">6.6%</td>
<td align="right">180</td>
<td align="right">6.8%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">878</td>
<td align="right">36.2%</td>
<td align="right">987</td>
<td align="right">37.0%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">330</td>
<td align="right">13.6%</td>
<td align="right">359</td>
<td align="right">13.5%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">620</td>
<td align="right">25.5%</td>
<td align="right">660</td>
<td align="right">24.8%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">380</td>
<td align="right">15.7%</td>
<td align="right">400</td>
<td align="right">15.0%</td>
<td align="right">5.3%</td>
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
<td align="right">2,406,349</td>
<td align="right">99.9%</td>
<td align="right">2,846,794</td>
<td align="right">100.0%</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">680</td>
<td align="right">0.0%</td>
<td align="right">680</td>
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
<td align="right">540</td>
<td align="right">100.0%</td>
<td align="right">540</td>
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
<td align="right">14,255,160</td>
<td align="right">3.1%</td>
<td align="right">30,329,192</td>
<td align="right">3.6%</td>
<td align="right">112.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">158,220,674</td>
<td align="right">34.3%</td>
<td align="right">289,740,088</td>
<td align="right">34.4%</td>
<td align="right">83.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">287,332,684</td>
<td align="right">62.4%</td>
<td align="right">520,274,984</td>
<td align="right">61.8%</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">992,014</td>
<td align="right">0.2%</td>
<td align="right">1,569,023</td>
<td align="right">0.2%</td>
<td align="right">58.2%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">5,072,697</td>
<td align="right">35.8%</td>
<td align="right">13,086,681</td>
<td align="right">43.3%</td>
<td align="right">158.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">424,658</td>
<td align="right">3.0%</td>
<td align="right">1,047,147</td>
<td align="right">3.5%</td>
<td align="right">146.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,989,781</td>
<td align="right">42.3%</td>
<td align="right">13,143,530</td>
<td align="right">43.5%</td>
<td align="right">119.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">792,349</td>
<td align="right">5.6%</td>
<td align="right">1,013,602</td>
<td align="right">3.4%</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,880</td>
<td align="right">0.1%</td>
<td align="right">19,280</td>
<td align="right">0.1%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,560</td>
<td align="right">0.2%</td>
<td align="right">27,120</td>
<td align="right">0.1%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">80,700</td>
<td align="right">0.6%</td>
<td align="right">82,300</td>
<td align="right">0.3%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,160,760</td>
<td align="right">8.2%</td>
<td align="right">1,181,420</td>
<td align="right">3.9%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">552,201</td>
<td align="right">3.9%</td>
<td align="right">561,791</td>
<td align="right">1.9%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">19,273</td>
<td align="right">0.1%</td>
<td align="right">19,307</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">210,262</td>
<td align="right">21.2%</td>
<td align="right">570,072</td>
<td align="right">36.3%</td>
<td align="right">171.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">124,906</td>
<td align="right">12.6%</td>
<td align="right">328,452</td>
<td align="right">20.9%</td>
<td align="right">163.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">370,506</td>
<td align="right">37.3%</td>
<td align="right">383,041</td>
<td align="right">24.4%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,380</td>
<td align="right">1.0%</td>
<td align="right">10,700</td>
<td align="right">0.7%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">171,800</td>
<td align="right">17.3%</td>
<td align="right">172,120</td>
<td align="right">11.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">62,220</td>
<td align="right">6.3%</td>
<td align="right">62,218</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,180</td>
<td align="right">1.8%</td>
<td align="right">18,180</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,380</td>
<td align="right">1.2%</td>
<td align="right">12,380</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,100</td>
<td align="right">0.5%</td>
<td align="right">5,100</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,140</td>
<td align="right">0.2%</td>
<td align="right">2,140</td>
<td align="right">0.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">418,856</td>
<td align="right">1.4%</td>
<td align="right">830,198</td>
<td align="right">1.7%</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">23,350,910</td>
<td align="right">79.1%</td>
<td align="right">43,098,675</td>
<td align="right">87.3%</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">20,812,517</td>
<td align="right">70.5%</td>
<td align="right">37,161,577</td>
<td align="right">75.3%</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">8,197,373</td>
<td align="right">27.8%</td>
<td align="right">11,682,558</td>
<td align="right">23.7%</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">8,198,813</td>
<td align="right">27.8%</td>
<td align="right">11,683,998</td>
<td align="right">23.7%</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,726,413</td>
<td align="right">29.5%</td>
<td align="right">12,219,998</td>
<td align="right">24.7%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,726,413</td>
<td align="right">29.5%</td>
<td align="right">12,219,998</td>
<td align="right">24.7%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">23,543</td>
<td align="right">0.1%</td>
<td align="right">25,214</td>
<td align="right">0.1%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">562,140</td>
<td align="right">1.9%</td>
<td align="right">571,260</td>
<td align="right">1.2%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">527,600</td>
<td align="right">1.8%</td>
<td align="right">536,000</td>
<td align="right">1.1%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">544,020</td>
<td align="right">1.8%</td>
<td align="right">544,820</td>
<td align="right">1.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">980</td>
<td align="right">0.0%</td>
<td align="right">980</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="left">Inline values</td>
<td align="right">1,209,082</td>
<td align="right"></td>
<td align="right">2,848,702</td>
<td align="right"></td>
<td align="right">135.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,427,839</td>
<td align="right"></td>
<td align="right">16,727,016</td>
<td align="right"></td>
<td align="right">125.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">800</td>
<td align="right">0.1%</td>
<td align="right">1,600</td>
<td align="right">0.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">89,378,211</td>
<td align="right">25.6%</td>
<td align="right">170,499,177</td>
<td align="right">26.7%</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">45,619,742</td>
<td align="right">11.7%</td>
<td align="right">86,680,623</td>
<td align="right">12.2%</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">90,591,684</td>
<td align="right">23.2%</td>
<td align="right">171,652,520</td>
<td align="right">24.2%</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">51,687,343</td>
<td align="right">14.8%</td>
<td align="right">96,938,575</td>
<td align="right">15.2%</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">37,187,966</td>
<td align="right">10.6%</td>
<td align="right">69,362,218</td>
<td align="right">10.9%</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">16,319,438</td>
<td align="right">47.9%</td>
<td align="right">30,423,292</td>
<td align="right">51.8%</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">16,331,247</td>
<td align="right"></td>
<td align="right">30,435,449</td>
<td align="right"></td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">190,364,884</td>
<td align="right">48.8%</td>
<td align="right">340,509,675</td>
<td align="right">47.9%</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">171,099,971</td>
<td align="right">49.0%</td>
<td align="right">302,027,580</td>
<td align="right">47.3%</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">63,488,466</td>
<td align="right">16.3%</td>
<td align="right">111,409,542</td>
<td align="right">15.7%</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">10,952,913</td>
<td align="right"></td>
<td align="right">18,866,233</td>
<td align="right"></td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">18,639,398</td>
<td align="right"></td>
<td align="right">30,627,966</td>
<td align="right"></td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">17,597,768</td>
<td align="right">51.7%</td>
<td align="right">28,110,184</td>
<td align="right">47.9%</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">17,729,343</td>
<td align="right">52.1%</td>
<td align="right">28,269,211</td>
<td align="right">48.2%</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">54,410</td>
<td align="right">0.2%</td>
<td align="right">72,337</td>
<td align="right">0.1%</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,165</td>
<td align="right">0.2%</td>
<td align="right">86,690</td>
<td align="right">0.1%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">18,927</td>
<td align="right"></td>
<td align="right">16,738</td>
<td align="right"></td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">56,944</td>
<td align="right"></td>
<td align="right">54,429</td>
<td align="right"></td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">44,152</td>
<td align="right"></td>
<td align="right">43,912</td>
<td align="right"></td>
<td align="right">-0.5%</td>
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
<td align="right">40</td>
<td align="right">3,840</td>
<td align="right">925,840</td>
<td align="right">40</td>
<td align="right">3,840</td>
<td align="right">925,840</td>
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
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-04
