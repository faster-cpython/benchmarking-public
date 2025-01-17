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
<td align="right">3,545</td>
<td align="right">25,195</td>
<td align="right">610.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">356,608</td>
<td align="right">58</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">356,612</td>
<td align="right">62</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">178,306</td>
<td align="right">31</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">204,659</td>
<td align="right">184</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">792,543</td>
<td align="right">1,047</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">415,695</td>
<td align="right">795</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,259,957</td>
<td align="right">20,245</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">210,826</td>
<td align="right">771</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">352,414</td>
<td align="right">1,366</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">367,616</td>
<td align="right">1,481</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">179,052</td>
<td align="right">815</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">885,870</td>
<td align="right">4,357</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">179,425</td>
<td align="right">1,012</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">179,458</td>
<td align="right">1,239</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">252,304</td>
<td align="right">1,878</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">368,347</td>
<td align="right">2,766</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">180,141</td>
<td align="right">1,858</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">56,170</td>
<td align="right">677</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">190,784</td>
<td align="right">2,724</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">353,386</td>
<td align="right">8,092</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,347,344</td>
<td align="right">8,540,302</td>
<td align="right">96.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,738</td>
<td align="right">74</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">78,345</td>
<td align="right">4,035</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">74,202</td>
<td align="right">4,787</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">17,870</td>
<td align="right">1,395</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">498,822</td>
<td align="right">73,069</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,137,244</td>
<td align="right">181,798</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">701,833</td>
<td align="right">123,774</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">590,967</td>
<td align="right">110,838</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">874,244</td>
<td align="right">184,025</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">808,087</td>
<td align="right">183,803</td>
<td align="right">-77.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">793,799</td>
<td align="right">186,897</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,328,497</td>
<td align="right">787,432</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">889,609</td>
<td align="right">252,450</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,599,704</td>
<td align="right">463,466</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">6,219</td>
<td align="right">1,962</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">577,784</td>
<td align="right">183,618</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">902,397</td>
<td align="right">301,017</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">959</td>
<td align="right">350</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,191,717</td>
<td align="right">1,936,081</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">7,832,614</td>
<td align="right">3,000,272</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">453,458</td>
<td align="right">183,440</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,028</td>
<td align="right">444</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,145,977</td>
<td align="right">505,790</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,450,530</td>
<td align="right">671,780</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,744,774</td>
<td align="right">1,802,283</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">4,782</td>
<td align="right">2,365</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">24</td>
<td align="right">12</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,139,782</td>
<td align="right">3,084,511</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">472,635</td>
<td align="right">250,790</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,119,059</td>
<td align="right">3,839,923</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,968,303</td>
<td align="right">1,607,233</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">459,178</td>
<td align="right">250,051</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,548</td>
<td align="right">3,141</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,591,663</td>
<td align="right">1,468,680</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60,630,513</td>
<td align="right">34,855,481</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,766,961</td>
<td align="right">1,639,858</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,486,482</td>
<td align="right">892,356</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,786,895</td>
<td align="right">2,910,219</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,180,700</td>
<td align="right">9,890,805</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">27,489,606</td>
<td align="right">17,488,865</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">848,790</td>
<td align="right">555,428</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">23,419,120</td>
<td align="right">15,526,129</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,086,910</td>
<td align="right">2,709,936</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,108,762</td>
<td align="right">2,725,829</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">6</td>
<td align="right">4</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,581,585</td>
<td align="right">3,816,759</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">6,294,553</td>
<td align="right">4,376,800</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,099,292</td>
<td align="right">2,213,277</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">104</td>
<td align="right">76</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">199,747</td>
<td align="right">147,155</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,964,488</td>
<td align="right">1,466,697</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,338,154</td>
<td align="right">2,509,427</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">69</td>
<td align="right">54</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">22,423,889</td>
<td align="right">18,436,694</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">3,145</td>
<td align="right">2,611</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,650,640</td>
<td align="right">2,233,332</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,251,502</td>
<td align="right">2,750,685</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">1,392,628</td>
<td align="right">1,188,948</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">4,665</td>
<td align="right">4,056</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,723,438</td>
<td align="right">1,514,541</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,769,057</td>
<td align="right">1,563,468</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">149</td>
<td align="right">134</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">608,819</td>
<td align="right">557,276</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">861,124</td>
<td align="right">793,520</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,884</td>
<td align="right">1,758</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">30</td>
<td align="right">28</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">33</td>
<td align="right">31</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">67</td>
<td align="right">63</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">327</td>
<td align="right">309</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">3,471,170</td>
<td align="right">3,300,904</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">109</td>
<td align="right">105</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">119</td>
<td align="right">115</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,799,609</td>
<td align="right">5,608,083</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">67</td>
<td align="right">65</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">68</td>
<td align="right">66</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,159</td>
<td align="right">5,989</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">522</td>
<td align="right">514</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">815,805</td>
<td align="right">806,442</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">204</td>
<td align="right">202</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">418</td>
<td align="right">414</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,579</td>
<td align="right">2,602</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">367,676</td>
<td align="right">366,019</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,840</td>
<td align="right">1,834</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,484,264</td>
<td align="right">5,499,697</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">845,328</td>
<td align="right">843,213</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">2,619</td>
<td align="right">2,617</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,155,713</td>
<td align="right">6,157,349</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">558,425</td>
<td align="right">558,384</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,174,551</td>
<td align="right">1,174,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">553,348</td>
<td align="right">553,348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">358,568</td>
<td align="right">358,568</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">201,477</td>
<td align="right">201,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">179,064</td>
<td align="right">179,064</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,454</td>
<td align="right">3,454</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">2,306</td>
<td align="right">2,306</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,032</td>
<td align="right">2,032</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,669</td>
<td align="right">1,669</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">586</td>
<td align="right">586</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">583</td>
<td align="right">583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">565</td>
<td align="right">565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">326</td>
<td align="right">326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">218</td>
<td align="right">218</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">108</td>
<td align="right">108</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">93</td>
<td align="right">93</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">78</td>
<td align="right">78</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">77</td>
<td align="right">77</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">68</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">66</td>
<td align="right">66</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">65</td>
<td align="right">65</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">48</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">39</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">32</td>
<td align="right">32</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">31</td>
<td align="right">31</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">10</td>
<td align="right">10</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">9</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">73,806</td>
<td align="right">1.6%</td>
<td align="right">4,461</td>
<td align="right">0.1%</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,439,463</td>
<td align="right">98.4%</td>
<td align="right">4,439,463</td>
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
<td align="left">Failure</td>
<td align="right">268</td>
<td align="right">67.7%</td>
<td align="right">198</td>
<td align="right">60.7%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">128</td>
<td align="right">32.3%</td>
<td align="right">128</td>
<td align="right">39.3%</td>
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
<td align="left">xor</td>
<td align="right">51</td>
<td align="right">19.0%</td>
<td align="right">5</td>
<td align="right">2.5%</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">47</td>
<td align="right">17.5%</td>
<td align="right">26</td>
<td align="right">13.1%</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">44</td>
<td align="right">16.4%</td>
<td align="right">43</td>
<td align="right">21.7%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">71</td>
<td align="right">26.5%</td>
<td align="right">71</td>
<td align="right">35.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">48</td>
<td align="right">17.9%</td>
<td align="right">48</td>
<td align="right">24.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3</td>
<td align="right">1.1%</td>
<td align="right">3</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">2</td>
<td align="right">1.0%</td>
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
<td align="right">498,822</td>
<td align="right">100.0%</td>
<td align="right">73,069</td>
<td align="right">100.0%</td>
<td align="right">-85.4%</td>
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
<td align="right">2,763,935</td>
<td align="right">19.9%</td>
<td align="right">1,637,296</td>
<td align="right">12.8%</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,149,596</td>
<td align="right">80.1%</td>
<td align="right">11,149,596</td>
<td align="right">87.2%</td>
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
<td align="right">1,705</td>
<td align="right">0.0%</td>
<td align="right">1,705</td>
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
<td align="right">1,863</td>
<td align="right">61.0%</td>
<td align="right">1,399</td>
<td align="right">54.0%</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,192</td>
<td align="right">39.0%</td>
<td align="right">1,192</td>
<td align="right">46.0%</td>
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
<td align="right">228</td>
<td align="right">12.2%</td>
<td align="right">21</td>
<td align="right">1.5%</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">194</td>
<td align="right">10.4%</td>
<td align="right">101</td>
<td align="right">7.2%</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">6</td>
<td align="right">0.3%</td>
<td align="right">4</td>
<td align="right">0.3%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">167</td>
<td align="right">9.0%</td>
<td align="right">121</td>
<td align="right">8.6%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,267</td>
<td align="right">68.0%</td>
<td align="right">1,151</td>
<td align="right">82.3%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
<td align="right">1,421,056</td>
<td align="right">7.5%</td>
<td align="right">1,181,752</td>
<td align="right">6.2%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,456,242</td>
<td align="right">92.5%</td>
<td align="right">17,831,937</td>
<td align="right">93.8%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">578</td>
<td align="right">0.0%</td>
<td align="right">578</td>
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
<td align="right">29,699</td>
<td align="right">100.0%</td>
<td align="right">25,201</td>
<td align="right">100.0%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
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
<td align="left">init not inline values</td>
<td align="right">24</td>
<td align="right">800.0%</td>
<td align="right">24</td>
<td align="right">800.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">3</td>
<td align="right">100.0%</td>
<td align="right">3</td>
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
<td align="right">10</td>
<td align="right">16.7%</td>
<td align="right">10</td>
<td align="right">16.7%</td>
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
<td align="right">700,515</td>
<td align="right">5.0%</td>
<td align="right">122,696</td>
<td align="right">0.9%</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,580</td>
<td align="right">0.1%</td>
<td align="right">7,553</td>
<td align="right">0.1%</td>
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
<td align="right">13,258,309</td>
<td align="right">94.9%</td>
<td align="right">13,258,309</td>
<td align="right">99.0%</td>
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
<td align="right">851</td>
<td align="right">58.8%</td>
<td align="right">611</td>
<td align="right">50.7%</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">596</td>
<td align="right">41.2%</td>
<td align="right">595</td>
<td align="right">49.3%</td>
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
<td align="left">tuple</td>
<td align="right">78</td>
<td align="right">9.2%</td>
<td align="right">5</td>
<td align="right">0.8%</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">479</td>
<td align="right">56.3%</td>
<td align="right">312</td>
<td align="right">51.1%</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">127</td>
<td align="right">14.9%</td>
<td align="right">127</td>
<td align="right">20.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">91</td>
<td align="right">10.7%</td>
<td align="right">91</td>
<td align="right">14.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">70</td>
<td align="right">8.2%</td>
<td align="right">70</td>
<td align="right">11.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6</td>
<td align="right">0.7%</td>
<td align="right">6</td>
<td align="right">1.0%</td>
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
<td align="right">458,213</td>
<td align="right">11.9%</td>
<td align="right">249,176</td>
<td align="right">6.8%</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,404,651</td>
<td align="right">88.1%</td>
<td align="right">3,404,651</td>
<td align="right">93.2%</td>
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
<td align="right">719</td>
<td align="right">74.5%</td>
<td align="right">629</td>
<td align="right">71.9%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">246</td>
<td align="right">25.5%</td>
<td align="right">246</td>
<td align="right">28.1%</td>
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
<td align="right">2</td>
<td align="right">0.3%</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">66</td>
<td align="right">9.2%</td>
<td align="right">45</td>
<td align="right">7.2%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">225</td>
<td align="right">31.3%</td>
<td align="right">157</td>
<td align="right">25.0%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">426</td>
<td align="right">59.2%</td>
<td align="right">426</td>
<td align="right">67.7%</td>
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
<td align="right">415,431</td>
<td align="right">28.8%</td>
<td align="right">693</td>
<td align="right">0.1%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,028,892</td>
<td align="right">71.2%</td>
<td align="right">806,475</td>
<td align="right">99.9%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18</td>
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
<td align="right">249</td>
<td align="right">94.3%</td>
<td align="right">87</td>
<td align="right">85.3%</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15</td>
<td align="right">5.7%</td>
<td align="right">15</td>
<td align="right">14.7%</td>
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
<td align="left">reversed list</td>
<td align="right">123</td>
<td align="right">49.4%</td>
<td align="right">8</td>
<td align="right">9.2%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">76</td>
<td align="right">30.5%</td>
<td align="right">29</td>
<td align="right">33.3%</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">17.3%</td>
<td align="right">43</td>
<td align="right">49.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6</td>
<td align="right">2.4%</td>
<td align="right">6</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">1.1%</td>
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
<td align="right">2,583,631</td>
<td align="right">4.1%</td>
<td align="right">1,461,169</td>
<td align="right">2.4%</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,840</td>
<td align="right">0.0%</td>
<td align="right">7,084</td>
<td align="right">0.0%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">60,116,067</td>
<td align="right">95.9%</td>
<td align="right">60,116,751</td>
<td align="right">97.6%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">2,765</td>
<td align="right">34.2%</td>
<td align="right">2,412</td>
<td align="right">31.9%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,318</td>
<td align="right">65.8%</td>
<td align="right">5,150</td>
<td align="right">68.1%</td>
<td align="right">-3.2%</td>
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
<td align="right">282</td>
<td align="right">10.2%</td>
<td align="right">68</td>
<td align="right">2.8%</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,813</td>
<td align="right">65.6%</td>
<td align="right">1,723</td>
<td align="right">71.4%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">140</td>
<td align="right">5.1%</td>
<td align="right">139</td>
<td align="right">5.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">241</td>
<td align="right">8.7%</td>
<td align="right">241</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">21</td>
<td align="right">0.9%</td>
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
<td align="right">10,446,980</td>
<td align="right">100.0%</td>
<td align="right">4,626,779</td>
<td align="right">99.9%</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">243</td>
<td align="right">0.0%</td>
<td align="right">243</td>
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
<td align="right">576</td>
<td align="right">0.0%</td>
<td align="right">576</td>
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
<td align="right">1,789</td>
<td align="right">100.0%</td>
<td align="right">1,789</td>
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
<td align="right">3</td>
<td align="right">1.2%</td>
<td align="right">3</td>
<td align="right">1.2%</td>
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
<td align="right">193</td>
<td align="right">74.5%</td>
<td align="right">193</td>
<td align="right">74.5%</td>
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
<td align="right">63</td>
<td align="right">100.0%</td>
<td align="right">63</td>
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
<td align="right">575,582</td>
<td align="right">7.8%</td>
<td align="right">181,621</td>
<td align="right">2.6%</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,839,539</td>
<td align="right">92.1%</td>
<td align="right">6,839,539</td>
<td align="right">97.3%</td>
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
<td align="right">7,463</td>
<td align="right">0.1%</td>
<td align="right">7,463</td>
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
<td align="left">Failure</td>
<td align="right">626</td>
<td align="right">27.3%</td>
<td align="right">421</td>
<td align="right">20.2%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,666</td>
<td align="right">72.7%</td>
<td align="right">1,666</td>
<td align="right">79.8%</td>
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
<td align="right">249</td>
<td align="right">39.8%</td>
<td align="right">86</td>
<td align="right">20.4%</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">176</td>
<td align="right">28.1%</td>
<td align="right">134</td>
<td align="right">31.8%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">180</td>
<td align="right">28.8%</td>
<td align="right">180</td>
<td align="right">42.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">21</td>
<td align="right">3.4%</td>
<td align="right">21</td>
<td align="right">5.0%</td>
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
<td align="right">181</td>
<td align="right">0.0%</td>
<td align="right">163</td>
<td align="right">0.0%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,506,213</td>
<td align="right">100.0%</td>
<td align="right">1,506,213</td>
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
<td align="right">143</td>
<td align="right">97.9%</td>
<td align="right">143</td>
<td align="right">97.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3</td>
<td align="right">2.1%</td>
<td align="right">3</td>
<td align="right">2.1%</td>
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
<td align="left">bytearray int</td>
<td align="right">2</td>
<td align="right">66.7%</td>
<td align="right">2</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">33.3%</td>
<td align="right">1</td>
<td align="right">33.3%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">26,760</td>
<td align="right">0.2%</td>
<td align="right">1,160</td>
<td align="right">0.0%</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,249,895</td>
<td align="right">23.7%</td>
<td align="right">2,749,238</td>
<td align="right">21.6%</td>
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
<td align="right">10,418,677</td>
<td align="right">76.1%</td>
<td align="right">9,959,025</td>
<td align="right">78.4%</td>
<td align="right">-4.4%</td>
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
<td align="right">1,138</td>
<td align="right">53.7%</td>
<td align="right">650</td>
<td align="right">44.2%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">981</td>
<td align="right">46.3%</td>
<td align="right">821</td>
<td align="right">55.8%</td>
<td align="right">-16.3%</td>
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
<td align="right">74</td>
<td align="right">7.5%</td>
<td align="right">4</td>
<td align="right">0.5%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">122</td>
<td align="right">12.4%</td>
<td align="right">53</td>
<td align="right">6.5%</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">69</td>
<td align="right">7.0%</td>
<td align="right">48</td>
<td align="right">5.8%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">692</td>
<td align="right">70.5%</td>
<td align="right">692</td>
<td align="right">84.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">24</td>
<td align="right">2.4%</td>
<td align="right">24</td>
<td align="right">2.9%</td>
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
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">11</td>
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
<td align="right">376,903</td>
<td align="right">100.0%</td>
<td align="right">376,903</td>
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
<td align="right">51</td>
<td align="right">100.0%</td>
<td align="right">51</td>
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
<td align="right">112,209,558</td>
<td align="right">37.8%</td>
<td align="right">61,548,868</td>
<td align="right">32.6%</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,343,641</td>
<td align="right">3.8%</td>
<td align="right">6,501,300</td>
<td align="right">3.4%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">172,074,892</td>
<td align="right">57.9%</td>
<td align="right">119,418,064</td>
<td align="right">63.3%</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,473,189</td>
<td align="right">0.5%</td>
<td align="right">1,207,470</td>
<td align="right">0.6%</td>
<td align="right">-18.0%</td>
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
<td align="right">415,431</td>
<td align="right">3.7%</td>
<td align="right">693</td>
<td align="right">0.0%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">73,806</td>
<td align="right">0.7%</td>
<td align="right">4,461</td>
<td align="right">0.1%</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">498,822</td>
<td align="right">4.4%</td>
<td align="right">73,069</td>
<td align="right">1.1%</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">700,515</td>
<td align="right">6.2%</td>
<td align="right">122,696</td>
<td align="right">1.9%</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">575,582</td>
<td align="right">5.1%</td>
<td align="right">181,621</td>
<td align="right">2.8%</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">458,213</td>
<td align="right">4.0%</td>
<td align="right">249,176</td>
<td align="right">3.8%</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,583,631</td>
<td align="right">22.8%</td>
<td align="right">1,461,169</td>
<td align="right">22.5%</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,763,935</td>
<td align="right">24.4%</td>
<td align="right">1,637,296</td>
<td align="right">25.3%</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,249,895</td>
<td align="right">28.7%</td>
<td align="right">2,749,238</td>
<td align="right">42.4%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">578</td>
<td align="right">0.0%</td>
<td align="right">578</td>
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
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">145,644</td>
<td align="right">9.9%</td>
<td align="right">3,731</td>
<td align="right">0.3%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,608</td>
<td align="right">0.3%</td>
<td align="right">4,104</td>
<td align="right">0.3%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,133,463</td>
<td align="right">76.9%</td>
<td align="right">1,036,072</td>
<td align="right">85.8%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">7,580</td>
<td align="right">0.5%</td>
<td align="right">7,553</td>
<td align="right">0.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">137,770</td>
<td align="right">9.4%</td>
<td align="right">137,770</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,521</td>
<td align="right">0.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">12,987</td>
<td align="right">0.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,628</td>
<td align="right">0.4%</td>
<td align="right">5,628</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,156</td>
<td align="right">0.3%</td>
<td align="right">4,156</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,238</td>
<td align="right">0.2%</td>
<td align="right">2,238</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,835</td>
<td align="right">0.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,688</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">201,558</td>
<td align="right">1.7%</td>
<td align="right">201,558</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">11,830,928</td>
<td align="right">98.3%</td>
<td align="right">11,830,928</td>
<td align="right">98.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">201,558</td>
<td align="right">1.7%</td>
<td align="right">201,558</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">201,549</td>
<td align="right">1.7%</td>
<td align="right">201,549</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">201,515</td>
<td align="right">1.7%</td>
<td align="right">201,515</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">7,476</td>
<td align="right">0.1%</td>
<td align="right">7,476</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">132</td>
<td align="right">0.0%</td>
<td align="right">132</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">179,060</td>
<td align="right">1.5%</td>
<td align="right">179,060</td>
<td align="right">1.5%</td>
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
<td align="right">76</td>
<td align="right">0.0%</td>
<td align="right">76</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">11,658,134</td>
<td align="right">96.9%</td>
<td align="right">11,658,134</td>
<td align="right">96.9%</td>
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
<td align="right">5,838</td>
<td align="right"></td>
<td align="right">915</td>
<td align="right"></td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">81,916,458</td>
<td align="right">24.5%</td>
<td align="right">134,818,912</td>
<td align="right">38.4%</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">99,347,948</td>
<td align="right">31.1%</td>
<td align="right">163,302,230</td>
<td align="right">50.4%</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">43,719,369</td>
<td align="right">13.1%</td>
<td align="right">62,486,180</td>
<td align="right">17.8%</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">122,803,890</td>
<td align="right">38.4%</td>
<td align="right">72,327,487</td>
<td align="right">22.3%</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">50,551,205</td>
<td align="right">15.8%</td>
<td align="right">36,917,828</td>
<td align="right">11.4%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">151,563,014</td>
<td align="right">45.4%</td>
<td align="right">112,140,962</td>
<td align="right">31.9%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">56,507,734</td>
<td align="right">16.9%</td>
<td align="right">42,039,508</td>
<td align="right">12.0%</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">13,942</td>
<td align="right"></td>
<td align="right">10,393</td>
<td align="right"></td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">8,397</td>
<td align="right"></td>
<td align="right">9,788</td>
<td align="right"></td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">47,022,100</td>
<td align="right">14.7%</td>
<td align="right">51,393,808</td>
<td align="right">15.9%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">111,527</td>
<td align="right">0.7%</td>
<td align="right">112,573</td>
<td align="right">0.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">900,652</td>
<td align="right"></td>
<td align="right">905,275</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,605,407</td>
<td align="right"></td>
<td align="right">3,602,534</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,695,891</td>
<td align="right"></td>
<td align="right">10,698,294</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,753,540</td>
<td align="right">71.7%</td>
<td align="right">11,755,076</td>
<td align="right">71.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,637,508</td>
<td align="right">71.0%</td>
<td align="right">11,637,998</td>
<td align="right">71.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">4,634,440</td>
<td align="right"></td>
<td align="right">4,634,540</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">4,640,030</td>
<td align="right">28.3%</td>
<td align="right">4,640,126</td>
<td align="right">28.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">4,505</td>
<td align="right">0.0%</td>
<td align="right">4,505</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">185,774</td>
<td align="right"></td>
<td align="right">185,774</td>
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
<td align="right">534</td>
<td align="right">818</td>
<td align="right">14,065,385</td>
<td align="right">534</td>
<td align="right">818</td>
<td align="right">14,060,003</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">834</td>
<td align="right">44.5%</td>
<td align="right">3,136</td>
<td align="right">62.9%</td>
<td align="right">276.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">641</td>
<td align="right">34.2%</td>
<td align="right">2,188</td>
<td align="right">43.9%</td>
<td align="right">241.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,874</td>
<td align="right"></td>
<td align="right">4,986</td>
<td align="right"></td>
<td align="right">166.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,233</td>
<td align="right">65.8%</td>
<td align="right">2,798</td>
<td align="right">56.1%</td>
<td align="right">126.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">234,106,981</td>
<td align="right">1,595.0%</td>
<td align="right">465,282,775</td>
<td align="right">1,941.9%</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">14,677,285</td>
<td align="right"></td>
<td align="right">23,960,275</td>
<td align="right"></td>
<td align="right">63.2%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">3 / 0 !!</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">641</td>
<td align="right"></td>
<td align="right">2,188</td>
<td align="right"></td>
<td align="right">241.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">641</td>
<td align="right">100.0%</td>
<td align="right">2,187</td>
<td align="right">100.0%</td>
<td align="right">241.2%</td>
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
<td align="right">7</td>
<td align="right">1.1%</td>
<td align="right">8</td>
<td align="right">0.4%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">12</td>
<td align="right">1.9%</td>
<td align="right">256</td>
<td align="right">11.7%</td>
<td align="right">2,033.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">136</td>
<td align="right">21.2%</td>
<td align="right">967</td>
<td align="right">44.2%</td>
<td align="right">611.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">271</td>
<td align="right">42.3%</td>
<td align="right">576</td>
<td align="right">26.3%</td>
<td align="right">112.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">86</td>
<td align="right">13.4%</td>
<td align="right">313</td>
<td align="right">14.3%</td>
<td align="right">264.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">129</td>
<td align="right">20.1%</td>
<td align="right">68</td>
<td align="right">3.1%</td>
<td align="right">-47.3%</td>
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
<td align="right">5</td>
<td align="right">0.8%</td>
<td align="right">6</td>
<td align="right">0.3%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">8</td>
<td align="right">1.2%</td>
<td align="right">13</td>
<td align="right">0.6%</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8</td>
<td align="right">1.2%</td>
<td align="right">508</td>
<td align="right">23.2%</td>
<td align="right">6,250.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">310</td>
<td align="right">48.4%</td>
<td align="right">982</td>
<td align="right">44.9%</td>
<td align="right">216.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">160</td>
<td align="right">25.0%</td>
<td align="right">518</td>
<td align="right">23.7%</td>
<td align="right">223.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">150</td>
<td align="right">23.4%</td>
<td align="right">160</td>
<td align="right">7.3%</td>
<td align="right">6.7%</td>
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
<td align="left">_BUILD_LIST</td>
<td align="right">22</td>
<td align="right">594,148</td>
<td align="right">2,700,572.7%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">12</td>
<td align="right">178,249</td>
<td align="right">1,485,308.3%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">12</td>
<td align="right">178,249</td>
<td align="right">1,485,308.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">18</td>
<td align="right">204,493</td>
<td align="right">1,135,972.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">69</td>
<td align="right">203,749</td>
<td align="right">295,188.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">99</td>
<td align="right">205,688</td>
<td align="right">207,665.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">556</td>
<td align="right">1,123,018</td>
<td align="right">201,881.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">480</td>
<td align="right">690,699</td>
<td align="right">143,795.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">427</td>
<td align="right">440,711</td>
<td align="right">103,111.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">585</td>
<td align="right">480,767</td>
<td align="right">82,082.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">228</td>
<td align="right">170,494</td>
<td align="right">74,678.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">22</td>
<td align="right">14,822</td>
<td align="right">67,272.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,359</td>
<td align="right">864,926</td>
<td align="right">63,544.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,300</td>
<td align="right">625,584</td>
<td align="right">48,021.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,300</td>
<td align="right">625,584</td>
<td align="right">48,021.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,967</td>
<td align="right">793,463</td>
<td align="right">40,238.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">1,667</td>
<td align="right">641,854</td>
<td align="right">38,403.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">576</td>
<td align="right">209,613</td>
<td align="right">36,291.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,432</td>
<td align="right">481,561</td>
<td align="right">33,528.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">14</td>
<td align="right">4,271</td>
<td align="right">30,407.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">14</td>
<td align="right">4,271</td>
<td align="right">30,407.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">709</td>
<td align="right">209,606</td>
<td align="right">29,463.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">2,143</td>
<td align="right">603,523</td>
<td align="right">28,062.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">866</td>
<td align="right">210,921</td>
<td align="right">24,255.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,260</td>
<td align="right">294,624</td>
<td align="right">23,282.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">48</td>
<td align="right">9,411</td>
<td align="right">19,506.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">2,266</td>
<td align="right">428,019</td>
<td align="right">18,788.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">2,205</td>
<td align="right">397,516</td>
<td align="right">17,927.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,275</td>
<td align="right">206,424</td>
<td align="right">16,090.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,746</td>
<td align="right">252,186</td>
<td align="right">14,343.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,984</td>
<td align="right">348,278</td>
<td align="right">11,571.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">25,780</td>
<td align="right">2,635,113</td>
<td align="right">10,121.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,069</td>
<td align="right">193,568</td>
<td align="right">9,255.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">19,228</td>
<td align="right">1,757,790</td>
<td align="right">9,041.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">4,355</td>
<td align="right">368,986</td>
<td align="right">8,372.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">6,059</td>
<td align="right">423,825</td>
<td align="right">6,895.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">45,242</td>
<td align="right">3,026,094</td>
<td align="right">6,588.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">21,222</td>
<td align="right">1,147,861</td>
<td align="right">5,308.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">6,643</td>
<td align="right">357,691</td>
<td align="right">5,284.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">7,143</td>
<td align="right">373,278</td>
<td align="right">5,125.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">39,284</td>
<td align="right">1,867,525</td>
<td align="right">4,653.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">15,566</td>
<td align="right">652,725</td>
<td align="right">4,093.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">82,990</td>
<td align="right">3,338,626</td>
<td align="right">3,922.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">59,227</td>
<td align="right">2,217,432</td>
<td align="right">3,644.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">180,180</td>
<td align="right">5,012,522</td>
<td align="right">2,682.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">33,143</td>
<td align="right">811,893</td>
<td align="right">2,349.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">21,073</td>
<td align="right">403,338</td>
<td align="right">1,814.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">14,995</td>
<td align="right">193,287</td>
<td align="right">1,189.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">63</td>
<td align="right">672</td>
<td align="right">966.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">63</td>
<td align="right">672</td>
<td align="right">966.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">150,029</td>
<td align="right">1,511,099</td>
<td align="right">907.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">72,578</td>
<td align="right">682,521</td>
<td align="right">840.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">16,646</td>
<td align="right">133,557</td>
<td align="right">702.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,465,665</td>
<td align="right">11,458,879</td>
<td align="right">681.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">129,030</td>
<td align="right">991,287</td>
<td align="right">668.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">3</td>
<td align="right">21</td>
<td align="right">600.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">252,970</td>
<td align="right">1,546,383</td>
<td align="right">511.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">67,506</td>
<td align="right">405,186</td>
<td align="right">500.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">14,962</td>
<td align="right">70,494</td>
<td align="right">371.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">14,962</td>
<td align="right">70,468</td>
<td align="right">371.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">847</td>
<td align="right">3,257</td>
<td align="right">284.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">3,203,197</td>
<td align="right">11,983,198</td>
<td align="right">274.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">6</td>
<td align="right">21</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">6,836,820</td>
<td align="right">22,383,729</td>
<td align="right">227.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">869,057</td>
<td align="right">2,575,838</td>
<td align="right">196.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">116,013</td>
<td align="right">337,857</td>
<td align="right">191.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">116,013</td>
<td align="right">337,840</td>
<td align="right">191.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">67</td>
<td align="right">193</td>
<td align="right">188.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">1,488,311</td>
<td align="right">3,965,514</td>
<td align="right">166.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,812,861</td>
<td align="right">7,078,539</td>
<td align="right">151.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">9,751,201</td>
<td align="right">24,262,138</td>
<td align="right">148.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">469,258</td>
<td align="right">1,160,033</td>
<td align="right">147.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,485,596</td>
<td align="right">3,451,078</td>
<td align="right">132.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,982,949</td>
<td align="right">13,882,801</td>
<td align="right">132.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">977,763</td>
<td align="right">2,257,825</td>
<td align="right">130.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">849,872</td>
<td align="right">1,945,210</td>
<td align="right">128.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,533,246</td>
<td align="right">3,476,346</td>
<td align="right">126.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,533,246</td>
<td align="right">3,476,346</td>
<td align="right">126.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,533,246</td>
<td align="right">3,475,737</td>
<td align="right">126.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">514,421</td>
<td align="right">1,092,266</td>
<td align="right">112.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,054,424</td>
<td align="right">2,235,987</td>
<td align="right">112.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">554,481</td>
<td align="right">1,172,284</td>
<td align="right">111.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,585,362</td>
<td align="right">37,034,900</td>
<td align="right">110.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">394,954</td>
<td align="right">812,262</td>
<td align="right">105.7%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,983,290</td>
<td align="right">3,977,379</td>
<td align="right">100.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">12</td>
<td align="right">24</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">18,140</td>
<td align="right">1,071</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,895,615</td>
<td align="right">5,597,557</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,429,950</td>
<td align="right">2,743,162</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">554,085</td>
<td align="right">1,054,742</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,448,955</td>
<td align="right">6,333,391</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">3,306,643</td>
<td align="right">553,226</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">516,904</td>
<td align="right">931,660</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,895,567</td>
<td align="right">5,037,763</td>
<td align="right">74.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,329</td>
<td align="right">3,999</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">13,995,034</td>
<td align="right">23,928,243</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">18,719,443</td>
<td align="right">31,789,683</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">5,246,183</td>
<td align="right">8,639,738</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">14,677,285</td>
<td align="right">23,960,275</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">15,137,636</td>
<td align="right">24,420,607</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">2,772,092</td>
<td align="right">4,469,767</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">16,741,748</td>
<td align="right">26,742,489</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,450,031</td>
<td align="right">2,294,586</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,856</td>
<td align="right">4,513</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">12,693,288</td>
<td align="right">19,981,786</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">415,091</td>
<td align="right">653,231</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,859,499</td>
<td align="right">4,441,120</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">704</td>
<td align="right">1,089</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">2,753,933</td>
<td align="right">4,130,907</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,753,933</td>
<td align="right">4,130,907</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,775,777</td>
<td align="right">8,596,035</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,355,447</td>
<td align="right">4,738,380</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">3,308,611</td>
<td align="right">4,628,074</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">465,118</td>
<td align="right">650,073</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">9,708,691</td>
<td align="right">12,605,365</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,754,825</td>
<td align="right">3,566,335</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">7,406</td>
<td align="right">9,521</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">393,880</td>
<td align="right">463,225</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,747,368</td>
<td align="right">3,160,071</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,747,368</td>
<td align="right">3,160,071</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">176</td>
<td align="right">153</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,785,518</td>
<td align="right">3,004,685</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,754,685</td>
<td align="right">2,828,995</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">2,746,714</td>
<td align="right">2,814,246</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">915</td>
<td align="right">930</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">893</td>
<td align="right">899</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">1,071</td>
<td align="right">1,077</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">1,071</td>
<td align="right">1,077</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">125,184</td>
<td align="right">125,768</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">125,184</td>
<td align="right">125,768</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,106</td>
<td align="right">1,108</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,753,874</td>
<td align="right">2,756,569</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">124,514</td>
<td align="right">124,573</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">124,037</td>
<td align="right">124,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">460,351</td>
<td align="right">460,332</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">553,314</td>
<td align="right">553,314</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">552,715</td>
<td align="right">552,715</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">924</td>
<td align="right">924</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">442</td>
<td align="right">442</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">7</td>
<td align="right">7</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">497,791</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">393,961</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">356,550</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">356,550</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">178,413</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">178,275</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right"></td>
<td align="right">178,219</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">178,213</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">178,211</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">52,592</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">52,592</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">51,543</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right"></td>
<td align="right">609</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">534</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">170</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">28</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right"></td>
<td align="right">26</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right"></td>
<td align="right">15</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right"></td>
<td align="right">9</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right"></td>
<td align="right">8</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">8</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
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
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right"></td>
<td align="right">3</td>
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
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
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
<td align="left">_CALL_TUPLE_1</td>
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
<td align="left">CALL</td>
<td align="right">455</td>
<td align="right">613</td>
<td align="right">34.7%</td>
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
Stats gathered on: 2024-10-25
