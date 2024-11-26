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
<td align="right">761,080</td>
<td align="right">1,952,377</td>
<td align="right">156.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">23,012,771</td>
<td align="right">52,719,663</td>
<td align="right">129.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">164,551</td>
<td align="right">157</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,427</td>
<td align="right">142</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,690,363</td>
<td align="right">12,435</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">165,611</td>
<td align="right">856</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,611,034</td>
<td align="right">93,045</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">215,365</td>
<td align="right">9,361</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,343,269</td>
<td align="right">103,399</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,688</td>
<td align="right">499</td>
<td align="right">-91.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,664,972</td>
<td align="right">555,440</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">3,932,112</td>
<td align="right">518,617</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">19,651</td>
<td align="right">4,207</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,198,483</td>
<td align="right">259,260</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">67,336</td>
<td align="right">15,684</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">231,437</td>
<td align="right">53,928</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">506,822</td>
<td align="right">135,483</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">553,256</td>
<td align="right">153,971</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,182,959</td>
<td align="right">2,912,433</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">223,694</td>
<td align="right">71,857</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">6,688,849</td>
<td align="right">2,166,577</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,765,922</td>
<td align="right">936,920</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,532,515</td>
<td align="right">2,267,431</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">134,132</td>
<td align="right">47,669</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">329,925</td>
<td align="right">120,786</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,947,816</td>
<td align="right">2,561,487</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,760,062</td>
<td align="right">660,303</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">284,623</td>
<td align="right">106,962</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">42,341,873</td>
<td align="right">16,102,872</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">280,550</td>
<td align="right">109,103</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">280,943</td>
<td align="right">109,368</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">946,423</td>
<td align="right">372,877</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,242,403</td>
<td align="right">901,612</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,105,923</td>
<td align="right">449,662</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,606,114</td>
<td align="right">2,313,528</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">288,746</td>
<td align="right">129,958</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">23,317,502</td>
<td align="right">10,556,859</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,566,587</td>
<td align="right">736,458</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,913,495</td>
<td align="right">902,708</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,076,730</td>
<td align="right">997,977</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,748,553</td>
<td align="right">4,316,832</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,685,373</td>
<td align="right">836,425</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,909,727</td>
<td align="right">975,562</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,752,002</td>
<td align="right">11,345,365</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,125,698</td>
<td align="right">590,451</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">77,082</td>
<td align="right">40,540</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">429,900</td>
<td align="right">230,604</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,569,042</td>
<td align="right">1,388,351</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">135,679,503</td>
<td align="right">76,209,060</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,838,524</td>
<td align="right">4,501,633</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">13,000,485</td>
<td align="right">7,593,419</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,424,716</td>
<td align="right">2,012,341</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">615,739</td>
<td align="right">364,725</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">8,391,453</td>
<td align="right">4,986,697</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,306,381</td>
<td align="right">1,966,048</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">5,900,493</td>
<td align="right">3,513,075</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">71,391</td>
<td align="right">43,392</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,689,145</td>
<td align="right">6,604,866</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20,977,846</td>
<td align="right">13,172,309</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,484,207</td>
<td align="right">2,194,627</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">31,918,237</td>
<td align="right">20,115,974</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">37,743,391</td>
<td align="right">23,880,920</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,469,923</td>
<td align="right">1,596,668</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,473,187</td>
<td align="right">1,610,935</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,659,499</td>
<td align="right">1,100,042</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">582,821</td>
<td align="right">389,267</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">868,404</td>
<td align="right">581,622</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">965,577</td>
<td align="right">657,992</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">23,486,039</td>
<td align="right">16,120,027</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,454,696</td>
<td align="right">1,001,402</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,471,373</td>
<td align="right">1,019,725</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">479,948</td>
<td align="right">334,929</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,536,992</td>
<td align="right">3,169,398</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">11,049</td>
<td align="right">7,741</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,898,071</td>
<td align="right">1,330,295</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">622,316</td>
<td align="right">436,849</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">12,253,007</td>
<td align="right">8,636,244</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,368,475</td>
<td align="right">2,375,838</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,141,475</td>
<td align="right">825,528</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">25,882,219</td>
<td align="right">18,836,337</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,293,273</td>
<td align="right">2,413,858</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">524</td>
<td align="right">386</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,398,620</td>
<td align="right">1,036,196</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,139,374</td>
<td align="right">847,989</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,795,098</td>
<td align="right">2,084,020</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">422,704</td>
<td align="right">316,827</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,359,776</td>
<td align="right">1,022,271</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">65,624</td>
<td align="right">49,500</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">586,011</td>
<td align="right">443,645</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,052,411</td>
<td align="right">802,304</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,540,541</td>
<td align="right">1,186,150</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,879,475</td>
<td align="right">1,459,093</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">354,890</td>
<td align="right">276,454</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">855,001</td>
<td align="right">675,611</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">19,529,886</td>
<td align="right">15,578,294</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">10,620,677</td>
<td align="right">8,503,427</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">31,277,658</td>
<td align="right">25,306,769</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,391,897</td>
<td align="right">1,134,245</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,042,826</td>
<td align="right">3,343,141</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">956,088</td>
<td align="right">796,625</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">317,979</td>
<td align="right">266,001</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">914,342</td>
<td align="right">770,510</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">18,923</td>
<td align="right">16,003</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">125,727</td>
<td align="right">107,677</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,826,388</td>
<td align="right">1,581,107</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,143,847</td>
<td align="right">1,000,410</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">13,516,296</td>
<td align="right">11,848,784</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">23,949,573</td>
<td align="right">21,046,899</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">83,962</td>
<td align="right">74,991</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">194,032</td>
<td align="right">177,427</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">26,582</td>
<td align="right">24,602</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,471,007</td>
<td align="right">1,384,555</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">818,451</td>
<td align="right">865,245</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">80,285</td>
<td align="right">76,358</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,841,256</td>
<td align="right">1,759,536</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">276,159</td>
<td align="right">265,529</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">36,258</td>
<td align="right">37,370</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">36,447,876</td>
<td align="right">35,353,064</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">28,950</td>
<td align="right">29,816</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">958,024</td>
<td align="right">936,326</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">437,125</td>
<td align="right">427,640</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">117,540</td>
<td align="right">115,148</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">486,466</td>
<td align="right">478,260</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">26,862,811</td>
<td align="right">27,278,849</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">804,130</td>
<td align="right">793,760</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">56,820</td>
<td align="right">56,134</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,591,452</td>
<td align="right">1,580,663</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,150,007</td>
<td align="right">11,103,326</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">255,244</td>
<td align="right">254,562</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,450,312</td>
<td align="right">1,446,888</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">41,671</td>
<td align="right">41,609</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">7,729,270</td>
<td align="right">7,739,717</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">776,155</td>
<td align="right">775,196</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">610,782</td>
<td align="right">611,333</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">19,102,275</td>
<td align="right">19,089,059</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">580,906</td>
<td align="right">581,141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">4,605,114</td>
<td align="right">4,606,808</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">5,081,272</td>
<td align="right">5,079,815</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,585,437</td>
<td align="right">11,585,184</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">4,702,081</td>
<td align="right">4,702,034</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">11,718,303</td>
<td align="right">11,718,303</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,152,475</td>
<td align="right">8,152,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,495,099</td>
<td align="right">6,495,099</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,048,062</td>
<td align="right">1,048,062</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">687,734</td>
<td align="right">687,734</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">611,589</td>
<td align="right">611,589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">118,722</td>
<td align="right">118,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,284</td>
<td align="right">98,284</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,138</td>
<td align="right">56,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,999</td>
<td align="right">41,999</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">26,835</td>
<td align="right">26,835</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">22,914</td>
<td align="right">22,914</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,127</td>
<td align="right">11,127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,023</td>
<td align="right">4,023</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,977</td>
<td align="right">2,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,410</td>
<td align="right">2,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,208</td>
<td align="right">2,208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2,009</td>
<td align="right">2,009</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,149</td>
<td align="right">1,149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,077</td>
<td align="right">1,077</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">935</td>
<td align="right">935</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">913</td>
<td align="right">913</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">780</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">525</td>
<td align="right">525</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">508</td>
<td align="right">508</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">217</td>
<td align="right">217</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">206</td>
<td align="right">206</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">53</td>
<td align="right">53</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">29</td>
<td align="right">29</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">10</td>
<td align="right">10</td>
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
<td align="right">315,240</td>
<td align="right">5.1%</td>
<td align="right">263,444</td>
<td align="right">4.3%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,875,744</td>
<td align="right">94.9%</td>
<td align="right">5,875,744</td>
<td align="right">95.7%</td>
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
<td align="right">2,300</td>
<td align="right">84.0%</td>
<td align="right">2,118</td>
<td align="right">82.8%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">439</td>
<td align="right">16.0%</td>
<td align="right">439</td>
<td align="right">17.2%</td>
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
<td align="left">add different types</td>
<td align="right">91</td>
<td align="right">4.0%</td>
<td align="right">111</td>
<td align="right">5.2%</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">249</td>
<td align="right">10.8%</td>
<td align="right">206</td>
<td align="right">9.7%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">156</td>
<td align="right">6.8%</td>
<td align="right">138</td>
<td align="right">6.5%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,029</td>
<td align="right">44.7%</td>
<td align="right">915</td>
<td align="right">43.2%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">196</td>
<td align="right">8.5%</td>
<td align="right">175</td>
<td align="right">8.3%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">144</td>
<td align="right">6.3%</td>
<td align="right">138</td>
<td align="right">6.5%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">173</td>
<td align="right">7.5%</td>
<td align="right">173</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">120</td>
<td align="right">5.2%</td>
<td align="right">120</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">2.9%</td>
<td align="right">66</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">37</td>
<td align="right">1.6%</td>
<td align="right">37</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">21</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">10</td>
<td align="right">0.4%</td>
<td align="right">10</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">288,746</td>
<td align="right">100.0%</td>
<td align="right">129,958</td>
<td align="right">100.0%</td>
<td align="right">-55.0%</td>
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
<td align="right">1,100,539</td>
<td align="right">9.8%</td>
<td align="right">444,984</td>
<td align="right">4.2%</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,116,521</td>
<td align="right">90.0%</td>
<td align="right">10,116,527</td>
<td align="right">95.6%</td>
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
<td align="right">15,346</td>
<td align="right">0.1%</td>
<td align="right">15,346</td>
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
<td align="right">3,958</td>
<td align="right">69.9%</td>
<td align="right">3,252</td>
<td align="right">65.6%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,704</td>
<td align="right">30.1%</td>
<td align="right">1,704</td>
<td align="right">34.4%</td>
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
<td align="left">buffer slice</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">887</td>
<td align="right">22.4%</td>
<td align="right">619</td>
<td align="right">19.0%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">636</td>
<td align="right">16.1%</td>
<td align="right">447</td>
<td align="right">13.7%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">822</td>
<td align="right">20.8%</td>
<td align="right">632</td>
<td align="right">19.4%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">5</td>
<td align="right">0.2%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">776</td>
<td align="right">19.6%</td>
<td align="right">722</td>
<td align="right">22.2%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">771</td>
<td align="right">19.5%</td>
<td align="right">771</td>
<td align="right">23.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">33</td>
<td align="right">0.8%</td>
<td align="right">33</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">21</td>
<td align="right">0.5%</td>
<td align="right">21</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,078,016</td>
<td align="right">10.4%</td>
<td align="right">6,923,356</td>
<td align="right">10.2%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">60,903,609</td>
<td align="right">89.6%</td>
<td align="right">61,032,055</td>
<td align="right">89.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,876</td>
<td align="right">0.0%</td>
<td align="right">6,876</td>
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
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">8,513</td>
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
<td align="right">164,723</td>
<td align="right">100.0%</td>
<td align="right">155,828</td>
<td align="right">100.0%</td>
<td align="right">-5.4%</td>
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
<td align="left">init not simple</td>
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">35</td>
<td align="right">35 / 0 !!</td>
<td align="right">35</td>
<td align="right">35 / 0 !!</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">517,467</td>
<td align="right">99.5%</td>
<td align="right">199,536</td>
<td align="right">98.8%</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">559</td>
<td align="right">0.1%</td>
<td align="right">559</td>
<td align="right">0.3%</td>
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
<td align="right">2,546</td>
<td align="right">0.0%</td>
<td align="right">2,151</td>
<td align="right">0.0%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">954,120</td>
<td align="right">5.3%</td>
<td align="right">932,443</td>
<td align="right">5.1%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,205,292</td>
<td align="right">94.7%</td>
<td align="right">17,199,837</td>
<td align="right">94.8%</td>
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
<td align="right">2,441</td>
<td align="right">61.7%</td>
<td align="right">2,420</td>
<td align="right">61.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,515</td>
<td align="right">38.3%</td>
<td align="right">1,507</td>
<td align="right">38.4%</td>
<td align="right">-0.5%</td>
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
<td align="right">188</td>
<td align="right">7.7%</td>
<td align="right">208</td>
<td align="right">8.6%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,014</td>
<td align="right">41.5%</td>
<td align="right">953</td>
<td align="right">39.4%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">633</td>
<td align="right">25.9%</td>
<td align="right">654</td>
<td align="right">27.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">237</td>
<td align="right">9.7%</td>
<td align="right">237</td>
<td align="right">9.8%</td>
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
<td align="left">set</td>
<td align="right">90</td>
<td align="right">3.7%</td>
<td align="right">90</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">51</td>
<td align="right">2.1%</td>
<td align="right">51</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">48</td>
<td align="right">2.0%</td>
<td align="right">48</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">18</td>
<td align="right">0.7%</td>
<td align="right">18</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">1,134,712</td>
<td align="right">21.5%</td>
<td align="right">819,452</td>
<td align="right">16.5%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,944</td>
<td align="right">0.5%</td>
<td align="right">26,322</td>
<td align="right">0.5%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,110,971</td>
<td align="right">77.9%</td>
<td align="right">4,113,890</td>
<td align="right">82.8%</td>
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
<td align="right">6,055</td>
<td align="right">83.5%</td>
<td align="right">5,368</td>
<td align="right">81.8%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,198</td>
<td align="right">16.5%</td>
<td align="right">1,198</td>
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
<td align="left">str</td>
<td align="right">1,214</td>
<td align="right">20.0%</td>
<td align="right">768</td>
<td align="right">14.3%</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">512</td>
<td align="right">8.5%</td>
<td align="right">484</td>
<td align="right">9.0%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,171</td>
<td align="right">52.4%</td>
<td align="right">3,000</td>
<td align="right">55.9%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,158</td>
<td align="right">19.1%</td>
<td align="right">1,116</td>
<td align="right">20.8%</td>
<td align="right">-3.6%</td>
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
<td align="right">1,386,447</td>
<td align="right">7.7%</td>
<td align="right">1,129,131</td>
<td align="right">6.7%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,567,810</td>
<td align="right">91.7%</td>
<td align="right">15,706,151</td>
<td align="right">92.7%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">107,506</td>
<td align="right">0.6%</td>
<td align="right">108,282</td>
<td align="right">0.6%</td>
<td align="right">0.7%</td>
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
<td align="right">4,321</td>
<td align="right">58.0%</td>
<td align="right">3,985</td>
<td align="right">55.7%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,133</td>
<td align="right">42.0%</td>
<td align="right">3,172</td>
<td align="right">44.3%</td>
<td align="right">1.2%</td>
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
<td align="left">seq iter</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">815</td>
<td align="right">18.9%</td>
<td align="right">590</td>
<td align="right">14.8%</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">236</td>
<td align="right">5.5%</td>
<td align="right">193</td>
<td align="right">4.8%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,000</td>
<td align="right">23.1%</td>
<td align="right">925</td>
<td align="right">23.2%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">82</td>
<td align="right">1.9%</td>
<td align="right">80</td>
<td align="right">2.0%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,186</td>
<td align="right">27.4%</td>
<td align="right">1,194</td>
<td align="right">30.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">444</td>
<td align="right">10.3%</td>
<td align="right">444</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">231</td>
<td align="right">5.3%</td>
<td align="right">231</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">228</td>
<td align="right">5.3%</td>
<td align="right">228</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">61</td>
<td align="right">1.4%</td>
<td align="right">61</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">25</td>
<td align="right">0.6%</td>
<td align="right">25</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">7</td>
<td align="right">0.2%</td>
<td align="right">7</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">5</td>
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
<td align="right">8,670,327</td>
<td align="right">8.0%</td>
<td align="right">4,254,080</td>
<td align="right">4.3%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,315,347</td>
<td align="right">20.7%</td>
<td align="right">18,046,884</td>
<td align="right">18.4%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">76,867,051</td>
<td align="right">71.2%</td>
<td align="right">75,478,425</td>
<td align="right">77.1%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">207,261</td>
<td align="right">0.2%</td>
<td align="right">207,114</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
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
<td align="right">15,485</td>
<td align="right">3.1%</td>
<td align="right">11,582</td>
<td align="right">2.9%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">479,849</td>
<td align="right">96.9%</td>
<td align="right">388,028</td>
<td align="right">97.1%</td>
<td align="right">-19.1%</td>
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
<td align="left">overridden</td>
<td align="right">488</td>
<td align="right">3.2%</td>
<td align="right">145</td>
<td align="right">1.3%</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">205</td>
<td align="right">1.3%</td>
<td align="right">110</td>
<td align="right">0.9%</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">66</td>
<td align="right">0.4%</td>
<td align="right">36</td>
<td align="right">0.3%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,399</td>
<td align="right">22.0%</td>
<td align="right">2,212</td>
<td align="right">19.1%</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">1.5%</td>
<td align="right">165</td>
<td align="right">1.4%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,241</td>
<td align="right">8.0%</td>
<td align="right">902</td>
<td align="right">7.8%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">4,903</td>
<td align="right">31.7%</td>
<td align="right">3,604</td>
<td align="right">31.1%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,583</td>
<td align="right">10.2%</td>
<td align="right">1,292</td>
<td align="right">11.2%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">343</td>
<td align="right">2.2%</td>
<td align="right">299</td>
<td align="right">2.6%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">852</td>
<td align="right">5.5%</td>
<td align="right">782</td>
<td align="right">6.8%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">58</td>
<td align="right">0.4%</td>
<td align="right">56</td>
<td align="right">0.5%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">835</td>
<td align="right">5.4%</td>
<td align="right">814</td>
<td align="right">7.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">42,725,958</td>
<td align="right">99.9%</td>
<td align="right">24,743,621</td>
<td align="right">99.9%</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,039</td>
<td align="right">0.0%</td>
<td align="right">5,039</td>
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
<td align="right">521</td>
<td align="right">0.0%</td>
<td align="right">521</td>
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
<td align="right">4,500</td>
<td align="right">0.0%</td>
<td align="right">4,500</td>
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
<td align="right">17,949</td>
<td align="right">100.0%</td>
<td align="right">17,949</td>
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
<td align="right">103</td>
<td align="right">0.0%</td>
<td align="right">103</td>
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
<td align="right">718,867</td>
<td align="right">99.9%</td>
<td align="right">718,867</td>
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
<td align="right">422</td>
<td align="right">100.0%</td>
<td align="right">422</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,492,134</td>
<td align="right">54.9%</td>
<td align="right">6,492,134</td>
<td align="right">54.9%</td>
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
<td align="right">5,332,554</td>
<td align="right">45.1%</td>
<td align="right">5,332,554</td>
<td align="right">45.1%</td>
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
<td align="right">104</td>
<td align="right">3.5%</td>
<td align="right">104</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,861</td>
<td align="right">96.5%</td>
<td align="right">2,861</td>
<td align="right">96.5%</td>
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
<td align="right">2,058</td>
<td align="right">71.9%</td>
<td align="right">2,058</td>
<td align="right">71.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">51</td>
<td align="right">1.8%</td>
<td align="right">51</td>
<td align="right">1.8%</td>
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
<td align="right">1,191,439</td>
<td align="right">8.5%</td>
<td align="right">253,423</td>
<td align="right">2.0%</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,960,035</td>
<td align="right">14.0%</td>
<td align="right">1,105,241</td>
<td align="right">8.7%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,823,060</td>
<td align="right">77.4%</td>
<td align="right">11,390,691</td>
<td align="right">89.3%</td>
<td align="right">5.2%</td>
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
<td align="right">2,518</td>
<td align="right">5.7%</td>
<td align="right">1,311</td>
<td align="right">4.9%</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,439</td>
<td align="right">94.3%</td>
<td align="right">25,339</td>
<td align="right">95.1%</td>
<td align="right">-38.9%</td>
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
<td align="right">1,383</td>
<td align="right">54.9%</td>
<td align="right">240</td>
<td align="right">18.3%</td>
<td align="right">-82.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">129</td>
<td align="right">5.1%</td>
<td align="right">103</td>
<td align="right">7.9%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">270</td>
<td align="right">10.7%</td>
<td align="right">230</td>
<td align="right">17.5%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">14</td>
<td align="right">1.1%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">8</td>
<td align="right">0.3%</td>
<td align="right">7</td>
<td align="right">0.5%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">52</td>
<td align="right">4.0%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">29</td>
<td align="right">1.2%</td>
<td align="right">30</td>
<td align="right">2.3%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">401</td>
<td align="right">15.9%</td>
<td align="right">401</td>
<td align="right">30.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">230</td>
<td align="right">9.1%</td>
<td align="right">230</td>
<td align="right">17.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.2%</td>
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
<td align="right">29</td>
<td align="right">100.0%</td>
<td align="right">29</td>
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
<td align="right">79,520</td>
<td align="right">3.0%</td>
<td align="right">75,635</td>
<td align="right">2.8%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,587,628</td>
<td align="right">97.0%</td>
<td align="right">2,587,628</td>
<td align="right">97.1%</td>
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
<td align="right">424</td>
<td align="right">55.4%</td>
<td align="right">382</td>
<td align="right">52.8%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">341</td>
<td align="right">44.6%</td>
<td align="right">341</td>
<td align="right">47.2%</td>
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
<td align="right">47</td>
<td align="right">11.1%</td>
<td align="right">4</td>
<td align="right">1.0%</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">13</td>
<td align="right">3.1%</td>
<td align="right">14</td>
<td align="right">3.7%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">240</td>
<td align="right">56.6%</td>
<td align="right">240</td>
<td align="right">62.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">92</td>
<td align="right">21.7%</td>
<td align="right">92</td>
<td align="right">24.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">26</td>
<td align="right">6.1%</td>
<td align="right">26</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">6</td>
<td align="right">1.4%</td>
<td align="right">6</td>
<td align="right">1.6%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">488,984</td>
<td align="right">1.2%</td>
<td align="right">125,272</td>
<td align="right">0.3%</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,138,064</td>
<td align="right">2.8%</td>
<td align="right">915,221</td>
<td align="right">2.5%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,727,210</td>
<td align="right">95.9%</td>
<td align="right">35,301,130</td>
<td align="right">97.1%</td>
<td align="right">-8.8%</td>
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
<td align="right">10,363</td>
<td align="right">26.6%</td>
<td align="right">2,744</td>
<td align="right">10.1%</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,651</td>
<td align="right">73.4%</td>
<td align="right">24,436</td>
<td align="right">89.9%</td>
<td align="right">-14.7%</td>
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
<td align="right">7,763</td>
<td align="right">74.9%</td>
<td align="right">653</td>
<td align="right">23.8%</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">665</td>
<td align="right">6.4%</td>
<td align="right">393</td>
<td align="right">14.3%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">121</td>
<td align="right">1.2%</td>
<td align="right">78</td>
<td align="right">2.8%</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">541</td>
<td align="right">5.2%</td>
<td align="right">416</td>
<td align="right">15.2%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">27</td>
<td align="right">0.3%</td>
<td align="right">25</td>
<td align="right">0.9%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">325</td>
<td align="right">3.1%</td>
<td align="right">301</td>
<td align="right">11.0%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">871</td>
<td align="right">8.4%</td>
<td align="right">828</td>
<td align="right">30.2%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">50</td>
<td align="right">0.5%</td>
<td align="right">50</td>
<td align="right">1.8%</td>
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
<td align="right">7,960,723</td>
<td align="right">100.0%</td>
<td align="right">7,964,151</td>
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
<td align="right">1,139</td>
<td align="right">0.0%</td>
<td align="right">1,139</td>
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
<td align="right">834</td>
<td align="right">95.9%</td>
<td align="right">834</td>
<td align="right">95.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">36</td>
<td align="right">4.1%</td>
<td align="right">36</td>
<td align="right">4.1%</td>
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
<td align="right">24</td>
<td align="right">66.7%</td>
<td align="right">24</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12</td>
<td align="right">33.3%</td>
<td align="right">12</td>
<td align="right">33.3%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">283,031,675</td>
<td align="right">32.7%</td>
<td align="right">159,186,522</td>
<td align="right">25.6%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">22,288,008</td>
<td align="right">2.6%</td>
<td align="right">15,079,474</td>
<td align="right">2.4%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">526,286,763</td>
<td align="right">60.9%</td>
<td align="right">419,778,947</td>
<td align="right">67.6%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">33,166,374</td>
<td align="right">3.8%</td>
<td align="right">27,348,890</td>
<td align="right">4.4%</td>
<td align="right">-17.5%</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">1,191,439</td>
<td align="right">5.4%</td>
<td align="right">253,423</td>
<td align="right">1.7%</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">488,984</td>
<td align="right">2.2%</td>
<td align="right">125,272</td>
<td align="right">0.8%</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,100,539</td>
<td align="right">5.0%</td>
<td align="right">444,984</td>
<td align="right">3.0%</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">288,746</td>
<td align="right">1.3%</td>
<td align="right">129,958</td>
<td align="right">0.9%</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,670,327</td>
<td align="right">39.2%</td>
<td align="right">4,254,080</td>
<td align="right">28.5%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,134,712</td>
<td align="right">5.1%</td>
<td align="right">819,452</td>
<td align="right">5.5%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,386,447</td>
<td align="right">6.3%</td>
<td align="right">1,129,131</td>
<td align="right">7.6%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">315,240</td>
<td align="right">1.4%</td>
<td align="right">263,444</td>
<td align="right">1.8%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">954,120</td>
<td align="right">4.3%</td>
<td align="right">932,443</td>
<td align="right">6.2%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,492,134</td>
<td align="right">29.4%</td>
<td align="right">6,492,134</td>
<td align="right">43.5%</td>
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
<td align="right">643,793</td>
<td align="right">1.9%</td>
<td align="right">323,192</td>
<td align="right">1.2%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">3,209,252</td>
<td align="right">9.7%</td>
<td align="right">1,668,698</td>
<td align="right">6.1%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,959,972</td>
<td align="right">5.9%</td>
<td align="right">1,105,125</td>
<td align="right">4.0%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,191,748</td>
<td align="right">15.7%</td>
<td align="right">3,857,207</td>
<td align="right">14.1%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">753,126</td>
<td align="right">2.3%</td>
<td align="right">633,756</td>
<td align="right">2.3%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,462,192</td>
<td align="right">4.4%</td>
<td align="right">1,289,218</td>
<td align="right">4.7%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,743,883</td>
<td align="right">35.4%</td>
<td align="right">10,843,573</td>
<td align="right">39.6%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,264,917</td>
<td align="right">3.8%</td>
<td align="right">1,219,960</td>
<td align="right">4.5%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,078,312</td>
<td align="right">15.3%</td>
<td align="right">5,040,778</td>
<td align="right">18.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">480,556</td>
<td align="right">1.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">410,047</td>
<td align="right">1.5%</td>
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
<td align="left">Frame objects created</td>
<td align="right">1,277,686</td>
<td align="right">1.8%</td>
<td align="right">1,276,159</td>
<td align="right">1.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">5,502,262</td>
<td align="right">7.9%</td>
<td align="right">5,501,518</td>
<td align="right">7.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">12,053,480</td>
<td align="right">17.4%</td>
<td align="right">12,052,504</td>
<td align="right">17.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">12,053,480</td>
<td align="right">17.4%</td>
<td align="right">12,052,504</td>
<td align="right">17.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,550,072</td>
<td align="right">9.4%</td>
<td align="right">6,549,840</td>
<td align="right">9.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,551,218</td>
<td align="right">9.4%</td>
<td align="right">6,550,986</td>
<td align="right">9.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">392,014</td>
<td align="right">0.6%</td>
<td align="right">392,017</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">47,800,327</td>
<td align="right">68.9%</td>
<td align="right">47,800,568</td>
<td align="right">68.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">57,342,015</td>
<td align="right">82.6%</td>
<td align="right">57,342,038</td>
<td align="right">82.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">233</td>
<td align="right">0.0%</td>
<td align="right">233</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">913</td>
<td align="right">0.0%</td>
<td align="right">913</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">454,264</td>
<td align="right">0.7%</td>
<td align="right">454,264</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,161,291</td>
<td align="right">1.7%</td>
<td align="right">1,161,291</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">22</td>
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
<td align="left">Mortal increfs</td>
<td align="right">480,047,710</td>
<td align="right">39.6%</td>
<td align="right">645,401,732</td>
<td align="right">50.7%</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">456,547,006</td>
<td align="right">35.2%</td>
<td align="right">596,600,316</td>
<td align="right">42.5%</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">363,383</td>
<td align="right">0.4%</td>
<td align="right">466,300</td>
<td align="right">0.5%</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">147,809,318</td>
<td align="right">12.2%</td>
<td align="right">110,382,232</td>
<td align="right">8.7%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">222,811,155</td>
<td align="right">17.2%</td>
<td align="right">277,006,445</td>
<td align="right">19.8%</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">363,801,389</td>
<td align="right">30.0%</td>
<td align="right">275,939,534</td>
<td align="right">21.7%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">149,418,507</td>
<td align="right">11.5%</td>
<td align="right">121,781,955</td>
<td align="right">8.7%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">469,300,848</td>
<td align="right">36.2%</td>
<td align="right">406,899,002</td>
<td align="right">29.0%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">220,633,019</td>
<td align="right">18.2%</td>
<td align="right">241,047,602</td>
<td align="right">18.9%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">311,459</td>
<td align="right"></td>
<td align="right">288,789</td>
<td align="right"></td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">52,413,091</td>
<td align="right"></td>
<td align="right">49,376,664</td>
<td align="right"></td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,790,578</td>
<td align="right"></td>
<td align="right">1,747,260</td>
<td align="right"></td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,481,019</td>
<td align="right"></td>
<td align="right">1,460,390</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">38,766</td>
<td align="right">0.0%</td>
<td align="right">38,913</td>
<td align="right">0.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">66,710,572</td>
<td align="right"></td>
<td align="right">66,878,018</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">67,990,650</td>
<td align="right">70.7%</td>
<td align="right">68,151,805</td>
<td align="right">70.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">67,588,501</td>
<td align="right">70.3%</td>
<td align="right">67,646,592</td>
<td align="right">70.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">28,614,696</td>
<td align="right"></td>
<td align="right">28,621,082</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">28,154,430</td>
<td align="right"></td>
<td align="right">28,152,456</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">28,133,292</td>
<td align="right">29.3%</td>
<td align="right">28,131,376</td>
<td align="right">29.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,110,313</td>
<td align="right"></td>
<td align="right">1,110,313</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">98,632</td>
<td align="right">8.9%</td>
<td align="right">98,632</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">4,973</td>
<td align="right">0.4%</td>
<td align="right">4,973</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="right">1,324</td>
<td align="right">29,513</td>
<td align="right">173,641,861</td>
<td align="right">1,358</td>
<td align="right">29,900</td>
<td align="right">174,859,627</td>
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
<td align="right">1,135</td>
<td align="right">1.0%</td>
<td align="right">6,746</td>
<td align="right">2.0%</td>
<td align="right">494.4%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">36,085</td>
<td align="right">32.2%</td>
<td align="right">165,051</td>
<td align="right">49.5%</td>
<td align="right">357.4%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">73</td>
<td align="right">0.0%</td>
<td align="right">217.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">81,926</td>
<td align="right">73.0%</td>
<td align="right">245,827</td>
<td align="right">73.8%</td>
<td align="right">200.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">112,198</td>
<td align="right"></td>
<td align="right">333,203</td>
<td align="right"></td>
<td align="right">197.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">30,272</td>
<td align="right">27.0%</td>
<td align="right">87,376</td>
<td align="right">26.2%</td>
<td align="right">188.6%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">637</td>
<td align="right">0.6%</td>
<td align="right">1,610</td>
<td align="right">0.5%</td>
<td align="right">152.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">966,577,709</td>
<td align="right">1,063.5%</td>
<td align="right">1,592,217,175</td>
<td align="right">1,103.0%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">90,884,524</td>
<td align="right"></td>
<td align="right">144,357,652</td>
<td align="right"></td>
<td align="right">58.8%</td>
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
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">126 / 0 !!</td>
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
<td align="right">80,019</td>
<td align="right">97.7%</td>
<td align="right">241,705</td>
<td align="right">98.3%</td>
<td align="right">202.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">81,926</td>
<td align="right"></td>
<td align="right">245,827</td>
<td align="right"></td>
<td align="right">200.1%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">39</td>
<td align="right">0.0%</td>
<td align="right">39.3%</td>
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
<td align="right">686</td>
<td align="right">0.3%</td>
<td align="right">686 / 0 !!</td>
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
<td align="right">16,564</td>
<td align="right">6.7%</td>
<td align="right">16,564 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">9,056</td>
<td align="right">11.1%</td>
<td align="right">18,702</td>
<td align="right">7.6%</td>
<td align="right">106.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">16,446</td>
<td align="right">20.1%</td>
<td align="right">33,932</td>
<td align="right">13.8%</td>
<td align="right">106.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">29,178</td>
<td align="right">35.6%</td>
<td align="right">89,682</td>
<td align="right">36.5%</td>
<td align="right">207.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">21,968</td>
<td align="right">26.8%</td>
<td align="right">60,485</td>
<td align="right">24.6%</td>
<td align="right">175.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,540</td>
<td align="right">5.5%</td>
<td align="right">22,644</td>
<td align="right">9.2%</td>
<td align="right">398.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">608</td>
<td align="right">0.7%</td>
<td align="right">3,618</td>
<td align="right">1.5%</td>
<td align="right">495.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">130</td>
<td align="right">0.2%</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">53.8%</td>
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
<td align="right">6,239</td>
<td align="right">7.6%</td>
<td align="right">30,018</td>
<td align="right">12.2%</td>
<td align="right">381.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">15,740</td>
<td align="right">19.2%</td>
<td align="right">24,908</td>
<td align="right">10.1%</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">10,810</td>
<td align="right">13.2%</td>
<td align="right">52,324</td>
<td align="right">21.3%</td>
<td align="right">384.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">34,090</td>
<td align="right">41.6%</td>
<td align="right">89,464</td>
<td align="right">36.4%</td>
<td align="right">162.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">11,659</td>
<td align="right">14.2%</td>
<td align="right">34,867</td>
<td align="right">14.2%</td>
<td align="right">199.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,349</td>
<td align="right">1.6%</td>
<td align="right">9,593</td>
<td align="right">3.9%</td>
<td align="right">611.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">131</td>
<td align="right">0.2%</td>
<td align="right">530</td>
<td align="right">0.2%</td>
<td align="right">304.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">682</td>
<td align="right">5,110,214</td>
<td align="right">749,198.2%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">84</td>
<td align="right">82,298</td>
<td align="right">97,873.8%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">317</td>
<td align="right">134,434</td>
<td align="right">42,308.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">317</td>
<td align="right">134,434</td>
<td align="right">42,308.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">293</td>
<td align="right">113,383</td>
<td align="right">38,597.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">293</td>
<td align="right">96,013</td>
<td align="right">32,668.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">293</td>
<td align="right">96,013</td>
<td align="right">32,668.9%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">718</td>
<td align="right">194,272</td>
<td align="right">26,957.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">964</td>
<td align="right">172,539</td>
<td align="right">17,798.2%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">964</td>
<td align="right">172,411</td>
<td align="right">17,785.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">1,905</td>
<td align="right">166,299</td>
<td align="right">8,629.6%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">2,818</td>
<td align="right">196,914</td>
<td align="right">6,887.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">18,147</td>
<td align="right">1,227,226</td>
<td align="right">6,662.7%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">116</td>
<td align="right">7,363</td>
<td align="right">6,247.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">43,179</td>
<td align="right">2,581,188</td>
<td align="right">5,877.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">43,144</td>
<td align="right">2,337,969</td>
<td align="right">5,319.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,090,880</td>
<td align="right">35,067,152</td>
<td align="right">3,114.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">150,702</td>
<td align="right">4,560,100</td>
<td align="right">2,925.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">150,702</td>
<td align="right">4,249,811</td>
<td align="right">2,720.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">345</td>
<td align="right">9,316</td>
<td align="right">2,600.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">47,892</td>
<td align="right">1,148,699</td>
<td align="right">2,298.5%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">26,858</td>
<td align="right">600,404</td>
<td align="right">2,135.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">26,858</td>
<td align="right">600,404</td>
<td align="right">2,135.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">221,347</td>
<td align="right">4,476,981</td>
<td align="right">1,922.6%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">99,024</td>
<td align="right">1,928,026</td>
<td align="right">1,847.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">44</td>
<td align="right">726</td>
<td align="right">1,550.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">13,329</td>
<td align="right">190,990</td>
<td align="right">1,332.9%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">1,022</td>
<td align="right">13,968</td>
<td align="right">1,266.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">107,796</td>
<td align="right">1,061,517</td>
<td align="right">884.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">390,115</td>
<td align="right">3,803,610</td>
<td align="right">875.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">36,767</td>
<td align="right">344,352</td>
<td align="right">836.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">156,127</td>
<td align="right">1,370,495</td>
<td align="right">777.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">579,299</td>
<td align="right">4,257,227</td>
<td align="right">634.9%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">88,757</td>
<td align="right">648,214</td>
<td align="right">630.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,575</td>
<td align="right">11,060</td>
<td align="right">602.2%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,251</td>
<td align="right">529,899</td>
<td align="right">577.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">36,038</td>
<td align="right">235,334</td>
<td align="right">553.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">49,846</td>
<td align="right">301,326</td>
<td align="right">504.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">124,432</td>
<td align="right">692,208</td>
<td align="right">456.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">497,411</td>
<td align="right">2,737,281</td>
<td align="right">450.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">721,070</td>
<td align="right">3,915,576</td>
<td align="right">443.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">14,665</td>
<td align="right">66,317</td>
<td align="right">352.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">261,262</td>
<td align="right">1,110,210</td>
<td align="right">324.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">29,555</td>
<td align="right">116,007</td>
<td align="right">292.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">2,409,518</td>
<td align="right">9,116,932</td>
<td align="right">278.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">335,436</td>
<td align="right">1,218,165</td>
<td align="right">263.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">14,345,770</td>
<td align="right">52,003,001</td>
<td align="right">262.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">86,955</td>
<td align="right">312,423</td>
<td align="right">259.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">4,809,349</td>
<td align="right">16,957,104</td>
<td align="right">252.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">2,354,793</td>
<td align="right">8,052,855</td>
<td align="right">242.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">488,672</td>
<td align="right">1,669,363</td>
<td align="right">241.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">311,877</td>
<td align="right">1,024,721</td>
<td align="right">228.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">79,615</td>
<td align="right">257,151</td>
<td align="right">223.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,404,038</td>
<td align="right">4,521,716</td>
<td align="right">222.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">400,773</td>
<td align="right">1,263,026</td>
<td align="right">215.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">41,465</td>
<td align="right">129,271</td>
<td align="right">211.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,421,049</td>
<td align="right">16,764,490</td>
<td align="right">209.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">41,465</td>
<td align="right">128,074</td>
<td align="right">208.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">6,070,196</td>
<td align="right">18,535,998</td>
<td align="right">205.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,674,388</td>
<td align="right">5,014,707</td>
<td align="right">199.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,366,547</td>
<td align="right">6,882,972</td>
<td align="right">190.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">21,613</td>
<td align="right">60,988</td>
<td align="right">182.2%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">90,371</td>
<td align="right">253,048</td>
<td align="right">180.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">2,625,498</td>
<td align="right">7,346,075</td>
<td align="right">179.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">108,533</td>
<td align="right">287,920</td>
<td align="right">165.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,928,636</td>
<td align="right">5,035,814</td>
<td align="right">161.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">23,164</td>
<td align="right">53,748</td>
<td align="right">132.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">3,622,711</td>
<td align="right">7,820,137</td>
<td align="right">115.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,173,297</td>
<td align="right">2,514,309</td>
<td align="right">114.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,350,885</td>
<td align="right">2,841,381</td>
<td align="right">110.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,379,851</td>
<td align="right">4,972,562</td>
<td align="right">108.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">5,394,684</td>
<td align="right">11,204,122</td>
<td align="right">107.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,442,980</td>
<td align="right">7,059,746</td>
<td align="right">105.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,601,324</td>
<td align="right">3,268,836</td>
<td align="right">104.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">9,761,623</td>
<td align="right">19,912,481</td>
<td align="right">104.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,360,399</td>
<td align="right">2,762,819</td>
<td align="right">103.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,406,733</td>
<td align="right">2,774,324</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">994,823</td>
<td align="right">1,946,659</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">645,844</td>
<td align="right">1,257,798</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">7,717,706</td>
<td align="right">15,028,715</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">23,876,015</td>
<td align="right">46,403,887</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">49,092,671</td>
<td align="right">93,324,776</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">320,122</td>
<td align="right">606,904</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">6,912,700</td>
<td align="right">13,037,290</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">459,596</td>
<td align="right">57,015</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,147,516</td>
<td align="right">2,151,957</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">2,740,713</td>
<td align="right">5,128,131</td>
<td align="right">87.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">186,518</td>
<td align="right">345,306</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">3,148,924</td>
<td align="right">5,823,482</td>
<td align="right">84.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">654,145</td>
<td align="right">1,189,392</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,741,649</td>
<td align="right">6,730,942</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">120,306</td>
<td align="right">213,965</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">37,439</td>
<td align="right">65,438</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">16,481,789</td>
<td align="right">28,739,452</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">190</td>
<td align="right">328</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">223,903</td>
<td align="right">383,366</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,575,626</td>
<td align="right">2,654,386</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">807</td>
<td align="right">256</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,065,348</td>
<td align="right">1,776,426</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">6,215</td>
<td align="right">10,100</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">75,677</td>
<td align="right">122,358</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">75,924,985</td>
<td align="right">122,222,742</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">14,765,938</td>
<td align="right">23,529,969</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">90,884,524</td>
<td align="right">144,357,652</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">96,179,473</td>
<td align="right">148,675,097</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">55,492,102</td>
<td align="right">85,602,771</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">341,193</td>
<td align="right">526,179</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">14,313,399</td>
<td align="right">6,576,410</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,019,376</td>
<td align="right">4,599,797</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">3,883,145</td>
<td align="right">5,912,913</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">19,934</td>
<td align="right">30,304</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">32,075</td>
<td align="right">48,680</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">9,351,909</td>
<td align="right">13,947,638</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">12,443,893</td>
<td align="right">18,450,248</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">79,905,298</td>
<td align="right">117,643,133</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">10,306,379</td>
<td align="right">15,169,366</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">791,660</td>
<td align="right">1,157,381</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">590,379</td>
<td align="right">862,761</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">11,849,792</td>
<td align="right">17,282,065</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">788,019</td>
<td align="right">1,145,691</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">465,593</td>
<td align="right">674,732</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">14,493,186</td>
<td align="right">20,495,468</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">7,646,902</td>
<td align="right">10,712,966</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">4,963</td>
<td align="right">6,943</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">13,864,127</td>
<td align="right">19,337,808</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">1,161,234</td>
<td align="right">1,581,613</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">6,670,452</td>
<td align="right">8,821,724</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">34,116</td>
<td align="right">44,905</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,739,064</td>
<td align="right">3,554,560</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,522,634</td>
<td align="right">4,564,680</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">109,033</td>
<td align="right">136,555</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">61,808</td>
<td align="right">77,009</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">3,990,897</td>
<td align="right">4,956,144</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">871,701</td>
<td align="right">1,077,705</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">6,409,722</td>
<td align="right">7,921,004</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">2,797,429</td>
<td align="right">3,452,984</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,060,181</td>
<td align="right">7,472,556</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">4,018,724</td>
<td align="right">4,953,112</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,664,170</td>
<td align="right">3,260,244</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,283,630</td>
<td align="right">1,565,417</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">255,703</td>
<td align="right">310,105</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">9,017</td>
<td align="right">7,112</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">8,123,848</td>
<td align="right">9,807,698</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">12,248</td>
<td align="right">14,640</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">233</td>
<td align="right">188</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">5,294,949</td>
<td align="right">4,317,445</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">34,900,246</td>
<td align="right">41,324,213</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">4,858,234</td>
<td align="right">5,737,648</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,717,929</td>
<td align="right">5,561,646</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,875,227</td>
<td align="right">5,734,458</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">951,307</td>
<td align="right">1,110,793</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">17,837,822</td>
<td align="right">20,719,086</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">12,166,733</td>
<td align="right">14,059,199</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,069,476</td>
<td align="right">1,221,766</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">4,019,602</td>
<td align="right">4,588,364</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">7,139,494</td>
<td align="right">8,136,211</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">2,276,146</td>
<td align="right">2,591,543</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">134,466</td>
<td align="right">152,516</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">134,466</td>
<td align="right">152,516</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,776,349</td>
<td align="right">1,558,193</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,226,712</td>
<td align="right">2,495,797</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">561</td>
<td align="right">623</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,317,879</td>
<td align="right">1,462,898</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">416,813</td>
<td align="right">459,331</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">978,055</td>
<td align="right">1,067,271</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">693</td>
<td align="right">755</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">1,604,783</td>
<td align="right">1,747,415</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,382,206</td>
<td align="right">1,503,490</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">39,407</td>
<td align="right">42,718</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">39,441</td>
<td align="right">42,751</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,775,737</td>
<td align="right">7,330,376</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">1,786,773</td>
<td align="right">1,929,672</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,961,731</td>
<td align="right">2,105,563</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,220,131</td>
<td align="right">1,134,884</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,738,248</td>
<td align="right">1,844,125</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">11,936,539</td>
<td align="right">12,640,199</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">11,956,723</td>
<td align="right">12,659,644</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,491,191</td>
<td align="right">4,748,521</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">9,267,017</td>
<td align="right">9,742,956</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,013,341</td>
<td align="right">1,065,137</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">5,933,405</td>
<td align="right">6,215,103</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,796,450</td>
<td align="right">7,049,985</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">5,541,203</td>
<td align="right">5,706,652</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">2,636,216</td>
<td align="right">2,711,819</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">426,849</td>
<td align="right">437,148</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">49,794</td>
<td align="right">48,682</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">528,979</td>
<td align="right">518,532</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">488,826</td>
<td align="right">486,490</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">187,767</td>
<td align="right">186,901</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">6,284,839</td>
<td align="right">6,302,604</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">727,440</td>
<td align="right">725,746</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,236,545</td>
<td align="right">1,236,545</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">824</td>
<td align="right">824</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">754</td>
<td align="right">754</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">520</td>
<td align="right">520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">130</td>
<td align="right">130</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">399,285</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right"></td>
<td align="right">223,829</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">164,755</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right"></td>
<td align="right">82,212</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">78,436</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">72,285</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">37,646</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">36,542</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right"></td>
<td align="right">17,370</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right"></td>
<td align="right">15,444</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right"></td>
<td align="right">13,324</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">12,266</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">5,189</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">2,977</td>
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
<td align="left">CALL_KW</td>
<td align="right">2</td>
<td align="right">82</td>
<td align="right">4,000.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">437</td>
<td align="right">4,717</td>
<td align="right">979.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">127</td>
<td align="right">699</td>
<td align="right">450.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,075</td>
<td align="right">2,311</td>
<td align="right">115.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,623</td>
<td align="right">8,282</td>
<td align="right">25.0%</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">15</td>
<td align="right">19</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">15</td>
<td align="right">19</td>
<td align="right">26.7%</td>
</tr>
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
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
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
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
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
