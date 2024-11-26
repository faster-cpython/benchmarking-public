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
<td align="right">1,418,360</td>
<td align="right">251,381,501</td>
<td align="right">17,623.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">332,641,580</td>
<td align="right">1,564,560,136</td>
<td align="right">370.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">103,822,258</td>
<td align="right">7,840,418</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">111,480,649</td>
<td align="right">15,662,269</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">56,231,933</td>
<td align="right">8,403,193</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,519,623</td>
<td align="right">1,209,743</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">50,021,947</td>
<td align="right">18,529,854</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,141,317</td>
<td align="right">32,630,021</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">275,117,863</td>
<td align="right">134,857,473</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,436,613</td>
<td align="right">2,537,304</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">93,339,285</td>
<td align="right">60,607,683</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">551,620</td>
<td align="right">358,840</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">338,854,918</td>
<td align="right">222,764,900</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,571,840</td>
<td align="right">2,406,640</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">276,934,751</td>
<td align="right">188,809,338</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">346,663,656</td>
<td align="right">242,670,661</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">410,170,542</td>
<td align="right">291,375,163</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">197,308,885</td>
<td align="right">140,918,087</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">150,513,697</td>
<td align="right">109,741,217</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">103,612,666</td>
<td align="right">76,066,170</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">90,962,818</td>
<td align="right">67,238,977</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">717,420,024</td>
<td align="right">538,617,706</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">52,686,649</td>
<td align="right">39,911,930</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">128,480,652</td>
<td align="right">97,515,762</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,096,423</td>
<td align="right">137,924,790</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">955,608,020</td>
<td align="right">730,661,154</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">245,686,072</td>
<td align="right">192,861,622</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,218,460,245</td>
<td align="right">1,777,462,160</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">434,670,048</td>
<td align="right">349,723,341</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,893,311</td>
<td align="right">2,329,250</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">136,771,828</td>
<td align="right">110,768,341</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">370,420,245</td>
<td align="right">300,171,955</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,723,128,728</td>
<td align="right">3,067,238,929</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,638,076,022</td>
<td align="right">1,355,551,775</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">189,625,287</td>
<td align="right">157,198,790</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">522,836,702</td>
<td align="right">433,438,597</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,575,351,290</td>
<td align="right">3,809,576,526</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">305,325,050</td>
<td align="right">255,038,613</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">107,214,373</td>
<td align="right">89,930,967</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,601,173,684</td>
<td align="right">2,203,749,693</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,648,354,163</td>
<td align="right">3,100,920,790</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,943,358,219</td>
<td align="right">1,655,867,901</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">807,891,717</td>
<td align="right">690,185,986</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,556,510,161</td>
<td align="right">2,196,327,045</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">354,316,223</td>
<td align="right">305,701,437</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">53,697,099</td>
<td align="right">46,359,390</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,713,810,401</td>
<td align="right">3,229,323,752</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">251,195,176</td>
<td align="right">219,028,559</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">84,393,076</td>
<td align="right">73,969,237</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,688,051</td>
<td align="right">90,899,867</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">238,747,252</td>
<td align="right">210,033,420</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,286,581,033</td>
<td align="right">13,505,173,620</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">301,792,347</td>
<td align="right">267,925,939</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">103,232,672</td>
<td align="right">91,888,006</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">56,247,678</td>
<td align="right">50,071,953</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">533,180,920</td>
<td align="right">479,259,393</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">226,040,479</td>
<td align="right">203,195,420</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">474,417,773</td>
<td align="right">426,520,175</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,289,863,491</td>
<td align="right">3,861,464,183</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">187,396,264</td>
<td align="right">168,897,860</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">91,862,781</td>
<td align="right">82,910,013</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">524,941</td>
<td align="right">474,548</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">764,984,003</td>
<td align="right">692,252,057</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,829,208,635</td>
<td align="right">2,565,684,152</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">180,452,986</td>
<td align="right">163,702,166</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">33,636,138</td>
<td align="right">30,669,778</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,727,995</td>
<td align="right">7,995,965</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,289,042,952</td>
<td align="right">1,185,829,335</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,530,480,005</td>
<td align="right">4,202,515,259</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">223,103</td>
<td align="right">239,054</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">154,240,279</td>
<td align="right">163,276,693</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">127,244,588</td>
<td align="right">120,266,834</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">218,503,118</td>
<td align="right">206,573,238</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">35,728,091</td>
<td align="right">33,910,345</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">150,191,899</td>
<td align="right">142,930,011</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,409,520</td>
<td align="right">89,034,086</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">744,032,575</td>
<td align="right">712,026,898</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">196,482,922</td>
<td align="right">188,210,380</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,454,383,458</td>
<td align="right">2,357,411,161</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,792,972,086</td>
<td align="right">1,723,514,642</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">151,663,207</td>
<td align="right">145,827,752</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">170,384,667</td>
<td align="right">164,658,183</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">190,131,184</td>
<td align="right">184,624,918</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">367,643,450</td>
<td align="right">357,185,494</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">62,071,559</td>
<td align="right">60,574,541</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">575,725,214</td>
<td align="right">589,021,474</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">120,055,837</td>
<td align="right">122,771,842</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">119,859,638</td>
<td align="right">117,265,347</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">340,903,631</td>
<td align="right">347,762,623</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,422,111</td>
<td align="right">10,233,933</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">76,943,115</td>
<td align="right">75,825,749</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">56,019,062</td>
<td align="right">55,250,291</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">423,616,795</td>
<td align="right">429,251,687</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">76,073,911</td>
<td align="right">75,067,242</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">566,681,778</td>
<td align="right">559,513,590</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,016,475,106</td>
<td align="right">1,005,169,298</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">98,765,985</td>
<td align="right">97,707,577</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">58,580</td>
<td align="right">59,160</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">197,256,053</td>
<td align="right">195,327,920</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">27,659,061</td>
<td align="right">27,405,314</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">451,268,909</td>
<td align="right">447,756,864</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">183,315,307</td>
<td align="right">181,889,931</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,347,086</td>
<td align="right">37,571,879</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,922,787</td>
<td align="right">2,937,849</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">28,234,038</td>
<td align="right">28,093,022</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,554,918</td>
<td align="right">57,312,855</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">61,416,896</td>
<td align="right">61,168,821</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,209,043</td>
<td align="right">9,245,799</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">254,923,616</td>
<td align="right">255,918,264</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,257,339</td>
<td align="right">1,262,076</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,464,948</td>
<td align="right">3,453,668</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">394,321,511</td>
<td align="right">395,556,521</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,026,984</td>
<td align="right">141,426,052</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,337,603</td>
<td align="right">10,365,683</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">107,385,789</td>
<td align="right">107,111,687</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,257,978,724</td>
<td align="right">2,263,473,256</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,447,242</td>
<td align="right">47,562,117</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">43,622,911</td>
<td align="right">43,521,023</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">43,952,508</td>
<td align="right">44,042,885</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,053,111,782</td>
<td align="right">1,050,964,082</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">71,226,284</td>
<td align="right">71,100,298</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">267,887</td>
<td align="right">268,273</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">65,073,268</td>
<td align="right">64,986,193</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">12,873,899</td>
<td align="right">12,888,266</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">8,541,633</td>
<td align="right">8,547,659</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">52,146,047</td>
<td align="right">52,182,558</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">331,655,452</td>
<td align="right">331,858,125</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,775,781</td>
<td align="right">18,786,828</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">618,149,548</td>
<td align="right">618,503,271</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">58,915,420</td>
<td align="right">58,947,273</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">16,223,706</td>
<td align="right">16,230,808</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">53,164,521</td>
<td align="right">53,141,520</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,996,018</td>
<td align="right">10,999,621</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">45,240,425</td>
<td align="right">45,228,883</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">33,170,872</td>
<td align="right">33,163,293</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,404,054</td>
<td align="right">198,367,650</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,079,046</td>
<td align="right">22,082,981</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,558,516</td>
<td align="right">402,627,845</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,372,069,061</td>
<td align="right">1,372,300,997</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,744,059</td>
<td align="right">3,744,582</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,035,008</td>
<td align="right">9,036,244</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">43,448,703</td>
<td align="right">43,443,447</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,354,076</td>
<td align="right">20,356,103</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">720,519</td>
<td align="right">720,466</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,167</td>
<td align="right">15,166</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,257,684</td>
<td align="right">11,257,051</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">88,069,016</td>
<td align="right">88,072,590</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,585,851</td>
<td align="right">3,585,729</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,460,936</td>
<td align="right">82,463,552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">66,760</td>
<td align="right">66,758</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,387,273</td>
<td align="right">21,387,032</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,395,614</td>
<td align="right">21,395,373</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,081,200</td>
<td align="right">21,080,965</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,029,431</td>
<td align="right">35,029,782</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">44,067,674</td>
<td align="right">44,067,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,829,451</td>
<td align="right">5,829,429</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">70,945,715</td>
<td align="right">70,945,892</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">14,931,966</td>
<td align="right">14,931,950</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">102,113,866</td>
<td align="right">102,113,780</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,999,712</td>
<td align="right">146,999,656</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,166,121</td>
<td align="right">268,166,093</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">10,774,139</td>
<td align="right">10,774,138</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,398,830</td>
<td align="right">173,398,822</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,103,986</td>
<td align="right">402,103,974</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,010,785</td>
<td align="right">225,010,781</td>
<td align="right">-0.0%</td>
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
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">763,376</td>
<td align="right">763,376</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">642,992</td>
<td align="right">642,992</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,470</td>
<td align="right">173,470</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">157,711</td>
<td align="right">157,711</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">91,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,641</td>
<td align="right">91,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">29,249</td>
<td align="right">29,249</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,686</td>
<td align="right">27,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,656</td>
<td align="right">21,656</td>
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
<td align="right">1,122</td>
<td align="right">1,122</td>
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
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">3</td>
<td align="right">3</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,480,870</td>
<td align="right">0.3%</td>
<td align="right">22,981,730</td>
<td align="right">0.2%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">369,261,440</td>
<td align="right">3.8%</td>
<td align="right">299,093,457</td>
<td align="right">3.1%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,405,389,672</td>
<td align="right">95.9%</td>
<td align="right">9,400,336,914</td>
<td align="right">96.7%</td>
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
<td align="right">598,424</td>
<td align="right">34.9%</td>
<td align="right">475,971</td>
<td align="right">31.5%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,116,461</td>
<td align="right">65.1%</td>
<td align="right">1,036,007</td>
<td align="right">68.5%</td>
<td align="right">-7.2%</td>
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
<td align="right">8,549</td>
<td align="right">0.8%</td>
<td align="right">4,068</td>
<td align="right">0.4%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,583</td>
<td align="right">7.3%</td>
<td align="right">62,343</td>
<td align="right">6.0%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">49,198</td>
<td align="right">4.4%</td>
<td align="right">37,729</td>
<td align="right">3.6%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,468</td>
<td align="right">0.8%</td>
<td align="right">6,947</td>
<td align="right">0.7%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,830</td>
<td align="right">0.3%</td>
<td align="right">2,389</td>
<td align="right">0.2%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">6,725</td>
<td align="right">0.6%</td>
<td align="right">5,684</td>
<td align="right">0.5%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,620</td>
<td align="right">0.5%</td>
<td align="right">4,833</td>
<td align="right">0.5%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">47,034</td>
<td align="right">4.2%</td>
<td align="right">42,235</td>
<td align="right">4.1%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,612</td>
<td align="right">2.8%</td>
<td align="right">29,572</td>
<td align="right">2.9%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,606</td>
<td align="right">70.0%</td>
<td align="right">747,704</td>
<td align="right">72.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,742</td>
<td align="right">0.9%</td>
<td align="right">9,442</td>
<td align="right">0.9%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,723</td>
<td align="right">0.2%</td>
<td align="right">2,643</td>
<td align="right">0.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,805</td>
<td align="right">1.0%</td>
<td align="right">10,544</td>
<td align="right">1.0%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,580</td>
<td align="right">0.2%</td>
<td align="right">2,620</td>
<td align="right">0.3%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">31,668</td>
<td align="right">2.8%</td>
<td align="right">31,516</td>
<td align="right">3.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">19,959</td>
<td align="right">1.8%</td>
<td align="right">19,983</td>
<td align="right">1.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">835</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,522</td>
<td align="right">1.3%</td>
<td align="right">14,519</td>
<td align="right">1.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">401</td>
<td align="right">0.0%</td>
<td align="right">401</td>
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
<td align="right">181,096,423</td>
<td align="right">100.0%</td>
<td align="right">137,924,790</td>
<td align="right">100.0%</td>
<td align="right">-23.8%</td>
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
<td align="right">474,147,883</td>
<td align="right">7.1%</td>
<td align="right">426,262,081</td>
<td align="right">6.4%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,792,417</td>
<td align="right">0.1%</td>
<td align="right">4,792,395</td>
<td align="right">0.1%</td>
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
<td align="right">6,201,935,947</td>
<td align="right">92.8%</td>
<td align="right">6,201,936,783</td>
<td align="right">93.5%</td>
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
<td align="right">178,249</td>
<td align="right">49.5%</td>
<td align="right">166,438</td>
<td align="right">47.8%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,602</td>
<td align="right">50.5%</td>
<td align="right">181,617</td>
<td align="right">52.2%</td>
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
<td align="left">buffer int</td>
<td align="right">21,331</td>
<td align="right">12.0%</td>
<td align="right">12,371</td>
<td align="right">7.4%</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">26,640</td>
<td align="right">14.9%</td>
<td align="right">25,440</td>
<td align="right">15.3%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">58,345</td>
<td align="right">32.7%</td>
<td align="right">56,545</td>
<td align="right">34.0%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">820</td>
<td align="right">0.5%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">940</td>
<td align="right">0.5%</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">125</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">65,328</td>
<td align="right">36.6%</td>
<td align="right">65,438</td>
<td align="right">39.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">2.4%</td>
<td align="right">4,300</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
<td align="right">144,724,298</td>
<td align="right">1.1%</td>
<td align="right">130,716,418</td>
<td align="right">1.0%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,511,076,693</td>
<td align="right">98.9%</td>
<td align="right">13,559,404,652</td>
<td align="right">99.0%</td>
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
<td align="right">714,420</td>
<td align="right">0.0%</td>
<td align="right">716,774</td>
<td align="right">0.0%</td>
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
<td align="right">32,060</td>
<td align="right">0.0%</td>
<td align="right">32,060</td>
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
<td align="right">3,305,907</td>
<td align="right">100.0%</td>
<td align="right">3,044,085</td>
<td align="right">100.0%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">363</td>
<td align="right">0.0%</td>
<td align="right">363</td>
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
<td align="left">init not inline values</td>
<td align="right">2,829</td>
<td align="right">779.3%</td>
<td align="right">2,829</td>
<td align="right">779.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,003</td>
<td align="right">551.8%</td>
<td align="right">2,003</td>
<td align="right">551.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">921</td>
<td align="right">253.7%</td>
<td align="right">921</td>
<td align="right">253.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">363</td>
<td align="right">100.0%</td>
<td align="right">363</td>
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
<td align="right">36,415</td>
<td align="right">7.3%</td>
<td align="right">36,413</td>
<td align="right">7.3%</td>
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
<td align="right">435,240</td>
<td align="right">86.7%</td>
<td align="right">435,240</td>
<td align="right">86.7%</td>
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
<td align="right">1,227,590</td>
<td align="right">0.0%</td>
<td align="right">965,471</td>
<td align="right">0.0%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">103,472,010</td>
<td align="right">1.8%</td>
<td align="right">90,699,137</td>
<td align="right">1.6%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,723,391,517</td>
<td align="right">98.2%</td>
<td align="right">5,733,753,711</td>
<td align="right">98.4%</td>
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
<td align="left">Failure</td>
<td align="right">160,795</td>
<td align="right">67.3%</td>
<td align="right">145,505</td>
<td align="right">66.6%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">78,061</td>
<td align="right">32.7%</td>
<td align="right">73,120</td>
<td align="right">33.4%</td>
<td align="right">-6.3%</td>
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
<td align="right">47,898</td>
<td align="right">29.8%</td>
<td align="right">38,309</td>
<td align="right">26.3%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,513</td>
<td align="right">9.0%</td>
<td align="right">11,613</td>
<td align="right">8.0%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">29,770</td>
<td align="right">18.5%</td>
<td align="right">27,063</td>
<td align="right">18.6%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">980</td>
<td align="right">0.7%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,555</td>
<td align="right">1.0%</td>
<td align="right">1,525</td>
<td align="right">1.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,540</td>
<td align="right">2.2%</td>
<td align="right">3,500</td>
<td align="right">2.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,420</td>
<td align="right">10.8%</td>
<td align="right">17,386</td>
<td align="right">11.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,189</td>
<td align="right">11.9%</td>
<td align="right">19,169</td>
<td align="right">13.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,080</td>
<td align="right">7.5%</td>
<td align="right">12,090</td>
<td align="right">8.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">6.6%</td>
<td align="right">10,680</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,700</td>
<td align="right">1.7%</td>
<td align="right">2,700</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">490</td>
<td align="right">0.3%</td>
<td align="right">490</td>
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
<td align="right">2,544,260</td>
<td align="right">0.1%</td>
<td align="right">1,807,380</td>
<td align="right">0.1%</td>
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
<td align="right">35,643,915</td>
<td align="right">1.4%</td>
<td align="right">33,826,349</td>
<td align="right">1.3%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,486,689,257</td>
<td align="right">98.5%</td>
<td align="right">2,487,421,131</td>
<td align="right">98.6%</td>
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
<td align="right">61,099</td>
<td align="right">46.3%</td>
<td align="right">47,199</td>
<td align="right">40.0%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">70,997</td>
<td align="right">53.7%</td>
<td align="right">70,817</td>
<td align="right">60.0%</td>
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
<td align="left">str</td>
<td align="right">14,322</td>
<td align="right">20.2%</td>
<td align="right">14,162</td>
<td align="right">20.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,470</td>
<td align="right">20.4%</td>
<td align="right">14,370</td>
<td align="right">20.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,195</td>
<td align="right">38.3%</td>
<td align="right">27,277</td>
<td align="right">38.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,010</td>
<td align="right">21.1%</td>
<td align="right">15,008</td>
<td align="right">21.2%</td>
<td align="right">-0.0%</td>
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
<td align="right">76,792,980</td>
<td align="right">12.5%</td>
<td align="right">75,676,823</td>
<td align="right">12.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">533,022,920</td>
<td align="right">86.4%</td>
<td align="right">527,183,918</td>
<td align="right">86.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,744,051</td>
<td align="right">1.1%</td>
<td align="right">6,712,382</td>
<td align="right">1.1%</td>
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
<td align="left">Failure</td>
<td align="right">101,306</td>
<td align="right">36.6%</td>
<td align="right">99,932</td>
<td align="right">36.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">175,771</td>
<td align="right">63.4%</td>
<td align="right">175,314</td>
<td align="right">63.7%</td>
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
<td align="left">enumerate</td>
<td align="right">10,837</td>
<td align="right">10.7%</td>
<td align="right">11,295</td>
<td align="right">11.3%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,710</td>
<td align="right">36.2%</td>
<td align="right">35,178</td>
<td align="right">35.2%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,047</td>
<td align="right">10.9%</td>
<td align="right">10,668</td>
<td align="right">10.7%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,565</td>
<td align="right">6.5%</td>
<td align="right">6,625</td>
<td align="right">6.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,981</td>
<td align="right">3.9%</td>
<td align="right">4,001</td>
<td align="right">4.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">618</td>
<td align="right">0.6%</td>
<td align="right">617</td>
<td align="right">0.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,602</td>
<td align="right">7.5%</td>
<td align="right">7,602</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,737</td>
<td align="right">6.7%</td>
<td align="right">6,737</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,222</td>
<td align="right">5.2%</td>
<td align="right">5,222</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,936</td>
<td align="right">4.9%</td>
<td align="right">4,936</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,464</td>
<td align="right">3.4%</td>
<td align="right">3,464</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,547</td>
<td align="right">2.5%</td>
<td align="right">2,547</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.3%</td>
<td align="right">280</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,289,180</td>
<td align="right">0.0%</td>
<td align="right">1,404,760</td>
<td align="right">0.0%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">306,171,717</td>
<td align="right">1.9%</td>
<td align="right">322,034,030</td>
<td align="right">2.0%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">421,498,239</td>
<td align="right">2.6%</td>
<td align="right">427,129,677</td>
<td align="right">2.6%</td>
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
<td align="right">15,532,803,090</td>
<td align="right">95.5%</td>
<td align="right">15,540,034,837</td>
<td align="right">95.4%</td>
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
<td align="right">7,409,354</td>
<td align="right">94.3%</td>
<td align="right">7,710,649</td>
<td align="right">94.5%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">451,353</td>
<td align="right">5.7%</td>
<td align="right">452,642</td>
<td align="right">5.5%</td>
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
<td align="right">80,409</td>
<td align="right">17.8%</td>
<td align="right">81,910</td>
<td align="right">18.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,924</td>
<td align="right">0.6%</td>
<td align="right">2,944</td>
<td align="right">0.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">87,951</td>
<td align="right">19.5%</td>
<td align="right">87,368</td>
<td align="right">19.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,425</td>
<td align="right">1.2%</td>
<td align="right">5,403</td>
<td align="right">1.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">32,255</td>
<td align="right">7.1%</td>
<td align="right">32,360</td>
<td align="right">7.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">138,613</td>
<td align="right">30.7%</td>
<td align="right">138,823</td>
<td align="right">30.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">15,275</td>
<td align="right">3.4%</td>
<td align="right">15,286</td>
<td align="right">3.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">27,499</td>
<td align="right">6.1%</td>
<td align="right">27,508</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">14,253</td>
<td align="right">3.2%</td>
<td align="right">14,251</td>
<td align="right">3.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">20,880</td>
<td align="right">4.6%</td>
<td align="right">20,880</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">5,300</td>
<td align="right">1.2%</td>
<td align="right">5,300</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">2,754</td>
<td align="right">0.6%</td>
<td align="right">2,754</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2,542</td>
<td align="right">0.6%</td>
<td align="right">2,542</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.3%</td>
<td align="right">1,140</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">680</td>
<td align="right">0.2%</td>
<td align="right">680</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
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
<td align="right">4,484,375,212</td>
<td align="right">99.5%</td>
<td align="right">3,812,664,537</td>
<td align="right">99.5%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">389,403</td>
<td align="right">0.0%</td>
<td align="right">393,119</td>
<td align="right">0.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,236</td>
<td align="right">0.0%</td>
<td align="right">9,234</td>
<td align="right">0.0%</td>
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
<td align="right">19,893,825</td>
<td align="right">0.4%</td>
<td align="right">19,894,820</td>
<td align="right">0.5%</td>
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
<td align="right">465,917</td>
<td align="right">100.0%</td>
<td align="right">467,012</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
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
<td align="right">86,133,543</td>
<td align="right">100.0%</td>
<td align="right">86,147,700</td>
<td align="right">100.0%</td>
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
<td align="right">7,626</td>
<td align="right">0.0%</td>
<td align="right">7,625</td>
<td align="right">0.0%</td>
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
<td align="right">7,541</td>
<td align="right">100.0%</td>
<td align="right">7,541</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,334,099</td>
<td align="right">18.1%</td>
<td align="right">173,334,091</td>
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
<td align="right">786,232,606</td>
<td align="right">81.9%</td>
<td align="right">786,232,570</td>
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
<td align="right">121,965,101</td>
<td align="right">4.7%</td>
<td align="right">132,235,102</td>
<td align="right">5.0%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,455,270,006</td>
<td align="right">93.6%</td>
<td align="right">2,449,509,728</td>
<td align="right">93.2%</td>
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
<td align="right">45,053,649</td>
<td align="right">1.7%</td>
<td align="right">45,042,007</td>
<td align="right">1.7%</td>
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
<td align="right">2,401,612</td>
<td align="right">96.6%</td>
<td align="right">2,595,367</td>
<td align="right">96.9%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">83,492</td>
<td align="right">3.4%</td>
<td align="right">83,570</td>
<td align="right">3.1%</td>
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
<td align="left">not managed dict</td>
<td align="right">9,775</td>
<td align="right">11.7%</td>
<td align="right">9,813</td>
<td align="right">11.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,363</td>
<td align="right">10.0%</td>
<td align="right">8,383</td>
<td align="right">10.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">31,884</td>
<td align="right">38.2%</td>
<td align="right">31,904</td>
<td align="right">38.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">16,525</td>
<td align="right">19.8%</td>
<td align="right">16,525</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,015</td>
<td align="right">6.0%</td>
<td align="right">5,015</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">5,001</td>
<td align="right">6.0%</td>
<td align="right">5,001</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,185</td>
<td align="right">3.8%</td>
<td align="right">3,185</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">2,100</td>
<td align="right">2.5%</td>
<td align="right">2,100</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">804</td>
<td align="right">1.0%</td>
<td align="right">804</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">780</td>
<td align="right">0.9%</td>
<td align="right">780</td>
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
<td align="right">7,519,623</td>
<td align="right">100.0%</td>
<td align="right">1,209,743</td>
<td align="right">100.0%</td>
<td align="right">-83.9%</td>
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
<td align="right">93,329,418</td>
<td align="right">9.6%</td>
<td align="right">88,954,620</td>
<td align="right">9.2%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">875,240,115</td>
<td align="right">90.4%</td>
<td align="right">875,246,647</td>
<td align="right">90.8%</td>
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
<td align="right">66,772</td>
<td align="right">83.3%</td>
<td align="right">66,136</td>
<td align="right">83.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,370</td>
<td align="right">16.7%</td>
<td align="right">13,370</td>
<td align="right">16.8%</td>
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
<td align="right">1,480</td>
<td align="right">2.2%</td>
<td align="right">1,600</td>
<td align="right">2.4%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">14,160</td>
<td align="right">21.2%</td>
<td align="right">13,120</td>
<td align="right">19.8%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">6,729</td>
<td align="right">10.1%</td>
<td align="right">6,933</td>
<td align="right">10.5%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,520</td>
<td align="right">2.3%</td>
<td align="right">1,540</td>
<td align="right">2.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">42,243</td>
<td align="right">63.3%</td>
<td align="right">42,303</td>
<td align="right">64.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">640</td>
<td align="right">1.0%</td>
<td align="right">640</td>
<td align="right">1.0%</td>
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
<td align="right">150,107,466</td>
<td align="right">2.5%</td>
<td align="right">109,345,160</td>
<td align="right">1.9%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,752,957,783</td>
<td align="right">97.0%</td>
<td align="right">5,731,977,027</td>
<td align="right">97.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,429,017</td>
<td align="right">0.4%</td>
<td align="right">24,378,179</td>
<td align="right">0.4%</td>
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
<td align="right">208,118</td>
<td align="right">24.1%</td>
<td align="right">197,966</td>
<td align="right">23.3%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">654,212</td>
<td align="right">75.9%</td>
<td align="right">653,233</td>
<td align="right">76.7%</td>
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
<td align="left">bytes</td>
<td align="right">19,132</td>
<td align="right">9.2%</td>
<td align="right">7,996</td>
<td align="right">4.0%</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,749</td>
<td align="right">0.8%</td>
<td align="right">1,469</td>
<td align="right">0.7%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">82,860</td>
<td align="right">39.8%</td>
<td align="right">84,482</td>
<td align="right">42.7%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,996</td>
<td align="right">2.9%</td>
<td align="right">6,108</td>
<td align="right">3.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">14,912</td>
<td align="right">7.2%</td>
<td align="right">14,657</td>
<td align="right">7.4%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">7,331</td>
<td align="right">3.5%</td>
<td align="right">7,251</td>
<td align="right">3.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,145</td>
<td align="right">7.8%</td>
<td align="right">16,005</td>
<td align="right">8.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">21,712</td>
<td align="right">10.4%</td>
<td align="right">21,702</td>
<td align="right">11.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">37,258</td>
<td align="right">17.9%</td>
<td align="right">37,273</td>
<td align="right">18.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">683</td>
<td align="right">0.3%</td>
<td align="right">683</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">445,680</td>
<td align="right">0.0%</td>
<td align="right">14,370.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,529,313,828</td>
<td align="right">100.0%</td>
<td align="right">2,055,790,705</td>
<td align="right">100.0%</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">190,705</td>
<td align="right">0.0%</td>
<td align="right">198,645</td>
<td align="right">0.0%</td>
<td align="right">4.2%</td>
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
<td align="right">30,675</td>
<td align="right">94.6%</td>
<td align="right">47,007</td>
<td align="right">96.4%</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,763</td>
<td align="right">5.4%</td>
<td align="right">1,762</td>
<td align="right">3.6%</td>
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
<td align="right">1,116</td>
<td align="right">63.3%</td>
<td align="right">1,115</td>
<td align="right">63.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">21.6%</td>
<td align="right">380</td>
<td align="right">21.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">267</td>
<td align="right">15.1%</td>
<td align="right">267</td>
<td align="right">15.2%</td>
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
<td align="right">30,238,578,693</td>
<td align="right">34.2%</td>
<td align="right">26,925,442,684</td>
<td align="right">33.7%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,157,909,033</td>
<td align="right">2.4%</td>
<td align="right">1,935,056,476</td>
<td align="right">2.4%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">55,254,097,489</td>
<td align="right">62.6%</td>
<td align="right">50,334,803,864</td>
<td align="right">63.0%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">643,145,621</td>
<td align="right">0.7%</td>
<td align="right">648,135,106</td>
<td align="right">0.8%</td>
<td align="right">0.8%</td>
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
<td align="right">150,107,466</td>
<td align="right">7.0%</td>
<td align="right">109,345,160</td>
<td align="right">5.7%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,096,423</td>
<td align="right">8.4%</td>
<td align="right">137,924,790</td>
<td align="right">7.1%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">369,261,440</td>
<td align="right">17.2%</td>
<td align="right">299,093,457</td>
<td align="right">15.5%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,472,010</td>
<td align="right">4.8%</td>
<td align="right">90,699,137</td>
<td align="right">4.7%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">474,147,883</td>
<td align="right">22.0%</td>
<td align="right">426,262,081</td>
<td align="right">22.1%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,329,418</td>
<td align="right">4.3%</td>
<td align="right">88,954,620</td>
<td align="right">4.6%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">76,792,980</td>
<td align="right">3.6%</td>
<td align="right">75,676,823</td>
<td align="right">3.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">421,498,239</td>
<td align="right">19.6%</td>
<td align="right">427,129,677</td>
<td align="right">22.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">45,053,649</td>
<td align="right">2.1%</td>
<td align="right">45,042,007</td>
<td align="right">2.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,334,099</td>
<td align="right">8.1%</td>
<td align="right">173,334,091</td>
<td align="right">9.0%</td>
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
<td align="right">78,771,704</td>
<td align="right">12.2%</td>
<td align="right">64,899,893</td>
<td align="right">10.0%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">98,116,424</td>
<td align="right">15.3%</td>
<td align="right">108,544,264</td>
<td align="right">16.7%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">119,036,821</td>
<td align="right">18.5%</td>
<td align="right">131,541,944</td>
<td align="right">20.3%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,177,240</td>
<td align="right">3.1%</td>
<td align="right">18,706,320</td>
<td align="right">2.9%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,278,458</td>
<td align="right">6.3%</td>
<td align="right">41,587,288</td>
<td align="right">6.4%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">82,234,180</td>
<td align="right">12.8%</td>
<td align="right">83,829,963</td>
<td align="right">12.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,088,343</td>
<td align="right">2.8%</td>
<td align="right">18,325,360</td>
<td align="right">2.8%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">23,844,071</td>
<td align="right">3.7%</td>
<td align="right">23,686,233</td>
<td align="right">3.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">26,513,028</td>
<td align="right">4.1%</td>
<td align="right">26,618,944</td>
<td align="right">4.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,975</td>
<td align="right">4.3%</td>
<td align="right">27,496,923</td>
<td align="right">4.2%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,405,390,469</td>
<td align="right">16.7%</td>
<td align="right">1,410,655,665</td>
<td align="right">16.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,409,838,150</td>
<td align="right">16.7%</td>
<td align="right">1,415,103,346</td>
<td align="right">16.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,261,794,519</td>
<td align="right">26.8%</td>
<td align="right">2,267,289,203</td>
<td align="right">26.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,261,794,519</td>
<td align="right">26.8%</td>
<td align="right">2,267,289,203</td>
<td align="right">26.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,680,227,179</td>
<td align="right">79.2%</td>
<td align="right">6,685,602,149</td>
<td align="right">79.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">851,956,369</td>
<td align="right">10.1%</td>
<td align="right">852,185,857</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,097,669</td>
<td align="right">0.4%</td>
<td align="right">31,098,654</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,169,058,028</td>
<td align="right">73.2%</td>
<td align="right">6,169,169,811</td>
<td align="right">73.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">333,925,400</td>
<td align="right">4.0%</td>
<td align="right">333,928,906</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,753,806</td>
<td align="right">1.0%</td>
<td align="right">84,753,205</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,637,501</td>
<td align="right">3.9%</td>
<td align="right">331,637,273</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,312</td>
<td align="right">2.1%</td>
<td align="right">175,480,382</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,418,012</td>
<td align="right">0.1%</td>
<td align="right">4,418,012</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">29,669</td>
<td align="right">0.0%</td>
<td align="right">29,669</td>
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
<td align="right">15,360,273</td>
<td align="right">0.1%</td>
<td align="right">21,104,842</td>
<td align="right">0.1%</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">92,948,455</td>
<td align="right">0.4%</td>
<td align="right">103,634,231</td>
<td align="right">0.4%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">11,447,098</td>
<td align="right"></td>
<td align="right">12,634,000</td>
<td align="right"></td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">66,853,447</td>
<td align="right"></td>
<td align="right">73,519,858</td>
<td align="right"></td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">58,919,201</td>
<td align="right"></td>
<td align="right">64,401,667</td>
<td align="right"></td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">40,821,313,781</td>
<td align="right">40,821,313,781 / 0 !!</td>
<td align="right">37,362,357,436</td>
<td align="right">37,362,357,436 / 0 !!</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">56,161,456,906</td>
<td align="right">56,161,456,906 / 0 !!</td>
<td align="right">53,766,649,298</td>
<td align="right">53,766,649,298 / 0 !!</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">96,713,808,318</td>
<td align="right">96,713,808,318 / 0 !!</td>
<td align="right">100,353,756,524</td>
<td align="right">100,353,756,524 / 0 !!</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,519,042,831</td>
<td align="right"></td>
<td align="right">13,959,397,105</td>
<td align="right"></td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">103,749,341,977</td>
<td align="right">103,749,341,977 / 0 !!</td>
<td align="right">106,806,484,135</td>
<td align="right">106,806,484,135 / 0 !!</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,818,235,687</td>
<td align="right">52.6%</td>
<td align="right">13,191,676,458</td>
<td align="right">52.8%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,709,926,959</td>
<td align="right">52.1%</td>
<td align="right">13,066,937,385</td>
<td align="right">52.3%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,379,253,998</td>
<td align="right"></td>
<td align="right">2,426,026,082</td>
<td align="right"></td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,567,479,259</td>
<td align="right">47.4%</td>
<td align="right">11,782,198,987</td>
<td align="right">47.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,569,354,396</td>
<td align="right"></td>
<td align="right">11,784,080,260</td>
<td align="right"></td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,700,423,540</td>
<td align="right"></td>
<td align="right">3,706,914,874</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">235,967,307</td>
<td align="right"></td>
<td align="right">235,975,022</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,160</td>
<td align="right">1.4%</td>
<td align="right">3,382,160</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">198,360</td>
<td align="right">0.1%</td>
<td align="right">198,360</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">16,243</td>
<td align="right">0.0%</td>
<td align="right">16,243</td>
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
<td align="right">453,926</td>
<td align="right">112,244,988</td>
<td align="right">19,401,199,116</td>
<td align="right">453,944</td>
<td align="right">112,412,767</td>
<td align="right">19,380,986,431</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">15,360</td>
<td align="right">10,755,840</td>
<td align="right">6,972,535,796</td>
<td align="right">15,360</td>
<td align="right">10,755,840</td>
<td align="right">6,974,338,024</td>
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
<td align="right">1,024</td>
<td align="right">0.1%</td>
<td align="right">31,879</td>
<td align="right">3.5%</td>
<td align="right">3,013.2%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">2,340</td>
<td align="right">0.3%</td>
<td align="right">631.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,912</td>
<td align="right">0.2%</td>
<td align="right">5,953</td>
<td align="right">0.6%</td>
<td align="right">211.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">12,210</td>
<td align="right">1.3%</td>
<td align="right">37,320</td>
<td align="right">4.0%</td>
<td align="right">205.7%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,701</td>
<td align="right">0.4%</td>
<td align="right">6,461</td>
<td align="right">0.7%</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">180,609</td>
<td align="right">20.0%</td>
<td align="right">226,030</td>
<td align="right">24.5%</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">9,434</td>
<td align="right">5.2%</td>
<td align="right">11,592</td>
<td align="right">5.1%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">9,502,794,248</td>
<td align="right"></td>
<td align="right">7,788,166,583</td>
<td align="right"></td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">304,090,308,421</td>
<td align="right">3,200.0%</td>
<td align="right">321,454,474,088</td>
<td align="right">4,127.5%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">722,402</td>
<td align="right">79.8%</td>
<td align="right">690,325</td>
<td align="right">74.8%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">656,925</td>
<td align="right">72.6%</td>
<td align="right">628,324</td>
<td align="right">68.1%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">904,923</td>
<td align="right"></td>
<td align="right">922,308</td>
<td align="right"></td>
<td align="right">1.9%</td>
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
<td align="right">180,609</td>
<td align="right"></td>
<td align="right">226,030</td>
<td align="right"></td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">168,829</td>
<td align="right">93.5%</td>
<td align="right">199,123</td>
<td align="right">88.1%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,553</td>
<td align="right">1.4%</td>
<td align="right">2,621</td>
<td align="right">1.2%</td>
<td align="right">2.7%</td>
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
<td align="right">3,684</td>
<td align="right">2.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">23,289</td>
<td align="right">12.9%</td>
<td align="right">20,860</td>
<td align="right">9.2%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20,690</td>
<td align="right">11.5%</td>
<td align="right">15,379</td>
<td align="right">6.8%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">48,928</td>
<td align="right">27.1%</td>
<td align="right">50,219</td>
<td align="right">22.2%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">40,801</td>
<td align="right">22.6%</td>
<td align="right">49,880</td>
<td align="right">22.1%</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">24,659</td>
<td align="right">13.7%</td>
<td align="right">47,390</td>
<td align="right">21.0%</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">15,299</td>
<td align="right">8.5%</td>
<td align="right">31,775</td>
<td align="right">14.1%</td>
<td align="right">107.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,899</td>
<td align="right">1.6%</td>
<td align="right">8,047</td>
<td align="right">3.6%</td>
<td align="right">177.6%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">360</td>
<td align="right">0.2%</td>
<td align="right">2,480</td>
<td align="right">1.1%</td>
<td align="right">588.9%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">20,142</td>
<td align="right">11.2%</td>
<td align="right">15,839</td>
<td align="right">7.0%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,810</td>
<td align="right">9.3%</td>
<td align="right">11,765</td>
<td align="right">5.2%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">31,226</td>
<td align="right">17.3%</td>
<td align="right">27,219</td>
<td align="right">12.0%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">50,363</td>
<td align="right">27.9%</td>
<td align="right">56,075</td>
<td align="right">24.8%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">30,219</td>
<td align="right">16.7%</td>
<td align="right">42,731</td>
<td align="right">18.9%</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">14,430</td>
<td align="right">8.0%</td>
<td align="right">28,909</td>
<td align="right">12.8%</td>
<td align="right">100.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,899</td>
<td align="right">2.7%</td>
<td align="right">12,465</td>
<td align="right">5.5%</td>
<td align="right">154.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">720</td>
<td align="right">0.4%</td>
<td align="right">4,120</td>
<td align="right">1.8%</td>
<td align="right">472.2%</td>
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
<td align="left">_MAKE_CELL</td>
<td align="right">6,467,384</td>
<td align="right">56,978,361</td>
<td align="right">781.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">25,246,820</td>
<td align="right">102,537,067</td>
<td align="right">306.1%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">35,282,660</td>
<td align="right">131,264,500</td>
<td align="right">272.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,426,799</td>
<td align="right">34,788,172</td>
<td align="right">269.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">36,213,280</td>
<td align="right">132,031,660</td>
<td align="right">264.6%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">18,198,300</td>
<td align="right">66,027,040</td>
<td align="right">262.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">175,979,851</td>
<td align="right">596,700,709</td>
<td align="right">239.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,885</td>
<td align="right">4,456,265</td>
<td align="right">188.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">210,378,782</td>
<td align="right">578,770,982</td>
<td align="right">175.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">203,727,703</td>
<td align="right">540,275,993</td>
<td align="right">165.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">60,881,251</td>
<td align="right">142,537,051</td>
<td align="right">134.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">318,824,187</td>
<td align="right">696,362,278</td>
<td align="right">118.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">50,305,040</td>
<td align="right">92,746,058</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,230,920</td>
<td align="right">3,971,540</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,900,460</td>
<td align="right">80,392,620</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,900,460</td>
<td align="right">80,392,620</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">622,827,984</td>
<td align="right">960,380,458</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,102,851,147</td>
<td align="right">1,662,159,790</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,730,613,036</td>
<td align="right">6,973,167,096</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">489,820</td>
<td align="right">682,600</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,587,500</td>
<td align="right">7,535,720</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">204,233,063</td>
<td align="right">273,820,689</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">209,484,983</td>
<td align="right">280,313,108</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,951,640</td>
<td align="right">8,883,740</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,157,770,608</td>
<td align="right">1,476,558,095</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">24,438,395</td>
<td align="right">30,639,231</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">122,857,594</td>
<td align="right">153,297,443</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">55,763,356</td>
<td align="right">69,467,664</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">785,032</td>
<td align="right">972,667</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,261,210,478</td>
<td align="right">1,537,104,130</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">388,135,326</td>
<td align="right">304,417,193</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">129,277,174</td>
<td align="right">156,418,663</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">8,505,920,779</td>
<td align="right">6,766,793,042</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,309,840</td>
<td align="right">108,056,561</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,416,351,685</td>
<td align="right">2,859,897,568</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">9,502,794,248</td>
<td align="right">7,788,166,583</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">760,037,567</td>
<td align="right">889,335,229</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,155,513,489</td>
<td align="right">2,489,638,332</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">913,625,279</td>
<td align="right">1,050,429,468</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,182,441,174</td>
<td align="right">2,500,670,889</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">904,438,957</td>
<td align="right">1,034,640,557</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">67,613,020</td>
<td align="right">77,265,740</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,550,863,528</td>
<td align="right">2,912,159,902</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,461,829,041</td>
<td align="right">2,799,752,370</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">160,124,855</td>
<td align="right">181,457,495</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,987,029,441</td>
<td align="right">9,034,597,205</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,756,775,181</td>
<td align="right">1,986,420,866</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">299,243,550</td>
<td align="right">337,529,772</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">89,439,472</td>
<td align="right">100,796,267</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">45,579,526</td>
<td align="right">51,335,520</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">45,583,086</td>
<td align="right">51,339,080</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">743,760,166</td>
<td align="right">830,893,436</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,007,642</td>
<td align="right">90,461,920</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">470,679,099</td>
<td align="right">524,611,849</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">451,943,608</td>
<td align="right">502,230,400</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">2,106,144</td>
<td align="right">1,873,638</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,286,443,109</td>
<td align="right">2,537,500,363</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,769,443,211</td>
<td align="right">4,178,549,571</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,196,485,603</td>
<td align="right">3,543,064,665</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">963,034,006</td>
<td align="right">1,066,013,319</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">5,472,894</td>
<td align="right">6,036,955</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">11,445,900</td>
<td align="right">12,624,740</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,574,829,948</td>
<td align="right">3,935,811,581</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,087,580</td>
<td align="right">94,464,458</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">353,772,279</td>
<td align="right">386,109,537</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">57,751,460</td>
<td align="right">62,993,960</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">112,960,166</td>
<td align="right">123,183,552</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">3,523,361,268</td>
<td align="right">3,841,976,623</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">366,309,252</td>
<td align="right">399,003,993</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,332,327,534</td>
<td align="right">1,448,458,055</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,395,622,714</td>
<td align="right">6,952,585,704</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">980,472,087</td>
<td align="right">1,065,454,241</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,083,857,339</td>
<td align="right">1,175,998,529</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">879,800,639</td>
<td align="right">953,545,198</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">223,408,189</td>
<td align="right">242,115,140</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,443,794,631</td>
<td align="right">4,815,010,873</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">580,626,340</td>
<td align="right">628,627,360</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,123,149,427</td>
<td align="right">1,030,358,135</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,699,936,509</td>
<td align="right">1,840,190,259</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,284,876,253</td>
<td align="right">8,962,086,957</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,854,257,997</td>
<td align="right">4,151,010,552</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,771,251,472</td>
<td align="right">4,061,296,505</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,948,633,923</td>
<td align="right">2,093,258,187</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">351,518,773</td>
<td align="right">377,599,274</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">10,334,350,784</td>
<td align="right">11,100,931,548</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,408,486,677</td>
<td align="right">1,512,729,089</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">122,709,672</td>
<td align="right">131,678,680</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">659,458,814</td>
<td align="right">611,273,471</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,804,191,237</td>
<td align="right">1,934,259,031</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,676,502,751</td>
<td align="right">1,796,396,659</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,575,306,499</td>
<td align="right">3,830,850,417</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,822,498,257</td>
<td align="right">1,952,617,471</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">359,596,211</td>
<td align="right">383,008,479</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">25,741,244,702</td>
<td align="right">27,382,471,673</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">134,024,584</td>
<td align="right">142,279,820</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,251,693,938</td>
<td align="right">10,877,821,783</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">205,156,292</td>
<td align="right">193,347,772</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">951,439,198</td>
<td align="right">1,002,568,589</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,315,961,174</td>
<td align="right">2,435,709,613</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">132,815,838</td>
<td align="right">139,527,141</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,065,099,670</td>
<td align="right">1,117,930,703</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,143,984,920</td>
<td align="right">1,199,140,860</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">394,788,386</td>
<td align="right">413,304,977</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">290,947,273</td>
<td align="right">304,483,216</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">962,391,575</td>
<td align="right">1,005,563,087</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,884,072,370</td>
<td align="right">3,011,046,781</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">158,952,999</td>
<td align="right">165,941,176</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,313,463,467</td>
<td align="right">1,369,510,430</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,276,214</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,907,540</td>
<td align="right">161,217,420</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">720,832,721</td>
<td align="right">749,847,244</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">838,628,860</td>
<td align="right">870,239,177</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,003,030,101</td>
<td align="right">1,039,041,492</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,232,020</td>
<td align="right">362,514,040</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">218,335,250</td>
<td align="right">225,867,524</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">245,514,909</td>
<td align="right">253,756,188</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,371,982,393</td>
<td align="right">8,644,373,794</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">32,688,677</td>
<td align="right">33,742,559</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">21,420,718,458</td>
<td align="right">22,092,031,430</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">236,465,788</td>
<td align="right">243,719,614</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,439,961</td>
<td align="right">621,528,143</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,617,113,949</td>
<td align="right">1,665,127,946</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,826,455,327</td>
<td align="right">3,712,981,712</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,664,557,149</td>
<td align="right">5,829,817,254</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,256,016,422</td>
<td align="right">5,406,309,589</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,715,357,908</td>
<td align="right">1,763,972,112</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,599,858,990</td>
<td align="right">2,672,647,813</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,943,210,279</td>
<td align="right">4,042,759,144</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">557,675,899</td>
<td align="right">570,905,837</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">42,810,971</td>
<td align="right">43,819,131</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">24,662</td>
<td align="right">24,082</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">43,496,391</td>
<td align="right">44,504,631</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,391,656,364</td>
<td align="right">2,336,989,544</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">281,605,925</td>
<td align="right">287,926,045</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">246,625,717</td>
<td align="right">252,096,925</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,620,449,303</td>
<td align="right">1,653,208,297</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">566,899,980</td>
<td align="right">577,756,360</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,479,179,306</td>
<td align="right">1,507,268,762</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">63,190,992</td>
<td align="right">62,008,452</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,817,566,079</td>
<td align="right">1,851,076,056</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,377,741,097</td>
<td align="right">2,334,322,659</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,754,409,093</td>
<td align="right">15,018,863,436</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">39,085,589</td>
<td align="right">38,387,140</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">169,366,554</td>
<td align="right">172,333,454</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">64,640,652</td>
<td align="right">63,599,952</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,626,331</td>
<td align="right">47,374,707</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,353,666,714</td>
<td align="right">2,390,944,902</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,842,060</td>
<td align="right">1,813,980</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">107,918,689</td>
<td align="right">109,415,646</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">112,699,071</td>
<td align="right">114,229,047</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,890,138,759</td>
<td align="right">4,954,545,896</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">11,163,200</td>
<td align="right">11,302,820</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">704,177,829</td>
<td align="right">695,433,722</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">699,327,797</td>
<td align="right">707,711,868</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">699,129,869</td>
<td align="right">690,843,942</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">156,001,285</td>
<td align="right">157,836,513</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">166,007,207</td>
<td align="right">167,936,300</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">938,470,164</td>
<td align="right">949,270,920</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">68,680,671</td>
<td align="right">67,890,376</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,074,228,830</td>
<td align="right">1,086,057,956</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">917,099,799</td>
<td align="right">907,141,090</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,331,665</td>
<td align="right">69,065,547</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">692,905,010</td>
<td align="right">699,960,640</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,082,201,369</td>
<td align="right">2,062,611,132</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,034,573</td>
<td align="right">739,925,428</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">578,098,384</td>
<td align="right">583,349,718</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,346,077,933</td>
<td align="right">1,358,011,251</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,471,160</td>
<td align="right">786,364,770</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">780,828,920</td>
<td align="right">786,981,350</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,728,729</td>
<td align="right">54,329,662</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,732,969</td>
<td align="right">54,333,902</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">74,421,289</td>
<td align="right">73,899,139</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">238,399,943</td>
<td align="right">240,047,034</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,224,900,061</td>
<td align="right">2,239,547,891</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,035,741,018</td>
<td align="right">3,054,160,420</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">676,910,694</td>
<td align="right">673,092,385</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">782,491,788</td>
<td align="right">786,866,566</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">394,296,368</td>
<td align="right">392,129,837</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">49,828,651</td>
<td align="right">50,076,656</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">49,828,651</td>
<td align="right">50,076,656</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">921,364</td>
<td align="right">917,282</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,904,564</td>
<td align="right">8,867,744</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,621,101,819</td>
<td align="right">3,630,009,349</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,840</td>
<td align="right">4,751,120</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">39,144,213</td>
<td align="right">39,231,213</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">41,164,573</td>
<td align="right">41,251,573</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,639,949</td>
<td align="right">2,634,957</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">36,581,731</td>
<td align="right">36,513,858</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">12,646,733</td>
<td align="right">12,623,948</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">114,714,231</td>
<td align="right">114,535,926</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">533,026,366</td>
<td align="right">533,791,246</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">845,840,197</td>
<td align="right">844,672,583</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">84,013,399</td>
<td align="right">84,125,775</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,154,864</td>
<td align="right">10,162,212</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,390,787</td>
<td align="right">97,331,522</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">342,605,699</td>
<td align="right">342,802,734</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">6,776,729</td>
<td align="right">6,772,923</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,994,660</td>
<td align="right">1,993,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,204,979,452</td>
<td align="right">1,204,415,464</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">530,785,094</td>
<td align="right">531,025,264</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,303,398</td>
<td align="right">1,303,976</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">99,657,024</td>
<td align="right">99,690,288</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">72,090,648</td>
<td align="right">72,076,281</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,437,022</td>
<td align="right">32,432,828</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">370,491</td>
<td align="right">370,453</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,071,396,801</td>
<td align="right">1,071,342,791</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">167,924,949</td>
<td align="right">167,930,204</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">229,356,044</td>
<td align="right">229,351,964</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,241,584</td>
<td align="right">97,241,883</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,289,684</td>
<td align="right">97,289,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,259,208</td>
<td align="right">4,259,200</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">125,369,780</td>
<td align="right">125,369,555</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,102,268</td>
<td align="right">518,102,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,588,820</td>
<td align="right">32,588,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">962,920</td>
<td align="right">962,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">962,920</td>
<td align="right">962,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">597,220</td>
<td align="right">597,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">376,020</td>
<td align="right">376,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">94,160</td>
<td align="right">94,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">10,164</td>
<td align="right">10,164</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">8,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">420</td>
<td align="right">420</td>
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
<td align="left">CALL_KW</td>
<td align="right">60</td>
<td align="right">140</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">21,966</td>
<td align="right">27,043</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,194</td>
<td align="right">44,891</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,580</td>
<td align="right">34,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,060</td>
<td align="right">1,060</td>
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
<td align="right">1,148</td>
<td align="right">1,155</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,148</td>
<td align="right">1,155</td>
<td align="right">0.6%</td>
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
<td align="right">240</td>
<td align="right">240</td>
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
<td align="right">400</td>
<td align="right">400</td>
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
<td align="right">1,941</td>
<td align="right">7.8%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
