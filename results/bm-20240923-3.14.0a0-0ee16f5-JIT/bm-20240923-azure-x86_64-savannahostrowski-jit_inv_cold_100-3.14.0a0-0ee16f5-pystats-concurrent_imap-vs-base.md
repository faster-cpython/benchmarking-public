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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">38,140</td>
<td align="right">3,781,394</td>
<td align="right">9,814.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">12,080</td>
<td align="right">337,720</td>
<td align="right">2,695.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,480</td>
<td align="right">569,772</td>
<td align="right">1,601.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">576,866</td>
<td align="right">5,400,692</td>
<td align="right">836.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">96,527</td>
<td align="right">808,441</td>
<td align="right">737.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">54,680</td>
<td align="right">380,178</td>
<td align="right">595.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">81,676</td>
<td align="right">449,549</td>
<td align="right">450.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,277,882</td>
<td align="right">5,800,847</td>
<td align="right">353.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">339,015</td>
<td align="right">987,710</td>
<td align="right">191.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,078,982</td>
<td align="right">2,510,573</td>
<td align="right">132.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">430</td>
<td align="right">931</td>
<td align="right">116.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">633,965</td>
<td align="right">1,308,080</td>
<td align="right">106.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">809,941</td>
<td align="right">1,566,902</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,262,562</td>
<td align="right">17,846,083</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,480,270</td>
<td align="right">2,836,156</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">39,080</td>
<td align="right">72,403</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">800</td>
<td align="right">1,440</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,723,275</td>
<td align="right">6,697,435</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,943,750</td>
<td align="right">3,490,973</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,227,524</td>
<td align="right">16,506,983</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,513,623</td>
<td align="right">9,756,149</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,819,525</td>
<td align="right">3,121,009</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,839,853</td>
<td align="right">4,771,734</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,770,307</td>
<td align="right">9,661,126</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,103,738</td>
<td align="right">11,868,315</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">668,792</td>
<td align="right">1,117,005</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">16,300,309</td>
<td align="right">27,045,175</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">577,542</td>
<td align="right">951,763</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">211,108</td>
<td align="right">346,252</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">16,818</td>
<td align="right">27,520</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">54,960</td>
<td align="right">89,520</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">829,230</td>
<td align="right">1,343,464</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,434,004</td>
<td align="right">3,929,372</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">789,157</td>
<td align="right">1,273,857</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,122,625</td>
<td align="right">6,634,847</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">561,561</td>
<td align="right">902,589</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,407,117</td>
<td align="right">2,260,665</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,343,907</td>
<td align="right">5,363,305</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">344,104</td>
<td align="right">550,956</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">136,360</td>
<td align="right">218,213</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2,140</td>
<td align="right">3,420</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">112,155</td>
<td align="right">179,194</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">224,426</td>
<td align="right">358,496</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">802,216</td>
<td align="right">1,279,041</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">800,161</td>
<td align="right">1,275,185</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">863,616</td>
<td align="right">1,375,321</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">934,661</td>
<td align="right">1,482,965</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">61,820</td>
<td align="right">97,980</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">571,538</td>
<td align="right">903,222</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">295,147</td>
<td align="right">464,326</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">63,600</td>
<td align="right">99,760</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">3,791,354</td>
<td align="right">5,929,698</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">912,076</td>
<td align="right">1,425,381</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">182,440</td>
<td align="right">284,055</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">44,866,460</td>
<td align="right">69,416,407</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,605,222</td>
<td align="right">4,025,409</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,721,069</td>
<td align="right">5,744,165</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">755,123</td>
<td align="right">1,161,970</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">379,913</td>
<td align="right">583,924</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,008,320</td>
<td align="right">3,072,756</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">128,062</td>
<td align="right">195,864</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">263,035</td>
<td align="right">400,112</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">246,301</td>
<td align="right">371,716</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">221,890</td>
<td align="right">334,019</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,042,945</td>
<td align="right">4,555,567</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">139,000</td>
<td align="right">207,118</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,266,362</td>
<td align="right">12,311,064</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,119,052</td>
<td align="right">6,127,551</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">148,473</td>
<td align="right">220,308</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,999,199</td>
<td align="right">4,436,511</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,628,288</td>
<td align="right">11,223,493</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">179,754</td>
<td align="right">262,312</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,811,081</td>
<td align="right">2,599,827</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,142,141</td>
<td align="right">1,626,265</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">186,017</td>
<td align="right">264,602</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,232,746</td>
<td align="right">5,955,300</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">27,480</td>
<td align="right">38,500</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">283,852</td>
<td align="right">396,782</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,193,310</td>
<td align="right">3,020,586</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">98,067</td>
<td align="right">134,990</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">924,516</td>
<td align="right">1,250,930</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">32,920</td>
<td align="right">44,260</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">32,920</td>
<td align="right">44,260</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,240</td>
<td align="right">1,660</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">570,305</td>
<td align="right">757,551</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">31,238</td>
<td align="right">41,416</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">181,690</td>
<td align="right">240,427</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,114,538</td>
<td align="right">22,294,278</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,278</td>
<td align="right">22,344</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">29,900</td>
<td align="right">38,380</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,971,830</td>
<td align="right">17,932,355</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,038,715</td>
<td align="right">1,316,705</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,122,651</td>
<td align="right">7,602,951</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,860,892</td>
<td align="right">10,315,328</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">24,800</td>
<td align="right">28,780</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">658,720</td>
<td align="right">763,128</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">24,320</td>
<td align="right">28,160</td>
<td align="right">15.8%</td>
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
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">672,722</td>
<td align="right">772,561</td>
<td align="right">14.8%</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">12,800</td>
<td align="right">14,540</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,854,829</td>
<td align="right">8,730,891</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">35,320</td>
<td align="right">39,160</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">50,880</td>
<td align="right">55,680</td>
<td align="right">9.4%</td>
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
<td align="left">CALL_KW_NON_PY</td>
<td align="right">89,020</td>
<td align="right">96,380</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">568,380</td>
<td align="right">613,430</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">29,012</td>
<td align="right">31,300</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">38,720</td>
<td align="right">41,600</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,155,961</td>
<td align="right">1,234,790</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">59,840</td>
<td align="right">63,680</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">87,817</td>
<td align="right">93,080</td>
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
<td align="left">CALL_STR_1</td>
<td align="right">11,260</td>
<td align="right">11,900</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,142</td>
<td align="right">46,583</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">109,120</td>
<td align="right">114,880</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,308,067</td>
<td align="right">2,414,007</td>
<td align="right">4.6%</td>
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
<td align="right">26,928</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">17,884</td>
<td align="right">17,882</td>
<td align="right">-0.0%</td>
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
<td align="right">5,356,626</td>
<td align="right">73.2%</td>
<td align="right">60.5%</td>
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
<td align="right">1,956,978</td>
<td align="right">26.7%</td>
<td align="right">18.1%</td>
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
<td align="right">6,059</td>
<td align="right">90.7%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">615</td>
<td align="right">10.2%</td>
<td align="right">620</td>
<td align="right">9.3%</td>
<td align="right">0.8%</td>
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
<td align="right">1.7%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">659</td>
<td align="right">12.2%</td>
<td align="right">778</td>
<td align="right">12.8%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,393</td>
<td align="right">25.7%</td>
<td align="right">1,568</td>
<td align="right">25.9%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2,688</td>
<td align="right">49.6%</td>
<td align="right">2,973</td>
<td align="right">49.1%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">600</td>
<td align="right">11.1%</td>
<td align="right">640</td>
<td align="right">10.6%</td>
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
<td align="right">448,473</td>
<td align="right">41.3%</td>
<td align="right">455.2%</td>
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
<td align="right">635,256</td>
<td align="right">58.6%</td>
<td align="right">33.4%</td>
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
<td align="right">836</td>
<td align="right">77.7%</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">240</td>
<td align="right">26.8%</td>
<td align="right">240</td>
<td align="right">22.3%</td>
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
<td align="right">836</td>
<td align="right">100.0%</td>
<td align="right">27.4%</td>
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
<td align="right">22,480,443</td>
<td align="right">99.9%</td>
<td align="right">36.6%</td>
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
<td align="right">1,480</td>
<td align="right">0.0%</td>
<td align="right">25.4%</td>
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
<td align="right">13,940</td>
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
<td align="right">461,498</td>
<td align="right">8.9%</td>
<td align="right">57.8%</td>
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
<td align="right">4,742,010</td>
<td align="right">90.9%</td>
<td align="right">27.3%</td>
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
<td align="right">7,631</td>
<td align="right">0.1%</td>
<td align="right">25.7%</td>
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
<td align="right">1,388</td>
<td align="right">47.3%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,531</td>
<td align="right">54.4%</td>
<td align="right">1,549</td>
<td align="right">52.7%</td>
<td align="right">1.2%</td>
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
<td align="right">240</td>
<td align="right">17.3%</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">340</td>
<td align="right">26.5%</td>
<td align="right">360</td>
<td align="right">25.9%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">777</td>
<td align="right">60.5%</td>
<td align="right">788</td>
<td align="right">56.8%</td>
<td align="right">1.4%</td>
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
<td align="right">1,461,769</td>
<td align="right">100.0%</td>
<td align="right">34.1%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">31,940</td>
<td align="right">0.4%</td>
<td align="right">567,968</td>
<td align="right">4.4%</td>
<td align="right">1,678.2%</td>
</tr>
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
<td align="right">12,204,243</td>
<td align="right">95.5%</td>
<td align="right">66.8%</td>
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
<td align="right">1,184</td>
<td align="right">65.6%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">620</td>
<td align="right">40.3%</td>
<td align="right">620</td>
<td align="right">34.4%</td>
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
<td align="right">220</td>
<td align="right">23.9%</td>
<td align="right">364</td>
<td align="right">30.7%</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">220</td>
<td align="right">23.9%</td>
<td align="right">320</td>
<td align="right">27.0%</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">260</td>
<td align="right">28.3%</td>
<td align="right">280</td>
<td align="right">23.6%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">23.9%</td>
<td align="right">220</td>
<td align="right">18.6%</td>
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
<td align="right">5,713,536</td>
<td align="right">11.8%</td>
<td align="right">54.8%</td>
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
<td align="right">42,175,091</td>
<td align="right">87.0%</td>
<td align="right">31.9%</td>
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
<td align="right">574,642</td>
<td align="right">1.2%</td>
<td align="right">18.3%</td>
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
<td align="right">13,669</td>
<td align="right">33.3%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">25,663</td>
<td align="right">67.1%</td>
<td align="right">27,364</td>
<td align="right">66.7%</td>
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
<td align="right">1.5%</td>
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
<td align="left">class method obj</td>
<td align="right">640</td>
<td align="right">5.1%</td>
<td align="right">740</td>
<td align="right">5.4%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,009</td>
<td align="right">24.0%</td>
<td align="right">3,319</td>
<td align="right">24.3%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,219</td>
<td align="right">33.6%</td>
<td align="right">4,553</td>
<td align="right">33.3%</td>
<td align="right">7.9%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">2,016</td>
<td align="right">16.0%</td>
<td align="right">2,084</td>
<td align="right">15.2%</td>
<td align="right">3.4%</td>
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
<td align="right">4,883</td>
<td align="right">0.0%</td>
<td align="right">174.6%</td>
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
<td align="right">18,261,481</td>
<td align="right">99.9%</td>
<td align="right">46.1%</td>
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
<td align="right">8,322</td>
<td align="right">0.0%</td>
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
<td align="right">9,599</td>
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
<td align="right">1,368,561</td>
<td align="right">100.0%</td>
<td align="right">59.7%</td>
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
<td align="right">3,531,700</td>
<td align="right">93.0%</td>
<td align="right">29.9%</td>
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
<td align="right">2.3%</td>
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
<td align="right">4.5%</td>
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
<td align="right">7,360</td>
<td align="right">79.1%</td>
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
<td align="right">1,482,675</td>
<td align="right">97.9%</td>
<td align="right">30.6%</td>
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
<td align="right">30,360</td>
<td align="right">2.0%</td>
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
<td align="right">70.2%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">275</td>
<td align="right">30.7%</td>
<td align="right">280</td>
<td align="right">29.8%</td>
<td align="right">1.8%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">241,322</td>
<td align="right">3.7%</td>
<td align="right">366,482</td>
<td align="right">3.8%</td>
<td align="right">51.9%</td>
</tr>
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
<td align="right">9,375,128</td>
<td align="right">96.2%</td>
<td align="right">47.3%</td>
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
<td align="right">2,574</td>
<td align="right">49.2%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,660</td>
<td align="right">53.4%</td>
<td align="right">2,660</td>
<td align="right">50.8%</td>
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
<td align="left">mapping</td>
<td align="right">919</td>
<td align="right">39.6%</td>
<td align="right">1,074</td>
<td align="right">41.7%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">360</td>
<td align="right">15.5%</td>
<td align="right">400</td>
<td align="right">15.5%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">200</td>
<td align="right">8.6%</td>
<td align="right">220</td>
<td align="right">8.5%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">420</td>
<td align="right">18.1%</td>
<td align="right">440</td>
<td align="right">17.1%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">420</td>
<td align="right">18.1%</td>
<td align="right">440</td>
<td align="right">17.1%</td>
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
<td align="right">3,078,014</td>
<td align="right">100.0%</td>
<td align="right">15.2%</td>
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
<td align="right">13,154,683</td>
<td align="right">3.3%</td>
<td align="right">66.4%</td>
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
<td align="right">132,984,257</td>
<td align="right">33.1%</td>
<td align="right">66.0%</td>
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
<td align="right">254,412,179</td>
<td align="right">63.4%</td>
<td align="right">51.1%</td>
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
<td align="right">790,666</td>
<td align="right">0.2%</td>
<td align="right">18.6%</td>
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
<td align="right">31,940</td>
<td align="right">0.4%</td>
<td align="right">567,968</td>
<td align="right">4.3%</td>
<td align="right">1,678.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">80,780</td>
<td align="right">1.0%</td>
<td align="right">448,473</td>
<td align="right">3.4%</td>
<td align="right">455.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,337,872</td>
<td align="right">42.6%</td>
<td align="right">5,356,626</td>
<td align="right">41.0%</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">292,422</td>
<td align="right">3.7%</td>
<td align="right">461,498</td>
<td align="right">3.5%</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,691,581</td>
<td align="right">47.2%</td>
<td align="right">5,713,536</td>
<td align="right">43.7%</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">241,322</td>
<td align="right">3.1%</td>
<td align="right">366,482</td>
<td align="right">2.8%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,220</td>
<td align="right">0.2%</td>
<td align="right">19,820</td>
<td align="right">0.2%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">28,117</td>
<td align="right">0.4%</td>
<td align="right">30,360</td>
<td align="right">0.2%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,742</td>
<td align="right">1.0%</td>
<td align="right">86,860</td>
<td align="right">0.7%</td>
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
<td align="right">4,543</td>
<td align="right">0.6%</td>
<td align="right">215.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,053</td>
<td align="right">0.9%</td>
<td align="right">7,611</td>
<td align="right">0.9%</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">410,240</td>
<td align="right">61.6%</td>
<td align="right">499,310</td>
<td align="right">60.8%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">61,881</td>
<td align="right">9.3%</td>
<td align="right">61,852</td>
<td align="right">7.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">171,520</td>
<td align="right">25.7%</td>
<td align="right">171,520</td>
<td align="right">20.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,380</td>
<td align="right">1.9%</td>
<td align="right">12,380</td>
<td align="right">1.5%</td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">340</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">30,230</td>
<td align="right">3.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">30,230</td>
<td align="right">3.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right"></td>
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
<td align="right">515,478</td>
<td align="right">1.6%</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">33,020</td>
<td align="right">0.1%</td>
<td align="right">44,384</td>
<td align="right">0.1%</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">19,467,772</td>
<td align="right">75.0%</td>
<td align="right">25,069,248</td>
<td align="right">78.5%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">18,082,681</td>
<td align="right">69.7%</td>
<td align="right">23,189,857</td>
<td align="right">72.6%</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,308,071</td>
<td align="right">28.2%</td>
<td align="right">8,150,851</td>
<td align="right">25.5%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,308,771</td>
<td align="right">28.2%</td>
<td align="right">8,151,551</td>
<td align="right">25.5%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,860,291</td>
<td align="right">30.3%</td>
<td align="right">8,736,671</td>
<td align="right">27.4%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,860,291</td>
<td align="right">30.3%</td>
<td align="right">8,736,671</td>
<td align="right">27.4%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">589,440</td>
<td align="right">2.3%</td>
<td align="right">625,920</td>
<td align="right">2.0%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">551,520</td>
<td align="right">2.1%</td>
<td align="right">585,120</td>
<td align="right">1.8%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">534,060</td>
<td align="right">2.1%</td>
<td align="right">535,340</td>
<td align="right">1.7%</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">98,992</td>
<td align="right">0.3%</td>
<td align="right">263,270</td>
<td align="right">0.7%</td>
<td align="right">166.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">104,606</td>
<td align="right">0.4%</td>
<td align="right">173,595</td>
<td align="right">0.5%</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">107,787,729</td>
<td align="right">107,787,729 / 0 !!</td>
<td align="right">162,989,173</td>
<td align="right">162,989,173 / 0 !!</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">5,244,049</td>
<td align="right"></td>
<td align="right">7,869,805</td>
<td align="right"></td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">680,150</td>
<td align="right"></td>
<td align="right">994,624</td>
<td align="right"></td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">134,749,820</td>
<td align="right">134,749,820 / 0 !!</td>
<td align="right">189,657,479</td>
<td align="right">189,657,479 / 0 !!</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,938,856</td>
<td align="right">44.6%</td>
<td align="right">16,884,201</td>
<td align="right">45.3%</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,950,968</td>
<td align="right"></td>
<td align="right">16,897,084</td>
<td align="right"></td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">6,720,223</td>
<td align="right"></td>
<td align="right">8,692,672</td>
<td align="right"></td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,802,597</td>
<td align="right"></td>
<td align="right">21,580,168</td>
<td align="right"></td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,094,871</td>
<td align="right">55.4%</td>
<td align="right">20,395,605</td>
<td align="right">54.7%</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,891,273</td>
<td align="right">54.7%</td>
<td align="right">19,958,740</td>
<td align="right">53.5%</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">57,967</td>
<td align="right"></td>
<td align="right">64,695</td>
<td align="right"></td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">230,740</td>
<td align="right"></td>
<td align="right">244,468</td>
<td align="right"></td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,237,206</td>
<td align="right"></td>
<td align="right">2,351,258</td>
<td align="right"></td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">116,266,886</td>
<td align="right">116,266,886 / 0 !!</td>
<td align="right">110,982,877</td>
<td align="right">110,982,877 / 0 !!</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">116,002,967</td>
<td align="right">116,002,967 / 0 !!</td>
<td align="right">118,370,193</td>
<td align="right">118,370,193 / 0 !!</td>
<td align="right">2.0%</td>
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
<td align="right">937,000</td>
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
<td align="right">23</td>
<td align="right">0.3%</td>
<td align="right">5,455</td>
<td align="right">3.0%</td>
<td align="right">23,617.4%</td>
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
<td align="right">156,860</td>
<td align="right">85.9%</td>
<td align="right">9,987.5%</td>
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
<td align="right">182,599</td>
<td align="right"></td>
<td align="right">2,673.8%</td>
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
<td align="right">55,383</td>
<td align="right">30.3%</td>
<td align="right">1,067.4%</td>
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
<td align="right">25,162</td>
<td align="right">13.8%</td>
<td align="right">455.3%</td>
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
<td align="right">15,717,935</td>
<td align="right"></td>
<td align="right">-31.3%</td>
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
<td align="right">254,901,258</td>
<td align="right">1,621.7%</td>
<td align="right">-21.1%</td>
</tr>
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
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">-18.2%</td>
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
<td align="right">577</td>
<td align="right">0.3%</td>
<td align="right">16.1%</td>
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
<td align="right">85</td>
<td align="right">0.0%</td>
<td align="right">85 / 0 !!</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,547</td>
<td align="right">99.5%</td>
<td align="right">156,854</td>
<td align="right">100.0%</td>
<td align="right">10,039.2%</td>
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
<td align="right">156,860</td>
<td align="right"></td>
<td align="right">9,987.5%</td>
</tr>
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
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">-25.0%</td>
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
<td align="right">9,940</td>
<td align="right">6.3%</td>
<td align="right">2,515.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">137</td>
<td align="right">8.8%</td>
<td align="right">15,352</td>
<td align="right">9.8%</td>
<td align="right">11,105.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">320</td>
<td align="right">20.6%</td>
<td align="right">48,438</td>
<td align="right">30.9%</td>
<td align="right">15,036.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">224</td>
<td align="right">14.4%</td>
<td align="right">27,673</td>
<td align="right">17.6%</td>
<td align="right">12,254.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">333</td>
<td align="right">21.4%</td>
<td align="right">46,411</td>
<td align="right">29.6%</td>
<td align="right">13,837.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">101</td>
<td align="right">6.5%</td>
<td align="right">8,566</td>
<td align="right">5.5%</td>
<td align="right">8,381.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">1.3%</td>
<td align="right">480</td>
<td align="right">0.3%</td>
<td align="right">2,300.0%</td>
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
<td align="right">2,918</td>
<td align="right">1.9%</td>
<td align="right">758.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">160</td>
<td align="right">10.3%</td>
<td align="right">17,154</td>
<td align="right">10.9%</td>
<td align="right">10,621.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">137</td>
<td align="right">8.8%</td>
<td align="right">5,708</td>
<td align="right">3.6%</td>
<td align="right">4,066.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">380</td>
<td align="right">24.4%</td>
<td align="right">63,408</td>
<td align="right">40.4%</td>
<td align="right">16,586.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">257</td>
<td align="right">16.5%</td>
<td align="right">41,594</td>
<td align="right">26.5%</td>
<td align="right">16,084.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">233</td>
<td align="right">15.0%</td>
<td align="right">22,538</td>
<td align="right">14.4%</td>
<td align="right">9,573.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">40</td>
<td align="right">2.6%</td>
<td align="right">3,534</td>
<td align="right">2.3%</td>
<td align="right">8,735.0%</td>
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
<td align="left">_DEOPT</td>
<td align="right">3,845</td>
<td align="right">50,279</td>
<td align="right">1,207.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">88</td>
<td align="right">388</td>
<td align="right">340.9%</td>
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
<td align="left">_TO_BOOL_NONE</td>
<td align="right">43,516</td>
<td align="right">4</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">32,260</td>
<td align="right">64,160</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">32,260</td>
<td align="right">64,160</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">31,840</td>
<td align="right">63,268</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">31,840</td>
<td align="right">63,268</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">31,840</td>
<td align="right">63,268</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">9,118</td>
<td align="right">482</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">3,845</td>
<td align="right">260</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">711,614</td>
<td align="right">1,185,988</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">141,675</td>
<td align="right">234,961</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">501,440</td>
<td align="right">174,595</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,250,029</td>
<td align="right">436,076</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,013,960</td>
<td align="right">362,602</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,008,000</td>
<td align="right">361,169</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">506,560</td>
<td align="right">182,527</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">506,560</td>
<td align="right">182,527</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">506,700</td>
<td align="right">184,082</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">40,640</td>
<td align="right">66,500</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">290,308</td>
<td align="right">474,540</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">106,155</td>
<td align="right">172,173</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">318,743</td>
<td align="right">516,563</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">211,670</td>
<td align="right">342,426</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">105,835</td>
<td align="right">171,213</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">217,268</td>
<td align="right">346,272</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">12,160</td>
<td align="right">4,960</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,595,412</td>
<td align="right">2,787,366</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">232,068</td>
<td align="right">361,672</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">353,661</td>
<td align="right">547,251</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">353,661</td>
<td align="right">547,251</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">5,554,414</td>
<td align="right">2,532,682</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">9,207,865</td>
<td align="right">4,337,641</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,427,254</td>
<td align="right">1,175,695</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,159,439</td>
<td align="right">1,564,014</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">662,960</td>
<td align="right">331,633</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">663,240</td>
<td align="right">332,525</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,469,388</td>
<td align="right">3,313,944</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,469,388</td>
<td align="right">3,313,944</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">6,356,923</td>
<td align="right">3,380,565</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">1,044,620</td>
<td align="right">567,562</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">16,561,458</td>
<td align="right">9,140,533</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,303,500</td>
<td align="right">727,560</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">8,669,963</td>
<td align="right">4,896,844</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,534,756</td>
<td align="right">2,198,919</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,367,714</td>
<td align="right">814,438</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,017,916</td>
<td align="right">1,210,406</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">142,022</td>
<td align="right">85,664</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">937,571</td>
<td align="right">568,873</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,188,440</td>
<td align="right">734,972</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">647,735</td>
<td align="right">401,676</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,108,260</td>
<td align="right">692,895</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,034,545</td>
<td align="right">680,291</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,206,075</td>
<td align="right">1,501,207</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">22,866,768</td>
<td align="right">15,717,935</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,019,191</td>
<td align="right">2,091,764</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,024,011</td>
<td align="right">2,096,804</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">124,740</td>
<td align="right">86,564</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,699,060</td>
<td align="right">1,201,355</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">4,337,867</td>
<td align="right">3,069,638</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">734,175</td>
<td align="right">520,860</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">20,096,914</td>
<td align="right">14,343,527</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">713,690</td>
<td align="right">514,663</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,554,152</td>
<td align="right">3,284,432</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,560</td>
<td align="right">1,140</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,081,360</td>
<td align="right">1,523,371</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,362,390</td>
<td align="right">997,458</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,240,965</td>
<td align="right">2,384,026</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">9,727,313</td>
<td align="right">7,176,809</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">9,723,468</td>
<td align="right">7,176,549</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,679,168</td>
<td align="right">1,270,665</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,262,735</td>
<td align="right">956,005</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">738,272</td>
<td align="right">564,940</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">867,008</td>
<td align="right">669,017</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,597,885</td>
<td align="right">1,245,796</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,598,045</td>
<td align="right">1,246,276</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,598,045</td>
<td align="right">1,246,276</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,342,794</td>
<td align="right">2,614,247</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">755,030</td>
<td align="right">917,786</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">28,508,559</td>
<td align="right">22,415,950</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">347,165</td>
<td align="right">421,306</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">11,082,546</td>
<td align="right">8,751,526</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,420,149</td>
<td align="right">5,992,667</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,102,536</td>
<td align="right">2,518,258</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,431,549</td>
<td align="right">1,180,994</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,002,600</td>
<td align="right">1,177,672</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,618,960</td>
<td align="right">1,342,080</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">554,054</td>
<td align="right">460,426</td>
<td align="right">-16.9%</td>
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
<td align="right">98,000</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">86,120</td>
<td align="right">99,140</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">20,345,029</td>
<td align="right">17,318,933</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">176,418</td>
<td align="right">150,306</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,277,115</td>
<td align="right">1,093,736</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,081,640</td>
<td align="right">934,623</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,195,948</td>
<td align="right">1,928,009</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,195,948</td>
<td align="right">1,928,009</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,168,632</td>
<td align="right">2,427,923</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,797,590</td>
<td align="right">2,010,348</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">2,080</td>
<td align="right">2,300</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">14,220</td>
<td align="right">15,680</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">14,220</td>
<td align="right">15,680</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">991,197</td>
<td align="right">1,069,802</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">634,703</td>
<td align="right">584,654</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">634,703</td>
<td align="right">584,654</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">9,325,514</td>
<td align="right">8,623,967</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">606,177</td>
<td align="right">649,136</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">834,781</td>
<td align="right">777,284</td>
<td align="right">-6.9%</td>
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
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,553,343</td>
<td align="right">8,020,554</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,720</td>
<td align="right">5,000</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">543,360</td>
<td align="right">575,360</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">626,633</td>
<td align="right">661,362</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">627,053</td>
<td align="right">661,782</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">6,301,463</td>
<td align="right">6,527,123</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">593,340</td>
<td align="right">614,356</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">542,703</td>
<td align="right">561,818</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">510,123</td>
<td align="right">498,990</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">251,730</td>
<td align="right">246,249</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">251,730</td>
<td align="right">246,249</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">507,843</td>
<td align="right">500,130</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">613,418</td>
<td align="right">610,082</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">5,982,720</td>
<td align="right">6,009,720</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">511,539</td>
<td align="right">509,386</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">17,442</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_BUILD_LIST</td>
<td align="right">420</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">420</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">140</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">16,328,017</td>
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
<td align="right">15,750</td>
<td align="right">2,707.5%</td>
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
<td align="right">11</td>
<td align="right">37.5%</td>
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
<td align="right">11</td>
<td align="right">37.5%</td>
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
