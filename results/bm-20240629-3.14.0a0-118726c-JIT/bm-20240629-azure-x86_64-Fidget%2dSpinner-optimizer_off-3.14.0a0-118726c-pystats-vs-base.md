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
<td align="right">3,818,536</td>
<td align="right">2,492,798</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">4,716,217</td>
<td align="right">3,959,990</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">146,457,380</td>
<td align="right">129,104,684</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">348,254,586</td>
<td align="right">310,292,880</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,347,683</td>
<td align="right">7,684,393</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,375,499</td>
<td align="right">9,675,056</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">42,432,486</td>
<td align="right">39,957,877</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,259,748,115</td>
<td align="right">1,195,448,858</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,410,497,068</td>
<td align="right">1,352,238,699</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">114,821,636</td>
<td align="right">110,832,441</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">318,101,225</td>
<td align="right">307,355,222</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,812,694</td>
<td align="right">42,152,150</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,247,936</td>
<td align="right">60,326,856</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,399,480,425</td>
<td align="right">2,329,104,735</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">773,874,979</td>
<td align="right">751,206,379</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,298,028</td>
<td align="right">2,236,891</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">140,540,314</td>
<td align="right">137,022,066</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">385,615,118</td>
<td align="right">376,143,763</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,240,499,998</td>
<td align="right">4,136,962,632</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,542,059</td>
<td align="right">46,614,177</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">201,773,379</td>
<td align="right">198,002,607</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,017,148,309</td>
<td align="right">999,417,831</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">108,592,765</td>
<td align="right">106,751,452</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">452,620,861</td>
<td align="right">446,161,520</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">162,004,970</td>
<td align="right">159,757,651</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,610,733,612</td>
<td align="right">21,320,312,763</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,850,250</td>
<td align="right">53,130,764</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">366,808,849</td>
<td align="right">361,908,119</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,999,030,496</td>
<td align="right">5,919,098,443</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,541,558</td>
<td align="right">122,951,305</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">942,096,405</td>
<td align="right">931,268,777</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">195,543,295</td>
<td align="right">193,334,362</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">294,704,735</td>
<td align="right">291,566,370</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">76,218,460</td>
<td align="right">75,411,503</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,568,221,088</td>
<td align="right">1,552,413,644</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">908,129,089</td>
<td align="right">899,217,030</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">219,460</td>
<td align="right">217,415</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">100,325,489</td>
<td align="right">99,413,954</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">481,536,053</td>
<td align="right">477,194,975</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">636,678,791</td>
<td align="right">630,972,634</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,870,985,633</td>
<td align="right">1,854,240,454</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,294,587,174</td>
<td align="right">3,265,372,667</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">334,209,892</td>
<td align="right">331,464,130</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,818,303,195</td>
<td align="right">2,795,413,596</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,672,096,534</td>
<td align="right">5,626,356,820</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,450,878,043</td>
<td align="right">2,432,118,268</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">272,966,441</td>
<td align="right">270,990,146</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,222,784,170</td>
<td align="right">6,178,495,079</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">828,616,432</td>
<td align="right">823,089,127</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,109,544,117</td>
<td align="right">1,102,772,965</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">210,848,327</td>
<td align="right">209,565,296</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">230,580,785</td>
<td align="right">229,233,350</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">331,679,861</td>
<td align="right">329,774,067</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">298,244,540</td>
<td align="right">296,592,394</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">79,270,465</td>
<td align="right">78,835,579</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,763,239</td>
<td align="right">66,401,470</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,100,779</td>
<td align="right">47,844,121</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">739,563,939</td>
<td align="right">735,681,280</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">87,574,578</td>
<td align="right">87,119,645</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,097,995,249</td>
<td align="right">4,077,404,498</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">276,486,545</td>
<td align="right">275,142,682</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">24,142,317</td>
<td align="right">24,031,157</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">666,477,559</td>
<td align="right">663,423,128</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">198,591,654</td>
<td align="right">197,707,202</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">386,013,111</td>
<td align="right">384,358,849</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,526,244,301</td>
<td align="right">3,511,271,024</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">118,711,507</td>
<td align="right">118,222,996</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">59,237,150</td>
<td align="right">58,994,206</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,488,640,985</td>
<td align="right">5,466,619,051</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">194,484,326</td>
<td align="right">193,845,348</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">135,755,200</td>
<td align="right">135,309,440</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">205,835,565</td>
<td align="right">205,160,024</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,714,481</td>
<td align="right">71,485,161</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">142,537,682</td>
<td align="right">142,085,062</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">378,237,902</td>
<td align="right">377,042,752</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,137,024,776</td>
<td align="right">1,133,455,703</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">485,240</td>
<td align="right">483,720</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,184,346</td>
<td align="right">91,905,837</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">404,081,028</td>
<td align="right">405,183,740</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">679,767,623</td>
<td align="right">677,956,951</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">677,128,929</td>
<td align="right">675,405,626</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">214,581,651</td>
<td align="right">214,048,142</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">556,304,549</td>
<td align="right">554,922,245</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,165,260</td>
<td align="right">91,941,500</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,447,100</td>
<td align="right">94,223,340</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">803,580,861</td>
<td align="right">801,891,384</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,401,816</td>
<td align="right">4,393,190</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,428,960</td>
<td align="right">17,397,162</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,374,165,308</td>
<td align="right">4,380,297,704</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,290,416,174</td>
<td align="right">1,288,664,076</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">408,983,513</td>
<td align="right">408,446,223</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,296,900</td>
<td align="right">216,014,360</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">228,038,357</td>
<td align="right">227,781,739</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">222,791</td>
<td align="right">223,033</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">485,045,583</td>
<td align="right">484,551,859</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,104,199,664</td>
<td align="right">4,108,238,434</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">56,479,695</td>
<td align="right">56,429,299</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">21,152,968</td>
<td align="right">21,136,024</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,805,177</td>
<td align="right">81,743,984</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">486,364,653</td>
<td align="right">486,012,013</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">431,612,272</td>
<td align="right">431,300,889</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,660,821</td>
<td align="right">101,588,294</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,603,435,324</td>
<td align="right">1,602,298,564</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">421,589,157</td>
<td align="right">421,295,234</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">49,309,252</td>
<td align="right">49,279,123</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,588</td>
<td align="right">687,983</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,371,454,898</td>
<td align="right">1,370,717,233</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">20,421,572</td>
<td align="right">20,413,025</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,263,790</td>
<td align="right">274,155,922</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">901,752,544</td>
<td align="right">901,440,518</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,890</td>
<td align="right">14,885</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">791,277,034</td>
<td align="right">791,016,354</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">166,835,490</td>
<td align="right">166,783,636</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,657,050</td>
<td align="right">9,659,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,640,865</td>
<td align="right">3,639,880</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,235,329</td>
<td align="right">9,237,676</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,451,559</td>
<td align="right">82,431,287</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,611</td>
<td align="right">1,874,017</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">138,065,600</td>
<td align="right">138,041,210</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,961,742</td>
<td align="right">10,959,932</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,692,538</td>
<td align="right">20,695,843</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,644,990,163</td>
<td align="right">2,644,593,779</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,151,004</td>
<td align="right">21,154,163</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,158,764</td>
<td align="right">21,161,922</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">54,270,912</td>
<td align="right">54,263,256</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">30,800,290</td>
<td align="right">30,796,294</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67,991,255</td>
<td align="right">67,982,509</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,795,358</td>
<td align="right">72,786,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">385,222,073</td>
<td align="right">385,185,138</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">35,530,742</td>
<td align="right">35,527,662</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,966,910</td>
<td align="right">402,936,989</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,808,875</td>
<td align="right">1,808,947</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,409,708</td>
<td align="right">1,047,374,245</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">199,226,930</td>
<td align="right">199,220,795</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,262,720</td>
<td align="right">83,264,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,950,686</td>
<td align="right">5,950,810</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,420</td>
<td align="right">173,423</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">81,682,578</td>
<td align="right">81,681,207</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,169,335</td>
<td align="right">232,165,915</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,345,122</td>
<td align="right">20,344,828</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,913,186</td>
<td align="right">149,915,288</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,569,470</td>
<td align="right">158,567,511</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,141,979</td>
<td align="right">91,142,658</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,368</td>
<td align="right">190,040,474</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,877,502</td>
<td align="right">9,877,445</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,911,303</td>
<td align="right">146,910,856</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">108,507,118</td>
<td align="right">108,507,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,906,248</td>
<td align="right">555,907,670</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">283,353,026</td>
<td align="right">283,353,581</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">173,188,457</td>
<td align="right">173,188,731</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,612,128</td>
<td align="right">46,612,112</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,338,387</td>
<td align="right">233,338,355</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">66,953,718</td>
<td align="right">66,953,721</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,220,538</td>
<td align="right">786,220,512</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,319,344</td>
<td align="right">173,319,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,641,564</td>
<td align="right">225,641,560</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,024,186</td>
<td align="right">402,024,180</td>
<td align="right">-0.0%</td>
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
<td align="left">CALL_STR_1</td>
<td align="right">31,808,661</td>
<td align="right">31,808,661</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">12,102,460</td>
<td align="right">12,102,460</td>
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
<td align="left">STORE_NAME</td>
<td align="right">657,680</td>
<td align="right">657,680</td>
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
<td align="left">SET_ADD</td>
<td align="right">46,620</td>
<td align="right">46,620</td>
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
<td align="right">436,764,156</td>
<td align="right">4.4%</td>
<td align="right">436,227,404</td>
<td align="right">4.4%</td>
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
<td align="right">9,428,308,240</td>
<td align="right">95.6%</td>
<td align="right">9,422,757,748</td>
<td align="right">95.6%</td>
<td align="right">-0.1%</td>
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
<td align="right">29,500,960</td>
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
<td align="right">1,122,561</td>
<td align="right">65.3%</td>
<td align="right">1,122,135</td>
<td align="right">65.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">597,716</td>
<td align="right">34.7%</td>
<td align="right">597,644</td>
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
<td align="left">and other</td>
<td align="right">1,909</td>
<td align="right">0.2%</td>
<td align="right">1,916</td>
<td align="right">0.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,562</td>
<td align="right">0.5%</td>
<td align="right">5,548</td>
<td align="right">0.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,886</td>
<td align="right">0.8%</td>
<td align="right">8,864</td>
<td align="right">0.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">13,619</td>
<td align="right">1.2%</td>
<td align="right">13,589</td>
<td align="right">1.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,408</td>
<td align="right">7.3%</td>
<td align="right">82,228</td>
<td align="right">7.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">22,650</td>
<td align="right">2.0%</td>
<td align="right">22,614</td>
<td align="right">2.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,034</td>
<td align="right">0.4%</td>
<td align="right">5,026</td>
<td align="right">0.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,266</td>
<td align="right">2.8%</td>
<td align="right">31,222</td>
<td align="right">2.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,332</td>
<td align="right">4.3%</td>
<td align="right">48,282</td>
<td align="right">4.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">48,662</td>
<td align="right">4.3%</td>
<td align="right">48,614</td>
<td align="right">4.3%</td>
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
<td align="left">rshift</td>
<td align="right">8,611</td>
<td align="right">0.8%</td>
<td align="right">8,608</td>
<td align="right">0.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,506</td>
<td align="right">0.9%</td>
<td align="right">10,504</td>
<td align="right">0.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,404</td>
<td align="right">2.9%</td>
<td align="right">32,399</td>
<td align="right">2.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,606</td>
<td align="right">69.6%</td>
<td align="right">781,617</td>
<td align="right">69.7%</td>
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
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
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
<td align="right">743,952,282</td>
<td align="right">10.8%</td>
<td align="right">740,070,784</td>
<td align="right">10.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,149,771,921</td>
<td align="right">89.2%</td>
<td align="right">6,135,875,953</td>
<td align="right">89.2%</td>
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
<td align="right">4,810,107</td>
<td align="right">0.1%</td>
<td align="right">4,809,965</td>
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
<td align="right">240,190</td>
<td align="right">56.9%</td>
<td align="right">238,900</td>
<td align="right">56.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,574</td>
<td align="right">43.1%</td>
<td align="right">181,561</td>
<td align="right">43.2%</td>
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
<td align="right">0.5%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">55,960</td>
<td align="right">23.3%</td>
<td align="right">54,960</td>
<td align="right">23.0%</td>
<td align="right">-1.8%</td>
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
<td align="left">buffer int</td>
<td align="right">30,499</td>
<td align="right">12.7%</td>
<td align="right">30,319</td>
<td align="right">12.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">110,425</td>
<td align="right">46.0%</td>
<td align="right">110,437</td>
<td align="right">46.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,500</td>
<td align="right">8.1%</td>
<td align="right">19,500</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">6.7%</td>
<td align="right">16,200</td>
<td align="right">6.8%</td>
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
<td align="right">181,621,002</td>
<td align="right">1.3%</td>
<td align="right">179,553,312</td>
<td align="right">1.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">662,551,305</td>
<td align="right">4.6%</td>
<td align="right">660,029,132</td>
<td align="right">4.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,665,436,711</td>
<td align="right">95.3%</td>
<td align="right">13,643,260,259</td>
<td align="right">95.4%</td>
<td align="right">-0.2%</td>
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
<td align="right">3,949,900</td>
<td align="right">96.0%</td>
<td align="right">3,910,825</td>
<td align="right">95.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">165,380</td>
<td align="right">4.0%</td>
<td align="right">165,214</td>
<td align="right">4.1%</td>
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
<td align="right">155,880</td>
<td align="right">94.3%</td>
<td align="right">155,714</td>
<td align="right">94.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">101,171,398</td>
<td align="right">1.6%</td>
<td align="right">100,251,379</td>
<td align="right">1.6%</td>
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
<td align="right">1,071,804</td>
<td align="right">0.0%</td>
<td align="right">1,062,572</td>
<td align="right">0.0%</td>
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
<td align="right">6,122,557,668</td>
<td align="right">98.4%</td>
<td align="right">6,105,934,006</td>
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
<td align="right">149,673</td>
<td align="right">66.3%</td>
<td align="right">149,115</td>
<td align="right">66.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">76,222</td>
<td align="right">33.7%</td>
<td align="right">76,032</td>
<td align="right">33.8%</td>
<td align="right">-0.2%</td>
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
<td align="right">840</td>
<td align="right">0.6%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.4%</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">42,513</td>
<td align="right">28.4%</td>
<td align="right">42,220</td>
<td align="right">28.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,186</td>
<td align="right">8.1%</td>
<td align="right">12,108</td>
<td align="right">8.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,423</td>
<td align="right">1.0%</td>
<td align="right">1,428</td>
<td align="right">1.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,980</td>
<td align="right">12.7%</td>
<td align="right">18,920</td>
<td align="right">12.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,667</td>
<td align="right">11.1%</td>
<td align="right">16,702</td>
<td align="right">11.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,376</td>
<td align="right">9.6%</td>
<td align="right">14,369</td>
<td align="right">9.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,068</td>
<td align="right">18.1%</td>
<td align="right">27,068</td>
<td align="right">18.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">10,680</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,620</td>
<td align="right">1.8%</td>
<td align="right">2,620</td>
<td align="right">1.8%</td>
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
<td align="right">208,206,956</td>
<td align="right">7.7%</td>
<td align="right">207,531,848</td>
<td align="right">7.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,489,594,665</td>
<td align="right">92.3%</td>
<td align="right">2,485,299,593</td>
<td align="right">92.3%</td>
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
<td align="right">113,729</td>
<td align="right">65.0%</td>
<td align="right">113,296</td>
<td align="right">65.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,120</td>
<td align="right">35.0%</td>
<td align="right">61,120</td>
<td align="right">35.0%</td>
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
<td align="left">tuple</td>
<td align="right">27,501</td>
<td align="right">24.2%</td>
<td align="right">27,259</td>
<td align="right">24.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">13,940</td>
<td align="right">12.3%</td>
<td align="right">13,820</td>
<td align="right">12.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,748</td>
<td align="right">13.8%</td>
<td align="right">15,677</td>
<td align="right">13.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">56,540</td>
<td align="right">49.7%</td>
<td align="right">56,540</td>
<td align="right">49.9%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,592,286</td>
<td align="right">0.3%</td>
<td align="right">2,550,311</td>
<td align="right">0.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">483,834,496</td>
<td align="right">46.9%</td>
<td align="right">479,453,884</td>
<td align="right">46.8%</td>
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
<td align="right">547,101,202</td>
<td align="right">53.1%</td>
<td align="right">543,893,364</td>
<td align="right">53.1%</td>
<td align="right">-0.6%</td>
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
<td align="right">96,662</td>
<td align="right">32.9%</td>
<td align="right">95,821</td>
<td align="right">32.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">197,181</td>
<td align="right">67.1%</td>
<td align="right">195,581</td>
<td align="right">67.1%</td>
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
<td align="left">reversed list</td>
<td align="right">4,060</td>
<td align="right">2.1%</td>
<td align="right">3,260</td>
<td align="right">1.7%</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,286</td>
<td align="right">5.7%</td>
<td align="right">11,010</td>
<td align="right">5.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">37,314</td>
<td align="right">18.9%</td>
<td align="right">36,807</td>
<td align="right">18.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">615</td>
<td align="right">0.3%</td>
<td align="right">619</td>
<td align="right">0.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,306</td>
<td align="right">5.2%</td>
<td align="right">10,285</td>
<td align="right">5.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,960</td>
<td align="right">53.2%</td>
<td align="right">104,960</td>
<td align="right">53.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,480</td>
<td align="right">3.3%</td>
<td align="right">6,480</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,300</td>
<td align="right">3.2%</td>
<td align="right">6,300</td>
<td align="right">3.2%</td>
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
<td align="left">dict values</td>
<td align="right">4,220</td>
<td align="right">2.1%</td>
<td align="right">4,220</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,840</td>
<td align="right">1.9%</td>
<td align="right">3,840</td>
<td align="right">2.0%</td>
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
<td align="right">419,363,364</td>
<td align="right">2.4%</td>
<td align="right">359,591,109</td>
<td align="right">2.0%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,519,412,256</td>
<td align="right">8.6%</td>
<td align="right">1,454,000,280</td>
<td align="right">8.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,087,023,176</td>
<td align="right">91.3%</td>
<td align="right">16,111,809,828</td>
<td align="right">91.7%</td>
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
<td align="right">320,000</td>
<td align="right">0.0%</td>
<td align="right">320,000</td>
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
<td align="right">8,522,886</td>
<td align="right">89.8%</td>
<td align="right">7,395,334</td>
<td align="right">88.4%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">972,339</td>
<td align="right">10.2%</td>
<td align="right">968,460</td>
<td align="right">11.6%</td>
<td align="right">-0.4%</td>
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
<td align="right">87,300</td>
<td align="right">9.0%</td>
<td align="right">86,012</td>
<td align="right">8.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">102,067</td>
<td align="right">10.5%</td>
<td align="right">101,231</td>
<td align="right">10.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">75,366</td>
<td align="right">7.8%</td>
<td align="right">74,840</td>
<td align="right">7.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,340</td>
<td align="right">2.1%</td>
<td align="right">20,220</td>
<td align="right">2.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,380</td>
<td align="right">1.5%</td>
<td align="right">14,300</td>
<td align="right">1.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">156,228</td>
<td align="right">16.1%</td>
<td align="right">155,721</td>
<td align="right">16.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,743</td>
<td align="right">1.8%</td>
<td align="right">17,713</td>
<td align="right">1.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">263,195</td>
<td align="right">27.1%</td>
<td align="right">262,871</td>
<td align="right">27.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,580</td>
<td align="right">0.6%</td>
<td align="right">5,574</td>
<td align="right">0.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">164,780</td>
<td align="right">16.9%</td>
<td align="right">164,618</td>
<td align="right">17.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,880</td>
<td align="right">2.8%</td>
<td align="right">26,880</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,840</td>
<td align="right">1.6%</td>
<td align="right">15,840</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.3%</td>
<td align="right">12,240</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,400</td>
<td align="right">0.6%</td>
<td align="right">5,400</td>
<td align="right">0.6%</td>
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
<td align="right">5,846,793,263</td>
<td align="right">99.6%</td>
<td align="right">5,806,000,177</td>
<td align="right">99.6%</td>
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
<td align="right">438,670</td>
<td align="right">0.0%</td>
<td align="right">437,642</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,320,950</td>
<td align="right">0.3%</td>
<td align="right">20,319,786</td>
<td align="right">0.3%</td>
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
<td align="right">462,842</td>
<td align="right">100.0%</td>
<td align="right">462,684</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,470</td>
<td align="right">0.0%</td>
<td align="right">7,464</td>
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
<td align="right">83,643,972</td>
<td align="right">100.0%</td>
<td align="right">83,582,851</td>
<td align="right">100.0%</td>
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
<td align="right">7,420</td>
<td align="right">100.0%</td>
<td align="right">7,421</td>
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
<td align="right">786,189,878</td>
<td align="right">81.9%</td>
<td align="right">786,189,852</td>
<td align="right">81.9%</td>
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
<td align="right">173,284,924</td>
<td align="right">18.1%</td>
<td align="right">173,284,920</td>
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
<td align="right">139,476,075</td>
<td align="right">4.8%</td>
<td align="right">90,186,227</td>
<td align="right">3.1%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">190,507,017</td>
<td align="right">6.5%</td>
<td align="right">141,428,049</td>
<td align="right">4.9%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,724,822,027</td>
<td align="right">93.4%</td>
<td align="right">2,725,367,469</td>
<td align="right">95.0%</td>
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
<td align="right">2,727,276</td>
<td align="right">96.7%</td>
<td align="right">1,797,294</td>
<td align="right">95.1%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">92,032</td>
<td align="right">3.3%</td>
<td align="right">91,648</td>
<td align="right">4.9%</td>
<td align="right">-0.4%</td>
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
<td align="right">2,720</td>
<td align="right">3.0%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,760</td>
<td align="right">9.5%</td>
<td align="right">8,600</td>
<td align="right">9.4%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,960</td>
<td align="right">15.2%</td>
<td align="right">13,880</td>
<td align="right">15.1%</td>
<td align="right">-0.6%</td>
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
<td align="left">not in keys</td>
<td align="right">6,320</td>
<td align="right">6.9%</td>
<td align="right">6,340</td>
<td align="right">6.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,732</td>
<td align="right">10.6%</td>
<td align="right">9,728</td>
<td align="right">10.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">32,280</td>
<td align="right">35.1%</td>
<td align="right">32,280</td>
<td align="right">35.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,480</td>
<td align="right">8.1%</td>
<td align="right">7,480</td>
<td align="right">8.2%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">877,085,203</td>
<td align="right">79.1%</td>
<td align="right">875,172,904</td>
<td align="right">79.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">232,059,362</td>
<td align="right">20.9%</td>
<td align="right">232,055,959</td>
<td align="right">21.0%</td>
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
<td align="right">12,908</td>
<td align="right">11.4%</td>
<td align="right">12,902</td>
<td align="right">11.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">99,965</td>
<td align="right">88.6%</td>
<td align="right">99,954</td>
<td align="right">88.6%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">7,525</td>
<td align="right">7.5%</td>
<td align="right">7,514</td>
<td align="right">7.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,420</td>
<td align="right">43.4%</td>
<td align="right">43,420</td>
<td align="right">43.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">39,720</td>
<td align="right">39.7%</td>
<td align="right">39,720</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,100,574,639</td>
<td align="right">96.1%</td>
<td align="right">6,315,029,816</td>
<td align="right">96.2%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">55,397,013</td>
<td align="right">0.9%</td>
<td align="right">55,041,415</td>
<td align="right">0.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">248,286,445</td>
<td align="right">3.9%</td>
<td align="right">247,298,874</td>
<td align="right">3.8%</td>
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
<td align="right">1,238,397</td>
<td align="right">77.6%</td>
<td align="right">1,231,650</td>
<td align="right">77.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">356,497</td>
<td align="right">22.4%</td>
<td align="right">356,239</td>
<td align="right">22.4%</td>
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
<td align="right">15,020</td>
<td align="right">4.2%</td>
<td align="right">14,900</td>
<td align="right">4.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,151</td>
<td align="right">1.4%</td>
<td align="right">5,130</td>
<td align="right">1.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,242</td>
<td align="right">3.7%</td>
<td align="right">13,201</td>
<td align="right">3.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">55,301</td>
<td align="right">15.5%</td>
<td align="right">55,199</td>
<td align="right">15.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">35,057</td>
<td align="right">9.8%</td>
<td align="right">35,074</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">135,478</td>
<td align="right">38.0%</td>
<td align="right">135,488</td>
<td align="right">38.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,168</td>
<td align="right">22.8%</td>
<td align="right">81,167</td>
<td align="right">22.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,160</td>
<td align="right">3.7%</td>
<td align="right">13,160</td>
<td align="right">3.7%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">193,938</td>
<td align="right">0.0%</td>
<td align="right">194,201</td>
<td align="right">0.0%</td>
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
<td align="right">1,558,858,253</td>
<td align="right">100.0%</td>
<td align="right">1,558,424,778</td>
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
<td align="right">1,849</td>
<td align="right">5.8%</td>
<td align="right">1,856</td>
<td align="right">5.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,084</td>
<td align="right">94.2%</td>
<td align="right">30,056</td>
<td align="right">94.2%</td>
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
<td align="left">sequence</td>
<td align="right">1,209</td>
<td align="right">65.4%</td>
<td align="right">1,216</td>
<td align="right">65.5%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">20.6%</td>
<td align="right">380</td>
<td align="right">20.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.1%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">914,751,577</td>
<td align="right">0.7%</td>
<td align="right">803,214,322</td>
<td align="right">0.7%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">42,717,879,717</td>
<td align="right">34.9%</td>
<td align="right">42,226,709,835</td>
<td align="right">34.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">67,016,218,752</td>
<td align="right">54.8%</td>
<td align="right">66,531,470,158</td>
<td align="right">54.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,717,373,644</td>
<td align="right">9.6%</td>
<td align="right">11,649,747,664</td>
<td align="right">9.6%</td>
<td align="right">-0.6%</td>
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
<td align="right">190,507,017</td>
<td align="right">3.8%</td>
<td align="right">141,428,049</td>
<td align="right">2.9%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,519,412,256</td>
<td align="right">30.3%</td>
<td align="right">1,454,000,280</td>
<td align="right">29.7%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">483,834,496</td>
<td align="right">9.6%</td>
<td align="right">479,453,884</td>
<td align="right">9.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">743,952,282</td>
<td align="right">14.8%</td>
<td align="right">740,070,784</td>
<td align="right">15.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">248,286,445</td>
<td align="right">4.9%</td>
<td align="right">247,298,874</td>
<td align="right">5.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">662,551,305</td>
<td align="right">13.2%</td>
<td align="right">660,029,132</td>
<td align="right">13.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">208,206,956</td>
<td align="right">4.1%</td>
<td align="right">207,531,848</td>
<td align="right">4.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">436,764,156</td>
<td align="right">8.7%</td>
<td align="right">436,227,404</td>
<td align="right">8.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,059,362</td>
<td align="right">4.6%</td>
<td align="right">232,055,959</td>
<td align="right">4.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,924</td>
<td align="right">3.5%</td>
<td align="right">173,284,920</td>
<td align="right">3.5%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">114,234,840</td>
<td align="right">11.5%</td>
<td align="right">64,968,220</td>
<td align="right">7.4%</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">125,734,992</td>
<td align="right">12.7%</td>
<td align="right">98,065,316</td>
<td align="right">11.1%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">172,061,255</td>
<td align="right">17.3%</td>
<td align="right">140,808,034</td>
<td align="right">16.0%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">98,379,072</td>
<td align="right">9.9%</td>
<td align="right">96,847,945</td>
<td align="right">11.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,365,363</td>
<td align="right">2.7%</td>
<td align="right">26,322,386</td>
<td align="right">3.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">58,784,490</td>
<td align="right">5.9%</td>
<td align="right">58,772,704</td>
<td align="right">6.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,369</td>
<td align="right">2.8%</td>
<td align="right">27,496,545</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,897,456</td>
<td align="right">7.8%</td>
<td align="right">77,897,929</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,897,456</td>
<td align="right">7.8%</td>
<td align="right">77,897,929</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,547,164</td>
<td align="right">3.6%</td>
<td align="right">35,547,160</td>
<td align="right">4.0%</td>
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
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,063,772,775</td>
<td align="right">69.6%</td>
<td align="right">6,048,443,584</td>
<td align="right">69.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,953,701,778</td>
<td align="right">79.8%</td>
<td align="right">6,938,488,005</td>
<td align="right">79.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">348,482,203</td>
<td align="right">4.0%</td>
<td align="right">348,226,699</td>
<td align="right">4.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,783,892,494</td>
<td align="right">20.5%</td>
<td align="right">1,783,537,151</td>
<td align="right">20.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,788,338,934</td>
<td align="right">20.5%</td>
<td align="right">1,787,983,591</td>
<td align="right">20.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,649,305,944</td>
<td align="right">30.4%</td>
<td align="right">2,648,908,574</td>
<td align="right">30.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,649,305,944</td>
<td align="right">30.4%</td>
<td align="right">2,648,908,574</td>
<td align="right">30.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,967,010</td>
<td align="right">9.9%</td>
<td align="right">860,924,983</td>
<td align="right">9.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,015,174</td>
<td align="right">0.4%</td>
<td align="right">31,015,676</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">550,010,377</td>
<td align="right">6.3%</td>
<td align="right">550,004,914</td>
<td align="right">6.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,398,390</td>
<td align="right">1.0%</td>
<td align="right">84,399,015</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,236</td>
<td align="right">2.0%</td>
<td align="right">175,480,413</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">9,126,587</td>
<td align="right"></td>
<td align="right">9,734,403</td>
<td align="right"></td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">61,773,096</td>
<td align="right"></td>
<td align="right">64,875,093</td>
<td align="right"></td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">55,966,743</td>
<td align="right"></td>
<td align="right">58,457,786</td>
<td align="right"></td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">53,464,810,248</td>
<td align="right">37.2%</td>
<td align="right">52,880,511,679</td>
<td align="right">36.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">72,192,050,398</td>
<td align="right">43.3%</td>
<td align="right">71,719,383,073</td>
<td align="right">43.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">90,290,380,121</td>
<td align="right">62.8%</td>
<td align="right">90,813,807,621</td>
<td align="right">63.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">94,381,310,373</td>
<td align="right">56.7%</td>
<td align="right">94,771,015,004</td>
<td align="right">56.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,087,820</td>
<td align="right"></td>
<td align="right">161,821,062</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">94,085,588</td>
<td align="right">0.4%</td>
<td align="right">93,952,660</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,528,930,723</td>
<td align="right"></td>
<td align="right">13,511,596,959</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,715,148,781</td>
<td align="right">55.2%</td>
<td align="right">12,698,887,912</td>
<td align="right">55.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,824,082,524</td>
<td align="right">55.7%</td>
<td align="right">12,807,684,073</td>
<td align="right">55.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,235,966,858</td>
<td align="right"></td>
<td align="right">3,232,450,884</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,208,030,192</td>
<td align="right"></td>
<td align="right">10,200,070,310</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,206,129,677</td>
<td align="right">44.3%</td>
<td align="right">10,198,205,101</td>
<td align="right">44.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">14,848,155</td>
<td align="right">0.1%</td>
<td align="right">14,843,501</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,571,335,563</td>
<td align="right"></td>
<td align="right">4,570,141,652</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,306,920</td>
<td align="right">2.0%</td>
<td align="right">3,306,920</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">113,940</td>
<td align="right">0.1%</td>
<td align="right">113,940</td>
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
<td align="right">115,475,500</td>
<td align="right">19,166,844,683</td>
<td align="right">0</td>
<td align="right">114,736,680</td>
<td align="right">19,132,795,660</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,985,683,876</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,987,823,400</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">12,584</td>
<td align="right">1.0%</td>
<td align="right">7,067</td>
<td align="right">0.6%</td>
<td align="right">-43.8%</td>
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
<td align="right">1,540</td>
<td align="right">0.1%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">125,842</td>
<td align="right">10.3%</td>
<td align="right">114,531</td>
<td align="right">9.4%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,356</td>
<td align="right">5.1%</td>
<td align="right">5,955</td>
<td align="right">5.2%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">50,540</td>
<td align="right">4.1%</td>
<td align="right">47,541</td>
<td align="right">3.9%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,327</td>
<td align="right">0.1%</td>
<td align="right">1,392</td>
<td align="right">0.1%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">253,767,083,565</td>
<td align="right">2,196.7%</td>
<td align="right">264,212,694,471</td>
<td align="right">2,267.6%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">494,730</td>
<td align="right">40.4%</td>
<td align="right">505,016</td>
<td align="right">41.2%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,098,250</td>
<td align="right">89.7%</td>
<td align="right">1,109,955</td>
<td align="right">90.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">11,552,331,000</td>
<td align="right"></td>
<td align="right">11,651,790,267</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,224,092</td>
<td align="right"></td>
<td align="right">1,224,486</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">125,842</td>
<td align="right"></td>
<td align="right">114,531</td>
<td align="right"></td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">110,991</td>
<td align="right">88.2%</td>
<td align="right">112,085</td>
<td align="right">97.9%</td>
<td align="right">1.0%</td>
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
<td align="right">2,446</td>
<td align="right">1.9%</td>
<td align="right">2,446</td>
<td align="right">2.1%</td>
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
<td align="right">5,180</td>
<td align="right">4.1%</td>
<td align="right">5,231</td>
<td align="right">4.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,554</td>
<td align="right">17.1%</td>
<td align="right">21,807</td>
<td align="right">19.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,457</td>
<td align="right">28.2%</td>
<td align="right">35,365</td>
<td align="right">30.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">30,859</td>
<td align="right">24.5%</td>
<td align="right">28,635</td>
<td align="right">25.0%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21,227</td>
<td align="right">16.9%</td>
<td align="right">15,365</td>
<td align="right">13.4%</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,705</td>
<td align="right">7.7%</td>
<td align="right">6,328</td>
<td align="right">5.5%</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,700</td>
<td align="right">1.4%</td>
<td align="right">1,640</td>
<td align="right">1.4%</td>
<td align="right">-3.5%</td>
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
<td align="right">4,020</td>
<td align="right">3.2%</td>
<td align="right">4,031</td>
<td align="right">3.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">14,778</td>
<td align="right">11.7%</td>
<td align="right">14,907</td>
<td align="right">13.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">25,477</td>
<td align="right">20.2%</td>
<td align="right">23,492</td>
<td align="right">20.5%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">36,462</td>
<td align="right">29.0%</td>
<td align="right">36,947</td>
<td align="right">32.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">18,429</td>
<td align="right">14.6%</td>
<td align="right">19,527</td>
<td align="right">17.0%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,765</td>
<td align="right">7.0%</td>
<td align="right">9,244</td>
<td align="right">8.1%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,680</td>
<td align="right">2.1%</td>
<td align="right">3,397</td>
<td align="right">3.0%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">380</td>
<td align="right">0.3%</td>
<td align="right">540</td>
<td align="right">0.5%</td>
<td align="right">42.1%</td>
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
<td align="left">_LOAD_CONST</td>
<td align="right">113,092,647</td>
<td align="right">13,010,240,049</td>
<td align="right">11,404.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,699,306</td>
<td align="right">2,217,756,865</td>
<td align="right">2,318.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,591,613</td>
<td align="right">128,102,477</td>
<td align="right">1,005.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,591,613</td>
<td align="right">128,102,477</td>
<td align="right">1,005.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">697,372,927</td>
<td align="right">6,690,542,138</td>
<td align="right">859.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">213,581,440</td>
<td align="right">1,853,809,951</td>
<td align="right">768.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">10,050,940</td>
<td align="right">27,226,840</td>
<td align="right">170.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">39,840</td>
<td align="right">103,560</td>
<td align="right">159.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">11,627,720</td>
<td align="right">28,867,360</td>
<td align="right">148.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">904,464,417</td>
<td align="right">2,219,623,657</td>
<td align="right">145.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">30,530,704</td>
<td align="right">69,708,266</td>
<td align="right">128.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,185,831,376</td>
<td align="right">1,185,382,905</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">972,068,417</td>
<td align="right">1,853,056,663</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,578,388,942</td>
<td align="right">802,246,482</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">81,769,160</td>
<td align="right">115,903,720</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">81,878,900</td>
<td align="right">116,014,820</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,118,669,598</td>
<td align="right">8,556,511,403</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">47,971,796</td>
<td align="right">55,151,964</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,420,824,180</td>
<td align="right">1,229,017,215</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,717,560</td>
<td align="right">22,284,220</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">394,131,008</td>
<td align="right">438,934,108</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,165,323,171</td>
<td align="right">2,404,796,102</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">149,998,658</td>
<td align="right">161,374,461</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">101,766,716</td>
<td align="right">108,946,884</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">48,461,208</td>
<td align="right">45,548,775</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">264,971,439</td>
<td align="right">280,584,932</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">266,198,699</td>
<td align="right">281,811,752</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,326,980,412</td>
<td align="right">1,404,443,666</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">67,143,554</td>
<td align="right">63,716,514</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,255,996,746</td>
<td align="right">6,524,831,624</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">75,915,288</td>
<td align="right">79,119,405</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,689,641,598</td>
<td align="right">1,754,826,790</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,491,404,316</td>
<td align="right">1,546,251,484</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,790,472,500</td>
<td align="right">1,853,809,951</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,964,300,387</td>
<td align="right">2,027,835,326</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,025,790,340</td>
<td align="right">2,089,380,354</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,086,237,421</td>
<td align="right">2,149,080,937</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">194,445,133</td>
<td align="right">189,287,410</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">658,506,242</td>
<td align="right">675,822,331</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,802,697,783</td>
<td align="right">6,937,190,763</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">7,006,686,615</td>
<td align="right">7,102,383,369</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">834,106,073</td>
<td align="right">844,447,268</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,660,032,412</td>
<td align="right">7,751,100,771</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">266,229,634</td>
<td align="right">269,251,644</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">338,012,663</td>
<td align="right">334,326,084</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,883,888,157</td>
<td align="right">1,904,388,735</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">992,069,386</td>
<td align="right">1,002,458,895</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">407,371,640</td>
<td align="right">411,627,230</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,385,534,161</td>
<td align="right">2,410,332,265</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,682,732</td>
<td align="right">69,337,701</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">126,698,732</td>
<td align="right">127,906,853</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">263,280,235</td>
<td align="right">260,871,880</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,411,789,221</td>
<td align="right">2,433,538,165</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">298,038,161</td>
<td align="right">300,604,995</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,996,012,826</td>
<td align="right">18,140,310,279</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,166,664,395</td>
<td align="right">3,191,868,949</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,276,374,840</td>
<td align="right">7,331,298,163</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">25,197,724</td>
<td align="right">25,377,924</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">104,768,340</td>
<td align="right">105,512,960</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,302,495,447</td>
<td align="right">1,310,737,069</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,323,164,127</td>
<td align="right">1,331,427,729</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,190,114,187</td>
<td align="right">1,197,546,709</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">387,535,304</td>
<td align="right">385,313,857</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">121,960,214</td>
<td align="right">121,268,791</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">884,695,183</td>
<td align="right">889,548,971</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,037,516,643</td>
<td align="right">3,053,795,466</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">15,664,535,254</td>
<td align="right">15,745,839,398</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,409,389</td>
<td align="right">94,915,900</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,653,249</td>
<td align="right">95,161,520</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,016,164,954</td>
<td align="right">2,025,322,642</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">801,129,240</td>
<td align="right">804,697,924</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">464,428</td>
<td align="right">462,407</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,741,254,759</td>
<td align="right">3,755,603,462</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,848,968,545</td>
<td align="right">1,855,395,093</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">893,810,198</td>
<td align="right">896,685,553</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,098,747,330</td>
<td align="right">1,102,071,608</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,387,514</td>
<td align="right">93,668,756</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">907,940,290</td>
<td align="right">905,396,800</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,838,410</td>
<td align="right">31,752,937</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,746,379,324</td>
<td align="right">2,753,689,160</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">317,177,968</td>
<td align="right">317,873,078</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">3,892,298,588</td>
<td align="right">3,900,689,496</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,025,020</td>
<td align="right">3,031,460</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,046,756,605</td>
<td align="right">1,044,574,620</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,426,889,117</td>
<td align="right">3,433,543,525</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">972,404,736</td>
<td align="right">970,535,523</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">651,665,627</td>
<td align="right">652,886,348</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">64,522,264</td>
<td align="right">64,640,624</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,152,813,341</td>
<td align="right">1,154,818,116</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">563,215,438</td>
<td align="right">562,398,996</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">173,877,110</td>
<td align="right">174,092,400</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">5,782,740</td>
<td align="right">5,789,600</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">458,240,665</td>
<td align="right">457,698,367</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">217,016,299</td>
<td align="right">217,270,597</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">219,546,318</td>
<td align="right">219,800,967</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,330,643,246</td>
<td align="right">2,333,305,137</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">274,599,681</td>
<td align="right">274,295,397</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,328,244</td>
<td align="right">2,325,828</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">436,069,778</td>
<td align="right">435,633,523</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">554,012,578</td>
<td align="right">553,461,299</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">137,490,758</td>
<td align="right">137,358,310</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,430,183</td>
<td align="right">78,497,669</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,217,495</td>
<td align="right">10,208,754</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">514,911,618</td>
<td align="right">514,475,303</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,829,218,935</td>
<td align="right">1,827,670,939</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">239,749,369</td>
<td align="right">239,550,687</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,562,814,506</td>
<td align="right">6,557,625,063</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">235,332,278</td>
<td align="right">235,146,291</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,652,522</td>
<td align="right">89,720,014</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,382,081</td>
<td align="right">96,449,845</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">163,088,380</td>
<td align="right">163,201,220</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,361</td>
<td align="right">134,281,587</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,361</td>
<td align="right">134,281,587</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,997,755,109</td>
<td align="right">1,998,992,089</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,319,300,627</td>
<td align="right">2,320,719,264</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,258,870,256</td>
<td align="right">2,260,175,013</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,620,123,428</td>
<td align="right">3,622,199,746</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,530,258</td>
<td align="right">2,531,665</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,340,453,588</td>
<td align="right">1,339,754,710</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,688,480,398</td>
<td align="right">4,690,879,835</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,383,991,842</td>
<td align="right">1,384,669,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">140,453,805</td>
<td align="right">140,521,218</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,611,832,225</td>
<td align="right">1,612,546,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,131,159,754</td>
<td align="right">1,131,635,018</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,683,011,899</td>
<td align="right">1,682,343,699</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,835,900</td>
<td align="right">61,858,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">664,854,810</td>
<td align="right">665,084,606</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,576,279</td>
<td align="right">731,818,882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,126,011</td>
<td align="right">778,362,851</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,663,331</td>
<td align="right">778,900,171</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,059,554,274</td>
<td align="right">1,059,256,438</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,841,122,995</td>
<td align="right">2,841,888,075</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">321,307,751</td>
<td align="right">321,223,371</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">924,450,124</td>
<td align="right">924,213,589</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,816,323,926</td>
<td align="right">1,816,725,202</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">28,421,198</td>
<td align="right">28,427,415</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,990,580</td>
<td align="right">144,971,780</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,819,378,439</td>
<td align="right">4,818,816,723</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,508,771,713</td>
<td align="right">2,508,493,293</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">777,651,964</td>
<td align="right">777,732,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,696,445,923</td>
<td align="right">9,697,437,950</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,776,520</td>
<td align="right">229,753,341</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">246,276,650</td>
<td align="right">246,300,479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">198,396,677</td>
<td align="right">198,381,220</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">861,041,620</td>
<td align="right">861,099,112</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,623,815,990</td>
<td align="right">3,623,622,297</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,027,039,600</td>
<td align="right">1,026,989,287</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,418,726,042</td>
<td align="right">4,418,932,203</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,253,908,771</td>
<td align="right">1,253,852,561</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,402,408</td>
<td align="right">32,403,632</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">164,119,766</td>
<td align="right">164,125,670</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">395,594,191</td>
<td align="right">395,586,279</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">67,794,040</td>
<td align="right">67,795,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,580,260</td>
<td align="right">86,579,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,366,914,203</td>
<td align="right">3,366,953,803</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,922,956</td>
<td align="right">4,922,900</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,550,540</td>
<td align="right">187,552,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,940</td>
<td align="right">6,584,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,685,040</td>
<td align="right">204,686,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,705,220</td>
<td align="right">80,704,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">643,760,629</td>
<td align="right">643,765,094</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,229,675</td>
<td align="right">97,230,158</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,187,015</td>
<td align="right">98,187,498</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,682,008</td>
<td align="right">10,682,038</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,092,152</td>
<td align="right">35,092,201</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,280,057,779</td>
<td align="right">1,280,056,697</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,713,847</td>
<td align="right">90,713,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,475,517</td>
<td align="right">160,475,610</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">3,628,062</td>
<td align="right">3,628,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,638,077</td>
<td align="right">384,637,957</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">395,745,104</td>
<td align="right">395,745,108</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,270,775,852</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,144,563,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">947,012,618</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,147</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">588,457,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,075,760</td>
<td align="right">533,075,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">510,187,700</td>
<td align="right">510,187,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">244,676,060</td>
<td align="right">244,676,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">218,973,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,965,460</td>
<td align="right">154,965,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">102,572,241</td>
<td align="right">102,572,241</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">60,988,920</td>
<td align="right">60,988,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">59,644,340</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_UNARY_INVERT</td>
<td align="right">12,697,060</td>
<td align="right">12,697,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,177,340</td>
<td align="right">8,177,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,862,100</td>
<td align="right">6,862,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,659,960</td>
<td align="right">5,659,960</td>
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
<td align="right">3,917,600</td>
<td align="right">3,917,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,671,620</td>
<td align="right">3,671,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,966,880</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,200</td>
<td align="right">1,160</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">620</td>
<td align="right">600</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,219</td>
<td align="right">6,101</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,601</td>
<td align="right">6,644</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,454</td>
<td align="right">2,459</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">639</td>
<td align="right">640</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">30,600</td>
<td align="right">30,560</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">486,637</td>
<td align="right">487,027</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,540</td>
<td align="right">3,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,649</td>
<td align="right">44,644</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">33,340</td>
<td align="right">33,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,680</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
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
<td align="right">1,107</td>
<td align="right">868</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,107</td>
<td align="right">868</td>
<td align="right">-21.6%</td>
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
Stats gathered on: 2024-07-01
