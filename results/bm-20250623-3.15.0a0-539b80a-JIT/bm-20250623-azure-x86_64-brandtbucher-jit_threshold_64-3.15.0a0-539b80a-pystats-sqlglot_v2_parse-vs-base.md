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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">921,685</td>
<td align="right">22,732</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">4,228</td>
<td align="right">132</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">494,446</td>
<td align="right">58,843</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">527,788</td>
<td align="right">89,392</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">121,496</td>
<td align="right">26,683</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">523,583</td>
<td align="right">174,803</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">12,681</td>
<td align="right">4,617</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,924,497</td>
<td align="right">708,388</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,714,488</td>
<td align="right">649,184</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">879,905</td>
<td align="right">355,080</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">526,902</td>
<td align="right">229,016</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">2,321,150</td>
<td align="right">1,040,399</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,188,704</td>
<td align="right">1,557,539</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,328</td>
<td align="right">4,341</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,259,709</td>
<td align="right">2,685,182</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,505,720</td>
<td align="right">2,844,140</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">13,487,122</td>
<td align="right">8,750,715</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,845,826</td>
<td align="right">2,559,803</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,994,523</td>
<td align="right">1,340,879</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,994,528</td>
<td align="right">1,340,884</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,081,480</td>
<td align="right">732,306</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,099,517</td>
<td align="right">2,810,701</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,076,446</td>
<td align="right">1,452,905</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,499,471</td>
<td align="right">3,297,018</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,550,915</td>
<td align="right">1,905,204</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,376,699</td>
<td align="right">1,031,620</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,817,771</td>
<td align="right">4,488,351</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">12,595,746</td>
<td align="right">9,785,381</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,016,774</td>
<td align="right">2,368,334</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,166,444</td>
<td align="right">5,014,272</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">51,265,962</td>
<td align="right">41,748,670</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,965,051</td>
<td align="right">1,620,588</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">108,373,809</td>
<td align="right">89,700,710</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,172,657</td>
<td align="right">6,807,550</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">5,735,871</td>
<td align="right">4,808,154</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,943,992</td>
<td align="right">1,641,570</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">21,207,184</td>
<td align="right">18,776,714</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,434,743</td>
<td align="right">2,163,986</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,250,940</td>
<td align="right">5,575,385</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,813,651</td>
<td align="right">2,510,900</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,665,617</td>
<td align="right">1,489,521</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">28,437,800</td>
<td align="right">25,595,283</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,804,734</td>
<td align="right">9,830,299</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">835,365</td>
<td align="right">761,261</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,646,167</td>
<td align="right">1,506,611</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">15,378,912</td>
<td align="right">14,079,571</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">497,705</td>
<td align="right">474,179</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,649,571</td>
<td align="right">6,384,967</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">27,264,496</td>
<td align="right">26,241,488</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">8,727,680</td>
<td align="right">8,405,492</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">18,343,699</td>
<td align="right">17,671,448</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">26,243,691</td>
<td align="right">25,286,408</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,450,062</td>
<td align="right">7,202,071</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">11,253,601</td>
<td align="right">10,900,474</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">7,692,966</td>
<td align="right">7,455,001</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">16,254,849</td>
<td align="right">15,950,038</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">411,741</td>
<td align="right">404,916</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">428,377</td>
<td align="right">421,552</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,639,136</td>
<td align="right">1,620,215</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,759,748</td>
<td align="right">3,722,812</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">545,614</td>
<td align="right">541,582</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">648,707</td>
<td align="right">644,704</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">865,176</td>
<td align="right">861,144</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,759,491</td>
<td align="right">1,753,905</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">678,855</td>
<td align="right">677,982</td>
<td align="right">-0.1%</td>
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
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,145,835</td>
<td align="right">1,145,835</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">696,769</td>
<td align="right">696,769</td>
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
<td align="left">CALL_TYPE_1</td>
<td align="right">490,760</td>
<td align="right">490,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">411,881</td>
<td align="right">411,881</td>
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
<td align="right">8,262</td>
<td align="right">0.0%</td>
<td align="right">4,259</td>
<td align="right">0.0%</td>
<td align="right">-48.5%</td>
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
<td align="right">99.9%</td>
<td align="right">36,832,066</td>
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
<td align="right">12</td>
<td align="right">3.9%</td>
<td align="right">28</td>
<td align="right">8.8%</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">292</td>
<td align="right">96.1%</td>
<td align="right">292</td>
<td align="right">91.2%</td>
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
<td align="right">11</td>
<td align="right">91.7%</td>
<td align="right">27</td>
<td align="right">96.4%</td>
<td align="right">145.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1</td>
<td align="right">8.3%</td>
<td align="right">1</td>
<td align="right">3.6%</td>
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
<td align="right">6,249,254</td>
<td align="right">29.3%</td>
<td align="right">5,573,858</td>
<td align="right">27.4%</td>
<td align="right">-10.8%</td>
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
<td align="right">70.7%</td>
<td align="right">14,760,323</td>
<td align="right">72.6%</td>
<td align="right">-2.3%</td>
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
<td align="right">1,663</td>
<td align="right">98.6%</td>
<td align="right">1,504</td>
<td align="right">98.5%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">23</td>
<td align="right">1.4%</td>
<td align="right">23</td>
<td align="right">1.5%</td>
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
<td align="left">different types</td>
<td align="right">117</td>
<td align="right">7.0%</td>
<td align="right">8</td>
<td align="right">0.5%</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">1,546</td>
<td align="right">93.0%</td>
<td align="right">1,496</td>
<td align="right">99.5%</td>
<td align="right">-3.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">125,724</td>
<td align="right">6.0%</td>
<td align="right">26,815</td>
<td align="right">1.6%</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,964,533</td>
<td align="right">94.0%</td>
<td align="right">1,620,148</td>
<td align="right">98.3%</td>
<td align="right">-17.5%</td>
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
<td align="right">513</td>
<td align="right">99.0%</td>
<td align="right">435</td>
<td align="right">98.9%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5</td>
<td align="right">1.0%</td>
<td align="right">5</td>
<td align="right">1.1%</td>
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
<td align="right">11</td>
<td align="right">2.1%</td>
<td align="right">27</td>
<td align="right">6.2%</td>
<td align="right">145.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">260</td>
<td align="right">50.7%</td>
<td align="right">169</td>
<td align="right">38.9%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">142</td>
<td align="right">27.7%</td>
<td align="right">140</td>
<td align="right">32.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">98</td>
<td align="right">19.1%</td>
<td align="right">97</td>
<td align="right">22.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### GET_ITER

<details>
<summary> specialization stats for GET_ITER family </summary>

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
<td align="right">1,043,979</td>
<td align="right">1,043,979 / 0 !!</td>
<td align="right">1,043,979</td>
<td align="right">1,043,979 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">1,018,955</td>
<td align="right">1,018,955 / 0 !!</td>
<td align="right">1,018,955</td>
<td align="right">1,018,955 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">390,946</td>
<td align="right">390,946 / 0 !!</td>
<td align="right">390,946</td>
<td align="right">390,946 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">54,067</td>
<td align="right">54,067 / 0 !!</td>
<td align="right">54,067</td>
<td align="right">54,067 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,159</td>
<td align="right">4,159 / 0 !!</td>
<td align="right">4,159</td>
<td align="right">4,159 / 0 !!</td>
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
<td align="right">2,207,853</td>
<td align="right">1.4%</td>
<td align="right">884,233</td>
<td align="right">0.6%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,443,858</td>
<td align="right">4.6%</td>
<td align="right">7,196,001</td>
<td align="right">4.6%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">151,300,455</td>
<td align="right">94.0%</td>
<td align="right">148,869,105</td>
<td align="right">94.8%</td>
<td align="right">-1.6%</td>
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
<td align="right">42,274</td>
<td align="right">88.3%</td>
<td align="right">17,310</td>
<td align="right">76.1%</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,576</td>
<td align="right">11.7%</td>
<td align="right">5,442</td>
<td align="right">23.9%</td>
<td align="right">-2.4%</td>
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
<td align="right">143</td>
<td align="right">2.6%</td>
<td align="right">101</td>
<td align="right">1.9%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">785</td>
<td align="right">14.1%</td>
<td align="right">743</td>
<td align="right">13.7%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">4,626</td>
<td align="right">83.0%</td>
<td align="right">4,576</td>
<td align="right">84.1%</td>
<td align="right">-1.1%</td>
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
<td align="right">17,902,960</td>
<td align="right">100.0%</td>
<td align="right">17,285,229</td>
<td align="right">100.0%</td>
<td align="right">-3.5%</td>
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
<td align="right">2,540,329</td>
<td align="right">6.4%</td>
<td align="right">1,664,771</td>
<td align="right">4.3%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">37,109,529</td>
<td align="right">93.6%</td>
<td align="right">37,294,028</td>
<td align="right">95.7%</td>
<td align="right">0.5%</td>
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
<td align="right">47,946</td>
<td align="right">100.0%</td>
<td align="right">31,468</td>
<td align="right">100.0%</td>
<td align="right">-34.4%</td>
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
<td align="right">1,459,598</td>
<td align="right">4.7%</td>
<td align="right">1,266,439</td>
<td align="right">4.2%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,317,216</td>
<td align="right">95.2%</td>
<td align="right">29,237,791</td>
<td align="right">95.8%</td>
<td align="right">-0.3%</td>
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
<td align="right">27,591</td>
<td align="right">99.8%</td>
<td align="right">23,972</td>
<td align="right">99.7%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">68</td>
<td align="right">0.3%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">7,668,946</td>
<td align="right">1.5%</td>
<td align="right">5,276,567</td>
<td align="right">1.2%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">273,280,515</td>
<td align="right">52.7%</td>
<td align="right">233,702,357</td>
<td align="right">52.6%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">218,434,766</td>
<td align="right">42.1%</td>
<td align="right">187,959,524</td>
<td align="right">42.3%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">19,113,417</td>
<td align="right">3.7%</td>
<td align="right">17,538,999</td>
<td align="right">3.9%</td>
<td align="right">-8.2%</td>
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
<td align="right">8,262</td>
<td align="right">0.0%</td>
<td align="right">4,259</td>
<td align="right">0.0%</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,964,533</td>
<td align="right">11.0%</td>
<td align="right">1,620,148</td>
<td align="right">9.7%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,249,254</td>
<td align="right">34.9%</td>
<td align="right">5,573,858</td>
<td align="right">33.5%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,443,858</td>
<td align="right">41.5%</td>
<td align="right">7,196,001</td>
<td align="right">43.2%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,451,491</td>
<td align="right">8.1%</td>
<td align="right">1,451,491</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">772,211</td>
<td align="right">4.3%</td>
<td align="right">772,211</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,445</td>
<td align="right">0.2%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">848,343</td>
<td align="right">11.1%</td>
<td align="right">331,540</td>
<td align="right">6.3%</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,540,329</td>
<td align="right">33.1%</td>
<td align="right">1,664,771</td>
<td align="right">31.5%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">436,691</td>
<td align="right">5.7%</td>
<td align="right">341,618</td>
<td align="right">6.5%</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">716,982</td>
<td align="right">9.3%</td>
<td align="right">620,158</td>
<td align="right">11.8%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">808,386</td>
<td align="right">10.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">551,089</td>
<td align="right">7.2%</td>
<td align="right">551,089</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">396,882</td>
<td align="right">5.2%</td>
<td align="right">396,882</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">384,127</td>
<td align="right">5.0%</td>
<td align="right">384,127</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">330,667</td>
<td align="right">4.3%</td>
<td align="right">330,667</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">330,630</td>
<td align="right">4.3%</td>
<td align="right">330,630</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">271,379</td>
<td align="right">5.1%</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">304</td>
<td align="right">0.0%</td>
<td align="right">82</td>
<td align="right">0.0%</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">44</td>
<td align="right">0.0%</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">12,105,767</td>
<td align="right">3.1%</td>
<td align="right">8,329,058</td>
<td align="right">2.2%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">9,613,231</td>
<td align="right">2.6%</td>
<td align="right">6,660,731</td>
<td align="right">1.8%</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">366,114</td>
<td align="right"></td>
<td align="right">436,470</td>
<td align="right"></td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">421,462</td>
<td align="right"></td>
<td align="right">489,402</td>
<td align="right"></td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">122,936,712</td>
<td align="right">31.8%</td>
<td align="right">136,694,837</td>
<td align="right">35.5%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">169,688,105</td>
<td align="right">44.0%</td>
<td align="right">154,598,879</td>
<td align="right">40.2%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">121,633,629</td>
<td align="right">33.3%</td>
<td align="right">132,200,872</td>
<td align="right">36.3%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">142,179,446</td>
<td align="right">38.9%</td>
<td align="right">130,290,820</td>
<td align="right">35.8%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">81,317,136</td>
<td align="right">21.1%</td>
<td align="right">84,991,432</td>
<td align="right">22.1%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">55,403</td>
<td align="right"></td>
<td align="right">52,994</td>
<td align="right"></td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">92,016,337</td>
<td align="right">25.2%</td>
<td align="right">94,874,774</td>
<td align="right">26.1%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">25,010,122</td>
<td align="right"></td>
<td align="right">24,921,923</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">12,010,463</td>
<td align="right"></td>
<td align="right">12,002,601</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">7,593,016</td>
<td align="right"></td>
<td align="right">7,595,441</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,342,774</td>
<td align="right">38.8%</td>
<td align="right">12,342,640</td>
<td align="right">38.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,342,426</td>
<td align="right">38.8%</td>
<td align="right">12,342,530</td>
<td align="right">38.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">19,442,820</td>
<td align="right">61.2%</td>
<td align="right">19,442,918</td>
<td align="right">61.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">19,439,387</td>
<td align="right"></td>
<td align="right">19,439,470</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
<td align="right">1,067,004</td>
<td align="right">11,982,281</td>
<td align="right">732,283</td>
<td align="right">1,197,096</td>
<td align="right">608</td>
<td align="right">1,062,414</td>
<td align="right">11,967,492</td>
<td align="right">739,435</td>
<td align="right">1,191,555</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">26</td>
<td align="right">1.9%</td>
<td align="right">2,500.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">217</td>
<td align="right">19.7%</td>
<td align="right">506</td>
<td align="right">36.3%</td>
<td align="right">133.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,220,593</td>
<td align="right"></td>
<td align="right">12,541,185</td>
<td align="right"></td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">413</td>
<td align="right">37.5%</td>
<td align="right">270</td>
<td align="right">19.4%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,100</td>
<td align="right"></td>
<td align="right">1,395</td>
<td align="right"></td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">898,411,377</td>
<td align="right">14,442.5%</td>
<td align="right">1,073,952,292</td>
<td align="right">8,563.4%</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">469</td>
<td align="right">42.6%</td>
<td align="right">549</td>
<td align="right">39.4%</td>
<td align="right">17.1%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">44</td>
<td align="right">3.2%</td>
<td align="right">44 / 0 !!</td>
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
<td align="right">44</td>
<td align="right">3.2%</td>
<td align="right">44 / 0 !!</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">413</td>
<td align="right"></td>
<td align="right">270</td>
<td align="right"></td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">348</td>
<td align="right">84.3%</td>
<td align="right">245</td>
<td align="right">90.7%</td>
<td align="right">-29.6%</td>
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

### JIT memory stats

<details>
<summary> JIT memory stats </summary>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Base Size (bytes)</th>
<th align="right">Base Ratio</th>
<th align="right">Head Size (bytes)</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">95,488</td>
<td align="right">2.2%</td>
<td align="right">47,152</td>
<td align="right">1.9%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">3,626,582</td>
<td align="right">82.5%</td>
<td align="right">1,855,690</td>
<td align="right">75.1%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">4,395,008</td>
<td align="right"></td>
<td align="right">2,469,888</td>
<td align="right"></td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">672,938</td>
<td align="right">15.3%</td>
<td align="right">567,046</td>
<td align="right">23.0%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">
Trampoline size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the trampolines of the JIT traces
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">4,096</td>
<td align="right">0.2%</td>
<td align="right">4,096 / 0 !!</td>
</tr>
</tbody>
</table>


</details>

### JIT trace total memory histogram

<details>
<summary> JIT trace total memory histogram </summary>

<table>
<thead>
<tr>
<th align="left">Size (bytes)</th>
<th align="left">Base Count</th>
<th align="right">Base Ratio</th>
<th align="left">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 4,096</td>
<td align="left">127</td>
<td align="right">36.5%</td>
<td align="left">171</td>
<td align="right">69.8%</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">46</td>
<td align="right">13.2%</td>
<td align="left">37</td>
<td align="right">15.1%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">131</td>
<td align="right">37.6%</td>
<td align="left">9</td>
<td align="right">3.7%</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">1</td>
<td align="right">0.3%</td>
<td align="left">3</td>
<td align="right">1.2%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">43</td>
<td align="right">12.4%</td>
<td align="left">25</td>
<td align="right">10.2%</td>
<td align="right">-41.9%</td>
</tr>
</tbody>
</table>


</details>

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
<td align="left"><= 16</td>
<td align="right">42</td>
<td align="right">10.2%</td>
<td align="right">32</td>
<td align="right">11.9%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">107</td>
<td align="right">25.9%</td>
<td align="right">7</td>
<td align="right">2.6%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">108</td>
<td align="right">26.2%</td>
<td align="right">39</td>
<td align="right">14.4%</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">68</td>
<td align="right">16.5%</td>
<td align="right">8</td>
<td align="right">3.0%</td>
<td align="right">-88.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">2 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">88</td>
<td align="right">21.3%</td>
<td align="right">27</td>
<td align="right">10.0%</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">134</td>
<td align="right">49.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21</td>
<td align="right">7.8%</td>
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
<td align="left"><= 16</td>
<td align="right">127</td>
<td align="right">30.8%</td>
<td align="right">36</td>
<td align="right">13.3%</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">107</td>
<td align="right">25.9%</td>
<td align="right">33</td>
<td align="right">12.2%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">69</td>
<td align="right">16.7%</td>
<td align="right">13</td>
<td align="right">4.8%</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">44</td>
<td align="right">10.7%</td>
<td align="right">5</td>
<td align="right">1.9%</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">3</td>
<td align="right">1.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">132</td>
<td align="right">48.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21</td>
<td align="right">7.8%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>


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
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">67,494</td>
<td align="right">945,589</td>
<td align="right">1,301.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">33,747</td>
<td align="right">472,143</td>
<td align="right">1,299.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">33,747</td>
<td align="right">469,350</td>
<td align="right">1,290.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">28,224</td>
<td align="right">123,037</td>
<td align="right">335.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">28,224</td>
<td align="right">123,037</td>
<td align="right">335.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">20,160</td>
<td align="right">77,547</td>
<td align="right">284.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,220,593</td>
<td align="right">12,541,185</td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,220,593</td>
<td align="right">12,541,185</td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">524,142</td>
<td align="right">1,026,543</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">840,934</td>
<td align="right">1,638,355</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">913,161</td>
<td align="right">1,516,888</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">2,065,466</td>
<td align="right">3,267,919</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">11,372,886</td>
<td align="right">17,631,483</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">568,114</td>
<td align="right">870,536</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">3,307,720</td>
<td align="right">5,062,640</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">587,856</td>
<td align="right">888,320</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">568,114</td>
<td align="right">838,871</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">695,688</td>
<td align="right">1,025,790</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">296,226</td>
<td align="right">435,782</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">3,108,591</td>
<td align="right">4,392,414</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,017,772</td>
<td align="right">4,219,012</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,869,253</td>
<td align="right">2,522,897</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">19,767,754</td>
<td align="right">25,835,127</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">212,287</td>
<td align="right">274,251</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">212,287</td>
<td align="right">274,251</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">212,287</td>
<td align="right">274,251</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">6,525,268</td>
<td align="right">8,411,373</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">7,247,209</td>
<td align="right">9,132,269</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">4,046,711</td>
<td align="right">5,022,744</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,120,839</td>
<td align="right">6,336,948</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">15,302,734</td>
<td align="right">18,911,183</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">142,779</td>
<td align="right">175,923</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">4,727,021</td>
<td align="right">5,750,029</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">3,262,402</td>
<td align="right">3,937,798</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">10,398,488</td>
<td align="right">12,524,354</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">185,529,497</td>
<td align="right">220,148,838</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">5,173,778</td>
<td align="right">6,131,061</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">5,173,778</td>
<td align="right">6,131,061</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">5,173,778</td>
<td align="right">6,131,061</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">5,173,778</td>
<td align="right">6,131,061</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">5,173,778</td>
<td align="right">6,127,029</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">9,171,844</td>
<td align="right">10,803,009</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">177,942,081</td>
<td align="right">208,559,076</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,029,405</td>
<td align="right">1,205,501</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">1,869,253</td>
<td align="right">2,177,755</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">142,779</td>
<td align="right">166,305</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">449,757</td>
<td align="right">523,861</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">9,054,610</td>
<td align="right">10,543,403</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,663,664</td>
<td align="right">1,933,777</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">14,383,030</td>
<td align="right">16,646,307</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">26,162,736</td>
<td align="right">30,208,084</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">7,961,440</td>
<td align="right">9,190,670</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">9,913,110</td>
<td align="right">11,370,050</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">2,141,701</td>
<td align="right">2,456,254</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">86,319,677</td>
<td align="right">98,538,381</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,474,482</td>
<td align="right">1,683,149</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">4,585,922</td>
<td align="right">5,234,362</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">9,314,623</td>
<td align="right">10,631,061</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">9,762,700</td>
<td align="right">11,141,081</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">23,072,389</td>
<td align="right">26,323,354</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,585,922</td>
<td align="right">5,231,633</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">9,171,844</td>
<td align="right">10,460,660</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,342,008</td>
<td align="right">20,914,368</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">9,171,844</td>
<td align="right">10,457,867</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">9,170,164</td>
<td align="right">10,450,915</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">65,447,307</td>
<td align="right">74,269,561</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">15,098,557</td>
<td align="right">17,118,255</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">6,113,277</td>
<td align="right">6,811,859</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">3,111,382</td>
<td align="right">3,460,162</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,663,520</td>
<td align="right">6,287,998</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,322,739</td>
<td align="right">4,754,151</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">4,285,847</td>
<td align="right">4,674,079</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,565,172</td>
<td align="right">4,909,557</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">445,077</td>
<td align="right">454,695</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">561,558</td>
<td align="right">571,147</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">5,152,293</td>
<td align="right">5,090,298</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">1,572,323</td>
<td align="right">1,587,183</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">445,077</td>
<td align="right">449,109</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">445,077</td>
<td align="right">449,109</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">445,077</td>
<td align="right">449,109</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">103,031</td>
<td align="right">103,904</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">561,558</td>
<td align="right">565,561</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">561,558</td>
<td align="right">565,561</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">561,558</td>
<td align="right">565,561</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">561,558</td>
<td align="right">565,561</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">565,688</td>
<td align="right">569,720</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">674,581</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">353,143</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right"></td>
<td align="right">349,174</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right"></td>
<td align="right">347,935</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right"></td>
<td align="right">347,935</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right"></td>
<td align="right">266,081</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right"></td>
<td align="right">103,904</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right"></td>
<td align="right">28,872</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">8,064</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">8,064</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">6,825</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">6,825</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">5,586</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right"></td>
<td align="right">4,096</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right"></td>
<td align="right">4,096</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">4,032</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">4,032</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right"></td>
<td align="right">4,032</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">4,032</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right"></td>
<td align="right">4,032</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right"></td>
<td align="right">2,793</td>
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
<td align="right"></td>
<td align="right">66</td>
<td align="right"></td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-24
