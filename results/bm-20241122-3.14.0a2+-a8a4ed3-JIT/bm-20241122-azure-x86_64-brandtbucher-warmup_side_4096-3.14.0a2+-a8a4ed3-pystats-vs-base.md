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
<td align="left">STORE_SLICE</td>
<td align="right">350,321</td>
<td align="right">1,194,074</td>
<td align="right">240.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">74,371,772</td>
<td align="right">36,612,246</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">80,409,122</td>
<td align="right">42,655,539</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">40,648,517</td>
<td align="right">21,772,687</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,705,954</td>
<td align="right">3,902,679</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">95,087,359</td>
<td align="right">58,606,871</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">874,694</td>
<td align="right">1,199,717</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">132,624,377</td>
<td align="right">95,334,203</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,344,149</td>
<td align="right">4,250,698</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">324,821,440</td>
<td align="right">255,571,332</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">204,303,533</td>
<td align="right">169,068,235</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">225,733,543</td>
<td align="right">189,553,643</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,802,254</td>
<td align="right">2,090,178</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">491,023,723</td>
<td align="right">568,884,903</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">177,080,356</td>
<td align="right">204,608,039</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">214,282,444</td>
<td align="right">182,227,542</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">335,257,931</td>
<td align="right">285,258,509</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">69,734,796</td>
<td align="right">78,786,815</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">21,894,995</td>
<td align="right">24,711,175</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">48,504,597</td>
<td align="right">54,610,464</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">70,851,501</td>
<td align="right">79,743,851</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">242,354,856</td>
<td align="right">268,624,912</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">119,981,338</td>
<td align="right">132,583,543</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">47,084,043</td>
<td align="right">51,845,539</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,616,342,350</td>
<td align="right">1,458,365,349</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">298,524,776</td>
<td align="right">326,605,872</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">327,755,955</td>
<td align="right">358,480,822</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">31,252,959</td>
<td align="right">34,155,538</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">114,671,862</td>
<td align="right">125,201,902</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">135,115,135</td>
<td align="right">147,247,362</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">143,926,467</td>
<td align="right">156,454,123</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">29,408,639</td>
<td align="right">31,666,907</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">23,387,056</td>
<td align="right">25,177,352</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">53,335,528</td>
<td align="right">57,231,838</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">95,525,606</td>
<td align="right">102,459,338</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">164,688,241</td>
<td align="right">176,191,192</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">326,338,140</td>
<td align="right">348,703,952</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">126,710,314</td>
<td align="right">135,337,175</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,509,237</td>
<td align="right">18,676,927</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">33,983,773</td>
<td align="right">36,230,552</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">90,122,456</td>
<td align="right">96,042,369</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">56,071,707</td>
<td align="right">59,740,773</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">170,298,664</td>
<td align="right">181,352,154</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">8,986,717</td>
<td align="right">9,564,432</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,895,878</td>
<td align="right">36,064,473</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">416,578,567</td>
<td align="right">389,927,833</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,863,945,888</td>
<td align="right">1,745,849,997</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,511,864</td>
<td align="right">9,043,777</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,125,849,461</td>
<td align="right">2,258,442,794</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">735,220</td>
<td align="right">781,020</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">428,141,939</td>
<td align="right">454,767,718</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">91,578,713</td>
<td align="right">97,193,575</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">286,964,511</td>
<td align="right">269,454,689</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">84,579,009</td>
<td align="right">89,575,867</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">49,217,519</td>
<td align="right">52,094,485</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">34,754,152</td>
<td align="right">36,779,151</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">47,243,155</td>
<td align="right">49,994,706</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">265,958,071</td>
<td align="right">280,902,054</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">534,392,720</td>
<td align="right">563,751,116</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,534,222</td>
<td align="right">37,484,883</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">223,497,133</td>
<td align="right">235,712,908</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">671,294,716</td>
<td align="right">706,428,611</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">862,098,910</td>
<td align="right">905,864,172</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">499,294,581</td>
<td align="right">524,472,460</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">53,762,163</td>
<td align="right">56,471,385</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">182,868,501</td>
<td align="right">173,688,837</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">96,957,259</td>
<td align="right">101,786,940</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">149,815,110</td>
<td align="right">157,183,942</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">216,190,532</td>
<td align="right">226,682,502</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,794,820</td>
<td align="right">3,974,944</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">618,516,809</td>
<td align="right">647,446,400</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">43,604,543</td>
<td align="right">45,565,367</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">451,872,543</td>
<td align="right">472,001,838</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">62,655,055</td>
<td align="right">65,317,419</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">180,808,988</td>
<td align="right">188,311,416</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">56,598,177</td>
<td align="right">58,922,597</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">117,278,686</td>
<td align="right">122,063,577</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,547,823,609</td>
<td align="right">1,610,551,732</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">647,142,484</td>
<td align="right">672,907,762</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">8,723,548</td>
<td align="right">9,066,651</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">49,553,221</td>
<td align="right">51,236,993</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">154,214,859</td>
<td align="right">159,346,365</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">509,673,030</td>
<td align="right">526,197,114</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">292,871,127</td>
<td align="right">302,286,295</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,152,080,767</td>
<td align="right">3,051,324,530</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">29,494,895</td>
<td align="right">30,432,398</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">89,098,153</td>
<td align="right">91,925,134</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">216,354,181</td>
<td align="right">223,013,431</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">401,493,519</td>
<td align="right">413,675,490</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,362,431</td>
<td align="right">11,705,435</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">4,068,864</td>
<td align="right">3,948,460</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">56,051,022</td>
<td align="right">57,701,826</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">288,418,424</td>
<td align="right">296,565,997</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">103,741,518</td>
<td align="right">106,668,980</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">153,371,688</td>
<td align="right">157,612,780</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">32,339,376</td>
<td align="right">33,210,276</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">263,960,161</td>
<td align="right">271,011,305</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,574,320</td>
<td align="right">10,292,090</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">83,545,822</td>
<td align="right">85,741,761</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">62,617,225</td>
<td align="right">64,192,099</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">68,465,650</td>
<td align="right">70,135,682</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">156,917,262</td>
<td align="right">160,631,442</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">111,939,178</td>
<td align="right">114,428,732</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">380,090,575</td>
<td align="right">388,304,124</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">472,573,149</td>
<td align="right">482,758,941</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,169,791,129</td>
<td align="right">1,194,618,505</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">771,139,853</td>
<td align="right">787,412,595</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">46,454,989</td>
<td align="right">47,400,531</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,755,052,578</td>
<td align="right">3,829,566,261</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,865,138,973</td>
<td align="right">3,793,419,423</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">231,805</td>
<td align="right">235,942</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,243,990</td>
<td align="right">13,022,518</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">57,319,359</td>
<td align="right">58,259,059</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">228,013,521</td>
<td align="right">231,576,269</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">66,471,820</td>
<td align="right">67,465,370</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">33,731,878</td>
<td align="right">34,232,276</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">48,281,245</td>
<td align="right">48,916,847</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,043,558,760</td>
<td align="right">13,203,509,279</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,450,811,594</td>
<td align="right">4,397,040,208</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">185,872,000</td>
<td align="right">188,039,094</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">406,375,477</td>
<td align="right">411,083,440</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">58,882</td>
<td align="right">59,548</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,329,188,818</td>
<td align="right">2,354,301,227</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">168,350,427</td>
<td align="right">170,068,018</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,724,285,271</td>
<td align="right">2,696,663,718</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">110,940,426</td>
<td align="right">112,042,772</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">204,513,188</td>
<td align="right">206,464,088</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">264,080,428</td>
<td align="right">266,568,972</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">11,777,093</td>
<td align="right">11,667,336</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">344,628,007</td>
<td align="right">347,643,030</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,030,102,765</td>
<td align="right">3,055,442,894</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">96,403,175</td>
<td align="right">97,134,602</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">806,028,533</td>
<td align="right">811,349,344</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">115,445,925</td>
<td align="right">114,767,740</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">82,788,625</td>
<td align="right">83,252,366</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">116,627,478</td>
<td align="right">117,236,007</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,628,999,155</td>
<td align="right">1,636,378,940</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,870,641</td>
<td align="right">3,854,163</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">771,106</td>
<td align="right">773,658</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,075,443,547</td>
<td align="right">2,082,128,097</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">644,942,753</td>
<td align="right">647,009,523</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">23,496,414</td>
<td align="right">23,563,774</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">57,583,032</td>
<td align="right">57,712,484</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">115,803,793</td>
<td align="right">116,016,067</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,840,723</td>
<td align="right">26,875,920</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,967,497</td>
<td align="right">8,976,944</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,726</td>
<td align="right">33,737</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">75,185,049</td>
<td align="right">75,207,531</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,923,429,724</td>
<td align="right">1,923,053,481</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,786,555,355</td>
<td align="right">1,786,745,193</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,828,540</td>
<td align="right">1,071,934,982</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,875,171</td>
<td align="right">20,876,583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,439,827</td>
<td align="right">1,439,922</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">405,874</td>
<td align="right">405,853</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,115,046</td>
<td align="right">3,115,130</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,875</td>
<td align="right">120,877</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,847</td>
<td align="right">6,169,885</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">153,381,565</td>
<td align="right">153,382,335</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,545,924</td>
<td align="right">20,545,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,876,545</td>
<td align="right">20,876,604</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,230</td>
<td align="right">14,760,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,814,165</td>
<td align="right">100,814,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,376</td>
<td align="right">302,607,376</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,588</td>
<td align="right">128,850,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
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
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">4,866,975</td>
<td align="right">4,866,975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,140</td>
<td align="right">2,597,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,935</td>
<td align="right">1,645,935</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,720</td>
<td align="right">98,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,553</td>
<td align="right">84,553</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,192</td>
<td align="right">57,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,672</td>
<td align="right">56,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,546</td>
<td align="right">17,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,321</td>
<td align="right">5,321</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,896</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,642</td>
<td align="right">3,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,708</td>
<td align="right">2,708</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">150</td>
<td align="right">150</td>
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
<td align="right">44</td>
<td align="right">44</td>
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
<td align="right">325,565,375</td>
<td align="right">4.2%</td>
<td align="right">347,913,633</td>
<td align="right">4.5%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21,763,160</td>
<td align="right">0.3%</td>
<td align="right">22,173,925</td>
<td align="right">0.3%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,375,449,413</td>
<td align="right">95.5%</td>
<td align="right">7,375,013,011</td>
<td align="right">95.2%</td>
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
<td align="right">765,713</td>
<td align="right">100.0%</td>
<td align="right">783,293</td>
<td align="right">100.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">add different types</td>
<td align="right">44,160</td>
<td align="right">5.8%</td>
<td align="right">59,034</td>
<td align="right">7.5%</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1,323</td>
<td align="right">0.2%</td>
<td align="right">1,627</td>
<td align="right">0.2%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,372</td>
<td align="right">0.7%</td>
<td align="right">6,212</td>
<td align="right">0.8%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">11,799</td>
<td align="right">1.5%</td>
<td align="right">13,445</td>
<td align="right">1.7%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,475</td>
<td align="right">0.5%</td>
<td align="right">3,770</td>
<td align="right">0.5%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">5,016</td>
<td align="right">0.7%</td>
<td align="right">5,313</td>
<td align="right">0.7%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">38,929</td>
<td align="right">5.1%</td>
<td align="right">36,898</td>
<td align="right">4.7%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">9,849</td>
<td align="right">1.3%</td>
<td align="right">10,347</td>
<td align="right">1.3%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">22,558</td>
<td align="right">2.9%</td>
<td align="right">23,551</td>
<td align="right">3.0%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">806</td>
<td align="right">0.1%</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">6,236</td>
<td align="right">0.8%</td>
<td align="right">6,351</td>
<td align="right">0.8%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,364</td>
<td align="right">0.2%</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,785</td>
<td align="right">2.6%</td>
<td align="right">19,643</td>
<td align="right">2.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">492</td>
<td align="right">0.1%</td>
<td align="right">490</td>
<td align="right">0.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">5,987</td>
<td align="right">0.8%</td>
<td align="right">6,007</td>
<td align="right">0.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">2,571</td>
<td align="right">0.3%</td>
<td align="right">2,569</td>
<td align="right">0.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">583,565</td>
<td align="right">76.2%</td>
<td align="right">583,390</td>
<td align="right">74.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.3%</td>
<td align="right">2,343</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">83</td>
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
<td align="right">91,578,713</td>
<td align="right">100.0%</td>
<td align="right">97,193,575</td>
<td align="right">100.0%</td>
<td align="right">6.1%</td>
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
<td align="right">401,354,901</td>
<td align="right">6.8%</td>
<td align="right">413,533,878</td>
<td align="right">7.0%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,826,429</td>
<td align="right">0.1%</td>
<td align="right">5,823,006</td>
<td align="right">0.1%</td>
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
<td align="right">5,470,712,659</td>
<td align="right">93.1%</td>
<td align="right">5,470,630,018</td>
<td align="right">92.9%</td>
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
<td align="right">129,340</td>
<td align="right">52.1%</td>
<td align="right">132,334</td>
<td align="right">52.7%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">119,017</td>
<td align="right">47.9%</td>
<td align="right">118,932</td>
<td align="right">47.3%</td>
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
<td align="left">buffer int</td>
<td align="right">2,915</td>
<td align="right">2.3%</td>
<td align="right">3,675</td>
<td align="right">2.8%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">6,519</td>
<td align="right">5.0%</td>
<td align="right">7,141</td>
<td align="right">5.4%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">728</td>
<td align="right">0.6%</td>
<td align="right">768</td>
<td align="right">0.6%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,479</td>
<td align="right">2.7%</td>
<td align="right">3,651</td>
<td align="right">2.8%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">47,168</td>
<td align="right">36.5%</td>
<td align="right">48,245</td>
<td align="right">36.5%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">18,167</td>
<td align="right">14.0%</td>
<td align="right">18,318</td>
<td align="right">13.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">34,884</td>
<td align="right">27.0%</td>
<td align="right">35,055</td>
<td align="right">26.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,446</td>
<td align="right">9.6%</td>
<td align="right">12,447</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.3%</td>
<td align="right">2,941</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">120,315,012</td>
<td align="right">1.1%</td>
<td align="right">120,571,150</td>
<td align="right">1.1%</td>
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
<td align="right">10,897,058,592</td>
<td align="right">98.9%</td>
<td align="right">10,893,278,877</td>
<td align="right">98.9%</td>
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
<td align="right">230,176</td>
<td align="right">0.0%</td>
<td align="right">230,188</td>
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
<td align="right">22,186</td>
<td align="right">0.0%</td>
<td align="right">22,186</td>
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
<td align="right">2,461,759</td>
<td align="right">100.0%</td>
<td align="right">2,469,140</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">569</td>
<td align="right">0.0%</td>
<td align="right">569</td>
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
<td align="right">752</td>
<td align="right">132.2%</td>
<td align="right">752</td>
<td align="right">132.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">569</td>
<td align="right">100.0%</td>
<td align="right">569</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">386</td>
<td align="right">67.8%</td>
<td align="right">386</td>
<td align="right">67.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">287</td>
<td align="right">50.4%</td>
<td align="right">287</td>
<td align="right">50.4%</td>
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
<td align="right">446,694</td>
<td align="right">78.7%</td>
<td align="right">584,207</td>
<td align="right">82.9%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">111,570</td>
<td align="right">19.7%</td>
<td align="right">111,570</td>
<td align="right">15.8%</td>
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
<td align="right">1,121,557</td>
<td align="right">0.0%</td>
<td align="right">1,311,403</td>
<td align="right">0.0%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">84,463,643</td>
<td align="right">1.8%</td>
<td align="right">89,451,706</td>
<td align="right">1.9%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,516,651,804</td>
<td align="right">98.1%</td>
<td align="right">4,516,414,688</td>
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
<td align="left">Success</td>
<td align="right">39,104</td>
<td align="right">28.7%</td>
<td align="right">42,700</td>
<td align="right">28.7%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97,107</td>
<td align="right">71.3%</td>
<td align="right">105,883</td>
<td align="right">71.3%</td>
<td align="right">9.0%</td>
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
<td align="right">36,643</td>
<td align="right">37.7%</td>
<td align="right">43,585</td>
<td align="right">41.2%</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">812</td>
<td align="right">0.8%</td>
<td align="right">935</td>
<td align="right">0.9%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,495</td>
<td align="right">8.7%</td>
<td align="right">9,356</td>
<td align="right">8.8%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,075</td>
<td align="right">7.3%</td>
<td align="right">7,772</td>
<td align="right">7.3%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,121</td>
<td align="right">1.2%</td>
<td align="right">1,221</td>
<td align="right">1.2%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">341</td>
<td align="right">0.4%</td>
<td align="right">361</td>
<td align="right">0.3%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,086</td>
<td align="right">4.2%</td>
<td align="right">4,146</td>
<td align="right">3.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,446</td>
<td align="right">6.6%</td>
<td align="right">6,424</td>
<td align="right">6.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,156</td>
<td align="right">23.8%</td>
<td align="right">23,151</td>
<td align="right">21.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.9%</td>
<td align="right">7,639</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">959</td>
<td align="right">1.0%</td>
<td align="right">959</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">334</td>
<td align="right">0.3%</td>
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
<td align="right">47,049,472</td>
<td align="right">2.1%</td>
<td align="right">51,809,272</td>
<td align="right">2.3%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,182,866,768</td>
<td align="right">97.8%</td>
<td align="right">2,182,673,985</td>
<td align="right">97.6%</td>
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
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
<td align="right">1,916,987</td>
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
<td align="right">32,311</td>
<td align="right">100.0%</td>
<td align="right">34,007</td>
<td align="right">100.0%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">str</td>
<td align="right">8,272</td>
<td align="right">25.6%</td>
<td align="right">9,226</td>
<td align="right">27.1%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,571</td>
<td align="right">23.4%</td>
<td align="right">7,846</td>
<td align="right">23.1%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,809</td>
<td align="right">33.5%</td>
<td align="right">11,195</td>
<td align="right">32.9%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,659</td>
<td align="right">17.5%</td>
<td align="right">5,740</td>
<td align="right">16.9%</td>
<td align="right">1.4%</td>
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
<td align="right">24,233,637</td>
<td align="right">3.3%</td>
<td align="right">32,961,182</td>
<td align="right">4.4%</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">117,208,472</td>
<td align="right">16.1%</td>
<td align="right">121,966,250</td>
<td align="right">16.2%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">584,492,991</td>
<td align="right">80.5%</td>
<td align="right">599,485,236</td>
<td align="right">79.5%</td>
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
<td align="left">Failure</td>
<td align="right">65,106</td>
<td align="right">12.3%</td>
<td align="right">92,238</td>
<td align="right">12.8%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">462,156</td>
<td align="right">87.7%</td>
<td align="right">626,860</td>
<td align="right">87.2%</td>
<td align="right">35.6%</td>
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
<td align="right">21,833</td>
<td align="right">33.5%</td>
<td align="right">50,337</td>
<td align="right">54.6%</td>
<td align="right">130.6%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">6,856</td>
<td align="right">10.5%</td>
<td align="right">4,183</td>
<td align="right">4.5%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">263</td>
<td align="right">0.4%</td>
<td align="right">327</td>
<td align="right">0.4%</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">9,676</td>
<td align="right">14.9%</td>
<td align="right">10,747</td>
<td align="right">11.7%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,747</td>
<td align="right">2.7%</td>
<td align="right">1,567</td>
<td align="right">1.7%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,706</td>
<td align="right">7.2%</td>
<td align="right">4,866</td>
<td align="right">5.3%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,356</td>
<td align="right">6.7%</td>
<td align="right">4,495</td>
<td align="right">4.9%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">2,929</td>
<td align="right">4.5%</td>
<td align="right">3,015</td>
<td align="right">3.3%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,282</td>
<td align="right">3.5%</td>
<td align="right">2,247</td>
<td align="right">2.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,879</td>
<td align="right">9.0%</td>
<td align="right">5,874</td>
<td align="right">6.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,866</td>
<td align="right">4.4%</td>
<td align="right">2,867</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,405</td>
<td align="right">2.2%</td>
<td align="right">1,405</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">174</td>
<td align="right">0.3%</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">134</td>
<td align="right">0.2%</td>
<td align="right">134</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">496,358,878</td>
<td align="right">3.8%</td>
<td align="right">576,009,031</td>
<td align="right">4.4%</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">450,439,854</td>
<td align="right">3.4%</td>
<td align="right">470,508,215</td>
<td align="right">3.6%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,401,145</td>
<td align="right">0.0%</td>
<td align="right">1,404,526</td>
<td align="right">0.0%</td>
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
<td align="right">12,172,908,967</td>
<td align="right">92.8%</td>
<td align="right">12,165,172,264</td>
<td align="right">92.1%</td>
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
<td align="left">Success</td>
<td align="right">10,575,448</td>
<td align="right">98.0%</td>
<td align="right">12,132,444</td>
<td align="right">98.2%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">212,693</td>
<td align="right">2.0%</td>
<td align="right">219,553</td>
<td align="right">1.8%</td>
<td align="right">3.2%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">22,166</td>
<td align="right">10.4%</td>
<td align="right">24,123</td>
<td align="right">11.0%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,520</td>
<td align="right">0.7%</td>
<td align="right">1,640</td>
<td align="right">0.7%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">920</td>
<td align="right">0.4%</td>
<td align="right">855</td>
<td align="right">0.4%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">58,739</td>
<td align="right">27.6%</td>
<td align="right">61,481</td>
<td align="right">28.0%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,469</td>
<td align="right">1.2%</td>
<td align="right">2,404</td>
<td align="right">1.1%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,589</td>
<td align="right">0.7%</td>
<td align="right">1,628</td>
<td align="right">0.7%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40,691</td>
<td align="right">19.1%</td>
<td align="right">41,640</td>
<td align="right">19.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,878</td>
<td align="right">2.3%</td>
<td align="right">4,980</td>
<td align="right">2.3%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">37,386</td>
<td align="right">17.6%</td>
<td align="right">38,129</td>
<td align="right">17.4%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,287</td>
<td align="right">6.7%</td>
<td align="right">14,513</td>
<td align="right">6.6%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,564</td>
<td align="right">3.6%</td>
<td align="right">7,585</td>
<td align="right">3.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,136</td>
<td align="right">3.8%</td>
<td align="right">8,128</td>
<td align="right">3.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,189</td>
<td align="right">0.6%</td>
<td align="right">1,189</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.5%</td>
<td align="right">1,092</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.2%</td>
<td align="right">400</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">151</td>
<td align="right">0.1%</td>
<td align="right">151</td>
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
<tr>
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">3,829,274,842</td>
<td align="right">99.6%</td>
<td align="right">3,673,935,094</td>
<td align="right">99.6%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,676</td>
<td align="right">0.4%</td>
<td align="right">14,622,690</td>
<td align="right">0.4%</td>
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
<td align="right">1,637</td>
<td align="right">0.0%</td>
<td align="right">1,637</td>
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
<td align="right">53,017</td>
<td align="right">0.0%</td>
<td align="right">53,017</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">64,431,355</td>
<td align="right">100.0%</td>
<td align="right">64,126,936</td>
<td align="right">100.0%</td>
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
<td align="right">253</td>
<td align="right">0.0%</td>
<td align="right">253</td>
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
<td align="right">2,455</td>
<td align="right">100.0%</td>
<td align="right">2,455</td>
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
<td align="right">593,288,763</td>
<td align="right">82.2%</td>
<td align="right">593,288,756</td>
<td align="right">82.2%</td>
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
<td align="right">128,815,796</td>
<td align="right">17.8%</td>
<td align="right">128,815,796</td>
<td align="right">17.8%</td>
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
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,412</td>
<td align="right">98.1%</td>
<td align="right">34,412</td>
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
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">3,261</td>
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
<td align="right">98,191,564</td>
<td align="right">4.9%</td>
<td align="right">110,439,912</td>
<td align="right">5.5%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">55,963,266</td>
<td align="right">2.8%</td>
<td align="right">57,613,696</td>
<td align="right">2.8%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,868,129,424</td>
<td align="right">92.4%</td>
<td align="right">1,857,864,747</td>
<td align="right">91.7%</td>
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
<td align="right">1,894,361</td>
<td align="right">97.7%</td>
<td align="right">2,125,536</td>
<td align="right">97.9%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,202</td>
<td align="right">2.3%</td>
<td align="right">45,577</td>
<td align="right">2.1%</td>
<td align="right">0.8%</td>
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
<td align="right">22,988</td>
<td align="right">50.9%</td>
<td align="right">23,317</td>
<td align="right">51.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,626</td>
<td align="right">16.9%</td>
<td align="right">7,666</td>
<td align="right">16.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,756</td>
<td align="right">3.9%</td>
<td align="right">1,758</td>
<td align="right">3.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,950</td>
<td align="right">11.0%</td>
<td align="right">4,954</td>
<td align="right">10.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,346</td>
<td align="right">7.4%</td>
<td align="right">3,346</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.6%</td>
<td align="right">1,619</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">913</td>
<td align="right">2.0%</td>
<td align="right">913</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.6%</td>
<td align="right">730</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.5%</td>
<td align="right">699</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">365</td>
<td align="right">0.8%</td>
<td align="right">365</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">100</td>
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
<td align="right">350,321</td>
<td align="right">100.0%</td>
<td align="right">1,194,074</td>
<td align="right">100.0%</td>
<td align="right">240.9%</td>
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
<td align="right">89,063,035</td>
<td align="right">8.8%</td>
<td align="right">91,889,346</td>
<td align="right">9.1%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">919,995,924</td>
<td align="right">91.2%</td>
<td align="right">919,805,723</td>
<td align="right">90.9%</td>
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
<td align="right">32,961</td>
<td align="right">93.8%</td>
<td align="right">33,632</td>
<td align="right">93.9%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,197</td>
<td align="right">6.2%</td>
<td align="right">2,196</td>
<td align="right">6.1%</td>
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
<td align="right">257</td>
<td align="right">0.8%</td>
<td align="right">341</td>
<td align="right">1.0%</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">3,313</td>
<td align="right">10.1%</td>
<td align="right">3,713</td>
<td align="right">11.0%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">214</td>
<td align="right">0.6%</td>
<td align="right">236</td>
<td align="right">0.7%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">8,896</td>
<td align="right">27.0%</td>
<td align="right">9,040</td>
<td align="right">26.9%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,010</td>
<td align="right">9.1%</td>
<td align="right">3,031</td>
<td align="right">9.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,703</td>
<td align="right">50.7%</td>
<td align="right">16,703</td>
<td align="right">49.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">500</td>
<td align="right">1.5%</td>
<td align="right">500</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">68</td>
<td align="right">0.2%</td>
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
<td align="right">32,385,554</td>
<td align="right">0.7%</td>
<td align="right">40,563,800</td>
<td align="right">0.9%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">95,174,400</td>
<td align="right">2.0%</td>
<td align="right">102,001,759</td>
<td align="right">2.2%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,546,520,637</td>
<td align="right">97.3%</td>
<td align="right">4,561,571,824</td>
<td align="right">97.0%</td>
<td align="right">0.3%</td>
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
<td align="right">300,923</td>
<td align="right">100.0%</td>
<td align="right">407,300</td>
<td align="right">100.0%</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">other</td>
<td align="right">10,361</td>
<td align="right">3.4%</td>
<td align="right">23,322</td>
<td align="right">5.7%</td>
<td align="right">125.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">165,114</td>
<td align="right">54.9%</td>
<td align="right">243,628</td>
<td align="right">59.8%</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">80,579</td>
<td align="right">26.8%</td>
<td align="right">93,867</td>
<td align="right">23.0%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,880</td>
<td align="right">1.3%</td>
<td align="right">4,500</td>
<td align="right">1.1%</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,237</td>
<td align="right">2.7%</td>
<td align="right">8,637</td>
<td align="right">2.1%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,991</td>
<td align="right">4.0%</td>
<td align="right">12,342</td>
<td align="right">3.0%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">13,269</td>
<td align="right">4.4%</td>
<td align="right">13,476</td>
<td align="right">3.3%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">5,650</td>
<td align="right">1.9%</td>
<td align="right">5,686</td>
<td align="right">1.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.5%</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">382</td>
<td align="right">0.1%</td>
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
<td align="right">1,427,405</td>
<td align="right">0.1%</td>
<td align="right">1,427,502</td>
<td align="right">0.1%</td>
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
<td align="right">1,233,423,371</td>
<td align="right">99.9%</td>
<td align="right">1,233,495,881</td>
<td align="right">99.9%</td>
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
<td align="right">859</td>
<td align="right">6.9%</td>
<td align="right">857</td>
<td align="right">6.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,643</td>
<td align="right">93.1%</td>
<td align="right">11,643</td>
<td align="right">93.1%</td>
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
<td align="right">632</td>
<td align="right">73.6%</td>
<td align="right">630</td>
<td align="right">73.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.8%</td>
<td align="right">136</td>
<td align="right">15.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">10.6%</td>
<td align="right">91</td>
<td align="right">10.6%</td>
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
<td align="right">802,812,219</td>
<td align="right">1.1%</td>
<td align="right">912,586,211</td>
<td align="right">1.2%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">1,906,829,857</td>
<td align="right">2.5%</td>
<td align="right">1,993,920,398</td>
<td align="right">2.6%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">28,420,107,244</td>
<td align="right">37.4%</td>
<td align="right">28,520,317,252</td>
<td align="right">37.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">44,825,089,912</td>
<td align="right">59.0%</td>
<td align="right">44,921,310,571</td>
<td align="right">58.8%</td>
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
<td align="right">95,174,400</td>
<td align="right">5.0%</td>
<td align="right">102,001,759</td>
<td align="right">5.1%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">325,565,375</td>
<td align="right">17.1%</td>
<td align="right">347,913,633</td>
<td align="right">17.5%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">91,578,713</td>
<td align="right">4.8%</td>
<td align="right">97,193,575</td>
<td align="right">4.9%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">84,463,643</td>
<td align="right">4.4%</td>
<td align="right">89,451,706</td>
<td align="right">4.5%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">450,439,854</td>
<td align="right">23.7%</td>
<td align="right">470,508,215</td>
<td align="right">23.6%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">117,208,472</td>
<td align="right">6.2%</td>
<td align="right">121,966,250</td>
<td align="right">6.1%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">89,063,035</td>
<td align="right">4.7%</td>
<td align="right">91,889,346</td>
<td align="right">4.6%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">401,354,901</td>
<td align="right">21.1%</td>
<td align="right">413,533,878</td>
<td align="right">20.8%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">55,963,266</td>
<td align="right">2.9%</td>
<td align="right">57,613,696</td>
<td align="right">2.9%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,796</td>
<td align="right">6.8%</td>
<td align="right">128,815,796</td>
<td align="right">6.5%</td>
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
<td align="right">62,498,593</td>
<td align="right">7.8%</td>
<td align="right">77,080,746</td>
<td align="right">8.4%</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">127,926,959</td>
<td align="right">15.9%</td>
<td align="right">152,272,680</td>
<td align="right">16.7%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">191,584,021</td>
<td align="right">23.9%</td>
<td align="right">220,381,929</td>
<td align="right">24.1%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">19,047,019</td>
<td align="right">2.4%</td>
<td align="right">21,593,628</td>
<td align="right">2.4%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">79,110,101</td>
<td align="right">9.9%</td>
<td align="right">88,810,647</td>
<td align="right">9.7%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">67,217,529</td>
<td align="right">8.4%</td>
<td align="right">75,385,272</td>
<td align="right">8.3%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">63,803,011</td>
<td align="right">7.9%</td>
<td align="right">62,411,556</td>
<td align="right">6.8%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">19,066,173</td>
<td align="right">2.4%</td>
<td align="right">19,205,698</td>
<td align="right">2.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,872,846</td>
<td align="right">2.6%</td>
<td align="right">20,872,854</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">15,341,776</td>
<td align="right">1.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">18,908,432</td>
<td align="right">2.1%</td>
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
<td align="right">71,803,931</td>
<td align="right">1.1%</td>
<td align="right">71,617,825</td>
<td align="right">1.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,222,577</td>
<td align="right">4.2%</td>
<td align="right">279,743,420</td>
<td align="right">4.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,898,494,703</td>
<td align="right">73.2%</td>
<td align="right">4,895,793,428</td>
<td align="right">73.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,291,862,012</td>
<td align="right">79.1%</td>
<td align="right">5,289,267,175</td>
<td align="right">79.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,118,623,756</td>
<td align="right">16.7%</td>
<td align="right">1,118,707,878</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,120,755,902</td>
<td align="right">16.8%</td>
<td align="right">1,120,840,024</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,791,317,183</td>
<td align="right">26.8%</td>
<td align="right">1,791,386,619</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,791,317,183</td>
<td align="right">26.8%</td>
<td align="right">1,791,386,619</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,561,281</td>
<td align="right">10.0%</td>
<td align="right">670,546,595</td>
<td align="right">10.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,128</td>
<td align="right">0.4%</td>
<td align="right">24,922,365</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,405,566</td>
<td align="right">3.9%</td>
<td align="right">261,406,040</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,250</td>
<td align="right">0.0%</td>
<td align="right">2,128,250</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,139</td>
<td align="right">2.0%</td>
<td align="right">132,513,139</td>
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
<td align="right">6,862,175</td>
<td align="right"></td>
<td align="right">9,198,650</td>
<td align="right"></td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">64,036,902</td>
<td align="right"></td>
<td align="right">67,610,924</td>
<td align="right"></td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">9,079,591,786</td>
<td align="right">5.5%</td>
<td align="right">8,690,890,399</td>
<td align="right">5.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">57,978,062</td>
<td align="right"></td>
<td align="right">59,217,181</td>
<td align="right"></td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">34,034,802,569</td>
<td align="right">20.7%</td>
<td align="right">34,597,594,343</td>
<td align="right">21.0%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">45,768,620,207</td>
<td align="right">22.7%</td>
<td align="right">46,229,184,088</td>
<td align="right">22.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">1,994,306,611</td>
<td align="right"></td>
<td align="right">2,012,693,870</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">42,497,213,913</td>
<td align="right">25.8%</td>
<td align="right">42,820,502,592</td>
<td align="right">26.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">16,065,894,619</td>
<td align="right">8.0%</td>
<td align="right">15,993,916,831</td>
<td align="right">7.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">79,103,995,691</td>
<td align="right">48.0%</td>
<td align="right">78,755,182,469</td>
<td align="right">47.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">84,574,076,834</td>
<td align="right">42.0%</td>
<td align="right">84,323,770,643</td>
<td align="right">41.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,512,181</td>
<td align="right"></td>
<td align="right">179,290,867</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">55,188,646,735</td>
<td align="right">27.4%</td>
<td align="right">55,254,247,421</td>
<td align="right">27.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,596,834</td>
<td align="right">0.4%</td>
<td align="right">71,515,094</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,421,401</td>
<td align="right">0.0%</td>
<td align="right">6,418,841</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,441,490,387</td>
<td align="right">45.7%</td>
<td align="right">8,439,455,474</td>
<td align="right">45.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,441,673,542</td>
<td align="right"></td>
<td align="right">8,439,664,532</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,609,001,333</td>
<td align="right"></td>
<td align="right">10,606,793,052</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,019,653,396</td>
<td align="right">54.3%</td>
<td align="right">10,017,846,722</td>
<td align="right">54.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">9,941,635,161</td>
<td align="right">53.9%</td>
<td align="right">9,939,912,787</td>
<td align="right">53.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,077,337,621</td>
<td align="right"></td>
<td align="right">3,077,079,888</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,139</td>
<td align="right">2.5%</td>
<td align="right">4,444,139</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">476,014</td>
<td align="right">0.3%</td>
<td align="right">476,014</td>
<td align="right">0.3%</td>
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
<td align="right">363,646</td>
<td align="right">105,878,128</td>
<td align="right">16,480,421,033</td>
<td align="right">363,780</td>
<td align="right">105,752,858</td>
<td align="right">16,487,096,425</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,604,239,300</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,604,226,168</td>
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
<td align="right">4,822</td>
<td align="right">0.6%</td>
<td align="right">956</td>
<td align="right">0.2%</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">724</td>
<td align="right">0.1%</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">193,624</td>
<td align="right">24.1%</td>
<td align="right">70,917</td>
<td align="right">14.8%</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">2,696</td>
<td align="right">0.3%</td>
<td align="right">1,282</td>
<td align="right">0.3%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">1,204</td>
<td align="right">0.6%</td>
<td align="right">601</td>
<td align="right">0.8%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">4,782</td>
<td align="right">0.6%</td>
<td align="right">2,804</td>
<td align="right">0.6%</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">804,581</td>
<td align="right"></td>
<td align="right">480,467</td>
<td align="right"></td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">575,823</td>
<td align="right">71.6%</td>
<td align="right">368,100</td>
<td align="right">76.6%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">610,233</td>
<td align="right">75.8%</td>
<td align="right">409,290</td>
<td align="right">85.2%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,496,665,531</td>
<td align="right"></td>
<td align="right">6,702,490,923</td>
<td align="right"></td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">244,749,002,846</td>
<td align="right">3,767.3%</td>
<td align="right">243,997,648,562</td>
<td align="right">3,640.4%</td>
<td align="right">-0.3%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">173,218</td>
<td align="right">89.5%</td>
<td align="right">62,217</td>
<td align="right">87.7%</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">193,624</td>
<td align="right"></td>
<td align="right">70,917</td>
<td align="right"></td>
<td align="right">-63.4%</td>
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
<td align="right">20,518</td>
<td align="right">10.6%</td>
<td align="right">5,476</td>
<td align="right">7.7%</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">35,653</td>
<td align="right">18.4%</td>
<td align="right">9,156</td>
<td align="right">12.9%</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">56,989</td>
<td align="right">29.4%</td>
<td align="right">22,055</td>
<td align="right">31.1%</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">45,049</td>
<td align="right">23.3%</td>
<td align="right">17,138</td>
<td align="right">24.2%</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">24,226</td>
<td align="right">12.5%</td>
<td align="right">10,482</td>
<td align="right">14.8%</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,233</td>
<td align="right">4.8%</td>
<td align="right">5,735</td>
<td align="right">8.1%</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,914</td>
<td align="right">1.0%</td>
<td align="right">795</td>
<td align="right">1.1%</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">90.5%</td>
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
<td align="right">3,710</td>
<td align="right">1.9%</td>
<td align="right">1,032</td>
<td align="right">1.5%</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">29,052</td>
<td align="right">15.0%</td>
<td align="right">9,755</td>
<td align="right">13.8%</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">47,948</td>
<td align="right">24.8%</td>
<td align="right">10,404</td>
<td align="right">14.7%</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">53,418</td>
<td align="right">27.6%</td>
<td align="right">25,953</td>
<td align="right">36.6%</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">27,775</td>
<td align="right">14.3%</td>
<td align="right">10,079</td>
<td align="right">14.2%</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,316</td>
<td align="right">4.3%</td>
<td align="right">3,665</td>
<td align="right">5.2%</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,755</td>
<td align="right">1.4%</td>
<td align="right">1,247</td>
<td align="right">1.8%</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">244</td>
<td align="right">0.1%</td>
<td align="right">82</td>
<td align="right">0.1%</td>
<td align="right">-66.4%</td>
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
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,225,456</td>
<td align="right">42,572</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">40,439,608</td>
<td align="right">78,199,134</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">41,718,835</td>
<td align="right">79,472,418</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">21,428,471</td>
<td align="right">40,304,301</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">731,418</td>
<td align="right">98,482</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">9,812,435</td>
<td align="right">1,575,268</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">9,866,498</td>
<td align="right">1,594,929</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">386,343</td>
<td align="right">123,165</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">1,551,675</td>
<td align="right">558,669</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">361,293</td>
<td align="right">181,915</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">7,554,146</td>
<td align="right">4,540,421</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,332,961</td>
<td align="right">2,615,370</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">4,872,444</td>
<td align="right">3,202,666</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">6,573,025</td>
<td align="right">4,452,269</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,290,652</td>
<td align="right">3,093,927</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">14,279,535</td>
<td align="right">10,323,143</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">1,259,041</td>
<td align="right">981,067</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">205,232,010</td>
<td align="right">161,727,884</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">186,177,558</td>
<td align="right">221,412,371</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">503,385,989</td>
<td align="right">416,412,072</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">35,914,178</td>
<td align="right">29,808,331</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">35,914,178</td>
<td align="right">29,808,331</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">499,250,057</td>
<td align="right">420,472,319</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">496,036,037</td>
<td align="right">417,811,079</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,605,734</td>
<td align="right">90,932,472</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">138,119,112</td>
<td align="right">116,749,062</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">256,138,382</td>
<td align="right">293,927,296</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">256,942,126</td>
<td align="right">294,145,246</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">8,236,799</td>
<td align="right">7,081,130</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">272,748,251</td>
<td align="right">309,229,360</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">7,091,909</td>
<td align="right">6,154,664</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">442,620,768</td>
<td align="right">500,430,593</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">253,201,085</td>
<td align="right">285,362,726</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">194,985,074</td>
<td align="right">172,479,559</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">105,111,233</td>
<td align="right">94,220,270</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">22,819,423</td>
<td align="right">20,513,017</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">313,350,114</td>
<td align="right">282,295,250</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">733,133,054</td>
<td align="right">802,300,915</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">82,742,916</td>
<td align="right">75,384,554</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">32,231,384</td>
<td align="right">29,440,962</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">144,873,410</td>
<td align="right">132,467,774</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">584,077,054</td>
<td align="right">633,301,054</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,085,763,800</td>
<td align="right">995,641,368</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">585,702,613</td>
<td align="right">537,667,345</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">32,896,364</td>
<td align="right">30,204,995</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">449,061,736</td>
<td align="right">412,910,765</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">62,091,483</td>
<td align="right">57,254,778</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">336,839,846</td>
<td align="right">311,469,596</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">260,011,580</td>
<td align="right">240,534,097</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">94,011,731</td>
<td align="right">86,986,662</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">329,505,258</td>
<td align="right">305,241,993</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">2,142,574</td>
<td align="right">1,989,784</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">70,978,944</td>
<td align="right">65,982,402</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">222,919,823</td>
<td align="right">207,820,136</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">783,924,172</td>
<td align="right">835,103,573</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,814,118,834</td>
<td align="right">1,929,370,541</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">89,779,756</td>
<td align="right">84,164,894</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">19,210,312</td>
<td align="right">18,019,991</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">27,612,207</td>
<td align="right">25,928,061</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">55,427,000</td>
<td align="right">52,060,700</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">403,421,602</td>
<td align="right">379,037,366</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,727,344,198</td>
<td align="right">2,883,254,896</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">719,242,915</td>
<td align="right">678,653,735</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">471,553,746</td>
<td align="right">497,879,289</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">40,781,911</td>
<td align="right">38,523,643</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">53,055,820</td>
<td align="right">50,239,680</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">53,055,820</td>
<td align="right">50,239,680</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">90,652,827</td>
<td align="right">85,877,022</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">28,504,171</td>
<td align="right">27,019,861</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,971,905</td>
<td align="right">6,628,879</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">59,170,474</td>
<td align="right">56,407,826</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">63,728,097</td>
<td align="right">60,825,168</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">23,319,091</td>
<td align="right">22,290,905</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">754,817,813</td>
<td align="right">721,561,904</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">108,208,145</td>
<td align="right">103,484,596</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">60,742,810</td>
<td align="right">58,103,990</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,664,035,315</td>
<td align="right">2,551,595,094</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">71,986,631</td>
<td align="right">68,968,120</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">5,636,612,564</td>
<td align="right">5,872,353,659</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,601,613,635</td>
<td align="right">2,494,142,152</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">723,488,592</td>
<td align="right">693,767,201</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">753,842,050</td>
<td align="right">784,389,701</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">35,225,827</td>
<td align="right">33,816,322</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">35,225,827</td>
<td align="right">33,816,322</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">605,515,001</td>
<td align="right">581,371,900</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">50,255,579</td>
<td align="right">48,289,581</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,402,666,014</td>
<td align="right">5,208,316,384</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">118,648,513</td>
<td align="right">114,407,438</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">844,525,437</td>
<td align="right">814,504,285</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">750,379,958</td>
<td align="right">776,811,231</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">868,152,386</td>
<td align="right">897,170,862</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">324,457,106</td>
<td align="right">313,734,092</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">179,739,350</td>
<td align="right">173,804,365</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">62,011,624</td>
<td align="right">59,982,881</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">156,864,955</td>
<td align="right">151,815,234</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,496,665,531</td>
<td align="right">6,702,490,923</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">124,298,378</td>
<td align="right">128,190,835</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,090,112,762</td>
<td align="right">5,901,183,650</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">781,039,420</td>
<td align="right">757,478,864</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">77,464,587</td>
<td align="right">75,166,451</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">147,828,763</td>
<td align="right">152,085,924</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">44,967,379</td>
<td align="right">43,714,033</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">72,239,241</td>
<td align="right">70,275,000</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">210,318,343</td>
<td align="right">216,025,228</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,329,068,588</td>
<td align="right">3,238,774,158</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">14,268,489</td>
<td align="right">14,651,912</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">102,316,135</td>
<td align="right">99,678,343</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">102,316,135</td>
<td align="right">99,678,343</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">8,921,856,802</td>
<td align="right">9,146,788,583</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,463,254,549</td>
<td align="right">3,549,913,145</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">523,911,014</td>
<td align="right">511,107,163</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,705,708,034</td>
<td align="right">2,770,558,910</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,520,064,812</td>
<td align="right">1,556,244,735</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,133,757,449</td>
<td align="right">4,230,171,931</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,871,719,695</td>
<td align="right">2,805,278,729</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">411,378,295</td>
<td align="right">401,939,495</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">188,273,097</td>
<td align="right">183,982,655</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,027,977,240</td>
<td align="right">1,004,757,111</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,822,920,407</td>
<td align="right">1,781,878,980</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">202,177,242</td>
<td align="right">197,664,257</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">509,031,892</td>
<td align="right">497,817,828</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">662,583,665</td>
<td align="right">677,032,060</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">507,842,419</td>
<td align="right">496,768,448</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">173,913,144</td>
<td align="right">170,197,786</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,359,133,189</td>
<td align="right">1,387,929,970</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,045,424,102</td>
<td align="right">4,128,131,685</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">870,472,938</td>
<td align="right">853,789,009</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,960,968,134</td>
<td align="right">5,848,118,298</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">803,532,047</td>
<td align="right">788,588,026</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,882,505,332</td>
<td align="right">1,848,154,700</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">164,255,825</td>
<td align="right">161,282,389</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,583,699,970</td>
<td align="right">4,666,650,571</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,721,588,396</td>
<td align="right">1,692,193,313</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,794,977,615</td>
<td align="right">1,764,382,000</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">72,491,510</td>
<td align="right">71,268,681</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">72,491,210</td>
<td align="right">71,268,681</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">118,922,655</td>
<td align="right">116,971,994</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,036,885,405</td>
<td align="right">1,053,703,513</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,961,453,638</td>
<td align="right">1,931,120,978</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">219,584,669</td>
<td align="right">216,364,877</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,345,829,048</td>
<td align="right">2,312,064,493</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,900,567,093</td>
<td align="right">1,873,690,612</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,548,017</td>
<td align="right">24,205,006</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,129,644,164</td>
<td align="right">2,100,451,947</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,203,829,124</td>
<td align="right">1,187,339,544</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,723,892,811</td>
<td align="right">1,701,396,423</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">250,486,815</td>
<td align="right">247,365,339</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">433,014,827</td>
<td align="right">427,671,988</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">564,223,566</td>
<td align="right">557,637,286</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">26,056,829</td>
<td align="right">25,765,231</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">26,056,829</td>
<td align="right">25,765,231</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,102,518,629</td>
<td align="right">2,079,501,118</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,545,079,330</td>
<td align="right">2,517,346,721</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,490,615,359</td>
<td align="right">1,474,833,425</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,046,281,853</td>
<td align="right">1,036,226,559</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,402,791,327</td>
<td align="right">1,415,892,313</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">20,572,909,933</td>
<td align="right">20,380,871,499</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,652,453</td>
<td align="right">6,591,433</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,232,101,684</td>
<td align="right">1,221,021,084</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,398,219,227</td>
<td align="right">9,480,940,749</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,940,594,645</td>
<td align="right">1,957,563,068</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">779,992,036</td>
<td align="right">773,226,791</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,063,058,871</td>
<td align="right">3,036,525,739</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">31,489,880</td>
<td align="right">31,220,720</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">71,907,700</td>
<td align="right">71,299,184</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">79,287,400</td>
<td align="right">78,651,966</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,425,191,271</td>
<td align="right">2,444,297,660</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">728,061,982</td>
<td align="right">722,570,960</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,306,571,126</td>
<td align="right">4,274,173,141</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">112,336,173</td>
<td align="right">111,492,420</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,950,346,592</td>
<td align="right">2,928,761,419</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">93,869,527</td>
<td align="right">94,545,647</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,503,618,319</td>
<td align="right">1,493,042,789</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">124,468,460</td>
<td align="right">123,597,560</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,094,522,931</td>
<td align="right">1,086,992,029</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">602,931,279</td>
<td align="right">598,921,664</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,952,513,982</td>
<td align="right">1,940,446,267</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,372,405,314</td>
<td align="right">1,364,257,383</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">518,526,656</td>
<td align="right">515,778,918</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,223,355,765</td>
<td align="right">3,206,418,096</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">40,593,823</td>
<td align="right">40,381,363</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">40,593,203</td>
<td align="right">40,380,943</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">393,736,873</td>
<td align="right">391,683,566</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,374,942,358</td>
<td align="right">8,331,357,581</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">97,685,650</td>
<td align="right">97,185,252</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">581,411,729</td>
<td align="right">578,472,461</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">547,968,901</td>
<td align="right">545,205,599</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">581,392,529</td>
<td align="right">578,472,461</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">388,790,286</td>
<td align="right">386,839,379</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,245,354,468</td>
<td align="right">1,239,130,726</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">172,996,685</td>
<td align="right">172,166,272</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,565,979</td>
<td align="right">60,278,080</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">611,816,883</td>
<td align="right">608,990,912</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">17,082,915,558</td>
<td align="right">17,008,438,122</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,323,833,423</td>
<td align="right">1,318,869,334</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,322,873,460</td>
<td align="right">1,317,963,046</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">716,583,530</td>
<td align="right">714,270,689</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">854,228,408</td>
<td align="right">851,688,574</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">3,903,120</td>
<td align="right">3,891,960</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">3,903,120</td>
<td align="right">3,891,960</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,824,790,561</td>
<td align="right">3,814,740,221</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">994,348,398</td>
<td align="right">991,837,750</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,353,063,689</td>
<td align="right">1,349,716,284</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">765,830</td>
<td align="right">764,033</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">765,830</td>
<td align="right">764,033</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">31,562,500</td>
<td align="right">31,490,980</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">270,035,925</td>
<td align="right">269,489,737</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">46,022,701</td>
<td align="right">46,104,892</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,989,149,723</td>
<td align="right">1,985,850,868</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,130,180</td>
<td align="right">47,062,820</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">168,286,730</td>
<td align="right">168,074,204</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,457,206</td>
<td align="right">40,422,504</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">3,844,140</td>
<td align="right">3,840,960</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,089,991,899</td>
<td align="right">5,088,130,941</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">468,818,138</td>
<td align="right">468,665,076</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,604,067,353</td>
<td align="right">4,603,798,148</td>
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
<td align="right">1,458,214</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">587,136</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">325,023</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">45,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">19,378</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">9,373</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">2,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">1,353</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">666</td>
<td align="right"></td>
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
<td align="right">21,273</td>
<td align="right">7,366</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">35,953</td>
<td align="right">24,585</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">25,869</td>
<td align="right">23,510</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">100</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">21</td>
<td align="right"></td>
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
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,629</td>
<td align="right">22,629</td>
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
<td align="right">31</td>
<td align="right">31</td>
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
<td align="right">38</td>
<td align="right">38</td>
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
<td align="right">160</td>
<td align="right">160</td>
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
<td align="right">160</td>
<td align="right">160</td>
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
<td align="right">2,476</td>
<td align="right">2,476</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-22
