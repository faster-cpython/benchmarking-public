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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,314,230</td>
<td align="right">19,877,499</td>
<td align="right">139.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,002,530</td>
<td align="right">804</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">536,416</td>
<td align="right">558</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,030,767</td>
<td align="right">1,191</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">516,315</td>
<td align="right">680</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,068,580</td>
<td align="right">1,644</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">20,683</td>
<td align="right">77</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">153</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,107</td>
<td align="right">1,282</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,137</td>
<td align="right">1,283</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">84,693</td>
<td align="right">1,122</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,547</td>
<td align="right">465</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">588,229</td>
<td align="right">10,431</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">50,952</td>
<td align="right">1,090</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,485</td>
<td align="right">183</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">15,933,217</td>
<td align="right">477,257</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">267,998</td>
<td align="right">10,269</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">268,060</td>
<td align="right">10,331</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">160,793</td>
<td align="right">7,161</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">830</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">8,731</td>
<td align="right">444</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">8,731</td>
<td align="right">444</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">26,276</td>
<td align="right">1,398</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,177,360</td>
<td align="right">121,910</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">150,728</td>
<td align="right">9,663</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">14</td>
<td align="right">1</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,746,133</td>
<td align="right">287,838</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">149,269</td>
<td align="right">12,513</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">9,142</td>
<td align="right">803</td>
<td align="right">-91.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">686,338</td>
<td align="right">67,041</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">43,864</td>
<td align="right">4,621</td>
<td align="right">-89.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">442,169</td>
<td align="right">58,595</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,255,310</td>
<td align="right">529,108</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,773,885</td>
<td align="right">1,272,323</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">21,679</td>
<td align="right">5,128</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">9,376</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">820,293</td>
<td align="right">228,263</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">300,184</td>
<td align="right">83,612</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">181,370</td>
<td align="right">52,664</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,436,030</td>
<td align="right">1,324,049</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">8,951</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,760,539</td>
<td align="right">2,712,562</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">29,902</td>
<td align="right">9,289</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,873</td>
<td align="right">13,791</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">146,988</td>
<td align="right">48,033</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">15</td>
<td align="right">5</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,338,325</td>
<td align="right">2,131,525</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">26,017</td>
<td align="right">9,458</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,585</td>
<td align="right">25,966</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,395,646</td>
<td align="right">1,328,687</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">184,651</td>
<td align="right">73,545</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,129,985</td>
<td align="right">453,113</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">8,529</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">94,327</td>
<td align="right">39,478</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">733,076</td>
<td align="right">1,154,076</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">89,297</td>
<td align="right">38,344</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,486,016</td>
<td align="right">1,070,784</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,487,537</td>
<td align="right">1,585,789</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">803,913</td>
<td align="right">368,418</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">139</td>
<td align="right">64</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,468</td>
<td align="right">26,400</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,553,508</td>
<td align="right">740,472</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">46,206,215</td>
<td align="right">22,248,250</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,315,564</td>
<td align="right">1,617,647</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,801,858</td>
<td align="right">879,505</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">57,473</td>
<td align="right">28,434</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,039,404</td>
<td align="right">1,529,272</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,440,708</td>
<td align="right">1,256,689</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">141,554</td>
<td align="right">210,193</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,356,764</td>
<td align="right">2,309,419</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">357,576</td>
<td align="right">514,495</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">939,298</td>
<td align="right">531,044</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">736,120</td>
<td align="right">1,049,890</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">249,324</td>
<td align="right">353,923</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,096,431</td>
<td align="right">1,226,919</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">378,682</td>
<td align="right">527,228</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,467</td>
<td align="right">13,138</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">22,093</td>
<td align="right">13,762</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,858,718</td>
<td align="right">5,114,300</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">10,342,304</td>
<td align="right">6,798,698</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">39,010</td>
<td align="right">26,138</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,728</td>
<td align="right">8,592</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">66,847</td>
<td align="right">46,099</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">834,296</td>
<td align="right">588,342</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">398,619</td>
<td align="right">515,486</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,763</td>
<td align="right">20,332</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">761,719</td>
<td align="right">541,371</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">28,680</td>
<td align="right">20,393</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">28,685</td>
<td align="right">20,413</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">4,793,421</td>
<td align="right">6,158,347</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">733,551</td>
<td align="right">541,172</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,628,246</td>
<td align="right">4,158,722</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,681,021</td>
<td align="right">1,289,635</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">37,955</td>
<td align="right">29,616</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,867,734</td>
<td align="right">1,493,648</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">792,378</td>
<td align="right">949,245</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,215,965</td>
<td align="right">994,533</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,076,155</td>
<td align="right">7,489,138</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,688,801</td>
<td align="right">12,280,926</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,098</td>
<td align="right">64,714</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,143,335</td>
<td align="right">2,657,028</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,393,924</td>
<td align="right">1,194,404</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,369</td>
<td align="right">53,404</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,408,308</td>
<td align="right">8,297,380</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,344,066</td>
<td align="right">2,115,848</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">489,418</td>
<td align="right">452,131</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">14,219,785</td>
<td align="right">15,226,796</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">407,883</td>
<td align="right">379,542</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">93</td>
<td align="right">97</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">892,576</td>
<td align="right">856,314</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">598,234</td>
<td align="right">621,639</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,737</td>
<td align="right">4,887</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">43,930</td>
<td align="right">42,577</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">453</td>
<td align="right">442</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,482</td>
<td align="right">4,386</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">95</td>
<td align="right">93</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,149</td>
<td align="right">3,097</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,135</td>
<td align="right">13,284</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">368</td>
<td align="right">372</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,358</td>
<td align="right">17,507</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,358</td>
<td align="right">17,507</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,463,477</td>
<td align="right">1,474,436</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,920,446</td>
<td align="right">9,849,257</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,504</td>
<td align="right">36,629</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,396</td>
<td align="right">4,381</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">443,666</td>
<td align="right">444,617</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,033</td>
<td align="right">33,995</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,642</td>
<td align="right">1,818,590</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,067,766</td>
<td align="right">5,067,766</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,466</td>
<td align="right">55,466</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,855</td>
<td align="right">12,855</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,831</td>
<td align="right">12,831</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">8,502</td>
<td align="right">8,502</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">8,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,227</td>
<td align="right">4,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">4,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">742</td>
<td align="right">742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">195</td>
<td align="right">195</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">179</td>
<td align="right">179</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">152</td>
<td align="right">152</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">148</td>
<td align="right">148</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">68</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">37</td>
<td align="right">37</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1</td>
<td align="right">1</td>
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
<td align="right">3,313,653</td>
<td align="right">69.9%</td>
<td align="right">1,616,559</td>
<td align="right">50.5%</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,425,388</td>
<td align="right">30.1%</td>
<td align="right">1,582,297</td>
<td align="right">49.4%</td>
<td align="right">11.0%</td>
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
<td align="right">1,795</td>
<td align="right">93.9%</td>
<td align="right">971</td>
<td align="right">89.2%</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">116</td>
<td align="right">6.1%</td>
<td align="right">117</td>
<td align="right">10.8%</td>
<td align="right">0.9%</td>
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
<td align="right">191</td>
<td align="right">10.6%</td>
<td align="right">60</td>
<td align="right">6.2%</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">482</td>
<td align="right">26.9%</td>
<td align="right">222</td>
<td align="right">22.9%</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">829</td>
<td align="right">46.2%</td>
<td align="right">444</td>
<td align="right">45.7%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">206</td>
<td align="right">11.5%</td>
<td align="right">158</td>
<td align="right">16.3%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">87</td>
<td align="right">4.8%</td>
<td align="right">87</td>
<td align="right">9.0%</td>
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
<td align="right">12,855</td>
<td align="right">100.0%</td>
<td align="right">12,855</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">455,844</td>
<td align="right">92.6%</td>
<td align="right">560,456</td>
<td align="right">93.9%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,211</td>
<td align="right">7.4%</td>
<td align="right">36,328</td>
<td align="right">6.1%</td>
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
<td align="left">Failure</td>
<td align="right">176</td>
<td align="right">60.1%</td>
<td align="right">184</td>
<td align="right">61.1%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">117</td>
<td align="right">39.9%</td>
<td align="right">117</td>
<td align="right">38.9%</td>
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
<td align="right">175</td>
<td align="right">99.4%</td>
<td align="right">183</td>
<td align="right">99.5%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">0.6%</td>
<td align="right">1</td>
<td align="right">0.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,711,408</td>
<td align="right">100.0%</td>
<td align="right">22,522,942</td>
<td align="right">100.0%</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,144</td>
<td align="right">0.0%</td>
<td align="right">1,104</td>
<td align="right">0.0%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">517</td>
<td align="right">0.0%</td>
<td align="right">510</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
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
<td align="right">3,478</td>
<td align="right">100.0%</td>
<td align="right">3,420</td>
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
<td align="right">41</td>
<td align="right">22.9%</td>
<td align="right">41</td>
<td align="right">22.9%</td>
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
<td align="right">397,935</td>
<td align="right">10.1%</td>
<td align="right">514,901</td>
<td align="right">11.0%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,529,964</td>
<td align="right">89.8%</td>
<td align="right">4,157,546</td>
<td align="right">88.9%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,277</td>
<td align="right">0.1%</td>
<td align="right">4,290</td>
<td align="right">0.1%</td>
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
<td align="left">Failure</td>
<td align="right">412</td>
<td align="right">54.9%</td>
<td align="right">320</td>
<td align="right">49.0%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">339</td>
<td align="right">45.1%</td>
<td align="right">333</td>
<td align="right">51.0%</td>
<td align="right">-1.8%</td>
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
<td align="right">95</td>
<td align="right">23.1%</td>
<td align="right">8</td>
<td align="right">2.5%</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">104</td>
<td align="right">25.2%</td>
<td align="right">102</td>
<td align="right">31.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">213</td>
<td align="right">51.7%</td>
<td align="right">210</td>
<td align="right">65.6%</td>
<td align="right">-1.4%</td>
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
<td align="right">1,266,141</td>
<td align="right">100.0%</td>
<td align="right">1,632,247</td>
<td align="right">100.0%</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
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
<td align="right">7</td>
<td align="right">100.0%</td>
<td align="right">7</td>
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
<td align="right">21,788</td>
<td align="right">0.4%</td>
<td align="right">13,501</td>
<td align="right">0.3%</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,504,856</td>
<td align="right">99.6%</td>
<td align="right">4,887,936</td>
<td align="right">99.7%</td>
<td align="right">-11.2%</td>
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
<td align="right">256</td>
<td align="right">83.9%</td>
<td align="right">212</td>
<td align="right">81.2%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">49</td>
<td align="right">16.1%</td>
<td align="right">49</td>
<td align="right">18.8%</td>
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
<td align="right">72</td>
<td align="right">28.1%</td>
<td align="right">28</td>
<td align="right">13.2%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">69</td>
<td align="right">27.0%</td>
<td align="right">69</td>
<td align="right">32.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">50</td>
<td align="right">23.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">50</td>
<td align="right">23.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">2.7%</td>
<td align="right">7</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">1.2%</td>
<td align="right">3</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">2</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">2</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
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
<td align="right">4,347,460</td>
<td align="right">12.0%</td>
<td align="right">2,301,542</td>
<td align="right">5.7%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">333,730</td>
<td align="right">0.9%</td>
<td align="right">183,425</td>
<td align="right">0.5%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">31,474,377</td>
<td align="right">87.0%</td>
<td align="right">37,646,719</td>
<td align="right">93.8%</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
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
<td align="right">4,595</td>
<td align="right">30.0%</td>
<td align="right">3,255</td>
<td align="right">29.0%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,709</td>
<td align="right">70.0%</td>
<td align="right">7,950</td>
<td align="right">71.0%</td>
<td align="right">-25.8%</td>
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
<td align="right">71</td>
<td align="right">1.5%</td>
<td align="right">27</td>
<td align="right">0.8%</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,348</td>
<td align="right">29.3%</td>
<td align="right">597</td>
<td align="right">18.3%</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">189</td>
<td align="right">4.1%</td>
<td align="right">142</td>
<td align="right">4.4%</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,135</td>
<td align="right">24.7%</td>
<td align="right">1,017</td>
<td align="right">31.2%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">10.0%</td>
<td align="right">416</td>
<td align="right">12.8%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">663</td>
<td align="right">14.4%</td>
<td align="right">658</td>
<td align="right">20.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">1.0%</td>
<td align="right">45</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">23</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.5%</td>
<td align="right">23</td>
<td align="right">0.7%</td>
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
<td align="right">12,506,398</td>
<td align="right">100.0%</td>
<td align="right">4,209,823</td>
<td align="right">99.9%</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">796</td>
<td align="right">0.0%</td>
<td align="right">773</td>
<td align="right">0.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
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
<td align="right">274</td>
<td align="right">0.0%</td>
<td align="right">274</td>
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
<td align="right">2,362</td>
<td align="right">100.0%</td>
<td align="right">2,333</td>
<td align="right">100.0%</td>
<td align="right">-1.2%</td>
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
<td align="right">1,375,272</td>
<td align="right">100.0%</td>
<td align="right">1,950,551</td>
<td align="right">100.0%</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13</td>
<td align="right">0.0%</td>
<td align="right">13</td>
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
<td align="right">55</td>
<td align="right">100.0%</td>
<td align="right">55</td>
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
<td align="right">140,654</td>
<td align="right">3.6%</td>
<td align="right">80,854</td>
<td align="right">1.6%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,692,135</td>
<td align="right">94.8%</td>
<td align="right">4,796,681</td>
<td align="right">97.3%</td>
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
<td align="right">59,827</td>
<td align="right">1.5%</td>
<td align="right">51,904</td>
<td align="right">1.1%</td>
<td align="right">-13.2%</td>
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
<td align="right">3,617</td>
<td align="right">86.6%</td>
<td align="right">2,500</td>
<td align="right">82.8%</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">561</td>
<td align="right">13.4%</td>
<td align="right">518</td>
<td align="right">17.2%</td>
<td align="right">-7.7%</td>
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
<td align="right">163</td>
<td align="right">29.1%</td>
<td align="right">120</td>
<td align="right">23.2%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">61.3%</td>
<td align="right">344</td>
<td align="right">66.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">44</td>
<td align="right">7.8%</td>
<td align="right">44</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.8%</td>
<td align="right">10</td>
<td align="right">1.9%</td>
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
<td align="right">21,262</td>
<td align="right">1.6%</td>
<td align="right">12,976</td>
<td align="right">0.8%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,332,279</td>
<td align="right">98.4%</td>
<td align="right">1,698,409</td>
<td align="right">99.2%</td>
<td align="right">27.5%</td>
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
<td align="right">187</td>
<td align="right">91.2%</td>
<td align="right">143</td>
<td align="right">88.3%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18</td>
<td align="right">8.8%</td>
<td align="right">19</td>
<td align="right">11.7%</td>
<td align="right">5.6%</td>
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
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">75</td>
<td align="right">52.4%</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
<td align="right">68</td>
<td align="right">47.6%</td>
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
<td align="right">8,004,400</td>
<td align="right">99.2%</td>
<td align="right">10,793,877</td>
<td align="right">99.6%</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">65,863</td>
<td align="right">0.8%</td>
<td align="right">45,164</td>
<td align="right">0.4%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">28</td>
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
<td align="right">538</td>
<td align="right">54.6%</td>
<td align="right">492</td>
<td align="right">52.5%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">448</td>
<td align="right">45.4%</td>
<td align="right">445</td>
<td align="right">47.5%</td>
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
<td align="left">mapping</td>
<td align="right">174</td>
<td align="right">32.3%</td>
<td align="right">130</td>
<td align="right">26.4%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">135</td>
<td align="right">25.1%</td>
<td align="right">133</td>
<td align="right">27.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">118</td>
<td align="right">21.9%</td>
<td align="right">118</td>
<td align="right">24.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">12.6%</td>
<td align="right">68</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">43</td>
<td align="right">8.0%</td>
<td align="right">43</td>
<td align="right">8.7%</td>
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
<td align="right">1,990,077</td>
<td align="right">100.0%</td>
<td align="right">2,094,533</td>
<td align="right">100.0%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">38</td>
<td align="right">0.0%</td>
<td align="right">38</td>
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
<td align="right">110</td>
<td align="right">100.0%</td>
<td align="right">110</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">81,312,820</td>
<td align="right">31.4%</td>
<td align="right">31,515,526</td>
<td align="right">18.5%</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,300,122</td>
<td align="right">3.2%</td>
<td align="right">4,626,331</td>
<td align="right">2.7%</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">479,541</td>
<td align="right">0.2%</td>
<td align="right">269,627</td>
<td align="right">0.2%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">168,983,371</td>
<td align="right">65.2%</td>
<td align="right">134,242,266</td>
<td align="right">78.7%</td>
<td align="right">-20.6%</td>
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
<td align="right">3,313,653</td>
<td align="right">40.0%</td>
<td align="right">1,616,559</td>
<td align="right">35.1%</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,347,460</td>
<td align="right">52.5%</td>
<td align="right">2,301,542</td>
<td align="right">49.9%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,262</td>
<td align="right">0.3%</td>
<td align="right">12,976</td>
<td align="right">0.3%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,788</td>
<td align="right">0.3%</td>
<td align="right">13,501</td>
<td align="right">0.3%</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">65,863</td>
<td align="right">0.8%</td>
<td align="right">45,164</td>
<td align="right">1.0%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">397,935</td>
<td align="right">4.8%</td>
<td align="right">514,901</td>
<td align="right">11.2%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">59,827</td>
<td align="right">0.7%</td>
<td align="right">51,904</td>
<td align="right">1.1%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,144</td>
<td align="right">0.0%</td>
<td align="right">1,104</td>
<td align="right">0.0%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,211</td>
<td align="right">0.4%</td>
<td align="right">36,328</td>
<td align="right">0.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,855</td>
<td align="right">0.2%</td>
<td align="right">12,855</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,489</td>
<td align="right">10.3%</td>
<td align="right">19,969</td>
<td align="right">7.4%</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">274,191</td>
<td align="right">57.2%</td>
<td align="right">153,415</td>
<td align="right">56.8%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,654</td>
<td align="right">29.3%</td>
<td align="right">80,854</td>
<td align="right">30.0%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,276</td>
<td align="right">0.9%</td>
<td align="right">4,289</td>
<td align="right">1.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">2.1%</td>
<td align="right">9,895</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">269</td>
<td align="right">0.1%</td>
<td align="right">269</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">188</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">144</td>
<td align="right">0.0%</td>
<td align="right">144</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">143</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">86</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">246</td>
<td align="right">0.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">246</td>
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
<td align="right">379,551</td>
<td align="right">1.5%</td>
<td align="right">484,171</td>
<td align="right">1.6%</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">20,776,549</td>
<td align="right">80.5%</td>
<td align="right">25,797,055</td>
<td align="right">83.7%</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">18,389,016</td>
<td align="right">71.3%</td>
<td align="right">22,520,450</td>
<td align="right">73.1%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,985,753</td>
<td align="right">27.1%</td>
<td align="right">7,874,825</td>
<td align="right">25.5%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,985,809</td>
<td align="right">27.1%</td>
<td align="right">7,874,881</td>
<td align="right">25.5%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,412,666</td>
<td align="right">28.7%</td>
<td align="right">8,301,738</td>
<td align="right">26.9%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,412,666</td>
<td align="right">28.7%</td>
<td align="right">8,301,738</td>
<td align="right">26.9%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,369</td>
<td align="right">0.1%</td>
<td align="right">17,518</td>
<td align="right">0.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">426,857</td>
<td align="right">1.7%</td>
<td align="right">426,857</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">15</td>
<td align="right">0.0%</td>
<td align="right">15</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">41</td>
<td align="right">0.0%</td>
<td align="right">41</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<td align="right">1.8%</td>
<td align="right">456,471</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,507</td>
<td align="right">1.7%</td>
<td align="right">441,507</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">24,713</td>
<td align="right"></td>
<td align="right">124,435</td>
<td align="right"></td>
<td align="right">403.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">51,923</td>
<td align="right"></td>
<td align="right">143,204</td>
<td align="right"></td>
<td align="right">175.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">118,579,428</td>
<td align="right">35.9%</td>
<td align="right">218,381,143</td>
<td align="right">51.9%</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">50,819,014</td>
<td align="right">15.4%</td>
<td align="right">82,760,130</td>
<td align="right">19.7%</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">112,383,922</td>
<td align="right">29.4%</td>
<td align="right">181,776,070</td>
<td align="right">36.1%</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">76,426,174</td>
<td align="right">20.0%</td>
<td align="right">123,105,234</td>
<td align="right">24.4%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,132,934</td>
<td align="right"></td>
<td align="right">1,551,280</td>
<td align="right"></td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">27,485</td>
<td align="right"></td>
<td align="right">19,024</td>
<td align="right"></td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">6,817,261</td>
<td align="right"></td>
<td align="right">8,859,555</td>
<td align="right"></td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">54,323,861</td>
<td align="right">16.4%</td>
<td align="right">39,326,900</td>
<td align="right">9.3%</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">106,826,865</td>
<td align="right">32.3%</td>
<td align="right">80,357,286</td>
<td align="right">19.1%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,617,383</td>
<td align="right">49.1%</td>
<td align="right">18,226,357</td>
<td align="right">50.7%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,620,218</td>
<td align="right"></td>
<td align="right">18,229,112</td>
<td align="right"></td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">9,585,863</td>
<td align="right"></td>
<td align="right">11,581,151</td>
<td align="right"></td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,097,059</td>
<td align="right"></td>
<td align="right">19,029,913</td>
<td align="right"></td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,037,092</td>
<td align="right">50.5%</td>
<td align="right">17,599,889</td>
<td align="right">49.0%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">15,158,444</td>
<td align="right">50.9%</td>
<td align="right">17,722,173</td>
<td align="right">49.3%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">53,616,121</td>
<td align="right">14.0%</td>
<td align="right">49,636,476</td>
<td align="right">9.8%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">140,236,711</td>
<td align="right">36.6%</td>
<td align="right">149,672,724</td>
<td align="right">29.7%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,817</td>
<td align="right">0.3%</td>
<td align="right">78,750</td>
<td align="right">0.2%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,535</td>
<td align="right">0.1%</td>
<td align="right">43,534</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.1%</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">346</td>
<td align="right">9.6%</td>
<td align="right">1,904</td>
<td align="right">17.9%</td>
<td align="right">450.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,598</td>
<td align="right"></td>
<td align="right">10,648</td>
<td align="right"></td>
<td align="right">195.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">3,060</td>
<td align="right">85.0%</td>
<td align="right">8,773</td>
<td align="right">82.4%</td>
<td align="right">186.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">3,050</td>
<td align="right">84.8%</td>
<td align="right">8,742</td>
<td align="right">82.1%</td>
<td align="right">186.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">361,402,973</td>
<td align="right">1,719.7%</td>
<td align="right">771,734,883</td>
<td align="right">1,931.5%</td>
<td align="right">113.5%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
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
<td align="right">5.6%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">21,015,303</td>
<td align="right"></td>
<td align="right">39,955,731</td>
<td align="right"></td>
<td align="right">90.1%</td>
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
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1 / 0 !!</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
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
<td align="right">342</td>
<td align="right">98.8%</td>
<td align="right">1,900</td>
<td align="right">99.8%</td>
<td align="right">455.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">346</td>
<td align="right"></td>
<td align="right">1,904</td>
<td align="right"></td>
<td align="right">450.3%</td>
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
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2 / 0 !!</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">4</td>
<td align="right">1.2%</td>
<td align="right">4</td>
<td align="right">0.2%</td>
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
<td align="right">3</td>
<td align="right">0.2%</td>
<td align="right">3 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">93</td>
<td align="right">26.9%</td>
<td align="right">175</td>
<td align="right">9.2%</td>
<td align="right">88.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">23</td>
<td align="right">6.6%</td>
<td align="right">400</td>
<td align="right">21.0%</td>
<td align="right">1,639.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">66</td>
<td align="right">19.1%</td>
<td align="right">845</td>
<td align="right">44.4%</td>
<td align="right">1,180.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">113</td>
<td align="right">32.7%</td>
<td align="right">273</td>
<td align="right">14.3%</td>
<td align="right">141.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">23</td>
<td align="right">6.6%</td>
<td align="right">157</td>
<td align="right">8.2%</td>
<td align="right">582.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">27</td>
<td align="right">7.8%</td>
<td align="right">50</td>
<td align="right">2.6%</td>
<td align="right">85.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1</td>
<td align="right">0.3%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
<td align="right">49</td>
<td align="right">14.2%</td>
<td align="right">88</td>
<td align="right">4.6%</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">61</td>
<td align="right">17.6%</td>
<td align="right">338</td>
<td align="right">17.8%</td>
<td align="right">454.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">29</td>
<td align="right">8.4%</td>
<td align="right">676</td>
<td align="right">35.5%</td>
<td align="right">2,231.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">90</td>
<td align="right">26.0%</td>
<td align="right">482</td>
<td align="right">25.3%</td>
<td align="right">435.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">76</td>
<td align="right">22.0%</td>
<td align="right">146</td>
<td align="right">7.7%</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">34</td>
<td align="right">9.8%</td>
<td align="right">154</td>
<td align="right">8.1%</td>
<td align="right">352.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3</td>
<td align="right">0.9%</td>
<td align="right">16</td>
<td align="right">0.8%</td>
<td align="right">433.3%</td>
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
<td align="left">_STORE_DEREF</td>
<td align="right">2</td>
<td align="right">103,827</td>
<td align="right">5,191,250.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">2</td>
<td align="right">29,084</td>
<td align="right">1,454,100.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2</td>
<td align="right">29,084</td>
<td align="right">1,454,100.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">6</td>
<td align="right">83,577</td>
<td align="right">1,392,850.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">4</td>
<td align="right">39,247</td>
<td align="right">981,075.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">59</td>
<td align="right">185,214</td>
<td align="right">313,822.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">21</td>
<td align="right">61,038</td>
<td align="right">290,557.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">4</td>
<td align="right">8,435</td>
<td align="right">210,775.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">4,151</td>
<td align="right">366,494</td>
<td align="right">8,729.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">4,151</td>
<td align="right">366,494</td>
<td align="right">8,729.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">4,151</td>
<td align="right">197,522</td>
<td align="right">4,658.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">4,151</td>
<td align="right">197,522</td>
<td align="right">4,658.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">189</td>
<td align="right">8,504</td>
<td align="right">4,399.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">16,802</td>
<td align="right">241,302</td>
<td align="right">1,336.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">6,385</td>
<td align="right">61,280</td>
<td align="right">859.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">8,302</td>
<td align="right">74,536</td>
<td align="right">797.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,385</td>
<td align="right">57,131</td>
<td align="right">794.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,385</td>
<td align="right">57,131</td>
<td align="right">794.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">548,799</td>
<td align="right">4,319,747</td>
<td align="right">687.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">548,799</td>
<td align="right">4,319,747</td>
<td align="right">687.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">3,831,009</td>
<td align="right">25,690,634</td>
<td align="right">570.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,077</td>
<td align="right">24,871</td>
<td align="right">510.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">116,314</td>
<td align="right">703,876</td>
<td align="right">505.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">348,944</td>
<td align="right">1,991,159</td>
<td align="right">470.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">348,944</td>
<td align="right">1,953,799</td>
<td align="right">459.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">348,942</td>
<td align="right">1,925,947</td>
<td align="right">451.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,312,883</td>
<td align="right">6,603,033</td>
<td align="right">402.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">153,496</td>
<td align="right">771,221</td>
<td align="right">402.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,171,529</td>
<td align="right">5,047,739</td>
<td align="right">330.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">823,550</td>
<td align="right">3,297,242</td>
<td align="right">300.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,530,885</td>
<td align="right">5,595,752</td>
<td align="right">265.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">10,389,400</td>
<td align="right">37,183,862</td>
<td align="right">257.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,163,371</td>
<td align="right">4,147,535</td>
<td align="right">256.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">348,948</td>
<td align="right">1,230,689</td>
<td align="right">252.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">14,341</td>
<td align="right">50,481</td>
<td align="right">252.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">348,942</td>
<td align="right">1,226,282</td>
<td align="right">251.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">4</td>
<td align="right">14</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,204,003</td>
<td align="right">7,599,756</td>
<td align="right">244.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,849,998</td>
<td align="right">12,366,610</td>
<td align="right">221.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">251,526</td>
<td align="right">791,807</td>
<td align="right">214.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">547,008</td>
<td align="right">1,713,090</td>
<td align="right">213.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">16,864</td>
<td align="right">52,321</td>
<td align="right">210.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,030,895</td>
<td align="right">3,183,252</td>
<td align="right">208.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,870,044</td>
<td align="right">5,763,607</td>
<td align="right">208.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">465,590</td>
<td align="right">1,423,991</td>
<td align="right">205.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,695,743</td>
<td align="right">11,291,271</td>
<td align="right">205.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">349,173</td>
<td align="right">1,065,741</td>
<td align="right">205.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">4,608,118</td>
<td align="right">13,901,037</td>
<td align="right">201.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">4,242,751</td>
<td align="right">12,798,475</td>
<td align="right">201.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,305,359</td>
<td align="right">3,820,710</td>
<td align="right">192.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,602,703</td>
<td align="right">7,566,014</td>
<td align="right">190.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,672,809</td>
<td align="right">7,458,930</td>
<td align="right">179.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,672,809</td>
<td align="right">7,458,930</td>
<td align="right">179.1%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">581,801</td>
<td align="right">1,588,273</td>
<td align="right">173.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,779,460</td>
<td align="right">4,831,476</td>
<td align="right">171.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">1,955,287</td>
<td align="right">5,224,137</td>
<td align="right">167.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,283,847</td>
<td align="right">3,345,528</td>
<td align="right">160.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">3,054,004</td>
<td align="right">7,928,534</td>
<td align="right">159.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">3,054,004</td>
<td align="right">7,928,534</td>
<td align="right">159.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,947,836</td>
<td align="right">23,111,288</td>
<td align="right">158.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">6,568,498</td>
<td align="right">16,782,905</td>
<td align="right">155.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,704,831</td>
<td align="right">6,862,793</td>
<td align="right">153.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,001,095</td>
<td align="right">2,520,348</td>
<td align="right">151.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,759,110</td>
<td align="right">4,407,679</td>
<td align="right">150.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">632,539</td>
<td align="right">1,581,904</td>
<td align="right">150.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,788,573</td>
<td align="right">16,806,982</td>
<td align="right">147.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,086,005</td>
<td align="right">7,630,170</td>
<td align="right">147.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">895,513</td>
<td align="right">2,200,419</td>
<td align="right">145.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">130,830</td>
<td align="right">319,783</td>
<td align="right">144.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">44,021</td>
<td align="right">105,597</td>
<td align="right">139.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,621,009</td>
<td align="right">6,251,323</td>
<td align="right">138.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">411,730</td>
<td align="right">946,936</td>
<td align="right">130.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,391</td>
<td align="right">14,695</td>
<td align="right">129.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,391</td>
<td align="right">14,695</td>
<td align="right">129.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">411,776</td>
<td align="right">944,166</td>
<td align="right">129.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">15,576,092</td>
<td align="right">33,593,901</td>
<td align="right">115.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,496,342</td>
<td align="right">3,130,858</td>
<td align="right">109.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">11,921</td>
<td align="right">24,793</td>
<td align="right">108.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">532,493</td>
<td align="right">1,090,978</td>
<td align="right">104.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">30,617,374</td>
<td align="right">61,679,316</td>
<td align="right">101.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">9,253,358</td>
<td align="right">18,575,345</td>
<td align="right">100.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">21,889,738</td>
<td align="right">43,856,291</td>
<td align="right">100.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,374,668</td>
<td align="right">2,715,381</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">8,564</td>
<td align="right">16,903</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">8,564</td>
<td align="right">16,903</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,425,887</td>
<td align="right">2,782,531</td>
<td align="right">95.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">829,765</td>
<td align="right">1,616,736</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">361,216</td>
<td align="right">699,154</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">7,255,307</td>
<td align="right">14,023,310</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">7,238,505</td>
<td align="right">13,782,008</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">21,015,303</td>
<td align="right">39,955,731</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">21,624,594</td>
<td align="right">40,615,705</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">8,991,937</td>
<td align="right">16,851,740</td>
<td align="right">87.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,887,842</td>
<td align="right">3,527,729</td>
<td align="right">86.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,332,780</td>
<td align="right">4,313,246</td>
<td align="right">84.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,160,726</td>
<td align="right">2,104,586</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">993,730</td>
<td align="right">1,789,381</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">116,430</td>
<td align="right">208,613</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,352,510</td>
<td align="right">14,345,851</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">532,136</td>
<td align="right">913,121</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,305,164</td>
<td align="right">2,228,741</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,881,633</td>
<td align="right">3,206,743</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,075,403</td>
<td align="right">1,819,561</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,568,893</td>
<td align="right">4,276,398</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">116,372</td>
<td align="right">189,239</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,602,090</td>
<td align="right">2,541,221</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">60,911</td>
<td align="right">89,759</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">257,287</td>
<td align="right">378,450</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">120,339</td>
<td align="right">176,773</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">390,228</td>
<td align="right">563,697</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">390,228</td>
<td align="right">563,697</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">244,908</td>
<td align="right">353,656</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">8,582,063</td>
<td align="right">12,207,012</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">60,907</td>
<td align="right">85,785</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">18,748,731</td>
<td align="right">26,356,554</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">191</td>
<td align="right">266</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">836,381</td>
<td align="right">1,103,199</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">671,703</td>
<td align="right">865,581</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">671,709</td>
<td align="right">865,572</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,375,013</td>
<td align="right">1,750,272</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">418,191</td>
<td align="right">529,561</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,340,861</td>
<td align="right">6,755,791</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,457,101</td>
<td align="right">8,147,263</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,457,101</td>
<td align="right">8,147,263</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">4,816,785</td>
<td align="right">5,946,862</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,024,231</td>
<td align="right">4,641,264</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">473,242</td>
<td align="right">365,977</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">544,590</td>
<td align="right">646,648</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,918,167</td>
<td align="right">3,409,247</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">544,531</td>
<td align="right">634,134</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,422,347</td>
<td align="right">6,305,337</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">534,595</td>
<td align="right">615,698</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">61,094</td>
<td align="right">69,424</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">60,907</td>
<td align="right">69,194</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">60,907</td>
<td align="right">69,194</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">572,233</td>
<td align="right">645,308</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">411,718</td>
<td align="right">461,580</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">609,291</td>
<td align="right">659,974</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">59</td>
<td align="right">55</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,657,862</td>
<td align="right">2,828,806</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">819,293</td>
<td align="right">827,580</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">918,323</td>
<td align="right">926,610</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">411,698</td>
<td align="right">410,746</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">411,726</td>
<td align="right">411,759</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">422,270</td>
<td align="right">422,285</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,645,240</td>
<td align="right">4,645,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">16,395</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">4</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">1,209,697</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">1,209,697</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right"></td>
<td align="right">205,886</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right"></td>
<td align="right">205,886</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right"></td>
<td align="right">103,854</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">45,509</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">41,619</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">37,377</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">37,289</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">37,276</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">29,070</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">29,068</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">29,033</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">28,992</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">23,647</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">20,746</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right"></td>
<td align="right">20,551</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">16,574</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right"></td>
<td align="right">16,574</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">12,459</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right"></td>
<td align="right">12,414</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">12,384</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">12,384</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">8,302</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">8,287</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">8,287</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">7,924</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">4,172</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">34</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">17</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">13</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">13</td>
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
<td align="right">156</td>
<td align="right">1,009</td>
<td align="right">546.8%</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-25
