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
<td align="right">949,650</td>
<td align="right">2,389.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">12,080</td>
<td align="right">74,960</td>
<td align="right">520.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">96,527</td>
<td align="right">393,548</td>
<td align="right">307.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">54,680</td>
<td align="right">187,940</td>
<td align="right">243.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,480</td>
<td align="right">107,153</td>
<td align="right">220.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">576,866</td>
<td align="right">1,548,119</td>
<td align="right">168.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">81,676</td>
<td align="right">217,037</td>
<td align="right">165.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,277,882</td>
<td align="right">1,947,580</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">26,520</td>
<td align="right">13,720</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">133,380</td>
<td align="right">69,380</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">133,660</td>
<td align="right">69,660</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">75,016</td>
<td align="right">39,180</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,308,067</td>
<td align="right">1,207,303</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">16,322</td>
<td align="right">8,640</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">38,080</td>
<td align="right">20,160</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">10,880</td>
<td align="right">5,760</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,440</td>
<td align="right">2,880</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">81,594</td>
<td align="right">43,200</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,529,020</td>
<td align="right">3,457,020</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">109,120</td>
<td align="right">57,920</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,460</td>
<td align="right">2,900</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">71,120</td>
<td align="right">37,840</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">71,120</td>
<td align="right">37,840</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,155,961</td>
<td align="right">617,644</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,142</td>
<td align="right">23,665</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">38,720</td>
<td align="right">20,800</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">568,380</td>
<td align="right">306,701</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">89,020</td>
<td align="right">48,060</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">11,260</td>
<td align="right">6,140</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">50,880</td>
<td align="right">27,840</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,278</td>
<td align="right">9,575</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">17,260</td>
<td align="right">9,580</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,854,829</td>
<td align="right">4,369,725</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">29,012</td>
<td align="right">16,160</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">658,720</td>
<td align="right">370,745</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">35,320</td>
<td align="right">19,960</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">59,840</td>
<td align="right">34,240</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">672,722</td>
<td align="right">387,027</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,220</td>
<td align="right">10,540</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">24,320</td>
<td align="right">14,080</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">24,940</td>
<td align="right">14,700</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">31,238</td>
<td align="right">18,440</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">87,817</td>
<td align="right">51,841</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">24,800</td>
<td align="right">14,700</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,260</td>
<td align="right">15,020</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">12,680</td>
<td align="right">7,560</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">12,680</td>
<td align="right">7,560</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,811,081</td>
<td align="right">1,116,829</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,122,651</td>
<td align="right">3,797,463</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">6,800</td>
<td align="right">4,240</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,860,892</td>
<td align="right">5,589,734</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">12,800</td>
<td align="right">8,100</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,038,715</td>
<td align="right">658,843</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">29,900</td>
<td align="right">19,180</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,971,830</td>
<td align="right">8,971,866</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,114,538</td>
<td align="right">11,141,033</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,240</td>
<td align="right">1,660</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">181,690</td>
<td align="right">120,263</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">570,305</td>
<td align="right">380,187</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">924,516</td>
<td align="right">625,461</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">32,920</td>
<td align="right">22,302</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">32,920</td>
<td align="right">22,302</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">98,067</td>
<td align="right">67,408</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,193,310</td>
<td align="right">1,512,727</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">829,230</td>
<td align="right">578,330</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">283,852</td>
<td align="right">199,479</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">186,017</td>
<td align="right">131,097</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,232,746</td>
<td align="right">2,983,698</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">27,480</td>
<td align="right">19,422</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,142,141</td>
<td align="right">815,999</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">179,754</td>
<td align="right">131,296</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,628,288</td>
<td align="right">5,600,609</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,999,199</td>
<td align="right">2,213,998</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,119,052</td>
<td align="right">3,052,565</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">246,301</td>
<td align="right">182,628</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,042,945</td>
<td align="right">2,262,341</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,266,362</td>
<td align="right">6,162,448</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">148,473</td>
<td align="right">110,918</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">139,000</td>
<td align="right">104,066</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">221,890</td>
<td align="right">167,360</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,008,320</td>
<td align="right">1,522,054</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">263,035</td>
<td align="right">200,790</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">128,062</td>
<td align="right">98,252</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">44,866,460</td>
<td align="right">34,636,049</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,605,222</td>
<td align="right">2,011,856</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">379,913</td>
<td align="right">293,390</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">755,123</td>
<td align="right">584,164</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,721,069</td>
<td align="right">2,893,447</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">16,300,309</td>
<td align="right">12,685,440</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">182,440</td>
<td align="right">142,361</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">3,791,354</td>
<td align="right">2,967,520</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">912,076</td>
<td align="right">715,313</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">571,538</td>
<td align="right">452,756</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">61,820</td>
<td align="right">49,020</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">934,661</td>
<td align="right">743,075</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">295,147</td>
<td align="right">235,200</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,122,625</td>
<td align="right">3,288,803</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">63,600</td>
<td align="right">50,800</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">863,616</td>
<td align="right">689,893</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">800,161</td>
<td align="right">639,295</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">802,216</td>
<td align="right">641,293</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">112,155</td>
<td align="right">89,964</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">224,426</td>
<td align="right">180,036</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">344,104</td>
<td align="right">276,768</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,343,907</td>
<td align="right">2,691,243</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">136,360</td>
<td align="right">109,835</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">561,561</td>
<td align="right">452,643</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,407,117</td>
<td align="right">1,135,133</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,434,004</td>
<td align="right">1,969,564</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">789,157</td>
<td align="right">639,912</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">54,960</td>
<td align="right">44,720</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">339,015</td>
<td align="right">399,790</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">211,108</td>
<td align="right">173,390</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">16,818</td>
<td align="right">13,882</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">577,542</td>
<td align="right">477,359</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,103,738</td>
<td align="right">5,905,333</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">668,792</td>
<td align="right">557,290</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,770,307</td>
<td align="right">4,819,238</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,839,853</td>
<td align="right">2,373,015</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,943,750</td>
<td align="right">1,639,090</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,513,623</td>
<td align="right">4,677,539</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,819,525</td>
<td align="right">1,554,325</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,078,982</td>
<td align="right">1,234,902</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">809,941</td>
<td align="right">702,104</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,262,562</td>
<td align="right">8,165,941</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,227,524</td>
<td align="right">8,181,485</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,723,275</td>
<td align="right">3,340,546</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">39,080</td>
<td align="right">36,805</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,480,270</td>
<td align="right">1,412,613</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">430</td>
<td align="right">443</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">633,965</td>
<td align="right">647,755</td>
<td align="right">2.2%</td>
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
<td align="right">17,880</td>
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
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2,140</td>
<td align="right">2,140</td>
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
<td align="left">CALL_TYPE_1</td>
<td align="right">800</td>
<td align="right">800</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,656,634</td>
<td align="right">33.1%</td>
<td align="right">979,734</td>
<td align="right">26.7%</td>
<td align="right">-40.9%</td>
</tr>
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
<td align="right">2,685,562</td>
<td align="right">73.2%</td>
<td align="right">-19.5%</td>
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
<td align="right">5,061</td>
<td align="right">89.1%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">615</td>
<td align="right">10.2%</td>
<td align="right">620</td>
<td align="right">10.9%</td>
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
<td align="left">or</td>
<td align="right">1,393</td>
<td align="right">25.7%</td>
<td align="right">1,281</td>
<td align="right">25.3%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2,688</td>
<td align="right">49.6%</td>
<td align="right">2,481</td>
<td align="right">49.0%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">600</td>
<td align="right">11.1%</td>
<td align="right">560</td>
<td align="right">11.1%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">659</td>
<td align="right">12.2%</td>
<td align="right">659</td>
<td align="right">13.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">80</td>
<td align="right">1.5%</td>
<td align="right">80</td>
<td align="right">1.6%</td>
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
<td align="right">18,220</td>
<td align="right">100.0%</td>
<td align="right">10,540</td>
<td align="right">100.0%</td>
<td align="right">-42.2%</td>
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
<td align="right">216,082</td>
<td align="right">40.3%</td>
<td align="right">167.5%</td>
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
<td align="right">319,196</td>
<td align="right">59.5%</td>
<td align="right">-33.0%</td>
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
<td align="right">715</td>
<td align="right">74.9%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">240</td>
<td align="right">26.8%</td>
<td align="right">240</td>
<td align="right">25.1%</td>
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
<td align="right">715</td>
<td align="right">100.0%</td>
<td align="right">9.0%</td>
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
<td align="right">11,265,839</td>
<td align="right">99.7%</td>
<td align="right">-31.6%</td>
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
<td align="right">13,626</td>
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
<td align="right">13,941</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,073</td>
<td align="right">0.2%</td>
<td align="right">3,789</td>
<td align="right">0.1%</td>
<td align="right">-37.6%</td>
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
<td align="right">2,373,911</td>
<td align="right">90.9%</td>
<td align="right">-36.3%</td>
</tr>
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
<td align="right">232,613</td>
<td align="right">8.9%</td>
<td align="right">-20.5%</td>
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
<td align="right">1,147</td>
<td align="right">43.5%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,531</td>
<td align="right">54.4%</td>
<td align="right">1,489</td>
<td align="right">56.5%</td>
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
<td align="left">different types</td>
<td align="right">168</td>
<td align="right">13.1%</td>
<td align="right">119</td>
<td align="right">10.4%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">777</td>
<td align="right">60.5%</td>
<td align="right">708</td>
<td align="right">61.7%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">340</td>
<td align="right">26.5%</td>
<td align="right">320</td>
<td align="right">27.9%</td>
<td align="right">-5.9%</td>
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
<td align="right">732,463</td>
<td align="right">100.0%</td>
<td align="right">-32.8%</td>
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
<td align="right">105,593</td>
<td align="right">2.0%</td>
<td align="right">230.6%</td>
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
<td align="right">5,147,800</td>
<td align="right">98.0%</td>
<td align="right">-29.6%</td>
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
<td align="left">other</td>
<td align="right">220</td>
<td align="right">23.9%</td>
<td align="right">300</td>
<td align="right">31.9%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">220</td>
<td align="right">23.9%</td>
<td align="right">200</td>
<td align="right">21.3%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">23.9%</td>
<td align="right">200</td>
<td align="right">21.3%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">260</td>
<td align="right">28.3%</td>
<td align="right">240</td>
<td align="right">25.5%</td>
<td align="right">-7.7%</td>
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
<td align="right">485,601</td>
<td align="right">1.3%</td>
<td align="right">287,606</td>
<td align="right">1.2%</td>
<td align="right">-40.8%</td>
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
<td align="right">21,122,836</td>
<td align="right">86.9%</td>
<td align="right">-33.9%</td>
</tr>
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
<td align="right">2,864,945</td>
<td align="right">11.8%</td>
<td align="right">-22.4%</td>
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
<td align="right">25,663</td>
<td align="right">67.1%</td>
<td align="right">21,880</td>
<td align="right">65.5%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">12,563</td>
<td align="right">32.9%</td>
<td align="right">11,540</td>
<td align="right">34.5%</td>
<td align="right">-8.1%</td>
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
<td align="right">2,016</td>
<td align="right">16.0%</td>
<td align="right">1,806</td>
<td align="right">15.6%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,219</td>
<td align="right">33.6%</td>
<td align="right">3,833</td>
<td align="right">33.2%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,009</td>
<td align="right">24.0%</td>
<td align="right">2,768</td>
<td align="right">24.0%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">520</td>
<td align="right">4.1%</td>
<td align="right">480</td>
<td align="right">4.2%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">260</td>
<td align="right">2.1%</td>
<td align="right">240</td>
<td align="right">2.1%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">640</td>
<td align="right">5.1%</td>
<td align="right">640</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">160</td>
<td align="right">1.3%</td>
<td align="right">160</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">80</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">60</td>
<td align="right">0.5%</td>
<td align="right">60</td>
<td align="right">0.5%</td>
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
<td align="right">12,497,330</td>
<td align="right">99.8%</td>
<td align="right">9,144,828</td>
<td align="right">99.8%</td>
<td align="right">-26.8%</td>
</tr>
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
<td align="right">1,318</td>
<td align="right">0.0%</td>
<td align="right">-25.9%</td>
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
<td align="right">8,320</td>
<td align="right">0.1%</td>
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
<td align="right">9,564</td>
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
<td align="right">857,176</td>
<td align="right">99.9%</td>
<td align="right">686,013</td>
<td align="right">99.9%</td>
<td align="right">-20.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">171,520</td>
<td align="right">5.8%</td>
<td align="right">85,520</td>
<td align="right">4.5%</td>
<td align="right">-50.1%</td>
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
<td align="right">45,901</td>
<td align="right">2.4%</td>
<td align="right">-43.8%</td>
</tr>
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
<td align="right">1,769,489</td>
<td align="right">92.8%</td>
<td align="right">-34.9%</td>
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
<td align="right">7,355</td>
<td align="right">80.3%</td>
<td align="right">5,680</td>
<td align="right">77.4%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,800</td>
<td align="right">19.7%</td>
<td align="right">1,660</td>
<td align="right">22.6%</td>
<td align="right">-7.8%</td>
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
<td align="right">980</td>
<td align="right">59.0%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">520</td>
<td align="right">28.9%</td>
<td align="right">480</td>
<td align="right">28.9%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">200</td>
<td align="right">11.1%</td>
<td align="right">200</td>
<td align="right">12.0%</td>
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
<td align="right">28,117</td>
<td align="right">2.4%</td>
<td align="right">15,320</td>
<td align="right">2.0%</td>
<td align="right">-45.5%</td>
</tr>
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
<td align="right">742,621</td>
<td align="right">97.9%</td>
<td align="right">-34.6%</td>
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
<td align="right">560</td>
<td align="right">66.7%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">275</td>
<td align="right">30.7%</td>
<td align="right">280</td>
<td align="right">33.3%</td>
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
<td align="right">180</td>
<td align="right">32.1%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">420</td>
<td align="right">67.7%</td>
<td align="right">380</td>
<td align="right">67.9%</td>
<td align="right">-9.5%</td>
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
<td align="right">177,774</td>
<td align="right">3.6%</td>
<td align="right">-26.3%</td>
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
<td align="right">4,700,996</td>
<td align="right">96.3%</td>
<td align="right">-26.1%</td>
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
<td align="right">2,193</td>
<td align="right">45.2%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,660</td>
<td align="right">53.4%</td>
<td align="right">2,661</td>
<td align="right">54.8%</td>
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
<td align="right">180</td>
<td align="right">8.2%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">420</td>
<td align="right">18.1%</td>
<td align="right">380</td>
<td align="right">17.3%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">420</td>
<td align="right">18.1%</td>
<td align="right">380</td>
<td align="right">17.3%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">360</td>
<td align="right">15.5%</td>
<td align="right">340</td>
<td align="right">15.5%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">919</td>
<td align="right">39.6%</td>
<td align="right">913</td>
<td align="right">41.6%</td>
<td align="right">-0.7%</td>
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
<td align="right">1,540,345</td>
<td align="right">99.9%</td>
<td align="right">-42.4%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">666,432</td>
<td align="right">0.3%</td>
<td align="right">403,382</td>
<td align="right">0.2%</td>
<td align="right">-39.5%</td>
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
<td align="right">123,970,099</td>
<td align="right">63.5%</td>
<td align="right">-26.4%</td>
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
<td align="right">64,384,469</td>
<td align="right">33.0%</td>
<td align="right">-19.6%</td>
</tr>
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
<td align="right">6,452,896</td>
<td align="right">3.3%</td>
<td align="right">-18.4%</td>
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
<td align="right">105,593</td>
<td align="right">1.7%</td>
<td align="right">230.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">80,780</td>
<td align="right">1.0%</td>
<td align="right">216,082</td>
<td align="right">3.4%</td>
<td align="right">167.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">28,117</td>
<td align="right">0.4%</td>
<td align="right">15,320</td>
<td align="right">0.2%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,742</td>
<td align="right">1.0%</td>
<td align="right">45,901</td>
<td align="right">0.7%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,220</td>
<td align="right">0.2%</td>
<td align="right">10,540</td>
<td align="right">0.2%</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">241,322</td>
<td align="right">3.1%</td>
<td align="right">177,774</td>
<td align="right">2.8%</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,691,581</td>
<td align="right">47.2%</td>
<td align="right">2,864,945</td>
<td align="right">44.9%</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">292,422</td>
<td align="right">3.7%</td>
<td align="right">232,613</td>
<td align="right">3.6%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,337,872</td>
<td align="right">42.6%</td>
<td align="right">2,685,562</td>
<td align="right">42.1%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">13,619</td>
<td align="right">0.2%</td>
<td align="right">13,626</td>
<td align="right">0.2%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">171,520</td>
<td align="right">25.7%</td>
<td align="right">85,520</td>
<td align="right">20.0%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,380</td>
<td align="right">1.9%</td>
<td align="right">6,180</td>
<td align="right">1.4%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">61,881</td>
<td align="right">9.3%</td>
<td align="right">30,895</td>
<td align="right">7.2%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">410,240</td>
<td align="right">61.6%</td>
<td align="right">249,431</td>
<td align="right">58.4%</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,053</td>
<td align="right">0.9%</td>
<td align="right">3,769</td>
<td align="right">0.9%</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,438</td>
<td align="right">0.2%</td>
<td align="right">978</td>
<td align="right">0.2%</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,100</td>
<td align="right">0.2%</td>
<td align="right">1,100</td>
<td align="right">0.3%</td>
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
<td align="right">23,389</td>
<td align="right">5.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">23,389</td>
<td align="right">5.5%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">534,060</td>
<td align="right">2.1%</td>
<td align="right">267,820</td>
<td align="right">1.7%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">589,440</td>
<td align="right">2.3%</td>
<td align="right">312,960</td>
<td align="right">2.0%</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">551,520</td>
<td align="right">2.1%</td>
<td align="right">292,960</td>
<td align="right">1.8%</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,860,291</td>
<td align="right">30.3%</td>
<td align="right">4,372,625</td>
<td align="right">27.3%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,860,291</td>
<td align="right">30.3%</td>
<td align="right">4,372,625</td>
<td align="right">27.3%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,308,071</td>
<td align="right">28.2%</td>
<td align="right">4,078,965</td>
<td align="right">25.5%</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,308,771</td>
<td align="right">28.2%</td>
<td align="right">4,079,665</td>
<td align="right">25.5%</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">18,082,681</td>
<td align="right">69.7%</td>
<td align="right">11,615,961</td>
<td align="right">72.7%</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">19,467,772</td>
<td align="right">75.0%</td>
<td align="right">12,559,786</td>
<td align="right">78.6%</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">33,020</td>
<td align="right">0.1%</td>
<td align="right">22,394</td>
<td align="right">0.1%</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">366,600</td>
<td align="right">1.4%</td>
<td align="right">258,582</td>
<td align="right">1.6%</td>
<td align="right">-29.5%</td>
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
<td align="right">147,724</td>
<td align="right">0.8%</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">116,266,886</td>
<td align="right">51.9%</td>
<td align="right">59,709,281</td>
<td align="right">42.7%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,237,206</td>
<td align="right"></td>
<td align="right">1,176,756</td>
<td align="right"></td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">116,002,967</td>
<td align="right">46.3%</td>
<td align="right">62,799,919</td>
<td align="right">40.0%</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">230,740</td>
<td align="right"></td>
<td align="right">127,820</td>
<td align="right"></td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,891,273</td>
<td align="right">54.7%</td>
<td align="right">10,039,137</td>
<td align="right">53.5%</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,094,871</td>
<td align="right">55.4%</td>
<td align="right">10,273,706</td>
<td align="right">54.8%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,802,597</td>
<td align="right"></td>
<td align="right">10,845,290</td>
<td align="right"></td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">6,720,223</td>
<td align="right"></td>
<td align="right">4,361,177</td>
<td align="right"></td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,938,856</td>
<td align="right">44.6%</td>
<td align="right">8,479,229</td>
<td align="right">45.2%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,950,968</td>
<td align="right"></td>
<td align="right">8,491,273</td>
<td align="right"></td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">57,967</td>
<td align="right"></td>
<td align="right">38,536</td>
<td align="right"></td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">134,749,820</td>
<td align="right">53.7%</td>
<td align="right">94,187,444</td>
<td align="right">60.0%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">680,150</td>
<td align="right"></td>
<td align="right">499,340</td>
<td align="right"></td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">107,787,729</td>
<td align="right">48.1%</td>
<td align="right">80,171,979</td>
<td align="right">57.3%</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">5,244,049</td>
<td align="right"></td>
<td align="right">3,967,982</td>
<td align="right"></td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">104,606</td>
<td align="right">0.4%</td>
<td align="right">86,845</td>
<td align="right">0.5%</td>
<td align="right">-17.0%</td>
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
<td align="right">936,280</td>
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
<td align="right">2,739</td>
<td align="right">2.4%</td>
<td align="right">11,808.7%</td>
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
<td align="right">97,540</td>
<td align="right">84.8%</td>
<td align="right">6,172.7%</td>
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
<td align="right">115,035</td>
<td align="right"></td>
<td align="right">1,647.5%</td>
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
<td align="right">34,586</td>
<td align="right">30.1%</td>
<td align="right">629.0%</td>
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
<td align="right">17,061</td>
<td align="right">14.8%</td>
<td align="right">276.5%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
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
<td align="right">9,899,812</td>
<td align="right"></td>
<td align="right">-56.7%</td>
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
<td align="right">149,423,008</td>
<td align="right">1,509.4%</td>
<td align="right">-53.7%</td>
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
<td align="right">434</td>
<td align="right">0.4%</td>
<td align="right">-12.7%</td>
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
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">23 / 0 !!</td>
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
<td align="right">97,540</td>
<td align="right">100.0%</td>
<td align="right">6,205.1%</td>
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
<td align="right">97,540</td>
<td align="right"></td>
<td align="right">6,172.7%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
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
<td align="right">7,591</td>
<td align="right">7.8%</td>
<td align="right">1,897.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">137</td>
<td align="right">8.8%</td>
<td align="right">9,490</td>
<td align="right">9.7%</td>
<td align="right">6,827.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">320</td>
<td align="right">20.6%</td>
<td align="right">31,777</td>
<td align="right">32.6%</td>
<td align="right">9,830.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">224</td>
<td align="right">14.4%</td>
<td align="right">16,261</td>
<td align="right">16.7%</td>
<td align="right">7,159.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">333</td>
<td align="right">21.4%</td>
<td align="right">27,995</td>
<td align="right">28.7%</td>
<td align="right">8,306.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">101</td>
<td align="right">6.5%</td>
<td align="right">4,266</td>
<td align="right">4.4%</td>
<td align="right">4,123.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">1.3%</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">700.0%</td>
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
<td align="right">13,568</td>
<td align="right">13.9%</td>
<td align="right">8,380.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">137</td>
<td align="right">8.8%</td>
<td align="right">3,572</td>
<td align="right">3.7%</td>
<td align="right">2,507.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">380</td>
<td align="right">24.4%</td>
<td align="right">39,451</td>
<td align="right">40.4%</td>
<td align="right">10,281.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">257</td>
<td align="right">16.5%</td>
<td align="right">24,939</td>
<td align="right">25.6%</td>
<td align="right">9,603.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">233</td>
<td align="right">15.0%</td>
<td align="right">14,318</td>
<td align="right">14.7%</td>
<td align="right">6,045.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">40</td>
<td align="right">2.6%</td>
<td align="right">1,692</td>
<td align="right">1.7%</td>
<td align="right">4,130.0%</td>
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
<td align="right">33,166</td>
<td align="right">762.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">9,118</td>
<td align="right">160</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">3,845</td>
<td align="right">113</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">28,508,559</td>
<td align="right">5,118,515</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,250,029</td>
<td align="right">231,404</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">506,700</td>
<td align="right">94,400</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">501,440</td>
<td align="right">94,866</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,008,000</td>
<td align="right">191,360</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,013,960</td>
<td align="right">198,212</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">506,560</td>
<td align="right">99,520</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">506,560</td>
<td align="right">99,520</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">12,160</td>
<td align="right">2,400</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,159,439</td>
<td align="right">795,172</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,427,254</td>
<td align="right">617,402</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">662,960</td>
<td align="right">174,805</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">663,240</td>
<td align="right">175,243</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,303,500</td>
<td align="right">380,461</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">142,022</td>
<td align="right">43,703</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,017,916</td>
<td align="right">625,743</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">937,571</td>
<td align="right">293,049</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,367,714</td>
<td align="right">429,875</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">9,207,865</td>
<td align="right">3,041,778</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,034,545</td>
<td align="right">348,665</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,595,412</td>
<td align="right">2,229,477</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">124,740</td>
<td align="right">44,283</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,019,191</td>
<td align="right">1,078,407</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,024,011</td>
<td align="right">1,080,247</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">1,044,620</td>
<td align="right">378,880</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,699,060</td>
<td align="right">617,440</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">734,175</td>
<td align="right">268,703</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">713,690</td>
<td align="right">264,885</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,554,152</td>
<td align="right">1,692,826</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,240,965</td>
<td align="right">1,206,227</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,362,390</td>
<td align="right">513,232</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,081,360</td>
<td align="right">785,518</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">9,727,313</td>
<td align="right">3,673,641</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">9,723,468</td>
<td align="right">3,673,528</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">5,554,414</td>
<td align="right">2,126,763</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,679,168</td>
<td align="right">645,087</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,206,075</td>
<td align="right">860,383</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,262,735</td>
<td align="right">492,548</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">16,561,458</td>
<td align="right">6,506,582</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">8,669,963</td>
<td align="right">3,425,780</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,597,885</td>
<td align="right">638,366</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,598,045</td>
<td align="right">638,526</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,598,045</td>
<td align="right">638,526</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,342,794</td>
<td align="right">1,341,631</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">6,356,923</td>
<td align="right">2,552,002</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">11,082,546</td>
<td align="right">4,459,059</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">4,337,867</td>
<td align="right">1,748,195</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,108,260</td>
<td align="right">447,342</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,469,388</td>
<td align="right">2,614,735</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,469,388</td>
<td align="right">2,614,735</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,102,536</td>
<td align="right">1,278,140</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,420,149</td>
<td align="right">3,064,229</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">554,054</td>
<td align="right">231,631</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">176,418</td>
<td align="right">75,703</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">22,866,768</td>
<td align="right">9,899,812</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,277,115</td>
<td align="right">555,187</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">647,735</td>
<td align="right">285,518</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,195,948</td>
<td align="right">981,124</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,195,948</td>
<td align="right">981,124</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,720</td>
<td align="right">2,160</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,188,440</td>
<td align="right">546,467</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">634,703</td>
<td align="right">293,262</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">634,703</td>
<td align="right">293,262</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">834,781</td>
<td align="right">396,003</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">9,325,514</td>
<td align="right">4,440,351</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">4,960</td>
<td align="right">2,400</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">4,960</td>
<td align="right">2,400</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">20,345,029</td>
<td align="right">9,856,177</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,431,549</td>
<td align="right">696,961</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">867,008</td>
<td align="right">422,268</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">510,123</td>
<td align="right">249,559</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">507,843</td>
<td align="right">250,699</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">251,730</td>
<td align="right">124,463</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">251,730</td>
<td align="right">124,463</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">511,539</td>
<td align="right">254,484</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">5,120</td>
<td align="right">2,560</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">5,120</td>
<td align="right">2,560</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">613,418</td>
<td align="right">307,871</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">738,272</td>
<td align="right">377,107</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">542,703</td>
<td align="right">280,841</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">5,982,720</td>
<td align="right">3,098,720</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,081,640</td>
<td align="right">569,640</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,618,960</td>
<td align="right">856,080</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">543,360</td>
<td align="right">287,360</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">593,340</td>
<td align="right">314,082</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">6,301,463</td>
<td align="right">3,360,064</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">991,197</td>
<td align="right">535,722</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">606,177</td>
<td align="right">330,375</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">626,633</td>
<td align="right">342,038</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">627,053</td>
<td align="right">342,458</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">20,096,914</td>
<td align="right">11,167,365</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,168,632</td>
<td align="right">1,224,846</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,797,590</td>
<td align="right">1,020,983</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">84,700</td>
<td align="right">48,720</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">84,560</td>
<td align="right">48,720</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">84,560</td>
<td align="right">48,720</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">84,560</td>
<td align="right">48,720</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">86,120</td>
<td align="right">49,860</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,002,600</td>
<td align="right">591,948</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">755,030</td>
<td align="right">459,806</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">14,220</td>
<td align="right">8,680</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">14,220</td>
<td align="right">8,680</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">347,165</td>
<td align="right">213,701</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,553,343</td>
<td align="right">11,833,572</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,534,756</td>
<td align="right">1,116,638</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,560</td>
<td align="right">1,140</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">353,661</td>
<td align="right">276,859</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">353,661</td>
<td align="right">276,859</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">232,068</td>
<td align="right">182,581</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">2,080</td>
<td align="right">1,660</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">217,268</td>
<td align="right">175,461</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">211,670</td>
<td align="right">172,446</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">105,835</td>
<td align="right">86,223</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">106,155</td>
<td align="right">86,543</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">318,743</td>
<td align="right">260,504</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">290,308</td>
<td align="right">239,543</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">711,614</td>
<td align="right">591,207</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">141,675</td>
<td align="right">117,785</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">40,640</td>
<td align="right">33,860</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">88</td>
<td align="right">98</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">31,840</td>
<td align="right">31,402</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">31,840</td>
<td align="right">31,402</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">31,840</td>
<td align="right">31,402</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">32,260</td>
<td align="right">31,840</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">32,260</td>
<td align="right">31,840</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">43,516</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">17,442</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
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
<td align="right">10,207,683</td>
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
<td align="right">7,918</td>
<td align="right">1,311.4%</td>
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
<td align="right">4</td>
<td align="right">-50.0%</td>
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
<td align="right">4</td>
<td align="right">-50.0%</td>
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
Stats gathered on: 2024-09-22
