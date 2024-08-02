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
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,554,054</td>
<td align="right">62,861,873</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,782,766</td>
<td align="right">41,728,140</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">171,382,487</td>
<td align="right">105,932,537</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">2,226,205</td>
<td align="right">1,470,313</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">298,878,121</td>
<td align="right">219,288,352</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,364,843,616</td>
<td align="right">1,003,150,764</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">144,651,888</td>
<td align="right">108,739,970</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,368</td>
<td align="right">148,322,572</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">392,707,458</td>
<td align="right">308,324,170</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">291,570,534</td>
<td align="right">232,424,221</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,386,760,357</td>
<td align="right">1,903,049,404</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">587,819,927</td>
<td align="right">470,938,401</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">368,274,585</td>
<td align="right">303,625,446</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">418,013,008</td>
<td align="right">347,521,769</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,329,806,884</td>
<td align="right">1,951,542,967</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,141,502,149</td>
<td align="right">2,641,213,345</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">285,252,008</td>
<td align="right">241,092,437</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">42,396,197</td>
<td align="right">36,696,837</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">474,313,895</td>
<td align="right">415,842,279</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,256,867,618</td>
<td align="right">1,123,149,796</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,495,615,166</td>
<td align="right">4,920,447,152</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,039,442,097</td>
<td align="right">938,900,072</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,313,599</td>
<td align="right">9,328,572</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">107,637,591</td>
<td align="right">98,197,996</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">583,226,659</td>
<td align="right">536,854,726</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,017,115,416</td>
<td align="right">3,703,165,317</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,048,701,181</td>
<td align="right">968,589,482</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">64,744,063</td>
<td align="right">59,921,622</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">147,324,975</td>
<td align="right">137,220,818</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,112,140,058</td>
<td align="right">1,039,426,752</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">515,873,470</td>
<td align="right">482,602,108</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,081,838,619</td>
<td align="right">4,787,297,751</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">588,004,438</td>
<td align="right">553,925,798</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,915,211,852</td>
<td align="right">1,810,704,753</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,288,899,931</td>
<td align="right">3,113,348,135</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">292,481,148</td>
<td align="right">277,871,707</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,877,399</td>
<td align="right">10,340,130</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">985,360,237</td>
<td align="right">936,921,370</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,593,217,749</td>
<td align="right">1,520,539,442</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,374,006,238</td>
<td align="right">18,608,055,276</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,857,242,416</td>
<td align="right">3,708,299,513</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">274,561,079</td>
<td align="right">263,971,956</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">46,043,460</td>
<td align="right">44,302,694</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">184,207,675</td>
<td align="right">177,628,256</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">337,964,814</td>
<td align="right">326,982,681</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">386,721,987</td>
<td align="right">374,252,892</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">219,943,845</td>
<td align="right">213,182,895</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">353,362,669</td>
<td align="right">342,797,942</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">13,038,643</td>
<td align="right">12,653,192</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">13,046,403</td>
<td align="right">12,660,952</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,050,281</td>
<td align="right">12,664,897</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,026,756,973</td>
<td align="right">4,886,997,687</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">365,580,027</td>
<td align="right">355,500,091</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">76,320,455</td>
<td align="right">74,261,981</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">436,579,670</td>
<td align="right">425,610,647</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">104,241,716</td>
<td align="right">101,686,323</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,447,260</td>
<td align="right">52,148,995</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,078,049,804</td>
<td align="right">4,962,521,777</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">32,319,230</td>
<td align="right">31,598,797</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">221,927,790</td>
<td align="right">216,993,095</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">71,759,281</td>
<td align="right">70,172,160</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">226,059,676</td>
<td align="right">221,073,893</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">86,673,441</td>
<td align="right">84,828,866</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">394,251,968</td>
<td align="right">386,180,348</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,235,436,170</td>
<td align="right">2,191,361,256</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">384,934,022</td>
<td align="right">377,690,503</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">33,192,410</td>
<td align="right">32,577,835</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,683,888,033</td>
<td align="right">2,642,362,459</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,293,147</td>
<td align="right">2,258,785</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">106,387,349</td>
<td align="right">104,918,944</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">330,124,136</td>
<td align="right">325,596,030</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,696,903</td>
<td align="right">18,452,269</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">196,132,182</td>
<td align="right">193,652,025</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">98,060,497</td>
<td align="right">96,891,640</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,387,058</td>
<td align="right">57,707,927</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">116,395,186</td>
<td align="right">115,077,467</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,212,141,384</td>
<td align="right">4,165,056,265</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">278,198,801</td>
<td align="right">275,136,930</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">172,973,172</td>
<td align="right">171,072,704</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">188,873,263</td>
<td align="right">186,885,157</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">894,280,174</td>
<td align="right">885,295,740</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">213,911</td>
<td align="right">211,833</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">628,061,100</td>
<td align="right">622,062,395</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">164,480</td>
<td align="right">162,960</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,432,380</td>
<td align="right">47,003,706</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">329,252,734</td>
<td align="right">326,498,837</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,612,806</td>
<td align="right">77,985,979</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">313,802,285</td>
<td align="right">311,302,458</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">323,246,971</td>
<td align="right">320,879,981</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">977,455,806</td>
<td align="right">970,440,144</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,152,949,974</td>
<td align="right">1,144,734,939</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">90,891,240</td>
<td align="right">90,353,942</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">90,896,380</td>
<td align="right">90,359,082</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,234,353,169</td>
<td align="right">1,227,150,113</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">190,001,758</td>
<td align="right">188,921,124</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,193,786</td>
<td align="right">65,832,028</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">205,996,467</td>
<td align="right">204,939,892</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">16,007</td>
<td align="right">15,925</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">150,918,392</td>
<td align="right">150,199,647</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">99,331,260</td>
<td align="right">98,885,500</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,727,421</td>
<td align="right">52,504,541</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">106,118,522</td>
<td align="right">105,672,762</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">111,557,009</td>
<td align="right">111,113,566</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">233,921,440</td>
<td align="right">233,039,453</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">400,251,991</td>
<td align="right">398,872,786</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">83,450,833</td>
<td align="right">83,187,765</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,085,798</td>
<td align="right">82,829,096</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">244,554</td>
<td align="right">243,820</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">94,682,948</td>
<td align="right">94,423,153</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">122,144,067</td>
<td align="right">121,831,706</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">48,015,507</td>
<td align="right">47,909,584</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">83,998,849</td>
<td align="right">83,850,404</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">350,375,329</td>
<td align="right">349,794,095</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">707,704,881</td>
<td align="right">706,604,684</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,946,181</td>
<td align="right">13,925,477</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">356,552,717</td>
<td align="right">356,073,352</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">278,941,242</td>
<td align="right">278,636,089</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">258,827,649</td>
<td align="right">258,572,311</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,378,886</td>
<td align="right">2,376,678</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">397,543,971</td>
<td align="right">397,305,833</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,305,491</td>
<td align="right">20,296,703</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,175,189</td>
<td align="right">216,102,531</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,782,827</td>
<td align="right">1,782,235</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">692,451</td>
<td align="right">692,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">22,329,979</td>
<td align="right">22,324,751</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,125,401</td>
<td align="right">35,120,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">6,621,084</td>
<td align="right">6,620,205</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,068</td>
<td align="right">1,873,234</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,288,907</td>
<td align="right">40,285,502</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">6,967,996</td>
<td align="right">6,967,492</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,651,846</td>
<td align="right">9,652,497</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,216,265</td>
<td align="right">9,216,772</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">42,167,460</td>
<td align="right">42,165,705</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68,003,129</td>
<td align="right">68,000,443</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">148,275,841</td>
<td align="right">148,270,333</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,575,216</td>
<td align="right">17,574,625</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">7,571,460</td>
<td align="right">7,571,257</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,110,966</td>
<td align="right">91,108,545</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,809,731</td>
<td align="right">72,807,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">444,724,079</td>
<td align="right">444,733,737</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,407,368</td>
<td align="right">4,407,426</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,978,582</td>
<td align="right">48,977,938</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,613,296</td>
<td align="right">9,613,195</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,312,713</td>
<td align="right">233,310,985</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">502,660</td>
<td align="right">502,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">143,313,031</td>
<td align="right">143,312,506</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">104,677,470</td>
<td align="right">104,677,155</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,823,030</td>
<td align="right">1,823,034</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,613,124</td>
<td align="right">46,613,188</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">33,292,589</td>
<td align="right">33,292,613</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,710,578</td>
<td align="right">555,710,846</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">72,221,012</td>
<td align="right">72,221,038</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">250,972,774</td>
<td align="right">250,972,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,216,119</td>
<td align="right">786,216,203</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,550</td>
<td align="right">173,318,558</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">228,622,190</td>
<td align="right">228,622,198</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">32,547,446</td>
<td align="right">32,547,445</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,024,585</td>
<td align="right">402,024,597</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">52,179,020</td>
<td align="right">52,179,020</td>
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
<td align="right">12,088,360</td>
<td align="right">12,088,360</td>
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
<td align="right">7,254,200</td>
<td align="right">7,254,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,464,680</td>
<td align="right">3,464,680</td>
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
<td align="right">546,320</td>
<td align="right">546,320</td>
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
<td align="right">147,100</td>
<td align="right">147,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">94,160</td>
<td align="right">94,160</td>
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
<td align="right">49,180</td>
<td align="right">49,180</td>
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
<td align="right">22,800</td>
<td align="right">22,800</td>
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
<td align="right">420,526,157</td>
<td align="right">5.8%</td>
<td align="right">336,171,189</td>
<td align="right">5.0%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,831,253,549</td>
<td align="right">94.2%</td>
<td align="right">6,373,284,761</td>
<td align="right">95.0%</td>
<td align="right">-6.7%</td>
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
<td align="right">0.4%</td>
<td align="right">29,500,920</td>
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
<td align="left">Failure</td>
<td align="right">1,090,669</td>
<td align="right">64.8%</td>
<td align="right">1,064,217</td>
<td align="right">64.3%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">591,552</td>
<td align="right">35.2%</td>
<td align="right">589,684</td>
<td align="right">35.7%</td>
<td align="right">-0.3%</td>
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
<td align="left">floor divide</td>
<td align="right">32,104</td>
<td align="right">2.9%</td>
<td align="right">10,316</td>
<td align="right">1.0%</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">2,060</td>
<td align="right">0.2%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,420</td>
<td align="right">0.2%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">37,298</td>
<td align="right">3.4%</td>
<td align="right">35,340</td>
<td align="right">3.3%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,466</td>
<td align="right">1.0%</td>
<td align="right">10,084</td>
<td align="right">0.9%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">16,008</td>
<td align="right">1.5%</td>
<td align="right">15,733</td>
<td align="right">1.5%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,648</td>
<td align="right">7.5%</td>
<td align="right">80,726</td>
<td align="right">7.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,542</td>
<td align="right">0.5%</td>
<td align="right">5,528</td>
<td align="right">0.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,866</td>
<td align="right">0.8%</td>
<td align="right">8,844</td>
<td align="right">0.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,896</td>
<td align="right">0.2%</td>
<td align="right">1,895</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,726</td>
<td align="right">0.4%</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">12,529</td>
<td align="right">1.1%</td>
<td align="right">12,534</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,028</td>
<td align="right">0.5%</td>
<td align="right">5,026</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,612</td>
<td align="right">71.7%</td>
<td align="right">781,350</td>
<td align="right">73.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">38,075</td>
<td align="right">3.5%</td>
<td align="right">38,086</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,609</td>
<td align="right">0.8%</td>
<td align="right">8,607</td>
<td align="right">0.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,922</td>
<td align="right">2.7%</td>
<td align="right">29,924</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
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
<td align="right">419,503,797</td>
<td align="right">8.9%</td>
<td align="right">349,034,189</td>
<td align="right">7.9%</td>
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
<td align="right">4,293,101,329</td>
<td align="right">91.1%</td>
<td align="right">4,071,124,670</td>
<td align="right">92.1%</td>
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
<td align="right">1,753,617</td>
<td align="right">0.0%</td>
<td align="right">1,753,482</td>
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
<td align="left">Failure</td>
<td align="right">149,737</td>
<td align="right">57.0%</td>
<td align="right">129,401</td>
<td align="right">53.7%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">113,091</td>
<td align="right">43.0%</td>
<td align="right">111,661</td>
<td align="right">46.3%</td>
<td align="right">-1.3%</td>
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
<td align="right">30,952</td>
<td align="right">20.7%</td>
<td align="right">12,618</td>
<td align="right">9.8%</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">840</td>
<td align="right">0.6%</td>
<td align="right">760</td>
<td align="right">0.6%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,100</td>
<td align="right">0.7%</td>
<td align="right">1,060</td>
<td align="right">0.8%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,439</td>
<td align="right">20.3%</td>
<td align="right">29,439</td>
<td align="right">22.8%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">44,900</td>
<td align="right">30.0%</td>
<td align="right">44,020</td>
<td align="right">34.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,760</td>
<td align="right">13.2%</td>
<td align="right">19,760</td>
<td align="right">15.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">10.8%</td>
<td align="right">16,200</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,320</td>
<td align="right">3.6%</td>
<td align="right">5,320</td>
<td align="right">4.1%</td>
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
<td align="right">10,804,490,758</td>
<td align="right">97.2%</td>
<td align="right">10,254,548,617</td>
<td align="right">97.1%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">198,594,314</td>
<td align="right">1.8%</td>
<td align="right">193,218,415</td>
<td align="right">1.8%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">310,686,616</td>
<td align="right">2.8%</td>
<td align="right">304,100,542</td>
<td align="right">2.9%</td>
<td align="right">-2.1%</td>
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
<td align="left">Success</td>
<td align="right">4,225,966</td>
<td align="right">98.2%</td>
<td align="right">4,120,018</td>
<td align="right">98.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">76,918</td>
<td align="right">1.8%</td>
<td align="right">75,322</td>
<td align="right">1.8%</td>
<td align="right">-2.1%</td>
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
<td align="right">67,998</td>
<td align="right">88.4%</td>
<td align="right">66,502</td>
<td align="right">88.3%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">8,440</td>
<td align="right">11.0%</td>
<td align="right">8,340</td>
<td align="right">11.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,000</td>
<td align="right">3.9%</td>
<td align="right">3,000</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">580</td>
<td align="right">0.8%</td>
<td align="right">580</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">480</td>
<td align="right">0.6%</td>
<td align="right">480</td>
<td align="right">0.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,854,407,476</td>
<td align="right">98.0%</td>
<td align="right">4,634,275,138</td>
<td align="right">97.9%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">748,584</td>
<td align="right">0.0%</td>
<td align="right">737,989</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">98,611,692</td>
<td align="right">2.0%</td>
<td align="right">97,435,045</td>
<td align="right">2.1%</td>
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
<td align="right">65,981</td>
<td align="right">33.4%</td>
<td align="right">64,347</td>
<td align="right">33.1%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">131,408</td>
<td align="right">66.6%</td>
<td align="right">130,237</td>
<td align="right">66.9%</td>
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
<td align="left">bytes</td>
<td align="right">1,080</td>
<td align="right">0.8%</td>
<td align="right">960</td>
<td align="right">0.7%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">500</td>
<td align="right">0.4%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">26,290</td>
<td align="right">20.0%</td>
<td align="right">25,462</td>
<td align="right">19.6%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,780</td>
<td align="right">9.0%</td>
<td align="right">11,696</td>
<td align="right">9.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,780</td>
<td align="right">14.3%</td>
<td align="right">18,720</td>
<td align="right">14.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,549</td>
<td align="right">1.2%</td>
<td align="right">1,546</td>
<td align="right">1.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">26,612</td>
<td align="right">20.3%</td>
<td align="right">26,576</td>
<td align="right">20.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,371</td>
<td align="right">10.9%</td>
<td align="right">14,367</td>
<td align="right">11.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,366</td>
<td align="right">12.5%</td>
<td align="right">16,370</td>
<td align="right">12.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">8.1%</td>
<td align="right">10,680</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,740</td>
<td align="right">1.3%</td>
<td align="right">1,740</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,620</td>
<td align="right">1.2%</td>
<td align="right">1,620</td>
<td align="right">1.2%</td>
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
<td align="right">2,371,029,014</td>
<td align="right">92.3%</td>
<td align="right">2,321,621,511</td>
<td align="right">92.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">198,489,744</td>
<td align="right">7.7%</td>
<td align="right">196,011,201</td>
<td align="right">7.8%</td>
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
<td align="right">100,678</td>
<td align="right">63.0%</td>
<td align="right">99,144</td>
<td align="right">62.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">59,020</td>
<td align="right">37.0%</td>
<td align="right">58,940</td>
<td align="right">37.3%</td>
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
<td align="left">list</td>
<td align="right">8,800</td>
<td align="right">8.7%</td>
<td align="right">7,520</td>
<td align="right">7.6%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">23,215</td>
<td align="right">23.1%</td>
<td align="right">22,979</td>
<td align="right">23.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">13,543</td>
<td align="right">13.5%</td>
<td align="right">13,525</td>
<td align="right">13.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">55,120</td>
<td align="right">54.7%</td>
<td align="right">55,120</td>
<td align="right">55.6%</td>
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
<td align="right">462,302,714</td>
<td align="right">85.8%</td>
<td align="right">395,475,722</td>
<td align="right">84.2%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">76,349,763</td>
<td align="right">14.2%</td>
<td align="right">74,291,370</td>
<td align="right">15.8%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">171,744</td>
<td align="right">0.0%</td>
<td align="right">168,843</td>
<td align="right">0.0%</td>
<td align="right">-1.7%</td>
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
<td align="right">47,786</td>
<td align="right">33.5%</td>
<td align="right">46,676</td>
<td align="right">33.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">94,650</td>
<td align="right">66.5%</td>
<td align="right">92,778</td>
<td align="right">66.5%</td>
<td align="right">-2.0%</td>
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
<td align="left">zip</td>
<td align="right">7,720</td>
<td align="right">8.2%</td>
<td align="right">7,400</td>
<td align="right">8.0%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,328</td>
<td align="right">38.4%</td>
<td align="right">34,872</td>
<td align="right">37.6%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,320</td>
<td align="right">3.5%</td>
<td align="right">3,220</td>
<td align="right">3.5%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">319</td>
<td align="right">0.3%</td>
<td align="right">320</td>
<td align="right">0.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,564</td>
<td align="right">10.1%</td>
<td align="right">9,571</td>
<td align="right">10.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,139</td>
<td align="right">10.7%</td>
<td align="right">10,135</td>
<td align="right">10.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,300</td>
<td align="right">7.7%</td>
<td align="right">7,300</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,480</td>
<td align="right">6.8%</td>
<td align="right">6,480</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,520</td>
<td align="right">5.8%</td>
<td align="right">5,520</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,840</td>
<td align="right">4.1%</td>
<td align="right">3,840</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,980</td>
<td align="right">2.1%</td>
<td align="right">1,980</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,360</td>
<td align="right">1.4%</td>
<td align="right">1,360</td>
<td align="right">1.5%</td>
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
<td align="right">1,226,078,273</td>
<td align="right">7.9%</td>
<td align="right">1,177,587,752</td>
<td align="right">7.8%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,372,784,654</td>
<td align="right">92.1%</td>
<td align="right">13,827,456,047</td>
<td align="right">92.1%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">246,706,700</td>
<td align="right">1.6%</td>
<td align="right">246,626,653</td>
<td align="right">1.6%</td>
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
<td align="left">Failure</td>
<td align="right">793,878</td>
<td align="right">13.3%</td>
<td align="right">770,945</td>
<td align="right">12.9%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,194,786</td>
<td align="right">86.7%</td>
<td align="right">5,189,326</td>
<td align="right">87.1%</td>
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
<td align="left">class method obj</td>
<td align="right">14,280</td>
<td align="right">1.8%</td>
<td align="right">13,020</td>
<td align="right">1.7%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">149,844</td>
<td align="right">18.9%</td>
<td align="right">141,116</td>
<td align="right">18.3%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">267,272</td>
<td align="right">33.7%</td>
<td align="right">257,216</td>
<td align="right">33.4%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">79,261</td>
<td align="right">10.0%</td>
<td align="right">76,725</td>
<td align="right">10.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">19,860</td>
<td align="right">2.5%</td>
<td align="right">19,740</td>
<td align="right">2.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">13,471</td>
<td align="right">1.7%</td>
<td align="right">13,434</td>
<td align="right">1.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">45,651</td>
<td align="right">5.8%</td>
<td align="right">45,551</td>
<td align="right">5.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">73,118</td>
<td align="right">9.2%</td>
<td align="right">73,035</td>
<td align="right">9.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,784</td>
<td align="right">0.7%</td>
<td align="right">5,782</td>
<td align="right">0.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">54,637</td>
<td align="right">6.9%</td>
<td align="right">54,626</td>
<td align="right">7.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,800</td>
<td align="right">3.4%</td>
<td align="right">26,800</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,760</td>
<td align="right">2.0%</td>
<td align="right">15,760</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.5%</td>
<td align="right">12,240</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">11,360</td>
<td align="right">1.4%</td>
<td align="right">11,360</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,780</td>
<td align="right">0.4%</td>
<td align="right">2,780</td>
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
<td align="right">5,312,614,470</td>
<td align="right">99.6%</td>
<td align="right">4,999,812,823</td>
<td align="right">99.6%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">444,211</td>
<td align="right">0.0%</td>
<td align="right">444,773</td>
<td align="right">0.0%</td>
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
<td align="right">20,304,622</td>
<td align="right">0.4%</td>
<td align="right">20,300,754</td>
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
<td align="right">11,340</td>
<td align="right">0.0%</td>
<td align="right">11,340</td>
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
<td align="right">445,080</td>
<td align="right">100.0%</td>
<td align="right">440,722</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">83,635,716</td>
<td align="right">100.0%</td>
<td align="right">43,581,094</td>
<td align="right">100.0%</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,127</td>
<td align="right">0.0%</td>
<td align="right">8,085</td>
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
<td align="right">7,880</td>
<td align="right">100.0%</td>
<td align="right">7,840</td>
<td align="right">100.0%</td>
<td align="right">-0.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">786,185,459</td>
<td align="right">81.9%</td>
<td align="right">786,185,543</td>
<td align="right">81.9%</td>
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
<td align="right">173,284,190</td>
<td align="right">18.1%</td>
<td align="right">173,284,198</td>
<td align="right">18.1%</td>
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
<td align="right">5,420</td>
<td align="right">8.3%</td>
<td align="right">5,420</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,679,441,990</td>
<td align="right">96.4%</td>
<td align="right">2,589,856,051</td>
<td align="right">96.3%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">99,388,359</td>
<td align="right">3.6%</td>
<td align="right">98,660,754</td>
<td align="right">3.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">68,523,995</td>
<td align="right">2.5%</td>
<td align="right">68,515,760</td>
<td align="right">2.5%</td>
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
<td align="right">71,492</td>
<td align="right">4.9%</td>
<td align="right">71,088</td>
<td align="right">4.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,383,374</td>
<td align="right">95.1%</td>
<td align="right">1,382,715</td>
<td align="right">95.1%</td>
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
<td align="left">property</td>
<td align="right">3,080</td>
<td align="right">4.3%</td>
<td align="right">2,940</td>
<td align="right">4.1%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,740</td>
<td align="right">12.2%</td>
<td align="right">8,580</td>
<td align="right">12.1%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,840</td>
<td align="right">19.4%</td>
<td align="right">13,760</td>
<td align="right">19.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,880</td>
<td align="right">6.8%</td>
<td align="right">4,860</td>
<td align="right">6.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">16,732</td>
<td align="right">23.4%</td>
<td align="right">16,728</td>
<td align="right">23.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">10,260</td>
<td align="right">14.4%</td>
<td align="right">10,260</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,740</td>
<td align="right">6.6%</td>
<td align="right">4,740</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,360</td>
<td align="right">6.1%</td>
<td align="right">4,360</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3,940</td>
<td align="right">5.5%</td>
<td align="right">3,940</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">800</td>
<td align="right">1.1%</td>
<td align="right">800</td>
<td align="right">1.1%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">64,680,471</td>
<td align="right">7.3%</td>
<td align="right">59,860,840</td>
<td align="right">6.9%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">820,321,947</td>
<td align="right">92.7%</td>
<td align="right">813,400,986</td>
<td align="right">93.1%</td>
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
<td align="right">52,570</td>
<td align="right">82.7%</td>
<td align="right">49,980</td>
<td align="right">82.2%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,022</td>
<td align="right">17.3%</td>
<td align="right">10,802</td>
<td align="right">17.8%</td>
<td align="right">-2.0%</td>
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
<td align="right">10,150</td>
<td align="right">19.3%</td>
<td align="right">7,559</td>
<td align="right">15.1%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">33,100</td>
<td align="right">63.0%</td>
<td align="right">33,101</td>
<td align="right">66.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">12.3%</td>
<td align="right">6,480</td>
<td align="right">13.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,140</td>
<td align="right">2.2%</td>
<td align="right">1,140</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">900</td>
<td align="right">1.7%</td>
<td align="right">900</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">800</td>
<td align="right">1.5%</td>
<td align="right">800</td>
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
<td align="right">273,777,889</td>
<td align="right">4.5%</td>
<td align="right">268,762,600</td>
<td align="right">4.5%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,796,825,770</td>
<td align="right">95.5%</td>
<td align="right">5,745,611,899</td>
<td align="right">95.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,002,319</td>
<td align="right">0.8%</td>
<td align="right">48,969,904</td>
<td align="right">0.8%</td>
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
<td align="right">175,856</td>
<td align="right">13.7%</td>
<td align="right">174,297</td>
<td align="right">13.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,108,250</td>
<td align="right">86.3%</td>
<td align="right">1,106,900</td>
<td align="right">86.4%</td>
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
<td align="left">dict</td>
<td align="right">13,580</td>
<td align="right">7.7%</td>
<td align="right">12,200</td>
<td align="right">7.0%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,610</td>
<td align="right">2.6%</td>
<td align="right">4,586</td>
<td align="right">2.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">4,716</td>
<td align="right">2.7%</td>
<td align="right">4,702</td>
<td align="right">2.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">14,724</td>
<td align="right">8.4%</td>
<td align="right">14,687</td>
<td align="right">8.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">48,162</td>
<td align="right">27.4%</td>
<td align="right">48,062</td>
<td align="right">27.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,112</td>
<td align="right">15.4%</td>
<td align="right">27,109</td>
<td align="right">15.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">46,273</td>
<td align="right">26.3%</td>
<td align="right">46,272</td>
<td align="right">26.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,759</td>
<td align="right">7.8%</td>
<td align="right">13,759</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,493,779,281</td>
<td align="right">100.0%</td>
<td align="right">1,198,426,396</td>
<td align="right">100.0%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">215,366</td>
<td align="right">0.0%</td>
<td align="right">215,049</td>
<td align="right">0.0%</td>
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
<td align="right">27,112</td>
<td align="right">92.9%</td>
<td align="right">26,696</td>
<td align="right">92.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,076</td>
<td align="right">7.1%</td>
<td align="right">2,075</td>
<td align="right">7.2%</td>
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
<td align="right">1,436</td>
<td align="right">69.2%</td>
<td align="right">1,435</td>
<td align="right">69.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">18.3%</td>
<td align="right">380</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">12.5%</td>
<td align="right">260</td>
<td align="right">12.5%</td>
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
<td align="right">57,814,462,243</td>
<td align="right">54.6%</td>
<td align="right">53,928,697,628</td>
<td align="right">54.1%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">37,553,814,048</td>
<td align="right">35.5%</td>
<td align="right">35,614,834,011</td>
<td align="right">35.7%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,838,296,992</td>
<td align="right">9.3%</td>
<td align="right">9,457,216,328</td>
<td align="right">9.5%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">675,868,882</td>
<td align="right">0.6%</td>
<td align="right">670,358,931</td>
<td align="right">0.7%</td>
<td align="right">-0.8%</td>
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
<td align="right">420,526,157</td>
<td align="right">12.4%</td>
<td align="right">336,171,189</td>
<td align="right">10.7%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">419,503,797</td>
<td align="right">12.4%</td>
<td align="right">349,034,189</td>
<td align="right">11.1%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,226,078,273</td>
<td align="right">36.3%</td>
<td align="right">1,177,587,752</td>
<td align="right">37.3%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">76,349,763</td>
<td align="right">2.3%</td>
<td align="right">74,291,370</td>
<td align="right">2.4%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">310,686,616</td>
<td align="right">9.2%</td>
<td align="right">304,100,542</td>
<td align="right">9.6%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">273,777,889</td>
<td align="right">8.1%</td>
<td align="right">268,762,600</td>
<td align="right">8.5%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">198,489,744</td>
<td align="right">5.9%</td>
<td align="right">196,011,201</td>
<td align="right">6.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">98,611,692</td>
<td align="right">2.9%</td>
<td align="right">97,435,045</td>
<td align="right">3.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">99,388,359</td>
<td align="right">2.9%</td>
<td align="right">98,660,754</td>
<td align="right">3.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,190</td>
<td align="right">5.1%</td>
<td align="right">173,284,198</td>
<td align="right">5.5%</td>
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
<td align="right">92,996,984</td>
<td align="right">12.3%</td>
<td align="right">88,998,037</td>
<td align="right">11.9%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,511,448</td>
<td align="right">3.6%</td>
<td align="right">26,616,745</td>
<td align="right">3.6%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">39,116,638</td>
<td align="right">5.2%</td>
<td align="right">38,986,045</td>
<td align="right">5.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,206,775</td>
<td align="right">3.3%</td>
<td align="right">25,200,460</td>
<td align="right">3.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,297,920</td>
<td align="right">5.7%</td>
<td align="right">43,296,000</td>
<td align="right">5.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,959,963</td>
<td align="right">5.4%</td>
<td align="right">40,958,275</td>
<td align="right">5.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">73,013,700</td>
<td align="right">9.7%</td>
<td align="right">73,012,849</td>
<td align="right">9.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,874,558</td>
<td align="right">10.3%</td>
<td align="right">77,874,272</td>
<td align="right">10.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,874,558</td>
<td align="right">10.3%</td>
<td align="right">77,874,272</td>
<td align="right">10.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">100,617,331</td>
<td align="right">13.3%</td>
<td align="right">100,617,078</td>
<td align="right">13.4%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,469,989</td>
<td align="right">10.6%</td>
<td align="right">434,720,245</td>
<td align="right">5.9%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,389,211,582</td>
<td align="right">29.5%</td>
<td align="right">1,905,500,031</td>
<td align="right">26.0%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,389,211,582</td>
<td align="right">29.5%</td>
<td align="right">1,905,500,031</td>
<td align="right">26.0%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">527,055,583</td>
<td align="right">6.5%</td>
<td align="right">483,788,400</td>
<td align="right">6.6%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,391,846,733</td>
<td align="right">78.9%</td>
<td align="right">6,062,471,397</td>
<td align="right">82.6%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,707,348,942</td>
<td align="right">70.5%</td>
<td align="right">5,435,781,321</td>
<td align="right">74.0%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,524,307,153</td>
<td align="right">18.8%</td>
<td align="right">1,466,345,346</td>
<td align="right">20.0%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,528,741,593</td>
<td align="right">18.9%</td>
<td align="right">1,470,779,786</td>
<td align="right">20.0%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">225,336,917</td>
<td align="right">2.8%</td>
<td align="right">222,892,729</td>
<td align="right">3.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,666,988</td>
<td align="right">0.9%</td>
<td align="right">71,280,094</td>
<td align="right">1.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">28,603,285</td>
<td align="right">0.4%</td>
<td align="right">28,603,105</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,380,864</td>
<td align="right">2.6%</td>
<td align="right">211,380,938</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,411,640</td>
<td align="right">0.1%</td>
<td align="right">4,411,640</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">22,800</td>
<td align="right">0.0%</td>
<td align="right">22,800</td>
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
<td align="left">Increfs</td>
<td align="right">67,019,047,845</td>
<td align="right">59.1%</td>
<td align="right">61,138,654,126</td>
<td align="right">58.3%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">69,731,903,346</td>
<td align="right">53.7%</td>
<td align="right">63,769,247,131</td>
<td align="right">53.1%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,467,581,832</td>
<td align="right"></td>
<td align="right">5,946,014,796</td>
<td align="right"></td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,465,786,176</td>
<td align="right">38.4%</td>
<td align="right">5,944,413,002</td>
<td align="right">37.6%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">60,096,013,670</td>
<td align="right">46.3%</td>
<td align="right">56,434,298,270</td>
<td align="right">46.9%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">46,475,741,661</td>
<td align="right">40.9%</td>
<td align="right">43,756,959,216</td>
<td align="right">41.7%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">5,899,953</td>
<td align="right"></td>
<td align="right">5,566,023</td>
<td align="right"></td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,235,885,568</td>
<td align="right">60.8%</td>
<td align="right">9,722,476,055</td>
<td align="right">61.6%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,359,584,417</td>
<td align="right">61.6%</td>
<td align="right">9,845,421,439</td>
<td align="right">62.4%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,690,456,623</td>
<td align="right"></td>
<td align="right">10,174,488,355</td>
<td align="right"></td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,642,161,903</td>
<td align="right"></td>
<td align="right">2,535,069,400</td>
<td align="right"></td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,112,391,839</td>
<td align="right"></td>
<td align="right">3,031,144,856</td>
<td align="right"></td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">28,873,409</td>
<td align="right"></td>
<td align="right">28,558,827</td>
<td align="right"></td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,879,172</td>
<td align="right">0.6%</td>
<td align="right">103,133,494</td>
<td align="right">0.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">150,384,158</td>
<td align="right"></td>
<td align="right">149,836,041</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">23,153,105</td>
<td align="right"></td>
<td align="right">23,169,981</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">19,819,677</td>
<td align="right">0.1%</td>
<td align="right">19,811,890</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,271,100</td>
<td align="right">2.2%</td>
<td align="right">3,271,100</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">63,880</td>
<td align="right">0.0%</td>
<td align="right">63,880</td>
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
<td align="right">19,271,680</td>
<td align="right">14,520,946,101</td>
<td align="right">0</td>
<td align="right">18,599,260</td>
<td align="right">14,397,864,294</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,996,576,600</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,995,511,692</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">438,673</td>
<td align="right">59.3%</td>
<td align="right">347,003</td>
<td align="right">54.3%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">637,128</td>
<td align="right">86.2%</td>
<td align="right">540,764</td>
<td align="right">84.6%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">739,161</td>
<td align="right"></td>
<td align="right">639,168</td>
<td align="right"></td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,048,044,881</td>
<td align="right"></td>
<td align="right">6,209,489,447</td>
<td align="right"></td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">198,119,458,441</td>
<td align="right">2,811.0%</td>
<td align="right">182,133,395,591</td>
<td align="right">2,933.1%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">45,606</td>
<td align="right">6.2%</td>
<td align="right">42,725</td>
<td align="right">6.7%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,529</td>
<td align="right">0.9%</td>
<td align="right">6,290</td>
<td align="right">1.0%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">102,033</td>
<td align="right">13.8%</td>
<td align="right">98,404</td>
<td align="right">15.4%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,194</td>
<td align="right">6.1%</td>
<td align="right">6,181</td>
<td align="right">6.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">821</td>
<td align="right">0.1%</td>
<td align="right">822</td>
<td align="right">0.1%</td>
<td align="right">0.1%</td>
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
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">1,300</td>
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
<td align="right">98,447</td>
<td align="right">96.5%</td>
<td align="right">94,824</td>
<td align="right">96.4%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">102,033</td>
<td align="right"></td>
<td align="right">98,404</td>
<td align="right"></td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,366</td>
<td align="right">2.3%</td>
<td align="right">2,360</td>
<td align="right">2.4%</td>
<td align="right">-0.3%</td>
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
<td align="right">4,579</td>
<td align="right">4.5%</td>
<td align="right">4,419</td>
<td align="right">4.5%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">19,533</td>
<td align="right">19.1%</td>
<td align="right">19,138</td>
<td align="right">19.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">32,369</td>
<td align="right">31.7%</td>
<td align="right">31,445</td>
<td align="right">32.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">24,864</td>
<td align="right">24.4%</td>
<td align="right">23,842</td>
<td align="right">24.2%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,122</td>
<td align="right">12.9%</td>
<td align="right">12,397</td>
<td align="right">12.6%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,986</td>
<td align="right">5.9%</td>
<td align="right">5,643</td>
<td align="right">5.7%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,420</td>
<td align="right">1.4%</td>
<td align="right">1,360</td>
<td align="right">1.4%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">160</td>
<td align="right">0.2%</td>
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
<td align="right">3,679</td>
<td align="right">3.6%</td>
<td align="right">3,539</td>
<td align="right">3.6%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">13,609</td>
<td align="right">13.3%</td>
<td align="right">13,279</td>
<td align="right">13.5%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,775</td>
<td align="right">21.3%</td>
<td align="right">21,385</td>
<td align="right">21.7%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">32,439</td>
<td align="right">31.8%</td>
<td align="right">31,512</td>
<td align="right">32.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">16,124</td>
<td align="right">15.8%</td>
<td align="right">15,129</td>
<td align="right">15.4%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,741</td>
<td align="right">7.6%</td>
<td align="right">7,200</td>
<td align="right">7.3%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,660</td>
<td align="right">2.6%</td>
<td align="right">2,400</td>
<td align="right">2.4%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">420</td>
<td align="right">0.4%</td>
<td align="right">380</td>
<td align="right">0.4%</td>
<td align="right">-9.5%</td>
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
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,400,114</td>
<td align="right">14,116,314</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">93,670,380</td>
<td align="right">21,010,080</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">592,598,219</td>
<td align="right">158,629,713</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,003,040</td>
<td align="right">24,719,262</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">13,606,780</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">93,423,571</td>
<td align="right">29,139,897</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,528,273</td>
<td align="right">29,244,597</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,610,440</td>
<td align="right">1,401,240</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">21,052,720</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">618,354,900</td>
<td align="right">368,177,717</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">133,773,437</td>
<td align="right">87,215,405</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,106,383,621</td>
<td align="right">732,189,966</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,317,833,306</td>
<td align="right">876,001,213</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">760,761,041</td>
<td align="right">512,634,245</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,378,284,778</td>
<td align="right">934,835,416</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,197,960</td>
<td align="right">70,017,443</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">108,946,898</td>
<td align="right">76,204,708</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,705,960</td>
<td align="right">638,896,520</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,339,449,167</td>
<td align="right">982,311,612</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,678,798,660</td>
<td align="right">5,034,590,532</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">154,174,340</td>
<td align="right">116,243,651</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,346,336,774</td>
<td align="right">1,016,643,761</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">382,246,925</td>
<td align="right">295,664,063</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">218,028,794</td>
<td align="right">171,054,208</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">905,037,900</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">342,161,824</td>
<td align="right">272,377,319</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">2,084,173,601</td>
<td align="right">1,708,624,647</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">576,682,472</td>
<td align="right">472,859,455</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">412,358,484</td>
<td align="right">346,528,197</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">410,262,326</td>
<td align="right">347,163,805</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,976,365,576</td>
<td align="right">1,677,671,372</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">173,126,581</td>
<td align="right">147,654,242</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,732,680</td>
<td align="right">22,299,339</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,548,620</td>
<td align="right">163,040,220</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">566,113,384</td>
<td align="right">496,122,968</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">875,579,828</td>
<td align="right">767,840,867</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,070,085</td>
<td align="right">31,194,657</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,746,517,939</td>
<td align="right">4,226,099,402</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,045,330,438</td>
<td align="right">937,604,814</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,812,888,779</td>
<td align="right">10,613,385,639</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,799,033,030</td>
<td align="right">1,617,465,338</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,575,162,369</td>
<td align="right">4,115,686,409</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">13,898,412,755</td>
<td align="right">12,513,928,919</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,865,861,157</td>
<td align="right">1,686,874,444</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,146,545,807</td>
<td align="right">1,037,884,380</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,963,871,280</td>
<td align="right">4,500,864,800</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,981,545,211</td>
<td align="right">1,801,867,000</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,246,600,087</td>
<td align="right">1,137,938,660</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,265,093,207</td>
<td align="right">1,156,431,780</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">947,935,548</td>
<td align="right">868,037,809</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,547,508</td>
<td align="right">672,467,612</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">780,161,746</td>
<td align="right">715,451,986</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">63,283,615</td>
<td align="right">58,059,370</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,624,426</td>
<td align="right">715,451,986</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,114,429,882</td>
<td align="right">1,024,305,343</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,508,827,006</td>
<td align="right">5,984,835,214</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,204,149,654</td>
<td align="right">2,949,049,082</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,319,222</td>
<td align="right">29,763,188</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,228,206</td>
<td align="right">9,470,197</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,278,622,368</td>
<td align="right">2,114,213,379</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,251,913,488</td>
<td align="right">2,090,937,840</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,667,514,569</td>
<td align="right">1,552,928,955</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">73,948,619</td>
<td align="right">69,122,811</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">140,198,408</td>
<td align="right">131,970,643</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,126,442,355</td>
<td align="right">6,708,793,290</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,389,961,382</td>
<td align="right">1,311,027,711</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,537,583,138</td>
<td align="right">2,405,399,779</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">552,073,151</td>
<td align="right">523,812,894</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,182,445,977</td>
<td align="right">2,073,932,273</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,873,874,763</td>
<td align="right">1,783,572,187</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,042,042,853</td>
<td align="right">992,503,295</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,274,927,977</td>
<td align="right">1,216,160,759</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,553,591,696</td>
<td align="right">1,482,552,261</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">213,616,900</td>
<td align="right">204,136,100</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,312,809,046</td>
<td align="right">3,173,468,775</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,367,111,663</td>
<td align="right">1,310,185,968</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,418,864,569</td>
<td align="right">1,366,377,134</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">101,012,378</td>
<td align="right">97,583,026</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">101,256,498</td>
<td align="right">97,827,146</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,503,656,275</td>
<td align="right">6,284,664,141</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,743,423,583</td>
<td align="right">5,573,091,934</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,183,195,393</td>
<td align="right">2,121,018,727</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,957,649,759</td>
<td align="right">2,875,060,473</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,653,306,162</td>
<td align="right">1,607,553,879</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,820,019,322</td>
<td align="right">2,743,260,944</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,238,392,632</td>
<td align="right">1,205,855,723</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">542,014,313</td>
<td align="right">527,961,527</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,608,491,182</td>
<td align="right">9,362,342,551</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">118,845,829</td>
<td align="right">115,983,270</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,015,024,784</td>
<td align="right">994,293,542</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">224,369,591</td>
<td align="right">220,388,957</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">30,054,839</td>
<td align="right">29,525,708</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">112,617,461</td>
<td align="right">110,654,326</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">688,103,385</td>
<td align="right">678,627,054</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">198,246,926</td>
<td align="right">195,525,212</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">329,223,770</td>
<td align="right">325,098,625</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,604,465,777</td>
<td align="right">3,564,312,920</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,050,298,051</td>
<td align="right">1,039,837,183</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,234,991,206</td>
<td align="right">2,213,573,539</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">713,629,564</td>
<td align="right">706,953,491</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,489,195</td>
<td align="right">125,310,260</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">485,541,171</td>
<td align="right">481,150,218</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,719,120</td>
<td align="right">505,271,620</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">334,177,456</td>
<td align="right">331,558,187</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,321,837,392</td>
<td align="right">1,312,141,045</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">485,613,722</td>
<td align="right">482,449,725</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,455,391,596</td>
<td align="right">3,432,975,197</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,646,101,837</td>
<td align="right">2,629,677,492</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">115,717,314</td>
<td align="right">115,025,816</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">244,191,168</td>
<td align="right">242,735,666</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">264,379,459</td>
<td align="right">263,099,620</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">265,606,279</td>
<td align="right">264,326,440</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">186,024,957</td>
<td align="right">185,216,126</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">446,888</td>
<td align="right">444,974</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">185,748,655</td>
<td align="right">184,956,345</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">188,277,697</td>
<td align="right">187,485,440</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">225,196,726</td>
<td align="right">224,326,148</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,875,490</td>
<td align="right">4,856,665</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">230,436,840</td>
<td align="right">229,728,500</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">199,684,291</td>
<td align="right">199,073,144</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">63,424,340</td>
<td align="right">63,238,740</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">959,972,158</td>
<td align="right">958,326,937</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,820,235,583</td>
<td align="right">1,817,716,310</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">724,080,692</td>
<td align="right">723,087,065</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">686,635,304</td>
<td align="right">685,760,951</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">128,702,767</td>
<td align="right">128,540,732</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">129,897,927</td>
<td align="right">129,735,892</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,094,572,664</td>
<td align="right">2,092,188,715</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">360,204,848</td>
<td align="right">359,795,230</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">400,249,408</td>
<td align="right">399,839,790</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">20,517,860</td>
<td align="right">20,499,060</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,412,790</td>
<td align="right">134,290,486</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,412,790</td>
<td align="right">134,290,486</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">232,174,683</td>
<td align="right">231,997,793</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">16,603,206</td>
<td align="right">16,591,513</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">168,379,994</td>
<td align="right">168,270,435</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">424,106,129</td>
<td align="right">423,851,890</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">129,284,934</td>
<td align="right">129,212,241</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,871,246</td>
<td align="right">1,335,131,943</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">35,252,540</td>
<td align="right">35,233,740</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">330,516,642</td>
<td align="right">330,366,736</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,578,954</td>
<td align="right">45,569,838</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">966,713,012</td>
<td align="right">966,537,390</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">588,353,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">66,194,480</td>
<td align="right">66,184,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,959,100</td>
<td align="right">144,940,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">64,879,220</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">315,041,515</td>
<td align="right">315,070,522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">109,975,322</td>
<td align="right">109,983,591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">7,112,067</td>
<td align="right">7,111,668</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,940</td>
<td align="right">6,583,580</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,756,351</td>
<td align="right">229,768,750</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">790,394,308</td>
<td align="right">790,368,919</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,638,020</td>
<td align="right">384,630,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,173,209</td>
<td align="right">203,169,823</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">145,316,580</td>
<td align="right">145,314,521</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">843,498,099</td>
<td align="right">843,508,673</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">280,605,796</td>
<td align="right">280,602,830</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">112,354,258</td>
<td align="right">112,353,099</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,580,380</td>
<td align="right">80,579,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">647,415</td>
<td align="right">647,419</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">4,437,028</td>
<td align="right">4,437,053</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,041,400</td>
<td align="right">22,041,286</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,898,160</td>
<td align="right">61,898,000</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">227,832,414</td>
<td align="right">227,832,958</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,197,789</td>
<td align="right">97,197,984</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,156,349</td>
<td align="right">98,156,544</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,387,018</td>
<td align="right">11,387,030</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,387,018</td>
<td align="right">11,387,030</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,316,060</td>
<td align="right">54,316,006</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,913,165</td>
<td align="right">68,913,197</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,914,078</td>
<td align="right">9,914,075</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">936,678,789</td>
<td align="right">936,678,528</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">24,825,568</td>
<td align="right">24,825,562</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">55,151,978</td>
<td align="right">55,151,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,831,940</td>
<td align="right">101,831,923</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">147,753,290</td>
<td align="right">147,753,293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,180</td>
<td align="right">645,067,183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,071,320</td>
<td align="right">533,071,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,039,140</td>
<td align="right">199,039,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,868,340</td>
<td align="right">149,868,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">99,651,520</td>
<td align="right">99,651,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">61,350,440</td>
<td align="right">61,350,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">61,236,920</td>
<td align="right">61,236,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">14,734,660</td>
<td align="right">14,734,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,693,200</td>
<td align="right">12,693,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,133,860</td>
<td align="right">8,133,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,660,000</td>
<td align="right">5,660,000</td>
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
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,116,480</td>
<td align="right">2,116,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,943,300</td>
<td align="right">1,943,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,889,580</td>
<td align="right">1,889,580</td>
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
<td align="left">_STORE_NAME</td>
<td align="right">543,660</td>
<td align="right">543,660</td>
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
<td align="right">71,760</td>
<td align="right">71,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">34,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">29,920</td>
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
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,300</td>
<td align="right">1,760</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">820</td>
<td align="right">720</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">29,160</td>
<td align="right">27,640</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">500</td>
<td align="right">480</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,160</td>
<td align="right">5,000</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">83,294</td>
<td align="right">81,293</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">1,568</td>
<td align="right">1,560</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,602</td>
<td align="right">6,595</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,398</td>
<td align="right">2,396</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40,581</td>
<td align="right">40,590</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">32,220</td>
<td align="right">32,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,660</td>
<td align="right">1,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,340</td>
<td align="right">1,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">540</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">260</td>
<td align="right">260</td>
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
<td align="right">1,086</td>
<td align="right">1,081</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,086</td>
<td align="right">1,081</td>
<td align="right">-0.5%</td>
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
<td align="right">1,900</td>
<td align="right">1,860</td>
<td align="right">-2.1%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-05-21
