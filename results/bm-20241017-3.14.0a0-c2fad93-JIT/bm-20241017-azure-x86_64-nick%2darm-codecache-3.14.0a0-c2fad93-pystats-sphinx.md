
# Pystats results

- benchmark: sphinx
- fork: nick-arm
- ref: codecache
- commit hash: c2fad93
- commit date: 2024-10-17T13:54:09+00:00

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
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
<th align="right">Miss ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">452,511,684</td>
<td align="right">16.8%</td>
<td align="right">16.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">131,299,070</td>
<td align="right">4.9%</td>
<td align="right">21.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">130,194,059</td>
<td align="right">4.8%</td>
<td align="right">26.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">117,632,877</td>
<td align="right">4.4%</td>
<td align="right">30.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">115,089,346</td>
<td align="right">4.3%</td>
<td align="right">35.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">112,974,217</td>
<td align="right">4.2%</td>
<td align="right">39.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">107,174,203</td>
<td align="right">4.0%</td>
<td align="right">43.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">96,914,418</td>
<td align="right">3.6%</td>
<td align="right">47.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">91,918,137</td>
<td align="right">3.4%</td>
<td align="right">50.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">83,570,707</td>
<td align="right">3.1%</td>
<td align="right">53.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">82,758,886</td>
<td align="right">3.1%</td>
<td align="right">56.6%</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">79,173,029</td>
<td align="right">2.9%</td>
<td align="right">59.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">75,888,416</td>
<td align="right">2.8%</td>
<td align="right">62.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">68,363,818</td>
<td align="right">2.5%</td>
<td align="right">64.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">61,947,815</td>
<td align="right">2.3%</td>
<td align="right">67.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">54,897,034</td>
<td align="right">2.0%</td>
<td align="right">69.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">42,716,123</td>
<td align="right">1.6%</td>
<td align="right">70.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">40,012,803</td>
<td align="right">1.5%</td>
<td align="right">72.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,526,700</td>
<td align="right">1.5%</td>
<td align="right">73.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,268,128</td>
<td align="right">1.5%</td>
<td align="right">75.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,864,488</td>
<td align="right">1.4%</td>
<td align="right">76.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,090,584</td>
<td align="right">1.4%</td>
<td align="right">78.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">36,146,849</td>
<td align="right">1.3%</td>
<td align="right">79.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">31,421,146</td>
<td align="right">1.2%</td>
<td align="right">80.7%</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,551,532</td>
<td align="right">1.1%</td>
<td align="right">81.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">28,035,845</td>
<td align="right">1.0%</td>
<td align="right">82.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">24,350,202</td>
<td align="right">0.9%</td>
<td align="right">83.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,677,619</td>
<td align="right">0.8%</td>
<td align="right">84.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,765,520</td>
<td align="right">0.8%</td>
<td align="right">85.4%</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,618,338</td>
<td align="right">0.7%</td>
<td align="right">86.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">16,111,793</td>
<td align="right">0.6%</td>
<td align="right">86.7%</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">14,929,248</td>
<td align="right">0.6%</td>
<td align="right">87.2%</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">14,895,020</td>
<td align="right">0.6%</td>
<td align="right">87.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">14,447,301</td>
<td align="right">0.5%</td>
<td align="right">88.3%</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">14,442,334</td>
<td align="right">0.5%</td>
<td align="right">88.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">14,273,635</td>
<td align="right">0.5%</td>
<td align="right">89.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">12,296,772</td>
<td align="right">0.5%</td>
<td align="right">89.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12,225,446</td>
<td align="right">0.5%</td>
<td align="right">90.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">11,993,244</td>
<td align="right">0.4%</td>
<td align="right">90.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">10,964,511</td>
<td align="right">0.4%</td>
<td align="right">91.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,876,533</td>
<td align="right">0.4%</td>
<td align="right">91.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">9,687,261</td>
<td align="right">0.4%</td>
<td align="right">91.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,894,044</td>
<td align="right">0.3%</td>
<td align="right">92.2%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,819,165</td>
<td align="right">0.3%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,322,022</td>
<td align="right">0.3%</td>
<td align="right">92.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,629,591</td>
<td align="right">0.3%</td>
<td align="right">93.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,288,210</td>
<td align="right">0.3%</td>
<td align="right">93.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">7,030,952</td>
<td align="right">0.3%</td>
<td align="right">93.6%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,421,542</td>
<td align="right">0.2%</td>
<td align="right">93.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,984,698</td>
<td align="right">0.2%</td>
<td align="right">94.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">5,932,456</td>
<td align="right">0.2%</td>
<td align="right">94.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,883,100</td>
<td align="right">0.2%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,698,664</td>
<td align="right">0.2%</td>
<td align="right">94.8%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,663,779</td>
<td align="right">0.2%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,646,577</td>
<td align="right">0.2%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">5,339,041</td>
<td align="right">0.2%</td>
<td align="right">95.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">5,162,664</td>
<td align="right">0.2%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,913,470</td>
<td align="right">0.2%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,607,832</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">4,590,929</td>
<td align="right">0.2%</td>
<td align="right">96.1%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,515,956</td>
<td align="right">0.2%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,470,648</td>
<td align="right">0.2%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,461,230</td>
<td align="right">0.2%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,219,156</td>
<td align="right">0.2%</td>
<td align="right">96.8%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">4,142,367</td>
<td align="right">0.2%</td>
<td align="right">96.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,699,957</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,487,757</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,451,197</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">3,299,733</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,158,176</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,994,333</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,973,844</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,912,875</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,907,884</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,839,721</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,686,947</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,481,939</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,318,399</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,024,679</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,889,886</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,736,239</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,724,962</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,539,709</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,520,958</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,520,958</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,512,691</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,495,927</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,475,755</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,382,574</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,285,090</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,265,664</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">1,202,518</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,200,689</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,191,525</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,178,983</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,131,363</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,089,088</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,055,938</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">967,121</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">826,350</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">813,058</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">785,634</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">770,565</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">751,250</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">741,279</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">675,641</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">630,203</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">604,139</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">554,360</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">549,109</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">543,167</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">540,615</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">482,624</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">472,548</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">452,768</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">341,596</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">320,123</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,750</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">266,423</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">257,622</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">254,403</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">243,730</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">219,438</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">192,030</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">162,514</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">158,435</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">151,758</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">146,477</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">140,137</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">136,486</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">130,757</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">128,497</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">118,283</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">84,414</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">76,817</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">70,199</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">38,479</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,881</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">32,159</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">27,855</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">27,275</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,704</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">22,034</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">21,144</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20,239</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,387</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">15,201</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">12,211</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,663</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">8,887</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,706</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,559</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4,541</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,131</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">136.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,908</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,892</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,081</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1,357</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">315</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">259</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">143</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">129</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">117</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">117</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">14</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
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

<table>
<thead>
<tr>
<th align="left">Pair</th>
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">94,347,375</td>
<td align="right">3.5%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">84,041,273</td>
<td align="right">3.1%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">71,030,846</td>
<td align="right">2.6%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">67,455,988</td>
<td align="right">2.5%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">52,241,327</td>
<td align="right">1.9%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">48,070,535</td>
<td align="right">1.8%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">47,895,569</td>
<td align="right">1.8%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">POP_TOP ENTER_EXECUTOR</td>
<td align="right">43,412,533</td>
<td align="right">1.6%</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">43,024,117</td>
<td align="right">1.6%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR RETURN_CONST</td>
<td align="right">42,217,456</td>
<td align="right">1.6%</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">POP_TOP RESUME_CHECK</td>
<td align="right">39,526,207</td>
<td align="right">1.5%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST</td>
<td align="right">39,513,324</td>
<td align="right">1.5%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN POP_TOP</td>
<td align="right">39,247,685</td>
<td align="right">1.5%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR GET_ITER</td>
<td align="right">39,046,977</td>
<td align="right">1.5%</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">END_FOR POP_TOP</td>
<td align="right">38,864,488</td>
<td align="right">1.4%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST END_FOR</td>
<td align="right">38,864,488</td>
<td align="right">1.4%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_GEN</td>
<td align="right">38,723,558</td>
<td align="right">1.4%</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">37,479,513</td>
<td align="right">1.4%</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR RETURN_GENERATOR</td>
<td align="right">37,024,005</td>
<td align="right">1.4%</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST ENTER_EXECUTOR</td>
<td align="right">34,501,973</td>
<td align="right">1.3%</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_ISINSTANCE</td>
<td align="right">33,670,677</td>
<td align="right">1.3%</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">30,958,049</td>
<td align="right">1.2%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_BOOL</td>
<td align="right">30,602,345</td>
<td align="right">1.1%</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST</td>
<td align="right">26,553,366</td>
<td align="right">1.0%</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">23,758,574</td>
<td align="right">0.9%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">23,156,327</td>
<td align="right">0.9%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">22,679,124</td>
<td align="right">0.8%</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">22,676,447</td>
<td align="right">0.8%</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">21,771,562</td>
<td align="right">0.8%</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE STORE_FAST</td>
<td align="right">21,702,378</td>
<td align="right">0.8%</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST YIELD_VALUE</td>
<td align="right">20,701,582</td>
<td align="right">0.8%</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_FAST</td>
<td align="right">20,352,365</td>
<td align="right">0.8%</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST</td>
<td align="right">19,957,146</td>
<td align="right">0.7%</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">19,785,310</td>
<td align="right">0.7%</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">18,581,164</td>
<td align="right">0.7%</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST POP_TOP</td>
<td align="right">18,479,229</td>
<td align="right">0.7%</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR RETURN_VALUE</td>
<td align="right">17,004,362</td>
<td align="right">0.6%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">16,792,091</td>
<td align="right">0.6%</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN</td>
<td align="right">16,753,781</td>
<td align="right">0.6%</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">15,602,009</td>
<td align="right">0.6%</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">14,975,202</td>
<td align="right">0.6%</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_CONST</td>
<td align="right">14,735,864</td>
<td align="right">0.5%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">14,428,570</td>
<td align="right">0.5%</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST INTERPRETER_EXIT</td>
<td align="right">14,413,086</td>
<td align="right">0.5%</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK NOP</td>
<td align="right">14,122,877</td>
<td align="right">0.5%</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,492,610</td>
<td align="right">0.5%</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">13,423,058</td>
<td align="right">0.5%</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,654,791</td>
<td align="right">0.5%</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">12,419,132</td>
<td align="right">0.5%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">12,148,501</td>
<td align="right">0.5%</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE CALL_ISINSTANCE</td>
<td align="right">11,995,218</td>
<td align="right">0.4%</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">11,809,633</td>
<td align="right">0.4%</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE</td>
<td align="right">11,218,710</td>
<td align="right">0.4%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">10,978,516</td>
<td align="right">0.4%</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">10,912,149</td>
<td align="right">0.4%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK RETURN_CONST</td>
<td align="right">10,671,356</td>
<td align="right">0.4%</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST</td>
<td align="right">10,440,650</td>
<td align="right">0.4%</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_NON_PY_GENERAL</td>
<td align="right">10,416,498</td>
<td align="right">0.4%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE POP_JUMP_IF_TRUE</td>
<td align="right">10,108,471</td>
<td align="right">0.4%</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST</td>
<td align="right">9,563,379</td>
<td align="right">0.4%</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">9,558,478</td>
<td align="right">0.4%</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">9,370,113</td>
<td align="right">0.3%</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">COPY TO_BOOL_NONE</td>
<td align="right">9,334,962</td>
<td align="right">0.3%</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST</td>
<td align="right">8,953,253</td>
<td align="right">0.3%</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">8,907,365</td>
<td align="right">0.3%</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">CACHE ENTER_EXECUTOR</td>
<td align="right">8,726,189</td>
<td align="right">0.3%</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">8,640,737</td>
<td align="right">0.3%</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">8,589,878</td>
<td align="right">0.3%</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE</td>
<td align="right">8,389,634</td>
<td align="right">0.3%</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL RESUME_CHECK</td>
<td align="right">8,231,946</td>
<td align="right">0.3%</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_SLOT</td>
<td align="right">8,154,201</td>
<td align="right">0.3%</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT RETURN_VALUE</td>
<td align="right">8,070,027</td>
<td align="right">0.3%</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_LOAD_FAST</td>
<td align="right">8,042,727</td>
<td align="right">0.3%</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST BUILD_TUPLE</td>
<td align="right">7,611,561</td>
<td align="right">0.3%</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST PUSH_NULL</td>
<td align="right">7,538,015</td>
<td align="right">0.3%</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE POP_TOP</td>
<td align="right">7,398,031</td>
<td align="right">0.3%</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE ENTER_EXECUTOR</td>
<td align="right">7,068,994</td>
<td align="right">0.3%</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">7,015,590</td>
<td align="right">0.3%</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_CONST</td>
<td align="right">6,912,884</td>
<td align="right">0.3%</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_PROPERTY</td>
<td align="right">6,897,011</td>
<td align="right">0.3%</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">6,831,579</td>
<td align="right">0.3%</td>
<td align="right">68.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NONE</td>
<td align="right">6,712,660</td>
<td align="right">0.2%</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST</td>
<td align="right">6,688,871</td>
<td align="right">0.2%</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_TYPE_1</td>
<td align="right">6,611,725</td>
<td align="right">0.2%</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR</td>
<td align="right">6,537,065</td>
<td align="right">0.2%</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,518,289</td>
<td align="right">0.2%</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">6,475,659</td>
<td align="right">0.2%</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE CALL_ISINSTANCE</td>
<td align="right">6,381,774</td>
<td align="right">0.2%</td>
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST NOP</td>
<td align="right">6,336,469</td>
<td align="right">0.2%</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE LOAD_FAST</td>
<td align="right">6,321,562</td>
<td align="right">0.2%</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR STORE_FAST</td>
<td align="right">6,308,774</td>
<td align="right">0.2%</td>
<td align="right">70.6%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_LIST</td>
<td align="right">6,220,999</td>
<td align="right">0.2%</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">NOP LOAD_GLOBAL_MODULE</td>
<td align="right">6,212,415</td>
<td align="right">0.2%</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,211,571</td>
<td align="right">0.2%</td>
<td align="right">71.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE COPY</td>
<td align="right">6,184,982</td>
<td align="right">0.2%</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE NOP</td>
<td align="right">6,174,241</td>
<td align="right">0.2%</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST GET_ITER</td>
<td align="right">6,127,056</td>
<td align="right">0.2%</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_CONST</td>
<td align="right">6,059,319</td>
<td align="right">0.2%</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_ATTR</td>
<td align="right">5,944,358</td>
<td align="right">0.2%</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,919,335</td>
<td align="right">0.2%</td>
<td align="right">72.7%</td>
</tr>
</tbody>
</table>


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each Tier 1 opcode. </summary>


This does not include the unspecialized instructions that occur after a
specialized instruction deoptimizes.

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,975,565</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">631,620</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">195,671</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">149,695</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">147,313</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,786,664</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,081,058</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">593,648</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">494,853</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">229,810</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">710,517</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">73,742</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">27,986</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">14,102</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">701,429</td>
<td align="right">84.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">124,585</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">254</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">79</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">30,958,049</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,726,189</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">283,060</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">271,026</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">248,371</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">158,395</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">85,367</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,369</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,192</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,182</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">73,406</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">40,444</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">39,020</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">38,733</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">38,658</td>
<td align="right">15.1%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">137,150</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">28,391</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">27,990</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">25,674</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">206</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">133,944</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,966</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">26,721</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,719</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,024</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,443,757</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">22,455</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">9,473</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">55</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,475,755</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">117,069</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,291</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,639</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,378</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">107</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">96,832</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">34,720</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,264</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,216</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">312</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">38,864,488</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">38,864,488</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">7,552</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">1,154</td>
<td align="right">13.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,706</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">543,167</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">543,167</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,646,577</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">150,270</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">43,370</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">12,859</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">12,031</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,128,939</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,705,609</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">27,299</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,411</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,834</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### FORMAT_WITH_SPEC

<details>
<summary> Successors and predecessors for FORMAT_WITH_SPEC </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">143</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">143</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,046,977</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,127,056</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,661,183</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,786,664</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,598,098</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">38,723,558</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,220,999</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,547,107</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,937,785</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">941,154</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">7,404</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,152</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,559</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">23,156,327</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">14,413,086</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">519,821</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,350</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,121</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">128</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">76</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">18</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">3</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,357</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">254,403</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">118,013</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">76,395</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">55,665</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">2,416</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,292</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">14,122,877</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,336,469</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">6,174,241</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">5,052,087</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,459,729</td>
<td align="right">6.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">26,553,366</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,212,415</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,568,782</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,974,880</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,040,922</td>
<td align="right">2.6%</td>
</tr>
</tbody>
</table>


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,050,008</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">327,751</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">115,129</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,530</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">7,398</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">969,548</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">327,751</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">115,129</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">87,192</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">11,198</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,247,685</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,864,488</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">18,479,229</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,398,031</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,563,549</td>
<td align="right">3.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">43,412,533</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">39,526,207</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,785,310</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,167,810</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,241,618</td>
<td align="right">1.9%</td>
</tr>
</tbody>
</table>


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">600,746</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">317,527</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">175,015</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">112,488</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">99,827</td>
<td align="right">6.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,448,984</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">49,921</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,854</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">165</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">8,589,878</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,538,015</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,049,410</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">861,704</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">157,923</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,370,113</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,059,319</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,176,664</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">495,676</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">175,027</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">37,024,005</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,157,603</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">821,769</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">479,309</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">17,174</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">39,046,977</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">207,425</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">205,825</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">25,147</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">17,860</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">17,004,362</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">8,070,027</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,831,579</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,785,678</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,303,486</td>
<td align="right">7.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">23,156,327</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,423,058</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,831,579</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,854,325</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,543,351</td>
<td align="right">6.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">454,057</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">300,027</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,940</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,202</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">3,083</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">476,695</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">153,352</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">79,357</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">27,481</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">15,746</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,392,722</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,194,184</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">894,953</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">818,529</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">771,619</td>
<td align="right">6.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,912,149</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">951,189</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">52,774</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">50,869</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">19,204</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,630</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">278</td>
<td align="right">9.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,904</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">71,889</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">4,927</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">71,744</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,926</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">145</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">38,445</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">19,204</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,247</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,087</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">216</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">38,161</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">31,310</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">512</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">216</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,828,405</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">895,051</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">756,526</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">734,586</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">673,151</td>
<td align="right">10.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,736,388</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">910,023</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">889,217</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">872,303</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">769,256</td>
<td align="right">12.0%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,094,079</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,442,133</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">870,816</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">829,188</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">774,812</td>
<td align="right">9.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,792,920</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,866,594</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">829,188</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">570,323</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">310,379</td>
<td align="right">3.7%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,068,251</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">874,662</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">695,186</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">643,305</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">375,905</td>
<td align="right">8.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,644,591</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,126,860</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">321,545</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">154,176</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">111,966</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">7,552</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,222</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">144</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">126</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">126</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">7,566</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,216</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">168</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">132</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">91</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">68,043</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">50,240</td>
<td align="right">42.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">117,069</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,214</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">2,705,609</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">202,275</td>
<td align="right">7.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,558,504</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">224,966</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">75,136</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">20,310</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,413</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,611,561</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,272,706</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,982,655</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">570,323</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">202,707</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">5,690,453</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,385,644</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,009,053</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">895,591</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">452,269</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">15,210</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,508</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,613</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,370</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,115</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,839</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">6,817</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">5,644</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,631</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,478</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,200,369</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">750,633</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">661,609</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">204,751</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">154,176</td>
<td align="right">5.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,272,294</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">721,088</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">496,775</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">270,689</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">104,125</td>
<td align="right">3.5%</td>
</tr>
</tbody>
</table>


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,255,286</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">283,060</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,344</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">874,662</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">284,404</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">204,751</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">175,872</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,081</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,353</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">396</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">116</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">53</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">376,727</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">185,918</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">28,502</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,766</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,832</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">513,983</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">91,544</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,800</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,477</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">697</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,148,598</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">498,051</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">344,639</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">326,310</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">88,969</td>
<td align="right">2.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,056,300</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">251,087</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">150,519</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,539</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,693</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,747,046</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,691,849</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60,860</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">60,543</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">60,543</td>
<td align="right">1.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,646,577</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,184,982</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,842,140</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">608,029</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">589,963</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">150,519</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">9,334,962</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">858,392</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">818,529</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">448,352</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">170,798</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">256,055</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">248,371</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">111,962</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,934</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">14,843</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">720,060</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">17,174</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,974</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">71</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">16,387</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">10,882</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,441</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">64</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,240</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,280</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">535</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">320</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">105</td>
<td align="right">4.7%</td>
</tr>
</tbody>
</table>


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,197,637</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,686</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">43</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,200,369</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">261</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">64</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">22</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">245</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">65</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">24</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">7</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">370,648</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">87,192</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">85,385</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">81,975</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">59,839</td>
<td align="right">7.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">324,058</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">274,436</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">90,680</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">32,009</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">23,426</td>
<td align="right">3.0%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,937,785</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">295,149</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">179,791</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">32,009</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,275</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,069,337</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,032,212</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">303,858</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">22,839</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">9,006</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">20,846</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">10,115</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,191</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,284</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">10,115</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">2,632</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">128</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">25,704</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">20,846</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,226</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">611</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">14</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">5</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,113,803</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">956,061</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">906,933</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">895,496</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">33,158</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,775,812</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,799,957</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">297,428</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">39,277</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">741</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">187,749</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">176,373</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">83,061</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">37,232</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">13,389</td>
<td align="right">2.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">295,149</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">73,418</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">50,567</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">31,307</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">22,322</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">11,198</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">10,063</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,590</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,724</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">3,335</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">3,259</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">324</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">199</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">833,880</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">558,449</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">401,548</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">153,664</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">90,680</td>
<td align="right">3.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,240,843</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">371,522</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">223,198</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">193,595</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">183,746</td>
<td align="right">7.9%</td>
</tr>
</tbody>
</table>


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">468,338</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">268,686</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">201,666</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">44,000</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">26,766</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,027,995</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">12,681</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,512</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">6,444</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">178</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,255,124</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,512</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,543</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,255,286</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,585</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,280</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,602,009</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,944,358</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,066,239</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,231,751</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,148,522</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,953,253</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,308,774</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,582,073</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">2,691,849</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,558,396</td>
<td align="right">8.4%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,957,146</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,735,864</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,912,884</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,059,319</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,944,208</td>
<td align="right">5.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,352,365</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,735,864</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,883,609</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">4,459,976</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,975,565</td>
<td align="right">4.8%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">430,786</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">281,161</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">165,757</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">151,100</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">115,921</td>
<td align="right">7.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">424,319</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">289,139</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">165,757</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">149,698</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">107,510</td>
<td align="right">7.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">84,041,273</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">52,241,327</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">48,070,535</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">43,024,117</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">26,553,366</td>
<td align="right">5.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">71,030,846</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">34,501,973</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">30,602,345</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">22,679,124</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">22,676,447</td>
<td align="right">5.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">941,154</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">147,934</td>
<td align="right">13.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">941,154</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">147,934</td>
<td align="right">13.6%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,056</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,795</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,085</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,111</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">930</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,332</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,583</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,241</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,309</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,024</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">39,513,324</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">8,042,727</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,688,871</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,475,659</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">5,685,593</td>
<td align="right">5.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">33,670,677</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">10,978,516</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,640,737</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">7,611,561</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,518,289</td>
<td align="right">6.7%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,825</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,388</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,062</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,670</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,623</td>
<td align="right">7.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,578</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,431</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">960</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">849</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">438</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">6,444</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,616</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,632</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,477</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,230</td>
<td align="right">8.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">8,192</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,863</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,533</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,115</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">787</td>
<td align="right">5.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SPECIAL

<details>
<summary> Successors and predecessors for LOAD_SPECIAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">170,798</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">170,798</td>
<td align="right">50.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">170,798</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">85,321</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">80,579</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">4,484</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">414</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">259</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">179</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">30</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">19</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">9</td>
<td align="right">3.5%</td>
</tr>
</tbody>
</table>


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">231,098</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">110,943</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">84,698</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">17,013</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,932</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">234,100</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">231,098</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">6,912</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">438</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">111,607</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,255</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">8,448</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,422</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,793</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">134,129</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,381</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,232</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,115</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">261</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">94,347,375</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">10,912,149</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,759,289</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,794,436</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,056,300</td>
<td align="right">2.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">84,041,273</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">16,753,781</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,389,634</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">6,174,241</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,249,967</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,712,660</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,791,833</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,323,772</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">39,212</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,875</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,321,562</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,789,307</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,081,929</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">334,916</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">147,022</td>
<td align="right">1.5%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,558,478</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,421,401</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">763,007</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">63,763</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">62,742</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,563,379</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,947,612</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">552,754</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">391,598</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">260,344</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">18,581,164</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">10,108,471</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,799,957</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,696,138</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">951,189</td>
<td align="right">2.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">10,440,650</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,398,031</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">7,068,994</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">3,659,712</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,511,491</td>
<td align="right">9.7%</td>
</tr>
</tbody>
</table>


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">82,743</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20,286</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,296</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">7,036</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,279</td>
<td align="right">3.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">65,648</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">59,972</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,280</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">284,404</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">115,129</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">49,921</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,017</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,280</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">112,488</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">54,515</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,344</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">42,217,456</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">10,671,356</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,249,967</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,167,810</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,659,712</td>
<td align="right">4.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,864,488</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">18,479,229</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">14,413,086</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,303,486</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">661,866</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,335</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,159</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">47</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">3,332</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,154</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">47</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">4</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">118,013</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">33,745</td>
<td align="right">22.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">100,616</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">33,745</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,137</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">3,533</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">3,525</td>
<td align="right">2.3%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,537,065</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,227,140</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">38,658</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">9,189</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,620</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,055,761</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">3,225,499</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">333,746</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">78,474</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">40,757</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">7,554</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,533</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,693</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,422</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,408</td>
<td align="right">7.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">9,287</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,845</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,474</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,250</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">655</td>
<td align="right">3.2%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">21,702,378</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,423,058</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,308,774</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,883,609</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">5,042,368</td>
<td align="right">5.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,070,535</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">12,148,501</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,015,590</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,475,659</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">6,336,469</td>
<td align="right">6.9%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">470,043</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,551</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,224</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,122</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,656</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">222,268</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">201,666</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">27,965</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,727</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">8,271</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,165,162</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,185,274</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">297,951</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">8,959</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,975</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,211,814</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">952,728</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">787,277</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">297,951</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">174,002</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,405</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,525</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">2,632</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,416</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,631</td>
<td align="right">7.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">12,029</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,632</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,441</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,415</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,191</td>
<td align="right">5.6%</td>
</tr>
</tbody>
</table>


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">941,154</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">829,188</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">370,361</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">250,664</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">227,798</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">829,188</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">547,236</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">452,645</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">388,911</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">327,751</td>
<td align="right">8.9%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">295,682</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">383</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">322</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">97</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">295,693</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">554</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">294</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">97</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">87</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,701,582</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,481,984</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">452,269</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">11,455</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,824</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,702,378</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">519,821</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">451,006</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">3,262</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,150</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CACHE</td>
<td align="right">1,553</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">711</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">438</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">159</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">71</td>
<td align="right">2.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,230</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">729</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">455</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">381</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">106</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,249,616</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">306,042</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">135,540</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">132,224</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">14,466</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,159,396</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">608,920</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">306,045</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">211,692</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">195,671</td>
<td align="right">6.9%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,776,871</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,200,464</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">307,633</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">121,152</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20,594</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,167,200</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">184,772</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">35,117</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">25,674</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">25,214</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,351</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">841</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">332</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">318</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">27</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,351</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">362</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">332</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">319</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">302</td>
<td align="right">10.4%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">42</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21</td>
<td align="right">33.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">63</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">844,034</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">235,452</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">146,046</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">84,425</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">71,750</td>
<td align="right">5.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">496,294</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">402,123</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">152,506</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">80,928</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">75,077</td>
<td align="right">5.4%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,690,453</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,415,240</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">949,423</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">401,336</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">295,678</td>
<td align="right">2.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,070,027</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,576,868</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">591,367</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">322,179</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">295,682</td>
<td align="right">2.4%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">955,164</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">116,933</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">71,731</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">52,944</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,748</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">899,130</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">287,347</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,793</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,890</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,741</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,344,360</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,833,987</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">265,844</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">80,928</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">42,703</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,808,191</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">222,334</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">99,827</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">83,939</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">72,329</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">479,945</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">49,841</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">49,726</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">49,726</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">40,009</td>
<td align="right">5.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">295,691</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">221,928</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">132,428</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,366</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,543</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,724,917</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">44</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">721,086</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">721,086</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">151,307</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">46,988</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">42,799</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">353,966</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">257,312</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80,697</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">67,884</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">15,550</td>
<td align="right">1.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">484,170</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">294,200</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,750</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">8,909</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">5,971</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,796,839</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">95,974</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">64,425</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,300</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,510</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,769,551</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">110,943</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">95,934</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">13,525</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,349</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BOUND_METHOD_GENERAL

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">126</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">129</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">309,683</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60,939</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">47,613</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">21,819</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">21,597</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">220,704</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">185,168</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">65,276</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">21,597</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,064</td>
<td align="right">3.9%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,459,976</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,558,396</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,509,785</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">89,965</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">20,618</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,042,368</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,838,370</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">299,995</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">210,018</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">134,653</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">493,305</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">31,476</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">22,781</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,218</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">16,356</td>
<td align="right">2.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">467,040</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">82,941</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,472</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">10,033</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">8,191</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">198,509</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">25,147</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,908</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">3,442</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,245</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">73,756</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">38,853</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">35,333</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">29,385</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">22,158</td>
<td align="right">9.1%</td>
</tr>
</tbody>
</table>


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">33,670,677</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">11,995,218</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">11,218,710</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,381,774</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,619,262</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">67,455,988</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">905,408</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,666</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">556</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">198</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW_BOUND_METHOD

<details>
<summary> Successors and predecessors for CALL_KW_BOUND_METHOD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">116</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">64</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">53</td>
<td align="right">45.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW_NON_PY

<details>
<summary> Successors and predecessors for CALL_KW_NON_PY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">319,727</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">396</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">143,244</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">93,656</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">71,871</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,010</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,278</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW_PY

<details>
<summary> Successors and predecessors for CALL_KW_PY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,734,886</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,353</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">887,141</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">821,769</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">14,843</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">7,932</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,553</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,341,575</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,547,859</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">943,185</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">49,842</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">14,140</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,515,962</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">754,079</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">586,431</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">329,342</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">240,071</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,739,216</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">721,086</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">201,117</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">126,853</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">63,614</td>
<td align="right">1.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,220,447</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,182,623</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">236,563</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">134,863</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">107,252</td>
<td align="right">1.8%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,612,992</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,052,103</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,238,848</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">992,096</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">321,545</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,123,606</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,125,015</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">531,714</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">291,624</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">282,479</td>
<td align="right">3.7%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,532,320</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">548,714</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">311,632</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">295,691</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">177,703</td>
<td align="right">6.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,228,091</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">615,518</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">344,009</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">303,032</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">225,919</td>
<td align="right">7.8%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,846,867</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">32,698</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">4,484</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,567</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,472</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">835,898</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">320,233</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">295,678</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">227,902</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">78,600</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,143,658</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">615,518</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">91,050</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">45,771</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">25,798</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">703,058</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">668,911</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">242,830</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">235,225</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">93,521</td>
<td align="right">4.6%</td>
</tr>
</tbody>
</table>


</details>

### CALL_NON_PY_GENERAL

<details>
<summary> Successors and predecessors for CALL_NON_PY_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">10,416,498</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,274,151</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">495,676</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">433,093</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">419,622</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,785,678</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,190,309</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,563,964</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,269,203</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">356,815</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">22,679,124</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,640,737</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,698,379</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,307,895</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">929,733</td>
<td align="right">2.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">37,479,513</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,656,288</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,157,603</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">256,055</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">84,698</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### CALL_PY_GENERAL

<details>
<summary> Successors and predecessors for CALL_PY_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,460,537</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,558,504</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">769,256</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">728,183</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">441,584</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">8,231,946</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,120,122</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">479,309</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">111,962</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">17,013</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">822,491</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">277,310</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,590</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">638</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">324,538</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">295,995</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">295,678</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">107,834</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">60,543</td>
<td align="right">5.4%</td>
</tr>
</tbody>
</table>


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">32,081</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,376</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">383</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">301</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">169</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">32,063</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,618</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">873</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">489</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">301</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,611,725</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">676,117</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">74</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,685,593</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">894,926</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">691,044</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">7,974</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,782</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">146,046</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">429</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">146,476</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,740,568</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">488,323</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">329,342</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">222,800</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">131,419</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,303,442</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">600,904</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">108,732</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">73,397</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">59,839</td>
<td align="right">1.9%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,001,439</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">585,150</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">295,678</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">184,986</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">34,884</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,973,531</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">589,963</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">573,917</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,136</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">361</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP_DICT

<details>
<summary> Successors and predecessors for CONTAINS_OP_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,625,723</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">315,847</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">202,042</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">105,352</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">77,256</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,169,057</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">750,938</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">552,623</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,834</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,513</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP_SET

<details>
<summary> Successors and predecessors for CONTAINS_OP_SET </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">153,694</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,849</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,737</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,622</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,558</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">186,215</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,121</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">994</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">699</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">38,723,558</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">324,058</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">200,509</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">19,919</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">39,247,685</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">12,387</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">8,036</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,220,999</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">547,236</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">113,402</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">73,418</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">29,704</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,460,318</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">852,560</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">579,938</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">470,043</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">325,232</td>
<td align="right">4.6%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">121,149</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">8,077</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,498</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">76,905</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">45,657</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,570</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,656</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">698</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">5,547,107</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">115,455</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">22,294</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,541</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,326</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,999,788</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">632,002</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">591,417</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">431,915</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">22,291</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,089,774</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">204,576</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">120,899</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">106,486</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">64,811</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,680,284</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,333,672</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,049,410</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">202,042</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">77,650</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_CLASS_WITH_METACLASS_CHECK

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS_WITH_METACLASS_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,685,285</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,342</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">43</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">894,975</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">894,953</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">894,908</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,349</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">71,030,846</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,919,335</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,565,924</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,224,354</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">448,352</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">14,428,570</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,897,011</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,211,571</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,184,982</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,066,239</td>
<td align="right">6.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">117,048</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">45,430</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">75,669</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">52,509</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">32,698</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,613</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">25</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,654,791</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,211,571</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,854,325</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,179,405</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">690,520</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,809,633</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,042,727</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,944,208</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,846,867</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">992,096</td>
<td align="right">3.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">22,676,447</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,582,073</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,301,053</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,746,253</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">357,412</td>
<td align="right">1.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">16,792,091</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,912,884</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,698,379</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,887,645</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">441,584</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">23,758,574</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">403,436</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">171,262</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">12,492</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,772</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">8,589,878</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">6,381,774</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,129,012</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,982,655</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">895,051</td>
<td align="right">3.7%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,776</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">86</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">24</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,452</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,431</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,407</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">447</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">63</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">14,975,202</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">568,401</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">340,467</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">134,058</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">87,448</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">3,842,140</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,500,399</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,598,098</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,547,859</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,092,666</td>
<td align="right">6.8%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,897,011</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,651,568</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,021,637</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">440,010</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">192,009</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,956,597</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,687,596</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,231,751</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">888,631</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">771,619</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,154,201</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">297,340</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">254,630</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">99,044</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">46,769</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,944,358</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">911,505</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">386,403</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">265,965</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">149,695</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">594,006</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">313,153</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">283,071</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">113,319</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">73,819</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">374,557</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">278,710</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">216,334</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">121,533</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">113,657</td>
<td align="right">7.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">47,895,569</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">16,753,781</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,419,132</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,148,501</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,686,105</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">52,241,327</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">39,513,324</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">11,218,710</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,443,757</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">895,496</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,771,562</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,389,634</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,015,590</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">6,212,415</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,428,585</td>
<td align="right">8.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">23,758,574</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">11,995,218</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,688,871</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,686,105</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,437,897</td>
<td align="right">7.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">158,405</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">30</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">157,923</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">512</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">266,244</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">179</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">138,308</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,208</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,070</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">33,343</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,536</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">39,526,207</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">37,479,513</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">30,958,049</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">8,231,946</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,956,597</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">47,895,569</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">43,024,117</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">14,122,877</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">10,671,356</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,428,585</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,400</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,259</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,401</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,260</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,492,610</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,518,289</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">452,645</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">178,572</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">89,048</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,907,365</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,052,087</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,777,326</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,351,157</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,316,381</td>
<td align="right">6.3%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">441,821</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">308,814</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">74</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">225,784</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">166,521</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">148,038</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">113,848</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">51,843</td>
<td align="right">6.9%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">674,780</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">574,396</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,550</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">7,895</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,428</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">630,964</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">613,687</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">19,510</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">11,240</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,818</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,217,467</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">932,375</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">721,086</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">295,995</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">83,395</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,987,030</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">712,537</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">370,771</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">176,373</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">71,871</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">495,445</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">35,516</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,550</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,587</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">11</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">452,962</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">64,896</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">21,892</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,255</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,097</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">762,484</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">88,411</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">86,017</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">18,155</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">6,902</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">484,344</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">393,319</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">85,385</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,368</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">384</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">67,455,988</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">30,602,345</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,543,351</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">3,838,370</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,563,964</td>
<td align="right">2.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">94,347,375</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">18,581,164</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">33,581</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">11,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">384</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">3,515,962</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">189,054</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">135,582</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">109,754</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">109,691</td>
<td align="right">2.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,794,436</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">340,810</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">81,975</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">1,087</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">531</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">562,178</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">323,020</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">265,861</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">10,971</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">10,024</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">985,209</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">184,650</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">5,131</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,756</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">216</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">9,334,962</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,664,022</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,700,320</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">340,134</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">235,922</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">10,108,471</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,759,289</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">52,077</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">3,710</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,368</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,942,795</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">604,024</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">282,479</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">146,081</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">141,273</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,696,138</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,557,852</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">38,445</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,690</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,544</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">83,388</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">704</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">320</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">75,135</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">8,959</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">320</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">791,954</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">322,179</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">29,717</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">24,773</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">12,247</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,185,274</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,725</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,497</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">29</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,100,468</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,032,212</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">591,417</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">451,006</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">255,663</td>
<td align="right">5.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,165,162</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">194,230</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">111,206</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">35</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">43,412,533</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">34,501,973</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">8,726,189</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,068,994</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">4,220,447</td>
<td align="right">3.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">42,217,456</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,024,005</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">17,004,362</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,063,660</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,675,484</td>
<td align="right">2.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_LOCALS

<details>
<summary> Successors and predecessors for LOAD_LOCALS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">315</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">315</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### SETUP_ANNOTATIONS

<details>
<summary> Successors and predecessors for SETUP_ANNOTATIONS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">108</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">9</td>
<td align="right">7.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">116</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">16</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">16</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_NAME

<details>
<summary> Successors and predecessors for DELETE_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">4</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">3</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1</td>
<td align="right">11.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">3</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1</td>
<td align="right">11.1%</td>
</tr>
</tbody>
</table>


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">7</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1</td>
<td align="right">7.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1</td>
<td align="right">7.1%</td>
</tr>
</tbody>
</table>


</details>


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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">6,412,264</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,823,994</td>
<td align="right">62.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">610</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,668</td>
<td align="right">93.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">remainder</td>
<td align="right">3,005</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,376</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,510</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">843</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">251</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">184</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">124</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">66</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">1</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">5,162,664</td>
<td align="right">100.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">252,806</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,461,199</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,363,120</td>
<td align="right">6.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">45,680</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,579</td>
<td align="right">7.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">out of range</td>
<td align="right">2,990</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">307</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">238</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">43</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">1</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">14,257</td>
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
<td align="right">239,383,807</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,809,659</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">59,918</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">init not simple</td>
<td align="right">424</td>
<td align="right">424 / 0 !!</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">24</td>
<td align="right">24 / 0 !!</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3</td>
<td align="right">3 / 0 !!</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">331</td>
<td align="right">15.4%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">626,360</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,926,687</td>
<td align="right">94.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,897</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">1,366</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,606</td>
<td align="right">65.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">different types</td>
<td align="right">1,760</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">259</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">255</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">158</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">103</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">27</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">21</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">21</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">3,482,537</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,731,099</td>
<td align="right">77.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">527</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,693</td>
<td align="right">89.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">str</td>
<td align="right">1,973</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,425</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">734</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">561</td>
<td align="right">12.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">3,447,278</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">71,516,081</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,363,316</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">45,229</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,275</td>
<td align="right">6.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dict items</td>
<td align="right">1,053</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">857</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">315</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">280</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">275</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">183</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">142</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">76</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">54</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">25</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15</td>
<td align="right">0.5%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">30,234,688</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">64,390</td>
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
<td align="right">207,498,955</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">67,142,732</td>
<td align="right">22.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">1,572,316</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,504</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">method</td>
<td align="right">2,986</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,158</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,049</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">995</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">645</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">530</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">279</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">115</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">72</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">69</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">2</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">3,025</td>
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
<td align="right">59</td>
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
<td align="right">169,109,635</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,383</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">19,444</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">424,921</td>
<td align="right">99.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">209</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">4</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">47</td>
<td align="right">92.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">list</td>
<td align="right">47</td>
<td align="right">100.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">8,804,525</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,096,880</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,541,724</td>
<td align="right">29.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">184,702</td>
<td align="right">95.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,488</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">class attr simple</td>
<td align="right">4,754</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,626</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">993</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">643</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">308</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">53</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">5</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">1</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">826,350</td>
<td align="right">100.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">767,005</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,156,383</td>
<td align="right">92.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">477</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,083</td>
<td align="right">86.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">py simple</td>
<td align="right">2,913</td>
<td align="right">94.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">113</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">47</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">10</td>
<td align="right">0.3%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">11,882,561</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">167,726,200</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,878,936</td>
<td align="right">2.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">77,116</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">106,705</td>
<td align="right">58.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">number</td>
<td align="right">93,107</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,950</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,160</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,074</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">213</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">107</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">94</td>
<td align="right">0.1%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,605,681</td>
<td align="right">98.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">383</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97</td>
<td align="right">20.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sequence</td>
<td align="right">74</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">23</td>
<td align="right">23.7%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">1,648,902,981</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">72,735,985</td>
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
<td align="right">879,419,064</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">87,124,103</td>
<td align="right">3.2%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,234,688</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">11,882,561</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,804,525</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,412,264</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">5,162,664</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,482,537</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,447,278</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">826,350</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">767,005</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">626,360</td>
<td align="right">0.9%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">32,146,008</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">11,018,715</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,591,258</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,500,690</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">8,595,286</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,253,036</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,172,511</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,338,581</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,181,775</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,181,541</td>
<td align="right">1.4%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,497,891</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">178,903,074</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,497,891</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,626,646</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">871,245</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">387</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,624,902</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">1,357</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">10,489,618</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">502,515</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">18,547,721</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">88</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">7,050,934</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,043,082</td>
<td align="right">72.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">88,059,594</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">88,085,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">242,448,036</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">240,831,806</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,554,381</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">61,849</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">251,863,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,079,133</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,191,705,720</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,591,516,830</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,641,864,775</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,497,433,543</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">434,228,805</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">443,005,689</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">816,949,270</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">847,189,100</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">997,148</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">98,881</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (str subclass)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">201,528,793</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">8,140,890</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">9,760,018</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">155,510,946</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,621,151</td>
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
<th align="right">Collections</th>
<th align="right">Objects collected</th>
<th align="right">Object visits</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">6,282</td>
<td align="right">12,390,712</td>
<td align="right">367,416,094</td>
</tr>
<tr>
<td align="right">2</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">329,458</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">226,827</td>
<td align="right">68.8%</td>
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
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">136,231</td>
<td align="right">41.4%</td>
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
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">102,631</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">3,729</td>
<td align="right">1.1%</td>
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
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,449</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">35</td>
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
<td align="right">401,199,359</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">3,821,056,298</td>
<td align="right">952.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">226,827</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">217,394</td>
<td align="right">95.8%</td>
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
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">57</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,277</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">58,516</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">85,967</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">48,913</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">16,809</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">345</td>
<td align="right">0.2%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">6,634</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">42,412</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">48,345</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">90,539</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">26,768</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,651</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">45</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
<th align="right">Miss ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">413,063,457</td>
<td align="right">10.8%</td>
<td align="right">10.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">401,199,359</td>
<td align="right">10.5%</td>
<td align="right">21.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">324,118,980</td>
<td align="right">8.5%</td>
<td align="right">29.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">307,943,460</td>
<td align="right">8.1%</td>
<td align="right">37.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">224,614,863</td>
<td align="right">5.9%</td>
<td align="right">43.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">189,580,027</td>
<td align="right">5.0%</td>
<td align="right">48.7%</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">120,197,371</td>
<td align="right">3.1%</td>
<td align="right">51.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">93,971,128</td>
<td align="right">2.5%</td>
<td align="right">54.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">79,859,259</td>
<td align="right">2.1%</td>
<td align="right">56.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">78,744,919</td>
<td align="right">2.1%</td>
<td align="right">58.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">73,193,632</td>
<td align="right">1.9%</td>
<td align="right">60.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">73,134,419</td>
<td align="right">1.9%</td>
<td align="right">62.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">71,201,690</td>
<td align="right">1.9%</td>
<td align="right">64.1%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">70,054,502</td>
<td align="right">1.8%</td>
<td align="right">66.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">67,255,775</td>
<td align="right">1.8%</td>
<td align="right">67.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">66,504,994</td>
<td align="right">1.7%</td>
<td align="right">69.5%</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">54,226,232</td>
<td align="right">1.4%</td>
<td align="right">70.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">53,348,246</td>
<td align="right">1.4%</td>
<td align="right">72.3%</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">50,582,014</td>
<td align="right">1.3%</td>
<td align="right">73.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">49,308,885</td>
<td align="right">1.3%</td>
<td align="right">74.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">47,138,795</td>
<td align="right">1.2%</td>
<td align="right">76.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">43,973,633</td>
<td align="right">1.2%</td>
<td align="right">77.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">41,391,377</td>
<td align="right">1.1%</td>
<td align="right">78.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">41,334,549</td>
<td align="right">1.1%</td>
<td align="right">79.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">38,903,434</td>
<td align="right">1.0%</td>
<td align="right">80.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">38,457,132</td>
<td align="right">1.0%</td>
<td align="right">81.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">37,264,463</td>
<td align="right">1.0%</td>
<td align="right">82.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">34,039,926</td>
<td align="right">0.9%</td>
<td align="right">83.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">29,902,746</td>
<td align="right">0.8%</td>
<td align="right">84.1%</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">27,864,529</td>
<td align="right">0.7%</td>
<td align="right">84.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">26,556,546</td>
<td align="right">0.7%</td>
<td align="right">85.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">26,318,541</td>
<td align="right">0.7%</td>
<td align="right">86.2%</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">25,866,450</td>
<td align="right">0.7%</td>
<td align="right">86.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">25,806,243</td>
<td align="right">0.7%</td>
<td align="right">87.6%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">25,224,501</td>
<td align="right">0.7%</td>
<td align="right">88.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">23,938,066</td>
<td align="right">0.6%</td>
<td align="right">88.9%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">21,750,896</td>
<td align="right">0.6%</td>
<td align="right">89.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">21,008,899</td>
<td align="right">0.5%</td>
<td align="right">90.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">18,669,905</td>
<td align="right">0.5%</td>
<td align="right">90.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">17,727,933</td>
<td align="right">0.5%</td>
<td align="right">90.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">14,990,956</td>
<td align="right">0.4%</td>
<td align="right">91.3%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">14,578,677</td>
<td align="right">0.4%</td>
<td align="right">91.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">13,789,410</td>
<td align="right">0.4%</td>
<td align="right">92.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">13,504,708</td>
<td align="right">0.4%</td>
<td align="right">92.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,774,046</td>
<td align="right">0.3%</td>
<td align="right">92.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">12,608,264</td>
<td align="right">0.3%</td>
<td align="right">93.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,909,966</td>
<td align="right">0.3%</td>
<td align="right">93.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">11,864,098</td>
<td align="right">0.3%</td>
<td align="right">93.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">10,698,808</td>
<td align="right">0.3%</td>
<td align="right">94.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">10,534,256</td>
<td align="right">0.3%</td>
<td align="right">94.3%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">10,507,903</td>
<td align="right">0.3%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">8,980,931</td>
<td align="right">0.2%</td>
<td align="right">94.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">8,548,905</td>
<td align="right">0.2%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,511,928</td>
<td align="right">0.2%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">7,413,766</td>
<td align="right">0.2%</td>
<td align="right">95.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,321,488</td>
<td align="right">0.2%</td>
<td align="right">95.6%</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,520,768</td>
<td align="right">0.2%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">5,547,013</td>
<td align="right">0.1%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,524,359</td>
<td align="right">0.1%</td>
<td align="right">96.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">5,515,560</td>
<td align="right">0.1%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">5,407,409</td>
<td align="right">0.1%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">5,302,772</td>
<td align="right">0.1%</td>
<td align="right">96.5%</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">5,271,701</td>
<td align="right">0.1%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">5,156,781</td>
<td align="right">0.1%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">5,120,008</td>
<td align="right">0.1%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">4,930,940</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,768,621</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">4,712,573</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,738,334</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,738,334</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">3,690,778</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,628,433</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">3,327,126</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">3,258,467</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">3,113,114</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">3,088,618</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">3,058,795</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,945,612</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">2,907,273</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">2,907,273</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,890,643</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,828,654</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,751,913</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,685,026</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,599,668</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,478,163</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,338,326</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">2,287,451</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,019,546</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,994,995</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,932,742</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,799,890</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,700,402</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,700,402</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,574,804</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,554,822</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,489,689</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">1,482,924</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,464,463</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,448,122</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,424,121</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,252,108</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,251,321</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,212,541</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">1,104,536</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,061,765</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">992,599</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">971,970</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">955,965</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">817,220</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">815,229</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">812,699</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">812,130</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">769,602</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">763,066</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">697,686</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">697,686</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">568,755</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">508,225</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">458,844</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">368,783</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">353,746</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">337,185</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">328,797</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">317,527</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">305,779</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">245,992</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">229,644</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">187,125</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">179,615</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">179,193</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">160,809</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">160,809</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">136,031</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">114,320</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">114,320</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">100,303</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">82,954</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">82,636</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">81,713</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">79,178</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">70,250</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">66,849</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">65,075</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">64,001</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">61,338</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">58,141</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">56,422</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">48,445</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">43,259</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">38,104</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">36,304</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">33,104</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,507</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,507</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">29,298</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">28,553</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">20,061</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">19,984</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,204</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">16,930</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">14,961</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">14,961</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">13,156</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">11,599</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">11,403</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">10,663</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">10,295</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">9,674</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">8,862</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">7,215</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">5,230</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">3,892</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">3,118</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,687</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_WITH_SPEC</td>
<td align="right">2,417</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">2,291</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,922</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">1,886</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,788</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,483</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">1,336</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,284</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">904</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">904</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">720</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">165</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">147</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">147</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">62</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
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


</details>

### Unsupported opcodes

<details>
<summary> unsupported opcodes </summary>

<table>
<thead>
<tr>
<th align="left">Opcode</th>
<th align="right">Count</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">4,438</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,198</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">127</td>
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
<th align="right">Count</th>
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
<th align="right">Count</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Number of data files</td>
<td align="right">21</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-18
