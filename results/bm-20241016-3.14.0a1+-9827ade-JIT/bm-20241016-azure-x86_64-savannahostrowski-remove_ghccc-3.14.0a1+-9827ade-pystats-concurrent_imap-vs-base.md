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
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,997,679</td>
<td align="right">1,183,695</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,345,031</td>
<td align="right">943,424</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,147,352</td>
<td align="right">2,270,423</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,293,797</td>
<td align="right">2,758,096</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">11,124,905</td>
<td align="right">9,077,348</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,896,242</td>
<td align="right">4,038,370</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,560,141</td>
<td align="right">2,162,011</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,660,987</td>
<td align="right">8,454,553</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,041,525</td>
<td align="right">5,537,279</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,788,418</td>
<td align="right">8,004,950</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">50,915,629</td>
<td align="right">47,737,710</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,179,350</td>
<td align="right">6,809,352</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">185,658</td>
<td align="right">177,010</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">440</td>
<td align="right">458</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,967</td>
<td align="right">4,772</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">10,808,474</td>
<td align="right">10,426,012</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">15,402,242</td>
<td align="right">15,043,255</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">17,311,448</td>
<td align="right">16,960,250</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">100</td>
<td align="right">98</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">444,190</td>
<td align="right">435,977</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,102</td>
<td align="right">3,152</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,417</td>
<td align="right">4,486</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,364</td>
<td align="right">13,170</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,587</td>
<td align="right">17,393</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,587</td>
<td align="right">17,393</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">422,280</td>
<td align="right">425,195</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">865,540</td>
<td align="right">871,348</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">292,458</td>
<td align="right">294,398</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,917,491</td>
<td align="right">2,936,687</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,175,094</td>
<td align="right">1,182,820</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">443,396</td>
<td align="right">446,280</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,203,331</td>
<td align="right">1,211,057</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">602,597</td>
<td align="right">606,460</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,876,718</td>
<td align="right">3,901,537</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">311,136</td>
<td align="right">313,081</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">311,201</td>
<td align="right">313,146</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,241,144</td>
<td align="right">1,248,870</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">463,374</td>
<td align="right">466,235</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">933,396</td>
<td align="right">939,079</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">472,606</td>
<td align="right">475,472</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">622,773</td>
<td align="right">626,508</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">949,784</td>
<td align="right">955,458</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">963,789</td>
<td align="right">969,460</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">163,135</td>
<td align="right">164,083</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">980,219</td>
<td align="right">985,906</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">674,511</td>
<td align="right">678,374</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">172,295</td>
<td align="right">173,265</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,748</td>
<td align="right">36,542</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">794,810</td>
<td align="right">799,225</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,918,586</td>
<td align="right">1,928,924</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">9,925,659</td>
<td align="right">9,977,463</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">182,374</td>
<td align="right">183,322</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,849,420</td>
<td align="right">3,868,967</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,530,340</td>
<td align="right">6,562,848</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,747,681</td>
<td align="right">1,756,337</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">202,943</td>
<td align="right">203,909</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,377,299</td>
<td align="right">5,402,355</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,567,349</td>
<td align="right">1,574,440</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,156,241</td>
<td align="right">4,174,299</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,679,445</td>
<td align="right">2,689,034</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,952,880</td>
<td align="right">1,959,584</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">857,096</td>
<td align="right">859,989</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,349,952</td>
<td align="right">2,357,634</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">67,248</td>
<td align="right">67,034</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,381,671</td>
<td align="right">3,391,261</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,665,680</td>
<td align="right">3,675,808</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">94,579</td>
<td align="right">94,340</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">776,232</td>
<td align="right">778,130</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,876,398</td>
<td align="right">3,885,434</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">15,640,329</td>
<td align="right">15,676,577</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,004,744</td>
<td align="right">1,006,982</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,770,768</td>
<td align="right">7,787,200</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">29,938</td>
<td align="right">29,875</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">891,366</td>
<td align="right">893,107</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,638,302</td>
<td align="right">8,655,160</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">43,988</td>
<td align="right">43,905</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">463,803</td>
<td align="right">464,655</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">863,335</td>
<td align="right">864,821</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">619,851</td>
<td align="right">620,734</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,973,980</td>
<td align="right">5,981,075</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">89,340</td>
<td align="right">89,252</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">20,694</td>
<td align="right">20,676</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,485,094</td>
<td align="right">1,485,977</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">37,966</td>
<td align="right">37,944</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">57,483</td>
<td align="right">57,461</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,469</td>
<td align="right">21,461</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">26,017</td>
<td align="right">26,025</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">149,284</td>
<td align="right">149,253</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">300,223</td>
<td align="right">300,165</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">28,684</td>
<td align="right">28,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,371</td>
<td align="right">61,363</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">146,976</td>
<td align="right">146,993</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">892,608</td>
<td align="right">892,542</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">22,094</td>
<td align="right">22,093</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,035</td>
<td align="right">34,036</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,656</td>
<td align="right">1,818,634</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">489,417</td>
<td align="right">489,413</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,067,766</td>
<td align="right">5,067,766</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,137</td>
<td align="right">105,137</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,107</td>
<td align="right">105,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">84,693</td>
<td align="right">84,693</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,098</td>
<td align="right">77,098</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,585</td>
<td align="right">67,585</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,468</td>
<td align="right">55,468</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,466</td>
<td align="right">55,466</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">50,952</td>
<td align="right">50,952</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">43,864</td>
<td align="right">43,864</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,873</td>
<td align="right">42,873</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">39,010</td>
<td align="right">39,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">38,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,547</td>
<td align="right">29,547</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,763</td>
<td align="right">28,763</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">28,680</td>
<td align="right">28,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">26,276</td>
<td align="right">26,276</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">21,676</td>
<td align="right">21,676</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">20,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">17,404</td>
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
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,728</td>
<td align="right">12,728</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">9,142</td>
<td align="right">9,142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">8,731</td>
<td align="right">8,731</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">8,731</td>
<td align="right">8,731</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">8,502</td>
<td align="right">8,502</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,485</td>
<td align="right">8,485</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">8,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,396</td>
<td align="right">4,396</td>
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
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">368</td>
<td align="right">368</td>
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
<td align="left">TO_BOOL_STR</td>
<td align="right">139</td>
<td align="right">139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">93</td>
<td align="right">93</td>
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
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
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
<td align="right">3,874,621</td>
<td align="right">72.2%</td>
<td align="right">3,899,487</td>
<td align="right">72.3%</td>
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
<td align="right">1,490,354</td>
<td align="right">27.8%</td>
<td align="right">1,493,016</td>
<td align="right">27.7%</td>
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
<td align="right">117</td>
<td align="right">5.6%</td>
<td align="right">113</td>
<td align="right">5.5%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,980</td>
<td align="right">94.4%</td>
<td align="right">1,937</td>
<td align="right">94.5%</td>
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
<td align="left">or</td>
<td align="right">553</td>
<td align="right">27.9%</td>
<td align="right">536</td>
<td align="right">27.7%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">943</td>
<td align="right">47.6%</td>
<td align="right">915</td>
<td align="right">47.2%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">206</td>
<td align="right">10.4%</td>
<td align="right">208</td>
<td align="right">10.7%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">191</td>
<td align="right">9.6%</td>
<td align="right">191</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">87</td>
<td align="right">4.4%</td>
<td align="right">87</td>
<td align="right">4.5%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,441</td>
<td align="right">6.8%</td>
<td align="right">36,246</td>
<td align="right">6.7%</td>
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
<td align="right">498,978</td>
<td align="right">93.1%</td>
<td align="right">500,918</td>
<td align="right">93.2%</td>
<td align="right">0.4%</td>
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
<td align="right">190</td>
<td align="right">61.9%</td>
<td align="right">179</td>
<td align="right">60.5%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">117</td>
<td align="right">38.1%</td>
<td align="right">117</td>
<td align="right">39.5%</td>
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
<td align="right">189</td>
<td align="right">99.5%</td>
<td align="right">178</td>
<td align="right">99.4%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">0.5%</td>
<td align="right">1</td>
<td align="right">0.6%</td>
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
<td align="right">1,111</td>
<td align="right">0.0%</td>
<td align="right">1,152</td>
<td align="right">0.0%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">19,698,167</td>
<td align="right">100.0%</td>
<td align="right">19,784,817</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
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
<td align="right">517</td>
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
<td align="right">3,446</td>
<td align="right">100.0%</td>
<td align="right">3,474</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
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
<td align="right">462,663</td>
<td align="right">10.9%</td>
<td align="right">465,533</td>
<td align="right">10.9%</td>
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
<td align="right">3,789,339</td>
<td align="right">89.0%</td>
<td align="right">3,800,412</td>
<td align="right">89.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,279</td>
<td align="right">0.1%</td>
<td align="right">4,277</td>
<td align="right">0.1%</td>
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
<td align="right">445</td>
<td align="right">57.1%</td>
<td align="right">428</td>
<td align="right">55.7%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">334</td>
<td align="right">42.9%</td>
<td align="right">341</td>
<td align="right">44.3%</td>
<td align="right">2.1%</td>
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
<td align="right">246</td>
<td align="right">55.3%</td>
<td align="right">227</td>
<td align="right">53.0%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">104</td>
<td align="right">23.4%</td>
<td align="right">106</td>
<td align="right">24.8%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">21.3%</td>
<td align="right">95</td>
<td align="right">22.2%</td>
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
<td align="right">1,417,127</td>
<td align="right">100.0%</td>
<td align="right">1,423,894</td>
<td align="right">100.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,634,344</td>
<td align="right">99.6%</td>
<td align="right">5,640,018</td>
<td align="right">99.6%</td>
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
<td align="right">21,788</td>
<td align="right">0.4%</td>
<td align="right">21,788</td>
<td align="right">0.4%</td>
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
<td align="right">50</td>
<td align="right">16.3%</td>
<td align="right">49</td>
<td align="right">16.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">256</td>
<td align="right">83.7%</td>
<td align="right">256</td>
<td align="right">83.9%</td>
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
<td align="right">72</td>
<td align="right">28.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">69</td>
<td align="right">27.0%</td>
<td align="right">69</td>
<td align="right">27.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">2.7%</td>
<td align="right">7</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">1.2%</td>
<td align="right">3</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
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
<td align="right">4,886,764</td>
<td align="right">12.3%</td>
<td align="right">4,029,177</td>
<td align="right">10.3%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,477,451</td>
<td align="right">86.8%</td>
<td align="right">34,607,486</td>
<td align="right">88.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">334,796</td>
<td align="right">0.8%</td>
<td align="right">334,047</td>
<td align="right">0.9%</td>
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
<td align="right">4,824</td>
<td align="right">31.1%</td>
<td align="right">4,517</td>
<td align="right">29.7%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,677</td>
<td align="right">68.9%</td>
<td align="right">10,680</td>
<td align="right">70.3%</td>
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
<td align="right">1,348</td>
<td align="right">27.9%</td>
<td align="right">1,126</td>
<td align="right">24.9%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">713</td>
<td align="right">14.8%</td>
<td align="right">679</td>
<td align="right">15.0%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,285</td>
<td align="right">26.6%</td>
<td align="right">1,240</td>
<td align="right">27.5%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">9.5%</td>
<td align="right">460</td>
<td align="right">10.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">189</td>
<td align="right">3.9%</td>
<td align="right">189</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.5%</td>
<td align="right">71</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.9%</td>
<td align="right">45</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">23</td>
<td align="right">0.5%</td>
<td align="right">23</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.5%</td>
<td align="right">23</td>
<td align="right">0.5%</td>
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
<td align="right">772</td>
<td align="right">0.0%</td>
<td align="right">799</td>
<td align="right">0.0%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,081,626</td>
<td align="right">100.0%</td>
<td align="right">14,151,488</td>
<td align="right">100.0%</td>
<td align="right">0.5%</td>
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
<td align="right">2,339</td>
<td align="right">100.0%</td>
<td align="right">2,362</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
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
<td align="right">1,612,540</td>
<td align="right">100.0%</td>
<td align="right">1,623,170</td>
<td align="right">100.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,123,544</td>
<td align="right">95.3%</td>
<td align="right">4,142,863</td>
<td align="right">95.4%</td>
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
<td align="right">59,828</td>
<td align="right">1.4%</td>
<td align="right">59,824</td>
<td align="right">1.4%</td>
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
<td align="right">140,654</td>
<td align="right">3.3%</td>
<td align="right">140,654</td>
<td align="right">3.2%</td>
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
<td align="right">3,618</td>
<td align="right">86.6%</td>
<td align="right">3,614</td>
<td align="right">86.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">561</td>
<td align="right">13.4%</td>
<td align="right">561</td>
<td align="right">13.4%</td>
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
<td align="right">344</td>
<td align="right">61.3%</td>
<td align="right">344</td>
<td align="right">61.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">163</td>
<td align="right">29.1%</td>
<td align="right">163</td>
<td align="right">29.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">44</td>
<td align="right">7.8%</td>
<td align="right">44</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.8%</td>
<td align="right">10</td>
<td align="right">1.8%</td>
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
<td align="right">1,482,913</td>
<td align="right">98.6%</td>
<td align="right">1,489,841</td>
<td align="right">98.6%</td>
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
<td align="right">21,263</td>
<td align="right">1.4%</td>
<td align="right">21,259</td>
<td align="right">1.4%</td>
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
<td align="right">19</td>
<td align="right">9.2%</td>
<td align="right">15</td>
<td align="right">7.4%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">90.8%</td>
<td align="right">187</td>
<td align="right">92.6%</td>
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
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
<td align="right">68</td>
<td align="right">36.4%</td>
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
<td align="right">9,192,136</td>
<td align="right">99.3%</td>
<td align="right">9,244,363</td>
<td align="right">99.3%</td>
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
<td align="right">66,258</td>
<td align="right">0.7%</td>
<td align="right">66,045</td>
<td align="right">0.7%</td>
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
<td align="right">544</td>
<td align="right">54.8%</td>
<td align="right">542</td>
<td align="right">54.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">448</td>
<td align="right">45.2%</td>
<td align="right">449</td>
<td align="right">45.3%</td>
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
<td align="left">sequence</td>
<td align="right">140</td>
<td align="right">25.7%</td>
<td align="right">139</td>
<td align="right">25.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">175</td>
<td align="right">32.2%</td>
<td align="right">174</td>
<td align="right">32.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">118</td>
<td align="right">21.7%</td>
<td align="right">118</td>
<td align="right">21.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">12.5%</td>
<td align="right">68</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">43</td>
<td align="right">7.9%</td>
<td align="right">43</td>
<td align="right">7.9%</td>
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
<td align="right">2,033,244</td>
<td align="right">100.0%</td>
<td align="right">2,035,118</td>
<td align="right">100.0%</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,466,047</td>
<td align="right">3.3%</td>
<td align="right">8,635,537</td>
<td align="right">3.2%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">183,129,987</td>
<td align="right">64.7%</td>
<td align="right">176,180,146</td>
<td align="right">64.7%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">90,000,611</td>
<td align="right">31.8%</td>
<td align="right">87,144,659</td>
<td align="right">32.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">480,629</td>
<td align="right">0.2%</td>
<td align="right">479,880</td>
<td align="right">0.2%</td>
<td align="right">-0.2%</td>
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
<td align="right">4,886,764</td>
<td align="right">51.7%</td>
<td align="right">4,029,177</td>
<td align="right">46.8%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,111</td>
<td align="right">0.0%</td>
<td align="right">1,152</td>
<td align="right">0.0%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,874,621</td>
<td align="right">41.0%</td>
<td align="right">3,899,487</td>
<td align="right">45.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">462,663</td>
<td align="right">4.9%</td>
<td align="right">465,533</td>
<td align="right">5.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,441</td>
<td align="right">0.4%</td>
<td align="right">36,246</td>
<td align="right">0.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">66,258</td>
<td align="right">0.7%</td>
<td align="right">66,045</td>
<td align="right">0.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,263</td>
<td align="right">0.2%</td>
<td align="right">21,259</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">59,828</td>
<td align="right">0.6%</td>
<td align="right">59,824</td>
<td align="right">0.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,788</td>
<td align="right">0.2%</td>
<td align="right">21,788</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,855</td>
<td align="right">0.1%</td>
<td align="right">12,855</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">275,255</td>
<td align="right">57.3%</td>
<td align="right">274,494</td>
<td align="right">57.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,278</td>
<td align="right">0.9%</td>
<td align="right">4,276</td>
<td align="right">0.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,491</td>
<td align="right">10.3%</td>
<td align="right">49,503</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,654</td>
<td align="right">29.3%</td>
<td align="right">140,654</td>
<td align="right">29.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">2.1%</td>
<td align="right">9,895</td>
<td align="right">2.1%</td>
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
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">144</td>
<td align="right">0.0%</td>
<td align="right">144</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">143</td>
<td align="right">0.0%</td>
<td align="right">143</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">86</td>
<td align="right">0.0%</td>
<td align="right">86</td>
<td align="right">0.0%</td>
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
<td align="left">Frame objects created</td>
<td align="right">17,598</td>
<td align="right">0.1%</td>
<td align="right">17,404</td>
<td align="right">0.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">418,461</td>
<td align="right">1.5%</td>
<td align="right">420,400</td>
<td align="right">1.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">22,844,783</td>
<td align="right">82.0%</td>
<td align="right">22,936,225</td>
<td align="right">82.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">20,094,790</td>
<td align="right">72.1%</td>
<td align="right">20,169,800</td>
<td align="right">72.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,348,213</td>
<td align="right">26.4%</td>
<td align="right">7,364,645</td>
<td align="right">26.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,348,269</td>
<td align="right">26.4%</td>
<td align="right">7,364,701</td>
<td align="right">26.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,775,126</td>
<td align="right">27.9%</td>
<td align="right">7,791,558</td>
<td align="right">27.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,775,126</td>
<td align="right">27.9%</td>
<td align="right">7,791,558</td>
<td align="right">27.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">426,857</td>
<td align="right">1.5%</td>
<td align="right">426,857</td>
<td align="right">1.5%</td>
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
<td align="right">1.6%</td>
<td align="right">456,471</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,507</td>
<td align="right">1.6%</td>
<td align="right">441,507</td>
<td align="right">1.6%</td>
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
<td align="right">73,626</td>
<td align="right"></td>
<td align="right">51,670</td>
<td align="right"></td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">88,003</td>
<td align="right"></td>
<td align="right">68,828</td>
<td align="right"></td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">14,627</td>
<td align="right"></td>
<td align="right">17,397</td>
<td align="right"></td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">60,048,099</td>
<td align="right">16.7%</td>
<td align="right">57,004,451</td>
<td align="right">15.8%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">55,930,482</td>
<td align="right">15.5%</td>
<td align="right">58,170,301</td>
<td align="right">16.2%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">127,423,691</td>
<td align="right">35.4%</td>
<td align="right">131,629,453</td>
<td align="right">36.6%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">59,817,043</td>
<td align="right">14.4%</td>
<td align="right">57,996,069</td>
<td align="right">13.9%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">116,450,519</td>
<td align="right">32.4%</td>
<td align="right">113,107,759</td>
<td align="right">31.4%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">83,347,818</td>
<td align="right">20.0%</td>
<td align="right">85,700,039</td>
<td align="right">20.5%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">120,122,854</td>
<td align="right">28.8%</td>
<td align="right">122,980,820</td>
<td align="right">29.4%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">153,232,914</td>
<td align="right">36.8%</td>
<td align="right">151,337,480</td>
<td align="right">36.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,740,251</td>
<td align="right"></td>
<td align="right">7,804,875</td>
<td align="right"></td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,305,498</td>
<td align="right"></td>
<td align="right">1,313,224</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">16,106,546</td>
<td align="right">49.8%</td>
<td align="right">16,172,637</td>
<td align="right">49.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">16,109,295</td>
<td align="right"></td>
<td align="right">16,175,295</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">10,414,212</td>
<td align="right"></td>
<td align="right">10,447,875</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">17,306,599</td>
<td align="right"></td>
<td align="right">17,359,292</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">16,095,372</td>
<td align="right">49.8%</td>
<td align="right">16,141,376</td>
<td align="right">49.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,216,713</td>
<td align="right">50.2%</td>
<td align="right">16,262,716</td>
<td align="right">50.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,802</td>
<td align="right">0.2%</td>
<td align="right">77,801</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,539</td>
<td align="right">0.1%</td>
<td align="right">43,539</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.0%</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">245</td>
<td align="right">6.3%</td>
<td align="right">216</td>
<td align="right">5.8%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">3,286</td>
<td align="right">84.8%</td>
<td align="right">2,953</td>
<td align="right">78.8%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">386,419,635</td>
<td align="right">1,780.3%</td>
<td align="right">404,536,028</td>
<td align="right">1,860.7%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">3,265</td>
<td align="right">84.2%</td>
<td align="right">3,152</td>
<td align="right">84.1%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,877</td>
<td align="right"></td>
<td align="right">3,747</td>
<td align="right"></td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">367</td>
<td align="right">9.5%</td>
<td align="right">379</td>
<td align="right">10.1%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">21,704,988</td>
<td align="right"></td>
<td align="right">21,740,659</td>
<td align="right"></td>
<td align="right">0.2%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
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
<td align="right">363</td>
<td align="right">98.9%</td>
<td align="right">375</td>
<td align="right">98.9%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">367</td>
<td align="right"></td>
<td align="right">379</td>
<td align="right"></td>
<td align="right">3.3%</td>
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
<td align="right">4</td>
<td align="right">1.1%</td>
<td align="right">4</td>
<td align="right">1.1%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">99</td>
<td align="right">27.0%</td>
<td align="right">101</td>
<td align="right">26.6%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">28</td>
<td align="right">7.6%</td>
<td align="right">36</td>
<td align="right">9.5%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">66</td>
<td align="right">18.0%</td>
<td align="right">71</td>
<td align="right">18.7%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">119</td>
<td align="right">32.4%</td>
<td align="right">125</td>
<td align="right">33.0%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">22</td>
<td align="right">6.0%</td>
<td align="right">19</td>
<td align="right">5.0%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">32</td>
<td align="right">8.7%</td>
<td align="right">26</td>
<td align="right">6.9%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1</td>
<td align="right">0.3%</td>
<td align="right">1</td>
<td align="right">0.3%</td>
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
<td align="right">13.4%</td>
<td align="right">52</td>
<td align="right">13.7%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">67</td>
<td align="right">18.3%</td>
<td align="right">70</td>
<td align="right">18.5%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">34</td>
<td align="right">9.3%</td>
<td align="right">38</td>
<td align="right">10.0%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">95</td>
<td align="right">25.9%</td>
<td align="right">102</td>
<td align="right">26.9%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">78</td>
<td align="right">21.3%</td>
<td align="right">76</td>
<td align="right">20.1%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">37</td>
<td align="right">10.1%</td>
<td align="right">34</td>
<td align="right">9.0%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3</td>
<td align="right">0.8%</td>
<td align="right">3</td>
<td align="right">0.8%</td>
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
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">21</td>
<td align="right">819,314</td>
<td align="right">3,901,395.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">137,882</td>
<td align="right">546,417</td>
<td align="right">296.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">740,398</td>
<td align="right">1,564,495</td>
<td align="right">111.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">411,776</td>
<td align="right">50</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">633,312</td>
<td align="right">1,044,724</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,387,135</td>
<td align="right">2,278,551</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,235,673</td>
<td align="right">3,068,182</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,419,035</td>
<td align="right">3,304,542</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">7,774,691</td>
<td align="right">9,878,696</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">7,791,468</td>
<td align="right">9,895,467</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,715,878</td>
<td align="right">9,458,627</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,061,009</td>
<td align="right">2,486,382</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">11,486,202</td>
<td align="right">13,615,578</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">7,495,311</td>
<td align="right">8,768,029</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,759,074</td>
<td align="right">2,293,072</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,759,074</td>
<td align="right">2,293,072</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,718,736</td>
<td align="right">2,268,112</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">4,434,838</td>
<td align="right">4,873,818</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">4,846,600</td>
<td align="right">5,281,405</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">5,276,669</td>
<td align="right">5,714,382</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">9,098,817</td>
<td align="right">9,541,858</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">9,552,085</td>
<td align="right">9,993,141</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">9,921,909</td>
<td align="right">10,359,622</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">32,729,281</td>
<td align="right">34,068,117</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">23,419,378</td>
<td align="right">24,324,362</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">19,394,521</td>
<td align="right">18,966,121</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">411,173</td>
<td align="right">419,390</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">417,666</td>
<td align="right">425,883</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">569,838</td>
<td align="right">579,029</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">569,838</td>
<td align="right">579,029</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,289,626</td>
<td align="right">1,303,613</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">553,695</td>
<td align="right">558,976</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,391,049</td>
<td align="right">1,403,230</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,100,999</td>
<td align="right">1,110,049</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">137,914</td>
<td align="right">138,925</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">137,976</td>
<td align="right">138,979</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">413,822</td>
<td align="right">416,814</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">551,816</td>
<td align="right">555,777</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">689,586</td>
<td align="right">694,514</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,378,996</td>
<td align="right">1,388,764</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,215,023</td>
<td align="right">2,230,691</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,521,069</td>
<td align="right">1,531,771</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">413,646</td>
<td align="right">416,550</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">413,646</td>
<td align="right">416,550</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">413,648</td>
<td align="right">416,552</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">413,648</td>
<td align="right">416,552</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">413,652</td>
<td align="right">416,556</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">559,509</td>
<td align="right">563,385</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,550,143</td>
<td align="right">1,560,779</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">141,906</td>
<td align="right">142,876</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">425,918</td>
<td align="right">428,826</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">288,042</td>
<td align="right">289,982</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">294,639</td>
<td align="right">296,614</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,203,386</td>
<td align="right">1,211,235</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,865,190</td>
<td align="right">1,877,316</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">300,421</td>
<td align="right">302,361</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">454,929</td>
<td align="right">457,839</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">454,929</td>
<td align="right">457,839</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">152,404</td>
<td align="right">153,366</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">3,528,380</td>
<td align="right">3,549,905</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">3,528,380</td>
<td align="right">3,549,905</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,114,558</td>
<td align="right">3,133,091</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,922,682</td>
<td align="right">2,939,941</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,527,442</td>
<td align="right">2,542,117</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">175,058</td>
<td align="right">176,036</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">4,213,288</td>
<td align="right">4,236,681</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,389,187</td>
<td align="right">4,413,420</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,817,708</td>
<td align="right">1,827,499</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,690,406</td>
<td align="right">1,699,211</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,724,937</td>
<td align="right">1,733,754</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,115,575</td>
<td align="right">1,120,502</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,409,514</td>
<td align="right">3,424,071</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,081,906</td>
<td align="right">2,090,713</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,075,733</td>
<td align="right">2,084,466</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">981,783</td>
<td align="right">985,659</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,087,392</td>
<td align="right">1,091,240</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">901,029</td>
<td align="right">904,023</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,775,210</td>
<td align="right">2,783,009</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">714,808</td>
<td align="right">716,794</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">714,814</td>
<td align="right">716,800</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,461,203</td>
<td align="right">1,465,208</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">16,201,062</td>
<td align="right">16,238,001</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,069,111</td>
<td align="right">3,075,942</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,780,595</td>
<td align="right">6,795,168</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,780,595</td>
<td align="right">6,795,168</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,369,860</td>
<td align="right">1,372,767</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,469,696</td>
<td align="right">5,479,714</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">553,680</td>
<td align="right">554,694</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">556,134</td>
<td align="right">557,147</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,118,510</td>
<td align="right">1,120,491</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">566,105</td>
<td align="right">567,067</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">566,164</td>
<td align="right">567,126</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">21,704,988</td>
<td align="right">21,740,659</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">22,335,586</td>
<td align="right">22,371,844</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,214,764</td>
<td align="right">8,227,485</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">593,993</td>
<td align="right">594,805</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">4,924,595</td>
<td align="right">4,929,478</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">630,598</td>
<td align="right">631,185</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,396,210</td>
<td align="right">1,397,221</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,110,436</td>
<td align="right">6,114,079</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,679,404</td>
<td align="right">2,680,415</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">44,035</td>
<td align="right">44,019</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">16,777</td>
<td align="right">16,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">16,393</td>
<td align="right">16,397</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,487,069</td>
<td align="right">5,485,802</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">16,857</td>
<td align="right">16,856</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">9,851,731</td>
<td align="right">9,851,755</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,645,240</td>
<td align="right">4,645,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">918,323</td>
<td align="right">918,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">829,765</td>
<td align="right">829,765</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">823,550</td>
<td align="right">823,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">819,293</td>
<td align="right">819,293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">422,270</td>
<td align="right">422,270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">411,730</td>
<td align="right">411,730</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">411,726</td>
<td align="right">411,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">411,718</td>
<td align="right">411,718</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">61,094</td>
<td align="right">61,094</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">60,911</td>
<td align="right">60,911</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">60,907</td>
<td align="right">60,907</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">60,907</td>
<td align="right">60,907</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">60,907</td>
<td align="right">60,907</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">14,341</td>
<td align="right">14,341</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">11,921</td>
<td align="right">11,921</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">8,564</td>
<td align="right">8,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">8,564</td>
<td align="right">8,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">8,302</td>
<td align="right">8,302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,391</td>
<td align="right">6,391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,391</td>
<td align="right">6,391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">6,385</td>
<td align="right">6,385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,385</td>
<td align="right">6,385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,385</td>
<td align="right">6,385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">4,151</td>
<td align="right">4,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">4,151</td>
<td align="right">4,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">4,151</td>
<td align="right">4,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">4,151</td>
<td align="right">4,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,077</td>
<td align="right">4,077</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">191</td>
<td align="right">191</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">59</td>
<td align="right">59</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">59</td>
<td align="right">59</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">378</td>
<td align="right">142.3%</td>
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
Stats gathered on: 2024-10-18
