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
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">6</td>
<td align="right">66</td>
<td align="right">1,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">574</td>
<td align="right">2,032</td>
<td align="right">254.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20</td>
<td align="right">60</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,134</td>
<td align="right">3,346</td>
<td align="right">195.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,531,768</td>
<td align="right">684,747</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">252</td>
<td align="right">126</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">12,308</td>
<td align="right">6,159</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">14,657</td>
<td align="right">7,349</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">9,390</td>
<td align="right">4,728</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">380,975</td>
<td align="right">191,870</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,904</td>
<td align="right">959</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,936,154</td>
<td align="right">1,982,851</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,190</td>
<td align="right">2,111</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,330,853</td>
<td align="right">1,174,551</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,188,075</td>
<td align="right">3,118,339</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2,763,640</td>
<td align="right">1,392,697</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,098,168</td>
<td align="right">553,407</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">707,644</td>
<td align="right">356,608</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">127</td>
<td align="right">64</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,898,273</td>
<td align="right">1,964,488</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,098,046</td>
<td align="right">553,348</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">707,648</td>
<td align="right">356,612</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">353,824</td>
<td align="right">178,306</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">396,370</td>
<td align="right">199,747</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,101,357</td>
<td align="right">555,021</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,186,109</td>
<td align="right">1,605,648</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,510,539</td>
<td align="right">1,769,156</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,686,754</td>
<td align="right">850,050</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,208,075</td>
<td align="right">608,819</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">604,166</td>
<td align="right">304,475</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">15,899,615</td>
<td align="right">8,012,794</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">14,811,018</td>
<td align="right">7,464,209</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">711,495</td>
<td align="right">358,569</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,205,747</td>
<td align="right">1,111,626</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,618,852</td>
<td align="right">815,853</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,421,115</td>
<td align="right">1,724,147</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">504,099</td>
<td align="right">254,052</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,466,186</td>
<td align="right">5,274,711</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,887,951</td>
<td align="right">3,471,398</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">358,257</td>
<td align="right">180,556</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,949,490</td>
<td align="right">1,486,504</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,718,981</td>
<td align="right">866,381</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,471,994</td>
<td align="right">5,278,020</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">355,444</td>
<td align="right">179,149</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">54,736,379</td>
<td align="right">27,588,472</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,943,635</td>
<td align="right">1,483,673</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">23,872,048</td>
<td align="right">12,032,200</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">141,125</td>
<td align="right">71,132</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">735,097</td>
<td align="right">370,516</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">23,129,647</td>
<td align="right">11,658,202</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">85,106,506</td>
<td align="right">42,897,132</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,630,484</td>
<td align="right">3,342,072</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,571,826</td>
<td align="right">6,840,843</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,794,478</td>
<td align="right">904,540</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">355,952</td>
<td align="right">179,425</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,602,937</td>
<td align="right">808,001</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">11,508,857</td>
<td align="right">5,801,676</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">355,985</td>
<td align="right">179,458</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,378,580</td>
<td align="right">3,719,850</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">175,846,758</td>
<td align="right">88,653,212</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,260,721</td>
<td align="right">6,181,289</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,215,087</td>
<td align="right">7,166,643</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,470,562</td>
<td align="right">2,758,034</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">43,243,788</td>
<td align="right">21,801,870</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">50,266,072</td>
<td align="right">25,342,341</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,392,073</td>
<td align="right">1,206,034</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,795,301</td>
<td align="right">905,175</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">5,618,575</td>
<td align="right">2,833,030</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">405,899</td>
<td align="right">204,677</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,895,624</td>
<td align="right">3,477,181</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">399,392</td>
<td align="right">201,404</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,274,341</td>
<td align="right">1,146,909</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,248,943</td>
<td align="right">629,840</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">5,267,817</td>
<td align="right">2,656,782</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,704,782</td>
<td align="right">3,381,629</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">6,456,329</td>
<td align="right">3,256,381</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">14,047,353</td>
<td align="right">7,085,411</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">963,586</td>
<td align="right">486,046</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,407,183</td>
<td align="right">6,258,709</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,829,788</td>
<td align="right">4,454,121</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">357,245</td>
<td align="right">180,212</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,573,321</td>
<td align="right">793,775</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,480,518</td>
<td align="right">5,792,830</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,174,015</td>
<td align="right">592,401</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">6,232</td>
<td align="right">3,145</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,733,290</td>
<td align="right">874,724</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">711,477</td>
<td align="right">359,055</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,689,564</td>
<td align="right">852,734</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,224,275</td>
<td align="right">617,900</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,441,689</td>
<td align="right">2,746,993</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">910,606</td>
<td align="right">459,775</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">419,088</td>
<td align="right">211,692</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,131,481</td>
<td align="right">2,592,153</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,766,363</td>
<td align="right">892,489</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,142,870</td>
<td align="right">577,784</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">739,220</td>
<td align="right">374,024</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">741,527</td>
<td align="right">375,197</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,621,062</td>
<td align="right">820,292</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,938</td>
<td align="right">1,489</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">10,988</td>
<td align="right">5,570</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">12,269</td>
<td align="right">6,221</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">702,437</td>
<td align="right">356,434</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">128</td>
<td align="right">65</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,026</td>
<td align="right">522</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">7,973</td>
<td align="right">4,067</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">130</td>
<td align="right">67</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">130</td>
<td align="right">67</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">130</td>
<td align="right">67</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">7,807,620</td>
<td align="right">4,026,537</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">393</td>
<td align="right">204</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">131</td>
<td align="right">68</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">6,736</td>
<td align="right">3,523</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">42</td>
<td align="right">62</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,747</td>
<td align="right">17,892</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,091</td>
<td align="right">586</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,589</td>
<td align="right">1,951</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,076,293</td>
<td align="right">585,979</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,400</td>
<td align="right">2,943</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">140</td>
<td align="right">77</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">281</td>
<td align="right">155</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">141</td>
<td align="right">78</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">845,911</td>
<td align="right">471,383</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">167</td>
<td align="right">104</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">175</td>
<td align="right">112</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,637</td>
<td align="right">2,755</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">4,687</td>
<td align="right">3,620</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">4,608</td>
<td align="right">3,725</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,226</td>
<td align="right">2,346</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">43</td>
<td align="right">42</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">109</td>
<td align="right">108</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">110</td>
<td align="right">109</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">120</td>
<td align="right">119</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">419</td>
<td align="right">418</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,404</td>
<td align="right">1,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,028</td>
<td align="right">1,028</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">583</td>
<td align="right">583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">326</td>
<td align="right">326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">218</td>
<td align="right">218</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">48</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">39</td>
<td align="right">39</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">36</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">33</td>
<td align="right">33</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">32</td>
<td align="right">32</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">31</td>
<td align="right">31</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">30</td>
<td align="right">30</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">10</td>
<td align="right">10</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">9</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">31,667,119</td>
<td align="right">85.3%</td>
<td align="right">15,963,068</td>
<td align="right">85.3%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,438,872</td>
<td align="right">14.7%</td>
<td align="right">2,743,708</td>
<td align="right">14.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,832</td>
<td align="right">0.0%</td>
<td align="right">1,706</td>
<td align="right">0.0%</td>
<td align="right">-6.9%</td>
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
<td align="right">304</td>
<td align="right">10.7%</td>
<td align="right">1,323</td>
<td align="right">39.9%</td>
<td align="right">335.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,543</td>
<td align="right">89.3%</td>
<td align="right">1,992</td>
<td align="right">60.1%</td>
<td align="right">-21.7%</td>
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
<td align="right">23</td>
<td align="right">0.9%</td>
<td align="right">43</td>
<td align="right">2.2%</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">52</td>
<td align="right">2.0%</td>
<td align="right">32</td>
<td align="right">1.6%</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,727</td>
<td align="right">67.9%</td>
<td align="right">1,310</td>
<td align="right">65.8%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">553</td>
<td align="right">21.7%</td>
<td align="right">423</td>
<td align="right">21.2%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">52</td>
<td align="right">2.0%</td>
<td align="right">50</td>
<td align="right">2.5%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">73</td>
<td align="right">2.9%</td>
<td align="right">71</td>
<td align="right">3.6%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">48</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">6</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
<td align="right">1,224,275</td>
<td align="right">100.0%</td>
<td align="right">617,900</td>
<td align="right">100.0%</td>
<td align="right">-49.5%</td>
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
<td align="right">29,308,562</td>
<td align="right">83.5%</td>
<td align="right">14,770,936</td>
<td align="right">83.5%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,785,417</td>
<td align="right">16.5%</td>
<td align="right">2,918,147</td>
<td align="right">16.5%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,676,760</td>
<td align="right">16.2%</td>
<td align="right">2,863,623</td>
<td align="right">16.2%</td>
<td align="right">-49.6%</td>
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
<td align="right">109,791</td>
<td align="right">100.0%</td>
<td align="right">57,870</td>
<td align="right">100.0%</td>
<td align="right">-47.3%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">10</td>
<td align="right">50.0%</td>
<td align="right">10</td>
<td align="right">16.7%</td>
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
<td align="right">10</td>
<td align="right">100.0%</td>
<td align="right">50</td>
<td align="right">100.0%</td>
<td align="right">400.0%</td>
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
<td align="right">15,094</td>
<td align="right">0.1%</td>
<td align="right">7,578</td>
<td align="right">0.1%</td>
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
<td align="right">26,304,783</td>
<td align="right">94.1%</td>
<td align="right">13,258,309</td>
<td align="right">94.1%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,619,580</td>
<td align="right">5.8%</td>
<td align="right">818,777</td>
<td align="right">5.8%</td>
<td align="right">-49.4%</td>
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
<td align="right">24.0%</td>
<td align="right">595</td>
<td align="right">36.2%</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,336</td>
<td align="right">76.0%</td>
<td align="right">1,049</td>
<td align="right">63.8%</td>
<td align="right">-21.5%</td>
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
<td align="right">186</td>
<td align="right">13.9%</td>
<td align="right">122</td>
<td align="right">11.6%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">92</td>
<td align="right">6.9%</td>
<td align="right">70</td>
<td align="right">6.7%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">200</td>
<td align="right">15.0%</td>
<td align="right">154</td>
<td align="right">14.7%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">677</td>
<td align="right">50.7%</td>
<td align="right">524</td>
<td align="right">50.0%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">175</td>
<td align="right">13.1%</td>
<td align="right">173</td>
<td align="right">16.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6</td>
<td align="right">0.4%</td>
<td align="right">6</td>
<td align="right">0.6%</td>
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
<td align="right">6,754,800</td>
<td align="right">88.1%</td>
<td align="right">3,404,649</td>
<td align="right">88.1%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">909,743</td>
<td align="right">11.9%</td>
<td align="right">458,789</td>
<td align="right">11.9%</td>
<td align="right">-49.6%</td>
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
<td align="right">46</td>
<td align="right">5.3%</td>
<td align="right">246</td>
<td align="right">24.9%</td>
<td align="right">434.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">817</td>
<td align="right">94.7%</td>
<td align="right">740</td>
<td align="right">75.1%</td>
<td align="right">-9.4%</td>
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
<td align="right">268</td>
<td align="right">32.8%</td>
<td align="right">225</td>
<td align="right">30.4%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">479</td>
<td align="right">58.6%</td>
<td align="right">447</td>
<td align="right">60.4%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">8.3%</td>
<td align="right">66</td>
<td align="right">8.9%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">2</td>
<td align="right">0.3%</td>
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
<td align="right">2,184,505</td>
<td align="right">72.1%</td>
<td align="right">1,145,906</td>
<td align="right">70.9%</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">845,508</td>
<td align="right">27.9%</td>
<td align="right">471,069</td>
<td align="right">29.1%</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">43</td>
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
<td align="right">385</td>
<td align="right">95.3%</td>
<td align="right">297</td>
<td align="right">94.3%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">19</td>
<td align="right">4.7%</td>
<td align="right">18</td>
<td align="right">5.7%</td>
<td align="right">-5.3%</td>
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
<td align="right">23</td>
<td align="right">6.0%</td>
<td align="right">43</td>
<td align="right">14.5%</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">188</td>
<td align="right">48.8%</td>
<td align="right">124</td>
<td align="right">41.8%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">163</td>
<td align="right">42.3%</td>
<td align="right">119</td>
<td align="right">40.1%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">8</td>
<td align="right">2.1%</td>
<td align="right">8</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1</td>
<td align="right">0.3%</td>
<td align="right">1</td>
<td align="right">0.3%</td>
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
<td align="right">18,976</td>
<td align="right">0.0%</td>
<td align="right">7,840</td>
<td align="right">0.0%</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">119,281,377</td>
<td align="right">95.9%</td>
<td align="right">60,116,142</td>
<td align="right">95.9%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,126,679</td>
<td align="right">4.1%</td>
<td align="right">2,584,124</td>
<td align="right">4.1%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">1,193</td>
<td align="right">25.0%</td>
<td align="right">5,165</td>
<td align="right">65.3%</td>
<td align="right">332.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,588</td>
<td align="right">75.0%</td>
<td align="right">2,741</td>
<td align="right">34.7%</td>
<td align="right">-23.6%</td>
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
<td align="right">387</td>
<td align="right">10.8%</td>
<td align="right">282</td>
<td align="right">10.3%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,391</td>
<td align="right">66.6%</td>
<td align="right">1,810</td>
<td align="right">66.0%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">184</td>
<td align="right">5.1%</td>
<td align="right">140</td>
<td align="right">5.1%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">267</td>
<td align="right">7.4%</td>
<td align="right">241</td>
<td align="right">8.8%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">22</td>
<td align="right">0.6%</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">22</td>
<td align="right">0.6%</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">-4.5%</td>
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
<td align="right">1,143</td>
<td align="right">0.0%</td>
<td align="right">576</td>
<td align="right">0.0%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">20,918,726</td>
<td align="right">100.0%</td>
<td align="right">10,547,696</td>
<td align="right">100.0%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">244</td>
<td align="right">0.0%</td>
<td align="right">243</td>
<td align="right">0.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">330</td>
<td align="right">100.0%</td>
<td align="right">1,789</td>
<td align="right">100.0%</td>
<td align="right">442.1%</td>
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
<td align="right">382</td>
<td align="right">98.5%</td>
<td align="right">193</td>
<td align="right">74.5%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3</td>
<td align="right">0.8%</td>
<td align="right">3</td>
<td align="right">1.2%</td>
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
<td align="right">3</td>
<td align="right">100.0%</td>
<td align="right">63</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">1,141,952</td>
<td align="right">7.8%</td>
<td align="right">575,582</td>
<td align="right">7.8%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,569,535</td>
<td align="right">92.1%</td>
<td align="right">6,839,539</td>
<td align="right">92.1%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,599</td>
<td align="right">0.1%</td>
<td align="right">7,463</td>
<td align="right">0.1%</td>
<td align="right">-48.9%</td>
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
<td align="right">430</td>
<td align="right">36.7%</td>
<td align="right">1,666</td>
<td align="right">72.7%</td>
<td align="right">287.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">742</td>
<td align="right">63.3%</td>
<td align="right">626</td>
<td align="right">27.3%</td>
<td align="right">-15.6%</td>
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
<td align="right">314</td>
<td align="right">42.3%</td>
<td align="right">249</td>
<td align="right">39.8%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">226</td>
<td align="right">30.5%</td>
<td align="right">180</td>
<td align="right">28.8%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">22</td>
<td align="right">3.0%</td>
<td align="right">21</td>
<td align="right">3.4%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">180</td>
<td align="right">24.3%</td>
<td align="right">176</td>
<td align="right">28.1%</td>
<td align="right">-2.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,988,729</td>
<td align="right">99.9%</td>
<td align="right">1,506,213</td>
<td align="right">99.8%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,196</td>
<td align="right">0.1%</td>
<td align="right">2,196</td>
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
<td align="left">Success</td>
<td align="right">23</td>
<td align="right">76.7%</td>
<td align="right">143</td>
<td align="right">95.3%</td>
<td align="right">521.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7</td>
<td align="right">23.3%</td>
<td align="right">7</td>
<td align="right">4.7%</td>
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
<td align="left">bytearray int</td>
<td align="right">6</td>
<td align="right">85.7%</td>
<td align="right">6</td>
<td align="right">85.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">14.3%</td>
<td align="right">1</td>
<td align="right">14.3%</td>
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
<td align="right">20,705,650</td>
<td align="right">76.1%</td>
<td align="right">10,437,867</td>
<td align="right">76.1%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,454,376</td>
<td align="right">23.7%</td>
<td align="right">3,254,731</td>
<td align="right">23.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,506</td>
<td align="right">0.2%</td>
<td align="right">26,760</td>
<td align="right">0.2%</td>
<td align="right">-49.0%</td>
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
<td align="right">1,847</td>
<td align="right">63.1%</td>
<td align="right">1,024</td>
<td align="right">47.4%</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,080</td>
<td align="right">36.9%</td>
<td align="right">1,138</td>
<td align="right">52.6%</td>
<td align="right">5.4%</td>
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
<td align="left">mapping</td>
<td align="right">158</td>
<td align="right">8.6%</td>
<td align="right">74</td>
<td align="right">7.2%</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,365</td>
<td align="right">73.9%</td>
<td align="right">693</td>
<td align="right">67.7%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">229</td>
<td align="right">12.4%</td>
<td align="right">164</td>
<td align="right">16.0%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">25</td>
<td align="right">1.4%</td>
<td align="right">24</td>
<td align="right">2.3%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">70</td>
<td align="right">3.8%</td>
<td align="right">69</td>
<td align="right">6.7%</td>
<td align="right">-1.4%</td>
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
<td align="right">746,336</td>
<td align="right">100.0%</td>
<td align="right">376,903</td>
<td align="right">100.0%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">11</td>
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
<td align="right">31</td>
<td align="right">100.0%</td>
<td align="right">51</td>
<td align="right">100.0%</td>
<td align="right">64.5%</td>
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
<td align="right">381,362,066</td>
<td align="right">49.6%</td>
<td align="right">192,191,370</td>
<td align="right">49.6%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">5,889,871</td>
<td align="right">0.8%</td>
<td align="right">2,970,227</td>
<td align="right">0.8%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">358,360,448</td>
<td align="right">46.6%</td>
<td align="right">180,778,137</td>
<td align="right">46.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">22,778,225</td>
<td align="right">3.0%</td>
<td align="right">11,550,573</td>
<td align="right">3.0%</td>
<td align="right">-49.3%</td>
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
<td align="right">1,141,952</td>
<td align="right">4.0%</td>
<td align="right">575,582</td>
<td align="right">4.0%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,126,679</td>
<td align="right">18.0%</td>
<td align="right">2,584,124</td>
<td align="right">18.0%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">6,454,376</td>
<td align="right">22.7%</td>
<td align="right">3,254,731</td>
<td align="right">22.6%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">909,743</td>
<td align="right">3.2%</td>
<td align="right">458,789</td>
<td align="right">3.2%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,676,760</td>
<td align="right">20.0%</td>
<td align="right">2,863,623</td>
<td align="right">19.9%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,438,872</td>
<td align="right">19.1%</td>
<td align="right">2,743,708</td>
<td align="right">19.1%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,224,275</td>
<td align="right">4.3%</td>
<td align="right">617,900</td>
<td align="right">4.3%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,619,580</td>
<td align="right">5.7%</td>
<td align="right">818,777</td>
<td align="right">5.7%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">845,508</td>
<td align="right">3.0%</td>
<td align="right">471,069</td>
<td align="right">3.3%</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,196</td>
<td align="right">0.0%</td>
<td align="right">2,196</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,333</td>
<td align="right">0.1%</td>
<td align="right">2,238</td>
<td align="right">0.1%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,830</td>
<td align="right">0.2%</td>
<td align="right">4,608</td>
<td align="right">0.2%</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,238</td>
<td align="right">0.4%</td>
<td align="right">12,987</td>
<td align="right">0.4%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">11,252</td>
<td align="right">0.2%</td>
<td align="right">5,628</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">15,094</td>
<td align="right">0.3%</td>
<td align="right">7,578</td>
<td align="right">0.3%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,272</td>
<td align="right">0.1%</td>
<td align="right">4,156</td>
<td align="right">0.1%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">273,388</td>
<td align="right">4.6%</td>
<td align="right">137,770</td>
<td align="right">4.6%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,751,565</td>
<td align="right">46.7%</td>
<td align="right">1,387,728</td>
<td align="right">46.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,749,356</td>
<td align="right">46.7%</td>
<td align="right">1,387,063</td>
<td align="right">46.7%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">25,764</td>
<td align="right">0.4%</td>
<td align="right">13,521</td>
<td align="right">0.5%</td>
<td align="right">-47.5%</td>
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
<td align="right">355,271</td>
<td align="right">1.5%</td>
<td align="right">179,060</td>
<td align="right">1.5%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">23,472,923</td>
<td align="right">98.3%</td>
<td align="right">11,831,001</td>
<td align="right">98.3%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">23,129,664</td>
<td align="right">96.9%</td>
<td align="right">11,658,219</td>
<td align="right">96.9%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">399,431</td>
<td align="right">1.7%</td>
<td align="right">201,442</td>
<td align="right">1.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">399,465</td>
<td align="right">1.7%</td>
<td align="right">201,476</td>
<td align="right">1.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">399,474</td>
<td align="right">1.7%</td>
<td align="right">201,485</td>
<td align="right">1.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">399,474</td>
<td align="right">1.7%</td>
<td align="right">201,485</td>
<td align="right">1.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">14,733</td>
<td align="right">0.1%</td>
<td align="right">7,488</td>
<td align="right">0.1%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">258</td>
<td align="right">0.0%</td>
<td align="right">132</td>
<td align="right">0.0%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">76</td>
<td align="right">0.0%</td>
<td align="right">76</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">682</td>
<td align="right"></td>
<td align="right">1,155</td>
<td align="right"></td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,365,936</td>
<td align="right"></td>
<td align="right">4,887,670</td>
<td align="right"></td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">57,762,621</td>
<td align="right">11.5%</td>
<td align="right">28,762,793</td>
<td align="right">11.4%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">68,868,201</td>
<td align="right">13.8%</td>
<td align="right">34,580,794</td>
<td align="right">13.7%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">335,629,655</td>
<td align="right">69.5%</td>
<td align="right">169,025,795</td>
<td align="right">69.4%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">371,290,244</td>
<td align="right">74.2%</td>
<td align="right">187,044,541</td>
<td align="right">74.3%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">368,537</td>
<td align="right"></td>
<td align="right">185,774</td>
<td align="right"></td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,266,631</td>
<td align="right">0.9%</td>
<td align="right">2,151,489</td>
<td align="right">0.9%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">220,003</td>
<td align="right">0.7%</td>
<td align="right">110,950</td>
<td align="right">0.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">74,032,467</td>
<td align="right">15.3%</td>
<td align="right">37,345,859</td>
<td align="right">15.3%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">1,798,112</td>
<td align="right"></td>
<td align="right">907,094</td>
<td align="right"></td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,154,021</td>
<td align="right"></td>
<td align="right">3,610,280</td>
<td align="right"></td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">2,757,285</td>
<td align="right">0.6%</td>
<td align="right">1,392,949</td>
<td align="right">0.6%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,916</td>
<td align="right">0.0%</td>
<td align="right">4,506</td>
<td align="right">0.0%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">69,269,389</td>
<td align="right">14.3%</td>
<td align="right">35,038,036</td>
<td align="right">14.4%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">21,464,614</td>
<td align="right"></td>
<td align="right">10,859,128</td>
<td align="right"></td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">21,468,166</td>
<td align="right">64.6%</td>
<td align="right">10,862,679</td>
<td align="right">64.6%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,755,521</td>
<td align="right">35.4%</td>
<td align="right">5,951,287</td>
<td align="right">35.4%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,526,602</td>
<td align="right">34.7%</td>
<td align="right">5,835,831</td>
<td align="right">34.7%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">4,843</td>
<td align="right"></td>
<td align="right">3,460</td>
<td align="right"></td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">5,409</td>
<td align="right"></td>
<td align="right">4,342</td>
<td align="right"></td>
<td align="right">-19.7%</td>
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
<td align="right">1,058</td>
<td align="right">296,258</td>
<td align="right">19,237,915</td>
<td align="right">1,398,652</td>
<td align="right">1,659,966</td>
<td align="right">534</td>
<td align="right">229</td>
<td align="right">9,138,659</td>
<td align="right">858,510</td>
<td align="right">620,520</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">83</td>
<td align="right">3.7%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">1,531,605</td>
<td align="right"></td>
<td align="right">684,788</td>
<td align="right"></td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">2,259</td>
<td align="right"></td>
<td align="right">1,106</td>
<td align="right"></td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">2,132</td>
<td align="right">94.4%</td>
<td align="right">1,062</td>
<td align="right">96.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">52,011,140</td>
<td align="right">3,395.9%</td>
<td align="right">26,411,727</td>
<td align="right">3,856.9%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">44</td>
<td align="right">1.9%</td>
<td align="right">44</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
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
<td align="right">44</td>
<td align="right"></td>
<td align="right">44</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">44</td>
<td align="right">100.0%</td>
<td align="right">44</td>
<td align="right">100.0%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">12,288</td>
<td align="right">3.4%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">364,544</td>
<td align="right"></td>
<td align="right">364,544</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">285,551</td>
<td align="right">78.3%</td>
<td align="right">285,551</td>
<td align="right">78.3%</td>
<td align="right">0.0%</td>
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
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">8,312</td>
<td align="right">2.3%</td>
<td align="right">8,312</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">70,681</td>
<td align="right">19.4%</td>
<td align="right">70,681</td>
<td align="right">19.4%</td>
<td align="right">0.0%</td>
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
<td align="left"><= 8,192</td>
<td align="left">43</td>
<td align="right">97.7%</td>
<td align="left">43</td>
<td align="right">97.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">1</td>
<td align="right">2.3%</td>
<td align="left">1</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
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
<td align="left"><= 32</td>
<td align="right">22</td>
<td align="right">50.0%</td>
<td align="right">22</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22</td>
<td align="right">50.0%</td>
<td align="right">22</td>
<td align="right">50.0%</td>
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
<td align="left"><= 32</td>
<td align="right">43</td>
<td align="right">97.7%</td>
<td align="right">43</td>
<td align="right">97.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1</td>
<td align="right">2.3%</td>
<td align="right">1</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
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
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">90,357</td>
<td align="right">2,709</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">90,357</td>
<td align="right">2,709</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,893</td>
<td align="right">735</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">2,893</td>
<td align="right">735</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">2,893</td>
<td align="right">735</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,893</td>
<td align="right">735</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,893</td>
<td align="right">735</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,893</td>
<td align="right">735</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,893</td>
<td align="right">735</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,893</td>
<td align="right">735</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">2,893</td>
<td align="right">735</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,893</td>
<td align="right">735</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,893</td>
<td align="right">735</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">1,531,605</td>
<td align="right">684,788</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">1,531,605</td>
<td align="right">684,788</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,004,227</td>
<td align="right">461,195</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,759,986</td>
<td align="right">1,799,596</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">2,311,123</td>
<td align="right">1,135,745</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,405,070</td>
<td align="right">1,684,994</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">795,949</td>
<td align="right">397,631</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">778,399</td>
<td align="right">389,547</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">778,399</td>
<td align="right">389,547</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,568,562</td>
<td align="right">785,708</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">775,506</td>
<td align="right">388,812</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">775,506</td>
<td align="right">388,812</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">790,163</td>
<td align="right">396,161</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">790,163</td>
<td align="right">396,161</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">790,163</td>
<td align="right">396,161</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,452,672</td>
<td align="right">1,731,118</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,659,616</td>
<td align="right">1,334,222</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,659,616</td>
<td align="right">1,334,222</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">1,884,110</td>
<td align="right">945,410</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">1,093,947</td>
<td align="right">549,249</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,093,947</td>
<td align="right">549,249</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">7,883,078</td>
<td align="right">4,050,438</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">6,362,688</td>
<td align="right">3,311,424</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,687,691</td>
<td align="right">906,995</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">779,518</td>
<td align="right">450,957</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">122,592</td>
<td align="right">122,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">122,592</td>
<td align="right">122,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">122,022</td>
<td align="right">122,022</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">122,022</td>
<td align="right">122,022</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">122,022</td>
<td align="right">122,022</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">122,022</td>
<td align="right">122,022</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">122,022</td>
<td align="right">122,022</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-03-28
