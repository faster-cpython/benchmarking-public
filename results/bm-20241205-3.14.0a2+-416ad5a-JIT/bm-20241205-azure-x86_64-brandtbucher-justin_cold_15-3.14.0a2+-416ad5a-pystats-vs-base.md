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
<td align="right">3,902,679</td>
<td align="right">5,925,679</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">173,781,876</td>
<td align="right">229,228,009</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">131,594,460</td>
<td align="right">160,495,333</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">236,407,944</td>
<td align="right">273,259,414</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">122,156,340</td>
<td align="right">139,616,048</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">11,643,557</td>
<td align="right">13,218,550</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">125,437,134</td>
<td align="right">141,421,079</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">131,110,549</td>
<td align="right">147,461,536</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">57,295,842</td>
<td align="right">62,052,028</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">25,175,631</td>
<td align="right">26,942,308</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">563,551,543</td>
<td align="right">601,743,284</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">204,619,617</td>
<td align="right">216,983,248</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">57,787,346</td>
<td align="right">60,981,645</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">223,201,385</td>
<td align="right">234,847,317</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">114,854,514</td>
<td align="right">120,707,240</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">302,477,297</td>
<td align="right">316,872,640</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">4,152,749</td>
<td align="right">3,961,100</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">52,094,402</td>
<td align="right">54,496,199</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">269,071,572</td>
<td align="right">280,853,743</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,295,500</td>
<td align="right">10,701,009</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">521,211,386</td>
<td align="right">541,618,586</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">268,145,550</td>
<td align="right">278,612,952</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,257,454,863</td>
<td align="right">2,338,865,990</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">106,054,659</td>
<td align="right">109,827,909</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,948,485</td>
<td align="right">3,810,600</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">60,790,697</td>
<td align="right">62,896,750</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">355,699,287</td>
<td align="right">367,819,900</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">54,610,569</td>
<td align="right">56,410,031</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">37,509,460</td>
<td align="right">38,706,383</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">61,503,078</td>
<td align="right">63,282,783</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">253,159,992</td>
<td align="right">260,445,440</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,903,801</td>
<td align="right">3,792,189</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">58,778,450</td>
<td align="right">60,426,645</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">51,734,325</td>
<td align="right">53,180,888</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">47,326,717</td>
<td align="right">48,639,089</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">36,088,031</td>
<td align="right">37,086,538</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,193,539</td>
<td align="right">99,753,452</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,195,537,073</td>
<td align="right">1,227,020,819</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">786,131,891</td>
<td align="right">806,774,467</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">223,935,992</td>
<td align="right">229,638,836</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">147,409,889</td>
<td align="right">151,139,304</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,931,064,648</td>
<td align="right">1,882,363,887</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,452,438,483</td>
<td align="right">1,488,625,231</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">78,937,047</td>
<td align="right">80,877,392</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">159,253,039</td>
<td align="right">163,080,336</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,786,270,825</td>
<td align="right">3,875,419,933</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">231,690,902</td>
<td align="right">237,081,576</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">12,832,846</td>
<td align="right">12,535,110</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">669,730,459</td>
<td align="right">685,180,694</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">31,650,548</td>
<td align="right">32,356,730</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">59,431,292</td>
<td align="right">60,670,147</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">568,427,725</td>
<td align="right">580,205,814</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">647,400,120</td>
<td align="right">660,647,533</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">705,926,012</td>
<td align="right">720,209,945</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,050,554,873</td>
<td align="right">3,112,241,184</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,741,360,790</td>
<td align="right">1,776,078,146</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">387,875,238</td>
<td align="right">395,500,512</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,194,437,797</td>
<td align="right">13,452,894,641</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">469,612,745</td>
<td align="right">478,806,946</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">102,681,428</td>
<td align="right">104,657,188</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,062,958,838</td>
<td align="right">3,121,137,025</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">647,473,091</td>
<td align="right">659,528,373</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,639,386,701</td>
<td align="right">1,669,517,965</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">36,072,860</td>
<td align="right">36,726,924</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">169,070,752</td>
<td align="right">172,102,597</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">411,148,407</td>
<td align="right">418,466,381</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,918,802</td>
<td align="right">59,927,945</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">279,780,785</td>
<td align="right">284,571,353</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">156,331,846</td>
<td align="right">158,996,858</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,696,300,726</td>
<td align="right">2,741,950,057</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">285,509,932</td>
<td align="right">290,016,465</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">187,972,181</td>
<td align="right">190,925,733</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">454,856,837</td>
<td align="right">461,901,964</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">182,099,828</td>
<td align="right">184,916,828</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">348,087,660</td>
<td align="right">353,012,179</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">296,566,506</td>
<td align="right">300,757,016</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">116,016,580</td>
<td align="right">117,601,815</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,610,374,103</td>
<td align="right">1,630,828,254</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">904,481,720</td>
<td align="right">915,890,331</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">45,571,326</td>
<td align="right">46,144,557</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">388,469,247</td>
<td align="right">393,346,664</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,832,373,825</td>
<td align="right">3,876,161,111</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">181,523,456</td>
<td align="right">183,573,064</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,081,318,812</td>
<td align="right">2,104,795,537</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">160,639,966</td>
<td align="right">162,450,574</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">66,785,096</td>
<td align="right">67,498,624</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">206,464,076</td>
<td align="right">208,632,759</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">23,563,774</td>
<td align="right">23,809,474</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">413,667,164</td>
<td align="right">417,841,948</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,830,561</td>
<td align="right">3,793,431</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">79,743,500</td>
<td align="right">80,494,910</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">329,111,862</td>
<td align="right">332,070,013</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,352,639,290</td>
<td align="right">2,373,781,067</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">91,935,127</td>
<td align="right">92,758,402</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">117,236,004</td>
<td align="right">118,254,729</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">326,630,224</td>
<td align="right">329,416,915</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">170,068,018</td>
<td align="right">171,460,216</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,996,317</td>
<td align="right">8,923,474</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,516,971</td>
<td align="right">9,443,782</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">189,563,774</td>
<td align="right">191,017,873</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">266,571,103</td>
<td align="right">268,278,817</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">58,602,821</td>
<td align="right">58,954,284</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">36,782,488</td>
<td align="right">36,989,297</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">347,649,075</td>
<td align="right">349,583,142</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">526,128,518</td>
<td align="right">528,908,313</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">56,282,233</td>
<td align="right">55,986,676</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">270,840,739</td>
<td align="right">272,218,534</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,629,260</td>
<td align="right">18,718,972</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">89,511,806</td>
<td align="right">89,914,430</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">114,426,072</td>
<td align="right">114,925,673</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">175,953,830</td>
<td align="right">176,662,146</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,135,393</td>
<td align="right">70,405,912</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">188,039,094</td>
<td align="right">188,716,113</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">48,916,702</td>
<td align="right">49,088,328</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,090,164</td>
<td align="right">2,096,773</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,875,890</td>
<td align="right">26,956,444</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">157,138,003</td>
<td align="right">157,563,788</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">811,435,011</td>
<td align="right">813,377,778</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,649,529</td>
<td align="right">11,676,730</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,464,442</td>
<td align="right">67,606,316</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,394,619,592</td>
<td align="right">4,402,964,587</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">101,743,616</td>
<td align="right">101,906,139</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">33,210,276</td>
<td align="right">33,258,896</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">34,232,280</td>
<td align="right">34,280,898</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">83,181,246</td>
<td align="right">83,069,601</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">65,379,331</td>
<td align="right">65,455,463</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,687</td>
<td align="right">33,715</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,708</td>
<td align="right">2,710</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">34,242,309</td>
<td align="right">34,262,623</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">96,028,602</td>
<td align="right">96,084,270</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">153,353,767</td>
<td align="right">153,437,783</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">36,614,426</td>
<td align="right">36,594,378</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">42,657,719</td>
<td align="right">42,637,671</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,785,742,549</td>
<td align="right">1,784,953,531</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">95,321,495</td>
<td align="right">95,361,204</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">75,192,628</td>
<td align="right">75,165,495</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">30,434,623</td>
<td align="right">30,444,878</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,066,577</td>
<td align="right">9,069,612</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,499</td>
<td align="right">773,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">112,042,546</td>
<td align="right">112,068,829</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">157,614,030</td>
<td align="right">157,645,074</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,439,773</td>
<td align="right">1,439,936</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,857,239</td>
<td align="right">1,071,764,559</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">85,642,994</td>
<td align="right">85,649,654</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">51,250,981</td>
<td align="right">51,247,408</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,545,911</td>
<td align="right">20,546,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,876,532</td>
<td align="right">20,877,383</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,876,512</td>
<td align="right">20,877,362</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,115,023</td>
<td align="right">3,115,131</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,878</td>
<td align="right">120,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,837</td>
<td align="right">6,169,897</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">97,134,701</td>
<td align="right">97,133,974</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,148</td>
<td align="right">14,760,235</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">24,711,147</td>
<td align="right">24,711,287</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">21,772,687</td>
<td align="right">21,772,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,938</td>
<td align="right">1,645,935</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">167,577,170</td>
<td align="right">167,577,257</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,814,193</td>
<td align="right">100,814,203</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,376</td>
<td align="right">302,607,376</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,588</td>
<td align="right">128,850,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right">29,134,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">29,134,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,944</td>
<td align="right">8,976,944</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,866,975</td>
<td align="right">4,866,975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,140</td>
<td align="right">2,597,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,199,717</td>
<td align="right">1,199,717</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,194,074</td>
<td align="right">1,194,074</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">781,020</td>
<td align="right">781,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">235,944</td>
<td align="right">235,944</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,720</td>
<td align="right">98,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,553</td>
<td align="right">84,553</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">59,548</td>
<td align="right">59,548</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,192</td>
<td align="right">57,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,672</td>
<td align="right">56,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,546</td>
<td align="right">17,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,321</td>
<td align="right">5,321</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,896</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,642</td>
<td align="right">3,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">150</td>
<td align="right">150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">44</td>
<td align="right">44</td>
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
<td align="right">347,297,564</td>
<td align="right">4.5%</td>
<td align="right">352,221,224</td>
<td align="right">4.5%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,172,144</td>
<td align="right">0.3%</td>
<td align="right">22,166,931</td>
<td align="right">0.3%</td>
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
<td align="right">7,374,918,309</td>
<td align="right">95.2%</td>
<td align="right">7,374,800,308</td>
<td align="right">95.2%</td>
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
<td align="right">783,073</td>
<td align="right">64.8%</td>
<td align="right">783,878</td>
<td align="right">64.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">425,362</td>
<td align="right">35.2%</td>
<td align="right">425,311</td>
<td align="right">35.2%</td>
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
<td align="left">xor</td>
<td align="right">2,571</td>
<td align="right">0.3%</td>
<td align="right">2,892</td>
<td align="right">0.4%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1,627</td>
<td align="right">0.2%</td>
<td align="right">1,748</td>
<td align="right">0.2%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">10,261</td>
<td align="right">1.3%</td>
<td align="right">10,567</td>
<td align="right">1.3%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">857</td>
<td align="right">0.1%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">6,298</td>
<td align="right">0.8%</td>
<td align="right">6,196</td>
<td align="right">0.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,674</td>
<td align="right">2.5%</td>
<td align="right">19,863</td>
<td align="right">2.5%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">13,457</td>
<td align="right">1.7%</td>
<td align="right">13,561</td>
<td align="right">1.7%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">58,917</td>
<td align="right">7.5%</td>
<td align="right">58,567</td>
<td align="right">7.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">36,896</td>
<td align="right">4.7%</td>
<td align="right">37,081</td>
<td align="right">4.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">493</td>
<td align="right">0.1%</td>
<td align="right">491</td>
<td align="right">0.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.3%</td>
<td align="right">2,350</td>
<td align="right">0.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,778</td>
<td align="right">0.5%</td>
<td align="right">3,780</td>
<td align="right">0.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">6,212</td>
<td align="right">0.8%</td>
<td align="right">6,215</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,532</td>
<td align="right">3.0%</td>
<td align="right">23,526</td>
<td align="right">3.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">583,392</td>
<td align="right">74.5%</td>
<td align="right">583,398</td>
<td align="right">74.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">6,006</td>
<td align="right">0.8%</td>
<td align="right">6,006</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">5,313</td>
<td align="right">0.7%</td>
<td align="right">5,313</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">83</td>
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
<td align="right">97,193,539</td>
<td align="right">100.0%</td>
<td align="right">99,753,452</td>
<td align="right">100.0%</td>
<td align="right">2.6%</td>
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
<td align="right">413,525,660</td>
<td align="right">7.0%</td>
<td align="right">417,699,683</td>
<td align="right">7.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,824,723</td>
<td align="right">0.1%</td>
<td align="right">5,827,580</td>
<td align="right">0.1%</td>
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
<td align="right">5,470,580,836</td>
<td align="right">92.9%</td>
<td align="right">5,470,512,994</td>
<td align="right">92.8%</td>
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
<td align="right">132,268</td>
<td align="right">52.7%</td>
<td align="right">133,023</td>
<td align="right">52.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118,909</td>
<td align="right">47.3%</td>
<td align="right">118,975</td>
<td align="right">47.2%</td>
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
<td align="right">48,244</td>
<td align="right">36.5%</td>
<td align="right">49,004</td>
<td align="right">36.8%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">7,121</td>
<td align="right">5.4%</td>
<td align="right">7,205</td>
<td align="right">5.4%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">18,318</td>
<td align="right">13.8%</td>
<td align="right">18,486</td>
<td align="right">13.9%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">35,055</td>
<td align="right">26.5%</td>
<td align="right">34,795</td>
<td align="right">26.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,446</td>
<td align="right">9.4%</td>
<td align="right">12,449</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">3,672</td>
<td align="right">2.8%</td>
<td align="right">3,672</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,609</td>
<td align="right">2.7%</td>
<td align="right">3,609</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.2%</td>
<td align="right">2,941</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">769</td>
<td align="right">0.6%</td>
<td align="right">769</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">120,535,398</td>
<td align="right">1.1%</td>
<td align="right">123,452,140</td>
<td align="right">1.1%</td>
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
<td align="right">10,890,994,328</td>
<td align="right">97.4%</td>
<td align="right">10,884,821,808</td>
<td align="right">97.4%</td>
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
<td align="right">167,358,281</td>
<td align="right">1.5%</td>
<td align="right">167,358,344</td>
<td align="right">1.5%</td>
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
<td align="right">22,186</td>
<td align="right">0.0%</td>
<td align="right">22,186</td>
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
<td align="right">2,468,039</td>
<td align="right">98.2%</td>
<td align="right">2,523,067</td>
<td align="right">98.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">44,327</td>
<td align="right">1.8%</td>
<td align="right">44,327</td>
<td align="right">1.7%</td>
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
<td align="left">out of versions</td>
<td align="right">44,327</td>
<td align="right">100.0%</td>
<td align="right">44,327</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">43,761</td>
<td align="right">98.7%</td>
<td align="right">43,761</td>
<td align="right">98.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">752</td>
<td align="right">1.7%</td>
<td align="right">752</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">287</td>
<td align="right">0.6%</td>
<td align="right">287</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
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
<td align="right">111,570</td>
<td align="right">15.8%</td>
<td align="right">111,572</td>
<td align="right">15.8%</td>
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
<td align="right">584,207</td>
<td align="right">82.9%</td>
<td align="right">584,207</td>
<td align="right">82.9%</td>
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
<td align="right">1,309,385</td>
<td align="right">0.0%</td>
<td align="right">1,300,978</td>
<td align="right">0.0%</td>
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
<td align="right">89,387,686</td>
<td align="right">1.9%</td>
<td align="right">89,790,395</td>
<td align="right">1.9%</td>
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
<td align="right">4,516,119,213</td>
<td align="right">98.0%</td>
<td align="right">4,515,691,184</td>
<td align="right">98.0%</td>
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
<td align="right">42,650</td>
<td align="right">28.7%</td>
<td align="right">42,490</td>
<td align="right">28.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">105,855</td>
<td align="right">71.3%</td>
<td align="right">105,768</td>
<td align="right">71.3%</td>
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
<td align="left">bool</td>
<td align="right">937</td>
<td align="right">0.9%</td>
<td align="right">996</td>
<td align="right">0.9%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">9,308</td>
<td align="right">8.8%</td>
<td align="right">9,085</td>
<td align="right">8.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,140</td>
<td align="right">3.9%</td>
<td align="right">4,209</td>
<td align="right">4.0%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">361</td>
<td align="right">0.3%</td>
<td align="right">363</td>
<td align="right">0.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,190</td>
<td align="right">21.9%</td>
<td align="right">23,173</td>
<td align="right">21.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,740</td>
<td align="right">7.3%</td>
<td align="right">7,744</td>
<td align="right">7.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,409</td>
<td align="right">6.1%</td>
<td align="right">6,412</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">43,573</td>
<td align="right">41.2%</td>
<td align="right">43,589</td>
<td align="right">41.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.2%</td>
<td align="right">7,639</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,221</td>
<td align="right">1.2%</td>
<td align="right">1,221</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,003</td>
<td align="right">0.9%</td>
<td align="right">1,003</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">334</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">51,698,088</td>
<td align="right">2.3%</td>
<td align="right">53,144,313</td>
<td align="right">2.4%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,182,507,453</td>
<td align="right">97.6%</td>
<td align="right">2,182,247,091</td>
<td align="right">97.5%</td>
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
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
<td align="right">1,916,987</td>
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
<td align="right">33,977</td>
<td align="right">46.9%</td>
<td align="right">34,315</td>
<td align="right">47.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,434</td>
<td align="right">53.1%</td>
<td align="right">38,434</td>
<td align="right">52.8%</td>
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
<td align="right">7,839</td>
<td align="right">23.1%</td>
<td align="right">7,956</td>
<td align="right">23.2%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,195</td>
<td align="right">32.9%</td>
<td align="right">11,295</td>
<td align="right">32.9%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,206</td>
<td align="right">27.1%</td>
<td align="right">9,286</td>
<td align="right">27.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,737</td>
<td align="right">16.9%</td>
<td align="right">5,778</td>
<td align="right">16.8%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,466,498</td>
<td align="right">4.3%</td>
<td align="right">50,790,409</td>
<td align="right">6.1%</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">122,051,824</td>
<td align="right">16.2%</td>
<td align="right">139,510,319</td>
<td align="right">16.7%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">596,932,084</td>
<td align="right">79.4%</td>
<td align="right">646,762,326</td>
<td align="right">77.3%</td>
<td align="right">8.3%</td>
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
<td align="right">617,494</td>
<td align="right">86.1%</td>
<td align="right">963,255</td>
<td align="right">90.5%</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">99,451</td>
<td align="right">13.9%</td>
<td align="right">100,662</td>
<td align="right">9.5%</td>
<td align="right">1.2%</td>
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
<td align="right">2,247</td>
<td align="right">2.3%</td>
<td align="right">2,707</td>
<td align="right">2.7%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,587</td>
<td align="right">1.6%</td>
<td align="right">1,887</td>
<td align="right">1.9%</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,914</td>
<td align="right">5.9%</td>
<td align="right">6,762</td>
<td align="right">6.7%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">6,164</td>
<td align="right">6.2%</td>
<td align="right">6,923</td>
<td align="right">6.9%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,495</td>
<td align="right">4.5%</td>
<td align="right">4,907</td>
<td align="right">4.9%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">55,503</td>
<td align="right">55.8%</td>
<td align="right">53,686</td>
<td align="right">53.3%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,405</td>
<td align="right">1.4%</td>
<td align="right">1,445</td>
<td align="right">1.4%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,753</td>
<td align="right">10.8%</td>
<td align="right">10,920</td>
<td align="right">10.8%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,867</td>
<td align="right">2.9%</td>
<td align="right">2,887</td>
<td align="right">2.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,866</td>
<td align="right">4.9%</td>
<td align="right">4,888</td>
<td align="right">4.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,015</td>
<td align="right">3.0%</td>
<td align="right">3,015</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">134</td>
<td align="right">0.1%</td>
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
<td align="right">575,677,447</td>
<td align="right">4.4%</td>
<td align="right">647,431,358</td>
<td align="right">4.9%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">468,119,900</td>
<td align="right">3.5%</td>
<td align="right">477,308,738</td>
<td align="right">3.6%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,163,385,475</td>
<td align="right">92.1%</td>
<td align="right">12,155,353,009</td>
<td align="right">91.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,404,526</td>
<td align="right">0.0%</td>
<td align="right">1,404,526</td>
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
<td align="right">12,126,097</td>
<td align="right">98.2%</td>
<td align="right">13,482,995</td>
<td align="right">98.4%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">218,879</td>
<td align="right">1.8%</td>
<td align="right">221,100</td>
<td align="right">1.6%</td>
<td align="right">1.0%</td>
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
<td align="right">856</td>
<td align="right">0.4%</td>
<td align="right">946</td>
<td align="right">0.4%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23,656</td>
<td align="right">10.8%</td>
<td align="right">24,834</td>
<td align="right">11.2%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,405</td>
<td align="right">1.1%</td>
<td align="right">2,495</td>
<td align="right">1.1%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,958</td>
<td align="right">2.3%</td>
<td align="right">4,894</td>
<td align="right">2.2%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">41,639</td>
<td align="right">19.0%</td>
<td align="right">42,053</td>
<td align="right">19.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">38,024</td>
<td align="right">17.4%</td>
<td align="right">38,232</td>
<td align="right">17.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">61,471</td>
<td align="right">28.1%</td>
<td align="right">61,793</td>
<td align="right">27.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,131</td>
<td align="right">3.7%</td>
<td align="right">8,144</td>
<td align="right">3.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,626</td>
<td align="right">0.7%</td>
<td align="right">1,627</td>
<td align="right">0.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,508</td>
<td align="right">6.6%</td>
<td align="right">14,508</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,585</td>
<td align="right">3.5%</td>
<td align="right">7,585</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,638</td>
<td align="right">0.7%</td>
<td align="right">1,638</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,189</td>
<td align="right">0.5%</td>
<td align="right">1,189</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.5%</td>
<td align="right">1,092</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.2%</td>
<td align="right">400</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">151</td>
<td align="right">0.1%</td>
<td align="right">151</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">3,667,196,130</td>
<td align="right">99.6%</td>
<td align="right">3,726,344,753</td>
<td align="right">99.6%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,653</td>
<td align="right">0.4%</td>
<td align="right">14,622,716</td>
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
<td align="right">1,594</td>
<td align="right">0.0%</td>
<td align="right">1,594</td>
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
<td align="right">52,974</td>
<td align="right">0.0%</td>
<td align="right">52,974</td>
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
<td align="right">138,283</td>
<td align="right">100.0%</td>
<td align="right">138,307</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">253</td>
<td align="right">0.0%</td>
<td align="right">255</td>
<td align="right">0.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">63,865,993</td>
<td align="right">100.0%</td>
<td align="right">63,456,726</td>
<td align="right">100.0%</td>
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
<td align="right">2,455</td>
<td align="right">100.0%</td>
<td align="right">2,455</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">593,288,744</td>
<td align="right">82.2%</td>
<td align="right">593,288,775</td>
<td align="right">82.2%</td>
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
<td align="right">128,815,796</td>
<td align="right">17.8%</td>
<td align="right">128,815,796</td>
<td align="right">17.8%</td>
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
<td align="right">14,711</td>
<td align="right">0.0%</td>
<td align="right">14,711</td>
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
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,412</td>
<td align="right">98.1%</td>
<td align="right">34,412</td>
<td align="right">98.1%</td>
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
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right">752</td>
<td align="right">2.2%</td>
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
<td align="right">60,701,846</td>
<td align="right">3.0%</td>
<td align="right">62,807,379</td>
<td align="right">3.1%</td>
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
<td align="right">110,444,053</td>
<td align="right">5.4%</td>
<td align="right">110,758,831</td>
<td align="right">5.5%</td>
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
<td align="right">1,857,385,907</td>
<td align="right">91.6%</td>
<td align="right">1,853,167,363</td>
<td align="right">91.4%</td>
<td align="right">-0.2%</td>
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
<td align="right">46,340</td>
<td align="right">2.1%</td>
<td align="right">46,853</td>
<td align="right">2.2%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,125,582</td>
<td align="right">97.9%</td>
<td align="right">2,131,480</td>
<td align="right">97.8%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">4,954</td>
<td align="right">10.7%</td>
<td align="right">5,121</td>
<td align="right">10.9%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,077</td>
<td align="right">52.0%</td>
<td align="right">24,417</td>
<td align="right">52.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,348</td>
<td align="right">7.2%</td>
<td align="right">3,356</td>
<td align="right">7.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,759</td>
<td align="right">3.8%</td>
<td align="right">1,757</td>
<td align="right">3.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">16.5%</td>
<td align="right">7,666</td>
<td align="right">16.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.5%</td>
<td align="right">1,619</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">913</td>
<td align="right">2.0%</td>
<td align="right">913</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.6%</td>
<td align="right">730</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.5%</td>
<td align="right">699</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">365</td>
<td align="right">0.8%</td>
<td align="right">365</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">100</td>
<td align="right">0.2%</td>
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
<td align="right">1,194,074</td>
<td align="right">100.0%</td>
<td align="right">1,194,074</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">91,899,337</td>
<td align="right">9.1%</td>
<td align="right">92,722,409</td>
<td align="right">9.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">919,639,911</td>
<td align="right">90.9%</td>
<td align="right">919,378,186</td>
<td align="right">90.8%</td>
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
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">2,220</td>
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
<td align="right">33,634</td>
<td align="right">93.9%</td>
<td align="right">33,828</td>
<td align="right">93.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,196</td>
<td align="right">6.1%</td>
<td align="right">2,205</td>
<td align="right">6.1%</td>
<td align="right">0.4%</td>
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
<td align="right">236</td>
<td align="right">0.7%</td>
<td align="right">376</td>
<td align="right">1.1%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">1.0%</td>
<td align="right">364</td>
<td align="right">1.1%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,031</td>
<td align="right">9.0%</td>
<td align="right">2,971</td>
<td align="right">8.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">3,715</td>
<td align="right">11.0%</td>
<td align="right">3,764</td>
<td align="right">11.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">9,040</td>
<td align="right">26.9%</td>
<td align="right">9,062</td>
<td align="right">26.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,703</td>
<td align="right">49.7%</td>
<td align="right">16,723</td>
<td align="right">49.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">500</td>
<td align="right">1.5%</td>
<td align="right">500</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">68</td>
<td align="right">0.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">41,055,227</td>
<td align="right">0.9%</td>
<td align="right">42,048,305</td>
<td align="right">0.9%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">102,210,128</td>
<td align="right">2.2%</td>
<td align="right">104,190,214</td>
<td align="right">2.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,562,277,739</td>
<td align="right">96.9%</td>
<td align="right">4,558,546,883</td>
<td align="right">96.9%</td>
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
<td align="right">823,261</td>
<td align="right">66.2%</td>
<td align="right">842,017</td>
<td align="right">66.9%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">421,157</td>
<td align="right">33.8%</td>
<td align="right">416,779</td>
<td align="right">33.1%</td>
<td align="right">-1.0%</td>
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
<td align="right">23,313</td>
<td align="right">5.5%</td>
<td align="right">19,026</td>
<td align="right">4.6%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,339</td>
<td align="right">2.9%</td>
<td align="right">12,649</td>
<td align="right">3.0%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">5,686</td>
<td align="right">1.4%</td>
<td align="right">5,799</td>
<td align="right">1.4%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">93,871</td>
<td align="right">22.3%</td>
<td align="right">94,356</td>
<td align="right">22.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,457</td>
<td align="right">61.1%</td>
<td align="right">256,470</td>
<td align="right">61.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,634</td>
<td align="right">2.1%</td>
<td align="right">8,622</td>
<td align="right">2.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">13,475</td>
<td align="right">3.2%</td>
<td align="right">13,475</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,540</td>
<td align="right">1.1%</td>
<td align="right">4,540</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,233,384,893</td>
<td align="right">99.9%</td>
<td align="right">1,233,177,008</td>
<td align="right">99.9%</td>
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
<td align="right">1,427,395</td>
<td align="right">0.1%</td>
<td align="right">1,427,536</td>
<td align="right">0.1%</td>
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
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">3,700</td>
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
<td align="right">857</td>
<td align="right">6.9%</td>
<td align="right">867</td>
<td align="right">6.9%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,601</td>
<td align="right">93.1%</td>
<td align="right">11,613</td>
<td align="right">93.1%</td>
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
<td align="left">sequence</td>
<td align="right">630</td>
<td align="right">73.5%</td>
<td align="right">640</td>
<td align="right">73.8%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.9%</td>
<td align="right">136</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">10.6%</td>
<td align="right">91</td>
<td align="right">10.5%</td>
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
<td align="right">912,217,901</td>
<td align="right">1.2%</td>
<td align="right">1,006,642,352</td>
<td align="right">1.3%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,161,316,170</td>
<td align="right">2.8%</td>
<td align="right">2,206,383,911</td>
<td align="right">2.8%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">28,358,601,820</td>
<td align="right">37.1%</td>
<td align="right">28,885,808,156</td>
<td align="right">37.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">44,904,399,515</td>
<td align="right">58.8%</td>
<td align="right">45,611,125,882</td>
<td align="right">58.7%</td>
<td align="right">1.6%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">122,051,824</td>
<td align="right">5.7%</td>
<td align="right">139,510,319</td>
<td align="right">6.3%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,193,539</td>
<td align="right">4.5%</td>
<td align="right">99,753,452</td>
<td align="right">4.5%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">468,119,900</td>
<td align="right">21.7%</td>
<td align="right">477,308,738</td>
<td align="right">21.7%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">102,210,128</td>
<td align="right">4.7%</td>
<td align="right">104,190,214</td>
<td align="right">4.7%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">347,297,564</td>
<td align="right">16.1%</td>
<td align="right">352,221,224</td>
<td align="right">16.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">413,525,660</td>
<td align="right">19.2%</td>
<td align="right">417,699,683</td>
<td align="right">19.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">91,899,337</td>
<td align="right">4.3%</td>
<td align="right">92,722,409</td>
<td align="right">4.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">89,387,686</td>
<td align="right">4.1%</td>
<td align="right">89,790,395</td>
<td align="right">4.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">167,358,281</td>
<td align="right">7.8%</td>
<td align="right">167,358,344</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,796</td>
<td align="right">6.0%</td>
<td align="right">128,815,796</td>
<td align="right">5.8%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">220,452,019</td>
<td align="right">24.2%</td>
<td align="right">255,978,651</td>
<td align="right">25.4%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">74,150,863</td>
<td align="right">8.1%</td>
<td align="right">83,535,899</td>
<td align="right">8.3%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">152,778,474</td>
<td align="right">16.7%</td>
<td align="right">171,946,915</td>
<td align="right">17.1%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,398,772</td>
<td align="right">8.3%</td>
<td align="right">81,005,689</td>
<td align="right">8.0%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">62,450,642</td>
<td align="right">6.8%</td>
<td align="right">65,348,431</td>
<td align="right">6.5%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,238,807</td>
<td align="right">2.3%</td>
<td align="right">21,145,421</td>
<td align="right">2.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">21,597,451</td>
<td align="right">2.4%</td>
<td align="right">21,672,109</td>
<td align="right">2.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">88,810,965</td>
<td align="right">9.7%</td>
<td align="right">89,051,085</td>
<td align="right">8.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,872,824</td>
<td align="right">2.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">19,399,127</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">25,437,424</td>
<td align="right">2.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">25,276,685</td>
<td align="right">2.5%</td>
<td align="right"></td>
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
<td align="right">71,617,898</td>
<td align="right">1.1%</td>
<td align="right">71,343,593</td>
<td align="right">1.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,286,929,475</td>
<td align="right">79.1%</td>
<td align="right">5,283,455,342</td>
<td align="right">79.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,117,782,782</td>
<td align="right">16.7%</td>
<td align="right">1,117,085,724</td>
<td align="right">16.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,119,914,928</td>
<td align="right">16.8%</td>
<td align="right">1,119,217,870</td>
<td align="right">16.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,158,629</td>
<td align="right">4.2%</td>
<td align="right">278,991,150</td>
<td align="right">4.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,894,395,641</td>
<td align="right">73.2%</td>
<td align="right">4,891,645,743</td>
<td align="right">73.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,790,384,479</td>
<td align="right">26.8%</td>
<td align="right">1,789,457,581</td>
<td align="right">26.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,790,384,479</td>
<td align="right">26.8%</td>
<td align="right">1,789,457,581</td>
<td align="right">26.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,469,551</td>
<td align="right">10.0%</td>
<td align="right">670,239,711</td>
<td align="right">10.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,102</td>
<td align="right">0.4%</td>
<td align="right">24,922,405</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,407,158</td>
<td align="right">3.9%</td>
<td align="right">261,408,088</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,250</td>
<td align="right">0.0%</td>
<td align="right">2,128,250</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,139</td>
<td align="right">2.0%</td>
<td align="right">132,513,139</td>
<td align="right">2.0%</td>
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
<td align="right">8,147,288</td>
<td align="right"></td>
<td align="right">7,276,664</td>
<td align="right"></td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">8,668,842,276</td>
<td align="right">5.3%</td>
<td align="right">8,848,375,278</td>
<td align="right">5.4%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">66,080,678</td>
<td align="right"></td>
<td align="right">64,831,247</td>
<td align="right"></td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">15,985,381,643</td>
<td align="right">7.9%</td>
<td align="right">16,198,948,367</td>
<td align="right">8.0%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">34,623,401,407</td>
<td align="right">21.0%</td>
<td align="right">35,051,619,715</td>
<td align="right">21.3%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">78,723,124,731</td>
<td align="right">47.8%</td>
<td align="right">77,939,037,976</td>
<td align="right">47.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">84,282,949,926</td>
<td align="right">41.8%</td>
<td align="right">83,518,140,328</td>
<td align="right">41.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">46,264,230,731</td>
<td align="right">22.9%</td>
<td align="right">46,670,115,268</td>
<td align="right">23.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">58,740,121</td>
<td align="right"></td>
<td align="right">58,360,650</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,011,692,268</td>
<td align="right"></td>
<td align="right">2,021,961,111</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">55,251,198,851</td>
<td align="right">27.4%</td>
<td align="right">54,977,593,318</td>
<td align="right">27.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">42,828,312,827</td>
<td align="right">26.0%</td>
<td align="right">42,659,426,411</td>
<td align="right">25.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,101,029</td>
<td align="right"></td>
<td align="right">178,803,510</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,076,305,337</td>
<td align="right"></td>
<td align="right">3,077,148,219</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">9,939,270,411</td>
<td align="right">53.9%</td>
<td align="right">9,937,021,470</td>
<td align="right">53.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,017,205,714</td>
<td align="right">54.3%</td>
<td align="right">10,014,970,503</td>
<td align="right">54.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,607,891,537</td>
<td align="right"></td>
<td align="right">10,605,701,902</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,437,157,988</td>
<td align="right">45.7%</td>
<td align="right">8,435,462,534</td>
<td align="right">45.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,437,376,802</td>
<td align="right"></td>
<td align="right">8,435,693,571</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,516,226</td>
<td align="right">0.4%</td>
<td align="right">71,530,108</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,419,077</td>
<td align="right">0.0%</td>
<td align="right">6,418,925</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,139</td>
<td align="right">2.5%</td>
<td align="right">4,444,139</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">476,014</td>
<td align="right">0.3%</td>
<td align="right">476,014</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">364,040</td>
<td align="right">103,261,049</td>
<td align="right">9,485,133,739</td>
<td align="right">771,027,661</td>
<td align="right">762,412,200</td>
<td align="right">364,008</td>
<td align="right">103,417,105</td>
<td align="right">9,481,149,020</td>
<td align="right">770,155,987</td>
<td align="right">762,580,022</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,605,395,918</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,605,401,162</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,002</td>
<td align="right">0.2%</td>
<td align="right">1,716</td>
<td align="right">0.4%</td>
<td align="right">71.3%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">2,804</td>
<td align="right">0.6%</td>
<td align="right">3,606</td>
<td align="right">0.8%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">70,422</td>
<td align="right">14.6%</td>
<td align="right">84,943</td>
<td align="right">17.7%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">601</td>
<td align="right">0.9%</td>
<td align="right">500</td>
<td align="right">0.6%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,299</td>
<td align="right">0.3%</td>
<td align="right">1,493</td>
<td align="right">0.3%</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,713,210,260</td>
<td align="right"></td>
<td align="right">6,425,087,713</td>
<td align="right"></td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">368,051</td>
<td align="right">76.3%</td>
<td align="right">353,319</td>
<td align="right">73.5%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">411,620</td>
<td align="right">85.3%</td>
<td align="right">395,516</td>
<td align="right">82.3%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">249</td>
<td align="right">0.1%</td>
<td align="right">241</td>
<td align="right">0.1%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">248,648,229,519</td>
<td align="right">3,703.9%</td>
<td align="right">244,949,269,075</td>
<td align="right">3,812.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">482,291</td>
<td align="right"></td>
<td align="right">480,700</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">62,502</td>
<td align="right">88.8%</td>
<td align="right">75,700</td>
<td align="right">89.1%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">70,422</td>
<td align="right"></td>
<td align="right">84,943</td>
<td align="right"></td>
<td align="right">20.6%</td>
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
<td align="right">5,492</td>
<td align="right">7.8%</td>
<td align="right">5,876</td>
<td align="right">6.9%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">9,094</td>
<td align="right">12.9%</td>
<td align="right">11,070</td>
<td align="right">13.0%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">22,107</td>
<td align="right">31.4%</td>
<td align="right">28,292</td>
<td align="right">33.3%</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">17,310</td>
<td align="right">24.6%</td>
<td align="right">20,558</td>
<td align="right">24.2%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">9,836</td>
<td align="right">14.0%</td>
<td align="right">11,871</td>
<td align="right">14.0%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,731</td>
<td align="right">8.1%</td>
<td align="right">6,365</td>
<td align="right">7.5%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">772</td>
<td align="right">1.1%</td>
<td align="right">831</td>
<td align="right">1.0%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
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
<td align="right">1,091</td>
<td align="right">1.5%</td>
<td align="right">1,157</td>
<td align="right">1.4%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">9,688</td>
<td align="right">13.8%</td>
<td align="right">11,388</td>
<td align="right">13.4%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">10,442</td>
<td align="right">14.8%</td>
<td align="right">12,052</td>
<td align="right">14.2%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">25,777</td>
<td align="right">36.6%</td>
<td align="right">33,347</td>
<td align="right">39.3%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,260</td>
<td align="right">14.6%</td>
<td align="right">12,216</td>
<td align="right">14.4%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,918</td>
<td align="right">5.6%</td>
<td align="right">4,255</td>
<td align="right">5.0%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,244</td>
<td align="right">1.8%</td>
<td align="right">1,183</td>
<td align="right">1.4%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">82</td>
<td align="right">0.1%</td>
<td align="right">102</td>
<td align="right">0.1%</td>
<td align="right">24.4%</td>
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
<td align="right">42,452</td>
<td align="right">819</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,093,927</td>
<td align="right">1,070,927</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">2,615,370</td>
<td align="right">1,223,172</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,417,435</td>
<td align="right">847,063</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">1,437,259</td>
<td align="right">863,924</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">558,979</td>
<td align="right">418,048</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">4,331,739</td>
<td align="right">3,473,400</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">416,968,512</td>
<td align="right">344,139,080</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">15,421,586</td>
<td align="right">12,744,923</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">7,234,883</td>
<td align="right">8,296,398</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,202,669</td>
<td align="right">2,932,524</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">383,799,516</td>
<td align="right">356,057,956</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">417,764,426</td>
<td align="right">388,282,056</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">132,417,950</td>
<td align="right">123,359,457</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">314,563,209</td>
<td align="right">293,898,368</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">96,627,981</td>
<td align="right">90,423,407</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">94,458,799</td>
<td align="right">88,606,086</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">29,808,211</td>
<td align="right">28,008,774</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">29,808,211</td>
<td align="right">28,008,774</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">22,265,425</td>
<td align="right">20,924,920</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">172,255,729</td>
<td align="right">161,940,939</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">693,595,553</td>
<td align="right">655,120,356</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">18,019,991</td>
<td align="right">17,020,642</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">281,480,892</td>
<td align="right">266,028,096</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">119,098,691</td>
<td align="right">112,755,650</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">313,332,655</td>
<td align="right">297,088,267</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">679,907,363</td>
<td align="right">647,041,628</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">5,883,359,839</td>
<td align="right">5,616,848,637</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,713,210,260</td>
<td align="right">6,425,087,713</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">216,017,943</td>
<td align="right">206,776,569</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">244,471,073</td>
<td align="right">234,363,030</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">981,263</td>
<td align="right">941,943</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">40,381,404</td>
<td align="right">38,795,815</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">40,380,444</td>
<td align="right">38,795,215</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">417,793,955</td>
<td align="right">402,109,361</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">420,455,195</td>
<td align="right">404,770,601</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">46,104,892</td>
<td align="right">44,492,867</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,782,195,510</td>
<td align="right">1,722,411,350</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,146,519,668</td>
<td align="right">8,850,044,791</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">991,729,922</td>
<td align="right">959,920,542</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,206,696,758</td>
<td align="right">5,040,828,703</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">84,164,930</td>
<td align="right">81,605,017</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">582,397,794</td>
<td align="right">565,730,462</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">68,961,736</td>
<td align="right">67,035,910</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,798,512,989</td>
<td align="right">2,720,391,351</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,079,325,726</td>
<td align="right">2,023,242,642</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">533,561,323</td>
<td align="right">519,962,393</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">4,468,737</td>
<td align="right">4,354,919</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">76,324,822</td>
<td align="right">74,405,110</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">48,289,695</td>
<td align="right">47,089,399</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">151,714,932</td>
<td align="right">148,090,308</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">75,293,124</td>
<td align="right">73,515,325</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">813,447,572</td>
<td align="right">794,552,210</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,493,798,072</td>
<td align="right">2,436,316,289</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">173,802,300</td>
<td align="right">169,827,234</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,551,279,989</td>
<td align="right">2,493,740,365</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,762,155,351</td>
<td align="right">1,722,753,220</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,534,676,125</td>
<td align="right">3,458,182,865</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">401,733,652</td>
<td align="right">393,074,681</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">557,337,913</td>
<td align="right">545,483,715</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,309,736,737</td>
<td align="right">2,260,732,212</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,699,462,818</td>
<td align="right">1,663,748,562</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">6,965,660</td>
<td align="right">6,822,317</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">900,142,325</td>
<td align="right">882,288,912</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,488,703,464</td>
<td align="right">1,460,104,843</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">713,655,038</td>
<td align="right">700,102,974</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,930,122,858</td>
<td align="right">1,893,768,506</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">167,860,584</td>
<td align="right">164,757,894</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">38,540,003</td>
<td align="right">37,833,821</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">183,984,431</td>
<td align="right">180,658,996</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">27,027,701</td>
<td align="right">26,539,341</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,933,406,954</td>
<td align="right">1,899,516,888</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">5,898,471,782</td>
<td align="right">5,796,442,568</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">43,705,386</td>
<td align="right">42,965,101</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,691,709,063</td>
<td align="right">1,663,557,017</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">247,813,956</td>
<td align="right">243,780,039</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">497,680,114</td>
<td align="right">489,711,574</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">56,366,762</td>
<td align="right">55,499,226</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">71,299,200</td>
<td align="right">70,280,472</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,209,358,728</td>
<td align="right">3,163,695,042</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">835,187,516</td>
<td align="right">823,360,788</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,886,576,686</td>
<td align="right">2,845,831,068</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,386,426,285</td>
<td align="right">1,367,130,187</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">221,410,299</td>
<td align="right">218,378,826</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">769,819,096</td>
<td align="right">759,317,406</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">103,575,350</td>
<td align="right">102,177,583</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,985,065,997</td>
<td align="right">1,958,634,937</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,318,040,958</td>
<td align="right">1,300,688,223</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,317,144,781</td>
<td align="right">1,299,818,792</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">207,389,397</td>
<td align="right">204,748,702</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,665,325,849</td>
<td align="right">4,606,556,269</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,087,968,949</td>
<td align="right">5,025,152,257</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">722,124,671</td>
<td align="right">713,358,431</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">22,583,116,262</td>
<td align="right">22,309,925,218</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">161,196,325</td>
<td align="right">159,256,297</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,831,026,193</td>
<td align="right">5,761,362,578</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">197,264,241</td>
<td align="right">194,907,798</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,236,430,489</td>
<td align="right">1,221,748,182</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">676,765,630</td>
<td align="right">669,010,138</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,775,673,814</td>
<td align="right">2,744,104,684</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">19,216,512,970</td>
<td align="right">19,002,757,983</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,414,596,546</td>
<td align="right">1,399,096,434</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">170,188,943</td>
<td align="right">168,379,371</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">116,947,354</td>
<td align="right">115,750,430</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">778,674,294</td>
<td align="right">770,755,785</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">633,026,970</td>
<td align="right">626,719,759</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">285,366,535</td>
<td align="right">282,595,731</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,320,773,830</td>
<td align="right">8,241,739,798</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">804,640,467</td>
<td align="right">797,245,633</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,188,341,694</td>
<td align="right">1,177,423,590</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">757,126,583</td>
<td align="right">750,653,111</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">485,906,864</td>
<td align="right">481,963,675</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,053,480,260</td>
<td align="right">1,044,991,394</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,848,277,064</td>
<td align="right">1,833,410,126</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">70,268,641</td>
<td align="right">69,703,714</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">152,060,704</td>
<td align="right">150,859,281</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">722,448,663</td>
<td align="right">716,806,508</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">484,898,214</td>
<td align="right">481,263,821</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,004,462,596</td>
<td align="right">997,254,919</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,474,126,334</td>
<td align="right">1,464,054,727</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">20,510,571</td>
<td align="right">20,374,050</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">90,967,708</td>
<td align="right">90,370,235</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,134,541,114</td>
<td align="right">4,107,539,546</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,957,471,905</td>
<td align="right">1,944,945,633</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,605,807,253</td>
<td align="right">4,577,530,517</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">789,709,233</td>
<td align="right">784,919,052</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,100,151,774</td>
<td align="right">2,087,696,497</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,873,564,384</td>
<td align="right">1,862,527,979</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,035,955,079</td>
<td align="right">1,029,855,345</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">65,884,855</td>
<td align="right">65,500,251</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">510,963,782</td>
<td align="right">508,010,679</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">386,839,379</td>
<td align="right">384,670,727</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,517,287,336</td>
<td align="right">2,503,853,903</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,062,820</td>
<td align="right">46,817,120</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">99,675,487</td>
<td align="right">99,170,883</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">99,675,487</td>
<td align="right">99,170,883</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,550,213,948</td>
<td align="right">3,533,863,385</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,229,513,878</td>
<td align="right">4,210,515,863</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">545,157,609</td>
<td align="right">542,769,907</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">578,401,333</td>
<td align="right">575,887,320</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">578,401,333</td>
<td align="right">575,887,320</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">58,103,990</td>
<td align="right">57,857,890</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">159,004,348</td>
<td align="right">159,670,911</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">128,191,418</td>
<td align="right">127,672,837</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,349,577,627</td>
<td align="right">1,344,150,515</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">853,523,456</td>
<td align="right">850,210,356</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">29,355,142</td>
<td align="right">29,242,490</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">30,119,175</td>
<td align="right">30,006,523</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,814,597,259</td>
<td align="right">3,801,067,279</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">504,270,438</td>
<td align="right">502,489,675</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,433,309,408</td>
<td align="right">2,424,957,078</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">59,979,438</td>
<td align="right">59,780,609</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,364,257,278</td>
<td align="right">1,360,067,702</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,566,176</td>
<td align="right">6,546,888</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,479,531,808</td>
<td align="right">9,453,295,740</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,087,308,255</td>
<td align="right">1,084,317,941</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,928,425,899</td>
<td align="right">2,920,835,717</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,274,170,954</td>
<td align="right">4,263,534,516</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">598,850,809</td>
<td align="right">597,387,725</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,036,437,069</td>
<td align="right">3,029,391,956</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">71,268,687</td>
<td align="right">71,104,795</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">71,268,687</td>
<td align="right">71,104,795</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,940,465,228</td>
<td align="right">1,936,219,020</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">78,651,966</td>
<td align="right">78,480,506</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,422,360</td>
<td align="right">40,342,018</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">991,835,619</td>
<td align="right">990,126,905</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,220,825,435</td>
<td align="right">1,218,739,111</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,152,220</td>
<td align="right">6,142,367</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">293,923,530</td>
<td align="right">293,515,768</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">294,141,480</td>
<td align="right">293,733,718</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">427,655,262</td>
<td align="right">427,074,245</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">608,980,630</td>
<td align="right">608,157,918</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">391,659,930</td>
<td align="right">391,148,044</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">57,254,806</td>
<td align="right">57,186,242</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,260,900</td>
<td align="right">24,233,730</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">87,004,424</td>
<td align="right">86,919,047</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">784,205,956</td>
<td align="right">783,465,655</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,556,234,277</td>
<td align="right">1,554,780,239</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">309,204,940</td>
<td align="right">308,937,364</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">851,688,574</td>
<td align="right">851,011,195</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">97,185,252</td>
<td align="right">97,136,632</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,628,879</td>
<td align="right">6,625,963</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">123,597,560</td>
<td align="right">123,548,940</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">60,738,415</td>
<td align="right">60,718,452</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">33,816,322</td>
<td align="right">33,806,076</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">33,816,322</td>
<td align="right">33,806,076</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">305,242,309</td>
<td align="right">305,152,040</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">114,406,158</td>
<td align="right">114,375,498</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">78,196,954</td>
<td align="right">78,217,002</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">79,470,238</td>
<td align="right">79,490,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">468,665,076</td>
<td align="right">468,576,448</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">25,914,301</td>
<td align="right">25,918,501</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">85,875,642</td>
<td align="right">85,864,656</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">25,679,371</td>
<td align="right">25,676,255</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">25,679,371</td>
<td align="right">25,676,255</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">216,364,877</td>
<td align="right">216,341,117</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,278,080</td>
<td align="right">60,271,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">500,430,593</td>
<td align="right">500,407,245</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">52,059,320</td>
<td align="right">52,058,580</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">31,491,420</td>
<td align="right">31,490,980</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">31,135,080</td>
<td align="right">31,134,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">172,166,252</td>
<td align="right">172,167,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">50,239,680</td>
<td align="right">50,239,540</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">50,239,680</td>
<td align="right">50,239,540</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,304,301</td>
<td align="right">40,304,195</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">269,489,737</td>
<td align="right">269,489,737</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,492,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">3,891,960</td>
<td align="right">3,891,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">3,891,960</td>
<td align="right">3,891,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">3,840,960</td>
<td align="right">3,840,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right">3,555,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">1,989,784</td>
<td align="right">1,989,784</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">764,033</td>
<td align="right">764,033</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">764,033</td>
<td align="right">764,033</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">181,915</td>
<td align="right">181,915</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">123,165</td>
<td align="right">123,165</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">98,482</td>
<td align="right">98,482</td>
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
<td align="left">CALL</td>
<td align="right">10,269</td>
<td align="right">9,901</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">24,537</td>
<td align="right">25,020</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,449</td>
<td align="right">23,131</td>
<td align="right">-1.4%</td>
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
<td align="right">22,629</td>
<td align="right">22,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">31</td>
<td align="right">31</td>
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
<td align="right">38</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">160</td>
<td align="right">160</td>
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
<td align="right">2,476</td>
<td align="right">2,476</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-12-06
