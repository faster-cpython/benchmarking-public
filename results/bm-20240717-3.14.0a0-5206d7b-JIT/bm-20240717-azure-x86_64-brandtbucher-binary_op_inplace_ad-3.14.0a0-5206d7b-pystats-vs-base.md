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
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">219,477</td>
<td align="right">974,902</td>
<td align="right">344.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">490,920</td>
<td align="right">1,006,200</td>
<td align="right">105.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">1,120</td>
<td align="right">420</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">720</td>
<td align="right">960</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,366,909</td>
<td align="right">1,605,359</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">30,799,981</td>
<td align="right">35,034,942</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,867,740</td>
<td align="right">3,387,349</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">100,339,393</td>
<td align="right">105,798,046</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">42,434,520</td>
<td align="right">44,508,166</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,694,682</td>
<td align="right">21,428,758</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,153,010</td>
<td align="right">21,886,756</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,160,770</td>
<td align="right">21,894,515</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">36,374,599</td>
<td align="right">37,588,056</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,471,098</td>
<td align="right">16,890,376</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,411,522</td>
<td align="right">4,268,338</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,420</td>
<td align="right">168,626</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">114,690,192</td>
<td align="right">116,921,540</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,808,260</td>
<td align="right">1,774,532</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">87,789,412</td>
<td align="right">86,458,361</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,569,302</td>
<td align="right">160,822,378</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">215,264,001</td>
<td align="right">218,263,695</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">164,202,504</td>
<td align="right">166,472,290</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,387,265</td>
<td align="right">10,245,439</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">913,680,480</td>
<td align="right">925,966,308</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,357,271</td>
<td align="right">8,247,796</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">332,007,056</td>
<td align="right">335,867,325</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">299,193,840</td>
<td align="right">302,643,837</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">23,976,385</td>
<td align="right">24,230,891</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,224,388</td>
<td align="right">1,058,298,665</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">21,172,873</td>
<td align="right">20,955,632</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">386,961,780</td>
<td align="right">390,604,706</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">28,760</td>
<td align="right">29,020</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">76,340,987</td>
<td align="right">75,683,954</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,242,304</td>
<td align="right">62,743,596</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,290,424,402</td>
<td align="right">1,300,739,139</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,340</td>
<td align="right">21,180</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">657,740</td>
<td align="right">662,420</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">202,854,942</td>
<td align="right">204,185,988</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,873,383</td>
<td align="right">81,360,391</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">56,523,748</td>
<td align="right">56,196,150</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">54,255,790</td>
<td align="right">54,570,106</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">404,588,786</td>
<td align="right">406,912,133</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">205,869,852</td>
<td align="right">207,020,115</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,885</td>
<td align="right">14,968</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">196,716,761</td>
<td align="right">195,722,417</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,223,700,834</td>
<td align="right">6,254,904,499</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">679,767,357</td>
<td align="right">683,088,762</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">119,399,217</td>
<td align="right">118,841,147</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">273,730,979</td>
<td align="right">274,982,276</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,802,642</td>
<td align="right">124,251,848</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">385,091,916</td>
<td align="right">386,786,504</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">222,894</td>
<td align="right">223,860</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">228,046,807</td>
<td align="right">228,929,061</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">454,619,156</td>
<td align="right">456,146,057</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,667,039,857</td>
<td align="right">5,685,960,802</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,131,550,367</td>
<td align="right">1,135,322,938</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">59,194,221</td>
<td align="right">59,390,821</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,453,176,338</td>
<td align="right">2,461,230,749</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,877,530</td>
<td align="right">9,845,273</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,563,374,237</td>
<td align="right">1,568,250,423</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">81,682,651</td>
<td align="right">81,932,033</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,451,640</td>
<td align="right">82,702,561</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">295,222,030</td>
<td align="right">296,108,497</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">486,474,572</td>
<td align="right">487,902,362</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,176,177</td>
<td align="right">83,419,692</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,399,990,590</td>
<td align="right">2,406,968,806</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">194,496,515</td>
<td align="right">195,056,942</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,585,653,531</td>
<td align="right">21,647,823,297</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,165,100</td>
<td align="right">92,409,662</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,446,900</td>
<td align="right">94,691,762</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">556,992,038</td>
<td align="right">555,557,989</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,110,538,416</td>
<td align="right">1,107,681,764</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">283,352,584</td>
<td align="right">284,038,818</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,017,137,693</td>
<td align="right">1,019,586,847</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">481,396,433</td>
<td align="right">482,486,759</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,297,068,452</td>
<td align="right">3,304,499,257</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">142,240</td>
<td align="right">141,920</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,106,575,501</td>
<td align="right">4,115,771,584</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,608,679</td>
<td align="right">101,830,945</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">318,038,422</td>
<td align="right">318,733,642</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">173,188,546</td>
<td align="right">173,563,034</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">378,503,832</td>
<td align="right">379,294,354</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,490,732,158</td>
<td align="right">5,501,774,828</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,991,169,315</td>
<td align="right">6,002,436,702</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">366,811,548</td>
<td align="right">367,465,582</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">942,148,390</td>
<td align="right">943,688,980</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68,000,998</td>
<td align="right">67,891,585</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">901,649,056</td>
<td align="right">903,093,839</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,100,437,465</td>
<td align="right">4,106,897,798</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">140,544,033</td>
<td align="right">140,764,444</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,222,905,973</td>
<td align="right">4,229,269,875</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,804,795</td>
<td align="right">72,696,154</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,820,186,184</td>
<td align="right">2,823,900,725</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">829,582,143</td>
<td align="right">830,641,538</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">386,363,811</td>
<td align="right">386,855,406</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">199,228,102</td>
<td align="right">199,475,932</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">804,758,147</td>
<td align="right">805,719,826</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,211,587</td>
<td align="right">92,101,675</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">49,265,983</td>
<td align="right">49,211,183</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">739,551,750</td>
<td align="right">740,344,879</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,255,226,279</td>
<td align="right">1,256,386,190</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">276,486,120</td>
<td align="right">276,734,490</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">666,613,286</td>
<td align="right">666,022,473</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">200,133,632</td>
<td align="right">200,300,950</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">431,639,002</td>
<td align="right">431,281,888</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,411,766,932</td>
<td align="right">1,412,859,346</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,871,676,838</td>
<td align="right">1,873,063,634</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,603,446,124</td>
<td align="right">1,604,595,820</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,371,139,191</td>
<td align="right">1,372,071,045</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">48,283,030</td>
<td align="right">48,309,698</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,923,813</td>
<td align="right">403,119,068</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,378,557,435</td>
<td align="right">4,380,590,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">678,041,624</td>
<td align="right">678,322,516</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,265,582</td>
<td align="right">274,160,528</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,640,441</td>
<td align="right">3,639,144</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">231,216,019</td>
<td align="right">231,134,878</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,644,656,244</td>
<td align="right">2,645,559,229</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">211,206,992</td>
<td align="right">211,273,101</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">409,185,488</td>
<td align="right">409,308,871</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,344,774</td>
<td align="right">20,350,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">773,917,155</td>
<td align="right">774,148,743</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">639,900,244</td>
<td align="right">639,712,187</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">791,281,595</td>
<td align="right">791,505,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,297,579</td>
<td align="right">216,351,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">328,735,636</td>
<td align="right">328,657,138</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">485,045,636</td>
<td align="right">485,159,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">146,457,069</td>
<td align="right">146,423,192</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,235,850</td>
<td align="right">9,233,810</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,657,652</td>
<td align="right">9,655,609</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">12,102,480</td>
<td align="right">12,104,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">20,348,254</td>
<td align="right">20,344,626</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">166,855,165</td>
<td align="right">166,880,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">421,590,041</td>
<td align="right">421,649,718</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,526,817,955</td>
<td align="right">3,527,258,215</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,142,245</td>
<td align="right">91,137,497</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">66,953,719</td>
<td align="right">66,950,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">4,628,789</td>
<td align="right">4,629,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,714,481</td>
<td align="right">71,711,561</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,389,362</td>
<td align="right">143,384,542</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">79,275,288</td>
<td align="right">79,277,921</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,824</td>
<td align="right">687,802</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,606,880</td>
<td align="right">136,603,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,961,794</td>
<td align="right">10,962,083</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,874,075</td>
<td align="right">1,874,027</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,907,417</td>
<td align="right">555,894,296</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">108,507,142</td>
<td align="right">108,504,813</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,101,044</td>
<td align="right">48,100,242</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,155,812</td>
<td align="right">232,152,439</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,808,501</td>
<td align="right">31,808,042</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,812,291</td>
<td align="right">40,812,852</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,836,694</td>
<td align="right">53,837,427</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,950,756</td>
<td align="right">5,950,834</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,366</td>
<td align="right">190,037,447</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,338,350</td>
<td align="right">233,340,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">349,319,197</td>
<td align="right">349,316,537</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,914,450</td>
<td align="right">149,915,269</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">108,591,652</td>
<td align="right">108,591,383</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">137,977,958</td>
<td align="right">137,978,183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,911,234</td>
<td align="right">146,911,134</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,612,160</td>
<td align="right">46,612,136</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,319,338</td>
<td align="right">173,319,254</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,024,177</td>
<td align="right">402,024,131</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,763,188</td>
<td align="right">66,763,191</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,641,558</td>
<td align="right">225,641,554</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,220,555</td>
<td align="right">786,220,561</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">59,677,580</td>
<td align="right">59,677,580</td>
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
<td align="right">7,461,660</td>
<td align="right">7,461,660</td>
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
<td align="left">CLEANUP_THROW</td>
<td align="right">150,560</td>
<td align="right">150,560</td>
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
<td align="left">SET_ADD</td>
<td align="right">46,620</td>
<td align="right">46,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,180</td>
<td align="right">27,180</td>
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
<td align="right">1,040</td>
<td align="right">1,040</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,428,333,607</td>
<td align="right">95.6%</td>
<td align="right">9,446,604,928</td>
<td align="right">95.6%</td>
<td align="right">0.2%</td>
</tr>
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
<td align="right">437,085,757</td>
<td align="right">4.4%</td>
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
<td align="right">29,500,920</td>
<td align="right">0.3%</td>
<td align="right">29,500,920</td>
<td align="right">0.3%</td>
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
<td align="right">1,125,467</td>
<td align="right">65.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">597,623</td>
<td align="right">34.7%</td>
<td align="right">598,567</td>
<td align="right">34.7%</td>
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
<td align="right">5,632</td>
<td align="right">0.5%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">3,000</td>
<td align="right">0.3%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,318</td>
<td align="right">2.8%</td>
<td align="right">32,599</td>
<td align="right">2.9%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,608</td>
<td align="right">0.8%</td>
<td align="right">8,872</td>
<td align="right">0.8%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">22,733</td>
<td align="right">2.0%</td>
<td align="right">22,997</td>
<td align="right">2.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">13,649</td>
<td align="right">1.2%</td>
<td align="right">13,495</td>
<td align="right">1.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,356</td>
<td align="right">2.9%</td>
<td align="right">32,621</td>
<td align="right">2.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,915</td>
<td align="right">0.2%</td>
<td align="right">1,918</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">48,666</td>
<td align="right">4.3%</td>
<td align="right">48,630</td>
<td align="right">4.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,324</td>
<td align="right">4.3%</td>
<td align="right">48,326</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,608</td>
<td align="right">69.6%</td>
<td align="right">781,612</td>
<td align="right">69.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,405</td>
<td align="right">7.3%</td>
<td align="right">82,405</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">0.9%</td>
<td align="right">10,620</td>
<td align="right">0.9%</td>
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
<td align="left">xor</td>
<td align="right">8,884</td>
<td align="right">0.8%</td>
<td align="right">8,884</td>
<td align="right">0.8%</td>
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
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
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
<td align="right">744,732,482</td>
<td align="right">10.8%</td>
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
<td align="right">6,149,769,667</td>
<td align="right">89.2%</td>
<td align="right">6,151,631,339</td>
<td align="right">89.2%</td>
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
<td align="right">4,810,145</td>
<td align="right">0.1%</td>
<td align="right">4,810,122</td>
<td align="right">0.1%</td>
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
<td align="right">240,177</td>
<td align="right">56.9%</td>
<td align="right">240,755</td>
<td align="right">57.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,561</td>
<td align="right">43.1%</td>
<td align="right">181,764</td>
<td align="right">43.0%</td>
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
<td align="left">buffer int</td>
<td align="right">30,498</td>
<td align="right">12.7%</td>
<td align="right">30,720</td>
<td align="right">12.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">55,960</td>
<td align="right">23.3%</td>
<td align="right">56,320</td>
<td align="right">23.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">110,415</td>
<td align="right">46.0%</td>
<td align="right">110,411</td>
<td align="right">45.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,500</td>
<td align="right">8.1%</td>
<td align="right">19,500</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">6.7%</td>
<td align="right">16,200</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.2%</td>
<td align="right">5,340</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,665,382,100</td>
<td align="right">95.3%</td>
<td align="right">13,696,064,363</td>
<td align="right">95.4%</td>
<td align="right">0.2%</td>
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
<td align="right">662,562,162</td>
<td align="right">4.6%</td>
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
<td align="right">181,481,361</td>
<td align="right">1.3%</td>
<td align="right">181,519,280</td>
<td align="right">1.3%</td>
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
<td align="right">3,947,065</td>
<td align="right">96.0%</td>
<td align="right">3,951,142</td>
<td align="right">96.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">165,400</td>
<td align="right">4.0%</td>
<td align="right">165,422</td>
<td align="right">4.0%</td>
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
<td align="left">init not inline values</td>
<td align="right">2,920</td>
<td align="right">1.8%</td>
<td align="right">2,980</td>
<td align="right">1.8%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">1,940</td>
<td align="right">1.2%</td>
<td align="right">1,960</td>
<td align="right">1.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">9,160</td>
<td align="right">5.5%</td>
<td align="right">9,120</td>
<td align="right">5.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">155,900</td>
<td align="right">94.3%</td>
<td align="right">155,962</td>
<td align="right">94.3%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">101,184,383</td>
<td align="right">1.6%</td>
<td align="right">106,640,031</td>
<td align="right">1.7%</td>
<td align="right">5.4%</td>
</tr>
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
<td align="right">1,072,397</td>
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
<td align="right">6,122,623,431</td>
<td align="right">98.4%</td>
<td align="right">6,127,393,871</td>
<td align="right">98.3%</td>
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
<td align="right">149,614</td>
<td align="right">66.3%</td>
<td align="right">153,523</td>
<td align="right">66.6%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">76,183</td>
<td align="right">33.7%</td>
<td align="right">76,889</td>
<td align="right">33.4%</td>
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
<td align="left">bytes</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">3,600</td>
<td align="right">2.3%</td>
<td align="right">275.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">42,467</td>
<td align="right">28.4%</td>
<td align="right">43,622</td>
<td align="right">28.4%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,068</td>
<td align="right">18.1%</td>
<td align="right">27,157</td>
<td align="right">17.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,174</td>
<td align="right">8.1%</td>
<td align="right">12,204</td>
<td align="right">7.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,361</td>
<td align="right">9.6%</td>
<td align="right">14,342</td>
<td align="right">9.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,699</td>
<td align="right">11.2%</td>
<td align="right">16,714</td>
<td align="right">10.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,425</td>
<td align="right">1.0%</td>
<td align="right">1,424</td>
<td align="right">0.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,000</td>
<td align="right">12.7%</td>
<td align="right">19,000</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">10,680</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,580</td>
<td align="right">1.7%</td>
<td align="right">2,580</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,620</td>
<td align="right">1.1%</td>
<td align="right">1,620</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.4%</td>
<td align="right">580</td>
<td align="right">0.4%</td>
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
<td align="right">209,390,166</td>
<td align="right">7.8%</td>
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
<td align="right">2,489,643,392</td>
<td align="right">92.3%</td>
<td align="right">2,490,564,292</td>
<td align="right">92.2%</td>
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
<td align="right">114,950</td>
<td align="right">65.2%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,119</td>
<td align="right">35.0%</td>
<td align="right">61,239</td>
<td align="right">34.8%</td>
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
<td align="left">tuple</td>
<td align="right">27,521</td>
<td align="right">24.2%</td>
<td align="right">28,400</td>
<td align="right">24.7%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,717</td>
<td align="right">13.8%</td>
<td align="right">15,950</td>
<td align="right">13.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">56,540</td>
<td align="right">49.7%</td>
<td align="right">56,640</td>
<td align="right">49.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">13,940</td>
<td align="right">12.3%</td>
<td align="right">13,960</td>
<td align="right">12.1%</td>
<td align="right">0.1%</td>
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
<td align="right">2,590,078</td>
<td align="right">0.3%</td>
<td align="right">-0.4%</td>
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
<td align="right">484,781,901</td>
<td align="right">46.9%</td>
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
<td align="right">548,215,226</td>
<td align="right">53.1%</td>
<td align="right">548,602,901</td>
<td align="right">53.1%</td>
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
<td align="right">197,252</td>
<td align="right">67.1%</td>
<td align="right">198,173</td>
<td align="right">67.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">96,797</td>
<td align="right">32.9%</td>
<td align="right">96,763</td>
<td align="right">32.8%</td>
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
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">280</td>
<td align="right">0.1%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,060</td>
<td align="right">2.1%</td>
<td align="right">4,320</td>
<td align="right">2.2%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,220</td>
<td align="right">2.1%</td>
<td align="right">4,480</td>
<td align="right">2.3%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,300</td>
<td align="right">3.2%</td>
<td align="right">6,560</td>
<td align="right">3.3%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,289</td>
<td align="right">5.7%</td>
<td align="right">11,545</td>
<td align="right">5.8%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,480</td>
<td align="right">3.3%</td>
<td align="right">6,520</td>
<td align="right">3.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">37,386</td>
<td align="right">19.0%</td>
<td align="right">37,186</td>
<td align="right">18.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,298</td>
<td align="right">5.2%</td>
<td align="right">10,283</td>
<td align="right">5.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,960</td>
<td align="right">53.2%</td>
<td align="right">104,960</td>
<td align="right">53.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,100</td>
<td align="right">2.6%</td>
<td align="right">5,100</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,840</td>
<td align="right">1.9%</td>
<td align="right">3,840</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,720</td>
<td align="right">0.9%</td>
<td align="right">1,720</td>
<td align="right">0.9%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,088,898,012</td>
<td align="right">91.3%</td>
<td align="right">16,126,366,257</td>
<td align="right">91.3%</td>
<td align="right">0.2%</td>
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
<td align="right">1,518,610,069</td>
<td align="right">8.6%</td>
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
<td align="right">420,448,428</td>
<td align="right">2.4%</td>
<td align="right">420,446,368</td>
<td align="right">2.4%</td>
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
<td align="left">Failure</td>
<td align="right">971,873</td>
<td align="right">10.2%</td>
<td align="right">971,016</td>
<td align="right">10.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,543,205</td>
<td align="right">89.8%</td>
<td align="right">8,547,047</td>
<td align="right">89.8%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">5,562</td>
<td align="right">0.6%</td>
<td align="right">5,708</td>
<td align="right">0.6%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,400</td>
<td align="right">1.5%</td>
<td align="right">14,340</td>
<td align="right">1.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,880</td>
<td align="right">2.8%</td>
<td align="right">26,780</td>
<td align="right">2.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,380</td>
<td align="right">0.6%</td>
<td align="right">5,400</td>
<td align="right">0.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">102,053</td>
<td align="right">10.5%</td>
<td align="right">101,688</td>
<td align="right">10.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,601</td>
<td align="right">9.0%</td>
<td align="right">87,890</td>
<td align="right">9.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.3%</td>
<td align="right">12,200</td>
<td align="right">1.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">263,056</td>
<td align="right">27.1%</td>
<td align="right">262,470</td>
<td align="right">27.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,340</td>
<td align="right">2.1%</td>
<td align="right">20,320</td>
<td align="right">2.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,751</td>
<td align="right">1.8%</td>
<td align="right">17,734</td>
<td align="right">1.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">156,174</td>
<td align="right">16.1%</td>
<td align="right">156,077</td>
<td align="right">16.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">75,346</td>
<td align="right">7.8%</td>
<td align="right">75,330</td>
<td align="right">7.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">164,770</td>
<td align="right">17.0%</td>
<td align="right">164,759</td>
<td align="right">17.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,300</td>
<td align="right">1.6%</td>
<td align="right">15,300</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,840</td>
<td align="right">0.3%</td>
<td align="right">2,840</td>
<td align="right">0.3%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">437,526</td>
<td align="right">0.0%</td>
<td align="right">447,747</td>
<td align="right">0.0%</td>
<td align="right">2.3%</td>
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
<td align="right">11,480</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
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
<td align="right">5,867,048,988</td>
<td align="right">99.6%</td>
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
<td align="right">20,333,083</td>
<td align="right">0.3%</td>
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
<td align="right">462,642</td>
<td align="right">100.0%</td>
<td align="right">465,569</td>
<td align="right">100.0%</td>
<td align="right">0.6%</td>
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
<td align="right">83,164,843</td>
<td align="right">100.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">7,508</td>
<td align="right">0.0%</td>
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
<td align="right">7,420</td>
<td align="right">100.0%</td>
<td align="right">7,460</td>
<td align="right">100.0%</td>
<td align="right">0.5%</td>
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
<td align="right">173,284,834</td>
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
<td align="right">786,189,895</td>
<td align="right">81.9%</td>
<td align="right">786,189,901</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,724,882,766</td>
<td align="right">93.4%</td>
<td align="right">2,736,887,005</td>
<td align="right">93.4%</td>
<td align="right">0.4%</td>
</tr>
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
<td align="right">139,464,877</td>
<td align="right">4.8%</td>
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
<td align="right">190,494,111</td>
<td align="right">6.5%</td>
<td align="right">190,481,150</td>
<td align="right">6.5%</td>
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
<td align="right">91,968</td>
<td align="right">3.3%</td>
<td align="right">91,868</td>
<td align="right">3.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,727,284</td>
<td align="right">96.7%</td>
<td align="right">2,729,286</td>
<td align="right">96.7%</td>
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
<td align="left">property</td>
<td align="right">2,860</td>
<td align="right">3.1%</td>
<td align="right">2,760</td>
<td align="right">3.0%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,780</td>
<td align="right">5.2%</td>
<td align="right">4,840</td>
<td align="right">5.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,940</td>
<td align="right">5.4%</td>
<td align="right">4,920</td>
<td align="right">5.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">32,220</td>
<td align="right">35.0%</td>
<td align="right">32,180</td>
<td align="right">35.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,960</td>
<td align="right">15.2%</td>
<td align="right">13,960</td>
<td align="right">15.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,728</td>
<td align="right">10.6%</td>
<td align="right">9,728</td>
<td align="right">10.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,760</td>
<td align="right">9.5%</td>
<td align="right">8,760</td>
<td align="right">9.5%</td>
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
<td align="right">6.9%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">877,138,730</td>
<td align="right">79.1%</td>
<td align="right">876,590,389</td>
<td align="right">79.1%</td>
<td align="right">-0.1%</td>
</tr>
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
<td align="right">232,042,530</td>
<td align="right">20.9%</td>
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
<td align="left">Success</td>
<td align="right">12,901</td>
<td align="right">11.4%</td>
<td align="right">12,927</td>
<td align="right">11.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">99,903</td>
<td align="right">88.6%</td>
<td align="right">99,882</td>
<td align="right">88.5%</td>
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
<td align="right">43,420</td>
<td align="right">43.5%</td>
<td align="right">43,400</td>
<td align="right">43.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,523</td>
<td align="right">7.5%</td>
<td align="right">7,521</td>
<td align="right">7.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">39,660</td>
<td align="right">39.7%</td>
<td align="right">39,661</td>
<td align="right">39.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">6.5%</td>
<td align="right">6,480</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,480</td>
<td align="right">1.5%</td>
<td align="right">1,480</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,340</td>
<td align="right">1.3%</td>
<td align="right">1,340</td>
<td align="right">1.3%</td>
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
<td align="right">248,974,140</td>
<td align="right">3.9%</td>
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
<td align="right">55,396,167</td>
<td align="right">0.9%</td>
<td align="right">55,515,770</td>
<td align="right">0.9%</td>
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
<td align="right">6,101,618,665</td>
<td align="right">96.1%</td>
<td align="right">6,107,215,447</td>
<td align="right">96.1%</td>
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
<td align="right">1,238,313</td>
<td align="right">77.6%</td>
<td align="right">1,241,305</td>
<td align="right">77.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">356,514</td>
<td align="right">22.4%</td>
<td align="right">357,267</td>
<td align="right">22.3%</td>
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
<td align="left">bytes</td>
<td align="right">13,248</td>
<td align="right">3.7%</td>
<td align="right">13,904</td>
<td align="right">3.9%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,158</td>
<td align="right">3.7%</td>
<td align="right">13,380</td>
<td align="right">3.7%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">55,303</td>
<td align="right">15.5%</td>
<td align="right">55,220</td>
<td align="right">15.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,020</td>
<td align="right">4.2%</td>
<td align="right">15,040</td>
<td align="right">4.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,136</td>
<td align="right">1.4%</td>
<td align="right">5,131</td>
<td align="right">1.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">35,066</td>
<td align="right">9.8%</td>
<td align="right">35,032</td>
<td align="right">9.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,178</td>
<td align="right">22.8%</td>
<td align="right">81,145</td>
<td align="right">22.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">135,485</td>
<td align="right">38.0%</td>
<td align="right">135,495</td>
<td align="right">37.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.4%</td>
<td align="right">1,460</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.3%</td>
<td align="right">1,040</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,558,579,012</td>
<td align="right">100.0%</td>
<td align="right">1,564,585,187</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
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
<td align="right">194,594</td>
<td align="right">0.0%</td>
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
<td align="right">30,056</td>
<td align="right">94.2%</td>
<td align="right">30,488</td>
<td align="right">94.3%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,855</td>
<td align="right">5.8%</td>
<td align="right">1,858</td>
<td align="right">5.7%</td>
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
<td align="left">sequence</td>
<td align="right">1,215</td>
<td align="right">65.5%</td>
<td align="right">1,218</td>
<td align="right">65.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">20.5%</td>
<td align="right">380</td>
<td align="right">20.5%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">42,700,996,207</td>
<td align="right">34.9%</td>
<td align="right">42,815,908,199</td>
<td align="right">34.9%</td>
<td align="right">0.3%</td>
</tr>
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
<td align="right">11,751,856,087</td>
<td align="right">9.6%</td>
<td align="right">0.2%</td>
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
<td align="right">67,153,599,119</td>
<td align="right">54.8%</td>
<td align="right">0.2%</td>
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
<td align="right">915,848,128</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
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
<td align="right">208,241,255</td>
<td align="right">4.1%</td>
<td align="right">209,390,166</td>
<td align="right">4.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">248,297,855</td>
<td align="right">4.9%</td>
<td align="right">248,974,140</td>
<td align="right">5.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">483,702,471</td>
<td align="right">9.6%</td>
<td align="right">484,781,901</td>
<td align="right">9.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,521,471,766</td>
<td align="right">30.3%</td>
<td align="right">1,518,610,069</td>
<td align="right">30.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">743,940,157</td>
<td align="right">14.8%</td>
<td align="right">744,732,482</td>
<td align="right">14.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">436,966,137</td>
<td align="right">8.7%</td>
<td align="right">437,085,757</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">662,414,532</td>
<td align="right">13.2%</td>
<td align="right">662,562,162</td>
<td align="right">13.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">190,494,111</td>
<td align="right">3.8%</td>
<td align="right">190,481,150</td>
<td align="right">3.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,045,908</td>
<td align="right">4.6%</td>
<td align="right">232,042,530</td>
<td align="right">4.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,918</td>
<td align="right">3.5%</td>
<td align="right">173,284,834</td>
<td align="right">3.4%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">98,363,888</td>
<td align="right">9.9%</td>
<td align="right">98,333,645</td>
<td align="right">9.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">125,994,724</td>
<td align="right">12.7%</td>
<td align="right">125,993,229</td>
<td align="right">12.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,365,644</td>
<td align="right">2.7%</td>
<td align="right">26,365,924</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">114,241,500</td>
<td align="right">11.5%</td>
<td align="right">114,242,260</td>
<td align="right">11.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,557</td>
<td align="right">2.8%</td>
<td align="right">27,496,694</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,897,849</td>
<td align="right">7.8%</td>
<td align="right">77,897,689</td>
<td align="right">7.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,897,849</td>
<td align="right">7.8%</td>
<td align="right">77,897,689</td>
<td align="right">7.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">172,482,356</td>
<td align="right">17.4%</td>
<td align="right">172,482,597</td>
<td align="right">17.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">58,788,249</td>
<td align="right">5.9%</td>
<td align="right">58,788,322</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,549,218</td>
<td align="right">3.6%</td>
<td align="right">35,549,218</td>
<td align="right">3.6%</td>
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
<td align="left">Frame objects created</td>
<td align="right">84,399,009</td>
<td align="right">1.0%</td>
<td align="right">85,384,157</td>
<td align="right">1.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">28,760</td>
<td align="right">0.0%</td>
<td align="right">29,020</td>
<td align="right">0.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,063,941,857</td>
<td align="right">69.6%</td>
<td align="right">6,076,310,670</td>
<td align="right">69.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,953,938,790</td>
<td align="right">79.8%</td>
<td align="right">6,966,273,733</td>
<td align="right">79.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">550,027,773</td>
<td align="right">6.3%</td>
<td align="right">550,432,640</td>
<td align="right">6.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">348,456,095</td>
<td align="right">4.0%</td>
<td align="right">348,701,475</td>
<td align="right">4.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,783,960,837</td>
<td align="right">20.5%</td>
<td align="right">1,784,832,677</td>
<td align="right">20.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,788,407,277</td>
<td align="right">20.5%</td>
<td align="right">1,789,279,417</td>
<td align="right">20.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,648,971,591</td>
<td align="right">30.4%</td>
<td align="right">2,649,874,362</td>
<td align="right">30.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,648,971,591</td>
<td align="right">30.4%</td>
<td align="right">2,649,874,362</td>
<td align="right">30.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,564,314</td>
<td align="right">9.9%</td>
<td align="right">860,594,945</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,015,392</td>
<td align="right">0.4%</td>
<td align="right">31,014,373</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,417,680</td>
<td align="right">0.1%</td>
<td align="right">4,417,720</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,363</td>
<td align="right">2.0%</td>
<td align="right">175,480,082</td>
<td align="right">2.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">56,796,739</td>
<td align="right"></td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">79,081,333</td>
<td align="right"></td>
<td align="right">63,022,836</td>
<td align="right"></td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">10,323,160</td>
<td align="right"></td>
<td align="right">9,432,877</td>
<td align="right"></td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">14,848,257</td>
<td align="right">0.1%</td>
<td align="right">15,211,128</td>
<td align="right">0.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">94,075,944</td>
<td align="right">0.4%</td>
<td align="right">92,998,426</td>
<td align="right">0.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,218,666,684</td>
<td align="right"></td>
<td align="right">3,232,627,017</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">53,443,966,322</td>
<td align="right">53,443,966,322 / 0 !!</td>
<td align="right">53,590,747,851</td>
<td align="right">53,590,747,851 / 0 !!</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,714,344,738</td>
<td align="right">55.2%</td>
<td align="right">12,745,704,756</td>
<td align="right">55.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,823,268,939</td>
<td align="right">55.7%</td>
<td align="right">12,853,914,310</td>
<td align="right">55.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">72,170,012,760</td>
<td align="right">72,170,012,760 / 0 !!</td>
<td align="right">72,336,613,458</td>
<td align="right">72,336,613,458 / 0 !!</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,527,517,116</td>
<td align="right"></td>
<td align="right">13,558,288,696</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,208,044,347</td>
<td align="right"></td>
<td align="right">10,216,954,873</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,206,180,055</td>
<td align="right">44.3%</td>
<td align="right">10,215,081,471</td>
<td align="right">44.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">94,422,203,988</td>
<td align="right">94,422,203,988 / 0 !!</td>
<td align="right">94,493,289,275</td>
<td align="right">94,493,289,275 / 0 !!</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">90,331,766,661</td>
<td align="right">90,331,766,661 / 0 !!</td>
<td align="right">90,380,012,261</td>
<td align="right">90,380,012,261 / 0 !!</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,125,686</td>
<td align="right"></td>
<td align="right">162,175,549</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,569,681,437</td>
<td align="right"></td>
<td align="right">4,570,396,230</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,305,720</td>
<td align="right">2.0%</td>
<td align="right">3,305,820</td>
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
<td align="right">115,313,704</td>
<td align="right">19,165,005,488</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,733,144</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,993,212</td>
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
<td align="right">1,339</td>
<td align="right">0.1%</td>
<td align="right">1,325</td>
<td align="right">0.1%</td>
<td align="right">-1.0%</td>
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
<td align="right">6,322</td>
<td align="right">5.0%</td>
<td align="right">-0.5%</td>
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
<td align="right">12,665</td>
<td align="right">1.0%</td>
<td align="right">0.4%</td>
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
<td align="right">497,348</td>
<td align="right">40.6%</td>
<td align="right">0.3%</td>
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
<td align="right">50,424</td>
<td align="right">4.1%</td>
<td align="right">-0.2%</td>
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
<td align="right">125,723</td>
<td align="right">10.3%</td>
<td align="right">0.1%</td>
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
<td align="right">1,226,119</td>
<td align="right"></td>
<td align="right">0.1%</td>
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
<td align="right">1,100,396</td>
<td align="right">89.7%</td>
<td align="right">0.1%</td>
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
<td align="right">250,043,978,978</td>
<td align="right">3,260.4%</td>
<td align="right">0.1%</td>
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
<td align="right">7,669,023,813</td>
<td align="right"></td>
<td align="right">-0.0%</td>
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
<td align="right">1,720</td>
<td align="right">0.1%</td>
<td align="right">1,720</td>
<td align="right">0.1%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,443</td>
<td align="right">1.9%</td>
<td align="right">2,460</td>
<td align="right">2.0%</td>
<td align="right">0.7%</td>
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
<td align="right">125,723</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
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
<td align="right">110,896</td>
<td align="right">88.2%</td>
<td align="right">0.1%</td>
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
<td align="right">5,070</td>
<td align="right">4.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,470</td>
<td align="right">17.1%</td>
<td align="right">21,477</td>
<td align="right">17.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,360</td>
<td align="right">28.2%</td>
<td align="right">35,343</td>
<td align="right">28.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">30,757</td>
<td align="right">24.5%</td>
<td align="right">31,150</td>
<td align="right">24.8%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21,361</td>
<td align="right">17.0%</td>
<td align="right">21,260</td>
<td align="right">16.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,630</td>
<td align="right">7.7%</td>
<td align="right">9,603</td>
<td align="right">7.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,660</td>
<td align="right">1.3%</td>
<td align="right">1,660</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
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
<td align="right">3,990</td>
<td align="right">3.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">14,806</td>
<td align="right">11.8%</td>
<td align="right">14,734</td>
<td align="right">11.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">25,289</td>
<td align="right">20.1%</td>
<td align="right">25,258</td>
<td align="right">20.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">36,375</td>
<td align="right">29.0%</td>
<td align="right">36,520</td>
<td align="right">29.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">18,534</td>
<td align="right">14.8%</td>
<td align="right">18,673</td>
<td align="right">14.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,787</td>
<td align="right">7.0%</td>
<td align="right">8,761</td>
<td align="right">7.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,600</td>
<td align="right">2.1%</td>
<td align="right">2,580</td>
<td align="right">2.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">380</td>
<td align="right">0.3%</td>
<td align="right">380</td>
<td align="right">0.3%</td>
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
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,966,880</td>
<td align="right">2,893,100</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,227,270</td>
<td align="right">10,119,161</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,705,220</td>
<td align="right">81,453,700</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,398,392</td>
<td align="right">96,216,451</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,642,252</td>
<td align="right">96,460,311</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">296,727,179</td>
<td align="right">299,020,165</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">970,228,623</td>
<td align="right">977,588,315</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">121,960,369</td>
<td align="right">122,859,994</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,059,545,388</td>
<td align="right">1,052,718,226</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">192,460,192</td>
<td align="right">193,681,601</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,092,184</td>
<td align="right">35,273,078</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">76,107,214</td>
<td align="right">75,720,459</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">553,848,296</td>
<td align="right">556,537,776</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">113,123,751</td>
<td align="right">112,589,435</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,475,754</td>
<td align="right">161,224,134</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,550,540</td>
<td align="right">188,408,420</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">270,904,974</td>
<td align="right">271,962,398</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,597,902</td>
<td align="right">89,936,167</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,193,950</td>
<td align="right">134,690,032</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,193,950</td>
<td align="right">134,690,032</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">338,015,782</td>
<td align="right">339,018,655</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">834,093,814</td>
<td align="right">836,537,017</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,131,155,755</td>
<td align="right">1,128,014,145</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,933,261</td>
<td align="right">229,311,962</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,583,106</td>
<td align="right">11,552,158</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,583,106</td>
<td align="right">11,552,158</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">136,726,362</td>
<td align="right">137,086,605</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,575,479,007</td>
<td align="right">1,579,620,030</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">923,767,825</td>
<td align="right">925,878,405</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">140,079,385</td>
<td align="right">140,392,377</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,383,640,585</td>
<td align="right">1,386,676,793</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">562,697,102</td>
<td align="right">563,875,477</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">860,627,259</td>
<td align="right">862,376,614</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,488,954,558</td>
<td align="right">1,491,838,565</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">940,130,182</td>
<td align="right">941,937,930</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">149,609,060</td>
<td align="right">149,894,059</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">658,513,087</td>
<td align="right">659,733,843</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">800,652,699</td>
<td align="right">799,220,465</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,430,760,611</td>
<td align="right">3,436,543,147</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">905,121,013</td>
<td align="right">906,592,016</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,683,480</td>
<td align="right">205,012,640</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,700,474</td>
<td align="right">91,558,037</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">126,341,149</td>
<td align="right">126,535,428</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">173,349,135</td>
<td align="right">173,092,247</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,046,179,304</td>
<td align="right">1,047,682,010</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">269,583,187</td>
<td align="right">269,962,745</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,325,176,387</td>
<td align="right">2,328,449,258</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">270,810,447</td>
<td align="right">271,190,005</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,098,625,361</td>
<td align="right">1,100,146,134</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,164,428,041</td>
<td align="right">2,167,407,884</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,032,829,215</td>
<td align="right">3,036,783,218</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,738,779,346</td>
<td align="right">3,743,608,522</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,404,384,390</td>
<td align="right">2,407,262,039</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,430,557,650</td>
<td align="right">2,433,435,299</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">198,398,358</td>
<td align="right">198,175,244</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">28,421,138</td>
<td align="right">28,389,503</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,508,803,479</td>
<td align="right">2,511,575,669</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,375,688</td>
<td align="right">78,461,173</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">104,757,000</td>
<td align="right">104,647,220</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">233,813,802</td>
<td align="right">234,036,363</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,619,566,649</td>
<td align="right">3,622,925,169</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,333,213</td>
<td align="right">93,418,697</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">972,409,134</td>
<td align="right">971,524,039</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,301,801,085</td>
<td align="right">1,300,616,596</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,189,392,105</td>
<td align="right">1,188,317,696</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,321,667,965</td>
<td align="right">1,320,483,136</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,085,253,964</td>
<td align="right">2,087,123,137</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,327,853</td>
<td align="right">96,413,339</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,419,034,042</td>
<td align="right">1,420,270,933</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,982,225,488</td>
<td align="right">17,997,011,522</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,152,807,838</td>
<td align="right">1,153,745,550</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,372,390,956</td>
<td align="right">3,375,105,705</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">15,651,341,300</td>
<td align="right">15,663,856,826</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">30,574,602</td>
<td align="right">30,596,524</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,790,016,836</td>
<td align="right">1,791,243,083</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">7,012,387,742</td>
<td align="right">7,007,701,940</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,826,009,167</td>
<td align="right">6,830,543,211</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,257,196,621</td>
<td align="right">6,261,093,055</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,578,576,329</td>
<td align="right">6,582,668,197</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">435,886,258</td>
<td align="right">436,145,231</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">316,309,046</td>
<td align="right">316,493,273</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">650,437,511</td>
<td align="right">650,803,550</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,027,049,917</td>
<td align="right">1,026,480,200</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">702,590,194</td>
<td align="right">702,954,088</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,819,330,275</td>
<td align="right">4,821,764,825</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">514,728,318</td>
<td align="right">514,987,231</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,183,972,898</td>
<td align="right">13,190,544,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,963,316,775</td>
<td align="right">1,964,286,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,611,491,440</td>
<td align="right">1,612,285,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,024,764,791</td>
<td align="right">2,025,754,291</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,688,898,382</td>
<td align="right">4,691,132,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">894,002,384</td>
<td align="right">893,584,058</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,672,545,371</td>
<td align="right">7,669,023,813</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,280,392,111</td>
<td align="right">7,283,611,644</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">216,495,378</td>
<td align="right">216,588,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,118,642,883</td>
<td align="right">6,121,263,457</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">219,024,135</td>
<td align="right">219,117,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,681,085,960</td>
<td align="right">1,681,795,501</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">777,595,743</td>
<td align="right">777,919,152</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,275,944,635</td>
<td align="right">4,277,703,292</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,158,181</td>
<td align="right">777,838,629</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,695,501</td>
<td align="right">778,375,949</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,323,630,944</td>
<td align="right">1,324,129,757</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,682,494,122</td>
<td align="right">1,683,104,599</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,816,325,714</td>
<td align="right">1,815,718,372</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">992,079,740</td>
<td align="right">992,410,290</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,326,044</td>
<td align="right">2,325,304</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,517,065</td>
<td align="right">2,516,297</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,598,528</td>
<td align="right">731,387,515</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">386,735,590</td>
<td align="right">386,843,178</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">890,076,806</td>
<td align="right">890,313,041</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,280,053,336</td>
<td align="right">1,280,358,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,921,070</td>
<td align="right">4,922,225</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,020,029,476</td>
<td align="right">2,020,445,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">221,352,540</td>
<td align="right">221,397,741</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">394,099,394</td>
<td align="right">394,018,924</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">25,201,696</td>
<td align="right">25,206,064</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,257,745,764</td>
<td align="right">2,257,436,694</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">406,359,417</td>
<td align="right">406,307,732</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">662,715,657</td>
<td align="right">662,796,658</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,996,839,771</td>
<td align="right">1,996,605,691</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,413,730,611</td>
<td align="right">4,414,247,647</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,883,887,175</td>
<td align="right">1,883,704,517</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,822,630</td>
<td align="right">31,825,310</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">462,455</td>
<td align="right">462,492</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">64,511,956</td>
<td align="right">64,516,512</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,744,534,634</td>
<td align="right">2,744,726,883</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,318,061,660</td>
<td align="right">2,317,929,274</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,659,960</td>
<td align="right">5,659,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,253,397,167</td>
<td align="right">1,253,331,297</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,345,927,844</td>
<td align="right">1,345,991,242</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,862,100</td>
<td align="right">6,861,780</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">395,106,603</td>
<td align="right">395,088,629</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">48,468,106</td>
<td align="right">48,466,105</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,853,882,628</td>
<td align="right">1,853,954,235</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">81,529,540</td>
<td align="right">81,532,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">81,660,820</td>
<td align="right">81,663,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">164,118,568</td>
<td align="right">164,123,597</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,621,056,398</td>
<td align="right">3,620,958,365</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,177,300</td>
<td align="right">8,177,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">274,503,937</td>
<td align="right">274,510,164</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,402,252</td>
<td align="right">32,402,942</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">266,224,195</td>
<td align="right">266,229,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">10,050,940</td>
<td align="right">10,051,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">85,735,820</td>
<td align="right">85,737,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">11,627,720</td>
<td align="right">11,627,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">904,464,212</td>
<td align="right">904,450,769</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,144,549,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,671,620</td>
<td align="right">3,671,580</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,164,660,446</td>
<td align="right">3,164,694,005</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">60,988,920</td>
<td align="right">60,989,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,840,870,976</td>
<td align="right">2,840,897,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,688,940,366</td>
<td align="right">9,689,029,678</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">246,277,913</td>
<td align="right">246,279,512</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,825,993,772</td>
<td align="right">1,826,005,273</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,681,948</td>
<td align="right">10,681,993</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,831,680</td>
<td align="right">61,831,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">643,774,743</td>
<td align="right">643,776,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">457,490,993</td>
<td align="right">457,492,014</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">239,755,007</td>
<td align="right">239,754,659</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">162,876,000</td>
<td align="right">162,875,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">3,628,059</td>
<td align="right">3,628,057</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">395,091,201</td>
<td align="right">395,091,413</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">66,421,885</td>
<td align="right">66,421,862</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,230,107</td>
<td align="right">97,230,077</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,187,447</td>
<td align="right">98,187,417</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">67,773,180</td>
<td align="right">67,773,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">321,308,144</td>
<td align="right">321,308,094</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,682,764</td>
<td align="right">68,682,758</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">244,676,040</td>
<td align="right">244,676,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,013,560</td>
<td align="right">533,013,520</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,713,807</td>
<td align="right">90,713,801</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">47,971,806</td>
<td align="right">47,971,809</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">101,766,726</td>
<td align="right">101,766,729</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">102,572,239</td>
<td align="right">102,572,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,187</td>
<td align="right">645,067,181</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,952</td>
<td align="right">384,637,949</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">588,457,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">510,187,700</td>
<td align="right">510,187,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">218,973,940</td>
<td align="right">218,973,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,965,460</td>
<td align="right">154,965,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,990,580</td>
<td align="right">144,990,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">59,644,340</td>
<td align="right">59,644,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">53,794,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">46,348,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,717,580</td>
<td align="right">25,717,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,697,060</td>
<td align="right">12,697,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">6,583,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,931,060</td>
<td align="right">4,931,060</td>
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
<td align="right">4,648,680</td>
<td align="right">4,648,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,065,920</td>
<td align="right">3,065,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,025,020</td>
<td align="right">3,025,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">2,714,740</td>
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
<td align="right">821,720</td>
<td align="right">821,720</td>
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
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">39,840</td>
<td align="right">39,840</td>
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
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">7,356,980</td>
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
<td align="right">1,180</td>
<td align="right">1,200</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,595</td>
<td align="right">6,690</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,081</td>
<td align="right">6,140</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,621</td>
<td align="right">3,640</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">486,354</td>
<td align="right">486,641</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,457</td>
<td align="right">2,458</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,650</td>
<td align="right">44,650</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">33,340</td>
<td align="right">33,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">30,480</td>
<td align="right">30,480</td>
<td align="right">0.0%</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">620</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">320</td>
<td align="right">320</td>
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
<td align="right">1,101</td>
<td align="right">-0.4%</td>
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
<td align="right">1,101</td>
<td align="right">-0.4%</td>
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
<td align="right">1,800</td>
<td align="right">1.1%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
