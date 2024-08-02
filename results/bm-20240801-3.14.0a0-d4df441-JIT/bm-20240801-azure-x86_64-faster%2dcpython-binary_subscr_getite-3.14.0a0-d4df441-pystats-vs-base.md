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
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">54,282,074</td>
<td align="right">141,599,521</td>
<td align="right">160.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">73,581,733</td>
<td align="right">107,536,120</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">69,169,939</td>
<td align="right">99,894,514</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">327,593,843</td>
<td align="right">195,491,563</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">163,214,352</td>
<td align="right">124,801,746</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">316,440,443</td>
<td align="right">244,699,121</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,226,827</td>
<td align="right">232,239,075</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">698,776,726</td>
<td align="right">547,111,326</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,034,576,229</td>
<td align="right">856,376,167</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,448,658</td>
<td align="right">267,328,204</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,032,373,845</td>
<td align="right">1,740,256,401</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">306,546,317</td>
<td align="right">273,391,905</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">391,660,805</td>
<td align="right">432,531,743</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,141,594,853</td>
<td align="right">2,832,466,638</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">412,688,808</td>
<td align="right">375,841,692</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">33,031,643</td>
<td align="right">35,922,112</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,281,259</td>
<td align="right">9,987,420</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,087,752,916</td>
<td align="right">3,783,834,270</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,871,452,675</td>
<td align="right">3,074,232,093</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">613,833,219</td>
<td align="right">654,966,700</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">50,329,545</td>
<td align="right">47,325,198</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,442,923,773</td>
<td align="right">2,301,593,231</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,531,951,816</td>
<td align="right">2,395,371,293</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">47,201,321</td>
<td align="right">49,547,350</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">39,824,496</td>
<td align="right">41,604,397</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,359,335</td>
<td align="right">2,457,639</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">31,801,622</td>
<td align="right">33,080,298</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,409,097,448</td>
<td align="right">5,198,525,111</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">49,894,723</td>
<td align="right">51,678,525</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">195,491,252</td>
<td align="right">202,014,308</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">668,022,922</td>
<td align="right">646,228,627</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">295,351,084</td>
<td align="right">304,703,046</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">209,663,752</td>
<td align="right">216,135,676</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,438,724,967</td>
<td align="right">16,903,821,579</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">320,710,855</td>
<td align="right">330,201,535</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,074,956</td>
<td align="right">11,369,490</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">781,683,122</td>
<td align="right">761,723,989</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">631,339,175</td>
<td align="right">616,558,506</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,472,793</td>
<td align="right">10,707,970</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">270,445,475</td>
<td align="right">276,446,465</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">121,056,230</td>
<td align="right">118,585,774</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,760,314</td>
<td align="right">3,832,975</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">76,842,021</td>
<td align="right">78,322,713</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">297,886,065</td>
<td align="right">303,411,064</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">50,401,893</td>
<td align="right">51,331,757</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">751,247,365</td>
<td align="right">763,851,981</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">52,118,145</td>
<td align="right">52,977,298</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">698,628,255</td>
<td align="right">709,675,339</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">166,000,025</td>
<td align="right">168,442,547</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">133,093,064</td>
<td align="right">135,002,135</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">127,192,540</td>
<td align="right">128,976,112</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,416,113,438</td>
<td align="right">1,396,801,906</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">225,381,127</td>
<td align="right">228,214,840</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">73,531</td>
<td align="right">72,611</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">298,717,249</td>
<td align="right">302,333,019</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">51,581,207</td>
<td align="right">50,971,884</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,969,638,012</td>
<td align="right">5,028,090,295</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">195,362,829</td>
<td align="right">197,522,114</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">832,817,644</td>
<td align="right">841,596,379</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">399,280,452</td>
<td align="right">403,471,185</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">178,925,084</td>
<td align="right">177,049,142</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">37,500,200</td>
<td align="right">37,860,196</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">105,250,156</td>
<td align="right">106,252,473</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">230,860,837</td>
<td align="right">232,673,677</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">211,054,833</td>
<td align="right">212,631,556</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">156,728,266</td>
<td align="right">157,873,266</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">28,935,479</td>
<td align="right">29,140,153</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">986,768,899</td>
<td align="right">993,702,546</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">910,915,569</td>
<td align="right">917,311,626</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">633,923,077</td>
<td align="right">638,243,421</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">921,660</td>
<td align="right">915,531</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">120,857,170</td>
<td align="right">121,615,745</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,359,722,551</td>
<td align="right">2,345,296,837</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">109,453,928</td>
<td align="right">110,121,800</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">482,023,796</td>
<td align="right">479,139,626</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,506,131</td>
<td align="right">7,549,619</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,680,662,348</td>
<td align="right">4,654,120,781</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,884,599,405</td>
<td align="right">2,900,954,138</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">183,586</td>
<td align="right">182,600</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,020,840,610</td>
<td align="right">4,042,273,661</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">448,618,589</td>
<td align="right">450,941,181</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">837,102,510</td>
<td align="right">841,341,537</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,962,020,062</td>
<td align="right">3,943,207,134</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">167,948,240</td>
<td align="right">168,675,483</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,896,496,957</td>
<td align="right">1,904,693,555</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">124,667,403</td>
<td align="right">125,173,753</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">337,214,210</td>
<td align="right">338,327,816</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,092,320</td>
<td align="right">136,537,450</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,328,406</td>
<td align="right">143,770,752</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,699,565</td>
<td align="right">4,714,045</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,890,764</td>
<td align="right">72,111,596</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">327,600,131</td>
<td align="right">328,597,368</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">20,485,338</td>
<td align="right">20,539,588</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">211,364,757</td>
<td align="right">211,906,972</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">75,252,359</td>
<td align="right">75,440,127</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">151,527,741</td>
<td align="right">151,905,662</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,176,526</td>
<td align="right">92,400,162</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,459,566</td>
<td align="right">94,683,202</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,383,972</td>
<td align="right">92,589,838</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">551,917,061</td>
<td align="right">553,116,209</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,578,837</td>
<td align="right">8,597,271</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">85,854,869</td>
<td align="right">85,676,964</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,016,880</td>
<td align="right">1,018,960</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,417,385</td>
<td align="right">1,419,487</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">55,610,099</td>
<td align="right">55,688,930</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">362,853,760</td>
<td align="right">363,356,861</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">231,922</td>
<td align="right">231,650</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">82,954,366</td>
<td align="right">83,050,409</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,982,402,147</td>
<td align="right">2,985,816,212</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">236,062,674</td>
<td align="right">236,312,703</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">323,955,276</td>
<td align="right">324,288,752</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">206,197,576</td>
<td align="right">206,381,290</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">354,799,175</td>
<td align="right">355,064,609</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">41,506,087</td>
<td align="right">41,475,238</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,073,191,005</td>
<td align="right">1,072,427,864</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">285,739,113</td>
<td align="right">285,926,052</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">50,315,807</td>
<td align="right">50,285,688</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">495,114,435</td>
<td align="right">495,403,339</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">60,214,720</td>
<td align="right">60,182,650</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">147,922,197</td>
<td align="right">147,988,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,801,276</td>
<td align="right">21,792,615</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">355,156,781</td>
<td align="right">355,296,310</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,398,175,012</td>
<td align="right">1,398,717,301</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">22,240,290</td>
<td align="right">22,231,754</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">22,248,636</td>
<td align="right">22,240,100</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">501,740,125</td>
<td align="right">501,922,818</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">39,942,914</td>
<td align="right">39,929,617</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">20,292,007</td>
<td align="right">20,298,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">217,217,227</td>
<td align="right">217,277,994</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">291,913</td>
<td align="right">291,854</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">194,603</td>
<td align="right">194,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">158,583</td>
<td align="right">158,613</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">153,647,748</td>
<td align="right">153,619,252</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,648,406</td>
<td align="right">48,657,356</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">11,411,252</td>
<td align="right">11,413,112</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">138,110</td>
<td align="right">138,090</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">71,753,233</td>
<td align="right">71,743,087</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,943,648</td>
<td align="right">3,943,094</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,837,460</td>
<td align="right">5,836,719</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,955,794</td>
<td align="right">91,946,244</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">145,634,088</td>
<td align="right">145,619,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,074,180,190</td>
<td align="right">1,074,086,213</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">829,313,143</td>
<td align="right">829,384,903</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">403,164,250</td>
<td align="right">403,134,064</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,274,298</td>
<td align="right">35,276,737</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">16,903</td>
<td align="right">16,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">47,905,967</td>
<td align="right">47,908,746</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">210,484,401</td>
<td align="right">210,473,018</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">28,796,928</td>
<td align="right">28,795,782</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,769,973</td>
<td align="right">268,759,477</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,701,288</td>
<td align="right">9,701,658</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,748,161</td>
<td align="right">3,748,287</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">38,984,284</td>
<td align="right">38,983,005</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,531,534</td>
<td align="right">225,524,655</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1,063,430</td>
<td align="right">1,063,409</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,647,160</td>
<td align="right">402,640,110</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,461,637</td>
<td align="right">20,461,295</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,928,180</td>
<td align="right">173,925,624</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">61,110,261</td>
<td align="right">61,109,757</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">15,028,868</td>
<td align="right">15,028,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,901,952</td>
<td align="right">82,902,042</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">47,536,401</td>
<td align="right">47,536,424</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,547,692</td>
<td align="right">82,547,723</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">12,310,940</td>
<td align="right">12,310,940</td>
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
<td align="right">3,465,700</td>
<td align="right">3,465,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">807,420</td>
<td align="right">807,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">640,500</td>
<td align="right">640,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">101,260</td>
<td align="right">101,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">91,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">29,840</td>
<td align="right">29,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,420</td>
<td align="right">21,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,400</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,120</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">320</td>
<td align="right">320</td>
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
<td align="right">390,630,860</td>
<td align="right">4.0%</td>
<td align="right">391,133,752</td>
<td align="right">4.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,405,567,021</td>
<td align="right">96.0%</td>
<td align="right">9,411,090,923</td>
<td align="right">96.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,506,672</td>
<td align="right">0.3%</td>
<td align="right">29,506,599</td>
<td align="right">0.3%</td>
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
<td align="right">1,126,844</td>
<td align="right">65.2%</td>
<td align="right">1,127,032</td>
<td align="right">65.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">602,728</td>
<td align="right">34.8%</td>
<td align="right">602,676</td>
<td align="right">34.8%</td>
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
<td align="left">remainder</td>
<td align="right">21,321</td>
<td align="right">1.9%</td>
<td align="right">21,386</td>
<td align="right">1.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">7,442</td>
<td align="right">0.7%</td>
<td align="right">7,463</td>
<td align="right">0.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">3,440</td>
<td align="right">0.3%</td>
<td align="right">3,433</td>
<td align="right">0.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">16,482</td>
<td align="right">1.5%</td>
<td align="right">16,514</td>
<td align="right">1.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,720</td>
<td align="right">0.9%</td>
<td align="right">9,702</td>
<td align="right">0.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">33,144</td>
<td align="right">2.9%</td>
<td align="right">33,199</td>
<td align="right">2.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">12,520</td>
<td align="right">1.1%</td>
<td align="right">12,501</td>
<td align="right">1.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,734</td>
<td align="right">0.5%</td>
<td align="right">5,741</td>
<td align="right">0.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">918</td>
<td align="right">0.1%</td>
<td align="right">917</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">83,694</td>
<td align="right">7.4%</td>
<td align="right">83,734</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">6,852</td>
<td align="right">0.6%</td>
<td align="right">6,849</td>
<td align="right">0.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">47,904</td>
<td align="right">4.3%</td>
<td align="right">47,921</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,169</td>
<td align="right">4.3%</td>
<td align="right">48,179</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">5,122</td>
<td align="right">0.5%</td>
<td align="right">5,123</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">6,164</td>
<td align="right">0.5%</td>
<td align="right">6,165</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,788</td>
<td align="right">2.9%</td>
<td align="right">32,787</td>
<td align="right">2.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">782,390</td>
<td align="right">69.4%</td>
<td align="right">782,378</td>
<td align="right">69.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,620</td>
<td align="right">0.2%</td>
<td align="right">2,620</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
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
<td align="right">618,246,692</td>
<td align="right">9.2%</td>
<td align="right">659,347,659</td>
<td align="right">9.6%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,085,646,709</td>
<td align="right">90.8%</td>
<td align="right">6,241,510,865</td>
<td align="right">90.4%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,812,868</td>
<td align="right">0.1%</td>
<td align="right">4,793,391</td>
<td align="right">0.1%</td>
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
<td align="left">Failure</td>
<td align="right">212,342</td>
<td align="right">53.2%</td>
<td align="right">225,882</td>
<td align="right">54.8%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">187,053</td>
<td align="right">46.8%</td>
<td align="right">186,550</td>
<td align="right">45.2%</td>
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
<td align="left">array int</td>
<td align="right">16,220</td>
<td align="right">7.6%</td>
<td align="right">26,640</td>
<td align="right">11.8%</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,380</td>
<td align="right">0.6%</td>
<td align="right">1,220</td>
<td align="right">0.5%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">820</td>
<td align="right">0.4%</td>
<td align="right">900</td>
<td align="right">0.4%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">55,120</td>
<td align="right">26.0%</td>
<td align="right">59,020</td>
<td align="right">26.1%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">122</td>
<td align="right">0.1%</td>
<td align="right">123</td>
<td align="right">0.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111,820</td>
<td align="right">52.7%</td>
<td align="right">110,957</td>
<td align="right">49.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,740</td>
<td align="right">10.2%</td>
<td align="right">21,902</td>
<td align="right">9.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">2.0%</td>
<td align="right">4,300</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">720</td>
<td align="right">0.3%</td>
<td align="right">720</td>
<td align="right">0.3%</td>
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
<td align="right">178,956,121</td>
<td align="right">1.3%</td>
<td align="right">181,480,670</td>
<td align="right">1.3%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">669,927,000</td>
<td align="right">4.7%</td>
<td align="right">672,693,152</td>
<td align="right">4.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,578,165,347</td>
<td align="right">95.3%</td>
<td align="right">13,599,740,557</td>
<td align="right">95.3%</td>
<td align="right">0.2%</td>
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
<td align="right">3,966,210</td>
<td align="right">95.7%</td>
<td align="right">4,013,402</td>
<td align="right">95.8%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">177,346</td>
<td align="right">4.3%</td>
<td align="right">177,455</td>
<td align="right">4.2%</td>
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
<td align="right">165,166</td>
<td align="right">93.1%</td>
<td align="right">165,275</td>
<td align="right">93.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">11,600</td>
<td align="right">6.5%</td>
<td align="right">11,600</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,320</td>
<td align="right">1.9%</td>
<td align="right">3,320</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,100</td>
<td align="right">1.2%</td>
<td align="right">2,100</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">960</td>
<td align="right">0.5%</td>
<td align="right">960</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">580</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,069,833</td>
<td align="right">0.0%</td>
<td align="right">1,202,123</td>
<td align="right">0.0%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">106,080,116</td>
<td align="right">1.8%</td>
<td align="right">107,206,578</td>
<td align="right">1.8%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,738,952,824</td>
<td align="right">98.2%</td>
<td align="right">5,756,270,233</td>
<td align="right">98.2%</td>
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
<td align="right">158,410</td>
<td align="right">66.0%</td>
<td align="right">164,128</td>
<td align="right">66.2%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">81,463</td>
<td align="right">34.0%</td>
<td align="right">83,890</td>
<td align="right">33.8%</td>
<td align="right">3.0%</td>
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
<td align="right">44,313</td>
<td align="right">28.0%</td>
<td align="right">49,473</td>
<td align="right">30.1%</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">1,560</td>
<td align="right">1.0%</td>
<td align="right">1,600</td>
<td align="right">1.0%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,120</td>
<td align="right">2.0%</td>
<td align="right">3,180</td>
<td align="right">1.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,174</td>
<td align="right">7.7%</td>
<td align="right">12,372</td>
<td align="right">7.5%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,351</td>
<td align="right">11.0%</td>
<td align="right">17,533</td>
<td align="right">10.7%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">20,139</td>
<td align="right">12.7%</td>
<td align="right">20,204</td>
<td align="right">12.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">16,159</td>
<td align="right">10.2%</td>
<td align="right">16,182</td>
<td align="right">9.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,466</td>
<td align="right">0.9%</td>
<td align="right">1,467</td>
<td align="right">0.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,888</td>
<td align="right">17.6%</td>
<td align="right">27,877</td>
<td align="right">17.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">6.7%</td>
<td align="right">10,680</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,640</td>
<td align="right">1.7%</td>
<td align="right">2,640</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">920</td>
<td align="right">0.6%</td>
<td align="right">920</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">52,728,178</td>
<td align="right">2.1%</td>
<td align="right">49,724,376</td>
<td align="right">1.9%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,496,561,927</td>
<td align="right">97.9%</td>
<td align="right">2,500,878,943</td>
<td align="right">98.0%</td>
<td align="right">0.2%</td>
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
<td align="right">84,489</td>
<td align="right">57.2%</td>
<td align="right">83,967</td>
<td align="right">57.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">63,118</td>
<td align="right">42.8%</td>
<td align="right">63,095</td>
<td align="right">42.9%</td>
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
<td align="right">19,752</td>
<td align="right">23.4%</td>
<td align="right">18,941</td>
<td align="right">22.6%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">13,960</td>
<td align="right">16.5%</td>
<td align="right">14,280</td>
<td align="right">17.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">18,680</td>
<td align="right">22.1%</td>
<td align="right">18,900</td>
<td align="right">22.5%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">32,097</td>
<td align="right">38.0%</td>
<td align="right">31,846</td>
<td align="right">37.9%</td>
<td align="right">-0.8%</td>
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
<td align="right">584,843,240</td>
<td align="right">54.7%</td>
<td align="right">592,736,832</td>
<td align="right">55.2%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">484,309,197</td>
<td align="right">45.3%</td>
<td align="right">481,422,901</td>
<td align="right">44.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,599,528</td>
<td align="right">0.2%</td>
<td align="right">2,596,500</td>
<td align="right">0.2%</td>
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
<td align="right">213,309</td>
<td align="right">67.9%</td>
<td align="right">212,451</td>
<td align="right">67.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">100,818</td>
<td align="right">32.1%</td>
<td align="right">100,774</td>
<td align="right">32.2%</td>
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
<td align="left">reversed list</td>
<td align="right">3,700</td>
<td align="right">1.7%</td>
<td align="right">2,960</td>
<td align="right">1.4%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">5,240</td>
<td align="right">2.5%</td>
<td align="right">5,180</td>
<td align="right">2.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4,180</td>
<td align="right">2.0%</td>
<td align="right">4,220</td>
<td align="right">2.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,440</td>
<td align="right">1.1%</td>
<td align="right">2,460</td>
<td align="right">1.2%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">820</td>
<td align="right">0.4%</td>
<td align="right">818</td>
<td align="right">0.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,148</td>
<td align="right">8.5%</td>
<td align="right">18,109</td>
<td align="right">8.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">39,789</td>
<td align="right">18.7%</td>
<td align="right">39,720</td>
<td align="right">18.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,926</td>
<td align="right">3.2%</td>
<td align="right">6,920</td>
<td align="right">3.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,967</td>
<td align="right">5.6%</td>
<td align="right">11,965</td>
<td align="right">5.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">105,820</td>
<td align="right">49.6%</td>
<td align="right">105,820</td>
<td align="right">49.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,279</td>
<td align="right">3.4%</td>
<td align="right">7,279</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,960</td>
<td align="right">2.8%</td>
<td align="right">5,960</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.3%</td>
<td align="right">740</td>
<td align="right">0.3%</td>
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
<td align="right">401,439,244</td>
<td align="right">2.5%</td>
<td align="right">387,302,742</td>
<td align="right">2.4%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,026,201,802</td>
<td align="right">6.4%</td>
<td align="right">1,016,650,234</td>
<td align="right">6.3%</td>
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
<td align="right">15,004,175,487</td>
<td align="right">93.5%</td>
<td align="right">15,053,301,463</td>
<td align="right">93.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">303,840</td>
<td align="right">0.0%</td>
<td align="right">303,840</td>
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
<td align="right">8,271,728</td>
<td align="right">90.3%</td>
<td align="right">8,004,214</td>
<td align="right">90.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">888,791</td>
<td align="right">9.7%</td>
<td align="right">891,715</td>
<td align="right">10.0%</td>
<td align="right">0.3%</td>
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
<td align="left">method</td>
<td align="right">104,622</td>
<td align="right">11.8%</td>
<td align="right">105,998</td>
<td align="right">11.9%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">161,375</td>
<td align="right">18.2%</td>
<td align="right">162,315</td>
<td align="right">18.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,511</td>
<td align="right">2.3%</td>
<td align="right">20,624</td>
<td align="right">2.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3,316</td>
<td align="right">0.4%</td>
<td align="right">3,304</td>
<td align="right">0.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">19,112</td>
<td align="right">2.2%</td>
<td align="right">19,151</td>
<td align="right">2.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">157,213</td>
<td align="right">17.7%</td>
<td align="right">157,460</td>
<td align="right">17.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">90,852</td>
<td align="right">10.2%</td>
<td align="right">90,956</td>
<td align="right">10.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">77,690</td>
<td align="right">8.7%</td>
<td align="right">77,776</td>
<td align="right">8.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,580</td>
<td align="right">1.8%</td>
<td align="right">15,563</td>
<td align="right">1.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">172,144</td>
<td align="right">19.4%</td>
<td align="right">172,192</td>
<td align="right">19.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">27,940</td>
<td align="right">3.1%</td>
<td align="right">27,940</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">18,660</td>
<td align="right">2.1%</td>
<td align="right">18,660</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">7,660</td>
<td align="right">0.9%</td>
<td align="right">7,660</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,756</td>
<td align="right">0.8%</td>
<td align="right">6,756</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">3,100</td>
<td align="right">0.3%</td>
<td align="right">3,100</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.1%</td>
<td align="right">1,140</td>
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
<td align="right">5,041,185,515</td>
<td align="right">99.6%</td>
<td align="right">4,820,083,600</td>
<td align="right">99.6%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">425,004</td>
<td align="right">0.0%</td>
<td align="right">422,843</td>
<td align="right">0.0%</td>
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
<td align="right">20,365,618</td>
<td align="right">0.4%</td>
<td align="right">20,363,442</td>
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
<td align="right">9,860</td>
<td align="right">0.0%</td>
<td align="right">9,860</td>
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
<td align="right">521,023</td>
<td align="right">100.0%</td>
<td align="right">520,696</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">86,732,447</td>
<td align="right">100.0%</td>
<td align="right">86,828,616</td>
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
<td align="right">8,443</td>
<td align="right">0.0%</td>
<td align="right">8,444</td>
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
<td align="right">8,460</td>
<td align="right">100.0%</td>
<td align="right">8,460</td>
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
<td align="right">173,886,908</td>
<td align="right">18.1%</td>
<td align="right">173,884,390</td>
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
<td align="right">786,861,685</td>
<td align="right">81.9%</td>
<td align="right">786,851,016</td>
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
<td align="right">27,720</td>
<td align="right">0.0%</td>
<td align="right">27,720</td>
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
<td align="right">7,106</td>
<td align="right">10.3%</td>
<td align="right">7,068</td>
<td align="right">10.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,886</td>
<td align="right">89.7%</td>
<td align="right">61,886</td>
<td align="right">89.7%</td>
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
<td align="right">53.6%</td>
<td align="right">33,180</td>
<td align="right">53.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,126</td>
<td align="right">26.1%</td>
<td align="right">16,126</td>
<td align="right">26.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,080</td>
<td align="right">16.3%</td>
<td align="right">10,080</td>
<td align="right">16.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">3.7%</td>
<td align="right">2,260</td>
<td align="right">3.7%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">189,556,524</td>
<td align="right">7.2%</td>
<td align="right">190,440,738</td>
<td align="right">7.2%</td>
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
<td align="right">2,447,425,265</td>
<td align="right">92.7%</td>
<td align="right">2,455,969,485</td>
<td align="right">92.7%</td>
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
<td align="right">140,303,175</td>
<td align="right">5.3%</td>
<td align="right">140,329,132</td>
<td align="right">5.3%</td>
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
<td align="right">99,844</td>
<td align="right">3.5%</td>
<td align="right">100,368</td>
<td align="right">3.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,764,952</td>
<td align="right">96.5%</td>
<td align="right">2,765,324</td>
<td align="right">96.5%</td>
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
<td align="left">property</td>
<td align="right">4,400</td>
<td align="right">4.4%</td>
<td align="right">4,540</td>
<td align="right">4.5%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,760</td>
<td align="right">8.8%</td>
<td align="right">8,902</td>
<td align="right">8.9%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,640</td>
<td align="right">14.7%</td>
<td align="right">14,720</td>
<td align="right">14.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">31,920</td>
<td align="right">32.0%</td>
<td align="right">32,060</td>
<td align="right">31.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">5,060</td>
<td align="right">5.1%</td>
<td align="right">5,080</td>
<td align="right">5.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,884</td>
<td align="right">9.9%</td>
<td align="right">9,886</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">10,900</td>
<td align="right">10.9%</td>
<td align="right">10,900</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,820</td>
<td align="right">6.8%</td>
<td align="right">6,820</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,820</td>
<td align="right">5.8%</td>
<td align="right">5,820</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,580</td>
<td align="right">1.6%</td>
<td align="right">1,580</td>
<td align="right">1.6%</td>
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
<td align="right">232,333,057</td>
<td align="right">20.9%</td>
<td align="right">267,203,624</td>
<td align="right">23.2%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">880,883,360</td>
<td align="right">79.1%</td>
<td align="right">882,834,012</td>
<td align="right">76.8%</td>
<td align="right">0.2%</td>
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
<td align="right">101,778</td>
<td align="right">85.9%</td>
<td align="right">110,758</td>
<td align="right">86.9%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,723</td>
<td align="right">14.1%</td>
<td align="right">16,722</td>
<td align="right">13.1%</td>
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
<td align="right">6.4%</td>
<td align="right">13,140</td>
<td align="right">11.9%</td>
<td align="right">102.8%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">40,396</td>
<td align="right">39.7%</td>
<td align="right">42,718</td>
<td align="right">38.6%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">8,602</td>
<td align="right">8.5%</td>
<td align="right">8,600</td>
<td align="right">7.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,440</td>
<td align="right">42.7%</td>
<td align="right">43,440</td>
<td align="right">39.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
<td align="right">1,500</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,360</td>
<td align="right">1.3%</td>
<td align="right">1,360</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">192,018,283</td>
<td align="right">3.2%</td>
<td align="right">192,773,449</td>
<td align="right">3.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,717,558,273</td>
<td align="right">96.7%</td>
<td align="right">5,734,373,705</td>
<td align="right">96.7%</td>
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
<td align="right">25,037,451</td>
<td align="right">0.4%</td>
<td align="right">25,066,187</td>
<td align="right">0.4%</td>
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
<td align="right">282,833</td>
<td align="right">29.2%</td>
<td align="right">283,201</td>
<td align="right">29.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">684,575</td>
<td align="right">70.8%</td>
<td align="right">685,020</td>
<td align="right">70.8%</td>
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
<td align="left">other</td>
<td align="right">5,267</td>
<td align="right">1.9%</td>
<td align="right">5,220</td>
<td align="right">1.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">23,323</td>
<td align="right">8.2%</td>
<td align="right">23,434</td>
<td align="right">8.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2,340</td>
<td align="right">0.8%</td>
<td align="right">2,333</td>
<td align="right">0.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">96,981</td>
<td align="right">34.3%</td>
<td align="right">97,242</td>
<td align="right">34.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">14,728</td>
<td align="right">5.2%</td>
<td align="right">14,766</td>
<td align="right">5.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">7,826</td>
<td align="right">2.8%</td>
<td align="right">7,819</td>
<td align="right">2.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">31,925</td>
<td align="right">11.3%</td>
<td align="right">31,901</td>
<td align="right">11.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">84,263</td>
<td align="right">29.8%</td>
<td align="right">84,314</td>
<td align="right">29.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">14,840</td>
<td align="right">5.2%</td>
<td align="right">14,832</td>
<td align="right">5.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">920</td>
<td align="right">0.3%</td>
<td align="right">920</td>
<td align="right">0.3%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">199,933</td>
<td align="right">0.0%</td>
<td align="right">199,681</td>
<td align="right">0.0%</td>
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
<td align="right">1,547,571,343</td>
<td align="right">100.0%</td>
<td align="right">1,547,876,666</td>
<td align="right">100.0%</td>
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
<td align="left">Success</td>
<td align="right">32,971</td>
<td align="right">94.0%</td>
<td align="right">32,952</td>
<td align="right">94.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,098</td>
<td align="right">6.0%</td>
<td align="right">2,097</td>
<td align="right">6.0%</td>
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
<td align="right">1,218</td>
<td align="right">58.1%</td>
<td align="right">1,217</td>
<td align="right">58.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">500</td>
<td align="right">23.8%</td>
<td align="right">500</td>
<td align="right">23.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">18.1%</td>
<td align="right">380</td>
<td align="right">18.1%</td>
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
<td align="right">34,694,623,008</td>
<td align="right">34.2%</td>
<td align="right">33,477,461,657</td>
<td align="right">33.6%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,325,434,419</td>
<td align="right">9.2%</td>
<td align="right">9,109,595,674</td>
<td align="right">9.1%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">786,938,653</td>
<td align="right">0.8%</td>
<td align="right">775,489,092</td>
<td align="right">0.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">56,702,293,181</td>
<td align="right">55.9%</td>
<td align="right">56,201,853,866</td>
<td align="right">56.4%</td>
<td align="right">-0.9%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">232,333,057</td>
<td align="right">5.6%</td>
<td align="right">267,203,624</td>
<td align="right">6.3%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">618,246,692</td>
<td align="right">14.9%</td>
<td align="right">659,347,659</td>
<td align="right">15.6%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">106,080,116</td>
<td align="right">2.6%</td>
<td align="right">107,206,578</td>
<td align="right">2.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,026,201,802</td>
<td align="right">24.7%</td>
<td align="right">1,016,650,234</td>
<td align="right">24.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">484,309,197</td>
<td align="right">11.7%</td>
<td align="right">481,422,901</td>
<td align="right">11.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">189,556,524</td>
<td align="right">4.6%</td>
<td align="right">190,440,738</td>
<td align="right">4.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">669,927,000</td>
<td align="right">16.1%</td>
<td align="right">672,693,152</td>
<td align="right">15.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">192,018,283</td>
<td align="right">4.6%</td>
<td align="right">192,773,449</td>
<td align="right">4.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">390,630,860</td>
<td align="right">9.4%</td>
<td align="right">391,133,752</td>
<td align="right">9.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,886,908</td>
<td align="right">4.2%</td>
<td align="right">173,884,390</td>
<td align="right">4.1%</td>
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
<td align="right">127,886,441</td>
<td align="right">16.2%</td>
<td align="right">113,778,415</td>
<td align="right">14.7%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">103,543,513</td>
<td align="right">13.2%</td>
<td align="right">105,855,627</td>
<td align="right">13.6%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,273,886</td>
<td align="right">2.3%</td>
<td align="right">18,139,586</td>
<td align="right">2.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,146,050</td>
<td align="right">3.2%</td>
<td align="right">25,135,126</td>
<td align="right">3.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">115,128,843</td>
<td align="right">14.6%</td>
<td align="right">115,165,798</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">173,631,872</td>
<td align="right">22.1%</td>
<td align="right">173,667,020</td>
<td align="right">22.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,974,264</td>
<td align="right">4.6%</td>
<td align="right">35,978,616</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,363,645</td>
<td align="right">4.5%</td>
<td align="right">35,366,823</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,601,422</td>
<td align="right">3.5%</td>
<td align="right">27,598,994</td>
<td align="right">3.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,179,360</td>
<td align="right">2.6%</td>
<td align="right">20,179,360</td>
<td align="right">2.6%</td>
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
<td align="right">477,023,672</td>
<td align="right">5.6%</td>
<td align="right">335,037,217</td>
<td align="right">3.9%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,583,007,158</td>
<td align="right">18.5%</td>
<td align="right">1,441,344,099</td>
<td align="right">16.8%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,588,335,438</td>
<td align="right">18.6%</td>
<td align="right">1,446,672,379</td>
<td align="right">16.9%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,447,488,119</td>
<td align="right">28.6%</td>
<td align="right">2,305,679,197</td>
<td align="right">26.9%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,447,488,119</td>
<td align="right">28.6%</td>
<td align="right">2,305,679,197</td>
<td align="right">26.9%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,096,250,174</td>
<td align="right">71.4%</td>
<td align="right">6,253,572,803</td>
<td align="right">73.1%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,756,055,045</td>
<td align="right">79.1%</td>
<td align="right">6,771,258,262</td>
<td align="right">79.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">340,898,285</td>
<td align="right">4.0%</td>
<td align="right">341,151,309</td>
<td align="right">4.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">36,900,120</td>
<td align="right">0.4%</td>
<td align="right">36,873,498</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">86,081,922</td>
<td align="right">1.0%</td>
<td align="right">86,067,301</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">859,152,681</td>
<td align="right">10.1%</td>
<td align="right">859,006,818</td>
<td align="right">10.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">177,010,113</td>
<td align="right">2.1%</td>
<td align="right">176,993,629</td>
<td align="right">2.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">5,298,440</td>
<td align="right">0.1%</td>
<td align="right">5,298,440</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">29,840</td>
<td align="right">0.0%</td>
<td align="right">29,840</td>
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
<td align="right">7,545,173</td>
<td align="right"></td>
<td align="right">7,779,931</td>
<td align="right"></td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,557,119,363</td>
<td align="right"></td>
<td align="right">4,416,027,159</td>
<td align="right"></td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">69,157,608</td>
<td align="right"></td>
<td align="right">67,212,493</td>
<td align="right"></td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">75,711,041</td>
<td align="right"></td>
<td align="right">73,998,377</td>
<td align="right"></td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">46,636,634,529</td>
<td align="right">33.7%</td>
<td align="right">45,957,297,013</td>
<td align="right">33.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,861,003,513</td>
<td align="right"></td>
<td align="right">2,894,098,226</td>
<td align="right"></td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">91,838,342,593</td>
<td align="right">66.3%</td>
<td align="right">92,813,231,040</td>
<td align="right">66.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">99,230,091,399</td>
<td align="right">61.6%</td>
<td align="right">99,645,480,237</td>
<td align="right">61.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,012,109</td>
<td align="right"></td>
<td align="right">174,300,836</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">61,961,065,674</td>
<td align="right">38.4%</td>
<td align="right">61,861,415,774</td>
<td align="right">38.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">93,861,413</td>
<td align="right">0.4%</td>
<td align="right">93,984,864</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,900,737,816</td>
<td align="right">52.1%</td>
<td align="right">12,916,773,567</td>
<td align="right">52.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">13,010,236,679</td>
<td align="right">52.5%</td>
<td align="right">13,026,399,475</td>
<td align="right">52.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,710,260,198</td>
<td align="right"></td>
<td align="right">13,726,580,662</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,760,096,364</td>
<td align="right">47.5%</td>
<td align="right">11,768,594,282</td>
<td align="right">47.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,762,110,699</td>
<td align="right"></td>
<td align="right">11,770,605,780</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">15,637,450</td>
<td align="right">0.1%</td>
<td align="right">15,641,044</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,384,660</td>
<td align="right">1.9%</td>
<td align="right">3,384,660</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">128,160</td>
<td align="right">0.1%</td>
<td align="right">128,160</td>
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
<td align="right">115,841,313</td>
<td align="right">19,718,699,203</td>
<td align="right">0</td>
<td align="right">116,266,640</td>
<td align="right">19,767,631,149</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,357,532</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,357,544</td>
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
<td align="right">574,673</td>
<td align="right">59.8%</td>
<td align="right">624,482</td>
<td align="right">61.9%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">806,005</td>
<td align="right">83.9%</td>
<td align="right">855,575</td>
<td align="right">84.8%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">961,022</td>
<td align="right"></td>
<td align="right">1,008,465</td>
<td align="right"></td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,247,968,210</td>
<td align="right"></td>
<td align="right">7,410,583,343</td>
<td align="right"></td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">7,436</td>
<td align="right">4.8%</td>
<td align="right">7,323</td>
<td align="right">4.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">265,051,446,351</td>
<td align="right">3,656.9%</td>
<td align="right">269,033,096,393</td>
<td align="right">3,630.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">153,856</td>
<td align="right">16.0%</td>
<td align="right">151,714</td>
<td align="right">15.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,161</td>
<td align="right">0.1%</td>
<td align="right">1,176</td>
<td align="right">0.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">18,727</td>
<td align="right">1.9%</td>
<td align="right">18,602</td>
<td align="right">1.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">17,187</td>
<td align="right">1.8%</td>
<td align="right">17,178</td>
<td align="right">1.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">160</td>
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
<td align="right">1,840</td>
<td align="right">0.2%</td>
<td align="right">1,840</td>
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
<td align="right">133,884</td>
<td align="right">87.0%</td>
<td align="right">131,767</td>
<td align="right">86.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">153,856</td>
<td align="right"></td>
<td align="right">151,714</td>
<td align="right"></td>
<td align="right">-1.4%</td>
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
<td align="right">2,532</td>
<td align="right">1.6%</td>
<td align="right">2,532</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
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
<td align="right">11,840</td>
<td align="right">7.7%</td>
<td align="right">16,157</td>
<td align="right">10.6%</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">17,368</td>
<td align="right">11.3%</td>
<td align="right">12,754</td>
<td align="right">8.4%</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">42,278</td>
<td align="right">27.5%</td>
<td align="right">41,906</td>
<td align="right">27.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">36,426</td>
<td align="right">23.7%</td>
<td align="right">35,640</td>
<td align="right">23.5%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">28,562</td>
<td align="right">18.6%</td>
<td align="right">28,275</td>
<td align="right">18.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">14,482</td>
<td align="right">9.4%</td>
<td align="right">14,082</td>
<td align="right">9.3%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,720</td>
<td align="right">1.8%</td>
<td align="right">2,720</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">180</td>
<td align="right">0.1%</td>
<td align="right">180</td>
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
<td align="right">10,522</td>
<td align="right">6.8%</td>
<td align="right">10,388</td>
<td align="right">6.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">11,376</td>
<td align="right">7.4%</td>
<td align="right">11,827</td>
<td align="right">7.8%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">27,737</td>
<td align="right">18.0%</td>
<td align="right">26,920</td>
<td align="right">17.7%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">41,501</td>
<td align="right">27.0%</td>
<td align="right">41,215</td>
<td align="right">27.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">25,844</td>
<td align="right">16.8%</td>
<td align="right">24,881</td>
<td align="right">16.4%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">12,371</td>
<td align="right">8.0%</td>
<td align="right">12,223</td>
<td align="right">8.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,993</td>
<td align="right">2.6%</td>
<td align="right">3,773</td>
<td align="right">2.5%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="right">736,620</td>
<td align="right">2,075,680</td>
<td align="right">181.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">55,490,254</td>
<td align="right">110,148,831</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">246,349,702</td>
<td align="right">438,273,285</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">313,059,148</td>
<td align="right">465,747,981</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">124,637,269</td>
<td align="right">179,295,904</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">757,374</td>
<td align="right">463,522</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">128,667,539</td>
<td align="right">166,967,494</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">939,636</td>
<td align="right">704,538</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">877,163,368</td>
<td align="right">1,080,219,411</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">186,682,244</td>
<td align="right">225,089,400</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,562,177,336</td>
<td align="right">2,882,395,431</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">150,540</td>
<td align="right">169,340</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,614,085,976</td>
<td align="right">2,937,809,011</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">62,940,240</td>
<td align="right">55,262,500</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,621,695,486</td>
<td align="right">1,441,751,439</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,675,002</td>
<td align="right">350,732,552</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,338,140,875</td>
<td align="right">2,525,739,242</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,113,566,572</td>
<td align="right">2,260,814,139</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">51,193,980</td>
<td align="right">54,665,900</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,089,917</td>
<td align="right">603,472,763</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">857,159,404</td>
<td align="right">912,201,286</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">901,252,350</td>
<td align="right">843,483,648</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">7,472,487</td>
<td align="right">7,009,092</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,394,743,476</td>
<td align="right">7,831,963,923</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">644,026,228</td>
<td align="right">609,156,540</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,466,020</td>
<td align="right">557,752,500</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">67,412,601</td>
<td align="right">70,846,233</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">659,089,179</td>
<td align="right">692,548,820</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,893,582,345</td>
<td align="right">3,029,118,174</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">794,124,183</td>
<td align="right">830,986,313</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,313,951,871</td>
<td align="right">4,509,495,120</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,996,424,484</td>
<td align="right">3,131,848,808</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,422,157,636</td>
<td align="right">6,697,755,742</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">78,947,068</td>
<td align="right">82,220,189</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,061,390,551</td>
<td align="right">7,346,175,511</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">892,516,367</td>
<td align="right">928,189,868</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,044,937,285</td>
<td align="right">1,005,201,167</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,215,870,556</td>
<td align="right">3,334,863,792</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">47,388,696</td>
<td align="right">49,140,809</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,578,807</td>
<td align="right">1,102,567,206</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">94,454,115</td>
<td align="right">97,606,853</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,448,771,278</td>
<td align="right">3,562,590,590</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">922,098,561</td>
<td align="right">951,645,020</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">826,490,196</td>
<td align="right">852,297,751</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,666,633,857</td>
<td align="right">2,744,595,884</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,386,930,970</td>
<td align="right">1,426,603,728</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,426,335,471</td>
<td align="right">1,388,273,468</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">145,243,975</td>
<td align="right">148,777,836</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,261,892,611</td>
<td align="right">6,408,079,598</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,247,968,210</td>
<td align="right">7,410,583,343</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,204,247,106</td>
<td align="right">1,230,279,129</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">164,272,312</td>
<td align="right">160,791,826</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,322,456,109</td>
<td align="right">1,348,392,841</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,344,623,944</td>
<td align="right">1,370,028,523</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">112,685,554</td>
<td align="right">114,784,628</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">112,928,174</td>
<td align="right">115,027,248</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,265,360,247</td>
<td align="right">5,168,627,811</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">8,252,853</td>
<td align="right">8,395,534</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,335,947,623</td>
<td align="right">6,442,232,156</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">405,313,598</td>
<td align="right">398,764,491</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,716,483,582</td>
<td align="right">1,739,509,036</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">376,605,192</td>
<td align="right">371,556,431</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,833,996,846</td>
<td align="right">1,858,261,776</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">658,631,961</td>
<td align="right">649,994,100</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,388,342,821</td>
<td align="right">14,573,372,688</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,800,621,552</td>
<td align="right">1,823,710,626</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,072,216,689</td>
<td align="right">2,097,385,007</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,893,590,258</td>
<td align="right">1,915,863,189</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,997,567,195</td>
<td align="right">2,020,167,862</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">14,903,138</td>
<td align="right">15,068,000</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">208,339,279</td>
<td align="right">206,057,811</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">383,255,188</td>
<td align="right">387,255,096</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,345,535,175</td>
<td align="right">10,239,460,119</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,627,770,028</td>
<td align="right">3,664,311,543</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">471,399,429</td>
<td align="right">475,817,101</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,576,899,998</td>
<td align="right">1,564,457,730</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">420,368,501</td>
<td align="right">417,383,919</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">840,809,037</td>
<td align="right">834,841,037</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">768,923,985</td>
<td align="right">764,755,144</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,750,608,746</td>
<td align="right">1,741,379,299</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,567,449,555</td>
<td align="right">4,543,873,265</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">702,267,006</td>
<td align="right">705,763,909</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,837,992,985</td>
<td align="right">3,856,275,208</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">150,972,010</td>
<td align="right">151,662,606</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,785,358</td>
<td align="right">90,388,474</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">286,833,851</td>
<td align="right">288,077,973</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">37,121,748</td>
<td align="right">36,964,701</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">238,372,080</td>
<td align="right">239,252,159</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">182,223,785</td>
<td align="right">181,560,296</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,082,431,877</td>
<td align="right">1,086,202,350</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">163,709,067</td>
<td align="right">163,145,393</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">275,800,242</td>
<td align="right">274,865,614</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,009,877,112</td>
<td align="right">1,013,246,470</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">901,513,044</td>
<td align="right">904,420,518</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">19,496,594,649</td>
<td align="right">19,557,828,042</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,502,255,520</td>
<td align="right">1,497,625,986</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">59,923,424</td>
<td align="right">59,738,946</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,034,841,654</td>
<td align="right">2,029,178,419</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">965,370,310</td>
<td align="right">968,008,503</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">98,902,686</td>
<td align="right">98,644,177</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">99,474,826</td>
<td align="right">99,216,317</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">539,334,920</td>
<td align="right">538,013,280</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,380,368,101</td>
<td align="right">2,374,581,466</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,299,508,882</td>
<td align="right">2,294,026,688</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,351,452,330</td>
<td align="right">2,346,069,387</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,542,318,599</td>
<td align="right">1,545,648,224</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">13,706,610</td>
<td align="right">13,735,465</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">13,706,610</td>
<td align="right">13,735,465</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">275,294,305</td>
<td align="right">274,715,491</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">10,205,600</td>
<td align="right">10,223,980</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">164,464,077</td>
<td align="right">164,168,995</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,343,924,506</td>
<td align="right">1,346,321,003</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,842,468,663</td>
<td align="right">2,837,556,129</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,019,550,855</td>
<td align="right">2,016,301,823</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,212,078</td>
<td align="right">10,226,371</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">993,145,394</td>
<td align="right">991,828,876</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">519,906,526</td>
<td align="right">519,231,647</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">440,925,898</td>
<td align="right">440,389,667</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,251,894,718</td>
<td align="right">1,250,450,418</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">16,132,472,839</td>
<td align="right">16,114,056,622</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">240,047,693</td>
<td align="right">240,275,687</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">213,776,409</td>
<td align="right">213,586,902</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">252,426,674</td>
<td align="right">252,650,329</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,504,110</td>
<td align="right">1,505,422</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">110,342,500</td>
<td align="right">110,247,640</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">45,633,932</td>
<td align="right">45,594,804</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,636,471,532</td>
<td align="right">3,633,382,857</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">135,342,844</td>
<td align="right">135,457,682</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">135,342,844</td>
<td align="right">135,457,682</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,553,894</td>
<td align="right">1,552,585</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">317,168,937</td>
<td align="right">316,928,961</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">676,611,951</td>
<td align="right">676,100,119</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,829,731,568</td>
<td align="right">1,828,449,270</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">165,019,445</td>
<td align="right">165,133,431</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">252,023,865</td>
<td align="right">251,860,310</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">558,117,035</td>
<td align="right">557,759,444</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">255,566,895</td>
<td align="right">255,403,465</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,606,433,182</td>
<td align="right">5,602,876,481</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">143,912,926</td>
<td align="right">143,832,489</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">576,508,675</td>
<td align="right">576,818,799</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">96,589,120</td>
<td align="right">96,640,440</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">196,586,749</td>
<td align="right">196,491,107</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">64,032,460</td>
<td align="right">64,004,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,102,582,885</td>
<td align="right">1,103,053,369</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,633,024</td>
<td align="right">40,616,317</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">47,987,974</td>
<td align="right">48,006,311</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">120,071,290</td>
<td align="right">120,116,684</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">198,505,933</td>
<td align="right">198,431,822</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,827,020</td>
<td align="right">97,862,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,691,439,915</td>
<td align="right">4,693,112,965</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,987,725</td>
<td align="right">79,013,807</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,354,199,274</td>
<td align="right">1,353,755,307</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,000,363,308</td>
<td align="right">2,000,970,033</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">387,525,706</td>
<td align="right">387,411,365</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">388,752,966</td>
<td align="right">388,638,625</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,010,871</td>
<td align="right">3,009,999</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,965,260</td>
<td align="right">154,920,900</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">94,536,936</td>
<td align="right">94,563,051</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">502,451</td>
<td align="right">502,327</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,127,526,156</td>
<td align="right">1,127,302,220</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,890,871</td>
<td align="right">4,889,999</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">57,791,780</td>
<td align="right">57,781,600</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">122,870</td>
<td align="right">122,890</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">9,666,541,388</td>
<td align="right">9,668,006,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">98,900,635</td>
<td align="right">98,886,924</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,948,735</td>
<td align="right">98,935,024</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,778,910</td>
<td align="right">8,777,755</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,679,948,267</td>
<td align="right">1,680,134,025</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">173,974,040</td>
<td align="right">173,992,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">323,755,387</td>
<td align="right">323,783,951</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">269,830</td>
<td align="right">269,850</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">870,514,947</td>
<td align="right">870,459,880</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">8,516,180</td>
<td align="right">8,516,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,474,908</td>
<td align="right">68,471,033</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">993,683,047</td>
<td align="right">993,727,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,280,412</td>
<td align="right">4,280,239</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">780,162,595</td>
<td align="right">780,181,136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">780,617,475</td>
<td align="right">780,636,016</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">395,807,588</td>
<td align="right">395,816,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,595,983,292</td>
<td align="right">1,595,963,097</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,446,110</td>
<td align="right">86,446,961</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">35,234,599</td>
<td align="right">35,234,888</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,008,620</td>
<td align="right">81,009,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,481,853</td>
<td align="right">733,486,849</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,820,614</td>
<td align="right">10,820,655</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">28,211,336</td>
<td align="right">28,211,434</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">73,431,640</td>
<td align="right">73,431,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,822,651</td>
<td align="right">32,822,712</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,392,719</td>
<td align="right">229,392,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,874,838</td>
<td align="right">3,874,834</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">69,147,015</td>
<td align="right">69,147,073</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,275,892</td>
<td align="right">518,275,719</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">131,859,996</td>
<td align="right">131,859,992</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">122,541,941</td>
<td align="right">122,541,940</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,584,660</td>
<td align="right">533,584,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,493,780</td>
<td align="right">32,493,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,688,800</td>
<td align="right">12,688,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">11,929,340</td>
<td align="right">11,929,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,351,700</td>
<td align="right">7,351,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,650,660</td>
<td align="right">5,650,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,635,980</td>
<td align="right">5,635,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,016,240</td>
<td align="right">3,016,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,701,920</td>
<td align="right">2,701,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,799,640</td>
<td align="right">1,799,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,225,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">581,940</td>
<td align="right">581,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">375,780</td>
<td align="right">375,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right">78,400</td>
<td align="right">78,400</td>
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
<td align="right">8,200</td>
<td align="right">8,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right"></td>
<td align="right">54,677,537</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right"></td>
<td align="right">54,670,937</td>
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
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,520</td>
<td align="right">1,560</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">45,952</td>
<td align="right">44,805</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">37,126</td>
<td align="right">36,642</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">158,304</td>
<td align="right">159,303</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,420</td>
<td align="right">34,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">4,600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">820</td>
<td align="right">820</td>
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
<td align="right">1,110</td>
<td align="right">1,107</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,110</td>
<td align="right">1,107</td>
<td align="right">-0.3%</td>
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
<td align="right">1,820</td>
<td align="right">1,820</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-08-01
