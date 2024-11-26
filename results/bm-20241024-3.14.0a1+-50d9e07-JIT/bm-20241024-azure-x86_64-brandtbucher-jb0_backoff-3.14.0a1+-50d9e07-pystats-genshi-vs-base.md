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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,905</td>
<td align="right">194,648</td>
<td align="right">10,117.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,908</td>
<td align="right">197,937</td>
<td align="right">3,932.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,110</td>
<td align="right">205,227</td>
<td align="right">1,173.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">12,738</td>
<td align="right">47,956</td>
<td align="right">276.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,123,935</td>
<td align="right">710</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,319,725</td>
<td align="right">802</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,931,817</td>
<td align="right">1,451</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,136,133</td>
<td align="right">9,025</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,825,339</td>
<td align="right">25,916</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,331,465</td>
<td align="right">13,876</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">194,472</td>
<td align="right">387,473</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">194,549</td>
<td align="right">1,494</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">195,938</td>
<td align="right">2,886</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">201,192</td>
<td align="right">3,488</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">155</td>
<td align="right">4</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">201,410</td>
<td align="right">5,712</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,056,963</td>
<td align="right">196,745</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,869,205</td>
<td align="right">201,515</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,327,002</td>
<td align="right">200,749</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,443,436</td>
<td align="right">397,963</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,358,327</td>
<td align="right">212,411</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,264,300</td>
<td align="right">216,408</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,825,852</td>
<td align="right">595,928</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,529,151</td>
<td align="right">402,547</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">14,763</td>
<td align="right">3,722</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">5,272,142</td>
<td align="right">1,410,986</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">16,745</td>
<td align="right">5,588</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,392,847</td>
<td align="right">2,337,631</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">21,576,303</td>
<td align="right">8,523,621</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">324,650</td>
<td align="right">517,333</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">7,227</td>
<td align="right">3,151</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,391</td>
<td align="right">3,603</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">668</td>
<td align="right">353</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">42,078,502</td>
<td align="right">23,425,125</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">14,623,220</td>
<td align="right">8,832,598</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">13,449,122</td>
<td align="right">18,610,584</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,288</td>
<td align="right">809</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">7,288</td>
<td align="right">4,634</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">312,592</td>
<td align="right">198,869</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,914</td>
<td align="right">7,897</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">24</td>
<td align="right">16</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">978</td>
<td align="right">684</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,673</td>
<td align="right">1,186</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,822,695</td>
<td align="right">5,668,498</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,823,886</td>
<td align="right">6,506,487</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">16,617</td>
<td align="right">12,436</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">155,844,149</td>
<td align="right">117,444,169</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17,057,491</td>
<td align="right">12,997,549</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">58,703,575</td>
<td align="right">46,728,500</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">324</td>
<td align="right">258</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">66</td>
<td align="right">54</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,331</td>
<td align="right">1,937</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">11,226,721</td>
<td align="right">9,487,947</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">13,903,877</td>
<td align="right">11,785,568</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,001</td>
<td align="right">3,455</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,512</td>
<td align="right">3,924</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">58,217,024</td>
<td align="right">51,902,989</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">3,605,776</td>
<td align="right">3,216,567</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">9,675</td>
<td align="right">8,675</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">63,890,180</td>
<td align="right">57,710,655</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,201</td>
<td align="right">8,333</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,564,961</td>
<td align="right">2,371,641</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,553</td>
<td align="right">3,287</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">5,248</td>
<td align="right">4,887</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,613</td>
<td align="right">2,440</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,492</td>
<td align="right">2,352</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,307,679</td>
<td align="right">42,180,281</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">269</td>
<td align="right">259</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,339</td>
<td align="right">3,223</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">13,003</td>
<td align="right">12,552</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,002</td>
<td align="right">970</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,256</td>
<td align="right">1,218</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">655</td>
<td align="right">637</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">225</td>
<td align="right">219</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">2,707</td>
<td align="right">2,640</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">292</td>
<td align="right">286</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">12,986,569</td>
<td align="right">12,791,292</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">207,546</td>
<td align="right">204,742</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">10,366,099</td>
<td align="right">10,250,463</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,046</td>
<td align="right">4,009</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">709,818</td>
<td align="right">705,272</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,441</td>
<td align="right">3,462</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,327</td>
<td align="right">1,321</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">453</td>
<td align="right">451</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">459</td>
<td align="right">457</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,641</td>
<td align="right">1,635</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">843</td>
<td align="right">841</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,896</td>
<td align="right">1,892</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,106</td>
<td align="right">1,104</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">3,152,828</td>
<td align="right">3,147,269</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,315</td>
<td align="right">2,311</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">5,410,159</td>
<td align="right">5,408,352</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">10,862,071</td>
<td align="right">10,859,393</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,070,094</td>
<td align="right">6,069,032</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">704,341</td>
<td align="right">704,257</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">768,612</td>
<td align="right">768,555</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,383,859</td>
<td align="right">4,383,764</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">4,747,959</td>
<td align="right">4,747,862</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,378,422</td>
<td align="right">4,378,402</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">708,709</td>
<td align="right">708,706</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">20,710,347</td>
<td align="right">20,710,337</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">5,418,844</td>
<td align="right">5,418,842</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">40,426,059</td>
<td align="right">40,426,059</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">10,920,920</td>
<td align="right">10,920,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">10,855,117</td>
<td align="right">10,855,117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">196,219</td>
<td align="right">196,219</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">195,322</td>
<td align="right">195,322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">194,863</td>
<td align="right">194,863</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,271</td>
<td align="right">6,271</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,666</td>
<td align="right">3,666</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,467</td>
<td align="right">3,467</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3,370</td>
<td align="right">3,370</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3,370</td>
<td align="right">3,370</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3,370</td>
<td align="right">3,370</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,358</td>
<td align="right">3,358</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,057</td>
<td align="right">2,057</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,842</td>
<td align="right">1,842</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,592</td>
<td align="right">1,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,559</td>
<td align="right">1,559</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,500</td>
<td align="right">1,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,260</td>
<td align="right">1,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,234</td>
<td align="right">1,234</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,047</td>
<td align="right">1,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,013</td>
<td align="right">1,013</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">770</td>
<td align="right">770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">644</td>
<td align="right">644</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">632</td>
<td align="right">632</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">580</td>
<td align="right">580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">495</td>
<td align="right">495</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">258</td>
<td align="right">258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">258</td>
<td align="right">258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">256</td>
<td align="right">256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">236</td>
<td align="right">236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">193</td>
<td align="right">193</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">29</td>
<td align="right">29</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">22</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">18</td>
<td align="right">18</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">18</td>
<td align="right">18</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">2</td>
<td align="right"></td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,404</td>
<td align="right">39.3%</td>
<td align="right">7,558</td>
<td align="right">36.8%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,196</td>
<td align="right">57.0%</td>
<td align="right">12,196</td>
<td align="right">59.4%</td>
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
<td align="right">624</td>
<td align="right">78.3%</td>
<td align="right">602</td>
<td align="right">77.7%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">173</td>
<td align="right">21.7%</td>
<td align="right">173</td>
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
<td align="left">remainder</td>
<td align="right">363</td>
<td align="right">58.2%</td>
<td align="right">341</td>
<td align="right">56.6%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">131</td>
<td align="right">21.0%</td>
<td align="right">131</td>
<td align="right">21.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">129</td>
<td align="right">20.7%</td>
<td align="right">129</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
<td align="right">0.2%</td>
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
<td align="right">1,559</td>
<td align="right">100.0%</td>
<td align="right">1,559</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">200,439</td>
<td align="right">0.9%</td>
<td align="right">2,912</td>
<td align="right">0.0%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,031,013</td>
<td align="right">99.1%</td>
<td align="right">23,031,013</td>
<td align="right">100.0%</td>
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
<td align="right">34</td>
<td align="right">0.0%</td>
<td align="right">34</td>
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
<td align="right">563</td>
<td align="right">74.7%</td>
<td align="right">386</td>
<td align="right">66.9%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">191</td>
<td align="right">25.3%</td>
<td align="right">191</td>
<td align="right">33.1%</td>
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
<td align="right">146</td>
<td align="right">25.9%</td>
<td align="right">54</td>
<td align="right">14.0%</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">309</td>
<td align="right">54.9%</td>
<td align="right">224</td>
<td align="right">58.0%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">108</td>
<td align="right">19.2%</td>
<td align="right">108</td>
<td align="right">28.0%</td>
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
<td align="right">3,968</td>
<td align="right">0.0%</td>
<td align="right">3,948</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">43,312,349</td>
<td align="right">100.0%</td>
<td align="right">43,312,397</td>
<td align="right">100.0%</td>
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
<td align="right">1,736</td>
<td align="right">0.0%</td>
<td align="right">1,736</td>
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
<td align="right">4,786</td>
<td align="right">100.0%</td>
<td align="right">4,786</td>
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
<td align="left">init not inline values</td>
<td align="right">43</td>
<td align="right">43 / 0 !!</td>
<td align="right">43</td>
<td align="right">43 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">28</td>
<td align="right">11.9%</td>
<td align="right">28</td>
<td align="right">11.9%</td>
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
<td align="right">709,239</td>
<td align="right">47.4%</td>
<td align="right">704,778</td>
<td align="right">47.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">785,457</td>
<td align="right">52.5%</td>
<td align="right">785,457</td>
<td align="right">52.7%</td>
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
<td align="right">10</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">403</td>
<td align="right">69.6%</td>
<td align="right">318</td>
<td align="right">64.4%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">176</td>
<td align="right">30.4%</td>
<td align="right">176</td>
<td align="right">35.6%</td>
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
<td align="left">tuple</td>
<td align="right">93</td>
<td align="right">23.1%</td>
<td align="right">8</td>
<td align="right">2.5%</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">266</td>
<td align="right">66.0%</td>
<td align="right">266</td>
<td align="right">83.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">10.7%</td>
<td align="right">43</td>
<td align="right">13.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
<td align="right">0.3%</td>
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
<td align="right">3,101</td>
<td align="right">0.1%</td>
<td align="right">3,122</td>
<td align="right">0.1%</td>
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
<td align="right">3,923,987</td>
<td align="right">99.9%</td>
<td align="right">3,923,987</td>
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
<td align="right">8</td>
<td align="right">2.4%</td>
<td align="right">8</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">332</td>
<td align="right">97.6%</td>
<td align="right">332</td>
<td align="right">97.6%</td>
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
<td align="right">200</td>
<td align="right">60.2%</td>
<td align="right">200</td>
<td align="right">60.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">89</td>
<td align="right">26.8%</td>
<td align="right">89</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">13.0%</td>
<td align="right">43</td>
<td align="right">13.0%</td>
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
<td align="right">2,325,962</td>
<td align="right">6.7%</td>
<td align="right">200,251</td>
<td align="right">0.6%</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,205</td>
<td align="right">0.0%</td>
<td align="right">3,432</td>
<td align="right">0.0%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,344,652</td>
<td align="right">93.3%</td>
<td align="right">32,342,355</td>
<td align="right">99.4%</td>
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
<td align="left">Failure</td>
<td align="right">988</td>
<td align="right">91.1%</td>
<td align="right">466</td>
<td align="right">86.0%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">97</td>
<td align="right">8.9%</td>
<td align="right">76</td>
<td align="right">14.0%</td>
<td align="right">-21.6%</td>
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
<td align="left">dict values</td>
<td align="right">12</td>
<td align="right">1.2%</td>
<td align="right">84</td>
<td align="right">18.0%</td>
<td align="right">600.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">597</td>
<td align="right">60.4%</td>
<td align="right">8</td>
<td align="right">1.7%</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">74</td>
<td align="right">7.5%</td>
<td align="right">31</td>
<td align="right">6.7%</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">94</td>
<td align="right">9.5%</td>
<td align="right">132</td>
<td align="right">28.3%</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">90</td>
<td align="right">9.1%</td>
<td align="right">90</td>
<td align="right">19.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">76</td>
<td align="right">7.7%</td>
<td align="right">76</td>
<td align="right">16.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">23</td>
<td align="right">2.3%</td>
<td align="right">23</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">22</td>
<td align="right">2.2%</td>
<td align="right">22</td>
<td align="right">4.7%</td>
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
<td align="right">5,818,951</td>
<td align="right">20.0%</td>
<td align="right">21,062</td>
<td align="right">0.1%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,148</td>
<td align="right">0.0%</td>
<td align="right">4,127</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,193,361</td>
<td align="right">79.9%</td>
<td align="right">23,192,320</td>
<td align="right">99.9%</td>
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
<td align="left">Failure</td>
<td align="right">2,782</td>
<td align="right">43.3%</td>
<td align="right">1,291</td>
<td align="right">26.4%</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,648</td>
<td align="right">56.7%</td>
<td align="right">3,605</td>
<td align="right">73.6%</td>
<td align="right">-1.2%</td>
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
<td align="left">class method obj</td>
<td align="right">1,642</td>
<td align="right">59.0%</td>
<td align="right">196</td>
<td align="right">15.2%</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">137</td>
<td align="right">4.9%</td>
<td align="right">95</td>
<td align="right">7.4%</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">100</td>
<td align="right">3.6%</td>
<td align="right">99</td>
<td align="right">7.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">768</td>
<td align="right">27.6%</td>
<td align="right">766</td>
<td align="right">59.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">48</td>
<td align="right">1.7%</td>
<td align="right">48</td>
<td align="right">3.7%</td>
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
<td align="right">71,711,017</td>
<td align="right">100.0%</td>
<td align="right">63,377,295</td>
<td align="right">100.0%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">500</td>
<td align="right">0.0%</td>
<td align="right">500</td>
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
<td align="right">1,858</td>
<td align="right">0.0%</td>
<td align="right">1,858</td>
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
<td align="right">3,166</td>
<td align="right">100.0%</td>
<td align="right">3,166</td>
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
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">2</td>
<td align="right">0.8%</td>
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
<td align="right">260</td>
<td align="right">98.5%</td>
<td align="right">260</td>
<td align="right">98.5%</td>
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
<td align="right">2</td>
<td align="right">100.0%</td>
<td align="right">2</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,552</td>
<td align="right">6.3%</td>
<td align="right">1,552</td>
<td align="right">6.3%</td>
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
<td align="right">21,310</td>
<td align="right">86.0%</td>
<td align="right">21,310</td>
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
<td align="right">1,492</td>
<td align="right">77.9%</td>
<td align="right">1,492</td>
<td align="right">77.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">423</td>
<td align="right">22.1%</td>
<td align="right">423</td>
<td align="right">22.1%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">315</td>
<td align="right">74.5%</td>
<td align="right">315</td>
<td align="right">74.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">86</td>
<td align="right">20.3%</td>
<td align="right">86</td>
<td align="right">20.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">22</td>
<td align="right">5.2%</td>
<td align="right">22</td>
<td align="right">5.2%</td>
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
<td align="right">258</td>
<td align="right">100.0%</td>
<td align="right">258</td>
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
<td align="right">34</td>
<td align="right">0.0%</td>
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,125,952</td>
<td align="right">100.0%</td>
<td align="right">2,125,952</td>
<td align="right">100.0%</td>
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
<td align="right">32</td>
<td align="right">100.0%</td>
<td align="right">32</td>
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
<td align="right">5,269,773</td>
<td align="right">21.0%</td>
<td align="right">1,409,581</td>
<td align="right">6.6%</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">321</td>
<td align="right">0.0%</td>
<td align="right">317</td>
<td align="right">0.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">19,798,594</td>
<td align="right">79.0%</td>
<td align="right">19,798,576</td>
<td align="right">93.3%</td>
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
<td align="left">Failure</td>
<td align="right">1,536</td>
<td align="right">64.8%</td>
<td align="right">572</td>
<td align="right">40.7%</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">834</td>
<td align="right">35.2%</td>
<td align="right">834</td>
<td align="right">59.3%</td>
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
<td align="left">dict</td>
<td align="right">1,022</td>
<td align="right">66.5%</td>
<td align="right">58</td>
<td align="right">10.1%</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">387</td>
<td align="right">25.2%</td>
<td align="right">387</td>
<td align="right">67.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">85</td>
<td align="right">5.5%</td>
<td align="right">85</td>
<td align="right">14.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">42</td>
<td align="right">2.7%</td>
<td align="right">42</td>
<td align="right">7.3%</td>
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
<td align="right">438</td>
<td align="right">0.0%</td>
<td align="right">144</td>
<td align="right">0.0%</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,747,883</td>
<td align="right">100.0%</td>
<td align="right">13,747,883</td>
<td align="right">100.0%</td>
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
<td align="right">46</td>
<td align="right">20.0%</td>
<td align="right">25</td>
<td align="right">12.0%</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">184</td>
<td align="right">80.0%</td>
<td align="right">184</td>
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
<td align="left">iterator</td>
<td align="right">46</td>
<td align="right">100.0%</td>
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">-45.7%</td>
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
<td align="right">14,364,330</td>
<td align="right">1.9%</td>
<td align="right">2,374,074</td>
<td align="right">0.4%</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">196,356,235</td>
<td align="right">26.2%</td>
<td align="right">149,839,353</td>
<td align="right">25.4%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">538,218,474</td>
<td align="right">71.9%</td>
<td align="right">437,365,855</td>
<td align="right">74.2%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">14,903</td>
<td align="right">0.0%</td>
<td align="right">14,264</td>
<td align="right">0.0%</td>
<td align="right">-4.3%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">5,818,951</td>
<td align="right">40.6%</td>
<td align="right">21,062</td>
<td align="right">0.9%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">200,439</td>
<td align="right">1.4%</td>
<td align="right">2,912</td>
<td align="right">0.1%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,325,962</td>
<td align="right">16.2%</td>
<td align="right">200,251</td>
<td align="right">8.5%</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">5,269,773</td>
<td align="right">36.7%</td>
<td align="right">1,409,581</td>
<td align="right">59.9%</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,404</td>
<td align="right">0.1%</td>
<td align="right">7,558</td>
<td align="right">0.3%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,101</td>
<td align="right">0.0%</td>
<td align="right">3,122</td>
<td align="right">0.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">709,239</td>
<td align="right">4.9%</td>
<td align="right">704,778</td>
<td align="right">29.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,736</td>
<td align="right">0.0%</td>
<td align="right">1,736</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,559</td>
<td align="right">0.0%</td>
<td align="right">1,559</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,552</td>
<td align="right">0.0%</td>
<td align="right">1,552</td>
<td align="right">0.1%</td>
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
<td align="left">RESUME</td>
<td align="right">359</td>
<td align="right">2.4%</td>
<td align="right">548</td>
<td align="right">3.7%</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">359</td>
<td align="right">2.4%</td>
<td align="right">548</td>
<td align="right">3.7%</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,821</td>
<td align="right">25.0%</td>
<td align="right">3,048</td>
<td align="right">20.6%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">183</td>
<td align="right">1.2%</td>
<td align="right">179</td>
<td align="right">1.2%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,577</td>
<td align="right">10.3%</td>
<td align="right">1,549</td>
<td align="right">10.5%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,886</td>
<td align="right">25.5%</td>
<td align="right">3,865</td>
<td align="right">26.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,379</td>
<td align="right">15.6%</td>
<td align="right">2,387</td>
<td align="right">16.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">962</td>
<td align="right">6.3%</td>
<td align="right">962</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">896</td>
<td align="right">5.9%</td>
<td align="right">896</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">384</td>
<td align="right">2.5%</td>
<td align="right">384</td>
<td align="right">2.6%</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">10,921,076</td>
<td align="right">18.1%</td>
<td align="right">10,921,076</td>
<td align="right">18.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">49,279,860</td>
<td align="right">81.9%</td>
<td align="right">49,279,860</td>
<td align="right">81.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">10,921,076</td>
<td align="right">18.1%</td>
<td align="right">10,921,076</td>
<td align="right">18.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">2,435,738</td>
<td align="right">4.0%</td>
<td align="right">2,435,738</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">8,485,338</td>
<td align="right">14.1%</td>
<td align="right">8,485,338</td>
<td align="right">14.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,123,195</td>
<td align="right">3.5%</td>
<td align="right">2,123,195</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">312,525</td>
<td align="right">0.5%</td>
<td align="right">312,525</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">18</td>
<td align="right">0.0%</td>
<td align="right">18</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">417</td>
<td align="right">0.0%</td>
<td align="right">417</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">972</td>
<td align="right">0.0%</td>
<td align="right">972</td>
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
<tr>
<td align="left">Frame objects created</td>
<td align="right">7,165</td>
<td align="right">0.0%</td>
<td align="right">7,165</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">19,579,732</td>
<td align="right">32.5%</td>
<td align="right">19,579,732</td>
<td align="right">32.5%</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">3,542</td>
<td align="right">0.0%</td>
<td align="right">4,904</td>
<td align="right">0.0%</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">86,141,998</td>
<td align="right">11.2%</td>
<td align="right">55,418,812</td>
<td align="right">7.3%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">267,693,556</td>
<td align="right">34.9%</td>
<td align="right">345,225,871</td>
<td align="right">45.2%</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">81,588,387</td>
<td align="right">9.6%</td>
<td align="right">63,592,288</td>
<td align="right">7.3%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">272,701,462</td>
<td align="right">32.2%</td>
<td align="right">331,918,611</td>
<td align="right">38.3%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">109,612,553</td>
<td align="right">12.9%</td>
<td align="right">132,774,416</td>
<td align="right">15.3%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">345,047,655</td>
<td align="right">44.9%</td>
<td align="right">281,037,420</td>
<td align="right">36.8%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">68,748,448</td>
<td align="right">9.0%</td>
<td align="right">81,387,724</td>
<td align="right">10.7%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">383,483,138</td>
<td align="right">45.3%</td>
<td align="right">337,792,029</td>
<td align="right">39.0%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">6,759</td>
<td align="right"></td>
<td align="right">6,478</td>
<td align="right"></td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">7,468</td>
<td align="right"></td>
<td align="right">7,187</td>
<td align="right"></td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">585</td>
<td align="right"></td>
<td align="right">575</td>
<td align="right"></td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">2,519</td>
<td align="right">0.0%</td>
<td align="right">2,517</td>
<td align="right">0.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">13,030,721</td>
<td align="right"></td>
<td align="right">13,028,023</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">30,161,957</td>
<td align="right"></td>
<td align="right">30,165,865</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">27,167,424</td>
<td align="right">50.6%</td>
<td align="right">27,168,852</td>
<td align="right">50.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,434,775</td>
<td align="right"></td>
<td align="right">4,434,763</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">26,559,984</td>
<td align="right"></td>
<td align="right">26,560,051</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">26,561,987</td>
<td align="right">49.4%</td>
<td align="right">26,562,054</td>
<td align="right">49.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">27,161,363</td>
<td align="right">50.6%</td>
<td align="right">27,161,431</td>
<td align="right">50.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">2,058</td>
<td align="right"></td>
<td align="right">2,058</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
<td align="right">408</td>
<td align="right">3,882</td>
<td align="right">7,548,802</td>
<td align="right">408</td>
<td align="right">3,882</td>
<td align="right">7,544,064</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">238</td>
<td align="right">3.0%</td>
<td align="right">23,700.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">42</td>
<td align="right">0.8%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,596</td>
<td align="right">31.1%</td>
<td align="right">3,024</td>
<td align="right">37.6%</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">2,832</td>
<td align="right">55.2%</td>
<td align="right">4,837</td>
<td align="right">60.1%</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">5,130</td>
<td align="right"></td>
<td align="right">8,045</td>
<td align="right"></td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">3,492</td>
<td align="right">68.1%</td>
<td align="right">5,021</td>
<td align="right">62.4%</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">836,699,291</td>
<td align="right">1,023.6%</td>
<td align="right">1,161,279,835</td>
<td align="right">1,288.9%</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">67</td>
<td align="right">1.3%</td>
<td align="right">44</td>
<td align="right">0.5%</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">81,744,729</td>
<td align="right"></td>
<td align="right">90,096,722</td>
<td align="right"></td>
<td align="right">10.2%</td>
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
<td align="right">1,554</td>
<td align="right">97.4%</td>
<td align="right">2,982</td>
<td align="right">98.6%</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,596</td>
<td align="right"></td>
<td align="right">3,024</td>
<td align="right"></td>
<td align="right">89.5%</td>
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
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">22</td>
<td align="right">1.4%</td>
<td align="right">20</td>
<td align="right">0.7%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">272</td>
<td align="right">17.0%</td>
<td align="right">274</td>
<td align="right">9.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">28</td>
<td align="right">1.8%</td>
<td align="right">527</td>
<td align="right">17.4%</td>
<td align="right">1,782.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">943</td>
<td align="right">59.1%</td>
<td align="right">1,272</td>
<td align="right">42.1%</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">158</td>
<td align="right">9.9%</td>
<td align="right">502</td>
<td align="right">16.6%</td>
<td align="right">217.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">129</td>
<td align="right">8.1%</td>
<td align="right">427</td>
<td align="right">14.1%</td>
<td align="right">231.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">44</td>
<td align="right">2.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">4</td>
<td align="right">0.3%</td>
<td align="right">5</td>
<td align="right">0.2%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">221</td>
<td align="right">13.8%</td>
<td align="right">222</td>
<td align="right">7.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">73</td>
<td align="right">4.6%</td>
<td align="right">268</td>
<td align="right">8.9%</td>
<td align="right">267.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">943</td>
<td align="right">59.1%</td>
<td align="right">1,534</td>
<td align="right">50.7%</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">157</td>
<td align="right">9.8%</td>
<td align="right">351</td>
<td align="right">11.6%</td>
<td align="right">123.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">27</td>
<td align="right">1.7%</td>
<td align="right">518</td>
<td align="right">17.1%</td>
<td align="right">1,818.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">129</td>
<td align="right">8.1%</td>
<td align="right">84</td>
<td align="right">2.8%</td>
<td align="right">-34.9%</td>
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
<td align="left">_DICT_MERGE</td>
<td align="right">1</td>
<td align="right">193,056</td>
<td align="right">19,305,500.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">85</td>
<td align="right">2,317,674</td>
<td align="right">2,726,575.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">85</td>
<td align="right">2,317,674</td>
<td align="right">2,726,575.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">85</td>
<td align="right">2,317,674</td>
<td align="right">2,726,575.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">14</td>
<td align="right">197,541</td>
<td align="right">1,410,907.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">402</td>
<td align="right">2,339,290</td>
<td align="right">581,812.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">374</td>
<td align="right">2,127,482</td>
<td align="right">568,745.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">39</td>
<td align="right">113,762</td>
<td align="right">291,597.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">168</td>
<td align="right">193,220</td>
<td align="right">114,911.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">6</td>
<td align="right">4,082</td>
<td align="right">67,933.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">17</td>
<td align="right">4,034</td>
<td align="right">23,629.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">78</td>
<td align="right">4,282</td>
<td align="right">5,389.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">26</td>
<td align="right">1,026</td>
<td align="right">3,846.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">2</td>
<td align="right">64</td>
<td align="right">3,100.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">34</td>
<td align="right">880</td>
<td align="right">2,488.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">181</td>
<td align="right">4,362</td>
<td align="right">2,309.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">181</td>
<td align="right">4,362</td>
<td align="right">2,309.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">193,097</td>
<td align="right">4,238,598</td>
<td align="right">2,095.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">193,097</td>
<td align="right">4,238,598</td>
<td align="right">2,095.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">134,046</td>
<td align="right">2,453,295</td>
<td align="right">1,730.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">582,431</td>
<td align="right">9,272,911</td>
<td align="right">1,492.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">195,941</td>
<td align="right">2,514,864</td>
<td align="right">1,183.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">21</td>
<td align="right">232</td>
<td align="right">1,004.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">579,157</td>
<td align="right">6,377,046</td>
<td align="right">1,001.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">386,151</td>
<td align="right">4,247,964</td>
<td align="right">1,000.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">193,058</td>
<td align="right">2,123,215</td>
<td align="right">999.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">193,089</td>
<td align="right">2,123,461</td>
<td align="right">999.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">193,743</td>
<td align="right">2,125,411</td>
<td align="right">997.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">44</td>
<td align="right">441</td>
<td align="right">902.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">42</td>
<td align="right">403</td>
<td align="right">859.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">579,112</td>
<td align="right">4,439,330</td>
<td align="right">666.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">2</td>
<td align="right">14</td>
<td align="right">600.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">85</td>
<td align="right">556</td>
<td align="right">554.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">9</td>
<td align="right">47</td>
<td align="right">422.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">13</td>
<td align="right">65</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">21</td>
<td align="right">88</td>
<td align="right">319.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,122,906</td>
<td align="right">8,679,003</td>
<td align="right">308.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">579,138</td>
<td align="right">2,316,671</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,702,095</td>
<td align="right">10,802,784</td>
<td align="right">299.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">138</td>
<td align="right">540</td>
<td align="right">291.3%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">11</td>
<td align="right">43</td>
<td align="right">290.9%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">11</td>
<td align="right">43</td>
<td align="right">290.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">4</td>
<td align="right">14</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,729,934</td>
<td align="right">5,590,150</td>
<td align="right">223.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">203</td>
<td align="right">654</td>
<td align="right">222.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">55</td>
<td align="right">171</td>
<td align="right">210.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">883</td>
<td align="right">2,690</td>
<td align="right">204.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">6,489,981</td>
<td align="right">19,543,070</td>
<td align="right">201.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">1</td>
<td align="right">3</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,639,196</td>
<td align="right">27,914,077</td>
<td align="right">189.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,390,556</td>
<td align="right">21,318,936</td>
<td align="right">188.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,325,106</td>
<td align="right">6,577,427</td>
<td align="right">182.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">72</td>
<td align="right">202</td>
<td align="right">180.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,281,340</td>
<td align="right">3,329,232</td>
<td align="right">159.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,720,509</td>
<td align="right">14,342,279</td>
<td align="right">150.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">10,475,941</td>
<td align="right">25,479,292</td>
<td align="right">143.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">5,528,840</td>
<td align="right">13,436,500</td>
<td align="right">143.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">6,296,956</td>
<td align="right">14,204,622</td>
<td align="right">125.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">4,631,771</td>
<td align="right">10,229,710</td>
<td align="right">120.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">61</td>
<td align="right">133</td>
<td align="right">118.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,765,856</td>
<td align="right">12,331,512</td>
<td align="right">113.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">7,851,800</td>
<td align="right">15,966,207</td>
<td align="right">103.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">193,044</td>
<td align="right">41</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">193,041</td>
<td align="right">298</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">193,615</td>
<td align="right">630</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">389,569</td>
<td align="right">6,130</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">193,842</td>
<td align="right">4,423</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">196,992</td>
<td align="right">6,602</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">7,784,677</td>
<td align="right">14,161,572</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">35,549,392</td>
<td align="right">59,493,848</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">12</td>
<td align="right">20</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,213,455</td>
<td align="right">5,340,059</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">9,951,869</td>
<td align="right">16,527,087</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">10,525,868</td>
<td align="right">17,031,722</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">321,223</td>
<td align="right">129,367</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,787,153</td>
<td align="right">5,905,462</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">4,179,933</td>
<td align="right">6,320,172</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">4,246,084</td>
<td align="right">6,392,000</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">66,400,197</td>
<td align="right">99,153,249</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,885,208</td>
<td align="right">7,011,925</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">901,924</td>
<td align="right">1,291,133</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">561</td>
<td align="right">764</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">28</td>
<td align="right">38</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">28</td>
<td align="right">38</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">6,147,005</td>
<td align="right">8,272,574</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">68</td>
<td align="right">47</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">7,182,233</td>
<td align="right">9,309,631</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">705,038</td>
<td align="right">900,315</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">34,055,836</td>
<td align="right">41,963,564</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">53,985,279</td>
<td align="right">62,334,659</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">32,838,376</td>
<td align="right">36,904,220</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,025,257</td>
<td align="right">1,140,876</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">1,747</td>
<td align="right">1,943</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">81,744,729</td>
<td align="right">90,096,722</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">81,877,586</td>
<td align="right">90,228,719</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">2,122,816</td>
<td align="right">1,929,785</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,123,478</td>
<td align="right">1,930,458</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">4,949,700</td>
<td align="right">4,563,626</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,826,745</td>
<td align="right">2,633,716</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">2,890,900</td>
<td align="right">2,697,899</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">3,212,793</td>
<td align="right">3,026,433</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">3,531,242</td>
<td align="right">3,724,562</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">4,245,682</td>
<td align="right">4,052,710</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">42,484,122</td>
<td align="right">44,224,106</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">50,403,745</td>
<td align="right">52,461,083</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">174</td>
<td align="right">180</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">768,132</td>
<td align="right">779,289</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">768,179</td>
<td align="right">779,304</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">768,138</td>
<td align="right">779,179</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">17,068,630</td>
<td align="right">16,875,771</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">24,300,609</td>
<td align="right">24,107,656</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">132,857</td>
<td align="right">131,997</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">707,120</td>
<td align="right">709,774</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,250,965</td>
<td align="right">2,256,524</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,250,965</td>
<td align="right">2,256,524</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">384,183</td>
<td align="right">384,729</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">2,890,908</td>
<td align="right">2,894,696</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">706,940</td>
<td align="right">707,206</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">706,940</td>
<td align="right">707,206</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">2,122,816</td>
<td align="right">2,123,303</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">2,122,816</td>
<td align="right">2,123,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">768,135</td>
<td align="right">768,308</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">8,430,165</td>
<td align="right">8,431,962</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">6,305,995</td>
<td align="right">6,306,887</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">703,980</td>
<td align="right">704,064</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">12,807,340</td>
<td align="right">12,808,714</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">128,863</td>
<td align="right">128,869</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,407,892</td>
<td align="right">1,407,949</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">193,042</td>
<td align="right">193,048</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">27,758,889</td>
<td align="right">27,759,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">31,938,137</td>
<td align="right">31,937,919</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">27,759,034</td>
<td align="right">27,759,054</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,178,102</td>
<td align="right">2,178,102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">768,116</td>
<td align="right">768,116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">768,113</td>
<td align="right">768,113</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">768,113</td>
<td align="right">768,113</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">129,019</td>
<td align="right">129,019</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">129,019</td>
<td align="right">129,019</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">128,869</td>
<td align="right">128,869</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">128,841</td>
<td align="right">128,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">128,841</td>
<td align="right">128,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right"></td>
<td align="right">4,431,430</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">4,229,924</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">2,123,225</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">4,471</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">2,139</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">588</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">312</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right"></td>
<td align="right">300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">294</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">151</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">133</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right"></td>
<td align="right">12</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right"></td>
<td align="right">8</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">6</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right"></td>
<td align="right">2</td>
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
<td align="right">24</td>
<td align="right">116</td>
<td align="right">383.3%</td>
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
