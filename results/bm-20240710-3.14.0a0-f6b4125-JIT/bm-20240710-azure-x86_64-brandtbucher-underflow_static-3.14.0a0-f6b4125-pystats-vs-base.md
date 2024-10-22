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
<td align="left">UNARY_NOT</td>
<td align="right">8,358,550</td>
<td align="right">37,507,266</td>
<td align="right">348.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,872,615</td>
<td align="right">7,607,046</td>
<td align="right">96.4%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">81,682,702</td>
<td align="right">6,736,145</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">135,755,200</td>
<td align="right">14,086,380</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">142,537,682</td>
<td align="right">20,742,142</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,714,481</td>
<td align="right">10,953,461</td>
<td align="right">-84.7%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">4,628,776</td>
<td align="right">8,224,621</td>
<td align="right">77.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,412,492</td>
<td align="right">1,067,634</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">118,780,220</td>
<td align="right">37,713,139</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68,002,114</td>
<td align="right">24,519,602</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">283,352,534</td>
<td align="right">103,235,096</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,101,400</td>
<td align="right">18,890,727</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,461,660</td>
<td align="right">3,046,580</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,582,629</td>
<td align="right">42,095,692</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">49,187,665</td>
<td align="right">22,059,363</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">79,283,548</td>
<td align="right">38,623,111</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,366</td>
<td align="right">93,297,713</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">215,047,544</td>
<td align="right">107,531,196</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">222,923</td>
<td align="right">116,299</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">385,013,946</td>
<td align="right">202,354,654</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">59,116,065</td>
<td align="right">31,987,226</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,016,892,277</td>
<td align="right">567,266,013</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,805,903</td>
<td align="right">40,739,014</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,590,087</td>
<td align="right">72,430,416</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">404,545,476</td>
<td align="right">237,401,121</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">114,694,877</td>
<td align="right">70,890,477</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">328,729,310</td>
<td align="right">204,737,554</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">295,222,477</td>
<td align="right">186,305,651</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">386,364,030</td>
<td align="right">248,717,035</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">298,241,806</td>
<td align="right">205,924,814</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,142,292</td>
<td align="right">63,000,581</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">386,009,618</td>
<td align="right">269,767,412</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">76,347,881</td>
<td align="right">53,777,929</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,420</td>
<td align="right">123,992</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">231,218,889</td>
<td align="right">166,927,596</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">804,771,453</td>
<td align="right">583,139,088</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,247,616</td>
<td align="right">45,951,140</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,664,462,997</td>
<td align="right">4,193,001,759</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,106,035,501</td>
<td align="right">3,071,519,470</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">21,174,969</td>
<td align="right">15,925,798</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,451,722</td>
<td align="right">62,150,410</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">100,342,278</td>
<td align="right">75,953,978</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">194,481,632</td>
<td align="right">148,288,911</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,388,245</td>
<td align="right">7,945,099</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,818,989,954</td>
<td align="right">2,192,255,310</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">942,147,086</td>
<td align="right">733,675,746</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">87,792,986</td>
<td align="right">69,589,243</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">146,473,449</td>
<td align="right">116,841,998</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,411,777,045</td>
<td align="right">1,128,597,241</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">108,591,602</td>
<td align="right">87,659,575</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,099,697,354</td>
<td align="right">3,333,671,341</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">409,202,823</td>
<td align="right">337,579,900</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">59,677,580</td>
<td align="right">49,307,879</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,525,675,761</td>
<td align="right">2,925,333,460</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">162,506,822</td>
<td align="right">135,325,215</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">173,188,558</td>
<td align="right">145,345,869</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">828,363,919</td>
<td align="right">696,590,943</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,579,509,283</td>
<td align="right">18,220,021,668</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">677,179,773</td>
<td align="right">576,032,081</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">453,787,946</td>
<td align="right">388,161,234</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,763,230</td>
<td align="right">57,300,065</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,399,936,718</td>
<td align="right">2,059,852,865</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">739,587,422</td>
<td align="right">638,031,606</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">66,953,725</td>
<td align="right">57,765,286</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">485,800</td>
<td align="right">419,440</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,221,923,193</td>
<td align="right">3,649,799,027</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">378,216,903</td>
<td align="right">328,000,236</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,450,562,324</td>
<td align="right">2,134,040,080</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">140,536,667</td>
<td align="right">122,774,484</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,221,174,548</td>
<td align="right">5,435,424,938</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,871,851,588</td>
<td align="right">1,635,463,580</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,255,223,860</td>
<td align="right">1,108,588,623</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,379,823,543</td>
<td align="right">3,872,444,722</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">30,785,605</td>
<td align="right">27,307,192</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">23,966,877</td>
<td align="right">21,387,861</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">42,434,945</td>
<td align="right">37,986,895</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">901,629,671</td>
<td align="right">808,210,941</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">639,895,536</td>
<td align="right">574,822,689</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,489,402,211</td>
<td align="right">4,932,224,457</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">773,915,403</td>
<td align="right">696,392,844</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,375,144</td>
<td align="right">83,510,326</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">349,280,523</td>
<td align="right">316,458,874</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">366,810,260</td>
<td align="right">332,681,708</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,297,302,371</td>
<td align="right">2,991,487,990</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">195,648,345</td>
<td align="right">177,728,813</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,880,197</td>
<td align="right">74,546,993</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">332,026,689</td>
<td align="right">303,206,003</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">909,373,301</td>
<td align="right">835,315,400</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">318,041,383</td>
<td align="right">292,648,714</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,110,607,013</td>
<td align="right">1,026,938,602</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">431,566,985</td>
<td align="right">400,580,481</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,845,653</td>
<td align="right">374,785,386</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,994,269,931</td>
<td align="right">5,584,638,401</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">679,740,809</td>
<td align="right">634,947,028</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,819,246</td>
<td align="right">38,172,998</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">219,489</td>
<td align="right">206,214</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">666,631,926</td>
<td align="right">627,329,696</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,915,383</td>
<td align="right">141,196,063</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">276,486,241</td>
<td align="right">290,661,254</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,131,545,121</td>
<td align="right">1,076,468,877</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">791,277,318</td>
<td align="right">754,092,312</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">211,083,186</td>
<td align="right">201,269,766</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">56,528,959</td>
<td align="right">54,004,354</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,553,537</td>
<td align="right">45,457,526</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,563,356,578</td>
<td align="right">1,496,237,370</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">198,428,791</td>
<td align="right">191,042,906</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">137,994,522</td>
<td align="right">132,964,749</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">272,715,059</td>
<td align="right">262,932,697</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">199,228,298</td>
<td align="right">192,201,003</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">20,334,125</td>
<td align="right">19,665,030</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,911,493</td>
<td align="right">142,114,583</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,569,294</td>
<td align="right">153,419,226</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">557,054,138</td>
<td align="right">540,332,560</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,370,892,334</td>
<td align="right">1,333,244,522</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,808,501</td>
<td align="right">32,672,101</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,850,499</td>
<td align="right">52,406,871</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,297,607</td>
<td align="right">211,181,020</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">421,589,822</td>
<td align="right">412,922,380</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,290,129,106</td>
<td align="right">1,272,274,604</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">166,873,760</td>
<td align="right">164,605,940</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">35,530,526</td>
<td align="right">35,998,179</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,165,100</td>
<td align="right">90,981,140</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">486,458,349</td>
<td align="right">480,826,801</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,024,183</td>
<td align="right">397,948,877</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,373,815</td>
<td align="right">2,350,009</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,165,245</td>
<td align="right">230,363,900</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">205,922,589</td>
<td align="right">204,344,183</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,955</td>
<td align="right">1,859,987</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,176,102</td>
<td align="right">82,650,261</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">481,314,538</td>
<td align="right">484,310,565</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">201,920,458</td>
<td align="right">200,705,334</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,474,390</td>
<td align="right">17,394,134</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,641,562</td>
<td align="right">224,627,238</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">54,270,983</td>
<td align="right">54,038,552</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,240</td>
<td align="right">3,450,500</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,877,595</td>
<td align="right">9,840,505</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,446,940</td>
<td align="right">94,223,180</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,644,410,487</td>
<td align="right">2,639,256,894</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">108,507,273</td>
<td align="right">108,674,367</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">228,048,131</td>
<td align="right">227,796,065</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">485,225,904</td>
<td align="right">484,732,522</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,194,944</td>
<td align="right">1,046,262,253</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,603,447,785</td>
<td align="right">1,602,314,592</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,640,637</td>
<td align="right">3,638,085</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,152,154</td>
<td align="right">21,138,955</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,886</td>
<td align="right">14,894</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,612,128</td>
<td align="right">46,593,216</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,339,421</td>
<td align="right">274,229,386</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,961,754</td>
<td align="right">10,958,938</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,657,736</td>
<td align="right">9,659,794</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,235,923</td>
<td align="right">9,237,554</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,843</td>
<td align="right">687,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,808,284</td>
<td align="right">1,808,181</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,693,837</td>
<td align="right">20,694,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,159,914</td>
<td align="right">21,160,589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,344,801</td>
<td align="right">20,345,244</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,950,764</td>
<td align="right">5,950,786</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,906,140</td>
<td align="right">555,906,513</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,338,342</td>
<td align="right">233,338,419</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,220,533</td>
<td align="right">786,220,571</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,319,342</td>
<td align="right">173,319,338</td>
<td align="right">-0.0%</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">12,102,480</td>
<td align="right">12,102,480</td>
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
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">719,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">657,740</td>
<td align="right">657,740</td>
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
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
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
<td align="right">29,500,920</td>
<td align="right">0.3%</td>
<td align="right">20,422,480</td>
<td align="right">0.2%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">436,983,590</td>
<td align="right">4.4%</td>
<td align="right">356,562,675</td>
<td align="right">3.7%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,428,334,896</td>
<td align="right">95.6%</td>
<td align="right">9,406,357,180</td>
<td align="right">96.3%</td>
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
<td align="left">Success</td>
<td align="right">597,632</td>
<td align="right">34.7%</td>
<td align="right">426,499</td>
<td align="right">29.6%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,122,521</td>
<td align="right">65.3%</td>
<td align="right">1,013,206</td>
<td align="right">70.4%</td>
<td align="right">-9.7%</td>
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
<td align="right">5,028</td>
<td align="right">0.4%</td>
<td align="right">2,520</td>
<td align="right">0.2%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">48,670</td>
<td align="right">4.3%</td>
<td align="right">31,653</td>
<td align="right">3.1%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,404</td>
<td align="right">7.3%</td>
<td align="right">54,312</td>
<td align="right">5.4%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,548</td>
<td align="right">0.5%</td>
<td align="right">3,956</td>
<td align="right">0.4%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">3,588</td>
<td align="right">0.4%</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,321</td>
<td align="right">4.3%</td>
<td align="right">40,203</td>
<td align="right">4.0%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,606</td>
<td align="right">69.6%</td>
<td align="right">733,911</td>
<td align="right">72.4%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,540</td>
<td align="right">0.3%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">13,633</td>
<td align="right">1.2%</td>
<td align="right">12,978</td>
<td align="right">1.3%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,276</td>
<td align="right">2.8%</td>
<td align="right">30,141</td>
<td align="right">3.0%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,884</td>
<td align="right">0.8%</td>
<td align="right">8,588</td>
<td align="right">0.8%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">0.9%</td>
<td align="right">10,280</td>
<td align="right">1.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,391</td>
<td align="right">2.9%</td>
<td align="right">31,947</td>
<td align="right">3.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,660</td>
<td align="right">0.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">22,630</td>
<td align="right">2.0%</td>
<td align="right">22,532</td>
<td align="right">2.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,607</td>
<td align="right">0.8%</td>
<td align="right">8,575</td>
<td align="right">0.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,915</td>
<td align="right">0.2%</td>
<td align="right">1,916</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,504</td>
<td align="right">0.9%</td>
<td align="right">10,506</td>
<td align="right">1.0%</td>
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
<td align="right">743,975,778</td>
<td align="right">10.8%</td>
<td align="right">642,393,532</td>
<td align="right">9.5%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,810,113</td>
<td align="right">0.1%</td>
<td align="right">4,754,690</td>
<td align="right">0.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,149,816,265</td>
<td align="right">89.2%</td>
<td align="right">6,135,656,596</td>
<td align="right">90.5%</td>
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
<td align="right">240,195</td>
<td align="right">57.0%</td>
<td align="right">212,218</td>
<td align="right">54.0%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,562</td>
<td align="right">43.0%</td>
<td align="right">180,546</td>
<td align="right">46.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">30,499</td>
<td align="right">12.7%</td>
<td align="right">20,778</td>
<td align="right">9.8%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">55,960</td>
<td align="right">23.3%</td>
<td align="right">41,200</td>
<td align="right">19.4%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">6.7%</td>
<td align="right">13,080</td>
<td align="right">6.2%</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">800</td>
<td align="right">0.4%</td>
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
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">128</td>
<td align="right">0.1%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">110,432</td>
<td align="right">46.0%</td>
<td align="right">110,172</td>
<td align="right">51.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,500</td>
<td align="right">8.1%</td>
<td align="right">19,500</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.2%</td>
<td align="right">5,340</td>
<td align="right">2.5%</td>
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
<td align="right">181,226,863</td>
<td align="right">1.3%</td>
<td align="right">150,826,339</td>
<td align="right">1.1%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">662,344,987</td>
<td align="right">4.6%</td>
<td align="right">632,024,605</td>
<td align="right">4.4%</td>
<td align="right">-4.6%</td>
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
<td align="right">28,400</td>
<td align="right">0.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,665,824,337</td>
<td align="right">95.3%</td>
<td align="right">13,671,517,888</td>
<td align="right">95.6%</td>
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
<td align="right">3,942,336</td>
<td align="right">96.0%</td>
<td align="right">3,368,978</td>
<td align="right">95.3%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">165,444</td>
<td align="right">4.0%</td>
<td align="right">165,278</td>
<td align="right">4.7%</td>
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
<td align="right">155,944</td>
<td align="right">94.3%</td>
<td align="right">155,778</td>
<td align="right">94.3%</td>
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
<td align="right">101,186,436</td>
<td align="right">1.6%</td>
<td align="right">76,730,738</td>
<td align="right">1.2%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,069,981</td>
<td align="right">0.0%</td>
<td align="right">990,976</td>
<td align="right">0.0%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,122,634,191</td>
<td align="right">98.4%</td>
<td align="right">6,106,115,672</td>
<td align="right">98.8%</td>
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
<td align="right">149,654</td>
<td align="right">66.3%</td>
<td align="right">139,562</td>
<td align="right">65.2%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">76,169</td>
<td align="right">33.7%</td>
<td align="right">74,654</td>
<td align="right">34.8%</td>
<td align="right">-2.0%</td>
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
<td align="left">float long</td>
<td align="right">14,367</td>
<td align="right">9.6%</td>
<td align="right">9,491</td>
<td align="right">6.8%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.4%</td>
<td align="right">480</td>
<td align="right">0.3%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">840</td>
<td align="right">0.6%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,580</td>
<td align="right">1.7%</td>
<td align="right">2,320</td>
<td align="right">1.7%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">42,493</td>
<td align="right">28.4%</td>
<td align="right">39,137</td>
<td align="right">28.0%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,704</td>
<td align="right">11.2%</td>
<td align="right">16,038</td>
<td align="right">11.5%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,425</td>
<td align="right">1.0%</td>
<td align="right">1,388</td>
<td align="right">1.0%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,180</td>
<td align="right">8.1%</td>
<td align="right">11,952</td>
<td align="right">8.6%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,000</td>
<td align="right">12.7%</td>
<td align="right">18,800</td>
<td align="right">13.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,065</td>
<td align="right">18.1%</td>
<td align="right">26,816</td>
<td align="right">19.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">10,680</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,620</td>
<td align="right">1.1%</td>
<td align="right">1,620</td>
<td align="right">1.2%</td>
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
<td align="right">2,546,240</td>
<td align="right">0.1%</td>
<td align="right">2,518,320</td>
<td align="right">0.1%</td>
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
<td align="right">208,293,964</td>
<td align="right">7.7%</td>
<td align="right">206,690,998</td>
<td align="right">7.7%</td>
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
<td align="right">2,489,650,137</td>
<td align="right">92.3%</td>
<td align="right">2,485,382,838</td>
<td align="right">92.3%</td>
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
<td align="right">113,745</td>
<td align="right">65.0%</td>
<td align="right">110,926</td>
<td align="right">64.7%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,120</td>
<td align="right">35.0%</td>
<td align="right">60,579</td>
<td align="right">35.3%</td>
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
<td align="left">tuple</td>
<td align="right">27,518</td>
<td align="right">24.2%</td>
<td align="right">25,486</td>
<td align="right">23.0%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,747</td>
<td align="right">13.8%</td>
<td align="right">15,320</td>
<td align="right">13.8%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">13,940</td>
<td align="right">12.3%</td>
<td align="right">13,580</td>
<td align="right">12.2%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">56,540</td>
<td align="right">49.7%</td>
<td align="right">56,540</td>
<td align="right">51.0%</td>
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
<td align="right">2,584,186</td>
<td align="right">0.3%</td>
<td align="right">190,747</td>
<td align="right">0.0%</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">547,137,231</td>
<td align="right">53.1%</td>
<td align="right">449,261,583</td>
<td align="right">48.1%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">483,605,440</td>
<td align="right">46.9%</td>
<td align="right">484,251,349</td>
<td align="right">51.9%</td>
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
<td align="right">96,491</td>
<td align="right">32.9%</td>
<td align="right">51,325</td>
<td align="right">20.5%</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">196,793</td>
<td align="right">67.1%</td>
<td align="right">198,638</td>
<td align="right">79.5%</td>
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
<td align="left">dict values</td>
<td align="right">4,220</td>
<td align="right">2.1%</td>
<td align="right">6,460</td>
<td align="right">3.3%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,060</td>
<td align="right">2.1%</td>
<td align="right">3,960</td>
<td align="right">2.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,288</td>
<td align="right">5.7%</td>
<td align="right">11,090</td>
<td align="right">5.6%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,100</td>
<td align="right">2.6%</td>
<td align="right">5,020</td>
<td align="right">2.5%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,274</td>
<td align="right">5.2%</td>
<td align="right">10,189</td>
<td align="right">5.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,952</td>
<td align="right">18.8%</td>
<td align="right">37,019</td>
<td align="right">18.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">619</td>
<td align="right">0.3%</td>
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,960</td>
<td align="right">53.3%</td>
<td align="right">104,960</td>
<td align="right">52.8%</td>
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
<td align="left">seq iter</td>
<td align="right">3,840</td>
<td align="right">2.0%</td>
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
<td align="right">420,251,267</td>
<td align="right">2.4%</td>
<td align="right">328,182,477</td>
<td align="right">1.9%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,521,346,778</td>
<td align="right">8.6%</td>
<td align="right">1,347,431,610</td>
<td align="right">7.8%</td>
<td align="right">-11.4%</td>
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
<td align="right">261,820</td>
<td align="right">0.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,088,154,419</td>
<td align="right">91.3%</td>
<td align="right">16,025,947,426</td>
<td align="right">92.2%</td>
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
<td align="right">8,539,474</td>
<td align="right">89.8%</td>
<td align="right">6,802,438</td>
<td align="right">88.5%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">972,028</td>
<td align="right">10.2%</td>
<td align="right">887,031</td>
<td align="right">11.5%</td>
<td align="right">-8.7%</td>
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
<td align="left">class attr simple</td>
<td align="right">156,169</td>
<td align="right">16.1%</td>
<td align="right">98,160</td>
<td align="right">11.1%</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,360</td>
<td align="right">1.5%</td>
<td align="right">17,760</td>
<td align="right">2.0%</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,752</td>
<td align="right">1.8%</td>
<td align="right">15,019</td>
<td align="right">1.7%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,578</td>
<td align="right">0.6%</td>
<td align="right">5,180</td>
<td align="right">0.6%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">263,165</td>
<td align="right">27.1%</td>
<td align="right">246,611</td>
<td align="right">27.8%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,643</td>
<td align="right">9.0%</td>
<td align="right">82,332</td>
<td align="right">9.3%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,880</td>
<td align="right">2.8%</td>
<td align="right">25,880</td>
<td align="right">2.9%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">164,790</td>
<td align="right">17.0%</td>
<td align="right">160,879</td>
<td align="right">18.1%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,340</td>
<td align="right">2.1%</td>
<td align="right">20,194</td>
<td align="right">2.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">75,349</td>
<td align="right">7.8%</td>
<td align="right">74,810</td>
<td align="right">8.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">102,042</td>
<td align="right">10.5%</td>
<td align="right">102,266</td>
<td align="right">11.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,300</td>
<td align="right">1.6%</td>
<td align="right">15,300</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.3%</td>
<td align="right">12,240</td>
<td align="right">1.4%</td>
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
<td align="right">5,849,192,532</td>
<td align="right">99.6%</td>
<td align="right">5,811,461,367</td>
<td align="right">99.6%</td>
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
<td align="right">438,884</td>
<td align="right">0.0%</td>
<td align="right">439,751</td>
<td align="right">0.0%</td>
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
<td align="right">20,320,990</td>
<td align="right">0.3%</td>
<td align="right">20,322,070</td>
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
<td align="right">462,695</td>
<td align="right">100.0%</td>
<td align="right">462,925</td>
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
<td align="right">7,466</td>
<td align="right">0.0%</td>
<td align="right">7,474</td>
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
<td align="right">83,718,401</td>
<td align="right">100.0%</td>
<td align="right">83,694,514</td>
<td align="right">100.0%</td>
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
<td align="right">7,420</td>
<td align="right">100.0%</td>
<td align="right">7,420</td>
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
<td align="right">786,189,873</td>
<td align="right">81.9%</td>
<td align="right">786,189,911</td>
<td align="right">81.9%</td>
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
<td align="right">173,284,922</td>
<td align="right">18.1%</td>
<td align="right">173,284,918</td>
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
<td align="right">139,444,778</td>
<td align="right">4.8%</td>
<td align="right">109,140,981</td>
<td align="right">3.8%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">190,476,578</td>
<td align="right">6.5%</td>
<td align="right">159,301,903</td>
<td align="right">5.5%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,724,915,900</td>
<td align="right">93.4%</td>
<td align="right">2,738,225,970</td>
<td align="right">94.4%</td>
<td align="right">0.5%</td>
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
<td align="right">2,726,671</td>
<td align="right">96.7%</td>
<td align="right">2,155,022</td>
<td align="right">96.0%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">92,028</td>
<td align="right">3.3%</td>
<td align="right">90,927</td>
<td align="right">4.0%</td>
<td align="right">-1.2%</td>
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
<td align="right">8,760</td>
<td align="right">9.5%</td>
<td align="right">8,220</td>
<td align="right">9.0%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">2,860</td>
<td align="right">3.1%</td>
<td align="right">2,720</td>
<td align="right">3.0%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">32,280</td>
<td align="right">35.1%</td>
<td align="right">31,960</td>
<td align="right">35.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,960</td>
<td align="right">15.2%</td>
<td align="right">13,877</td>
<td align="right">15.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,940</td>
<td align="right">5.4%</td>
<td align="right">4,914</td>
<td align="right">5.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,728</td>
<td align="right">10.6%</td>
<td align="right">9,736</td>
<td align="right">10.7%</td>
<td align="right">0.1%</td>
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
<td align="left">not in keys</td>
<td align="right">6,320</td>
<td align="right">6.9%</td>
<td align="right">6,320</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,780</td>
<td align="right">5.2%</td>
<td align="right">4,780</td>
<td align="right">5.3%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">232,055,289</td>
<td align="right">20.9%</td>
<td align="right">230,254,766</td>
<td align="right">20.8%</td>
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
<td align="right">877,150,915</td>
<td align="right">79.1%</td>
<td align="right">875,257,544</td>
<td align="right">79.2%</td>
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
<td align="right">99,952</td>
<td align="right">88.6%</td>
<td align="right">99,123</td>
<td align="right">88.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,904</td>
<td align="right">11.4%</td>
<td align="right">12,911</td>
<td align="right">11.5%</td>
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
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">6.5%</td>
<td align="right">6,040</td>
<td align="right">6.1%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,512</td>
<td align="right">7.5%</td>
<td align="right">7,443</td>
<td align="right">7.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">39,720</td>
<td align="right">39.7%</td>
<td align="right">39,400</td>
<td align="right">39.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,420</td>
<td align="right">43.4%</td>
<td align="right">43,420</td>
<td align="right">43.8%</td>
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
<td align="right">1.4%</td>
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
<td align="right">248,283,650</td>
<td align="right">3.9%</td>
<td align="right">197,819,980</td>
<td align="right">3.1%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">55,396,436</td>
<td align="right">0.9%</td>
<td align="right">51,030,982</td>
<td align="right">0.8%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,101,684,342</td>
<td align="right">96.1%</td>
<td align="right">6,093,690,066</td>
<td align="right">96.8%</td>
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
<td align="right">1,238,330</td>
<td align="right">77.7%</td>
<td align="right">1,156,139</td>
<td align="right">77.1%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">356,088</td>
<td align="right">22.3%</td>
<td align="right">343,774</td>
<td align="right">22.9%</td>
<td align="right">-3.5%</td>
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
<td align="right">13,246</td>
<td align="right">3.7%</td>
<td align="right">6,727</td>
<td align="right">2.0%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,022</td>
<td align="right">4.2%</td>
<td align="right">17,220</td>
<td align="right">5.0%</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,164</td>
<td align="right">22.8%</td>
<td align="right">74,010</td>
<td align="right">21.5%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,151</td>
<td align="right">1.4%</td>
<td align="right">5,098</td>
<td align="right">1.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12,780</td>
<td align="right">3.6%</td>
<td align="right">12,658</td>
<td align="right">3.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">55,259</td>
<td align="right">15.5%</td>
<td align="right">54,780</td>
<td align="right">15.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">35,071</td>
<td align="right">9.8%</td>
<td align="right">34,853</td>
<td align="right">10.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">135,475</td>
<td align="right">38.0%</td>
<td align="right">135,508</td>
<td align="right">39.4%</td>
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
<td align="right">194,088</td>
<td align="right">0.0%</td>
<td align="right">87,535</td>
<td align="right">0.0%</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,558,467,021</td>
<td align="right">100.0%</td>
<td align="right">1,558,022,596</td>
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
<td align="right">1,855</td>
<td align="right">5.8%</td>
<td align="right">1,756</td>
<td align="right">5.5%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,060</td>
<td align="right">94.2%</td>
<td align="right">30,088</td>
<td align="right">94.5%</td>
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
<td align="right">380</td>
<td align="right">20.5%</td>
<td align="right">320</td>
<td align="right">18.2%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.0%</td>
<td align="right">240</td>
<td align="right">13.7%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,215</td>
<td align="right">65.5%</td>
<td align="right">1,196</td>
<td align="right">68.1%</td>
<td align="right">-1.6%</td>
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
<td align="right">915,204,110</td>
<td align="right">0.7%</td>
<td align="right">746,432,414</td>
<td align="right">0.7%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">66,986,281,975</td>
<td align="right">54.8%</td>
<td align="right">56,505,018,677</td>
<td align="right">53.8%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,721,220,222</td>
<td align="right">9.6%</td>
<td align="right">10,178,182,296</td>
<td align="right">9.7%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">42,686,034,581</td>
<td align="right">34.9%</td>
<td align="right">37,633,054,636</td>
<td align="right">35.8%</td>
<td align="right">-11.8%</td>
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
<td align="right">248,283,650</td>
<td align="right">4.9%</td>
<td align="right">197,819,980</td>
<td align="right">4.4%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">436,983,590</td>
<td align="right">8.7%</td>
<td align="right">356,562,675</td>
<td align="right">7.9%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">190,476,578</td>
<td align="right">3.8%</td>
<td align="right">159,301,903</td>
<td align="right">3.5%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">743,975,778</td>
<td align="right">14.8%</td>
<td align="right">642,393,532</td>
<td align="right">14.2%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,521,346,778</td>
<td align="right">30.3%</td>
<td align="right">1,347,431,610</td>
<td align="right">29.8%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">662,344,987</td>
<td align="right">13.2%</td>
<td align="right">632,024,605</td>
<td align="right">14.0%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,055,289</td>
<td align="right">4.6%</td>
<td align="right">230,254,766</td>
<td align="right">5.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">208,293,964</td>
<td align="right">4.1%</td>
<td align="right">206,690,998</td>
<td align="right">4.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">483,605,440</td>
<td align="right">9.6%</td>
<td align="right">484,251,349</td>
<td align="right">10.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,922</td>
<td align="right">3.5%</td>
<td align="right">173,284,918</td>
<td align="right">3.8%</td>
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
<td align="right">98,361,907</td>
<td align="right">9.9%</td>
<td align="right">68,322,362</td>
<td align="right">8.3%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">114,234,100</td>
<td align="right">11.5%</td>
<td align="right">83,939,181</td>
<td align="right">10.2%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">172,481,809</td>
<td align="right">17.4%</td>
<td align="right">132,545,453</td>
<td align="right">16.1%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">125,829,032</td>
<td align="right">12.7%</td>
<td align="right">98,443,782</td>
<td align="right">11.9%</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">58,788,301</td>
<td align="right">5.9%</td>
<td align="right">50,252,208</td>
<td align="right">6.1%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,529</td>
<td align="right">2.8%</td>
<td align="right">27,496,689</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,897,802</td>
<td align="right">7.8%</td>
<td align="right">77,898,031</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,897,802</td>
<td align="right">7.8%</td>
<td align="right">77,898,031</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,549,222</td>
<td align="right">3.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,365,772</td>
<td align="right">2.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">25,440,201</td>
<td align="right">3.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">25,178,140</td>
<td align="right">3.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,318,329</td>
<td align="right">9.9%</td>
<td align="right">853,328,608</td>
<td align="right">9.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">348,462,155</td>
<td align="right">4.0%</td>
<td align="right">350,185,542</td>
<td align="right">4.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,954,259,212</td>
<td align="right">79.8%</td>
<td align="right">6,939,264,631</td>
<td align="right">79.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,648,726,033</td>
<td align="right">30.4%</td>
<td align="right">2,643,628,331</td>
<td align="right">30.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,648,726,033</td>
<td align="right">30.4%</td>
<td align="right">2,643,628,331</td>
<td align="right">30.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,064,262,044</td>
<td align="right">69.6%</td>
<td align="right">6,053,946,237</td>
<td align="right">69.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,783,961,264</td>
<td align="right">20.5%</td>
<td align="right">1,785,853,283</td>
<td align="right">20.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,788,407,704</td>
<td align="right">20.5%</td>
<td align="right">1,790,299,723</td>
<td align="right">20.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">550,013,406</td>
<td align="right">6.3%</td>
<td align="right">550,229,819</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,398,671</td>
<td align="right">1.0%</td>
<td align="right">84,395,590</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,311</td>
<td align="right">2.0%</td>
<td align="right">175,480,392</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,015,463</td>
<td align="right">0.4%</td>
<td align="right">31,015,470</td>
<td align="right">0.4%</td>
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
<td align="right">9,790,698</td>
<td align="right"></td>
<td align="right">8,155,403</td>
<td align="right"></td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">53,429,234,309</td>
<td align="right">53,429,234,309 / 0 !!</td>
<td align="right">46,758,417,254</td>
<td align="right">46,758,417,254 / 0 !!</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">72,152,319,658</td>
<td align="right">72,152,319,658 / 0 !!</td>
<td align="right">66,567,908,370</td>
<td align="right">66,567,908,370 / 0 !!</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">90,336,842,862</td>
<td align="right">90,336,842,862 / 0 !!</td>
<td align="right">96,493,672,965</td>
<td align="right">96,493,672,965 / 0 !!</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">94,431,114,025</td>
<td align="right">94,431,114,025 / 0 !!</td>
<td align="right">99,497,206,906</td>
<td align="right">99,497,206,906 / 0 !!</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">55,573,731</td>
<td align="right"></td>
<td align="right">57,487,445</td>
<td align="right"></td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,235,892,624</td>
<td align="right"></td>
<td align="right">3,191,342,314</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">62,044,563</td>
<td align="right"></td>
<td align="right">62,328,281</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,129,840</td>
<td align="right"></td>
<td align="right">161,884,496</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">94,086,731</td>
<td align="right">0.4%</td>
<td align="right">93,956,567</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,714,659,337</td>
<td align="right">55.2%</td>
<td align="right">12,698,401,345</td>
<td align="right">55.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,823,594,449</td>
<td align="right">55.7%</td>
<td align="right">12,807,202,327</td>
<td align="right">55.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,527,914,070</td>
<td align="right"></td>
<td align="right">13,511,317,532</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,208,623,947</td>
<td align="right"></td>
<td align="right">10,217,376,738</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,206,754,839</td>
<td align="right">44.3%</td>
<td align="right">10,215,505,199</td>
<td align="right">44.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">14,848,381</td>
<td align="right">0.1%</td>
<td align="right">14,844,415</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,570,645,442</td>
<td align="right"></td>
<td align="right">4,571,775,173</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,305,720</td>
<td align="right">2.0%</td>
<td align="right">3,305,720</td>
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
<td align="right">115,238,760</td>
<td align="right">19,141,706,266</td>
<td align="right">0</td>
<td align="right">114,792,520</td>
<td align="right">19,141,372,871</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,395,224</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,426,108</td>
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
<td align="right">12,567</td>
<td align="right">1.0%</td>
<td align="right">26,058</td>
<td align="right">2.4%</td>
<td align="right">107.4%</td>
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
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">496,205</td>
<td align="right">40.5%</td>
<td align="right">296,202</td>
<td align="right">26.9%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,342</td>
<td align="right">0.1%</td>
<td align="right">1,828</td>
<td align="right">0.2%</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">50,495</td>
<td align="right">4.1%</td>
<td align="right">62,014</td>
<td align="right">5.6%</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">125,495</td>
<td align="right">10.2%</td>
<td align="right">149,213</td>
<td align="right">13.6%</td>
<td align="right">18.9%</td>
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
<td align="right">1,980</td>
<td align="right">0.2%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,099,268</td>
<td align="right">89.8%</td>
<td align="right">951,778</td>
<td align="right">86.4%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">249,964,951,879</td>
<td align="right">3,262.1%</td>
<td align="right">279,135,445,049</td>
<td align="right">3,517.1%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,224,763</td>
<td align="right"></td>
<td align="right">1,100,991</td>
<td align="right"></td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,662,783,662</td>
<td align="right"></td>
<td align="right">7,936,596,481</td>
<td align="right"></td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,350</td>
<td align="right">5.1%</td>
<td align="right">6,512</td>
<td align="right">4.4%</td>
<td align="right">2.6%</td>
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
<td align="right">2,444</td>
<td align="right">1.9%</td>
<td align="right">6,066</td>
<td align="right">4.1%</td>
<td align="right">148.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">125,495</td>
<td align="right"></td>
<td align="right">149,213</td>
<td align="right"></td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">110,704</td>
<td align="right">88.2%</td>
<td align="right">121,397</td>
<td align="right">81.4%</td>
<td align="right">9.7%</td>
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
<td align="right">5,292</td>
<td align="right">4.2%</td>
<td align="right">3,315</td>
<td align="right">2.2%</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,467</td>
<td align="right">17.1%</td>
<td align="right">19,597</td>
<td align="right">13.1%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,069</td>
<td align="right">27.9%</td>
<td align="right">36,433</td>
<td align="right">24.4%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">30,839</td>
<td align="right">24.6%</td>
<td align="right">36,699</td>
<td align="right">24.6%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21,325</td>
<td align="right">17.0%</td>
<td align="right">32,008</td>
<td align="right">21.5%</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,643</td>
<td align="right">7.7%</td>
<td align="right">17,547</td>
<td align="right">11.8%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,700</td>
<td align="right">1.4%</td>
<td align="right">3,394</td>
<td align="right">2.3%</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">37.5%</td>
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
<td align="right">4,112</td>
<td align="right">3.3%</td>
<td align="right">2,195</td>
<td align="right">1.5%</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">14,828</td>
<td align="right">11.8%</td>
<td align="right">13,539</td>
<td align="right">9.1%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">25,072</td>
<td align="right">20.0%</td>
<td align="right">24,677</td>
<td align="right">16.5%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">36,402</td>
<td align="right">29.0%</td>
<td align="right">39,398</td>
<td align="right">26.4%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">18,549</td>
<td align="right">14.8%</td>
<td align="right">24,522</td>
<td align="right">16.4%</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,721</td>
<td align="right">6.9%</td>
<td align="right">12,093</td>
<td align="right">8.1%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,640</td>
<td align="right">2.1%</td>
<td align="right">4,153</td>
<td align="right">2.8%</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">380</td>
<td align="right">0.3%</td>
<td align="right">820</td>
<td align="right">0.5%</td>
<td align="right">115.8%</td>
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
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">7,339,340</td>
<td align="right">24,429.9%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,917,600</td>
<td align="right">125,140,660</td>
<td align="right">3,094.3%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">5,782,740</td>
<td align="right">127,132,520</td>
<td align="right">2,098.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,025,020</td>
<td align="right">63,563,160</td>
<td align="right">2,001.2%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,671,620</td>
<td align="right">31,813,640</td>
<td align="right">766.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">113,126,413</td>
<td align="right">970,904,767</td>
<td align="right">758.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">374,444,989</td>
<td align="right">707.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">382,113,829</td>
<td align="right">610.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">101,766,721</td>
<td align="right">686,373,088</td>
<td align="right">574.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">47,971,801</td>
<td align="right">304,259,219</td>
<td align="right">534.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">13,084,440</td>
<td align="right">382.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">462,511</td>
<td align="right">2,208,546</td>
<td align="right">377.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,726,251</td>
<td align="right">419,518,523</td>
<td align="right">357.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">10,050,940</td>
<td align="right">39,583,080</td>
<td align="right">293.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">11,627,700</td>
<td align="right">41,148,660</td>
<td align="right">253.9%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">21,494</td>
<td align="right">182.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">905,787,417</td>
<td align="right">2,161,701,223</td>
<td align="right">138.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,717,580</td>
<td align="right">59,846,920</td>
<td align="right">132.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">213,840,159</td>
<td align="right">445,284,327</td>
<td align="right">108.2%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,512,307</td>
<td align="right">5,176,468</td>
<td align="right">106.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">67,776,860</td>
<td align="right">139,134,180</td>
<td align="right">105.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,648,680</td>
<td align="right">336,540</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,092,185</td>
<td align="right">62,935,131</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">244,676,060</td>
<td align="right">424,794,564</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">2,231,620</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">126,488,520</td>
<td align="right">210,025,099</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,659,960</td>
<td align="right">9,001,737</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">25,197,724</td>
<td align="right">39,753,320</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">76,110,377</td>
<td align="right">119,158,518</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,591,681</td>
<td align="right">17,953,346</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,420,486,294</td>
<td align="right">2,126,907,425</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,591,681</td>
<td align="right">17,263,066</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,862,100</td>
<td align="right">10,203,877</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">269,595,055</td>
<td align="right">399,294,432</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">270,822,315</td>
<td align="right">400,521,692</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,682,765</td>
<td align="right">39,531,105</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">800,703,305</td>
<td align="right">1,122,571,194</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">173,373,044</td>
<td align="right">239,926,784</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">149,615,705</td>
<td align="right">201,624,458</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">39,840</td>
<td align="right">26,060</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,473,921</td>
<td align="right">105,597,912</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,697,199</td>
<td align="right">120,433,223</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">81,529,680</td>
<td align="right">108,630,780</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">81,660,960</td>
<td align="right">108,766,180</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">407,708,772</td>
<td align="right">538,187,597</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">317,176,840</td>
<td align="right">417,318,071</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">163,092,480</td>
<td align="right">213,801,455</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,426,115</td>
<td align="right">124,482,191</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,431,473</td>
<td align="right">120,556,314</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,165,660,876</td>
<td align="right">2,791,667,173</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">30,568,098</td>
<td align="right">39,127,916</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">3,628,061</td>
<td align="right">4,642,379</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">457,491,124</td>
<td align="right">585,124,089</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">394,201,379</td>
<td align="right">494,919,593</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">834,125,077</td>
<td align="right">1,042,131,070</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">702,492,374</td>
<td align="right">875,621,439</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,491,313,814</td>
<td align="right">1,845,963,632</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">777,697,297</td>
<td align="right">960,360,034</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">263,318,456</td>
<td align="right">323,540,923</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,688,932,707</td>
<td align="right">2,065,765,012</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,025,132,238</td>
<td align="right">2,469,279,118</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">121,960,501</td>
<td align="right">148,610,488</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,085,613,560</td>
<td align="right">2,525,637,072</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,963,676,239</td>
<td align="right">2,377,050,384</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,189,408,460</td>
<td align="right">1,439,657,818</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,430,654,706</td>
<td align="right">2,932,418,036</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">193,403,082</td>
<td align="right">232,864,956</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">395,731,858</td>
<td align="right">476,335,764</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,301,792,100</td>
<td align="right">1,562,962,458</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">274,720,053</td>
<td align="right">329,594,312</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,322,510,660</td>
<td align="right">1,586,121,498</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,404,436,106</td>
<td align="right">2,871,892,776</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,790,352,355</td>
<td align="right">2,137,174,244</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">338,030,338</td>
<td align="right">398,550,584</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,619,553,404</td>
<td align="right">4,218,942,001</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">310,680</td>
<td align="right">360,108</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,046,270,502</td>
<td align="right">1,212,297,652</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,152,863,056</td>
<td align="right">1,335,135,669</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,120,591,954</td>
<td align="right">7,084,763,780</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,418,359,060</td>
<td align="right">5,085,991,181</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,824,211,573</td>
<td align="right">7,832,909,808</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,415,372</td>
<td align="right">109,251,114</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,659,232</td>
<td align="right">109,496,534</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">658,594,590</td>
<td align="right">753,429,047</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">651,277,592</td>
<td align="right">743,151,708</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">266,228,276</td>
<td align="right">301,236,808</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">436,193,357</td>
<td align="right">493,057,634</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">904,464,323</td>
<td align="right">1,020,322,505</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,282,113,648</td>
<td align="right">8,187,333,988</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,739,447,806</td>
<td align="right">4,198,075,535</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,695,466,751</td>
<td align="right">10,866,052,496</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,324,581,236</td>
<td align="right">1,482,069,001</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,431,840,320</td>
<td align="right">3,836,987,039</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">923,984,306</td>
<td align="right">1,030,730,604</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,989,941,469</td>
<td align="right">19,988,177,625</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">515,035,377</td>
<td align="right">571,900,118</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">860,509,833</td>
<td align="right">953,715,718</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">562,771,551</td>
<td align="right">623,641,543</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,921,048</td>
<td align="right">5,448,029</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,020,164,817</td>
<td align="right">2,232,829,377</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">15,659,063,378</td>
<td align="right">17,229,004,215</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">104,757,000</td>
<td align="right">115,083,100</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">239,755,494</td>
<td align="right">216,554,533</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,131,192,110</td>
<td align="right">1,240,229,392</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,713,892</td>
<td align="right">99,433,148</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,037,317,327</td>
<td align="right">3,320,174,774</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,059,561,050</td>
<td align="right">1,155,736,713</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">102,572,233</td>
<td align="right">111,760,671</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,345,934,210</td>
<td align="right">1,466,485,066</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,831,680</td>
<td align="right">67,086,260</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,685,040</td>
<td align="right">221,564,260</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,238,052,860</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,258,544,892</td>
<td align="right">6,764,545,114</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">510,187,700</td>
<td align="right">550,405,462</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">28,421,142</td>
<td align="right">30,653,519</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,983</td>
<td align="right">414,659,100</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">947,361,243</td>
<td align="right">1,021,021,337</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,894,772</td>
<td align="right">34,298,982</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">970,230,546</td>
<td align="right">1,042,831,823</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">246,295,251</td>
<td align="right">264,160,673</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">216,572,786</td>
<td align="right">232,260,954</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">219,101,558</td>
<td align="right">234,794,105</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">889,878,710</td>
<td align="right">953,015,137</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,650,560</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,990,580</td>
<td align="right">154,073,200</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,682,494,162</td>
<td align="right">1,787,611,404</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,611,668,832</td>
<td align="right">1,710,098,282</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,688,889,199</td>
<td align="right">4,973,394,234</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">137,740,730</td>
<td align="right">145,418,268</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,187,379</td>
<td align="right">103,430,088</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,819,494,272</td>
<td align="right">5,067,655,578</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,230,039</td>
<td align="right">102,024,666</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,383,672,429</td>
<td align="right">1,446,022,977</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">614,586,157</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">198,419,590</td>
<td align="right">207,004,180</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">164,118,908</td>
<td align="right">171,145,552</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,027,078,195</td>
<td align="right">1,070,014,793</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,192</td>
<td align="right">671,741,960</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">553,952,231</td>
<td align="right">576,793,409</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,883,902,915</td>
<td align="right">1,959,223,948</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">664,492,575</td>
<td align="right">689,686,170</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,702,632</td>
<td align="right">807,970,628</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,165,312</td>
<td align="right">807,367,648</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,060</td>
<td align="right">139,083,024</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,060</td>
<td align="right">139,083,024</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,662,783,662</td>
<td align="right">7,936,596,481</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,567,981,343</td>
<td align="right">6,338,181,935</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">67,154,700</td>
<td align="right">64,834,230</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,253,466,122</td>
<td align="right">1,294,309,899</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,825,999,504</td>
<td align="right">1,883,817,427</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">59,644,340</td>
<td align="right">61,506,960</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,853,908,199</td>
<td align="right">1,911,686,740</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">387,294,368</td>
<td align="right">399,221,822</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,280,056,495</td>
<td align="right">1,316,979,386</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,326,686</td>
<td align="right">2,393,732</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,965,460</td>
<td align="right">159,380,540</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">7,009,658,531</td>
<td align="right">7,208,657,268</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,228,286</td>
<td align="right">10,509,881</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,329,504,601</td>
<td align="right">2,392,877,615</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,576,495,380</td>
<td align="right">1,619,178,234</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">235,521,457</td>
<td align="right">241,865,315</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">48,454,202</td>
<td align="right">49,692,964</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">992,081,756</td>
<td align="right">1,017,142,396</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,720</td>
<td align="right">840,680</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">395,091,324</td>
<td align="right">403,710,340</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,490,215</td>
<td align="right">163,964,693</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,622,792,819</td>
<td align="right">3,698,200,413</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">64,522,824</td>
<td align="right">65,852,620</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,816,548,580</td>
<td align="right">1,853,265,036</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,841,188,412</td>
<td align="right">2,890,937,219</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">218,973,940</td>
<td align="right">222,603,840</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,681,958</td>
<td align="right">10,514,666</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">321,365,542</td>
<td align="right">326,285,188</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,372,400,142</td>
<td align="right">3,423,943,113</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,966,880</td>
<td align="right">3,011,580</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,746,571,766</td>
<td align="right">2,785,815,101</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">60,988,920</td>
<td align="right">60,146,280</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,550,540</td>
<td align="right">189,898,400</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,508,815,238</td>
<td align="right">2,538,759,784</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,098,403,788</td>
<td align="right">1,089,447,655</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,259,100,376</td>
<td align="right">2,276,091,999</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,013,560</td>
<td align="right">529,105,800</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,186,475,474</td>
<td align="right">13,275,392,319</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">140,211,736</td>
<td align="right">141,110,312</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">972,676,531</td>
<td align="right">978,843,013</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,319,667,689</td>
<td align="right">2,333,921,120</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,275,734,978</td>
<td align="right">4,249,543,305</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,997,909,397</td>
<td align="right">2,009,792,080</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,580,260</td>
<td align="right">86,108,500</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,165,983,048</td>
<td align="right">3,182,982,626</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,604,321</td>
<td align="right">735,463,970</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,177,300</td>
<td align="right">8,214,320</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">894,226,760</td>
<td align="right">897,763,259</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,954,499</td>
<td align="right">230,829,324</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,754,260</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">643,765,623</td>
<td align="right">645,566,819</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">297,178,439</td>
<td align="right">297,754,413</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,705,220</td>
<td align="right">80,715,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,402,696</td>
<td align="right">32,404,336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,697,060</td>
<td align="right">12,697,060</td>
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
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">34,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALLER_IP</td>
<td align="right"></td>
<td align="right">1,457,049,379</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">37,007,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">4,075,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_INIT_CHECK</td>
<td align="right"></td>
<td align="right">960,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">14,120</td>
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
<td align="right">1,200</td>
<td align="right">1,820</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">320</td>
<td align="right">460</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,142</td>
<td align="right">8,484</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,540</td>
<td align="right">4,461</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">600</td>
<td align="right">720</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">409</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">30,500</td>
<td align="right">34,344</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,624</td>
<td align="right">7,261</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">486,367</td>
<td align="right">519,636</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,668</td>
<td align="right">47,013</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,456</td>
<td align="right">2,546</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">640</td>
<td align="right">660</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,680</td>
<td align="right">1,720</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">33,340</td>
<td align="right">33,960</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right"></td>
<td align="right">20</td>
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
<td align="right">1,106</td>
<td align="right">1,107</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,106</td>
<td align="right">1,107</td>
<td align="right">0.1%</td>
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
Stats gathered on: 2024-10-21
