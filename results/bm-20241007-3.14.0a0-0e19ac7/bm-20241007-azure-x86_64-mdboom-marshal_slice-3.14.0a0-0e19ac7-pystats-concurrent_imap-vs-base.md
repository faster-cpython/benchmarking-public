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
<td align="right">427,577</td>
<td align="right">384,420</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,368,454</td>
<td align="right">3,937,022</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,618,640</td>
<td align="right">1,460,420</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,038,194</td>
<td align="right">937,541</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,863,941</td>
<td align="right">5,295,936</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,338,912</td>
<td align="right">1,209,439</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">892,736</td>
<td align="right">806,444</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">299,094</td>
<td align="right">270,228</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">395,548</td>
<td align="right">357,488</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,655,580</td>
<td align="right">1,497,360</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,538,368</td>
<td align="right">1,394,391</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">309,134</td>
<td align="right">280,268</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,880</td>
<td align="right">17,120</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,703,780</td>
<td align="right">1,545,560</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,542,206</td>
<td align="right">1,399,562</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,419,232</td>
<td align="right">1,289,759</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">489,233</td>
<td align="right">445,444</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">652,583</td>
<td align="right">594,991</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">492,145</td>
<td align="right">448,892</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">494,061</td>
<td align="right">450,765</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">329,150</td>
<td align="right">300,425</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">330,610</td>
<td align="right">301,885</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">177,069</td>
<td align="right">162,659</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">535,261</td>
<td align="right">492,127</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">7,350,843</td>
<td align="right">6,776,422</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">189,911</td>
<td align="right">175,356</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">188,747</td>
<td align="right">174,314</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,121,187</td>
<td align="right">1,961,829</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,708,461</td>
<td align="right">6,204,663</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">193,709</td>
<td align="right">179,296</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">11,426,389</td>
<td align="right">10,578,293</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">15,001,771</td>
<td align="right">13,894,375</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">7,052,097</td>
<td align="right">6,550,524</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,247,715</td>
<td align="right">2,089,305</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">14,131,142</td>
<td align="right">13,169,646</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,217,643</td>
<td align="right">6,728,385</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,531,474</td>
<td align="right">1,430,821</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,319,590</td>
<td align="right">3,103,992</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,214,223</td>
<td align="right">3,942,324</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,607,761</td>
<td align="right">1,505,970</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,902,755</td>
<td align="right">3,658,092</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,640,670</td>
<td align="right">4,352,835</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,162,921</td>
<td align="right">12,356,129</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,470,015</td>
<td align="right">1,383,536</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,718,644</td>
<td align="right">2,561,030</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">85,918,522</td>
<td align="right">80,971,073</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,512,556</td>
<td align="right">3,312,407</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,181,378</td>
<td align="right">3,009,005</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">8,640,075</td>
<td align="right">8,180,749</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">847,291</td>
<td align="right">804,085</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,411,296</td>
<td align="right">6,094,539</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">18,172,836</td>
<td align="right">17,295,217</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">26,639,792</td>
<td align="right">25,445,594</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">965,619</td>
<td align="right">922,482</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,432,562</td>
<td align="right">9,015,299</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">31,393,436</td>
<td align="right">30,014,244</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,330,027</td>
<td align="right">1,272,252</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,691,520</td>
<td align="right">14,072,209</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">343,511</td>
<td align="right">329,121</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">21,457,962</td>
<td align="right">20,580,840</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,700,299</td>
<td align="right">5,469,593</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,443,542</td>
<td align="right">1,386,014</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">20,321,721</td>
<td align="right">19,545,581</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">8,876,634</td>
<td align="right">8,574,318</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,457,232</td>
<td align="right">8,169,415</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,731,666</td>
<td align="right">1,674,099</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,669,536</td>
<td align="right">3,554,442</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,880,423</td>
<td align="right">3,765,360</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">9,054,177</td>
<td align="right">8,809,666</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,389,158</td>
<td align="right">1,360,338</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">97</td>
<td align="right">95</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,590,645</td>
<td align="right">6,461,356</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">816,955</td>
<td align="right">803,643</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">16,350,071</td>
<td align="right">16,147,321</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,270,828</td>
<td align="right">1,256,399</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,966,018</td>
<td align="right">3,937,198</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">7,331</td>
<td align="right">7,288</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">553,339</td>
<td align="right">555,075</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">18,091</td>
<td align="right">18,052</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">23,291</td>
<td align="right">23,252</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">23,291</td>
<td align="right">23,252</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">118,688</td>
<td align="right">118,780</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,112</td>
<td align="right">35,086</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">25,570</td>
<td align="right">25,558</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">70,982</td>
<td align="right">71,005</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,121,906</td>
<td align="right">1,121,975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">751,107</td>
<td align="right">751,067</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">43,776</td>
<td align="right">43,774</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">27,400</td>
<td align="right">27,399</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">124,755</td>
<td align="right">124,758</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">44,888</td>
<td align="right">44,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,056,282</td>
<td align="right">1,056,305</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">86,740</td>
<td align="right">86,739</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,241,042</td>
<td align="right">2,241,062</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">236,536</td>
<td align="right">236,534</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,241,220</td>
<td align="right">6,241,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,823,420</td>
<td align="right">5,823,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">5,730,320</td>
<td align="right">5,730,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,163,100</td>
<td align="right">1,163,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,053,600</td>
<td align="right">1,053,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">571,260</td>
<td align="right">571,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">525,740</td>
<td align="right">525,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">130,860</td>
<td align="right">130,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">130,280</td>
<td align="right">130,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">108,280</td>
<td align="right">108,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">107,300</td>
<td align="right">107,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">95,160</td>
<td align="right">95,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">86,200</td>
<td align="right">86,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">86,200</td>
<td align="right">86,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">83,700</td>
<td align="right">83,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">78,000</td>
<td align="right">78,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">69,940</td>
<td align="right">69,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">69,900</td>
<td align="right">69,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">62,680</td>
<td align="right">62,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">61,240</td>
<td align="right">61,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">57,160</td>
<td align="right">57,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">47,800</td>
<td align="right">47,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">41,220</td>
<td align="right">41,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">38,780</td>
<td align="right">38,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">36,760</td>
<td align="right">36,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">35,860</td>
<td align="right">35,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">32,460</td>
<td align="right">32,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">29,440</td>
<td align="right">29,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">25,860</td>
<td align="right">25,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">21,440</td>
<td align="right">21,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">18,640</td>
<td align="right">18,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">16,700</td>
<td align="right">16,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">15,660</td>
<td align="right">15,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">11,380</td>
<td align="right">11,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">10,400</td>
<td align="right">10,400</td>
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
<td align="right">8,317</td>
<td align="right">8,317</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,320</td>
<td align="right">5,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,200</td>
<td align="right">5,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,860</td>
<td align="right">4,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,780</td>
<td align="right">4,780</td>
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
<td align="left">CALL_TYPE_1</td>
<td align="right">880</td>
<td align="right">880</td>
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
<td align="left">EXTENDED_ARG</td>
<td align="right">180</td>
<td align="right">180</td>
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
<td align="right">245,208</td>
<td align="right">3.1%</td>
<td align="right">220,027</td>
<td align="right">3.0%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,843,353</td>
<td align="right">73.2%</td>
<td align="right">5,276,899</td>
<td align="right">72.0%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,873,112</td>
<td align="right">23.5%</td>
<td align="right">1,817,079</td>
<td align="right">24.8%</td>
<td align="right">-3.0%</td>
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
<td align="right">5,294</td>
<td align="right">21.0%</td>
<td align="right">4,818</td>
<td align="right">20.8%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">19,910</td>
<td align="right">79.0%</td>
<td align="right">18,360</td>
<td align="right">79.2%</td>
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
<td align="left">add different types</td>
<td align="right">14,402</td>
<td align="right">72.3%</td>
<td align="right">12,982</td>
<td align="right">70.7%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,620</td>
<td align="right">8.1%</td>
<td align="right">1,569</td>
<td align="right">8.5%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,070</td>
<td align="right">15.4%</td>
<td align="right">2,992</td>
<td align="right">16.3%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">678</td>
<td align="right">3.4%</td>
<td align="right">677</td>
<td align="right">3.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">140</td>
<td align="right">0.7%</td>
<td align="right">140</td>
<td align="right">0.8%</td>
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
<td align="right">18,880</td>
<td align="right">100.0%</td>
<td align="right">17,120</td>
<td align="right">100.0%</td>
<td align="right">-9.3%</td>
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
<td align="right">559,854</td>
<td align="right">50.3%</td>
<td align="right">530,988</td>
<td align="right">48.9%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">552,311</td>
<td align="right">49.6%</td>
<td align="right">554,028</td>
<td align="right">51.0%</td>
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
<td align="right">728</td>
<td align="right">70.8%</td>
<td align="right">747</td>
<td align="right">71.3%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">300</td>
<td align="right">29.2%</td>
<td align="right">300</td>
<td align="right">28.7%</td>
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
<td align="right">728</td>
<td align="right">100.0%</td>
<td align="right">727</td>
<td align="right">97.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">2.7%</td>
<td align="right"></td>
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
<td align="right">21,490,272</td>
<td align="right">99.8%</td>
<td align="right">20,165,936</td>
<td align="right">99.8%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19,269</td>
<td align="right">0.1%</td>
<td align="right">19,265</td>
<td align="right">0.1%</td>
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
<td align="right">5,100</td>
<td align="right">0.0%</td>
<td align="right">5,100</td>
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
<td align="right">16,723</td>
<td align="right">100.0%</td>
<td align="right">16,701</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">144,551</td>
<td align="right">2.9%</td>
<td align="right">130,209</td>
<td align="right">2.8%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">483,789</td>
<td align="right">9.8%</td>
<td align="right">440,292</td>
<td align="right">9.3%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,308,155</td>
<td align="right">87.2%</td>
<td align="right">4,135,695</td>
<td align="right">87.8%</td>
<td align="right">-4.0%</td>
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
<td align="right">3,681</td>
<td align="right">45.2%</td>
<td align="right">3,393</td>
<td align="right">44.8%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,460</td>
<td align="right">54.8%</td>
<td align="right">4,187</td>
<td align="right">55.2%</td>
<td align="right">-6.1%</td>
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
<td align="right">3,243</td>
<td align="right">88.1%</td>
<td align="right">2,956</td>
<td align="right">87.1%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">138</td>
<td align="right">3.7%</td>
<td align="right">137</td>
<td align="right">4.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">300</td>
<td align="right">8.1%</td>
<td align="right">300</td>
<td align="right">8.8%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,533,894</td>
<td align="right">100.0%</td>
<td align="right">1,433,241</td>
<td align="right">100.0%</td>
<td align="right">-6.6%</td>
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
<td align="right">15,133,475</td>
<td align="right">92.9%</td>
<td align="right">14,787,863</td>
<td align="right">92.7%</td>
<td align="right">-2.3%</td>
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
<td align="right">7.1%</td>
<td align="right">1,160,760</td>
<td align="right">7.3%</td>
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
<td align="right">700</td>
<td align="right">29.9%</td>
<td align="right">700</td>
<td align="right">29.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,640</td>
<td align="right">70.1%</td>
<td align="right">1,640</td>
<td align="right">70.1%</td>
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
<td align="right">460</td>
<td align="right">28.0%</td>
<td align="right">460</td>
<td align="right">28.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">460</td>
<td align="right">28.0%</td>
<td align="right">460</td>
<td align="right">28.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">340</td>
<td align="right">20.7%</td>
<td align="right">340</td>
<td align="right">20.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">200</td>
<td align="right">12.2%</td>
<td align="right">200</td>
<td align="right">12.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">140</td>
<td align="right">8.5%</td>
<td align="right">140</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">40</td>
<td align="right">2.4%</td>
<td align="right">40</td>
<td align="right">2.4%</td>
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
<td align="right">6,675,295</td>
<td align="right">14.3%</td>
<td align="right">6,171,673</td>
<td align="right">13.9%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">39,681,449</td>
<td align="right">84.7%</td>
<td align="right">37,595,698</td>
<td align="right">85.0%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">450,190</td>
<td align="right">1.0%</td>
<td align="right">451,144</td>
<td align="right">1.0%</td>
<td align="right">0.2%</td>
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
<td align="right">13,330</td>
<td align="right">32.4%</td>
<td align="right">13,204</td>
<td align="right">32.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">27,840</td>
<td align="right">67.6%</td>
<td align="right">27,800</td>
<td align="right">67.8%</td>
<td align="right">-0.1%</td>
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
<td align="right">3,310</td>
<td align="right">24.8%</td>
<td align="right">3,233</td>
<td align="right">24.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">2,372</td>
<td align="right">17.8%</td>
<td align="right">2,352</td>
<td align="right">17.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,942</td>
<td align="right">29.6%</td>
<td align="right">3,929</td>
<td align="right">29.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,200</td>
<td align="right">9.0%</td>
<td align="right">1,200</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">560</td>
<td align="right">4.2%</td>
<td align="right">560</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">220</td>
<td align="right">1.7%</td>
<td align="right">220</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">80</td>
<td align="right">0.6%</td>
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
<td align="left">metaclass attribute</td>
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
<td align="right">22,190,854</td>
<td align="right">99.8%</td>
<td align="right">20,594,200</td>
<td align="right">99.7%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,592</td>
<td align="right">0.1%</td>
<td align="right">13,592</td>
<td align="right">0.1%</td>
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
<td align="right">800</td>
<td align="right">0.0%</td>
<td align="right">800</td>
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
<td align="right">28,560</td>
<td align="right">0.1%</td>
<td align="right">28,560</td>
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
<td align="left">Success</td>
<td align="right">12,038</td>
<td align="right">100.0%</td>
<td align="right">12,026</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">1,648,080</td>
<td align="right">100.0%</td>
<td align="right">1,489,860</td>
<td align="right">100.0%</td>
<td align="right">-9.6%</td>
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
<td align="right">4,504,730</td>
<td align="right">94.6%</td>
<td align="right">4,216,895</td>
<td align="right">94.2%</td>
<td align="right">-6.4%</td>
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
<td align="right">1.7%</td>
<td align="right">80,700</td>
<td align="right">1.8%</td>
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
<td align="right">171,800</td>
<td align="right">3.6%</td>
<td align="right">171,800</td>
<td align="right">3.8%</td>
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
<td align="right">7,500</td>
<td align="right">82.2%</td>
<td align="right">7,499</td>
<td align="right">82.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,620</td>
<td align="right">17.8%</td>
<td align="right">1,620</td>
<td align="right">17.8%</td>
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
<td align="right">880</td>
<td align="right">54.3%</td>
<td align="right">880</td>
<td align="right">54.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">460</td>
<td align="right">28.4%</td>
<td align="right">460</td>
<td align="right">28.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">200</td>
<td align="right">12.3%</td>
<td align="right">200</td>
<td align="right">12.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">80</td>
<td align="right">4.9%</td>
<td align="right">80</td>
<td align="right">4.9%</td>
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
<td align="right">1,607,761</td>
<td align="right">98.3%</td>
<td align="right">1,505,970</td>
<td align="right">98.2%</td>
<td align="right">-6.3%</td>
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
<td align="right">1.6%</td>
<td align="right">26,560</td>
<td align="right">1.7%</td>
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
<td align="right">35.7%</td>
<td align="right">299</td>
<td align="right">35.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">540</td>
<td align="right">64.3%</td>
<td align="right">540</td>
<td align="right">64.4%</td>
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
<td align="right">380</td>
<td align="right">70.4%</td>
<td align="right">380</td>
<td align="right">70.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">160</td>
<td align="right">29.6%</td>
<td align="right">160</td>
<td align="right">29.6%</td>
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
<td align="right">9,720,249</td>
<td align="right">92.2%</td>
<td align="right">8,930,624</td>
<td align="right">91.7%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">811,472</td>
<td align="right">7.7%</td>
<td align="right">798,158</td>
<td align="right">8.2%</td>
<td align="right">-1.6%</td>
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
<td align="right">2,426</td>
<td align="right">44.2%</td>
<td align="right">2,431</td>
<td align="right">44.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,057</td>
<td align="right">55.8%</td>
<td align="right">3,054</td>
<td align="right">55.7%</td>
<td align="right">-0.1%</td>
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
<td align="right">326</td>
<td align="right">13.4%</td>
<td align="right">332</td>
<td align="right">13.7%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">880</td>
<td align="right">36.3%</td>
<td align="right">879</td>
<td align="right">36.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">620</td>
<td align="right">25.6%</td>
<td align="right">620</td>
<td align="right">25.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">380</td>
<td align="right">15.7%</td>
<td align="right">380</td>
<td align="right">15.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">160</td>
<td align="right">6.6%</td>
<td align="right">160</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">60</td>
<td align="right">2.5%</td>
<td align="right">60</td>
<td align="right">2.5%</td>
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
<td align="right">2,445,440</td>
<td align="right">100.0%</td>
<td align="right">2,416,643</td>
<td align="right">99.9%</td>
<td align="right">-1.2%</td>
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
<td align="right">15,792,371</td>
<td align="right">3.2%</td>
<td align="right">14,663,403</td>
<td align="right">3.1%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">170,676,217</td>
<td align="right">34.5%</td>
<td align="right">161,532,068</td>
<td align="right">34.4%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">306,646,628</td>
<td align="right">62.1%</td>
<td align="right">292,465,833</td>
<td align="right">62.3%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,046,289</td>
<td align="right">0.2%</td>
<td align="right">1,007,720</td>
<td align="right">0.2%</td>
<td align="right">-3.7%</td>
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
<td align="right">5,843,353</td>
<td align="right">37.2%</td>
<td align="right">5,276,899</td>
<td align="right">36.2%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,880</td>
<td align="right">0.1%</td>
<td align="right">17,120</td>
<td align="right">0.1%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">483,789</td>
<td align="right">3.1%</td>
<td align="right">440,292</td>
<td align="right">3.0%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,675,295</td>
<td align="right">42.6%</td>
<td align="right">6,171,673</td>
<td align="right">42.4%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">811,472</td>
<td align="right">5.2%</td>
<td align="right">798,158</td>
<td align="right">5.5%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">552,311</td>
<td align="right">3.5%</td>
<td align="right">554,028</td>
<td align="right">3.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">19,269</td>
<td align="right">0.1%</td>
<td align="right">19,265</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,160,760</td>
<td align="right">7.4%</td>
<td align="right">1,160,760</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">80,700</td>
<td align="right">0.5%</td>
<td align="right">80,700</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,560</td>
<td align="right">0.2%</td>
<td align="right">26,560</td>
<td align="right">0.2%</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">245,208</td>
<td align="right">23.4%</td>
<td align="right">220,027</td>
<td align="right">21.8%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">144,491</td>
<td align="right">13.8%</td>
<td align="right">130,149</td>
<td align="right">12.9%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">370,242</td>
<td align="right">35.4%</td>
<td align="right">371,201</td>
<td align="right">36.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">62,228</td>
<td align="right">5.9%</td>
<td align="right">62,223</td>
<td align="right">6.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">171,800</td>
<td align="right">16.4%</td>
<td align="right">171,800</td>
<td align="right">17.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,180</td>
<td align="right">1.7%</td>
<td align="right">18,180</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,380</td>
<td align="right">1.2%</td>
<td align="right">12,380</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,380</td>
<td align="right">1.0%</td>
<td align="right">10,380</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,100</td>
<td align="right">0.5%</td>
<td align="right">5,100</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,140</td>
<td align="right">0.2%</td>
<td align="right">2,140</td>
<td align="right">0.2%</td>
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
<td align="right">458,051</td>
<td align="right">1.5%</td>
<td align="right">429,327</td>
<td align="right">1.4%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">25,230,433</td>
<td align="right">80.3%</td>
<td align="right">23,851,241</td>
<td align="right">79.4%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">22,359,016</td>
<td align="right">71.2%</td>
<td align="right">21,224,335</td>
<td align="right">70.7%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">8,530,397</td>
<td align="right">27.2%</td>
<td align="right">8,285,886</td>
<td align="right">27.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">8,531,837</td>
<td align="right">27.2%</td>
<td align="right">8,287,326</td>
<td align="right">27.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">9,059,437</td>
<td align="right">28.8%</td>
<td align="right">8,814,926</td>
<td align="right">29.3%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">9,059,437</td>
<td align="right">28.8%</td>
<td align="right">8,814,926</td>
<td align="right">29.3%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">23,651</td>
<td align="right">0.1%</td>
<td align="right">23,612</td>
<td align="right">0.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">527,600</td>
<td align="right">1.7%</td>
<td align="right">527,600</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">562,140</td>
<td align="right">1.8%</td>
<td align="right">562,140</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">544,020</td>
<td align="right">1.7%</td>
<td align="right">544,020</td>
<td align="right">1.8%</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">18,703</td>
<td align="right"></td>
<td align="right">38,341</td>
<td align="right"></td>
<td align="right">105.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">60,467</td>
<td align="right"></td>
<td align="right">104,936</td>
<td align="right"></td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">47,980</td>
<td align="right"></td>
<td align="right">72,462</td>
<td align="right"></td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,365,772</td>
<td align="right"></td>
<td align="right">1,250,638</td>
<td align="right"></td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">8,305,331</td>
<td align="right"></td>
<td align="right">7,633,941</td>
<td align="right"></td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">97,096,702</td>
<td align="right">25.8%</td>
<td align="right">91,428,400</td>
<td align="right">25.6%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">98,290,819</td>
<td align="right">23.4%</td>
<td align="right">92,640,559</td>
<td align="right">23.3%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">49,484,040</td>
<td align="right">11.8%</td>
<td align="right">46,678,794</td>
<td align="right">11.7%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">17,664,604</td>
<td align="right"></td>
<td align="right">16,683,130</td>
<td align="right"></td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">17,652,805</td>
<td align="right">48.6%</td>
<td align="right">16,672,578</td>
<td align="right">48.1%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">55,901,684</td>
<td align="right">14.8%</td>
<td align="right">52,853,697</td>
<td align="right">14.8%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">40,189,907</td>
<td align="right">10.7%</td>
<td align="right">38,031,883</td>
<td align="right">10.7%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">204,586,803</td>
<td align="right">48.7%</td>
<td align="right">194,143,666</td>
<td align="right">48.8%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">183,498,486</td>
<td align="right">48.7%</td>
<td align="right">174,395,984</td>
<td align="right">48.9%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">11,697,458</td>
<td align="right"></td>
<td align="right">11,131,221</td>
<td align="right"></td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">67,918,270</td>
<td align="right">16.2%</td>
<td align="right">64,700,572</td>
<td align="right">16.2%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">19,736,415</td>
<td align="right"></td>
<td align="right">18,927,465</td>
<td align="right"></td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">18,557,722</td>
<td align="right">51.1%</td>
<td align="right">17,852,362</td>
<td align="right">51.5%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">18,689,312</td>
<td align="right">51.4%</td>
<td align="right">17,983,907</td>
<td align="right">51.9%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,176</td>
<td align="right">0.2%</td>
<td align="right">77,143</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">54,414</td>
<td align="right">0.1%</td>
<td align="right">54,402</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">800</td>
<td align="right">0.1%</td>
<td align="right">800</td>
<td align="right">0.1%</td>
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
<td align="right">40</td>
<td align="right">3,840</td>
<td align="right">925,840</td>
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
Stats gathered on: 2024-10-08
