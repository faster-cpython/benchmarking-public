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
<td align="left">UNARY_INVERT</td>
<td align="right">1,596,758</td>
<td align="right">9,440,690</td>
<td align="right">491.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">35,312,939</td>
<td align="right">86,241,102</td>
<td align="right">144.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">128,675,408</td>
<td align="right">293,396,750</td>
<td align="right">128.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">40,179,544</td>
<td align="right">90,526,178</td>
<td align="right">125.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">20,062,199</td>
<td align="right">45,069,979</td>
<td align="right">124.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">26,752,133</td>
<td align="right">59,995,927</td>
<td align="right">124.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,906,638,794</td>
<td align="right">4,264,516,231</td>
<td align="right">123.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">69,086,884</td>
<td align="right">145,768,466</td>
<td align="right">111.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">254,591,287</td>
<td align="right">156,309</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">63,837,742</td>
<td align="right">65,561</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,588,871</td>
<td align="right">4,951</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,554</td>
<td align="right">249</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">50,929,909</td>
<td align="right">431,137</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,071,384</td>
<td align="right">34,269</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,918,031</td>
<td align="right">272,028</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,623,266</td>
<td align="right">66,503</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,723</td>
<td align="right">803</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,280,501</td>
<td align="right">4,415,974</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,186,338</td>
<td align="right">136,410</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,850,921</td>
<td align="right">611,111</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">90,486,205</td>
<td align="right">12,328,811</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">211</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,873,685</td>
<td align="right">1,147,001</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">178,985,538</td>
<td align="right">27,707,622</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">794,670,199</td>
<td align="right">126,143,050</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,108,386</td>
<td align="right">1,139,564</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">212,906,617</td>
<td align="right">40,012,759</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">801,055,954</td>
<td align="right">162,753,978</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">38,346,277</td>
<td align="right">8,167,201</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">51,180,648</td>
<td align="right">11,037,233</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">28,919,713</td>
<td align="right">6,546,412</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">27,971,251</td>
<td align="right">6,903,963</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">58,519,767</td>
<td align="right">14,937,615</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">109,163,801</td>
<td align="right">28,589,851</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,513,911,988</td>
<td align="right">964,418,531</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">120,374,667</td>
<td align="right">36,884,106</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,649</td>
<td align="right">1,119</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">150,356,794</td>
<td align="right">46,908,635</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">451,724,727</td>
<td align="right">150,504,248</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,547,064</td>
<td align="right">12,533,130</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">254,828,246</td>
<td align="right">86,756,626</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">113,259,659</td>
<td align="right">38,925,231</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">93,506,360</td>
<td align="right">34,591,477</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">43,982,117</td>
<td align="right">16,491,531</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">78,125,122</td>
<td align="right">30,440,390</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,280,815,050</td>
<td align="right">502,426,106</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">147,958,451</td>
<td align="right">58,089,189</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">596,821,576</td>
<td align="right">236,696,683</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">91,913,894</td>
<td align="right">36,665,387</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">36,749,241</td>
<td align="right">58,515,124</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">22,954,180</td>
<td align="right">9,461,718</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">473,050,984</td>
<td align="right">199,414,887</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">178,174,162</td>
<td align="right">77,008,411</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">247,398,917</td>
<td align="right">108,049,559</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">149,941,237</td>
<td align="right">65,524,098</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">50,942,653</td>
<td align="right">22,664,323</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">59,046,452</td>
<td align="right">26,461,074</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,836,103,518</td>
<td align="right">1,292,442,038</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">308,508,080</td>
<td align="right">140,642,855</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">170,939</td>
<td align="right">78,316</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">131,652,097</td>
<td align="right">61,848,382</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">105,494,071</td>
<td align="right">49,785,932</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">83,643,107</td>
<td align="right">39,576,797</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">592,329</td>
<td align="right">286,315</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">33,097,850</td>
<td align="right">50,042,488</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,950,660,364</td>
<td align="right">955,785,720</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">119,703,384</td>
<td align="right">59,101,107</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">220,528,636</td>
<td align="right">112,035,973</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">352,877,206</td>
<td align="right">180,120,430</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">156,267,615</td>
<td align="right">80,204,052</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">112,100,346</td>
<td align="right">58,949,659</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">86,006,929</td>
<td align="right">45,830,699</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,269,922</td>
<td align="right">5,487,233</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">151,843,598</td>
<td align="right">222,240,565</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">400,810,546</td>
<td align="right">216,211,532</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">404,234,897</td>
<td align="right">218,338,722</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,998,983,626</td>
<td align="right">1,112,173,124</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">287,761,618</td>
<td align="right">163,461,896</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">596,587,471</td>
<td align="right">339,328,923</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">240,370,362</td>
<td align="right">343,335,960</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">83,367,429</td>
<td align="right">117,463,074</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,258,314,899</td>
<td align="right">1,973,420,632</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">12,988,394</td>
<td align="right">7,887,400</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">66,590,623</td>
<td align="right">41,522,199</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">57,421,645</td>
<td align="right">35,903,753</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">145,222,620</td>
<td align="right">91,764,038</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">43,386,341</td>
<td align="right">27,497,718</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,797,873,570</td>
<td align="right">1,803,772,060</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,757,690,061</td>
<td align="right">7,620,525,945</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,408,542</td>
<td align="right">11,379,384</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">80,230,216</td>
<td align="right">52,681,524</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">581,682,835</td>
<td align="right">383,074,223</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">82,481,910</td>
<td align="right">55,531,597</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">485,445,977</td>
<td align="right">328,114,976</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">73,344,787</td>
<td align="right">49,610,744</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">279,356,046</td>
<td align="right">191,280,131</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,030,613,546</td>
<td align="right">728,691,604</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">45,852,382</td>
<td align="right">32,522,894</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">258,121,930</td>
<td align="right">184,256,755</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">38,196,499</td>
<td align="right">27,775,724</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">40,447,884</td>
<td align="right">51,426,681</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">5,762,082</td>
<td align="right">4,222,525</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">486,138,624</td>
<td align="right">357,572,428</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,475,443,185</td>
<td align="right">1,098,512,629</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,769,786,833</td>
<td align="right">3,476,241,527</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">426,057,693</td>
<td align="right">319,836,522</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">162,524,904</td>
<td align="right">122,010,970</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">201,152,438</td>
<td align="right">151,051,371</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">77,962,546</td>
<td align="right">58,866,980</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">501,850</td>
<td align="right">380,007</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">8,699,005</td>
<td align="right">10,801,732</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,844,585</td>
<td align="right">41,547,053</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">111,611,134</td>
<td align="right">87,055,352</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">53,714</td>
<td align="right">41,929</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">15,122,503</td>
<td align="right">11,819,187</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">653,739,423</td>
<td align="right">791,920,039</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">199,783,091</td>
<td align="right">240,611,972</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">351,580,966</td>
<td align="right">286,008,717</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">583,437,789</td>
<td align="right">479,630,045</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">342,272,536</td>
<td align="right">401,538,685</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">514,000,528</td>
<td align="right">425,545,813</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">43,447,085</td>
<td align="right">50,499,616</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">172,850,769</td>
<td align="right">145,541,098</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,334,845,129</td>
<td align="right">2,812,063,185</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,482</td>
<td align="right">2,976</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">45,770,979</td>
<td align="right">39,175,339</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">24,225,047</td>
<td align="right">20,807,561</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">104,346,053</td>
<td align="right">90,587,733</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">205,137,714</td>
<td align="right">178,307,984</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">743,421</td>
<td align="right">647,090</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">42,370</td>
<td align="right">37,706</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,181,259,539</td>
<td align="right">2,418,842,419</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">269,893,414</td>
<td align="right">242,353,434</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">187,371,488</td>
<td align="right">168,902,872</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">170,900,533</td>
<td align="right">154,673,199</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">24,362,698</td>
<td align="right">22,143,631</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,374,692</td>
<td align="right">41,799,445</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">35,312,468</td>
<td align="right">32,550,708</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,579,726,075</td>
<td align="right">1,459,122,582</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">111,306,863</td>
<td align="right">105,936,073</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">212,645</td>
<td align="right">222,570</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">74,820,492</td>
<td align="right">71,896,037</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">168,492,385</td>
<td align="right">173,019,749</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,482,957,414</td>
<td align="right">1,522,745,421</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">32,740,599</td>
<td align="right">31,900,807</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">45,724,520</td>
<td align="right">44,728,643</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">34,808,342</td>
<td align="right">34,058,666</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">203,269,986</td>
<td align="right">207,480,436</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">18,502</td>
<td align="right">18,146</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">31,919,522</td>
<td align="right">31,370,018</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,361,109</td>
<td align="right">3,406,820</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,364,787</td>
<td align="right">11,268,234</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">153,205,490</td>
<td align="right">151,965,084</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">16,648,893</td>
<td align="right">16,544,618</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">16,984,914</td>
<td align="right">16,880,066</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">16,985,744</td>
<td align="right">16,881,239</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">54,186,715</td>
<td align="right">53,917,477</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,747,512,001</td>
<td align="right">1,740,078,066</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,449,457</td>
<td align="right">3,435,710</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">218,580</td>
<td align="right">219,420</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,741,825</td>
<td align="right">2,752,126</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">149,307,099</td>
<td align="right">149,773,454</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,409,806</td>
<td align="right">4,400,938</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">107,314,986</td>
<td align="right">107,149,406</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,038,075,188</td>
<td align="right">1,037,178,746</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">26,801,770</td>
<td align="right">26,791,150</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,934,333</td>
<td align="right">302,817,219</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,104,870</td>
<td align="right">129,094,297</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,826,329</td>
<td align="right">100,821,521</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">347,752</td>
<td align="right">347,739</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,688,866</td>
<td align="right">14,688,861</td>
<td align="right">-0.0%</td>
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
<td align="right">29,134,260</td>
<td align="right">29,134,260</td>
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
<td align="left">CALL_KW</td>
<td align="right">116,918</td>
<td align="right">116,918</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,791</td>
<td align="right">98,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,138</td>
<td align="right">56,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,359</td>
<td align="right">5,359</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">336</td>
<td align="right">336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">170</td>
<td align="right">170</td>
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
<td align="right">40</td>
<td align="right">40</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">287,002,287</td>
<td align="right">3.8%</td>
<td align="right">163,107,460</td>
<td align="right">2.2%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21,947,451</td>
<td align="right">0.3%</td>
<td align="right">21,461,408</td>
<td align="right">0.3%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,262,843,131</td>
<td align="right">95.9%</td>
<td align="right">7,289,339,979</td>
<td align="right">97.5%</td>
<td align="right">0.4%</td>
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
<td align="right">753,153</td>
<td align="right">64.2%</td>
<td align="right">348,294</td>
<td align="right">45.9%</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">420,238</td>
<td align="right">35.8%</td>
<td align="right">411,062</td>
<td align="right">54.1%</td>
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
<td align="left">add different types</td>
<td align="right">27,601</td>
<td align="right">3.7%</td>
<td align="right">111,222</td>
<td align="right">31.9%</td>
<td align="right">303.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">52,638</td>
<td align="right">7.0%</td>
<td align="right">142,045</td>
<td align="right">40.8%</td>
<td align="right">169.9%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1,006</td>
<td align="right">0.1%</td>
<td align="right">2,447</td>
<td align="right">0.7%</td>
<td align="right">143.2%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">583,291</td>
<td align="right">77.4%</td>
<td align="right">30,308</td>
<td align="right">8.7%</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">7,793</td>
<td align="right">1.0%</td>
<td align="right">14,970</td>
<td align="right">4.3%</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">18,739</td>
<td align="right">2.5%</td>
<td align="right">1,970</td>
<td align="right">0.6%</td>
<td align="right">-89.5%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">2,609</td>
<td align="right">0.3%</td>
<td align="right">820</td>
<td align="right">0.2%</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,328</td>
<td align="right">0.3%</td>
<td align="right">760</td>
<td align="right">0.2%</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">5,867</td>
<td align="right">0.8%</td>
<td align="right">2,960</td>
<td align="right">0.8%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">4,618</td>
<td align="right">0.6%</td>
<td align="right">2,675</td>
<td align="right">0.8%</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">2,826</td>
<td align="right">0.4%</td>
<td align="right">2,070</td>
<td align="right">0.6%</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">9,703</td>
<td align="right">1.3%</td>
<td align="right">7,349</td>
<td align="right">2.1%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">64</td>
<td align="right">0.0%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">21,614</td>
<td align="right">2.9%</td>
<td align="right">17,161</td>
<td align="right">4.9%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,052</td>
<td align="right">0.1%</td>
<td align="right">907</td>
<td align="right">0.3%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">735</td>
<td align="right">0.1%</td>
<td align="right">637</td>
<td align="right">0.2%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">5,973</td>
<td align="right">0.8%</td>
<td align="right">5,182</td>
<td align="right">1.5%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">492</td>
<td align="right">0.1%</td>
<td align="right">451</td>
<td align="right">0.1%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">4,184</td>
<td align="right">0.6%</td>
<td align="right">4,296</td>
<td align="right">1.2%</td>
<td align="right">2.7%</td>
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
<td align="right">86,006,929</td>
<td align="right">100.0%</td>
<td align="right">45,830,699</td>
<td align="right">100.0%</td>
<td align="right">-46.7%</td>
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
<td align="right">425,914,895</td>
<td align="right">8.2%</td>
<td align="right">319,723,776</td>
<td align="right">6.3%</td>
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
<td align="right">5,755,190</td>
<td align="right">0.1%</td>
<td align="right">5,701,010</td>
<td align="right">0.1%</td>
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
<td align="right">4,783,444,679</td>
<td align="right">91.7%</td>
<td align="right">4,778,353,014</td>
<td align="right">93.6%</td>
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
<td align="right">134,561</td>
<td align="right">53.6%</td>
<td align="right">104,511</td>
<td align="right">47.5%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">116,619</td>
<td align="right">46.4%</td>
<td align="right">115,592</td>
<td align="right">52.5%</td>
<td align="right">-0.9%</td>
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
<td align="right">793</td>
<td align="right">0.6%</td>
<td align="right">288</td>
<td align="right">0.3%</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,437</td>
<td align="right">9.2%</td>
<td align="right">6,418</td>
<td align="right">6.1%</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">45,171</td>
<td align="right">33.6%</td>
<td align="right">28,955</td>
<td align="right">27.7%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">18,032</td>
<td align="right">13.4%</td>
<td align="right">23,470</td>
<td align="right">22.5%</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">36,434</td>
<td align="right">27.1%</td>
<td align="right">26,457</td>
<td align="right">25.3%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,491</td>
<td align="right">2.6%</td>
<td align="right">2,586</td>
<td align="right">2.5%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,811</td>
<td align="right">3.6%</td>
<td align="right">4,173</td>
<td align="right">4.0%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">10,357</td>
<td align="right">7.7%</td>
<td align="right">9,129</td>
<td align="right">8.7%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.2%</td>
<td align="right">2,941</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">73</td>
<td align="right">0.1%</td>
<td align="right">73</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,641</td>
<td align="right">0.0%</td>
<td align="right">14,609</td>
<td align="right">0.0%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">119,473,457</td>
<td align="right">1.1%</td>
<td align="right">125,648,655</td>
<td align="right">1.2%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,573,554,654</td>
<td align="right">98.9%</td>
<td align="right">10,542,840,597</td>
<td align="right">98.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">204,302</td>
<td align="right">0.0%</td>
<td align="right">204,302</td>
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
<td align="right">2,413,182</td>
<td align="right">100.0%</td>
<td align="right">2,522,360</td>
<td align="right">100.0%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">486</td>
<td align="right">0.0%</td>
<td align="right">486</td>
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
<td align="right">732</td>
<td align="right">150.6%</td>
<td align="right">732</td>
<td align="right">150.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">486</td>
<td align="right">100.0%</td>
<td align="right">486</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">394</td>
<td align="right">81.1%</td>
<td align="right">394</td>
<td align="right">81.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">308</td>
<td align="right">63.4%</td>
<td align="right">308</td>
<td align="right">63.4%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">528,176</td>
<td align="right">81.9%</td>
<td align="right">145,032</td>
<td align="right">55.4%</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">109,638</td>
<td align="right">17.0%</td>
<td align="right">109,638</td>
<td align="right">41.9%</td>
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
<td align="right">911,923</td>
<td align="right">0.0%</td>
<td align="right">459,651</td>
<td align="right">0.0%</td>
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
<td align="right">77,871,788</td>
<td align="right">1.8%</td>
<td align="right">58,806,745</td>
<td align="right">1.3%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,361,284,284</td>
<td align="right">98.2%</td>
<td align="right">4,357,122,456</td>
<td align="right">98.7%</td>
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
<td align="right">82,893</td>
<td align="right">76.9%</td>
<td align="right">52,398</td>
<td align="right">76.2%</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">24,968</td>
<td align="right">23.1%</td>
<td align="right">16,387</td>
<td align="right">23.8%</td>
<td align="right">-34.4%</td>
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
<td align="left">big int</td>
<td align="right">21,734</td>
<td align="right">26.2%</td>
<td align="right">9,924</td>
<td align="right">18.9%</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">25,591</td>
<td align="right">30.9%</td>
<td align="right">13,132</td>
<td align="right">25.1%</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,999</td>
<td align="right">4.8%</td>
<td align="right">2,054</td>
<td align="right">3.9%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,190</td>
<td align="right">7.5%</td>
<td align="right">4,382</td>
<td align="right">8.4%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,514</td>
<td align="right">7.9%</td>
<td align="right">4,631</td>
<td align="right">8.8%</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">344</td>
<td align="right">0.4%</td>
<td align="right">264</td>
<td align="right">0.5%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,055</td>
<td align="right">1.3%</td>
<td align="right">853</td>
<td align="right">1.6%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">7,929</td>
<td align="right">9.6%</td>
<td align="right">7,721</td>
<td align="right">14.7%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,554</td>
<td align="right">9.1%</td>
<td align="right">7,464</td>
<td align="right">14.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">666</td>
<td align="right">0.8%</td>
<td align="right">659</td>
<td align="right">1.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">979</td>
<td align="right">1.2%</td>
<td align="right">976</td>
<td align="right">1.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">338</td>
<td align="right">0.4%</td>
<td align="right">338</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,916,370</td>
<td align="right">0.1%</td>
<td align="right">66,001</td>
<td align="right">0.0%</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">35,280,196</td>
<td align="right">1.8%</td>
<td align="right">32,524,292</td>
<td align="right">1.7%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,897,408,953</td>
<td align="right">98.1%</td>
<td align="right">1,859,197,346</td>
<td align="right">98.3%</td>
<td align="right">-2.0%</td>
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
<td align="right">38,417</td>
<td align="right">56.1%</td>
<td align="right">3,497</td>
<td align="right">12.6%</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">30,008</td>
<td align="right">43.9%</td>
<td align="right">24,152</td>
<td align="right">87.4%</td>
<td align="right">-19.5%</td>
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
<td align="right">6,879</td>
<td align="right">22.9%</td>
<td align="right">4,676</td>
<td align="right">19.4%</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,910</td>
<td align="right">36.4%</td>
<td align="right">7,859</td>
<td align="right">32.5%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,367</td>
<td align="right">24.6%</td>
<td align="right">6,063</td>
<td align="right">25.1%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">4,852</td>
<td align="right">16.2%</td>
<td align="right">5,554</td>
<td align="right">23.0%</td>
<td align="right">14.5%</td>
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
<td align="right">73,299,646</td>
<td align="right">12.2%</td>
<td align="right">49,576,248</td>
<td align="right">10.6%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,206,296</td>
<td align="right">4.2%</td>
<td align="right">19,935,393</td>
<td align="right">4.3%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">500,619,716</td>
<td align="right">83.6%</td>
<td align="right">397,214,416</td>
<td align="right">85.1%</td>
<td align="right">-20.7%</td>
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
<td align="right">41,563</td>
<td align="right">8.0%</td>
<td align="right">30,967</td>
<td align="right">7.5%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">479,041</td>
<td align="right">92.0%</td>
<td align="right">379,625</td>
<td align="right">92.5%</td>
<td align="right">-20.8%</td>
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
<td align="left">seq iter</td>
<td align="right">1,779</td>
<td align="right">4.3%</td>
<td align="right">3,196</td>
<td align="right">10.3%</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,606</td>
<td align="right">8.7%</td>
<td align="right">1,220</td>
<td align="right">3.9%</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">938</td>
<td align="right">2.3%</td>
<td align="right">323</td>
<td align="right">1.0%</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,226</td>
<td align="right">2.9%</td>
<td align="right">563</td>
<td align="right">1.8%</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,814</td>
<td align="right">4.4%</td>
<td align="right">978</td>
<td align="right">3.2%</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">56</td>
<td align="right">0.2%</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,850</td>
<td align="right">4.5%</td>
<td align="right">1,218</td>
<td align="right">3.9%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">14,021</td>
<td align="right">33.7%</td>
<td align="right">9,544</td>
<td align="right">30.8%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,594</td>
<td align="right">8.6%</td>
<td align="right">2,628</td>
<td align="right">8.5%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,666</td>
<td align="right">16.0%</td>
<td align="right">5,649</td>
<td align="right">18.2%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">3,410</td>
<td align="right">8.2%</td>
<td align="right">3,139</td>
<td align="right">10.1%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,369</td>
<td align="right">5.7%</td>
<td align="right">2,254</td>
<td align="right">7.3%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">130</td>
<td align="right">0.3%</td>
<td align="right">130</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">69</td>
<td align="right">0.2%</td>
<td align="right">69</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">598,195</td>
<td align="right">0.0%</td>
<td align="right">249,708</td>
<td align="right">0.0%</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">402,931,896</td>
<td align="right">3.2%</td>
<td align="right">217,330,382</td>
<td align="right">1.8%</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">412,489,541</td>
<td align="right">3.2%</td>
<td align="right">328,180,379</td>
<td align="right">2.7%</td>
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
<td align="right">11,950,659,620</td>
<td align="right">93.6%</td>
<td align="right">11,769,066,621</td>
<td align="right">95.6%</td>
<td align="right">-1.5%</td>
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
<td align="right">202,191</td>
<td align="right">2.2%</td>
<td align="right">129,129</td>
<td align="right">1.8%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,874,708</td>
<td align="right">97.8%</td>
<td align="right">7,062,953</td>
<td align="right">98.2%</td>
<td align="right">-20.4%</td>
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
<td align="right">48</td>
<td align="right">0.0%</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,405</td>
<td align="right">1.2%</td>
<td align="right">270</td>
<td align="right">0.2%</td>
<td align="right">-88.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,718</td>
<td align="right">3.8%</td>
<td align="right">1,846</td>
<td align="right">1.4%</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">361</td>
<td align="right">0.2%</td>
<td align="right">101</td>
<td align="right">0.1%</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">20,115</td>
<td align="right">9.9%</td>
<td align="right">6,359</td>
<td align="right">4.9%</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,293</td>
<td align="right">7.1%</td>
<td align="right">6,047</td>
<td align="right">4.7%</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">42,453</td>
<td align="right">21.0%</td>
<td align="right">21,973</td>
<td align="right">17.0%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,425</td>
<td align="right">0.7%</td>
<td align="right">739</td>
<td align="right">0.6%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,230</td>
<td align="right">0.6%</td>
<td align="right">827</td>
<td align="right">0.6%</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,420</td>
<td align="right">0.7%</td>
<td align="right">964</td>
<td align="right">0.7%</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,268</td>
<td align="right">0.6%</td>
<td align="right">938</td>
<td align="right">0.7%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">51,457</td>
<td align="right">25.4%</td>
<td align="right">39,563</td>
<td align="right">30.6%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,001</td>
<td align="right">2.5%</td>
<td align="right">4,100</td>
<td align="right">3.2%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">37,339</td>
<td align="right">18.5%</td>
<td align="right">31,592</td>
<td align="right">24.5%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">901</td>
<td align="right">0.4%</td>
<td align="right">843</td>
<td align="right">0.7%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,521</td>
<td align="right">3.7%</td>
<td align="right">7,186</td>
<td align="right">5.6%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">3,374,390,523</td>
<td align="right">99.6%</td>
<td align="right">1,580,998,087</td>
<td align="right">99.1%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,296</td>
<td align="right">0.0%</td>
<td align="right">32,760</td>
<td align="right">0.0%</td>
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
<td align="right">14,586,260</td>
<td align="right">0.4%</td>
<td align="right">14,586,232</td>
<td align="right">0.9%</td>
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
<td align="right">1,485</td>
<td align="right">0.0%</td>
<td align="right">1,485</td>
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
<td align="right">103,355</td>
<td align="right">100.0%</td>
<td align="right">103,416</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
<td align="right">62,827,959</td>
<td align="right">100.0%</td>
<td align="right">62,554,162</td>
<td align="right">100.0%</td>
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
<td align="right">254</td>
<td align="right">0.0%</td>
<td align="right">254</td>
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
<td align="right">2,498</td>
<td align="right">100.0%</td>
<td align="right">2,498</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,714</td>
<td align="right">0.0%</td>
<td align="right">9,878</td>
<td align="right">0.0%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">593,497,417</td>
<td align="right">82.1%</td>
<td align="right">593,151,022</td>
<td align="right">82.1%</td>
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
<td align="right">129,069,587</td>
<td align="right">17.9%</td>
<td align="right">129,059,374</td>
<td align="right">17.9%</td>
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
<td align="right">709</td>
<td align="right">2.0%</td>
<td align="right">600</td>
<td align="right">1.7%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,846</td>
<td align="right">98.0%</td>
<td align="right">34,527</td>
<td align="right">98.3%</td>
<td align="right">-0.9%</td>
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
<td align="right">3,261</td>
<td align="right">9.4%</td>
<td align="right">2,942</td>
<td align="right">8.5%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">24,440</td>
<td align="right">70.1%</td>
<td align="right">24,440</td>
<td align="right">70.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,387</td>
<td align="right">18.3%</td>
<td align="right">6,387</td>
<td align="right">18.5%</td>
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
<td align="right">104,365,029</td>
<td align="right">5.2%</td>
<td align="right">73,625,131</td>
<td align="right">3.7%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">53,771,275</td>
<td align="right">2.7%</td>
<td align="right">41,484,019</td>
<td align="right">2.1%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,834,463,719</td>
<td align="right">92.1%</td>
<td align="right">1,849,933,486</td>
<td align="right">94.1%</td>
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
<td align="right">2,000,137</td>
<td align="right">98.0%</td>
<td align="right">1,420,265</td>
<td align="right">97.8%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">41,632</td>
<td align="right">2.0%</td>
<td align="right">31,319</td>
<td align="right">2.2%</td>
<td align="right">-24.8%</td>
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
<td align="right">2,002</td>
<td align="right">4.8%</td>
<td align="right">410</td>
<td align="right">1.3%</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">592</td>
<td align="right">1.4%</td>
<td align="right">272</td>
<td align="right">0.9%</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">365</td>
<td align="right">0.9%</td>
<td align="right">238</td>
<td align="right">0.8%</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">645</td>
<td align="right">1.5%</td>
<td align="right">445</td>
<td align="right">1.4%</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">895</td>
<td align="right">2.1%</td>
<td align="right">619</td>
<td align="right">2.0%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">20,147</td>
<td align="right">48.4%</td>
<td align="right">14,205</td>
<td align="right">45.4%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">8,492</td>
<td align="right">20.4%</td>
<td align="right">7,172</td>
<td align="right">22.9%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,744</td>
<td align="right">4.2%</td>
<td align="right">1,530</td>
<td align="right">4.9%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,913</td>
<td align="right">4.6%</td>
<td align="right">1,795</td>
<td align="right">5.7%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,633</td>
<td align="right">11.1%</td>
<td align="right">4,432</td>
<td align="right">14.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">108</td>
<td align="right">0.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">93</td>
<td align="right">0.3%</td>
<td align="right">-1.1%</td>
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
<td align="right">212,645</td>
<td align="right">100.0%</td>
<td align="right">222,570</td>
<td align="right">100.0%</td>
<td align="right">4.7%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">380</td>
<td align="right">0.0%</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">83,333,305</td>
<td align="right">11.0%</td>
<td align="right">117,421,177</td>
<td align="right">14.9%</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">672,234,350</td>
<td align="right">89.0%</td>
<td align="right">668,225,982</td>
<td align="right">85.0%</td>
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
<td align="left">Failure</td>
<td align="right">31,871</td>
<td align="right">93.3%</td>
<td align="right">39,664</td>
<td align="right">94.6%</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,293</td>
<td align="right">6.7%</td>
<td align="right">2,253</td>
<td align="right">5.4%</td>
<td align="right">-1.7%</td>
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
<td align="right">2,441</td>
<td align="right">7.7%</td>
<td align="right">13,723</td>
<td align="right">34.6%</td>
<td align="right">462.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,934</td>
<td align="right">9.2%</td>
<td align="right">1,534</td>
<td align="right">3.9%</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">8,633</td>
<td align="right">27.1%</td>
<td align="right">7,066</td>
<td align="right">17.8%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">500</td>
<td align="right">1.6%</td>
<td align="right">414</td>
<td align="right">1.0%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">185</td>
<td align="right">0.6%</td>
<td align="right">205</td>
<td align="right">0.5%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,944</td>
<td align="right">53.2%</td>
<td align="right">16,488</td>
<td align="right">41.6%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">207</td>
<td align="right">0.6%</td>
<td align="right">207</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">24</td>
<td align="right">0.1%</td>
<td align="right">24</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
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
<td align="right">120,062,087</td>
<td align="right">2.6%</td>
<td align="right">36,725,257</td>
<td align="right">0.8%</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,330,520</td>
<td align="right">0.5%</td>
<td align="right">20,981,127</td>
<td align="right">0.5%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,524,767,094</td>
<td align="right">96.9%</td>
<td align="right">4,560,712,014</td>
<td align="right">98.7%</td>
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
<td align="left">Failure</td>
<td align="right">277,053</td>
<td align="right">36.0%</td>
<td align="right">123,489</td>
<td align="right">22.3%</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">493,342</td>
<td align="right">64.0%</td>
<td align="right">429,925</td>
<td align="right">77.7%</td>
<td align="right">-12.9%</td>
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
<td align="left">bytearray</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,806</td>
<td align="right">5.0%</td>
<td align="right">3,234</td>
<td align="right">2.6%</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">12,019</td>
<td align="right">4.3%</td>
<td align="right">3,105</td>
<td align="right">2.5%</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">143,764</td>
<td align="right">51.9%</td>
<td align="right">37,379</td>
<td align="right">30.3%</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,442</td>
<td align="right">3.4%</td>
<td align="right">3,557</td>
<td align="right">2.9%</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">10,049</td>
<td align="right">3.6%</td>
<td align="right">5,693</td>
<td align="right">4.6%</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">431</td>
<td align="right">0.2%</td>
<td align="right">591</td>
<td align="right">0.5%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">75,404</td>
<td align="right">27.2%</td>
<td align="right">59,429</td>
<td align="right">48.1%</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">3,898</td>
<td align="right">1.4%</td>
<td align="right">3,346</td>
<td align="right">2.7%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,117</td>
<td align="right">2.9%</td>
<td align="right">7,152</td>
<td align="right">5.8%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">584,249</td>
<td align="right">0.0%</td>
<td align="right">278,327</td>
<td align="right">0.0%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,176,308,247</td>
<td align="right">99.9%</td>
<td align="right">1,175,198,523</td>
<td align="right">100.0%</td>
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
<td align="right">705</td>
<td align="right">8.6%</td>
<td align="right">594</td>
<td align="right">7.4%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,455</td>
<td align="right">91.4%</td>
<td align="right">7,474</td>
<td align="right">92.6%</td>
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
<td align="left">sequence</td>
<td align="right">471</td>
<td align="right">66.8%</td>
<td align="right">359</td>
<td align="right">60.4%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">143</td>
<td align="right">20.3%</td>
<td align="right">144</td>
<td align="right">24.2%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">12.9%</td>
<td align="right">91</td>
<td align="right">15.3%</td>
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
<td align="right">23,226,352,919</td>
<td align="right">34.1%</td>
<td align="right">12,529,726,317</td>
<td align="right">24.9%</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">1,793,333,751</td>
<td align="right">2.6%</td>
<td align="right">1,229,149,956</td>
<td align="right">2.4%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">717,143,717</td>
<td align="right">1.1%</td>
<td align="right">596,426,232</td>
<td align="right">1.2%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">42,366,988,569</td>
<td align="right">62.2%</td>
<td align="right">35,967,989,816</td>
<td align="right">71.5%</td>
<td align="right">-15.1%</td>
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
<td align="right">120,062,087</td>
<td align="right">6.7%</td>
<td align="right">36,725,257</td>
<td align="right">3.0%</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">86,006,929</td>
<td align="right">4.8%</td>
<td align="right">45,830,699</td>
<td align="right">3.7%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">402,931,896</td>
<td align="right">22.5%</td>
<td align="right">217,330,382</td>
<td align="right">17.7%</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">287,002,287</td>
<td align="right">16.0%</td>
<td align="right">163,107,460</td>
<td align="right">13.3%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">83,333,305</td>
<td align="right">4.7%</td>
<td align="right">117,421,177</td>
<td align="right">9.6%</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">73,299,646</td>
<td align="right">4.1%</td>
<td align="right">49,576,248</td>
<td align="right">4.0%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">425,914,895</td>
<td align="right">23.8%</td>
<td align="right">319,723,776</td>
<td align="right">26.1%</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">77,871,788</td>
<td align="right">4.3%</td>
<td align="right">58,806,745</td>
<td align="right">4.8%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,771,275</td>
<td align="right">3.0%</td>
<td align="right">41,484,019</td>
<td align="right">3.4%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,069,587</td>
<td align="right">7.2%</td>
<td align="right">129,059,374</td>
<td align="right">10.5%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">63,177,505</td>
<td align="right">8.8%</td>
<td align="right">40,118,262</td>
<td align="right">6.7%</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">18,179,063</td>
<td align="right">2.5%</td>
<td align="right">13,902,827</td>
<td align="right">2.3%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">86,770,130</td>
<td align="right">12.1%</td>
<td align="right">66,944,780</td>
<td align="right">11.2%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">62,108,468</td>
<td align="right">8.7%</td>
<td align="right">71,278,971</td>
<td align="right">11.9%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">154,941,740</td>
<td align="right">21.6%</td>
<td align="right">147,610,540</td>
<td align="right">24.7%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">15,190,654</td>
<td align="right">2.1%</td>
<td align="right">14,822,119</td>
<td align="right">2.5%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">103,586,068</td>
<td align="right">14.4%</td>
<td align="right">106,080,865</td>
<td align="right">17.8%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,966,807</td>
<td align="right">2.9%</td>
<td align="right">20,927,305</td>
<td align="right">3.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">50,344,150</td>
<td align="right">7.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">17,575,143</td>
<td align="right">2.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">10,537,725</td>
<td align="right">1.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">9,960,502</td>
<td align="right">1.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">278,457,571</td>
<td align="right">4.2%</td>
<td align="right">274,569,276</td>
<td align="right">4.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,113,049,163</td>
<td align="right">17.0%</td>
<td align="right">1,106,392,242</td>
<td align="right">16.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,115,181,372</td>
<td align="right">17.0%</td>
<td align="right">1,108,524,451</td>
<td align="right">16.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,752,570,037</td>
<td align="right">26.7%</td>
<td align="right">1,745,124,393</td>
<td align="right">26.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,752,570,037</td>
<td align="right">26.7%</td>
<td align="right">1,745,124,393</td>
<td align="right">26.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,999,805</td>
<td align="right">0.4%</td>
<td align="right">24,911,660</td>
<td align="right">0.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,198,958,378</td>
<td align="right">79.2%</td>
<td align="right">5,182,079,089</td>
<td align="right">79.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">69,836,315</td>
<td align="right">1.1%</td>
<td align="right">69,691,439</td>
<td align="right">1.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,811,443,131</td>
<td align="right">73.3%</td>
<td align="right">4,803,752,311</td>
<td align="right">73.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">262,223,337</td>
<td align="right">4.0%</td>
<td align="right">261,833,986</td>
<td align="right">4.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">637,388,665</td>
<td align="right">9.7%</td>
<td align="right">636,599,942</td>
<td align="right">9.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">133,173,287</td>
<td align="right">2.0%</td>
<td align="right">133,173,785</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,265</td>
<td align="right">0.0%</td>
<td align="right">2,128,265</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,944</td>
<td align="right">0.0%</td>
<td align="right">3,944</td>
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
<td align="left">Interpreter mortal increfs</td>
<td align="right">31,993,543,188</td>
<td align="right">19.6%</td>
<td align="right">23,347,546,681</td>
<td align="right">13.9%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">12,160,706,939</td>
<td align="right">7.5%</td>
<td align="right">9,470,331,042</td>
<td align="right">5.6%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">76,209,001,041</td>
<td align="right">46.8%</td>
<td align="right">91,827,496,608</td>
<td align="right">54.5%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">81,417,572,285</td>
<td align="right">41.8%</td>
<td align="right">93,419,086,466</td>
<td align="right">45.8%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">15,045,155,414</td>
<td align="right">7.7%</td>
<td align="right">12,829,061,557</td>
<td align="right">6.3%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">43,604,787,794</td>
<td align="right">22.4%</td>
<td align="right">38,523,038,271</td>
<td align="right">18.9%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,687,067</td>
<td align="right"></td>
<td align="right">5,962,676</td>
<td align="right"></td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">54,761,382,397</td>
<td align="right">28.1%</td>
<td align="right">59,230,656,827</td>
<td align="right">29.0%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">63,518,754</td>
<td align="right"></td>
<td align="right">60,922,004</td>
<td align="right"></td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">1,968,101,296</td>
<td align="right"></td>
<td align="right">1,903,881,475</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">57,618,927</td>
<td align="right"></td>
<td align="right">55,744,974</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">177,764,102</td>
<td align="right"></td>
<td align="right">173,167,214</td>
<td align="right"></td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">42,635,489,406</td>
<td align="right">26.2%</td>
<td align="right">43,733,677,787</td>
<td align="right">26.0%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,336,731</td>
<td align="right">0.4%</td>
<td align="right">72,109,016</td>
<td align="right">0.4%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,053,919,796</td>
<td align="right"></td>
<td align="right">3,032,889,550</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,347,129,242</td>
<td align="right">45.4%</td>
<td align="right">8,308,942,923</td>
<td align="right">45.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,347,263,938</td>
<td align="right"></td>
<td align="right">8,309,113,467</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">9,955,635,808</td>
<td align="right">54.2%</td>
<td align="right">9,929,055,395</td>
<td align="right">54.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,033,278,166</td>
<td align="right">54.6%</td>
<td align="right">10,007,474,699</td>
<td align="right">54.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,615,107,069</td>
<td align="right"></td>
<td align="right">10,590,195,851</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,305,627</td>
<td align="right">0.0%</td>
<td align="right">6,310,288</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,443,437</td>
<td align="right">2.5%</td>
<td align="right">4,443,437</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">392,274</td>
<td align="right">0.2%</td>
<td align="right">392,274</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">13,407</td>
<td align="right">0.0%</td>
<td align="right">13,407</td>
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
<td align="right">353,686</td>
<td align="right">100,393,769</td>
<td align="right">15,147,533,152</td>
<td align="right">353,922</td>
<td align="right">100,707,071</td>
<td align="right">15,191,013,274</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,438</td>
<td align="right">5,249,711,658</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,249,859,378</td>
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
<td align="right">14,205</td>
<td align="right">1.0%</td>
<td align="right">66,521</td>
<td align="right">1.9%</td>
<td align="right">368.3%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">3,750</td>
<td align="right">0.5%</td>
<td align="right">12,372</td>
<td align="right">0.7%</td>
<td align="right">229.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">736,286</td>
<td align="right">50.2%</td>
<td align="right">2,041,234</td>
<td align="right">58.6%</td>
<td align="right">177.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">7,474</td>
<td align="right">0.5%</td>
<td align="right">19,668</td>
<td align="right">0.6%</td>
<td align="right">163.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">749,818</td>
<td align="right">51.1%</td>
<td align="right">1,864,010</td>
<td align="right">53.5%</td>
<td align="right">148.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,467,327</td>
<td align="right"></td>
<td align="right">3,483,662</td>
<td align="right"></td>
<td align="right">137.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">715,625</td>
<td align="right">48.8%</td>
<td align="right">1,619,226</td>
<td align="right">46.5%</td>
<td align="right">126.3%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,884</td>
<td align="right">0.1%</td>
<td align="right">426</td>
<td align="right">0.0%</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,209,333,067</td>
<td align="right"></td>
<td align="right">12,327,180,193</td>
<td align="right"></td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">321</td>
<td align="right">0.0%</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">242,994,359,859</td>
<td align="right">3,370.6%</td>
<td align="right">294,942,353,294</td>
<td align="right">2,392.6%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">8,809</td>
<td align="right">0.6%</td>
<td align="right">9,075</td>
<td align="right">0.3%</td>
<td align="right">3.0%</td>
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
<td align="right">716,651</td>
<td align="right">95.6%</td>
<td align="right">1,835,123</td>
<td align="right">98.5%</td>
<td align="right">156.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">749,818</td>
<td align="right"></td>
<td align="right">1,864,010</td>
<td align="right"></td>
<td align="right">148.6%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">448</td>
<td align="right">0.1%</td>
<td align="right">639</td>
<td align="right">0.0%</td>
<td align="right">42.6%</td>
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
<td align="right">1,549</td>
<td align="right">0.1%</td>
<td align="right">1,549 / 0 !!</td>
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
<td align="right">32,964</td>
<td align="right">1.8%</td>
<td align="right">32,964 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">52,502</td>
<td align="right">7.0%</td>
<td align="right">91,518</td>
<td align="right">4.9%</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">136,850</td>
<td align="right">18.3%</td>
<td align="right">264,216</td>
<td align="right">14.2%</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">258,840</td>
<td align="right">34.5%</td>
<td align="right">723,995</td>
<td align="right">38.8%</td>
<td align="right">179.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">193,364</td>
<td align="right">25.8%</td>
<td align="right">499,140</td>
<td align="right">26.8%</td>
<td align="right">158.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">84,202</td>
<td align="right">11.2%</td>
<td align="right">200,640</td>
<td align="right">10.8%</td>
<td align="right">138.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">20,395</td>
<td align="right">2.7%</td>
<td align="right">43,930</td>
<td align="right">2.4%</td>
<td align="right">115.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">3,445</td>
<td align="right">0.5%</td>
<td align="right">7,546</td>
<td align="right">0.4%</td>
<td align="right">119.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">-72.3%</td>
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
<td align="right">29,842</td>
<td align="right">4.0%</td>
<td align="right">92,917</td>
<td align="right">5.0%</td>
<td align="right">211.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">101,713</td>
<td align="right">13.6%</td>
<td align="right">127,496</td>
<td align="right">6.8%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">141,170</td>
<td align="right">18.8%</td>
<td align="right">466,314</td>
<td align="right">25.0%</td>
<td align="right">230.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">284,667</td>
<td align="right">38.0%</td>
<td align="right">734,720</td>
<td align="right">39.4%</td>
<td align="right">158.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">118,685</td>
<td align="right">15.8%</td>
<td align="right">317,536</td>
<td align="right">17.0%</td>
<td align="right">167.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">32,887</td>
<td align="right">4.4%</td>
<td align="right">81,665</td>
<td align="right">4.4%</td>
<td align="right">148.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,715</td>
<td align="right">0.9%</td>
<td align="right">13,887</td>
<td align="right">0.7%</td>
<td align="right">106.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">972</td>
<td align="right">0.1%</td>
<td align="right">588</td>
<td align="right">0.0%</td>
<td align="right">-39.5%</td>
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
<td align="left">_DELETE_ATTR</td>
<td align="right">1,905</td>
<td align="right">1,558,685</td>
<td align="right">81,720.7%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">14,623</td>
<td align="right">4,254,433</td>
<td align="right">28,994.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">58,486</td>
<td align="right">8,701,241</td>
<td align="right">14,777.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">948,152</td>
<td align="right">27,172,873</td>
<td align="right">2,765.9%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">3,001,182</td>
<td align="right">66,583,119</td>
<td align="right">2,118.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">845,638</td>
<td align="right">6,390,632</td>
<td align="right">655.7%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">986,313</td>
<td align="right">6,731,632</td>
<td align="right">582.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">8,826,666</td>
<td align="right">59,899,662</td>
<td align="right">578.6%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">5,659,231</td>
<td align="right">30,599,741</td>
<td align="right">440.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">177,450,184</td>
<td align="right">846,029,953</td>
<td align="right">376.8%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">1,481,042</td>
<td align="right">6,514,222</td>
<td align="right">339.8%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">87,231,615</td>
<td align="right">340,388,245</td>
<td align="right">290.2%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">4,238</td>
<td align="right">16,023</td>
<td align="right">278.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">7,945,978</td>
<td align="right">27,900,484</td>
<td align="right">251.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,515,015,898</td>
<td align="right">4,671,941,555</td>
<td align="right">208.4%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">40,536</td>
<td align="right">118,795</td>
<td align="right">193.1%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,408,292</td>
<td align="right">6,828,576</td>
<td align="right">183.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">25,500,613</td>
<td align="right">71,773,790</td>
<td align="right">181.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">18,965,247</td>
<td align="right">49,601,562</td>
<td align="right">161.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">11,472,542</td>
<td align="right">29,723,791</td>
<td align="right">159.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">18,589,364</td>
<td align="right">48,059,990</td>
<td align="right">158.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,279,315</td>
<td align="right">3,273,412</td>
<td align="right">155.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">35,428,401</td>
<td align="right">79,286,628</td>
<td align="right">123.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">36,148,340</td>
<td align="right">79,649,327</td>
<td align="right">120.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">22,107,112</td>
<td align="right">47,236,492</td>
<td align="right">113.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">67,415,454</td>
<td align="right">141,984,543</td>
<td align="right">110.6%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">462</td>
<td align="right">968</td>
<td align="right">109.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">25,426,600</td>
<td align="right">52,900,876</td>
<td align="right">108.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,337,357</td>
<td align="right">4,817,669</td>
<td align="right">106.1%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">25,780,332</td>
<td align="right">51,119,521</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">105,072,067</td>
<td align="right">208,280,127</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">45,051,334</td>
<td align="right">89,202,034</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">35,396,538</td>
<td align="right">1,024,472</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">35,396,538</td>
<td align="right">1,024,472</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">27,564,892</td>
<td align="right">53,068,500</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">265,486,634</td>
<td align="right">507,695,389</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">25,876,243</td>
<td align="right">2,873,058</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">890,566,449</td>
<td align="right">127,721,871</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">209,553,679</td>
<td align="right">380,461,665</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">9,110,831</td>
<td align="right">1,764,634</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">74,573,143</td>
<td align="right">14,774,251</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,095</td>
<td align="right">65,967,083</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,095</td>
<td align="right">65,967,083</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">220,183</td>
<td align="right">392,243</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">28,597,806</td>
<td align="right">6,319,213</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">28,597,806</td>
<td align="right">6,324,758</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">154,024,883</td>
<td align="right">271,608,726</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">844,652,787</td>
<td align="right">1,487,362,193</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">805,246,008</td>
<td align="right">1,416,994,701</td>
<td align="right">76.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">359,897,106</td>
<td align="right">631,681,311</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,368,599,396</td>
<td align="right">11,076,994,944</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">81,728,184</td>
<td align="right">141,308,791</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,563,640</td>
<td align="right">6,147,560</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">123,864,156</td>
<td align="right">213,408,352</td>
<td align="right">72.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,209,333,067</td>
<td align="right">12,327,180,193</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">36,373,675</td>
<td align="right">62,073,000</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">78,663,041</td>
<td align="right">133,403,296</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">256,827,589</td>
<td align="right">92,090,461</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">79,477,134</td>
<td align="right">28,547,673</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">193,378,908</td>
<td align="right">314,805,548</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">80,631,024</td>
<td align="right">30,283,093</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,142,934</td>
<td align="right">3,100,439</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,702,551</td>
<td align="right">15,694,123</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,088,379,802</td>
<td align="right">466,380,562</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">526,519,230</td>
<td align="right">827,419,740</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">527,284,156</td>
<td align="right">828,071,783</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">43,170,728</td>
<td align="right">67,703,353</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">43,169,045</td>
<td align="right">67,694,287</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,225,640,177</td>
<td align="right">9,692,319,248</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">155,706,153</td>
<td align="right">240,486,207</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,894,848,533</td>
<td align="right">9,032,300,100</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,385,354,478</td>
<td align="right">14,294,766,388</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,171,082</td>
<td align="right">2,035,609</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">66,446,669</td>
<td align="right">33,185,383</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">178,239,216</td>
<td align="right">263,968,180</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">816,218,271</td>
<td align="right">1,196,120,181</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">279,283,708</td>
<td align="right">405,783,786</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">654,259,812</td>
<td align="right">939,836,343</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">117,059,835</td>
<td align="right">167,824,007</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,848,393</td>
<td align="right">118,758,950</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">93,835,688</td>
<td align="right">134,010,657</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">807</td>
<td align="right">1,145</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">422,589,766</td>
<td align="right">595,501,291</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,935,007,647</td>
<td align="right">4,128,840,760</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">345,591,829</td>
<td align="right">484,716,505</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">68,143,705</td>
<td align="right">95,397,669</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">25,842,491</td>
<td align="right">36,170,850</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">118,208,399</td>
<td align="right">164,907,990</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">598,183,721</td>
<td align="right">833,127,962</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">222,122,524</td>
<td align="right">302,304,876</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,041,100,167</td>
<td align="right">8,192,750,985</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">148,412,611</td>
<td align="right">199,695,653</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">116,135,314</td>
<td align="right">155,164,580</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,810,185,202</td>
<td align="right">3,753,745,601</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">37,610,145</td>
<td align="right">50,092,315</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">37,610,145</td>
<td align="right">50,092,315</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">713,236,554</td>
<td align="right">948,054,643</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">38,540,302</td>
<td align="right">51,212,816</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">63,421,860</td>
<td align="right">84,101,185</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">43,351,650</td>
<td align="right">56,842,833</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,740,067,338</td>
<td align="right">3,588,943,560</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,702,661,285</td>
<td align="right">3,524,666,152</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,072,315,973</td>
<td align="right">2,701,023,025</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">472,285,871</td>
<td align="right">614,297,369</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">476,064,431</td>
<td align="right">619,187,824</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,872,054,343</td>
<td align="right">2,411,582,361</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">270,350,090</td>
<td align="right">345,303,711</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">583,456,057</td>
<td align="right">744,996,282</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,865,368,706</td>
<td align="right">3,652,701,991</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,384,030,683</td>
<td align="right">1,763,804,011</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">63,150,164</td>
<td align="right">45,887,533</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,236,587</td>
<td align="right">1,569,553</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,381,118,420</td>
<td align="right">1,752,608,778</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,297,712,034</td>
<td align="right">1,632,425,036</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,928,800,468</td>
<td align="right">2,415,335,349</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,707,401,466</td>
<td align="right">2,134,467,748</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,432,933,979</td>
<td align="right">3,017,887,421</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">124,551,953</td>
<td align="right">152,690,532</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,902,591,248</td>
<td align="right">3,526,651,885</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">576,889,483</td>
<td align="right">699,723,477</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">824,652,119</td>
<td align="right">996,008,039</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">70,904,723</td>
<td align="right">56,223,762</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">300,524,405</td>
<td align="right">359,825,417</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">511,587,429</td>
<td align="right">611,217,233</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,231,302,816</td>
<td align="right">1,464,602,020</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">420,515,546</td>
<td align="right">498,088,852</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,001,224,456</td>
<td align="right">1,169,283,133</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">671,731,799</td>
<td align="right">559,091,747</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">433,844,041</td>
<td align="right">361,670,261</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">695,686</td>
<td align="right">805,334</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">829,755,612</td>
<td align="right">957,056,919</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">75,081,718</td>
<td align="right">63,677,520</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">312,473,657</td>
<td align="right">359,913,897</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">17,266</td>
<td align="right">14,725</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">19,624,258,507</td>
<td align="right">22,454,701,413</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">98,818,398</td>
<td align="right">85,125,657</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">735,318,366</td>
<td align="right">837,095,644</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">775,440,944</td>
<td align="right">882,607,344</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,829,478,362</td>
<td align="right">2,081,332,533</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">107,550,867</td>
<td align="right">121,794,615</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">107,550,867</td>
<td align="right">121,794,549</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">302,671,747</td>
<td align="right">342,217,696</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">526,597,931</td>
<td align="right">595,343,371</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">508,055,120</td>
<td align="right">574,247,574</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">16,212,017,638</td>
<td align="right">18,321,261,326</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">729,625,404</td>
<td align="right">822,979,618</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">10,186,604,036</td>
<td align="right">11,484,078,384</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">314,903,128</td>
<td align="right">354,750,023</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">688,267,585</td>
<td align="right">774,645,686</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,010,258,697</td>
<td align="right">3,507,466,147</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,448,404,369</td>
<td align="right">5,004,958,114</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">857,678</td>
<td align="right">964,033</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,437,860,540</td>
<td align="right">1,611,700,299</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">818,310,853</td>
<td align="right">916,152,175</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,533,658,850</td>
<td align="right">3,954,522,944</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">7,353,887</td>
<td align="right">8,219,944</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,318,416,759</td>
<td align="right">1,473,417,051</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">768,354</td>
<td align="right">857,620</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">768,270</td>
<td align="right">857,523</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">916,634,180</td>
<td align="right">1,020,659,091</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">124,553,926</td>
<td align="right">138,674,807</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">296,777,285</td>
<td align="right">328,225,868</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,087,041,953</td>
<td align="right">1,199,471,550</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,020,649,001</td>
<td align="right">2,215,696,711</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,176,021,411</td>
<td align="right">1,967,586,195</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">8,412,013,591</td>
<td align="right">7,659,595,084</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,167,989,806</td>
<td align="right">1,268,863,678</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">774,824,336</td>
<td align="right">840,071,071</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">25,111,829</td>
<td align="right">22,997,862</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">72,836,895</td>
<td align="right">78,953,909</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">29,982,444</td>
<td align="right">32,499,481</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,044,622,822</td>
<td align="right">8,684,514,620</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,358,700,333</td>
<td align="right">1,465,948,532</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,067,389,356</td>
<td align="right">2,226,562,913</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">72,822,346</td>
<td align="right">78,181,461</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,981,833,455</td>
<td align="right">5,335,995,166</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">308,442,256</td>
<td align="right">329,768,265</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">54,227,907</td>
<td align="right">57,943,624</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,865,961,321</td>
<td align="right">1,745,182,748</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">501,464,439</td>
<td align="right">470,130,427</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,041,297,478</td>
<td align="right">3,223,654,450</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,791,692,557</td>
<td align="right">4,014,554,017</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">617,619,122</td>
<td align="right">583,337,712</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,929,819,076</td>
<td align="right">2,035,078,648</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">956,553,512</td>
<td align="right">1,006,036,708</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">622,492,195</td>
<td align="right">653,914,633</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">871,090,135</td>
<td align="right">830,153,551</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">438,999,830</td>
<td align="right">458,301,565</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">270,210,582</td>
<td align="right">281,864,101</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">489,006,599</td>
<td align="right">468,878,567</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">52,509,145</td>
<td align="right">54,600,593</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">181,942,370</td>
<td align="right">174,874,994</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,740,568,687</td>
<td align="right">2,841,709,577</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,368,130,062</td>
<td align="right">2,448,986,449</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">208,355,034</td>
<td align="right">215,452,890</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">541,556,222</td>
<td align="right">558,950,500</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">51,980,959</td>
<td align="right">53,532,434</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">399,950,250</td>
<td align="right">411,466,824</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">159,219,038</td>
<td align="right">163,444,327</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,010,291,715</td>
<td align="right">1,033,316,758</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,349,203,170</td>
<td align="right">1,378,762,599</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,188,053,706</td>
<td align="right">4,275,613,000</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,733,322</td>
<td align="right">61,771,970</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,067,063,058</td>
<td align="right">1,083,159,275</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,720,858,057</td>
<td align="right">1,746,261,783</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,865,444,182</td>
<td align="right">1,890,286,885</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">2,925,410,628</td>
<td align="right">2,962,204,873</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,629,813,307</td>
<td align="right">1,649,490,158</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">81,844,246</td>
<td align="right">82,816,641</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">390,243,734</td>
<td align="right">385,681,672</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,849,967,368</td>
<td align="right">1,829,364,503</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">4,219,689</td>
<td align="right">4,265,064</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">4,220,711</td>
<td align="right">4,265,697</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,898,093,704</td>
<td align="right">1,917,340,035</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">98,767,754</td>
<td align="right">99,607,548</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">124,942,360</td>
<td align="right">125,491,864</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">556,160,168</td>
<td align="right">554,338,262</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">590,723,168</td>
<td align="right">588,906,897</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">591,741,728</td>
<td align="right">589,925,457</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">562,440</td>
<td align="right">561,600</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">101,691,756</td>
<td align="right">101,826,331</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,545,341</td>
<td align="right">24,516,449</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">112,473,853</td>
<td align="right">112,463,797</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">43,050,050</td>
<td align="right">43,051,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,527,364</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_WITH_SPEC</td>
<td align="right">2,417</td>
<td align="right">2,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">2,189,094</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">84,305</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_UPDATE</td>
<td align="right"></td>
<td align="right">16,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_LOCALS</td>
<td align="right"></td>
<td align="right">2,530</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FROM_DICT_OR_DEREF</td>
<td align="right"></td>
<td align="right">1,265</td>
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
<td align="left">RAISE_VARARGS</td>
<td align="right">2,161</td>
<td align="right">7,119</td>
<td align="right">229.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">52,007</td>
<td align="right">114,343</td>
<td align="right">119.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">23,746</td>
<td align="right">42,590</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">126</td>
<td align="right">197</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">29,926</td>
<td align="right">30,047</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right"></td>
<td align="right">7,500</td>
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
<td align="right">247</td>
<td align="right">393</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">247</td>
<td align="right">393</td>
<td align="right">59.1%</td>
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
<td align="right">29</td>
<td align="right">29</td>
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
<td align="right">29</td>
<td align="right">29</td>
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
<td align="right">1,794</td>
<td align="right">1,794</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-25
