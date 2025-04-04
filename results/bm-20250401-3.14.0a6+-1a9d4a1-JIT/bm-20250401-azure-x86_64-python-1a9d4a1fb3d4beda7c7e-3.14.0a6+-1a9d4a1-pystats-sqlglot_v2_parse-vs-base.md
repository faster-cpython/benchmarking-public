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
<td align="left">BINARY_OP</td>
<td align="right">570,015</td>
<td align="right">8,328</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,634,965</td>
<td align="right">523,583</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">11,491,314</td>
<td align="right">2,321,150</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">8,330,477</td>
<td align="right">1,714,488</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">12,360,548</td>
<td align="right">3,188,704</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">7,739,966</td>
<td align="right">2,076,446</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,045,336</td>
<td align="right">1,924,497</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">13,017,670</td>
<td align="right">3,845,826</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,531,340</td>
<td align="right">1,965,098</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">13,271,361</td>
<td align="right">4,099,517</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">13,820,343</td>
<td align="right">4,505,720</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">39,654,248</td>
<td align="right">13,487,082</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">7,136,837</td>
<td align="right">2,550,915</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">7,602,696</td>
<td align="right">3,016,774</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">116,717,374</td>
<td align="right">51,265,962</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">221,193,446</td>
<td align="right">109,388,566</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,863,776</td>
<td align="right">1,994,566</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,863,781</td>
<td align="right">1,994,571</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,832,230</td>
<td align="right">5,247,988</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,210,265</td>
<td align="right">648,707</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,242,530</td>
<td align="right">6,166,469</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,297,647</td>
<td align="right">5,735,871</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">47,841,047</td>
<td align="right">28,437,843</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,641,514</td>
<td align="right">2,813,651</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,695,022</td>
<td align="right">1,665,642</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">20,212,810</td>
<td align="right">12,595,728</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,901,358</td>
<td align="right">8,172,657</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,285,122</td>
<td align="right">835,365</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">9,514,121</td>
<td align="right">6,250,940</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">32,186,396</td>
<td align="right">21,207,184</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,564,937</td>
<td align="right">4,499,471</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">10,679,475</td>
<td align="right">7,450,062</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,906,155</td>
<td align="right">15,378,912</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">15,575,530</td>
<td align="right">11,253,644</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">10,360,381</td>
<td align="right">7,692,966</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,216,499</td>
<td align="right">921,685</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">22,966,579</td>
<td align="right">17,678,000</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">14,036,905</td>
<td align="right">10,804,755</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,512,106</td>
<td align="right">1,943,992</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">640,484</td>
<td align="right">497,705</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,002,857</td>
<td align="right">2,434,743</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">149,720</td>
<td align="right">121,496</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,060,184</td>
<td align="right">6,649,578</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">31,417,469</td>
<td align="right">26,243,691</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,942,393</td>
<td align="right">1,646,167</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">31,991,517</td>
<td align="right">27,264,496</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,190,093</td>
<td align="right">2,745,016</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">781,886</td>
<td align="right">678,855</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">528,193</td>
<td align="right">494,446</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">561,535</td>
<td align="right">527,788</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">16,842,705</td>
<td align="right">16,254,849</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">8,731,583</td>
<td align="right">8,727,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">10,289,436</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">3,942,739</td>
<td align="right">3,942,739</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,811,761</td>
<td align="right">2,811,761</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,786,530</td>
<td align="right">2,786,530</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,004,778</td>
<td align="right">2,004,778</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,759,491</td>
<td align="right">1,759,491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,639,136</td>
<td align="right">1,639,136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,518,030</td>
<td align="right">1,518,030</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,451,491</td>
<td align="right">1,451,491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,376,699</td>
<td align="right">1,376,699</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,145,835</td>
<td align="right">1,145,835</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,081,480</td>
<td align="right">1,081,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">865,176</td>
<td align="right">865,176</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">696,769</td>
<td align="right">696,769</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">665,551</td>
<td align="right">665,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">648,874</td>
<td align="right">648,874</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">640,477</td>
<td align="right">640,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">573,941</td>
<td align="right">573,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">573,941</td>
<td align="right">573,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">573,941</td>
<td align="right">573,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">545,614</td>
<td align="right">545,614</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">490,760</td>
<td align="right">490,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">428,377</td>
<td align="right">428,377</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">411,881</td>
<td align="right">411,881</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">411,741</td>
<td align="right">411,741</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">390,927</td>
<td align="right">390,927</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">341,108</td>
<td align="right">341,108</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">262,011</td>
<td align="right">262,011</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">245,451</td>
<td align="right">245,451</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,773</td>
<td align="right">70,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,556</td>
<td align="right">37,556</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">33,342</td>
<td align="right">33,342</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">29,111</td>
<td align="right">29,111</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">25,020</td>
<td align="right">25,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">24,954</td>
<td align="right">24,954</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">24,954</td>
<td align="right">24,954</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">24,357</td>
<td align="right">24,357</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">20,791</td>
<td align="right">20,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">16,635</td>
<td align="right">16,635</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">12,681</td>
<td align="right">12,681</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">12,477</td>
<td align="right">12,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">12,477</td>
<td align="right">12,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">12,477</td>
<td align="right">12,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">8,388</td>
<td align="right">8,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,388</td>
<td align="right">8,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">8,317</td>
<td align="right">8,317</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,085</td>
<td align="right">7,085</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,631</td>
<td align="right">4,631</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">4,228</td>
<td align="right">4,228</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">4,159</td>
<td align="right">4,159</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">4,158</td>
<td align="right">4,158</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">4,158</td>
<td align="right">4,158</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">4,155</td>
<td align="right">4,155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">784</td>
<td align="right">784</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">414</td>
<td align="right">414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">148</td>
<td align="right">148</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">107</td>
<td align="right">107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">86</td>
<td align="right">86</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">70</td>
<td align="right">70</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">70</td>
<td align="right">70</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">70</td>
<td align="right">70</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">69</td>
<td align="right">69</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">69</td>
<td align="right">69</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">50</td>
<td align="right">50</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">30</td>
<td align="right">30</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">23</td>
<td align="right">23</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">4,259,670</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">879,952</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">526,902</td>
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
<td align="right">569,820</td>
<td align="right">1.5%</td>
<td align="right">8,262</td>
<td align="right">0.0%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,832,066</td>
<td align="right">98.4%</td>
<td align="right">36,832,066</td>
<td align="right">99.9%</td>
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
<td align="right">12,782</td>
<td align="right">0.0%</td>
<td align="right">12,782</td>
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
<td align="right">141</td>
<td align="right">32.6%</td>
<td align="right">12</td>
<td align="right">3.9%</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">292</td>
<td align="right">67.4%</td>
<td align="right">292</td>
<td align="right">96.1%</td>
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
<td align="right">140</td>
<td align="right">99.3%</td>
<td align="right">11</td>
<td align="right">91.7%</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1</td>
<td align="right">0.7%</td>
<td align="right">1</td>
<td align="right">8.3%</td>
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
<td align="right">1,451,491</td>
<td align="right">100.0%</td>
<td align="right">1,451,491</td>
<td align="right">100.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">772,211</td>
<td align="right">2.1%</td>
<td align="right">772,211</td>
<td align="right">2.1%</td>
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
<td align="right">36,229,174</td>
<td align="right">97.9%</td>
<td align="right">36,229,174</td>
<td align="right">97.9%</td>
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
<td align="right">786,786</td>
<td align="right">2.1%</td>
<td align="right">786,786</td>
<td align="right">2.1%</td>
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
<td align="right">15,359</td>
<td align="right">100.0%</td>
<td align="right">15,359</td>
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
<td align="right">25</td>
<td align="right">50.0%</td>
<td align="right">25</td>
<td align="right">50.0%</td>
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
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">25</td>
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
<td align="right">9,511,656</td>
<td align="right">38.6%</td>
<td align="right">6,249,254</td>
<td align="right">29.3%</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,105,465</td>
<td align="right">61.4%</td>
<td align="right">15,105,465</td>
<td align="right">70.7%</td>
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
<td align="right">2,442</td>
<td align="right">99.1%</td>
<td align="right">1,663</td>
<td align="right">98.6%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">23</td>
<td align="right">0.9%</td>
<td align="right">23</td>
<td align="right">1.4%</td>
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
<td align="left">baseobject</td>
<td align="right">2,304</td>
<td align="right">94.3%</td>
<td align="right">1,546</td>
<td align="right">93.0%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">138</td>
<td align="right">5.7%</td>
<td align="right">117</td>
<td align="right">7.0%</td>
<td align="right">-15.2%</td>
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
<td align="right">37,445</td>
<td align="right">0.5%</td>
<td align="right">37,445</td>
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
<td align="right">7,049,475</td>
<td align="right">91.0%</td>
<td align="right">7,049,475</td>
<td align="right">91.0%</td>
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
<td align="right">661,297</td>
<td align="right">8.5%</td>
<td align="right">661,297</td>
<td align="right">8.5%</td>
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
<td align="right">12,491</td>
<td align="right">99.2%</td>
<td align="right">12,491</td>
<td align="right">99.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97</td>
<td align="right">0.8%</td>
<td align="right">97</td>
<td align="right">0.8%</td>
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
<td align="right">50</td>
<td align="right">51.5%</td>
<td align="right">50</td>
<td align="right">51.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">47</td>
<td align="right">48.5%</td>
<td align="right">47</td>
<td align="right">48.5%</td>
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
<td align="right">6,529,705</td>
<td align="right">97.7%</td>
<td align="right">1,964,580</td>
<td align="right">94.0%</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">153,948</td>
<td align="right">2.3%</td>
<td align="right">125,724</td>
<td align="right">6.0%</td>
<td align="right">-18.3%</td>
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
<td align="right">1,630</td>
<td align="right">99.7%</td>
<td align="right">513</td>
<td align="right">99.0%</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5</td>
<td align="right">0.3%</td>
<td align="right">5</td>
<td align="right">1.0%</td>
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
<td align="left">enumerate</td>
<td align="right">140</td>
<td align="right">8.6%</td>
<td align="right">11</td>
<td align="right">2.1%</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">819</td>
<td align="right">50.2%</td>
<td align="right">260</td>
<td align="right">50.7%</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">292</td>
<td align="right">17.9%</td>
<td align="right">98</td>
<td align="right">19.1%</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">377</td>
<td align="right">23.1%</td>
<td align="right">142</td>
<td align="right">27.7%</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
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
<td align="right">10,672,513</td>
<td align="right">6.0%</td>
<td align="right">7,443,858</td>
<td align="right">4.3%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,608,354</td>
<td align="right">1.5%</td>
<td align="right">2,207,853</td>
<td align="right">1.3%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">163,722,089</td>
<td align="right">92.5%</td>
<td align="right">164,035,958</td>
<td align="right">94.4%</td>
<td align="right">0.2%</td>
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
<td align="right">49,841</td>
<td align="right">88.7%</td>
<td align="right">42,274</td>
<td align="right">88.3%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,334</td>
<td align="right">11.3%</td>
<td align="right">5,576</td>
<td align="right">11.7%</td>
<td align="right">-12.0%</td>
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
<td align="right">5,384</td>
<td align="right">85.0%</td>
<td align="right">4,626</td>
<td align="right">83.0%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">785</td>
<td align="right">12.4%</td>
<td align="right">785</td>
<td align="right">14.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">143</td>
<td align="right">2.3%</td>
<td align="right">143</td>
<td align="right">2.6%</td>
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
<td align="right">23,635,502</td>
<td align="right">100.0%</td>
<td align="right">17,903,010</td>
<td align="right">100.0%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">167</td>
<td align="right">0.0%</td>
<td align="right">167</td>
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
<td align="right">212</td>
<td align="right">0.0%</td>
<td align="right">212</td>
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
<td align="right">251</td>
<td align="right">100.0%</td>
<td align="right">251</td>
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
<td align="right">2,771,313</td>
<td align="right">7.0%</td>
<td align="right">2,540,329</td>
<td align="right">6.4%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,882,935</td>
<td align="right">93.0%</td>
<td align="right">37,109,529</td>
<td align="right">93.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">43</td>
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
<td align="right">52,336</td>
<td align="right">100.0%</td>
<td align="right">47,946</td>
<td align="right">100.0%</td>
<td align="right">-8.4%</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">4,158</td>
<td align="right">100.0%</td>
<td align="right">4,158</td>
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
<td align="right">1</td>
<td align="right">100.0%</td>
<td align="right">1</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,900,287</td>
<td align="right">5.9%</td>
<td align="right">1,459,598</td>
<td align="right">4.6%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">30,130,256</td>
<td align="right">94.1%</td>
<td align="right">30,346,621</td>
<td align="right">95.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,386</td>
<td align="right">0.0%</td>
<td align="right">4,386</td>
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
<td align="right">35,912</td>
<td align="right">99.8%</td>
<td align="right">27,591</td>
<td align="right">99.8%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">68</td>
<td align="right">0.2%</td>
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
<td align="right">47</td>
<td align="right">69.1%</td>
<td align="right">47</td>
<td align="right">69.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">30.9%</td>
<td align="right">21</td>
<td align="right">30.9%</td>
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
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">5</td>
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
<td align="right">3,863,776</td>
<td align="right">100.0%</td>
<td align="right">3,863,776</td>
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
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">25</td>
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
<td align="right">434,642,064</td>
<td align="right">47.4%</td>
<td align="right">236,778,431</td>
<td align="right">45.7%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">444,182,860</td>
<td align="right">48.5%</td>
<td align="right">256,311,248</td>
<td align="right">49.5%</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">28,789,995</td>
<td align="right">3.1%</td>
<td align="right">17,169,472</td>
<td align="right">3.3%</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">8,741,032</td>
<td align="right">1.0%</td>
<td align="right">7,668,982</td>
<td align="right">1.5%</td>
<td align="right">-12.3%</td>
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
<td align="right">569,820</td>
<td align="right">1.9%</td>
<td align="right">8,262</td>
<td align="right">0.0%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,529,705</td>
<td align="right">22.1%</td>
<td align="right">1,964,580</td>
<td align="right">11.0%</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">9,511,656</td>
<td align="right">32.2%</td>
<td align="right">6,249,254</td>
<td align="right">34.9%</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">10,672,513</td>
<td align="right">36.1%</td>
<td align="right">7,443,858</td>
<td align="right">41.5%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,451,491</td>
<td align="right">4.9%</td>
<td align="right">1,451,491</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">772,211</td>
<td align="right">2.6%</td>
<td align="right">772,211</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,445</td>
<td align="right">0.1%</td>
<td align="right">37,445</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,386</td>
<td align="right">0.0%</td>
<td align="right">4,386</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">167</td>
<td align="right">0.0%</td>
<td align="right">167</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">43</td>
<td align="right">0.0%</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">657,142</td>
<td align="right">7.5%</td>
<td align="right">436,691</td>
<td align="right">5.7%</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">937,198</td>
<td align="right">10.7%</td>
<td align="right">716,982</td>
<td align="right">9.3%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,065,359</td>
<td align="right">12.2%</td>
<td align="right">848,343</td>
<td align="right">11.1%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">991,871</td>
<td align="right">11.3%</td>
<td align="right">808,386</td>
<td align="right">10.5%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,771,313</td>
<td align="right">31.7%</td>
<td align="right">2,540,329</td>
<td align="right">33.1%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">551,089</td>
<td align="right">6.3%</td>
<td align="right">551,089</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">396,882</td>
<td align="right">4.5%</td>
<td align="right">396,882</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">384,127</td>
<td align="right">4.4%</td>
<td align="right">384,127</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">330,667</td>
<td align="right">3.8%</td>
<td align="right">330,667</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">330,630</td>
<td align="right">3.8%</td>
<td align="right">330,630</td>
<td align="right">4.3%</td>
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
<td align="right">3,942,809</td>
<td align="right">12.5%</td>
<td align="right">3,942,809</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">27,474,767</td>
<td align="right">87.5%</td>
<td align="right">27,474,767</td>
<td align="right">87.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">3,942,809</td>
<td align="right">12.5%</td>
<td align="right">3,942,809</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">3,942,809</td>
<td align="right">12.5%</td>
<td align="right">3,942,809</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">3,942,809</td>
<td align="right">12.5%</td>
<td align="right">3,942,809</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">457,491</td>
<td align="right">1.5%</td>
<td align="right">457,491</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">70</td>
<td align="right">0.0%</td>
<td align="right">70</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,786,535</td>
<td align="right">8.9%</td>
<td align="right">2,786,535</td>
<td align="right">8.9%</td>
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
<td align="right">12,477</td>
<td align="right">0.0%</td>
<td align="right">12,477</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">31,991,517</td>
<td align="right">101.8%</td>
<td align="right">31,991,517</td>
<td align="right">101.8%</td>
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
<td align="left">Mortal decrefs</td>
<td align="right">45,393,070</td>
<td align="right">11.9%</td>
<td align="right">124,284,663</td>
<td align="right">31.4%</td>
<td align="right">173.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">55,114,174</td>
<td align="right">15.1%</td>
<td align="right">123,027,295</td>
<td align="right">33.0%</td>
<td align="right">123.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">29,525,167</td>
<td align="right">8.1%</td>
<td align="right">9,613,211</td>
<td align="right">2.6%</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">35,209,219</td>
<td align="right">9.2%</td>
<td align="right">12,105,727</td>
<td align="right">3.1%</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">58,867,175</td>
<td align="right">15.4%</td>
<td align="right">85,364,980</td>
<td align="right">21.6%</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">266,200</td>
<td align="right"></td>
<td align="right">189,881</td>
<td align="right"></td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">243,227,225</td>
<td align="right">63.6%</td>
<td align="right">174,059,883</td>
<td align="right">44.0%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">204,640,052</td>
<td align="right">56.2%</td>
<td align="right">146,451,087</td>
<td align="right">39.3%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">316,156</td>
<td align="right"></td>
<td align="right">227,806</td>
<td align="right"></td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">74,566,818</td>
<td align="right">20.5%</td>
<td align="right">93,613,939</td>
<td align="right">25.1%</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">50,008</td>
<td align="right"></td>
<td align="right">37,997</td>
<td align="right"></td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">25,663,538</td>
<td align="right"></td>
<td align="right">25,185,921</td>
<td align="right"></td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">7,598,540</td>
<td align="right"></td>
<td align="right">7,610,422</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">14,151,812</td>
<td align="right">44.4%</td>
<td align="right">14,152,181</td>
<td align="right">44.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,820,322</td>
<td align="right"></td>
<td align="right">13,820,420</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">17,683,965</td>
<td align="right"></td>
<td align="right">17,684,052</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">17,687,393</td>
<td align="right">55.6%</td>
<td align="right">17,687,480</td>
<td align="right">55.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">14,151,812</td>
<td align="right">44.4%</td>
<td align="right">14,151,833</td>
<td align="right">44.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">304</td>
<td align="right">0.0%</td>
<td align="right">304 / 0 !!</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">44</td>
<td align="right">0.0%</td>
<td align="right">44 / 0 !!</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">657,122</td>
<td align="right"></td>
<td align="right">657,122</td>
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
<td align="right">607</td>
<td align="right">1,067,240</td>
<td align="right">11,942,350</td>
<td align="right">731,946</td>
<td align="right">1,193,565</td>
<td align="right">607</td>
<td align="right">1,067,240</td>
<td align="right">11,942,383</td>
<td align="right">732,036</td>
<td align="right">1,193,873</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-04
