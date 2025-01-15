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
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,981</td>
<td align="right">21,973</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">38,327</td>
<td align="right">38,319</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">640,685</td>
<td align="right">640,576</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">767,189</td>
<td align="right">767,097</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">53,278</td>
<td align="right">53,273</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,245,080</td>
<td align="right">9,244,971</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">30,222,674</td>
<td align="right">30,222,582</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">111,703,518</td>
<td align="right">111,703,426</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,085,458</td>
<td align="right">38,085,430</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">136,000,233</td>
<td align="right">136,000,141</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">163,080,534</td>
<td align="right">163,080,437</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">578,063,645</td>
<td align="right">578,063,451</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">46,763,180</td>
<td align="right">46,763,172</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">50,489,714</td>
<td align="right">50,489,717</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">166,998,053</td>
<td align="right">166,998,053</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,106,923</td>
<td align="right">155,106,923</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">138,866,856</td>
<td align="right">138,866,856</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">126,058,474</td>
<td align="right">126,058,474</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">118,680,745</td>
<td align="right">118,680,745</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">110,146,565</td>
<td align="right">110,146,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">88,734,164</td>
<td align="right">88,734,164</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">87,386,679</td>
<td align="right">87,386,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">85,960,148</td>
<td align="right">85,960,148</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">73,886,911</td>
<td align="right">73,886,911</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">58,928,741</td>
<td align="right">58,928,741</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">55,146,340</td>
<td align="right">55,146,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">52,538,963</td>
<td align="right">52,538,963</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">49,875,225</td>
<td align="right">49,875,225</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">45,508,344</td>
<td align="right">45,508,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">44,402,311</td>
<td align="right">44,402,311</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,528,154</td>
<td align="right">39,528,154</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,864,488</td>
<td align="right">38,864,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">36,343,789</td>
<td align="right">36,343,789</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">34,135,450</td>
<td align="right">34,135,450</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">28,091,045</td>
<td align="right">28,091,045</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">23,127,110</td>
<td align="right">23,127,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,677,584</td>
<td align="right">22,677,584</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">21,489,386</td>
<td align="right">21,489,386</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">20,948,688</td>
<td align="right">20,948,688</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">20,483,568</td>
<td align="right">20,483,568</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">19,434,744</td>
<td align="right">19,434,744</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">18,192,237</td>
<td align="right">18,192,237</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">17,669,006</td>
<td align="right">17,669,006</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,319,158</td>
<td align="right">17,319,158</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,294,443</td>
<td align="right">17,294,443</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,962,930</td>
<td align="right">16,962,930</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">16,939,203</td>
<td align="right">16,939,203</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">16,847,593</td>
<td align="right">16,847,593</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">16,302,813</td>
<td align="right">16,302,813</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">14,383,448</td>
<td align="right">14,383,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">14,210,591</td>
<td align="right">14,210,591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,941,859</td>
<td align="right">12,941,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,488,981</td>
<td align="right">12,488,981</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">11,191,973</td>
<td align="right">11,191,973</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,840,147</td>
<td align="right">10,840,147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,050,394</td>
<td align="right">10,050,394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">10,042,966</td>
<td align="right">10,042,966</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">9,971,230</td>
<td align="right">9,971,230</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,949,147</td>
<td align="right">9,949,147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">9,918,107</td>
<td align="right">9,918,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">9,431,415</td>
<td align="right">9,431,415</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,643,180</td>
<td align="right">8,643,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">8,273,677</td>
<td align="right">8,273,677</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,308,757</td>
<td align="right">7,308,757</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,616,397</td>
<td align="right">6,616,397</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,458,219</td>
<td align="right">6,458,219</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,948,829</td>
<td align="right">5,948,829</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,682,859</td>
<td align="right">5,682,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">5,587,561</td>
<td align="right">5,587,561</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">5,568,576</td>
<td align="right">5,568,576</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,557,368</td>
<td align="right">5,557,368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,192,788</td>
<td align="right">5,192,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,953,169</td>
<td align="right">4,953,169</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,689,038</td>
<td align="right">4,689,038</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,588,852</td>
<td align="right">4,588,852</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,577,115</td>
<td align="right">4,577,115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,521,086</td>
<td align="right">4,521,086</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,468,904</td>
<td align="right">4,468,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,397,224</td>
<td align="right">4,397,224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,370,530</td>
<td align="right">4,370,530</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,068,960</td>
<td align="right">4,068,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,780,130</td>
<td align="right">3,780,130</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,688,674</td>
<td align="right">3,688,674</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,276,977</td>
<td align="right">3,276,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,044,625</td>
<td align="right">3,044,625</td>
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
<td align="right">2,941,653</td>
<td align="right">2,941,653</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,937,216</td>
<td align="right">2,937,216</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,931,791</td>
<td align="right">2,931,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,877,538</td>
<td align="right">2,877,538</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,732,416</td>
<td align="right">2,732,416</td>
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
<td align="right">2,480,752</td>
<td align="right">2,480,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,411,307</td>
<td align="right">2,411,307</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,285,049</td>
<td align="right">2,285,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,020,085</td>
<td align="right">2,020,085</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,898,237</td>
<td align="right">1,898,237</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,794,158</td>
<td align="right">1,794,158</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,723,465</td>
<td align="right">1,723,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,672,348</td>
<td align="right">1,672,348</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">1,515,800</td>
<td align="right">1,515,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,511,475</td>
<td align="right">1,511,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,490,318</td>
<td align="right">1,490,318</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,477,262</td>
<td align="right">1,477,262</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,359,116</td>
<td align="right">1,359,116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,341,773</td>
<td align="right">1,341,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,335,647</td>
<td align="right">1,335,647</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,334,132</td>
<td align="right">1,334,132</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,313,748</td>
<td align="right">1,313,748</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,280,588</td>
<td align="right">1,280,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,248,245</td>
<td align="right">1,248,245</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,133,223</td>
<td align="right">1,133,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,091,638</td>
<td align="right">1,091,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">892,860</td>
<td align="right">892,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">833,644</td>
<td align="right">833,644</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">743,593</td>
<td align="right">743,593</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">712,414</td>
<td align="right">712,414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">578,943</td>
<td align="right">578,943</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">554,442</td>
<td align="right">554,442</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">501,774</td>
<td align="right">501,774</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">475,689</td>
<td align="right">475,689</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">462,002</td>
<td align="right">462,002</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">345,350</td>
<td align="right">345,350</td>
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
<td align="right">266,454</td>
<td align="right">266,454</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">255,558</td>
<td align="right">255,558</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">236,335</td>
<td align="right">236,335</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">212,519</td>
<td align="right">212,519</td>
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
<td align="right">192,013</td>
<td align="right">192,013</td>
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
<td align="right">152,870</td>
<td align="right">152,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">149,587</td>
<td align="right">149,587</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">146,469</td>
<td align="right">146,469</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">129,125</td>
<td align="right">129,125</td>
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
<td align="right">84,308</td>
<td align="right">84,308</td>
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
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,860</td>
<td align="right">35,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">32,094</td>
<td align="right">32,094</td>
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
<td align="right">25,986</td>
<td align="right">25,986</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">24,161</td>
<td align="right">24,161</td>
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
<td align="right">23,192</td>
<td align="right">23,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">21,466</td>
<td align="right">21,466</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,384</td>
<td align="right">16,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">13,850</td>
<td align="right">13,850</td>
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
<td align="left">UNARY_INVERT</td>
<td align="right">8,139</td>
<td align="right">8,139</td>
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
<td align="right">3,079</td>
<td align="right">3,079</td>
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
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">118</td>
<td align="right">118</td>
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
<td align="right">9,235,140</td>
<td align="right">46.0%</td>
<td align="right">9,235,043</td>
<td align="right">46.0%</td>
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
<td align="right">10,829,552</td>
<td align="right">53.9%</td>
<td align="right">10,829,552</td>
<td align="right">53.9%</td>
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
<td align="right">9,351</td>
<td align="right">94.1%</td>
<td align="right">9,339</td>
<td align="right">94.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">589</td>
<td align="right">5.9%</td>
<td align="right">589</td>
<td align="right">5.9%</td>
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
<td align="right">131</td>
<td align="right">1.4%</td>
<td align="right">119</td>
<td align="right">1.3%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,403</td>
<td align="right">36.4%</td>
<td align="right">3,403</td>
<td align="right">36.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,401</td>
<td align="right">25.7%</td>
<td align="right">2,401</td>
<td align="right">25.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,492</td>
<td align="right">16.0%</td>
<td align="right">1,492</td>
<td align="right">16.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,017</td>
<td align="right">10.9%</td>
<td align="right">1,017</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">251</td>
<td align="right">2.7%</td>
<td align="right">251</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">230</td>
<td align="right">2.5%</td>
<td align="right">230</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">2.4%</td>
<td align="right">229</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">66</td>
<td align="right">0.7%</td>
<td align="right">66</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.7%</td>
<td align="right">66</td>
<td align="right">0.7%</td>
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
<td align="left">xor</td>
<td align="right">16</td>
<td align="right">0.2%</td>
<td align="right">16</td>
<td align="right">0.2%</td>
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
<td align="right">2,732,416</td>
<td align="right">100.0%</td>
<td align="right">2,732,416</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,366,707</td>
<td align="right">6.1%</td>
<td align="right">2,366,807</td>
<td align="right">6.1%</td>
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
<td align="right">32,467,028</td>
<td align="right">84.1%</td>
<td align="right">32,466,928</td>
<td align="right">84.1%</td>
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
<td align="right">3,773,243</td>
<td align="right">9.8%</td>
<td align="right">3,773,243</td>
<td align="right">9.8%</td>
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
<td align="right">45,742</td>
<td align="right">89.0%</td>
<td align="right">45,742</td>
<td align="right">89.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,654</td>
<td align="right">11.0%</td>
<td align="right">5,654</td>
<td align="right">11.0%</td>
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
<td align="left">out of range</td>
<td align="right">2,655</td>
<td align="right">47.0%</td>
<td align="right">2,655</td>
<td align="right">47.0%</td>
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
<td align="left">list slice</td>
<td align="right">865</td>
<td align="right">15.3%</td>
<td align="right">865</td>
<td align="right">15.3%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,880,306</td>
<td align="right">0.8%</td>
<td align="right">1,879,093</td>
<td align="right">0.8%</td>
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
<td align="right">14,175</td>
<td align="right">0.0%</td>
<td align="right">14,170</td>
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
<td align="right">239,318,424</td>
<td align="right">99.2%</td>
<td align="right">239,319,548</td>
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
<td align="right">59,430</td>
<td align="right">100.0%</td>
<td align="right">59,430</td>
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
<td align="right">636,795</td>
<td align="right">5.5%</td>
<td align="right">636,698</td>
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
<td align="right">10,926,008</td>
<td align="right">94.4%</td>
<td align="right">10,926,008</td>
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
<td align="right">2,670</td>
<td align="right">66.4%</td>
<td align="right">2,658</td>
<td align="right">66.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,351</td>
<td align="right">33.6%</td>
<td align="right">1,351</td>
<td align="right">33.7%</td>
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
<td align="right">106</td>
<td align="right">4.0%</td>
<td align="right">94</td>
<td align="right">3.5%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,804</td>
<td align="right">67.6%</td>
<td align="right">1,804</td>
<td align="right">67.9%</td>
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
<td align="right">4,364,983</td>
<td align="right">27.1%</td>
<td align="right">4,364,983</td>
<td align="right">27.1%</td>
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
<td align="right">11,734,432</td>
<td align="right">72.9%</td>
<td align="right">11,734,432</td>
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
<td align="right">5,019</td>
<td align="right">90.5%</td>
<td align="right">5,019</td>
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
<td align="right">622</td>
<td align="right">12.4%</td>
<td align="right">622</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,942,966</td>
<td align="right">9.4%</td>
<td align="right">9,942,966</td>
<td align="right">9.4%</td>
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
<td align="right">91,698,152</td>
<td align="right">86.3%</td>
<td align="right">91,698,152</td>
<td align="right">86.3%</td>
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
<td align="right">4,650,539</td>
<td align="right">4.4%</td>
<td align="right">4,650,539</td>
<td align="right">4.4%</td>
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
<td align="right">88,387</td>
<td align="right">94.1%</td>
<td align="right">88,387</td>
<td align="right">94.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,545</td>
<td align="right">5.9%</td>
<td align="right">5,545</td>
<td align="right">5.9%</td>
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
<td align="left">dict items</td>
<td align="right">1,589</td>
<td align="right">28.7%</td>
<td align="right">1,589</td>
<td align="right">28.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,250</td>
<td align="right">22.5%</td>
<td align="right">1,250</td>
<td align="right">22.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">710</td>
<td align="right">12.8%</td>
<td align="right">710</td>
<td align="right">12.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">469</td>
<td align="right">8.5%</td>
<td align="right">469</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">465</td>
<td align="right">8.4%</td>
<td align="right">465</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">351</td>
<td align="right">6.3%</td>
<td align="right">351</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">272</td>
<td align="right">4.9%</td>
<td align="right">272</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">234</td>
<td align="right">4.2%</td>
<td align="right">234</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">97</td>
<td align="right">1.7%</td>
<td align="right">97</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">61</td>
<td align="right">1.1%</td>
<td align="right">61</td>
<td align="right">1.1%</td>
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
<td align="right">95,690,399</td>
<td align="right">28.1%</td>
<td align="right">95,690,271</td>
<td align="right">28.1%</td>
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
<td align="right">197,576,516</td>
<td align="right">58.1%</td>
<td align="right">197,576,552</td>
<td align="right">58.1%</td>
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
<td align="right">46,302,732</td>
<td align="right">13.6%</td>
<td align="right">46,302,727</td>
<td align="right">13.6%</td>
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
<td align="left">Success</td>
<td align="right">1,808,771</td>
<td align="right">96.9%</td>
<td align="right">1,808,768</td>
<td align="right">96.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">57,065</td>
<td align="right">3.1%</td>
<td align="right">57,065</td>
<td align="right">3.1%</td>
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
<td align="left">method</td>
<td align="right">3,203</td>
<td align="right">5.6%</td>
<td align="right">3,203</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,856</td>
<td align="right">5.0%</td>
<td align="right">2,856</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,294</td>
<td align="right">2.3%</td>
<td align="right">1,294</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">993</td>
<td align="right">1.7%</td>
<td align="right">993</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">645</td>
<td align="right">1.1%</td>
<td align="right">645</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">636</td>
<td align="right">1.1%</td>
<td align="right">636</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">323</td>
<td align="right">0.6%</td>
<td align="right">323</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">115</td>
<td align="right">0.2%</td>
<td align="right">115</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">71</td>
<td align="right">0.1%</td>
<td align="right">71</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">68</td>
<td align="right">0.1%</td>
<td align="right">68</td>
<td align="right">0.1%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,005</td>
<td align="right">0.0%</td>
<td align="right">3,000</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">209,875,029</td>
<td align="right">100.0%</td>
<td align="right">209,874,937</td>
<td align="right">100.0%</td>
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
<td align="right">12,115</td>
<td align="right">0.0%</td>
<td align="right">12,115</td>
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
<td align="right">19,401</td>
<td align="right">100.0%</td>
<td align="right">19,398</td>
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
<td align="right">10,035,434</td>
<td align="right">29.8%</td>
<td align="right">10,035,434</td>
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
<td align="right">14,054,852</td>
<td align="right">41.7%</td>
<td align="right">14,054,852</td>
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
<td align="right">46,208</td>
<td align="right">470.9%</td>
<td align="right">46,208</td>
<td align="right">470.9%</td>
<td align="right">0.0%</td>
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
<td align="right">1,486,370</td>
<td align="right">14.0%</td>
<td align="right">1,486,370</td>
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
<td align="right">9,156,361</td>
<td align="right">86.0%</td>
<td align="right">9,156,361</td>
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
<td align="right">14,060,359</td>
<td align="right">7.5%</td>
<td align="right">14,060,359</td>
<td align="right">7.5%</td>
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
<td align="right">168,734,239</td>
<td align="right">89.6%</td>
<td align="right">168,734,239</td>
<td align="right">89.6%</td>
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
<td align="right">5,384,927</td>
<td align="right">2.9%</td>
<td align="right">5,384,927</td>
<td align="right">2.9%</td>
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
<td align="right">105,531</td>
<td align="right">41.9%</td>
<td align="right">105,531</td>
<td align="right">41.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">146,241</td>
<td align="right">58.1%</td>
<td align="right">146,241</td>
<td align="right">58.1%</td>
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
<td align="left">number</td>
<td align="right">132,890</td>
<td align="right">90.9%</td>
<td align="right">132,890</td>
<td align="right">90.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,950</td>
<td align="right">6.8%</td>
<td align="right">9,950</td>
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
<td align="right">14,605,561</td>
<td align="right">98.0%</td>
<td align="right">14,605,561</td>
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
<td align="right">119,606,157</td>
<td align="right">3.5%</td>
<td align="right">119,604,916</td>
<td align="right">3.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">103,792,679</td>
<td align="right">3.1%</td>
<td align="right">103,792,437</td>
<td align="right">3.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,283,806,863</td>
<td align="right">37.8%</td>
<td align="right">1,283,807,739</td>
<td align="right">37.8%</td>
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
<td align="right">1,885,629,334</td>
<td align="right">55.6%</td>
<td align="right">1,885,629,010</td>
<td align="right">55.6%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">636,795</td>
<td align="right">0.6%</td>
<td align="right">636,698</td>
<td align="right">0.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,235,140</td>
<td align="right">9.0%</td>
<td align="right">9,235,043</td>
<td align="right">9.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">46,302,732</td>
<td align="right">44.9%</td>
<td align="right">46,302,727</td>
<td align="right">44.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">14,060,359</td>
<td align="right">13.6%</td>
<td align="right">14,060,359</td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,035,434</td>
<td align="right">9.7%</td>
<td align="right">10,035,434</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,942,966</td>
<td align="right">9.6%</td>
<td align="right">9,942,966</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,364,983</td>
<td align="right">4.2%</td>
<td align="right">4,364,983</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,773,243</td>
<td align="right">3.7%</td>
<td align="right">3,773,243</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,732,416</td>
<td align="right">2.7%</td>
<td align="right">2,732,416</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,486,370</td>
<td align="right">1.4%</td>
<td align="right">1,486,370</td>
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
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">10,358,933</td>
<td align="right">8.7%</td>
<td align="right">10,358,805</td>
<td align="right">8.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">44,386,190</td>
<td align="right">37.1%</td>
<td align="right">44,386,190</td>
<td align="right">37.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">17,912,424</td>
<td align="right">15.0%</td>
<td align="right">17,912,424</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">14,564,272</td>
<td align="right">12.2%</td>
<td align="right">14,564,272</td>
<td align="right">12.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,554,980</td>
<td align="right">8.0%</td>
<td align="right">9,554,980</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,690,862</td>
<td align="right">6.4%</td>
<td align="right">7,690,862</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,391,510</td>
<td align="right">3.7%</td>
<td align="right">4,391,510</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,342,048</td>
<td align="right">2.0%</td>
<td align="right">2,342,048</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,325,493</td>
<td align="right">1.9%</td>
<td align="right">2,325,493</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,325,046</td>
<td align="right">1.9%</td>
<td align="right">2,325,046</td>
<td align="right">1.9%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">10,484,701</td>
<td align="right">4.8%</td>
<td align="right">10,484,801</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">18,558,151</td>
<td align="right">8.5%</td>
<td align="right">18,558,023</td>
<td align="right">8.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,619,850</td>
<td align="right">18.1%</td>
<td align="right">39,619,822</td>
<td align="right">18.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,621,573</td>
<td align="right">18.1%</td>
<td align="right">39,621,545</td>
<td align="right">18.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,251,867</td>
<td align="right">18.4%</td>
<td align="right">40,251,839</td>
<td align="right">18.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,251,867</td>
<td align="right">18.4%</td>
<td align="right">40,251,839</td>
<td align="right">18.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">178,914,420</td>
<td align="right">81.6%</td>
<td align="right">178,914,448</td>
<td align="right">81.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">630,294</td>
<td align="right">0.3%</td>
<td align="right">630,294</td>
<td align="right">0.3%</td>
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
<tr>
<td align="left">Frame objects created</td>
<td align="right">6,693,557</td>
<td align="right">3.1%</td>
<td align="right">6,693,557</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,060,630</td>
<td align="right">72.1%</td>
<td align="right">158,060,630</td>
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
<td align="left">Method cache misses</td>
<td align="right">8,328,216</td>
<td align="right"></td>
<td align="right">9,147,336</td>
<td align="right"></td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">10,601,259</td>
<td align="right"></td>
<td align="right">11,484,001</td>
<td align="right"></td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,274,973</td>
<td align="right"></td>
<td align="right">2,338,539</td>
<td align="right"></td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">215,185,014</td>
<td align="right"></td>
<td align="right">214,365,758</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">726,984,995</td>
<td align="right">19.3%</td>
<td align="right">727,826,988</td>
<td align="right">19.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,125,355,602</td>
<td align="right">27.1%</td>
<td align="right">1,126,278,161</td>
<td align="right">27.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,270,903,962</td>
<td align="right">33.8%</td>
<td align="right">1,271,826,850</td>
<td align="right">33.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">155,502,382</td>
<td align="right"></td>
<td align="right">155,438,916</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">709,168,836</td>
<td align="right">17.1%</td>
<td align="right">709,289,594</td>
<td align="right">17.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">91,330,575</td>
<td align="right"></td>
<td align="right">91,329,381</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">91,372,637</td>
<td align="right">32.1%</td>
<td align="right">91,371,443</td>
<td align="right">32.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">204,110,030</td>
<td align="right"></td>
<td align="right">204,109,502</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">546,570,540</td>
<td align="right">13.2%</td>
<td align="right">546,571,670</td>
<td align="right">13.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">191,660,671</td>
<td align="right">67.4%</td>
<td align="right">191,660,319</td>
<td align="right">67.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">193,149,479</td>
<td align="right">67.9%</td>
<td align="right">193,149,127</td>
<td align="right">67.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,773,196,429</td>
<td align="right">42.7%</td>
<td align="right">1,773,194,721</td>
<td align="right">42.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,375,994,055</td>
<td align="right">36.5%</td>
<td align="right">1,375,993,644</td>
<td align="right">36.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">391,238,542</td>
<td align="right">10.4%</td>
<td align="right">391,238,550</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,426,693</td>
<td align="right">0.5%</td>
<td align="right">1,426,693</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">62,115</td>
<td align="right">0.0%</td>
<td align="right">62,115</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,079,694</td>
<td align="right"></td>
<td align="right">3,079,694</td>
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
<td align="right">6,281</td>
<td align="right">13,137,598</td>
<td align="right">263,867,364</td>
<td align="right">16,052,244</td>
<td align="right">24,221,239</td>
<td align="right">6,281</td>
<td align="right">13,137,598</td>
<td align="right">263,867,370</td>
<td align="right">16,052,244</td>
<td align="right">24,221,239</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,129,925,419</td>
<td align="right">918.5%</td>
<td align="right">2,130,465,451</td>
<td align="right">918.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">25,651</td>
<td align="right"></td>
<td align="right">25,651</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">9,928</td>
<td align="right">38.7%</td>
<td align="right">9,928</td>
<td align="right">38.7%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">16,255</td>
<td align="right">63.4%</td>
<td align="right">16,255</td>
<td align="right">63.4%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">15,723</td>
<td align="right">61.3%</td>
<td align="right">15,723</td>
<td align="right">61.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">84</td>
<td align="right">0.3%</td>
<td align="right">84</td>
<td align="right">0.3%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">22</td>
<td align="right">0.1%</td>
<td align="right">22</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
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
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">231,887,516</td>
<td align="right"></td>
<td align="right">231,887,516</td>
<td align="right"></td>
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
<td align="right">9,928</td>
<td align="right"></td>
<td align="right">9,928</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">9,886</td>
<td align="right">99.6%</td>
<td align="right">9,886</td>
<td align="right">99.6%</td>
<td align="right">0.0%</td>
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
<td align="right">450</td>
<td align="right">4.5%</td>
<td align="right">450</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,071</td>
<td align="right">20.9%</td>
<td align="right">2,071</td>
<td align="right">20.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,798</td>
<td align="right">48.3%</td>
<td align="right">4,798</td>
<td align="right">48.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,335</td>
<td align="right">23.5%</td>
<td align="right">2,335</td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">274</td>
<td align="right">2.8%</td>
<td align="right">274</td>
<td align="right">2.8%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,965</td>
<td align="right">19.8%</td>
<td align="right">1,965</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,411</td>
<td align="right">14.2%</td>
<td align="right">1,411</td>
<td align="right">14.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,511</td>
<td align="right">55.5%</td>
<td align="right">5,489</td>
<td align="right">55.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">873</td>
<td align="right">8.8%</td>
<td align="right">895</td>
<td align="right">9.0%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">126</td>
<td align="right">1.3%</td>
<td align="right">126</td>
<td align="right">1.3%</td>
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
<td align="left">_POP_TOP</td>
<td align="right">45,146,278</td>
<td align="right">44,623,057</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">164,281,917</td>
<td align="right">164,281,953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">217,793,114</td>
<td align="right">217,793,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">236,559,406</td>
<td align="right">236,559,406</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">231,887,516</td>
<td align="right">231,887,516</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">178,208,563</td>
<td align="right">178,208,563</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">78,299,981</td>
<td align="right">78,299,981</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">70,971,285</td>
<td align="right">70,971,285</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">69,988,549</td>
<td align="right">69,988,549</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">63,572,981</td>
<td align="right">63,572,981</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">56,605,613</td>
<td align="right">56,605,613</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">54,444,525</td>
<td align="right">54,444,525</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">49,513,292</td>
<td align="right">49,513,292</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">49,513,292</td>
<td align="right">49,513,292</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">35,775,385</td>
<td align="right">35,775,385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">35,327,991</td>
<td align="right">35,327,991</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">34,885,680</td>
<td align="right">34,885,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">34,002,364</td>
<td align="right">34,002,364</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">33,768,934</td>
<td align="right">33,768,934</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">33,569,578</td>
<td align="right">33,569,578</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">33,535,266</td>
<td align="right">33,535,266</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">33,485,515</td>
<td align="right">33,485,515</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">33,348,784</td>
<td align="right">33,348,784</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">32,261,112</td>
<td align="right">32,261,112</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">30,986,742</td>
<td align="right">30,986,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">21,834,186</td>
<td align="right">21,834,186</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">21,302,594</td>
<td align="right">21,302,594</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">15,510,680</td>
<td align="right">15,510,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">12,593,588</td>
<td align="right">12,593,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">12,355,430</td>
<td align="right">12,355,430</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">5,671,876</td>
<td align="right">5,671,876</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">5,325,565</td>
<td align="right">5,325,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,320,656</td>
<td align="right">5,320,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">5,021,753</td>
<td align="right">5,021,753</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">4,830,275</td>
<td align="right">4,830,275</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,671,890</td>
<td align="right">4,671,890</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,165,522</td>
<td align="right">4,165,522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">3,855,598</td>
<td align="right">3,855,598</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,708,054</td>
<td align="right">3,708,054</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,652,732</td>
<td align="right">3,652,732</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,603,805</td>
<td align="right">3,603,805</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,832,471</td>
<td align="right">2,832,471</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,811,014</td>
<td align="right">2,811,014</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,770,639</td>
<td align="right">2,770,639</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,588,084</td>
<td align="right">2,588,084</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,562,111</td>
<td align="right">2,562,111</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,541,250</td>
<td align="right">2,541,250</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,536,495</td>
<td align="right">2,536,495</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,348,199</td>
<td align="right">2,348,199</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,218,653</td>
<td align="right">2,218,653</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,094,520</td>
<td align="right">2,094,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">2,093,362</td>
<td align="right">2,093,362</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,013,661</td>
<td align="right">2,013,661</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,961,021</td>
<td align="right">1,961,021</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,590,589</td>
<td align="right">1,590,589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,256,625</td>
<td align="right">1,256,625</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">1,194,916</td>
<td align="right">1,194,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,190,895</td>
<td align="right">1,190,895</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,155,836</td>
<td align="right">1,155,836</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,125,964</td>
<td align="right">1,125,964</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,074,618</td>
<td align="right">1,074,618</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,001,602</td>
<td align="right">1,001,602</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">997,822</td>
<td align="right">997,822</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">988,300</td>
<td align="right">988,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">969,747</td>
<td align="right">969,747</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">945,217</td>
<td align="right">945,217</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">829,903</td>
<td align="right">829,903</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">722,101</td>
<td align="right">722,101</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">720,669</td>
<td align="right">720,669</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">660,050</td>
<td align="right">660,050</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">660,050</td>
<td align="right">660,050</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">652,230</td>
<td align="right">652,230</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">647,932</td>
<td align="right">647,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">632,779</td>
<td align="right">632,779</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">577,199</td>
<td align="right">577,199</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">470,940</td>
<td align="right">470,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">425,832</td>
<td align="right">425,832</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">400,256</td>
<td align="right">400,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">339,429</td>
<td align="right">339,429</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">328,682</td>
<td align="right">328,682</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">322,605</td>
<td align="right">322,605</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">320,039</td>
<td align="right">320,039</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">319,691</td>
<td align="right">319,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">319,691</td>
<td align="right">319,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">316,949</td>
<td align="right">316,949</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">284,138</td>
<td align="right">284,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">265,121</td>
<td align="right">265,121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">246,304</td>
<td align="right">246,304</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">246,304</td>
<td align="right">246,304</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">220,794</td>
<td align="right">220,794</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">217,689</td>
<td align="right">217,689</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">194,996</td>
<td align="right">194,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">186,482</td>
<td align="right">186,482</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">181,036</td>
<td align="right">181,036</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">179,598</td>
<td align="right">179,598</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">163,298</td>
<td align="right">163,298</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">153,953</td>
<td align="right">153,953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">140,926</td>
<td align="right">140,926</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">140,786</td>
<td align="right">140,786</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">131,082</td>
<td align="right">131,082</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">124,286</td>
<td align="right">124,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">124,223</td>
<td align="right">124,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">123,257</td>
<td align="right">123,257</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">120,767</td>
<td align="right">120,767</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">110,375</td>
<td align="right">110,375</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">102,057</td>
<td align="right">102,057</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">95,467</td>
<td align="right">95,467</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">69,232</td>
<td align="right">69,232</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">60,726</td>
<td align="right">60,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">57,391</td>
<td align="right">57,391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">54,969</td>
<td align="right">54,969</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">32,461</td>
<td align="right">32,461</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">25,643</td>
<td align="right">25,643</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">20,958</td>
<td align="right">20,958</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,426</td>
<td align="right">20,426</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">19,236</td>
<td align="right">19,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">19,236</td>
<td align="right">19,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">19,236</td>
<td align="right">19,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">19,236</td>
<td align="right">19,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">16,317</td>
<td align="right">16,317</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">7,938</td>
<td align="right">7,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,298</td>
<td align="right">6,298</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,298</td>
<td align="right">6,298</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">5,716</td>
<td align="right">5,716</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,691</td>
<td align="right">3,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">3,691</td>
<td align="right">3,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">3,691</td>
<td align="right">3,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">3,561</td>
<td align="right">3,561</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,214</td>
<td align="right">2,214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">1,932</td>
<td align="right">1,932</td>
<td align="right">0.0%</td>
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
<td align="right">248</td>
<td align="right">248</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">248</td>
<td align="right">248</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">139</td>
<td align="right">139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">36</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">36</td>
<td align="right">36</td>
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
<tr>
<td align="left">_POP_TOP_IMMORTAL</td>
<td align="right"></td>
<td align="right">523,221</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_UNDER_INT</td>
<td align="right"></td>
<td align="right">336,959</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_UNDER_IMMORTAL</td>
<td align="right"></td>
<td align="right">198,495</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_UNDER</td>
<td align="right"></td>
<td align="right">4,467</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_UNDER_UNICODE</td>
<td align="right"></td>
<td align="right">39</td>
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
<td align="right">191</td>
<td align="right">191</td>
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
Stats gathered on: 2025-01-15
