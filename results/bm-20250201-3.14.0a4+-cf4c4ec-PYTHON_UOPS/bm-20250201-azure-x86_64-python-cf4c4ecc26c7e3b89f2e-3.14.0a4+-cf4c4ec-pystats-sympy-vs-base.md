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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">124,121,152</td>
<td align="right">2,418,153</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">16,016,973</td>
<td align="right">2,814,387</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,977,627</td>
<td align="right">2,069,570</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">23,421,678</td>
<td align="right">5,685,527</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">17,336,905</td>
<td align="right">4,577,677</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">48,517,939</td>
<td align="right">15,285,266</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,585,167</td>
<td align="right">883,648</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,989,612</td>
<td align="right">3,430,759</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,651,579</td>
<td align="right">33,572,716</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,071,850</td>
<td align="right">3,431,430</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">18,459,599</td>
<td align="right">8,255,145</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">10,995,257</td>
<td align="right">5,042,067</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,084,183</td>
<td align="right">5,165,324</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">36,628,296</td>
<td align="right">17,493,644</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">82,152,337</td>
<td align="right">41,937,652</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">83,661,726</td>
<td align="right">44,003,081</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">50,007,882</td>
<td align="right">26,507,451</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">30,461,573</td>
<td align="right">16,279,281</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,397,182</td>
<td align="right">5,035,657</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">3,325,022</td>
<td align="right">1,787,945</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,029,774</td>
<td align="right">2,201,685</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">27,122,656</td>
<td align="right">15,268,538</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">6,241,954</td>
<td align="right">3,728,154</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">77,947,102</td>
<td align="right">50,286,811</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">24,072,699</td>
<td align="right">15,550,424</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,631,016</td>
<td align="right">12,106,529</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">23,125,067</td>
<td align="right">15,281,226</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">36,546,639</td>
<td align="right">24,436,384</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">18,314,252</td>
<td align="right">12,801,579</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">198,250,823</td>
<td align="right">140,976,705</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">280,950,851</td>
<td align="right">203,113,845</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">44,811,962</td>
<td align="right">32,836,214</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,270,099</td>
<td align="right">13,399,595</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">40,093,227</td>
<td align="right">29,764,188</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,727,229</td>
<td align="right">18,359,367</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">113,104,138</td>
<td align="right">84,990,826</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">53,185,219</td>
<td align="right">40,040,432</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,008,771</td>
<td align="right">1,521,604</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">25,914,534</td>
<td align="right">19,926,154</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">78,195,228</td>
<td align="right">60,247,450</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">52,783,387</td>
<td align="right">41,294,883</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">758,946,013</td>
<td align="right">597,570,396</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">26,730,482</td>
<td align="right">21,097,815</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">23,360,502</td>
<td align="right">18,588,560</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,306,411</td>
<td align="right">2,676,004</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,554,518</td>
<td align="right">61,474,510</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">211,588,075</td>
<td align="right">172,469,869</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">52,115,773</td>
<td align="right">43,365,249</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">71,942,433</td>
<td align="right">60,504,809</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">35,436,699</td>
<td align="right">30,244,776</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,409,564</td>
<td align="right">25,963,826</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">199,370,353</td>
<td align="right">171,192,174</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,002,457</td>
<td align="right">3,438,542</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">49,300,404</td>
<td align="right">42,390,245</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">12,709,459</td>
<td align="right">10,946,918</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">134,021,435</td>
<td align="right">115,460,047</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">64,253,990</td>
<td align="right">55,901,707</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">26,231,975</td>
<td align="right">23,224,960</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">178,797,861</td>
<td align="right">159,489,609</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">13,162,686</td>
<td align="right">11,876,914</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">115,530,890</td>
<td align="right">104,342,366</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">33,147,200</td>
<td align="right">30,304,351</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,787,226</td>
<td align="right">6,227,997</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,449,564</td>
<td align="right">16,040,588</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">19,077,475</td>
<td align="right">17,706,145</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">46,638,042</td>
<td align="right">43,428,317</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,695,810</td>
<td align="right">20,334,938</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">37,176,780</td>
<td align="right">34,875,565</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,942,736</td>
<td align="right">16,036,164</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,694,376</td>
<td align="right">3,550,037</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,811,471</td>
<td align="right">1,758,528</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,831,731</td>
<td align="right">6,641,698</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,190,455</td>
<td align="right">26,537,683</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,714,014</td>
<td align="right">4,609,543</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,778,172</td>
<td align="right">9,938,753</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">47,124,159</td>
<td align="right">46,437,079</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">461,742</td>
<td align="right">456,447</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,617,206</td>
<td align="right">2,587,942</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,742,479</td>
<td align="right">15,566,545</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,985,530</td>
<td align="right">21,740,022</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9,055</td>
<td align="right">8,971</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,654,754</td>
<td align="right">17,806,442</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,614,347</td>
<td align="right">4,587,455</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,984,191</td>
<td align="right">15,908,992</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,964</td>
<td align="right">2,951</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,541,483</td>
<td align="right">7,516,675</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,346</td>
<td align="right">40,222</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,949</td>
<td align="right">10,924</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,908,953</td>
<td align="right">17,882,954</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,035</td>
<td align="right">18,055</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">916</td>
<td align="right">917</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">16,989</td>
<td align="right">17,007</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,697</td>
<td align="right">165,547</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,905,148</td>
<td align="right">97,992,505</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">493,712</td>
<td align="right">493,330</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,443</td>
<td align="right">1,444</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,350</td>
<td align="right">175,263</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,389</td>
<td align="right">655,077</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,389</td>
<td align="right">655,077</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,389</td>
<td align="right">655,077</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,235</td>
<td align="right">1,287,626</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,133</td>
<td align="right">83,095</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">147,497</td>
<td align="right">147,552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">20,696</td>
<td align="right">20,690</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">78,683</td>
<td align="right">78,661</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">182,050,986</td>
<td align="right">182,101,442</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">745,062</td>
<td align="right">744,866</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,889</td>
<td align="right">1,389,579</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,623,306</td>
<td align="right">6,621,919</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,590,428</td>
<td align="right">6,589,093</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,753,768</td>
<td align="right">5,752,653</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,028,566</td>
<td align="right">1,028,376</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,029,162</td>
<td align="right">1,028,972</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,966,427</td>
<td align="right">1,966,099</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,835</td>
<td align="right">389,878</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,024,984</td>
<td align="right">6,024,485</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,163</td>
<td align="right">24,165</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,650</td>
<td align="right">942,573</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,569</td>
<td align="right">4,497,212</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,418</td>
<td align="right">4,469,095</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,917,178</td>
<td align="right">10,916,473</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,405</td>
<td align="right">141,396</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,222,749</td>
<td align="right">1,222,821</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,252</td>
<td align="right">746,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,909</td>
<td align="right">745,873</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,722</td>
<td align="right">4,181,549</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,570</td>
<td align="right">21,976,772</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">171,837</td>
<td align="right">171,843</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">597,628</td>
<td align="right">597,608</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,144</td>
<td align="right">2,195,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,199</td>
<td align="right">2,281,137</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,460</td>
<td align="right">1,754,429</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,357</td>
<td align="right">6,744,265</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,533</td>
<td align="right">1,244,517</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,174</td>
<td align="right">1,323,157</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,382</td>
<td align="right">654,375</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,398</td>
<td align="right">654,391</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,532</td>
<td align="right">427,529</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,036,043</td>
<td align="right">1,036,043</td>
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
<td align="right">339,309</td>
<td align="right">339,309</td>
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
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">69,373,386</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">18,669,344</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">1,416,644</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,081,609</td>
<td align="right">35.6%</td>
<td align="right">8,469,290</td>
<td align="right">24.2%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,167,405</td>
<td align="right">64.2%</td>
<td align="right">26,514,846</td>
<td align="right">75.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,769</td>
<td align="right">0.1%</td>
<td align="right">50,032</td>
<td align="right">0.1%</td>
<td align="right">0.5%</td>
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
<td align="right">21,738</td>
<td align="right">90.6%</td>
<td align="right">21,526</td>
<td align="right">90.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,258</td>
<td align="right">9.4%</td>
<td align="right">2,258</td>
<td align="right">9.5%</td>
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
<td align="left">multiply different types</td>
<td align="right">2,353</td>
<td align="right">10.8%</td>
<td align="right">2,226</td>
<td align="right">10.3%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">738</td>
<td align="right">3.4%</td>
<td align="right">716</td>
<td align="right">3.3%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">577</td>
<td align="right">2.7%</td>
<td align="right">565</td>
<td align="right">2.6%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">213</td>
<td align="right">1.0%</td>
<td align="right">211</td>
<td align="right">1.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,217</td>
<td align="right">5.6%</td>
<td align="right">1,209</td>
<td align="right">5.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,905</td>
<td align="right">18.0%</td>
<td align="right">3,880</td>
<td align="right">18.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">706</td>
<td align="right">3.2%</td>
<td align="right">702</td>
<td align="right">3.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,908</td>
<td align="right">13.4%</td>
<td align="right">2,892</td>
<td align="right">13.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">999</td>
<td align="right">4.6%</td>
<td align="right">1,003</td>
<td align="right">4.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">14.8%</td>
<td align="right">3,221</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">10.2%</td>
<td align="right">2,225</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,085</td>
<td align="right">5.0%</td>
<td align="right">1,085</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">4.5%</td>
<td align="right">982</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.7%</td>
<td align="right">363</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.7%</td>
<td align="right">155</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.4%</td>
<td align="right">91</td>
<td align="right">0.4%</td>
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
<td align="right">18,451,137</td>
<td align="right">36.0%</td>
<td align="right">8,249,163</td>
<td align="right">22.8%</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,733,461</td>
<td align="right">63.9%</td>
<td align="right">27,932,159</td>
<td align="right">77.2%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,755</td>
<td align="right">0.0%</td>
<td align="right">10,753</td>
<td align="right">0.0%</td>
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
<td align="right">7,680</td>
<td align="right">88.7%</td>
<td align="right">5,200</td>
<td align="right">84.1%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">982</td>
<td align="right">11.3%</td>
<td align="right">982</td>
<td align="right">15.9%</td>
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
<td align="right">6,149</td>
<td align="right">80.1%</td>
<td align="right">3,669</td>
<td align="right">70.6%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">273</td>
<td align="right">3.6%</td>
<td align="right">272</td>
<td align="right">5.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">687</td>
<td align="right">8.9%</td>
<td align="right">688</td>
<td align="right">13.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">5.5%</td>
<td align="right">422</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">148</td>
<td align="right">1.9%</td>
<td align="right">148</td>
<td align="right">2.8%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">295,900,880</td>
<td align="right">92.3%</td>
<td align="right">233,372,974</td>
<td align="right">90.4%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,767,241</td>
<td align="right">7.7%</td>
<td align="right">24,884,737</td>
<td align="right">9.6%</td>
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
<td align="right">8,439</td>
<td align="right">0.0%</td>
<td align="right">8,426</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">482,876</td>
<td align="right">100.0%</td>
<td align="right">485,115</td>
<td align="right">100.0%</td>
<td align="right">0.5%</td>
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
<td align="right">1,065</td>
<td align="right">100.0%</td>
<td align="right">1,066</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,028,338</td>
<td align="right">62.3%</td>
<td align="right">40,698,538</td>
<td align="right">60.7%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30,370,959</td>
<td align="right">37.1%</td>
<td align="right">25,926,337</td>
<td align="right">38.7%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">409,599</td>
<td align="right">0.5%</td>
<td align="right">409,652</td>
<td align="right">0.6%</td>
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
<td align="right">37,443</td>
<td align="right">80.9%</td>
<td align="right">36,324</td>
<td align="right">80.4%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,835</td>
<td align="right">19.1%</td>
<td align="right">8,838</td>
<td align="right">19.6%</td>
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
<td align="left">bool</td>
<td align="right">1,443</td>
<td align="right">3.9%</td>
<td align="right">407</td>
<td align="right">1.1%</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,474</td>
<td align="right">17.3%</td>
<td align="right">6,393</td>
<td align="right">17.6%</td>
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
<td align="right">3,139</td>
<td align="right">8.4%</td>
<td align="right">3,157</td>
<td align="right">8.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,114</td>
<td align="right">37.7%</td>
<td align="right">14,098</td>
<td align="right">38.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,268</td>
<td align="right">11.4%</td>
<td align="right">4,266</td>
<td align="right">11.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">20.0%</td>
<td align="right">7,480</td>
<td align="right">20.6%</td>
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
<td align="right">0.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,341</td>
<td align="right">57.5%</td>
<td align="right">5,763,168</td>
<td align="right">55.7%</td>
<td align="right">-75.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,329,849</td>
<td align="right">42.4%</td>
<td align="right">4,573,741</td>
<td align="right">44.2%</td>
<td align="right">-73.6%</td>
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
<td align="right">6,934</td>
<td align="right">98.3%</td>
<td align="right">3,814</td>
<td align="right">96.9%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">122</td>
<td align="right">1.7%</td>
<td align="right">122</td>
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
<td align="left">other</td>
<td align="right">5,024</td>
<td align="right">72.5%</td>
<td align="right">1,907</td>
<td align="right">50.0%</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,474</td>
<td align="right">21.3%</td>
<td align="right">1,471</td>
<td align="right">38.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">4.3%</td>
<td align="right">299</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">137</td>
<td align="right">2.0%</td>
<td align="right">137</td>
<td align="right">3.6%</td>
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
<td align="right">83,536,767</td>
<td align="right">50.2%</td>
<td align="right">31,988,343</td>
<td align="right">48.2%</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">81,591,865</td>
<td align="right">49.0%</td>
<td align="right">33,519,124</td>
<td align="right">50.5%</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,228,952</td>
<td align="right">0.7%</td>
<td align="right">782,583</td>
<td align="right">1.2%</td>
<td align="right">-36.3%</td>
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
<td align="right">23,814</td>
<td align="right">28.8%</td>
<td align="right">15,378</td>
<td align="right">22.5%</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,009</td>
<td align="right">71.2%</td>
<td align="right">52,898</td>
<td align="right">77.5%</td>
<td align="right">-10.4%</td>
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
<td align="left">set</td>
<td align="right">6,333</td>
<td align="right">10.7%</td>
<td align="right">2,866</td>
<td align="right">5.4%</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,200</td>
<td align="right">7.1%</td>
<td align="right">2,709</td>
<td align="right">5.1%</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">45,146</td>
<td align="right">76.5%</td>
<td align="right">43,998</td>
<td align="right">83.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,336</td>
<td align="right">2.3%</td>
<td align="right">1,332</td>
<td align="right">2.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">558</td>
<td align="right">0.9%</td>
<td align="right">557</td>
<td align="right">1.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.3%</td>
<td align="right">758</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.6%</td>
<td align="right">382</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.4%</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.0%</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">24</td>
<td align="right">0.0%</td>
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
<td align="right">78,130,485</td>
<td align="right">22.8%</td>
<td align="right">60,187,103</td>
<td align="right">22.0%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">211,753,914</td>
<td align="right">61.7%</td>
<td align="right">170,113,873</td>
<td align="right">62.2%</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,297,987</td>
<td align="right">15.5%</td>
<td align="right">43,123,819</td>
<td align="right">15.8%</td>
<td align="right">-19.1%</td>
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
<td align="right">1,016,385</td>
<td align="right">95.3%</td>
<td align="right">824,390</td>
<td align="right">94.8%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">49,579</td>
<td align="right">4.7%</td>
<td align="right">45,185</td>
<td align="right">5.2%</td>
<td align="right">-8.9%</td>
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
<td align="right">568</td>
<td align="right">1.1%</td>
<td align="right">242</td>
<td align="right">0.5%</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,551</td>
<td align="right">9.2%</td>
<td align="right">3,004</td>
<td align="right">6.6%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,361</td>
<td align="right">8.8%</td>
<td align="right">3,167</td>
<td align="right">7.0%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,684</td>
<td align="right">5.4%</td>
<td align="right">2,358</td>
<td align="right">5.2%</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">7,090</td>
<td align="right">14.3%</td>
<td align="right">6,812</td>
<td align="right">15.1%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,867</td>
<td align="right">44.1%</td>
<td align="right">21,163</td>
<td align="right">46.8%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,107</td>
<td align="right">6.3%</td>
<td align="right">3,093</td>
<td align="right">6.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,072</td>
<td align="right">8.2%</td>
<td align="right">4,068</td>
<td align="right">9.0%</td>
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
<td align="right">291,900,689</td>
<td align="right">100.0%</td>
<td align="right">244,479,137</td>
<td align="right">100.0%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,310</td>
<td align="right">0.0%</td>
<td align="right">1,298</td>
<td align="right">0.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,531</td>
<td align="right">0.0%</td>
<td align="right">4,522</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">13,554</td>
<td align="right">100.0%</td>
<td align="right">13,583</td>
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
<td align="right">2,265,824</td>
<td align="right">100.0%</td>
<td align="right">2,265,730</td>
<td align="right">100.0%</td>
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
<td align="right">731,541</td>
<td align="right">72.0%</td>
<td align="right">731,584</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">174,042</td>
<td align="right">1.9%</td>
<td align="right">173,952</td>
<td align="right">1.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,575,908</td>
<td align="right">17.4%</td>
<td align="right">1,575,339</td>
<td align="right">17.4%</td>
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
<td align="right">7,328,597</td>
<td align="right">80.7%</td>
<td align="right">7,327,717</td>
<td align="right">80.7%</td>
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
<td align="right">972</td>
<td align="right">3.1%</td>
<td align="right">975</td>
<td align="right">3.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">29,987</td>
<td align="right">96.9%</td>
<td align="right">29,973</td>
<td align="right">96.8%</td>
<td align="right">-0.0%</td>
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
<td align="right">294</td>
<td align="right">30.2%</td>
<td align="right">296</td>
<td align="right">30.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.3%</td>
<td align="right">518</td>
<td align="right">53.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">102</td>
<td align="right">10.5%</td>
<td align="right">102</td>
<td align="right">10.5%</td>
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
<td align="right">2,583,048</td>
<td align="right">12.7%</td>
<td align="right">881,936</td>
<td align="right">4.8%</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,738,651</td>
<td align="right">87.3%</td>
<td align="right">17,663,421</td>
<td align="right">95.2%</td>
<td align="right">-0.4%</td>
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
<td align="right">1,543</td>
<td align="right">72.8%</td>
<td align="right">1,136</td>
<td align="right">66.4%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">576</td>
<td align="right">27.2%</td>
<td align="right">576</td>
<td align="right">33.6%</td>
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
<td align="right">1,543</td>
<td align="right">100.0%</td>
<td align="right">1,136</td>
<td align="right">100.0%</td>
<td align="right">-26.4%</td>
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
<td align="right">596,729</td>
<td align="right">0.4%</td>
<td align="right">442,580</td>
<td align="right">0.3%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">153,542,840</td>
<td align="right">93.7%</td>
<td align="right">134,472,183</td>
<td align="right">92.8%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,756,274</td>
<td align="right">6.0%</td>
<td align="right">9,919,314</td>
<td align="right">6.8%</td>
<td align="right">1.7%</td>
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
<td align="right">14,275</td>
<td align="right">43.8%</td>
<td align="right">11,793</td>
<td align="right">43.3%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,340</td>
<td align="right">56.2%</td>
<td align="right">15,454</td>
<td align="right">56.7%</td>
<td align="right">-15.7%</td>
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
<td align="right">2,593</td>
<td align="right">18.2%</td>
<td align="right">1,880</td>
<td align="right">15.9%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,018</td>
<td align="right">56.2%</td>
<td align="right">6,234</td>
<td align="right">52.9%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">721</td>
<td align="right">5.1%</td>
<td align="right">728</td>
<td align="right">6.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,253</td>
<td align="right">8.8%</td>
<td align="right">1,265</td>
<td align="right">10.7%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">721</td>
<td align="right">5.1%</td>
<td align="right">717</td>
<td align="right">6.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">6.2%</td>
<td align="right">883</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.6%</td>
<td align="right">84</td>
<td align="right">0.7%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,581,977</td>
<td align="right">100.0%</td>
<td align="right">43,366,674</td>
<td align="right">100.0%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,361</td>
<td align="right">0.0%</td>
<td align="right">6,276</td>
<td align="right">0.0%</td>
<td align="right">-1.3%</td>
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
<td align="right">302</td>
<td align="right">11.2%</td>
<td align="right">303</td>
<td align="right">11.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,392</td>
<td align="right">88.8%</td>
<td align="right">2,392</td>
<td align="right">88.8%</td>
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
<td align="right">259</td>
<td align="right">85.8%</td>
<td align="right">260</td>
<td align="right">85.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.2%</td>
<td align="right">43</td>
<td align="right">14.2%</td>
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
<td align="right">266,114,320</td>
<td align="right">5.6%</td>
<td align="right">170,484,401</td>
<td align="right">4.6%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,746,716,451</td>
<td align="right">37.0%</td>
<td align="right">1,300,874,739</td>
<td align="right">35.3%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,628,718,974</td>
<td align="right">55.7%</td>
<td align="right">2,138,411,439</td>
<td align="right">58.1%</td>
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
<td align="right">81,956,786</td>
<td align="right">1.7%</td>
<td align="right">71,299,664</td>
<td align="right">1.9%</td>
<td align="right">-13.0%</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">17,329,849</td>
<td align="right">6.5%</td>
<td align="right">4,573,741</td>
<td align="right">2.7%</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,583,048</td>
<td align="right">1.0%</td>
<td align="right">881,936</td>
<td align="right">0.5%</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,591,865</td>
<td align="right">30.7%</td>
<td align="right">33,519,124</td>
<td align="right">19.7%</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">18,451,137</td>
<td align="right">6.9%</td>
<td align="right">8,249,163</td>
<td align="right">4.8%</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">78,130,485</td>
<td align="right">29.4%</td>
<td align="right">60,187,103</td>
<td align="right">35.4%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,370,959</td>
<td align="right">11.4%</td>
<td align="right">25,926,337</td>
<td align="right">15.2%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,167,405</td>
<td align="right">10.2%</td>
<td align="right">26,514,846</td>
<td align="right">15.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,756,274</td>
<td align="right">3.7%</td>
<td align="right">9,919,314</td>
<td align="right">5.8%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">174,042</td>
<td align="right">0.1%</td>
<td align="right">173,952</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">29,016,929</td>
<td align="right">35.4%</td>
<td align="right">20,575,823</td>
<td align="right">28.9%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">621,951</td>
<td align="right">0.8%</td>
<td align="right">542,481</td>
<td align="right">0.8%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">13,348,384</td>
<td align="right">16.3%</td>
<td align="right">11,807,806</td>
<td align="right">16.6%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,312,277</td>
<td align="right">8.9%</td>
<td align="right">7,157,371</td>
<td align="right">10.0%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,303,780</td>
<td align="right">13.8%</td>
<td align="right">11,458,570</td>
<td align="right">16.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,202,680</td>
<td align="right">3.9%</td>
<td align="right">3,164,413</td>
<td align="right">4.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,149,775</td>
<td align="right">7.5%</td>
<td align="right">6,112,672</td>
<td align="right">8.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,575,129</td>
<td align="right">1.9%</td>
<td align="right">1,574,560</td>
<td align="right">2.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,446</td>
<td align="right">6.2%</td>
<td align="right">5,102,525</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,581</td>
<td align="right">2.6%</td>
<td align="right">2,103,572</td>
<td align="right">3.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">22,377,854</td>
<td align="right">10.6%</td>
<td align="right">22,528,739</td>
<td align="right">10.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,396,948</td>
<td align="right">19.7%</td>
<td align="right">41,334,303</td>
<td align="right">19.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,397,938</td>
<td align="right">53.4%</td>
<td align="right">112,510,357</td>
<td align="right">53.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">98,059,562</td>
<td align="right">46.6%</td>
<td align="right">98,146,919</td>
<td align="right">46.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">98,059,562</td>
<td align="right">46.6%</td>
<td align="right">98,146,919</td>
<td align="right">46.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,680,923</td>
<td align="right">36.0%</td>
<td align="right">75,617,395</td>
<td align="right">35.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,681,708</td>
<td align="right">36.0%</td>
<td align="right">75,618,180</td>
<td align="right">35.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,846,637</td>
<td align="right">89.3%</td>
<td align="right">187,895,423</td>
<td align="right">89.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,366</td>
<td align="right">0.5%</td>
<td align="right">950,149</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,537</td>
<td align="right">8.8%</td>
<td align="right">18,490,116</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,332,161</td>
<td align="right">4.4%</td>
<td align="right">9,331,951</td>
<td align="right">4.4%</td>
<td align="right">-0.0%</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">921,723</td>
<td align="right"></td>
<td align="right">1,556,674</td>
<td align="right"></td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,044,927</td>
<td align="right"></td>
<td align="right">4,778,864</td>
<td align="right"></td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,124,423</td>
<td align="right"></td>
<td align="right">3,223,446</td>
<td align="right"></td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">843,737,052</td>
<td align="right">15.4%</td>
<td align="right">915,064,606</td>
<td align="right">16.1%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,994,250,462</td>
<td align="right">42.5%</td>
<td align="right">2,138,831,966</td>
<td align="right">44.5%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">158,129,048</td>
<td align="right"></td>
<td align="right">146,841,891</td>
<td align="right"></td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,324,761,246</td>
<td align="right">42.3%</td>
<td align="right">2,454,665,746</td>
<td align="right">43.2%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">995,248,030</td>
<td align="right">21.2%</td>
<td align="right">982,904,658</td>
<td align="right">20.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">756,579</td>
<td align="right">0.1%</td>
<td align="right">765,691</td>
<td align="right">0.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,803</td>
<td align="right">0.0%</td>
<td align="right">8,903</td>
<td align="right">0.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,120,229,018</td>
<td align="right">23.9%</td>
<td align="right">1,108,321,232</td>
<td align="right">23.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,078,832,870</td>
<td align="right">19.6%</td>
<td align="right">1,071,327,847</td>
<td align="right">18.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">578,957,843</td>
<td align="right">12.3%</td>
<td align="right">581,582,230</td>
<td align="right">12.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,244,091,427</td>
<td align="right">22.7%</td>
<td align="right">1,246,863,591</td>
<td align="right">21.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">265,253,287</td>
<td align="right"></td>
<td align="right">264,784,434</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,271</td>
<td align="right"></td>
<td align="right">866,178</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">173,976,264</td>
<td align="right">33.8%</td>
<td align="right">173,969,562</td>
<td align="right">33.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">339,778,562</td>
<td align="right">66.0%</td>
<td align="right">339,783,474</td>
<td align="right">66.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">339,813,203</td>
<td align="right"></td>
<td align="right">339,818,115</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">174,741,646</td>
<td align="right">34.0%</td>
<td align="right">174,744,156</td>
<td align="right">34.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">187,386,164</td>
<td align="right"></td>
<td align="right">187,387,628</td>
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
Stats gathered on: 2025-02-03
