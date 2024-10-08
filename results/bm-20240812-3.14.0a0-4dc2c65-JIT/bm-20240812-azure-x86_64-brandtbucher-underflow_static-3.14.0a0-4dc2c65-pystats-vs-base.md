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
<td align="right">2,659,357</td>
<td align="right">7,176,447</td>
<td align="right">169.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,584,863</td>
<td align="right">131,163</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,641</td>
<td align="right">2,581</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">3,380</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,461,787</td>
<td align="right">4,861,551</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">418,386,582</td>
<td align="right">28,550,513</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,785,481</td>
<td align="right">1,272,396</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">123,780,342</td>
<td align="right">24,638,436</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,501,442</td>
<td align="right">937,332</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">276,937,308</td>
<td align="right">68,377,442</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">393,832,956</td>
<td align="right">97,641,337</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">98,831,505</td>
<td align="right">26,048,463</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">57,409,643</td>
<td align="right">15,313,438</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">236,562,207</td>
<td align="right">64,933,827</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">104,498,600</td>
<td align="right">28,770,222</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">183,619,050</td>
<td align="right">55,080,553</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,635,822</td>
<td align="right">854,123</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,745,379</td>
<td align="right">16,464,524</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">732,807,101</td>
<td align="right">250,617,025</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">298,590,171</td>
<td align="right">102,213,298</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">107,206,212</td>
<td align="right">38,367,361</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,153,715</td>
<td align="right">30,455,648</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,714,510</td>
<td align="right">18,128,444</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">319,443,176</td>
<td align="right">121,402,370</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">109,713,818</td>
<td align="right">42,889,717</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,087,578</td>
<td align="right">53,385,158</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,030,739,719</td>
<td align="right">410,204,420</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,115,529</td>
<td align="right">57,269,309</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,730,853</td>
<td align="right">29,679,353</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,225,385</td>
<td align="right">25,074,196</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">475,201,646</td>
<td align="right">218,034,689</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">123,162,395</td>
<td align="right">58,340,192</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">43,141,638</td>
<td align="right">20,669,292</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">63,921,027</td>
<td align="right">30,742,225</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">117,514,813</td>
<td align="right">59,798,202</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">457,672,980</td>
<td align="right">234,195,974</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,990,712</td>
<td align="right">53,977,636</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">364,452,185</td>
<td align="right">189,268,643</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">54,309,159</td>
<td align="right">28,394,073</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">265,434,908</td>
<td align="right">141,303,550</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,994,967</td>
<td align="right">5,861,883</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">270,400,306</td>
<td align="right">144,628,769</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">200,401,386</td>
<td align="right">107,379,448</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,120,135,460</td>
<td align="right">2,744,301,243</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">186,402,514</td>
<td align="right">100,090,911</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">80,792,268</td>
<td align="right">45,238,802</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">183,774,980</td>
<td align="right">103,760,255</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">223,937</td>
<td align="right">126,708</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">35,817,241</td>
<td align="right">20,291,039</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,828,886,575</td>
<td align="right">2,219,034,622</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">239,777,676</td>
<td align="right">139,024,695</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">240,427,325</td>
<td align="right">139,834,425</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">216,975,436</td>
<td align="right">126,533,449</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,636,032</td>
<td align="right">85,836,912</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,497,274,606</td>
<td align="right">1,527,612,417</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,115,845,178</td>
<td align="right">2,541,803,127</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,775,909,269</td>
<td align="right">1,721,386,398</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">91,677,535</td>
<td align="right">57,279,967</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">379,786,625</td>
<td align="right">241,340,879</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,059,155</td>
<td align="right">57,882,896</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,988,499</td>
<td align="right">59,618,622</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">221,218,439</td>
<td align="right">141,918,436</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">91,866,129</td>
<td align="right">59,236,261</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,462,825</td>
<td align="right">2,237,756</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">67,148,737</td>
<td align="right">43,579,100</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,295,449,228</td>
<td align="right">2,791,626,286</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,468,229,274</td>
<td align="right">11,385,915,530</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,520,198</td>
<td align="right">35,174,495</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,247,259,048</td>
<td align="right">1,486,676,171</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,418,339</td>
<td align="right">946,275</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">712,757,746</td>
<td align="right">477,218,494</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">756,858,521</td>
<td align="right">510,751,684</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,213,008</td>
<td align="right">15,005,591</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">34,631,783</td>
<td align="right">23,418,179</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,856,180,733</td>
<td align="right">3,308,400,963</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,826,877,930</td>
<td align="right">1,940,273,324</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">567,596,579</td>
<td align="right">396,097,453</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">138,697,219</td>
<td align="right">96,972,854</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,805,817</td>
<td align="right">40,629,534</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,334,441,793</td>
<td align="right">939,343,423</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,895,289,436</td>
<td align="right">1,342,497,644</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">894,903,795</td>
<td align="right">639,475,888</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,470</td>
<td align="right">124,033</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,560,554</td>
<td align="right">27,246,590</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,742,492,201</td>
<td align="right">1,995,465,270</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">157,612,905</td>
<td align="right">114,764,735</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">53,511,179</td>
<td align="right">39,228,527</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">351,675,122</td>
<td align="right">258,191,401</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">449,937,275</td>
<td align="right">330,380,946</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">677,039,759</td>
<td align="right">497,241,586</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">15,202,850</td>
<td align="right">11,323,354</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">838,901,778</td>
<td align="right">627,206,642</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">653,153,408</td>
<td align="right">489,487,032</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">853,612,791</td>
<td align="right">640,276,979</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">199,860,332</td>
<td align="right">150,303,698</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">52,829,709</td>
<td align="right">39,869,287</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">825,147,690</td>
<td align="right">625,594,864</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,926,605,791</td>
<td align="right">2,246,434,749</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,203,952</td>
<td align="right">7,131,832</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">628,091,454</td>
<td align="right">493,159,603</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,847,222,627</td>
<td align="right">1,461,487,841</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">43,994,437</td>
<td align="right">35,299,195</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">43,396,519</td>
<td align="right">34,920,779</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">752,144,828</td>
<td align="right">614,640,431</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">199,038,645</td>
<td align="right">162,827,898</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,372,431,270</td>
<td align="right">1,126,460,997</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,048,481,717</td>
<td align="right">4,149,235,597</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">337,735,969</td>
<td align="right">277,744,567</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,583,786</td>
<td align="right">331,242,606</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">60,311,178</td>
<td align="right">49,766,278</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">247,357,656</td>
<td align="right">204,626,666</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">297,072,422</td>
<td align="right">248,015,009</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">272,018,726</td>
<td align="right">228,947,507</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">825,837,701</td>
<td align="right">699,401,616</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">196,290,172</td>
<td align="right">168,228,795</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,060,889,926</td>
<td align="right">909,722,345</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">719,190</td>
<td align="right">617,831</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">324,679,236</td>
<td align="right">283,386,194</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,317,525</td>
<td align="right">41,347,424</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">103,722,057</td>
<td align="right">91,571,161</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">82,301,389</td>
<td align="right">72,854,039</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">350,685,656</td>
<td align="right">311,126,089</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">353,537,247</td>
<td align="right">314,285,969</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,104,103</td>
<td align="right">363,555,149</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,798,238</td>
<td align="right">18,214,806</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,262,766</td>
<td align="right">10,364,036</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,354,283</td>
<td align="right">9,537,863</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">150,192,798</td>
<td align="right">138,389,620</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">133,920,677</td>
<td align="right">124,226,415</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">539,154,553</td>
<td align="right">500,709,235</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">49,445,271</td>
<td align="right">45,959,057</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,019,767</td>
<td align="right">32,579,056</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,592,813</td>
<td align="right">9,934,726</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">120,762,159</td>
<td align="right">113,373,056</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">201,096,123</td>
<td align="right">189,997,817</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">494,554,040</td>
<td align="right">468,160,989</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,324,514</td>
<td align="right">7,884,456</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">524,878</td>
<td align="right">501,542</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">147,153,032</td>
<td align="right">141,280,832</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,057,127,741</td>
<td align="right">1,035,557,832</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">474,667,365</td>
<td align="right">465,059,531</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">33,266,542</td>
<td align="right">32,626,381</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">91,887,611</td>
<td align="right">90,222,191</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,166,102</td>
<td align="right">263,630,477</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,388,936</td>
<td align="right">21,029,244</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,744,107</td>
<td align="right">3,692,940</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">712,060</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,288</td>
<td align="right">3,435,808</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,010,784</td>
<td align="right">223,853,741</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">16,179,088</td>
<td align="right">16,152,930</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,369,538</td>
<td align="right">198,518,935</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">493,047,945</td>
<td align="right">493,409,177</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,586,210</td>
<td align="right">3,586,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">268,662</td>
<td align="right">268,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,806</td>
<td align="right">27,804</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,184</td>
<td align="right">15,185</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">231,600,545</td>
<td align="right">231,614,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,397,277</td>
<td align="right">21,396,482</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,082,882</td>
<td align="right">21,082,176</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,269,866,646</td>
<td align="right">2,269,801,190</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">70,946,696</td>
<td align="right">70,947,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,830,545</td>
<td align="right">5,830,593</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,356,663</td>
<td align="right">20,356,814</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,399,108</td>
<td align="right">173,399,102</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,169,586</td>
<td align="right">94,169,586</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">77,693,920</td>
<td align="right">77,693,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,240</td>
<td align="right">38,846,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,680</td>
<td align="right">38,845,680</td>
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
<td align="left">STORE_NAME</td>
<td align="right">658,912</td>
<td align="right">658,912</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">157,711</td>
<td align="right">157,711</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">58,580</td>
<td align="right">58,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">30,149</td>
<td align="right">30,149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,916</td>
<td align="right">21,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16,120</td>
<td align="right">16,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">982</td>
<td align="right">982</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">423</td>
<td align="right">423</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">241</td>
<td align="right">241</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">140</td>
<td align="right">140</td>
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
<td align="right">407,641,105</td>
<td align="right">4.2%</td>
<td align="right">260,072,714</td>
<td align="right">2.7%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,575,090</td>
<td align="right">0.3%</td>
<td align="right">20,134,550</td>
<td align="right">0.2%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,395,496,641</td>
<td align="right">95.8%</td>
<td align="right">9,384,654,132</td>
<td align="right">97.3%</td>
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
<td align="right">599,863</td>
<td align="right">34.9%</td>
<td align="right">421,763</td>
<td align="right">30.1%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,120,747</td>
<td align="right">65.1%</td>
<td align="right">980,952</td>
<td align="right">69.9%</td>
<td align="right">-12.5%</td>
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
<td align="left">true divide float</td>
<td align="right">4,727</td>
<td align="right">0.4%</td>
<td align="right">1,709</td>
<td align="right">0.2%</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">6,906</td>
<td align="right">0.6%</td>
<td align="right">2,866</td>
<td align="right">0.3%</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">49,339</td>
<td align="right">4.4%</td>
<td align="right">23,356</td>
<td align="right">2.4%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,940</td>
<td align="right">7.4%</td>
<td align="right">54,256</td>
<td align="right">5.5%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,803</td>
<td align="right">4.4%</td>
<td align="right">32,352</td>
<td align="right">3.3%</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,599</td>
<td align="right">0.5%</td>
<td align="right">3,720</td>
<td align="right">0.4%</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">7,442</td>
<td align="right">0.7%</td>
<td align="right">5,439</td>
<td align="right">0.6%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">401</td>
<td align="right">0.0%</td>
<td align="right">321</td>
<td align="right">0.0%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">7,086</td>
<td align="right">0.6%</td>
<td align="right">5,958</td>
<td align="right">0.6%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,426</td>
<td align="right">2.8%</td>
<td align="right">26,697</td>
<td align="right">2.7%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,454</td>
<td align="right">1.3%</td>
<td align="right">12,864</td>
<td align="right">1.3%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,963</td>
<td align="right">0.3%</td>
<td align="right">2,723</td>
<td align="right">0.3%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,742</td>
<td align="right">0.9%</td>
<td align="right">8,961</td>
<td align="right">0.9%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,600</td>
<td align="right">69.7%</td>
<td align="right">734,108</td>
<td align="right">74.8%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,623</td>
<td align="right">2.9%</td>
<td align="right">31,318</td>
<td align="right">3.2%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">834</td>
<td align="right">0.1%</td>
<td align="right">816</td>
<td align="right">0.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,620</td>
<td align="right">0.2%</td>
<td align="right">2,572</td>
<td align="right">0.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">20,440</td>
<td align="right">1.8%</td>
<td align="right">20,177</td>
<td align="right">2.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,802</td>
<td align="right">1.0%</td>
<td align="right">10,739</td>
<td align="right">1.1%</td>
<td align="right">-0.6%</td>
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
<td align="right">657,541,622</td>
<td align="right">9.6%</td>
<td align="right">493,868,878</td>
<td align="right">7.4%</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,792,351</td>
<td align="right">0.1%</td>
<td align="right">4,741,068</td>
<td align="right">0.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,201,954,912</td>
<td align="right">90.4%</td>
<td align="right">6,201,954,916</td>
<td align="right">92.6%</td>
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
<td align="right">222,247</td>
<td align="right">55.0%</td>
<td align="right">178,323</td>
<td align="right">49.6%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,890</td>
<td align="right">45.0%</td>
<td align="right">180,899</td>
<td align="right">50.4%</td>
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
<td align="left">array int</td>
<td align="right">26,640</td>
<td align="right">12.0%</td>
<td align="right">10,100</td>
<td align="right">5.7%</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,253</td>
<td align="right">9.6%</td>
<td align="right">10,732</td>
<td align="right">6.0%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">58,665</td>
<td align="right">26.4%</td>
<td align="right">42,905</td>
<td align="right">24.1%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">940</td>
<td align="right">0.4%</td>
<td align="right">920</td>
<td align="right">0.5%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">122</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">109,107</td>
<td align="right">49.1%</td>
<td align="right">108,022</td>
<td align="right">60.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">1.9%</td>
<td align="right">4,300</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">320</td>
<td align="right">0.1%</td>
<td align="right">320</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">171,256,633</td>
<td align="right">1.2%</td>
<td align="right">130,635,263</td>
<td align="right">0.9%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">660,378,305</td>
<td align="right">4.7%</td>
<td align="right">620,884,354</td>
<td align="right">4.4%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,467,992,016</td>
<td align="right">95.3%</td>
<td align="right">13,516,170,734</td>
<td align="right">95.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">33,000</td>
<td align="right">0.0%</td>
<td align="right">33,000</td>
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
<td align="right">3,758,709</td>
<td align="right">95.7%</td>
<td align="right">2,992,434</td>
<td align="right">94.7%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">167,564</td>
<td align="right">4.3%</td>
<td align="right">167,652</td>
<td align="right">5.3%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">156,711</td>
<td align="right">93.5%</td>
<td align="right">156,799</td>
<td align="right">93.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">10,490</td>
<td align="right">6.3%</td>
<td align="right">10,490</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,989</td>
<td align="right">1.8%</td>
<td align="right">2,989</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,003</td>
<td align="right">1.2%</td>
<td align="right">2,003</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">921</td>
<td align="right">0.5%</td>
<td align="right">921</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">363</td>
<td align="right">0.2%</td>
<td align="right">363</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">105,078,232</td>
<td align="right">1.8%</td>
<td align="right">54,823,519</td>
<td align="right">0.9%</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,333,470</td>
<td align="right">0.0%</td>
<td align="right">1,061,044</td>
<td align="right">0.0%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,721,976,471</td>
<td align="right">98.2%</td>
<td align="right">5,721,406,827</td>
<td align="right">99.0%</td>
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
<td align="right">164,754</td>
<td align="right">67.0%</td>
<td align="right">139,385</td>
<td align="right">64.8%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">81,196</td>
<td align="right">33.0%</td>
<td align="right">75,776</td>
<td align="right">35.2%</td>
<td align="right">-6.7%</td>
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
<td align="left">float long</td>
<td align="right">14,516</td>
<td align="right">8.8%</td>
<td align="right">9,158</td>
<td align="right">6.6%</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,389</td>
<td align="right">11.8%</td>
<td align="right">13,969</td>
<td align="right">10.0%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,700</td>
<td align="right">1.6%</td>
<td align="right">2,180</td>
<td align="right">1.6%</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">48,590</td>
<td align="right">29.5%</td>
<td align="right">40,866</td>
<td align="right">29.3%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,411</td>
<td align="right">10.6%</td>
<td align="right">15,576</td>
<td align="right">11.2%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">33,149</td>
<td align="right">20.1%</td>
<td align="right">29,849</td>
<td align="right">21.4%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,200</td>
<td align="right">7.4%</td>
<td align="right">11,034</td>
<td align="right">7.9%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">550</td>
<td align="right">0.3%</td>
<td align="right">530</td>
<td align="right">0.4%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,549</td>
<td align="right">0.9%</td>
<td align="right">1,523</td>
<td align="right">1.1%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">6.5%</td>
<td align="right">10,680</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,060</td>
<td align="right">1.9%</td>
<td align="right">3,060</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">960</td>
<td align="right">0.7%</td>
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
<td align="right">2,546,240</td>
<td align="right">0.1%</td>
<td align="right">755,400</td>
<td align="right">0.0%</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">51,853,125</td>
<td align="right">2.0%</td>
<td align="right">46,613,787</td>
<td align="right">1.8%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,486,651,416</td>
<td align="right">98.0%</td>
<td align="right">2,488,446,966</td>
<td align="right">98.2%</td>
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
<td align="left">Success</td>
<td align="right">61,299</td>
<td align="right">44.3%</td>
<td align="right">27,499</td>
<td align="right">27.3%</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">77,087</td>
<td align="right">55.7%</td>
<td align="right">73,171</td>
<td align="right">72.7%</td>
<td align="right">-5.1%</td>
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
<td align="right">28,013</td>
<td align="right">36.3%</td>
<td align="right">25,770</td>
<td align="right">35.2%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,410</td>
<td align="right">18.7%</td>
<td align="right">13,410</td>
<td align="right">18.3%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,182</td>
<td align="right">19.7%</td>
<td align="right">14,749</td>
<td align="right">20.2%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">19,482</td>
<td align="right">25.3%</td>
<td align="right">19,242</td>
<td align="right">26.3%</td>
<td align="right">-1.2%</td>
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
<td align="right">6,741,550</td>
<td align="right">0.6%</td>
<td align="right">2,271,806</td>
<td align="right">0.3%</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">566,097,830</td>
<td align="right">54.0%</td>
<td align="right">423,598,980</td>
<td align="right">47.5%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">481,034,701</td>
<td align="right">45.9%</td>
<td align="right">467,043,892</td>
<td align="right">52.4%</td>
<td align="right">-2.9%</td>
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
<td align="right">175,611</td>
<td align="right">46.9%</td>
<td align="right">91,265</td>
<td align="right">31.8%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">198,603</td>
<td align="right">53.1%</td>
<td align="right">196,180</td>
<td align="right">68.2%</td>
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
<td align="left">dict values</td>
<td align="right">4,956</td>
<td align="right">2.5%</td>
<td align="right">7,836</td>
<td align="right">4.0%</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,467</td>
<td align="right">1.2%</td>
<td align="right">1,707</td>
<td align="right">0.9%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,214</td>
<td align="right">18.2%</td>
<td align="right">33,106</td>
<td align="right">16.9%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,041</td>
<td align="right">5.6%</td>
<td align="right">10,204</td>
<td align="right">5.2%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,375</td>
<td align="right">5.7%</td>
<td align="right">10,796</td>
<td align="right">5.5%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4,661</td>
<td align="right">2.3%</td>
<td align="right">4,881</td>
<td align="right">2.5%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">2,744</td>
<td align="right">1.4%</td>
<td align="right">2,664</td>
<td align="right">1.4%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,202</td>
<td align="right">2.6%</td>
<td align="right">5,102</td>
<td align="right">2.6%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,565</td>
<td align="right">3.3%</td>
<td align="right">6,505</td>
<td align="right">3.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">619</td>
<td align="right">0.3%</td>
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,982</td>
<td align="right">52.9%</td>
<td align="right">104,982</td>
<td align="right">53.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,737</td>
<td align="right">3.4%</td>
<td align="right">6,737</td>
<td align="right">3.4%</td>
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
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.1%</td>
<td align="right">280</td>
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
<td align="right">403,084,270</td>
<td align="right">2.5%</td>
<td align="right">229,972,985</td>
<td align="right">1.5%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">303,860</td>
<td align="right">0.0%</td>
<td align="right">175,420</td>
<td align="right">0.0%</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,071,036,787</td>
<td align="right">6.7%</td>
<td align="right">721,567,558</td>
<td align="right">4.6%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,019,198,060</td>
<td align="right">93.3%</td>
<td align="right">15,105,099,338</td>
<td align="right">95.4%</td>
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
<td align="left">Success</td>
<td align="right">8,221,208</td>
<td align="right">90.5%</td>
<td align="right">4,956,033</td>
<td align="right">87.8%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">866,034</td>
<td align="right">9.5%</td>
<td align="right">690,980</td>
<td align="right">12.2%</td>
<td align="right">-20.2%</td>
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
<td align="right">159,467</td>
<td align="right">18.4%</td>
<td align="right">50,972</td>
<td align="right">7.4%</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,668</td>
<td align="right">2.0%</td>
<td align="right">13,920</td>
<td align="right">2.0%</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">157,112</td>
<td align="right">18.1%</td>
<td align="right">131,269</td>
<td align="right">19.0%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,385</td>
<td align="right">10.1%</td>
<td align="right">77,728</td>
<td align="right">11.2%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">89,753</td>
<td align="right">10.4%</td>
<td align="right">80,597</td>
<td align="right">11.7%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,735</td>
<td align="right">0.7%</td>
<td align="right">5,237</td>
<td align="right">0.8%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.1%</td>
<td align="right">1,060</td>
<td align="right">0.2%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">177,186</td>
<td align="right">20.5%</td>
<td align="right">165,224</td>
<td align="right">23.9%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,904</td>
<td align="right">0.3%</td>
<td align="right">2,719</td>
<td align="right">0.4%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,680</td>
<td align="right">3.1%</td>
<td align="right">25,000</td>
<td align="right">3.6%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">78,451</td>
<td align="right">9.1%</td>
<td align="right">75,463</td>
<td align="right">10.9%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,293</td>
<td align="right">2.3%</td>
<td align="right">19,951</td>
<td align="right">2.9%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,622</td>
<td align="right">1.8%</td>
<td align="right">15,362</td>
<td align="right">2.2%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2,542</td>
<td align="right">0.3%</td>
<td align="right">2,523</td>
<td align="right">0.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">17,609</td>
<td align="right">2.0%</td>
<td align="right">17,568</td>
<td align="right">2.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,425</td>
<td align="right">0.6%</td>
<td align="right">5,425</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.1%</td>
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
<tr>
<td align="left">property</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">4,957,083,972</td>
<td align="right">99.6%</td>
<td align="right">4,668,105,000</td>
<td align="right">99.6%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">435,667</td>
<td align="right">0.0%</td>
<td align="right">436,020</td>
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
<td align="right">20,324,363</td>
<td align="right">0.4%</td>
<td align="right">20,324,840</td>
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
<td align="right">9,556</td>
<td align="right">0.0%</td>
<td align="right">9,556</td>
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
<td align="right">467,967</td>
<td align="right">100.0%</td>
<td align="right">467,994</td>
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
<td align="right">86,075,416</td>
<td align="right">100.0%</td>
<td align="right">86,161,720</td>
<td align="right">100.0%</td>
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
<td align="right">7,623</td>
<td align="right">0.0%</td>
<td align="right">7,624</td>
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
<td align="right">7,561</td>
<td align="right">100.0%</td>
<td align="right">7,561</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">786,232,565</td>
<td align="right">81.9%</td>
<td align="right">786,232,614</td>
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
<td align="right">173,364,460</td>
<td align="right">18.1%</td>
<td align="right">173,364,454</td>
<td align="right">18.1%</td>
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
<td align="right">30,643</td>
<td align="right">0.0%</td>
<td align="right">30,643</td>
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
<td align="right">5,557</td>
<td align="right">8.5%</td>
<td align="right">5,557</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,734</td>
<td align="right">91.5%</td>
<td align="right">59,734</td>
<td align="right">91.5%</td>
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
<td align="right">55.5%</td>
<td align="right">33,180</td>
<td align="right">55.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,268</td>
<td align="right">23.9%</td>
<td align="right">14,268</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,020</td>
<td align="right">16.8%</td>
<td align="right">10,020</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
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
<td align="right">139,672,680</td>
<td align="right">5.3%</td>
<td align="right">99,141,848</td>
<td align="right">3.8%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">189,676,899</td>
<td align="right">7.2%</td>
<td align="right">136,954,915</td>
<td align="right">5.3%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,427,893,512</td>
<td align="right">92.7%</td>
<td align="right">2,459,470,552</td>
<td align="right">94.7%</td>
<td align="right">1.3%</td>
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
<td align="right">2,732,966</td>
<td align="right">96.7%</td>
<td align="right">1,968,401</td>
<td align="right">95.7%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">92,524</td>
<td align="right">3.3%</td>
<td align="right">87,819</td>
<td align="right">4.3%</td>
<td align="right">-5.1%</td>
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
<td align="right">31,964</td>
<td align="right">34.5%</td>
<td align="right">28,784</td>
<td align="right">32.8%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,185</td>
<td align="right">3.4%</td>
<td align="right">2,905</td>
<td align="right">3.3%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,663</td>
<td align="right">9.4%</td>
<td align="right">8,283</td>
<td align="right">9.4%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,077</td>
<td align="right">15.2%</td>
<td align="right">13,465</td>
<td align="right">15.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">5,003</td>
<td align="right">5.4%</td>
<td align="right">4,786</td>
<td align="right">5.4%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,075</td>
<td align="right">5.5%</td>
<td align="right">5,055</td>
<td align="right">5.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,419</td>
<td align="right">6.9%</td>
<td align="right">6,399</td>
<td align="right">7.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,769</td>
<td align="right">10.6%</td>
<td align="right">9,773</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,505</td>
<td align="right">8.1%</td>
<td align="right">7,505</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">804</td>
<td align="right">0.9%</td>
<td align="right">804</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">60</td>
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
<td align="right">271,897,647</td>
<td align="right">23.7%</td>
<td align="right">228,838,638</td>
<td align="right">20.7%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">875,194,709</td>
<td align="right">76.3%</td>
<td align="right">875,173,802</td>
<td align="right">79.3%</td>
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
<td align="right">110,609</td>
<td align="right">89.2%</td>
<td align="right">98,401</td>
<td align="right">88.0%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,370</td>
<td align="right">10.8%</td>
<td align="right">13,368</td>
<td align="right">12.0%</td>
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
<td align="right">14,280</td>
<td align="right">12.9%</td>
<td align="right">6,020</td>
<td align="right">6.1%</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">42,203</td>
<td align="right">38.2%</td>
<td align="right">38,523</td>
<td align="right">39.1%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,666</td>
<td align="right">6.9%</td>
<td align="right">7,398</td>
<td align="right">7.5%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,420</td>
<td align="right">39.3%</td>
<td align="right">43,420</td>
<td align="right">44.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,520</td>
<td align="right">1.4%</td>
<td align="right">1,520</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,520</td>
<td align="right">1.4%</td>
<td align="right">1,520</td>
<td align="right">1.5%</td>
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
<td align="right">208,466,682</td>
<td align="right">3.5%</td>
<td align="right">121,070,749</td>
<td align="right">2.1%</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,634,170</td>
<td align="right">0.4%</td>
<td align="right">18,087,021</td>
<td align="right">0.3%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,769,914,839</td>
<td align="right">96.5%</td>
<td align="right">5,742,270,758</td>
<td align="right">97.9%</td>
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
<td align="right">678,721</td>
<td align="right">72.0%</td>
<td align="right">536,600</td>
<td align="right">69.1%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">263,747</td>
<td align="right">28.0%</td>
<td align="right">239,927</td>
<td align="right">30.9%</td>
<td align="right">-9.0%</td>
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
<td align="right">19,890</td>
<td align="right">7.5%</td>
<td align="right">7,876</td>
<td align="right">3.3%</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,144</td>
<td align="right">2.3%</td>
<td align="right">5,104</td>
<td align="right">2.1%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">85,140</td>
<td align="right">32.3%</td>
<td align="right">76,231</td>
<td align="right">31.8%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">55,757</td>
<td align="right">21.1%</td>
<td align="right">54,621</td>
<td align="right">22.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12,204</td>
<td align="right">4.6%</td>
<td align="right">11,997</td>
<td align="right">5.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">37,532</td>
<td align="right">14.2%</td>
<td align="right">37,063</td>
<td align="right">15.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">17,205</td>
<td align="right">6.5%</td>
<td align="right">17,177</td>
<td align="right">7.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">26,983</td>
<td align="right">10.2%</td>
<td align="right">26,966</td>
<td align="right">11.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,749</td>
<td align="right">0.7%</td>
<td align="right">1,749</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">723</td>
<td align="right">0.3%</td>
<td align="right">723</td>
<td align="right">0.3%</td>
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
<td align="right">194,645</td>
<td align="right">0.0%</td>
<td align="right">97,484</td>
<td align="right">0.0%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,529,783,310</td>
<td align="right">100.0%</td>
<td align="right">1,529,573,201</td>
<td align="right">100.0%</td>
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
<td align="right">1,861</td>
<td align="right">5.7%</td>
<td align="right">1,783</td>
<td align="right">5.5%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,511</td>
<td align="right">94.3%</td>
<td align="right">30,521</td>
<td align="right">94.5%</td>
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
<td align="left">other</td>
<td align="right">380</td>
<td align="right">20.4%</td>
<td align="right">340</td>
<td align="right">19.1%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">267</td>
<td align="right">14.3%</td>
<td align="right">247</td>
<td align="right">13.9%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,214</td>
<td align="right">65.2%</td>
<td align="right">1,196</td>
<td align="right">67.1%</td>
<td align="right">-1.5%</td>
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
<td align="right">785,316,526</td>
<td align="right">0.8%</td>
<td align="right">507,480,822</td>
<td align="right">0.7%</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,740,857,203</td>
<td align="right">9.7%</td>
<td align="right">6,579,397,819</td>
<td align="right">9.5%</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">56,493,730,750</td>
<td align="right">56.1%</td>
<td align="right">38,511,776,899</td>
<td align="right">55.8%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">33,646,420,708</td>
<td align="right">33.4%</td>
<td align="right">23,449,666,063</td>
<td align="right">34.0%</td>
<td align="right">-30.3%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">105,078,232</td>
<td align="right">2.4%</td>
<td align="right">54,823,519</td>
<td align="right">1.6%</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">208,466,682</td>
<td align="right">4.8%</td>
<td align="right">121,070,749</td>
<td align="right">3.6%</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">407,641,105</td>
<td align="right">9.5%</td>
<td align="right">260,072,714</td>
<td align="right">7.8%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,071,036,787</td>
<td align="right">24.9%</td>
<td align="right">721,567,558</td>
<td align="right">21.6%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">189,676,899</td>
<td align="right">4.4%</td>
<td align="right">136,954,915</td>
<td align="right">4.1%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">657,541,622</td>
<td align="right">15.3%</td>
<td align="right">493,868,878</td>
<td align="right">14.8%</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">271,897,647</td>
<td align="right">6.3%</td>
<td align="right">228,838,638</td>
<td align="right">6.8%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">660,378,305</td>
<td align="right">15.4%</td>
<td align="right">620,884,354</td>
<td align="right">18.6%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">481,034,701</td>
<td align="right">11.2%</td>
<td align="right">467,043,892</td>
<td align="right">14.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,364,460</td>
<td align="right">4.0%</td>
<td align="right">173,364,454</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">121,738,550</td>
<td align="right">15.5%</td>
<td align="right">48,150,110</td>
<td align="right">9.5%</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,507,979</td>
<td align="right">4.5%</td>
<td align="right">19,202,947</td>
<td align="right">3.8%</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">37,874,434</td>
<td align="right">4.8%</td>
<td align="right">21,339,710</td>
<td align="right">4.2%</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">173,155,521</td>
<td align="right">22.0%</td>
<td align="right">113,628,628</td>
<td align="right">22.4%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">100,725,588</td>
<td align="right">12.8%</td>
<td align="right">68,267,359</td>
<td align="right">13.4%</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">115,800,616</td>
<td align="right">14.7%</td>
<td align="right">80,656,896</td>
<td align="right">15.9%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">23,848,398</td>
<td align="right">3.0%</td>
<td align="right">18,461,286</td>
<td align="right">3.6%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,177,240</td>
<td align="right">2.6%</td>
<td align="right">18,122,140</td>
<td align="right">3.6%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,446,299</td>
<td align="right">2.3%</td>
<td align="right">18,176,735</td>
<td align="right">3.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,497,285</td>
<td align="right">3.5%</td>
<td align="right">27,497,531</td>
<td align="right">5.4%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">852,318,276</td>
<td align="right">10.1%</td>
<td align="right">852,058,385</td>
<td align="right">10.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,669,243,064</td>
<td align="right">79.1%</td>
<td align="right">6,670,348,442</td>
<td align="right">79.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,156,774,487</td>
<td align="right">73.0%</td>
<td align="right">6,157,682,760</td>
<td align="right">73.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,644,622</td>
<td align="right">3.9%</td>
<td align="right">331,690,798</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,416,916,756</td>
<td align="right">16.8%</td>
<td align="right">1,417,111,677</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,421,365,197</td>
<td align="right">16.9%</td>
<td align="right">1,421,560,118</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">334,200,400</td>
<td align="right">4.0%</td>
<td align="right">334,235,597</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,273,683,473</td>
<td align="right">27.0%</td>
<td align="right">2,273,618,503</td>
<td align="right">27.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,273,683,473</td>
<td align="right">27.0%</td>
<td align="right">2,273,618,503</td>
<td align="right">27.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,097,696</td>
<td align="right">0.4%</td>
<td align="right">31,097,987</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,757,373</td>
<td align="right">1.0%</td>
<td align="right">84,757,760</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,336</td>
<td align="right">2.1%</td>
<td align="right">175,480,607</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,418,292</td>
<td align="right">0.1%</td>
<td align="right">4,418,292</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">30,149</td>
<td align="right">0.0%</td>
<td align="right">30,149</td>
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
<td align="left">Interpreter increfs</td>
<td align="right">45,679,645,053</td>
<td align="right">33.1%</td>
<td align="right">32,984,467,453</td>
<td align="right">23.8%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">61,541,576,403</td>
<td align="right">38.4%</td>
<td align="right">51,491,141,606</td>
<td align="right">31.9%</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">92,174,480,863</td>
<td align="right">66.9%</td>
<td align="right">105,852,437,935</td>
<td align="right">76.2%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">98,824,957,440</td>
<td align="right">61.6%</td>
<td align="right">109,859,493,365</td>
<td align="right">68.1%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,636,926,114</td>
<td align="right"></td>
<td align="right">2,515,072,209</td>
<td align="right"></td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,767,373</td>
<td align="right"></td>
<td align="right">6,566,509</td>
<td align="right"></td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">69,529,138</td>
<td align="right"></td>
<td align="right">68,040,032</td>
<td align="right"></td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">63,755,988</td>
<td align="right"></td>
<td align="right">62,467,251</td>
<td align="right"></td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,362,108,129</td>
<td align="right"></td>
<td align="right">4,356,271,335</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">92,955,544</td>
<td align="right">0.4%</td>
<td align="right">93,011,726</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">173,420,463</td>
<td align="right"></td>
<td align="right">173,470,234</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">15,359,492</td>
<td align="right">0.1%</td>
<td align="right">15,363,322</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,892,222,978</td>
<td align="right">52.6%</td>
<td align="right">12,893,228,953</td>
<td align="right">52.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,591,833,155</td>
<td align="right"></td>
<td align="right">13,592,890,480</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,783,907,942</td>
<td align="right">52.1%</td>
<td align="right">12,784,853,905</td>
<td align="right">52.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,636,748,733</td>
<td align="right">47.4%</td>
<td align="right">11,637,476,810</td>
<td align="right">47.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,638,651,765</td>
<td align="right"></td>
<td align="right">11,639,368,513</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,240</td>
<td align="right">2.0%</td>
<td align="right">3,382,240</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">127,883</td>
<td align="right">0.1%</td>
<td align="right">127,883</td>
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
<td align="right">113,922,208</td>
<td align="right">19,544,345,518</td>
<td align="right">0</td>
<td align="right">113,822,308</td>
<td align="right">19,521,508,981</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,972,166,364</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,972,288,956</td>
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
<td align="right">1,259</td>
<td align="right">0.1%</td>
<td align="right">3,380</td>
<td align="right">0.4%</td>
<td align="right">168.5%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">9,365</td>
<td align="right">1.0%</td>
<td align="right">20,461</td>
<td align="right">2.5%</td>
<td align="right">118.5%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">116.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">577,724</td>
<td align="right">60.4%</td>
<td align="right">292,770</td>
<td align="right">36.0%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">163,911</td>
<td align="right">17.1%</td>
<td align="right">235,212</td>
<td align="right">28.9%</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">791,239</td>
<td align="right">82.7%</td>
<td align="right">575,075</td>
<td align="right">70.7%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">265,890,822,958</td>
<td align="right">3,111.4%</td>
<td align="right">325,692,397,385</td>
<td align="right">3,153.2%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">925</td>
<td align="right">0.1%</td>
<td align="right">1,128</td>
<td align="right">0.1%</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">8,545,796,910</td>
<td align="right"></td>
<td align="right">10,328,988,862</td>
<td align="right"></td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,100</td>
<td align="right">0.3%</td>
<td align="right">3,700</td>
<td align="right">0.5%</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">956,409</td>
<td align="right"></td>
<td align="right">813,667</td>
<td align="right"></td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">8,441</td>
<td align="right">5.1%</td>
<td align="right">9,337</td>
<td align="right">4.0%</td>
<td align="right">10.6%</td>
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
<td align="right">2,622</td>
<td align="right">1.6%</td>
<td align="right">9,646</td>
<td align="right">4.1%</td>
<td align="right">267.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">163,911</td>
<td align="right"></td>
<td align="right">235,212</td>
<td align="right"></td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">155,023</td>
<td align="right">94.6%</td>
<td align="right">217,665</td>
<td align="right">92.5%</td>
<td align="right">40.4%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20 / 0 !!</td>
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
<td align="right">3,146</td>
<td align="right">1.9%</td>
<td align="right">3,618</td>
<td align="right">1.5%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">22,029</td>
<td align="right">13.4%</td>
<td align="right">18,600</td>
<td align="right">7.9%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">19,646</td>
<td align="right">12.0%</td>
<td align="right">25,074</td>
<td align="right">10.7%</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">47,379</td>
<td align="right">28.9%</td>
<td align="right">61,018</td>
<td align="right">25.9%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">36,680</td>
<td align="right">22.4%</td>
<td align="right">56,658</td>
<td align="right">24.1%</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21,318</td>
<td align="right">13.0%</td>
<td align="right">41,423</td>
<td align="right">17.6%</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">11,413</td>
<td align="right">7.0%</td>
<td align="right">23,861</td>
<td align="right">10.1%</td>
<td align="right">109.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,160</td>
<td align="right">1.3%</td>
<td align="right">4,480</td>
<td align="right">1.9%</td>
<td align="right">107.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">480</td>
<td align="right">0.2%</td>
<td align="right">242.9%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">19,176</td>
<td align="right">11.7%</td>
<td align="right">11,871</td>
<td align="right">5.0%</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,510</td>
<td align="right">10.1%</td>
<td align="right">22,307</td>
<td align="right">9.5%</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">33,475</td>
<td align="right">20.4%</td>
<td align="right">42,525</td>
<td align="right">18.1%</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">45,518</td>
<td align="right">27.8%</td>
<td align="right">60,895</td>
<td align="right">25.9%</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">24,259</td>
<td align="right">14.8%</td>
<td align="right">45,642</td>
<td align="right">19.4%</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">11,825</td>
<td align="right">7.2%</td>
<td align="right">24,870</td>
<td align="right">10.6%</td>
<td align="right">110.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,880</td>
<td align="right">2.4%</td>
<td align="right">8,294</td>
<td align="right">3.5%</td>
<td align="right">113.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">360</td>
<td align="right">0.2%</td>
<td align="right">1,241</td>
<td align="right">0.5%</td>
<td align="right">244.7%</td>
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
<td align="right">9,563,501</td>
<td align="right">31,863.6%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">367,098</td>
<td align="right">4,376.8%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,018,060</td>
<td align="right">85,720,480</td>
<td align="right">2,740.3%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,580,340</td>
<td align="right">90,426,560</td>
<td align="right">1,874.2%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,700,900</td>
<td align="right">44,752,400</td>
<td align="right">1,556.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">114,326,671</td>
<td align="right">1,553,193,158</td>
<td align="right">1,258.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,625,937</td>
<td align="right">457,084,766</td>
<td align="right">880.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,787,748</td>
<td align="right">36,964,514</td>
<td align="right">875.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">11,624</td>
<td align="right">113,112</td>
<td align="right">873.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">251,374</td>
<td align="right">2,335,896</td>
<td align="right">829.3%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,455,054</td>
<td align="right">59,155,227</td>
<td align="right">816.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">99,746,598</td>
<td align="right">890,833,076</td>
<td align="right">793.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">126,290,576</td>
<td align="right">865,688,466</td>
<td align="right">585.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,081,160</td>
<td align="right">12,626,060</td>
<td align="right">506.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">235,352,273</td>
<td align="right">1,385,770,192</td>
<td align="right">488.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">109,061,697</td>
<td align="right">520,081,586</td>
<td align="right">376.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,457,018</td>
<td align="right">37,559,124</td>
<td align="right">297.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">60,626,872</td>
<td align="right">233,733,033</td>
<td align="right">285.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">228,702,215</td>
<td align="right">844,144,666</td>
<td align="right">269.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">365,562</td>
<td align="right">1,266,261</td>
<td align="right">246.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">922,505,970</td>
<td align="right">2,919,195,016</td>
<td align="right">216.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,981,100</td>
<td align="right">7,935,460</td>
<td align="right">166.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">166,572,864</td>
<td align="right">396,858,545</td>
<td align="right">138.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">37,841,440</td>
<td align="right">87,132,180</td>
<td align="right">130.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">13,251,362</td>
<td align="right">30,355,608</td>
<td align="right">129.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">13,251,362</td>
<td align="right">30,310,016</td>
<td align="right">128.7%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">614,472</td>
<td align="right">1,274,130</td>
<td align="right">107.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">13,018,874</td>
<td align="right">26,657,450</td>
<td align="right">104.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,119,413</td>
<td align="right">109,908,108</td>
<td align="right">103.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,123,333</td>
<td align="right">109,915,728</td>
<td align="right">103.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,330,584</td>
<td align="right">16,843,938</td>
<td align="right">102.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">210,374,262</td>
<td align="right">418,934,664</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">112,481,015</td>
<td align="right">213,098,422</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">26,781,361</td>
<td align="right">48,055,402</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">75,104,876</td>
<td align="right">132,897,160</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">168,746,450</td>
<td align="right">294,666,048</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,399,603</td>
<td align="right">168,744,631</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">55,898,774</td>
<td align="right">96,514,303</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">845,967,875</td>
<td align="right">1,414,872,335</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">94,415,740</td>
<td align="right">155,625,500</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">95,269,420</td>
<td align="right">156,483,540</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,577,440</td>
<td align="right">9,126,726</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">171,478,955</td>
<td align="right">266,066,667</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">723,508,217</td>
<td align="right">1,121,235,908</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">6,789,006</td>
<td align="right">10,503,590</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">375,511,700</td>
<td align="right">580,555,994</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">376,738,960</td>
<td align="right">581,783,254</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">41,825,949</td>
<td align="right">64,298,295</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">64,114,920</td>
<td align="right">98,495,138</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">35,144,230</td>
<td align="right">53,675,262</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">66,045,642</td>
<td align="right">100,546,520</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,991,820</td>
<td align="right">10,563,846</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">186,764,011</td>
<td align="right">280,934,494</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">414,955,253</td>
<td align="right">614,779,022</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">185,629,530</td>
<td align="right">274,761,942</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,408,061,111</td>
<td align="right">2,065,396,342</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,807,689,466</td>
<td align="right">2,639,750,227</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">437,833,005</td>
<td align="right">635,874,794</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,825,860</td>
<td align="right">2,642,280</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">27,709,502</td>
<td align="right">39,918,881</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,066,773,166</td>
<td align="right">2,976,859,441</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,154,343,007</td>
<td align="right">3,098,755,822</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">159,387,100</td>
<td align="right">229,074,730</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,177,517,486</td>
<td align="right">3,124,274,022</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,867,155,672</td>
<td align="right">2,669,468,682</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,203,815</td>
<td align="right">152,007,502</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,979,826,827</td>
<td align="right">2,801,376,382</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">95,658,544</td>
<td align="right">135,309,891</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">103,276,016</td>
<td align="right">145,900,298</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">103,276,016</td>
<td align="right">145,900,298</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,927,851</td>
<td align="right">111,212,596</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">39,063,007</td>
<td align="right">54,895,350</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">162,993,245</td>
<td align="right">227,790,943</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">436,236,891</td>
<td align="right">607,803,781</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,761,674,276</td>
<td align="right">3,764,712,995</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">626,435,186</td>
<td align="right">849,569,403</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">143,040</td>
<td align="right">193,160</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">94,635,781</td>
<td align="right">127,791,284</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,963,216,695</td>
<td align="right">3,981,446,189</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">856,222,459</td>
<td align="right">1,149,337,570</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,090,696,284</td>
<td align="right">9,511,533,592</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,924,214,975</td>
<td align="right">3,892,825,589</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">471,225,280</td>
<td align="right">621,892,517</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">707,028,210</td>
<td align="right">931,082,096</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,331,481,173</td>
<td align="right">4,387,000,800</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,252,799,190</td>
<td align="right">1,642,647,119</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">5,730,323</td>
<td align="right">7,512,022</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">280,202,965</td>
<td align="right">367,302,234</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">825,470,691</td>
<td align="right">1,081,011,334</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">52,935,266</td>
<td align="right">68,585,698</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,397,401,637</td>
<td align="right">9,532,543,554</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,498,843,433</td>
<td align="right">1,922,597,244</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,355,572,373</td>
<td align="right">1,734,328,085</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,594,956,411</td>
<td align="right">4,589,059,142</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">876,574,454</td>
<td align="right">1,118,346,585</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,353,457,686</td>
<td align="right">9,377,730,742</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,479,087,033</td>
<td align="right">1,884,515,424</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">939,961,116</td>
<td align="right">1,197,203,813</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">185,046,560</td>
<td align="right">235,522,821</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,259,206</td>
<td align="right">5,416,240</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">122,707,771</td>
<td align="right">155,336,466</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">563,109,407</td>
<td align="right">712,743,718</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">390,531,070</td>
<td align="right">489,879,489</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,121,396,606</td>
<td align="right">5,140,241,698</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,107,915,226</td>
<td align="right">1,363,667,976</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">102,841,450</td>
<td align="right">126,411,215</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,906,618,436</td>
<td align="right">2,336,884,015</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">108,218,000</td>
<td align="right">131,422,419</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">18,392,492,134</td>
<td align="right">22,309,315,365</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">134,029,881</td>
<td align="right">162,088,040</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">978,507,152</td>
<td align="right">1,183,305,420</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">8,545,796,910</td>
<td align="right">10,328,988,862</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">7,614,593,605</td>
<td align="right">9,186,913,348</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">868,515,525</td>
<td align="right">1,035,057,621</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,231,201</td>
<td align="right">417,043,508</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,309,954,845</td>
<td align="right">1,558,489,395</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,581,085,628</td>
<td align="right">1,878,562,144</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,460,103,107</td>
<td align="right">5,290,056,255</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">689,651,195</td>
<td align="right">815,212,049</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">340,163,213</td>
<td align="right">402,031,452</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,071,640,619</td>
<td align="right">7,148,492,655</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">14,908,998,846</td>
<td align="right">17,522,282,516</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">235,875,560</td>
<td align="right">277,124,123</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">197,061,041</td>
<td align="right">230,828,619</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">238,789,743</td>
<td align="right">277,701,624</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">308,160,481</td>
<td align="right">357,200,958</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">245,080,655</td>
<td align="right">283,995,231</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,994,980</td>
<td align="right">1,678,900</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,436,740</td>
<td align="right">37,570,602</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,973,677,219</td>
<td align="right">11,474,833,293</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,080,966,151</td>
<td align="right">1,239,762,276</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">864,127,753</td>
<td align="right">990,370,946</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,119,104,253</td>
<td align="right">1,281,001,701</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,598,976,727</td>
<td align="right">1,828,501,019</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,096,877,160</td>
<td align="right">1,252,386,520</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,035,208,952</td>
<td align="right">1,175,458,469</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">959,868,840</td>
<td align="right">1,088,407,334</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">375,780</td>
<td align="right">425,220</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,308,855</td>
<td align="right">102,114,140</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">559,022,320</td>
<td align="right">631,195,305</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">528,296,320</td>
<td align="right">594,784,871</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">273,928,919</td>
<td align="right">306,956,546</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">85,708,668</td>
<td align="right">96,023,402</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,318,040</td>
<td align="right">36,197,600</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">11,492,440</td>
<td align="right">12,803,725</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,438,704,208</td>
<td align="right">1,602,365,547</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,820,785,360</td>
<td align="right">2,016,336,563</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,340,485,249</td>
<td align="right">2,586,201,954</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">656,968,180</td>
<td align="right">723,701,873</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">981,497,516</td>
<td align="right">1,076,854,234</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">63,348,593</td>
<td align="right">69,369,939</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">377,553,422</td>
<td align="right">413,270,910</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">555,625,471</td>
<td align="right">606,566,080</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,528,269,477</td>
<td align="right">1,668,173,168</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,160,396,854</td>
<td align="right">5,600,167,954</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,509,822,986</td>
<td align="right">2,723,261,397</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">233,632,635</td>
<td align="right">252,899,594</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,570,655,689</td>
<td align="right">6,014,764,677</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">531,632,326</td>
<td align="right">573,732,129</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,792,870</td>
<td align="right">173,149,154</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,137,986</td>
<td align="right">104,370,856</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,851,498,634</td>
<td align="right">1,987,051,607</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,910,348,969</td>
<td align="right">2,048,028,088</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">603,925,399</td>
<td align="right">647,071,588</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">125,443,220</td>
<td align="right">134,138,462</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,464,786,274</td>
<td align="right">1,565,391,524</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">162,167,334</td>
<td align="right">173,266,147</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,034,367,189</td>
<td align="right">1,102,393,593</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">673,451,924</td>
<td align="right">716,523,356</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,061,281</td>
<td align="right">10,702,014</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,885</td>
<td align="right">1,641,634</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,751,730,626</td>
<td align="right">3,987,272,714</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,088,666</td>
<td align="right">102,962,030</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,343,354,979</td>
<td align="right">1,422,668,437</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,316,434</td>
<td align="right">1,393,020</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">9,355,123,449</td>
<td align="right">9,895,028,516</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,660,955,226</td>
<td align="right">2,813,813,632</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,445,212,944</td>
<td align="right">3,634,772,981</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,717,604,217</td>
<td align="right">1,811,087,365</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,246,254,613</td>
<td align="right">1,312,829,496</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">167,977,090</td>
<td align="right">176,452,830</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,842,300</td>
<td align="right">162,296,000</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">57,780,100</td>
<td align="right">60,241,196</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">986,073,338</td>
<td align="right">1,027,432,872</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,412,436,465</td>
<td align="right">3,552,585,375</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,173,130</td>
<td align="right">808,798,743</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">779,530,890</td>
<td align="right">810,156,503</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,193,177,858</td>
<td align="right">14,665,602,355</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,439,877</td>
<td align="right">623,510,410</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,022,731,763</td>
<td align="right">3,116,239,977</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">325,692,182</td>
<td align="right">335,534,947</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,598,894,501</td>
<td align="right">3,707,594,043</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,622,100,664</td>
<td align="right">4,742,748,630</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">228,477,524</td>
<td align="right">234,336,936</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">142,373,169</td>
<td align="right">146,014,471</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">27,411,340</td>
<td align="right">28,040,006</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">329,380</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">901,433,367</td>
<td align="right">921,019,669</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,347,769,703</td>
<td align="right">2,395,578,788</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">51,906,580</td>
<td align="right">52,950,720</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,249,631</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,361,516,579</td>
<td align="right">2,404,550,564</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,055,272,195</td>
<td align="right">2,091,014,214</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">916,709,523</td>
<td align="right">928,934,776</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">440,492,422</td>
<td align="right">444,425,484</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,102,246</td>
<td align="right">522,637,920</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,745,752</td>
<td align="right">737,010,779</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,725,937</td>
<td align="right">69,178,991</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,769,000</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,007,580</td>
<td align="right">81,479,682</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">532,673,160</td>
<td align="right">529,654,970</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">590,540</td>
<td align="right">590,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">24,662</td>
<td align="right">24,662</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALLER_IP</td>
<td align="right"></td>
<td align="right">3,171,962,362</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">245,706,757</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">38,548,945</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_INIT_CHECK</td>
<td align="right"></td>
<td align="right">1,665,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">89,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">51,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_UPDATE</td>
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
<td align="left">CALL_KW</td>
<td align="right">36,484</td>
<td align="right">62,340</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">11,221</td>
<td align="right">15,302</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">43,445</td>
<td align="right">50,643</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">126,927</td>
<td align="right">144,099</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,260</td>
<td align="right">34,890</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">920</td>
<td align="right">920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right"></td>
<td align="right">220</td>
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
<td align="right">1,152</td>
<td align="right">1,153</td>
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
<td align="right">1,152</td>
<td align="right">1,153</td>
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
<td align="right">460</td>
<td align="right">460</td>
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
<td align="right">1,801</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-08-13
