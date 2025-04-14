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
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,471,541</td>
<td align="right">15,379,188</td>
<td align="right">522.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">18,993,974</td>
<td align="right">71,158,443</td>
<td align="right">274.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,721,306</td>
<td align="right">20,240,687</td>
<td align="right">253.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">15,314,128</td>
<td align="right">30,875,846</td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">189,354</td>
<td align="right">121</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">16,993</td>
<td align="right">73</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,518</td>
<td align="right">7,418</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">338,565</td>
<td align="right">3,575</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,036,043</td>
<td align="right">16,324</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">881,841</td>
<td align="right">14,719</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">147,534</td>
<td align="right">2,607</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">89,010</td>
<td align="right">1,611</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">389,282</td>
<td align="right">7,709</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">178,534</td>
<td align="right">3,736</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">178,536</td>
<td align="right">3,738</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,741</td>
<td align="right">5,277</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,182,264</td>
<td align="right">165,645</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,390</td>
<td align="right">4,748</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">597,611</td>
<td align="right">20,288</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,740,085</td>
<td align="right">750,831</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">23,554</td>
<td align="right">1,014</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,396</td>
<td align="right">67,169</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,729</td>
<td align="right">243,502</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,521,804</td>
<td align="right">85,605</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,028,341</td>
<td align="right">66,223</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,028,946</td>
<td align="right">66,528</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,588</td>
<td align="right">62,080</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,911,564</td>
<td align="right">1,094,818</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,401</td>
<td align="right">51,977</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">29,765,219</td>
<td align="right">3,128,894</td>
<td align="right">-89.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,214</td>
<td align="right">718,968</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">18,590,834</td>
<td align="right">2,286,161</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">78,652</td>
<td align="right">10,580</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,587,487</td>
<td align="right">649,627</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">17,504,005</td>
<td align="right">32,507,004</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,223,067</td>
<td align="right">175,988</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,179</td>
<td align="right">345,398</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">14,629</td>
<td align="right">2,267</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,610,107</td>
<td align="right">825,053</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,331</td>
<td align="right">136,689</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">20,680</td>
<td align="right">3,808</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,787,250</td>
<td align="right">338,423</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">17,704,319</td>
<td align="right">3,366,114</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">394</td>
<td align="right">78</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">42,394,686</td>
<td align="right">8,673,564</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,039,005</td>
<td align="right">1,156,195</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,500,579</td>
<td align="right">2,456,172</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">456,454</td>
<td align="right">107,920</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,091,434</td>
<td align="right">6,740,518</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,209</td>
<td align="right">10,165</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">8,858</td>
<td align="right">2,367</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,069,652</td>
<td align="right">598,700</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">102</td>
<td align="right">30</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,227,995</td>
<td align="right">1,865,457</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">489,144</td>
<td align="right">152,464</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,728,177</td>
<td align="right">6,228,947</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,914</td>
<td align="right">129,158</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,568,892</td>
<td align="right">5,330,115</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">129,473</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">48,649,895</td>
<td align="right">17,465,532</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,966,373</td>
<td align="right">741,933</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,516,988</td>
<td align="right">2,889,460</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">140,594,268</td>
<td align="right">54,224,162</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,430,960</td>
<td align="right">1,323,983</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">42,949,454</td>
<td align="right">17,040,759</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,588,314</td>
<td align="right">1,079,019</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,589,857</td>
<td align="right">2,778,787</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,058,151</td>
<td align="right">6,831,177</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">158,260,913</td>
<td align="right">67,491,823</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,573,317</td>
<td align="right">52,784,904</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,045,361</td>
<td align="right">6,939,046</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">20,335,118</td>
<td align="right">8,794,339</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,431,585</td>
<td align="right">1,489,020</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">60,514,478</td>
<td align="right">26,653,164</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">591</td>
<td align="right">261</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">19,944,377</td>
<td align="right">8,878,816</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,843,343</td>
<td align="right">14,795,764</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,439,141</td>
<td align="right">1,551,221</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,753,256</td>
<td align="right">2,617,354</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">190,605,914</td>
<td align="right">86,786,568</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,643,224</td>
<td align="right">3,037,649</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,872</td>
<td align="right">342,431</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,128</td>
<td align="right">303,099</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">255</td>
<td align="right">120</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,401,044</td>
<td align="right">4,061,673</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">171,648,389</td>
<td align="right">83,819,779</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,216</td>
<td align="right">2,205,681</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">114,629,873</td>
<td align="right">56,954,078</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,999,648</td>
<td align="right">3,005,783</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">15,281,308</td>
<td align="right">7,687,230</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">103,959,327</td>
<td align="right">53,264,834</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">202,742,035</td>
<td align="right">104,458,860</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">8,943</td>
<td align="right">4,636</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">13,589,972</td>
<td align="right">7,100,356</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">18,509,013</td>
<td align="right">9,704,892</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD_METHOD</td>
<td align="right">1,323,166</td>
<td align="right">694,615</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">182,138,684</td>
<td align="right">97,215,010</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,843,307</td>
<td align="right">19,259,179</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">595,651,897</td>
<td align="right">331,104,841</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,645</td>
<td align="right">1,553</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">55,971,064</td>
<td align="right">32,904,077</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">5,058,947</td>
<td align="right">3,022,505</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">172,036</td>
<td align="right">102,846</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">46,432,755</td>
<td align="right">27,890,762</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">85,032,582</td>
<td align="right">51,277,456</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">23,392,537</td>
<td align="right">14,215,031</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,679</td>
<td align="right">1,024</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">16,263,991</td>
<td align="right">9,984,296</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,199,854</td>
<td align="right">1,384,474</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">171,315,398</td>
<td align="right">108,166,971</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">29,888,685</td>
<td align="right">18,999,952</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">30,246,337</td>
<td align="right">19,540,648</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,759,239</td>
<td align="right">1,142,656</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">25,968,385</td>
<td align="right">16,867,122</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">49,908,003</td>
<td align="right">33,455,768</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">43,431,025</td>
<td align="right">29,873,466</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,097,982</td>
<td align="right">14,555,836</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,313,511</td>
<td align="right">29,140,246</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">447</td>
<td align="right">316</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,106,738</td>
<td align="right">8,608,031</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,846,212</td>
<td align="right">12,694,496</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,622,932</td>
<td align="right">4,920,489</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,639</td>
<td align="right">3,197,130</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">15,599,633</td>
<td align="right">11,964,018</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">40,223,549</td>
<td align="right">32,181,793</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">12,801,580</td>
<td align="right">10,362,588</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">13,518,418</td>
<td align="right">11,238,382</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,128</td>
<td align="right">548,851</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,128</td>
<td align="right">548,851</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,578,735</td>
<td align="right">3,885,547</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,550,121</td>
<td align="right">3,024,800</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,253</td>
<td align="right">151,626</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">133,724</td>
<td align="right">116,982</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,087</td>
<td align="right">74,217</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,773,855</td>
<td align="right">16,253,603</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">44,053,482</td>
<td align="right">40,424,269</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,939,029</td>
<td align="right">9,123,426</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,055</td>
<td align="right">971</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,442</td>
<td align="right">1,615,968</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,877,031</td>
<td align="right">10,973,143</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,550</td>
<td align="right">396,458</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,455</td>
<td align="right">1,371</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">23,070,003</td>
<td align="right">21,952,824</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,167</td>
<td align="right">2,091,838</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">61,484,375</td>
<td align="right">58,817,921</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">258,802</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,381</td>
<td align="right">627,463</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">41,986,619</td>
<td align="right">40,375,572</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,961,921</td>
<td align="right">94,698,767</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,185,119</td>
<td align="right">12,868,285</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,675,958</td>
<td align="right">2,613,126</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,038</td>
<td align="right">17,655</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,964,338</td>
<td align="right">11,166,193</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,976,767</td>
<td align="right">21,594,048</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,442</td>
<td align="right">1,446</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,872</td>
<td align="right">9,895</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,160</td>
<td align="right">24,193</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,959</td>
<td align="right">2,961</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">70,915,301</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">1,409,624</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">9,212</td>
<td align="right">9,212</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,941</td>
<td align="right">8,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,742</td>
<td align="right">3,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">133</td>
<td align="right">133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_LAZY_DICT</td>
<td align="right">92</td>
<td align="right">92</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD</td>
<td align="right">50</td>
<td align="right">50</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">10</td>
<td align="right">10</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
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
<td align="right">27,071,021</td>
<td align="right">65.0%</td>
<td align="right">6,730,559</td>
<td align="right">35.8%</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,576,344</td>
<td align="right">35.0%</td>
<td align="right">12,048,168</td>
<td align="right">64.1%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">123</td>
<td align="right">0.0%</td>
<td align="right">-2.4%</td>
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
<td align="right">19,134</td>
<td align="right">93.7%</td>
<td align="right">8,668</td>
<td align="right">87.0%</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,279</td>
<td align="right">6.3%</td>
<td align="right">1,291</td>
<td align="right">13.0%</td>
<td align="right">0.9%</td>
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
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">11.6%</td>
<td align="right">38</td>
<td align="right">0.4%</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">189</td>
<td align="right">1.0%</td>
<td align="right">8</td>
<td align="right">0.1%</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.5%</td>
<td align="right">29</td>
<td align="right">0.3%</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,288</td>
<td align="right">6.7%</td>
<td align="right">435</td>
<td align="right">5.0%</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,208</td>
<td align="right">6.3%</td>
<td align="right">408</td>
<td align="right">4.7%</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,891</td>
<td align="right">15.1%</td>
<td align="right">987</td>
<td align="right">11.4%</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.8%</td>
<td align="right">70</td>
<td align="right">0.8%</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">5.1%</td>
<td align="right">467</td>
<td align="right">5.4%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">16.8%</td>
<td align="right">1,547</td>
<td align="right">17.8%</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">5.7%</td>
<td align="right">555</td>
<td align="right">6.4%</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">570</td>
<td align="right">3.0%</td>
<td align="right">296</td>
<td align="right">3.4%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">704</td>
<td align="right">3.7%</td>
<td align="right">478</td>
<td align="right">5.5%</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">716</td>
<td align="right">3.7%</td>
<td align="right">508</td>
<td align="right">5.9%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,008</td>
<td align="right">5.3%</td>
<td align="right">721</td>
<td align="right">8.3%</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">211</td>
<td align="right">1.1%</td>
<td align="right">152</td>
<td align="right">1.8%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,226</td>
<td align="right">11.6%</td>
<td align="right">1,673</td>
<td align="right">19.3%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.9%</td>
<td align="right">296</td>
<td align="right">3.4%</td>
<td align="right">-18.5%</td>
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
<td align="right">8,858</td>
<td align="right">100.0%</td>
<td align="right">2,367</td>
<td align="right">100.0%</td>
<td align="right">-73.3%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,750</td>
<td align="right">0.0%</td>
<td align="right">4,378</td>
<td align="right">0.0%</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,395,029</td>
<td align="right">20.4%</td>
<td align="right">4,057,827</td>
<td align="right">12.9%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,778,633</td>
<td align="right">79.6%</td>
<td align="right">27,445,685</td>
<td align="right">87.1%</td>
<td align="right">-16.3%</td>
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
<td align="right">5,233</td>
<td align="right">84.2%</td>
<td align="right">3,071</td>
<td align="right">78.3%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">982</td>
<td align="right">15.8%</td>
<td align="right">849</td>
<td align="right">21.7%</td>
<td align="right">-13.5%</td>
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
<td align="right">689</td>
<td align="right">13.2%</td>
<td align="right">216</td>
<td align="right">7.0%</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,702</td>
<td align="right">70.7%</td>
<td align="right">2,229</td>
<td align="right">72.6%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">271</td>
<td align="right">5.2%</td>
<td align="right">165</td>
<td align="right">5.4%</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">148</td>
<td align="right">2.8%</td>
<td align="right">103</td>
<td align="right">3.4%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">8.1%</td>
<td align="right">357</td>
<td align="right">11.6%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">13,673</td>
<td align="right">0.0%</td>
<td align="right">5,676</td>
<td align="right">0.0%</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,851,673</td>
<td align="right">7.7%</td>
<td align="right">22,106,601</td>
<td align="right">7.3%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">296,131,782</td>
<td align="right">92.3%</td>
<td align="right">281,440,747</td>
<td align="right">92.7%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,429</td>
<td align="right">0.0%</td>
<td align="right">8,442</td>
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
<td align="left">Success</td>
<td align="right">484,465</td>
<td align="right">100.0%</td>
<td align="right">432,524</td>
<td align="right">100.0%</td>
<td align="right">-10.7%</td>
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
<td align="right">2,805</td>
<td align="right">66.0%</td>
<td align="right">2,619</td>
<td align="right">64.4%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">399</td>
<td align="right">9.4%</td>
<td align="right">399</td>
<td align="right">9.8%</td>
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
<td align="right">1,064</td>
<td align="right">100.0%</td>
<td align="right">1,047</td>
<td align="right">100.0%</td>
<td align="right">-1.6%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">409,664</td>
<td align="right">0.5%</td>
<td align="right">66,383</td>
<td align="right">0.1%</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">25,930,916</td>
<td align="right">33.5%</td>
<td align="right">16,851,627</td>
<td align="right">26.9%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,030,237</td>
<td align="right">65.9%</td>
<td align="right">45,696,462</td>
<td align="right">73.0%</td>
<td align="right">-10.5%</td>
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
<td align="right">8,839</td>
<td align="right">19.6%</td>
<td align="right">2,354</td>
<td align="right">14.1%</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">36,303</td>
<td align="right">80.4%</td>
<td align="right">14,324</td>
<td align="right">85.9%</td>
<td align="right">-60.5%</td>
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
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">20.6%</td>
<td align="right">206</td>
<td align="right">1.4%</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,158</td>
<td align="right">8.7%</td>
<td align="right">707</td>
<td align="right">4.9%</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">403</td>
<td align="right">1.1%</td>
<td align="right">111</td>
<td align="right">0.8%</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,104</td>
<td align="right">38.9%</td>
<td align="right">5,812</td>
<td align="right">40.6%</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,228</td>
<td align="right">11.6%</td>
<td align="right">1,926</td>
<td align="right">13.4%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">135</td>
<td align="right">0.4%</td>
<td align="right">91</td>
<td align="right">0.6%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">69</td>
<td align="right">0.5%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,408</td>
<td align="right">17.7%</td>
<td align="right">5,150</td>
<td align="right">36.0%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">114</td>
<td align="right">0.3%</td>
<td align="right">92</td>
<td align="right">0.6%</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">116</td>
<td align="right">0.8%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">44</td>
<td align="right">0.1%</td>
<td align="right">44</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">512</td>
<td align="right">0.0%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,574,799</td>
<td align="right">16.3%</td>
<td align="right">3,882,512</td>
<td align="right">14.9%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,561</td>
<td align="right">83.7%</td>
<td align="right">22,168,642</td>
<td align="right">85.1%</td>
<td align="right">-5.7%</td>
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
<td align="right">3,814</td>
<td align="right">96.9%</td>
<td align="right">2,914</td>
<td align="right">96.0%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">122</td>
<td align="right">3.1%</td>
<td align="right">121</td>
<td align="right">4.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">299</td>
<td align="right">7.8%</td>
<td align="right">121</td>
<td align="right">4.2%</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,471</td>
<td align="right">38.6%</td>
<td align="right">758</td>
<td align="right">26.0%</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">137</td>
<td align="right">3.6%</td>
<td align="right">114</td>
<td align="right">3.9%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,907</td>
<td align="right">50.0%</td>
<td align="right">1,921</td>
<td align="right">65.9%</td>
<td align="right">0.7%</td>
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
<td align="right">33,519,631</td>
<td align="right">52.1%</td>
<td align="right">52,733,658</td>
<td align="right">54.2%</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,917,972</td>
<td align="right">46.5%</td>
<td align="right">43,951,160</td>
<td align="right">45.2%</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">798,461</td>
<td align="right">1.2%</td>
<td align="right">496,048</td>
<td align="right">0.5%</td>
<td align="right">-37.9%</td>
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
<td align="right">15,688</td>
<td align="right">22.8%</td>
<td align="right">10,059</td>
<td align="right">16.6%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">52,978</td>
<td align="right">77.2%</td>
<td align="right">50,520</td>
<td align="right">83.4%</td>
<td align="right">-4.6%</td>
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
<td align="right">2,709</td>
<td align="right">5.1%</td>
<td align="right">1,313</td>
<td align="right">2.6%</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">150</td>
<td align="right">0.3%</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,332</td>
<td align="right">2.5%</td>
<td align="right">968</td>
<td align="right">1.9%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">557</td>
<td align="right">1.1%</td>
<td align="right">436</td>
<td align="right">0.9%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.4%</td>
<td align="right">664</td>
<td align="right">1.3%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,888</td>
<td align="right">5.5%</td>
<td align="right">3,171</td>
<td align="right">6.3%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.7%</td>
<td align="right">358</td>
<td align="right">0.7%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">28</td>
<td align="right">0.1%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">44,056</td>
<td align="right">83.2%</td>
<td align="right">43,409</td>
<td align="right">85.9%</td>
<td align="right">-1.5%</td>
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
<td align="right">48,601,701</td>
<td align="right">16.0%</td>
<td align="right">17,436,049</td>
<td align="right">6.6%</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,588</td>
<td align="right">0.0%</td>
<td align="right">9,524</td>
<td align="right">0.0%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">35,922,951</td>
<td align="right">11.8%</td>
<td align="right">38,757,964</td>
<td align="right">14.8%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">220,042,616</td>
<td align="right">72.2%</td>
<td align="right">206,235,872</td>
<td align="right">78.6%</td>
<td align="right">-6.3%</td>
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
<td align="right">39,149</td>
<td align="right">5.4%</td>
<td align="right">22,047</td>
<td align="right">2.9%</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">683,601</td>
<td align="right">94.6%</td>
<td align="right">736,527</td>
<td align="right">97.1%</td>
<td align="right">7.7%</td>
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
<td align="left">builtin class method</td>
<td align="right">246</td>
<td align="right">0.6%</td>
<td align="right">12</td>
<td align="right">0.1%</td>
<td align="right">-95.1%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,812</td>
<td align="right">17.4%</td>
<td align="right">2,257</td>
<td align="right">10.2%</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">2,979</td>
<td align="right">7.6%</td>
<td align="right">1,362</td>
<td align="right">6.2%</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,673</td>
<td align="right">6.8%</td>
<td align="right">1,344</td>
<td align="right">6.1%</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,151</td>
<td align="right">54.0%</td>
<td align="right">13,236</td>
<td align="right">60.0%</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">1,870</td>
<td align="right">4.8%</td>
<td align="right">1,243</td>
<td align="right">5.6%</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,092</td>
<td align="right">7.9%</td>
<td align="right">2,326</td>
<td align="right">10.6%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">148</td>
<td align="right">0.4%</td>
<td align="right">142</td>
<td align="right">0.6%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">2</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,294</td>
<td align="right">0.0%</td>
<td align="right">1,874</td>
<td align="right">0.0%</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">244,553,128</td>
<td align="right">100.0%</td>
<td align="right">281,103,939</td>
<td align="right">100.0%</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,520</td>
<td align="right">0.0%</td>
<td align="right">4,481</td>
<td align="right">0.0%</td>
<td align="right">-0.9%</td>
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
<td align="right">13,566</td>
<td align="right">100.0%</td>
<td align="right">13,262</td>
<td align="right">100.0%</td>
<td align="right">-2.2%</td>
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

### LOAD_METHOD

<details>
<summary> specialization stats for LOAD_METHOD family </summary>

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
<td align="right">7,233,597</td>
<td align="right">34.9%</td>
<td align="right">4,210,575</td>
<td align="right">27.3%</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,504,170</td>
<td align="right">65.1%</td>
<td align="right">11,227,050</td>
<td align="right">72.7%</td>
<td align="right">-16.9%</td>
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
<td align="right">141,344</td>
<td align="right">94.5%</td>
<td align="right">84,221</td>
<td align="right">93.8%</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,206</td>
<td align="right">5.5%</td>
<td align="right">5,587</td>
<td align="right">6.2%</td>
<td align="right">-31.9%</td>
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
<td align="left">kind 12</td>
<td align="right">332</td>
<td align="right">4.0%</td>
<td align="right">129</td>
<td align="right">2.3%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,922</td>
<td align="right">84.4%</td>
<td align="right">4,761</td>
<td align="right">85.2%</td>
<td align="right">-31.2%</td>
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
<td align="right">2,265,754</td>
<td align="right">100.0%</td>
<td align="right">2,215,523</td>
<td align="right">100.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">5</td>
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
<td align="right">5</td>
<td align="right">100.0%</td>
<td align="right">5</td>
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

### LOAD_SUPER_METHOD

<details>
<summary> specialization stats for LOAD_SUPER_METHOD family </summary>

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
<td align="right">25</td>
<td align="right">50.0%</td>
<td align="right">25</td>
<td align="right">50.0%</td>
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
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">25</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,711</td>
<td align="right">1.4%</td>
<td align="right">7,390</td>
<td align="right">1.1%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">731,620</td>
<td align="right">72.0%</td>
<td align="right">388,391</td>
<td align="right">59.3%</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">268,986</td>
<td align="right">26.5%</td>
<td align="right">257,987</td>
<td align="right">39.4%</td>
<td align="right">-4.1%</td>
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
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">144</td>
<td align="right">15.0%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
<td align="right">813</td>
<td align="right">85.0%</td>
<td align="right">-26.6%</td>
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
<td align="right">1,108</td>
<td align="right">100.0%</td>
<td align="right">813</td>
<td align="right">100.0%</td>
<td align="right">-26.6%</td>
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
<td align="right">173,940</td>
<td align="right">1.9%</td>
<td align="right">150,467</td>
<td align="right">1.7%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,578,414</td>
<td align="right">17.4%</td>
<td align="right">1,450,007</td>
<td align="right">16.7%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,325,697</td>
<td align="right">80.7%</td>
<td align="right">7,075,585</td>
<td align="right">81.5%</td>
<td align="right">-3.4%</td>
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
<td align="right">977</td>
<td align="right">3.2%</td>
<td align="right">828</td>
<td align="right">2.9%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,027</td>
<td align="right">96.8%</td>
<td align="right">27,634</td>
<td align="right">97.1%</td>
<td align="right">-8.0%</td>
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
<td align="right">518</td>
<td align="right">53.0%</td>
<td align="right">373</td>
<td align="right">45.0%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">300</td>
<td align="right">30.7%</td>
<td align="right">292</td>
<td align="right">35.3%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">102</td>
<td align="right">10.4%</td>
<td align="right">101</td>
<td align="right">12.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3</td>
<td align="right">0.3%</td>
<td align="right">3</td>
<td align="right">0.4%</td>
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
<td align="right">591</td>
<td align="right">100.0%</td>
<td align="right">261</td>
<td align="right">100.0%</td>
<td align="right">-55.8%</td>
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
<td align="right">880,129</td>
<td align="right">4.7%</td>
<td align="right">13,539</td>
<td align="right">0.1%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,739,358</td>
<td align="right">95.3%</td>
<td align="right">13,376,336</td>
<td align="right">99.9%</td>
<td align="right">-24.6%</td>
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
<td align="right">1,136</td>
<td align="right">66.4%</td>
<td align="right">604</td>
<td align="right">51.2%</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">576</td>
<td align="right">33.6%</td>
<td align="right">576</td>
<td align="right">48.8%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">1,136</td>
<td align="right">100.0%</td>
<td align="right">604</td>
<td align="right">100.0%</td>
<td align="right">-46.8%</td>
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
<td align="right">442,510</td>
<td align="right">0.3%</td>
<td align="right">215,457</td>
<td align="right">0.1%</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,919,586</td>
<td align="right">6.1%</td>
<td align="right">9,108,282</td>
<td align="right">5.8%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">153,573,491</td>
<td align="right">93.7%</td>
<td align="right">147,381,234</td>
<td align="right">94.0%</td>
<td align="right">-4.0%</td>
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
<td align="right">11,780</td>
<td align="right">43.2%</td>
<td align="right">7,881</td>
<td align="right">42.2%</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,466</td>
<td align="right">56.8%</td>
<td align="right">10,789</td>
<td align="right">57.8%</td>
<td align="right">-30.2%</td>
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
<td align="right">726</td>
<td align="right">6.2%</td>
<td align="right">267</td>
<td align="right">3.4%</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">7.5%</td>
<td align="right">355</td>
<td align="right">4.5%</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,264</td>
<td align="right">10.7%</td>
<td align="right">754</td>
<td align="right">9.6%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">716</td>
<td align="right">6.1%</td>
<td align="right">488</td>
<td align="right">6.2%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">6,231</td>
<td align="right">52.9%</td>
<td align="right">4,444</td>
<td align="right">56.4%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,874</td>
<td align="right">15.9%</td>
<td align="right">1,487</td>
<td align="right">18.9%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.7%</td>
<td align="right">84</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">6,245</td>
<td align="right">0.0%</td>
<td align="right">2,122</td>
<td align="right">0.0%</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,833,091</td>
<td align="right">100.0%</td>
<td align="right">82,544,989</td>
<td align="right">100.0%</td>
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
<td align="right">306</td>
<td align="right">11.3%</td>
<td align="right">175</td>
<td align="right">7.0%</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,392</td>
<td align="right">88.7%</td>
<td align="right">2,339</td>
<td align="right">93.0%</td>
<td align="right">-2.2%</td>
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
<td align="right">263</td>
<td align="right">85.9%</td>
<td align="right">133</td>
<td align="right">76.0%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.1%</td>
<td align="right">42</td>
<td align="right">24.0%</td>
<td align="right">-2.3%</td>
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
<td align="right">1,272,136,613</td>
<td align="right">33.2%</td>
<td align="right">705,962,538</td>
<td align="right">31.4%</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,318,614,736</td>
<td align="right">60.5%</td>
<td align="right">1,351,911,619</td>
<td align="right">60.1%</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">173,109,539</td>
<td align="right">4.5%</td>
<td align="right">122,642,869</td>
<td align="right">5.5%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">71,268,314</td>
<td align="right">1.9%</td>
<td align="right">67,319,931</td>
<td align="right">3.0%</td>
<td align="right">-5.5%</td>
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
<td align="right">27,071,021</td>
<td align="right">15.7%</td>
<td align="right">6,730,559</td>
<td align="right">5.5%</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">48,601,701</td>
<td align="right">28.1%</td>
<td align="right">17,436,049</td>
<td align="right">14.2%</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,519,631</td>
<td align="right">19.4%</td>
<td align="right">52,733,658</td>
<td align="right">43.1%</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,395,029</td>
<td align="right">4.9%</td>
<td align="right">4,057,827</td>
<td align="right">3.3%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">25,930,916</td>
<td align="right">15.0%</td>
<td align="right">16,851,627</td>
<td align="right">13.8%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">13,504,170</td>
<td align="right">7.8%</td>
<td align="right">11,227,050</td>
<td align="right">9.2%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,574,799</td>
<td align="right">2.6%</td>
<td align="right">3,882,512</td>
<td align="right">3.2%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,919,586</td>
<td align="right">5.7%</td>
<td align="right">9,108,282</td>
<td align="right">7.4%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.2%</td>
<td align="right">257,987</td>
<td align="right">0.2%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">880,129</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">150,467</td>
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
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">7,157,384</td>
<td align="right">10.0%</td>
<td align="right">4,173,452</td>
<td align="right">6.2%</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,112,690</td>
<td align="right">8.6%</td>
<td align="right">4,002,228</td>
<td align="right">5.9%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,165,012</td>
<td align="right">4.4%</td>
<td align="right">2,282,146</td>
<td align="right">3.4%</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">20,604,763</td>
<td align="right">28.9%</td>
<td align="right">25,653,271</td>
<td align="right">38.1%</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">11,810,382</td>
<td align="right">16.6%</td>
<td align="right">10,629,262</td>
<td align="right">15.8%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">535,852</td>
<td align="right">0.8%</td>
<td align="right">488,292</td>
<td align="right">0.7%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,577,635</td>
<td align="right">2.2%</td>
<td align="right">1,449,622</td>
<td align="right">2.2%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,425,280</td>
<td align="right">16.0%</td>
<td align="right">10,945,499</td>
<td align="right">16.3%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,570</td>
<td align="right">3.0%</td>
<td align="right">2,074,324</td>
<td align="right">3.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,596</td>
<td align="right">7.2%</td>
<td align="right">5,062,784</td>
<td align="right">7.5%</td>
<td align="right">-0.8%</td>
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
<td align="right">950,223</td>
<td align="right">0.5%</td>
<td align="right">806,123</td>
<td align="right">0.4%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,592,422</td>
<td align="right">53.4%</td>
<td align="right">107,023,223</td>
<td align="right">53.0%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,496,865</td>
<td align="right">10.7%</td>
<td align="right">21,585,855</td>
<td align="right">10.7%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,335,416</td>
<td align="right">19.6%</td>
<td align="right">39,663,140</td>
<td align="right">19.6%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,978,768</td>
<td align="right">89.2%</td>
<td align="right">180,400,891</td>
<td align="right">89.4%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">98,116,337</td>
<td align="right">46.6%</td>
<td align="right">94,830,519</td>
<td align="right">47.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">98,116,337</td>
<td align="right">46.6%</td>
<td align="right">94,830,519</td>
<td align="right">47.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,618,687</td>
<td align="right">35.9%</td>
<td align="right">73,243,879</td>
<td align="right">36.3%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,619,472</td>
<td align="right">35.9%</td>
<td align="right">73,244,664</td>
<td align="right">36.3%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,307</td>
<td align="right">8.8%</td>
<td align="right">18,073,340</td>
<td align="right">9.0%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,331,910</td>
<td align="right">4.4%</td>
<td align="right">9,243,814</td>
<td align="right">4.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">348</td>
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
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,907</td>
<td align="right">0.0%</td>
<td align="right">19,628</td>
<td align="right">0.0%</td>
<td align="right">120.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">705,470,074</td>
<td align="right">12.2%</td>
<td align="right">445,990,823</td>
<td align="right">8.3%</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,650,371,321</td>
<td align="right">33.5%</td>
<td align="right">1,092,948,744</td>
<td align="right">23.6%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">441,756,421</td>
<td align="right">9.0%</td>
<td align="right">294,559,886</td>
<td align="right">6.4%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">720,772</td>
<td align="right"></td>
<td align="right">918,139</td>
<td align="right"></td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,008,754,857</td>
<td align="right">34.8%</td>
<td align="right">1,569,497,027</td>
<td align="right">29.3%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,672,857,262</td>
<td align="right">34.0%</td>
<td align="right">1,984,372,894</td>
<td align="right">42.9%</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,769,084,631</td>
<td align="right">30.7%</td>
<td align="right">1,948,805,979</td>
<td align="right">36.3%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,281,741,072</td>
<td align="right">22.2%</td>
<td align="right">1,400,650,075</td>
<td align="right">26.1%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,154,169,211</td>
<td align="right">23.5%</td>
<td align="right">1,249,976,411</td>
<td align="right">27.0%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,165</td>
<td align="right"></td>
<td align="right">818,759</td>
<td align="right"></td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,270,435</td>
<td align="right"></td>
<td align="right">2,174,828</td>
<td align="right"></td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">269,043,947</td>
<td align="right"></td>
<td align="right">259,041,934</td>
<td align="right"></td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">206,839,693</td>
<td align="right">40.2%</td>
<td align="right">199,280,443</td>
<td align="right">39.8%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">207,621,420</td>
<td align="right">40.3%</td>
<td align="right">200,047,789</td>
<td align="right">40.0%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">220,265,131</td>
<td align="right"></td>
<td align="right">212,415,334</td>
<td align="right"></td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,989,989</td>
<td align="right"></td>
<td align="right">3,092,194</td>
<td align="right"></td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">772,820</td>
<td align="right">0.2%</td>
<td align="right">747,718</td>
<td align="right">0.1%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">307,182,368</td>
<td align="right"></td>
<td align="right">300,332,891</td>
<td align="right"></td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">307,147,558</td>
<td align="right">59.7%</td>
<td align="right">300,299,139</td>
<td align="right">60.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">148,112,457</td>
<td align="right"></td>
<td align="right">149,940,256</td>
<td align="right"></td>
<td align="right">1.2%</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,947,908,440</td>
<td align="right">2,083.3%</td>
<td align="right">6,249,612,300</td>
<td align="right">3,134.1%</td>
<td align="right">112.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">17,901</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">7,232</td>
<td align="right">40.4%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">10,856</td>
<td align="right">60.6%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">10,669</td>
<td align="right">59.6%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">225</td>
<td align="right">1.3%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">236</td>
<td align="right">1.3%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">141,498,826</td>
<td align="right"></td>
<td align="right">199,409,993</td>
<td align="right"></td>
<td align="right">40.9%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right">7,232</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">7,144</td>
<td align="right">98.8%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,122</td>
<td align="right">15.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,131</td>
<td align="right">15.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,554</td>
<td align="right">35.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,587</td>
<td align="right">21.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">817</td>
<td align="right">11.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">274</td>
<td align="right">3.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">954</td>
<td align="right">13.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,097</td>
<td align="right">15.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">3,372</td>
<td align="right">46.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,256</td>
<td align="right">17.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">170</td>
<td align="right">2.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">628</td>
<td align="right">815,497</td>
<td align="right">129,756.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">511</td>
<td align="right">595,764</td>
<td align="right">116,487.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">744</td>
<td align="right">332,721</td>
<td align="right">44,620.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">24,402</td>
<td align="right">4,429,876</td>
<td align="right">18,053.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">24,402</td>
<td align="right">4,429,457</td>
<td align="right">18,052.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">3,908,275</td>
<td align="right">14,411.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">73,352</td>
<td align="right">10,550,899</td>
<td align="right">14,283.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">245,074</td>
<td align="right">20,887,820</td>
<td align="right">8,423.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,166</td>
<td align="right">330,128</td>
<td align="right">6,290.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">174,242</td>
<td align="right">10,115,493</td>
<td align="right">5,705.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,610,971</td>
<td align="right">83,096,613</td>
<td align="right">5,058.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,260,927</td>
<td align="right">58,660,251</td>
<td align="right">4,552.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,260,927</td>
<td align="right">58,380,250</td>
<td align="right">4,529.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">28,820</td>
<td align="right">1,234,802</td>
<td align="right">4,184.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">651,733</td>
<td align="right">20,994,586</td>
<td align="right">3,121.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">28,292,889</td>
<td align="right">647,534,468</td>
<td align="right">2,188.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">416,305</td>
<td align="right">8,547,940</td>
<td align="right">1,953.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">416,305</td>
<td align="right">8,175,858</td>
<td align="right">1,863.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">188,232</td>
<td align="right">3,165,582</td>
<td align="right">1,581.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,373,419</td>
<td align="right">15,526,390</td>
<td align="right">1,030.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">896,597</td>
<td align="right">9,665,716</td>
<td align="right">978.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">52,447</td>
<td align="right">542,614</td>
<td align="right">934.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">27,701,159</td>
<td align="right">244,045,190</td>
<td align="right">781.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">559,109</td>
<td align="right">4,793,630</td>
<td align="right">757.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,382,801</td>
<td align="right">11,747,417</td>
<td align="right">749.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,390,891</td>
<td align="right">10,303,220</td>
<td align="right">640.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,390,891</td>
<td align="right">10,303,220</td>
<td align="right">640.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">2,451,935</td>
<td align="right">17,003,253</td>
<td align="right">593.5%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">38,871</td>
<td align="right">244,461</td>
<td align="right">528.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">320,399</td>
<td align="right">1,760,354</td>
<td align="right">449.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">25,328,470</td>
<td align="right">121,090,883</td>
<td align="right">378.1%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD</td>
<td align="right">1,293,475</td>
<td align="right">5,660,701</td>
<td align="right">337.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">563,070</td>
<td align="right">2,455,795</td>
<td align="right">336.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">3,163,771</td>
<td align="right">13,298,669</td>
<td align="right">320.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">144,184</td>
<td align="right">595,435</td>
<td align="right">313.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">3,257,704</td>
<td align="right">13,233,052</td>
<td align="right">306.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,046,691</td>
<td align="right">38,825,757</td>
<td align="right">286.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">9,164,992</td>
<td align="right">34,076,767</td>
<td align="right">271.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">19,433,930</td>
<td align="right">71,708,002</td>
<td align="right">269.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">8,385,671</td>
<td align="right">29,539,357</td>
<td align="right">252.3%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_NO_DICT</td>
<td align="right">11,440,590</td>
<td align="right">39,857,621</td>
<td align="right">248.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,815,066</td>
<td align="right">16,531,638</td>
<td align="right">243.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">4,530,870</td>
<td align="right">14,904,543</td>
<td align="right">229.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">43,689,523</td>
<td align="right">136,273,738</td>
<td align="right">211.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">10,330,248</td>
<td align="right">31,909,186</td>
<td align="right">208.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">16,613,140</td>
<td align="right">47,178,247</td>
<td align="right">184.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">5,190,264</td>
<td align="right">13,331,625</td>
<td align="right">156.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">51,880,470</td>
<td align="right">131,531,200</td>
<td align="right">153.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">20,099,003</td>
<td align="right">48,955,985</td>
<td align="right">143.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">12,042,065</td>
<td align="right">29,318,308</td>
<td align="right">143.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">12,148,244</td>
<td align="right">29,376,942</td>
<td align="right">141.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">20,099,003</td>
<td align="right">48,009,291</td>
<td align="right">138.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">117,552,999</td>
<td align="right">279,154,466</td>
<td align="right">137.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">6,262,282</td>
<td align="right">14,000,804</td>
<td align="right">123.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,844,372</td>
<td align="right">17,228,338</td>
<td align="right">119.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">14,404,820</td>
<td align="right">30,656,040</td>
<td align="right">112.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">5,632,291</td>
<td align="right">11,795,279</td>
<td align="right">109.4%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,513,694</td>
<td align="right">1,747</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">13,180,955</td>
<td align="right">29,587</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">13,180,955</td>
<td align="right">41,093</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">320,466,819</td>
<td align="right">615,583,285</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">17,700,623</td>
<td align="right">1,854,496</td>
<td align="right">-89.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">18,591,230</td>
<td align="right">33,089,704</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">5,946,468</td>
<td align="right">10,421,552</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">13,315,697</td>
<td align="right">4,918,648</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">18,029,354</td>
<td align="right">29,376,942</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">27,163,760</td>
<td align="right">10,522,003</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,285,622</td>
<td align="right">2,034,768</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">33,028,216</td>
<td align="right">14,531,637</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">34,332,385</td>
<td align="right">15,817,795</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">127,341,139</td>
<td align="right">61,047,647</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">13,170,492</td>
<td align="right">19,278,414</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">375,103,034</td>
<td align="right">545,382,488</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">48,541,387</td>
<td align="right">27,769,602</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">14,118,305</td>
<td align="right">20,051,569</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,512,341</td>
<td align="right">7,670,376</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">8,682,738</td>
<td align="right">12,024,641</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">8,682,738</td>
<td align="right">12,024,641</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,828,467</td>
<td align="right">2,530,622</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">4,685,541</td>
<td align="right">6,465,123</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">1,702,794</td>
<td align="right">2,341,223</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">10,265,748</td>
<td align="right">13,861,617</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_WITH_VALUES</td>
<td align="right">8,682,110</td>
<td align="right">11,208,934</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">1,744,767</td>
<td align="right">1,273,905</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">5,980,698</td>
<td align="right">7,582,303</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">42,876,382</td>
<td align="right">49,905,121</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,524,906</td>
<td align="right">7,578,426</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,524,906</td>
<td align="right">7,578,426</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">12,846,056</td>
<td align="right">10,808,178</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,399,458</td>
<td align="right">9,608,775</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">133,568,767</td>
<td align="right">115,817,357</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">6,908,342</td>
<td align="right">6,069,939</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">6,908,342</td>
<td align="right">6,069,939</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">6,503,929</td>
<td align="right">5,744,237</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">14,570,914</td>
<td align="right">13,203,162</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">13,776,634</td>
<td align="right">14,741,416</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">17,441,222</td>
<td align="right">18,619,972</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,558,589</td>
<td align="right">6,139,034</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">13,900,280</td>
<td align="right">13,203,110</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">630,363</td>
<td align="right">607,574</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40,416,686</td>
<td align="right">40,777,639</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">183,545,379</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">141,498,826</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">65,043,885</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">58,126,723</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">50,871,948</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">50,179,500</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">42,534,645</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">42,046,553</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">39,271,629</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">38,193,032</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">28,216,446</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">27,614,554</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">26,650,998</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">19,150,848</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,784,393</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,879,269</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">12,317,878</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">11,661,140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">8,863,768</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">8,767,734</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">8,171,939</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">7,798,721</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">6,788,114</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">6,746,541</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">6,491,795</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">5,980,698</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">4,848,821</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,286,054</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,155,359</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">389,868</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">159,560</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">101,452</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,228</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">1,195,897,751</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">103,957,247</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">103,956,936</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right"></td>
<td align="right">103,956,284</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">77,630,301</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right"></td>
<td align="right">58,332,474</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">52,230,366</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP</td>
<td align="right"></td>
<td align="right">49,416,636</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right"></td>
<td align="right">37,369,489</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">29,376,638</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right"></td>
<td align="right">16,136,025</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_NONE</td>
<td align="right"></td>
<td align="right">11,225,664</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">5,587,921</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">4,193,161</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">3,890,535</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right"></td>
<td align="right">3,548,499</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">3,483,369</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right"></td>
<td align="right">2,919,610</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right"></td>
<td align="right">2,360,887</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">2,360,887</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right"></td>
<td align="right">2,099,395</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">1,772,698</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right"></td>
<td align="right">1,772,698</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">1,772,698</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">1,487,007</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">1,226,504</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right"></td>
<td align="right">1,195,313</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">1,003,475</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">940,855</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">938,757</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">938,588</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">890,943</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">864,458</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_METHOD_METHOD</td>
<td align="right"></td>
<td align="right">594,370</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">575,502</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">575,502</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">561,224</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">561,224</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">514,283</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">372,010</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">327,448</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">326,962</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right"></td>
<td align="right">263,439</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right"></td>
<td align="right">245,752</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">186,043</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">186,043</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">173,488</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">173,488</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right"></td>
<td align="right">156,095</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right"></td>
<td align="right">156,095</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">135,268</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">126,283</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">124,548</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">114,651</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">107,515</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right"></td>
<td align="right">102,022</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">86,744</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">76,705</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">63,903</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right"></td>
<td align="right">58,684</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">30,649</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">15,432</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_FOR</td>
<td align="right"></td>
<td align="right">12,101</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">11,956</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right"></td>
<td align="right">10,330</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right"></td>
<td align="right">10,330</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">5,181</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right"></td>
<td align="right">5,157</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right"></td>
<td align="right">911</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right"></td>
<td align="right">911</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">830</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right"></td>
<td align="right">316</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right"></td>
<td align="right">316</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right"></td>
<td align="right">199</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">84</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right">84</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">72</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,792</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">790</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-01-27
