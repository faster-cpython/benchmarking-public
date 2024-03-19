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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">325,613,628</td>
<td align="right">601,833,981</td>
<td align="right">84.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,591,815</td>
<td align="right">6,405,055</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">7,836,528</td>
<td align="right">11,828,896</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,328,247</td>
<td align="right">12,137,247</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,792,682,669</td>
<td align="right">3,236,465,103</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">96,449,559</td>
<td align="right">110,946,313</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">427,686,518</td>
<td align="right">473,484,744</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,876,934</td>
<td align="right">2,610,524</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">45,299,748</td>
<td align="right">48,495,356</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">205,940,247</td>
<td align="right">219,680,788</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">546,776</td>
<td align="right">582,576</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">644,402,264</td>
<td align="right">680,548,568</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,165,193,892</td>
<td align="right">6,487,018,086</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,055,552,695</td>
<td align="right">3,200,532,994</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,330,423,845</td>
<td align="right">5,574,433,470</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">320,051,609</td>
<td align="right">333,291,650</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">663,282,291</td>
<td align="right">687,766,281</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">243,525,373</td>
<td align="right">252,224,592</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">67,214,948</td>
<td align="right">64,914,355</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">128,128,317</td>
<td align="right">132,399,154</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,549,373,215</td>
<td align="right">2,627,725,857</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">66,554,996</td>
<td align="right">68,569,954</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">148,546,288</td>
<td align="right">152,530,248</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,795,188,846</td>
<td align="right">6,964,804,114</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">77,263,974</td>
<td align="right">78,912,379</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">455,028,989</td>
<td align="right">445,380,770</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">204,018,497</td>
<td align="right">208,102,259</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,556,427,741</td>
<td align="right">3,622,844,126</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">25,235,756,241</td>
<td align="right">25,687,850,525</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">182,239,276</td>
<td align="right">185,285,284</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">463,625,525</td>
<td align="right">456,701,647</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,736,021,723</td>
<td align="right">1,759,655,772</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">44,826,957</td>
<td align="right">44,234,406</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">391,725,709</td>
<td align="right">396,899,046</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,046,674,538</td>
<td align="right">1,060,305,138</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">118,429,723</td>
<td align="right">117,044,967</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">848,686,067</td>
<td align="right">857,355,200</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">72,359</td>
<td align="right">71,715</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">680,168,943</td>
<td align="right">685,869,836</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">47,086,286</td>
<td align="right">47,469,056</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">217,533,859</td>
<td align="right">219,284,101</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,742,501,877</td>
<td align="right">1,754,258,044</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">513,274,281</td>
<td align="right">516,693,497</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,371,404,975</td>
<td align="right">1,380,215,528</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">505,241,291</td>
<td align="right">508,459,379</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">480,241,977</td>
<td align="right">477,252,777</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">540,110,416</td>
<td align="right">543,399,358</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">158,017,639</td>
<td align="right">157,077,835</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">116,460,828</td>
<td align="right">115,797,523</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">147,962,248</td>
<td align="right">147,149,254</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,319,581,092</td>
<td align="right">2,307,416,969</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">28,276,849</td>
<td align="right">28,422,874</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,271,966,155</td>
<td align="right">1,278,301,016</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">139,959,944</td>
<td align="right">140,647,110</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,348,604</td>
<td align="right">82,748,434</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">610,576,970</td>
<td align="right">613,529,862</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">311,798,211</td>
<td align="right">310,328,304</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">563,271,658</td>
<td align="right">560,781,797</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">74,048,735</td>
<td align="right">74,372,771</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">150,366,753</td>
<td align="right">149,709,341</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">321,451,192</td>
<td align="right">322,810,567</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">78,599,832</td>
<td align="right">78,922,976</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">446,485,158</td>
<td align="right">444,665,624</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">604,895,368</td>
<td align="right">607,249,719</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">2,320,536</td>
<td align="right">2,329,278</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">10,079,670</td>
<td align="right">10,117,359</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">146,188,910</td>
<td align="right">145,660,184</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">11,058,077</td>
<td align="right">11,097,725</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">117,940,014</td>
<td align="right">118,352,979</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">30,951,740</td>
<td align="right">30,850,895</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">9,976</td>
<td align="right">10,008</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">726,154,545</td>
<td align="right">723,961,176</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">109,460,275</td>
<td align="right">109,133,183</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_FOR_ITER</td>
<td align="right">11,336</td>
<td align="right">11,368</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,256,161,587</td>
<td align="right">1,252,661,507</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">175,069,908</td>
<td align="right">174,598,598</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">234,463,950</td>
<td align="right">235,049,440</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">166,171,975</td>
<td align="right">165,768,490</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">272,767,871</td>
<td align="right">273,422,355</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_POP_JUMP_IF_TRUE</td>
<td align="right">13,416</td>
<td align="right">13,448</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,203,845,197</td>
<td align="right">3,211,411,858</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,517,809,643</td>
<td align="right">1,521,336,845</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">127,216,959</td>
<td align="right">126,948,983</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">321,908,249</td>
<td align="right">322,564,125</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">71,616,720</td>
<td align="right">71,474,001</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,225,026</td>
<td align="right">2,220,634</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">730,850,404</td>
<td align="right">729,423,766</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,627,810,860</td>
<td align="right">5,638,708,923</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,360,431,691</td>
<td align="right">4,368,779,002</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">146,854,133</td>
<td align="right">146,608,142</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,021,969,022</td>
<td align="right">7,032,772,445</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_WITH_DEFAULTS</td>
<td align="right">218,690,307</td>
<td align="right">218,392,478</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">955,406</td>
<td align="right">956,516</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,636,664</td>
<td align="right">36,676,924</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,138,057,628</td>
<td align="right">1,136,993,023</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">59,514,775</td>
<td align="right">59,466,916</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,048,583,803</td>
<td align="right">1,049,426,341</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">58,519,143</td>
<td align="right">58,474,101</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">74,943,075</td>
<td align="right">74,886,890</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">463,391,186</td>
<td align="right">463,058,033</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">230,368,599</td>
<td align="right">230,209,383</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">368,613,304</td>
<td align="right">368,367,288</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">361,455,270</td>
<td align="right">361,216,380</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">677,128,744</td>
<td align="right">676,718,506</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,989,282,328</td>
<td align="right">1,988,164,378</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,251,769,829</td>
<td align="right">1,251,096,353</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">744,968,809</td>
<td align="right">744,584,507</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">169,119,414</td>
<td align="right">169,205,880</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,084,323,471</td>
<td align="right">4,082,582,704</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">95,305,412</td>
<td align="right">95,271,981</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">359,503,918</td>
<td align="right">359,389,881</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">268,027,070</td>
<td align="right">267,943,056</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">131,434,935</td>
<td align="right">131,470,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,383,340,266</td>
<td align="right">1,383,703,266</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">306,600,650</td>
<td align="right">306,526,308</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">110,415,332</td>
<td align="right">110,441,682</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">156,596,776</td>
<td align="right">156,633,581</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,508,640,073</td>
<td align="right">1,508,924,369</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">273,971,542</td>
<td align="right">273,928,557</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">379,922,319</td>
<td align="right">379,981,261</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">156,126,512</td>
<td align="right">156,102,641</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">556,671</td>
<td align="right">556,589</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">202,186,729</td>
<td align="right">202,157,738</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">425,937,172</td>
<td align="right">425,876,367</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">75,504,537</td>
<td align="right">75,494,353</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">348,177,653</td>
<td align="right">348,139,003</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">2,055,119,343</td>
<td align="right">2,054,918,772</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">292,309,460</td>
<td align="right">292,331,399</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">148,458,866</td>
<td align="right">148,448,078</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">181,100,989</td>
<td align="right">181,089,052</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">505,414,630</td>
<td align="right">505,445,535</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">12,594,694</td>
<td align="right">12,594,050</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">23,525</td>
<td align="right">23,524</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">24,464,436</td>
<td align="right">24,463,505</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">24,975,726</td>
<td align="right">24,974,830</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">24,975,871</td>
<td align="right">24,974,978</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">229,788,855</td>
<td align="right">229,784,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,645,809,969</td>
<td align="right">3,645,742,154</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">343,167</td>
<td align="right">343,173</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">71,678,187</td>
<td align="right">71,676,948</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">44,274,976</td>
<td align="right">44,274,293</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,836,366</td>
<td align="right">173,834,338</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,613,910</td>
<td align="right">402,609,535</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">161,281,958</td>
<td align="right">161,280,254</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">787,093,090</td>
<td align="right">787,085,511</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">400,038,546</td>
<td align="right">400,034,702</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">137,018,693</td>
<td align="right">137,017,701</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">176,479,848</td>
<td align="right">176,478,794</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">556,667,931</td>
<td align="right">556,664,734</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">7,752,440</td>
<td align="right">7,752,399</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">12,428,380</td>
<td align="right">12,428,332</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,799,353</td>
<td align="right">20,799,274</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,185,047</td>
<td align="right">6,185,031</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">39,916,889</td>
<td align="right">39,916,987</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">72,237,282</td>
<td align="right">72,237,114</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">135,175,157</td>
<td align="right">135,175,432</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">13,099,501</td>
<td align="right">13,099,526</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">6,692,829</td>
<td align="right">6,692,817</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">64,671,067</td>
<td align="right">64,670,954</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">28,281,471</td>
<td align="right">28,281,498</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">94,700,762</td>
<td align="right">94,700,772</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">96,988,984</td>
<td align="right">96,988,994</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">138,439,328</td>
<td align="right">138,439,328</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">47,320,091</td>
<td align="right">47,320,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_POP_JUMP_IF_FALSE</td>
<td align="right">38,888,640</td>
<td align="right">38,888,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,866,420</td>
<td align="right">38,866,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,857,520</td>
<td align="right">38,857,520</td>
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
<td align="left">STORE_GLOBAL</td>
<td align="right">6,944,700</td>
<td align="right">6,944,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,847,443</td>
<td align="right">3,847,443</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">3,005,920</td>
<td align="right">3,005,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">1,129,926</td>
<td align="right">1,129,926</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">233,480</td>
<td align="right">233,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">200,448</td>
<td align="right">200,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">151,980</td>
<td align="right">151,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">92,500</td>
<td align="right">92,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">28,906</td>
<td align="right">28,906</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">7,200</td>
<td align="right">7,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,260</td>
<td align="right">2,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,240</td>
<td align="right">2,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,504</td>
<td align="right">1,504</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">1,080</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_POP_JUMP_IF_NONE</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_FORWARD</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_POP_JUMP_IF_NOT_NONE</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 Tier 1 instructions </summary>


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
<td align="right">630,764,753</td>
<td align="right">28.3%</td>
<td align="right">633,717,069</td>
<td align="right">28.3%</td>
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
<td align="right">1,598,828,449</td>
<td align="right">71.7%</td>
<td align="right">1,605,751,492</td>
<td align="right">71.7%</td>
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
<td align="right">21,800,771</td>
<td align="right">1.0%</td>
<td align="right">21,800,766</td>
<td align="right">1.0%</td>
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
<td align="right">1,148,344</td>
<td align="right">71.2%</td>
<td align="right">1,148,974</td>
<td align="right">71.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">464,644</td>
<td align="right">28.8%</td>
<td align="right">464,585</td>
<td align="right">28.8%</td>
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
<td align="left">true divide other</td>
<td align="right">3,520</td>
<td align="right">0.3%</td>
<td align="right">3,400</td>
<td align="right">0.3%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">62,335</td>
<td align="right">5.4%</td>
<td align="right">63,377</td>
<td align="right">5.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">40,780</td>
<td align="right">3.6%</td>
<td align="right">40,909</td>
<td align="right">3.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">53,276</td>
<td align="right">4.6%</td>
<td align="right">53,108</td>
<td align="right">4.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,600</td>
<td align="right">2.8%</td>
<td align="right">32,512</td>
<td align="right">2.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,735</td>
<td align="right">0.5%</td>
<td align="right">5,721</td>
<td align="right">0.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">67,754</td>
<td align="right">5.9%</td>
<td align="right">67,636</td>
<td align="right">5.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">2,013</td>
<td align="right">0.2%</td>
<td align="right">2,011</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">65,591</td>
<td align="right">5.7%</td>
<td align="right">65,568</td>
<td align="right">5.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">5,765</td>
<td align="right">0.5%</td>
<td align="right">5,763</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">9,832</td>
<td align="right">0.9%</td>
<td align="right">9,834</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">9,845</td>
<td align="right">0.9%</td>
<td align="right">9,843</td>
<td align="right">0.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">11,824</td>
<td align="right">1.0%</td>
<td align="right">11,823</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">17,447</td>
<td align="right">1.5%</td>
<td align="right">17,446</td>
<td align="right">1.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">736,427</td>
<td align="right">64.1%</td>
<td align="right">736,423</td>
<td align="right">64.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">12,194</td>
<td align="right">1.1%</td>
<td align="right">12,194</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,627</td>
<td align="right">0.5%</td>
<td align="right">5,627</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">5,200</td>
<td align="right">0.5%</td>
<td align="right">5,200</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">579</td>
<td align="right">0.1%</td>
<td align="right">579</td>
<td align="right">0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,811,761,098</td>
<td align="right">80.8%</td>
<td align="right">1,806,308,069</td>
<td align="right">80.7%</td>
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
<td align="right">430,449,342</td>
<td align="right">19.2%</td>
<td align="right">430,388,755</td>
<td align="right">19.2%</td>
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
<td align="right">4,899,788</td>
<td align="right">0.2%</td>
<td align="right">4,899,786</td>
<td align="right">0.2%</td>
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
<td align="right">185,831</td>
<td align="right">47.9%</td>
<td align="right">185,620</td>
<td align="right">47.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">201,787</td>
<td align="right">52.1%</td>
<td align="right">201,778</td>
<td align="right">52.1%</td>
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
<td align="left">tuple slice</td>
<td align="right">185</td>
<td align="right">0.1%</td>
<td align="right">183</td>
<td align="right">0.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">57,091</td>
<td align="right">30.7%</td>
<td align="right">56,917</td>
<td align="right">30.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">22,578</td>
<td align="right">12.1%</td>
<td align="right">22,544</td>
<td align="right">12.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">78,281</td>
<td align="right">42.1%</td>
<td align="right">78,280</td>
<td align="right">42.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,680</td>
<td align="right">9.0%</td>
<td align="right">16,680</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">5,036</td>
<td align="right">2.7%</td>
<td align="right">5,036</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">2.3%</td>
<td align="right">4,300</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">900</td>
<td align="right">0.5%</td>
<td align="right">900</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">680</td>
<td align="right">0.4%</td>
<td align="right">680</td>
<td align="right">0.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,827,420,307</td>
<td align="right">83.9%</td>
<td align="right">8,154,527,044</td>
<td align="right">84.4%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">254,221,033</td>
<td align="right">2.7%</td>
<td align="right">254,794,545</td>
<td align="right">2.6%</td>
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
<td align="right">1,499,552,768</td>
<td align="right">16.1%</td>
<td align="right">1,499,442,795</td>
<td align="right">15.5%</td>
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
<td align="right">39,400</td>
<td align="right">0.0%</td>
<td align="right">39,400</td>
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
<td align="right">5,418,994</td>
<td align="right">84.2%</td>
<td align="right">5,429,726</td>
<td align="right">84.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,019,100</td>
<td align="right">15.8%</td>
<td align="right">1,018,377</td>
<td align="right">15.8%</td>
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
<td align="left">metaclass</td>
<td align="right">43,587</td>
<td align="right">4.3%</td>
<td align="right">43,252</td>
<td align="right">4.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">method wrapper</td>
<td align="right">8,250</td>
<td align="right">0.8%</td>
<td align="right">8,276</td>
<td align="right">0.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">78,747</td>
<td align="right">7.7%</td>
<td align="right">78,581</td>
<td align="right">7.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">class mutable</td>
<td align="right">24,704</td>
<td align="right">2.4%</td>
<td align="right">24,654</td>
<td align="right">2.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">cfunc varargs keywords</td>
<td align="right">32,079</td>
<td align="right">3.1%</td>
<td align="right">32,028</td>
<td align="right">3.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">bound method</td>
<td align="right">11,850</td>
<td align="right">1.2%</td>
<td align="right">11,832</td>
<td align="right">1.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">meth descr varargs keywords</td>
<td align="right">20,857</td>
<td align="right">2.0%</td>
<td align="right">20,835</td>
<td align="right">2.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">cfunc noargs</td>
<td align="right">70,042</td>
<td align="right">6.9%</td>
<td align="right">69,988</td>
<td align="right">6.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">operator wrapper</td>
<td align="right">10,140</td>
<td align="right">1.0%</td>
<td align="right">10,144</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">cfunc varargs</td>
<td align="right">14,147</td>
<td align="right">1.4%</td>
<td align="right">14,151</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">186,086</td>
<td align="right">18.3%</td>
<td align="right">186,045</td>
<td align="right">18.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">72,069</td>
<td align="right">7.1%</td>
<td align="right">72,076</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">meth descr varargs</td>
<td align="right">74,719</td>
<td align="right">7.3%</td>
<td align="right">74,712</td>
<td align="right">7.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">meth descr method fastcall keywords</td>
<td align="right">207,269</td>
<td align="right">20.3%</td>
<td align="right">207,251</td>
<td align="right">20.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">105,156</td>
<td align="right">10.3%</td>
<td align="right">105,154</td>
<td align="right">10.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">16,406</td>
<td align="right">1.6%</td>
<td align="right">16,406</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">13,934</td>
<td align="right">1.4%</td>
<td align="right">13,934</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">cmethod</td>
<td align="right">13,620</td>
<td align="right">1.3%</td>
<td align="right">13,620</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">12,258</td>
<td align="right">1.2%</td>
<td align="right">12,258</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">3,180</td>
<td align="right">0.3%</td>
<td align="right">3,180</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">160</td>
<td align="right">0.0%</td>
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
<td align="right">141,347,513</td>
<td align="right">7.4%</td>
<td align="right">142,030,251</td>
<td align="right">7.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,722,053</td>
<td align="right">0.1%</td>
<td align="right">1,717,586</td>
<td align="right">0.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,757,448,772</td>
<td align="right">92.5%</td>
<td align="right">1,754,597,098</td>
<td align="right">92.5%</td>
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
<td align="right">110,550</td>
<td align="right">33.1%</td>
<td align="right">110,452</td>
<td align="right">33.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">223,934</td>
<td align="right">66.9%</td>
<td align="right">223,993</td>
<td align="right">67.0%</td>
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
<td align="right">33,670</td>
<td align="right">15.0%</td>
<td align="right">34,282</td>
<td align="right">15.3%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">1,540</td>
<td align="right">0.7%</td>
<td align="right">1,527</td>
<td align="right">0.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">48,862</td>
<td align="right">21.8%</td>
<td align="right">48,582</td>
<td align="right">21.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">62,733</td>
<td align="right">28.0%</td>
<td align="right">62,473</td>
<td align="right">27.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">3,737</td>
<td align="right">1.7%</td>
<td align="right">3,744</td>
<td align="right">1.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">13,249</td>
<td align="right">5.9%</td>
<td align="right">13,231</td>
<td align="right">5.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">23,863</td>
<td align="right">10.7%</td>
<td align="right">23,871</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">14,486</td>
<td align="right">6.5%</td>
<td align="right">14,489</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">11,080</td>
<td align="right">4.9%</td>
<td align="right">11,080</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">4,251</td>
<td align="right">1.9%</td>
<td align="right">4,251</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,120</td>
<td align="right">1.8%</td>
<td align="right">4,120</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,343</td>
<td align="right">1.0%</td>
<td align="right">2,343</td>
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
<td align="right">118,807,964</td>
<td align="right">14.8%</td>
<td align="right">118,144,593</td>
<td align="right">14.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">685,797,949</td>
<td align="right">85.2%</td>
<td align="right">688,745,855</td>
<td align="right">85.3%</td>
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
<td align="right">2,546,240</td>
<td align="right">0.3%</td>
<td align="right">2,546,240</td>
<td align="right">0.3%</td>
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
<td align="right">131,631</td>
<td align="right">66.1%</td>
<td align="right">131,700</td>
<td align="right">66.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">67,473</td>
<td align="right">33.9%</td>
<td align="right">67,470</td>
<td align="right">33.9%</td>
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
<td align="left">list</td>
<td align="right">19,301</td>
<td align="right">14.7%</td>
<td align="right">19,442</td>
<td align="right">14.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">46,975</td>
<td align="right">35.7%</td>
<td align="right">46,891</td>
<td align="right">35.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">36,472</td>
<td align="right">27.7%</td>
<td align="right">36,499</td>
<td align="right">27.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">28,883</td>
<td align="right">21.9%</td>
<td align="right">28,868</td>
<td align="right">21.9%</td>
<td align="right">-0.1%</td>
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
<td align="right">1,317,194,295</td>
<td align="right">82.8%</td>
<td align="right">1,328,694,641</td>
<td align="right">82.9%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">271,247,784</td>
<td align="right">17.0%</td>
<td align="right">270,895,163</td>
<td align="right">16.9%</td>
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
<td align="right">127,062,522</td>
<td align="right">8.0%</td>
<td align="right">126,949,048</td>
<td align="right">7.9%</td>
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
<td align="right">205,296</td>
<td align="right">7.7%</td>
<td align="right">200,635</td>
<td align="right">7.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,463,575</td>
<td align="right">92.3%</td>
<td align="right">2,461,392</td>
<td align="right">92.5%</td>
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
<td align="left">dict items</td>
<td align="right">73,131</td>
<td align="right">35.6%</td>
<td align="right">68,425</td>
<td align="right">34.1%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">8,065</td>
<td align="right">3.9%</td>
<td align="right">8,025</td>
<td align="right">4.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">27,918</td>
<td align="right">13.6%</td>
<td align="right">27,994</td>
<td align="right">14.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">14,878</td>
<td align="right">7.2%</td>
<td align="right">14,918</td>
<td align="right">7.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">14,734</td>
<td align="right">7.2%</td>
<td align="right">14,714</td>
<td align="right">7.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">21,206</td>
<td align="right">10.3%</td>
<td align="right">21,195</td>
<td align="right">10.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,899</td>
<td align="right">7.3%</td>
<td align="right">14,899</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">10,540</td>
<td align="right">5.1%</td>
<td align="right">10,540</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">7,633</td>
<td align="right">3.7%</td>
<td align="right">7,633</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">7,030</td>
<td align="right">3.4%</td>
<td align="right">7,030</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,700</td>
<td align="right">1.3%</td>
<td align="right">2,700</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">1,600</td>
<td align="right">0.8%</td>
<td align="right">1,600</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">660</td>
<td align="right">0.3%</td>
<td align="right">660</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">282</td>
<td align="right">0.1%</td>
<td align="right">282</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">1,592,587,646</td>
<td align="right">13.7%</td>
<td align="right">1,606,695,558</td>
<td align="right">13.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,045,413,710</td>
<td align="right">86.2%</td>
<td align="right">10,071,935,721</td>
<td align="right">86.1%</td>
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
<td align="right">558,733,931</td>
<td align="right">4.8%</td>
<td align="right">559,226,644</td>
<td align="right">4.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,139,322</td>
<td align="right">0.0%</td>
<td align="right">2,139,446</td>
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
<td align="right">1,415,257</td>
<td align="right">11.0%</td>
<td align="right">1,421,239</td>
<td align="right">11.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,405,566</td>
<td align="right">89.0%</td>
<td align="right">11,414,985</td>
<td align="right">88.9%</td>
<td align="right">0.1%</td>
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
<td align="right">22,490</td>
<td align="right">1.6%</td>
<td align="right">25,370</td>
<td align="right">1.8%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">76,569</td>
<td align="right">5.4%</td>
<td align="right">77,290</td>
<td align="right">5.4%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">109,723</td>
<td align="right">7.8%</td>
<td align="right">110,268</td>
<td align="right">7.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">192,886</td>
<td align="right">13.6%</td>
<td align="right">193,393</td>
<td align="right">13.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">has managed dict</td>
<td align="right">549,864</td>
<td align="right">38.9%</td>
<td align="right">551,123</td>
<td align="right">38.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">119,526</td>
<td align="right">8.4%</td>
<td align="right">119,757</td>
<td align="right">8.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">13,718</td>
<td align="right">1.0%</td>
<td align="right">13,696</td>
<td align="right">1.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">26,195</td>
<td align="right">1.9%</td>
<td align="right">26,174</td>
<td align="right">1.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">209,720</td>
<td align="right">14.8%</td>
<td align="right">209,607</td>
<td align="right">14.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">19,407</td>
<td align="right">1.4%</td>
<td align="right">19,402</td>
<td align="right">1.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">29,320</td>
<td align="right">2.1%</td>
<td align="right">29,320</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">17,582</td>
<td align="right">1.2%</td>
<td align="right">17,582</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">13,420</td>
<td align="right">0.9%</td>
<td align="right">13,420</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">3,776</td>
<td align="right">0.3%</td>
<td align="right">3,776</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">3,620</td>
<td align="right">0.3%</td>
<td align="right">3,620</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3,600</td>
<td align="right">0.3%</td>
<td align="right">3,600</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">2,341</td>
<td align="right">0.2%</td>
<td align="right">2,341</td>
<td align="right">0.2%</td>
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
<td align="left">property</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">6,348,745,296</td>
<td align="right">99.7%</td>
<td align="right">6,858,946,481</td>
<td align="right">99.7%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">365,114</td>
<td align="right">0.0%</td>
<td align="right">362,748</td>
<td align="right">0.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,497,225</td>
<td align="right">0.3%</td>
<td align="right">20,494,839</td>
<td align="right">0.3%</td>
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
<td align="right">12,982</td>
<td align="right">0.0%</td>
<td align="right">12,982</td>
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
<td align="right">667,242</td>
<td align="right">100.0%</td>
<td align="right">667,183</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">134,969,399</td>
<td align="right">100.0%</td>
<td align="right">134,701,382</td>
<td align="right">100.0%</td>
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
<td align="right">11,828</td>
<td align="right">0.0%</td>
<td align="right">11,827</td>
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
<td align="left">Success</td>
<td align="right">11,697</td>
<td align="right">100.0%</td>
<td align="right">11,697</td>
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
<td align="right">173,798,444</td>
<td align="right">18.1%</td>
<td align="right">173,796,434</td>
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
<td align="right">787,062,190</td>
<td align="right">81.9%</td>
<td align="right">787,054,611</td>
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
<td align="right">30,900</td>
<td align="right">0.0%</td>
<td align="right">30,900</td>
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
<td align="right">7,085</td>
<td align="right">10.3%</td>
<td align="right">7,088</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,737</td>
<td align="right">89.7%</td>
<td align="right">61,716</td>
<td align="right">89.7%</td>
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
<td align="left">other</td>
<td align="right">16,117</td>
<td align="right">26.1%</td>
<td align="right">16,096</td>
<td align="right">26.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">53.7%</td>
<td align="right">33,180</td>
<td align="right">53.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,980</td>
<td align="right">16.2%</td>
<td align="right">9,980</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,220</td>
<td align="right">3.6%</td>
<td align="right">2,220</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">240</td>
<td align="right">0.4%</td>
<td align="right">240</td>
<td align="right">0.4%</td>
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
<td align="right">166,250,582</td>
<td align="right">6.0%</td>
<td align="right">165,545,886</td>
<td align="right">5.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">235,064,812</td>
<td align="right">8.4%</td>
<td align="right">234,373,264</td>
<td align="right">8.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,545,118,186</td>
<td align="right">91.4%</td>
<td align="right">2,545,042,460</td>
<td align="right">91.5%</td>
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
<td align="right">3,292,010</td>
<td align="right">96.2%</td>
<td align="right">3,278,759</td>
<td align="right">96.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">131,042</td>
<td align="right">3.8%</td>
<td align="right">130,977</td>
<td align="right">3.8%</td>
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
<td align="left">class attr simple</td>
<td align="right">50,218</td>
<td align="right">38.3%</td>
<td align="right">50,157</td>
<td align="right">38.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">28,512</td>
<td align="right">21.8%</td>
<td align="right">28,508</td>
<td align="right">21.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">15,725</td>
<td align="right">12.0%</td>
<td align="right">15,725</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">10,640</td>
<td align="right">8.1%</td>
<td align="right">10,640</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">7,961</td>
<td align="right">6.1%</td>
<td align="right">7,961</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">6,832</td>
<td align="right">5.2%</td>
<td align="right">6,832</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">5,580</td>
<td align="right">4.3%</td>
<td align="right">5,580</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">3,420</td>
<td align="right">2.6%</td>
<td align="right">3,420</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,520</td>
<td align="right">1.2%</td>
<td align="right">1,520</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">594</td>
<td align="right">0.5%</td>
<td align="right">594</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="right">287,546,257</td>
<td align="right">65.7%</td>
<td align="right">286,247,967</td>
<td align="right">65.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">150,263,465</td>
<td align="right">34.3%</td>
<td align="right">149,606,287</td>
<td align="right">34.3%</td>
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
<td align="right">2,880</td>
<td align="right">0.0%</td>
<td align="right">2,880</td>
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
<td align="right">87,521</td>
<td align="right">82.4%</td>
<td align="right">87,286</td>
<td align="right">82.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,647</td>
<td align="right">17.6%</td>
<td align="right">18,648</td>
<td align="right">17.6%</td>
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
<td align="left">array int</td>
<td align="right">7,200</td>
<td align="right">8.2%</td>
<td align="right">7,040</td>
<td align="right">8.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">43,557</td>
<td align="right">49.8%</td>
<td align="right">43,479</td>
<td align="right">49.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">29,856</td>
<td align="right">34.1%</td>
<td align="right">29,859</td>
<td align="right">34.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,748</td>
<td align="right">4.3%</td>
<td align="right">3,748</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,080</td>
<td align="right">2.4%</td>
<td align="right">2,080</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,080</td>
<td align="right">1.2%</td>
<td align="right">1,080</td>
<td align="right">1.2%</td>
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
<td align="right">3,845,421,429</td>
<td align="right">91.7%</td>
<td align="right">3,994,659,036</td>
<td align="right">91.8%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">344,794,093</td>
<td align="right">8.2%</td>
<td align="right">356,192,775</td>
<td align="right">8.2%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">104,141,131</td>
<td align="right">2.5%</td>
<td align="right">106,896,723</td>
<td align="right">2.5%</td>
<td align="right">2.6%</td>
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
<td align="right">2,249,151</td>
<td align="right">78.3%</td>
<td align="right">2,301,313</td>
<td align="right">78.6%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">623,260</td>
<td align="right">21.7%</td>
<td align="right">627,227</td>
<td align="right">21.4%</td>
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
<td align="left">dict</td>
<td align="right">31,070</td>
<td align="right">5.0%</td>
<td align="right">33,059</td>
<td align="right">5.3%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">95,821</td>
<td align="right">15.4%</td>
<td align="right">97,563</td>
<td align="right">15.6%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">58,158</td>
<td align="right">9.3%</td>
<td align="right">58,510</td>
<td align="right">9.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">18,152</td>
<td align="right">2.9%</td>
<td align="right">18,095</td>
<td align="right">2.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,238</td>
<td align="right">0.2%</td>
<td align="right">1,235</td>
<td align="right">0.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,997</td>
<td align="right">3.0%</td>
<td align="right">18,987</td>
<td align="right">3.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">39,428</td>
<td align="right">6.3%</td>
<td align="right">39,448</td>
<td align="right">6.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">183,625</td>
<td align="right">29.5%</td>
<td align="right">183,565</td>
<td align="right">29.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">173,751</td>
<td align="right">27.9%</td>
<td align="right">173,745</td>
<td align="right">27.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2,600</td>
<td align="right">0.4%</td>
<td align="right">2,600</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">420</td>
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
<td align="right">953,848,090</td>
<td align="right">99.9%</td>
<td align="right">967,502,485</td>
<td align="right">99.9%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">426,660</td>
<td align="right">0.0%</td>
<td align="right">427,900</td>
<td align="right">0.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">923,914</td>
<td align="right">0.1%</td>
<td align="right">925,066</td>
<td align="right">0.1%</td>
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
<td align="right">3,516</td>
<td align="right">5.9%</td>
<td align="right">3,514</td>
<td align="right">5.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">55,901</td>
<td align="right">94.1%</td>
<td align="right">55,909</td>
<td align="right">94.1%</td>
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
<td align="right">2,435</td>
<td align="right">69.3%</td>
<td align="right">2,433</td>
<td align="right">69.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">701</td>
<td align="right">19.9%</td>
<td align="right">701</td>
<td align="right">19.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">10.8%</td>
<td align="right">380</td>
<td align="right">10.8%</td>
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
<td align="right">46,905,815,745</td>
<td align="right">34.9%</td>
<td align="right">47,951,457,244</td>
<td align="right">35.0%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">12,563,725,322</td>
<td align="right">9.3%</td>
<td align="right">12,840,276,624</td>
<td align="right">9.4%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">73,815,701,719</td>
<td align="right">54.9%</td>
<td align="right">74,962,597,601</td>
<td align="right">54.7%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,242,725,258</td>
<td align="right">0.9%</td>
<td align="right">1,245,723,909</td>
<td align="right">0.9%</td>
<td align="right">0.2%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">344,794,093</td>
<td align="right">6.1%</td>
<td align="right">356,192,775</td>
<td align="right">6.3%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,592,587,646</td>
<td align="right">28.4%</td>
<td align="right">1,606,695,558</td>
<td align="right">28.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">141,347,513</td>
<td align="right">2.5%</td>
<td align="right">142,030,251</td>
<td align="right">2.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">630,764,753</td>
<td align="right">11.2%</td>
<td align="right">633,717,069</td>
<td align="right">11.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">150,263,465</td>
<td align="right">2.7%</td>
<td align="right">149,606,287</td>
<td align="right">2.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">235,064,812</td>
<td align="right">4.2%</td>
<td align="right">234,373,264</td>
<td align="right">4.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">271,247,784</td>
<td align="right">4.8%</td>
<td align="right">270,895,163</td>
<td align="right">4.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">430,449,342</td>
<td align="right">7.7%</td>
<td align="right">430,388,755</td>
<td align="right">7.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,499,552,768</td>
<td align="right">26.7%</td>
<td align="right">1,499,442,795</td>
<td align="right">26.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,798,444</td>
<td align="right">3.1%</td>
<td align="right">173,796,434</td>
<td align="right">3.1%</td>
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
<td align="right">70,807,869</td>
<td align="right">5.7%</td>
<td align="right">70,091,388</td>
<td align="right">5.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">131,463,099</td>
<td align="right">10.6%</td>
<td align="right">131,654,711</td>
<td align="right">10.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">63,491,713</td>
<td align="right">5.1%</td>
<td align="right">63,429,960</td>
<td align="right">5.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">63,333,809</td>
<td align="right">5.1%</td>
<td align="right">63,280,928</td>
<td align="right">5.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">70,252,873</td>
<td align="right">5.7%</td>
<td align="right">70,306,689</td>
<td align="right">5.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">160,299,915</td>
<td align="right">12.9%</td>
<td align="right">160,198,085</td>
<td align="right">12.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">109,243,148</td>
<td align="right">8.8%</td>
<td align="right">109,289,253</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">152,993,515</td>
<td align="right">12.3%</td>
<td align="right">152,974,176</td>
<td align="right">12.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">95,390,005</td>
<td align="right">7.7%</td>
<td align="right">95,401,835</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">48,929,627</td>
<td align="right">3.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">49,637,844</td>
<td align="right">4.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">874,844,993</td>
<td align="right">11.6%</td>
<td align="right">861,471,847</td>
<td align="right">11.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,323,248,091</td>
<td align="right">30.7%</td>
<td align="right">2,311,083,969</td>
<td align="right">30.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,323,248,091</td>
<td align="right">30.7%</td>
<td align="right">2,311,083,969</td>
<td align="right">30.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">477,625,405</td>
<td align="right">6.3%</td>
<td align="right">479,913,285</td>
<td align="right">6.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,243,040,650</td>
<td align="right">69.3%</td>
<td align="right">5,266,038,329</td>
<td align="right">69.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">258,077,408</td>
<td align="right">3.4%</td>
<td align="right">257,543,668</td>
<td align="right">3.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,443,955,888</td>
<td align="right">19.1%</td>
<td align="right">1,445,164,912</td>
<td align="right">19.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,448,403,098</td>
<td align="right">19.1%</td>
<td align="right">1,449,612,122</td>
<td align="right">19.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">4,969,862,157</td>
<td align="right">65.7%</td>
<td align="right">4,965,889,136</td>
<td align="right">65.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">38,354,634</td>
<td align="right">0.5%</td>
<td align="right">38,341,989</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">213,125,297</td>
<td align="right">2.8%</td>
<td align="right">213,111,549</td>
<td align="right">2.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">88,452,602</td>
<td align="right">1.2%</td>
<td align="right">88,448,274</td>
<td align="right">1.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,418,304</td>
<td align="right">0.1%</td>
<td align="right">4,418,304</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">28,906</td>
<td align="right">0.0%</td>
<td align="right">28,906</td>
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

"New values" is the number of values arrays created for objects with
managed dicts.

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
<td align="right">13,378,779</td>
<td align="right"></td>
<td align="right">14,425,614</td>
<td align="right"></td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">87,121,054</td>
<td align="right"></td>
<td align="right">89,863,232</td>
<td align="right"></td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">81,517,670</td>
<td align="right"></td>
<td align="right">83,216,325</td>
<td align="right"></td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,883,930,214</td>
<td align="right">36.6%</td>
<td align="right">6,818,372,066</td>
<td align="right">36.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,891,862,737</td>
<td align="right"></td>
<td align="right">6,826,252,584</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,811,187,049</td>
<td align="right">62.8%</td>
<td align="right">11,760,672,869</td>
<td align="right">62.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,937,516,958</td>
<td align="right">63.4%</td>
<td align="right">11,886,651,801</td>
<td align="right">63.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Dematerialize dict</td>
<td align="right">2,704,760</td>
<td align="right">3.0%</td>
<td align="right">2,693,440</td>
<td align="right">3.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">12,292,227,351</td>
<td align="right"></td>
<td align="right">12,241,126,090</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">108,383,069,804</td>
<td align="right">78.5%</td>
<td align="right">107,981,726,126</td>
<td align="right">78.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">105,137,040</td>
<td align="right">0.6%</td>
<td align="right">104,813,011</td>
<td align="right">0.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">93,734,014,555</td>
<td align="right">77.8%</td>
<td align="right">93,449,262,284</td>
<td align="right">77.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">26,809,911,986</td>
<td align="right">22.2%</td>
<td align="right">26,730,043,366</td>
<td align="right">22.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">29,770,176,253</td>
<td align="right">21.5%</td>
<td align="right">29,690,839,633</td>
<td align="right">21.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,273,425</td>
<td align="right">4.7%</td>
<td align="right">4,262,065</td>
<td align="right">4.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">New values</td>
<td align="right">90,965,747</td>
<td align="right"></td>
<td align="right">90,814,293</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">21,192,869</td>
<td align="right">0.1%</td>
<td align="right">21,165,921</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,309,933,371</td>
<td align="right"></td>
<td align="right">3,306,330,363</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,563,897,075</td>
<td align="right"></td>
<td align="right">3,564,658,779</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">215,335</td>
<td align="right">0.2%</td>
<td align="right">215,335</td>
<td align="right">0.2%</td>
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
<td align="right">745,843</td>
<td align="right">46,927,240</td>
<td align="right">6,179,285,346</td>
<td align="right">745,897</td>
<td align="right">46,785,332</td>
<td align="right">6,182,438,784</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">66,746</td>
<td align="right">36,611,134</td>
<td align="right">5,049,440,552</td>
<td align="right">66,743</td>
<td align="right">36,867,229</td>
<td align="right">5,051,589,412</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">20,991</td>
<td align="right">53,686,146</td>
<td align="right">18,392,572,533</td>
<td align="right">20,980</td>
<td align="right">53,528,352</td>
<td align="right">18,347,142,900</td>
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
<td align="right">2,273</td>
<td align="right">0.0%</td>
<td align="right">409</td>
<td align="right">0.0%</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">178,896,312,704</td>
<td align="right">2,854.3%</td>
<td align="right">257,889,671,479</td>
<td align="right">4,381.5%</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">54,565,148</td>
<td align="right">95.9%</td>
<td align="right">45,066,983</td>
<td align="right">95.1%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">56,891,194</td>
<td align="right"></td>
<td align="right">47,398,580</td>
<td align="right"></td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">16,672,025</td>
<td align="right">29.3%</td>
<td align="right">14,783,583</td>
<td align="right">31.2%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">421,395</td>
<td align="right">0.7%</td>
<td align="right">375,493</td>
<td align="right">0.8%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,267,531,895</td>
<td align="right"></td>
<td align="right">5,885,810,156</td>
<td align="right"></td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">7,706</td>
<td align="right">0.0%</td>
<td align="right">7,444</td>
<td align="right">0.0%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">5,620</td>
<td align="right">0.2%</td>
<td align="right">5,580</td>
<td align="right">0.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">781,672</td>
<td align="right">1.4%</td>
<td align="right">776,473</td>
<td align="right">1.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,326,046</td>
<td align="right">4.1%</td>
<td align="right">2,331,597</td>
<td align="right">4.9%</td>
<td align="right">0.2%</td>
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
<td align="right">100,887</td>
<td align="right">4.3%</td>
<td align="right">99,088</td>
<td align="right">4.2%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,326,046</td>
<td align="right"></td>
<td align="right">2,331,597</td>
<td align="right"></td>
<td align="right">0.2%</td>
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
<td align="right">4,197</td>
<td align="right">0.2%</td>
<td align="right">3,019</td>
<td align="right">0.1%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">788,915</td>
<td align="right">33.9%</td>
<td align="right">777,266</td>
<td align="right">33.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">248,479</td>
<td align="right">10.7%</td>
<td align="right">269,159</td>
<td align="right">11.5%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">777,161</td>
<td align="right">33.4%</td>
<td align="right">777,937</td>
<td align="right">33.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">496,597</td>
<td align="right">21.3%</td>
<td align="right">495,317</td>
<td align="right">21.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,472</td>
<td align="right">0.4%</td>
<td align="right">7,853</td>
<td align="right">0.3%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,225</td>
<td align="right">0.1%</td>
<td align="right">786</td>
<td align="right">0.0%</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">260</td>
<td align="right">0.0%</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">8,000.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">8,861</td>
<td align="right">0.4%</td>
<td align="right">9,169</td>
<td align="right">0.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">31,473</td>
<td align="right">1.4%</td>
<td align="right">31,403</td>
<td align="right">1.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">32,216</td>
<td align="right">1.4%</td>
<td align="right">30,715</td>
<td align="right">1.3%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">18,340</td>
<td align="right">0.8%</td>
<td align="right">17,829</td>
<td align="right">0.8%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,326</td>
<td align="right">0.3%</td>
<td align="right">7,207</td>
<td align="right">0.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,090</td>
<td align="right">0.1%</td>
<td align="right">2,144</td>
<td align="right">0.1%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">580</td>
<td align="right">0.0%</td>
<td align="right">540</td>
<td align="right">0.0%</td>
<td align="right">-6.9%</td>
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
<tr>
<td align="left"><= 2</td>
<td align="right">22,715,260</td>
<td align="right">0.4%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">538,968,636</td>
<td align="right">8.6%</td>
<td align="right">93,288,696</td>
<td align="right">1.6%</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">540,114,656</td>
<td align="right">8.6%</td>
<td align="right">608,760,592</td>
<td align="right">10.3%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,237,006,660</td>
<td align="right">19.7%</td>
<td align="right">738,508,145</td>
<td align="right">12.5%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">997,819,559</td>
<td align="right">15.9%</td>
<td align="right">1,487,950,623</td>
<td align="right">25.3%</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">626,306,290</td>
<td align="right">10.0%</td>
<td align="right">693,060,889</td>
<td align="right">11.8%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">317,620,081</td>
<td align="right">5.1%</td>
<td align="right">501,632,268</td>
<td align="right">8.5%</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">122,349,120</td>
<td align="right">2.0%</td>
<td align="right">167,738,937</td>
<td align="right">2.8%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">25,522,540</td>
<td align="right">0.4%</td>
<td align="right">46,399,375</td>
<td align="right">0.8%</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">7,561,641</td>
<td align="right">0.1%</td>
<td align="right">17,372,375</td>
<td align="right">0.3%</td>
<td align="right">129.7%</td>
</tr>
<tr>
<td align="left"><= 2,048</td>
<td align="right">18,455,765</td>
<td align="right">0.3%</td>
<td align="right">7,068,343</td>
<td align="right">0.1%</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left"><= 4,096</td>
<td align="right">691,986</td>
<td align="right">0.0%</td>
<td align="right">15,014,048</td>
<td align="right">0.3%</td>
<td align="right">2,069.7%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="right">740,618</td>
<td align="right">0.0%</td>
<td align="right">633,849</td>
<td align="right">0.0%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="right">263,700</td>
<td align="right">0.0%</td>
<td align="right">542,480</td>
<td align="right">0.0%</td>
<td align="right">105.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="right">41,280</td>
<td align="right">0.0%</td>
<td align="right">228,240</td>
<td align="right">0.0%</td>
<td align="right">452.9%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="right">13,281</td>
<td align="right">0.0%</td>
<td align="right">44,800</td>
<td align="right">0.0%</td>
<td align="right">237.3%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="right">1,028</td>
<td align="right">0.0%</td>
<td align="right">9,120</td>
<td align="right">0.0%</td>
<td align="right">787.2%</td>
</tr>
<tr>
<td align="left"><= 262,144</td>
<td align="right">2,180</td>
<td align="right">0.0%</td>
<td align="right">2,159</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left"><= 524,288</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">601</td>
<td align="right">0.0%</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left"><= 1,048,576</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">520</td>
<td align="right">0.0%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left"><= 2,097,152</td>
<td align="right">138</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 4,194,304</td>
<td align="right">342</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left"><= 8,388,608</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">160 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 16,777,216</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">4,074,181</td>
<td align="right">80,786</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">933,151</td>
<td align="right">1,237,071</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">4,171,087</td>
<td align="right">2,863,707</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">14,252,236</td>
<td align="right">9,905,506</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,008,941,158</td>
<td align="right">732,524,094</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">356,863</td>
<td align="right">278,673</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">783,351,580</td>
<td align="right">645,352,466</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">1,811,336,034</td>
<td align="right">1,507,553,376</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,821,781,257</td>
<td align="right">1,535,896,393</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,176,530,780</td>
<td align="right">1,874,481,803</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">214,622,490</td>
<td align="right">186,372,366</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,335,236,770</td>
<td align="right">2,030,503,574</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">377,978,031</td>
<td align="right">332,652,584</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">359,001,149</td>
<td align="right">322,661,117</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">22,475,540</td>
<td align="right">20,462,270</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,830,647,797</td>
<td align="right">1,684,994,737</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">52,095,388</td>
<td align="right">48,064,262</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,232,043,818</td>
<td align="right">1,137,277,338</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">27,061,356</td>
<td align="right">25,364,420</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">65,699,444</td>
<td align="right">61,613,720</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">65,759,284</td>
<td align="right">61,673,560</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">581,660</td>
<td align="right">545,860</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,163,471,381</td>
<td align="right">1,093,457,049</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">256,897,418</td>
<td align="right">241,830,588</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">577,835,760</td>
<td align="right">545,839,980</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">7,605,255</td>
<td align="right">7,206,732</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,154,850,061</td>
<td align="right">8,700,718,879</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">695,554,185</td>
<td align="right">662,960,152</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">2,151,327,868</td>
<td align="right">2,053,815,318</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">71,050,154</td>
<td align="right">67,853,454</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,338,418,776</td>
<td align="right">5,099,434,387</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">93,373,970</td>
<td align="right">89,202,487</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">736,909,376</td>
<td align="right">704,228,298</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">738,267,136</td>
<td align="right">705,586,058</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">607,162,074</td>
<td align="right">582,711,253</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">1,640,032,341</td>
<td align="right">1,576,687,182</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">5,190,822,560</td>
<td align="right">5,005,349,911</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">399,182,237</td>
<td align="right">386,465,616</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">16,109,217,426</td>
<td align="right">15,605,183,680</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,257,271,323</td>
<td align="right">1,218,359,057</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">17,710,935,068</td>
<td align="right">17,173,780,599</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">468,268</td>
<td align="right">454,108</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">447,599,113</td>
<td align="right">434,355,872</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">309,325,538</td>
<td align="right">300,439,847</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">148,705,948</td>
<td align="right">144,460,302</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,192,923,180</td>
<td align="right">1,160,924,560</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">52,084,073</td>
<td align="right">53,470,100</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,763,500,693</td>
<td align="right">4,645,573,167</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">43,360,221</td>
<td align="right">42,327,943</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">18,356,010</td>
<td align="right">18,768,001</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">498,337,483</td>
<td align="right">487,493,428</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">1,845,184,965</td>
<td align="right">1,806,250,918</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">19,433,835</td>
<td align="right">19,825,993</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,551,280,976</td>
<td align="right">2,504,521,969</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">350,822,961</td>
<td align="right">344,467,873</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,456,195,861</td>
<td align="right">4,378,256,780</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,390,435,282</td>
<td align="right">2,354,130,975</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,096,992,249</td>
<td align="right">2,065,287,066</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,123,160,984</td>
<td align="right">1,106,762,664</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">23,203,801</td>
<td align="right">22,879,765</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">597,598,204</td>
<td align="right">590,117,849</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">140,777,596</td>
<td align="right">139,025,176</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,250,264,960</td>
<td align="right">1,234,887,165</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">657,860,450</td>
<td align="right">650,397,433</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">678,361,938</td>
<td align="right">670,880,035</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,192,728,078</td>
<td align="right">1,179,590,996</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,193,420,211</td>
<td align="right">1,180,283,159</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,193,420,211</td>
<td align="right">1,180,283,159</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,193,466,096</td>
<td align="right">1,180,330,947</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">222,507,123</td>
<td align="right">220,133,634</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">808,431,941</td>
<td align="right">800,269,805</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">676,050,501</td>
<td align="right">669,469,373</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">2,879,188</td>
<td align="right">2,904,886</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">55,889,857</td>
<td align="right">55,395,257</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">5,182,805,782</td>
<td align="right">5,137,182,488</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">329,383,764</td>
<td align="right">326,802,065</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">899,170,766</td>
<td align="right">892,291,211</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">175,674,784</td>
<td align="right">177,006,028</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">106,918,648</td>
<td align="right">107,717,536</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,303,566,916</td>
<td align="right">6,257,016,823</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">102,603,446</td>
<td align="right">101,846,610</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES</td>
<td align="right">103,299,386</td>
<td align="right">102,542,550</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,052,306,285</td>
<td align="right">1,059,184,960</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">658,745,740</td>
<td align="right">654,493,180</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">104,775,767</td>
<td align="right">104,166,866</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">2,411,877</td>
<td align="right">2,398,094</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,974,981,248</td>
<td align="right">2,958,230,869</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,197,776,901</td>
<td align="right">5,168,919,476</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">112,733,109</td>
<td align="right">112,143,809</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">862,838,587</td>
<td align="right">858,623,780</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">399,204,489</td>
<td align="right">401,018,556</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">98,494,454</td>
<td align="right">98,939,541</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,428,452,597</td>
<td align="right">2,418,201,738</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">873,243,038</td>
<td align="right">869,560,655</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">873,249,704</td>
<td align="right">869,567,561</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">222,912,555</td>
<td align="right">222,002,613</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,740,311</td>
<td align="right">9,701,408</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">153,351,504</td>
<td align="right">153,940,999</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">9,300,334</td>
<td align="right">9,265,694</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">9,303,854</td>
<td align="right">9,269,214</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">911,840,421</td>
<td align="right">914,957,619</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">62,384,209</td>
<td align="right">62,200,492</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">471,094,220</td>
<td align="right">472,476,600</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">122,848,592</td>
<td align="right">122,499,402</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,301,121</td>
<td align="right">3,309,583</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,485,145,007</td>
<td align="right">2,478,789,421</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,853,605,104</td>
<td align="right">1,849,072,621</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,426,185,451</td>
<td align="right">1,422,733,123</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,119,099,218</td>
<td align="right">1,121,761,385</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">125,066,263</td>
<td align="right">124,787,032</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">93,314,977</td>
<td align="right">93,114,451</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">93,315,617</td>
<td align="right">93,115,091</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">14,746,266</td>
<td align="right">14,774,632</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">27,362,619</td>
<td align="right">27,411,066</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">194,475,647</td>
<td align="right">194,133,717</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,459,065,622</td>
<td align="right">1,456,585,949</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">352,883,333</td>
<td align="right">352,308,010</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">21,575,844</td>
<td align="right">21,541,044</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,251,345,001</td>
<td align="right">1,253,361,375</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">828,654</td>
<td align="right">827,394</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">674,483,254</td>
<td align="right">673,554,475</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">440,475,042</td>
<td align="right">440,982,519</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">18,717,647</td>
<td align="right">18,697,246</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">57,427,952</td>
<td align="right">57,487,505</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">59,142,440</td>
<td align="right">59,203,580</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">65,655,120</td>
<td align="right">65,716,260</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">602,219,633</td>
<td align="right">602,778,241</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">9,556,166</td>
<td align="right">9,564,588</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">361,928,965</td>
<td align="right">362,209,547</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">966,262,196</td>
<td align="right">965,515,385</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">1,459,520</td>
<td align="right">1,458,410</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">57,575,920</td>
<td align="right">57,535,600</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">57,575,920</td>
<td align="right">57,535,600</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,144,358,291</td>
<td align="right">1,144,956,508</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">776,466,281</td>
<td align="right">776,864,704</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">258,864,956</td>
<td align="right">258,992,783</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,229,392,948</td>
<td align="right">1,228,804,115</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">170,269,520</td>
<td align="right">170,189,407</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">479,659,834</td>
<td align="right">479,870,836</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">242,934,785</td>
<td align="right">242,836,037</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">1,924,328,277</td>
<td align="right">1,923,550,657</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,927,875,102</td>
<td align="right">1,927,134,102</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,825,512,534</td>
<td align="right">1,824,818,043</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">408,321,883</td>
<td align="right">408,459,230</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">178,889,068</td>
<td align="right">178,830,081</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,830,482</td>
<td align="right">1,829,894</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,208,927,877</td>
<td align="right">1,209,246,710</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">311,786,927</td>
<td align="right">311,863,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,359,071,891</td>
<td align="right">3,359,888,262</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,385,017,585</td>
<td align="right">1,385,353,204</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">189,592,629</td>
<td align="right">189,633,572</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">3,105,464,107</td>
<td align="right">3,104,907,122</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">182,025,115</td>
<td align="right">182,002,675</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,665,296</td>
<td align="right">204,690,507</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">195,345,227</td>
<td align="right">195,364,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,447,418,181</td>
<td align="right">1,447,522,034</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">301,401,725</td>
<td align="right">301,419,011</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">393,776,440</td>
<td align="right">393,785,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,882,730</td>
<td align="right">35,882,346</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">20,587,977</td>
<td align="right">20,588,156</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">70,026,241</td>
<td align="right">70,026,802</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">96,035,404</td>
<td align="right">96,035,268</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">96,961,164</td>
<td align="right">96,961,028</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">184,996,300</td>
<td align="right">184,996,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,874,320</td>
<td align="right">149,874,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">139,786,440</td>
<td align="right">139,786,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">77,462,480</td>
<td align="right">77,462,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,537,420</td>
<td align="right">12,537,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">6,512,680</td>
<td align="right">6,512,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">3,993,400</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">3,434,265</td>
<td align="right">3,434,265</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,809,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">1,434,600</td>
<td align="right">1,434,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">1,260,560</td>
<td align="right">1,260,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">798,920</td>
<td align="right">798,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">540,960</td>
<td align="right">540,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">185,480</td>
<td align="right">185,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BEFORE_WITH</td>
<td align="right">113,196</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">8,781</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">6,000</td>
<td align="right">6,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_WITH_SPEC</td>
<td align="right">680</td>
<td align="right">680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">79,713,078,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SIDE_EXIT</td>
<td align="right"></td>
<td align="right">3,257,962,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">1,119,804,308</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_N</td>
<td align="right"></td>
<td align="right">489,792</td>
<td align="right"></td>
</tr>
</tbody>
</table>


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
<td align="right">3,277,596</td>
<td align="right">33,060</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">21,898</td>
<td align="right">663</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">86,088</td>
<td align="right">2,815</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,555</td>
<td align="right">583</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">13,212,263</td>
<td align="right">10,225,734</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">690</td>
<td align="right">630</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">14,812,641</td>
<td align="right">13,577,777</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">7,139</td>
<td align="right">7,018</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_WITH_DEFAULTS</td>
<td align="right">89,375</td>
<td align="right">90,623</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">13,731</td>
<td align="right">13,552</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,928,036</td>
<td align="right">1,929,890</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">74,221</td>
<td align="right">74,164</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">3,928,200</td>
<td align="right">3,928,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">84,645</td>
<td align="right">84,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right"></td>
<td align="right">3,670</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right"></td>
<td align="right">2,340</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right"></td>
<td align="right">467</td>
<td align="right"></td>
</tr>
</tbody>
</table>


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
<td align="right">261</td>
<td align="right">261</td>
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
<td align="right">441</td>
<td align="right">441</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,060</td>
<td align="right">1,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,060</td>
<td align="right">1,060</td>
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
<td align="right">2,020</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-03-19
