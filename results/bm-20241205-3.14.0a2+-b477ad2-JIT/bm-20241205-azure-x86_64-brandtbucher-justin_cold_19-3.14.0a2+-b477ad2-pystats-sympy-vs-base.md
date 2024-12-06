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
<td align="left">JUMP_BACKWARD</td>
<td align="right">18,942,693</td>
<td align="right">7,968,768</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">883,870</td>
<td align="right">459,171</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">597,608</td>
<td align="right">352,328</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,329,742</td>
<td align="right">5,062,214</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,575,310</td>
<td align="right">2,800,550</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">15,283,368</td>
<td align="right">10,751,665</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,069,729</td>
<td align="right">1,467,741</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,199,821</td>
<td align="right">1,578,438</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">12,121,544</td>
<td align="right">9,249,634</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">5,048,467</td>
<td align="right">4,019,834</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,675,982</td>
<td align="right">2,161,765</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">15,281,630</td>
<td align="right">12,460,634</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,495,735</td>
<td align="right">27,314,905</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,688,895</td>
<td align="right">4,677,448</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,432,017</td>
<td align="right">2,830,702</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,431,223</td>
<td align="right">2,847,142</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,220,504</td>
<td align="right">11,051,790</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">24,118,052</td>
<td align="right">20,349,509</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">16,315,935</td>
<td align="right">13,831,427</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,171,754</td>
<td align="right">4,405,184</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,787,322</td>
<td align="right">1,524,201</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,032,986</td>
<td align="right">4,302,890</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">18,444,808</td>
<td align="right">16,167,352</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,039,679</td>
<td align="right">14,081,842</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">41,937,287</td>
<td align="right">37,030,679</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">44,003,504</td>
<td align="right">39,253,596</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,438,834</td>
<td align="right">3,085,322</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">54,253,015</td>
<td align="right">48,786,000</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,521,656</td>
<td align="right">1,371,839</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,876,788</td>
<td align="right">10,718,954</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">60,529,800</td>
<td align="right">54,640,138</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">49,878,553</td>
<td align="right">45,212,057</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,952,537</td>
<td align="right">9,974,104</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,097,845</td>
<td align="right">19,259,177</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">15,550,002</td>
<td align="right">14,280,957</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">19,939,377</td>
<td align="right">18,326,412</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">40,119,718</td>
<td align="right">36,888,183</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">29,764,786</td>
<td align="right">27,375,569</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">23,315,393</td>
<td align="right">21,473,927</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">30,247,362</td>
<td align="right">27,864,259</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,837,732</td>
<td align="right">30,285,932</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,496,994</td>
<td align="right">4,159,864</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">12,801,590</td>
<td align="right">11,855,739</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">140,547,167</td>
<td align="right">130,185,481</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">202,757,253</td>
<td align="right">187,834,536</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,821,491</td>
<td align="right">2,618,069</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">55,923,961</td>
<td align="right">51,928,853</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">43,426,759</td>
<td align="right">40,342,988</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">20,336,816</td>
<td align="right">18,911,465</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,287,111</td>
<td align="right">38,399,750</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">60,249,182</td>
<td align="right">56,093,605</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">114,629,307</td>
<td align="right">107,277,573</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,106,931</td>
<td align="right">11,340,517</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">595,446,488</td>
<td align="right">558,547,525</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">171,635,299</td>
<td align="right">161,226,933</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,752,892</td>
<td align="right">5,415,309</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,609,828</td>
<td align="right">4,347,368</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,550,094</td>
<td align="right">3,355,617</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">85,006,702</td>
<td align="right">80,509,632</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,227,891</td>
<td align="right">5,901,691</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,589,355</td>
<td align="right">6,251,757</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">70,493,507</td>
<td align="right">74,097,437</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">18,594,943</td>
<td align="right">17,678,553</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">42,392,735</td>
<td align="right">40,327,208</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">17,727,365</td>
<td align="right">16,881,236</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">61,557,694</td>
<td align="right">58,679,280</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">103,938,482</td>
<td align="right">99,188,112</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,740,757</td>
<td align="right">20,757,741</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">29,888,149</td>
<td align="right">28,544,248</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,740,700</td>
<td align="right">33,204,282</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">25,961,315</td>
<td align="right">24,869,986</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">171,142,277</td>
<td align="right">164,810,619</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">158,248,623</td>
<td align="right">152,986,740</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,628</td>
<td align="right">4,049,244</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">42,948,813</td>
<td align="right">41,707,102</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,758,844</td>
<td align="right">1,709,838</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,741,742</td>
<td align="right">17,308,595</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,588,246</td>
<td align="right">2,530,786</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,280,167</td>
<td align="right">26,696,808</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,046,590</td>
<td align="right">15,806,042</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,671,167</td>
<td align="right">17,469,318</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,587,409</td>
<td align="right">4,538,836</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,642,723</td>
<td align="right">6,577,024</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">8,930</td>
<td align="right">9,017</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,567,713</td>
<td align="right">15,423,904</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,914,582</td>
<td align="right">15,815,569</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,938,841</td>
<td align="right">9,971,311</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,169</td>
<td align="right">40,299</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,869,477</td>
<td align="right">97,558,087</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,222,137</td>
<td align="right">1,219,558</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,042</td>
<td align="right">18,069</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,954</td>
<td align="right">2,958</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,651</td>
<td align="right">165,519</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,444</td>
<td align="right">1,445</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">493,598</td>
<td align="right">493,270</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">36,444</td>
<td align="right">36,467</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,225</td>
<td align="right">175,313</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,079</td>
<td align="right">83,117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">17,033</td>
<td align="right">17,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,045</td>
<td align="right">1,287,524</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">78,652</td>
<td align="right">78,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">172,051</td>
<td align="right">172,008</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">456,431</td>
<td align="right">456,533</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,516,756</td>
<td align="right">7,515,488</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,028,325</td>
<td align="right">1,028,496</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,028,930</td>
<td align="right">1,029,101</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">20,688</td>
<td align="right">20,690</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">182,107,814</td>
<td align="right">182,092,882</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">642,591</td>
<td align="right">642,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,568</td>
<td align="right">942,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">642,575</td>
<td align="right">642,622</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,352</td>
<td align="right">4,469,046</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,012</td>
<td align="right">2,281,159</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,399</td>
<td align="right">141,406</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">17,497,461</td>
<td align="right">17,496,670</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,885</td>
<td align="right">745,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,126</td>
<td align="right">2,195,053</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,563</td>
<td align="right">427,549</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,976,719</td>
<td align="right">21,977,237</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,622,369</td>
<td align="right">6,622,218</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,859</td>
<td align="right">389,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,427</td>
<td align="right">1,754,458</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,510</td>
<td align="right">1,244,528</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">147,673</td>
<td align="right">147,671</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,160</td>
<td align="right">1,323,177</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,324</td>
<td align="right">6,744,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,500,358</td>
<td align="right">10,500,479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,966,257</td>
<td align="right">1,966,235</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,276</td>
<td align="right">746,283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,646</td>
<td align="right">1,389,658</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,728,123</td>
<td align="right">3,728,091</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,035,335</td>
<td align="right">6,035,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,036,043</td>
<td align="right">1,036,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,070</td>
<td align="right">655,070</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,070</td>
<td align="right">655,070</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,070</td>
<td align="right">655,070</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">389,282</td>
<td align="right">389,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">372,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">338,565</td>
<td align="right">338,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">270,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">178,536</td>
<td align="right">178,536</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">178,534</td>
<td align="right">178,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">133,724</td>
<td align="right">133,724</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">89,010</td>
<td align="right">89,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">14,629</td>
<td align="right">14,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">9,212</td>
<td align="right">9,212</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,941</td>
<td align="right">8,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">8,858</td>
<td align="right">8,858</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,742</td>
<td align="right">3,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,645</td>
<td align="right">2,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,679</td>
<td align="right">1,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,455</td>
<td align="right">1,455</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,055</td>
<td align="right">1,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">591</td>
<td align="right">591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">447</td>
<td align="right">447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">394</td>
<td align="right">394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">255</td>
<td align="right">255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">133</td>
<td align="right">133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">102</td>
<td align="right">102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">92</td>
<td align="right">92</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
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
<td align="right">27,259,407</td>
<td align="right">65.4%</td>
<td align="right">26,676,180</td>
<td align="right">64.9%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,387,610</td>
<td align="right">34.5%</td>
<td align="right">14,385,917</td>
<td align="right">35.0%</td>
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
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">126</td>
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
<td align="right">19,492</td>
<td align="right">93.9%</td>
<td align="right">19,359</td>
<td align="right">93.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,268</td>
<td align="right">6.1%</td>
<td align="right">1,269</td>
<td align="right">6.2%</td>
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
<td align="left">multiply different types</td>
<td align="right">2,578</td>
<td align="right">13.2%</td>
<td align="right">2,450</td>
<td align="right">12.7%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">211</td>
<td align="right">1.1%</td>
<td align="right">210</td>
<td align="right">1.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">572</td>
<td align="right">2.9%</td>
<td align="right">571</td>
<td align="right">2.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">704</td>
<td align="right">3.6%</td>
<td align="right">703</td>
<td align="right">3.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,085</td>
<td align="right">5.6%</td>
<td align="right">1,086</td>
<td align="right">5.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,212</td>
<td align="right">6.2%</td>
<td align="right">1,211</td>
<td align="right">6.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,288</td>
<td align="right">6.6%</td>
<td align="right">1,287</td>
<td align="right">6.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,894</td>
<td align="right">14.8%</td>
<td align="right">2,893</td>
<td align="right">14.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">16.5%</td>
<td align="right">3,221</td>
<td align="right">16.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">11.4%</td>
<td align="right">2,225</td>
<td align="right">11.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,006</td>
<td align="right">5.2%</td>
<td align="right">1,006</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">5.0%</td>
<td align="right">982</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">716</td>
<td align="right">3.7%</td>
<td align="right">716</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.9%</td>
<td align="right">363</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">189</td>
<td align="right">1.0%</td>
<td align="right">189</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.8%</td>
<td align="right">155</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.5%</td>
<td align="right">91</td>
<td align="right">0.5%</td>
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
<td align="right">8,858</td>
<td align="right">100.0%</td>
<td align="right">8,858</td>
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
<td align="right">8,323,736</td>
<td align="right">20.3%</td>
<td align="right">5,057,020</td>
<td align="right">13.4%</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,751</td>
<td align="right">0.0%</td>
<td align="right">10,762</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,750,146</td>
<td align="right">79.7%</td>
<td align="right">32,747,499</td>
<td align="right">86.6%</td>
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
<td align="right">5,224</td>
<td align="right">84.2%</td>
<td align="right">4,412</td>
<td align="right">81.8%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">982</td>
<td align="right">15.8%</td>
<td align="right">982</td>
<td align="right">18.2%</td>
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
<td align="right">3,687</td>
<td align="right">70.6%</td>
<td align="right">2,876</td>
<td align="right">65.2%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">691</td>
<td align="right">13.2%</td>
<td align="right">690</td>
<td align="right">15.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">8.1%</td>
<td align="right">422</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">275</td>
<td align="right">5.3%</td>
<td align="right">275</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">148</td>
<td align="right">2.8%</td>
<td align="right">148</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">24,747,895</td>
<td align="right">7.7%</td>
<td align="right">24,444,391</td>
<td align="right">7.6%</td>
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
<td align="right">296,029,884</td>
<td align="right">92.3%</td>
<td align="right">296,113,382</td>
<td align="right">92.4%</td>
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
<td align="right">20,193</td>
<td align="right">0.0%</td>
<td align="right">20,195</td>
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
<td align="right">13,673</td>
<td align="right">0.0%</td>
<td align="right">13,673</td>
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
<td align="right">483,570</td>
<td align="right">99.9%</td>
<td align="right">477,871</td>
<td align="right">99.9%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">536</td>
<td align="right">0.1%</td>
<td align="right">536</td>
<td align="right">0.1%</td>
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
<td align="left">out of versions</td>
<td align="right">536</td>
<td align="right">100.0%</td>
<td align="right">536</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">536</td>
<td align="right">100.0%</td>
<td align="right">536</td>
<td align="right">100.0%</td>
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
<td align="right">399</td>
<td align="right">9.4%</td>
<td align="right">399</td>
<td align="right">9.4%</td>
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
<td align="right">2,805</td>
<td align="right">66.0%</td>
<td align="right">2,805</td>
<td align="right">66.0%</td>
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
<td align="right">25,923,841</td>
<td align="right">33.5%</td>
<td align="right">24,832,776</td>
<td align="right">32.5%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">409,643</td>
<td align="right">0.5%</td>
<td align="right">409,704</td>
<td align="right">0.5%</td>
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
<td align="right">51,026,880</td>
<td align="right">65.9%</td>
<td align="right">51,033,798</td>
<td align="right">66.9%</td>
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
<td align="right">36,311</td>
<td align="right">80.4%</td>
<td align="right">36,037</td>
<td align="right">80.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,836</td>
<td align="right">19.6%</td>
<td align="right">8,846</td>
<td align="right">19.7%</td>
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
<td align="left">bool</td>
<td align="right">409</td>
<td align="right">1.1%</td>
<td align="right">233</td>
<td align="right">0.6%</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,395</td>
<td align="right">17.6%</td>
<td align="right">6,314</td>
<td align="right">17.5%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">116</td>
<td align="right">0.3%</td>
<td align="right">115</td>
<td align="right">0.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">136</td>
<td align="right">0.4%</td>
<td align="right">135</td>
<td align="right">0.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,145</td>
<td align="right">8.7%</td>
<td align="right">3,137</td>
<td align="right">8.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,254</td>
<td align="right">11.7%</td>
<td align="right">4,251</td>
<td align="right">11.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,103</td>
<td align="right">38.8%</td>
<td align="right">14,099</td>
<td align="right">39.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">20.6%</td>
<td align="right">7,480</td>
<td align="right">20.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">44</td>
<td align="right">0.1%</td>
<td align="right">44</td>
<td align="right">0.1%</td>
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
<td align="right">4,571,380</td>
<td align="right">16.3%</td>
<td align="right">2,797,055</td>
<td align="right">10.6%</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,953</td>
<td align="right">83.7%</td>
<td align="right">23,499,804</td>
<td align="right">89.3%</td>
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
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">1,020</td>
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
<td align="right">3,808</td>
<td align="right">96.9%</td>
<td align="right">3,373</td>
<td align="right">96.5%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">122</td>
<td align="right">3.1%</td>
<td align="right">122</td>
<td align="right">3.5%</td>
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
<td align="right">1,901</td>
<td align="right">49.9%</td>
<td align="right">1,463</td>
<td align="right">43.4%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,471</td>
<td align="right">38.6%</td>
<td align="right">1,474</td>
<td align="right">43.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">7.9%</td>
<td align="right">299</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">137</td>
<td align="right">3.6%</td>
<td align="right">137</td>
<td align="right">4.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">829,461</td>
<td align="right">1.3%</td>
<td align="right">446,091</td>
<td align="right">0.9%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,891,813</td>
<td align="right">46.5%</td>
<td align="right">22,972,776</td>
<td align="right">45.3%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">33,440,309</td>
<td align="right">52.1%</td>
<td align="right">27,280,072</td>
<td align="right">53.8%</td>
<td align="right">-18.4%</td>
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
<td align="right">16,270</td>
<td align="right">22.9%</td>
<td align="right">9,034</td>
<td align="right">20.9%</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">54,729</td>
<td align="right">77.1%</td>
<td align="right">34,133</td>
<td align="right">79.1%</td>
<td align="right">-37.6%</td>
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
<td align="right">45,819</td>
<td align="right">83.7%</td>
<td align="right">25,891</td>
<td align="right">75.9%</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,709</td>
<td align="right">4.9%</td>
<td align="right">2,383</td>
<td align="right">7.0%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,875</td>
<td align="right">5.3%</td>
<td align="right">2,556</td>
<td align="right">7.5%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,333</td>
<td align="right">2.4%</td>
<td align="right">1,310</td>
<td align="right">3.8%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.4%</td>
<td align="right">758</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">557</td>
<td align="right">1.0%</td>
<td align="right">557</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.7%</td>
<td align="right">382</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.4%</td>
<td align="right">243</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">24</td>
<td align="right">0.1%</td>
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
<td align="right">60,188,943</td>
<td align="right">18.5%</td>
<td align="right">56,034,330</td>
<td align="right">17.5%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">43,142,551</td>
<td align="right">13.3%</td>
<td align="right">40,308,146</td>
<td align="right">12.6%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">221,823,341</td>
<td align="right">68.2%</td>
<td align="right">224,385,660</td>
<td align="right">69.9%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,588</td>
<td align="right">0.0%</td>
<td align="right">18,588</td>
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
<td align="right">826,808</td>
<td align="right">94.8%</td>
<td align="right">773,405</td>
<td align="right">94.6%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,081</td>
<td align="right">5.2%</td>
<td align="right">44,077</td>
<td align="right">5.4%</td>
<td align="right">-2.2%</td>
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
<td align="left">builtin class method</td>
<td align="right">244</td>
<td align="right">0.5%</td>
<td align="right">208</td>
<td align="right">0.5%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,009</td>
<td align="right">6.7%</td>
<td align="right">2,777</td>
<td align="right">6.3%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,165</td>
<td align="right">7.0%</td>
<td align="right">3,083</td>
<td align="right">7.0%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,158</td>
<td align="right">46.9%</td>
<td align="right">20,611</td>
<td align="right">46.8%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,059</td>
<td align="right">9.0%</td>
<td align="right">3,995</td>
<td align="right">9.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,360</td>
<td align="right">5.2%</td>
<td align="right">2,324</td>
<td align="right">5.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,812</td>
<td align="right">15.1%</td>
<td align="right">6,807</td>
<td align="right">15.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,097</td>
<td align="right">6.9%</td>
<td align="right">3,095</td>
<td align="right">7.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">148</td>
<td align="right">0.3%</td>
<td align="right">148</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">244,526,562</td>
<td align="right">100.0%</td>
<td align="right">234,932,974</td>
<td align="right">100.0%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,522</td>
<td align="right">0.0%</td>
<td align="right">4,526</td>
<td align="right">0.0%</td>
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
<td align="right">1,294</td>
<td align="right">0.0%</td>
<td align="right">1,294</td>
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
<td align="right">13,568</td>
<td align="right">100.0%</td>
<td align="right">13,591</td>
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
<td align="right">2,265,728</td>
<td align="right">100.0%</td>
<td align="right">2,265,815</td>
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
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">30</td>
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
<td align="right">30</td>
<td align="right">100.0%</td>
<td align="right">30</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">731,565</td>
<td align="right">72.0%</td>
<td align="right">731,572</td>
<td align="right">72.0%</td>
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
<td align="right">268,986</td>
<td align="right">26.5%</td>
<td align="right">268,986</td>
<td align="right">26.5%</td>
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
<td align="right">14,711</td>
<td align="right">1.4%</td>
<td align="right">14,711</td>
<td align="right">1.4%</td>
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
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
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
<td align="right">1,108</td>
<td align="right">100.0%</td>
<td align="right">1,108</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,578,206</td>
<td align="right">17.4%</td>
<td align="right">1,575,196</td>
<td align="right">17.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,915</td>
<td align="right">1.9%</td>
<td align="right">174,004</td>
<td align="right">1.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,325,175</td>
<td align="right">80.7%</td>
<td align="right">7,328,181</td>
<td align="right">80.7%</td>
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
<td align="right">30,031</td>
<td align="right">96.9%</td>
<td align="right">29,971</td>
<td align="right">96.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">975</td>
<td align="right">3.1%</td>
<td align="right">974</td>
<td align="right">3.1%</td>
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
<td align="left">not managed dict</td>
<td align="right">296</td>
<td align="right">30.4%</td>
<td align="right">294</td>
<td align="right">30.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">158</td>
<td align="right">16.2%</td>
<td align="right">159</td>
<td align="right">16.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.1%</td>
<td align="right">518</td>
<td align="right">53.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3</td>
<td align="right">0.3%</td>
<td align="right">3</td>
<td align="right">0.3%</td>
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
<td align="right">591</td>
<td align="right">100.0%</td>
<td align="right">591</td>
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
<td align="right">882,159</td>
<td align="right">4.7%</td>
<td align="right">457,569</td>
<td align="right">2.5%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,742,361</td>
<td align="right">95.3%</td>
<td align="right">17,740,609</td>
<td align="right">97.5%</td>
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
<td align="right">1,135</td>
<td align="right">66.3%</td>
<td align="right">1,026</td>
<td align="right">64.0%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">576</td>
<td align="right">33.7%</td>
<td align="right">576</td>
<td align="right">36.0%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">1,135</td>
<td align="right">100.0%</td>
<td align="right">1,026</td>
<td align="right">100.0%</td>
<td align="right">-9.6%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">442,501</td>
<td align="right">0.3%</td>
<td align="right">395,894</td>
<td align="right">0.2%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,919,432</td>
<td align="right">6.1%</td>
<td align="right">9,952,903</td>
<td align="right">6.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">153,538,918</td>
<td align="right">93.7%</td>
<td align="right">153,549,497</td>
<td align="right">93.7%</td>
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
<td align="right">11,776</td>
<td align="right">43.3%</td>
<td align="right">10,772</td>
<td align="right">42.5%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,437</td>
<td align="right">56.7%</td>
<td align="right">14,582</td>
<td align="right">57.5%</td>
<td align="right">-5.5%</td>
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
<td align="right">1,873</td>
<td align="right">15.9%</td>
<td align="right">1,612</td>
<td align="right">15.0%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">6,231</td>
<td align="right">52.9%</td>
<td align="right">5,489</td>
<td align="right">51.0%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">717</td>
<td align="right">6.1%</td>
<td align="right">722</td>
<td align="right">6.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,263</td>
<td align="right">10.7%</td>
<td align="right">1,258</td>
<td align="right">11.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">723</td>
<td align="right">6.1%</td>
<td align="right">722</td>
<td align="right">6.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">7.5%</td>
<td align="right">883</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.7%</td>
<td align="right">84</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">6,241</td>
<td align="right">0.0%</td>
<td align="right">6,320</td>
<td align="right">0.0%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,693,760</td>
<td align="right">100.0%</td>
<td align="right">83,475,609</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
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
<td align="right">297</td>
<td align="right">11.0%</td>
<td align="right">305</td>
<td align="right">11.3%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,392</td>
<td align="right">89.0%</td>
<td align="right">2,392</td>
<td align="right">88.7%</td>
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
<td align="right">254</td>
<td align="right">85.5%</td>
<td align="right">262</td>
<td align="right">85.9%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.5%</td>
<td align="right">43</td>
<td align="right">14.1%</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">171,233,852</td>
<td align="right">4.7%</td>
<td align="right">153,788,466</td>
<td align="right">4.5%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,152,446,052</td>
<td align="right">59.0%</td>
<td align="right">2,017,098,185</td>
<td align="right">59.0%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,253,482,511</td>
<td align="right">34.4%</td>
<td align="right">1,180,243,675</td>
<td align="right">34.5%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">71,181,312</td>
<td align="right">2.0%</td>
<td align="right">67,610,225</td>
<td align="right">2.0%</td>
<td align="right">-5.0%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">882,159</td>
<td align="right">0.5%</td>
<td align="right">457,569</td>
<td align="right">0.3%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,323,736</td>
<td align="right">4.9%</td>
<td align="right">5,057,020</td>
<td align="right">3.3%</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,571,380</td>
<td align="right">2.7%</td>
<td align="right">2,797,055</td>
<td align="right">1.8%</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,440,309</td>
<td align="right">19.6%</td>
<td align="right">27,280,072</td>
<td align="right">17.8%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">60,188,943</td>
<td align="right">35.2%</td>
<td align="right">56,034,330</td>
<td align="right">36.5%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">25,923,841</td>
<td align="right">15.2%</td>
<td align="right">24,832,776</td>
<td align="right">16.2%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,259,407</td>
<td align="right">15.9%</td>
<td align="right">26,676,180</td>
<td align="right">17.4%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,919,432</td>
<td align="right">5.8%</td>
<td align="right">9,952,903</td>
<td align="right">6.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">173,915</td>
<td align="right">0.1%</td>
<td align="right">174,004</td>
<td align="right">0.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.2%</td>
<td align="right">268,986</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">11,806,877</td>
<td align="right">16.6%</td>
<td align="right">9,960,915</td>
<td align="right">14.7%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">20,594,991</td>
<td align="right">28.9%</td>
<td align="right">19,850,365</td>
<td align="right">29.4%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,157,327</td>
<td align="right">10.1%</td>
<td align="right">6,950,645</td>
<td align="right">10.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,320,939</td>
<td align="right">15.9%</td>
<td align="right">11,114,899</td>
<td align="right">16.4%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,113,215</td>
<td align="right">8.6%</td>
<td align="right">6,015,913</td>
<td align="right">8.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,165,404</td>
<td align="right">4.4%</td>
<td align="right">3,130,492</td>
<td align="right">4.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,577,427</td>
<td align="right">2.2%</td>
<td align="right">1,574,417</td>
<td align="right">2.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,579</td>
<td align="right">3.0%</td>
<td align="right">2,103,592</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,495</td>
<td align="right">7.2%</td>
<td align="right">5,102,511</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">581,605</td>
<td align="right">0.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">408,684</td>
<td align="right">0.6%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,393,853</td>
<td align="right">10.6%</td>
<td align="right">22,191,531</td>
<td align="right">10.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">98,023,893</td>
<td align="right">46.6%</td>
<td align="right">97,712,503</td>
<td align="right">46.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">98,023,893</td>
<td align="right">46.6%</td>
<td align="right">97,712,503</td>
<td align="right">46.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,333,964</td>
<td align="right">19.6%</td>
<td align="right">41,224,284</td>
<td align="right">19.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,629,255</td>
<td align="right">35.9%</td>
<td align="right">75,520,187</td>
<td align="right">35.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,630,040</td>
<td align="right">35.9%</td>
<td align="right">75,520,972</td>
<td align="right">35.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,531,522</td>
<td align="right">53.4%</td>
<td align="right">112,625,837</td>
<td align="right">53.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,185</td>
<td align="right">0.5%</td>
<td align="right">950,090</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,916,546</td>
<td align="right">89.2%</td>
<td align="right">187,901,835</td>
<td align="right">89.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,500</td>
<td align="right">8.8%</td>
<td align="right">18,490,913</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,331,894</td>
<td align="right">4.4%</td>
<td align="right">9,332,080</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">348</td>
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
<td align="right">2,373,652</td>
<td align="right"></td>
<td align="right">2,022,397</td>
<td align="right"></td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,337,418</td>
<td align="right"></td>
<td align="right">2,886,723</td>
<td align="right"></td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">965,387</td>
<td align="right"></td>
<td align="right">865,937</td>
<td align="right"></td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,665,210,493</td>
<td align="right">33.7%</td>
<td align="right">1,786,926,190</td>
<td align="right">36.0%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,763,602,675</td>
<td align="right">30.6%</td>
<td align="right">1,881,313,637</td>
<td align="right">32.5%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,651,296,300</td>
<td align="right">33.4%</td>
<td align="right">1,562,873,507</td>
<td align="right">31.5%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,007,375,167</td>
<td align="right">34.9%</td>
<td align="right">1,922,948,484</td>
<td align="right">33.2%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">441,369,490</td>
<td align="right">8.9%</td>
<td align="right">423,456,268</td>
<td align="right">8.5%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">705,027,323</td>
<td align="right">12.2%</td>
<td align="right">684,036,954</td>
<td align="right">11.8%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">147,717,431</td>
<td align="right"></td>
<td align="right">145,229,941</td>
<td align="right"></td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,280,691,277</td>
<td align="right">22.2%</td>
<td align="right">1,301,089,698</td>
<td align="right">22.5%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,178,916,645</td>
<td align="right">23.9%</td>
<td align="right">1,191,807,476</td>
<td align="right">24.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">765,010</td>
<td align="right">0.1%</td>
<td align="right">761,833</td>
<td align="right">0.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,630</td>
<td align="right">0.0%</td>
<td align="right">8,651</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">265,421,911</td>
<td align="right"></td>
<td align="right">265,474,997</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,115</td>
<td align="right"></td>
<td align="right">866,243</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">245,548,910</td>
<td align="right"></td>
<td align="right">245,542,178</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">232,901,802</td>
<td align="right">45.3%</td>
<td align="right">232,895,442</td>
<td align="right">45.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">232,128,162</td>
<td align="right">45.1%</td>
<td align="right">232,124,958</td>
<td align="right">45.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">281,718,200</td>
<td align="right">54.7%</td>
<td align="right">281,716,807</td>
<td align="right">54.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">281,749,590</td>
<td align="right"></td>
<td align="right">281,748,202</td>
<td align="right"></td>
<td align="right">-0.0%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">208</td>
<td align="right">1.2%</td>
<td align="right">66</td>
<td align="right">0.4%</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">237</td>
<td align="right">1.3%</td>
<td align="right">111</td>
<td align="right">0.6%</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">7,080</td>
<td align="right">39.9%</td>
<td align="right">3,497</td>
<td align="right">19.6%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">10,679</td>
<td align="right">60.1%</td>
<td align="right">14,386</td>
<td align="right">80.4%</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">138,115,144</td>
<td align="right"></td>
<td align="right">170,545,811</td>
<td align="right"></td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,691,363,293</td>
<td align="right">1,948.6%</td>
<td align="right">3,212,298,310</td>
<td align="right">1,883.5%</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">10,864</td>
<td align="right">61.2%</td>
<td align="right">12,618</td>
<td align="right">70.6%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">17,759</td>
<td align="right"></td>
<td align="right">17,883</td>
<td align="right"></td>
<td align="right">0.7%</td>
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
<td align="right">6,992</td>
<td align="right">98.8%</td>
<td align="right">3,350</td>
<td align="right">95.8%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">7,080</td>
<td align="right"></td>
<td align="right">3,497</td>
<td align="right"></td>
<td align="right">-50.6%</td>
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
<td align="right">974</td>
<td align="right">13.8%</td>
<td align="right">663</td>
<td align="right">19.0%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,148</td>
<td align="right">16.2%</td>
<td align="right">625</td>
<td align="right">17.9%</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,667</td>
<td align="right">37.7%</td>
<td align="right">1,019</td>
<td align="right">29.1%</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,499</td>
<td align="right">21.2%</td>
<td align="right">657</td>
<td align="right">18.8%</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">771</td>
<td align="right">10.9%</td>
<td align="right">491</td>
<td align="right">14.0%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">42</td>
<td align="right">1.2%</td>
<td align="right">100.0%</td>
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
<td align="right">130</td>
<td align="right">1.8%</td>
<td align="right">114</td>
<td align="right">3.3%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,059</td>
<td align="right">15.0%</td>
<td align="right">740</td>
<td align="right">21.2%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,490</td>
<td align="right">21.0%</td>
<td align="right">759</td>
<td align="right">21.7%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">3,108</td>
<td align="right">43.9%</td>
<td align="right">1,053</td>
<td align="right">30.1%</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,082</td>
<td align="right">15.3%</td>
<td align="right">597</td>
<td align="right">17.1%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">123</td>
<td align="right">1.7%</td>
<td align="right">87</td>
<td align="right">2.5%</td>
<td align="right">-29.3%</td>
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
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">159,560</td>
<td align="right">1,063,545</td>
<td align="right">566.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">245,074</td>
<td align="right">1,228,272</td>
<td align="right">401.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">389,868</td>
<td align="right">1,470,296</td>
<td align="right">277.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">98,155</td>
<td align="right">361,171</td>
<td align="right">268.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">902,203</td>
<td align="right">2,860,414</td>
<td align="right">217.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">28,820</td>
<td align="right">86,105</td>
<td align="right">198.8%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">75,547</td>
<td align="right">180.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">144,184</td>
<td align="right">338,644</td>
<td align="right">134.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">73,352</td>
<td align="right">170,582</td>
<td align="right">132.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,676,202</td>
<td align="right">3,783,855</td>
<td align="right">125.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,382,790</td>
<td align="right">2,884,823</td>
<td align="right">108.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">3,163,771</td>
<td align="right">6,157,588</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">52,447</td>
<td align="right">101,062</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,285,620</td>
<td align="right">2,443,770</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">651,732</td>
<td align="right">1,234,293</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">174,242</td>
<td align="right">316,580</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">630,363</td>
<td align="right">1,144,610</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">14,413,893</td>
<td align="right">24,227,666</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">563,070</td>
<td align="right">916,374</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,350,102</td>
<td align="right">2,195,589</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">740</td>
<td align="right">301</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">559,109</td>
<td align="right">885,514</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">1,756,371</td>
<td align="right">2,735,336</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,997,152</td>
<td align="right">3,089,750</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">2,451,940</td>
<td align="right">3,786,203</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,418,944</td>
<td align="right">17,302,044</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">8,363,227</td>
<td align="right">12,356,757</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">5,190,269</td>
<td align="right">7,573,099</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,289,854</td>
<td align="right">3,280,814</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">3,257,658</td>
<td align="right">4,601,929</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">28,217,477</td>
<td align="right">39,836,582</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">19,401,269</td>
<td align="right">26,752,973</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">12,897,171</td>
<td align="right">17,632,829</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">6,294,843</td>
<td align="right">8,572,458</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">320,482</td>
<td align="right">435,835</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,845,323</td>
<td align="right">10,665,526</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">188,292</td>
<td align="right">253,310</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,828,471</td>
<td align="right">2,450,166</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,167,025</td>
<td align="right">2,902,082</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">5,632,289</td>
<td align="right">7,471,083</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">14,115,583</td>
<td align="right">18,578,635</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">10,287,240</td>
<td align="right">13,520,604</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">27,616,421</td>
<td align="right">35,940,376</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">12,320,998</td>
<td align="right">15,856,244</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">8,164,711</td>
<td align="right">10,445,532</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">18,170,104</td>
<td align="right">23,231,511</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">20,075,215</td>
<td align="right">25,566,657</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">20,075,215</td>
<td align="right">25,566,657</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">28,183,801</td>
<td align="right">35,497,924</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">1,700,867</td>
<td align="right">2,125,635</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">43,862,115</td>
<td align="right">54,658,332</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">8,857,957</td>
<td align="right">11,032,783</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">17,422,331</td>
<td align="right">21,684,898</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">4,518,304</td>
<td align="right">5,593,196</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">138,115,144</td>
<td align="right">170,545,811</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">10,327,560</td>
<td align="right">12,723,782</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">17,930,785</td>
<td align="right">22,084,995</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">13,152,572</td>
<td align="right">16,167,323</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">123,959,761</td>
<td align="right">151,921,494</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">65,044,876</td>
<td align="right">79,424,349</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">50,863,037</td>
<td align="right">61,912,483</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">12,145,732</td>
<td align="right">14,751,866</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">8,754,165</td>
<td align="right">10,625,285</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">12,003,080</td>
<td align="right">14,551,956</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">4,844,884</td>
<td align="right">5,858,156</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">13,829,904</td>
<td align="right">16,676,305</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">6,470,729</td>
<td align="right">7,802,171</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">18,570,974</td>
<td align="right">22,295,929</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">180,676,028</td>
<td align="right">215,766,739</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,782,421</td>
<td align="right">5,696,262</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">6,789,340</td>
<td align="right">8,079,337</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">11,619,473</td>
<td align="right">13,818,686</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">18,009,098</td>
<td align="right">21,380,581</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">67,652,140</td>
<td align="right">80,244,488</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">19,153,321</td>
<td align="right">22,686,660</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">13,061,559</td>
<td align="right">15,438,242</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">27,640,796</td>
<td align="right">32,612,335</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">277,943,844</td>
<td align="right">327,780,594</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">38,183,322</td>
<td align="right">44,911,268</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">24,311,134</td>
<td align="right">28,561,998</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">5,959,657</td>
<td align="right">6,988,022</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">5,959,657</td>
<td align="right">6,988,022</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,512,341</td>
<td align="right">6,458,319</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,402,495</td>
<td align="right">1,643,124</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,402,495</td>
<td align="right">1,643,124</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">229,000,852</td>
<td align="right">267,222,838</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">22,814,997</td>
<td align="right">26,590,307</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">39,060</td>
<td align="right">45,381</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">31,966,902</td>
<td align="right">37,019,817</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">26,637,130</td>
<td align="right">30,644,152</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">6,747,959</td>
<td align="right">7,738,001</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,044,003</td>
<td align="right">11,505,642</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">14,717,363</td>
<td align="right">16,806,248</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">13,917,454</td>
<td align="right">15,874,903</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">133,379,502</td>
<td align="right">152,001,169</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">12,832,674</td>
<td align="right">14,590,263</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">9,165,055</td>
<td align="right">10,407,661</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">64,917,843</td>
<td align="right">73,674,026</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">48,364,818</td>
<td align="right">54,837,535</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,272,531</td>
<td align="right">1,437,896</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,272,531</td>
<td align="right">1,437,896</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">5,925,402</td>
<td align="right">6,691,649</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">4,652,896</td>
<td align="right">5,253,753</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,410,975</td>
<td align="right">9,480,715</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">33,118,751</td>
<td align="right">37,322,580</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">58,082,989</td>
<td align="right">65,316,329</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,611,167</td>
<td align="right">9,662,606</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">8,611,795</td>
<td align="right">9,663,234</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">8,611,795</td>
<td align="right">9,663,234</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,526,324</td>
<td align="right">7,292,023</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,526,324</td>
<td align="right">7,292,023</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40,327,029</td>
<td align="right">45,016,000</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">34,410,665</td>
<td align="right">38,352,331</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">27,241,753</td>
<td align="right">30,260,962</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">39,216,208</td>
<td align="right">42,830,620</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">7,785,993</td>
<td align="right">8,500,416</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,560,007</td>
<td align="right">7,142,859</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">6,909,856</td>
<td align="right">7,510,923</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">6,909,856</td>
<td align="right">7,510,923</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">6,505,347</td>
<td align="right">7,047,522</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">42,560,884</td>
<td align="right">45,220,928</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">24,402</td>
<td align="right">25,796</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">24,402</td>
<td align="right">25,796</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">17,733,426</td>
<td align="right">18,744,704</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">42,491,080</td>
<td align="right">43,880,723</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">13,195,318</td>
<td align="right">13,398,977</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">13,195,318</td>
<td align="right">13,398,977</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">416,256</td>
<td align="right">416,123</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">416,256</td>
<td align="right">416,123</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,513,838</td>
<td align="right">2,513,934</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,798,069</td>
<td align="right">15,798,501</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,228</td>
<td align="right">18,228</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,166</td>
<td align="right">5,166</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">744</td>
<td align="right">744</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">628</td>
<td align="right">628</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right"></td>
<td align="right">337,554</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right"></td>
<td align="right">337,552</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right"></td>
<td align="right">337,552</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">245,299</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">245,299</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right"></td>
<td align="right">168,776</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">132,426</td>
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
<td align="left">CALL</td>
<td align="right">784</td>
<td align="right">1,209</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,792</td>
<td align="right">2,000</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">21</td>
<td align="right">21</td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-12-06
