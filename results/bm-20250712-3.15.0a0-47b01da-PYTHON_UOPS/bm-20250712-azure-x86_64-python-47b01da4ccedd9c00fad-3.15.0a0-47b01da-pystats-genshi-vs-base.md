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
<td align="right">85,945,346</td>
<td align="right">1,051</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,412,395</td>
<td align="right">202,788</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,798,307</td>
<td align="right">885,297</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,323,590</td>
<td align="right">1,642,452</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,682,615</td>
<td align="right">6,001,155</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,604,138</td>
<td align="right">2,282,934</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,890,333</td>
<td align="right">2,988,908</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">25,823,914</td>
<td align="right">11,530,080</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">25,839,070</td>
<td align="right">11,544,704</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">12,083,291</td>
<td align="right">5,411,294</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">11,354,548</td>
<td align="right">5,150,656</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">23,561,260</td>
<td align="right">10,708,367</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">71,541,673</td>
<td align="right">32,967,894</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,753,555</td>
<td align="right">9,324,581</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">101,969,961</td>
<td align="right">48,892,724</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">142,111,105</td>
<td align="right">68,341,929</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">144,850,295</td>
<td align="right">69,816,597</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">384,513,910</td>
<td align="right">185,954,358</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">141,493,818</td>
<td align="right">68,571,589</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">118,684,663</td>
<td align="right">58,583,944</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,524,233</td>
<td align="right">756,105</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,412,682</td>
<td align="right">4,676,149</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">80,056,163</td>
<td align="right">39,796,998</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">63,641,338</td>
<td align="right">31,637,312</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">27,117,933</td>
<td align="right">13,481,616</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">13,395,781</td>
<td align="right">6,660,570</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">10,697,694</td>
<td align="right">5,319,629</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">41,000,607</td>
<td align="right">20,390,525</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">104,168,429</td>
<td align="right">51,809,185</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,801,880</td>
<td align="right">1,393,554</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">8,919,528</td>
<td align="right">4,436,892</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">4,204,140</td>
<td align="right">2,091,367</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,553,208</td>
<td align="right">4,752,440</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">9,174,969</td>
<td align="right">4,564,325</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">35,034,453</td>
<td align="right">17,429,289</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,204,485</td>
<td align="right">2,091,706</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">4,203,953</td>
<td align="right">2,091,561</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">384,927</td>
<td align="right">191,519</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">52,748,707</td>
<td align="right">26,246,805</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">6,115,227</td>
<td align="right">3,042,895</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">5,734,034</td>
<td align="right">2,853,606</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">9,179,751</td>
<td align="right">4,569,716</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">17,079,368</td>
<td align="right">8,502,218</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,206,158</td>
<td align="right">2,093,940</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,177,640</td>
<td align="right">4,569,024</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">10,707,603</td>
<td align="right">5,330,932</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">382,766</td>
<td align="right">190,570</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,973,482</td>
<td align="right">2,477,001</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">10,711,296</td>
<td align="right">5,335,031</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,604,883</td>
<td align="right">8,770,167</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">11,994,968</td>
<td align="right">5,978,341</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">817,359</td>
<td align="right">407,399</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">766,542</td>
<td align="right">382,099</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">385,699</td>
<td align="right">192,279</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">384,810</td>
<td align="right">191,836</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">6,769,535</td>
<td align="right">3,374,907</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,405,732</td>
<td align="right">701,415</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,219,055</td>
<td align="right">2,106,449</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,603,280</td>
<td align="right">2,298,411</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,667,725</td>
<td align="right">6,327,532</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">38,635,844</td>
<td align="right">19,298,895</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,054,673</td>
<td align="right">6,523,890</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">385,133</td>
<td align="right">192,532</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">386,562</td>
<td align="right">193,252</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">21,512,568</td>
<td align="right">10,755,413</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">22,424,920</td>
<td align="right">11,221,046</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">55,478,634</td>
<td align="right">27,812,099</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,541,916</td>
<td align="right">773,372</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">28,010,448</td>
<td align="right">14,051,088</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,547,312</td>
<td align="right">778,740</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,164,694</td>
<td align="right">587,780</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">388,788</td>
<td align="right">196,554</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">44,237,065</td>
<td align="right">22,645,485</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">404,283</td>
<td align="right">211,141</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">504,242</td>
<td align="right">309,808</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">8,273</td>
<td align="right">5,608</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,001</td>
<td align="right">1,415</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,445</td>
<td align="right">3,206</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,378</td>
<td align="right">2,467</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,753</td>
<td align="right">1,287</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,666</td>
<td align="right">3,560</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,130</td>
<td align="right">865</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">2,547</td>
<td align="right">1,961</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,785</td>
<td align="right">1,391</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,054</td>
<td align="right">862</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,398</td>
<td align="right">1,988</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,535</td>
<td align="right">1,329</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,485</td>
<td align="right">3,065</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">2,379</td>
<td align="right">2,108</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,379</td>
<td align="right">2,108</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,771</td>
<td align="right">4,266</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">18,080</td>
<td align="right">16,231</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,130</td>
<td align="right">4,682</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,069</td>
<td align="right">7,584</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,697</td>
<td align="right">2,535</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">25,049</td>
<td align="right">23,723</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">11,036</td>
<td align="right">10,571</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">14,932</td>
<td align="right">14,308</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">22,777</td>
<td align="right">22,029</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">87</td>
<td align="right">85</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">216</td>
<td align="right">212</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">690</td>
<td align="right">678</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">130,963</td>
<td align="right">128,767</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">130,700</td>
<td align="right">128,608</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">131,071</td>
<td align="right">128,986</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">64</td>
<td align="right">63</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">193</td>
<td align="right">190</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">644</td>
<td align="right">634</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">258</td>
<td align="right">254</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,438</td>
<td align="right">3,386</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">7,473</td>
<td align="right">7,361</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">904</td>
<td align="right">891</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">493</td>
<td align="right">486</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3,690</td>
<td align="right">3,638</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3,690</td>
<td align="right">3,638</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3,690</td>
<td align="right">3,638</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">300</td>
<td align="right">296</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">6,514</td>
<td align="right">6,430</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,190</td>
<td align="right">2,162</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">619</td>
<td align="right">612</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,338</td>
<td align="right">1,323</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">895</td>
<td align="right">885</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">2,648</td>
<td align="right">2,620</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">25,542</td>
<td align="right">25,320</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">6,794</td>
<td align="right">6,742</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">7,975</td>
<td align="right">7,926</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,055</td>
<td align="right">2,043</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">3,385</td>
<td align="right">3,367</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">9,904</td>
<td align="right">9,870</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">675</td>
<td align="right">673</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2,548</td>
<td align="right">2,541</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,421</td>
<td align="right">4,414</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">2,187</td>
<td align="right">2,184</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5,532</td>
<td align="right">5,526</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">4,185</td>
<td align="right">4,182</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,168</td>
<td align="right">21,168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">5,418</td>
<td align="right">5,418</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">3,906</td>
<td align="right">3,906</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,058</td>
<td align="right">2,058</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,260</td>
<td align="right">1,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,008</td>
<td align="right">1,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">756</td>
<td align="right">756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">651</td>
<td align="right">651</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">462</td>
<td align="right">462</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">441</td>
<td align="right">441</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">378</td>
<td align="right">378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">378</td>
<td align="right">378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">315</td>
<td align="right">315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">168</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">41,501,356</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">1,300,110</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">709,191</td>
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
<td align="right">46,393,746</td>
<td align="right">99.9%</td>
<td align="right">23,094,419</td>
<td align="right">99.9%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19,089</td>
<td align="right">0.0%</td>
<td align="right">18,414</td>
<td align="right">0.1%</td>
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
<td align="right">903</td>
<td align="right">0.0%</td>
<td align="right">903</td>
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
<td align="right">1,861</td>
<td align="right">49.9%</td>
<td align="right">1,788</td>
<td align="right">48.9%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,869</td>
<td align="right">50.1%</td>
<td align="right">1,869</td>
<td align="right">51.1%</td>
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
<td align="left">subscr tuple slice</td>
<td align="right">169</td>
<td align="right">9.1%</td>
<td align="right">147</td>
<td align="right">8.2%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">231</td>
<td align="right">12.4%</td>
<td align="right">210</td>
<td align="right">11.7%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">763</td>
<td align="right">41.0%</td>
<td align="right">736</td>
<td align="right">41.2%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">129</td>
<td align="right">6.9%</td>
<td align="right">127</td>
<td align="right">7.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">569</td>
<td align="right">30.6%</td>
<td align="right">568</td>
<td align="right">31.8%</td>
<td align="right">-0.2%</td>
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
<td align="right">2,190</td>
<td align="right">100.0%</td>
<td align="right">2,162</td>
<td align="right">100.0%</td>
<td align="right">-1.3%</td>
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
<td align="right">85,572,182</td>
<td align="right">100.0%</td>
<td align="right">42,678,269</td>
<td align="right">99.9%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,990</td>
<td align="right">0.0%</td>
<td align="right">3,921</td>
<td align="right">0.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,183</td>
<td align="right">0.0%</td>
<td align="right">17,097</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
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
<td align="right">12,349</td>
<td align="right">100.0%</td>
<td align="right">12,144</td>
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
<td align="right">588</td>
<td align="right">46.7%</td>
<td align="right">588</td>
<td align="right">46.7%</td>
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
<td align="right">672</td>
<td align="right">100.0%</td>
<td align="right">672</td>
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
<td align="right">1,403,982</td>
<td align="right">47.5%</td>
<td align="right">699,839</td>
<td align="right">47.1%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,551,652</td>
<td align="right">52.5%</td>
<td align="right">783,074</td>
<td align="right">52.7%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">210</td>
<td align="right">0.0%</td>
<td align="right">210</td>
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
<td align="right">994</td>
<td align="right">56.8%</td>
<td align="right">820</td>
<td align="right">52.0%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">756</td>
<td align="right">43.2%</td>
<td align="right">756</td>
<td align="right">48.0%</td>
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
<td align="right">634</td>
<td align="right">63.8%</td>
<td align="right">462</td>
<td align="right">56.3%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">4.3%</td>
<td align="right">42</td>
<td align="right">5.1%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">233</td>
<td align="right">23.4%</td>
<td align="right">232</td>
<td align="right">28.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">63</td>
<td align="right">6.3%</td>
<td align="right">63</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">21</td>
<td align="right">2.1%</td>
<td align="right">21</td>
<td align="right">2.6%</td>
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
<td align="right">7,771,789</td>
<td align="right">99.9%</td>
<td align="right">3,362,298</td>
<td align="right">99.8%</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,949</td>
<td align="right">0.1%</td>
<td align="right">5,902</td>
<td align="right">0.2%</td>
<td align="right">-0.8%</td>
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
<td align="right">677</td>
<td align="right">80.1%</td>
<td align="right">672</td>
<td align="right">80.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">168</td>
<td align="right">19.9%</td>
<td align="right">168</td>
<td align="right">20.0%</td>
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
<td align="right">43</td>
<td align="right">6.4%</td>
<td align="right">42</td>
<td align="right">6.2%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">465</td>
<td align="right">68.7%</td>
<td align="right">462</td>
<td align="right">68.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">169</td>
<td align="right">25.0%</td>
<td align="right">168</td>
<td align="right">25.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">15,675,115</td>
<td align="right">16.2%</td>
<td align="right">5,996,106</td>
<td align="right">13.0%</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,757</td>
<td align="right">0.0%</td>
<td align="right">811</td>
<td align="right">0.0%</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">80,856,426</td>
<td align="right">83.8%</td>
<td align="right">40,273,916</td>
<td align="right">87.0%</td>
<td align="right">-50.2%</td>
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
<td align="right">6,533</td>
<td align="right">87.1%</td>
<td align="right">4,082</td>
<td align="right">80.8%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">969</td>
<td align="right">12.9%</td>
<td align="right">967</td>
<td align="right">19.2%</td>
<td align="right">-0.2%</td>
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
<td align="right">1,501</td>
<td align="right">23.0%</td>
<td align="right">652</td>
<td align="right">16.0%</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">780</td>
<td align="right">11.9%</td>
<td align="right">441</td>
<td align="right">10.8%</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,714</td>
<td align="right">26.2%</td>
<td align="right">1,053</td>
<td align="right">25.8%</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">172</td>
<td align="right">2.6%</td>
<td align="right">106</td>
<td align="right">2.6%</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1,437</td>
<td align="right">22.0%</td>
<td align="right">926</td>
<td align="right">22.7%</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">63</td>
<td align="right">1.0%</td>
<td align="right">42</td>
<td align="right">1.0%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">213</td>
<td align="right">3.3%</td>
<td align="right">210</td>
<td align="right">5.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">317</td>
<td align="right">4.9%</td>
<td align="right">316</td>
<td align="right">7.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">210</td>
<td align="right">3.2%</td>
<td align="right">210</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">105</td>
<td align="right">1.6%</td>
<td align="right">105</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
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
<td align="right">5,985,286</td>
<td align="right">5,985,286 / 0 !!</td>
<td align="right">2,976,369</td>
<td align="right">2,976,369 / 0 !!</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">766,746</td>
<td align="right">766,746 / 0 !!</td>
<td align="right">381,773</td>
<td align="right">381,773 / 0 !!</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">4,209,754</td>
<td align="right">4,209,754 / 0 !!</td>
<td align="right">2,097,412</td>
<td align="right">2,097,412 / 0 !!</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">387,077</td>
<td align="right">387,077 / 0 !!</td>
<td align="right">194,378</td>
<td align="right">194,378 / 0 !!</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">323</td>
<td align="right">323 / 0 !!</td>
<td align="right">318</td>
<td align="right">318 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,093</td>
<td align="right">3,093 / 0 !!</td>
<td align="right">3,047</td>
<td align="right">3,047 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,185</td>
<td align="right">2,185 / 0 !!</td>
<td align="right">2,157</td>
<td align="right">2,157 / 0 !!</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">84</td>
<td align="right">84 / 0 !!</td>
<td align="right">84</td>
<td align="right">84 / 0 !!</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">45,724,760</td>
<td align="right">78.3%</td>
<td align="right">22,360,385</td>
<td align="right">77.9%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,650,798</td>
<td align="right">21.7%</td>
<td align="right">6,312,467</td>
<td align="right">22.0%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,168</td>
<td align="right">0.0%</td>
<td align="right">4,106</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">6,781</td>
<td align="right">41.8%</td>
<td align="right">4,921</td>
<td align="right">34.3%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,429</td>
<td align="right">58.2%</td>
<td align="right">9,429</td>
<td align="right">65.7%</td>
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
<td align="left">class method obj</td>
<td align="right">4,506</td>
<td align="right">66.5%</td>
<td align="right">2,968</td>
<td align="right">60.3%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,263</td>
<td align="right">18.6%</td>
<td align="right">945</td>
<td align="right">19.2%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">380</td>
<td align="right">5.6%</td>
<td align="right">378</td>
<td align="right">7.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">337</td>
<td align="right">5.0%</td>
<td align="right">336</td>
<td align="right">6.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">168</td>
<td align="right">2.5%</td>
<td align="right">168</td>
<td align="right">3.4%</td>
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
<td align="right">169,502,366</td>
<td align="right">100.0%</td>
<td align="right">82,620,806</td>
<td align="right">100.0%</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,900</td>
<td align="right">0.0%</td>
<td align="right">1,871</td>
<td align="right">0.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">10,500</td>
<td align="right">0.0%</td>
<td align="right">10,500</td>
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
<td align="right">10,668</td>
<td align="right">100.0%</td>
<td align="right">10,668</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">300</td>
<td align="right">78.1%</td>
<td align="right">296</td>
<td align="right">77.9%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">42</td>
<td align="right">10.9%</td>
<td align="right">42</td>
<td align="right">11.1%</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
<td align="right">42</td>
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
<td align="right">4,750</td>
<td align="right">12.4%</td>
<td align="right">4,350</td>
<td align="right">12.1%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">30,179</td>
<td align="right">78.9%</td>
<td align="right">28,405</td>
<td align="right">78.9%</td>
<td align="right">-5.9%</td>
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
<td align="right">547</td>
<td align="right">16.5%</td>
<td align="right">462</td>
<td align="right">14.3%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,772</td>
<td align="right">83.5%</td>
<td align="right">2,772</td>
<td align="right">85.7%</td>
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
<td align="right">210</td>
<td align="right">38.4%</td>
<td align="right">126</td>
<td align="right">27.3%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">22</td>
<td align="right">4.0%</td>
<td align="right">21</td>
<td align="right">4.5%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">315</td>
<td align="right">57.6%</td>
<td align="right">315</td>
<td align="right">68.2%</td>
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
<td align="right">254</td>
<td align="right">100.0%</td>
<td align="right">-1.6%</td>
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
<td align="right">4,206,788</td>
<td align="right">100.0%</td>
<td align="right">2,093,987</td>
<td align="right">100.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">756</td>
<td align="right">0.0%</td>
<td align="right">756</td>
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
<td align="right">252</td>
<td align="right">100.0%</td>
<td align="right">252</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,980,193</td>
<td align="right">73.5%</td>
<td align="right">18,351,927</td>
<td align="right">72.4%</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">673,802</td>
<td align="right">1.3%</td>
<td align="right">334,593</td>
<td align="right">1.3%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,324,946</td>
<td align="right">25.1%</td>
<td align="right">6,623,312</td>
<td align="right">26.1%</td>
<td align="right">-50.3%</td>
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
<td align="right">68,063</td>
<td align="right">81.5%</td>
<td align="right">34,486</td>
<td align="right">79.2%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,472</td>
<td align="right">18.5%</td>
<td align="right">9,072</td>
<td align="right">20.8%</td>
<td align="right">-41.4%</td>
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
<td align="right">65,019</td>
<td align="right">95.5%</td>
<td align="right">32,508</td>
<td align="right">94.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">105</td>
<td align="right">0.2%</td>
<td align="right">63</td>
<td align="right">0.2%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,897</td>
<td align="right">4.3%</td>
<td align="right">1,873</td>
<td align="right">5.4%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">0.1%</td>
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
<td align="right">27,236,525</td>
<td align="right">100.0%</td>
<td align="right">11,733,080</td>
<td align="right">100.0%</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,518</td>
<td align="right">0.0%</td>
<td align="right">1,512</td>
<td align="right">0.0%</td>
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
<td align="right">106</td>
<td align="right">10.3%</td>
<td align="right">105</td>
<td align="right">10.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">924</td>
<td align="right">89.7%</td>
<td align="right">924</td>
<td align="right">89.8%</td>
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
<td align="right">106</td>
<td align="right">100.0%</td>
<td align="right">105</td>
<td align="right">100.0%</td>
<td align="right">-0.9%</td>
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
<td align="right">54,598,099</td>
<td align="right">2.5%</td>
<td align="right">24,931,480</td>
<td align="right">2.3%</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">720,850,818</td>
<td align="right">32.8%</td>
<td align="right">351,192,058</td>
<td align="right">32.8%</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,422,613,458</td>
<td align="right">64.7%</td>
<td align="right">693,586,689</td>
<td align="right">64.8%</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">686,730</td>
<td align="right">0.0%</td>
<td align="right">346,415</td>
<td align="right">0.0%</td>
<td align="right">-49.6%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">15,675,115</td>
<td align="right">36.4%</td>
<td align="right">5,996,106</td>
<td align="right">30.4%</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">13,324,946</td>
<td align="right">30.9%</td>
<td align="right">6,623,312</td>
<td align="right">33.6%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,403,982</td>
<td align="right">3.3%</td>
<td align="right">699,839</td>
<td align="right">3.6%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,650,798</td>
<td align="right">29.3%</td>
<td align="right">6,312,467</td>
<td align="right">32.1%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">4,750</td>
<td align="right">0.0%</td>
<td align="right">4,350</td>
<td align="right">0.0%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">19,089</td>
<td align="right">0.0%</td>
<td align="right">18,414</td>
<td align="right">0.1%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,190</td>
<td align="right">0.0%</td>
<td align="right">2,162</td>
<td align="right">0.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,949</td>
<td align="right">0.0%</td>
<td align="right">5,902</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,183</td>
<td align="right">0.0%</td>
<td align="right">17,097</td>
<td align="right">0.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">10,500</td>
<td align="right">0.0%</td>
<td align="right">10,500</td>
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
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,674</td>
<td align="right">0.2%</td>
<td align="right">781</td>
<td align="right">0.2%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">673,100</td>
<td align="right">98.0%</td>
<td align="right">333,900</td>
<td align="right">96.4%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">577</td>
<td align="right">0.1%</td>
<td align="right">533</td>
<td align="right">0.2%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">323</td>
<td align="right">0.0%</td>
<td align="right">315</td>
<td align="right">0.1%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">856</td>
<td align="right">0.1%</td>
<td align="right">842</td>
<td align="right">0.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,866</td>
<td align="right">0.6%</td>
<td align="right">3,808</td>
<td align="right">1.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,044</td>
<td align="right">0.2%</td>
<td align="right">1,029</td>
<td align="right">0.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,119</td>
<td align="right">0.5%</td>
<td align="right">3,094</td>
<td align="right">0.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">588</td>
<td align="right">0.1%</td>
<td align="right">588</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">315</td>
<td align="right">0.0%</td>
<td align="right">315</td>
<td align="right">0.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">16,802,934</td>
<td align="right">14.1%</td>
<td align="right">8,353,656</td>
<td align="right">14.1%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,202,424</td>
<td align="right">3.5%</td>
<td align="right">2,090,232</td>
<td align="right">3.5%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">97,563,493</td>
<td align="right">81.9%</td>
<td align="right">48,531,497</td>
<td align="right">81.9%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">38,636,538</td>
<td align="right">32.4%</td>
<td align="right">19,299,525</td>
<td align="right">32.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">21,513,264</td>
<td align="right">18.1%</td>
<td align="right">10,756,107</td>
<td align="right">18.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">21,513,264</td>
<td align="right">18.1%</td>
<td align="right">10,756,107</td>
<td align="right">18.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,710,330</td>
<td align="right">4.0%</td>
<td align="right">2,402,451</td>
<td align="right">4.1%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">507,528</td>
<td align="right">0.4%</td>
<td align="right">311,841</td>
<td align="right">0.5%</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">553</td>
<td align="right">0.0%</td>
<td align="right">359</td>
<td align="right">0.0%</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,321</td>
<td align="right">0.0%</td>
<td align="right">1,117</td>
<td align="right">0.0%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">8,565</td>
<td align="right">0.0%</td>
<td align="right">8,455</td>
<td align="right">0.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">3,847</td>
<td align="right">0.0%</td>
<td align="right">3,843</td>
<td align="right">0.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">378</td>
<td align="right">0.0%</td>
<td align="right">378</td>
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
<td align="left">Mortal increfs</td>
<td align="right">255,645,638</td>
<td align="right">30.8%</td>
<td align="right">127,399,152</td>
<td align="right">30.6%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">249,701,076</td>
<td align="right">27.9%</td>
<td align="right">124,586,677</td>
<td align="right">27.8%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">25,720,319</td>
<td align="right"></td>
<td align="right">12,848,248</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">563,097,921</td>
<td align="right">62.9%</td>
<td align="right">281,808,202</td>
<td align="right">62.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">67,584,821</td>
<td align="right"></td>
<td align="right">33,832,021</td>
<td align="right"></td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">67,586,143</td>
<td align="right">66.7%</td>
<td align="right">33,833,450</td>
<td align="right">66.5%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">475,739,163</td>
<td align="right">57.4%</td>
<td align="right">238,250,836</td>
<td align="right">57.3%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">8,736,537</td>
<td align="right"></td>
<td align="right">4,380,522</td>
<td align="right"></td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">39,825,421</td>
<td align="right"></td>
<td align="right">19,969,598</td>
<td align="right"></td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">2,189,381</td>
<td align="right">0.2%</td>
<td align="right">1,098,213</td>
<td align="right">0.2%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">12,762,344</td>
<td align="right">1.5%</td>
<td align="right">6,420,098</td>
<td align="right">1.5%</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">33,750,629</td>
<td align="right">33.3%</td>
<td align="right">17,027,388</td>
<td align="right">33.5%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">33,758,137</td>
<td align="right">33.3%</td>
<td align="right">17,034,298</td>
<td align="right">33.5%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">79,622,988</td>
<td align="right">8.9%</td>
<td align="right">40,422,356</td>
<td align="right">9.0%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">85,138,790</td>
<td align="right">10.3%</td>
<td align="right">44,037,514</td>
<td align="right">10.6%</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,885</td>
<td align="right"></td>
<td align="right">3,287</td>
<td align="right"></td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,775</td>
<td align="right"></td>
<td align="right">3,003</td>
<td align="right"></td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">2,786</td>
<td align="right">0.0%</td>
<td align="right">2,558</td>
<td align="right">0.0%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">4,722</td>
<td align="right">0.0%</td>
<td align="right">4,352</td>
<td align="right">0.0%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">16,951</td>
<td align="right"></td>
<td align="right">16,020</td>
<td align="right"></td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">15,214</td>
<td align="right"></td>
<td align="right">14,822</td>
<td align="right"></td>
<td align="right">-2.6%</td>
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
<td align="right">826</td>
<td align="right">37,008</td>
<td align="right">10,305,697</td>
<td align="right">555,198</td>
<td align="right">1,585,048</td>
<td align="right">442</td>
<td align="right">35,925</td>
<td align="right">4,089,242</td>
<td align="right">79,691</td>
<td align="right">798,493</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-14
