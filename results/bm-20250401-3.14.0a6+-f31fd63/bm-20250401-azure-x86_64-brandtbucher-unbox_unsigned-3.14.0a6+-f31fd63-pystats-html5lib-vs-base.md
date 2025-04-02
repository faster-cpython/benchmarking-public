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
<td align="right">573</td>
<td align="right">2,032</td>
<td align="right">254.6%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20</td>
<td align="right">60</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,131</td>
<td align="right">3,346</td>
<td align="right">195.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">250</td>
<td align="right">126</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">12,213</td>
<td align="right">6,159</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">9,316</td>
<td align="right">4,728</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,889</td>
<td align="right">959</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">377,929</td>
<td align="right">191,870</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,905,153</td>
<td align="right">1,982,851</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,157</td>
<td align="right">2,111</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,312,499</td>
<td align="right">1,174,551</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,139,351</td>
<td align="right">3,118,339</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2,741,879</td>
<td align="right">1,392,697</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,089,521</td>
<td align="right">553,407</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">702,072</td>
<td align="right">356,608</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">126</td>
<td align="right">64</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,867,578</td>
<td align="right">1,964,488</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,089,400</td>
<td align="right">553,348</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">702,076</td>
<td align="right">356,612</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">351,038</td>
<td align="right">178,306</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">393,249</td>
<td align="right">199,747</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,092,685</td>
<td align="right">555,021</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,161,021</td>
<td align="right">1,605,648</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,482,898</td>
<td align="right">1,769,156</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,673,473</td>
<td align="right">850,050</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,198,563</td>
<td align="right">608,819</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">599,409</td>
<td align="right">304,475</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">16,575,424</td>
<td align="right">8,419,633</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">5,995,740</td>
<td align="right">3,045,594</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">15,774,428</td>
<td align="right">8,012,794</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,259,304</td>
<td align="right">1,147,644</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">705,893</td>
<td align="right">358,569</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">14,694,402</td>
<td align="right">7,464,251</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,188,380</td>
<td align="right">1,111,626</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">87,075,094</td>
<td align="right">44,231,354</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,606,106</td>
<td align="right">815,853</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,394,179</td>
<td align="right">1,724,147</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">500,130</td>
<td align="right">254,052</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,383,783</td>
<td align="right">5,274,711</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">13,730,282</td>
<td align="right">6,974,699</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,833,720</td>
<td align="right">3,471,398</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">355,437</td>
<td align="right">180,556</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,926,268</td>
<td align="right">1,486,504</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,705,448</td>
<td align="right">866,381</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,389,550</td>
<td align="right">5,278,020</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">352,646</td>
<td align="right">179,149</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">54,305,460</td>
<td align="right">27,588,472</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,920,461</td>
<td align="right">1,483,673</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">23,684,114</td>
<td align="right">12,032,200</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">140,014</td>
<td align="right">71,132</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">729,310</td>
<td align="right">370,516</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,947,561</td>
<td align="right">11,658,202</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">7,491,081</td>
<td align="right">3,805,778</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,578,287</td>
<td align="right">3,342,072</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,464,985</td>
<td align="right">6,840,843</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,835,803</td>
<td align="right">932,684</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,563,806</td>
<td align="right">794,510</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">51,441,134</td>
<td align="right">26,135,398</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">179,461,615</td>
<td align="right">91,178,122</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,780,352</td>
<td align="right">904,540</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">353,150</td>
<td align="right">179,425</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,590,319</td>
<td align="right">808,001</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">11,418,269</td>
<td align="right">5,801,676</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">353,183</td>
<td align="right">179,458</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,320,505</td>
<td align="right">3,719,850</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,657,751</td>
<td align="right">3,383,099</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,164,219</td>
<td align="right">6,181,289</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,103,207</td>
<td align="right">7,166,643</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,427,506</td>
<td align="right">2,758,034</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,373,247</td>
<td align="right">1,206,034</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,781,172</td>
<td align="right">905,175</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">5,574,360</td>
<td align="right">2,833,030</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">402,705</td>
<td align="right">204,677</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,841,363</td>
<td align="right">3,477,181</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">396,249</td>
<td align="right">201,404</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,239,116</td>
<td align="right">629,840</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,168,450</td>
<td align="right">3,135,910</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">956,006</td>
<td align="right">486,046</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">354,435</td>
<td align="right">180,212</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,392,440</td>
<td align="right">1,216,538</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,164,783</td>
<td align="right">592,401</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,157,476</td>
<td align="right">588,688</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">6,183</td>
<td align="right">3,145</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,719,662</td>
<td align="right">874,724</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">705,883</td>
<td align="right">359,055</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,676,281</td>
<td align="right">852,734</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,214,650</td>
<td align="right">617,900</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">903,447</td>
<td align="right">459,775</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">736,282</td>
<td align="right">374,759</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">738,571</td>
<td align="right">375,932</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">415,796</td>
<td align="right">211,692</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,091,103</td>
<td align="right">2,592,153</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,752,492</td>
<td align="right">892,489</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">43,812,230</td>
<td align="right">22,320,788</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,133,876</td>
<td align="right">577,784</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,915</td>
<td align="right">1,489</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">10,902</td>
<td align="right">5,570</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">12,173</td>
<td align="right">6,221</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">696,945</td>
<td align="right">356,434</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">127</td>
<td align="right">65</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,203,837</td>
<td align="right">6,770,278</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,018</td>
<td align="right">522</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">7,911</td>
<td align="right">4,067</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">10,040,199</td>
<td align="right">5,162,350</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,882,355</td>
<td align="right">4,576,143</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">129</td>
<td align="right">67</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">129</td>
<td align="right">67</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">129</td>
<td align="right">67</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">390</td>
<td align="right">204</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">130</td>
<td align="right">68</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">42</td>
<td align="right">62</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">6,685</td>
<td align="right">3,523</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,541</td>
<td align="right">17,892</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,083</td>
<td align="right">586</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,563</td>
<td align="right">1,951</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,361</td>
<td align="right">2,943</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">139</td>
<td align="right">77</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">279</td>
<td align="right">155</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">140</td>
<td align="right">78</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">166</td>
<td align="right">104</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,623</td>
<td align="right">2,755</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">4,594</td>
<td align="right">3,725</td>
<td align="right">-18.9%</td>
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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">127,262</td>
<td align="right">126,212</td>
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
<td align="right">124,278</td>
<td align="right">124,398</td>
<td align="right">0.1%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,165,459</td>
<td align="right">16.4%</td>
<td align="right">3,132,520</td>
<td align="right">16.4%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">31,417,849</td>
<td align="right">83.6%</td>
<td align="right">15,963,002</td>
<td align="right">83.6%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,830</td>
<td align="right">0.0%</td>
<td align="right">1,772</td>
<td align="right">0.0%</td>
<td align="right">-3.2%</td>
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
<td align="right">303</td>
<td align="right">10.0%</td>
<td align="right">1,323</td>
<td align="right">38.7%</td>
<td align="right">336.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,718</td>
<td align="right">90.0%</td>
<td align="right">2,097</td>
<td align="right">61.3%</td>
<td align="right">-22.8%</td>
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
<td align="right">0.8%</td>
<td align="right">43</td>
<td align="right">2.1%</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">240</td>
<td align="right">8.8%</td>
<td align="right">137</td>
<td align="right">6.5%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,717</td>
<td align="right">63.2%</td>
<td align="right">1,310</td>
<td align="right">62.5%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">550</td>
<td align="right">20.2%</td>
<td align="right">423</td>
<td align="right">20.2%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">52</td>
<td align="right">1.9%</td>
<td align="right">50</td>
<td align="right">2.4%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">73</td>
<td align="right">2.7%</td>
<td align="right">71</td>
<td align="right">3.4%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48</td>
<td align="right">1.8%</td>
<td align="right">48</td>
<td align="right">2.3%</td>
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
<td align="right">0.1%</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">4</td>
<td align="right">0.1%</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">1,214,650</td>
<td align="right">100.0%</td>
<td align="right">617,900</td>
<td align="right">100.0%</td>
<td align="right">-49.1%</td>
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
<td align="right">29,077,806</td>
<td align="right">83.5%</td>
<td align="right">14,770,936</td>
<td align="right">83.5%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,739,909</td>
<td align="right">16.5%</td>
<td align="right">2,918,147</td>
<td align="right">16.5%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,632,111</td>
<td align="right">16.2%</td>
<td align="right">2,863,623</td>
<td align="right">16.2%</td>
<td align="right">-49.2%</td>
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
<td align="right">108,929</td>
<td align="right">100.0%</td>
<td align="right">57,870</td>
<td align="right">100.0%</td>
<td align="right">-46.9%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">26,097,698</td>
<td align="right">91.6%</td>
<td align="right">13,256,384</td>
<td align="right">91.5%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,390,776</td>
<td align="right">8.4%</td>
<td align="right">1,214,938</td>
<td align="right">8.4%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,975</td>
<td align="right">0.1%</td>
<td align="right">9,545</td>
<td align="right">0.1%</td>
<td align="right">-36.3%</td>
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
<td align="right">420</td>
<td align="right">21.7%</td>
<td align="right">637</td>
<td align="right">36.0%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,518</td>
<td align="right">78.3%</td>
<td align="right">1,134</td>
<td align="right">64.0%</td>
<td align="right">-25.3%</td>
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
<td align="right">373</td>
<td align="right">24.6%</td>
<td align="right">207</td>
<td align="right">18.3%</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">92</td>
<td align="right">6.1%</td>
<td align="right">70</td>
<td align="right">6.2%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">199</td>
<td align="right">13.1%</td>
<td align="right">154</td>
<td align="right">13.6%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">673</td>
<td align="right">44.3%</td>
<td align="right">524</td>
<td align="right">46.2%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">175</td>
<td align="right">11.5%</td>
<td align="right">173</td>
<td align="right">15.3%</td>
<td align="right">-1.1%</td>
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
<td align="right">6,701,623</td>
<td align="right">88.1%</td>
<td align="right">3,404,649</td>
<td align="right">88.1%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">902,585</td>
<td align="right">11.9%</td>
<td align="right">458,789</td>
<td align="right">11.9%</td>
<td align="right">-49.2%</td>
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
<td align="right">816</td>
<td align="right">94.7%</td>
<td align="right">740</td>
<td align="right">75.1%</td>
<td align="right">-9.3%</td>
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
<td align="right">267</td>
<td align="right">32.7%</td>
<td align="right">225</td>
<td align="right">30.4%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">479</td>
<td align="right">58.7%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,835,172</td>
<td align="right">43.5%</td>
<td align="right">932,264</td>
<td align="right">42.3%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,379,577</td>
<td align="right">56.4%</td>
<td align="right">1,271,207</td>
<td align="right">57.7%</td>
<td align="right">-46.6%</td>
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
<td align="right">613</td>
<td align="right">97.0%</td>
<td align="right">403</td>
<td align="right">95.7%</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">19</td>
<td align="right">3.0%</td>
<td align="right">18</td>
<td align="right">4.3%</td>
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
<td align="right">3.8%</td>
<td align="right">43</td>
<td align="right">10.7%</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">375</td>
<td align="right">61.2%</td>
<td align="right">209</td>
<td align="right">51.9%</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">204</td>
<td align="right">33.3%</td>
<td align="right">140</td>
<td align="right">34.7%</td>
<td align="right">-31.4%</td>
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
<td align="left">seq iter</td>
<td align="right">2</td>
<td align="right">0.3%</td>
<td align="right">2</td>
<td align="right">0.5%</td>
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
<td align="right">18,838</td>
<td align="right">0.0%</td>
<td align="right">7,840</td>
<td align="right">0.0%</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">118,342,211</td>
<td align="right">95.9%</td>
<td align="right">60,116,142</td>
<td align="right">95.9%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,086,321</td>
<td align="right">4.1%</td>
<td align="right">2,584,124</td>
<td align="right">4.1%</td>
<td align="right">-49.2%</td>
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
<td align="right">25.1%</td>
<td align="right">5,165</td>
<td align="right">65.3%</td>
<td align="right">332.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,569</td>
<td align="right">74.9%</td>
<td align="right">2,741</td>
<td align="right">34.7%</td>
<td align="right">-23.2%</td>
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
<td align="right">2,375</td>
<td align="right">66.5%</td>
<td align="right">1,810</td>
<td align="right">66.0%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">183</td>
<td align="right">5.1%</td>
<td align="right">140</td>
<td align="right">5.1%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">266</td>
<td align="right">7.5%</td>
<td align="right">241</td>
<td align="right">8.8%</td>
<td align="right">-9.4%</td>
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
<td align="right">1,134</td>
<td align="right">0.0%</td>
<td align="right">576</td>
<td align="right">0.0%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">20,759,824</td>
<td align="right">100.0%</td>
<td align="right">10,549,166</td>
<td align="right">100.0%</td>
<td align="right">-49.2%</td>
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
<td align="right">329</td>
<td align="right">100.0%</td>
<td align="right">1,789</td>
<td align="right">100.0%</td>
<td align="right">443.8%</td>
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
<td align="right">379</td>
<td align="right">98.4%</td>
<td align="right">193</td>
<td align="right">74.5%</td>
<td align="right">-49.1%</td>
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
<td align="right">1,132,962</td>
<td align="right">7.8%</td>
<td align="right">575,582</td>
<td align="right">7.8%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,462,711</td>
<td align="right">92.1%</td>
<td align="right">6,839,539</td>
<td align="right">92.1%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,487</td>
<td align="right">0.1%</td>
<td align="right">7,463</td>
<td align="right">0.1%</td>
<td align="right">-48.5%</td>
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
<td align="right">36.8%</td>
<td align="right">1,666</td>
<td align="right">72.7%</td>
<td align="right">287.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">738</td>
<td align="right">63.2%</td>
<td align="right">626</td>
<td align="right">27.3%</td>
<td align="right">-15.2%</td>
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
<td align="right">226</td>
<td align="right">30.6%</td>
<td align="right">180</td>
<td align="right">28.8%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">312</td>
<td align="right">42.3%</td>
<td align="right">249</td>
<td align="right">39.8%</td>
<td align="right">-20.2%</td>
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
<td align="right">178</td>
<td align="right">24.1%</td>
<td align="right">176</td>
<td align="right">28.1%</td>
<td align="right">-1.1%</td>
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
<td align="right">2,965,197</td>
<td align="right">96.0%</td>
<td align="right">1,506,213</td>
<td align="right">92.4%</td>
<td align="right">-49.2%</td>
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
<td align="right">38.3%</td>
<td align="right">143</td>
<td align="right">79.4%</td>
<td align="right">521.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">37</td>
<td align="right">61.7%</td>
<td align="right">37</td>
<td align="right">20.6%</td>
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
<td align="right">36</td>
<td align="right">97.3%</td>
<td align="right">36</td>
<td align="right">97.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">2.7%</td>
<td align="right">1</td>
<td align="right">2.7%</td>
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
<td align="right">7,488,889</td>
<td align="right">25.9%</td>
<td align="right">3,803,980</td>
<td align="right">25.9%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">21,326,554</td>
<td align="right">73.9%</td>
<td align="right">10,834,028</td>
<td align="right">73.9%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,123</td>
<td align="right">0.2%</td>
<td align="right">26,760</td>
<td align="right">0.2%</td>
<td align="right">-48.7%</td>
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
<td align="right">2,086</td>
<td align="right">66.0%</td>
<td align="right">1,172</td>
<td align="right">50.7%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,074</td>
<td align="right">34.0%</td>
<td align="right">1,138</td>
<td align="right">49.3%</td>
<td align="right">6.0%</td>
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
<td align="right">157</td>
<td align="right">7.5%</td>
<td align="right">74</td>
<td align="right">6.3%</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,606</td>
<td align="right">77.0%</td>
<td align="right">841</td>
<td align="right">71.8%</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">228</td>
<td align="right">10.9%</td>
<td align="right">164</td>
<td align="right">14.0%</td>
<td align="right">-28.1%</td>
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
<td align="right">70</td>
<td align="right">3.4%</td>
<td align="right">69</td>
<td align="right">5.9%</td>
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
<td align="right">740,472</td>
<td align="right">100.0%</td>
<td align="right">376,903</td>
<td align="right">100.0%</td>
<td align="right">-49.1%</td>
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
<td align="right">363,807,989</td>
<td align="right">46.4%</td>
<td align="right">184,945,729</td>
<td align="right">46.4%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">387,962,549</td>
<td align="right">49.5%</td>
<td align="right">197,304,707</td>
<td align="right">49.5%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">5,843,495</td>
<td align="right">0.7%</td>
<td align="right">2,972,257</td>
<td align="right">0.7%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">26,356,900</td>
<td align="right">3.4%</td>
<td align="right">13,468,486</td>
<td align="right">3.4%</td>
<td align="right">-48.9%</td>
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
<td align="right">7,488,889</td>
<td align="right">23.4%</td>
<td align="right">3,803,980</td>
<td align="right">23.3%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,835,172</td>
<td align="right">5.7%</td>
<td align="right">932,264</td>
<td align="right">5.7%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,132,962</td>
<td align="right">3.5%</td>
<td align="right">575,582</td>
<td align="right">3.5%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,086,321</td>
<td align="right">15.9%</td>
<td align="right">2,584,124</td>
<td align="right">15.8%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,165,459</td>
<td align="right">19.3%</td>
<td align="right">3,132,520</td>
<td align="right">19.2%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,390,776</td>
<td align="right">7.5%</td>
<td align="right">1,214,938</td>
<td align="right">7.4%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">902,585</td>
<td align="right">2.8%</td>
<td align="right">458,789</td>
<td align="right">2.8%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,632,111</td>
<td align="right">17.6%</td>
<td align="right">2,863,623</td>
<td align="right">17.6%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,214,650</td>
<td align="right">3.8%</td>
<td align="right">617,900</td>
<td align="right">3.8%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">124,218</td>
<td align="right">0.4%</td>
<td align="right">124,218</td>
<td align="right">0.8%</td>
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
<td align="right">6,300</td>
<td align="right">0.1%</td>
<td align="right">2,238</td>
<td align="right">0.1%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,738</td>
<td align="right">0.2%</td>
<td align="right">4,608</td>
<td align="right">0.2%</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,018</td>
<td align="right">0.4%</td>
<td align="right">12,987</td>
<td align="right">0.4%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">11,164</td>
<td align="right">0.2%</td>
<td align="right">5,628</td>
<td align="right">0.2%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">14,975</td>
<td align="right">0.3%</td>
<td align="right">7,578</td>
<td align="right">0.3%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,207</td>
<td align="right">0.1%</td>
<td align="right">4,156</td>
<td align="right">0.1%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">271,234</td>
<td align="right">4.6%</td>
<td align="right">137,770</td>
<td align="right">4.6%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,729,928</td>
<td align="right">46.7%</td>
<td align="right">1,387,728</td>
<td align="right">46.7%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,727,726</td>
<td align="right">46.7%</td>
<td align="right">1,387,063</td>
<td align="right">46.7%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">25,605</td>
<td align="right">0.4%</td>
<td align="right">13,521</td>
<td align="right">0.5%</td>
<td align="right">-47.2%</td>
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
<td align="right">352,474</td>
<td align="right">1.5%</td>
<td align="right">179,060</td>
<td align="right">1.5%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">23,288,131</td>
<td align="right">98.3%</td>
<td align="right">11,831,001</td>
<td align="right">98.3%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">22,947,578</td>
<td align="right">96.9%</td>
<td align="right">11,658,219</td>
<td align="right">96.9%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">396,288</td>
<td align="right">1.7%</td>
<td align="right">201,442</td>
<td align="right">1.7%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">396,322</td>
<td align="right">1.7%</td>
<td align="right">201,476</td>
<td align="right">1.7%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">396,331</td>
<td align="right">1.7%</td>
<td align="right">201,485</td>
<td align="right">1.7%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">396,331</td>
<td align="right">1.7%</td>
<td align="right">201,485</td>
<td align="right">1.7%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">14,618</td>
<td align="right">0.1%</td>
<td align="right">7,488</td>
<td align="right">0.1%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">256</td>
<td align="right">0.0%</td>
<td align="right">132</td>
<td align="right">0.0%</td>
<td align="right">-48.4%</td>
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
<td align="right">590</td>
<td align="right"></td>
<td align="right">952</td>
<td align="right"></td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,289,728</td>
<td align="right"></td>
<td align="right">4,887,657</td>
<td align="right"></td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,233,057</td>
<td align="right">0.9%</td>
<td align="right">2,051,849</td>
<td align="right">0.8%</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">49,233,003</td>
<td align="right">10.0%</td>
<td align="right">24,541,353</td>
<td align="right">9.8%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">66,024,996</td>
<td align="right">13.4%</td>
<td align="right">33,500,806</td>
<td align="right">13.4%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">337,045,532</td>
<td align="right">70.8%</td>
<td align="right">171,231,582</td>
<td align="right">70.8%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">365,636</td>
<td align="right"></td>
<td align="right">185,774</td>
<td align="right"></td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">373,417,474</td>
<td align="right">75.9%</td>
<td align="right">189,758,207</td>
<td align="right">76.0%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">218,228</td>
<td align="right">0.7%</td>
<td align="right">110,906</td>
<td align="right">0.7%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">61,632,448</td>
<td align="right">12.9%</td>
<td align="right">31,336,081</td>
<td align="right">13.0%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">73,451,037</td>
<td align="right">15.4%</td>
<td align="right">37,345,573</td>
<td align="right">15.4%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">1,784,061</td>
<td align="right"></td>
<td align="right">907,297</td>
<td align="right"></td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,095,885</td>
<td align="right"></td>
<td align="right">3,609,146</td>
<td align="right"></td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">3,519,536</td>
<td align="right">0.7%</td>
<td align="right">1,791,035</td>
<td align="right">0.7%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">21,297,000</td>
<td align="right"></td>
<td align="right">10,847,541</td>
<td align="right"></td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,846</td>
<td align="right">0.0%</td>
<td align="right">4,506</td>
<td align="right">0.0%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">21,300,530</td>
<td align="right">64.6%</td>
<td align="right">10,851,094</td>
<td align="right">64.6%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,662,620</td>
<td align="right">35.4%</td>
<td align="right">5,951,239</td>
<td align="right">35.4%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,435,546</td>
<td align="right">34.7%</td>
<td align="right">5,835,827</td>
<td align="right">34.7%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">6,657</td>
<td align="right"></td>
<td align="right">4,594</td>
<td align="right"></td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">7,124</td>
<td align="right"></td>
<td align="right">5,350</td>
<td align="right"></td>
<td align="right">-24.9%</td>
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
<td align="right">1,050</td>
<td align="right">296,258</td>
<td align="right">19,178,751</td>
<td align="right">1,391,019</td>
<td align="right">1,654,005</td>
<td align="right">534</td>
<td align="right">229</td>
<td align="right">9,041,242</td>
<td align="right">888,565</td>
<td align="right">589,868</td>
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
Stats gathered on: 2025-04-02
