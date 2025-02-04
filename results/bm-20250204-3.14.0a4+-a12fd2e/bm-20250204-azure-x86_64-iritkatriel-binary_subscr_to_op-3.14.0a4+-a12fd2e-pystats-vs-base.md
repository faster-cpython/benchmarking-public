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
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">83,650,520</td>
<td align="right">3</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,297,842</td>
<td align="right">2</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,867</td>
<td align="right">2</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,910,995</td>
<td align="right">12</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6,998,249</td>
<td align="right">8</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">23,493,435</td>
<td align="right">55</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,780,917</td>
<td align="right">12</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,924</td>
<td align="right">15</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,691</td>
<td align="right">173</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">73,338,796</td>
<td align="right">2,144</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,793</td>
<td align="right">2,079</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,639,599</td>
<td align="right">257</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,937,295</td>
<td align="right">36,693</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,563</td>
<td align="right">68</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">101,012,103</td>
<td align="right">37,189</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,321</td>
<td align="right">2</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,828,655</td>
<td align="right">712</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,758,240</td>
<td align="right">6,556</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,648</td>
<td align="right">2</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,758</td>
<td align="right">101</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">15,697,665</td>
<td align="right">30,725</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">242,354,631</td>
<td align="right">511,841</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">701,064,531</td>
<td align="right">2,400,716</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,586,998,542</td>
<td align="right">7,027,169</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">133,165</td>
<td align="right">842</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,791,760</td>
<td align="right">1,351,546</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,753</td>
<td align="right">346</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,147</td>
<td align="right">639</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">77,226,714</td>
<td align="right">1,017,085</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">183,157,135</td>
<td align="right">2,475,073</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,134</td>
<td align="right">73</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,896</td>
<td align="right">70</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,620</td>
<td align="right">66</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,561,584</td>
<td align="right">1,331,291</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">73,121,184</td>
<td align="right">1,676,525</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,850,358</td>
<td align="right">3,571,406</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,637,951,720</td>
<td align="right">46,896,753</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">68,025,726</td>
<td align="right">1,962,212</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">403,165</td>
<td align="right">12,220</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">348,666,237</td>
<td align="right">10,839,135</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,113,304,797</td>
<td align="right">35,084,949</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,276,192,150</td>
<td align="right">43,714,402</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">519,111,695</td>
<td align="right">18,178,662</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">89,937,644</td>
<td align="right">3,165,633</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,712,839</td>
<td align="right">6,444,200</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,850,148</td>
<td align="right">6,706,523</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">259,701,889</td>
<td align="right">10,477,741</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">115,831,084</td>
<td align="right">4,802,190</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">79,693,934</td>
<td align="right">3,395,266</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,536,715,126</td>
<td align="right">113,452,874</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">69,707,787</td>
<td align="right">3,133,295</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">63,890,409</td>
<td align="right">2,995,838</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,380,012,661</td>
<td align="right">65,070,433</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,992,770</td>
<td align="right">4,801,554</td>
<td align="right">-95.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,732</td>
<td align="right">6,491,340</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">842,165,923</td>
<td align="right">44,827,599</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">175,328,740</td>
<td align="right">10,003,319</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,189</td>
<td align="right">11,159,963</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">816,494,743</td>
<td align="right">50,628,481</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">76,086,856</td>
<td align="right">5,263,344</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">42</td>
<td align="right">3</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">94,951,819</td>
<td align="right">6,884,290</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">225,848,071</td>
<td align="right">17,406,782</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">972,650,751</td>
<td align="right">76,818,563</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,630,237,095</td>
<td align="right">128,796,738</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,404,608,191</td>
<td align="right">112,239,633</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">138,634,168</td>
<td align="right">12,476,985</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">211,103,004</td>
<td align="right">21,237,626</td>
<td align="right">-89.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">195,032,323</td>
<td align="right">19,984,617</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">99,391,334</td>
<td align="right">10,584,379</td>
<td align="right">-89.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,662,973,079</td>
<td align="right">187,302,320</td>
<td align="right">-88.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,560,074,458</td>
<td align="right">291,651,289</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">320,310,349</td>
<td align="right">39,987,339</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,264,185,946</td>
<td align="right">158,382,767</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,970,767</td>
<td align="right">7,895,526</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,494,526,766</td>
<td align="right">465,084,507</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">630,557,755</td>
<td align="right">85,040,748</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,876,915</td>
<td align="right">2,894,403</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,876,895</td>
<td align="right">2,894,401</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">669,017,425</td>
<td align="right">93,169,015</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,546,411</td>
<td align="right">2,894,401</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,756,095,608</td>
<td align="right">393,249,747</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">852,431,454</td>
<td align="right">122,139,333</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">168,526,363</td>
<td align="right">24,803,226</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,037,985,275</td>
<td align="right">154,806,921</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">364,064,556</td>
<td align="right">57,012,780</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">568,951,573</td>
<td align="right">91,004,442</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,198,057,096</td>
<td align="right">357,074,278</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,759,753,767</td>
<td align="right">951,321,959</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,318,053,080</td>
<td align="right">1,210,958,794</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,656,159</td>
<td align="right">1,663,943</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">498,511,432</td>
<td align="right">89,802,928</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,036,433</td>
<td align="right">1,663,866</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,303,397</td>
<td align="right">116,536,335</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,734,805,916</td>
<td align="right">2,128,245,309</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,699,925,179</td>
<td align="right">341,011,598</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">93,806,760</td>
<td align="right">19,203,092</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,022,068</td>
<td align="right">57,106,582</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">389,073,629</td>
<td align="right">85,094,334</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">6,510,234,521</td>
<td align="right">1,528,406,502</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">781,616,298</td>
<td align="right">191,037,825</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,310,861,484</td>
<td align="right">1,547,031,679</td>
<td align="right">-75.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,535,631,362</td>
<td align="right">379,831,605</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">37,484,724,472</td>
<td align="right">9,361,343,086</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,176,829,115</td>
<td align="right">809,933,114</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,492,942,970</td>
<td align="right">3,446,704,691</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">503,540,972</td>
<td align="right">130,923,312</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,852,580,876</td>
<td align="right">1,261,953,127</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">264,372,986</td>
<td align="right">69,630,947</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,047,289,539</td>
<td align="right">3,016,543,654</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">441,799,097</td>
<td align="right">121,084,237</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,801,809</td>
<td align="right">117,496,018</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,146,240,640</td>
<td align="right">607,700,910</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,348,603,031</td>
<td align="right">962,991,321</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,210,740,869</td>
<td align="right">350,941,211</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,427,763,543</td>
<td align="right">1,632,392,369</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,476,670,805</td>
<td align="right">447,036,064</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">331,398,409</td>
<td align="right">101,051,438</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,756,317,837</td>
<td align="right">537,492,377</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">320,700,295</td>
<td align="right">99,967,126</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">537,422,463</td>
<td align="right">167,669,321</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">226,884,371</td>
<td align="right">71,873,615</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">984,838,126</td>
<td align="right">329,098,213</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,247,848,004</td>
<td align="right">756,891,254</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">792,896,684</td>
<td align="right">280,971,940</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,212,359,490</td>
<td align="right">1,172,367,023</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,846,276</td>
<td align="right">5,325,042</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,899</td>
<td align="right">116,536,332</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,783,533,011</td>
<td align="right">2,263,086,037</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,486,876,268</td>
<td align="right">993,428,756</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">497,365,532</td>
<td align="right">206,729,402</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,955,582</td>
<td align="right">31,542,759</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,872,652,988</td>
<td align="right">1,704,838,228</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">57,318,882</td>
<td align="right">25,760,387</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,436,108</td>
<td align="right">492,514,940</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">813,886,256</td>
<td align="right">391,759,845</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,475,079</td>
<td align="right">120,445,344</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,097,811,527</td>
<td align="right">1,034,953,563</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">520,479,961</td>
<td align="right">257,846,904</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,418,450</td>
<td align="right">120,445,303</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,299,495</td>
<td align="right">33,550,224</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,613,605</td>
<td align="right">261,878,970</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">332,409,484</td>
<td align="right">173,523,929</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,115,211</td>
<td align="right">1,663,799</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,742,052</td>
<td align="right">184,717,036</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">918,390,666</td>
<td align="right">534,009,217</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">288,472,352</td>
<td align="right">168,224,164</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,417,726</td>
<td align="right">76,800,195</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">566,125,400</td>
<td align="right">349,030,751</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,253,697</td>
<td align="right">38,400,076</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,481,380</td>
<td align="right">76,800,143</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">357,283,056</td>
<td align="right">224,095,797</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">379,266,753</td>
<td align="right">241,598,330</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,116,871,093</td>
<td align="right">741,143,727</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,162,417</td>
<td align="right">76,800,000</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">116,536,320</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,742,322</td>
<td align="right">5,740,800</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,767,775</td>
<td align="right">44,753,945</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,788,798</td>
<td align="right">291,517,228</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">403,677,199</td>
<td align="right">322,183,753</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,370,319</td>
<td align="right">60,351,420</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,720,965,889</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,357,302,863</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,260,966,304</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,079,535,411</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">292,955,593</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">156,807,836</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">156,403,086</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,677</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,686,498</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">76,990,644</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,800,296</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">781,020</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,734</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,552</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">59,727</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,770</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,546</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">151</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">551,371,298</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">522,714,275</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">93,210,432</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right"></td>
<td align="right">158,250</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right">71</td>
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
<td align="right">7,641,259,916</td>
<td align="right">89.8%</td>
<td align="right">2,933,099,514</td>
<td align="right">86.8%</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">813,469,493</td>
<td align="right">9.6%</td>
<td align="right">391,517,008</td>
<td align="right">11.6%</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,085,947</td>
<td align="right">0.6%</td>
<td align="right">52,514,630</td>
<td align="right">1.6%</td>
<td align="right">-1.1%</td>
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
<td align="right">408,207</td>
<td align="right">28.8%</td>
<td align="right">241,101</td>
<td align="right">19.5%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,010,120</td>
<td align="right">71.2%</td>
<td align="right">992,539</td>
<td align="right">80.5%</td>
<td align="right">-1.7%</td>
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
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">4.8%</td>
<td align="right">1,180</td>
<td align="right">0.5%</td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">2.8%</td>
<td align="right">1,780</td>
<td align="right">0.7%</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,036</td>
<td align="right">0.5%</td>
<td align="right">364</td>
<td align="right">0.2%</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,612</td>
<td align="right">9.0%</td>
<td align="right">7,560</td>
<td align="right">3.1%</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">7,225</td>
<td align="right">1.8%</td>
<td align="right">1,530</td>
<td align="right">0.6%</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,801</td>
<td align="right">10.7%</td>
<td align="right">10,068</td>
<td align="right">4.2%</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,976</td>
<td align="right">8.3%</td>
<td align="right">11,658</td>
<td align="right">4.8%</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,519</td>
<td align="right">5.8%</td>
<td align="right">11,480</td>
<td align="right">4.8%</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,513</td>
<td align="right">2.1%</td>
<td align="right">4,200</td>
<td align="right">1.7%</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.7%</td>
<td align="right">1,780</td>
<td align="right">0.7%</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">43,342</td>
<td align="right">10.6%</td>
<td align="right">30,121</td>
<td align="right">12.5%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">2.0%</td>
<td align="right">5,900</td>
<td align="right">2.4%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,209</td>
<td align="right">18.2%</td>
<td align="right">70,220</td>
<td align="right">29.1%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">21.0%</td>
<td align="right">83,260</td>
<td align="right">34.5%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,154</td>
<td align="right">0.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,251</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">627</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">597</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">399</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">181,850,148</td>
<td align="right">100.0%</td>
<td align="right">6,706,523</td>
<td align="right">100.0%</td>
<td align="right">-96.3%</td>
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
<td align="right">152,389,449</td>
<td align="right">1.4%</td>
<td align="right">24,083,263</td>
<td align="right">0.7%</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">155,084,432</td>
<td align="right">1.4%</td>
<td align="right">24,545,267</td>
<td align="right">0.7%</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,116,412,073</td>
<td align="right">98.6%</td>
<td align="right">3,373,938,184</td>
<td align="right">99.3%</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,186</td>
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
<td align="left">Success</td>
<td align="right">3,097,702</td>
<td align="right">100.0%</td>
<td align="right">474,098</td>
<td align="right">100.0%</td>
<td align="right">-84.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">446</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">-71.7%</td>
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
<td align="right">752</td>
<td align="right">168.6%</td>
<td align="right">64</td>
<td align="right">50.8%</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">126</td>
<td align="right">100.0%</td>
<td align="right">-77.7%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">684,422</td>
<td align="right">97.1%</td>
<td align="right">15</td>
<td align="right">14.9%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">583,846</td>
<td align="right">82.9%</td>
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
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20,062</td>
<td align="right">99.4%</td>
<td align="right">86</td>
<td align="right">100.0%</td>
<td align="right">-99.6%</td>
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
<td align="right">518,880,470</td>
<td align="right">10.3%</td>
<td align="right">18,166,294</td>
<td align="right">4.2%</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,530,203,247</td>
<td align="right">89.7%</td>
<td align="right">411,272,955</td>
<td align="right">95.7%</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,426,092</td>
<td align="right">0.0%</td>
<td align="right">163,924</td>
<td align="right">0.0%</td>
<td align="right">-88.5%</td>
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
<td align="right">213,281</td>
<td align="right">82.7%</td>
<td align="right">11,969</td>
<td align="right">77.3%</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">44,529</td>
<td align="right">17.3%</td>
<td align="right">3,519</td>
<td align="right">22.7%</td>
<td align="right">-92.1%</td>
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
<td align="right">7,760</td>
<td align="right">3.6%</td>
<td align="right">44</td>
<td align="right">0.4%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,367</td>
<td align="right">0.6%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,004</td>
<td align="right">0.9%</td>
<td align="right">43</td>
<td align="right">0.4%</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,770</td>
<td align="right">21.5%</td>
<td align="right">1,183</td>
<td align="right">9.9%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,377</td>
<td align="right">6.7%</td>
<td align="right">3,085</td>
<td align="right">25.8%</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,374</td>
<td align="right">11.0%</td>
<td align="right">7,594</td>
<td align="right">63.4%</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">90,853</td>
<td align="right">42.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">11,955</td>
<td align="right">5.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">3.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,822</td>
<td align="right">3.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,004</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">155,730,449</td>
<td align="right">6.6%</td>
<td align="right">1,350,970</td>
<td align="right">0.2%</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,196,199,947</td>
<td align="right">93.3%</td>
<td align="right">658,576,614</td>
<td align="right">99.8%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
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
<td align="left">Success</td>
<td align="right">38,235</td>
<td align="right">39.2%</td>
<td align="right">63</td>
<td align="right">10.9%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,250</td>
<td align="right">60.8%</td>
<td align="right">513</td>
<td align="right">89.1%</td>
<td align="right">-99.1%</td>
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
<td align="right">14,565</td>
<td align="right">24.6%</td>
<td align="right">40</td>
<td align="right">7.8%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,704</td>
<td align="right">19.8%</td>
<td align="right">44</td>
<td align="right">8.6%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,601</td>
<td align="right">19.6%</td>
<td align="right">65</td>
<td align="right">12.7%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">21,380</td>
<td align="right">36.1%</td>
<td align="right">364</td>
<td align="right">71.0%</td>
<td align="right">-98.3%</td>
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
<td align="right">3,444,392,811</td>
<td align="right">67.7%</td>
<td align="right">514,189,416</td>
<td align="right">48.6%</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,476,234,555</td>
<td align="right">29.0%</td>
<td align="right">446,926,556</td>
<td align="right">42.3%</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,999,134</td>
<td align="right">3.2%</td>
<td align="right">96,106,772</td>
<td align="right">9.1%</td>
<td align="right">-41.4%</td>
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
<td align="right">431,185</td>
<td align="right">12.2%</td>
<td align="right">109,459</td>
<td align="right">5.7%</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,099,217</td>
<td align="right">87.8%</td>
<td align="right">1,813,381</td>
<td align="right">94.3%</td>
<td align="right">-41.5%</td>
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
<td align="left">dict values</td>
<td align="right">6,911</td>
<td align="right">1.6%</td>
<td align="right">18</td>
<td align="right">0.0%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,514</td>
<td align="right">4.5%</td>
<td align="right">98</td>
<td align="right">0.1%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">172,146</td>
<td align="right">39.9%</td>
<td align="right">2,320</td>
<td align="right">2.1%</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,601</td>
<td align="right">1.1%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,325</td>
<td align="right">2.6%</td>
<td align="right">961</td>
<td align="right">0.9%</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">70,793</td>
<td align="right">16.4%</td>
<td align="right">6,666</td>
<td align="right">6.1%</td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,995</td>
<td align="right">8.1%</td>
<td align="right">18,373</td>
<td align="right">16.8%</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,979</td>
<td align="right">19.5%</td>
<td align="right">80,943</td>
<td align="right">73.9%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,261</td>
<td align="right">4.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,390</td>
<td align="right">0.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,139</td>
<td align="right">0.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">734</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,404,473</td>
<td align="right">0.0%</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">850,585,038</td>
<td align="right">6.1%</td>
<td align="right">122,098,238</td>
<td align="right">3.9%</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,173,500,623</td>
<td align="right">87.6%</td>
<td align="right">2,788,558,887</td>
<td align="right">88.4%</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">871,353,531</td>
<td align="right">6.3%</td>
<td align="right">243,066,767</td>
<td align="right">7.7%</td>
<td align="right">-72.1%</td>
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
<td align="right">565,427</td>
<td align="right">3.3%</td>
<td align="right">32,292</td>
<td align="right">0.7%</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,521,824</td>
<td align="right">96.7%</td>
<td align="right">4,594,548</td>
<td align="right">99.3%</td>
<td align="right">-72.2%</td>
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
<td align="right">16,613</td>
<td align="right">2.9%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,088</td>
<td align="right">0.9%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,080</td>
<td align="right">1.1%</td>
<td align="right">12</td>
<td align="right">0.0%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,802</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">57,925</td>
<td align="right">10.2%</td>
<td align="right">3,544</td>
<td align="right">11.0%</td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">66,162</td>
<td align="right">11.7%</td>
<td align="right">4,902</td>
<td align="right">15.2%</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,128</td>
<td align="right">1.6%</td>
<td align="right">1,180</td>
<td align="right">3.7%</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">81,377</td>
<td align="right">14.4%</td>
<td align="right">20,498</td>
<td align="right">63.5%</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">25,289</td>
<td align="right">4.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,729</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,584</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,180</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">163</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">14,622,718</td>
<td align="right">0.2%</td>
<td align="right">539</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,151</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,132,082,891</td>
<td align="right">99.8%</td>
<td align="right">3,226,076,998</td>
<td align="right">100.0%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,508</td>
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
<td align="left">Success</td>
<td align="right">136,289</td>
<td align="right">100.0%</td>
<td align="right">6,020</td>
<td align="right">100.0%</td>
<td align="right">-95.6%</td>
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
<td align="right">253</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,085,978</td>
<td align="right">100.0%</td>
<td align="right">9,559,325</td>
<td align="right">100.0%</td>
<td align="right">-85.1%</td>
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
<td align="right">2,395</td>
<td align="right">100.0%</td>
<td align="right">1</td>
<td align="right">100.0%</td>
<td align="right">-100.0%</td>
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
<td align="right">593,288,686</td>
<td align="right">82.2%</td>
<td align="right">116,536,335</td>
<td align="right">100.0%</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,816,906</td>
<td align="right">17.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">Success</td>
<td align="right">651</td>
<td align="right">1.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,392</td>
<td align="right">98.1%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">async generator send</td>
<td align="right">24,440</td>
<td align="right">71.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">732</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">77,133,377</td>
<td align="right">3.8%</td>
<td align="right">1,015,712</td>
<td align="right">0.2%</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,849,862,141</td>
<td align="right">90.5%</td>
<td align="right">381,174,076</td>
<td align="right">93.7%</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">116,603,577</td>
<td align="right">5.7%</td>
<td align="right">24,742,700</td>
<td align="right">6.1%</td>
<td align="right">-78.8%</td>
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
<td align="right">52,763</td>
<td align="right">2.3%</td>
<td align="right">757</td>
<td align="right">0.2%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,239,878</td>
<td align="right">97.7%</td>
<td align="right">467,336</td>
<td align="right">99.8%</td>
<td align="right">-79.1%</td>
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
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">46.4%</td>
<td align="right">2</td>
<td align="right">0.3%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">6,033</td>
<td align="right">11.4%</td>
<td align="right">3</td>
<td align="right">0.4%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,350</td>
<td align="right">6.3%</td>
<td align="right">3</td>
<td align="right">0.4%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">272,058</td>
<td align="right">515.6%</td>
<td align="right">1,351</td>
<td align="right">178.5%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,322</td>
<td align="right">10.1%</td>
<td align="right">410</td>
<td align="right">54.2%</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">86</td>
<td align="right">11.4%</td>
<td align="right">-88.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">231</td>
<td align="right">30.5%</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">810</td>
<td align="right">1.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">112,686,498</td>
<td align="right">100.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">700,880,195</td>
<td align="right">43.1%</td>
<td align="right">2,400,059</td>
<td align="right">0.4%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">923,406,236</td>
<td align="right">56.8%</td>
<td align="right">573,126,548</td>
<td align="right">99.6%</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,220</td>
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
<td align="right">182,300</td>
<td align="right">98.9%</td>
<td align="right">562</td>
<td align="right">85.5%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,076</td>
<td align="right">1.1%</td>
<td align="right">95</td>
<td align="right">14.5%</td>
<td align="right">-95.4%</td>
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
<td align="right">86,613</td>
<td align="right">47.5%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.8%</td>
<td align="right">560</td>
<td align="right">99.6%</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,343</td>
<td align="right">10.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">9.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,309</td>
<td align="right">2.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,032</td>
<td align="right">1.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">0.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">112,464,627</td>
<td align="right">2.2%</td>
<td align="right">1,458,327</td>
<td align="right">0.1%</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">263,691,827</td>
<td align="right">5.2%</td>
<td align="right">69,612,330</td>
<td align="right">3.7%</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,741,683,250</td>
<td align="right">92.6%</td>
<td align="right">1,826,988,874</td>
<td align="right">96.3%</td>
<td align="right">-61.5%</td>
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
<td align="right">2,169,947</td>
<td align="right">77.5%</td>
<td align="right">28,343</td>
<td align="right">61.4%</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">631,631</td>
<td align="right">22.5%</td>
<td align="right">17,784</td>
<td align="right">38.6%</td>
<td align="right">-97.2%</td>
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
<td align="right">10,046</td>
<td align="right">1.6%</td>
<td align="right">576</td>
<td align="right">3.2%</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">97,669</td>
<td align="right">15.5%</td>
<td align="right">10,453</td>
<td align="right">58.8%</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">20,552</td>
<td align="right">3.3%</td>
<td align="right">6,395</td>
<td align="right">36.0%</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">360</td>
<td align="right">2.0%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,649</td>
<td align="right">40.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">132,992</td>
<td align="right">21.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">77,643</td>
<td align="right">12.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,878</td>
<td align="right">3.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,316</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">1,816,218</td>
<td align="right">0.1%</td>
<td align="right">57</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,247,660,116</td>
<td align="right">99.9%</td>
<td align="right">573,572,998</td>
<td align="right">100.0%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,700</td>
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
<td align="right">996</td>
<td align="right">8.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,521</td>
<td align="right">92.0%</td>
<td align="right">655</td>
<td align="right">100.0%</td>
<td align="right">-94.3%</td>
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
<td align="right">769</td>
<td align="right">77.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">13.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">9.1%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">7,658,360,853</td>
<td align="right">3.6%</td>
<td align="right">1,060,240,312</td>
<td align="right">2.1%</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">115,381,791,235</td>
<td align="right">54.6%</td>
<td align="right">27,480,334,728</td>
<td align="right">54.0%</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">86,720,332,552</td>
<td align="right">41.1%</td>
<td align="right">21,950,490,328</td>
<td align="right">43.1%</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,482,646,404</td>
<td align="right">0.7%</td>
<td align="right">442,600,826</td>
<td align="right">0.9%</td>
<td align="right">-70.1%</td>
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
<td align="right">700,880,195</td>
<td align="right">9.0%</td>
<td align="right">2,400,059</td>
<td align="right">0.2%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,730,449</td>
<td align="right">2.0%</td>
<td align="right">1,350,970</td>
<td align="right">0.1%</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">518,880,470</td>
<td align="right">6.6%</td>
<td align="right">18,166,294</td>
<td align="right">1.7%</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,850,148</td>
<td align="right">2.3%</td>
<td align="right">6,706,523</td>
<td align="right">0.6%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">850,585,038</td>
<td align="right">10.9%</td>
<td align="right">122,098,238</td>
<td align="right">11.3%</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">152,389,449</td>
<td align="right">2.0%</td>
<td align="right">24,083,263</td>
<td align="right">2.2%</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">263,691,827</td>
<td align="right">3.4%</td>
<td align="right">69,612,330</td>
<td align="right">6.4%</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,476,234,555</td>
<td align="right">18.9%</td>
<td align="right">446,926,556</td>
<td align="right">41.2%</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">813,469,493</td>
<td align="right">10.4%</td>
<td align="right">391,517,008</td>
<td align="right">36.1%</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,356,686,682</td>
<td align="right">30.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,015,712</td>
<td align="right">0.1%</td>
<td align="right"></td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">82,381,334</td>
<td align="right">5.6%</td>
<td align="right">19,752,765</td>
<td align="right">4.5%</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,279,957</td>
<td align="right">6.4%</td>
<td align="right">24,742,700</td>
<td align="right">5.6%</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">266,996,947</td>
<td align="right">18.0%</td>
<td align="right">88,579,581</td>
<td align="right">20.0%</td>
<td align="right">-66.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">368,080,330</td>
<td align="right">24.8%</td>
<td align="right">154,487,008</td>
<td align="right">34.9%</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,014,999</td>
<td align="right">5.5%</td>
<td align="right">48,053,348</td>
<td align="right">10.9%</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,905,875</td>
<td align="right">5.5%</td>
<td align="right">48,053,424</td>
<td align="right">10.9%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">90,676,908</td>
<td align="right">6.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">86,869,074</td>
<td align="right">5.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">55,296,449</td>
<td align="right">3.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,780,874</td>
<td align="right">3.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">26,031,120</td>
<td align="right">5.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">9,524,100</td>
<td align="right">2.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">7,400,280</td>
<td align="right">1.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">4,766,754</td>
<td align="right">1.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,139</td>
<td align="right">2.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
<td align="right">70</td>
<td align="right">0.0%</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">678,916,319</td>
<td align="right">10.0%</td>
<td align="right">35,532,731</td>
<td align="right">2.1%</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,512</td>
<td align="right">0.4%</td>
<td align="right">1,875,531</td>
<td align="right">0.1%</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,634,730,501</td>
<td align="right">24.2%</td>
<td align="right">128,798,521</td>
<td align="right">7.7%</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,634,730,501</td>
<td align="right">24.2%</td>
<td align="right">128,798,521</td>
<td align="right">7.7%</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,326,872</td>
<td align="right">1.1%</td>
<td align="right">6,869,265</td>
<td align="right">0.4%</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">955,814,182</td>
<td align="right">14.1%</td>
<td align="right">93,265,790</td>
<td align="right">5.6%</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">951,536,844</td>
<td align="right">14.1%</td>
<td align="right">93,265,712</td>
<td align="right">5.6%</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,414,364</td>
<td align="right">3.9%</td>
<td align="right">37,712,588</td>
<td align="right">2.3%</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,437,272</td>
<td align="right">4.1%</td>
<td align="right">40,932,839</td>
<td align="right">2.5%</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,484,878,634</td>
<td align="right">81.2%</td>
<td align="right">1,632,392,439</td>
<td align="right">98.1%</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,122,270,440</td>
<td align="right">75.8%</td>
<td align="right">1,535,729,522</td>
<td align="right">92.3%</td>
<td align="right">-70.0%</td>
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
<td align="left">Materialize dict (new key)</td>
<td align="right">476,016</td>
<td align="right">0.3%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">9,065,605</td>
<td align="right"></td>
<td align="right">2,022</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">73,866,295</td>
<td align="right"></td>
<td align="right">2,828,332</td>
<td align="right"></td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">65,608,232</td>
<td align="right"></td>
<td align="right">2,827,071</td>
<td align="right"></td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,581,816</td>
<td align="right">0.4%</td>
<td align="right">5,233,847</td>
<td align="right">0.1%</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">23,843,789,501</td>
<td align="right">12.5%</td>
<td align="right">2,600,464,041</td>
<td align="right">6.3%</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">21,982,080,589</td>
<td align="right">14.2%</td>
<td align="right">3,179,649,173</td>
<td align="right">8.8%</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,438,382,572</td>
<td align="right">67.1%</td>
<td align="right">2,175,215,024</td>
<td align="right">55.8%</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,438,512,783</td>
<td align="right"></td>
<td align="right">2,175,283,118</td>
<td align="right"></td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,287,255,438</td>
<td align="right"></td>
<td align="right">447,184,977</td>
<td align="right"></td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">25,402,727,751</td>
<td align="right">16.4%</td>
<td align="right">5,031,400,241</td>
<td align="right">13.9%</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,904,561,867</td>
<td align="right"></td>
<td align="right">594,702,433</td>
<td align="right"></td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">33,078,557,795</td>
<td align="right">17.3%</td>
<td align="right">7,153,767,913</td>
<td align="right">17.3%</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">89,046,535,887</td>
<td align="right">46.5%</td>
<td align="right">20,941,198,104</td>
<td align="right">50.6%</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">45,509,487,506</td>
<td align="right">23.8%</td>
<td align="right">10,723,659,593</td>
<td align="right">25.9%</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">79,636,726,943</td>
<td align="right">51.5%</td>
<td align="right">19,429,481,992</td>
<td align="right">53.6%</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,700,279,607</td>
<td align="right"></td>
<td align="right">1,832,069,483</td>
<td align="right"></td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,445,959</td>
<td align="right"></td>
<td align="right">50,165,274</td>
<td align="right"></td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,106,345,633</td>
<td align="right">32.9%</td>
<td align="right">1,720,198,094</td>
<td align="right">44.2%</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,028,342,647</td>
<td align="right">32.5%</td>
<td align="right">1,709,908,357</td>
<td align="right">43.9%</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">27,494,817,655</td>
<td align="right">17.8%</td>
<td align="right">8,621,290,160</td>
<td align="right">23.8%</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,171</td>
<td align="right">2.5%</td>
<td align="right">2,283,748</td>
<td align="right">4.6%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,421,170</td>
<td align="right">0.0%</td>
<td align="right">5,055,890</td>
<td align="right">0.1%</td>
<td align="right">-21.3%</td>
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
<td align="right">365,656</td>
<td align="right">103,623,946</td>
<td align="right">9,545,446,257</td>
<td align="right">751,896,858</td>
<td align="right">766,477,145</td>
<td align="right">10,503</td>
<td align="right">665</td>
<td align="right">674,380,520</td>
<td align="right">111,308,700</td>
<td align="right">16,637,779</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,607,511,928</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,607,489,920</td>
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
<td align="right">22,629</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">30</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">37</td>
<td align="right">6</td>
<td align="right">-83.8%</td>
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
<td align="right">2,476</td>
<td align="right">573</td>
<td align="right">-76.9%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-04
