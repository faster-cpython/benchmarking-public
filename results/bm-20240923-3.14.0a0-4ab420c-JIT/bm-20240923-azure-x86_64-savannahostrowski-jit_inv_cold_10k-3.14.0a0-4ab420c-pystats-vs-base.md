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
<td align="right">2,370,866</td>
<td align="right">1,589,182,068</td>
<td align="right">66,929.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">77,590,421</td>
<td align="right">928,683,855</td>
<td align="right">1,096.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">187,865,586</td>
<td align="right">1,525,255,421</td>
<td align="right">711.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,416,942</td>
<td align="right">535,548,573</td>
<td align="right">473.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">169,661,882</td>
<td align="right">964,851,685</td>
<td align="right">468.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,873,322</td>
<td align="right">972,209,913</td>
<td align="right">434.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">220,869,727</td>
<td align="right">1,151,740,861</td>
<td align="right">421.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">233,409,273</td>
<td align="right">1,166,648,090</td>
<td align="right">399.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">266,414,410</td>
<td align="right">1,127,911,709</td>
<td align="right">323.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,258,769</td>
<td align="right">440,262,630</td>
<td align="right">322.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">354,602,023</td>
<td align="right">1,284,256,635</td>
<td align="right">262.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">357,901,370</td>
<td align="right">1,220,422,643</td>
<td align="right">241.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">168,664</td>
<td align="right">539,008</td>
<td align="right">219.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">533,379,930</td>
<td align="right">1,637,174,176</td>
<td align="right">206.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">155,432,361</td>
<td align="right">467,146,226</td>
<td align="right">200.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,894,015</td>
<td align="right">6,667,342</td>
<td align="right">130.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">750,357,009</td>
<td align="right">1,727,623,653</td>
<td align="right">130.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">770,137,958</td>
<td align="right">1,715,194,569</td>
<td align="right">122.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">395,394,062</td>
<td align="right">862,336,867</td>
<td align="right">118.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,374,696,744</td>
<td align="right">8,442,550,213</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">477,715,646</td>
<td align="right">921,080,279</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,662,020,579</td>
<td align="right">3,177,351,360</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">435,804,695</td>
<td align="right">806,571,783</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">617,613,985</td>
<td align="right">1,078,927,857</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">565,318,372</td>
<td align="right">972,915,813</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,519,623</td>
<td align="right">12,603,683</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">524,431</td>
<td align="right">834,693</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">83,904,713</td>
<td align="right">125,779,516</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,621,508,292</td>
<td align="right">6,916,617,914</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,313,870</td>
<td align="right">53,974,562</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,652,025,240</td>
<td align="right">5,091,328,507</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,748,833,395</td>
<td align="right">5,183,736,021</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">43,622,922</td>
<td align="right">59,980,667</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,794,211,492</td>
<td align="right">21,652,761,081</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,448,892</td>
<td align="right">64,793,891</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">68,076,928</td>
<td align="right">92,770,800</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">107,983,655</td>
<td align="right">144,595,929</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,793,539</td>
<td align="right">3,734,771</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">54,350,039</td>
<td align="right">72,167,998</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">53,161,417</td>
<td align="right">69,993,319</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">36,930,594</td>
<td align="right">44,634,913</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">27,680,632</td>
<td align="right">32,428,537</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">53,732,222</td>
<td align="right">62,294,160</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">260,816,195</td>
<td align="right">301,805,847</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">534,957,636</td>
<td align="right">609,711,082</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">197,984,251</td>
<td align="right">221,979,083</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,539,818</td>
<td align="right">158,419,688</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">190,266,155</td>
<td align="right">212,676,076</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">58,580</td>
<td align="right">65,180</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">53,362,005</td>
<td align="right">59,240,649</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">315,152,163</td>
<td align="right">347,629,160</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,315,417,329</td>
<td align="right">1,443,893,546</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">340,958,561</td>
<td align="right">374,162,739</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,467,214,993</td>
<td align="right">2,249,861,626</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">741,696,588</td>
<td align="right">806,864,673</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,616,088</td>
<td align="right">9,308,975</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,783,561</td>
<td align="right">20,286,389</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">470,967,967</td>
<td align="right">507,678,199</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,607,342,370</td>
<td align="right">2,805,519,466</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,419,483</td>
<td align="right">9,630,049</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,569,747</td>
<td align="right">61,820,617</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">45,967,503</td>
<td align="right">49,358,553</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">105,347,100</td>
<td align="right">112,948,887</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,255,344</td>
<td align="right">10,447,668</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">33,582,590</td>
<td align="right">35,986,286</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">367,230,659</td>
<td align="right">392,669,668</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">964,509,931</td>
<td align="right">1,028,519,559</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">239,113,280</td>
<td align="right">254,484,037</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,952,204,382</td>
<td align="right">2,077,200,593</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">119,888,122</td>
<td align="right">127,524,984</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">137,110,490</td>
<td align="right">145,140,613</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">138,923,820</td>
<td align="right">146,802,024</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,226,769,381</td>
<td align="right">2,352,306,382</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">331,065,023</td>
<td align="right">349,477,517</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">197,268,706</td>
<td align="right">208,183,961</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">150,190,988</td>
<td align="right">158,338,467</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">51,810,581</td>
<td align="right">54,601,965</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">29,951,382</td>
<td align="right">31,529,939</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">278,408,646</td>
<td align="right">292,809,579</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">367,939,052</td>
<td align="right">386,327,920</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">91,865,234</td>
<td align="right">96,136,041</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,567,596,014</td>
<td align="right">4,776,780,476</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,327,530</td>
<td align="right">4,514,929</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">410,108,909</td>
<td align="right">427,790,031</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,035,636,209</td>
<td align="right">1,079,305,723</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,208,431</td>
<td align="right">9,587,319</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,561,839</td>
<td align="right">418,729,612</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">158,443,389</td>
<td align="right">164,635,136</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">252,588,116</td>
<td align="right">262,440,117</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">822,966,741</td>
<td align="right">854,645,616</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">552,520</td>
<td align="right">573,580</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">15,628,408</td>
<td align="right">16,216,820</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">452,940,581</td>
<td align="right">469,895,934</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,700,733</td>
<td align="right">74,105,376</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">103,734,499</td>
<td align="right">107,083,644</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">142,419,229</td>
<td align="right">146,874,355</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,585,656</td>
<td align="right">3,476,399</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">8,406,213</td>
<td align="right">8,653,365</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">590,113,168</td>
<td align="right">606,888,479</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,611,243,859</td>
<td align="right">2,681,705,701</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">134,761,818</td>
<td align="right">138,339,138</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">338,852,098</td>
<td align="right">347,736,784</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">61,489,489</td>
<td align="right">63,101,692</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">61,259,969</td>
<td align="right">59,741,830</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">309,002,831</td>
<td align="right">316,335,790</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">93,339,882</td>
<td align="right">95,489,221</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">190,507,736</td>
<td align="right">194,842,937</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">76,207,663</td>
<td align="right">77,850,084</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">44,064,468</td>
<td align="right">44,988,146</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,860,207,032</td>
<td align="right">2,919,609,420</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">15,800</td>
<td align="right">16,120</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">280,538,888</td>
<td align="right">285,999,059</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">70,932,379</td>
<td align="right">72,312,917</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">186,991,097</td>
<td align="right">190,325,017</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,654,101,816</td>
<td align="right">1,683,474,880</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">198,141,890</td>
<td align="right">201,607,708</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">70,445,334</td>
<td align="right">71,651,869</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">32,346,260</td>
<td align="right">31,828,554</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">56,464,096</td>
<td align="right">57,352,628</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">21,858,217</td>
<td align="right">22,189,177</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">33,168,987</td>
<td align="right">33,654,220</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">43,810,459</td>
<td align="right">44,412,091</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">29,249</td>
<td align="right">29,649</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,715,909,336</td>
<td align="right">3,755,251,796</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">128,116,120</td>
<td align="right">129,466,880</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">119,860,269</td>
<td align="right">121,030,358</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,710,295</td>
<td align="right">3,744,636</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">62,071,616</td>
<td align="right">62,641,889</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">65,292,565</td>
<td align="right">65,781,143</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">154,428,209</td>
<td align="right">153,281,844</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,053,083,002</td>
<td align="right">1,060,860,925</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">763,336</td>
<td align="right">768,755</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">720,727</td>
<td align="right">715,709</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">197,306,974</td>
<td align="right">198,385,309</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,996,182</td>
<td align="right">11,051,138</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,835,826,834</td>
<td align="right">1,844,189,533</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">49,900,357</td>
<td align="right">50,104,317</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,166,144</td>
<td align="right">269,138,471</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">88,064,410</td>
<td align="right">87,754,703</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">90,850,895</td>
<td align="right">91,110,330</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">102,333,374</td>
<td align="right">102,088,314</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">99,690,977</td>
<td align="right">99,919,184</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">107,104,102</td>
<td align="right">107,248,064</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,373,621</td>
<td align="right">21,394,569</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,067,712</td>
<td align="right">21,080,987</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,381,962</td>
<td align="right">21,395,428</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,136,956</td>
<td align="right">83,085,174</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,372,717,882</td>
<td align="right">1,371,902,049</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,299,418</td>
<td align="right">198,404,586</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,029,143</td>
<td align="right">35,043,128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">14,953,078</td>
<td align="right">14,958,375</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,035,146</td>
<td align="right">9,037,348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">147,002,215</td>
<td align="right">146,970,305</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,262,462,336</td>
<td align="right">2,262,924,430</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">262,501,370</td>
<td align="right">262,461,290</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">268,309</td>
<td align="right">268,333</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,010,782</td>
<td align="right">225,026,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">239,380</td>
<td align="right">239,396</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,166</td>
<td align="right">15,167</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,262,371</td>
<td align="right">1,262,434</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,829,279</td>
<td align="right">5,829,529</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">66,758</td>
<td align="right">66,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,460,207</td>
<td align="right">82,460,801</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">10,868,298</td>
<td align="right">10,868,355</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,356,431</td>
<td align="right">20,356,510</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,398,744</td>
<td align="right">173,398,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,103,937</td>
<td align="right">402,103,991</td>
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
<td align="right">10,337,403</td>
<td align="right">10,337,403</td>
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
<td align="right">3,464,928</td>
<td align="right">3,464,928</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">642,472</td>
<td align="right">642,472</td>
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
<td align="left">DICT_UPDATE</td>
<td align="right">27,726</td>
<td align="right">27,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,656</td>
<td align="right">21,656</td>
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
<td align="right">100</td>
<td align="right">100</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">366,072,520</td>
<td align="right">3.7%</td>
<td align="right">391,484,875</td>
<td align="right">4.0%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,421,027,588</td>
<td align="right">96.0%</td>
<td align="right">9,360,782,366</td>
<td align="right">95.7%</td>
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
<td align="right">29,480,870</td>
<td align="right">0.3%</td>
<td align="right">29,650,210</td>
<td align="right">0.3%</td>
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
<td align="left">Failure</td>
<td align="right">1,115,633</td>
<td align="right">65.1%</td>
<td align="right">1,142,269</td>
<td align="right">65.5%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">598,586</td>
<td align="right">34.9%</td>
<td align="right">601,804</td>
<td align="right">34.5%</td>
<td align="right">0.5%</td>
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
<td align="right">19,957</td>
<td align="right">1.8%</td>
<td align="right">23,618</td>
<td align="right">2.1%</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">49,156</td>
<td align="right">4.4%</td>
<td align="right">56,733</td>
<td align="right">5.0%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,470</td>
<td align="right">0.8%</td>
<td align="right">9,387</td>
<td align="right">0.8%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,625</td>
<td align="right">7.3%</td>
<td align="right">90,079</td>
<td align="right">7.9%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">6,744</td>
<td align="right">0.6%</td>
<td align="right">7,405</td>
<td align="right">0.6%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">30,997</td>
<td align="right">2.8%</td>
<td align="right">34,012</td>
<td align="right">3.0%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,742</td>
<td align="right">0.9%</td>
<td align="right">10,222</td>
<td align="right">0.9%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,227</td>
<td align="right">1.3%</td>
<td align="right">14,748</td>
<td align="right">1.3%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">8,548</td>
<td align="right">0.8%</td>
<td align="right">8,809</td>
<td align="right">0.8%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,723</td>
<td align="right">0.2%</td>
<td align="right">2,803</td>
<td align="right">0.2%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,829</td>
<td align="right">0.3%</td>
<td align="right">2,890</td>
<td align="right">0.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,824</td>
<td align="right">1.0%</td>
<td align="right">11,043</td>
<td align="right">1.0%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,580</td>
<td align="right">0.2%</td>
<td align="right">2,622</td>
<td align="right">0.2%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">47,042</td>
<td align="right">4.2%</td>
<td align="right">47,514</td>
<td align="right">4.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">31,706</td>
<td align="right">2.8%</td>
<td align="right">31,924</td>
<td align="right">2.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">837</td>
<td align="right">0.1%</td>
<td align="right">834</td>
<td align="right">0.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,613</td>
<td align="right">0.5%</td>
<td align="right">5,620</td>
<td align="right">0.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,612</td>
<td align="right">70.1%</td>
<td align="right">781,605</td>
<td align="right">68.4%</td>
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
<td align="right">181,873,322</td>
<td align="right">100.0%</td>
<td align="right">972,209,913</td>
<td align="right">100.0%</td>
<td align="right">434.6%</td>
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
<td align="right">477,444,797</td>
<td align="right">7.1%</td>
<td align="right">920,701,850</td>
<td align="right">12.9%</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,792,535</td>
<td align="right">0.1%</td>
<td align="right">4,809,816</td>
<td align="right">0.1%</td>
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
<td align="right">6,215,635,770</td>
<td align="right">92.8%</td>
<td align="right">6,200,453,513</td>
<td align="right">87.0%</td>
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
<td align="right">179,433</td>
<td align="right">49.7%</td>
<td align="right">287,008</td>
<td align="right">61.2%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,377</td>
<td align="right">50.3%</td>
<td align="right">181,702</td>
<td align="right">38.8%</td>
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
<td align="left">other</td>
<td align="right">65,375</td>
<td align="right">36.4%</td>
<td align="right">174,843</td>
<td align="right">60.9%</td>
<td align="right">167.4%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">980</td>
<td align="right">0.5%</td>
<td align="right">1,040</td>
<td align="right">0.4%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">59,225</td>
<td align="right">33.0%</td>
<td align="right">56,805</td>
<td align="right">19.8%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">880</td>
<td align="right">0.5%</td>
<td align="right">860</td>
<td align="right">0.3%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,469</td>
<td align="right">12.0%</td>
<td align="right">21,695</td>
<td align="right">7.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">26,640</td>
<td align="right">14.8%</td>
<td align="right">26,900</td>
<td align="right">9.4%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">125</td>
<td align="right">0.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">2.4%</td>
<td align="right">4,300</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,060</td>
<td align="right">0.0%</td>
<td align="right">37,409</td>
<td align="right">0.0%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">152,335,896</td>
<td align="right">1.1%</td>
<td align="right">158,264,757</td>
<td align="right">1.2%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,548,676,657</td>
<td align="right">98.9%</td>
<td align="right">13,524,467,618</td>
<td align="right">98.8%</td>
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
<td align="right">716,858</td>
<td align="right">0.0%</td>
<td align="right">716,910</td>
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
<td align="right">3,452,140</td>
<td align="right">100.0%</td>
<td align="right">3,570,535</td>
<td align="right">100.0%</td>
<td align="right">3.4%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">435,240</td>
<td align="right">86.7%</td>
<td align="right">786,105</td>
<td align="right">92.2%</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,413</td>
<td align="right">7.3%</td>
<td align="right">36,415</td>
<td align="right">4.3%</td>
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
<td align="right">104,051,536</td>
<td align="right">1.8%</td>
<td align="right">439,967,240</td>
<td align="right">7.1%</td>
<td align="right">322.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,035,915</td>
<td align="right">0.0%</td>
<td align="right">1,106,351</td>
<td align="right">0.0%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,749,095,667</td>
<td align="right">98.2%</td>
<td align="right">5,733,653,024</td>
<td align="right">92.9%</td>
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
<td align="right">151,913</td>
<td align="right">67.1%</td>
<td align="right">240,025</td>
<td align="right">76.0%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">74,533</td>
<td align="right">32.9%</td>
<td align="right">75,886</td>
<td align="right">24.0%</td>
<td align="right">1.8%</td>
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
<td align="right">12,236</td>
<td align="right">8.1%</td>
<td align="right">93,235</td>
<td align="right">38.8%</td>
<td align="right">662.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">530</td>
<td align="right">0.3%</td>
<td align="right">490</td>
<td align="right">0.2%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">38,695</td>
<td align="right">25.5%</td>
<td align="right">41,553</td>
<td align="right">17.3%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">29,734</td>
<td align="right">19.6%</td>
<td align="right">31,843</td>
<td align="right">13.3%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,480</td>
<td align="right">9.5%</td>
<td align="right">15,288</td>
<td align="right">6.4%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,441</td>
<td align="right">11.5%</td>
<td align="right">18,312</td>
<td align="right">7.6%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,548</td>
<td align="right">1.0%</td>
<td align="right">1,615</td>
<td align="right">0.7%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">1,000</td>
<td align="right">0.4%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,640</td>
<td align="right">2.4%</td>
<td align="right">3,520</td>
<td align="right">1.5%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,249</td>
<td align="right">12.7%</td>
<td align="right">19,629</td>
<td align="right">8.2%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.0%</td>
<td align="right">10,820</td>
<td align="right">4.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,720</td>
<td align="right">1.8%</td>
<td align="right">2,720</td>
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
<td align="right">36,845,599</td>
<td align="right">1.5%</td>
<td align="right">44,544,900</td>
<td align="right">1.8%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,490,354,764</td>
<td align="right">98.4%</td>
<td align="right">2,486,671,760</td>
<td align="right">98.1%</td>
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
<td align="right">2,544,260</td>
<td align="right">0.1%</td>
<td align="right">2,545,570</td>
<td align="right">0.1%</td>
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
<td align="right">71,816</td>
<td align="right">54.0%</td>
<td align="right">76,835</td>
<td align="right">55.7%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,099</td>
<td align="right">46.0%</td>
<td align="right">61,120</td>
<td align="right">44.3%</td>
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
<td align="left">str</td>
<td align="right">14,522</td>
<td align="right">20.2%</td>
<td align="right">17,802</td>
<td align="right">23.2%</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,590</td>
<td align="right">20.3%</td>
<td align="right">15,414</td>
<td align="right">20.1%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,375</td>
<td align="right">38.1%</td>
<td align="right">28,332</td>
<td align="right">36.9%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,329</td>
<td align="right">21.3%</td>
<td align="right">15,287</td>
<td align="right">19.9%</td>
<td align="right">-0.3%</td>
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
<td align="right">77,438,447</td>
<td align="right">12.5%</td>
<td align="right">928,312,147</td>
<td align="right">40.1%</td>
<td align="right">1,098.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,764,877</td>
<td align="right">1.1%</td>
<td align="right">41,630,713</td>
<td align="right">1.8%</td>
<td align="right">515.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">533,217,599</td>
<td align="right">86.3%</td>
<td align="right">1,347,174,962</td>
<td align="right">58.1%</td>
<td align="right">152.7%</td>
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
<td align="right">176,321</td>
<td align="right">63.1%</td>
<td align="right">834,050</td>
<td align="right">72.1%</td>
<td align="right">373.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">102,976</td>
<td align="right">36.9%</td>
<td align="right">322,773</td>
<td align="right">27.9%</td>
<td align="right">213.4%</td>
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
<td align="left">zip</td>
<td align="right">7,602</td>
<td align="right">7.4%</td>
<td align="right">207,302</td>
<td align="right">64.2%</td>
<td align="right">2,626.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4,741</td>
<td align="right">4.6%</td>
<td align="right">10,700</td>
<td align="right">3.3%</td>
<td align="right">125.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">614</td>
<td align="right">0.6%</td>
<td align="right">1,277</td>
<td align="right">0.4%</td>
<td align="right">108.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,936</td>
<td align="right">4.8%</td>
<td align="right">8,076</td>
<td align="right">2.5%</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,063</td>
<td align="right">10.7%</td>
<td align="right">14,748</td>
<td align="right">4.6%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,379</td>
<td align="right">11.1%</td>
<td align="right">14,022</td>
<td align="right">4.3%</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,547</td>
<td align="right">2.5%</td>
<td align="right">2,887</td>
<td align="right">0.9%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,906</td>
<td align="right">35.8%</td>
<td align="right">40,601</td>
<td align="right">12.6%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,584</td>
<td align="right">3.5%</td>
<td align="right">3,484</td>
<td align="right">1.1%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,625</td>
<td align="right">6.4%</td>
<td align="right">6,677</td>
<td align="right">2.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,717</td>
<td align="right">6.5%</td>
<td align="right">6,737</td>
<td align="right">2.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,222</td>
<td align="right">5.1%</td>
<td align="right">5,222</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">740</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.3%</td>
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
<td align="right">320,527,488</td>
<td align="right">2.0%</td>
<td align="right">501,805,103</td>
<td align="right">3.0%</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,289,160</td>
<td align="right">0.0%</td>
<td align="right">1,908,460</td>
<td align="right">0.0%</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">468,812,167</td>
<td align="right">2.9%</td>
<td align="right">505,484,704</td>
<td align="right">3.0%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,596,155,105</td>
<td align="right">95.2%</td>
<td align="right">15,585,252,321</td>
<td align="right">93.9%</td>
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
<td align="right">7,708,318</td>
<td align="right">94.4%</td>
<td align="right">11,152,173</td>
<td align="right">95.9%</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">460,388</td>
<td align="right">5.6%</td>
<td align="right">473,664</td>
<td align="right">4.1%</td>
<td align="right">2.9%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">31,259</td>
<td align="right">6.8%</td>
<td align="right">37,756</td>
<td align="right">8.0%</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2,502</td>
<td align="right">0.5%</td>
<td align="right">2,682</td>
<td align="right">0.6%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">32,233</td>
<td align="right">7.0%</td>
<td align="right">33,214</td>
<td align="right">7.0%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">680</td>
<td align="right">0.1%</td>
<td align="right">700</td>
<td align="right">0.1%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">20,880</td>
<td align="right">4.5%</td>
<td align="right">21,483</td>
<td align="right">4.5%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,425</td>
<td align="right">1.2%</td>
<td align="right">5,545</td>
<td align="right">1.2%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,924</td>
<td align="right">0.6%</td>
<td align="right">2,984</td>
<td align="right">0.6%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">15,015</td>
<td align="right">3.3%</td>
<td align="right">15,292</td>
<td align="right">3.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,120</td>
<td align="right">0.2%</td>
<td align="right">1,140</td>
<td align="right">0.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">87,772</td>
<td align="right">19.1%</td>
<td align="right">89,274</td>
<td align="right">18.8%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">2,794</td>
<td align="right">0.6%</td>
<td align="right">2,754</td>
<td align="right">0.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">15,164</td>
<td align="right">3.3%</td>
<td align="right">15,345</td>
<td align="right">3.2%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">138,711</td>
<td align="right">30.1%</td>
<td align="right">140,365</td>
<td align="right">29.6%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">85,153</td>
<td align="right">18.5%</td>
<td align="right">85,840</td>
<td align="right">18.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">5,300</td>
<td align="right">1.2%</td>
<td align="right">5,300</td>
<td align="right">1.1%</td>
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
<td align="right">4,518,391,236</td>
<td align="right">99.5%</td>
<td align="right">6,084,553,079</td>
<td align="right">99.7%</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">388,282</td>
<td align="right">0.0%</td>
<td align="right">390,930</td>
<td align="right">0.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19,894,942</td>
<td align="right">0.4%</td>
<td align="right">19,894,998</td>
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
<td align="right">9,234</td>
<td align="right">0.0%</td>
<td align="right">9,234</td>
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
<td align="right">467,157</td>
<td align="right">100.0%</td>
<td align="right">467,220</td>
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
<td align="right">85,318,849</td>
<td align="right">100.0%</td>
<td align="right">86,108,884</td>
<td align="right">100.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,625</td>
<td align="right">0.0%</td>
<td align="right">7,626</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">30,643</td>
<td align="right">0.0%</td>
<td align="right">30,663</td>
<td align="right">0.0%</td>
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
<td align="right">173,334,013</td>
<td align="right">18.1%</td>
<td align="right">173,334,049</td>
<td align="right">18.1%</td>
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
<td align="right">786,232,623</td>
<td align="right">81.9%</td>
<td align="right">786,232,729</td>
<td align="right">81.9%</td>
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
<td align="right">59,734</td>
<td align="right">91.5%</td>
<td align="right">59,754</td>
<td align="right">91.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,557</td>
<td align="right">8.5%</td>
<td align="right">5,557</td>
<td align="right">8.5%</td>
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
<td align="left">list</td>
<td align="right">10,020</td>
<td align="right">16.8%</td>
<td align="right">10,040</td>
<td align="right">16.8%</td>
<td align="right">0.2%</td>
</tr>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45,780,232</td>
<td align="right">1.7%</td>
<td align="right">49,171,178</td>
<td align="right">1.9%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">121,962,372</td>
<td align="right">4.6%</td>
<td align="right">126,651,762</td>
<td align="right">4.8%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,473,010,689</td>
<td align="right">93.6%</td>
<td align="right">2,463,648,169</td>
<td align="right">93.3%</td>
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
<td align="right">2,401,545</td>
<td align="right">96.6%</td>
<td align="right">2,490,115</td>
<td align="right">96.7%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">83,990</td>
<td align="right">3.4%</td>
<td align="right">83,891</td>
<td align="right">3.3%</td>
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
<td align="left">not in dict</td>
<td align="right">16,965</td>
<td align="right">20.2%</td>
<td align="right">15,445</td>
<td align="right">18.4%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,935</td>
<td align="right">5.9%</td>
<td align="right">5,215</td>
<td align="right">6.2%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">31,844</td>
<td align="right">37.9%</td>
<td align="right">33,064</td>
<td align="right">39.4%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">4,841</td>
<td align="right">5.8%</td>
<td align="right">5,021</td>
<td align="right">6.0%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">2,180</td>
<td align="right">2.6%</td>
<td align="right">2,100</td>
<td align="right">2.5%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">800</td>
<td align="right">1.0%</td>
<td align="right">780</td>
<td align="right">0.9%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,523</td>
<td align="right">10.1%</td>
<td align="right">8,363</td>
<td align="right">10.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,225</td>
<td align="right">3.8%</td>
<td align="right">3,185</td>
<td align="right">3.8%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,813</td>
<td align="right">11.7%</td>
<td align="right">9,854</td>
<td align="right">11.7%</td>
<td align="right">0.4%</td>
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
<td align="right">12,603,683</td>
<td align="right">100.0%</td>
<td align="right">67.6%</td>
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
<td align="right">93,336,893</td>
<td align="right">9.6%</td>
<td align="right">535,359,381</td>
<td align="right">37.9%</td>
<td align="right">473.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">876,557,430</td>
<td align="right">90.4%</td>
<td align="right">875,229,455</td>
<td align="right">62.0%</td>
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
<td align="right">66,724</td>
<td align="right">83.3%</td>
<td align="right">175,862</td>
<td align="right">92.9%</td>
<td align="right">163.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,365</td>
<td align="right">16.7%</td>
<td align="right">13,370</td>
<td align="right">7.1%</td>
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
<td align="right">620</td>
<td align="right">0.9%</td>
<td align="right">104,760</td>
<td align="right">59.6%</td>
<td align="right">16,796.8%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">6,721</td>
<td align="right">10.1%</td>
<td align="right">11,019</td>
<td align="right">6.3%</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,480</td>
<td align="right">2.2%</td>
<td align="right">1,700</td>
<td align="right">1.0%</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,520</td>
<td align="right">2.3%</td>
<td align="right">1,580</td>
<td align="right">0.9%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">14,160</td>
<td align="right">21.2%</td>
<td align="right">14,560</td>
<td align="right">8.3%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">42,223</td>
<td align="right">63.3%</td>
<td align="right">42,243</td>
<td align="right">24.0%</td>
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
<td align="right">24,679,023</td>
<td align="right">0.4%</td>
<td align="right">35,831,211</td>
<td align="right">0.6%</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">154,021,066</td>
<td align="right">2.6%</td>
<td align="right">152,799,031</td>
<td align="right">2.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,760,907,579</td>
<td align="right">97.0%</td>
<td align="right">5,761,129,822</td>
<td align="right">96.8%</td>
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
<td align="right">209,028</td>
<td align="right">24.1%</td>
<td align="right">284,638</td>
<td align="right">24.7%</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">658,892</td>
<td align="right">75.9%</td>
<td align="right">869,188</td>
<td align="right">75.3%</td>
<td align="right">31.9%</td>
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
<td align="left">number</td>
<td align="right">37,263</td>
<td align="right">17.8%</td>
<td align="right">106,374</td>
<td align="right">37.4%</td>
<td align="right">185.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,998</td>
<td align="right">2.9%</td>
<td align="right">6,590</td>
<td align="right">2.3%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">8,149</td>
<td align="right">3.9%</td>
<td align="right">7,403</td>
<td align="right">2.6%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">82,834</td>
<td align="right">39.6%</td>
<td align="right">87,961</td>
<td align="right">30.9%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,245</td>
<td align="right">7.8%</td>
<td align="right">16,945</td>
<td align="right">6.0%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">14,910</td>
<td align="right">7.1%</td>
<td align="right">15,252</td>
<td align="right">5.4%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">21,687</td>
<td align="right">10.4%</td>
<td align="right">22,170</td>
<td align="right">7.8%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">19,170</td>
<td align="right">9.2%</td>
<td align="right">19,171</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,749</td>
<td align="right">0.8%</td>
<td align="right">1,749</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">683</td>
<td align="right">0.3%</td>
<td align="right">683</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">433,280</td>
<td align="right">0.0%</td>
<td align="right">2,197,060</td>
<td align="right">0.1%</td>
<td align="right">407.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,058,218,754</td>
<td align="right">100.0%</td>
<td align="right">2,056,190,286</td>
<td align="right">99.9%</td>
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
<td align="right">198,889</td>
<td align="right">0.0%</td>
<td align="right">198,896</td>
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
<td align="right">46,747</td>
<td align="right">96.4%</td>
<td align="right">80,155</td>
<td align="right">97.8%</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,764</td>
<td align="right">3.6%</td>
<td align="right">1,765</td>
<td align="right">2.2%</td>
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
<td align="right">1,117</td>
<td align="right">63.3%</td>
<td align="right">1,118</td>
<td align="right">63.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">21.5%</td>
<td align="right">380</td>
<td align="right">21.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">267</td>
<td align="right">15.1%</td>
<td align="right">267</td>
<td align="right">15.1%</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,213,238,505</td>
<td align="right">2.4%</td>
<td align="right">5,153,351,157</td>
<td align="right">4.1%</td>
<td align="right">132.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">665,618,131</td>
<td align="right">0.7%</td>
<td align="right">906,516,073</td>
<td align="right">0.7%</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">30,829,470,490</td>
<td align="right">33.8%</td>
<td align="right">41,968,915,403</td>
<td align="right">33.4%</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">57,499,552,695</td>
<td align="right">63.0%</td>
<td align="right">77,736,755,878</td>
<td align="right">61.8%</td>
<td align="right">35.2%</td>
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
<td align="right">77,438,447</td>
<td align="right">3.5%</td>
<td align="right">928,312,147</td>
<td align="right">18.0%</td>
<td align="right">1,098.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,336,893</td>
<td align="right">4.2%</td>
<td align="right">535,359,381</td>
<td align="right">10.4%</td>
<td align="right">473.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">181,873,322</td>
<td align="right">8.2%</td>
<td align="right">972,209,913</td>
<td align="right">18.9%</td>
<td align="right">434.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,051,536</td>
<td align="right">4.7%</td>
<td align="right">439,967,240</td>
<td align="right">8.5%</td>
<td align="right">322.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">477,444,797</td>
<td align="right">21.6%</td>
<td align="right">920,701,850</td>
<td align="right">17.9%</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">468,812,167</td>
<td align="right">21.2%</td>
<td align="right">505,484,704</td>
<td align="right">9.8%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">45,780,232</td>
<td align="right">2.1%</td>
<td align="right">49,171,178</td>
<td align="right">1.0%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">366,072,520</td>
<td align="right">16.6%</td>
<td align="right">391,484,875</td>
<td align="right">7.6%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">154,021,066</td>
<td align="right">7.0%</td>
<td align="right">152,799,031</td>
<td align="right">3.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,334,013</td>
<td align="right">7.9%</td>
<td align="right">173,334,049</td>
<td align="right">3.4%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">82,653,026</td>
<td align="right">12.4%</td>
<td align="right">144,320,890</td>
<td align="right">15.9%</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">38,083,191</td>
<td align="right">5.7%</td>
<td align="right">64,622,563</td>
<td align="right">7.1%</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,606,245</td>
<td align="right">6.1%</td>
<td align="right">68,396,940</td>
<td align="right">7.5%</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">120,159,815</td>
<td align="right">18.0%</td>
<td align="right">178,847,618</td>
<td align="right">19.7%</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">23,841,542</td>
<td align="right">3.6%</td>
<td align="right">25,751,140</td>
<td align="right">2.8%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,097,302</td>
<td align="right">12.2%</td>
<td align="right">84,020,937</td>
<td align="right">9.3%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">98,116,224</td>
<td align="right">14.7%</td>
<td align="right">100,895,963</td>
<td align="right">11.1%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,839</td>
<td align="right">4.1%</td>
<td align="right">27,497,001</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,177,240</td>
<td align="right">3.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,521,463</td>
<td align="right">2.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20,798,568</td>
<td align="right">2.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20,765,054</td>
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
<td align="left">Frame objects created</td>
<td align="right">84,741,862</td>
<td align="right">1.0%</td>
<td align="right">84,592,739</td>
<td align="right">1.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,176,128,932</td>
<td align="right">73.2%</td>
<td align="right">6,169,022,373</td>
<td align="right">73.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,691,354,031</td>
<td align="right">79.3%</td>
<td align="right">6,685,280,428</td>
<td align="right">79.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">852,265,276</td>
<td align="right">10.1%</td>
<td align="right">851,680,191</td>
<td align="right">10.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,409,565,739</td>
<td align="right">16.7%</td>
<td align="right">1,410,503,418</td>
<td align="right">16.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,414,013,380</td>
<td align="right">16.7%</td>
<td align="right">1,414,951,059</td>
<td align="right">16.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">333,916,589</td>
<td align="right">4.0%</td>
<td align="right">333,801,331</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,266,278,656</td>
<td align="right">26.8%</td>
<td align="right">2,266,631,250</td>
<td align="right">26.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,266,278,656</td>
<td align="right">26.8%</td>
<td align="right">2,266,631,250</td>
<td align="right">26.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,609,349</td>
<td align="right">3.9%</td>
<td align="right">331,637,653</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,097,892</td>
<td align="right">0.4%</td>
<td align="right">31,098,649</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,206</td>
<td align="right">2.1%</td>
<td align="right">175,480,343</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,417,972</td>
<td align="right">0.1%</td>
<td align="right">4,417,972</td>
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
<td align="left">Interpreter increfs</td>
<td align="right">41,569,660,634</td>
<td align="right">41,569,660,634 / 0 !!</td>
<td align="right">52,691,587,422</td>
<td align="right">52,691,587,422 / 0 !!</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">56,859,434,672</td>
<td align="right">56,859,434,672 / 0 !!</td>
<td align="right">69,989,506,642</td>
<td align="right">69,989,506,642 / 0 !!</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">105,692,194,503</td>
<td align="right">105,692,194,503 / 0 !!</td>
<td align="right">89,777,384,572</td>
<td align="right">89,777,384,572 / 0 !!</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">98,136,306,988</td>
<td align="right">98,136,306,988 / 0 !!</td>
<td align="right">84,177,570,496</td>
<td align="right">84,177,570,496 / 0 !!</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,405,911,928</td>
<td align="right"></td>
<td align="right">2,368,957,531</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,697,669</td>
<td align="right">0.4%</td>
<td align="right">104,944,725</td>
<td align="right">0.4%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">57,485,773</td>
<td align="right"></td>
<td align="right">57,954,412</td>
<td align="right"></td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">63,222,524</td>
<td align="right"></td>
<td align="right">62,849,955</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,767,380,496</td>
<td align="right">47.1%</td>
<td align="right">11,821,798,603</td>
<td align="right">47.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,769,253,458</td>
<td align="right"></td>
<td align="right">11,823,670,762</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">21,032,349</td>
<td align="right">0.1%</td>
<td align="right">21,128,235</td>
<td align="right">0.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,667,242,469</td>
<td align="right"></td>
<td align="right">3,677,358,176</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">235,707,825</td>
<td align="right"></td>
<td align="right">235,952,507</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">13,074,214,175</td>
<td align="right">52.4%</td>
<td align="right">13,066,587,975</td>
<td align="right">52.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">13,198,944,193</td>
<td align="right">52.9%</td>
<td align="right">13,192,660,935</td>
<td align="right">52.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,965,810,475</td>
<td align="right"></td>
<td align="right">13,960,729,140</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">117,304,484</td>
<td align="right"></td>
<td align="right">117,278,719</td>
<td align="right"></td>
<td align="right">-0.0%</td>
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
<td align="right">454,554</td>
<td align="right">112,655,150</td>
<td align="right">19,128,848,982</td>
<td align="right">453,772</td>
<td align="right">112,324,686</td>
<td align="right">19,148,089,991</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">15,360</td>
<td align="right">10,756,040</td>
<td align="right">6,959,114,584</td>
<td align="right">15,360</td>
<td align="right">10,756,040</td>
<td align="right">6,958,596,828</td>
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
<td align="right">34,784</td>
<td align="right">1.2%</td>
<td align="right">3,296.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">179,915</td>
<td align="right">19.8%</td>
<td align="right">1,955,838</td>
<td align="right">66.6%</td>
<td align="right">987.1%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">580</td>
<td align="right">0.1%</td>
<td align="right">5,680</td>
<td align="right">0.2%</td>
<td align="right">879.3%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,661</td>
<td align="right">0.4%</td>
<td align="right">21,854</td>
<td align="right">0.7%</td>
<td align="right">496.9%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">12,285</td>
<td align="right">1.4%</td>
<td align="right">65,539</td>
<td align="right">2.2%</td>
<td align="right">433.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">907,347</td>
<td align="right"></td>
<td align="right">2,936,003</td>
<td align="right"></td>
<td align="right">223.6%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,757</td>
<td align="right">0.2%</td>
<td align="right">3,125</td>
<td align="right">0.1%</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">662,470</td>
<td align="right">73.0%</td>
<td align="right">1,130,881</td>
<td align="right">38.5%</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">725,675</td>
<td align="right">80.0%</td>
<td align="right">977,040</td>
<td align="right">33.3%</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">9,482,582,109</td>
<td align="right"></td>
<td align="right">7,014,218,432</td>
<td align="right"></td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">9,462</td>
<td align="right">5.3%</td>
<td align="right">7,700</td>
<td align="right">0.4%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">306,323,671,354</td>
<td align="right">3,230.4%</td>
<td align="right">252,036,226,818</td>
<td align="right">3,593.2%</td>
<td align="right">-17.7%</td>
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
<td align="right">168,129</td>
<td align="right">93.4%</td>
<td align="right">1,916,549</td>
<td align="right">98.0%</td>
<td align="right">1,039.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">179,915</td>
<td align="right"></td>
<td align="right">1,955,838</td>
<td align="right"></td>
<td align="right">987.1%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,551</td>
<td align="right">1.4%</td>
<td align="right">2,461</td>
<td align="right">0.1%</td>
<td align="right">-3.5%</td>
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
<td align="right">3,791</td>
<td align="right">2.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">23,227</td>
<td align="right">12.9%</td>
<td align="right">121,575</td>
<td align="right">6.2%</td>
<td align="right">423.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20,642</td>
<td align="right">11.5%</td>
<td align="right">266,002</td>
<td align="right">13.6%</td>
<td align="right">1,188.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">48,421</td>
<td align="right">26.9%</td>
<td align="right">671,913</td>
<td align="right">34.4%</td>
<td align="right">1,287.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">41,455</td>
<td align="right">23.0%</td>
<td align="right">525,860</td>
<td align="right">26.9%</td>
<td align="right">1,168.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">23,997</td>
<td align="right">13.3%</td>
<td align="right">242,861</td>
<td align="right">12.4%</td>
<td align="right">912.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">14,882</td>
<td align="right">8.3%</td>
<td align="right">99,437</td>
<td align="right">5.1%</td>
<td align="right">568.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,880</td>
<td align="right">1.6%</td>
<td align="right">22,310</td>
<td align="right">1.1%</td>
<td align="right">674.7%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">5,880</td>
<td align="right">0.3%</td>
<td align="right">848.4%</td>
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
<td align="right">20,213</td>
<td align="right">11.2%</td>
<td align="right">80,159</td>
<td align="right">4.1%</td>
<td align="right">296.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,655</td>
<td align="right">9.3%</td>
<td align="right">202,321</td>
<td align="right">10.3%</td>
<td align="right">1,114.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">30,957</td>
<td align="right">17.2%</td>
<td align="right">290,420</td>
<td align="right">14.8%</td>
<td align="right">838.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">50,702</td>
<td align="right">28.2%</td>
<td align="right">775,946</td>
<td align="right">39.7%</td>
<td align="right">1,430.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">30,144</td>
<td align="right">16.8%</td>
<td align="right">355,516</td>
<td align="right">18.2%</td>
<td align="right">1,079.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,658</td>
<td align="right">7.6%</td>
<td align="right">159,634</td>
<td align="right">8.2%</td>
<td align="right">1,068.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,800</td>
<td align="right">2.7%</td>
<td align="right">41,757</td>
<td align="right">2.1%</td>
<td align="right">769.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">980</td>
<td align="right">0.5%</td>
<td align="right">10,796</td>
<td align="right">0.6%</td>
<td align="right">1,001.6%</td>
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
<td align="left">_IMPORT_FROM</td>
<td align="right">370,690</td>
<td align="right">1,180,352</td>
<td align="right">218.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">785,163</td>
<td align="right">1,576,920</td>
<td align="right">100.8%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">376,020</td>
<td align="right">10,482</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">420</td>
<td align="right">20</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">718</td>
<td align="right">-91.2%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,949,540</td>
<td align="right">324,897</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">5,715,760</td>
<td align="right">819,674</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">4,785,180</td>
<td align="right">765,940</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">962,382,979</td>
<td align="right">171,277,902</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">2,125,264</td>
<td align="right">617,139</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,344,806,656</td>
<td align="right">412,914,151</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">5,473,310</td>
<td align="right">1,698,863</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,320,420,551</td>
<td align="right">470,380,228</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,478,658,397</td>
<td align="right">543,810,798</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">558,549,512</td>
<td align="right">221,620,563</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">692,746,591</td>
<td align="right">286,597,455</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">699,169,512</td>
<td align="right">291,047,645</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">782,482,224</td>
<td align="right">340,462,224</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">845,133,130</td>
<td align="right">377,859,185</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,715,219,716</td>
<td align="right">785,416,569</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">1,606,400</td>
<td align="right">805,790</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,757,458,699</td>
<td align="right">1,942,918,708</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">10,164</td>
<td align="right">14,964</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">682,148,169</td>
<td align="right">369,225,971</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,670,503,470</td>
<td align="right">3,083,187,815</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">34,034,356</td>
<td align="right">18,721,509</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,035,524,967</td>
<td align="right">1,695,992,038</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">32,600,136</td>
<td align="right">18,270,280</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">48,892,966</td>
<td align="right">27,746,370</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,071,692,922</td>
<td align="right">610,554,074</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,268,515,306</td>
<td align="right">3,003,262,572</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">954,051,813</td>
<td align="right">555,782,465</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,357,654,417</td>
<td align="right">1,378,898,310</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,893,293,018</td>
<td align="right">2,901,138,535</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,622,978,723</td>
<td align="right">968,475,759</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,229,602,069</td>
<td align="right">1,367,593,430</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,815,651,047</td>
<td align="right">2,346,585,257</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">979,685,909</td>
<td align="right">608,591,197</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,320,867,204</td>
<td align="right">1,457,880,527</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,602,855,317</td>
<td align="right">1,649,645,881</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,081,067,841</td>
<td align="right">1,320,486,549</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,376,294,753</td>
<td align="right">1,583,165,901</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,392,382,821</td>
<td align="right">1,597,791,022</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,223,580</td>
<td align="right">37,336,031</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,227,820</td>
<td align="right">37,339,511</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,555,579,192</td>
<td align="right">2,488,549,284</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,256,822,865</td>
<td align="right">7,317,550,472</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">869,791,799</td>
<td align="right">620,643,113</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,946,654,493</td>
<td align="right">2,839,037,519</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,735,953,445</td>
<td align="right">10,618,346,990</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">8,487,658,386</td>
<td align="right">6,131,457,019</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,617,132,696</td>
<td align="right">1,172,313,046</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">24,470,253</td>
<td align="right">17,792,264</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,230,920</td>
<td align="right">1,629,760</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">24,662</td>
<td align="right">18,062</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">9,482,582,109</td>
<td align="right">7,014,218,432</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">916,222</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,299,404,441</td>
<td align="right">1,762,162,840</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,446,082,932</td>
<td align="right">3,427,466,088</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,423,066,827</td>
<td align="right">1,100,970,378</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">25,666,105,678</td>
<td align="right">19,949,496,691</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">21,364,195,712</td>
<td align="right">16,667,855,689</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">10,365,728,586</td>
<td align="right">8,253,787,332</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,951,320</td>
<td align="right">5,543,578</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">84,031,504</td>
<td align="right">67,670,726</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,270,728,550</td>
<td align="right">6,694,590,777</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">308,478,204</td>
<td align="right">250,515,144</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,895,611,411</td>
<td align="right">2,355,259,560</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">6,552,961,529</td>
<td align="right">5,362,416,164</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,626,364</td>
<td align="right">38,435,162</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">94,617,668</td>
<td align="right">78,056,565</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">99,675,346</td>
<td align="right">82,842,992</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,404,663</td>
<td align="right">81,234,585</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">469,339,576</td>
<td align="right">394,131,334</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">114,733,252</td>
<td align="right">96,883,515</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">388,310,517</td>
<td align="right">328,257,826</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">111,498,879</td>
<td align="right">95,451,144</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">217,556,377</td>
<td align="right">186,584,482</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,994,680</td>
<td align="right">1,734,505</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">205,468,655</td>
<td align="right">181,776,017</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,217,088,082</td>
<td align="right">1,081,501,193</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">728,265,379</td>
<td align="right">648,633,670</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">305,878,895</td>
<td align="right">274,084,644</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">659,067,208</td>
<td align="right">594,567,571</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">112,699,124</td>
<td align="right">101,825,102</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">943,391,233</td>
<td align="right">852,582,019</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">566,899,980</td>
<td align="right">512,606,700</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">452,125,376</td>
<td align="right">409,639,080</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">950,323,849</td>
<td align="right">861,238,146</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">60,894,431</td>
<td align="right">55,568,323</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">117,898,619</td>
<td align="right">128,152,648</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">100,794,777</td>
<td align="right">92,582,741</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">209,466,413</td>
<td align="right">192,535,773</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">245,515,080</td>
<td align="right">225,886,948</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">153,763,357</td>
<td align="right">141,518,693</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,639,522</td>
<td align="right">2,433,024</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,374,504,010</td>
<td align="right">5,888,971,254</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">204,656,514</td>
<td align="right">189,433,637</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,501,547,298</td>
<td align="right">2,315,902,466</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">530,392,988</td>
<td align="right">491,300,624</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">53,738,545</td>
<td align="right">49,950,130</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">36,581,519</td>
<td align="right">34,115,082</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,429,276,721</td>
<td align="right">2,265,618,990</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">132,815,956</td>
<td align="right">124,061,846</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">165,992,778</td>
<td align="right">155,080,079</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,168,159,360</td>
<td align="right">2,030,401,573</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">68,678,234</td>
<td align="right">64,376,044</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">39,077,597</td>
<td align="right">36,636,603</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">579,434,425</td>
<td align="right">543,799,474</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,163,764,509</td>
<td align="right">2,976,944,924</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">56,752,445</td>
<td align="right">53,434,288</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">74,422,018</td>
<td align="right">70,117,385</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">281,312,617</td>
<td align="right">265,510,788</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">167,207,416</td>
<td align="right">158,262,104</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,583,273,971</td>
<td align="right">3,391,855,795</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">3,528,378,786</td>
<td align="right">3,341,712,883</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">155,403,663</td>
<td align="right">147,253,940</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,413,855,677</td>
<td align="right">2,288,605,639</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">112,931,950</td>
<td align="right">107,137,484</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,069,005,486</td>
<td align="right">1,015,229,331</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">342,183,316</td>
<td align="right">325,373,606</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,738,379,184</td>
<td align="right">1,653,641,389</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">42,810,938</td>
<td align="right">40,766,981</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,742,740,534</td>
<td align="right">3,564,119,892</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,154,506</td>
<td align="right">9,670,957</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,245,493,651</td>
<td align="right">7,857,700,836</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">6,776,783</td>
<td align="right">7,090,981</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">170,871,951</td>
<td align="right">163,113,036</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,439,939</td>
<td align="right">577,232,677</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">488,920</td>
<td align="right">467,860</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">8,203,400,413</td>
<td align="right">7,851,134,177</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">134,547,542</td>
<td align="right">128,867,887</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">885,029,678</td>
<td align="right">847,935,344</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,790,130,201</td>
<td align="right">1,715,596,762</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">43,496,358</td>
<td align="right">41,717,719</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,781,064,401</td>
<td align="right">1,709,093,809</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">11,163,220</td>
<td align="right">10,712,379</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">893,294,649</td>
<td align="right">857,452,775</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">12,309,560</td>
<td align="right">11,828,711</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,872,364</td>
<td align="right">8,526,130</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,049,474,090</td>
<td align="right">1,008,845,221</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">89,133,912</td>
<td align="right">85,693,820</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,117,825,540</td>
<td align="right">2,037,764,465</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">123,045,993</td>
<td align="right">118,451,296</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,119,353,615</td>
<td align="right">1,081,316,518</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">916,937,421</td>
<td align="right">885,962,063</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,907,540</td>
<td align="right">149,823,480</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">353,783,902</td>
<td align="right">342,362,825</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">49,748,269</td>
<td align="right">48,143,971</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">49,748,269</td>
<td align="right">48,143,971</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">707,587,865</td>
<td align="right">684,881,866</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">702,539,905</td>
<td align="right">680,005,006</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,653,403,811</td>
<td align="right">1,601,259,697</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">359,309,240</td>
<td align="right">348,274,438</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,084,363,610</td>
<td align="right">1,116,452,298</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">25,309,960</td>
<td align="right">24,577,744</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">238,368,688</td>
<td align="right">231,677,166</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,951,741,602</td>
<td align="right">1,900,450,231</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">841,769,467</td>
<td align="right">820,598,098</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">891,970,925</td>
<td align="right">870,891,104</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">236,451,885</td>
<td align="right">230,912,214</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">770,513,912</td>
<td align="right">752,690,599</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">32,264,883</td>
<td align="right">31,527,979</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">739,851,897</td>
<td align="right">723,602,646</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">721,638,130</td>
<td align="right">705,907,090</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">246,943,520</td>
<td align="right">241,581,608</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">786,177,680</td>
<td align="right">769,163,377</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">787,535,440</td>
<td align="right">770,531,817</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">160,080,355</td>
<td align="right">156,767,367</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,064,489,990</td>
<td align="right">1,042,592,269</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,845,603,190</td>
<td align="right">3,769,873,408</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">394,322,927</td>
<td align="right">386,809,382</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">987,573,922</td>
<td align="right">968,944,945</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">290,921,991</td>
<td align="right">296,355,644</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">39,144,273</td>
<td align="right">38,436,853</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">351,212,771</td>
<td align="right">344,946,577</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,419,439,862</td>
<td align="right">1,394,656,497</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">41,164,553</td>
<td align="right">40,459,833</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">11,445,280</td>
<td align="right">11,257,980</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">158,953,808</td>
<td align="right">156,713,762</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">72,855,500</td>
<td align="right">72,008,600</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">476,476,042</td>
<td align="right">471,105,183</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">44,190,530</td>
<td align="right">43,709,016</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">44,190,530</td>
<td align="right">43,709,016</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,700,434,869</td>
<td align="right">1,682,228,565</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,759,754</td>
<td align="right">1,323,366,558</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,307,156</td>
<td align="right">1,295,512</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,467,317</td>
<td align="right">6,523,394</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,331,450</td>
<td align="right">67,747,080</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,587,180</td>
<td align="right">5,541,300</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,817,233,767</td>
<td align="right">1,802,727,462</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">125,369,740</td>
<td align="right">124,449,287</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,526,086,199</td>
<td align="right">1,514,993,058</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,316,115</td>
<td align="right">9,382,522</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">366,309,250</td>
<td align="right">364,159,735</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">167,943,749</td>
<td align="right">166,961,580</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">107,918,713</td>
<td align="right">107,348,347</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">229,355,424</td>
<td align="right">228,188,524</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,628,481,468</td>
<td align="right">3,611,191,916</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">394,788,642</td>
<td align="right">393,342,743</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,259,202</td>
<td align="right">4,243,854</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">205,061,660</td>
<td align="right">204,446,638</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">533,026,306</td>
<td align="right">531,699,085</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,102,262</td>
<td align="right">517,126,432</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,438,782</td>
<td align="right">32,381,886</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,143,971,480</td>
<td align="right">1,142,452,840</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,288,268</td>
<td align="right">97,172,611</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,861,820</td>
<td align="right">48,818,440</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,861,820</td>
<td align="right">48,818,440</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,240,168</td>
<td align="right">97,161,834</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,008,284</td>
<td align="right">81,056,047</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">580,625,560</td>
<td align="right">580,377,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">62,993,920</td>
<td align="right">62,980,560</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,567,700</td>
<td align="right">32,562,419</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,232,020</td>
<td align="right">350,195,120</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">962,920</td>
<td align="right">963,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">2,849,145</td>
<td align="right">2,848,983</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,840</td>
<td align="right">4,739,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,842,060</td>
<td align="right">1,842,060</td>
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
<td align="left">_MAKE_WARM</td>
<td align="right"></td>
<td align="right">9,369,477,992</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,175</td>
<td align="right">94,543</td>
<td align="right">114.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">60</td>
<td align="right">120</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20,125</td>
<td align="right">39,111</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,020</td>
<td align="right">1,593</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,440</td>
<td align="right">49,596</td>
<td align="right">44.0%</td>
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
<td align="right">1,172</td>
<td align="right">2.1%</td>
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
<td align="right">1,172</td>
<td align="right">2.1%</td>
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
<td align="right">1,941</td>
<td align="right">1,941</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-09-23
