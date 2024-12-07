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
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">254</td>
<td align="right">126</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">12,407</td>
<td align="right">6,159</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">9,464</td>
<td align="right">4,728</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">383,946</td>
<td align="right">191,870</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,919</td>
<td align="right">959</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,967,135</td>
<td align="right">1,982,851</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,223</td>
<td align="right">2,111</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,349,207</td>
<td align="right">1,174,551</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,236,801</td>
<td align="right">3,118,339</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2,785,401</td>
<td align="right">1,392,697</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,106,815</td>
<td align="right">553,407</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">713,216</td>
<td align="right">356,608</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">128</td>
<td align="right">64</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,928,968</td>
<td align="right">1,964,488</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,106,692</td>
<td align="right">553,348</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">713,220</td>
<td align="right">356,612</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">356,610</td>
<td align="right">178,306</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">399,491</td>
<td align="right">199,747</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,110,029</td>
<td align="right">555,021</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,211,195</td>
<td align="right">1,605,648</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,538,180</td>
<td align="right">1,769,156</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,700,035</td>
<td align="right">850,050</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,217,587</td>
<td align="right">608,819</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">16,838,514</td>
<td align="right">8,419,633</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">6,090,906</td>
<td align="right">3,045,594</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">16,024,802</td>
<td align="right">8,012,794</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">14,927,634</td>
<td align="right">7,464,209</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,295,164</td>
<td align="right">1,147,644</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">717,097</td>
<td align="right">358,569</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,223,110</td>
<td align="right">1,111,622</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">88,457,150</td>
<td align="right">44,231,354</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">508,065</td>
<td align="right">254,049</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,631,598</td>
<td align="right">815,853</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,448,051</td>
<td align="right">1,724,147</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,548,585</td>
<td align="right">5,274,707</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">13,948,202</td>
<td align="right">6,974,697</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,942,182</td>
<td align="right">3,471,398</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,972,712</td>
<td align="right">1,486,504</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,732,510</td>
<td align="right">866,377</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,554,438</td>
<td align="right">5,278,020</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">358,072</td>
<td align="right">179,064</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">358,072</td>
<td align="right">179,064</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,966,809</td>
<td align="right">1,483,673</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">24,059,982</td>
<td align="right">12,032,200</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">52,874,125</td>
<td align="right">26,442,243</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">142,236</td>
<td align="right">71,132</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">740,883</td>
<td align="right">370,515</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">23,311,563</td>
<td align="right">11,658,117</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">7,609,966</td>
<td align="right">3,805,765</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,682,681</td>
<td align="right">3,342,072</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,678,667</td>
<td align="right">6,840,843</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,588,622</td>
<td align="right">794,510</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">52,257,448</td>
<td align="right">26,135,398</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">182,309,459</td>
<td align="right">91,178,112</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,808,604</td>
<td align="right">904,540</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">358,754</td>
<td align="right">179,425</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,865,005</td>
<td align="right">932,754</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,615,555</td>
<td align="right">808,001</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">11,599,444</td>
<td align="right">5,801,675</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">358,787</td>
<td align="right">179,458</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,436,783</td>
<td align="right">3,719,914</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,763,381</td>
<td align="right">3,383,095</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,357,244</td>
<td align="right">6,181,289</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,326,965</td>
<td align="right">7,166,641</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">5,513,618</td>
<td align="right">2,758,034</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,410,899</td>
<td align="right">1,206,034</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,809,430</td>
<td align="right">905,175</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">5,662,790</td>
<td align="right">2,833,030</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">402,693</td>
<td align="right">201,477</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">409,106</td>
<td align="right">204,690</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">5,572,580</td>
<td align="right">2,788,227</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,101,842</td>
<td align="right">1,051,664</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,150,960</td>
<td align="right">3,077,680</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">360,053</td>
<td align="right">180,210</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,430,393</td>
<td align="right">1,216,540</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,175,753</td>
<td align="right">588,617</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,183,245</td>
<td align="right">592,399</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">6,281</td>
<td align="right">3,145</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,746,918</td>
<td align="right">874,724</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">717,073</td>
<td align="right">359,057</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,702,847</td>
<td align="right">852,734</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,000,288</td>
<td align="right">501,088</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">917,766</td>
<td align="right">459,774</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">747,944</td>
<td align="right">374,759</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">750,269</td>
<td align="right">375,932</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">934,339</td>
<td align="right">468,173</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">422,380</td>
<td align="right">211,692</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,171,860</td>
<td align="right">2,592,157</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,780,240</td>
<td align="right">892,495</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">44,505,496</td>
<td align="right">22,320,782</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,151,864</td>
<td align="right">577,784</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,961</td>
<td align="right">1,489</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">11,074</td>
<td align="right">5,570</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">707,864</td>
<td align="right">356,370</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">12,377</td>
<td align="right">6,233</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">129</td>
<td align="right">65</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,411,371</td>
<td align="right">6,770,278</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,034</td>
<td align="right">522</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">8,035</td>
<td align="right">4,067</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">10,197,549</td>
<td align="right">5,162,350</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">9,021,265</td>
<td align="right">4,576,143</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">131</td>
<td align="right">67</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">131</td>
<td align="right">67</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">396</td>
<td align="right">204</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">132</td>
<td align="right">68</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">132</td>
<td align="right">68</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">42</td>
<td align="right">62</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">34,030</td>
<td align="right">17,892</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,099</td>
<td align="right">586</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,615</td>
<td align="right">1,951</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,439</td>
<td align="right">2,943</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">141</td>
<td align="right">77</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">283</td>
<td align="right">155</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">142</td>
<td align="right">78</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">168</td>
<td align="right">104</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,651</td>
<td align="right">2,755</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">4,622</td>
<td align="right">3,725</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,122</td>
<td align="right">4,861</td>
<td align="right">17.9%</td>
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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">127,296</td>
<td align="right">126,212</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">124,277</td>
<td align="right">124,397</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">984</td>
<td align="right">984</td>
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
<td align="right">8,874,279</td>
<td align="right">90.5%</td>
<td align="right">4,439,463</td>
<td align="right">90.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">933,799</td>
<td align="right">9.5%</td>
<td align="right">467,686</td>
<td align="right">9.5%</td>
<td align="right">-49.9%</td>
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
<td align="right">69</td>
<td align="right">12.8%</td>
<td align="right">128</td>
<td align="right">26.3%</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">471</td>
<td align="right">87.2%</td>
<td align="right">359</td>
<td align="right">73.7%</td>
<td align="right">-23.8%</td>
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
<td align="right">24</td>
<td align="right">5.1%</td>
<td align="right">44</td>
<td align="right">12.3%</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">244</td>
<td align="right">51.8%</td>
<td align="right">137</td>
<td align="right">38.2%</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">93</td>
<td align="right">19.7%</td>
<td align="right">71</td>
<td align="right">19.8%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">52</td>
<td align="right">11.0%</td>
<td align="right">50</td>
<td align="right">13.9%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48</td>
<td align="right">10.2%</td>
<td align="right">47</td>
<td align="right">13.1%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">4</td>
<td align="right">0.8%</td>
<td align="right">4</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">4</td>
<td align="right">0.8%</td>
<td align="right">4</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.6%</td>
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
<td align="right">1,000,288</td>
<td align="right">100.0%</td>
<td align="right">501,088</td>
<td align="right">100.0%</td>
<td align="right">-49.9%</td>
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
<td align="right">5,569,885</td>
<td align="right">20.0%</td>
<td align="right">2,785,157</td>
<td align="right">20.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">22,294,469</td>
<td align="right">80.0%</td>
<td align="right">11,149,596</td>
<td align="right">80.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,833</td>
<td align="right">0.0%</td>
<td align="right">1,705</td>
<td align="right">0.0%</td>
<td align="right">-7.0%</td>
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
<td align="right">232</td>
<td align="right">8.5%</td>
<td align="right">1,192</td>
<td align="right">38.5%</td>
<td align="right">413.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,492</td>
<td align="right">91.5%</td>
<td align="right">1,907</td>
<td align="right">61.5%</td>
<td align="right">-23.5%</td>
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
<td align="right">337</td>
<td align="right">13.5%</td>
<td align="right">228</td>
<td align="right">12.0%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,735</td>
<td align="right">69.6%</td>
<td align="right">1,310</td>
<td align="right">68.7%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">192</td>
<td align="right">7.7%</td>
<td align="right">167</td>
<td align="right">8.8%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">221</td>
<td align="right">8.9%</td>
<td align="right">195</td>
<td align="right">10.2%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">6</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">29,539,094</td>
<td align="right">83.5%</td>
<td align="right">14,770,843</td>
<td align="right">83.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,828,114</td>
<td align="right">16.5%</td>
<td align="right">2,916,739</td>
<td align="right">16.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,440</td>
<td align="right">0.0%</td>
<td align="right">1,964</td>
<td align="right">0.0%</td>
<td align="right">-42.9%</td>
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
<td align="right">110,595</td>
<td align="right">100.0%</td>
<td align="right">57,897</td>
<td align="right">99.9%</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">45</td>
<td align="right">0.1%</td>
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
<td align="left">out of versions</td>
<td align="right">46</td>
<td align="right">100.0%</td>
<td align="right">45</td>
<td align="right">100.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">46</td>
<td align="right">100.0%</td>
<td align="right">45</td>
<td align="right">100.0%</td>
<td align="right">-2.2%</td>
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
<td align="right">15,214</td>
<td align="right">0.1%</td>
<td align="right">7,579</td>
<td align="right">0.1%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">26,511,866</td>
<td align="right">91.6%</td>
<td align="right">13,258,307</td>
<td align="right">91.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,428,711</td>
<td align="right">8.4%</td>
<td align="right">1,214,939</td>
<td align="right">8.4%</td>
<td align="right">-50.0%</td>
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
<td align="right">425</td>
<td align="right">21.7%</td>
<td align="right">596</td>
<td align="right">34.5%</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,535</td>
<td align="right">78.3%</td>
<td align="right">1,134</td>
<td align="right">65.5%</td>
<td align="right">-26.1%</td>
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
<td align="right">378</td>
<td align="right">24.6%</td>
<td align="right">207</td>
<td align="right">18.3%</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">92</td>
<td align="right">6.0%</td>
<td align="right">70</td>
<td align="right">6.2%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">682</td>
<td align="right">44.4%</td>
<td align="right">524</td>
<td align="right">46.2%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">200</td>
<td align="right">13.0%</td>
<td align="right">154</td>
<td align="right">13.6%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">177</td>
<td align="right">11.5%</td>
<td align="right">173</td>
<td align="right">15.3%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6</td>
<td align="right">0.4%</td>
<td align="right">6</td>
<td align="right">0.5%</td>
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
<td align="right">6,807,979</td>
<td align="right">88.1%</td>
<td align="right">3,404,651</td>
<td align="right">88.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">916,901</td>
<td align="right">11.9%</td>
<td align="right">458,789</td>
<td align="right">11.9%</td>
<td align="right">-50.0%</td>
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
<td align="right">25.0%</td>
<td align="right">434.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">819</td>
<td align="right">94.7%</td>
<td align="right">739</td>
<td align="right">75.0%</td>
<td align="right">-9.8%</td>
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
<td align="right">271</td>
<td align="right">33.1%</td>
<td align="right">225</td>
<td align="right">30.4%</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">479</td>
<td align="right">58.5%</td>
<td align="right">447</td>
<td align="right">60.5%</td>
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
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,864,368</td>
<td align="right">43.6%</td>
<td align="right">932,334</td>
<td align="right">42.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,415,291</td>
<td align="right">56.4%</td>
<td align="right">1,271,167</td>
<td align="right">57.7%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12</td>
<td align="right">0.0%</td>
<td align="right">12</td>
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
<td align="right">619</td>
<td align="right">97.2%</td>
<td align="right">403</td>
<td align="right">96.0%</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18</td>
<td align="right">2.8%</td>
<td align="right">17</td>
<td align="right">4.0%</td>
<td align="right">-5.6%</td>
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
<td align="right">3.7%</td>
<td align="right">43</td>
<td align="right">10.7%</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">380</td>
<td align="right">61.4%</td>
<td align="right">209</td>
<td align="right">51.9%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">206</td>
<td align="right">33.3%</td>
<td align="right">141</td>
<td align="right">35.0%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">8</td>
<td align="right">1.3%</td>
<td align="right">8</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">19,114</td>
<td align="right">0.0%</td>
<td align="right">7,840</td>
<td align="right">0.0%</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">120,220,539</td>
<td align="right">95.9%</td>
<td align="right">60,116,136</td>
<td align="right">95.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,167,037</td>
<td align="right">4.1%</td>
<td align="right">2,584,124</td>
<td align="right">4.1%</td>
<td align="right">-50.0%</td>
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
<td align="right">1,479</td>
<td align="right">29.1%</td>
<td align="right">5,340</td>
<td align="right">66.1%</td>
<td align="right">261.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,605</td>
<td align="right">70.9%</td>
<td align="right">2,744</td>
<td align="right">33.9%</td>
<td align="right">-23.9%</td>
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
<td align="right">392</td>
<td align="right">10.9%</td>
<td align="right">282</td>
<td align="right">10.3%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,402</td>
<td align="right">66.6%</td>
<td align="right">1,813</td>
<td align="right">66.1%</td>
<td align="right">-24.5%</td>
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
<td align="right">1,152</td>
<td align="right">0.0%</td>
<td align="right">576</td>
<td align="right">0.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">21,089,194</td>
<td align="right">100.0%</td>
<td align="right">10,549,160</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
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
<td align="right">385</td>
<td align="right">98.5%</td>
<td align="right">193</td>
<td align="right">74.5%</td>
<td align="right">-49.9%</td>
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
<td align="right">1,150,942</td>
<td align="right">7.8%</td>
<td align="right">575,582</td>
<td align="right">7.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,676,359</td>
<td align="right">92.1%</td>
<td align="right">6,839,539</td>
<td align="right">92.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,715</td>
<td align="right">0.1%</td>
<td align="right">7,463</td>
<td align="right">0.1%</td>
<td align="right">-49.3%</td>
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
<td align="right">434</td>
<td align="right">36.8%</td>
<td align="right">1,666</td>
<td align="right">72.7%</td>
<td align="right">283.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">746</td>
<td align="right">63.2%</td>
<td align="right">626</td>
<td align="right">27.3%</td>
<td align="right">-16.1%</td>
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
<td align="right">317</td>
<td align="right">42.5%</td>
<td align="right">249</td>
<td align="right">39.8%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">227</td>
<td align="right">30.4%</td>
<td align="right">180</td>
<td align="right">28.8%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">22</td>
<td align="right">2.9%</td>
<td align="right">21</td>
<td align="right">3.4%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">180</td>
<td align="right">24.1%</td>
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
<td align="right">3,012,261</td>
<td align="right">96.0%</td>
<td align="right">1,506,213</td>
<td align="right">92.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">124,218</td>
<td align="right">4.0%</td>
<td align="right">124,218</td>
<td align="right">7.6%</td>
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
<td align="right">39.0%</td>
<td align="right">143</td>
<td align="right">79.9%</td>
<td align="right">521.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">36</td>
<td align="right">61.0%</td>
<td align="right">36</td>
<td align="right">20.1%</td>
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
<td align="right">35</td>
<td align="right">97.2%</td>
<td align="right">35</td>
<td align="right">97.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">2.8%</td>
<td align="right">1</td>
<td align="right">2.8%</td>
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
<td align="right">7,607,744</td>
<td align="right">25.9%</td>
<td align="right">3,803,967</td>
<td align="right">25.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">21,665,042</td>
<td align="right">73.9%</td>
<td align="right">10,834,026</td>
<td align="right">73.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,932</td>
<td align="right">0.2%</td>
<td align="right">26,773</td>
<td align="right">0.2%</td>
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
<td align="left">Failure</td>
<td align="right">2,116</td>
<td align="right">66.0%</td>
<td align="right">1,172</td>
<td align="right">50.7%</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,088</td>
<td align="right">34.0%</td>
<td align="right">1,138</td>
<td align="right">49.3%</td>
<td align="right">4.6%</td>
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
<td align="right">159</td>
<td align="right">7.5%</td>
<td align="right">74</td>
<td align="right">6.3%</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,631</td>
<td align="right">77.1%</td>
<td align="right">841</td>
<td align="right">71.8%</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">230</td>
<td align="right">10.9%</td>
<td align="right">164</td>
<td align="right">14.0%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">25</td>
<td align="right">1.2%</td>
<td align="right">24</td>
<td align="right">2.0%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">71</td>
<td align="right">3.4%</td>
<td align="right">69</td>
<td align="right">5.9%</td>
<td align="right">-2.8%</td>
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
<td align="right">752,200</td>
<td align="right">100.0%</td>
<td align="right">376,903</td>
<td align="right">100.0%</td>
<td align="right">-49.9%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">355,821,293</td>
<td align="right">44.9%</td>
<td align="right">178,005,690</td>
<td align="right">44.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">5,933,195</td>
<td align="right">0.7%</td>
<td align="right">2,968,751</td>
<td align="right">0.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">404,031,553</td>
<td align="right">51.0%</td>
<td align="right">202,327,099</td>
<td align="right">51.0%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">26,783,102</td>
<td align="right">3.4%</td>
<td align="right">13,473,740</td>
<td align="right">3.4%</td>
<td align="right">-49.7%</td>
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
<td align="right">7,607,744</td>
<td align="right">28.4%</td>
<td align="right">3,803,967</td>
<td align="right">28.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">5,569,885</td>
<td align="right">20.8%</td>
<td align="right">2,785,157</td>
<td align="right">20.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,864,368</td>
<td align="right">7.0%</td>
<td align="right">932,334</td>
<td align="right">6.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,150,942</td>
<td align="right">4.3%</td>
<td align="right">575,582</td>
<td align="right">4.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,167,037</td>
<td align="right">19.3%</td>
<td align="right">2,584,124</td>
<td align="right">19.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,428,711</td>
<td align="right">9.1%</td>
<td align="right">1,214,939</td>
<td align="right">9.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">916,901</td>
<td align="right">3.4%</td>
<td align="right">458,789</td>
<td align="right">3.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">933,799</td>
<td align="right">3.5%</td>
<td align="right">467,686</td>
<td align="right">3.5%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,000,288</td>
<td align="right">3.7%</td>
<td align="right">501,088</td>
<td align="right">3.7%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">124,218</td>
<td align="right">0.5%</td>
<td align="right">124,218</td>
<td align="right">0.9%</td>
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
<td align="right">6,366</td>
<td align="right">0.1%</td>
<td align="right">2,238</td>
<td align="right">0.1%</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,922</td>
<td align="right">0.2%</td>
<td align="right">4,608</td>
<td align="right">0.2%</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,435</td>
<td align="right">0.4%</td>
<td align="right">12,987</td>
<td align="right">0.4%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">11,344</td>
<td align="right">0.2%</td>
<td align="right">5,628</td>
<td align="right">0.2%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">15,214</td>
<td align="right">0.3%</td>
<td align="right">7,579</td>
<td align="right">0.3%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,337</td>
<td align="right">0.1%</td>
<td align="right">4,156</td>
<td align="right">0.1%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">275,540</td>
<td align="right">4.6%</td>
<td align="right">137,770</td>
<td align="right">4.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,773,222</td>
<td align="right">46.7%</td>
<td align="right">1,387,728</td>
<td align="right">46.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,770,993</td>
<td align="right">46.7%</td>
<td align="right">1,387,063</td>
<td align="right">46.7%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">25,976</td>
<td align="right">0.4%</td>
<td align="right">13,521</td>
<td align="right">0.5%</td>
<td align="right">-47.9%</td>
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
<td align="right">358,068</td>
<td align="right">1.5%</td>
<td align="right">179,060</td>
<td align="right">1.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">23,657,557</td>
<td align="right">98.3%</td>
<td align="right">11,830,928</td>
<td align="right">98.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">23,311,580</td>
<td align="right">96.9%</td>
<td align="right">11,658,134</td>
<td align="right">96.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">402,732</td>
<td align="right">1.7%</td>
<td align="right">201,515</td>
<td align="right">1.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">402,766</td>
<td align="right">1.7%</td>
<td align="right">201,549</td>
<td align="right">1.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">402,775</td>
<td align="right">1.7%</td>
<td align="right">201,558</td>
<td align="right">1.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">402,775</td>
<td align="right">1.7%</td>
<td align="right">201,558</td>
<td align="right">1.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">14,836</td>
<td align="right">0.1%</td>
<td align="right">7,476</td>
<td align="right">0.1%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">132</td>
<td align="right">0.0%</td>
<td align="right">-49.2%</td>
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
<td align="left">Method cache misses</td>
<td align="right">2,615</td>
<td align="right"></td>
<td align="right">8,041</td>
<td align="right"></td>
<td align="right">207.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,926</td>
<td align="right"></td>
<td align="right">8,744</td>
<td align="right"></td>
<td align="right">198.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">419</td>
<td align="right"></td>
<td align="right">913</td>
<td align="right"></td>
<td align="right">117.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">125,942,549</td>
<td align="right">20.3%</td>
<td align="right">1,787,228</td>
<td align="right">0.7%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">57,562,314</td>
<td align="right">10.6%</td>
<td align="right">1,916,022</td>
<td align="right">0.8%</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">21,924,428</td>
<td align="right"></td>
<td align="right">10,692,447</td>
<td align="right"></td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">49,990,397</td>
<td align="right">8.1%</td>
<td align="right">24,540,461</td>
<td align="right">9.9%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">9,307,544</td>
<td align="right"></td>
<td align="right">4,633,152</td>
<td align="right"></td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">9,308,014</td>
<td align="right">28.5%</td>
<td align="right">4,640,806</td>
<td align="right">28.3%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">64,545,993</td>
<td align="right">10.4%</td>
<td align="right">32,246,274</td>
<td align="right">13.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,212,574</td>
<td align="right"></td>
<td align="right">3,605,701</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">371,438</td>
<td align="right"></td>
<td align="right">185,774</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">1,810,244</td>
<td align="right"></td>
<td align="right">905,578</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">221,689</td>
<td align="right">0.7%</td>
<td align="right">110,905</td>
<td align="right">0.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">343,233,143</td>
<td align="right">63.0%</td>
<td align="right">171,780,349</td>
<td align="right">69.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">62,602,554</td>
<td align="right">11.5%</td>
<td align="right">31,335,379</td>
<td align="right">12.7%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">379,337,772</td>
<td align="right">61.2%</td>
<td align="right">189,897,287</td>
<td align="right">76.4%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,985</td>
<td align="right">0.0%</td>
<td align="right">4,505</td>
<td align="right">0.0%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">23,333,711</td>
<td align="right">71.5%</td>
<td align="right">11,751,910</td>
<td align="right">71.7%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">23,103,037</td>
<td align="right">70.8%</td>
<td align="right">11,636,500</td>
<td align="right">71.0%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">81,719,852</td>
<td align="right">15.0%</td>
<td align="right">42,123,204</td>
<td align="right">17.0%</td>
<td align="right">-48.5%</td>
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
<td align="right">1,067</td>
<td align="right">296,258</td>
<td align="right">21,027,588</td>
<td align="right">1,296,030</td>
<td align="right">1,535,042</td>
<td align="right">534</td>
<td align="right">229</td>
<td align="right">6,867,573</td>
<td align="right">293,177</td>
<td align="right">626,919</td>
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
Stats gathered on: 2024-12-07
