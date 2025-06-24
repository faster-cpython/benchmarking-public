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
<td align="left">UNARY_NOT</td>
<td align="right">17,997,316</td>
<td align="right">30,746,918</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,262,226</td>
<td align="right">438,570</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,232,482</td>
<td align="right">547,383</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">123,859,666</td>
<td align="right">76,115,824</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">13,984</td>
<td align="right">9,824</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">55,208,411</td>
<td align="right">39,080,674</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">84,065,100</td>
<td align="right">63,438,707</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,103,890</td>
<td align="right">2,379,301</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">50,022,666</td>
<td align="right">39,639,524</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">13,279,791</td>
<td align="right">10,593,884</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">96,022,708</td>
<td align="right">76,927,306</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">879,986,973</td>
<td align="right">749,528,165</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">190,310,614</td>
<td align="right">162,431,613</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">38,869,883</td>
<td align="right">33,193,856</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">439,033,454</td>
<td align="right">375,601,384</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">364,841,982</td>
<td align="right">314,311,208</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,600,864</td>
<td align="right">49,923,819</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">87,341,176</td>
<td align="right">75,964,914</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">210,095,352</td>
<td align="right">183,242,614</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,286,382</td>
<td align="right">115,080,477</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,551</td>
<td align="right">60,977</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,892,278</td>
<td align="right">163,081,952</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">113,116,738</td>
<td align="right">100,439,374</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">195,664,125</td>
<td align="right">174,980,629</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">104,984,330</td>
<td align="right">94,061,134</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">925,868,515</td>
<td align="right">838,267,210</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">346,418,972</td>
<td align="right">314,248,071</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">93,465,715</td>
<td align="right">84,794,945</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,347,866</td>
<td align="right">4,861,414</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">179,417,513</td>
<td align="right">163,331,565</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,011,637,398</td>
<td align="right">1,841,427,110</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">432,062,761</td>
<td align="right">396,031,577</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">27,125,636</td>
<td align="right">24,910,141</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">151,243,127</td>
<td align="right">139,279,295</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">169,641,196</td>
<td align="right">156,608,723</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">123,779,647</td>
<td align="right">114,382,818</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">608,762,474</td>
<td align="right">562,554,972</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">200,201,994</td>
<td align="right">185,110,402</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">42,000,596</td>
<td align="right">38,916,530</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">215,754,521</td>
<td align="right">200,124,924</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">159,564,106</td>
<td align="right">148,308,832</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">885,511,403</td>
<td align="right">823,374,526</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">46,710,047</td>
<td align="right">43,518,947</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,588,662</td>
<td align="right">17,340,055</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">56,998</td>
<td align="right">53,189</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">366,624,045</td>
<td align="right">343,099,206</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">865,361,500</td>
<td align="right">809,847,382</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,347,468,460</td>
<td align="right">15,311,648,919</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,805,507</td>
<td align="right">33,564,823</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,046,300,755</td>
<td align="right">982,767,895</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,079,176,870</td>
<td align="right">1,015,826,035</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">76,372,556</td>
<td align="right">71,931,713</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">363,005,571</td>
<td align="right">342,265,506</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">929,821,700</td>
<td align="right">879,068,622</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,970,771,151</td>
<td align="right">4,700,768,773</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">171,187,250</td>
<td align="right">162,202,151</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">135,827,717</td>
<td align="right">128,780,000</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">164,133,980</td>
<td align="right">155,684,482</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">459,904,690</td>
<td align="right">436,917,708</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">369,501,209</td>
<td align="right">351,186,189</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">34,636,709</td>
<td align="right">32,929,721</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">205,116,489</td>
<td align="right">195,189,557</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">265,872,067</td>
<td align="right">253,160,199</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">145,970,793</td>
<td align="right">139,068,017</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">103,589,945</td>
<td align="right">98,742,869</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">682,753,781</td>
<td align="right">651,949,382</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">657,313,922</td>
<td align="right">627,825,351</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">341,264,160</td>
<td align="right">325,968,880</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">900,556,220</td>
<td align="right">860,506,743</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">864,396,862</td>
<td align="right">826,008,236</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,198,256,039</td>
<td align="right">3,056,253,257</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,429,609,113</td>
<td align="right">1,369,036,589</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">116,054,283</td>
<td align="right">111,185,683</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,130,182,952</td>
<td align="right">3,957,808,519</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,997,811,704</td>
<td align="right">1,922,016,025</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">129,350,980</td>
<td align="right">124,636,102</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">165,801,240</td>
<td align="right">159,808,604</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">51,499,939</td>
<td align="right">49,647,346</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,951,487,783</td>
<td align="right">1,881,622,713</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">44,022,230</td>
<td align="right">42,519,049</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">67,329,713</td>
<td align="right">65,096,978</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">538,367,526</td>
<td align="right">520,546,757</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,721,274,525</td>
<td align="right">3,601,971,340</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">384,706,593</td>
<td align="right">372,434,257</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">871,360,649</td>
<td align="right">843,578,075</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">121,970,953</td>
<td align="right">118,376,510</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">108,264,076</td>
<td align="right">105,264,610</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">73,078,597</td>
<td align="right">71,065,478</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,603,016</td>
<td align="right">9,340,374</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,984,130,519</td>
<td align="right">3,875,859,237</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">468,453,321</td>
<td align="right">455,865,863</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,344,664</td>
<td align="right">2,285,597</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">276,134,008</td>
<td align="right">269,456,255</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">546,115,277</td>
<td align="right">532,964,099</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">239,798,710</td>
<td align="right">234,030,872</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">494,509,652</td>
<td align="right">483,088,099</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">609,799,881</td>
<td align="right">596,340,981</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">438,152,202</td>
<td align="right">429,374,565</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">273,243,804</td>
<td align="right">267,886,826</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">246,504,242</td>
<td align="right">241,734,422</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,121,746</td>
<td align="right">3,061,681</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">810,301,635</td>
<td align="right">794,758,015</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,496,246,296</td>
<td align="right">2,449,202,732</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">68,105,123</td>
<td align="right">66,835,683</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">228,496,780</td>
<td align="right">224,266,115</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,677,393,369</td>
<td align="right">4,590,842,885</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">244,654,176</td>
<td align="right">240,230,895</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">441,880,088</td>
<td align="right">449,518,220</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,112,341,446</td>
<td align="right">1,093,268,649</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,986,459,897</td>
<td align="right">4,901,614,804</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">441,306</td>
<td align="right">433,825</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">63,645,738</td>
<td align="right">62,593,248</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">81,344,062</td>
<td align="right">80,072,417</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">55,798,516</td>
<td align="right">54,928,433</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">114,765,144</td>
<td align="right">112,982,655</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">824,772,028</td>
<td align="right">812,461,230</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">290,015,569</td>
<td align="right">285,870,378</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,343,786</td>
<td align="right">40,764,342</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,617,768,136</td>
<td align="right">2,582,401,957</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">69,150,935</td>
<td align="right">68,218,648</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">118,564,651</td>
<td align="right">117,019,802</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">288,386,592</td>
<td align="right">284,663,851</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">70,018,844</td>
<td align="right">69,118,355</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">646,668,285</td>
<td align="right">638,954,676</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">282,845,418</td>
<td align="right">279,857,379</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">119,492,211</td>
<td align="right">118,247,764</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">64,893,847</td>
<td align="right">64,250,788</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,844,673</td>
<td align="right">61,292,796</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">139,602,773</td>
<td align="right">138,403,313</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,721,898</td>
<td align="right">25,504,335</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">75,309,712</td>
<td align="right">74,783,724</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,367,154</td>
<td align="right">4,338,538</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,219,975,175</td>
<td align="right">2,207,183,400</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">367,096,316</td>
<td align="right">365,279,076</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,187,412</td>
<td align="right">9,146,023</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">255,326,127</td>
<td align="right">256,442,092</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">169,224,480</td>
<td align="right">169,926,998</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">30,824,491</td>
<td align="right">30,698,692</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,712,749</td>
<td align="right">70,481,033</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,367</td>
<td align="right">5,356</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,584,889,224</td>
<td align="right">1,582,591,258</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,645</td>
<td align="right">9,729,256</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,314,144</td>
<td align="right">190,079,389</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,509,609</td>
<td align="right">242,219,816</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,997,571</td>
<td align="right">9,985,650</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,559,772</td>
<td align="right">244,269,957</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,474,799</td>
<td align="right">20,452,205</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,801,568</td>
<td align="right">20,778,974</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,801,547</td>
<td align="right">20,778,955</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">332,103,107</td>
<td align="right">332,436,142</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,515</td>
<td align="right">2,513</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,714</td>
<td align="right">33,689</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,945,581</td>
<td align="right">27,927,896</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">245,633</td>
<td align="right">245,548</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,930</td>
<td align="right">12,934</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,108,157,438</td>
<td align="right">1,108,328,363</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,089</td>
<td align="right">35,544,150</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,604,972</td>
<td align="right">114,598,745</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,453,678</td>
<td align="right">418,439,171</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">10,549,274</td>
<td align="right">10,548,942</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,619,522</td>
<td align="right">591,602,901</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">214,351</td>
<td align="right">214,357</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,096,859</td>
<td align="right">156,092,612</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,704,710</td>
<td align="right">12,704,992</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,288,294</td>
<td align="right">5,288,368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,154</td>
<td align="right">302,244,074</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,758,319</td>
<td align="right">14,758,229</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,090,882</td>
<td align="right">3,090,895</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,165,323</td>
<td align="right">6,165,339</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,749</td>
<td align="right">128,851,749</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,443</td>
<td align="right">41,964,443</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right">29,134,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">29,134,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,796</td>
<td align="right">8,976,796</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,784,349</td>
<td align="right">3,784,349</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,140</td>
<td align="right">2,597,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,749,760</td>
<td align="right">1,749,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">117,444</td>
<td align="right">117,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,577</td>
<td align="right">98,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,564</td>
<td align="right">72,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,970</td>
<td align="right">53,970</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,864</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,550</td>
<td align="right">3,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,072</td>
<td align="right">1,072</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">176</td>
<td align="right">176</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">25</td>
<td align="right">25</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">55,499,051</td>
<td align="right">0.3%</td>
<td align="right">58,983,765</td>
<td align="right">0.3%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,078,696,165</td>
<td align="right">6.2%</td>
<td align="right">1,015,378,895</td>
<td align="right">5.9%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,239,723,898</td>
<td align="right">93.5%</td>
<td align="right">16,216,980,598</td>
<td align="right">93.8%</td>
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
<td align="right">463,289</td>
<td align="right">30.3%</td>
<td align="right">429,843</td>
<td align="right">27.6%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,064,334</td>
<td align="right">69.7%</td>
<td align="right">1,129,978</td>
<td align="right">72.4%</td>
<td align="right">6.2%</td>
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
<td align="left">and int</td>
<td align="right">18,479</td>
<td align="right">4.0%</td>
<td align="right">7,475</td>
<td align="right">1.7%</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">1,812</td>
<td align="right">0.4%</td>
<td align="right">1,012</td>
<td align="right">0.2%</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,305</td>
<td align="right">1.8%</td>
<td align="right">4,867</td>
<td align="right">1.1%</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">16,343</td>
<td align="right">3.5%</td>
<td align="right">12,703</td>
<td align="right">3.0%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21,781</td>
<td align="right">4.7%</td>
<td align="right">17,079</td>
<td align="right">4.0%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">11,555</td>
<td align="right">2.5%</td>
<td align="right">10,104</td>
<td align="right">2.4%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">36,076</td>
<td align="right">7.8%</td>
<td align="right">32,216</td>
<td align="right">7.5%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,009</td>
<td align="right">1.5%</td>
<td align="right">6,443</td>
<td align="right">1.5%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">793</td>
<td align="right">0.2%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">22,374</td>
<td align="right">4.8%</td>
<td align="right">21,294</td>
<td align="right">5.0%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,336</td>
<td align="right">0.5%</td>
<td align="right">2,236</td>
<td align="right">0.5%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">41,352</td>
<td align="right">8.9%</td>
<td align="right">39,594</td>
<td align="right">9.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,695</td>
<td align="right">1.4%</td>
<td align="right">6,452</td>
<td align="right">1.5%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,194</td>
<td align="right">1.3%</td>
<td align="right">6,394</td>
<td align="right">1.5%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,768</td>
<td align="right">0.6%</td>
<td align="right">2,721</td>
<td align="right">0.6%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">63,015</td>
<td align="right">13.6%</td>
<td align="right">62,407</td>
<td align="right">14.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">330</td>
<td align="right">0.1%</td>
<td align="right">333</td>
<td align="right">0.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,994</td>
<td align="right">0.4%</td>
<td align="right">1,976</td>
<td align="right">0.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,858</td>
<td align="right">4.3%</td>
<td align="right">19,686</td>
<td align="right">4.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">169</td>
<td align="right">0.0%</td>
<td align="right">168</td>
<td align="right">0.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">28,692</td>
<td align="right">6.2%</td>
<td align="right">28,603</td>
<td align="right">6.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,350</td>
<td align="right">0.5%</td>
<td align="right">2,343</td>
<td align="right">0.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">348</td>
<td align="right">0.1%</td>
<td align="right">347</td>
<td align="right">0.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">25,838</td>
<td align="right">5.6%</td>
<td align="right">25,908</td>
<td align="right">6.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">107,942</td>
<td align="right">23.3%</td>
<td align="right">107,851</td>
<td align="right">25.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,165</td>
<td align="right">0.7%</td>
<td align="right">3,165</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,110</td>
<td align="right">0.7%</td>
<td align="right">3,110</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">630</td>
<td align="right">0.1%</td>
<td align="right">630</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr structtime</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">184,892,278</td>
<td align="right">100.0%</td>
<td align="right">163,081,952</td>
<td align="right">100.0%</td>
<td align="right">-11.8%</td>
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
<td align="right">153,992,059</td>
<td align="right">1.4%</td>
<td align="right">151,621,230</td>
<td align="right">1.3%</td>
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
<td align="right">151,160,858</td>
<td align="right">1.3%</td>
<td align="right">148,834,691</td>
<td align="right">1.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,096,370,718</td>
<td align="right">98.6%</td>
<td align="right">11,079,647,313</td>
<td align="right">98.6%</td>
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
<td align="right">3,076,688</td>
<td align="right">100.0%</td>
<td align="right">3,031,941</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">146</td>
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
<td align="left">init not simple</td>
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">146</td>
<td align="right">100.0%</td>
<td align="right">146</td>
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
<td align="right">574,330</td>
<td align="right">96.6%</td>
<td align="right">574,328</td>
<td align="right">96.6%</td>
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
<td align="right">581,624</td>
<td align="right">97.8%</td>
<td align="right">581,624</td>
<td align="right">97.8%</td>
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
<td align="right">20,224</td>
<td align="right">100.0%</td>
<td align="right">20,230</td>
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
<td align="right">93,342,129</td>
<td align="right">2.0%</td>
<td align="right">84,673,964</td>
<td align="right">1.8%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,273,848</td>
<td align="right">0.0%</td>
<td align="right">1,252,727</td>
<td align="right">0.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,505,144,273</td>
<td align="right">97.9%</td>
<td align="right">4,496,104,037</td>
<td align="right">98.1%</td>
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
<td align="left">Failure</td>
<td align="right">105,689</td>
<td align="right">71.7%</td>
<td align="right">103,091</td>
<td align="right">71.4%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,622</td>
<td align="right">28.3%</td>
<td align="right">41,217</td>
<td align="right">28.6%</td>
<td align="right">-1.0%</td>
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
<td align="right">5,870</td>
<td align="right">5.6%</td>
<td align="right">5,005</td>
<td align="right">4.9%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,882</td>
<td align="right">1.8%</td>
<td align="right">1,633</td>
<td align="right">1.6%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,649</td>
<td align="right">8.2%</td>
<td align="right">7,781</td>
<td align="right">7.5%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">370</td>
<td align="right">0.4%</td>
<td align="right">352</td>
<td align="right">0.3%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,712</td>
<td align="right">7.3%</td>
<td align="right">7,458</td>
<td align="right">7.2%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,152</td>
<td align="right">3.9%</td>
<td align="right">4,048</td>
<td align="right">3.9%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,324</td>
<td align="right">1.3%</td>
<td align="right">1,303</td>
<td align="right">1.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">7.2%</td>
<td align="right">7,559</td>
<td align="right">7.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">43,704</td>
<td align="right">41.4%</td>
<td align="right">43,435</td>
<td align="right">42.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,184</td>
<td align="right">21.9%</td>
<td align="right">23,323</td>
<td align="right">22.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">998</td>
<td align="right">0.9%</td>
<td align="right">998</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">196</td>
<td align="right">0.2%</td>
<td align="right">196</td>
<td align="right">0.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,389,959</td>
<td align="right">0.1%</td>
<td align="right">1,059,239</td>
<td align="right">0.0%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">87,297,005</td>
<td align="right">3.8%</td>
<td align="right">75,923,406</td>
<td align="right">3.4%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,186,452,030</td>
<td align="right">96.1%</td>
<td align="right">2,182,796,568</td>
<td align="right">96.6%</td>
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
<td align="right">28,333</td>
<td align="right">40.2%</td>
<td align="right">22,093</td>
<td align="right">35.9%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">42,061</td>
<td align="right">59.8%</td>
<td align="right">39,398</td>
<td align="right">64.1%</td>
<td align="right">-6.3%</td>
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
<td align="right">10,196</td>
<td align="right">24.2%</td>
<td align="right">9,206</td>
<td align="right">23.4%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,270</td>
<td align="right">22.0%</td>
<td align="right">8,411</td>
<td align="right">21.3%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">12,055</td>
<td align="right">28.7%</td>
<td align="right">11,457</td>
<td align="right">29.1%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,540</td>
<td align="right">25.1%</td>
<td align="right">10,324</td>
<td align="right">26.2%</td>
<td align="right">-2.0%</td>
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
<td align="right">209,978,165</td>
<td align="right">13.4%</td>
<td align="right">183,137,056</td>
<td align="right">12.2%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,293,323,604</td>
<td align="right">82.6%</td>
<td align="right">1,255,287,537</td>
<td align="right">83.7%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">61,945,014</td>
<td align="right">4.0%</td>
<td align="right">61,227,136</td>
<td align="right">4.1%</td>
<td align="right">-1.2%</td>
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
<td align="right">111,786</td>
<td align="right">8.7%</td>
<td align="right">100,162</td>
<td align="right">7.9%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,174,004</td>
<td align="right">91.3%</td>
<td align="right">1,160,471</td>
<td align="right">92.1%</td>
<td align="right">-1.2%</td>
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
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">147</td>
<td align="right">0.1%</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">5,891</td>
<td align="right">5.3%</td>
<td align="right">2,939</td>
<td align="right">2.9%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,889</td>
<td align="right">11.5%</td>
<td align="right">9,132</td>
<td align="right">9.1%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,398</td>
<td align="right">1.3%</td>
<td align="right">1,020</td>
<td align="right">1.0%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">6,417</td>
<td align="right">5.7%</td>
<td align="right">5,384</td>
<td align="right">5.4%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,180</td>
<td align="right">3.7%</td>
<td align="right">3,713</td>
<td align="right">3.7%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">0.2%</td>
<td align="right">211</td>
<td align="right">0.2%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">260</td>
<td align="right">0.2%</td>
<td align="right">237</td>
<td align="right">0.2%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">10,948</td>
<td align="right">9.8%</td>
<td align="right">10,511</td>
<td align="right">10.5%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">50,511</td>
<td align="right">45.2%</td>
<td align="right">48,495</td>
<td align="right">48.4%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,027</td>
<td align="right">3.6%</td>
<td align="right">3,910</td>
<td align="right">3.9%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">5,657</td>
<td align="right">5.1%</td>
<td align="right">5,531</td>
<td align="right">5.5%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,490</td>
<td align="right">3.1%</td>
<td align="right">3,439</td>
<td align="right">3.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">2,042</td>
<td align="right">1.8%</td>
<td align="right">2,020</td>
<td align="right">2.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,497</td>
<td align="right">3.1%</td>
<td align="right">3,473</td>
<td align="right">3.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">string</td>
<td align="right">2,806,694</td>
<td align="right">2,806,694 / 0 !!</td>
<td align="right">2,297,094</td>
<td align="right">2,297,094 / 0 !!</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,925,771</td>
<td align="right">34,925,771 / 0 !!</td>
<td align="right">34,728,171</td>
<td align="right">34,728,171 / 0 !!</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">116,959,246</td>
<td align="right">116,959,246 / 0 !!</td>
<td align="right">116,377,202</td>
<td align="right">116,377,202 / 0 !!</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,120,761</td>
<td align="right">12,120,761 / 0 !!</td>
<td align="right">12,093,462</td>
<td align="right">12,093,462 / 0 !!</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,499,218</td>
<td align="right">5,499,218 / 0 !!</td>
<td align="right">5,495,085</td>
<td align="right">5,495,085 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">302,244,490</td>
<td align="right">302,244,490 / 0 !!</td>
<td align="right">302,045,593</td>
<td align="right">302,045,593 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,812,906</td>
<td align="right">101,812,906 / 0 !!</td>
<td align="right">101,806,692</td>
<td align="right">101,806,692 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">171,443,532</td>
<td align="right">171,443,532 / 0 !!</td>
<td align="right">171,437,669</td>
<td align="right">171,437,669 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,943,222</td>
<td align="right">341,943,222 / 0 !!</td>
<td align="right">341,938,609</td>
<td align="right">341,938,609 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,262,383</td>
<td align="right">0.0%</td>
<td align="right">988,991</td>
<td align="right">0.0%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">536,678,923</td>
<td align="right">4.7%</td>
<td align="right">518,893,007</td>
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
<td align="right">10,217,654,427</td>
<td align="right">89.9%</td>
<td align="right">10,033,468,990</td>
<td align="right">89.9%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">612,138,439</td>
<td align="right">5.4%</td>
<td align="right">605,001,160</td>
<td align="right">5.4%</td>
<td align="right">-1.2%</td>
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
<td align="right">11,630,913</td>
<td align="right">96.4%</td>
<td align="right">11,495,986</td>
<td align="right">96.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">435,576</td>
<td align="right">3.6%</td>
<td align="right">431,614</td>
<td align="right">3.6%</td>
<td align="right">-0.9%</td>
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
<td align="right">40,022</td>
<td align="right">9.2%</td>
<td align="right">37,754</td>
<td align="right">8.7%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">743</td>
<td align="right">0.2%</td>
<td align="right">779</td>
<td align="right">0.2%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">573</td>
<td align="right">0.1%</td>
<td align="right">592</td>
<td align="right">0.1%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">36,242</td>
<td align="right">8.3%</td>
<td align="right">35,565</td>
<td align="right">8.2%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,379</td>
<td align="right">0.5%</td>
<td align="right">2,414</td>
<td align="right">0.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">6,969</td>
<td align="right">1.6%</td>
<td align="right">7,053</td>
<td align="right">1.6%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23,399</td>
<td align="right">5.4%</td>
<td align="right">23,676</td>
<td align="right">5.5%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,062</td>
<td align="right">0.9%</td>
<td align="right">4,014</td>
<td align="right">0.9%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">47,965</td>
<td align="right">11.0%</td>
<td align="right">47,458</td>
<td align="right">11.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,408</td>
<td align="right">3.5%</td>
<td align="right">15,360</td>
<td align="right">3.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,841</td>
<td align="right">0.4%</td>
<td align="right">1,843</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">1.0%</td>
<td align="right">4,448</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,720</td>
<td align="right">0.4%</td>
<td align="right">1,720</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">545</td>
<td align="right">0.1%</td>
<td align="right">545</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">46</td>
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
<td align="right">4,603,907,688</td>
<td align="right">99.7%</td>
<td align="right">4,504,240,350</td>
<td align="right">99.7%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">51,816</td>
<td align="right">0.0%</td>
<td align="right">51,807</td>
<td align="right">0.0%</td>
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
<td align="right">14,622,516</td>
<td align="right">0.3%</td>
<td align="right">14,622,453</td>
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
<td align="right">1,376</td>
<td align="right">0.0%</td>
<td align="right">1,376</td>
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
<td align="right">136,554</td>
<td align="right">100.0%</td>
<td align="right">136,527</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">205</td>
<td align="right">0.0%</td>
<td align="right">203</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,155,598</td>
<td align="right">100.0%</td>
<td align="right">64,155,588</td>
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
<td align="right">2,310</td>
<td align="right">100.0%</td>
<td align="right">2,310</td>
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
<td align="right">591,604,811</td>
<td align="right">82.1%</td>
<td align="right">591,588,190</td>
<td align="right">82.1%</td>
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
<td align="right">128,816,951</td>
<td align="right">17.9%</td>
<td align="right">128,816,951</td>
<td align="right">17.9%</td>
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
<td align="right">0.0%</td>
<td align="right">14,711</td>
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
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
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
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right">752</td>
<td align="right">2.2%</td>
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
<td align="right">108,010,458</td>
<td align="right">5.4%</td>
<td align="right">94,818,460</td>
<td align="right">4.8%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">61,761,122</td>
<td align="right">3.1%</td>
<td align="right">61,209,283</td>
<td align="right">3.1%</td>
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
<td align="right">1,817,144,974</td>
<td align="right">91.5%</td>
<td align="right">1,808,917,393</td>
<td align="right">92.1%</td>
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
<td align="right">2,076,738</td>
<td align="right">97.9%</td>
<td align="right">1,828,075</td>
<td align="right">97.7%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43,826</td>
<td align="right">2.1%</td>
<td align="right">43,788</td>
<td align="right">2.3%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">4,715</td>
<td align="right">10.8%</td>
<td align="right">4,683</td>
<td align="right">10.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,741</td>
<td align="right">8.5%</td>
<td align="right">3,719</td>
<td align="right">8.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">240,691</td>
<td align="right">549.2%</td>
<td align="right">239,883</td>
<td align="right">547.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,338</td>
<td align="right">7.6%</td>
<td align="right">3,346</td>
<td align="right">7.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">19,647</td>
<td align="right">44.8%</td>
<td align="right">19,647</td>
<td align="right">44.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,227</td>
<td align="right">16.5%</td>
<td align="right">7,227</td>
<td align="right">16.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,321</td>
<td align="right">3.0%</td>
<td align="right">1,321</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">747</td>
<td align="right">1.7%</td>
<td align="right">747</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">1.0%</td>
<td align="right">423</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">363</td>
<td align="right">0.8%</td>
<td align="right">363</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.3%</td>
<td align="right">111</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">91</td>
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
<td align="right">1,232,482</td>
<td align="right">100.0%</td>
<td align="right">547,383</td>
<td align="right">100.0%</td>
<td align="right">-55.6%</td>
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
<td align="right">103,551,753</td>
<td align="right">10.1%</td>
<td align="right">98,705,332</td>
<td align="right">9.7%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">917,911,353</td>
<td align="right">89.9%</td>
<td align="right">917,796,070</td>
<td align="right">90.3%</td>
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
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">2,220</td>
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
<td align="right">36,146</td>
<td align="right">94.5%</td>
<td align="right">35,493</td>
<td align="right">94.5%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,086</td>
<td align="right">5.5%</td>
<td align="right">2,084</td>
<td align="right">5.5%</td>
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
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">26</td>
<td align="right">0.1%</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">273</td>
<td align="right">0.8%</td>
<td align="right">184</td>
<td align="right">0.5%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">162</td>
<td align="right">0.4%</td>
<td align="right">211</td>
<td align="right">0.6%</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">3,323</td>
<td align="right">9.2%</td>
<td align="right">2,837</td>
<td align="right">8.0%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,991</td>
<td align="right">8.3%</td>
<td align="right">2,951</td>
<td align="right">8.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,164</td>
<td align="right">47.5%</td>
<td align="right">17,124</td>
<td align="right">48.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">10,484</td>
<td align="right">29.0%</td>
<td align="right">10,479</td>
<td align="right">29.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">4.7%</td>
<td align="right">1,681</td>
<td align="right">4.7%</td>
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
<td align="right">63,758,193</td>
<td align="right">1.5%</td>
<td align="right">57,668,543</td>
<td align="right">1.3%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">135,284,222</td>
<td align="right">3.1%</td>
<td align="right">128,284,341</td>
<td align="right">3.0%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,154,733,821</td>
<td align="right">95.4%</td>
<td align="right">4,103,859,418</td>
<td align="right">95.7%</td>
<td align="right">-1.2%</td>
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
<td align="right">492,924</td>
<td align="right">28.3%</td>
<td align="right">445,080</td>
<td align="right">28.1%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,251,881</td>
<td align="right">71.7%</td>
<td align="right">1,137,079</td>
<td align="right">71.9%</td>
<td align="right">-9.2%</td>
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
<td align="right">51,862</td>
<td align="right">10.5%</td>
<td align="right">4,974</td>
<td align="right">1.1%</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">182</td>
<td align="right">0.0%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,656</td>
<td align="right">0.9%</td>
<td align="right">4,096</td>
<td align="right">0.9%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">10,847</td>
<td align="right">2.2%</td>
<td align="right">10,768</td>
<td align="right">2.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,383</td>
<td align="right">1.9%</td>
<td align="right">9,346</td>
<td align="right">2.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">74,381</td>
<td align="right">15.1%</td>
<td align="right">74,231</td>
<td align="right">16.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">72,043</td>
<td align="right">14.6%</td>
<td align="right">72,147</td>
<td align="right">16.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,061</td>
<td align="right">2.0%</td>
<td align="right">10,050</td>
<td align="right">2.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,849</td>
<td align="right">52.3%</td>
<td align="right">257,826</td>
<td align="right">57.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">1,251,584</td>
<td align="right">0.1%</td>
<td align="right">427,997</td>
<td align="right">0.0%</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,231,267,794</td>
<td align="right">99.9%</td>
<td align="right">1,229,444,825</td>
<td align="right">100.0%</td>
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
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">3,700</td>
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
<td align="right">781</td>
<td align="right">7.3%</td>
<td align="right">724</td>
<td align="right">6.8%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,941</td>
<td align="right">92.7%</td>
<td align="right">9,929</td>
<td align="right">93.2%</td>
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
<td align="left">sequence</td>
<td align="right">547</td>
<td align="right">70.0%</td>
<td align="right">490</td>
<td align="right">67.7%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">17.4%</td>
<td align="right">136</td>
<td align="right">18.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">12.5%</td>
<td align="right">98</td>
<td align="right">13.5%</td>
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
<td align="right">3,187,082,383</td>
<td align="right">3.2%</td>
<td align="right">3,010,093,907</td>
<td align="right">3.2%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">58,843,662,630</td>
<td align="right">59.7%</td>
<td align="right">56,343,251,274</td>
<td align="right">59.7%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">35,497,255,928</td>
<td align="right">36.0%</td>
<td align="right">34,028,066,890</td>
<td align="right">36.0%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,058,822,258</td>
<td align="right">1.1%</td>
<td align="right">1,032,449,605</td>
<td align="right">1.1%</td>
<td align="right">-2.5%</td>
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
<td align="right">87,297,005</td>
<td align="right">3.1%</td>
<td align="right">75,923,406</td>
<td align="right">2.9%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">209,978,165</td>
<td align="right">7.5%</td>
<td align="right">183,137,056</td>
<td align="right">7.0%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,892,278</td>
<td align="right">6.6%</td>
<td align="right">163,081,952</td>
<td align="right">6.2%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">93,342,129</td>
<td align="right">3.3%</td>
<td align="right">84,673,964</td>
<td align="right">3.2%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,078,696,165</td>
<td align="right">38.7%</td>
<td align="right">1,015,378,895</td>
<td align="right">38.7%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">135,284,222</td>
<td align="right">4.9%</td>
<td align="right">128,284,341</td>
<td align="right">4.9%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">103,551,753</td>
<td align="right">3.7%</td>
<td align="right">98,705,332</td>
<td align="right">3.8%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">536,678,923</td>
<td align="right">19.2%</td>
<td align="right">518,893,007</td>
<td align="right">19.8%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">151,160,858</td>
<td align="right">5.4%</td>
<td align="right">148,834,691</td>
<td align="right">5.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,951</td>
<td align="right">4.6%</td>
<td align="right">128,816,951</td>
<td align="right">4.9%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">89,009,246</td>
<td align="right">8.4%</td>
<td align="right">78,600,882</td>
<td align="right">7.6%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">30,526,491</td>
<td align="right">2.9%</td>
<td align="right">27,214,693</td>
<td align="right">2.6%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">176,919,591</td>
<td align="right">16.7%</td>
<td align="right">166,916,160</td>
<td align="right">16.2%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">55,253,213</td>
<td align="right">5.2%</td>
<td align="right">57,891,768</td>
<td align="right">5.6%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">219,513,587</td>
<td align="right">20.7%</td>
<td align="right">228,868,784</td>
<td align="right">22.2%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">82,330,964</td>
<td align="right">7.8%</td>
<td align="right">79,913,629</td>
<td align="right">7.7%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">78,787,590</td>
<td align="right">7.4%</td>
<td align="right">77,038,885</td>
<td align="right">7.5%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">30,935,091</td>
<td align="right">2.9%</td>
<td align="right">30,583,517</td>
<td align="right">3.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,932,528</td>
<td align="right">2.9%</td>
<td align="right">30,612,864</td>
<td align="right">3.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">26,626,650</td>
<td align="right">2.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">24,860,184</td>
<td align="right">2.4%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">274,400,851</td>
<td align="right">4.1%</td>
<td align="right">272,955,427</td>
<td align="right">4.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,401,308,587</td>
<td align="right">81.0%</td>
<td align="right">5,382,875,465</td>
<td align="right">81.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,077,091,884</td>
<td align="right">76.2%</td>
<td align="right">5,061,315,572</td>
<td align="right">76.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,001,119,676</td>
<td align="right">15.0%</td>
<td align="right">999,069,073</td>
<td align="right">15.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,005,396,997</td>
<td align="right">15.1%</td>
<td align="right">1,003,346,394</td>
<td align="right">15.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,589,376,846</td>
<td align="right">23.8%</td>
<td align="right">1,587,078,873</td>
<td align="right">23.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,589,376,846</td>
<td align="right">23.8%</td>
<td align="right">1,587,078,873</td>
<td align="right">23.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,055,793</td>
<td align="right">3.9%</td>
<td align="right">258,827,155</td>
<td align="right">3.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">583,979,849</td>
<td align="right">8.8%</td>
<td align="right">583,732,479</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,668,085</td>
<td align="right">1.1%</td>
<td align="right">70,645,446</td>
<td align="right">1.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,557,556</td>
<td align="right">0.4%</td>
<td align="right">23,551,389</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,457</td>
<td align="right">0.1%</td>
<td align="right">4,273,457</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,898</td>
<td align="right">2.0%</td>
<td align="right">132,513,898</td>
<td align="right">2.0%</td>
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
<td align="right">5,135,471</td>
<td align="right"></td>
<td align="right">4,745,369</td>
<td align="right"></td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,207,094,314</td>
<td align="right">1.1%</td>
<td align="right">1,148,557,265</td>
<td align="right">1.0%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,992,723,707</td>
<td align="right">3.2%</td>
<td align="right">2,849,054,189</td>
<td align="right">3.1%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">58,885,342</td>
<td align="right"></td>
<td align="right">56,998,316</td>
<td align="right"></td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">54,554,420</td>
<td align="right"></td>
<td align="right">53,055,780</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">24,833,305,702</td>
<td align="right">26.8%</td>
<td align="right">24,207,855,514</td>
<td align="right">26.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">33,257,541,981</td>
<td align="right">30.3%</td>
<td align="right">32,662,666,347</td>
<td align="right">29.8%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">40,353,297,832</td>
<td align="right">43.6%</td>
<td align="right">40,905,648,354</td>
<td align="right">44.3%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">49,774,968,923</td>
<td align="right">45.4%</td>
<td align="right">50,278,619,362</td>
<td align="right">45.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,189,335,037</td>
<td align="right"></td>
<td align="right">2,208,796,927</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,323,830,210</td>
<td align="right">26.3%</td>
<td align="right">24,394,099,750</td>
<td align="right">26.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,551,846</td>
<td align="right"></td>
<td align="right">174,201,661</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,420,417,080</td>
<td align="right"></td>
<td align="right">2,415,980,299</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,468,227,786</td>
<td align="right">28.6%</td>
<td align="right">5,460,335,621</td>
<td align="right">28.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,545,852,711</td>
<td align="right">29.0%</td>
<td align="right">5,538,006,351</td>
<td align="right">29.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,143,044,311</td>
<td align="right"></td>
<td align="right">6,134,874,222</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,368,883</td>
<td align="right">0.0%</td>
<td align="right">6,377,337</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,548,251,171</td>
<td align="right"></td>
<td align="right">13,536,604,761</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,548,148,546</td>
<td align="right">71.0%</td>
<td align="right">13,536,512,745</td>
<td align="right">71.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,256,042</td>
<td align="right">0.4%</td>
<td align="right">71,293,393</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">25,370,587,456</td>
<td align="right">23.1%</td>
<td align="right">25,367,301,981</td>
<td align="right">23.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,404,481</td>
<td align="right">2.0%</td>
<td align="right">3,404,481</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">306,771</td>
<td align="right">0.2%</td>
<td align="right">306,771</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">364,775</td>
<td align="right">102,178,750</td>
<td align="right">9,525,618,702</td>
<td align="right">756,406,771</td>
<td align="right">764,593,420</td>
<td align="right">364,420</td>
<td align="right">101,428,498</td>
<td align="right">9,515,694,420</td>
<td align="right">754,448,248</td>
<td align="right">765,513,768</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,681,293,444</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,681,466,820</td>
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">82</td>
<td align="right">0.0%</td>
<td align="right">625</td>
<td align="right">0.1%</td>
<td align="right">662.2%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">221</td>
<td align="right">0.8%</td>
<td align="right">1,346</td>
<td align="right">1.3%</td>
<td align="right">509.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">182</td>
<td align="right">0.0%</td>
<td align="right">791</td>
<td align="right">0.1%</td>
<td align="right">334.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">671</td>
<td align="right">0.2%</td>
<td align="right">2,762</td>
<td align="right">0.4%</td>
<td align="right">311.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">27,839</td>
<td align="right">6.3%</td>
<td align="right">102,742</td>
<td align="right">16.2%</td>
<td align="right">269.1%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">866</td>
<td align="right">0.2%</td>
<td align="right">2,536</td>
<td align="right">0.4%</td>
<td align="right">192.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,754</td>
<td align="right">0.4%</td>
<td align="right">2,847</td>
<td align="right">0.4%</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">443,624</td>
<td align="right"></td>
<td align="right">635,489</td>
<td align="right"></td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">136,316</td>
<td align="right">30.7%</td>
<td align="right">177,488</td>
<td align="right">27.9%</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">231,920</td>
<td align="right">52.3%</td>
<td align="right">295,094</td>
<td align="right">46.4%</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">47,367</td>
<td align="right">10.7%</td>
<td align="right">59,374</td>
<td align="right">9.3%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">259,505,063,052</td>
<td align="right">6,495.9%</td>
<td align="right">268,142,534,000</td>
<td align="right">6,621.0%</td>
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
<td align="right">3,994,922,911</td>
<td align="right"></td>
<td align="right">4,049,870,265</td>
<td align="right"></td>
<td align="right">1.4%</td>
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
<td align="right">23,079</td>
<td align="right">82.9%</td>
<td align="right">93,049</td>
<td align="right">90.6%</td>
<td align="right">303.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">27,839</td>
<td align="right"></td>
<td align="right">102,742</td>
<td align="right"></td>
<td align="right">269.1%</td>
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
<td align="right">109</td>
<td align="right">0.1%</td>
<td align="right">109 / 0 !!</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">1,634,304</td>
<td align="right">0.5%</td>
<td align="right">279,199,744</td>
<td align="right">24.9%</td>
<td align="right">16,983.7%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">48,470,727</td>
<td align="right">16.1%</td>
<td align="right">201,913,384</td>
<td align="right">18.0%</td>
<td align="right">316.6%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">6,279,472</td>
<td align="right">2.1%</td>
<td align="right">23,562,288</td>
<td align="right">2.1%</td>
<td align="right">275.2%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">300,838,912</td>
<td align="right"></td>
<td align="right">1,120,362,496</td>
<td align="right"></td>
<td align="right">272.4%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">246,088,713</td>
<td align="right">81.8%</td>
<td align="right">894,886,824</td>
<td align="right">79.9%</td>
<td align="right">263.6%</td>
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
<td align="left">5,196</td>
<td align="right">22.5%</td>
<td align="left">17,173</td>
<td align="right">18.5%</td>
<td align="right">230.5%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">6,866</td>
<td align="right">29.7%</td>
<td align="left">37,975</td>
<td align="right">40.8%</td>
<td align="right">453.1%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">7,005</td>
<td align="right">30.4%</td>
<td align="left">24,639</td>
<td align="right">26.5%</td>
<td align="right">251.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,813</td>
<td align="right">12.2%</td>
<td align="left">10,376</td>
<td align="right">11.2%</td>
<td align="right">268.9%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,139</td>
<td align="right">4.9%</td>
<td align="left">2,465</td>
<td align="right">2.6%</td>
<td align="right">116.4%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">60</td>
<td align="right">0.3%</td>
<td align="left">421</td>
<td align="right">0.5%</td>
<td align="right">601.7%</td>
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
<td align="right">1,298</td>
<td align="right">4.7%</td>
<td align="right">3,184</td>
<td align="right">3.1%</td>
<td align="right">145.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">810</td>
<td align="right">2.9%</td>
<td align="right">5,666</td>
<td align="right">5.5%</td>
<td align="right">599.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,028</td>
<td align="right">14.5%</td>
<td align="right">13,627</td>
<td align="right">13.3%</td>
<td align="right">238.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,393</td>
<td align="right">30.1%</td>
<td align="right">41,872</td>
<td align="right">40.8%</td>
<td align="right">398.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">5,672</td>
<td align="right">20.4%</td>
<td align="right">18,650</td>
<td align="right">18.2%</td>
<td align="right">228.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,306</td>
<td align="right">19.1%</td>
<td align="right">14,343</td>
<td align="right">14.0%</td>
<td align="right">170.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,982</td>
<td align="right">7.1%</td>
<td align="right">4,284</td>
<td align="right">4.2%</td>
<td align="right">116.1%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">350</td>
<td align="right">1.3%</td>
<td align="right">1,116</td>
<td align="right">1.1%</td>
<td align="right">218.9%</td>
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
<td align="right">749</td>
<td align="right">2.7%</td>
<td align="right">1,855</td>
<td align="right">1.8%</td>
<td align="right">147.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">839</td>
<td align="right">3.0%</td>
<td align="right">3,140</td>
<td align="right">3.1%</td>
<td align="right">274.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,037</td>
<td align="right">7.3%</td>
<td align="right">8,269</td>
<td align="right">8.0%</td>
<td align="right">305.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,547</td>
<td align="right">27.1%</td>
<td align="right">36,207</td>
<td align="right">35.2%</td>
<td align="right">379.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">6,711</td>
<td align="right">24.1%</td>
<td align="right">26,571</td>
<td align="right">25.9%</td>
<td align="right">295.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,865</td>
<td align="right">10.3%</td>
<td align="right">10,665</td>
<td align="right">10.4%</td>
<td align="right">272.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,060</td>
<td align="right">7.4%</td>
<td align="right">5,368</td>
<td align="right">5.2%</td>
<td align="right">160.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">271</td>
<td align="right">1.0%</td>
<td align="right">974</td>
<td align="right">0.9%</td>
<td align="right">259.4%</td>
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
<td align="left">_DELETE_SUBSCR</td>
<td align="right">15,603</td>
<td align="right">16,221,512</td>
<td align="right">103,864.1%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">62</td>
<td align="right">8,636</td>
<td align="right">13,829.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">20,173</td>
<td align="right">525,070</td>
<td align="right">2,502.8%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">513,463</td>
<td align="right">1,806.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">3,709,046</td>
<td align="right">51,452,990</td>
<td align="right">1,287.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">36,000</td>
<td align="right">140,940</td>
<td align="right">291.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">36,040</td>
<td align="right">140,600</td>
<td align="right">290.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">154,160</td>
<td align="right">564,353</td>
<td align="right">266.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">1,212,416</td>
<td align="right">211.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">143,096</td>
<td align="right">430,802</td>
<td align="right">201.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,152,113</td>
<td align="right">2,745,650</td>
<td align="right">138.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">94,858,325</td>
<td align="right">225,013,993</td>
<td align="right">137.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,858,325</td>
<td align="right">225,013,993</td>
<td align="right">137.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">95,607,725</td>
<td align="right">226,616,393</td>
<td align="right">137.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">267,905</td>
<td align="right">530,547</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">8,323,320</td>
<td align="right">14,384,252</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">392,500</td>
<td align="right">611,940</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">211,872,933</td>
<td align="right">289,983,993</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,635,678</td>
<td align="right">6,318,439</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">38,523,146</td>
<td align="right">25,761,102</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">158,910,016</td>
<td align="right">210,891,804</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,761,135</td>
<td align="right">67,859,091</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,761,135</td>
<td align="right">67,469,179</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">6,017,140</td>
<td align="right">7,775,466</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">79,004,912</td>
<td align="right">100,353,886</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">229,826</td>
<td align="right">283,133</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,253,140</td>
<td align="right">4,003,480</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">348,192,254</td>
<td align="right">413,913,137</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">147,815,936</td>
<td align="right">175,011,529</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">338,993,252</td>
<td align="right">400,310,520</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">66,342,403</td>
<td align="right">77,615,968</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">5,266,200</td>
<td align="right">6,136,260</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">103,178,820</td>
<td align="right">119,301,800</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">103,178,069</td>
<td align="right">119,283,313</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,070,900</td>
<td align="right">3,529,766</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,123,223</td>
<td align="right">5,795,025</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,545,786</td>
<td align="right">1,742,262</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">8,140,533</td>
<td align="right">9,171,262</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">118,884,105</td>
<td align="right">133,672,124</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">7,339,049</td>
<td align="right">8,250,456</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">7,325,900</td>
<td align="right">8,233,220</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,714,440</td>
<td align="right">3,049,197</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,372,248</td>
<td align="right">3,776,491</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">168,063,305</td>
<td align="right">186,881,948</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,583,966</td>
<td align="right">48,353,880</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">12,248,707</td>
<td align="right">13,549,614</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">182,403,379</td>
<td align="right">163,725,676</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">666,859,531</td>
<td align="right">734,994,478</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">98,482</td>
<td align="right">108,526</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">47,912,441</td>
<td align="right">52,760,335</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">204,461,426</td>
<td align="right">225,086,668</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">41,237,221</td>
<td align="right">45,386,834</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">500,058,971</td>
<td align="right">549,668,300</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">4,279,396</td>
<td align="right">4,698,976</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">312,114,511</td>
<td align="right">342,621,534</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">83,680,143</td>
<td align="right">91,785,725</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,510,797,052</td>
<td align="right">1,654,069,991</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,511,084,170</td>
<td align="right">1,654,230,281</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">34,720,259</td>
<td align="right">31,444,774</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">10,568,590</td>
<td align="right">11,546,858</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">48,491,886</td>
<td align="right">52,904,047</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">307,910,140</td>
<td align="right">335,111,456</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">230,588,327</td>
<td align="right">248,940,800</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,702,411</td>
<td align="right">13,708,947</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,702,411</td>
<td align="right">13,708,947</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">155,096,777</td>
<td align="right">167,335,440</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">37,692,986</td>
<td align="right">40,649,165</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,159,872</td>
<td align="right">6,636,562</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">76,740,980</td>
<td align="right">82,457,785</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">20,095,502</td>
<td align="right">21,582,270</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">449,391,838</td>
<td align="right">481,876,723</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">448,447,521</td>
<td align="right">480,600,959</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">671,060,182</td>
<td align="right">719,111,003</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">727,586,822</td>
<td align="right">779,589,788</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">43,817,917</td>
<td align="right">46,933,672</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">155,378,583</td>
<td align="right">166,242,082</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">308,882,849</td>
<td align="right">330,105,152</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">37,153,757</td>
<td align="right">39,700,071</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">153,037,305</td>
<td align="right">163,485,718</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">24,484,725</td>
<td align="right">26,058,585</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">24,484,725</td>
<td align="right">26,058,585</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">131,204,056</td>
<td align="right">139,629,970</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">71,285,220</td>
<td align="right">75,857,343</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">57,363,422</td>
<td align="right">61,032,749</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,963,698,360</td>
<td align="right">8,450,975,873</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">35,808,174</td>
<td align="right">37,992,728</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">3,074,804,704</td>
<td align="right">3,261,254,362</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">294,511,981</td>
<td align="right">312,237,605</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">30,896,592</td>
<td align="right">32,719,514</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">30,896,592</td>
<td align="right">32,719,514</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">360,587,445</td>
<td align="right">381,662,226</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">442,899,227</td>
<td align="right">467,269,498</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">343,160,867</td>
<td align="right">362,039,323</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">395,752,204</td>
<td align="right">417,471,590</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,306,840,800</td>
<td align="right">1,376,700,343</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,306,840,800</td>
<td align="right">1,376,700,343</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,294,138,389</td>
<td align="right">1,362,991,396</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">551,183,686</td>
<td align="right">579,950,356</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">56,025,976</td>
<td align="right">58,822,915</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,227,315,225</td>
<td align="right">1,288,146,588</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">263,041,285</td>
<td align="right">276,054,062</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,267,005,892</td>
<td align="right">1,329,357,768</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,904,185,801</td>
<td align="right">4,093,483,528</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,560</td>
<td align="right">49,875,981</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">4,161,571,297</td>
<td align="right">4,352,365,034</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">45,068,860</td>
<td align="right">47,104,173</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">155,428,015</td>
<td align="right">148,489,472</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">48,050,999</td>
<td align="right">50,168,421</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">131,031,703</td>
<td align="right">125,458,884</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">469,930,922</td>
<td align="right">489,022,578</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,910,855,377</td>
<td align="right">1,987,188,551</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,565,027,248</td>
<td align="right">1,503,227,267</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,593,190</td>
<td align="right">48,411,461</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">40,547,060,802</td>
<td align="right">42,064,772,290</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,888,574,731</td>
<td align="right">4,032,503,898</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">263,848,363</td>
<td align="right">273,592,226</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">244,950,124</td>
<td align="right">253,734,313</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,430,861,768</td>
<td align="right">1,481,730,303</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">419,919,111</td>
<td align="right">434,820,654</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,940,449</td>
<td align="right">49,638,201</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,534,037,361</td>
<td align="right">3,655,411,898</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">45,757,239,355</td>
<td align="right">47,304,109,778</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">148,521,765</td>
<td align="right">153,489,655</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,304,961,036</td>
<td align="right">1,347,856,001</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">835,638,607</td>
<td align="right">862,586,758</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">415,521,665</td>
<td align="right">428,900,396</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,222,472,906</td>
<td align="right">2,290,947,122</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">11,120,727,858</td>
<td align="right">11,461,575,217</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">103,831,657</td>
<td align="right">107,006,301</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,849,247,991</td>
<td align="right">1,905,610,523</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">400,645,501</td>
<td align="right">412,766,544</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">787,400,476</td>
<td align="right">811,045,351</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,847,690,943</td>
<td align="right">1,902,115,072</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">56,155,877</td>
<td align="right">57,749,363</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,004,097,247</td>
<td align="right">1,032,544,559</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,003,967,087</td>
<td align="right">1,031,841,414</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">440,901,006</td>
<td align="right">453,115,065</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,279,229,832</td>
<td align="right">2,340,691,619</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">179,241,294</td>
<td align="right">184,042,795</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,225,102,451</td>
<td align="right">1,257,560,925</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">7,148,147,042</td>
<td align="right">7,329,183,822</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,069,224,158</td>
<td align="right">2,121,294,188</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,069,401,788</td>
<td align="right">3,145,174,566</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,869,133,537</td>
<td align="right">2,938,779,711</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">32,831,684</td>
<td align="right">33,622,727</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">2,509,970,716</td>
<td align="right">2,566,509,665</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">585,072,289</td>
<td align="right">597,825,627</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">531,563,251</td>
<td align="right">543,045,938</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">544,467,694</td>
<td align="right">556,082,609</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,402,325,925</td>
<td align="right">1,431,806,343</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">768,856,688</td>
<td align="right">784,729,006</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,250,788,479</td>
<td align="right">1,275,562,422</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">455,524,823</td>
<td align="right">464,508,431</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">455,524,823</td>
<td align="right">464,508,431</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">604,429,191</td>
<td align="right">592,748,286</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">358,301,634</td>
<td align="right">365,203,650</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,146,019,480</td>
<td align="right">1,167,875,415</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">434,055,902</td>
<td align="right">442,243,864</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,123,795,968</td>
<td align="right">1,144,857,247</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">118,974,119</td>
<td align="right">121,189,796</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">143,590,077</td>
<td align="right">146,216,667</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">655,286,703</td>
<td align="right">666,997,185</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">245,263,006</td>
<td align="right">249,590,064</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,493</td>
<td align="right">71,588,771</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,493</td>
<td align="right">71,588,771</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">263,905,177</td>
<td align="right">268,343,580</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,087,407,991</td>
<td align="right">1,069,770,931</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,770,000</td>
<td align="right">74,951,660</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">504,406,438</td>
<td align="right">512,367,012</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">229,988,990</td>
<td align="right">233,471,896</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,119,801,609</td>
<td align="right">1,136,674,139</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,960,182,479</td>
<td align="right">4,017,900,421</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">40,586,464</td>
<td align="right">41,147,417</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,994,922,911</td>
<td align="right">4,049,870,265</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,873,531,405</td>
<td align="right">2,913,036,241</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">39,818,680</td>
<td align="right">40,339,096</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,472,840,530</td>
<td align="right">4,531,054,794</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,013,202,971</td>
<td align="right">1,026,267,559</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,187,668,336</td>
<td align="right">1,202,954,871</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">867,457,716</td>
<td align="right">878,548,874</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,327,793,128</td>
<td align="right">1,311,137,274</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,391,363,466</td>
<td align="right">2,421,036,920</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,457,696,372</td>
<td align="right">6,536,302,216</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,454,107,403</td>
<td align="right">4,507,284,572</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">4,040,875,304</td>
<td align="right">4,087,701,659</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">416,677,115</td>
<td align="right">421,094,417</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">261,479,355</td>
<td align="right">264,128,283</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">805,129,038</td>
<td align="right">813,252,406</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,754,598,360</td>
<td align="right">1,771,873,796</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,462,773,461</td>
<td align="right">2,486,431,951</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">927,042,227</td>
<td align="right">935,814,037</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">259,280,781</td>
<td align="right">261,728,046</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,069,782,788</td>
<td align="right">1,079,073,601</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">927,027,367</td>
<td align="right">935,077,516</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">597,053,767</td>
<td align="right">601,900,254</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,975,980</td>
<td align="right">2,999,640</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,975,980</td>
<td align="right">2,999,640</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,801,676,121</td>
<td align="right">1,787,418,651</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">112,177,519</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">445,741,619</td>
<td align="right">448,424,688</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">445,741,619</td>
<td align="right">448,424,688</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,025,452</td>
<td align="right">40,241,259</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">40,765,829</td>
<td align="right">40,565,975</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">20,612,164</td>
<td align="right">20,712,502</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">45,671,120</td>
<td align="right">45,869,468</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">746,007,085</td>
<td align="right">749,230,453</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,344,881,921</td>
<td align="right">1,349,901,979</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,481,108,626</td>
<td align="right">1,485,768,032</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">982,062,705</td>
<td align="right">985,008,803</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,200,917,638</td>
<td align="right">1,204,215,248</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,079</td>
<td align="right">47,182,318</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">753,657,523</td>
<td align="right">755,034,174</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">498,439,034</td>
<td align="right">499,165,971</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,013,740</td>
<td align="right">60,072,771</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">975,769,285</td>
<td align="right">976,657,223</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,998,262,818</td>
<td align="right">1,998,718,204</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">3,106,080</td>
<td align="right">3,106,061</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right">3,555,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">74,500</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_THIRD_NULL</td>
<td align="right"></td>
<td align="right">57,371</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">38,918</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">13,389</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">7,528</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_TYPE_1</td>
<td align="right"></td>
<td align="right">5,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right"></td>
<td align="right">3,809</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">2,878</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_TUPLE_1</td>
<td align="right"></td>
<td align="right">1,437</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INSERT_NULL</td>
<td align="right"></td>
<td align="right">336</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right"></td>
<td align="right">336</td>
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
<td align="right">1,822</td>
<td align="right">5,232</td>
<td align="right">187.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">23,564</td>
<td align="right">34,480</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right">23,046</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">1,380</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right"></td>
<td align="right">21</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">101</td>
<td align="right">188</td>
<td align="right">86.1%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">101</td>
<td align="right">188</td>
<td align="right">86.1%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,592</td>
<td align="right">22,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">34</td>
<td align="right">34</td>
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
<td align="right">41</td>
<td align="right">41</td>
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
<td align="right">2,397</td>
<td align="right">2,397</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-24
