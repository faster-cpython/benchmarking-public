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
<td align="right">36,749,241</td>
<td align="right">116,331,572</td>
<td align="right">216.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">35,312,939</td>
<td align="right">88,093,825</td>
<td align="right">149.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">40,179,544</td>
<td align="right">92,405,089</td>
<td align="right">130.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">20,062,199</td>
<td align="right">45,919,616</td>
<td align="right">128.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">26,752,133</td>
<td align="right">59,789,837</td>
<td align="right">123.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,906,638,794</td>
<td align="right">4,129,017,416</td>
<td align="right">116.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">128,675,408</td>
<td align="right">274,970,374</td>
<td align="right">113.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">254,591,287</td>
<td align="right">190,741</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">63,837,742</td>
<td align="right">114,292</td>
<td align="right">-99.8%</td>
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
<td align="right">269</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">50,929,909</td>
<td align="right">438,827</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,071,384</td>
<td align="right">37,238</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,918,031</td>
<td align="right">295,978</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,623,266</td>
<td align="right">69,250</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,723</td>
<td align="right">903</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,596,758</td>
<td align="right">103,568</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,850,921</td>
<td align="right">619,968</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,186,338</td>
<td align="right">159,464</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">90,486,205</td>
<td align="right">12,347,172</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,873,685</td>
<td align="right">1,190,419</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">178,985,538</td>
<td align="right">27,720,534</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">794,670,199</td>
<td align="right">126,519,134</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,108,386</td>
<td align="right">1,176,168</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,280,501</td>
<td align="right">4,154,261</td>
<td align="right">82.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">69,086,884</td>
<td align="right">125,488,570</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">801,055,954</td>
<td align="right">169,752,828</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">38,346,277</td>
<td align="right">8,168,182</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">212,906,617</td>
<td align="right">46,321,074</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">51,180,648</td>
<td align="right">11,490,392</td>
<td align="right">-77.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">28,919,713</td>
<td align="right">6,618,637</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">27,971,251</td>
<td align="right">7,100,695</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">58,519,767</td>
<td align="right">16,231,886</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,513,911,988</td>
<td align="right">980,645,869</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">447</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">120,374,667</td>
<td align="right">37,251,248</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">150,356,794</td>
<td align="right">47,822,906</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">109,163,801</td>
<td align="right">35,454,724</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">451,724,727</td>
<td align="right">151,391,865</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,547,064</td>
<td align="right">12,551,978</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">254,828,246</td>
<td align="right">86,834,597</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">113,259,659</td>
<td align="right">38,944,303</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">43,982,117</td>
<td align="right">16,614,883</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">178,174,162</td>
<td align="right">69,061,635</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,280,815,050</td>
<td align="right">502,540,700</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">147,958,451</td>
<td align="right">58,122,052</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">93,506,360</td>
<td align="right">37,116,235</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">91,913,894</td>
<td align="right">36,600,952</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">596,821,576</td>
<td align="right">244,499,281</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">78,125,122</td>
<td align="right">32,044,111</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">22,954,180</td>
<td align="right">9,517,752</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">247,398,917</td>
<td align="right">102,853,007</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">149,941,237</td>
<td align="right">63,343,315</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">473,050,984</td>
<td align="right">200,247,345</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,649</td>
<td align="right">1,591</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">50,942,653</td>
<td align="right">22,658,564</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,836,103,518</td>
<td align="right">1,287,454,013</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">170,939</td>
<td align="right">78,312</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">105,494,071</td>
<td align="right">48,850,145</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">308,508,080</td>
<td align="right">144,391,699</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">83,643,107</td>
<td align="right">39,985,503</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">287,761,618</td>
<td align="right">138,696,306</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">592,329</td>
<td align="right">286,085</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">119,703,384</td>
<td align="right">57,917,739</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">33,097,850</td>
<td align="right">50,076,120</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,950,660,364</td>
<td align="right">953,058,222</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">131,652,097</td>
<td align="right">66,019,484</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">220,528,636</td>
<td align="right">112,882,556</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">352,877,206</td>
<td align="right">181,244,507</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">156,267,615</td>
<td align="right">81,878,012</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">86,006,929</td>
<td align="right">45,963,026</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,269,922</td>
<td align="right">5,489,153</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">400,810,546</td>
<td align="right">215,967,123</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,998,983,626</td>
<td align="right">1,084,076,062</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">404,234,897</td>
<td align="right">227,653,943</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">59,046,452</td>
<td align="right">33,814,830</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">596,587,471</td>
<td align="right">346,016,685</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">83,367,429</td>
<td align="right">117,478,329</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">112,100,346</td>
<td align="right">66,922,027</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,258,314,899</td>
<td align="right">1,976,150,751</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">12,988,394</td>
<td align="right">7,891,760</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">57,421,645</td>
<td align="right">35,145,006</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">66,590,623</td>
<td align="right">41,544,694</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">43,386,341</td>
<td align="right">27,558,059</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,757,690,061</td>
<td align="right">7,508,953,451</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,797,873,570</td>
<td align="right">1,806,083,530</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">485,445,977</td>
<td align="right">314,774,266</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">145,222,620</td>
<td align="right">94,206,307</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,408,542</td>
<td align="right">11,396,679</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">581,682,835</td>
<td align="right">381,752,304</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">80,230,216</td>
<td align="right">52,789,620</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">151,843,598</td>
<td align="right">203,340,106</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">82,481,910</td>
<td align="right">55,523,595</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">279,356,046</td>
<td align="right">193,436,397</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">45,852,382</td>
<td align="right">32,617,864</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">258,121,930</td>
<td align="right">186,238,746</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,030,613,546</td>
<td align="right">743,727,671</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">40,447,884</td>
<td align="right">51,514,249</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">486,138,624</td>
<td align="right">357,317,898</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">73,344,787</td>
<td align="right">54,133,874</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">5,762,082</td>
<td align="right">4,266,138</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">38,196,499</td>
<td align="right">28,383,282</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,475,443,185</td>
<td align="right">1,103,819,859</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">426,057,693</td>
<td align="right">320,069,662</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">162,524,904</td>
<td align="right">122,147,351</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">583,437,789</td>
<td align="right">440,108,304</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">77,962,546</td>
<td align="right">59,049,927</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">111,611,134</td>
<td align="right">86,666,585</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">205,137,714</td>
<td align="right">160,090,302</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,844,585</td>
<td align="right">42,037,864</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">201,152,438</td>
<td align="right">157,423,143</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">15,122,503</td>
<td align="right">11,875,025</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">351,580,966</td>
<td align="right">278,855,291</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">212,645</td>
<td align="right">251,984</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,769,786,833</td>
<td align="right">3,266,164,954</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,334,845,129</td>
<td align="right">2,757,069,066</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">342,272,536</td>
<td align="right">400,912,753</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">240,370,362</td>
<td align="right">279,242,308</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">653,739,423</td>
<td align="right">759,079,324</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">53,714</td>
<td align="right">45,482</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">514,000,528</td>
<td align="right">435,906,486</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">45,770,979</td>
<td align="right">39,328,956</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">269,893,414</td>
<td align="right">233,222,041</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">501,850</td>
<td align="right">435,938</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">743,421</td>
<td align="right">647,464</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">104,346,053</td>
<td align="right">91,782,755</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">199,783,091</td>
<td align="right">223,326,114</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">24,225,047</td>
<td align="right">21,447,787</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">42,370</td>
<td align="right">37,905</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,579,726,075</td>
<td align="right">1,420,268,700</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">187,371,488</td>
<td align="right">170,080,656</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">170,900,533</td>
<td align="right">155,295,520</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,181,259,539</td>
<td align="right">2,351,007,618</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">43,447,085</td>
<td align="right">40,153,490</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,374,692</td>
<td align="right">42,388,883</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">24,362,698</td>
<td align="right">22,774,132</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">107,314,986</td>
<td align="right">113,423,472</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">111,306,863</td>
<td align="right">105,923,661</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">26,801,770</td>
<td align="right">28,007,116</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">74,820,492</td>
<td align="right">71,893,703</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">168,492,385</td>
<td align="right">173,019,009</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">35,312,468</td>
<td align="right">34,409,188</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">203,269,986</td>
<td align="right">207,569,963</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">45,724,520</td>
<td align="right">44,768,174</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">34,808,342</td>
<td align="right">34,127,735</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">32,740,599</td>
<td align="right">32,201,065</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">31,919,522</td>
<td align="right">31,403,930</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,482,957,414</td>
<td align="right">1,505,501,136</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">8,699,005</td>
<td align="right">8,588,242</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,482</td>
<td align="right">3,440</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,361,109</td>
<td align="right">3,401,479</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,741,825</td>
<td align="right">2,717,698</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">172,850,769</td>
<td align="right">171,409,676</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">153,205,490</td>
<td align="right">151,964,346</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,364,787</td>
<td align="right">11,281,007</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">16,648,893</td>
<td align="right">16,544,308</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">16,985,744</td>
<td align="right">16,880,917</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">16,984,914</td>
<td align="right">16,880,636</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,747,512,001</td>
<td align="right">1,739,180,109</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">149,307,099</td>
<td align="right">150,018,850</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,449,457</td>
<td align="right">3,433,392</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">218,580</td>
<td align="right">219,420</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">54,186,715</td>
<td align="right">54,054,719</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,409,806</td>
<td align="right">4,400,902</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,038,075,188</td>
<td align="right">1,036,985,452</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">18,502</td>
<td align="right">18,491</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">347,752</td>
<td align="right">347,597</td>
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
<td align="right">100,821,455</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">116,918</td>
<td align="right">116,917</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,688,866</td>
<td align="right">14,688,798</td>
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
<td align="right">138,349,870</td>
<td align="right">1.9%</td>
<td align="right">-51.8%</td>
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
<td align="right">21,308,607</td>
<td align="right">0.3%</td>
<td align="right">-2.9%</td>
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
<td align="right">7,270,543,650</td>
<td align="right">97.8%</td>
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
<td align="right">753,153</td>
<td align="right">64.2%</td>
<td align="right">340,333</td>
<td align="right">45.5%</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">420,238</td>
<td align="right">35.8%</td>
<td align="right">408,143</td>
<td align="right">54.5%</td>
<td align="right">-2.9%</td>
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
<td align="right">108,524</td>
<td align="right">31.9%</td>
<td align="right">293.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">52,638</td>
<td align="right">7.0%</td>
<td align="right">141,730</td>
<td align="right">41.6%</td>
<td align="right">169.3%</td>
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
<td align="right">30,323</td>
<td align="right">8.9%</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">18,739</td>
<td align="right">2.5%</td>
<td align="right">2,059</td>
<td align="right">0.6%</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">2,609</td>
<td align="right">0.3%</td>
<td align="right">598</td>
<td align="right">0.2%</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,328</td>
<td align="right">0.3%</td>
<td align="right">797</td>
<td align="right">0.2%</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">4,184</td>
<td align="right">0.6%</td>
<td align="right">1,954</td>
<td align="right">0.6%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">5,867</td>
<td align="right">0.8%</td>
<td align="right">2,984</td>
<td align="right">0.9%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">4,618</td>
<td align="right">0.6%</td>
<td align="right">2,765</td>
<td align="right">0.8%</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">7,793</td>
<td align="right">1.0%</td>
<td align="right">10,591</td>
<td align="right">3.1%</td>
<td align="right">35.9%</td>
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
<td align="left">rshift</td>
<td align="right">2,826</td>
<td align="right">0.4%</td>
<td align="right">2,189</td>
<td align="right">0.6%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">21,614</td>
<td align="right">2.9%</td>
<td align="right">17,177</td>
<td align="right">5.0%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,052</td>
<td align="right">0.1%</td>
<td align="right">908</td>
<td align="right">0.3%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">5,973</td>
<td align="right">0.8%</td>
<td align="right">5,238</td>
<td align="right">1.5%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">492</td>
<td align="right">0.1%</td>
<td align="right">433</td>
<td align="right">0.1%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">735</td>
<td align="right">0.1%</td>
<td align="right">666</td>
<td align="right">0.2%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">9,703</td>
<td align="right">1.3%</td>
<td align="right">8,886</td>
<td align="right">2.6%</td>
<td align="right">-8.4%</td>
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
<td align="right">45,963,026</td>
<td align="right">100.0%</td>
<td align="right">-46.6%</td>
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
<td align="right">319,956,651</td>
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
<td align="right">5,704,585</td>
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
<td align="right">4,778,394,819</td>
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
<td align="right">104,775</td>
<td align="right">47.5%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">116,619</td>
<td align="right">46.4%</td>
<td align="right">115,653</td>
<td align="right">52.5%</td>
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
<td align="left">buffer slice</td>
<td align="right">793</td>
<td align="right">0.6%</td>
<td align="right">311</td>
<td align="right">0.3%</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,437</td>
<td align="right">9.2%</td>
<td align="right">6,481</td>
<td align="right">6.2%</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">45,171</td>
<td align="right">33.6%</td>
<td align="right">29,039</td>
<td align="right">27.7%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">18,032</td>
<td align="right">13.4%</td>
<td align="right">23,474</td>
<td align="right">22.4%</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,491</td>
<td align="right">2.6%</td>
<td align="right">2,532</td>
<td align="right">2.4%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">36,434</td>
<td align="right">27.1%</td>
<td align="right">26,461</td>
<td align="right">25.3%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">10,357</td>
<td align="right">7.7%</td>
<td align="right">9,158</td>
<td align="right">8.7%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,811</td>
<td align="right">3.6%</td>
<td align="right">4,284</td>
<td align="right">4.1%</td>
<td align="right">-11.0%</td>
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
<td align="right">122,478,587</td>
<td align="right">1.1%</td>
<td align="right">2.5%</td>
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
<td align="right">10,545,828,028</td>
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
<td align="right">204,252</td>
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
<td align="right">2,413,182</td>
<td align="right">100.0%</td>
<td align="right">2,463,719</td>
<td align="right">100.0%</td>
<td align="right">2.1%</td>
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
<td align="right">210,059</td>
<td align="right">64.2%</td>
<td align="right">-60.2%</td>
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
<td align="right">33.5%</td>
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
<td align="right">461,489</td>
<td align="right">0.0%</td>
<td align="right">-49.4%</td>
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
<td align="right">58,988,945</td>
<td align="right">1.3%</td>
<td align="right">-24.2%</td>
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
<td align="right">4,355,682,945</td>
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
<td align="right">53,181</td>
<td align="right">76.4%</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">24,968</td>
<td align="right">23.1%</td>
<td align="right">16,390</td>
<td align="right">23.6%</td>
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
<td align="right">9,850</td>
<td align="right">18.5%</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">25,591</td>
<td align="right">30.9%</td>
<td align="right">13,427</td>
<td align="right">25.2%</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,999</td>
<td align="right">4.8%</td>
<td align="right">2,371</td>
<td align="right">4.5%</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,190</td>
<td align="right">7.5%</td>
<td align="right">4,407</td>
<td align="right">8.3%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,514</td>
<td align="right">7.9%</td>
<td align="right">4,856</td>
<td align="right">9.1%</td>
<td align="right">-25.5%</td>
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
<td align="right">7,699</td>
<td align="right">14.5%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">979</td>
<td align="right">1.2%</td>
<td align="right">998</td>
<td align="right">1.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">666</td>
<td align="right">0.8%</td>
<td align="right">654</td>
<td align="right">1.2%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,554</td>
<td align="right">9.1%</td>
<td align="right">7,464</td>
<td align="right">14.0%</td>
<td align="right">-1.2%</td>
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
<td align="right">66,021</td>
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
<td align="right">34,381,307</td>
<td align="right">1.8%</td>
<td align="right">-2.5%</td>
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
<td align="right">1,898,262,701</td>
<td align="right">98.2%</td>
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
<td align="right">38,417</td>
<td align="right">56.1%</td>
<td align="right">3,497</td>
<td align="right">12.0%</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">30,008</td>
<td align="right">43.9%</td>
<td align="right">25,617</td>
<td align="right">88.0%</td>
<td align="right">-14.6%</td>
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
<td align="right">4,964</td>
<td align="right">19.4%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,910</td>
<td align="right">36.4%</td>
<td align="right">8,132</td>
<td align="right">31.7%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">4,852</td>
<td align="right">16.2%</td>
<td align="right">5,944</td>
<td align="right">23.2%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,367</td>
<td align="right">24.6%</td>
<td align="right">6,577</td>
<td align="right">25.7%</td>
<td align="right">-10.7%</td>
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
<td align="right">54,098,248</td>
<td align="right">10.7%</td>
<td align="right">-26.2%</td>
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
<td align="right">29,512,004</td>
<td align="right">5.9%</td>
<td align="right">17.1%</td>
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
<td align="right">420,440,374</td>
<td align="right">83.4%</td>
<td align="right">-16.0%</td>
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
<td align="right">32,073</td>
<td align="right">5.4%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">479,041</td>
<td align="right">92.0%</td>
<td align="right">560,292</td>
<td align="right">94.6%</td>
<td align="right">17.0%</td>
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
<td align="right">3,496</td>
<td align="right">10.9%</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,606</td>
<td align="right">8.7%</td>
<td align="right">1,181</td>
<td align="right">3.7%</td>
<td align="right">-67.2%</td>
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
<td align="right">565</td>
<td align="right">1.8%</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,814</td>
<td align="right">4.4%</td>
<td align="right">978</td>
<td align="right">3.0%</td>
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
<td align="right">3.8%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">14,021</td>
<td align="right">33.7%</td>
<td align="right">10,008</td>
<td align="right">31.2%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,594</td>
<td align="right">8.6%</td>
<td align="right">2,592</td>
<td align="right">8.1%</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,666</td>
<td align="right">16.0%</td>
<td align="right">6,043</td>
<td align="right">18.8%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">3,410</td>
<td align="right">8.2%</td>
<td align="right">3,180</td>
<td align="right">9.9%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,369</td>
<td align="right">5.7%</td>
<td align="right">2,234</td>
<td align="right">7.0%</td>
<td align="right">-5.7%</td>
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
<td align="right">263,025</td>
<td align="right">0.0%</td>
<td align="right">-56.0%</td>
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
<td align="right">226,636,630</td>
<td align="right">1.8%</td>
<td align="right">-43.8%</td>
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
<td align="right">369,209,230</td>
<td align="right">3.0%</td>
<td align="right">-10.5%</td>
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
<td align="right">11,793,867,959</td>
<td align="right">95.2%</td>
<td align="right">-1.3%</td>
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
<td align="right">134,393</td>
<td align="right">1.7%</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,874,708</td>
<td align="right">97.8%</td>
<td align="right">7,840,988</td>
<td align="right">98.3%</td>
<td align="right">-11.6%</td>
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
<td align="left">expected error</td>
<td align="right">2,405</td>
<td align="right">1.2%</td>
<td align="right">278</td>
<td align="right">0.2%</td>
<td align="right">-88.4%</td>
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
<td align="left">overridden</td>
<td align="right">7,718</td>
<td align="right">3.8%</td>
<td align="right">2,255</td>
<td align="right">1.7%</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">20,115</td>
<td align="right">9.9%</td>
<td align="right">8,421</td>
<td align="right">6.3%</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,293</td>
<td align="right">7.1%</td>
<td align="right">6,208</td>
<td align="right">4.6%</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">42,453</td>
<td align="right">21.0%</td>
<td align="right">22,754</td>
<td align="right">16.9%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">48</td>
<td align="right">0.0%</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,425</td>
<td align="right">0.7%</td>
<td align="right">806</td>
<td align="right">0.6%</td>
<td align="right">-43.4%</td>
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
<td align="right">849</td>
<td align="right">0.6%</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">165</td>
<td align="right">0.1%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,420</td>
<td align="right">0.7%</td>
<td align="right">1,001</td>
<td align="right">0.7%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">51,457</td>
<td align="right">25.4%</td>
<td align="right">40,648</td>
<td align="right">30.2%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,268</td>
<td align="right">0.6%</td>
<td align="right">1,041</td>
<td align="right">0.8%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,001</td>
<td align="right">2.5%</td>
<td align="right">4,181</td>
<td align="right">3.1%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">37,339</td>
<td align="right">18.5%</td>
<td align="right">31,805</td>
<td align="right">23.7%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">901</td>
<td align="right">0.4%</td>
<td align="right">850</td>
<td align="right">0.6%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,521</td>
<td align="right">3.7%</td>
<td align="right">7,186</td>
<td align="right">5.3%</td>
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
<td align="right">1,586,103,597</td>
<td align="right">99.1%</td>
<td align="right">-53.0%</td>
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
<td align="right">32,844</td>
<td align="right">0.0%</td>
<td align="right">1.7%</td>
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
<td align="right">14,586,218</td>
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
<td align="right">103,367</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">62,827,959</td>
<td align="right">100.0%</td>
<td align="right">62,520,968</td>
<td align="right">100.0%</td>
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
<td align="right">593,151,034</td>
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
<td align="right">78,645,931</td>
<td align="right">4.0%</td>
<td align="right">-24.6%</td>
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
<td align="right">41,974,391</td>
<td align="right">2.1%</td>
<td align="right">-21.9%</td>
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
<td align="right">1,846,823,210</td>
<td align="right">93.9%</td>
<td align="right">0.7%</td>
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
<td align="right">1,514,961</td>
<td align="right">97.9%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">41,632</td>
<td align="right">2.0%</td>
<td align="right">31,796</td>
<td align="right">2.1%</td>
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
<td align="left">not managed dict</td>
<td align="right">2,002</td>
<td align="right">4.8%</td>
<td align="right">519</td>
<td align="right">1.6%</td>
<td align="right">-74.1%</td>
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
<td align="right">241</td>
<td align="right">0.8%</td>
<td align="right">-34.0%</td>
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
<td align="right">636</td>
<td align="right">2.0%</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">20,147</td>
<td align="right">48.4%</td>
<td align="right">14,503</td>
<td align="right">45.6%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">8,492</td>
<td align="right">20.4%</td>
<td align="right">7,152</td>
<td align="right">22.5%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,744</td>
<td align="right">4.2%</td>
<td align="right">1,553</td>
<td align="right">4.9%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,633</td>
<td align="right">11.1%</td>
<td align="right">4,432</td>
<td align="right">13.9%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,913</td>
<td align="right">4.6%</td>
<td align="right">1,841</td>
<td align="right">5.8%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">93</td>
<td align="right">0.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">109</td>
<td align="right">0.3%</td>
<td align="right">-0.9%</td>
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
<td align="right">251,984</td>
<td align="right">100.0%</td>
<td align="right">18.5%</td>
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
<td align="right">117,436,404</td>
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
<td align="right">668,231,089</td>
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
<td align="right">39,691</td>
<td align="right">94.6%</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,293</td>
<td align="right">6.7%</td>
<td align="right">2,254</td>
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
<td align="right">13,742</td>
<td align="right">34.6%</td>
<td align="right">463.0%</td>
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
<td align="right">7,067</td>
<td align="right">17.8%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">500</td>
<td align="right">1.6%</td>
<td align="right">415</td>
<td align="right">1.0%</td>
<td align="right">-17.0%</td>
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
<td align="right">16,494</td>
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
<td align="right">37,077,778</td>
<td align="right">0.8%</td>
<td align="right">-69.1%</td>
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
<td align="right">21,860,412</td>
<td align="right">0.5%</td>
<td align="right">-10.2%</td>
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
<td align="right">4,567,740,824</td>
<td align="right">98.7%</td>
<td align="right">0.9%</td>
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
<td align="right">138,153</td>
<td align="right">23.6%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">493,342</td>
<td align="right">64.0%</td>
<td align="right">446,560</td>
<td align="right">76.4%</td>
<td align="right">-9.5%</td>
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
<td align="right">3,532</td>
<td align="right">2.6%</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">12,019</td>
<td align="right">4.3%</td>
<td align="right">3,183</td>
<td align="right">2.3%</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,442</td>
<td align="right">3.4%</td>
<td align="right">3,333</td>
<td align="right">2.4%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">143,764</td>
<td align="right">51.9%</td>
<td align="right">51,233</td>
<td align="right">37.1%</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">10,049</td>
<td align="right">3.6%</td>
<td align="right">5,755</td>
<td align="right">4.2%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">431</td>
<td align="right">0.2%</td>
<td align="right">551</td>
<td align="right">0.4%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">75,404</td>
<td align="right">27.2%</td>
<td align="right">59,842</td>
<td align="right">43.3%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">3,898</td>
<td align="right">1.4%</td>
<td align="right">3,408</td>
<td align="right">2.5%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,117</td>
<td align="right">2.9%</td>
<td align="right">7,313</td>
<td align="right">5.3%</td>
<td align="right">-9.9%</td>
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
<td align="right">278,137</td>
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
<td align="right">1,175,072,725</td>
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
<td align="right">573</td>
<td align="right">7.1%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,455</td>
<td align="right">91.4%</td>
<td align="right">7,455</td>
<td align="right">92.9%</td>
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
<td align="left">sequence</td>
<td align="right">471</td>
<td align="right">66.8%</td>
<td align="right">359</td>
<td align="right">62.7%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">143</td>
<td align="right">20.3%</td>
<td align="right">123</td>
<td align="right">21.5%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">12.9%</td>
<td align="right">91</td>
<td align="right">15.9%</td>
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
<td align="right">12,383,385,109</td>
<td align="right">25.0%</td>
<td align="right">-46.7%</td>
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
<td align="right">1,221,531,797</td>
<td align="right">2.5%</td>
<td align="right">-31.9%</td>
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
<td align="right">35,325,095,962</td>
<td align="right">71.2%</td>
<td align="right">-16.6%</td>
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
<td align="right">649,730,227</td>
<td align="right">1.3%</td>
<td align="right">-9.4%</td>
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
<td align="right">37,077,778</td>
<td align="right">3.0%</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">287,002,287</td>
<td align="right">16.0%</td>
<td align="right">138,349,870</td>
<td align="right">11.3%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">86,006,929</td>
<td align="right">4.8%</td>
<td align="right">45,963,026</td>
<td align="right">3.8%</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">402,931,896</td>
<td align="right">22.5%</td>
<td align="right">226,636,630</td>
<td align="right">18.6%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">83,333,305</td>
<td align="right">4.7%</td>
<td align="right">117,436,404</td>
<td align="right">9.6%</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">73,299,646</td>
<td align="right">4.1%</td>
<td align="right">54,098,248</td>
<td align="right">4.4%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">425,914,895</td>
<td align="right">23.8%</td>
<td align="right">319,956,651</td>
<td align="right">26.2%</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">77,871,788</td>
<td align="right">4.3%</td>
<td align="right">58,988,945</td>
<td align="right">4.8%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,771,275</td>
<td align="right">3.0%</td>
<td align="right">41,974,391</td>
<td align="right">3.4%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,069,587</td>
<td align="right">7.2%</td>
<td align="right">129,059,374</td>
<td align="right">10.6%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">50,344,150</td>
<td align="right">7.0%</td>
<td align="right">13,650,273</td>
<td align="right">2.1%</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">63,177,505</td>
<td align="right">8.8%</td>
<td align="right">45,217,078</td>
<td align="right">7.0%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">103,586,068</td>
<td align="right">14.4%</td>
<td align="right">121,610,309</td>
<td align="right">18.7%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">86,770,130</td>
<td align="right">12.1%</td>
<td align="right">71,737,821</td>
<td align="right">11.0%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">62,108,468</td>
<td align="right">8.7%</td>
<td align="right">68,431,971</td>
<td align="right">10.5%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">154,941,740</td>
<td align="right">21.6%</td>
<td align="right">161,791,231</td>
<td align="right">24.9%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">15,190,654</td>
<td align="right">2.1%</td>
<td align="right">14,625,332</td>
<td align="right">2.3%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,966,807</td>
<td align="right">2.9%</td>
<td align="right">20,927,334</td>
<td align="right">3.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">18,179,063</td>
<td align="right">2.5%</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">14,749,307</td>
<td align="right">2.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">14,734,724</td>
<td align="right">2.3%</td>
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
<td align="right">273,909,619</td>
<td align="right">4.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,113,049,163</td>
<td align="right">17.0%</td>
<td align="right">1,105,688,874</td>
<td align="right">16.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,115,181,372</td>
<td align="right">17.0%</td>
<td align="right">1,107,821,083</td>
<td align="right">16.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,752,570,037</td>
<td align="right">26.7%</td>
<td align="right">1,744,192,246</td>
<td align="right">26.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,752,570,037</td>
<td align="right">26.7%</td>
<td align="right">1,744,192,246</td>
<td align="right">26.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,999,805</td>
<td align="right">0.4%</td>
<td align="right">24,911,460</td>
<td align="right">0.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,198,958,378</td>
<td align="right">79.2%</td>
<td align="right">5,181,848,400</td>
<td align="right">79.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">69,836,315</td>
<td align="right">1.1%</td>
<td align="right">69,651,177</td>
<td align="right">1.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">637,388,665</td>
<td align="right">9.7%</td>
<td align="right">636,371,163</td>
<td align="right">9.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,811,443,131</td>
<td align="right">73.3%</td>
<td align="right">4,804,227,034</td>
<td align="right">73.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">262,223,337</td>
<td align="right">4.0%</td>
<td align="right">261,833,152</td>
<td align="right">4.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">133,173,287</td>
<td align="right">2.0%</td>
<td align="right">133,173,889</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">6,687,067</td>
<td align="right"></td>
<td align="right">9,279,010</td>
<td align="right"></td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">31,993,543,188</td>
<td align="right">19.6%</td>
<td align="right">23,111,757,397</td>
<td align="right">13.8%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">12,160,706,939</td>
<td align="right">7.5%</td>
<td align="right">9,347,595,772</td>
<td align="right">5.6%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">76,209,001,041</td>
<td align="right">46.8%</td>
<td align="right">91,119,419,855</td>
<td align="right">54.4%</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">15,045,155,414</td>
<td align="right">7.7%</td>
<td align="right">12,672,085,960</td>
<td align="right">6.2%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">81,417,572,285</td>
<td align="right">41.8%</td>
<td align="right">92,775,131,541</td>
<td align="right">45.7%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">43,604,787,794</td>
<td align="right">22.4%</td>
<td align="right">38,240,637,021</td>
<td align="right">18.8%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">63,518,754</td>
<td align="right"></td>
<td align="right">71,028,333</td>
<td align="right"></td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">57,618,927</td>
<td align="right"></td>
<td align="right">62,536,652</td>
<td align="right"></td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">54,761,382,397</td>
<td align="right">28.1%</td>
<td align="right">59,250,264,129</td>
<td align="right">29.2%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">1,968,101,296</td>
<td align="right"></td>
<td align="right">1,875,282,291</td>
<td align="right"></td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">42,635,489,406</td>
<td align="right">26.2%</td>
<td align="right">43,864,328,541</td>
<td align="right">26.2%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">177,764,102</td>
<td align="right"></td>
<td align="right">173,142,976</td>
<td align="right"></td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,336,731</td>
<td align="right">0.4%</td>
<td align="right">72,547,312</td>
<td align="right">0.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,053,919,796</td>
<td align="right"></td>
<td align="right">3,030,392,321</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">9,955,635,808</td>
<td align="right">54.2%</td>
<td align="right">9,928,782,455</td>
<td align="right">54.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,033,278,166</td>
<td align="right">54.6%</td>
<td align="right">10,007,644,428</td>
<td align="right">54.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,615,107,069</td>
<td align="right"></td>
<td align="right">10,589,272,701</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,347,129,242</td>
<td align="right">45.4%</td>
<td align="right">8,327,825,147</td>
<td align="right">45.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,347,263,938</td>
<td align="right"></td>
<td align="right">8,328,006,984</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,305,627</td>
<td align="right">0.0%</td>
<td align="right">6,314,661</td>
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
<td align="right">353,932</td>
<td align="right">100,119,768</td>
<td align="right">15,043,556,669</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,438</td>
<td align="right">5,249,711,658</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,249,683,948</td>
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
<td align="right">100,197</td>
<td align="right">2.4%</td>
<td align="right">605.4%</td>
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
<td align="right">2,460,465</td>
<td align="right">59.5%</td>
<td align="right">228.1%</td>
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
<td align="right">2,289,097</td>
<td align="right">55.3%</td>
<td align="right">210.9%</td>
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
<td align="right">4,137,107</td>
<td align="right"></td>
<td align="right">181.9%</td>
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
<td align="right">10,527</td>
<td align="right">0.4%</td>
<td align="right">180.7%</td>
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
<td align="right">19,353</td>
<td align="right">0.5%</td>
<td align="right">158.9%</td>
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
<td align="right">1,676,120</td>
<td align="right">40.5%</td>
<td align="right">134.2%</td>
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
<td align="right">380</td>
<td align="right">0.0%</td>
<td align="right">90.0%</td>
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
<td align="right">522</td>
<td align="right">0.0%</td>
<td align="right">-72.3%</td>
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
<td align="right">11,506,507,117</td>
<td align="right"></td>
<td align="right">59.6%</td>
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
<td align="right">292,903,139,709</td>
<td align="right">2,545.5%</td>
<td align="right">20.5%</td>
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
<td align="right">8,528</td>
<td align="right">0.2%</td>
<td align="right">-3.2%</td>
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
<td align="right">2,424,124</td>
<td align="right">98.5%</td>
<td align="right">238.3%</td>
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
<td align="right">2,460,465</td>
<td align="right"></td>
<td align="right">228.1%</td>
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
<td align="right">435</td>
<td align="right">0.0%</td>
<td align="right">-2.9%</td>
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
<td align="right">1,451</td>
<td align="right">0.1%</td>
<td align="right">1,451 / 0 !!</td>
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
<td align="right">43,414</td>
<td align="right">1.8%</td>
<td align="right">43,414 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">52,502</td>
<td align="right">7.0%</td>
<td align="right">113,666</td>
<td align="right">4.6%</td>
<td align="right">116.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">136,850</td>
<td align="right">18.3%</td>
<td align="right">335,537</td>
<td align="right">13.6%</td>
<td align="right">145.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">258,840</td>
<td align="right">34.5%</td>
<td align="right">969,762</td>
<td align="right">39.4%</td>
<td align="right">274.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">193,364</td>
<td align="right">25.8%</td>
<td align="right">649,570</td>
<td align="right">26.4%</td>
<td align="right">235.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">84,202</td>
<td align="right">11.2%</td>
<td align="right">275,492</td>
<td align="right">11.2%</td>
<td align="right">227.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">20,395</td>
<td align="right">2.7%</td>
<td align="right">62,149</td>
<td align="right">2.5%</td>
<td align="right">204.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">3,445</td>
<td align="right">0.5%</td>
<td align="right">10,835</td>
<td align="right">0.4%</td>
<td align="right">214.5%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">-81.8%</td>
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
<td align="right">115,769</td>
<td align="right">4.7%</td>
<td align="right">287.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">101,713</td>
<td align="right">13.6%</td>
<td align="right">162,946</td>
<td align="right">6.6%</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">141,170</td>
<td align="right">18.8%</td>
<td align="right">612,503</td>
<td align="right">24.9%</td>
<td align="right">333.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">284,667</td>
<td align="right">38.0%</td>
<td align="right">967,029</td>
<td align="right">39.3%</td>
<td align="right">239.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">118,685</td>
<td align="right">15.8%</td>
<td align="right">432,041</td>
<td align="right">17.6%</td>
<td align="right">264.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">32,887</td>
<td align="right">4.4%</td>
<td align="right">110,323</td>
<td align="right">4.5%</td>
<td align="right">235.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,715</td>
<td align="right">0.9%</td>
<td align="right">22,670</td>
<td align="right">0.9%</td>
<td align="right">237.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">972</td>
<td align="right">0.1%</td>
<td align="right">843</td>
<td align="right">0.0%</td>
<td align="right">-13.3%</td>
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
<td align="right">1,555,938</td>
<td align="right">81,576.5%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">14,623</td>
<td align="right">4,245,576</td>
<td align="right">28,933.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">58,486</td>
<td align="right">8,677,397</td>
<td align="right">14,736.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">948,152</td>
<td align="right">27,326,506</td>
<td align="right">2,782.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">3,001,182</td>
<td align="right">66,534,292</td>
<td align="right">2,116.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">845,638</td>
<td align="right">6,362,166</td>
<td align="right">652.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">8,826,666</td>
<td align="right">59,858,849</td>
<td align="right">578.2%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">986,313</td>
<td align="right">6,680,213</td>
<td align="right">577.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">5,659,231</td>
<td align="right">30,577,055</td>
<td align="right">440.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">177,450,184</td>
<td align="right">845,671,451</td>
<td align="right">376.6%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">1,481,042</td>
<td align="right">6,469,993</td>
<td align="right">336.9%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">87,231,615</td>
<td align="right">340,311,342</td>
<td align="right">290.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">7,945,978</td>
<td align="right">27,703,315</td>
<td align="right">248.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,515,015,898</td>
<td align="right">4,662,886,978</td>
<td align="right">207.8%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">4,238</td>
<td align="right">12,470</td>
<td align="right">194.2%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">40,536</td>
<td align="right">118,304</td>
<td align="right">191.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">25,500,613</td>
<td align="right">70,157,453</td>
<td align="right">175.1%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,408,292</td>
<td align="right">6,615,984</td>
<td align="right">174.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">11,472,542</td>
<td align="right">30,570,956</td>
<td align="right">166.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,279,315</td>
<td align="right">3,351,340</td>
<td align="right">162.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">18,965,247</td>
<td align="right">43,743,000</td>
<td align="right">130.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">18,589,364</td>
<td align="right">42,034,046</td>
<td align="right">126.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">35,428,401</td>
<td align="right">77,887,251</td>
<td align="right">119.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">36,148,340</td>
<td align="right">78,352,707</td>
<td align="right">116.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">22,107,112</td>
<td align="right">47,626,712</td>
<td align="right">115.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">67,415,454</td>
<td align="right">141,965,240</td>
<td align="right">110.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">25,426,600</td>
<td align="right">52,768,181</td>
<td align="right">107.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,337,357</td>
<td align="right">4,767,917</td>
<td align="right">104.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">45,051,334</td>
<td align="right">91,659,312</td>
<td align="right">103.5%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,527,364</td>
<td align="right">740</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">25,780,332</td>
<td align="right">51,125,264</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">105,072,067</td>
<td align="right">207,364,736</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">27,564,892</td>
<td align="right">53,061,683</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">25,876,243</td>
<td align="right">2,881,976</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">265,486,634</td>
<td align="right">499,610,515</td>
<td align="right">88.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">209,553,679</td>
<td align="right">385,519,008</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">28,597,806</td>
<td align="right">5,628,300</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">28,597,806</td>
<td align="right">5,632,822</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,095</td>
<td align="right">65,965,987</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,095</td>
<td align="right">65,965,987</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">74,573,143</td>
<td align="right">15,391,828</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">154,024,883</td>
<td align="right">274,304,479</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">805,246,008</td>
<td align="right">1,416,167,516</td>
<td align="right">75.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">36,373,675</td>
<td align="right">63,936,091</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">359,897,106</td>
<td align="right">630,825,183</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">35,396,538</td>
<td align="right">9,414,683</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">35,396,538</td>
<td align="right">9,414,683</td>
<td align="right">-73.4%</td>
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
<td align="right">213,375,329</td>
<td align="right">72.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">78,663,041</td>
<td align="right">134,369,229</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">38,540,302</td>
<td align="right">65,817,552</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">807</td>
<td align="right">256</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">220,183</td>
<td align="right">368,136</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">79,477,134</td>
<td align="right">26,694,950</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">844,652,787</td>
<td align="right">1,398,339,012</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">81,728,184</td>
<td align="right">134,985,212</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">80,631,024</td>
<td align="right">28,404,182</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,702,551</td>
<td align="right">14,844,486</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,142,934</td>
<td align="right">3,081,570</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">193,378,908</td>
<td align="right">312,269,734</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,368,599,396</td>
<td align="right">10,263,335,798</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">890,566,449</td>
<td align="right">354,819,120</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,209,333,067</td>
<td align="right">11,506,507,117</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,088,379,802</td>
<td align="right">458,813,517</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">43,170,728</td>
<td align="right">68,091,715</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">43,169,045</td>
<td align="right">68,083,046</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">256,827,589</td>
<td align="right">110,515,699</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">526,519,230</td>
<td align="right">826,424,661</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">527,284,156</td>
<td align="right">827,034,697</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">155,706,153</td>
<td align="right">242,834,754</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,225,640,177</td>
<td align="right">9,704,030,618</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,894,848,533</td>
<td align="right">8,840,660,542</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">66,446,669</td>
<td align="right">33,390,832</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">178,239,216</td>
<td align="right">263,949,681</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">816,218,271</td>
<td align="right">1,188,928,627</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">654,259,812</td>
<td align="right">952,901,613</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,171,082</td>
<td align="right">2,297,322</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,385,354,478</td>
<td align="right">13,557,928,318</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">279,283,708</td>
<td align="right">402,850,716</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">93,835,688</td>
<td align="right">133,878,316</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">345,591,829</td>
<td align="right">489,925,250</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">422,589,766</td>
<td align="right">591,237,965</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">68,143,705</td>
<td align="right">95,267,275</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">118,208,399</td>
<td align="right">164,486,981</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,848,393</td>
<td align="right">115,046,027</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">117,059,835</td>
<td align="right">161,415,187</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,935,007,647</td>
<td align="right">3,976,511,984</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,041,100,167</td>
<td align="right">8,181,361,454</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">222,122,524</td>
<td align="right">299,597,488</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,810,185,202</td>
<td align="right">3,748,014,190</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">472,285,871</td>
<td align="right">629,530,915</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,740,067,338</td>
<td align="right">3,651,637,457</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">476,064,431</td>
<td align="right">634,116,940</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">37,610,145</td>
<td align="right">49,997,380</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">37,610,145</td>
<td align="right">49,997,380</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,702,661,285</td>
<td align="right">3,586,465,446</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">63,421,860</td>
<td align="right">83,730,797</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">713,236,554</td>
<td align="right">936,402,535</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,072,315,973</td>
<td align="right">2,714,740,932</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">43,351,650</td>
<td align="right">56,786,916</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">25,842,491</td>
<td align="right">33,803,201</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">148,412,611</td>
<td align="right">192,066,097</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,872,054,343</td>
<td align="right">2,400,187,599</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">583,456,057</td>
<td align="right">746,658,355</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,384,030,683</td>
<td align="right">1,763,874,941</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">63,150,164</td>
<td align="right">45,845,979</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,865,368,706</td>
<td align="right">3,649,359,705</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">270,350,090</td>
<td align="right">344,088,289</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,381,118,420</td>
<td align="right">1,752,985,284</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">598,183,721</td>
<td align="right">758,577,312</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,236,587</td>
<td align="right">1,559,560</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,297,712,034</td>
<td align="right">1,636,544,525</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,928,800,468</td>
<td align="right">2,408,802,248</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,707,401,466</td>
<td align="right">2,129,932,536</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,432,933,979</td>
<td align="right">3,000,523,629</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,902,591,248</td>
<td align="right">3,547,864,926</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">124,551,953</td>
<td align="right">151,744,491</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">9,110,831</td>
<td align="right">11,074,635</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">70,904,723</td>
<td align="right">56,271,305</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">576,889,483</td>
<td align="right">692,415,717</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">824,652,119</td>
<td align="right">989,688,223</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">300,524,405</td>
<td align="right">360,527,158</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">308,442,256</td>
<td align="right">366,308,941</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,231,302,816</td>
<td align="right">1,461,767,131</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">729,625,404</td>
<td align="right">862,461,696</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">818,310,853</td>
<td align="right">959,714,855</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">420,515,546</td>
<td align="right">492,101,811</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,001,224,456</td>
<td align="right">1,169,223,591</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">511,587,429</td>
<td align="right">596,806,540</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">17,266</td>
<td align="right">14,526</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">829,755,612</td>
<td align="right">957,168,415</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">75,081,718</td>
<td align="right">63,581,792</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">695,686</td>
<td align="right">801,598</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">312,473,657</td>
<td align="right">359,804,703</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,533,658,850</td>
<td align="right">4,057,526,120</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">19,624,258,507</td>
<td align="right">22,452,715,619</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">775,440,944</td>
<td align="right">881,977,989</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">735,318,366</td>
<td align="right">833,898,616</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,829,478,362</td>
<td align="right">2,074,653,622</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">16,212,017,638</td>
<td align="right">18,356,288,964</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">508,055,120</td>
<td align="right">574,926,982</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">302,671,747</td>
<td align="right">341,886,880</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">107,550,867</td>
<td align="right">121,122,836</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">107,550,867</td>
<td align="right">121,122,836</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">10,186,604,036</td>
<td align="right">11,471,127,148</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,448,404,369</td>
<td align="right">5,007,446,045</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">314,903,128</td>
<td align="right">354,296,363</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">526,597,931</td>
<td align="right">591,141,311</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">433,844,041</td>
<td align="right">381,794,113</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,437,860,540</td>
<td align="right">1,610,218,047</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,318,416,759</td>
<td align="right">1,473,403,982</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">7,353,887</td>
<td align="right">8,205,594</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">768,270</td>
<td align="right">856,646</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">768,354</td>
<td align="right">856,732</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,010,258,697</td>
<td align="right">3,561,188,349</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">916,634,180</td>
<td align="right">1,019,150,188</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">688,267,585</td>
<td align="right">764,232,717</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">296,777,285</td>
<td align="right">328,180,050</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,087,041,953</td>
<td align="right">1,200,462,267</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">124,553,926</td>
<td align="right">137,459,783</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,067,389,356</td>
<td align="right">2,275,763,683</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,020,649,001</td>
<td align="right">2,216,921,012</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">774,824,336</td>
<td align="right">847,202,222</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,167,989,806</td>
<td align="right">1,276,806,667</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">462</td>
<td align="right">504</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">72,836,895</td>
<td align="right">78,930,549</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">622,492,195</td>
<td align="right">674,335,098</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">29,982,444</td>
<td align="right">32,454,499</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,044,622,822</td>
<td align="right">8,701,710,055</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">8,412,013,591</td>
<td align="right">7,731,009,565</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,358,700,333</td>
<td align="right">1,463,763,419</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">72,822,346</td>
<td align="right">78,159,386</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">671,731,799</td>
<td align="right">623,263,686</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,791,692,557</td>
<td align="right">4,023,141,561</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">101,691,756</td>
<td align="right">95,556,495</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,041,297,478</td>
<td align="right">3,223,925,695</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">857,678</td>
<td align="right">908,153</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">501,464,439</td>
<td align="right">472,026,936</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">98,818,398</td>
<td align="right">93,145,480</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,176,021,411</td>
<td align="right">2,051,421,201</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,981,833,455</td>
<td align="right">5,265,940,214</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">617,619,122</td>
<td align="right">583,294,209</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,929,819,076</td>
<td align="right">2,034,960,403</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">54,227,907</td>
<td align="right">57,128,398</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">956,553,512</td>
<td align="right">1,006,116,952</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">871,090,135</td>
<td align="right">830,244,460</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">438,999,830</td>
<td align="right">459,577,716</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">270,210,582</td>
<td align="right">281,863,049</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">489,006,599</td>
<td align="right">468,878,477</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,865,961,321</td>
<td align="right">1,791,584,949</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,740,568,687</td>
<td align="right">2,845,192,378</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,010,291,715</td>
<td align="right">1,046,679,154</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,368,130,062</td>
<td align="right">2,451,144,682</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">208,355,034</td>
<td align="right">215,222,419</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">541,556,222</td>
<td align="right">557,648,044</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">51,980,959</td>
<td align="right">53,485,523</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">399,950,250</td>
<td align="right">411,431,492</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,349,203,170</td>
<td align="right">1,387,892,812</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">159,219,038</td>
<td align="right">163,784,693</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">52,509,145</td>
<td align="right">53,995,208</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">43,050,050</td>
<td align="right">41,835,141</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,188,053,706</td>
<td align="right">4,299,388,316</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,720,858,057</td>
<td align="right">1,764,411,150</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">181,942,370</td>
<td align="right">185,211,726</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,733,322</td>
<td align="right">61,748,908</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">116,135,314</td>
<td align="right">114,302,423</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,067,063,058</td>
<td align="right">1,082,532,827</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">390,243,734</td>
<td align="right">385,592,157</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">81,844,246</td>
<td align="right">82,776,912</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,865,444,182</td>
<td align="right">1,845,661,993</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">4,219,689</td>
<td align="right">4,261,559</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">4,220,711</td>
<td align="right">4,262,203</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,898,093,704</td>
<td align="right">1,881,674,238</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,629,813,307</td>
<td align="right">1,615,995,292</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">2,925,410,628</td>
<td align="right">2,942,320,612</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">98,767,754</td>
<td align="right">99,307,287</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">124,942,360</td>
<td align="right">125,457,952</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">25,111,829</td>
<td align="right">25,211,226</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">556,160,168</td>
<td align="right">554,265,195</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">590,723,168</td>
<td align="right">588,809,991</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">591,741,728</td>
<td align="right">589,843,371</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,849,967,368</td>
<td align="right">1,846,590,084</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,545,341</td>
<td align="right">24,503,688</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">562,440</td>
<td align="right">561,600</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">112,473,853</td>
<td align="right">112,434,383</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
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
<td align="right">2,186,054</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">84,285</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_UPDATE</td>
<td align="right"></td>
<td align="right">16,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_LOCALS</td>
<td align="right"></td>
<td align="right">2,058</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FROM_DICT_OR_DEREF</td>
<td align="right"></td>
<td align="right">1,029</td>
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
<td align="right">8,119</td>
<td align="right">275.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">52,007</td>
<td align="right">138,019</td>
<td align="right">165.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">23,746</td>
<td align="right">45,564</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">126</td>
<td align="right">206</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">29,926</td>
<td align="right">32,538</td>
<td align="right">8.7%</td>
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
<td align="right">391</td>
<td align="right">58.3%</td>
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
<td align="right">391</td>
<td align="right">58.3%</td>
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
