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
<td align="left">STORE_SLICE</td>
<td align="right">1,232,482</td>
<td align="right">932,342</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">364,786,060</td>
<td align="right">300,209,923</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,362,747</td>
<td align="right">3,933,742</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">117,785,200</td>
<td align="right">98,494,330</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">195,981,617</td>
<td align="right">168,092,001</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">53,679,924</td>
<td align="right">60,080,810</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">42,971,831</td>
<td align="right">47,382,293</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">116,796,988</td>
<td align="right">128,388,337</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">167,393,868</td>
<td align="right">183,258,118</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">110,659,046</td>
<td align="right">121,134,226</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">27,218,390</td>
<td align="right">24,915,208</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">370,677,066</td>
<td align="right">341,188,082</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">56,571,607</td>
<td align="right">60,747,296</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">288,847,117</td>
<td align="right">269,901,921</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,771,012</td>
<td align="right">17,640,941</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">367,901,540</td>
<td align="right">387,988,273</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">339,455,458</td>
<td align="right">355,085,226</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,565,756</td>
<td align="right">3,403,594</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">197,594,382</td>
<td align="right">206,450,150</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,421,256,134</td>
<td align="right">1,484,404,986</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">151,834,698</td>
<td align="right">145,263,886</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">244,646,626</td>
<td align="right">254,740,400</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,156,159,247</td>
<td align="right">3,277,649,798</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,981,760,202</td>
<td align="right">1,905,886,168</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">654,545,391</td>
<td align="right">629,878,197</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">875,466,276</td>
<td align="right">843,917,575</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">773,331,761</td>
<td align="right">800,881,554</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">446,005,882</td>
<td align="right">461,535,292</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">176,056,236</td>
<td align="right">181,650,244</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">18,217,794</td>
<td align="right">17,641,890</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">67,758,225</td>
<td align="right">69,724,103</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,946,239,603</td>
<td align="right">2,000,616,623</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">371,701,441</td>
<td align="right">382,022,459</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,207,961,089</td>
<td align="right">2,146,808,565</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">645,646,097</td>
<td align="right">662,705,168</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">233,948,482</td>
<td align="right">239,927,505</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">85,846,947</td>
<td align="right">87,923,607</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">227,837,810</td>
<td align="right">233,302,818</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,641</td>
<td align="right">2,582</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">243,292,361</td>
<td align="right">248,634,162</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">878,729,426</td>
<td align="right">897,812,169</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">196,353,061</td>
<td align="right">192,337,632</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,380,468</td>
<td align="right">63,609,923</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">850,514,253</td>
<td align="right">865,966,141</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">85,670,785</td>
<td align="right">87,211,853</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">288,324,989</td>
<td align="right">293,333,609</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">866,368,632</td>
<td align="right">881,020,144</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,654,546,905</td>
<td align="right">3,714,427,194</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,583,685,156</td>
<td align="right">3,525,158,830</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">273,007,134</td>
<td align="right">277,458,434</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">349,221,773</td>
<td align="right">354,914,712</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">862,591,409</td>
<td align="right">848,610,911</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">364,275,233</td>
<td align="right">369,874,418</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">43,342,293</td>
<td align="right">43,926,634</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,928,431,351</td>
<td align="right">4,994,853,373</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">51,325,435</td>
<td align="right">51,993,852</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">695,109,055</td>
<td align="right">704,081,999</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">270,410,897</td>
<td align="right">273,900,256</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">195,432,207</td>
<td align="right">197,948,689</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,435,113,979</td>
<td align="right">2,466,073,455</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">531,072,924</td>
<td align="right">537,697,393</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">73,440,696</td>
<td align="right">74,339,433</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">164,563,075</td>
<td align="right">166,252,008</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">67,043,554</td>
<td align="right">67,711,733</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,047,367,388</td>
<td align="right">1,057,702,838</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">119,450,260</td>
<td align="right">118,303,709</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,361,313</td>
<td align="right">61,926,302</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,617,868,609</td>
<td align="right">4,577,135,980</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,569,802,069</td>
<td align="right">2,548,232,046</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">133,361,400</td>
<td align="right">134,469,972</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">38,414,445</td>
<td align="right">38,731,777</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">13,155,401</td>
<td align="right">13,261,661</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">252,260</td>
<td align="right">250,259</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">185,934,637</td>
<td align="right">184,522,565</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">169,748,621</td>
<td align="right">170,942,241</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">369,146,694</td>
<td align="right">371,721,427</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">92,496,365</td>
<td align="right">93,135,075</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">95,710,355</td>
<td align="right">96,367,174</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">822,972,649</td>
<td align="right">828,511,971</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">105,480,922</td>
<td align="right">106,184,738</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">281,036,937</td>
<td align="right">282,720,578</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">606,144,421</td>
<td align="right">609,709,241</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">459,051,184</td>
<td align="right">461,645,449</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">574,958,166</td>
<td align="right">578,189,549</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">103,557,553</td>
<td align="right">104,133,383</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">146,105,845</td>
<td align="right">146,902,484</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,226,803</td>
<td align="right">35,405,054</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">162,095,026</td>
<td align="right">162,911,871</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">866,760,061</td>
<td align="right">871,117,641</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,204,352</td>
<td align="right">10,254,662</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,171,138</td>
<td align="right">185,072,464</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,536,966</td>
<td align="right">13,602,762</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,002,971</td>
<td align="right">56,732,060</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">74,941,780</td>
<td align="right">75,284,858</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">138,698,789</td>
<td align="right">139,309,548</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,936,654,585</td>
<td align="right">4,914,948,458</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">120,043,809</td>
<td align="right">120,557,513</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">114,517,656</td>
<td align="right">115,007,402</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,177,109</td>
<td align="right">41,352,608</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">80,967,906</td>
<td align="right">81,310,984</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">922,229,805</td>
<td align="right">925,939,088</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">609,467,866</td>
<td align="right">611,915,510</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,957,326,757</td>
<td align="right">3,942,361,605</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">67,647,701</td>
<td align="right">67,880,639</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">514,106,086</td>
<td align="right">515,711,679</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">13,153</td>
<td align="right">13,115</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">114,765,177</td>
<td align="right">115,091,657</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">468,522,076</td>
<td align="right">469,848,318</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,558,232,697</td>
<td align="right">16,600,032,737</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">908,666,319</td>
<td align="right">910,824,040</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">34,145</td>
<td align="right">34,223</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">437,756,354</td>
<td align="right">438,657,358</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,492,900</td>
<td align="right">4,501,163</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,006,343,169</td>
<td align="right">2,002,758,779</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">367,100,576</td>
<td align="right">367,751,310</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,469</td>
<td align="right">5,478</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">213,369,515</td>
<td align="right">213,716,039</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,951,635</td>
<td align="right">9,967,556</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,076,702,571</td>
<td align="right">1,078,354,362</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">162,935,797</td>
<td align="right">163,182,483</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">336,159,221</td>
<td align="right">336,667,855</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,471,007</td>
<td align="right">12,486,771</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">494,662,786</td>
<td align="right">495,281,117</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">44,303,601</td>
<td align="right">44,357,456</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,267,722</td>
<td align="right">2,269,793</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">171,500,463</td>
<td align="right">171,363,557</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,300,661</td>
<td align="right">242,476,873</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,350,122</td>
<td align="right">244,527,744</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">34,572,051</td>
<td align="right">34,594,026</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">141,112</td>
<td align="right">141,189</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,112,630,067</td>
<td align="right">1,113,138,201</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">192,026,512</td>
<td align="right">191,943,376</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">107,287,067</td>
<td align="right">107,333,174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,937,027</td>
<td align="right">27,948,449</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">76,725,028</td>
<td align="right">76,749,704</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">431,739,356</td>
<td align="right">431,877,931</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">440,782</td>
<td align="right">440,654</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,534,002,991</td>
<td align="right">1,534,337,310</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,720,644</td>
<td align="right">25,725,067</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">810,302,191</td>
<td align="right">810,438,153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">64,420,106</td>
<td align="right">64,428,330</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,762,832</td>
<td align="right">14,761,559</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,262,492</td>
<td align="right">1,262,392</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,724,734</td>
<td align="right">155,730,774</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,092,128</td>
<td align="right">5,091,946</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">69,831,795</td>
<td align="right">69,829,431</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">277,693</td>
<td align="right">277,687</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,048,042</td>
<td align="right">3,048,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">263,058,397</td>
<td align="right">263,053,792</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">54,908,720</td>
<td align="right">54,907,911</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,774,480</td>
<td align="right">5,774,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">129,275,990</td>
<td align="right">129,274,230</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,187,528</td>
<td align="right">9,187,421</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,510</td>
<td align="right">5,803,470</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">246,507,524</td>
<td align="right">246,508,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,354,013</td>
<td align="right">131,353,648</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">123,859,735</td>
<td align="right">123,860,037</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,612,830</td>
<td align="right">114,613,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,188,635</td>
<td align="right">20,188,617</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">19,857,656</td>
<td align="right">19,857,639</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,188,654</td>
<td align="right">20,188,637</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,118</td>
<td align="right">35,549,094</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">30,832,980</td>
<td align="right">30,832,999</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,372,623</td>
<td align="right">70,372,608</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,234,057</td>
<td align="right">418,234,037</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,619,559</td>
<td align="right">591,619,535</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,137</td>
<td align="right">302,246,137</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,732</td>
<td align="right">128,851,732</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,571</td>
<td align="right">41,964,571</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">9,742,833</td>
<td align="right">9,742,833</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,796</td>
<td align="right">8,976,796</td>
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
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,484,985</td>
<td align="right">3,484,985</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,144</td>
<td align="right">2,597,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,720,427</td>
<td align="right">1,720,427</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">117,444</td>
<td align="right">117,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,575</td>
<td align="right">98,575</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,564</td>
<td align="right">72,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,551</td>
<td align="right">69,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,753</td>
<td align="right">57,753</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,916</td>
<td align="right">53,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">13,984</td>
<td align="right">13,984</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,295</td>
<td align="right">5,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,904</td>
<td align="right">3,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,586</td>
<td align="right">3,586</td>
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
<td align="right">176</td>
<td align="right">176</td>
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
<td align="right">25</td>
<td align="right">25</td>
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
<td align="right">1,076,220,407</td>
<td align="right">6.2%</td>
<td align="right">1,077,871,086</td>
<td align="right">6.2%</td>
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
<td align="right">55,522,824</td>
<td align="right">0.3%</td>
<td align="right">55,583,475</td>
<td align="right">0.3%</td>
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
<td align="right">16,228,533,903</td>
<td align="right">93.5%</td>
<td align="right">16,244,681,921</td>
<td align="right">93.5%</td>
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
<td align="right">463,520</td>
<td align="right">30.3%</td>
<td align="right">465,629</td>
<td align="right">30.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,066,027</td>
<td align="right">69.7%</td>
<td align="right">1,066,130</td>
<td align="right">69.6%</td>
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
<td align="left">subscr bytes</td>
<td align="right">1,814</td>
<td align="right">0.4%</td>
<td align="right">1,176</td>
<td align="right">0.3%</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">169</td>
<td align="right">0.0%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">327</td>
<td align="right">0.1%</td>
<td align="right">349</td>
<td align="right">0.1%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21,979</td>
<td align="right">4.7%</td>
<td align="right">23,441</td>
<td align="right">5.0%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,194</td>
<td align="right">1.3%</td>
<td align="right">6,394</td>
<td align="right">1.4%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">6,996</td>
<td align="right">1.5%</td>
<td align="right">7,176</td>
<td align="right">1.5%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">16,343</td>
<td align="right">3.5%</td>
<td align="right">16,683</td>
<td align="right">3.6%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">338</td>
<td align="right">0.1%</td>
<td align="right">333</td>
<td align="right">0.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">40,935</td>
<td align="right">8.8%</td>
<td align="right">41,272</td>
<td align="right">8.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">11,552</td>
<td align="right">2.5%</td>
<td align="right">11,633</td>
<td align="right">2.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,130</td>
<td align="right">0.7%</td>
<td align="right">3,110</td>
<td align="right">0.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">633</td>
<td align="right">0.1%</td>
<td align="right">629</td>
<td align="right">0.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.5%</td>
<td align="right">2,350</td>
<td align="right">0.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">62,995</td>
<td align="right">13.6%</td>
<td align="right">63,138</td>
<td align="right">13.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,518</td>
<td align="right">4.0%</td>
<td align="right">18,483</td>
<td align="right">4.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,861</td>
<td align="right">4.3%</td>
<td align="right">19,883</td>
<td align="right">4.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,294</td>
<td align="right">1.8%</td>
<td align="right">8,302</td>
<td align="right">1.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,767</td>
<td align="right">0.6%</td>
<td align="right">2,768</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">22,444</td>
<td align="right">4.8%</td>
<td align="right">22,447</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">36,397</td>
<td align="right">7.9%</td>
<td align="right">36,400</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">107,940</td>
<td align="right">23.3%</td>
<td align="right">107,942</td>
<td align="right">23.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">28,692</td>
<td align="right">6.2%</td>
<td align="right">28,692</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">25,838</td>
<td align="right">5.6%</td>
<td align="right">25,838</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,693</td>
<td align="right">1.4%</td>
<td align="right">6,693</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,163</td>
<td align="right">0.7%</td>
<td align="right">3,163</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,334</td>
<td align="right">0.5%</td>
<td align="right">2,334</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">0.4%</td>
<td align="right">1,996</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr structtime</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">106</td>
<td align="right">0.0%</td>
<td align="right">106</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">184,171,138</td>
<td align="right">100.0%</td>
<td align="right">185,072,464</td>
<td align="right">100.0%</td>
<td align="right">0.5%</td>
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
<td align="right">145,932,980</td>
<td align="right">1.3%</td>
<td align="right">160,494,669</td>
<td align="right">1.4%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">143,255,111</td>
<td align="right">1.3%</td>
<td align="right">157,542,214</td>
<td align="right">1.4%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,976,692,645</td>
<td align="right">98.7%</td>
<td align="right">10,980,275,026</td>
<td align="right">98.6%</td>
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
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">8,513</td>
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
<td align="right">2,929,983</td>
<td align="right">100.0%</td>
<td align="right">3,202,568</td>
<td align="right">100.0%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">146</td>
<td align="right">0.0%</td>
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
<td align="left">init not simple</td>
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">146</td>
<td align="right">100.0%</td>
<td align="right">146</td>
<td align="right">100.0%</td>
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
<td align="right">575,465</td>
<td align="right">96.6%</td>
<td align="right">575,467</td>
<td align="right">96.6%</td>
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
<td align="right">582,741</td>
<td align="right">97.8%</td>
<td align="right">582,741</td>
<td align="right">97.8%</td>
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
<td align="right">20,429</td>
<td align="right">100.0%</td>
<td align="right">20,389</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">92,378,471</td>
<td align="right">2.0%</td>
<td align="right">93,017,294</td>
<td align="right">2.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,160,369</td>
<td align="right">0.0%</td>
<td align="right">1,164,829</td>
<td align="right">0.0%</td>
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
<td align="right">4,494,051,595</td>
<td align="right">98.0%</td>
<td align="right">4,507,187,711</td>
<td align="right">98.0%</td>
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
<td align="left">Success</td>
<td align="right">40,114</td>
<td align="right">28.7%</td>
<td align="right">39,892</td>
<td align="right">28.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">99,473</td>
<td align="right">71.3%</td>
<td align="right">99,672</td>
<td align="right">71.4%</td>
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
<td align="left">long float</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">196</td>
<td align="right">0.2%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,323</td>
<td align="right">1.3%</td>
<td align="right">1,369</td>
<td align="right">1.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,851</td>
<td align="right">1.9%</td>
<td align="right">1,884</td>
<td align="right">1.9%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,104</td>
<td align="right">4.1%</td>
<td align="right">4,173</td>
<td align="right">4.2%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,636</td>
<td align="right">7.7%</td>
<td align="right">7,527</td>
<td align="right">7.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">9,403</td>
<td align="right">9.5%</td>
<td align="right">9,310</td>
<td align="right">9.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">36,917</td>
<td align="right">37.1%</td>
<td align="right">37,092</td>
<td align="right">37.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,180</td>
<td align="right">23.3%</td>
<td align="right">23,235</td>
<td align="right">23.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">5,893</td>
<td align="right">5.9%</td>
<td align="right">5,894</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">7.7%</td>
<td align="right">7,648</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">974</td>
<td align="right">1.0%</td>
<td align="right">974</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">370</td>
<td align="right">0.4%</td>
<td align="right">370</td>
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
<td align="right">85,802,906</td>
<td align="right">3.8%</td>
<td align="right">87,879,240</td>
<td align="right">3.9%</td>
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
<td align="right">2,183,589,548</td>
<td align="right">96.2%</td>
<td align="right">2,186,997,321</td>
<td align="right">96.1%</td>
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
<td align="right">1,389,959</td>
<td align="right">0.1%</td>
<td align="right">1,389,959</td>
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
<td align="right">41,725</td>
<td align="right">59.4%</td>
<td align="right">42,251</td>
<td align="right">59.9%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,539</td>
<td align="right">40.6%</td>
<td align="right">28,339</td>
<td align="right">40.1%</td>
<td align="right">-0.7%</td>
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
<td align="left">str</td>
<td align="right">9,842</td>
<td align="right">23.6%</td>
<td align="right">10,179</td>
<td align="right">24.1%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,625</td>
<td align="right">25.5%</td>
<td align="right">10,718</td>
<td align="right">25.4%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">11,987</td>
<td align="right">28.7%</td>
<td align="right">12,090</td>
<td align="right">28.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,271</td>
<td align="right">22.2%</td>
<td align="right">9,264</td>
<td align="right">21.9%</td>
<td align="right">-0.1%</td>
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
<td align="right">195,319,174</td>
<td align="right">12.5%</td>
<td align="right">197,834,734</td>
<td align="right">12.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,311,194,922</td>
<td align="right">83.6%</td>
<td align="right">1,321,533,131</td>
<td align="right">83.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">61,322,438</td>
<td align="right">3.9%</td>
<td align="right">61,522,521</td>
<td align="right">3.9%</td>
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
<td align="right">107,555</td>
<td align="right">8.5%</td>
<td align="right">108,471</td>
<td align="right">8.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,162,335</td>
<td align="right">91.5%</td>
<td align="right">1,166,122</td>
<td align="right">91.5%</td>
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
<td align="left">ascii string</td>
<td align="right">1,136</td>
<td align="right">1.1%</td>
<td align="right">1,196</td>
<td align="right">1.1%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,639</td>
<td align="right">1.5%</td>
<td align="right">1,703</td>
<td align="right">1.6%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,835</td>
<td align="right">11.9%</td>
<td align="right">13,038</td>
<td align="right">12.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,211</td>
<td align="right">3.9%</td>
<td align="right">4,149</td>
<td align="right">3.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">49,429</td>
<td align="right">46.0%</td>
<td align="right">50,109</td>
<td align="right">46.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">5,892</td>
<td align="right">5.5%</td>
<td align="right">5,829</td>
<td align="right">5.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,432</td>
<td align="right">6.0%</td>
<td align="right">6,472</td>
<td align="right">6.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,169</td>
<td align="right">3.9%</td>
<td align="right">4,149</td>
<td align="right">3.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">6,603</td>
<td align="right">6.1%</td>
<td align="right">6,617</td>
<td align="right">6.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">10,965</td>
<td align="right">10.2%</td>
<td align="right">10,965</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,567</td>
<td align="right">3.3%</td>
<td align="right">3,567</td>
<td align="right">3.3%</td>
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
<td align="right">260</td>
<td align="right">0.2%</td>
<td align="right">260</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">90</td>
<td align="right">0.1%</td>
<td align="right">90</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### GET_ITER

<details>
<summary> specialization stats for GET_ITER family </summary>

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
<td align="left">set</td>
<td align="right">12,099,416</td>
<td align="right">12,099,416 / 0 !!</td>
<td align="right">12,124,070</td>
<td align="right">12,124,070 / 0 !!</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">302,574,861</td>
<td align="right">302,574,861 / 0 !!</td>
<td align="right">303,136,602</td>
<td align="right">303,136,602 / 0 !!</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">116,678,617</td>
<td align="right">116,678,617 / 0 !!</td>
<td align="right">116,791,341</td>
<td align="right">116,791,341 / 0 !!</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">390,670,347</td>
<td align="right">390,670,347 / 0 !!</td>
<td align="right">390,908,455</td>
<td align="right">390,908,455 / 0 !!</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">171,577,033</td>
<td align="right">171,577,033 / 0 !!</td>
<td align="right">171,475,862</td>
<td align="right">171,475,862 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,730,138</td>
<td align="right">5,730,138 / 0 !!</td>
<td align="right">5,730,074</td>
<td align="right">5,730,074 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">102,092,378</td>
<td align="right">102,092,378 / 0 !!</td>
<td align="right">102,092,371</td>
<td align="right">102,092,371 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,813,451</td>
<td align="right">34,813,451 / 0 !!</td>
<td align="right">34,813,451</td>
<td align="right">34,813,451 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,693,965</td>
<td align="right">2,693,965 / 0 !!</td>
<td align="right">2,693,965</td>
<td align="right">2,693,965 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
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
<td align="right">597,478,509</td>
<td align="right">4.6%</td>
<td align="right">673,874,089</td>
<td align="right">5.1%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">529,371,442</td>
<td align="right">4.1%</td>
<td align="right">535,996,011</td>
<td align="right">4.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,918,953,475</td>
<td align="right">91.4%</td>
<td align="right">11,976,240,501</td>
<td align="right">90.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,262,336</td>
<td align="right">0.0%</td>
<td align="right">1,262,336</td>
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
<td align="right">11,362,852</td>
<td align="right">96.3%</td>
<td align="right">12,799,784</td>
<td align="right">96.7%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">439,435</td>
<td align="right">3.7%</td>
<td align="right">443,390</td>
<td align="right">3.3%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">22,431</td>
<td align="right">5.1%</td>
<td align="right">23,574</td>
<td align="right">5.3%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,738</td>
<td align="right">0.4%</td>
<td align="right">1,764</td>
<td align="right">0.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,913</td>
<td align="right">1.1%</td>
<td align="right">4,864</td>
<td align="right">1.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">37,202</td>
<td align="right">8.5%</td>
<td align="right">37,450</td>
<td align="right">8.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">41,038</td>
<td align="right">9.3%</td>
<td align="right">40,953</td>
<td align="right">9.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,661</td>
<td align="right">1.7%</td>
<td align="right">7,652</td>
<td align="right">1.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,498</td>
<td align="right">3.5%</td>
<td align="right">15,483</td>
<td align="right">3.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">48,027</td>
<td align="right">10.9%</td>
<td align="right">48,064</td>
<td align="right">10.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">1.0%</td>
<td align="right">4,449</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,379</td>
<td align="right">0.5%</td>
<td align="right">2,379</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,715</td>
<td align="right">0.4%</td>
<td align="right">1,715</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,033</td>
<td align="right">0.2%</td>
<td align="right">1,033</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">741</td>
<td align="right">0.2%</td>
<td align="right">741</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">545</td>
<td align="right">0.1%</td>
<td align="right">545</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">255</td>
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
<td align="right">47,937</td>
<td align="right">0.0%</td>
<td align="right">48,504</td>
<td align="right">0.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,528,053,589</td>
<td align="right">99.7%</td>
<td align="right">4,482,910,409</td>
<td align="right">99.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,623,253</td>
<td align="right">0.3%</td>
<td align="right">14,623,385</td>
<td align="right">0.3%</td>
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
<td align="right">1,381</td>
<td align="right">0.0%</td>
<td align="right">1,381</td>
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
<td align="right">140,290</td>
<td align="right">100.0%</td>
<td align="right">138,885</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">216</td>
<td align="right">0.0%</td>
<td align="right">217</td>
<td align="right">0.0%</td>
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
<td align="right">65,216,143</td>
<td align="right">100.0%</td>
<td align="right">65,306,747</td>
<td align="right">100.0%</td>
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
<td align="right">2,425</td>
<td align="right">100.0%</td>
<td align="right">2,365</td>
<td align="right">100.0%</td>
<td align="right">-2.5%</td>
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
<td align="right">591,604,848</td>
<td align="right">82.1%</td>
<td align="right">591,604,824</td>
<td align="right">82.1%</td>
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
<td align="right">128,816,934</td>
<td align="right">17.9%</td>
<td align="right">128,816,934</td>
<td align="right">17.9%</td>
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
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">34,411</td>
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
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">3,260</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">106,854,880</td>
<td align="right">5.4%</td>
<td align="right">109,589,400</td>
<td align="right">5.5%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">61,274,724</td>
<td align="right">3.1%</td>
<td align="right">61,841,003</td>
<td align="right">3.1%</td>
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
<td align="right">1,811,550,276</td>
<td align="right">91.5%</td>
<td align="right">1,815,768,130</td>
<td align="right">91.4%</td>
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
<td align="right">2,057,370</td>
<td align="right">97.9%</td>
<td align="right">2,107,598</td>
<td align="right">97.9%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">44,474</td>
<td align="right">2.1%</td>
<td align="right">44,586</td>
<td align="right">2.1%</td>
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
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.6%</td>
<td align="right">1,665</td>
<td align="right">3.7%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,650</td>
<td align="right">10.5%</td>
<td align="right">4,715</td>
<td align="right">10.6%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">240,942</td>
<td align="right">541.8%</td>
<td align="right">243,516</td>
<td align="right">546.2%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,346</td>
<td align="right">7.5%</td>
<td align="right">3,342</td>
<td align="right">7.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,781</td>
<td align="right">8.5%</td>
<td align="right">3,785</td>
<td align="right">8.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">19,853</td>
<td align="right">44.6%</td>
<td align="right">19,853</td>
<td align="right">44.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,227</td>
<td align="right">16.2%</td>
<td align="right">7,227</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">764</td>
<td align="right">1.7%</td>
<td align="right">764</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">1.0%</td>
<td align="right">423</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">365</td>
<td align="right">0.8%</td>
<td align="right">365</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">91</td>
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
<td align="right">1,232,482</td>
<td align="right">100.0%</td>
<td align="right">932,342</td>
<td align="right">100.0%</td>
<td align="right">-24.4%</td>
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
<td align="right">103,519,036</td>
<td align="right">10.1%</td>
<td align="right">104,094,869</td>
<td align="right">10.2%</td>
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
<td align="right">916,744,351</td>
<td align="right">89.9%</td>
<td align="right">918,283,964</td>
<td align="right">89.8%</td>
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
<td align="left">Success</td>
<td align="right">2,224</td>
<td align="right">5.8%</td>
<td align="right">2,102</td>
<td align="right">5.5%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">36,333</td>
<td align="right">94.2%</td>
<td align="right">36,452</td>
<td align="right">94.5%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">3,323</td>
<td align="right">9.1%</td>
<td align="right">3,443</td>
<td align="right">9.4%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,284</td>
<td align="right">47.6%</td>
<td align="right">17,283</td>
<td align="right">47.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">10,484</td>
<td align="right">28.9%</td>
<td align="right">10,484</td>
<td align="right">28.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,990</td>
<td align="right">8.2%</td>
<td align="right">2,990</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">4.6%</td>
<td align="right">1,681</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.9%</td>
<td align="right">341</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">162</td>
<td align="right">0.4%</td>
<td align="right">162</td>
<td align="right">0.4%</td>
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
<td align="right">63,127,551</td>
<td align="right">1.4%</td>
<td align="right">79,599,777</td>
<td align="right">1.8%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,264,840,806</td>
<td align="right">95.6%</td>
<td align="right">4,218,092,163</td>
<td align="right">95.2%</td>
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
<td align="right">132,840,850</td>
<td align="right">3.0%</td>
<td align="right">133,951,374</td>
<td align="right">3.0%</td>
<td align="right">0.8%</td>
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
<td align="right">1,240,921</td>
<td align="right">72.6%</td>
<td align="right">1,551,224</td>
<td align="right">76.8%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">469,010</td>
<td align="right">27.4%</td>
<td align="right">467,577</td>
<td align="right">23.2%</td>
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
<td align="left">bytes</td>
<td align="right">4,677</td>
<td align="right">1.0%</td>
<td align="right">4,118</td>
<td align="right">0.9%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">8,851</td>
<td align="right">1.9%</td>
<td align="right">9,530</td>
<td align="right">2.0%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">27,789</td>
<td align="right">5.9%</td>
<td align="right">26,063</td>
<td align="right">5.6%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">10,889</td>
<td align="right">2.3%</td>
<td align="right">10,957</td>
<td align="right">2.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">72,285</td>
<td align="right">15.4%</td>
<td align="right">72,378</td>
<td align="right">15.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,076</td>
<td align="right">2.1%</td>
<td align="right">10,064</td>
<td align="right">2.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">74,719</td>
<td align="right">15.9%</td>
<td align="right">74,735</td>
<td align="right">16.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,838</td>
<td align="right">55.0%</td>
<td align="right">257,846</td>
<td align="right">55.1%</td>
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
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">84</td>
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
<td align="right">1,232,108,162</td>
<td align="right">99.9%</td>
<td align="right">1,232,610,077</td>
<td align="right">99.9%</td>
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
<td align="right">1,251,720</td>
<td align="right">0.1%</td>
<td align="right">1,251,640</td>
<td align="right">0.1%</td>
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
<td align="right">792</td>
<td align="right">7.3%</td>
<td align="right">784</td>
<td align="right">7.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,060</td>
<td align="right">92.7%</td>
<td align="right">10,048</td>
<td align="right">92.8%</td>
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
<td align="right">558</td>
<td align="right">70.5%</td>
<td align="right">550</td>
<td align="right">70.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">17.2%</td>
<td align="right">136</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">12.4%</td>
<td align="right">98</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,033,602,219</td>
<td align="right">1.1%</td>
<td align="right">1,144,032,440</td>
<td align="right">1.2%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">3,185,338,176</td>
<td align="right">3.3%</td>
<td align="right">3,204,924,777</td>
<td align="right">3.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">39,257,253,008</td>
<td align="right">40.2%</td>
<td align="right">39,367,468,183</td>
<td align="right">40.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">54,233,029,530</td>
<td align="right">55.5%</td>
<td align="right">54,251,566,672</td>
<td align="right">55.4%</td>
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
<td align="left">CALL</td>
<td align="right">143,255,111</td>
<td align="right">5.2%</td>
<td align="right">157,542,214</td>
<td align="right">5.7%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">85,802,906</td>
<td align="right">3.1%</td>
<td align="right">87,879,240</td>
<td align="right">3.2%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">195,319,174</td>
<td align="right">7.1%</td>
<td align="right">197,834,734</td>
<td align="right">7.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">529,371,442</td>
<td align="right">19.2%</td>
<td align="right">535,996,011</td>
<td align="right">19.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">132,840,850</td>
<td align="right">4.8%</td>
<td align="right">133,951,374</td>
<td align="right">4.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">92,378,471</td>
<td align="right">3.4%</td>
<td align="right">93,017,294</td>
<td align="right">3.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">103,519,036</td>
<td align="right">3.8%</td>
<td align="right">104,094,869</td>
<td align="right">3.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,171,138</td>
<td align="right">6.7%</td>
<td align="right">185,072,464</td>
<td align="right">6.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,076,220,407</td>
<td align="right">39.1%</td>
<td align="right">1,077,871,086</td>
<td align="right">38.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,934</td>
<td align="right">4.7%</td>
<td align="right">128,816,934</td>
<td align="right">4.6%</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">26,730,874</td>
<td align="right">2.6%</td>
<td align="right">35,108,642</td>
<td align="right">3.1%</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">29,837,139</td>
<td align="right">2.9%</td>
<td align="right">37,910,693</td>
<td align="right">3.3%</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">53,629,580</td>
<td align="right">5.2%</td>
<td align="right">66,569,036</td>
<td align="right">5.8%</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">173,561,637</td>
<td align="right">16.8%</td>
<td align="right">203,997,754</td>
<td align="right">17.8%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">216,445,140</td>
<td align="right">20.9%</td>
<td align="right">253,021,097</td>
<td align="right">22.1%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">78,065,911</td>
<td align="right">7.6%</td>
<td align="right">82,918,781</td>
<td align="right">7.2%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">75,254,707</td>
<td align="right">7.3%</td>
<td align="right">79,281,737</td>
<td align="right">6.9%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">87,859,459</td>
<td align="right">8.5%</td>
<td align="right">90,588,851</td>
<td align="right">7.9%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,621,944</td>
<td align="right">3.0%</td>
<td align="right">30,727,945</td>
<td align="right">2.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">30,623,099</td>
<td align="right">3.0%</td>
<td align="right">30,717,181</td>
<td align="right">2.7%</td>
<td align="right">0.3%</td>
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
<td align="right">5,078,222,271</td>
<td align="right">76.7%</td>
<td align="right">5,090,490,233</td>
<td align="right">76.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,346,862,760</td>
<td align="right">80.8%</td>
<td align="right">5,359,132,959</td>
<td align="right">80.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">274,619,433</td>
<td align="right">4.2%</td>
<td align="right">274,809,819</td>
<td align="right">4.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">949,808,505</td>
<td align="right">14.4%</td>
<td align="right">950,143,140</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">954,085,882</td>
<td align="right">14.4%</td>
<td align="right">954,420,517</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,538,494,531</td>
<td align="right">23.3%</td>
<td align="right">1,538,828,857</td>
<td align="right">23.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,538,494,531</td>
<td align="right">23.3%</td>
<td align="right">1,538,828,857</td>
<td align="right">23.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,504,136</td>
<td align="right">3.9%</td>
<td align="right">259,510,835</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,999,142</td>
<td align="right">0.4%</td>
<td align="right">23,999,065</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,150,754</td>
<td align="right">1.1%</td>
<td align="right">70,150,844</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,408,649</td>
<td align="right">8.8%</td>
<td align="right">584,408,340</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,473</td>
<td align="right">0.1%</td>
<td align="right">4,273,473</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,904</td>
<td align="right">0.0%</td>
<td align="right">3,904</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,421</td>
<td align="right">2.0%</td>
<td align="right">132,513,421</td>
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
<td align="left">Method cache misses</td>
<td align="right">56,170,360</td>
<td align="right"></td>
<td align="right">54,361,805</td>
<td align="right"></td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,198,144</td>
<td align="right"></td>
<td align="right">7,409,863</td>
<td align="right"></td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">62,562,855</td>
<td align="right"></td>
<td align="right">60,966,384</td>
<td align="right"></td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,922,448,248</td>
<td align="right">3.1%</td>
<td align="right">2,944,974,124</td>
<td align="right">3.2%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">24,682,791,569</td>
<td align="right">26.5%</td>
<td align="right">24,860,435,221</td>
<td align="right">26.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,063,860,619</td>
<td align="right"></td>
<td align="right">2,072,595,402</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,217,015,917</td>
<td align="right">1.1%</td>
<td align="right">1,222,106,116</td>
<td align="right">1.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">33,698,906,558</td>
<td align="right">30.5%</td>
<td align="right">33,793,135,519</td>
<td align="right">30.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,363,229,558</td>
<td align="right"></td>
<td align="right">2,368,505,166</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,407,988</td>
<td align="right">0.0%</td>
<td align="right">6,419,197</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,150,952</td>
<td align="right">0.4%</td>
<td align="right">71,275,340</td>
<td align="right">0.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">25,150,821,256</td>
<td align="right">22.7%</td>
<td align="right">25,194,048,431</td>
<td align="right">22.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">175,150,538</td>
<td align="right"></td>
<td align="right">175,398,941</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">41,339,879,740</td>
<td align="right">44.4%</td>
<td align="right">41,282,214,018</td>
<td align="right">44.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,545,107,308</td>
<td align="right">28.2%</td>
<td align="right">5,550,926,044</td>
<td align="right">28.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,467,548,368</td>
<td align="right">27.8%</td>
<td align="right">5,473,231,507</td>
<td align="right">27.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,142,647,034</td>
<td align="right"></td>
<td align="right">6,148,546,229</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,090,692,622</td>
<td align="right"></td>
<td align="right">14,101,758,702</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,090,585,591</td>
<td align="right">71.8%</td>
<td align="right">14,101,636,637</td>
<td align="right">71.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">50,588,246,563</td>
<td align="right">45.7%</td>
<td align="right">50,627,649,145</td>
<td align="right">45.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">24,141,719,045</td>
<td align="right">25.9%</td>
<td align="right">24,139,423,767</td>
<td align="right">25.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,405,028</td>
<td align="right">1.9%</td>
<td align="right">3,405,028</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">265,159</td>
<td align="right">0.2%</td>
<td align="right">265,159</td>
<td align="right">0.2%</td>
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
<td align="right">363,973</td>
<td align="right">100,870,399</td>
<td align="right">9,470,231,871</td>
<td align="right">750,338,659</td>
<td align="right">762,836,932</td>
<td align="right">364,534</td>
<td align="right">101,480,063</td>
<td align="right">9,447,836,267</td>
<td align="right">745,349,243</td>
<td align="right">762,171,191</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,675,668,984</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,675,664,388</td>
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
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,997,979,910</td>
<td align="right"></td>
<td align="right">1,382,862,133</td>
<td align="right"></td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,770</td>
<td align="right">0.4%</td>
<td align="right">2,763</td>
<td align="right">0.6%</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">261</td>
<td align="right">0.9%</td>
<td align="right">341</td>
<td align="right">1.1%</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">102</td>
<td align="right">0.0%</td>
<td align="right">82</td>
<td align="right">0.0%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">27,744</td>
<td align="right">6.3%</td>
<td align="right">32,233</td>
<td align="right">7.5%</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">202</td>
<td align="right">0.0%</td>
<td align="right">182</td>
<td align="right">0.0%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">630</td>
<td align="right">0.1%</td>
<td align="right">569</td>
<td align="right">0.1%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">233,370</td>
<td align="right">52.7%</td>
<td align="right">213,762</td>
<td align="right">49.9%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">442,870</td>
<td align="right"></td>
<td align="right">428,166</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">47,562</td>
<td align="right">10.7%</td>
<td align="right">46,577</td>
<td align="right">10.9%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">255,407,746,308</td>
<td align="right">6,388.4%</td>
<td align="right">251,456,891,038</td>
<td align="right">18,183.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">133,992</td>
<td align="right">30.3%</td>
<td align="right">135,412</td>
<td align="right">31.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,846</td>
<td align="right">0.4%</td>
<td align="right">1,862</td>
<td align="right">0.4%</td>
<td align="right">0.9%</td>
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
<td align="right">27,744</td>
<td align="right"></td>
<td align="right">32,233</td>
<td align="right"></td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">23,757</td>
<td align="right">85.6%</td>
<td align="right">26,159</td>
<td align="right">81.2%</td>
<td align="right">10.1%</td>
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
<td align="right">1,552,384</td>
<td align="right">0.5%</td>
<td align="right">184,184,832</td>
<td align="right">25.0%</td>
<td align="right">11,764.6%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">261,709,988</td>
<td align="right">82.1%</td>
<td align="right">648,508,424</td>
<td align="right">88.0%</td>
<td align="right">147.8%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">318,951,424</td>
<td align="right"></td>
<td align="right">736,993,280</td>
<td align="right"></td>
<td align="right">131.1%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">6,749,912</td>
<td align="right">2.1%</td>
<td align="right">15,267,208</td>
<td align="right">2.1%</td>
<td align="right">126.2%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">50,491,524</td>
<td align="right">15.8%</td>
<td align="right">73,217,648</td>
<td align="right">9.9%</td>
<td align="right">45.0%</td>
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
<td align="left"><= 4,096</td>
<td align="left">4,847</td>
<td align="right">20.4%</td>
<td align="left">5,476</td>
<td align="right">15.7%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">7,445</td>
<td align="right">31.3%</td>
<td align="left">9,365</td>
<td align="right">26.8%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">7,523</td>
<td align="right">31.7%</td>
<td align="left">8,931</td>
<td align="right">25.6%</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,373</td>
<td align="right">10.0%</td>
<td align="left">5,194</td>
<td align="right">14.9%</td>
<td align="right">118.9%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,509</td>
<td align="right">6.4%</td>
<td align="left">3,818</td>
<td align="right">10.9%</td>
<td align="right">153.0%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">60</td>
<td align="right">0.3%</td>
<td align="left">2,083</td>
<td align="right">6.0%</td>
<td align="right">3,371.7%</td>
</tr>
<tr>
<td align="left"><= 262,144</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">20</td>
<td align="right">0.1%</td>
<td align="right"></td>
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
<td align="left"><= 8</td>
<td align="right">1,299</td>
<td align="right">4.7%</td>
<td align="right">1,289</td>
<td align="right">4.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">693</td>
<td align="right">2.5%</td>
<td align="right">2,607</td>
<td align="right">8.1%</td>
<td align="right">276.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">3,942</td>
<td align="right">14.2%</td>
<td align="right">4,854</td>
<td align="right">15.1%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">9,082</td>
<td align="right">32.7%</td>
<td align="right">9,567</td>
<td align="right">29.7%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">5,407</td>
<td align="right">19.5%</td>
<td align="right">5,513</td>
<td align="right">17.1%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,074</td>
<td align="right">18.3%</td>
<td align="right">6,328</td>
<td align="right">19.6%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,039</td>
<td align="right">7.3%</td>
<td align="right">1,971</td>
<td align="right">6.1%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">208</td>
<td align="right">0.7%</td>
<td align="right">104</td>
<td align="right">0.3%</td>
<td align="right">-50.0%</td>
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
<td align="left"><= 4</td>
<td align="right">732</td>
<td align="right">2.6%</td>
<td align="right">700</td>
<td align="right">2.2%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">708</td>
<td align="right">2.6%</td>
<td align="right">1,250</td>
<td align="right">3.9%</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,133</td>
<td align="right">7.7%</td>
<td align="right">2,575</td>
<td align="right">8.0%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">8,645</td>
<td align="right">31.2%</td>
<td align="right">9,816</td>
<td align="right">30.5%</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">6,354</td>
<td align="right">22.9%</td>
<td align="right">6,183</td>
<td align="right">19.2%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,675</td>
<td align="right">9.6%</td>
<td align="right">3,084</td>
<td align="right">9.6%</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,084</td>
<td align="right">7.5%</td>
<td align="right">2,212</td>
<td align="right">6.9%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">426</td>
<td align="right">1.5%</td>
<td align="right">339</td>
<td align="right">1.1%</td>
<td align="right">-20.4%</td>
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
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">151,860</td>
<td align="right">38,320</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">5,596,494</td>
<td align="right">1,511,344</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,963,188,021</td>
<td align="right">1,348,260,841</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,997,979,910</td>
<td align="right">1,382,862,133</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,463,090,898</td>
<td align="right">3,628,587,336</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">49,127,463</td>
<td align="right">28,467,378</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">13,970,555</td>
<td align="right">9,062,445</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">83,680,123</td>
<td align="right">63,017,803</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">182,726,042</td>
<td align="right">225,457,674</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">73,695,044</td>
<td align="right">57,174,445</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">351,155,516</td>
<td align="right">275,797,555</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,528,543</td>
<td align="right">1,281,179</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">147,539,888</td>
<td align="right">126,501,903</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">204,876,433</td>
<td align="right">232,766,051</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">499,951,980</td>
<td align="right">566,579,630</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">40,237,291</td>
<td align="right">35,666,595</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">42,981,223</td>
<td align="right">38,414,379</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">366,404,021</td>
<td align="right">402,574,184</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">57,155,142</td>
<td align="right">51,868,805</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">179,539,695</td>
<td align="right">163,318,262</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">41,564,461</td>
<td align="right">38,093,256</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">57,693,716</td>
<td align="right">52,962,723</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">245,266,431</td>
<td align="right">264,884,722</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">672,308,315</td>
<td align="right">725,300,090</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">103,226,860</td>
<td align="right">95,254,682</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">231,491,208</td>
<td align="right">249,302,404</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">101,725,720</td>
<td align="right">94,020,962</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">101,725,720</td>
<td align="right">94,020,962</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">273,268,816</td>
<td align="right">292,592,590</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">73,375,094</td>
<td align="right">78,560,336</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">273,484,876</td>
<td align="right">292,808,650</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">6,133,360</td>
<td align="right">5,756,980</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">143,096</td>
<td align="right">134,318</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">104,179,751</td>
<td align="right">97,860,445</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">264,044,051</td>
<td align="right">248,589,869</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">266,435,091</td>
<td align="right">250,980,909</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">449,359,163</td>
<td align="right">425,993,642</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">345,462,060</td>
<td align="right">363,090,885</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">313,642,312</td>
<td align="right">298,147,947</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,366,565</td>
<td align="right">3,530,365</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,560</td>
<td align="right">49,968,360</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,560</td>
<td align="right">49,968,360</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">555,365,575</td>
<td align="right">580,993,869</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">234,346,266</td>
<td align="right">223,942,062</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">3,115,071,348</td>
<td align="right">3,247,646,938</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,147,568,543</td>
<td align="right">1,101,307,123</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">756,871,015</td>
<td align="right">786,633,391</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,302,710,883</td>
<td align="right">1,252,027,290</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,315,410,934</td>
<td align="right">1,264,698,875</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,315,410,934</td>
<td align="right">1,264,698,875</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,461,070,808</td>
<td align="right">6,707,327,472</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">7,945,000</td>
<td align="right">7,647,540</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">53,749,735</td>
<td align="right">55,736,955</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,235,587,718</td>
<td align="right">1,190,079,921</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,227,005,859</td>
<td align="right">1,182,109,246</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">300,707,892</td>
<td align="right">289,742,877</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">229,826</td>
<td align="right">222,098</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">726,049</td>
<td align="right">749,771</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">674,647,135</td>
<td align="right">653,032,929</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,296,585,547</td>
<td align="right">1,256,740,255</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">412,294,220</td>
<td align="right">399,631,430</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,013,299,367</td>
<td align="right">984,808,797</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,013,444,567</td>
<td align="right">984,960,997</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">415,077,867</td>
<td align="right">426,474,115</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,087,330,872</td>
<td align="right">2,031,464,580</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">159,965,439</td>
<td align="right">164,237,289</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,517,279,623</td>
<td align="right">1,477,262,871</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,517,100,469</td>
<td align="right">1,477,247,823</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">312,331,476</td>
<td align="right">304,163,663</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">837,518,241</td>
<td align="right">858,248,693</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,883,748,146</td>
<td align="right">2,954,106,334</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">956,144,225</td>
<td align="right">932,939,992</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">53,749,735</td>
<td align="right">55,050,235</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">31,486,032</td>
<td align="right">30,725,921</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">31,486,032</td>
<td align="right">30,725,921</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">11,122,805</td>
<td align="right">11,390,513</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,744,100</td>
<td align="right">2,678,400</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">66,198,654</td>
<td align="right">64,630,413</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,055,148,760</td>
<td align="right">5,173,463,407</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">15,561</td>
<td align="right">15,921</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,910,205,756</td>
<td align="right">4,000,586,983</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">155,428,015</td>
<td align="right">151,890,288</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">43,824,863</td>
<td align="right">42,880,337</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,100,500</td>
<td align="right">3,034,740</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,848,503,937</td>
<td align="right">3,929,410,102</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">76,910,740</td>
<td align="right">78,491,467</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,413,344,476</td>
<td align="right">4,330,028,273</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,229,474,434</td>
<td align="right">1,251,247,484</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">8,085,333</td>
<td align="right">8,226,821</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,400,763,153</td>
<td align="right">2,439,911,667</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,482</td>
<td align="right">71,496,911</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,482</td>
<td align="right">71,496,911</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">38,457,360</td>
<td align="right">39,041,440</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">689,563,177</td>
<td align="right">679,115,877</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">4,210,295,764</td>
<td align="right">4,146,614,671</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">12,505,259</td>
<td align="right">12,684,876</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,616,961,486</td>
<td align="right">3,565,085,776</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,860,538,531</td>
<td align="right">1,833,894,873</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,593,190</td>
<td align="right">45,936,194</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">48,051,000</td>
<td align="right">47,394,002</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">105,632,713</td>
<td align="right">104,197,466</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">397,194,088</td>
<td align="right">391,868,200</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">47,940,450</td>
<td align="right">47,301,008</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,124,375,618</td>
<td align="right">1,109,629,472</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">7,112,859,661</td>
<td align="right">7,200,712,347</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">451,847,726</td>
<td align="right">446,868,643</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">453,122,112</td>
<td align="right">448,273,379</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">56,037,776</td>
<td align="right">55,457,236</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">531,854,629</td>
<td align="right">526,686,658</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,152,036,781</td>
<td align="right">1,141,303,055</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">32,672,264</td>
<td align="right">32,371,040</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">103,838,603</td>
<td align="right">102,894,077</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">8,000,549,468</td>
<td align="right">8,067,966,264</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">868,176,501</td>
<td align="right">861,053,323</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,334,050,247</td>
<td align="right">1,344,933,258</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">810,046,525</td>
<td align="right">816,575,190</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,802,235,210</td>
<td align="right">1,788,578,654</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,465,409,958</td>
<td align="right">1,476,359,069</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,075,332,255</td>
<td align="right">1,067,374,935</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,211,505,515</td>
<td align="right">1,220,407,108</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">309,921,166</td>
<td align="right">307,826,743</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">79,741,313</td>
<td align="right">80,273,369</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">169,548,729</td>
<td align="right">168,449,555</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,848,573,774</td>
<td align="right">1,836,916,566</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">743,999,642</td>
<td align="right">739,454,696</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,960,892,956</td>
<td align="right">1,948,949,066</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,666,424,074</td>
<td align="right">1,656,305,261</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,762,397,470</td>
<td align="right">3,785,077,941</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">419,919,993</td>
<td align="right">417,464,212</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">155,441,812</td>
<td align="right">154,560,047</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">37,549,647</td>
<td align="right">37,338,585</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">20,170,982</td>
<td align="right">20,058,584</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">148,459,028</td>
<td align="right">147,639,285</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">34,771,716</td>
<td align="right">34,581,119</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,462,360,113</td>
<td align="right">4,438,036,327</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,224,094,264</td>
<td align="right">2,212,046,434</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">731,032,633</td>
<td align="right">727,259,071</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,621,434,519</td>
<td align="right">1,613,771,940</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">73,770,000</td>
<td align="right">73,443,520</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">564,799,171</td>
<td align="right">562,403,773</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,012,971,147</td>
<td align="right">1,008,760,980</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">659,344,263</td>
<td align="right">656,909,961</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">169,308,989</td>
<td align="right">168,702,389</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">498,487,103</td>
<td align="right">496,739,789</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,996,181,579</td>
<td align="right">4,009,312,403</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">103,178,820</td>
<td align="right">103,479,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">49,308,441</td>
<td align="right">49,449,949</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">771,680,613</td>
<td align="right">769,473,091</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,587,184,183</td>
<td align="right">1,591,652,043</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,792,560</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">585,073,171</td>
<td align="right">583,745,270</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">12,700,051</td>
<td align="right">12,671,585</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">12,700,051</td>
<td align="right">12,671,585</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">358,301,634</td>
<td align="right">357,513,553</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">179,610,526</td>
<td align="right">180,002,045</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">4,208,676</td>
<td align="right">4,200,948</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">982,575,548</td>
<td align="right">980,786,456</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">975,799,827</td>
<td align="right">974,060,975</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">416,633,951</td>
<td align="right">417,366,453</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">118,898,799</td>
<td align="right">118,723,631</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,266,619,200</td>
<td align="right">1,268,281,031</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">504,702,136</td>
<td align="right">505,347,104</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">34,359,942</td>
<td align="right">34,401,833</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">114,059,737</td>
<td align="right">114,195,208</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">131,031,817</td>
<td align="right">130,901,475</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">45,428,774</td>
<td align="right">45,383,858</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">597,053,787</td>
<td align="right">596,477,784</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,188,407,620</td>
<td align="right">1,189,528,797</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">39,142,323,335</td>
<td align="right">39,106,532,200</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">608,672,214</td>
<td align="right">608,122,329</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">24,484,641</td>
<td align="right">24,462,712</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">24,484,641</td>
<td align="right">24,462,712</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">44,313,440,492</td>
<td align="right">44,352,793,144</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">120,274,293</td>
<td align="right">120,375,212</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">360,332,644</td>
<td align="right">360,037,693</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">154,523,739</td>
<td align="right">154,636,915</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">469,892,962</td>
<td align="right">469,588,611</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,755,287,371</td>
<td align="right">1,754,385,161</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">262,312,359</td>
<td align="right">262,182,703</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,532,111</td>
<td align="right">5,534,734</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,111,656,248</td>
<td align="right">4,113,465,787</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">455,387,801</td>
<td align="right">455,550,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">455,387,801</td>
<td align="right">455,550,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">7,742,631</td>
<td align="right">7,745,254</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,480,739,651</td>
<td align="right">1,480,247,997</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,200,525,021</td>
<td align="right">1,200,910,350</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,873,905,235</td>
<td align="right">2,873,152,846</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">434,026,728</td>
<td align="right">434,136,264</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,280,252,527</td>
<td align="right">2,279,743,737</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">39,828,020</td>
<td align="right">39,835,978</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,345,425,105</td>
<td align="right">1,345,161,123</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">40,595,804</td>
<td align="right">40,603,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,545,778</td>
<td align="right">1,545,524</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">445,742,672</td>
<td align="right">445,684,859</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">445,742,672</td>
<td align="right">445,684,859</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">3,709,046</td>
<td align="right">3,708,686</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,026,013</td>
<td align="right">40,022,791</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,225,170,690</td>
<td align="right">1,225,239,459</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">37,152,077</td>
<td align="right">37,151,615</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">43,582,286</td>
<td align="right">43,581,802</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,975,980</td>
<td align="right">2,975,960</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,975,980</td>
<td align="right">2,975,960</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,159,872</td>
<td align="right">6,159,851</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,998,348,066</td>
<td align="right">1,998,341,812</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">20,612,164</td>
<td align="right">20,612,183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,079</td>
<td align="right">47,071,059</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">143,590,097</td>
<td align="right">143,590,077</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">263,905,177</td>
<td align="right">263,905,177</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,013,740</td>
<td align="right">60,013,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">8,323,320</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,635,678</td>
<td align="right">4,635,678</td>
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
<td align="right">2,351,667</td>
<td align="right">2,351,667</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">27,762</td>
<td align="right">27,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">26,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">20,173</td>
<td align="right">20,173</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">62</td>
<td align="right">62</td>
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
<td align="right">1,803</td>
<td align="right">503</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">23,635</td>
<td align="right">23,607</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right">23,001</td>
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
<td align="right">101</td>
<td align="right">141</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">101</td>
<td align="right">141</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,592</td>
<td align="right">22,592</td>
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
<td align="right">34</td>
<td align="right">34</td>
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
<td align="right">41</td>
<td align="right">41</td>
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
<td align="right">2,439</td>
<td align="right">2,439</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-05-13
