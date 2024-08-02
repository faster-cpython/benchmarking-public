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
<td align="right">1,715,084</td>
<td align="right">9,950,453</td>
<td align="right">480.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">90,628,560</td>
<td align="right">71,208,554</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,152,752</td>
<td align="right">68,537,076</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,143,329,977</td>
<td align="right">1,058,188,379</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">168,763,209</td>
<td align="right">175,917,934</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,664,203</td>
<td align="right">17,929,913</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">115,893,231</td>
<td align="right">112,677,587</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">101,760,578</td>
<td align="right">98,963,987</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">283,480,646</td>
<td align="right">289,782,791</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,582,358,040</td>
<td align="right">1,548,517,656</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">382,901,368</td>
<td align="right">390,027,301</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,598,709</td>
<td align="right">1,569,232</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">366,827,357</td>
<td align="right">373,005,201</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67,888,516</td>
<td align="right">66,784,831</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">80,950,780</td>
<td align="right">79,650,550</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,411,544</td>
<td align="right">48,139,396</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,987,256,251</td>
<td align="right">3,929,224,304</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,042,433</td>
<td align="right">52,291,155</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,298,642,196</td>
<td align="right">2,268,074,468</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">96,871,455</td>
<td align="right">95,784,886</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,693,059</td>
<td align="right">73,488,191</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,905,856,095</td>
<td align="right">4,860,992,517</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,807,064,819</td>
<td align="right">3,773,617,496</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,037,445</td>
<td align="right">191,637,691</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">129,928,345</td>
<td align="right">128,863,127</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,457,798,987</td>
<td align="right">5,417,590,574</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">122,032,690</td>
<td align="right">121,172,430</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,207,137,788</td>
<td align="right">2,192,062,493</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,223,134,255</td>
<td align="right">1,214,872,021</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,884,366,602</td>
<td align="right">4,854,246,338</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">421,090,856</td>
<td align="right">418,591,234</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">195,412,191</td>
<td align="right">194,374,822</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">289,414,997</td>
<td align="right">287,903,069</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">977,951,931</td>
<td align="right">973,089,785</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,086,330,891</td>
<td align="right">3,071,154,322</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">215,810,645</td>
<td align="right">214,792,346</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,915,272,526</td>
<td align="right">18,826,590,098</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">284,905,822</td>
<td align="right">283,611,393</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">6,140,321</td>
<td align="right">6,114,883</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,170,697,019</td>
<td align="right">4,153,420,234</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">697,003,616</td>
<td align="right">694,656,249</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">571,510,606</td>
<td align="right">569,668,059</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">326,498,130</td>
<td align="right">325,492,485</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">382,838,531</td>
<td align="right">381,755,499</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,840,537,530</td>
<td align="right">1,836,646,721</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">75,630,342</td>
<td align="right">75,780,168</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">622,057,373</td>
<td align="right">620,872,314</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">105,633,325</td>
<td align="right">105,456,494</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">343,580,551</td>
<td align="right">343,068,829</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">957,653,865</td>
<td align="right">956,286,756</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,382,093,843</td>
<td align="right">2,378,774,209</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">278,723,539</td>
<td align="right">278,353,277</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">80,686,960</td>
<td align="right">80,581,252</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">6,591,029</td>
<td align="right">6,582,579</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">217,176,869</td>
<td align="right">216,918,556</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">378,451,562</td>
<td align="right">378,008,816</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">506,544,576</td>
<td align="right">506,008,571</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,753,807</td>
<td align="right">1,752,016</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">288,494,834</td>
<td align="right">288,228,830</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">211,237,682</td>
<td align="right">211,043,358</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">472,914,123</td>
<td align="right">472,483,197</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,096,074,320</td>
<td align="right">1,095,117,914</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">39,470,013</td>
<td align="right">39,440,527</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">352,849,776</td>
<td align="right">352,592,947</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,922,593,965</td>
<td align="right">4,919,164,049</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,661,263,669</td>
<td align="right">2,659,418,337</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">886,463,555</td>
<td align="right">885,896,734</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">327,234,894</td>
<td align="right">327,028,157</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">7,454,957</td>
<td align="right">7,450,586</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,340,734</td>
<td align="right">17,332,079</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">214,420</td>
<td align="right">214,315</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">84,644,062</td>
<td align="right">84,602,725</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">246,176,688</td>
<td align="right">246,290,797</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,218,931,613</td>
<td align="right">3,220,376,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,462,315</td>
<td align="right">9,458,077</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">944,995,480</td>
<td align="right">944,583,537</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">150,521,092</td>
<td align="right">150,457,190</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">189,363,126</td>
<td align="right">189,283,963</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">110,523,087</td>
<td align="right">110,488,940</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,461</td>
<td align="right">687,282</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,554,005</td>
<td align="right">158,524,209</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">202,643,640</td>
<td align="right">202,608,806</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">94,606,231</td>
<td align="right">94,621,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,641,597</td>
<td align="right">9,640,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,961,400</td>
<td align="right">48,968,664</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,207,345</td>
<td align="right">9,206,037</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">580,211,745</td>
<td align="right">580,291,933</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">258,546,943</td>
<td align="right">258,582,617</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">414,683,682</td>
<td align="right">414,628,976</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">70,592,365</td>
<td align="right">70,583,421</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,309,434</td>
<td align="right">58,316,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">187,634,420</td>
<td align="right">187,611,655</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">12,963,946</td>
<td align="right">12,962,571</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">12,946,889</td>
<td align="right">12,945,601</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">12,954,649</td>
<td align="right">12,953,361</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">83,860,598</td>
<td align="right">83,854,441</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">33,113,187</td>
<td align="right">33,110,796</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">42,153,538</td>
<td align="right">42,150,605</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,445</td>
<td align="right">15,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,774,346</td>
<td align="right">1,774,232</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">250,940,163</td>
<td align="right">250,925,217</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">134,513,804</td>
<td align="right">134,521,632</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">207,275</td>
<td align="right">207,263</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">1,449,952</td>
<td align="right">1,449,874</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">391,726,765</td>
<td align="right">391,705,753</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,363,601,035</td>
<td align="right">1,363,666,195</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">399,866,447</td>
<td align="right">399,848,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">586,043,825</td>
<td align="right">586,021,167</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">397,030,002</td>
<td align="right">397,016,671</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">12,084,360</td>
<td align="right">12,084,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">372,340,861</td>
<td align="right">372,330,521</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">225,037,084</td>
<td align="right">225,031,088</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">221,378,965</td>
<td align="right">221,374,093</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">356,445,004</td>
<td align="right">356,452,219</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,244</td>
<td align="right">1,873,209</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">143,300,167</td>
<td align="right">143,298,103</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">312,449,879</td>
<td align="right">312,445,486</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,384,000</td>
<td align="right">4,383,948</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">39,854,791</td>
<td align="right">39,854,418</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,064,851</td>
<td align="right">83,064,187</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">31,396,533</td>
<td align="right">31,396,324</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">320,969,445</td>
<td align="right">320,967,365</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,867,626</td>
<td align="right">10,867,683</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">104,828,905</td>
<td align="right">104,829,304</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">104,599,900</td>
<td align="right">104,599,551</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">65,812,461</td>
<td align="right">65,812,261</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,253,060,161</td>
<td align="right">1,253,056,742</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,279,568</td>
<td align="right">20,279,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,580,037</td>
<td align="right">9,580,061</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,102,419</td>
<td align="right">91,102,205</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,642,429</td>
<td align="right">13,642,457</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">22,133,974</td>
<td align="right">22,133,938</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">56,321,099</td>
<td align="right">56,321,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">273,312,233</td>
<td align="right">273,311,854</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">172,973,239</td>
<td align="right">172,973,028</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,693,348</td>
<td align="right">555,692,762</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">355,798,120</td>
<td align="right">355,797,783</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,332,979</td>
<td align="right">1,047,332,041</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">37,815,788</td>
<td align="right">37,815,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">32,498,350</td>
<td align="right">32,498,333</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">184,061,324</td>
<td align="right">184,061,416</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">47,905,878</td>
<td align="right">47,905,897</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,610,588</td>
<td align="right">46,610,604</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">148,276,385</td>
<td align="right">148,276,343</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">33,217,343</td>
<td align="right">33,217,347</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">275,106,737</td>
<td align="right">275,106,710</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,586</td>
<td align="right">173,318,572</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">65,829,453</td>
<td align="right">65,829,448</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">228,622,206</td>
<td align="right">228,622,192</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,022,089</td>
<td align="right">402,022,068</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">49,527,058</td>
<td align="right">49,527,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,211,043</td>
<td align="right">786,211,024</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,305,686</td>
<td align="right">233,305,690</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">105,641,622</td>
<td align="right">105,641,622</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">98,868,760</td>
<td align="right">98,868,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">90,633,700</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,486,661</td>
<td align="right">52,486,661</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,460</td>
<td align="right">38,846,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,760</td>
<td align="right">38,845,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">22,309,441</td>
<td align="right">22,309,441</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">8,000,960</td>
<td align="right">8,000,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,254,160</td>
<td align="right">7,254,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,464,720</td>
<td align="right">3,464,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">2,995,200</td>
<td align="right">2,995,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">719,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">543,600</td>
<td align="right">543,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">474,820</td>
<td align="right">474,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">151,680</td>
<td align="right">151,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">150,560</td>
<td align="right">150,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">141,800</td>
<td align="right">141,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,600</td>
<td align="right">91,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">90,000</td>
<td align="right">90,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">46,620</td>
<td align="right">46,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">25,780</td>
<td align="right">25,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">22,520</td>
<td align="right">22,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,020</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,000</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">68,657,780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT_GENERAL</td>
<td align="right"></td>
<td align="right">1,351,514</td>
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
<td align="right">410,724,808</td>
<td align="right">5.7%</td>
<td align="right">417,494,648</td>
<td align="right">5.8%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,500,860</td>
<td align="right">0.4%</td>
<td align="right">29,130,680</td>
<td align="right">0.4%</td>
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
<td align="right">6,805,209,837</td>
<td align="right">94.3%</td>
<td align="right">6,805,568,073</td>
<td align="right">94.2%</td>
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
<td align="right">590,543</td>
<td align="right">35.2%</td>
<td align="right">583,552</td>
<td align="right">35.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,086,877</td>
<td align="right">64.8%</td>
<td align="right">1,079,781</td>
<td align="right">64.9%</td>
<td align="right">-0.7%</td>
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
<td align="right">37,887</td>
<td align="right">3.5%</td>
<td align="right">29,060</td>
<td align="right">2.7%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">12,300</td>
<td align="right">1.1%</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">14,154</td>
<td align="right">1.3%</td>
<td align="right">14,039</td>
<td align="right">1.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,844</td>
<td align="right">0.8%</td>
<td align="right">8,784</td>
<td align="right">0.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,604</td>
<td align="right">7.5%</td>
<td align="right">81,907</td>
<td align="right">7.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,716</td>
<td align="right">3.4%</td>
<td align="right">36,661</td>
<td align="right">3.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,896</td>
<td align="right">0.2%</td>
<td align="right">1,894</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">12,177</td>
<td align="right">1.1%</td>
<td align="right">12,167</td>
<td align="right">1.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,190</td>
<td align="right">2.7%</td>
<td align="right">29,173</td>
<td align="right">2.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,026</td>
<td align="right">0.5%</td>
<td align="right">5,028</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,605</td>
<td align="right">71.9%</td>
<td align="right">781,610</td>
<td align="right">72.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,096</td>
<td align="right">3.0%</td>
<td align="right">32,096</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,464</td>
<td align="right">1.0%</td>
<td align="right">10,464</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,606</td>
<td align="right">0.8%</td>
<td align="right">8,606</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,528</td>
<td align="right">0.5%</td>
<td align="right">5,528</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


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
<td align="right">416,164,789</td>
<td align="right">8.9%</td>
<td align="right">416,110,098</td>
<td align="right">8.9%</td>
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
<td align="right">1,740,995</td>
<td align="right">0.0%</td>
<td align="right">1,740,963</td>
<td align="right">0.0%</td>
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
<td align="right">4,278,511,076</td>
<td align="right">91.1%</td>
<td align="right">4,278,528,391</td>
<td align="right">91.1%</td>
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
<td align="right">147,787</td>
<td align="right">56.9%</td>
<td align="right">147,739</td>
<td align="right">56.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">112,101</td>
<td align="right">43.1%</td>
<td align="right">112,102</td>
<td align="right">43.1%</td>
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
<td align="right">30,215</td>
<td align="right">20.4%</td>
<td align="right">30,117</td>
<td align="right">20.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">30,708</td>
<td align="right">20.8%</td>
<td align="right">30,758</td>
<td align="right">20.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">43,760</td>
<td align="right">29.6%</td>
<td align="right">43,760</td>
<td align="right">29.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,520</td>
<td align="right">13.2%</td>
<td align="right">19,520</td>
<td align="right">13.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">11.0%</td>
<td align="right">16,200</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">3.6%</td>
<td align="right">5,340</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,060</td>
<td align="right">0.7%</td>
<td align="right">1,060</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">760</td>
<td align="right">0.5%</td>
<td align="right">760</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">286,775,649</td>
<td align="right">2.6%</td>
<td align="right">283,239,465</td>
<td align="right">2.6%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">174,714,280</td>
<td align="right">1.6%</td>
<td align="right">174,381,567</td>
<td align="right">1.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,628,596,946</td>
<td align="right">97.3%</td>
<td align="right">10,632,169,175</td>
<td align="right">97.4%</td>
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
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">28,860</td>
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
<td align="right">73,998</td>
<td align="right">1.9%</td>
<td align="right">66,040</td>
<td align="right">1.7%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,757,864</td>
<td align="right">98.1%</td>
<td align="right">3,753,649</td>
<td align="right">98.3%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">65,678</td>
<td align="right">88.8%</td>
<td align="right">65,700</td>
<td align="right">99.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">7,980</td>
<td align="right">10.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,920</td>
<td align="right">3.9%</td>
<td align="right">2,920</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">580</td>
<td align="right">0.8%</td>
<td align="right">580</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">200</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">97,413,051</td>
<td align="right">2.0%</td>
<td align="right">96,321,345</td>
<td align="right">2.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">734,129</td>
<td align="right">0.0%</td>
<td align="right">727,687</td>
<td align="right">0.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,828,798,621</td>
<td align="right">98.0%</td>
<td align="right">4,828,766,831</td>
<td align="right">98.0%</td>
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
<td align="right">128,645</td>
<td align="right">66.8%</td>
<td align="right">127,454</td>
<td align="right">66.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">63,888</td>
<td align="right">33.2%</td>
<td align="right">63,774</td>
<td align="right">33.3%</td>
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
<td align="left">big int</td>
<td align="right">26,266</td>
<td align="right">20.4%</td>
<td align="right">25,467</td>
<td align="right">20.0%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,640</td>
<td align="right">14.5%</td>
<td align="right">18,360</td>
<td align="right">14.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,321</td>
<td align="right">11.1%</td>
<td align="right">14,225</td>
<td align="right">11.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,540</td>
<td align="right">9.0%</td>
<td align="right">11,528</td>
<td align="right">9.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,423</td>
<td align="right">1.1%</td>
<td align="right">1,424</td>
<td align="right">1.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,619</td>
<td align="right">1.3%</td>
<td align="right">1,620</td>
<td align="right">1.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">24,920</td>
<td align="right">19.4%</td>
<td align="right">24,913</td>
<td align="right">19.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,336</td>
<td align="right">12.7%</td>
<td align="right">16,337</td>
<td align="right">12.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">8.3%</td>
<td align="right">10,680</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,600</td>
<td align="right">1.2%</td>
<td align="right">1,600</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">800</td>
<td align="right">0.6%</td>
<td align="right">800</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">500</td>
<td align="right">0.4%</td>
<td align="right">500</td>
<td align="right">0.4%</td>
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
<td align="right">197,774,242</td>
<td align="right">7.7%</td>
<td align="right">196,737,174</td>
<td align="right">7.7%</td>
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
<td align="right">2,365,993,509</td>
<td align="right">92.3%</td>
<td align="right">2,365,972,804</td>
<td align="right">92.3%</td>
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
<td align="right">2,517,260</td>
<td align="right">0.1%</td>
<td align="right">2,517,260</td>
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
<td align="right">96,550</td>
<td align="right">62.2%</td>
<td align="right">96,248</td>
<td align="right">62.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">58,659</td>
<td align="right">37.8%</td>
<td align="right">58,660</td>
<td align="right">37.9%</td>
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
<td align="right">53,360</td>
<td align="right">55.3%</td>
<td align="right">53,040</td>
<td align="right">55.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,775</td>
<td align="right">13.2%</td>
<td align="right">12,791</td>
<td align="right">13.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">22,035</td>
<td align="right">22.8%</td>
<td align="right">22,037</td>
<td align="right">22.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">8,380</td>
<td align="right">8.7%</td>
<td align="right">8,380</td>
<td align="right">8.7%</td>
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
<td align="right">458,380,355</td>
<td align="right">85.8%</td>
<td align="right">466,278,301</td>
<td align="right">86.0%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">75,637,184</td>
<td align="right">14.2%</td>
<td align="right">75,787,190</td>
<td align="right">14.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">143,279</td>
<td align="right">0.0%</td>
<td align="right">143,513</td>
<td align="right">0.0%</td>
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
<td align="left">Failure</td>
<td align="right">90,473</td>
<td align="right">66.3%</td>
<td align="right">90,520</td>
<td align="right">66.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">45,964</td>
<td align="right">33.7%</td>
<td align="right">45,971</td>
<td align="right">33.7%</td>
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
<td align="right">9,977</td>
<td align="right">11.0%</td>
<td align="right">10,038</td>
<td align="right">11.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,052</td>
<td align="right">10.0%</td>
<td align="right">9,044</td>
<td align="right">10.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">35,864</td>
<td align="right">39.6%</td>
<td align="right">35,858</td>
<td align="right">39.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,720</td>
<td align="right">8.5%</td>
<td align="right">7,720</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,460</td>
<td align="right">7.1%</td>
<td align="right">6,460</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,240</td>
<td align="right">6.9%</td>
<td align="right">6,240</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">4,240</td>
<td align="right">4.7%</td>
<td align="right">4,240</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,580</td>
<td align="right">4.0%</td>
<td align="right">3,580</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,060</td>
<td align="right">3.4%</td>
<td align="right">3,060</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,960</td>
<td align="right">2.2%</td>
<td align="right">1,960</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,220</td>
<td align="right">1.3%</td>
<td align="right">1,220</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">560</td>
<td align="right">0.6%</td>
<td align="right">560</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">320</td>
<td align="right">0.4%</td>
<td align="right">320</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.2%</td>
<td align="right">220</td>
<td align="right">0.2%</td>
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
<td align="right">1,218,663,766</td>
<td align="right">7.9%</td>
<td align="right">1,214,302,554</td>
<td align="right">7.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">246,651,855</td>
<td align="right">1.6%</td>
<td align="right">247,161,031</td>
<td align="right">1.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,258,649,654</td>
<td align="right">92.1%</td>
<td align="right">14,258,457,757</td>
<td align="right">92.1%</td>
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
<td align="right">320,700</td>
<td align="right">0.0%</td>
<td align="right">320,700</td>
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
<td align="right">5,178,308</td>
<td align="right">87.2%</td>
<td align="right">5,187,966</td>
<td align="right">87.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">761,712</td>
<td align="right">12.8%</td>
<td align="right">760,296</td>
<td align="right">12.8%</td>
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
<td align="left">method</td>
<td align="right">75,145</td>
<td align="right">9.9%</td>
<td align="right">74,285</td>
<td align="right">9.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">72,760</td>
<td align="right">9.6%</td>
<td align="right">72,446</td>
<td align="right">9.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">148,673</td>
<td align="right">19.5%</td>
<td align="right">148,404</td>
<td align="right">19.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">44,876</td>
<td align="right">5.9%</td>
<td align="right">44,908</td>
<td align="right">5.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">13,413</td>
<td align="right">1.8%</td>
<td align="right">13,407</td>
<td align="right">1.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">54,088</td>
<td align="right">7.1%</td>
<td align="right">54,078</td>
<td align="right">7.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">250,298</td>
<td align="right">32.9%</td>
<td align="right">250,309</td>
<td align="right">32.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">25,860</td>
<td align="right">3.4%</td>
<td align="right">25,860</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">19,720</td>
<td align="right">2.6%</td>
<td align="right">19,720</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,760</td>
<td align="right">2.1%</td>
<td align="right">15,760</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">13,759</td>
<td align="right">1.8%</td>
<td align="right">13,759</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,200</td>
<td align="right">1.6%</td>
<td align="right">12,200</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,420</td>
<td align="right">0.7%</td>
<td align="right">5,420</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,180</td>
<td align="right">0.7%</td>
<td align="right">5,180</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,800</td>
<td align="right">0.4%</td>
<td align="right">2,800</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">5,167,977,039</td>
<td align="right">99.6%</td>
<td align="right">5,174,062,061</td>
<td align="right">99.6%</td>
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
<td align="right">438,975</td>
<td align="right">0.0%</td>
<td align="right">438,597</td>
<td align="right">0.0%</td>
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
<td align="right">20,287,624</td>
<td align="right">0.4%</td>
<td align="right">20,287,250</td>
<td align="right">0.4%</td>
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
<td align="right">10,680</td>
<td align="right">0.0%</td>
<td align="right">10,680</td>
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
<td align="right">430,919</td>
<td align="right">100.0%</td>
<td align="right">430,970</td>
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
<td align="right">82,755,046</td>
<td align="right">100.0%</td>
<td align="right">82,725,462</td>
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
<td align="right">7,865</td>
<td align="right">0.0%</td>
<td align="right">7,866</td>
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
<td align="right">7,580</td>
<td align="right">100.0%</td>
<td align="right">7,580</td>
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

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NONE family </summary>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NOT_NONE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


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
<td align="right">173,284,246</td>
<td align="right">18.1%</td>
<td align="right">173,284,232</td>
<td align="right">18.1%</td>
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
<td align="right">786,180,383</td>
<td align="right">81.9%</td>
<td align="right">786,180,364</td>
<td align="right">81.9%</td>
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
<td align="right">30,660</td>
<td align="right">0.0%</td>
<td align="right">30,660</td>
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
<td align="right">5,400</td>
<td align="right">8.3%</td>
<td align="right">5,400</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
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
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">55.7%</td>
<td align="right">33,180</td>
<td align="right">55.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,240</td>
<td align="right">23.9%</td>
<td align="right">14,240</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,220</td>
<td align="right">3.7%</td>
<td align="right">2,220</td>
<td align="right">3.7%</td>
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
<td align="right">68,503,901</td>
<td align="right">2.5%</td>
<td align="right">67,595,445</td>
<td align="right">2.4%</td>
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
<td align="right">98,460,531</td>
<td align="right">3.6%</td>
<td align="right">97,569,008</td>
<td align="right">3.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,667,400,321</td>
<td align="right">96.4%</td>
<td align="right">2,667,525,912</td>
<td align="right">96.4%</td>
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
<td align="right">1,377,995</td>
<td align="right">95.7%</td>
<td align="right">1,360,853</td>
<td align="right">95.6%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,908</td>
<td align="right">4.3%</td>
<td align="right">61,908</td>
<td align="right">4.4%</td>
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
<td align="left">non string or split</td>
<td align="right">12,920</td>
<td align="right">20.9%</td>
<td align="right">12,920</td>
<td align="right">20.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">9,800</td>
<td align="right">15.8%</td>
<td align="right">9,800</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,748</td>
<td align="right">15.7%</td>
<td align="right">9,748</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,580</td>
<td align="right">13.9%</td>
<td align="right">8,580</td>
<td align="right">13.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,700</td>
<td align="right">7.6%</td>
<td align="right">4,700</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,600</td>
<td align="right">7.4%</td>
<td align="right">4,600</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,360</td>
<td align="right">7.0%</td>
<td align="right">4,360</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3,800</td>
<td align="right">6.1%</td>
<td align="right">3,800</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">2,480</td>
<td align="right">4.0%</td>
<td align="right">2,480</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">800</td>
<td align="right">1.3%</td>
<td align="right">800</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>


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
<td align="right">817,766,974</td>
<td align="right">93.6%</td>
<td align="right">817,751,741</td>
<td align="right">93.6%</td>
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
<td align="right">56,261,937</td>
<td align="right">6.4%</td>
<td align="right">56,262,017</td>
<td align="right">6.4%</td>
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
<td align="right">10,621</td>
<td align="right">18.0%</td>
<td align="right">10,624</td>
<td align="right">18.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">48,541</td>
<td align="right">82.0%</td>
<td align="right">48,539</td>
<td align="right">82.0%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">7,521</td>
<td align="right">15.5%</td>
<td align="right">7,519</td>
<td align="right">15.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">32,520</td>
<td align="right">67.0%</td>
<td align="right">32,520</td>
<td align="right">67.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">13.3%</td>
<td align="right">6,480</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">900</td>
<td align="right">1.9%</td>
<td align="right">900</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">800</td>
<td align="right">1.6%</td>
<td align="right">800</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">320</td>
<td align="right">0.7%</td>
<td align="right">320</td>
<td align="right">0.7%</td>
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
<td align="right">5,764,695,473</td>
<td align="right">95.5%</td>
<td align="right">5,764,146,512</td>
<td align="right">95.5%</td>
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
<td align="right">272,690,084</td>
<td align="right">4.5%</td>
<td align="right">272,684,589</td>
<td align="right">4.5%</td>
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
<td align="right">48,924,299</td>
<td align="right">0.8%</td>
<td align="right">48,924,846</td>
<td align="right">0.8%</td>
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
<td align="right">171,731</td>
<td align="right">13.5%</td>
<td align="right">171,751</td>
<td align="right">13.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,099,568</td>
<td align="right">86.5%</td>
<td align="right">1,099,594</td>
<td align="right">86.5%</td>
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
<td align="left">number</td>
<td align="right">4,809</td>
<td align="right">2.8%</td>
<td align="right">4,830</td>
<td align="right">2.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,428</td>
<td align="right">2.6%</td>
<td align="right">4,419</td>
<td align="right">2.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">26,823</td>
<td align="right">15.6%</td>
<td align="right">26,835</td>
<td align="right">15.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,207</td>
<td align="right">7.7%</td>
<td align="right">13,202</td>
<td align="right">7.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,115</td>
<td align="right">7.6%</td>
<td align="right">13,117</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">45,989</td>
<td align="right">26.8%</td>
<td align="right">45,988</td>
<td align="right">26.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">47,860</td>
<td align="right">27.9%</td>
<td align="right">47,860</td>
<td align="right">27.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">12,580</td>
<td align="right">7.3%</td>
<td align="right">12,580</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.9%</td>
<td align="right">1,460</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">420</td>
<td align="right">0.2%</td>
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
<td align="right">186,388</td>
<td align="right">0.0%</td>
<td align="right">186,281</td>
<td align="right">0.0%</td>
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
<td align="right">1,491,489,748</td>
<td align="right">100.0%</td>
<td align="right">1,491,612,481</td>
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
<td align="left">Failure</td>
<td align="right">1,776</td>
<td align="right">6.3%</td>
<td align="right">1,774</td>
<td align="right">6.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">26,256</td>
<td align="right">93.7%</td>
<td align="right">26,260</td>
<td align="right">93.7%</td>
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
<td align="right">1,136</td>
<td align="right">64.0%</td>
<td align="right">1,134</td>
<td align="right">63.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">21.4%</td>
<td align="right">380</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.6%</td>
<td align="right">260</td>
<td align="right">14.7%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">56,552,394,746</td>
<td align="right">54.4%</td>
<td align="right">56,197,387,341</td>
<td align="right">54.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">37,044,059,505</td>
<td align="right">35.7%</td>
<td align="right">36,846,952,648</td>
<td align="right">35.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">651,775,011</td>
<td align="right">0.6%</td>
<td align="right">650,666,695</td>
<td align="right">0.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,629,676,084</td>
<td align="right">9.3%</td>
<td align="right">9,619,825,832</td>
<td align="right">9.3%</td>
<td align="right">-0.1%</td>
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
<td align="right">410,724,808</td>
<td align="right">12.4%</td>
<td align="right">417,494,648</td>
<td align="right">12.6%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">286,775,649</td>
<td align="right">8.6%</td>
<td align="right">283,239,465</td>
<td align="right">8.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">97,413,051</td>
<td align="right">2.9%</td>
<td align="right">96,321,345</td>
<td align="right">2.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">98,460,531</td>
<td align="right">3.0%</td>
<td align="right">97,569,008</td>
<td align="right">2.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">197,774,242</td>
<td align="right">5.9%</td>
<td align="right">196,737,174</td>
<td align="right">5.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,218,663,766</td>
<td align="right">36.7%</td>
<td align="right">1,214,302,554</td>
<td align="right">36.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">75,637,184</td>
<td align="right">2.3%</td>
<td align="right">75,787,190</td>
<td align="right">2.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">416,164,789</td>
<td align="right">12.5%</td>
<td align="right">416,110,098</td>
<td align="right">12.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">272,690,084</td>
<td align="right">8.2%</td>
<td align="right">272,684,589</td>
<td align="right">8.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,246</td>
<td align="right">5.2%</td>
<td align="right">173,284,232</td>
<td align="right">5.2%</td>
<td align="right">-0.0%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,280,203</td>
<td align="right">5.9%</td>
<td align="right">42,371,080</td>
<td align="right">5.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">100,608,214</td>
<td align="right">13.8%</td>
<td align="right">101,403,615</td>
<td align="right">13.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">90,768,036</td>
<td align="right">12.4%</td>
<td align="right">90,378,189</td>
<td align="right">12.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">73,023,649</td>
<td align="right">10.0%</td>
<td align="right">72,739,928</td>
<td align="right">10.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,958,299</td>
<td align="right">5.6%</td>
<td align="right">40,956,611</td>
<td align="right">5.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,204,278</td>
<td align="right">3.5%</td>
<td align="right">25,204,945</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">24,452,281</td>
<td align="right">3.4%</td>
<td align="right">24,452,118</td>
<td align="right">3.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,874,518</td>
<td align="right">10.7%</td>
<td align="right">77,874,446</td>
<td align="right">10.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,874,518</td>
<td align="right">10.7%</td>
<td align="right">77,874,446</td>
<td align="right">10.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,481,349</td>
<td align="right">3.8%</td>
<td align="right">27,481,327</td>
<td align="right">3.8%</td>
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
<td align="right">5,649,898,857</td>
<td align="right">70.3%</td>
<td align="right">5,747,025,649</td>
<td align="right">70.7%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,519,756,668</td>
<td align="right">18.9%</td>
<td align="right">1,516,372,134</td>
<td align="right">18.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,524,190,808</td>
<td align="right">19.0%</td>
<td align="right">1,520,806,274</td>
<td align="right">18.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,384,539,940</td>
<td align="right">29.7%</td>
<td align="right">2,381,218,519</td>
<td align="right">29.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,384,539,940</td>
<td align="right">29.7%</td>
<td align="right">2,381,218,519</td>
<td align="right">29.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,330,798,472</td>
<td align="right">78.8%</td>
<td align="right">6,333,911,775</td>
<td align="right">77.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">224,360,838</td>
<td align="right">2.8%</td>
<td align="right">224,333,285</td>
<td align="right">2.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,349,132</td>
<td align="right">10.7%</td>
<td align="right">860,412,245</td>
<td align="right">10.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,554,360</td>
<td align="right">0.9%</td>
<td align="right">71,549,576</td>
<td align="right">0.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">28,576,112</td>
<td align="right">0.4%</td>
<td align="right">28,575,837</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">526,894,179</td>
<td align="right">6.6%</td>
<td align="right">526,893,421</td>
<td align="right">6.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,357,989</td>
<td align="right">2.6%</td>
<td align="right">211,357,954</td>
<td align="right">2.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,411,620</td>
<td align="right">0.1%</td>
<td align="right">4,411,620</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">22,520</td>
<td align="right">0.0%</td>
<td align="right">22,520</td>
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
<td align="right">21,535,064</td>
<td align="right"></td>
<td align="right">25,695,850</td>
<td align="right"></td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">26,223,810</td>
<td align="right"></td>
<td align="right">31,046,876</td>
<td align="right"></td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,092,167</td>
<td align="right"></td>
<td align="right">7,755,544</td>
<td align="right"></td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">45,802,219,079</td>
<td align="right">40.7%</td>
<td align="right">45,488,581,844</td>
<td align="right">40.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">66,635,219,417</td>
<td align="right">59.3%</td>
<td align="right">66,890,334,529</td>
<td align="right">59.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">59,271,792,801</td>
<td align="right">46.1%</td>
<td align="right">59,087,037,901</td>
<td align="right">45.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">69,414,165,447</td>
<td align="right">53.9%</td>
<td align="right">69,537,890,388</td>
<td align="right">54.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,631,652,836</td>
<td align="right"></td>
<td align="right">2,626,984,888</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,103,136,460</td>
<td align="right"></td>
<td align="right">3,099,228,019</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,450,211,476</td>
<td align="right"></td>
<td align="right">6,447,697,853</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,448,446,059</td>
<td align="right">38.5%</td>
<td align="right">6,445,933,249</td>
<td align="right">38.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">149,564,562</td>
<td align="right"></td>
<td align="right">149,547,704</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,672,468</td>
<td align="right">0.6%</td>
<td align="right">103,675,733</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">19,741,864</td>
<td align="right">0.1%</td>
<td align="right">19,741,972</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,157,744,588</td>
<td align="right">60.7%</td>
<td align="right">10,157,725,952</td>
<td align="right">60.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,281,158,920</td>
<td align="right">61.5%</td>
<td align="right">10,281,143,657</td>
<td align="right">61.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,610,033,033</td>
<td align="right"></td>
<td align="right">10,610,034,868</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,271,240</td>
<td align="right">2.2%</td>
<td align="right">3,271,240</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">63,660</td>
<td align="right">0.0%</td>
<td align="right">63,660</td>
<td align="right">0.0%</td>
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
<td align="right">0</td>
<td align="right">18,557,940</td>
<td align="right">14,350,717,695</td>
<td align="right">0</td>
<td align="right">18,555,820</td>
<td align="right">14,343,991,496</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,982,877,628</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,983,549,028</td>
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
<td align="right">686</td>
<td align="right">0.1%</td>
<td align="right">3,520</td>
<td align="right">0.5%</td>
<td align="right">413.1%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,506</td>
<td align="right">0.9%</td>
<td align="right">6,595</td>
<td align="right">0.9%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">632,610</td>
<td align="right">86.4%</td>
<td align="right">626,554</td>
<td align="right">86.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">732,475</td>
<td align="right"></td>
<td align="right">726,447</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,995,874,487</td>
<td align="right"></td>
<td align="right">6,941,054,937</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">199,518,084,361</td>
<td align="right">2,851.9%</td>
<td align="right">200,588,670,069</td>
<td align="right">2,889.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">44,495</td>
<td align="right">6.1%</td>
<td align="right">44,665</td>
<td align="right">6.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,201</td>
<td align="right">6.2%</td>
<td align="right">6,222</td>
<td align="right">6.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">99,865</td>
<td align="right">13.6%</td>
<td align="right">99,893</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">436,264</td>
<td align="right">59.6%</td>
<td align="right">436,223</td>
<td align="right">60.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,340</td>
<td align="right">0.2%</td>
<td align="right">1,340</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
<td align="right">96,285</td>
<td align="right">96.4%</td>
<td align="right">96,313</td>
<td align="right">96.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">99,865</td>
<td align="right"></td>
<td align="right">99,893</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
<td align="right">2,360</td>
<td align="right">2.4%</td>
<td align="right">2,360</td>
<td align="right">2.4%</td>
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
<td align="right">4,417</td>
<td align="right">4.4%</td>
<td align="right">4,395</td>
<td align="right">4.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">18,770</td>
<td align="right">18.8%</td>
<td align="right">18,605</td>
<td align="right">18.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">31,426</td>
<td align="right">31.5%</td>
<td align="right">31,040</td>
<td align="right">31.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">24,676</td>
<td align="right">24.7%</td>
<td align="right">24,679</td>
<td align="right">24.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,011</td>
<td align="right">13.0%</td>
<td align="right">13,105</td>
<td align="right">13.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,905</td>
<td align="right">5.9%</td>
<td align="right">6,189</td>
<td align="right">6.2%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
<td align="right">1,680</td>
<td align="right">1.7%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">200</td>
<td align="right">0.2%</td>
<td align="right">25.0%</td>
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
<td align="right">3,517</td>
<td align="right">3.5%</td>
<td align="right">3,495</td>
<td align="right">3.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">13,190</td>
<td align="right">13.2%</td>
<td align="right">13,165</td>
<td align="right">13.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,044</td>
<td align="right">21.1%</td>
<td align="right">20,666</td>
<td align="right">20.7%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">31,645</td>
<td align="right">31.7%</td>
<td align="right">31,488</td>
<td align="right">31.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">15,828</td>
<td align="right">15.8%</td>
<td align="right">15,777</td>
<td align="right">15.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,777</td>
<td align="right">7.8%</td>
<td align="right">8,081</td>
<td align="right">8.1%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,864</td>
<td align="right">2.9%</td>
<td align="right">3,181</td>
<td align="right">3.2%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">420</td>
<td align="right">0.4%</td>
<td align="right">460</td>
<td align="right">0.5%</td>
<td align="right">9.5%</td>
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
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">1,300,680</td>
<td align="right">4,247.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">112,294,657</td>
<td align="right">174,952,304</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">263,234,288</td>
<td align="right">347,575,561</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">264,461,108</td>
<td align="right">348,802,381</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">161,727,964</td>
<td align="right">188,251,711</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">109,944,001</td>
<td align="right">125,759,363</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">55,151,951</td>
<td align="right">59,982,105</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">875,622,191</td>
<td align="right">946,002,423</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">108,946,871</td>
<td align="right">117,477,145</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">57,495,040</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">49,472,300</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">14,733,440</td>
<td align="right">15,601,860</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">14,750,660</td>
<td align="right">15,619,080</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">16,532,656</td>
<td align="right">17,254,320</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,354,565</td>
<td align="right">11,746,970</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,354,565</td>
<td align="right">11,746,970</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">30,061,559</td>
<td align="right">30,836,790</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">63,288,260</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,666,575,631</td>
<td align="right">1,706,435,642</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,859,490,873</td>
<td align="right">1,899,502,023</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">571,278,550</td>
<td align="right">583,499,694</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,974,016,180</td>
<td align="right">2,014,027,320</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">723,894,216</td>
<td align="right">737,941,326</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,717,760</td>
<td align="right">519,338,660</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">759,387,446</td>
<td align="right">773,346,148</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,656,314,967</td>
<td align="right">6,768,090,386</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,464,344,158</td>
<td align="right">6,571,301,178</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">2,073,773,270</td>
<td align="right">2,043,050,048</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">88,974,636</td>
<td align="right">90,259,228</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,182,043,428</td>
<td align="right">2,212,803,400</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">128,979,703</td>
<td align="right">130,602,256</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">948,339,282</td>
<td align="right">936,600,145</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,146,853</td>
<td align="right">92,214,979</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,390,973</td>
<td align="right">92,459,099</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">243,947,697</td>
<td align="right">246,754,664</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,311,234,991</td>
<td align="right">1,325,172,489</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">618,070,128</td>
<td align="right">611,891,390</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">111,806,699</td>
<td align="right">112,922,605</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">185,440,069</td>
<td align="right">187,265,810</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">410,807,585</td>
<td align="right">414,847,262</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">187,963,243</td>
<td align="right">189,788,829</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,728,710,570</td>
<td align="right">1,744,777,594</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,918,726,671</td>
<td align="right">1,935,046,896</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">133,656,618</td>
<td align="right">134,772,500</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">714,411,449</td>
<td align="right">708,771,271</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,146,375,424</td>
<td align="right">1,155,268,876</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,233,766,789</td>
<td align="right">2,250,827,977</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,275,734</td>
<td align="right">135,293,970</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,275,734</td>
<td align="right">135,293,970</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,257,031,289</td>
<td align="right">2,274,092,497</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,246,464,824</td>
<td align="right">1,255,358,276</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,265,133,784</td>
<td align="right">1,274,027,236</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,041,466,866</td>
<td align="right">1,034,206,722</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,183,671,810</td>
<td align="right">2,198,589,530</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">199,272,547</td>
<td align="right">200,594,233</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,309,613,499</td>
<td align="right">1,302,386,599</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,099,366,093</td>
<td align="right">1,093,401,241</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,560,740,706</td>
<td align="right">4,536,405,782</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,370,134,108</td>
<td align="right">1,362,878,103</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,226,348,272</td>
<td align="right">2,238,035,175</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,201,882,244</td>
<td align="right">3,217,758,306</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,922,101,217</td>
<td align="right">4,898,004,889</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">13,838,445,458</td>
<td align="right">13,903,554,105</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,784,973,417</td>
<td align="right">11,833,723,173</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,013,864,955</td>
<td align="right">1,017,962,335</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,870,745,840</td>
<td align="right">1,863,775,714</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,093,491,602</td>
<td align="right">7,117,407,113</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,875,183,871</td>
<td align="right">1,869,528,457</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">551,047,405</td>
<td align="right">552,690,499</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">63,424,460</td>
<td align="right">63,602,180</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">139,987,220</td>
<td align="right">139,619,755</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">24,787,939</td>
<td align="right">24,851,260</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">687,095,548</td>
<td align="right">688,721,605</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,635,720</td>
<td align="right">5,648,200</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,940</td>
<td align="right">383,838,660</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">73,719,228</td>
<td align="right">73,868,596</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">686,406,779</td>
<td align="right">687,723,956</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,345,275,032</td>
<td align="right">1,347,650,010</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,487,575,199</td>
<td align="right">6,498,827,819</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">822,854,645</td>
<td align="right">824,210,957</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,708,606,074</td>
<td align="right">4,700,862,518</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">230,436,740</td>
<td align="right">230,806,340</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,974,586,850</td>
<td align="right">1,977,386,507</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,776,574</td>
<td align="right">5,784,638</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,292,731,288</td>
<td align="right">3,297,003,051</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,274,582,084</td>
<td align="right">1,276,172,131</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">958,951,116</td>
<td align="right">960,131,114</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">589,153,820</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">217,854,426</td>
<td align="right">218,107,928</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,454,700,186</td>
<td align="right">3,458,609,595</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,093,256,740</td>
<td align="right">2,095,563,726</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">484,898,826</td>
<td align="right">485,409,389</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,549,860</td>
<td align="right">1,143,348,180</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,248,288</td>
<td align="right">732,522,413</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">313,297,428</td>
<td align="right">313,599,751</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,200,646</td>
<td align="right">778,462,595</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">779,737,966</td>
<td align="right">778,999,915</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,043,487,026</td>
<td align="right">1,044,410,278</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,231,275,102</td>
<td align="right">1,232,333,704</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,941,470,707</td>
<td align="right">2,943,994,849</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,151,630</td>
<td align="right">1,336,215,135</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">179,421,667</td>
<td align="right">179,559,301</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,367,092,815</td>
<td align="right">1,368,124,743</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">342,016,375</td>
<td align="right">342,264,925</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,820,170,770</td>
<td align="right">2,822,060,620</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">118,551,306</td>
<td align="right">118,630,428</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,818,524,606</td>
<td align="right">1,819,704,629</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,510,984,929</td>
<td align="right">1,511,917,076</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">177,501,460</td>
<td align="right">177,602,961</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">213,613,440</td>
<td align="right">213,732,160</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,048,318,904</td>
<td align="right">1,048,846,700</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,387,999,946</td>
<td align="right">1,388,680,919</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">172,894,806</td>
<td align="right">172,977,362</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">232,033,452</td>
<td align="right">232,135,328</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,117,617</td>
<td align="right">10,113,426</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">360,002,536</td>
<td align="right">360,148,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">400,047,096</td>
<td align="right">400,193,430</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,692,440</td>
<td align="right">909,986,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,727,426,828</td>
<td align="right">5,729,252,466</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,030,720</td>
<td align="right">199,094,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">930,166,016</td>
<td align="right">930,409,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,114,192,745</td>
<td align="right">1,114,467,112</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">61,045,260</td>
<td align="right">61,060,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">61,155,800</td>
<td align="right">61,170,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,645,330,819</td>
<td align="right">2,645,868,662</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">485,229,132</td>
<td align="right">485,324,552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,536,056,102</td>
<td align="right">2,535,573,013</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,399,462</td>
<td align="right">78,413,041</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,548,540</td>
<td align="right">187,578,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">130,802,401</td>
<td align="right">130,822,646</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">543,380</td>
<td align="right">543,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">93,423,288</td>
<td align="right">93,436,750</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,527,876</td>
<td align="right">93,541,343</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">145,252,400</td>
<td align="right">145,273,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,547,427</td>
<td align="right">45,552,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">4,437,384</td>
<td align="right">4,436,845</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,554,804,253</td>
<td align="right">9,555,871,287</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,339,107,271</td>
<td align="right">1,339,248,782</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">315,041,692</td>
<td align="right">315,070,103</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,765,180</td>
<td align="right">229,783,576</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,157,418</td>
<td align="right">203,172,855</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">224,415,462</td>
<td align="right">224,430,348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">782,652,754</td>
<td align="right">782,694,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">565,760,042</td>
<td align="right">565,788,769</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">444,917</td>
<td align="right">444,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">227,835,680</td>
<td align="right">227,846,182</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">330,402,469</td>
<td align="right">330,415,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">541,056,271</td>
<td align="right">541,072,263</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">423,188,480</td>
<td align="right">423,200,165</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">93,665,280</td>
<td align="right">93,667,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,603,088,192</td>
<td align="right">3,603,152,981</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">592,507,283</td>
<td align="right">592,497,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,318,784</td>
<td align="right">32,319,226</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">647,423</td>
<td align="right">647,416</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">226,303,551</td>
<td align="right">226,305,461</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,315,992</td>
<td align="right">126,316,675</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">59,833,566</td>
<td align="right">59,833,867</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,875,160</td>
<td align="right">4,875,145</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">280,538,331</td>
<td align="right">280,537,644</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">325,040,038</td>
<td align="right">325,039,269</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,198,196</td>
<td align="right">97,198,005</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,155,536</td>
<td align="right">98,155,345</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,193,422</td>
<td align="right">101,193,615</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">966,570,333</td>
<td align="right">966,572,164</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,021,992</td>
<td align="right">22,021,964</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">375,828,062</td>
<td align="right">375,827,625</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">22,284,200</td>
<td align="right">22,284,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,070,107</td>
<td align="right">35,070,082</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,261,092</td>
<td align="right">54,261,064</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,911,747</td>
<td align="right">68,911,722</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,908,150</td>
<td align="right">9,908,152</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">154,174,508</td>
<td align="right">154,174,531</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">409,921,260</td>
<td align="right">409,921,208</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">147,639,762</td>
<td align="right">147,639,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">114,548,487</td>
<td align="right">114,548,477</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,652,510,816</td>
<td align="right">1,652,510,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,180</td>
<td align="right">645,067,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,073,040</td>
<td align="right">533,073,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,868,340</td>
<td align="right">149,868,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,940,100</td>
<td align="right">144,940,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,197,960</td>
<td align="right">101,197,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">99,814,960</td>
<td align="right">99,814,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,571,420</td>
<td align="right">80,571,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">66,194,480</td>
<td align="right">66,194,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,901,080</td>
<td align="right">61,901,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,693,340</td>
<td align="right">12,693,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,134,100</td>
<td align="right">8,134,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">6,583,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,625,240</td>
<td align="right">4,625,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,610,440</td>
<td align="right">3,610,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">2,714,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,126,620</td>
<td align="right">2,126,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,940,740</td>
<td align="right">1,940,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,887,020</td>
<td align="right">1,887,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,543,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,160</td>
<td align="right">821,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">71,600</td>
<td align="right">71,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">34,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">17,200</td>
<td align="right">17,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">7,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ALLOC_AND_ENTER_INIT_COMMON</td>
<td align="right"></td>
<td align="right">23,926,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_INIT_CHECK</td>
<td align="right"></td>
<td align="right">22,720,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ALLOC_AND_ENTER_INIT_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">21,975,900</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ALLOC_AND_ENTER_INIT_GENERAL</td>
<td align="right"></td>
<td align="right">1,948,120</td>
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
<td align="right">82,008</td>
<td align="right">73,074</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,201</td>
<td align="right">5,581</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">538</td>
<td align="right">540</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,571</td>
<td align="right">6,561</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,417</td>
<td align="right">2,415</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">1,440</td>
<td align="right">1,441</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">28,920</td>
<td align="right">28,940</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40,479</td>
<td align="right">40,490</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">32,220</td>
<td align="right">32,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,340</td>
<td align="right">2,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,620</td>
<td align="right">1,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,340</td>
<td align="right">1,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">820</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">360</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,081</td>
<td align="right">1,082</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,081</td>
<td align="right">1,082</td>
<td align="right">0.1%</td>
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
<td align="right">240</td>
<td align="right">240</td>
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
<td align="right">360</td>
<td align="right">360</td>
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
<td align="right">1,860</td>
<td align="right">1,860</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-06-08
