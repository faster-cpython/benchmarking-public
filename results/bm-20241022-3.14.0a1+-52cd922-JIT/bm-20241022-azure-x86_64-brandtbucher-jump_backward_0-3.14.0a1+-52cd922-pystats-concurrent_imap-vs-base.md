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
<td align="right">8,504,468</td>
<td align="right">20,137,881</td>
<td align="right">136.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,103,734</td>
<td align="right">533</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,131,971</td>
<td align="right">840</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">566,917</td>
<td align="right">427</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">587,124</td>
<td align="right">643</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,169,784</td>
<td align="right">1,293</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">20,695</td>
<td align="right">54</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">105</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">84,693</td>
<td align="right">675</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,107</td>
<td align="right">1,201</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,137</td>
<td align="right">1,202</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">50,952</td>
<td align="right">676</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,547</td>
<td align="right">432</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">638,831</td>
<td align="right">9,691</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,485</td>
<td align="right">169</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">8,731</td>
<td align="right">176</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">8,731</td>
<td align="right">176</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">26,276</td>
<td align="right">720</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">16,743,531</td>
<td align="right">461,531</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">293,292</td>
<td align="right">9,787</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">293,354</td>
<td align="right">9,849</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">642</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">173,448</td>
<td align="right">6,988</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,278,574</td>
<td align="right">120,880</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">163,378</td>
<td align="right">9,395</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">14</td>
<td align="right">1</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,986,597</td>
<td align="right">287,621</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">149,271</td>
<td align="right">11,981</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">749,583</td>
<td align="right">67,558</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">9,142</td>
<td align="right">840</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">43,864</td>
<td align="right">4,621</td>
<td align="right">-89.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">454,897</td>
<td align="right">57,459</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,495,500</td>
<td align="right">525,594</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,217,098</td>
<td align="right">1,277,664</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">21,683</td>
<td align="right">4,824</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">9,178</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">896,324</td>
<td align="right">230,411</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">194,012</td>
<td align="right">52,311</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">300,229</td>
<td align="right">82,009</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,790,419</td>
<td align="right">1,331,096</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">9,443,760</td>
<td align="right">2,723,026</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">8,847</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">29,954</td>
<td align="right">9,012</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,831,933</td>
<td align="right">2,140,061</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,873</td>
<td align="right">13,758</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">146,979</td>
<td align="right">47,263</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">15</td>
<td align="right">5</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">26,019</td>
<td align="right">9,088</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,661,567</td>
<td align="right">1,337,194</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,231,307</td>
<td align="right">456,534</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,585</td>
<td align="right">25,582</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,739,094</td>
<td align="right">1,083,299</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">184,604</td>
<td align="right">74,704</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">8,519</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">879,924</td>
<td align="right">372,320</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">94,413</td>
<td align="right">40,040</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,715,189</td>
<td align="right">1,601,585</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">139</td>
<td align="right">60</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">89,332</td>
<td align="right">39,253</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,667,383</td>
<td align="right">743,191</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,644,751</td>
<td align="right">1,636,139</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,966,155</td>
<td align="right">22,384,155</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,890,435</td>
<td align="right">878,984</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">758,401</td>
<td align="right">1,162,029</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,468</td>
<td align="right">26,352</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">57,481</td>
<td align="right">28,002</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,579,945</td>
<td align="right">1,262,271</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,102,764</td>
<td align="right">1,529,508</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,673,331</td>
<td align="right">2,332,987</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">977,496</td>
<td align="right">530,281</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,210,661</td>
<td align="right">1,230,595</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,469</td>
<td align="right">12,940</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">22,090</td>
<td align="right">13,494</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,402,826</td>
<td align="right">5,149,863</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">154,209</td>
<td align="right">212,310</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">10,797,812</td>
<td align="right">6,832,621</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">44,003</td>
<td align="right">28,116</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">910,286</td>
<td align="right">594,469</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">837,649</td>
<td align="right">547,348</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">39,010</td>
<td align="right">25,822</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,728</td>
<td align="right">8,512</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">809,310</td>
<td align="right">548,228</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">395,519</td>
<td align="right">520,730</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">812,016</td>
<td align="right">1,062,375</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">274,624</td>
<td align="right">358,079</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,763</td>
<td align="right">20,127</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">66,768</td>
<td align="right">46,915</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">28,680</td>
<td align="right">20,188</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">28,689</td>
<td align="right">20,202</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,830,539</td>
<td align="right">4,170,640</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,820,316</td>
<td align="right">1,302,918</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">416,623</td>
<td align="right">533,190</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,943,803</td>
<td align="right">1,499,038</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,291,988</td>
<td align="right">999,512</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">37,964</td>
<td align="right">29,616</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,135,170</td>
<td align="right">6,214,840</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,418,032</td>
<td align="right">7,513,095</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">436,640</td>
<td align="right">521,749</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,495,196</td>
<td align="right">1,206,319</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">15,246,345</td>
<td align="right">12,325,415</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,283,067</td>
<td align="right">2,669,709</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,098</td>
<td align="right">64,666</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">830,326</td>
<td align="right">955,499</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">445,851</td>
<td align="right">383,430</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,470,467</td>
<td align="right">2,128,037</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,371</td>
<td align="right">53,111</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,623,323</td>
<td align="right">8,332,708</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">96</td>
<td align="right">104</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">489,422</td>
<td align="right">451,702</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">93</td>
<td align="right">97</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">892,602</td>
<td align="right">857,041</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">14,915,558</td>
<td align="right">15,488,740</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">476</td>
<td align="right">458</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">10,440,393</td>
<td align="right">10,080,367</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,805</td>
<td align="right">4,940</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">610,947</td>
<td align="right">623,754</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">368</td>
<td align="right">372</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,203</td>
<td align="right">13,338</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,510</td>
<td align="right">4,555</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,426</td>
<td align="right">17,561</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,426</td>
<td align="right">17,561</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,155</td>
<td align="right">3,142</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">443,472</td>
<td align="right">445,018</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,396</td>
<td align="right">4,381</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,576</td>
<td align="right">36,688</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,038</td>
<td align="right">34,007</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,476,190</td>
<td align="right">1,476,536</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,831</td>
<td align="right">12,833</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,647</td>
<td align="right">1,818,609</td>
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
<td align="right"></td>
<td align="right"></td>
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
<td align="right">3,642,725</td>
<td align="right">71.3%</td>
<td align="right">1,635,009</td>
<td align="right">50.7%</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,463,428</td>
<td align="right">28.6%</td>
<td align="right">1,588,642</td>
<td align="right">49.3%</td>
<td align="right">8.6%</td>
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
<td align="right">1,909</td>
<td align="right">94.2%</td>
<td align="right">1,009</td>
<td align="right">89.3%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">117</td>
<td align="right">5.8%</td>
<td align="right">121</td>
<td align="right">10.7%</td>
<td align="right">3.4%</td>
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
<td align="right">10.0%</td>
<td align="right">36</td>
<td align="right">3.6%</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">526</td>
<td align="right">27.6%</td>
<td align="right">240</td>
<td align="right">23.8%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">900</td>
<td align="right">47.1%</td>
<td align="right">485</td>
<td align="right">48.1%</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">205</td>
<td align="right">10.7%</td>
<td align="right">161</td>
<td align="right">16.0%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">87</td>
<td align="right">4.6%</td>
<td align="right">87</td>
<td align="right">8.6%</td>
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
<td align="right">481,144</td>
<td align="right">92.9%</td>
<td align="right">564,612</td>
<td align="right">93.9%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,279</td>
<td align="right">7.0%</td>
<td align="right">36,385</td>
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
<td align="right">180</td>
<td align="right">60.6%</td>
<td align="right">186</td>
<td align="right">61.4%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">117</td>
<td align="right">39.4%</td>
<td align="right">117</td>
<td align="right">38.6%</td>
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
<td align="right">179</td>
<td align="right">99.4%</td>
<td align="right">185</td>
<td align="right">99.5%</td>
<td align="right">3.4%</td>
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
<td align="right">18,875,910</td>
<td align="right">100.0%</td>
<td align="right">22,715,117</td>
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
<td align="right">1,202</td>
<td align="right">0.0%</td>
<td align="right">1,179</td>
<td align="right">0.0%</td>
<td align="right">-1.9%</td>
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
<td align="right">3,448</td>
<td align="right">100.0%</td>
<td align="right">3,514</td>
<td align="right">100.0%</td>
<td align="right">1.9%</td>
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
<td align="right">435,935</td>
<td align="right">10.6%</td>
<td align="right">521,135</td>
<td align="right">11.1%</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,681,924</td>
<td align="right">89.3%</td>
<td align="right">4,182,680</td>
<td align="right">88.8%</td>
<td align="right">13.6%</td>
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
<td align="right">4,331</td>
<td align="right">0.1%</td>
<td align="right">1.3%</td>
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
<td align="right">435</td>
<td align="right">56.3%</td>
<td align="right">347</td>
<td align="right">50.7%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">337</td>
<td align="right">43.7%</td>
<td align="right">337</td>
<td align="right">49.3%</td>
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
<td align="right">95</td>
<td align="right">21.8%</td>
<td align="right">6</td>
<td align="right">1.7%</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">103</td>
<td align="right">23.7%</td>
<td align="right">107</td>
<td align="right">30.8%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">237</td>
<td align="right">54.5%</td>
<td align="right">234</td>
<td align="right">67.4%</td>
<td align="right">-1.3%</td>
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
<td align="right">1,354,666</td>
<td align="right">100.0%</td>
<td align="right">1,646,780</td>
<td align="right">100.0%</td>
<td align="right">21.6%</td>
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
<td align="right">13,233</td>
<td align="right">0.3%</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,580,891</td>
<td align="right">99.6%</td>
<td align="right">4,889,817</td>
<td align="right">99.7%</td>
<td align="right">-12.4%</td>
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
<td align="right">84.8%</td>
<td align="right">212</td>
<td align="right">81.2%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">46</td>
<td align="right">15.2%</td>
<td align="right">49</td>
<td align="right">18.8%</td>
<td align="right">6.5%</td>
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
<td align="right">4,663,941</td>
<td align="right">12.2%</td>
<td align="right">2,324,895</td>
<td align="right">5.7%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">333,830</td>
<td align="right">0.9%</td>
<td align="right">184,355</td>
<td align="right">0.5%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">33,233,833</td>
<td align="right">86.9%</td>
<td align="right">37,922,640</td>
<td align="right">93.8%</td>
<td align="right">14.1%</td>
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
<td align="right">4,740</td>
<td align="right">30.8%</td>
<td align="right">3,320</td>
<td align="right">29.0%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,658</td>
<td align="right">69.2%</td>
<td align="right">8,121</td>
<td align="right">71.0%</td>
<td align="right">-23.8%</td>
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
<td align="right">26</td>
<td align="right">0.8%</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,348</td>
<td align="right">28.4%</td>
<td align="right">549</td>
<td align="right">16.5%</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">189</td>
<td align="right">4.0%</td>
<td align="right">141</td>
<td align="right">4.2%</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,225</td>
<td align="right">25.8%</td>
<td align="right">1,093</td>
<td align="right">32.9%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">9.7%</td>
<td align="right">415</td>
<td align="right">12.5%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">699</td>
<td align="right">14.7%</td>
<td align="right">703</td>
<td align="right">21.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.9%</td>
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
<td align="right">13,430,083</td>
<td align="right">100.0%</td>
<td align="right">4,234,647</td>
<td align="right">99.9%</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">820</td>
<td align="right">0.0%</td>
<td align="right">793</td>
<td align="right">0.0%</td>
<td align="right">-3.3%</td>
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
<td align="right">2,344</td>
<td align="right">100.0%</td>
<td align="right">2,358</td>
<td align="right">100.0%</td>
<td align="right">0.6%</td>
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
<td align="right">1,514,399</td>
<td align="right">100.0%</td>
<td align="right">1,973,413</td>
<td align="right">100.0%</td>
<td align="right">30.3%</td>
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
<td align="right">3.4%</td>
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
<td align="right">3,945,144</td>
<td align="right">95.1%</td>
<td align="right">4,838,322</td>
<td align="right">97.3%</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">59,828</td>
<td align="right">1.4%</td>
<td align="right">51,607</td>
<td align="right">1.0%</td>
<td align="right">-13.7%</td>
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
<td align="right">3,618</td>
<td align="right">86.6%</td>
<td align="right">2,504</td>
<td align="right">82.9%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">561</td>
<td align="right">13.4%</td>
<td align="right">518</td>
<td align="right">17.1%</td>
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
<td align="right">21,263</td>
<td align="right">1.5%</td>
<td align="right">12,775</td>
<td align="right">0.7%</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,420,943</td>
<td align="right">98.5%</td>
<td align="right">1,712,182</td>
<td align="right">99.2%</td>
<td align="right">20.5%</td>
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
<td align="right">90.8%</td>
<td align="right">142</td>
<td align="right">86.1%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">19</td>
<td align="right">9.2%</td>
<td align="right">23</td>
<td align="right">13.9%</td>
<td align="right">21.1%</td>
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
<td align="right">74</td>
<td align="right">52.1%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
<td align="right">68</td>
<td align="right">47.9%</td>
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
<td align="right">65,790</td>
<td align="right">0.8%</td>
<td align="right">45,975</td>
<td align="right">0.4%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,700,038</td>
<td align="right">99.2%</td>
<td align="right">10,909,154</td>
<td align="right">99.6%</td>
<td align="right">25.4%</td>
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
<td align="right">537</td>
<td align="right">54.8%</td>
<td align="right">493</td>
<td align="right">52.3%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">443</td>
<td align="right">45.2%</td>
<td align="right">449</td>
<td align="right">47.7%</td>
<td align="right">1.4%</td>
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
<td align="right">176</td>
<td align="right">32.8%</td>
<td align="right">132</td>
<td align="right">26.8%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">132</td>
<td align="right">24.6%</td>
<td align="right">132</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">118</td>
<td align="right">22.0%</td>
<td align="right">118</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">12.7%</td>
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
<td align="right">2,015,404</td>
<td align="right">100.0%</td>
<td align="right">2,098,737</td>
<td align="right">100.0%</td>
<td align="right">4.1%</td>
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
<td align="right">86,401,114</td>
<td align="right">31.6%</td>
<td align="right">31,652,479</td>
<td align="right">18.4%</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,983,925</td>
<td align="right">3.3%</td>
<td align="right">4,674,984</td>
<td align="right">2.7%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">479,639</td>
<td align="right">0.2%</td>
<td align="right">270,614</td>
<td align="right">0.2%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">177,466,399</td>
<td align="right">64.9%</td>
<td align="right">135,412,561</td>
<td align="right">78.7%</td>
<td align="right">-23.7%</td>
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
<td align="right">3,642,725</td>
<td align="right">40.6%</td>
<td align="right">1,635,009</td>
<td align="right">35.1%</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,663,941</td>
<td align="right">52.0%</td>
<td align="right">2,324,895</td>
<td align="right">49.9%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,263</td>
<td align="right">0.2%</td>
<td align="right">12,775</td>
<td align="right">0.3%</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,788</td>
<td align="right">0.2%</td>
<td align="right">13,233</td>
<td align="right">0.3%</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">65,790</td>
<td align="right">0.7%</td>
<td align="right">45,975</td>
<td align="right">1.0%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">435,935</td>
<td align="right">4.9%</td>
<td align="right">521,135</td>
<td align="right">11.2%</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">59,828</td>
<td align="right">0.7%</td>
<td align="right">51,607</td>
<td align="right">1.1%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,202</td>
<td align="right">0.0%</td>
<td align="right">1,179</td>
<td align="right">0.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,279</td>
<td align="right">0.4%</td>
<td align="right">36,385</td>
<td align="right">0.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,855</td>
<td align="right">0.1%</td>
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
<td align="right">49,519</td>
<td align="right">10.3%</td>
<td align="right">19,975</td>
<td align="right">7.4%</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">274,261</td>
<td align="right">57.2%</td>
<td align="right">154,344</td>
<td align="right">57.0%</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,654</td>
<td align="right">29.3%</td>
<td align="right">80,854</td>
<td align="right">29.8%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,276</td>
<td align="right">0.9%</td>
<td align="right">4,330</td>
<td align="right">1.6%</td>
<td align="right">1.3%</td>
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
<td align="right">262</td>
<td align="right">0.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">262</td>
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
<td align="right">404,837</td>
<td align="right">1.5%</td>
<td align="right">488,308</td>
<td align="right">1.6%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">21,990,927</td>
<td align="right">81.4%</td>
<td align="right">25,998,626</td>
<td align="right">83.8%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">19,388,379</td>
<td align="right">71.8%</td>
<td align="right">22,686,693</td>
<td align="right">73.1%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,200,768</td>
<td align="right">26.7%</td>
<td align="right">7,910,153</td>
<td align="right">25.5%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,200,824</td>
<td align="right">26.7%</td>
<td align="right">7,910,209</td>
<td align="right">25.5%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,627,681</td>
<td align="right">28.2%</td>
<td align="right">8,337,066</td>
<td align="right">26.9%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,627,681</td>
<td align="right">28.2%</td>
<td align="right">8,337,066</td>
<td align="right">26.9%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,437</td>
<td align="right">0.1%</td>
<td align="right">17,572</td>
<td align="right">0.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">426,857</td>
<td align="right">1.6%</td>
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
<td align="right">1.7%</td>
<td align="right">456,471</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,507</td>
<td align="right">1.6%</td>
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
<td align="right">21,610</td>
<td align="right"></td>
<td align="right">50,946</td>
<td align="right"></td>
<td align="right">135.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">45,887</td>
<td align="right"></td>
<td align="right">83,517</td>
<td align="right"></td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">124,202,494</td>
<td align="right">35.7%</td>
<td align="right">221,246,975</td>
<td align="right">52.0%</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">117,173,111</td>
<td align="right">29.1%</td>
<td align="right">184,083,018</td>
<td align="right">36.1%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">53,784,381</td>
<td align="right">15.4%</td>
<td align="right">83,357,354</td>
<td align="right">19.6%</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">80,454,571</td>
<td align="right">20.0%</td>
<td align="right">124,112,047</td>
<td align="right">24.4%</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">24,500</td>
<td align="right"></td>
<td align="right">32,832</td>
<td align="right"></td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">57,677,807</td>
<td align="right">16.6%</td>
<td align="right">39,572,886</td>
<td align="right">9.3%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">112,472,095</td>
<td align="right">32.3%</td>
<td align="right">80,926,793</td>
<td align="right">19.0%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,234,138</td>
<td align="right"></td>
<td align="right">1,567,938</td>
<td align="right"></td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,389,908</td>
<td align="right"></td>
<td align="right">9,027,922</td>
<td align="right"></td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">15,490,056</td>
<td align="right">49.5%</td>
<td align="right">18,370,710</td>
<td align="right">50.8%</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">15,492,795</td>
<td align="right"></td>
<td align="right">18,373,503</td>
<td align="right"></td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">10,069,512</td>
<td align="right"></td>
<td align="right">11,646,394</td>
<td align="right"></td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,806,347</td>
<td align="right"></td>
<td align="right">19,148,057</td>
<td align="right"></td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,657,569</td>
<td align="right">50.1%</td>
<td align="right">17,702,719</td>
<td align="right">48.9%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">15,778,938</td>
<td align="right">50.5%</td>
<td align="right">17,825,824</td>
<td align="right">49.2%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">57,248,147</td>
<td align="right">14.2%</td>
<td align="right">50,025,977</td>
<td align="right">9.8%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,825</td>
<td align="right">0.2%</td>
<td align="right">79,551</td>
<td align="right">0.2%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">148,044,617</td>
<td align="right">36.7%</td>
<td align="right">151,021,799</td>
<td align="right">29.7%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,544</td>
<td align="right">0.1%</td>
<td align="right">43,554</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">26</td>
<td align="right">0.2%</td>
<td align="right">1,200.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">372</td>
<td align="right">9.8%</td>
<td align="right">3,031</td>
<td align="right">25.2%</td>
<td align="right">714.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,805</td>
<td align="right"></td>
<td align="right">12,037</td>
<td align="right"></td>
<td align="right">216.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">3,224</td>
<td align="right">84.7%</td>
<td align="right">9,824</td>
<td align="right">81.6%</td>
<td align="right">204.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">3,201</td>
<td align="right">84.1%</td>
<td align="right">9,005</td>
<td align="right">74.8%</td>
<td align="right">181.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">376,571,373</td>
<td align="right">1,758.1%</td>
<td align="right">780,744,108</td>
<td align="right">1,886.1%</td>
<td align="right">107.3%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">232</td>
<td align="right">6.1%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">21,418,729</td>
<td align="right"></td>
<td align="right">41,393,969</td>
<td align="right"></td>
<td align="right">93.3%</td>
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
<td align="right">25</td>
<td align="right">0.2%</td>
<td align="right">25 / 0 !!</td>
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
<td align="right">368</td>
<td align="right">98.9%</td>
<td align="right">3,021</td>
<td align="right">99.7%</td>
<td align="right">720.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">372</td>
<td align="right"></td>
<td align="right">3,031</td>
<td align="right"></td>
<td align="right">714.8%</td>
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
<td align="right">1.1%</td>
<td align="right">10</td>
<td align="right">0.3%</td>
<td align="right">150.0%</td>
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
<td align="right">0.1%</td>
<td align="right">3 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">103</td>
<td align="right">27.7%</td>
<td align="right">171</td>
<td align="right">5.6%</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">29</td>
<td align="right">7.8%</td>
<td align="right">537</td>
<td align="right">17.7%</td>
<td align="right">1,751.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">69</td>
<td align="right">18.5%</td>
<td align="right">1,304</td>
<td align="right">43.0%</td>
<td align="right">1,789.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">115</td>
<td align="right">30.9%</td>
<td align="right">624</td>
<td align="right">20.6%</td>
<td align="right">442.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">26</td>
<td align="right">7.0%</td>
<td align="right">249</td>
<td align="right">8.2%</td>
<td align="right">857.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">29</td>
<td align="right">7.8%</td>
<td align="right">132</td>
<td align="right">4.4%</td>
<td align="right">355.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1</td>
<td align="right">0.3%</td>
<td align="right">11</td>
<td align="right">0.4%</td>
<td align="right">1,000.0%</td>
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
<td align="right">51</td>
<td align="right">13.7%</td>
<td align="right">71</td>
<td align="right">2.3%</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">73</td>
<td align="right">19.6%</td>
<td align="right">446</td>
<td align="right">14.7%</td>
<td align="right">511.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">31</td>
<td align="right">8.3%</td>
<td align="right">1,021</td>
<td align="right">33.7%</td>
<td align="right">3,193.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">96</td>
<td align="right">25.8%</td>
<td align="right">941</td>
<td align="right">31.0%</td>
<td align="right">880.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">79</td>
<td align="right">21.2%</td>
<td align="right">233</td>
<td align="right">7.7%</td>
<td align="right">194.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">35</td>
<td align="right">9.4%</td>
<td align="right">261</td>
<td align="right">8.6%</td>
<td align="right">645.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3</td>
<td align="right">0.8%</td>
<td align="right">48</td>
<td align="right">1.6%</td>
<td align="right">1,500.0%</td>
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
<td align="right">103,908</td>
<td align="right">5,195,300.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">2</td>
<td align="right">29,117</td>
<td align="right">1,455,750.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2</td>
<td align="right">29,117</td>
<td align="right">1,455,750.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">6</td>
<td align="right">84,024</td>
<td align="right">1,400,300.0%</td>
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
<td align="right">187,592</td>
<td align="right">317,852.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">21</td>
<td align="right">62,022</td>
<td align="right">295,242.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">4</td>
<td align="right">8,640</td>
<td align="right">215,900.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">4,151</td>
<td align="right">371,133</td>
<td align="right">8,840.8%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">4,151</td>
<td align="right">371,133</td>
<td align="right">8,840.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">4,151</td>
<td align="right">199,868</td>
<td align="right">4,714.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">4,151</td>
<td align="right">199,868</td>
<td align="right">4,714.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">189</td>
<td align="right">8,486</td>
<td align="right">4,389.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">16,751</td>
<td align="right">244,762</td>
<td align="right">1,361.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">6,385</td>
<td align="right">60,803</td>
<td align="right">852.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,385</td>
<td align="right">56,281</td>
<td align="right">781.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,385</td>
<td align="right">56,281</td>
<td align="right">781.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">8,302</td>
<td align="right">67,195</td>
<td align="right">709.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">561,618</td>
<td align="right">4,364,902</td>
<td align="right">677.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">561,618</td>
<td align="right">4,364,902</td>
<td align="right">677.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">4,184,834</td>
<td align="right">25,907,815</td>
<td align="right">519.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,077</td>
<td align="right">24,887</td>
<td align="right">510.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">128,955</td>
<td align="right">712,670</td>
<td align="right">452.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">386,867</td>
<td align="right">2,014,372</td>
<td align="right">420.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">386,867</td>
<td align="right">1,977,012</td>
<td align="right">411.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">386,865</td>
<td align="right">1,949,080</td>
<td align="right">403.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">166,140</td>
<td align="right">780,539</td>
<td align="right">369.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,451,966</td>
<td align="right">6,676,899</td>
<td align="right">359.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">823,550</td>
<td align="right">3,314,968</td>
<td align="right">302.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,297,861</td>
<td align="right">5,097,267</td>
<td align="right">292.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">4</td>
<td align="right">14</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">14,341</td>
<td align="right">49,797</td>
<td align="right">247.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,644,537</td>
<td align="right">5,650,928</td>
<td align="right">243.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">11,034,555</td>
<td align="right">37,500,977</td>
<td align="right">239.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,393,468</td>
<td align="right">7,878,038</td>
<td align="right">229.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,289,711</td>
<td align="right">4,197,340</td>
<td align="right">225.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">386,871</td>
<td align="right">1,245,475</td>
<td align="right">221.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">386,865</td>
<td align="right">1,241,249</td>
<td align="right">220.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">16,809</td>
<td align="right">53,658</td>
<td align="right">219.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,166,058</td>
<td align="right">12,498,570</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">597,563</td>
<td align="right">1,733,075</td>
<td align="right">190.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">276,788</td>
<td align="right">799,249</td>
<td align="right">188.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,999,004</td>
<td align="right">11,409,950</td>
<td align="right">185.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,131,991</td>
<td align="right">3,218,611</td>
<td align="right">184.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,356,064</td>
<td align="right">3,850,426</td>
<td align="right">183.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,703,797</td>
<td align="right">7,636,419</td>
<td align="right">182.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,072,174</td>
<td align="right">5,832,424</td>
<td align="right">181.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">4,596,567</td>
<td align="right">12,934,870</td>
<td align="right">181.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">4,999,875</td>
<td align="right">14,050,703</td>
<td align="right">181.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">516,092</td>
<td align="right">1,440,919</td>
<td align="right">179.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">387,026</td>
<td align="right">1,078,335</td>
<td align="right">178.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,723,389</td>
<td align="right">7,519,471</td>
<td align="right">176.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,723,389</td>
<td align="right">7,519,471</td>
<td align="right">176.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,830,153</td>
<td align="right">4,861,550</td>
<td align="right">165.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,119,265</td>
<td align="right">5,311,133</td>
<td align="right">150.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">9,478,644</td>
<td align="right">23,726,715</td>
<td align="right">150.3%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">644,936</td>
<td align="right">1,606,909</td>
<td align="right">149.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,051,708</td>
<td align="right">2,546,752</td>
<td align="right">142.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">44,035</td>
<td align="right">106,079</td>
<td align="right">140.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">3,331,886</td>
<td align="right">8,016,775</td>
<td align="right">140.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">3,331,886</td>
<td align="right">8,016,775</td>
<td align="right">140.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">7,112,032</td>
<td align="right">16,969,923</td>
<td align="right">138.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,422,883</td>
<td align="right">3,385,472</td>
<td align="right">137.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,944,860</td>
<td align="right">6,938,440</td>
<td align="right">135.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,275,626</td>
<td align="right">7,705,486</td>
<td align="right">135.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">946,095</td>
<td align="right">2,211,493</td>
<td align="right">133.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,391</td>
<td align="right">14,900</td>
<td align="right">133.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,391</td>
<td align="right">14,900</td>
<td align="right">133.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">411,730</td>
<td align="right">953,434</td>
<td align="right">131.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,332,052</td>
<td align="right">16,974,954</td>
<td align="right">131.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">695,769</td>
<td align="right">1,599,620</td>
<td align="right">129.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">411,776</td>
<td align="right">944,743</td>
<td align="right">129.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">143,487</td>
<td align="right">322,429</td>
<td align="right">124.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,798,374</td>
<td align="right">6,280,706</td>
<td align="right">124.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,935,966</td>
<td align="right">4,290,813</td>
<td align="right">121.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">15,941,641</td>
<td align="right">35,021,835</td>
<td align="right">119.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">11,921</td>
<td align="right">25,109</td>
<td align="right">110.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">545,259</td>
<td align="right">1,098,455</td>
<td align="right">101.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,387,275</td>
<td align="right">2,732,529</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">8,564</td>
<td align="right">16,866</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">8,564</td>
<td align="right">16,866</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,610,067</td>
<td align="right">3,162,421</td>
<td align="right">96.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">829,765</td>
<td align="right">1,625,805</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">31,856,593</td>
<td align="right">62,155,851</td>
<td align="right">95.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">9,645,115</td>
<td align="right">18,725,062</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">21,418,729</td>
<td align="right">41,393,969</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">22,787,764</td>
<td align="right">43,675,050</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">22,041,057</td>
<td align="right">41,885,491</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,489,037</td>
<td align="right">2,806,190</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">7,571,996</td>
<td align="right">14,119,082</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">7,555,245</td>
<td align="right">13,874,320</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">9,320,593</td>
<td align="right">16,980,689</td>
<td align="right">82.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,383,334</td>
<td align="right">4,331,864</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,001,561</td>
<td align="right">3,559,470</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">399,157</td>
<td align="right">707,810</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,057,066</td>
<td align="right">1,805,506</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,516,765</td>
<td align="right">14,428,333</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,236,795</td>
<td align="right">2,089,730</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">544,740</td>
<td align="right">918,326</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,343,078</td>
<td align="right">2,241,164</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,100,649</td>
<td align="right">1,829,900</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">129,039</td>
<td align="right">210,689</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,995,424</td>
<td align="right">3,233,711</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,657,677</td>
<td align="right">4,306,514</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">128,979</td>
<td align="right">191,610</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,728,433</td>
<td align="right">2,567,064</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">60,911</td>
<td align="right">89,947</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">60,907</td>
<td align="right">86,463</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">191</td>
<td align="right">270</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">19,128,596</td>
<td align="right">26,482,347</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">8,884,896</td>
<td align="right">12,113,669</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">282,587</td>
<td align="right">382,907</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">132,989</td>
<td align="right">178,867</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">428,178</td>
<td align="right">570,232</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">428,178</td>
<td align="right">570,232</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">270,208</td>
<td align="right">357,892</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">523,824</td>
<td align="right">370,514</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">874,243</td>
<td align="right">1,109,041</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">418,384</td>
<td align="right">528,535</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,416,855</td>
<td align="right">6,780,540</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">696,941</td>
<td align="right">869,500</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">696,935</td>
<td align="right">869,127</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,074,442</td>
<td align="right">4,641,380</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,425,482</td>
<td align="right">1,757,100</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,646,726</td>
<td align="right">8,188,822</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,646,726</td>
<td align="right">8,188,822</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">4,879,962</td>
<td align="right">5,967,603</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">622,328</td>
<td align="right">491,522</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">557,247</td>
<td align="right">649,156</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,460,279</td>
<td align="right">6,314,288</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">557,188</td>
<td align="right">636,632</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">61,094</td>
<td align="right">69,692</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">60,907</td>
<td align="right">69,462</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">60,907</td>
<td align="right">69,462</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,006,674</td>
<td align="right">3,422,098</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">547,200</td>
<td align="right">617,771</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">411,718</td>
<td align="right">461,994</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">584,896</td>
<td align="right">647,401</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">59</td>
<td align="right">55</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,670,469</td>
<td align="right">2,830,355</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">819,293</td>
<td align="right">827,596</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">918,323</td>
<td align="right">926,878</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">411,891</td>
<td align="right">410,341</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">411,726</td>
<td align="right">411,755</td>
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
<td align="right">16,413</td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">1,224,274</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">1,224,274</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right"></td>
<td align="right">208,156</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right"></td>
<td align="right">208,156</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right"></td>
<td align="right">103,935</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">46,260</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">42,003</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">38,014</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">38,001</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">37,677</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">29,435</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">29,231</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">29,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">29,116</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">23,695</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">20,850</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right"></td>
<td align="right">20,603</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right"></td>
<td align="right">16,984</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">16,762</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">12,469</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right"></td>
<td align="right">12,447</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">12,432</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">12,432</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">8,492</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">8,492</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">8,316</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">8,225</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">4,188</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right"></td>
<td align="right">132</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">34</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right"></td>
<td align="right">21</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">18</td>
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
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right"></td>
<td align="right">3</td>
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
<td align="right">1,011</td>
<td align="right">548.1%</td>
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
Stats gathered on: 2024-10-23
