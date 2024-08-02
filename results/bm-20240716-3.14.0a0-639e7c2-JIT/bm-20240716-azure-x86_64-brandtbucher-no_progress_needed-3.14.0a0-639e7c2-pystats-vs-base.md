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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">490,920</td>
<td align="right">8,111,820</td>
<td align="right">1,552.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">54,255,790</td>
<td align="right">192,458,090</td>
<td align="right">254.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">219,477</td>
<td align="right">699,590</td>
<td align="right">218.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,366,909</td>
<td align="right">4,441,705</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">913,680,480</td>
<td align="right">1,583,943,748</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">4,628,789</td>
<td align="right">7,868,687</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">23,976,385</td>
<td align="right">40,350,421</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">108,591,652</td>
<td align="right">165,309,202</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">378,503,832</td>
<td align="right">575,284,845</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,804,795</td>
<td align="right">107,215,539</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">20,348,254</td>
<td align="right">29,891,282</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68,000,998</td>
<td align="right">98,843,469</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">42,434,520</td>
<td align="right">61,184,180</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">211,206,992</td>
<td align="right">296,587,621</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,812,291</td>
<td align="right">56,393,815</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">66,953,719</td>
<td align="right">91,618,532</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">202,854,942</td>
<td align="right">273,288,255</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">146,457,069</td>
<td align="right">96,211,286</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">295,222,030</td>
<td align="right">392,868,496</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">404,588,786</td>
<td align="right">537,681,751</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">679,767,357</td>
<td align="right">892,214,116</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">328,735,636</td>
<td align="right">420,027,892</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,867,740</td>
<td align="right">2,881,956</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">791,281,595</td>
<td align="right">990,542,538</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,366</td>
<td align="right">236,437,592</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">46,620</td>
<td align="right">57,780</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">385,091,916</td>
<td align="right">468,172,558</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">194,496,515</td>
<td align="right">230,345,181</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,378,557,435</td>
<td align="right">3,588,780,571</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,155,812</td>
<td align="right">270,490,816</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,297,579</td>
<td align="right">250,185,047</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,453,176,338</td>
<td align="right">2,804,514,880</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,490,732,158</td>
<td align="right">6,268,095,818</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,563,374,237</td>
<td align="right">1,776,370,406</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,873,383</td>
<td align="right">71,484,041</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">276,486,120</td>
<td align="right">310,671,844</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,017,137,693</td>
<td align="right">1,141,559,946</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">386,363,811</td>
<td align="right">432,039,517</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">36,374,599</td>
<td align="right">40,661,509</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">283,352,584</td>
<td align="right">316,593,652</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,585,653,531</td>
<td align="right">24,049,331,959</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,100,437,465</td>
<td align="right">4,566,707,343</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,131,550,367</td>
<td align="right">1,258,677,177</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">273,730,979</td>
<td align="right">303,645,325</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">739,551,750</td>
<td align="right">819,805,128</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">140,544,033</td>
<td align="right">155,771,575</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,808,501</td>
<td align="right">35,017,741</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">454,619,156</td>
<td align="right">410,665,812</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">366,811,548</td>
<td align="right">399,747,242</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">409,185,488</td>
<td align="right">444,773,322</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">666,613,286</td>
<td align="right">723,613,786</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,223,700,834</td>
<td align="right">6,743,722,112</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">76,340,987</td>
<td align="right">82,620,759</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,411,766,932</td>
<td align="right">1,299,252,573</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">87,789,412</td>
<td align="right">94,691,392</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">299,193,840</td>
<td align="right">321,800,453</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,110,538,416</td>
<td align="right">1,186,340,287</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">332,007,056</td>
<td align="right">354,643,981</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">421,590,041</td>
<td align="right">449,608,786</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">114,690,192</td>
<td align="right">122,068,885</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,387,265</td>
<td align="right">9,740,720</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">119,399,217</td>
<td align="right">126,755,746</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,644,656,244</td>
<td align="right">2,482,090,950</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,399,990,590</td>
<td align="right">2,260,289,163</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,608,679</td>
<td align="right">107,507,940</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,667,039,857</td>
<td align="right">5,991,269,601</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">196,716,761</td>
<td align="right">206,891,134</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">773,917,155</td>
<td align="right">812,315,169</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">21,172,873</td>
<td align="right">22,223,058</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">386,961,780</td>
<td align="right">406,148,918</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">804,758,147</td>
<td align="right">843,606,956</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">231,216,019</td>
<td align="right">220,544,753</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">942,148,390</td>
<td align="right">984,892,637</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,820,186,184</td>
<td align="right">2,942,543,542</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">556,992,038</td>
<td align="right">581,009,934</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,836,694</td>
<td align="right">55,819,704</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">137,977,958</td>
<td align="right">133,864,737</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">215,264,001</td>
<td align="right">220,793,770</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">205,869,852</td>
<td align="right">210,894,563</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">431,639,002</td>
<td align="right">421,363,457</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,411,522</td>
<td align="right">4,513,444</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">166,855,165</td>
<td align="right">170,540,973</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,991,169,315</td>
<td align="right">5,863,706,753</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">318,038,422</td>
<td align="right">324,506,969</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,877,530</td>
<td align="right">10,071,349</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,871,676,838</td>
<td align="right">1,835,177,072</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,255,226,279</td>
<td align="right">1,231,708,568</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">349,319,197</td>
<td align="right">343,127,103</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,357,271</td>
<td align="right">8,497,556</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,461,660</td>
<td align="right">7,584,820</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,176,177</td>
<td align="right">81,833,041</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">200,133,632</td>
<td align="right">203,258,074</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,222,905,973</td>
<td align="right">4,158,941,851</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">199,228,102</td>
<td align="right">202,168,169</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">678,041,624</td>
<td align="right">687,324,036</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">829,582,143</td>
<td align="right">840,401,700</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,242,304</td>
<td align="right">61,440,580</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,569,302</td>
<td align="right">156,532,910</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">59,677,580</td>
<td align="right">60,326,780</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,802,642</td>
<td align="right">123,525,053</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">639,900,244</td>
<td align="right">646,430,334</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">481,396,433</td>
<td align="right">486,190,894</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">486,474,572</td>
<td align="right">491,204,994</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">79,275,288</td>
<td align="right">79,996,726</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,290,424,402</td>
<td align="right">1,300,881,111</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">173,188,546</td>
<td align="right">174,422,980</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,101,044</td>
<td align="right">47,779,175</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">56,523,748</td>
<td align="right">56,174,740</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">901,649,056</td>
<td align="right">896,199,773</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,526,817,955</td>
<td align="right">3,547,480,554</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,106,575,501</td>
<td align="right">4,085,270,658</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">81,682,651</td>
<td align="right">82,100,996</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,211,587</td>
<td align="right">92,595,663</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,612,160</td>
<td align="right">46,783,880</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">100,339,393</td>
<td align="right">100,696,535</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,224,388</td>
<td align="right">1,050,823,482</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">108,507,142</td>
<td align="right">108,877,204</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">30,799,981</td>
<td align="right">30,704,597</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,606,880</td>
<td align="right">136,213,920</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,165,100</td>
<td align="right">91,941,340</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,446,900</td>
<td align="right">94,223,140</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">49,265,983</td>
<td align="right">49,377,954</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,914,450</td>
<td align="right">150,195,075</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,714,481</td>
<td align="right">71,832,521</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">164,202,504</td>
<td align="right">163,948,606</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,297,068,452</td>
<td align="right">3,292,703,201</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">228,046,807</td>
<td align="right">227,791,753</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,911,234</td>
<td align="right">147,055,679</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,471,098</td>
<td align="right">17,457,402</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,603,446,124</td>
<td align="right">1,602,310,671</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,371,139,191</td>
<td align="right">1,370,188,864</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,763,188</td>
<td align="right">66,805,148</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">59,194,221</td>
<td align="right">59,161,222</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,389,362</td>
<td align="right">143,312,202</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">48,283,030</td>
<td align="right">48,307,597</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">485,045,636</td>
<td align="right">484,822,063</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,923,813</td>
<td align="right">403,072,284</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,640,441</td>
<td align="right">3,641,285</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,451,640</td>
<td align="right">82,460,615</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,808,260</td>
<td align="right">1,808,072</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,885</td>
<td align="right">14,884</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,961,794</td>
<td align="right">10,961,113</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,874,075</td>
<td align="right">1,873,970</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,824</td>
<td align="right">687,792</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">222,894</td>
<td align="right">222,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,694,682</td>
<td align="right">20,695,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,153,010</td>
<td align="right">21,153,878</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,160,770</td>
<td align="right">21,161,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,641,558</td>
<td align="right">225,648,082</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,657,652</td>
<td align="right">9,657,837</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,142,245</td>
<td align="right">91,143,741</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,235,850</td>
<td align="right">9,235,968</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,265,582</td>
<td align="right">274,264,873</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,344,774</td>
<td align="right">20,344,733</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,907,417</td>
<td align="right">555,908,514</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,950,756</td>
<td align="right">5,950,752</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,338,350</td>
<td align="right">233,338,343</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,319,338</td>
<td align="right">173,319,342</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,024,177</td>
<td align="right">402,024,183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,220,555</td>
<td align="right">786,220,565</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">12,102,480</td>
<td align="right">12,102,480</td>
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
<td align="right">3,465,240</td>
<td align="right">3,465,240</td>
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
<td align="right">657,740</td>
<td align="right">657,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,420</td>
<td align="right">173,420</td>
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
<td align="right">142,240</td>
<td align="right">142,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,640</td>
<td align="right">91,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">89,960</td>
<td align="right">89,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">28,760</td>
<td align="right">28,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,180</td>
<td align="right">27,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,340</td>
<td align="right">21,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">1,120</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,040</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">436,966,137</td>
<td align="right">4.4%</td>
<td align="right">472,615,354</td>
<td align="right">4.8%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,500,920</td>
<td align="right">0.3%</td>
<td align="right">29,578,200</td>
<td align="right">0.3%</td>
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
<td align="right">9,428,333,607</td>
<td align="right">95.6%</td>
<td align="right">9,430,645,009</td>
<td align="right">95.2%</td>
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
<td align="right">1,122,648</td>
<td align="right">65.3%</td>
<td align="right">1,137,092</td>
<td align="right">65.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">597,623</td>
<td align="right">34.7%</td>
<td align="right">599,076</td>
<td align="right">34.5%</td>
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
<td align="left">lshift</td>
<td align="right">5,026</td>
<td align="right">0.4%</td>
<td align="right">7,264</td>
<td align="right">0.6%</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">22,733</td>
<td align="right">2.0%</td>
<td align="right">27,715</td>
<td align="right">2.4%</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,608</td>
<td align="right">0.8%</td>
<td align="right">9,205</td>
<td align="right">0.8%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,884</td>
<td align="right">0.8%</td>
<td align="right">8,424</td>
<td align="right">0.7%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,324</td>
<td align="right">4.3%</td>
<td align="right">50,798</td>
<td align="right">4.5%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">13,649</td>
<td align="right">1.2%</td>
<td align="right">14,310</td>
<td align="right">1.3%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">48,666</td>
<td align="right">4.3%</td>
<td align="right">50,980</td>
<td align="right">4.5%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,318</td>
<td align="right">2.8%</td>
<td align="right">32,510</td>
<td align="right">2.9%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,356</td>
<td align="right">2.9%</td>
<td align="right">31,256</td>
<td align="right">2.7%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">0.9%</td>
<td align="right">10,820</td>
<td align="right">1.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,405</td>
<td align="right">7.3%</td>
<td align="right">83,747</td>
<td align="right">7.4%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,720</td>
<td align="right">0.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,915</td>
<td align="right">0.2%</td>
<td align="right">1,919</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,608</td>
<td align="right">69.6%</td>
<td align="right">781,608</td>
<td align="right">68.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,504</td>
<td align="right">0.9%</td>
<td align="right">10,504</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,548</td>
<td align="right">0.5%</td>
<td align="right">5,548</td>
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
<td align="left">and different types</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
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
<td align="right">743,940,157</td>
<td align="right">10.8%</td>
<td align="right">824,182,176</td>
<td align="right">11.6%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,149,769,667</td>
<td align="right">89.2%</td>
<td align="right">6,274,049,361</td>
<td align="right">88.4%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,810,145</td>
<td align="right">0.1%</td>
<td align="right">4,819,751</td>
<td align="right">0.1%</td>
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
<td align="right">240,177</td>
<td align="right">56.9%</td>
<td align="right">261,003</td>
<td align="right">59.0%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,561</td>
<td align="right">43.1%</td>
<td align="right">181,700</td>
<td align="right">41.0%</td>
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
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">6.7%</td>
<td align="right">36,080</td>
<td align="right">13.8%</td>
<td align="right">122.7%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">800</td>
<td align="right">0.3%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
<td align="right">1,120</td>
<td align="right">0.4%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.2%</td>
<td align="right">5,440</td>
<td align="right">2.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">55,960</td>
<td align="right">23.3%</td>
<td align="right">55,140</td>
<td align="right">21.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">110,415</td>
<td align="right">46.0%</td>
<td align="right">111,959</td>
<td align="right">42.9%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,498</td>
<td align="right">12.7%</td>
<td align="right">30,740</td>
<td align="right">11.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,500</td>
<td align="right">8.1%</td>
<td align="right">19,500</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
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
<td align="right">181,481,361</td>
<td align="right">1.3%</td>
<td align="right">151,904,129</td>
<td align="right">1.1%</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">662,414,532</td>
<td align="right">4.6%</td>
<td align="right">633,171,982</td>
<td align="right">4.4%</td>
<td align="right">-4.4%</td>
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
<td align="right">29,280</td>
<td align="right">0.0%</td>
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
<td align="right">13,665,382,100</td>
<td align="right">95.3%</td>
<td align="right">13,667,024,427</td>
<td align="right">95.5%</td>
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
<td align="right">3,947,065</td>
<td align="right">96.0%</td>
<td align="right">3,388,910</td>
<td align="right">95.3%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">165,400</td>
<td align="right">4.0%</td>
<td align="right">165,300</td>
<td align="right">4.7%</td>
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
<td align="right">155,900</td>
<td align="right">94.3%</td>
<td align="right">155,800</td>
<td align="right">94.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">9,160</td>
<td align="right">5.5%</td>
<td align="right">9,160</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,920</td>
<td align="right">1.8%</td>
<td align="right">2,920</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">1,940</td>
<td align="right">1.2%</td>
<td align="right">1,940</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">940</td>
<td align="right">0.6%</td>
<td align="right">940</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
<td align="right">0.2%</td>
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
<td align="right">1,070,787</td>
<td align="right">0.0%</td>
<td align="right">1,333,908</td>
<td align="right">0.0%</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">101,184,383</td>
<td align="right">1.6%</td>
<td align="right">101,787,514</td>
<td align="right">1.6%</td>
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
<td align="right">6,122,623,431</td>
<td align="right">98.4%</td>
<td align="right">6,106,713,471</td>
<td align="right">98.4%</td>
<td align="right">-0.3%</td>
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
<td align="right">149,614</td>
<td align="right">66.3%</td>
<td align="right">161,752</td>
<td align="right">66.6%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">76,183</td>
<td align="right">33.7%</td>
<td align="right">81,177</td>
<td align="right">33.4%</td>
<td align="right">6.6%</td>
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
<td align="right">27,068</td>
<td align="right">18.1%</td>
<td align="right">33,279</td>
<td align="right">20.6%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">840</td>
<td align="right">0.5%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">42,467</td>
<td align="right">28.4%</td>
<td align="right">47,245</td>
<td align="right">29.2%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,425</td>
<td align="right">1.0%</td>
<td align="right">1,541</td>
<td align="right">1.0%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.4%</td>
<td align="right">540</td>
<td align="right">0.3%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,699</td>
<td align="right">11.2%</td>
<td align="right">17,347</td>
<td align="right">10.7%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,000</td>
<td align="right">12.7%</td>
<td align="right">19,360</td>
<td align="right">12.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,620</td>
<td align="right">1.1%</td>
<td align="right">1,640</td>
<td align="right">1.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,361</td>
<td align="right">9.6%</td>
<td align="right">14,484</td>
<td align="right">9.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,174</td>
<td align="right">8.1%</td>
<td align="right">12,216</td>
<td align="right">7.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">10,680</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,580</td>
<td align="right">1.7%</td>
<td align="right">2,580</td>
<td align="right">1.6%</td>
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
<td align="right">208,241,255</td>
<td align="right">7.7%</td>
<td align="right">213,264,128</td>
<td align="right">7.9%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,489,643,392</td>
<td align="right">92.3%</td>
<td align="right">2,485,363,462</td>
<td align="right">92.1%</td>
<td align="right">-0.2%</td>
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
<td align="right">0.1%</td>
<td align="right">2,546,240</td>
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
<td align="right">113,718</td>
<td align="right">65.0%</td>
<td align="right">115,555</td>
<td align="right">65.4%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,119</td>
<td align="right">35.0%</td>
<td align="right">61,120</td>
<td align="right">34.6%</td>
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
<td align="right">56,540</td>
<td align="right">49.7%</td>
<td align="right">58,320</td>
<td align="right">50.5%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">13,940</td>
<td align="right">12.3%</td>
<td align="right">14,300</td>
<td align="right">12.4%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,521</td>
<td align="right">24.2%</td>
<td align="right">27,262</td>
<td align="right">23.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,717</td>
<td align="right">13.8%</td>
<td align="right">15,673</td>
<td align="right">13.6%</td>
<td align="right">-0.3%</td>
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
<td align="right">2,600,087</td>
<td align="right">0.3%</td>
<td align="right">6,746,020</td>
<td align="right">0.6%</td>
<td align="right">159.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">548,215,226</td>
<td align="right">53.1%</td>
<td align="right">568,117,292</td>
<td align="right">53.5%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">483,702,471</td>
<td align="right">46.9%</td>
<td align="right">492,561,163</td>
<td align="right">46.4%</td>
<td align="right">1.8%</td>
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
<td align="right">96,797</td>
<td align="right">32.9%</td>
<td align="right">174,975</td>
<td align="right">46.6%</td>
<td align="right">80.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">197,252</td>
<td align="right">67.1%</td>
<td align="right">200,776</td>
<td align="right">53.4%</td>
<td align="right">1.8%</td>
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
<td align="left">ascii string</td>
<td align="right">1,720</td>
<td align="right">0.9%</td>
<td align="right">2,440</td>
<td align="right">1.2%</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,840</td>
<td align="right">1.9%</td>
<td align="right">4,520</td>
<td align="right">2.3%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,298</td>
<td align="right">5.2%</td>
<td align="right">11,351</td>
<td align="right">5.7%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">37,386</td>
<td align="right">19.0%</td>
<td align="right">38,342</td>
<td align="right">19.1%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,060</td>
<td align="right">2.1%</td>
<td align="right">3,960</td>
<td align="right">2.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,289</td>
<td align="right">5.7%</td>
<td align="right">11,484</td>
<td align="right">5.7%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,100</td>
<td align="right">2.6%</td>
<td align="right">5,120</td>
<td align="right">2.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,960</td>
<td align="right">53.2%</td>
<td align="right">104,960</td>
<td align="right">52.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,480</td>
<td align="right">3.3%</td>
<td align="right">6,480</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,300</td>
<td align="right">3.2%</td>
<td align="right">6,300</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,220</td>
<td align="right">2.1%</td>
<td align="right">4,220</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">619</td>
<td align="right">0.3%</td>
<td align="right">619</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">220</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">420,448,428</td>
<td align="right">2.4%</td>
<td align="right">367,768,242</td>
<td align="right">2.1%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,521,471,766</td>
<td align="right">8.6%</td>
<td align="right">1,545,561,842</td>
<td align="right">8.7%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,088,898,012</td>
<td align="right">91.3%</td>
<td align="right">16,272,454,398</td>
<td align="right">91.3%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">263,380</td>
<td align="right">0.0%</td>
<td align="right">263,380</td>
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
<td align="right">8,543,205</td>
<td align="right">89.8%</td>
<td align="right">7,549,134</td>
<td align="right">88.3%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">971,873</td>
<td align="right">10.2%</td>
<td align="right">997,553</td>
<td align="right">11.7%</td>
<td align="right">2.6%</td>
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
<td align="right">14,400</td>
<td align="right">1.5%</td>
<td align="right">17,820</td>
<td align="right">1.8%</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">164,770</td>
<td align="right">17.0%</td>
<td align="right">176,378</td>
<td align="right">17.7%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,300</td>
<td align="right">1.6%</td>
<td align="right">15,780</td>
<td align="right">1.6%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">75,346</td>
<td align="right">7.8%</td>
<td align="right">77,627</td>
<td align="right">7.8%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">102,053</td>
<td align="right">10.5%</td>
<td align="right">104,071</td>
<td align="right">10.4%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">263,056</td>
<td align="right">27.1%</td>
<td align="right">267,490</td>
<td align="right">26.8%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">156,174</td>
<td align="right">16.1%</td>
<td align="right">158,642</td>
<td align="right">15.9%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,840</td>
<td align="right">0.3%</td>
<td align="right">2,880</td>
<td align="right">0.3%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,601</td>
<td align="right">9.0%</td>
<td align="right">86,697</td>
<td align="right">8.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,340</td>
<td align="right">2.1%</td>
<td align="right">20,220</td>
<td align="right">2.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,751</td>
<td align="right">1.8%</td>
<td align="right">17,714</td>
<td align="right">1.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,562</td>
<td align="right">0.6%</td>
<td align="right">5,554</td>
<td align="right">0.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,880</td>
<td align="right">2.8%</td>
<td align="right">26,880</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.3%</td>
<td align="right">12,240</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,380</td>
<td align="right">0.6%</td>
<td align="right">5,380</td>
<td align="right">0.5%</td>
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
<td align="left">out of versions</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">340</td>
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
<td align="right">5,851,573,990</td>
<td align="right">99.6%</td>
<td align="right">6,248,527,577</td>
<td align="right">99.7%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">437,526</td>
<td align="right">0.0%</td>
<td align="right">438,664</td>
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
<td align="right">20,319,658</td>
<td align="right">0.3%</td>
<td align="right">20,320,748</td>
<td align="right">0.3%</td>
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
<td align="right">11,640</td>
<td align="right">0.0%</td>
<td align="right">11,640</td>
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
<td align="right">462,642</td>
<td align="right">100.0%</td>
<td align="right">462,649</td>
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
<td align="right">83,711,563</td>
<td align="right">100.0%</td>
<td align="right">83,674,653</td>
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
<td align="right">7,465</td>
<td align="right">0.0%</td>
<td align="right">7,464</td>
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
<td align="right">7,420</td>
<td align="right">100.0%</td>
<td align="right">7,420</td>
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
<td align="right">173,284,918</td>
<td align="right">18.1%</td>
<td align="right">173,284,922</td>
<td align="right">18.1%</td>
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
<td align="right">786,189,895</td>
<td align="right">81.9%</td>
<td align="right">786,189,905</td>
<td align="right">81.9%</td>
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
<td align="right">5,460</td>
<td align="right">8.4%</td>
<td align="right">5,460</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,620</td>
<td align="right">91.6%</td>
<td align="right">59,620</td>
<td align="right">91.6%</td>
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
<td align="right">9,980</td>
<td align="right">16.7%</td>
<td align="right">9,980</td>
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
<td align="right">139,476,669</td>
<td align="right">4.8%</td>
<td align="right">125,697,748</td>
<td align="right">4.3%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">190,494,111</td>
<td align="right">6.5%</td>
<td align="right">178,957,655</td>
<td align="right">6.1%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,724,882,766</td>
<td align="right">93.4%</td>
<td align="right">2,735,018,309</td>
<td align="right">93.8%</td>
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
<td align="left">Success</td>
<td align="right">2,727,284</td>
<td align="right">96.7%</td>
<td align="right">2,467,209</td>
<td align="right">96.4%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">91,968</td>
<td align="right">3.3%</td>
<td align="right">92,588</td>
<td align="right">3.6%</td>
<td align="right">0.7%</td>
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
<td align="right">2,860</td>
<td align="right">3.1%</td>
<td align="right">3,180</td>
<td align="right">3.4%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">32,220</td>
<td align="right">35.0%</td>
<td align="right">32,760</td>
<td align="right">35.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,760</td>
<td align="right">9.5%</td>
<td align="right">8,620</td>
<td align="right">9.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,960</td>
<td align="right">15.2%</td>
<td align="right">13,880</td>
<td align="right">15.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,940</td>
<td align="right">5.4%</td>
<td align="right">4,920</td>
<td align="right">5.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,728</td>
<td align="right">10.6%</td>
<td align="right">9,728</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,480</td>
<td align="right">8.1%</td>
<td align="right">7,480</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,320</td>
<td align="right">6.9%</td>
<td align="right">6,320</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,780</td>
<td align="right">5.2%</td>
<td align="right">4,780</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">800</td>
<td align="right">0.9%</td>
<td align="right">800</td>
<td align="right">0.9%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">232,045,908</td>
<td align="right">20.9%</td>
<td align="right">270,370,580</td>
<td align="right">23.6%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">877,138,730</td>
<td align="right">79.1%</td>
<td align="right">875,232,064</td>
<td align="right">76.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,900</td>
<td align="right">0.0%</td>
<td align="right">2,900</td>
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
<td align="right">99,903</td>
<td align="right">88.6%</td>
<td align="right">110,236</td>
<td align="right">89.5%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,901</td>
<td align="right">11.4%</td>
<td align="right">12,900</td>
<td align="right">10.5%</td>
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
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">6.5%</td>
<td align="right">14,280</td>
<td align="right">13.0%</td>
<td align="right">120.4%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,340</td>
<td align="right">1.3%</td>
<td align="right">1,520</td>
<td align="right">1.4%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">39,660</td>
<td align="right">39.7%</td>
<td align="right">41,860</td>
<td align="right">38.0%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,480</td>
<td align="right">1.5%</td>
<td align="right">1,520</td>
<td align="right">1.4%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,523</td>
<td align="right">7.5%</td>
<td align="right">7,636</td>
<td align="right">6.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,420</td>
<td align="right">43.5%</td>
<td align="right">43,420</td>
<td align="right">39.4%</td>
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
<td align="right">248,297,855</td>
<td align="right">3.9%</td>
<td align="right">289,512,703</td>
<td align="right">4.5%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">55,396,167</td>
<td align="right">0.9%</td>
<td align="right">61,044,705</td>
<td align="right">0.9%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,101,618,665</td>
<td align="right">96.1%</td>
<td align="right">6,138,326,319</td>
<td align="right">95.5%</td>
<td align="right">0.6%</td>
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
<td align="right">356,514</td>
<td align="right">22.4%</td>
<td align="right">532,331</td>
<td align="right">28.4%</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,238,313</td>
<td align="right">77.6%</td>
<td align="right">1,344,852</td>
<td align="right">71.6%</td>
<td align="right">8.6%</td>
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
<td align="right">5,136</td>
<td align="right">1.4%</td>
<td align="right">138,652</td>
<td align="right">26.0%</td>
<td align="right">2,599.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,248</td>
<td align="right">3.7%</td>
<td align="right">19,306</td>
<td align="right">3.6%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">135,485</td>
<td align="right">38.0%</td>
<td align="right">165,128</td>
<td align="right">31.0%</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,020</td>
<td align="right">4.2%</td>
<td align="right">17,420</td>
<td align="right">3.3%</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,178</td>
<td align="right">22.8%</td>
<td align="right">84,882</td>
<td align="right">15.9%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">55,303</td>
<td align="right">15.5%</td>
<td align="right">55,770</td>
<td align="right">10.5%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,158</td>
<td align="right">3.7%</td>
<td align="right">13,180</td>
<td align="right">2.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">35,066</td>
<td align="right">9.8%</td>
<td align="right">35,073</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.4%</td>
<td align="right">1,460</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.3%</td>
<td align="right">1,040</td>
<td align="right">0.2%</td>
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
<td align="right">1,558,579,012</td>
<td align="right">100.0%</td>
<td align="right">1,557,977,743</td>
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
<td align="right">194,063</td>
<td align="right">0.0%</td>
<td align="right">194,073</td>
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
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">3,080</td>
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
<td align="right">1,855</td>
<td align="right">5.8%</td>
<td align="right">1,859</td>
<td align="right">5.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,056</td>
<td align="right">94.2%</td>
<td align="right">30,052</td>
<td align="right">94.2%</td>
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
<td align="left">sequence</td>
<td align="right">1,215</td>
<td align="right">65.5%</td>
<td align="right">1,219</td>
<td align="right">65.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">20.5%</td>
<td align="right">380</td>
<td align="right">20.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.0%</td>
<td align="right">260</td>
<td align="right">14.0%</td>
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
<td align="right">11,723,539,604</td>
<td align="right">9.6%</td>
<td align="right">12,887,424,503</td>
<td align="right">10.0%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">915,702,819</td>
<td align="right">0.7%</td>
<td align="right">829,812,394</td>
<td align="right">0.6%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">42,700,996,207</td>
<td align="right">34.9%</td>
<td align="right">45,361,446,679</td>
<td align="right">35.1%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">67,004,773,646</td>
<td align="right">54.8%</td>
<td align="right">70,308,397,761</td>
<td align="right">54.3%</td>
<td align="right">4.9%</td>
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
<td align="right">248,297,855</td>
<td align="right">4.9%</td>
<td align="right">289,512,703</td>
<td align="right">5.6%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,045,908</td>
<td align="right">4.6%</td>
<td align="right">270,370,580</td>
<td align="right">5.2%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">743,940,157</td>
<td align="right">14.8%</td>
<td align="right">824,182,176</td>
<td align="right">15.8%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">436,966,137</td>
<td align="right">8.7%</td>
<td align="right">472,615,354</td>
<td align="right">9.1%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">190,494,111</td>
<td align="right">3.8%</td>
<td align="right">178,957,655</td>
<td align="right">3.4%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">662,414,532</td>
<td align="right">13.2%</td>
<td align="right">633,171,982</td>
<td align="right">12.1%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">208,241,255</td>
<td align="right">4.1%</td>
<td align="right">213,264,128</td>
<td align="right">4.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">483,702,471</td>
<td align="right">9.6%</td>
<td align="right">492,561,163</td>
<td align="right">9.4%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,521,471,766</td>
<td align="right">30.3%</td>
<td align="right">1,545,561,842</td>
<td align="right">29.6%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,918</td>
<td align="right">3.5%</td>
<td align="right">173,284,922</td>
<td align="right">3.3%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">98,363,888</td>
<td align="right">9.9%</td>
<td align="right">71,357,060</td>
<td align="right">7.9%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">125,994,724</td>
<td align="right">12.7%</td>
<td align="right">98,707,964</td>
<td align="right">10.9%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,365,644</td>
<td align="right">2.7%</td>
<td align="right">31,482,184</td>
<td align="right">3.5%</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">172,482,356</td>
<td align="right">17.4%</td>
<td align="right">141,939,251</td>
<td align="right">15.6%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">114,241,500</td>
<td align="right">11.5%</td>
<td align="right">100,635,120</td>
<td align="right">11.1%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">58,788,249</td>
<td align="right">5.9%</td>
<td align="right">56,889,728</td>
<td align="right">6.3%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,549,218</td>
<td align="right">3.6%</td>
<td align="right">35,475,122</td>
<td align="right">3.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,897,849</td>
<td align="right">7.8%</td>
<td align="right">77,898,147</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,897,849</td>
<td align="right">7.8%</td>
<td align="right">77,898,147</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,557</td>
<td align="right">2.8%</td>
<td align="right">27,496,598</td>
<td align="right">3.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">550,027,773</td>
<td align="right">6.3%</td>
<td align="right">411,816,481</td>
<td align="right">4.7%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,783,960,837</td>
<td align="right">20.5%</td>
<td align="right">1,630,174,890</td>
<td align="right">18.7%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,788,407,277</td>
<td align="right">20.5%</td>
<td align="right">1,634,621,330</td>
<td align="right">18.8%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,648,971,591</td>
<td align="right">30.4%</td>
<td align="right">2,485,938,145</td>
<td align="right">28.6%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,648,971,591</td>
<td align="right">30.4%</td>
<td align="right">2,485,938,145</td>
<td align="right">28.6%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">348,456,095</td>
<td align="right">4.0%</td>
<td align="right">332,946,656</td>
<td align="right">3.8%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,063,941,857</td>
<td align="right">69.6%</td>
<td align="right">6,211,459,372</td>
<td align="right">71.4%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,564,314</td>
<td align="right">9.9%</td>
<td align="right">851,316,815</td>
<td align="right">9.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,953,938,790</td>
<td align="right">79.8%</td>
<td align="right">6,939,148,634</td>
<td align="right">79.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,399,009</td>
<td align="right">1.0%</td>
<td align="right">84,401,154</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,015,392</td>
<td align="right">0.4%</td>
<td align="right">31,015,238</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,363</td>
<td align="right">2.0%</td>
<td align="right">175,480,421</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,417,680</td>
<td align="right">0.1%</td>
<td align="right">4,417,680</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">28,760</td>
<td align="right">0.0%</td>
<td align="right">28,760</td>
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
<td align="right">72,069,976</td>
<td align="right"></td>
<td align="right">66,320,431</td>
<td align="right"></td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,218,666,684</td>
<td align="right"></td>
<td align="right">2,966,384,611</td>
<td align="right"></td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">79,081,333</td>
<td align="right"></td>
<td align="right">73,407,404</td>
<td align="right"></td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">90,331,766,661</td>
<td align="right">62.8%</td>
<td align="right">85,781,918,223</td>
<td align="right">60.5%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">53,443,966,322</td>
<td align="right">37.2%</td>
<td align="right">55,889,770,140</td>
<td align="right">39.5%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">94,422,203,988</td>
<td align="right">56.7%</td>
<td align="right">90,743,142,877</td>
<td align="right">55.2%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,569,681,437</td>
<td align="right"></td>
<td align="right">4,410,051,930</td>
<td align="right"></td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">72,170,012,760</td>
<td align="right">43.3%</td>
<td align="right">73,721,041,245</td>
<td align="right">44.8%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">94,075,944</td>
<td align="right">0.4%</td>
<td align="right">92,635,691</td>
<td align="right">0.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">10,323,160</td>
<td align="right"></td>
<td align="right">10,396,401</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">14,848,257</td>
<td align="right">0.1%</td>
<td align="right">14,772,675</td>
<td align="right">0.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,823,268,939</td>
<td align="right">55.7%</td>
<td align="right">12,802,958,631</td>
<td align="right">55.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,125,686</td>
<td align="right"></td>
<td align="right">161,872,832</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,527,517,116</td>
<td align="right"></td>
<td align="right">13,507,170,840</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,714,344,738</td>
<td align="right">55.2%</td>
<td align="right">12,695,550,265</td>
<td align="right">55.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,206,180,055</td>
<td align="right">44.3%</td>
<td align="right">10,199,024,287</td>
<td align="right">44.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,208,044,347</td>
<td align="right"></td>
<td align="right">10,200,892,928</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,305,720</td>
<td align="right">2.0%</td>
<td align="right">3,305,720</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">114,680</td>
<td align="right">0.1%</td>
<td align="right">114,680</td>
<td align="right">0.1%</td>
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
<td align="right">115,241,360</td>
<td align="right">19,134,550,032</td>
<td align="right">0</td>
<td align="right">114,831,260</td>
<td align="right">19,135,613,045</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,733,144</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,713,224</td>
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,720</td>
<td align="right">0.1%</td>
<td align="right">4,200</td>
<td align="right">0.4%</td>
<td align="right">144.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,339</td>
<td align="right">0.1%</td>
<td align="right">1,988</td>
<td align="right">0.2%</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">125,555</td>
<td align="right">10.3%</td>
<td align="right">146,280</td>
<td align="right">13.7%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,098,998</td>
<td align="right">89.7%</td>
<td align="right">924,607</td>
<td align="right">86.3%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">12,615</td>
<td align="right">1.0%</td>
<td align="right">10,618</td>
<td align="right">1.0%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">50,523</td>
<td align="right">4.1%</td>
<td align="right">57,606</td>
<td align="right">5.4%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,224,553</td>
<td align="right"></td>
<td align="right">1,070,887</td>
<td align="right"></td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,352</td>
<td align="right">5.1%</td>
<td align="right">7,138</td>
<td align="right">4.9%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,672,545,371</td>
<td align="right"></td>
<td align="right">7,025,988,247</td>
<td align="right"></td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">495,905</td>
<td align="right">40.5%</td>
<td align="right">458,840</td>
<td align="right">42.8%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">249,908,488,719</td>
<td align="right">3,257.2%</td>
<td align="right">236,632,998,112</td>
<td align="right">3,368.0%</td>
<td align="right">-5.3%</td>
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
<td align="right">140</td>
<td align="right">0.0%</td>
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
<td align="right">110,768</td>
<td align="right">88.2%</td>
<td align="right">133,583</td>
<td align="right">91.3%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">125,555</td>
<td align="right"></td>
<td align="right">146,280</td>
<td align="right"></td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,443</td>
<td align="right">1.9%</td>
<td align="right">2,400</td>
<td align="right">1.6%</td>
<td align="right">-1.8%</td>
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
<td align="right">5,157</td>
<td align="right">4.1%</td>
<td align="right">7,724</td>
<td align="right">5.3%</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,470</td>
<td align="right">17.1%</td>
<td align="right">25,977</td>
<td align="right">17.8%</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,360</td>
<td align="right">28.2%</td>
<td align="right">41,011</td>
<td align="right">28.0%</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">30,757</td>
<td align="right">24.5%</td>
<td align="right">34,241</td>
<td align="right">23.4%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21,361</td>
<td align="right">17.0%</td>
<td align="right">21,722</td>
<td align="right">14.8%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,630</td>
<td align="right">7.7%</td>
<td align="right">13,185</td>
<td align="right">9.0%</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,660</td>
<td align="right">1.3%</td>
<td align="right">2,260</td>
<td align="right">1.5%</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">160</td>
<td align="right">0.1%</td>
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
<td align="right">3,997</td>
<td align="right">3.2%</td>
<td align="right">6,690</td>
<td align="right">4.6%</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">14,806</td>
<td align="right">11.8%</td>
<td align="right">16,846</td>
<td align="right">11.5%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">25,289</td>
<td align="right">20.1%</td>
<td align="right">31,340</td>
<td align="right">21.4%</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">36,375</td>
<td align="right">29.0%</td>
<td align="right">41,410</td>
<td align="right">28.3%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">18,534</td>
<td align="right">14.8%</td>
<td align="right">21,778</td>
<td align="right">14.9%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,787</td>
<td align="right">7.0%</td>
<td align="right">11,239</td>
<td align="right">7.7%</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,600</td>
<td align="right">2.1%</td>
<td align="right">3,820</td>
<td align="right">2.6%</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">380</td>
<td align="right">0.3%</td>
<td align="right">460</td>
<td align="right">0.3%</td>
<td align="right">21.1%</td>
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
<td align="right">10,382,540</td>
<td align="right">34,601.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">10,050,940</td>
<td align="right">60,225,600</td>
<td align="right">499.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">11,627,720</td>
<td align="right">62,034,940</td>
<td align="right">433.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">47,971,806</td>
<td align="right">98,760,940</td>
<td align="right">105.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">239,755,007</td>
<td align="right">27,410,380</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,648,680</td>
<td align="right">652,560</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">2,587,460</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,831,680</td>
<td align="right">98,457,240</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">338,015,782</td>
<td align="right">159,892,933</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">101,766,726</td>
<td align="right">151,748,160</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,717,580</td>
<td align="right">14,254,180</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">39,840</td>
<td align="right">22,560</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">23,620</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,325,176,387</td>
<td align="right">1,648,447,531</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">126,341,149</td>
<td align="right">162,997,643</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,921,070</td>
<td align="right">6,264,523</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">394,099,394</td>
<td align="right">500,202,966</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">30,574,602</td>
<td align="right">22,649,634</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">296,727,179</td>
<td align="right">224,648,091</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">274,503,937</td>
<td align="right">340,616,960</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">102,572,239</td>
<td align="right">77,907,428</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">2,065,540</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,193,950</td>
<td align="right">102,185,534</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,193,950</td>
<td align="right">102,185,534</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">149,609,060</td>
<td align="right">184,826,010</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">136,726,362</td>
<td align="right">104,704,477</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">64,511,956</td>
<td align="right">49,614,720</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">395,091,201</td>
<td align="right">308,389,621</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,517,065</td>
<td align="right">1,971,203</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">266,224,195</td>
<td align="right">323,635,910</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,323,630,944</td>
<td align="right">1,042,522,641</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,720</td>
<td align="right">650,000</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,027,049,917</td>
<td align="right">812,743,823</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">435,886,258</td>
<td align="right">526,582,709</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,398,392</td>
<td align="right">75,887,790</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,862,100</td>
<td align="right">5,627,240</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">48,468,106</td>
<td align="right">39,826,876</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">514,728,318</td>
<td align="right">606,311,149</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,688,940,366</td>
<td align="right">8,022,984,891</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,697,060</td>
<td align="right">10,585,640</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,642,252</td>
<td align="right">80,279,030</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,280,053,336</td>
<td align="right">1,080,530,542</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,738,779,346</td>
<td align="right">3,203,402,600</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,611,491,440</td>
<td align="right">1,389,978,175</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">244,676,040</td>
<td align="right">211,435,160</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,098,625,361</td>
<td align="right">949,596,123</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">28,421,138</td>
<td align="right">24,720,261</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">59,644,340</td>
<td align="right">51,948,180</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,046,179,304</td>
<td align="right">912,007,364</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,189,392,105</td>
<td align="right">1,335,020,395</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">457,490,993</td>
<td align="right">401,800,509</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,275,944,635</td>
<td align="right">3,757,185,662</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,853,882,628</td>
<td align="right">1,631,586,880</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,301,801,085</td>
<td align="right">1,457,097,815</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,321,667,965</td>
<td align="right">1,477,093,775</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">216,495,378</td>
<td align="right">191,614,881</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">219,024,135</td>
<td align="right">193,950,950</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">462,455</td>
<td align="right">409,981</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,025,020</td>
<td align="right">2,684,100</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,597,902</td>
<td align="right">99,629,597</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">76,107,214</td>
<td align="right">67,955,469</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">777,595,743</td>
<td align="right">694,533,289</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">15,651,341,300</td>
<td align="right">14,020,396,190</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">7,012,387,742</td>
<td align="right">6,328,379,742</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">67,773,180</td>
<td align="right">61,399,940</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,819,330,275</td>
<td align="right">4,369,784,780</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,488,954,558</td>
<td align="right">1,351,255,129</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,164,660,446</td>
<td align="right">2,877,507,489</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,952</td>
<td align="right">350,222,070</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">192,460,192</td>
<td align="right">175,666,387</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,383,640,585</td>
<td align="right">1,265,250,259</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,982,225,488</td>
<td align="right">16,451,219,835</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">113,123,751</td>
<td align="right">103,551,354</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,672,545,371</td>
<td align="right">7,025,988,247</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">81,660,820</td>
<td align="right">88,347,700</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,032,829,215</td>
<td align="right">2,794,477,489</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">81,529,540</td>
<td align="right">87,927,520</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,688,898,382</td>
<td align="right">4,328,967,314</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,931,060</td>
<td align="right">4,562,460</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,227,270</td>
<td align="right">9,467,282</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,681,085,960</td>
<td align="right">1,802,501,544</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,345,927,844</td>
<td align="right">1,251,150,548</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,840,870,976</td>
<td align="right">2,643,166,009</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">121,960,369</td>
<td align="right">130,247,628</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">890,076,806</td>
<td align="right">830,234,746</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">66,421,885</td>
<td align="right">62,070,173</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,024,764,791</td>
<td align="right">2,156,713,743</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,187</td>
<td align="right">603,430,907</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,257,196,621</td>
<td align="right">5,857,924,679</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,790,016,836</td>
<td align="right">1,903,735,076</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,085,253,964</td>
<td align="right">2,216,731,896</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,963,316,775</td>
<td align="right">2,086,507,448</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,583,106</td>
<td align="right">12,307,151</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,583,106</td>
<td align="right">12,307,151</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,280,392,111</td>
<td align="right">6,825,766,457</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">269,583,187</td>
<td align="right">286,122,245</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">270,810,447</td>
<td align="right">287,349,505</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,682,494,122</td>
<td align="right">1,581,041,020</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">270,904,974</td>
<td align="right">287,100,209</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">643,774,743</td>
<td align="right">605,450,163</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,430,760,611</td>
<td align="right">3,227,325,968</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,020,029,476</td>
<td align="right">1,902,360,296</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">386,735,590</td>
<td align="right">408,537,093</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,164,428,041</td>
<td align="right">2,046,246,562</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">173,349,135</td>
<td align="right">182,804,998</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,700,474</td>
<td align="right">96,596,549</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">904,464,212</td>
<td align="right">856,433,330</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">60,988,920</td>
<td align="right">57,779,680</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,413,730,611</td>
<td align="right">4,181,539,869</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">940,130,182</td>
<td align="right">989,335,946</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">557,752,020</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">834,093,814</td>
<td align="right">790,886,948</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">85,735,820</td>
<td align="right">81,444,140</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">905,121,013</td>
<td align="right">948,118,333</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,404,384,390</td>
<td align="right">2,518,330,089</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,430,557,650</td>
<td align="right">2,533,299,729</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,059,545,388</td>
<td align="right">1,015,299,282</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,183,972,898</td>
<td align="right">12,640,115,405</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,098,234,400</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">140,079,385</td>
<td align="right">134,611,196</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,372,390,956</td>
<td align="right">3,241,824,252</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,575,479,007</td>
<td align="right">1,514,643,579</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,744,534,634</td>
<td align="right">2,639,221,755</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">25,201,696</td>
<td align="right">24,262,540</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">650,437,511</td>
<td align="right">627,232,088</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,092,184</td>
<td align="right">33,857,736</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,681,948</td>
<td align="right">10,311,331</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,816,325,714</td>
<td align="right">1,757,040,848</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">658,513,087</td>
<td align="right">637,070,399</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">316,309,046</td>
<td align="right">306,009,472</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">406,359,417</td>
<td align="right">394,403,322</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,826,009,167</td>
<td align="right">6,628,150,406</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,621,056,398</td>
<td align="right">3,524,390,993</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,419,034,042</td>
<td align="right">1,382,502,371</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">104,757,000</td>
<td align="right">102,221,540</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,177,300</td>
<td align="right">7,983,320</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">972,409,134</td>
<td align="right">994,786,637</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">246,277,913</td>
<td align="right">240,617,523</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,883,887,175</td>
<td align="right">1,843,260,707</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,966,880</td>
<td align="right">2,906,100</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">395,106,603</td>
<td align="right">387,276,780</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">800,652,699</td>
<td align="right">815,715,690</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">233,813,802</td>
<td align="right">229,617,570</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">164,118,568</td>
<td align="right">161,178,133</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,065,920</td>
<td align="right">3,013,120</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,659,960</td>
<td align="right">5,573,240</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">52,987,220</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">970,228,623</td>
<td align="right">956,701,797</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">702,590,194</td>
<td align="right">711,792,810</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">321,308,144</td>
<td align="right">325,421,335</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,257,745,764</td>
<td align="right">2,284,223,114</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">221,352,540</td>
<td align="right">223,842,040</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,550,540</td>
<td align="right">189,595,760</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,187,447</td>
<td align="right">97,126,729</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,822,630</td>
<td align="right">32,155,790</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,118,642,883</td>
<td align="right">6,181,891,242</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,996,839,771</td>
<td align="right">2,017,360,467</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">46,000,340</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,825,993,772</td>
<td align="right">1,813,032,477</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">992,079,740</td>
<td align="right">985,262,377</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">923,767,825</td>
<td align="right">917,467,880</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">562,697,102</td>
<td align="right">559,010,846</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">218,973,940</td>
<td align="right">220,320,860</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,253,397,167</td>
<td align="right">1,245,817,620</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,705,220</td>
<td align="right">80,222,480</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">860,627,259</td>
<td align="right">865,677,279</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,318,061,660</td>
<td align="right">2,304,804,429</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">553,848,296</td>
<td align="right">551,135,175</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,326,044</td>
<td align="right">2,318,566</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,619,566,649</td>
<td align="right">3,630,995,450</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,475,754</td>
<td align="right">159,979,393</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,713,807</td>
<td align="right">90,435,207</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,990,580</td>
<td align="right">144,568,060</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,508,803,479</td>
<td align="right">2,502,052,725</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">662,715,657</td>
<td align="right">661,080,635</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">510,187,700</td>
<td align="right">509,019,680</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,682,764</td>
<td align="right">68,537,216</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">198,398,358</td>
<td align="right">197,997,906</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,131,155,755</td>
<td align="right">1,129,011,866</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">894,002,384</td>
<td align="right">895,624,188</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">3,628,059</td>
<td align="right">3,621,541</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,578,576,329</td>
<td align="right">6,589,757,113</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,230,107</td>
<td align="right">97,086,469</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,683,480</td>
<td align="right">204,389,180</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,327,853</td>
<td align="right">96,196,460</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,375,688</td>
<td align="right">78,281,063</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,933,261</td>
<td align="right">229,669,442</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">162,876,000</td>
<td align="right">162,693,505</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,013,560</td>
<td align="right">532,564,220</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,965,460</td>
<td align="right">154,842,300</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,333,213</td>
<td align="right">93,383,630</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,152,807,838</td>
<td align="right">1,152,200,480</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,695,501</td>
<td align="right">779,104,179</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,598,528</td>
<td align="right">731,911,717</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,158,181</td>
<td align="right">778,466,839</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,671,620</td>
<td align="right">3,670,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,402,252</td>
<td align="right">32,401,870</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,543,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">545,860</td>
<td align="right">545,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">310,680</td>
<td align="right">310,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">7,620</td>
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
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,081</td>
<td align="right">200,825</td>
<td align="right">3,202.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,180</td>
<td align="right">11,000</td>
<td align="right">832.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,621</td>
<td align="right">22,056</td>
<td align="right">509.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">320</td>
<td align="right">1,860</td>
<td align="right">481.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">620</td>
<td align="right">2,580</td>
<td align="right">316.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,595</td>
<td align="right">17,041</td>
<td align="right">158.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">486,354</td>
<td align="right">122,444</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,457</td>
<td align="right">2,717</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">33,340</td>
<td align="right">31,580</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,650</td>
<td align="right">42,910</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">30,480</td>
<td align="right">31,500</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,680</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">640</td>
<td align="right">640</td>
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
<td align="right">1,105</td>
<td align="right">1,103</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,105</td>
<td align="right">1,103</td>
<td align="right">-0.2%</td>
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
<td align="right">300</td>
<td align="right">300</td>
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
<td align="right">420</td>
<td align="right">420</td>
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
<td align="right">1,780</td>
<td align="right">1,780</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-07-16
