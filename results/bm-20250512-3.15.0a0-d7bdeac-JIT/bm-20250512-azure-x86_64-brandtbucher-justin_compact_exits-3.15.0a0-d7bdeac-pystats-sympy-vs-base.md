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
<td align="left">NOT_TAKEN</td>
<td align="right">245,126</td>
<td align="right">283,405</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,569,784</td>
<td align="right">9,760,596</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">42,380,791</td>
<td align="right">41,547,366</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,508,104</td>
<td align="right">5,401,489</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">15,116,537</td>
<td align="right">15,387,969</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">61</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,349,340</td>
<td align="right">9,490,756</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">56,878,473</td>
<td align="right">56,102,355</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,953</td>
<td align="right">2,991</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9,067</td>
<td align="right">8,987</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">30,009,622</td>
<td align="right">29,744,909</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,043</td>
<td align="right">18,185</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">41,577,152</td>
<td align="right">41,872,873</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">998</td>
<td align="right">1,005</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">44,468,466</td>
<td align="right">44,777,031</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">44,379,598</td>
<td align="right">44,108,666</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">172,301,320</td>
<td align="right">171,486,942</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">10,800,754</td>
<td align="right">10,851,642</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">22,419,746</td>
<td align="right">22,315,002</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">23,781</td>
<td align="right">23,887</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">67,271,473</td>
<td align="right">67,552,606</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,614</td>
<td align="right">40,486</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">51,305,718</td>
<td align="right">51,457,409</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">28,446,571</td>
<td align="right">28,529,547</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">34,148,620</td>
<td align="right">34,247,546</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,084</td>
<td align="right">11,114</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">57,188,311</td>
<td align="right">57,045,933</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">53,809,249</td>
<td align="right">53,937,660</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">172,085,662</td>
<td align="right">172,482,635</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">143,421,449</td>
<td align="right">143,111,968</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,544,389</td>
<td align="right">17,507,825</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">53,019,957</td>
<td align="right">53,124,813</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">55,123,554</td>
<td align="right">55,228,859</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">18,945,574</td>
<td align="right">18,909,447</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">56,634,016</td>
<td align="right">56,739,323</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">7,915,506</td>
<td align="right">7,926,928</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">8,079,262</td>
<td align="right">8,090,684</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,444</td>
<td align="right">1,446</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,792,146</td>
<td align="right">17,768,144</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">123,401,596</td>
<td align="right">123,549,840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,223,691</td>
<td align="right">1,222,239</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">9,564,883</td>
<td align="right">9,576,067</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">9,653,890</td>
<td align="right">9,665,121</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">642,851,822</td>
<td align="right">643,511,007</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,465,902</td>
<td align="right">11,477,243</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,409,572</td>
<td align="right">12,421,087</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">38,679,416</td>
<td align="right">38,713,531</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">45,501,699</td>
<td align="right">45,536,562</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">181,760,227</td>
<td align="right">181,896,060</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">744,592</td>
<td align="right">745,122</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">220,107,415</td>
<td align="right">220,261,397</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">17,483,300</td>
<td align="right">17,495,423</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">13,942,200</td>
<td align="right">13,932,718</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">43,217,990</td>
<td align="right">43,192,488</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,369</td>
<td align="right">175,277</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">198,969,075</td>
<td align="right">199,068,310</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,136</td>
<td align="right">83,096</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">23,241,377</td>
<td align="right">23,252,529</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">50,956,301</td>
<td align="right">50,979,503</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,735,296</td>
<td align="right">24,745,918</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">24,483,092</td>
<td align="right">24,493,209</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">239,240,398</td>
<td align="right">239,142,852</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">20,698</td>
<td align="right">20,690</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,475</td>
<td align="right">655,231</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,475</td>
<td align="right">655,231</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,475</td>
<td align="right">655,231</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">78,942</td>
<td align="right">78,918</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">14,950,129</td>
<td align="right">14,954,382</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">48,039,025</td>
<td align="right">48,025,677</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,555,593</td>
<td align="right">1,555,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,585,819</td>
<td align="right">1,585,470</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">13,242,348</td>
<td align="right">13,239,481</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">85,952,030</td>
<td align="right">85,934,085</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">172,008</td>
<td align="right">172,042</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,029,195</td>
<td align="right">1,029,010</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,030,086</td>
<td align="right">1,029,901</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,658,775</td>
<td align="right">21,655,807</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">31,306,362</td>
<td align="right">31,302,087</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">456,568</td>
<td align="right">456,510</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,989</td>
<td align="right">4,497,439</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,556</td>
<td align="right">654,476</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,007,787</td>
<td align="right">2,007,548</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">17,983,016</td>
<td align="right">17,980,886</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,572</td>
<td align="right">654,496</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,590,486</td>
<td align="right">6,589,750</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,868</td>
<td align="right">1,389,726</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,753,770</td>
<td align="right">5,753,191</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">36,967,093</td>
<td align="right">36,963,587</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,711</td>
<td align="right">2,281,519</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,623,241</td>
<td align="right">6,622,712</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,002,015</td>
<td align="right">4,001,697</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,418,528</td>
<td align="right">2,418,346</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,891,418</td>
<td align="right">59,887,288</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,813,597</td>
<td align="right">6,813,154</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,667</td>
<td align="right">942,606</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,585,432</td>
<td align="right">2,585,265</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">2,995,113</td>
<td align="right">2,995,299</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,931</td>
<td align="right">389,907</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,262,139</td>
<td align="right">75,257,716</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,414</td>
<td align="right">141,406</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">24,793,729</td>
<td align="right">24,792,382</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,541,770</td>
<td align="right">7,541,379</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">78,744,708</td>
<td align="right">78,741,214</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,618,141</td>
<td align="right">2,618,034</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,588,670</td>
<td align="right">2,588,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">32,100,838</td>
<td align="right">32,099,564</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">33,139,430</td>
<td align="right">33,138,115</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,711,386</td>
<td align="right">21,710,554</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,038,896</td>
<td align="right">11,038,479</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,921,207</td>
<td align="right">10,920,835</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,348</td>
<td align="right">746,324</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,767</td>
<td align="right">21,977,074</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">10,871,229</td>
<td align="right">10,871,569</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,026,457</td>
<td align="right">6,026,272</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,282,834</td>
<td align="right">5,282,675</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,900,578</td>
<td align="right">9,900,282</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,933,965</td>
<td align="right">8,933,701</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,913,591</td>
<td align="right">15,913,133</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,119</td>
<td align="right">2,195,179</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">49,109,734</td>
<td align="right">49,108,466</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,163,082</td>
<td align="right">18,162,618</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">598,550</td>
<td align="right">598,535</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,632,791</td>
<td align="right">18,632,336</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">495,135</td>
<td align="right">495,147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,645</td>
<td align="right">165,649</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,752</td>
<td align="right">4,181,655</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,586,142</td>
<td align="right">4,586,038</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,408</td>
<td align="right">6,744,257</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,008,636</td>
<td align="right">2,008,676</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">21,006,263</td>
<td align="right">21,005,870</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,985,928</td>
<td align="right">21,985,539</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,778,017</td>
<td align="right">9,777,861</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,510</td>
<td align="right">4,469,440</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,544</td>
<td align="right">1,754,519</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,728,277</td>
<td align="right">3,728,227</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,534</td>
<td align="right">1,244,518</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,758,906</td>
<td align="right">1,758,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,036</td>
<td align="right">1,288,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">746,001</td>
<td align="right">745,994</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">15,881,625</td>
<td align="right">15,881,504</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,322</td>
<td align="right">1,323,319</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,786,187</td>
<td align="right">6,786,176</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,567,790</td>
<td align="right">15,567,809</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,036,043</td>
<td align="right">1,036,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,543</td>
<td align="right">427,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">388,827</td>
<td align="right">388,827</td>
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
<td align="right">341,720</td>
<td align="right">341,720</td>
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
<td align="right">178,534</td>
<td align="right">178,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">178,532</td>
<td align="right">178,532</td>
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
<td align="right">89,009</td>
<td align="right">89,009</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">14,629</td>
<td align="right">14,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,037</td>
<td align="right">12,037</td>
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
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">7,111</td>
<td align="right">7,111</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,550</td>
<td align="right">5,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">4,150</td>
<td align="right">4,150</td>
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
<td align="left">BUILD_SLICE</td>
<td align="right">200</td>
<td align="right">200</td>
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
<td align="right">44,437,481</td>
<td align="right">38.4%</td>
<td align="right">44,745,940</td>
<td align="right">38.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">60,333</td>
<td align="right">0.1%</td>
<td align="right">60,643</td>
<td align="right">0.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">71,200,834</td>
<td align="right">61.5%</td>
<td align="right">71,222,863</td>
<td align="right">61.4%</td>
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
<td align="right">3,267</td>
<td align="right">10.2%</td>
<td align="right">3,315</td>
<td align="right">10.3%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">28,858</td>
<td align="right">89.8%</td>
<td align="right">28,920</td>
<td align="right">89.7%</td>
<td align="right">0.2%</td>
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
<td align="left">and other</td>
<td align="right">216</td>
<td align="right">0.7%</td>
<td align="right">211</td>
<td align="right">0.7%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,019</td>
<td align="right">3.5%</td>
<td align="right">1,001</td>
<td align="right">3.5%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">4,519</td>
<td align="right">15.7%</td>
<td align="right">4,593</td>
<td align="right">15.9%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">1,756</td>
<td align="right">6.1%</td>
<td align="right">1,779</td>
<td align="right">6.2%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.3%</td>
<td align="right">367</td>
<td align="right">1.3%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">92</td>
<td align="right">0.3%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,939</td>
<td align="right">13.6%</td>
<td align="right">3,904</td>
<td align="right">13.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">3.4%</td>
<td align="right">989</td>
<td align="right">3.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">573</td>
<td align="right">2.0%</td>
<td align="right">569</td>
<td align="right">2.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,208</td>
<td align="right">4.2%</td>
<td align="right">1,215</td>
<td align="right">4.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">624</td>
<td align="right">2.2%</td>
<td align="right">626</td>
<td align="right">2.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">703</td>
<td align="right">2.4%</td>
<td align="right">705</td>
<td align="right">2.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,897</td>
<td align="right">10.0%</td>
<td align="right">2,900</td>
<td align="right">10.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">11.2%</td>
<td align="right">3,221</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">7.7%</td>
<td align="right">2,225</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,142</td>
<td align="right">7.4%</td>
<td align="right">2,142</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">3.8%</td>
<td align="right">1,086</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">716</td>
<td align="right">2.5%</td>
<td align="right">716</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">1.5%</td>
<td align="right">422</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.5%</td>
<td align="right">155</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">12,037</td>
<td align="right">100.0%</td>
<td align="right">12,037</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">36,360,323</td>
<td align="right">11.6%</td>
<td align="right">36,314,721</td>
<td align="right">11.6%</td>
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
<td align="right">35,682,787</td>
<td align="right">11.4%</td>
<td align="right">35,638,114</td>
<td align="right">11.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">276,280,435</td>
<td align="right">88.4%</td>
<td align="right">276,438,567</td>
<td align="right">88.4%</td>
<td align="right">0.1%</td>
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
<td align="right">701,317</td>
<td align="right">100.0%</td>
<td align="right">700,494</td>
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
<td align="right">3,183</td>
<td align="right">74.9%</td>
<td align="right">3,185</td>
<td align="right">74.9%</td>
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
<td align="right">1,066</td>
<td align="right">100.0%</td>
<td align="right">1,066</td>
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
<td align="right">29,971,115</td>
<td align="right">36.8%</td>
<td align="right">29,706,449</td>
<td align="right">36.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">409,680</td>
<td align="right">0.5%</td>
<td align="right">410,752</td>
<td align="right">0.5%</td>
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
<td align="right">51,039,199</td>
<td align="right">62.7%</td>
<td align="right">51,030,366</td>
<td align="right">62.9%</td>
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
<td align="left">Success</td>
<td align="right">8,833</td>
<td align="right">19.1%</td>
<td align="right">8,861</td>
<td align="right">19.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">37,347</td>
<td align="right">80.9%</td>
<td align="right">37,292</td>
<td align="right">80.8%</td>
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
<td align="left">bool</td>
<td align="right">1,432</td>
<td align="right">3.8%</td>
<td align="right">1,465</td>
<td align="right">3.9%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,391</td>
<td align="right">17.1%</td>
<td align="right">6,282</td>
<td align="right">16.8%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">115</td>
<td align="right">0.3%</td>
<td align="right">114</td>
<td align="right">0.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,267</td>
<td align="right">11.4%</td>
<td align="right">4,247</td>
<td align="right">11.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,098</td>
<td align="right">37.7%</td>
<td align="right">14,135</td>
<td align="right">37.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,156</td>
<td align="right">8.5%</td>
<td align="right">3,161</td>
<td align="right">8.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">20.0%</td>
<td align="right">7,480</td>
<td align="right">20.1%</td>
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
<td align="left">set</td>
<td align="right">135</td>
<td align="right">0.4%</td>
<td align="right">135</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">91</td>
<td align="right">0.2%</td>
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
<td align="right">10,795,256</td>
<td align="right">31.5%</td>
<td align="right">10,846,133</td>
<td align="right">31.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,974</td>
<td align="right">68.5%</td>
<td align="right">23,500,022</td>
<td align="right">68.4%</td>
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
<td align="right">5,375</td>
<td align="right">97.8%</td>
<td align="right">5,386</td>
<td align="right">97.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">123</td>
<td align="right">2.2%</td>
<td align="right">123</td>
<td align="right">2.2%</td>
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
<td align="right">3,424</td>
<td align="right">63.7%</td>
<td align="right">3,433</td>
<td align="right">63.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,470</td>
<td align="right">27.3%</td>
<td align="right">1,472</td>
<td align="right">27.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">5.6%</td>
<td align="right">299</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">182</td>
<td align="right">3.4%</td>
<td align="right">182</td>
<td align="right">3.4%</td>
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
<td align="right">1,227,946</td>
<td align="right">1.1%</td>
<td align="right">1,235,203</td>
<td align="right">1.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,021,468</td>
<td align="right">57.8%</td>
<td align="right">63,877,329</td>
<td align="right">57.7%</td>
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
<td align="right">45,451,077</td>
<td align="right">41.0%</td>
<td align="right">45,485,605</td>
<td align="right">41.1%</td>
<td align="right">0.1%</td>
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
<td align="right">49,799</td>
<td align="right">67.6%</td>
<td align="right">50,126</td>
<td align="right">67.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">23,907</td>
<td align="right">32.4%</td>
<td align="right">24,053</td>
<td align="right">32.4%</td>
<td align="right">0.6%</td>
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
<td align="right">37,497</td>
<td align="right">75.3%</td>
<td align="right">37,807</td>
<td align="right">75.4%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,664</td>
<td align="right">5.3%</td>
<td align="right">2,644</td>
<td align="right">5.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,283</td>
<td align="right">12.6%</td>
<td align="right">6,326</td>
<td align="right">12.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,362</td>
<td align="right">2.7%</td>
<td align="right">1,356</td>
<td align="right">2.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.5%</td>
<td align="right">758</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">557</td>
<td align="right">1.1%</td>
<td align="right">557</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.8%</td>
<td align="right">382</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">243</td>
<td align="right">0.5%</td>
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
<td align="right">0.0%</td>
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
<td align="left">set</td>
<td align="right">7,164,552</td>
<td align="right">7,164,552 / 0 !!</td>
<td align="right">7,189,206</td>
<td align="right">7,189,206 / 0 !!</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">157,982</td>
<td align="right">157,982 / 0 !!</td>
<td align="right">157,918</td>
<td align="right">157,918 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">70,486</td>
<td align="right">70,486 / 0 !!</td>
<td align="right">70,479</td>
<td align="right">70,479 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,717,045</td>
<td align="right">8,717,045 / 0 !!</td>
<td align="right">8,716,305</td>
<td align="right">8,716,305 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">16,381,701</td>
<td align="right">16,381,701 / 0 !!</td>
<td align="right">16,381,251</td>
<td align="right">16,381,251 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,440,159</td>
<td align="right">9,440,159 / 0 !!</td>
<td align="right">9,440,065</td>
<td align="right">9,440,065 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,249,430</td>
<td align="right">12,249,430 / 0 !!</td>
<td align="right">12,249,322</td>
<td align="right">12,249,322 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6,028</td>
<td align="right">6,028 / 0 !!</td>
<td align="right">6,028</td>
<td align="right">6,028 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">443</td>
<td align="right">443 / 0 !!</td>
<td align="right">443</td>
<td align="right">443 / 0 !!</td>
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
<td align="right">52,022,561</td>
<td align="right">15.5%</td>
<td align="right">51,830,048</td>
<td align="right">15.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">224,133,609</td>
<td align="right">66.7%</td>
<td align="right">224,426,694</td>
<td align="right">66.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">59,831,089</td>
<td align="right">17.8%</td>
<td align="right">59,827,006</td>
<td align="right">17.8%</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">992,408</td>
<td align="right">95.7%</td>
<td align="right">988,740</td>
<td align="right">95.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,105</td>
<td align="right">4.3%</td>
<td align="right">45,065</td>
<td align="right">4.4%</td>
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
<td align="left">class method obj</td>
<td align="right">4,079</td>
<td align="right">9.0%</td>
<td align="right">4,064</td>
<td align="right">9.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,105</td>
<td align="right">6.9%</td>
<td align="right">3,095</td>
<td align="right">6.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,117</td>
<td align="right">6.9%</td>
<td align="right">3,112</td>
<td align="right">6.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,746</td>
<td align="right">6.1%</td>
<td align="right">2,745</td>
<td align="right">6.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,435</td>
<td align="right">47.5%</td>
<td align="right">21,428</td>
<td align="right">47.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,815</td>
<td align="right">15.1%</td>
<td align="right">6,815</td>
<td align="right">15.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,324</td>
<td align="right">5.2%</td>
<td align="right">2,324</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">206</td>
<td align="right">0.5%</td>
<td align="right">206</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
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
<td align="right">4,518</td>
<td align="right">0.0%</td>
<td align="right">4,612</td>
<td align="right">0.0%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">259,689,941</td>
<td align="right">100.0%</td>
<td align="right">258,857,616</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,299</td>
<td align="right">0.0%</td>
<td align="right">1,299</td>
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
<td align="right">13,575</td>
<td align="right">100.0%</td>
<td align="right">13,623</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
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
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">31</td>
<td align="right">0.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,265,989</td>
<td align="right">100.0%</td>
<td align="right">2,265,925</td>
<td align="right">100.0%</td>
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
<td align="right">731,637</td>
<td align="right">72.0%</td>
<td align="right">731,613</td>
<td align="right">72.0%</td>
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
<td align="right">174,054</td>
<td align="right">1.9%</td>
<td align="right">173,966</td>
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
<td align="right">1,575,705</td>
<td align="right">17.4%</td>
<td align="right">1,575,209</td>
<td align="right">17.3%</td>
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
<td align="right">7,329,247</td>
<td align="right">80.7%</td>
<td align="right">7,329,022</td>
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
<td align="right">979</td>
<td align="right">3.2%</td>
<td align="right">975</td>
<td align="right">3.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">29,975</td>
<td align="right">96.8%</td>
<td align="right">29,981</td>
<td align="right">96.9%</td>
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
<td align="left">not managed dict</td>
<td align="right">302</td>
<td align="right">30.8%</td>
<td align="right">298</td>
<td align="right">30.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">52.9%</td>
<td align="right">518</td>
<td align="right">53.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">102</td>
<td align="right">10.4%</td>
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
<td align="right">2,583,313</td>
<td align="right">12.7%</td>
<td align="right">2,583,146</td>
<td align="right">12.7%</td>
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
<td align="right">17,741,487</td>
<td align="right">87.3%</td>
<td align="right">17,741,004</td>
<td align="right">87.3%</td>
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
<td align="left">Success</td>
<td align="right">576</td>
<td align="right">27.2%</td>
<td align="right">576</td>
<td align="right">27.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,543</td>
<td align="right">72.8%</td>
<td align="right">1,543</td>
<td align="right">72.8%</td>
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
<td align="right">1,543</td>
<td align="right">100.0%</td>
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
<td align="right">169,346,996</td>
<td align="right">94.2%</td>
<td align="right">169,319,231</td>
<td align="right">94.2%</td>
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
<td align="right">623,375</td>
<td align="right">0.3%</td>
<td align="right">623,360</td>
<td align="right">0.3%</td>
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
<td align="right">9,755,944</td>
<td align="right">5.4%</td>
<td align="right">9,755,790</td>
<td align="right">5.4%</td>
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
<td align="right">14,291</td>
<td align="right">43.0%</td>
<td align="right">14,285</td>
<td align="right">42.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,982</td>
<td align="right">57.0%</td>
<td align="right">18,988</td>
<td align="right">57.1%</td>
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
<td align="left">set</td>
<td align="right">732</td>
<td align="right">5.1%</td>
<td align="right">720</td>
<td align="right">5.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,255</td>
<td align="right">8.8%</td>
<td align="right">1,263</td>
<td align="right">8.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,612</td>
<td align="right">18.3%</td>
<td align="right">2,605</td>
<td align="right">18.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">726</td>
<td align="right">5.1%</td>
<td align="right">725</td>
<td align="right">5.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">7,997</td>
<td align="right">56.0%</td>
<td align="right">8,003</td>
<td align="right">56.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">6.2%</td>
<td align="right">883</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.6%</td>
<td align="right">84</td>
<td align="right">0.6%</td>
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
<td align="right">6,371</td>
<td align="right">0.0%</td>
<td align="right">6,291</td>
<td align="right">0.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,443,976</td>
<td align="right">100.0%</td>
<td align="right">83,561,574</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
<td align="right">305</td>
<td align="right">11.3%</td>
<td align="right">297</td>
<td align="right">11.0%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,391</td>
<td align="right">88.7%</td>
<td align="right">2,399</td>
<td align="right">89.0%</td>
<td align="right">0.3%</td>
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
<td align="right">262</td>
<td align="right">85.9%</td>
<td align="right">254</td>
<td align="right">85.5%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.1%</td>
<td align="right">43</td>
<td align="right">14.5%</td>
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
<td align="right">92,299,760</td>
<td align="right">2.2%</td>
<td align="right">92,069,774</td>
<td align="right">2.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,553,465,275</td>
<td align="right">36.4%</td>
<td align="right">1,551,927,924</td>
<td align="right">36.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">254,502,197</td>
<td align="right">6.0%</td>
<td align="right">254,650,628</td>
<td align="right">6.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,368,897,404</td>
<td align="right">55.5%</td>
<td align="right">2,369,744,450</td>
<td align="right">55.5%</td>
<td align="right">0.0%</td>
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
<td align="right">29,971,115</td>
<td align="right">12.5%</td>
<td align="right">29,706,449</td>
<td align="right">12.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">44,437,481</td>
<td align="right">18.6%</td>
<td align="right">44,745,940</td>
<td align="right">18.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">10,795,256</td>
<td align="right">4.5%</td>
<td align="right">10,846,133</td>
<td align="right">4.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,682,787</td>
<td align="right">14.9%</td>
<td align="right">35,638,114</td>
<td align="right">14.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">45,451,077</td>
<td align="right">19.0%</td>
<td align="right">45,485,605</td>
<td align="right">19.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">174,054</td>
<td align="right">0.1%</td>
<td align="right">173,966</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">59,831,089</td>
<td align="right">25.0%</td>
<td align="right">59,827,006</td>
<td align="right">25.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,583,313</td>
<td align="right">1.1%</td>
<td align="right">2,583,146</td>
<td align="right">1.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,755,944</td>
<td align="right">4.1%</td>
<td align="right">9,755,790</td>
<td align="right">4.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.1%</td>
<td align="right">268,986</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">12,163,091</td>
<td align="right">13.2%</td>
<td align="right">11,976,013</td>
<td align="right">13.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,190,567</td>
<td align="right">12.1%</td>
<td align="right">11,154,030</td>
<td align="right">12.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,707,076</td>
<td align="right">12.7%</td>
<td align="right">11,697,649</td>
<td align="right">12.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,574,926</td>
<td align="right">1.7%</td>
<td align="right">1,574,430</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,211,430</td>
<td align="right">3.5%</td>
<td align="right">3,211,023</td>
<td align="right">3.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,917,635</td>
<td align="right">31.3%</td>
<td align="right">28,914,341</td>
<td align="right">31.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,312,122</td>
<td align="right">7.9%</td>
<td align="right">7,311,635</td>
<td align="right">7.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,149,443</td>
<td align="right">6.7%</td>
<td align="right">6,149,596</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,649</td>
<td align="right">5.5%</td>
<td align="right">5,102,591</td>
<td align="right">5.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,599</td>
<td align="right">2.3%</td>
<td align="right">2,103,590</td>
<td align="right">2.3%</td>
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
<td align="left">Calls to Python functions inlined</td>
<td align="right">131,164,685</td>
<td align="right">62.4%</td>
<td align="right">131,278,677</td>
<td align="right">62.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,563,671</td>
<td align="right">89.3%</td>
<td align="right">187,710,553</td>
<td align="right">89.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,443</td>
<td align="right">0.5%</td>
<td align="right">950,307</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">3,469,129</td>
<td align="right">1.7%</td>
<td align="right">3,468,820</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,144,482</td>
<td align="right">19.6%</td>
<td align="right">41,142,210</td>
<td align="right">19.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">78,899,123</td>
<td align="right">37.6%</td>
<td align="right">78,895,633</td>
<td align="right">37.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">78,899,123</td>
<td align="right">37.6%</td>
<td align="right">78,895,633</td>
<td align="right">37.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,429,209</td>
<td align="right">35.9%</td>
<td align="right">75,426,028</td>
<td align="right">35.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,429,994</td>
<td align="right">35.9%</td>
<td align="right">75,426,813</td>
<td align="right">35.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,958</td>
<td align="right">8.8%</td>
<td align="right">18,490,413</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,332,200</td>
<td align="right">4.4%</td>
<td align="right">9,331,998</td>
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
<td align="right">416</td>
<td align="right">0.0%</td>
<td align="right">416</td>
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
<td align="right">2,220,066</td>
<td align="right"></td>
<td align="right">2,388,006</td>
<td align="right"></td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,402,526</td>
<td align="right"></td>
<td align="right">1,341,318</td>
<td align="right"></td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,976</td>
<td align="right">0.0%</td>
<td align="right">9,258</td>
<td align="right">0.0%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,621,129</td>
<td align="right"></td>
<td align="right">3,727,805</td>
<td align="right"></td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">755,195</td>
<td align="right">0.2%</td>
<td align="right">767,208</td>
<td align="right">0.2%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">51,310,085</td>
<td align="right">1.3%</td>
<td align="right">51,080,401</td>
<td align="right">1.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">149,359,712</td>
<td align="right"></td>
<td align="right">148,995,136</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,257,889,141</td>
<td align="right">36.0%</td>
<td align="right">1,260,009,322</td>
<td align="right">36.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,374,474,358</td>
<td align="right">34.5%</td>
<td align="right">1,376,756,940</td>
<td align="right">34.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">248,732,289</td>
<td align="right"></td>
<td align="right">248,927,825</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,186,458,174</td>
<td align="right">34.0%</td>
<td align="right">1,185,567,259</td>
<td align="right">33.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,054,386,801</td>
<td align="right">26.4%</td>
<td align="right">1,055,176,113</td>
<td align="right">26.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,509,413,778</td>
<td align="right">37.8%</td>
<td align="right">1,508,449,684</td>
<td align="right">37.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">970,832,604</td>
<td align="right">27.8%</td>
<td align="right">971,277,853</td>
<td align="right">27.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">129,175,630</td>
<td align="right">25.9%</td>
<td align="right">129,231,713</td>
<td align="right">25.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,815,635</td>
<td align="right"></td>
<td align="right">141,871,743</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">128,411,459</td>
<td align="right">25.7%</td>
<td align="right">128,455,247</td>
<td align="right">25.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">76,055,825</td>
<td align="right">2.2%</td>
<td align="right">76,076,425</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,467</td>
<td align="right"></td>
<td align="right">866,301</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">370,503,972</td>
<td align="right">74.1%</td>
<td align="right">370,546,489</td>
<td align="right">74.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">370,538,767</td>
<td align="right"></td>
<td align="right">370,581,280</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">150</td>
<td align="right">0.8%</td>
<td align="right">339</td>
<td align="right">1.9%</td>
<td align="right">126.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">49,913,203</td>
<td align="right"></td>
<td align="right">35,499,570</td>
<td align="right"></td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,866</td>
<td align="right">10.0%</td>
<td align="right">1,329</td>
<td align="right">7.3%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,836</td>
<td align="right">9.8%</td>
<td align="right">1,939</td>
<td align="right">10.7%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">95</td>
<td align="right">0.5%</td>
<td align="right">100</td>
<td align="right">0.6%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">18,744</td>
<td align="right"></td>
<td align="right">18,157</td>
<td align="right"></td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">5,914</td>
<td align="right">31.6%</td>
<td align="right">5,740</td>
<td align="right">31.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,667,202,805</td>
<td align="right">3,340.2%</td>
<td align="right">1,658,952,078</td>
<td align="right">4,673.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">9,128</td>
<td align="right">48.7%</td>
<td align="right">9,149</td>
<td align="right">50.4%</td>
<td align="right">0.2%</td>
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
<td align="right">1,773</td>
<td align="right">96.6%</td>
<td align="right">1,876</td>
<td align="right">96.8%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,836</td>
<td align="right"></td>
<td align="right">1,939</td>
<td align="right"></td>
<td align="right">5.6%</td>
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
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">12,798,296</td>
<td align="right">76.5%</td>
<td align="right">32,664,154</td>
<td align="right">83.5%</td>
<td align="right">155.2%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">400,432</td>
<td align="right">2.4%</td>
<td align="right">951,536</td>
<td align="right">2.4%</td>
<td align="right">137.6%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">16,736,256</td>
<td align="right"></td>
<td align="right">39,112,704</td>
<td align="right"></td>
<td align="right">133.7%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">3,537,528</td>
<td align="right">21.1%</td>
<td align="right">5,497,014</td>
<td align="right">14.1%</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">90,112</td>
<td align="right">0.5%</td>
<td align="right">110,592</td>
<td align="right">0.3%</td>
<td align="right">22.7%</td>
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
<td align="left">391</td>
<td align="right">22.1%</td>
<td align="left">387</td>
<td align="right">15.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">886</td>
<td align="right">50.0%</td>
<td align="left">880</td>
<td align="right">34.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">430</td>
<td align="right">24.3%</td>
<td align="left">924</td>
<td align="right">36.1%</td>
<td align="right">114.9%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">66</td>
<td align="right">3.7%</td>
<td align="left">190</td>
<td align="right">7.4%</td>
<td align="right">187.9%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">108</td>
<td align="right">4.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">70</td>
<td align="right">2.7%</td>
<td align="right"></td>
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
<td align="left"><= 8</td>
<td align="right">70</td>
<td align="right">3.8%</td>
<td align="right">76</td>
<td align="right">3.9%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">125</td>
<td align="right">6.8%</td>
<td align="right">199</td>
<td align="right">10.3%</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">394</td>
<td align="right">21.5%</td>
<td align="right">314</td>
<td align="right">16.2%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">860</td>
<td align="right">46.8%</td>
<td align="right">775</td>
<td align="right">40.0%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">321</td>
<td align="right">17.5%</td>
<td align="right">509</td>
<td align="right">26.3%</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">45</td>
<td align="right">2.5%</td>
<td align="right">45</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">21</td>
<td align="right">1.1%</td>
<td align="right">21</td>
<td align="right">1.1%</td>
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
<td align="left"><= 4</td>
<td align="right">48</td>
<td align="right">2.6%</td>
<td align="right">54</td>
<td align="right">2.8%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">22</td>
<td align="right">1.2%</td>
<td align="right">22</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">239</td>
<td align="right">13.0%</td>
<td align="right">284</td>
<td align="right">14.6%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">864</td>
<td align="right">47.1%</td>
<td align="right">769</td>
<td align="right">39.7%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">320</td>
<td align="right">17.4%</td>
<td align="right">279</td>
<td align="right">14.4%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">259</td>
<td align="right">14.1%</td>
<td align="right">447</td>
<td align="right">23.1%</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">1.1%</td>
<td align="right">21</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
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
<td align="left">_COMPARE_OP</td>
<td align="right">352,188</td>
<td align="right">756,195</td>
<td align="right">114.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">833,316</td>
<td align="right">145,449</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">5,037,087</td>
<td align="right">7,087,377</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">2,139,710</td>
<td align="right">2,948,230</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,223,277</td>
<td align="right">3,031,807</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">5,089,930</td>
<td align="right">6,789,876</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">49,913,203</td>
<td align="right">35,499,527</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">49,913,203</td>
<td align="right">35,499,570</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,278</td>
<td align="right">1,024</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,828,633</td>
<td align="right">1,556,693</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,741,950</td>
<td align="right">3,146,211</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,999,253</td>
<td align="right">2,266,982</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">3,954,836</td>
<td align="right">3,682,899</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">7,651</td>
<td align="right">7,145</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">7,170,116</td>
<td align="right">7,597,897</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,674,738</td>
<td align="right">4,405,203</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">14,342,035</td>
<td align="right">15,164,382</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">23,665,267</td>
<td align="right">24,826,120</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">39,868,197</td>
<td align="right">41,747,759</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">6,387,613</td>
<td align="right">6,669,462</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">89,781,400</td>
<td align="right">93,697,013</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">12,551,318</td>
<td align="right">12,268,467</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">9,891,887</td>
<td align="right">10,091,836</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">26,386,327</td>
<td align="right">26,804,586</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">11,784,328</td>
<td align="right">11,617,899</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">6,491,887</td>
<td align="right">6,582,658</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">336,147,109</td>
<td align="right">340,774,373</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">7,375,330</td>
<td align="right">7,466,099</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">10,334,649</td>
<td align="right">10,208,497</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">306,512</td>
<td align="right">308,922</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">15,522,908</td>
<td align="right">15,629,595</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">17,913,948</td>
<td align="right">18,020,635</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">31,033,108</td>
<td align="right">30,850,387</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">303,046,922</td>
<td align="right">304,610,785</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">22,409,537</td>
<td align="right">22,499,971</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">26,088,814</td>
<td align="right">26,185,548</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">26,088,814</td>
<td align="right">26,185,548</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">4,076,753</td>
<td align="right">4,088,461</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">80,369,721</td>
<td align="right">80,592,591</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">36,006,124</td>
<td align="right">36,100,181</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,094,367</td>
<td align="right">1,096,777</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">6,321,038</td>
<td align="right">6,332,743</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,250,025</td>
<td align="right">1,248,078</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,250,025</td>
<td align="right">1,248,078</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,250,025</td>
<td align="right">1,248,078</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">3,117,137</td>
<td align="right">3,113,254</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,133,036</td>
<td align="right">3,129,153</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,239,347</td>
<td align="right">3,235,464</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">8,564</td>
<td align="right">8,574</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">5,509,593</td>
<td align="right">5,514,201</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">31,241,850</td>
<td align="right">31,267,310</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,060,468</td>
<td align="right">3,058,529</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">5,072,008</td>
<td align="right">5,074,631</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,072,008</td>
<td align="right">5,074,631</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">26,169,048</td>
<td align="right">26,181,339</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">26,890,972</td>
<td align="right">26,903,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">26,890,972</td>
<td align="right">26,903,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">6,134,588</td>
<td align="right">6,137,208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">6,576,409</td>
<td align="right">6,579,034</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">7,689,409</td>
<td align="right">7,692,030</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">12,183,126</td>
<td align="right">12,186,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">12,183,126</td>
<td align="right">12,186,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,370,973</td>
<td align="right">8,373,378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">10,906,979</td>
<td align="right">10,909,598</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,514,078</td>
<td align="right">2,513,880</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">24,484,211</td>
<td align="right">24,482,667</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">3,351,060</td>
<td align="right">3,350,853</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,797,831</td>
<td align="right">15,798,634</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">5,974,086</td>
<td align="right">5,973,871</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">32,545,344</td>
<td align="right">32,545,849</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">13,399,042</td>
<td align="right">13,398,959</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">13,399,042</td>
<td align="right">13,398,959</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,072,553</td>
<td align="right">1,072,558</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,125,160</td>
<td align="right">2,125,152</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,609,441</td>
<td align="right">1,609,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,686,384</td>
<td align="right">1,686,390</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,231,525</td>
<td align="right">3,231,514</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,125,160</td>
<td align="right">2,125,154</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">1,062,580</td>
<td align="right">1,062,577</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">3,340,644</td>
<td align="right">3,340,638</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">2,279,124</td>
<td align="right">2,279,120</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">1,437,890</td>
<td align="right">1,437,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,437,890</td>
<td align="right">1,437,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,437,890</td>
<td align="right">1,437,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,437,890</td>
<td align="right">1,437,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,437,890</td>
<td align="right">1,437,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,437,890</td>
<td align="right">1,437,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,437,890</td>
<td align="right">1,437,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,437,890</td>
<td align="right">1,437,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,437,890</td>
<td align="right">1,437,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,437,890</td>
<td align="right">1,437,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,567,854</td>
<td align="right">1,567,852</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,567,854</td>
<td align="right">1,567,852</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,449,416</td>
<td align="right">2,449,413</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,209,506</td>
<td align="right">2,209,504</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,763,671</td>
<td align="right">1,763,671</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,763,671</td>
<td align="right">1,763,671</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">174,242</td>
<td align="right">174,242</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">155,735</td>
<td align="right">155,735</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">144,184</td>
<td align="right">144,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">128,958</td>
<td align="right">128,958</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">90,320</td>
<td align="right">90,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">73,352</td>
<td align="right">73,352</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">52,447</td>
<td align="right">52,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">45,128</td>
<td align="right">45,128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">45,128</td>
<td align="right">45,128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">39,898</td>
<td align="right">39,898</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">36,456</td>
<td align="right">36,456</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">35,660</td>
<td align="right">35,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">28,192</td>
<td align="right">28,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">28,192</td>
<td align="right">28,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">26,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">18,228</td>
<td align="right">18,228</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,384</td>
<td align="right">7,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,166</td>
<td align="right">5,166</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,096</td>
<td align="right">3,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">43</td>
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
<td align="right">561</td>
<td align="right">42</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,474</td>
<td align="right">1,433</td>
<td align="right">-2.8%</td>
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
Stats gathered on: 2025-05-13
