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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">430</td>
<td align="right">954</td>
<td align="right">121.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">577,542</td>
<td align="right">1,118,041</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,434,004</td>
<td align="right">4,676,418</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">112,155</td>
<td align="right">214,171</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">224,426</td>
<td align="right">428,450</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">561,561</td>
<td align="right">1,071,946</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">789,157</td>
<td align="right">1,503,622</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,343,907</td>
<td align="right">6,340,840</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">344,104</td>
<td align="right">651,749</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">802,216</td>
<td align="right">1,518,254</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">800,161</td>
<td align="right">1,514,300</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">576,866</td>
<td align="right">1,087,371</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,277,882</td>
<td align="right">2,402,342</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">863,616</td>
<td align="right">1,614,534</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">39,080</td>
<td align="right">72,067</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">934,661</td>
<td align="right">1,722,080</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">912,076</td>
<td align="right">1,664,594</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">755,123</td>
<td align="right">1,371,118</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">633,965</td>
<td align="right">1,149,756</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">379,913</td>
<td align="right">688,239</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">295,147</td>
<td align="right">534,040</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">128,062</td>
<td align="right">230,743</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">571,538</td>
<td align="right">1,028,976</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">800</td>
<td align="right">1,440</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">263,035</td>
<td align="right">469,968</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">809,941</td>
<td align="right">1,432,334</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">136,360</td>
<td align="right">239,330</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">182,440</td>
<td align="right">319,010</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">139,000</td>
<td align="right">241,997</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">16,818</td>
<td align="right">29,042</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,078,982</td>
<td align="right">1,861,211</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">148,473</td>
<td align="right">255,285</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,723,275</td>
<td align="right">6,397,457</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,513,623</td>
<td align="right">9,467,858</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,480,270</td>
<td align="right">2,504,388</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">96,527</td>
<td align="right">161,512</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,103,738</td>
<td align="right">11,845,246</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,721,069</td>
<td align="right">6,199,633</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,770,307</td>
<td align="right">9,576,138</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,266,362</td>
<td align="right">13,703,866</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,407,117</td>
<td align="right">2,299,822</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">211,108</td>
<td align="right">344,968</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">54,960</td>
<td align="right">89,520</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">339,015</td>
<td align="right">548,508</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2,140</td>
<td align="right">3,420</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">61,820</td>
<td align="right">97,980</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,232,746</td>
<td align="right">6,692,599</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">186,017</td>
<td align="right">293,681</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">63,600</td>
<td align="right">99,760</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">246,301</td>
<td align="right">384,698</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,119,052</td>
<td align="right">6,406,662</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">81,676</td>
<td align="right">126,902</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,142,141</td>
<td align="right">1,766,648</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">668,792</td>
<td align="right">1,024,196</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">44,866,460</td>
<td align="right">68,242,966</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">3,791,354</td>
<td align="right">5,730,837</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,819,525</td>
<td align="right">2,722,689</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">221,890</td>
<td align="right">328,150</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,122,625</td>
<td align="right">6,056,445</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,605,222</td>
<td align="right">3,825,705</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,193,310</td>
<td align="right">3,216,561</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">179,754</td>
<td align="right">262,746</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">27,480</td>
<td align="right">40,022</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">570,305</td>
<td align="right">826,633</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,227,524</td>
<td align="right">13,243,273</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,999,199</td>
<td align="right">4,285,073</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,839,853</td>
<td align="right">4,041,590</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,262,562</td>
<td align="right">13,002,807</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,038,715</td>
<td align="right">1,452,569</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">32,920</td>
<td align="right">45,782</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">32,920</td>
<td align="right">45,782</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">98,067</td>
<td align="right">134,892</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">16,300,309</td>
<td align="right">22,344,557</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">283,852</td>
<td align="right">385,836</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,971,830</td>
<td align="right">18,957,867</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,811,081</td>
<td align="right">2,431,823</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,114,538</td>
<td align="right">22,789,119</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,628,288</td>
<td align="right">9,925,539</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">829,230</td>
<td align="right">1,071,075</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,008,320</td>
<td align="right">2,561,066</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">924,516</td>
<td align="right">1,170,099</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,122,651</td>
<td align="right">7,729,731</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,042,945</td>
<td align="right">3,779,997</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">672,722</td>
<td align="right">807,376</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,860,892</td>
<td align="right">10,348,605</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,854,829</td>
<td align="right">9,106,294</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">24,320</td>
<td align="right">28,160</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,943,750</td>
<td align="right">2,248,955</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">24,800</td>
<td align="right">28,640</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">12,680</td>
<td align="right">14,600</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">12,680</td>
<td align="right">14,600</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">6,800</td>
<td align="right">7,760</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">24,940</td>
<td align="right">28,460</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,260</td>
<td align="right">28,780</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">38,140</td>
<td align="right">42,620</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">658,720</td>
<td align="right">731,068</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">35,320</td>
<td align="right">39,160</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">12,800</td>
<td align="right">14,080</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">50,880</td>
<td align="right">55,680</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">31,238</td>
<td align="right">34,143</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">17,260</td>
<td align="right">18,860</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,220</td>
<td align="right">19,820</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,480</td>
<td align="right">36,380</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">181,690</td>
<td align="right">196,940</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">89,020</td>
<td align="right">96,380</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">29,012</td>
<td align="right">31,297</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">38,720</td>
<td align="right">41,600</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">59,840</td>
<td align="right">63,680</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,155,961</td>
<td align="right">1,227,716</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">87,817</td>
<td align="right">93,078</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,529,020</td>
<td align="right">6,913,660</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">81,594</td>
<td align="right">86,400</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">10,880</td>
<td align="right">11,520</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,440</td>
<td align="right">5,760</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">16,322</td>
<td align="right">17,280</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,460</td>
<td align="right">5,780</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">71,120</td>
<td align="right">75,280</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">71,120</td>
<td align="right">75,280</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">568,380</td>
<td align="right">601,399</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">11,260</td>
<td align="right">11,900</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,142</td>
<td align="right">46,619</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,278</td>
<td align="right">18,236</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">12,080</td>
<td align="right">12,720</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">109,120</td>
<td align="right">114,880</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">54,680</td>
<td align="right">57,240</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,308,067</td>
<td align="right">2,413,985</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">29,900</td>
<td align="right">31,180</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">75,016</td>
<td align="right">78,220</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">26,520</td>
<td align="right">27,480</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">133,380</td>
<td align="right">138,180</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">133,660</td>
<td align="right">138,460</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">38,080</td>
<td align="right">39,040</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">26,909</td>
<td align="right">26,927</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">17,884</td>
<td align="right">17,886</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">9,140</td>
<td align="right">9,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5,940</td>
<td align="right">5,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">2,160</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,240</td>
<td align="right">1,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,240</td>
<td align="right">1,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">920</td>
<td align="right">920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">620</td>
<td align="right">620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">520</td>
<td align="right">520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">140</td>
<td align="right">140</td>
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
<td align="right">3,337,872</td>
<td align="right">66.8%</td>
<td align="right">6,333,991</td>
<td align="right">75.7%</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,656,634</td>
<td align="right">33.1%</td>
<td align="right">2,028,161</td>
<td align="right">24.2%</td>
<td align="right">22.4%</td>
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
<td align="right">5,420</td>
<td align="right">89.8%</td>
<td align="right">6,231</td>
<td align="right">91.0%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">615</td>
<td align="right">10.2%</td>
<td align="right">618</td>
<td align="right">9.0%</td>
<td align="right">0.5%</td>
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
<td align="left">add other</td>
<td align="right">80</td>
<td align="right">1.5%</td>
<td align="right">100</td>
<td align="right">1.6%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,393</td>
<td align="right">25.7%</td>
<td align="right">1,656</td>
<td align="right">26.6%</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2,688</td>
<td align="right">49.6%</td>
<td align="right">3,114</td>
<td align="right">50.0%</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">659</td>
<td align="right">12.2%</td>
<td align="right">721</td>
<td align="right">11.6%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">600</td>
<td align="right">11.1%</td>
<td align="right">640</td>
<td align="right">10.3%</td>
<td align="right">6.7%</td>
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
<td align="right">18,220</td>
<td align="right">100.0%</td>
<td align="right">19,820</td>
<td align="right">100.0%</td>
<td align="right">8.8%</td>
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
<td align="right">80,780</td>
<td align="right">14.5%</td>
<td align="right">125,962</td>
<td align="right">15.1%</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">476,226</td>
<td align="right">85.4%</td>
<td align="right">705,210</td>
<td align="right">84.7%</td>
<td align="right">48.1%</td>
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
<td align="right">656</td>
<td align="right">73.2%</td>
<td align="right">700</td>
<td align="right">74.5%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">240</td>
<td align="right">26.8%</td>
<td align="right">240</td>
<td align="right">25.5%</td>
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
<td align="right">656</td>
<td align="right">100.0%</td>
<td align="right">700</td>
<td align="right">100.0%</td>
<td align="right">6.7%</td>
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
<td align="right">16,462,829</td>
<td align="right">99.8%</td>
<td align="right">24,903,058</td>
<td align="right">99.9%</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,619</td>
<td align="right">0.1%</td>
<td align="right">13,628</td>
<td align="right">0.1%</td>
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
<td align="right">1,180</td>
<td align="right">0.0%</td>
<td align="right">1,180</td>
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
<td align="right">13,910</td>
<td align="right">100.0%</td>
<td align="right">13,919</td>
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
<td align="right">620</td>
<td align="right">50.0%</td>
<td align="right">620</td>
<td align="right">50.0%</td>
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
<td align="right">292,422</td>
<td align="right">7.3%</td>
<td align="right">531,228</td>
<td align="right">9.6%</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,726,116</td>
<td align="right">92.5%</td>
<td align="right">5,016,188</td>
<td align="right">90.3%</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,073</td>
<td align="right">0.2%</td>
<td align="right">6,631</td>
<td align="right">0.1%</td>
<td align="right">9.2%</td>
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
<td align="right">1,285</td>
<td align="right">45.6%</td>
<td align="right">1,371</td>
<td align="right">47.2%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,531</td>
<td align="right">54.4%</td>
<td align="right">1,533</td>
<td align="right">52.8%</td>
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
<td align="left">different types</td>
<td align="right">168</td>
<td align="right">13.1%</td>
<td align="right">191</td>
<td align="right">13.9%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">340</td>
<td align="right">26.5%</td>
<td align="right">360</td>
<td align="right">26.3%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">777</td>
<td align="right">60.5%</td>
<td align="right">820</td>
<td align="right">59.8%</td>
<td align="right">5.5%</td>
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
<td align="right">1,089,701</td>
<td align="right">100.0%</td>
<td align="right">1,631,126</td>
<td align="right">100.0%</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">80</td>
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
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">80</td>
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
<td align="right">7,316,720</td>
<td align="right">99.5%</td>
<td align="right">8,798,005</td>
<td align="right">99.6%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">31,940</td>
<td align="right">0.4%</td>
<td align="right">34,820</td>
<td align="right">0.4%</td>
<td align="right">9.0%</td>
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
<td align="right">920</td>
<td align="right">59.7%</td>
<td align="right">940</td>
<td align="right">60.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">620</td>
<td align="right">40.3%</td>
<td align="right">620</td>
<td align="right">39.7%</td>
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
<td align="left">itertools</td>
<td align="right">260</td>
<td align="right">28.3%</td>
<td align="right">280</td>
<td align="right">29.8%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">23.9%</td>
<td align="right">220</td>
<td align="right">23.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">220</td>
<td align="right">23.9%</td>
<td align="right">220</td>
<td align="right">23.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">23.9%</td>
<td align="right">220</td>
<td align="right">23.4%</td>
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
<td align="right">3,691,581</td>
<td align="right">10.2%</td>
<td align="right">6,168,864</td>
<td align="right">11.7%</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">31,967,961</td>
<td align="right">88.4%</td>
<td align="right">46,131,925</td>
<td align="right">87.2%</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">485,601</td>
<td align="right">1.3%</td>
<td align="right">561,155</td>
<td align="right">1.1%</td>
<td align="right">15.6%</td>
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
<td align="right">12,563</td>
<td align="right">32.9%</td>
<td align="right">13,820</td>
<td align="right">33.8%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">25,663</td>
<td align="right">67.1%</td>
<td align="right">27,117</td>
<td align="right">66.2%</td>
<td align="right">5.7%</td>
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
<td align="right">60</td>
<td align="right">0.5%</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">160</td>
<td align="right">1.3%</td>
<td align="right">200</td>
<td align="right">1.4%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">100</td>
<td align="right">0.7%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,009</td>
<td align="right">24.0%</td>
<td align="right">3,454</td>
<td align="right">25.0%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">640</td>
<td align="right">5.1%</td>
<td align="right">700</td>
<td align="right">5.1%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">520</td>
<td align="right">4.1%</td>
<td align="right">560</td>
<td align="right">4.1%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">260</td>
<td align="right">2.1%</td>
<td align="right">280</td>
<td align="right">2.0%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,219</td>
<td align="right">33.6%</td>
<td align="right">4,533</td>
<td align="right">32.8%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">2,016</td>
<td align="right">16.0%</td>
<td align="right">2,140</td>
<td align="right">15.5%</td>
<td align="right">6.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,778</td>
<td align="right">0.0%</td>
<td align="right">4,733</td>
<td align="right">0.0%</td>
<td align="right">166.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,497,330</td>
<td align="right">99.8%</td>
<td align="right">20,391,732</td>
<td align="right">99.9%</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,324</td>
<td align="right">0.1%</td>
<td align="right">8,324</td>
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
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
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
<td align="right">9,568</td>
<td align="right">100.0%</td>
<td align="right">9,593</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">857,176</td>
<td align="right">99.9%</td>
<td align="right">1,607,774</td>
<td align="right">100.0%</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
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
<td align="right">280</td>
<td align="right">100.0%</td>
<td align="right">280</td>
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
<td align="right">2,718,313</td>
<td align="right">91.3%</td>
<td align="right">3,880,980</td>
<td align="right">93.6%</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">81,742</td>
<td align="right">2.7%</td>
<td align="right">86,860</td>
<td align="right">2.1%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">171,520</td>
<td align="right">5.8%</td>
<td align="right">171,520</td>
<td align="right">4.1%</td>
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
<td align="right">1,800</td>
<td align="right">19.7%</td>
<td align="right">1,940</td>
<td align="right">20.9%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,355</td>
<td align="right">80.3%</td>
<td align="right">7,358</td>
<td align="right">79.1%</td>
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
<td align="left">property</td>
<td align="right">1,080</td>
<td align="right">60.0%</td>
<td align="right">1,180</td>
<td align="right">60.8%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">520</td>
<td align="right">28.9%</td>
<td align="right">560</td>
<td align="right">28.9%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">200</td>
<td align="right">11.1%</td>
<td align="right">200</td>
<td align="right">10.3%</td>
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
<td align="right">1,135,405</td>
<td align="right">97.5%</td>
<td align="right">1,651,196</td>
<td align="right">98.1%</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">28,117</td>
<td align="right">2.4%</td>
<td align="right">30,359</td>
<td align="right">1.8%</td>
<td align="right">8.0%</td>
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
<td align="right">620</td>
<td align="right">69.3%</td>
<td align="right">660</td>
<td align="right">70.4%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">275</td>
<td align="right">30.7%</td>
<td align="right">278</td>
<td align="right">29.6%</td>
<td align="right">1.1%</td>
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
<td align="right">200</td>
<td align="right">32.3%</td>
<td align="right">220</td>
<td align="right">33.3%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">420</td>
<td align="right">67.7%</td>
<td align="right">440</td>
<td align="right">66.7%</td>
<td align="right">4.8%</td>
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
<td align="right">6,364,908</td>
<td align="right">96.3%</td>
<td align="right">10,794,462</td>
<td align="right">96.6%</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">241,322</td>
<td align="right">3.7%</td>
<td align="right">379,557</td>
<td align="right">3.4%</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">280</td>
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
<td align="right">2,319</td>
<td align="right">46.6%</td>
<td align="right">2,480</td>
<td align="right">48.2%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,660</td>
<td align="right">53.4%</td>
<td align="right">2,661</td>
<td align="right">51.8%</td>
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
<td align="right">200</td>
<td align="right">8.6%</td>
<td align="right">220</td>
<td align="right">8.9%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">919</td>
<td align="right">39.6%</td>
<td align="right">1,000</td>
<td align="right">40.3%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">360</td>
<td align="right">15.5%</td>
<td align="right">380</td>
<td align="right">15.3%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">420</td>
<td align="right">18.1%</td>
<td align="right">440</td>
<td align="right">17.7%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">420</td>
<td align="right">18.1%</td>
<td align="right">440</td>
<td align="right">17.7%</td>
<td align="right">4.8%</td>
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
<td align="right">2,672,029</td>
<td align="right">100.0%</td>
<td align="right">3,214,006</td>
<td align="right">100.0%</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">480</td>
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
<td align="right">440</td>
<td align="right">100.0%</td>
<td align="right">440</td>
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
<td align="right">7,904,262</td>
<td align="right">3.1%</td>
<td align="right">13,814,341</td>
<td align="right">3.7%</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">80,091,316</td>
<td align="right">31.2%</td>
<td align="right">123,018,767</td>
<td align="right">32.8%</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">168,352,795</td>
<td align="right">65.5%</td>
<td align="right">236,955,705</td>
<td align="right">63.3%</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">666,432</td>
<td align="right">0.3%</td>
<td align="right">745,506</td>
<td align="right">0.2%</td>
<td align="right">11.9%</td>
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
<td align="right">3,337,872</td>
<td align="right">42.6%</td>
<td align="right">6,333,991</td>
<td align="right">46.1%</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">292,422</td>
<td align="right">3.7%</td>
<td align="right">531,228</td>
<td align="right">3.9%</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,691,581</td>
<td align="right">47.2%</td>
<td align="right">6,168,864</td>
<td align="right">44.9%</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">241,322</td>
<td align="right">3.1%</td>
<td align="right">379,557</td>
<td align="right">2.8%</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">80,780</td>
<td align="right">1.0%</td>
<td align="right">125,962</td>
<td align="right">0.9%</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">31,940</td>
<td align="right">0.4%</td>
<td align="right">34,820</td>
<td align="right">0.3%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,220</td>
<td align="right">0.2%</td>
<td align="right">19,820</td>
<td align="right">0.1%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">28,117</td>
<td align="right">0.4%</td>
<td align="right">30,359</td>
<td align="right">0.2%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,742</td>
<td align="right">1.0%</td>
<td align="right">86,860</td>
<td align="right">0.6%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">13,619</td>
<td align="right">0.2%</td>
<td align="right">13,628</td>
<td align="right">0.1%</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,438</td>
<td align="right">0.2%</td>
<td align="right">4,393</td>
<td align="right">0.6%</td>
<td align="right">205.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">410,240</td>
<td align="right">61.6%</td>
<td align="right">485,806</td>
<td align="right">65.2%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,053</td>
<td align="right">0.9%</td>
<td align="right">6,611</td>
<td align="right">0.9%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">61,881</td>
<td align="right">9.3%</td>
<td align="right">61,869</td>
<td align="right">8.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">171,520</td>
<td align="right">25.7%</td>
<td align="right">171,520</td>
<td align="right">23.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,380</td>
<td align="right">1.9%</td>
<td align="right">12,380</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,100</td>
<td align="right">0.2%</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">340</td>
<td align="right">0.1%</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
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
<td align="right">366,600</td>
<td align="right">1.4%</td>
<td align="right">581,812</td>
<td align="right">1.7%</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">19,467,772</td>
<td align="right">75.0%</td>
<td align="right">27,477,675</td>
<td align="right">80.0%</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">18,082,681</td>
<td align="right">69.7%</td>
<td align="right">25,222,881</td>
<td align="right">73.5%</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">33,020</td>
<td align="right">0.1%</td>
<td align="right">45,902</td>
<td align="right">0.1%</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,308,071</td>
<td align="right">28.2%</td>
<td align="right">8,526,254</td>
<td align="right">24.8%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,308,771</td>
<td align="right">28.2%</td>
<td align="right">8,526,954</td>
<td align="right">24.8%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,860,291</td>
<td align="right">30.3%</td>
<td align="right">9,112,074</td>
<td align="right">26.5%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,860,291</td>
<td align="right">30.3%</td>
<td align="right">9,112,074</td>
<td align="right">26.5%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">589,440</td>
<td align="right">2.3%</td>
<td align="right">625,920</td>
<td align="right">1.8%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">551,520</td>
<td align="right">2.1%</td>
<td align="right">585,120</td>
<td align="right">1.7%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">534,060</td>
<td align="right">2.1%</td>
<td align="right">535,340</td>
<td align="right">1.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">560</td>
<td align="right">0.0%</td>
<td align="right">560</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">5,244,049</td>
<td align="right"></td>
<td align="right">8,913,230</td>
<td align="right"></td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">680,150</td>
<td align="right"></td>
<td align="right">1,134,336</td>
<td align="right"></td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">104,606</td>
<td align="right">0.4%</td>
<td align="right">173,094</td>
<td align="right">0.4%</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">57,967</td>
<td align="right"></td>
<td align="right">88,738</td>
<td align="right"></td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">107,787,729</td>
<td align="right">107,787,729 / 0 !!</td>
<td align="right">154,549,462</td>
<td align="right">154,549,462 / 0 !!</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">134,749,820</td>
<td align="right">134,749,820 / 0 !!</td>
<td align="right">191,538,705</td>
<td align="right">191,538,705 / 0 !!</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">6,720,223</td>
<td align="right"></td>
<td align="right">9,441,837</td>
<td align="right"></td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,938,856</td>
<td align="right">44.6%</td>
<td align="right">18,168,452</td>
<td align="right">46.1%</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,950,968</td>
<td align="right"></td>
<td align="right">18,181,360</td>
<td align="right"></td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">98,992</td>
<td align="right">0.3%</td>
<td align="right">133,040</td>
<td align="right">0.3%</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,802,597</td>
<td align="right"></td>
<td align="right">22,574,120</td>
<td align="right"></td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,094,871</td>
<td align="right">55.4%</td>
<td align="right">21,254,068</td>
<td align="right">53.9%</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,891,273</td>
<td align="right">54.7%</td>
<td align="right">20,947,934</td>
<td align="right">53.1%</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">116,266,886</td>
<td align="right">116,266,886 / 0 !!</td>
<td align="right">150,007,484</td>
<td align="right">150,007,484 / 0 !!</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">116,002,967</td>
<td align="right">116,002,967 / 0 !!</td>
<td align="right">148,970,797</td>
<td align="right">148,970,797 / 0 !!</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">230,740</td>
<td align="right"></td>
<td align="right">254,990</td>
<td align="right"></td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,237,206</td>
<td align="right"></td>
<td align="right">2,357,941</td>
<td align="right"></td>
<td align="right">5.4%</td>
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
<td align="right">40</td>
<td align="right">3,840</td>
<td align="right">930,240</td>
<td align="right">40</td>
<td align="right">3,840</td>
<td align="right">930,240</td>
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
<td align="right">11</td>
<td align="right">0.7%</td>
<td align="right">27</td>
<td align="right">1.6%</td>
<td align="right">145.5%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">23</td>
<td align="right">0.3%</td>
<td align="right">49</td>
<td align="right">0.7%</td>
<td align="right">113.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">322,937,316</td>
<td align="right">1,412.3%</td>
<td align="right">423,718,828</td>
<td align="right">1,633.8%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">497</td>
<td align="right">7.5%</td>
<td align="right">638</td>
<td align="right">8.7%</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">22,866,768</td>
<td align="right"></td>
<td align="right">25,934,909</td>
<td align="right"></td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">6,583</td>
<td align="right"></td>
<td align="right">7,293</td>
<td align="right"></td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">4,531</td>
<td align="right">68.8%</td>
<td align="right">4,988</td>
<td align="right">68.4%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">4,744</td>
<td align="right">72.1%</td>
<td align="right">5,209</td>
<td align="right">71.4%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,555</td>
<td align="right">23.6%</td>
<td align="right">1,667</td>
<td align="right">22.9%</td>
<td align="right">7.2%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">8</td>
<td align="right">0.5%</td>
<td align="right">22</td>
<td align="right">1.3%</td>
<td align="right">175.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,555</td>
<td align="right"></td>
<td align="right">1,667</td>
<td align="right"></td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,547</td>
<td align="right">99.5%</td>
<td align="right">1,645</td>
<td align="right">98.7%</td>
<td align="right">6.3%</td>
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
<td align="right">40</td>
<td align="right">2.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">380</td>
<td align="right">24.4%</td>
<td align="right">340</td>
<td align="right">20.4%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">137</td>
<td align="right">8.8%</td>
<td align="right">215</td>
<td align="right">12.9%</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">320</td>
<td align="right">20.6%</td>
<td align="right">379</td>
<td align="right">22.7%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">224</td>
<td align="right">14.4%</td>
<td align="right">226</td>
<td align="right">13.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">333</td>
<td align="right">21.4%</td>
<td align="right">365</td>
<td align="right">21.9%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">101</td>
<td align="right">6.5%</td>
<td align="right">122</td>
<td align="right">7.3%</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">1.3%</td>
<td align="right">20</td>
<td align="right">1.2%</td>
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
<td align="right">340</td>
<td align="right">21.9%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">160</td>
<td align="right">10.3%</td>
<td align="right">500</td>
<td align="right">30.0%</td>
<td align="right">212.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">137</td>
<td align="right">8.8%</td>
<td align="right">94</td>
<td align="right">5.6%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">380</td>
<td align="right">24.4%</td>
<td align="right">480</td>
<td align="right">28.8%</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">257</td>
<td align="right">16.5%</td>
<td align="right">237</td>
<td align="right">14.2%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">233</td>
<td align="right">15.0%</td>
<td align="right">294</td>
<td align="right">17.6%</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">40</td>
<td align="right">2.6%</td>
<td align="right">40</td>
<td align="right">2.4%</td>
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
<td align="left">_IS_OP</td>
<td align="right">88</td>
<td align="right">375</td>
<td align="right">326.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,553,343</td>
<td align="right">26,651,939</td>
<td align="right">211.6%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">160</td>
<td align="right">480</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">160</td>
<td align="right">480</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">160</td>
<td align="right">480</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">160</td>
<td align="right">480</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">31,840</td>
<td align="right">64,160</td>
<td align="right">101.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">31,840</td>
<td align="right">64,160</td>
<td align="right">101.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">31,840</td>
<td align="right">64,160</td>
<td align="right">101.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">32,260</td>
<td align="right">64,580</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">32,260</td>
<td align="right">64,580</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">347,165</td>
<td align="right">684,961</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">106,155</td>
<td align="right">208,169</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">211,670</td>
<td align="right">414,418</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">105,835</td>
<td align="right">207,209</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">318,743</td>
<td align="right">623,795</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">141,675</td>
<td align="right">275,686</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">251,730</td>
<td align="right">487,836</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">251,730</td>
<td align="right">487,836</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">217,268</td>
<td align="right">420,334</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">290,308</td>
<td align="right">558,008</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">834,781</td>
<td align="right">1,579,257</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">232,068</td>
<td align="right">435,734</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">353,661</td>
<td align="right">659,379</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">353,661</td>
<td align="right">659,379</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">124,740</td>
<td align="right">227,417</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">40,640</td>
<td align="right">73,280</td>
<td align="right">80.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">176,418</td>
<td align="right">311,414</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">554,054</td>
<td align="right">959,370</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">142,022</td>
<td align="right">244,395</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,598,045</td>
<td align="right">2,644,659</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,598,045</td>
<td align="right">2,644,659</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,597,885</td>
<td align="right">2,644,179</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,699,060</td>
<td align="right">2,783,131</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,362,390</td>
<td align="right">2,172,082</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">20,096,914</td>
<td align="right">32,007,064</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,262,735</td>
<td align="right">2,006,821</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,342,794</td>
<td align="right">5,031,883</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,081,360</td>
<td align="right">3,094,440</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,002,600</td>
<td align="right">1,474,093</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,019,191</td>
<td align="right">4,402,588</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,024,011</td>
<td align="right">4,408,048</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">28,508,559</td>
<td align="right">15,527,757</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,420,149</td>
<td align="right">10,606,689</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">991,197</td>
<td align="right">1,394,860</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">937,571</td>
<td align="right">1,308,208</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">867,008</td>
<td align="right">1,204,158</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,797,590</td>
<td align="right">2,473,713</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,427,254</td>
<td align="right">3,282,883</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">11,082,546</td>
<td align="right">14,908,803</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">738,272</td>
<td align="right">973,419</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">755,030</td>
<td align="right">989,778</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">2,080</td>
<td align="right">2,720</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,554,152</td>
<td align="right">5,908,181</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">711,614</td>
<td align="right">915,172</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">713,690</td>
<td align="right">916,758</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,168,632</td>
<td align="right">2,737,650</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">9,723,468</td>
<td align="right">12,268,274</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">9,727,313</td>
<td align="right">12,272,121</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,367,714</td>
<td align="right">1,702,078</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,534,756</td>
<td align="right">1,906,264</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,303,500</td>
<td align="right">1,604,214</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">9,325,514</td>
<td align="right">11,366,603</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,431,549</td>
<td align="right">1,740,333</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,240,965</td>
<td align="right">3,914,760</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">647,735</td>
<td align="right">780,789</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,017,916</td>
<td align="right">2,429,498</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">662,960</td>
<td align="right">797,317</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">663,240</td>
<td align="right">797,597</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">734,175</td>
<td align="right">881,309</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">9,207,865</td>
<td align="right">11,019,087</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,250,029</td>
<td align="right">1,486,100</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">634,703</td>
<td align="right">737,959</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">634,703</td>
<td align="right">737,959</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">626,633</td>
<td align="right">728,322</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">627,053</td>
<td align="right">728,742</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">84,560</td>
<td align="right">98,000</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">84,560</td>
<td align="right">98,000</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">84,560</td>
<td align="right">98,000</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">84,700</td>
<td align="right">98,140</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">4,337,867</td>
<td align="right">5,022,794</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">86,120</td>
<td align="right">99,560</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,595,412</td>
<td align="right">7,557,517</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">16,561,458</td>
<td align="right">18,972,540</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,277,115</td>
<td align="right">1,456,249</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">14,220</td>
<td align="right">16,140</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">14,220</td>
<td align="right">16,140</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">22,866,768</td>
<td align="right">25,934,909</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">20,345,029</td>
<td align="right">22,792,856</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,469,388</td>
<td align="right">7,231,086</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,469,388</td>
<td align="right">7,231,086</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,102,536</td>
<td align="right">3,464,328</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">6,356,923</td>
<td align="right">7,084,355</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">606,177</td>
<td align="right">673,046</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">8,669,963</td>
<td align="right">9,610,208</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">6,301,463</td>
<td align="right">6,958,515</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,108,260</td>
<td align="right">1,203,940</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">593,340</td>
<td align="right">638,519</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">5,554,414</td>
<td align="right">5,976,695</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,206,075</td>
<td align="right">2,372,092</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,188,440</td>
<td align="right">1,268,120</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">5,120</td>
<td align="right">5,440</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">5,120</td>
<td align="right">5,440</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,679,168</td>
<td align="right">1,783,350</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">542,703</td>
<td align="right">575,613</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,081,640</td>
<td align="right">1,145,960</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,720</td>
<td align="right">5,000</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,618,960</td>
<td align="right">1,714,320</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">543,360</td>
<td align="right">575,360</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">5,982,720</td>
<td align="right">6,334,720</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,195,948</td>
<td align="right">2,275,235</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,195,948</td>
<td align="right">2,275,235</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">9,118</td>
<td align="right">9,440</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">1,044,620</td>
<td align="right">1,076,620</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">613,418</td>
<td align="right">629,053</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,159,439</td>
<td align="right">3,208,030</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,845</td>
<td align="right">3,854</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">511,539</td>
<td align="right">512,465</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">507,843</td>
<td align="right">508,742</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">510,123</td>
<td align="right">511,022</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">17,442</td>
<td align="right">17,458</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,034,545</td>
<td align="right">1,035,460</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">506,700</td>
<td align="right">507,020</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">3,845</td>
<td align="right">3,847</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">43,516</td>
<td align="right">43,514</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,013,960</td>
<td align="right">1,013,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,008,000</td>
<td align="right">1,008,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">506,560</td>
<td align="right">506,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">506,560</td>
<td align="right">506,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">501,440</td>
<td align="right">501,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">12,160</td>
<td align="right">12,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right"></td>
<td align="right">26,563,962</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">561</td>
<td align="right">562</td>
<td align="right">0.2%</td>
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
<td align="right">8</td>
<td align="right">13</td>
<td align="right">62.5%</td>
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
<td align="right">13</td>
<td align="right">62.5%</td>
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
Stats gathered on: 2024-10-21
