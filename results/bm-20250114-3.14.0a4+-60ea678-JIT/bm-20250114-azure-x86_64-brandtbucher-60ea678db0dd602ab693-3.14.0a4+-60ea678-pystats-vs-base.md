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
<td align="right">3,428,749</td>
<td align="right">3,638,622</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">21,861,195</td>
<td align="right">21,130,299</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,111,372</td>
<td align="right">4,247,471</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,407,890</td>
<td align="right">13,770,818</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">66,258,006</td>
<td align="right">67,199,738</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,897,775</td>
<td align="right">3,943,129</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,131,166</td>
<td align="right">9,222,404</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,651,714</td>
<td align="right">9,742,772</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">36,439,272</td>
<td align="right">36,711,636</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,623,321</td>
<td align="right">60,990,159</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,763,483</td>
<td align="right">18,854,336</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">36,934,436</td>
<td align="right">36,772,716</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">329,024,406</td>
<td align="right">330,412,140</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">322,288,160</td>
<td align="right">323,548,321</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">263,847,507</td>
<td align="right">264,781,300</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,476,135</td>
<td align="right">48,637,383</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">538,897,165</td>
<td align="right">540,446,423</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">58,758,773</td>
<td align="right">58,919,594</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">292,898,974</td>
<td align="right">293,651,957</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">17,794,818</td>
<td align="right">17,840,264</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">107,528,067</td>
<td align="right">107,801,180</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">126,915,655</td>
<td align="right">127,225,732</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">85,877,243</td>
<td align="right">86,084,910</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">127,355,270</td>
<td align="right">127,655,223</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">157,375,241</td>
<td align="right">157,723,292</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">171,708,571</td>
<td align="right">172,061,647</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">229,333,539</td>
<td align="right">229,734,603</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">79,818,092</td>
<td align="right">79,954,191</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">185,417,456</td>
<td align="right">185,722,500</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">86,218,868</td>
<td align="right">86,359,634</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">51,818,241</td>
<td align="right">51,897,296</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,107,990,534</td>
<td align="right">2,110,906,455</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">96,033,975</td>
<td align="right">96,165,275</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">379,574,238</td>
<td align="right">380,058,950</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,778,754,510</td>
<td align="right">1,781,012,284</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">617,826,924</td>
<td align="right">618,598,331</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">320,995,401</td>
<td align="right">321,377,002</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">379,558,335</td>
<td align="right">379,985,023</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,289,398,049</td>
<td align="right">1,290,845,063</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">66,797,110</td>
<td align="right">66,868,481</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">181,866,724</td>
<td align="right">182,053,004</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">160,133,024</td>
<td align="right">159,971,240</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">714,130,747</td>
<td align="right">714,831,167</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">132,014,706</td>
<td align="right">131,885,562</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">159,544,845</td>
<td align="right">159,694,152</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">171,643,366</td>
<td align="right">171,487,578</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,230,156,437</td>
<td align="right">2,232,069,012</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">610,752,795</td>
<td align="right">611,269,078</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,738,682,636</td>
<td align="right">4,742,624,406</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,883,149,221</td>
<td align="right">3,886,355,361</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">413,288,130</td>
<td align="right">413,629,062</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,483,835,128</td>
<td align="right">13,494,313,831</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,266,477,877</td>
<td align="right">2,268,159,209</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">236,390,415</td>
<td align="right">236,565,410</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">153,299,217</td>
<td align="right">153,410,185</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">828,716,975</td>
<td align="right">829,308,144</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">65,382,833</td>
<td align="right">65,428,650</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,144,929,375</td>
<td align="right">3,147,122,399</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,771,048,195</td>
<td align="right">2,772,957,112</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,494,447,292</td>
<td align="right">1,495,448,169</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,072,526,194</td>
<td align="right">3,074,558,132</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,815,377,730</td>
<td align="right">3,817,632,566</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">621,909,656</td>
<td align="right">622,245,636</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">622,265,745</td>
<td align="right">622,599,661</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">95,300,399</td>
<td align="right">95,349,605</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,619,672,295</td>
<td align="right">1,620,457,575</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">58,466,431</td>
<td align="right">58,494,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">51,892,418</td>
<td align="right">51,916,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">702,163,520</td>
<td align="right">702,452,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">153,458,454</td>
<td align="right">153,519,536</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">119,078,472</td>
<td align="right">119,125,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,564,216,069</td>
<td align="right">1,564,807,166</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">79,458,067</td>
<td align="right">79,428,483</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,670</td>
<td align="right">33,682</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,305,358</td>
<td align="right">10,308,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">537,814,572</td>
<td align="right">537,996,251</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">647,340,332</td>
<td align="right">647,550,125</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">262,564,356</td>
<td align="right">262,640,015</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,885,336,378</td>
<td align="right">1,885,875,118</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">433,940,688</td>
<td align="right">434,052,458</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">256,017,498</td>
<td align="right">256,082,767</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">130,950</td>
<td align="right">130,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">264,082,926</td>
<td align="right">264,031,846</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">188,169,004</td>
<td align="right">188,199,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">405,478</td>
<td align="right">405,542</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">36,612,389</td>
<td align="right">36,607,549</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">482,480,087</td>
<td align="right">482,541,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">112,753,628</td>
<td align="right">112,766,728</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">102,903,846</td>
<td align="right">102,915,771</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">42,658,126</td>
<td align="right">42,653,286</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">36,151,839</td>
<td align="right">36,148,499</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">200,295,958</td>
<td align="right">200,311,570</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">181,870,599</td>
<td align="right">181,882,373</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,650</td>
<td align="right">773,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,990,376,101</td>
<td align="right">1,990,487,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">229,234,570</td>
<td align="right">229,245,896</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,924,195</td>
<td align="right">58,921,343</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">30,413,003</td>
<td align="right">30,414,398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">59,426,191</td>
<td align="right">59,423,952</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">223,104,311</td>
<td align="right">223,096,891</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,439,869</td>
<td align="right">1,439,914</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,162,481</td>
<td align="right">9,162,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">300,502,543</td>
<td align="right">300,495,091</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">278,305,608</td>
<td align="right">278,299,752</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">905,566,538</td>
<td align="right">905,584,924</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">61,578,075</td>
<td align="right">61,578,903</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">68,337,483</td>
<td align="right">68,338,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,531,175</td>
<td align="right">67,531,885</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,115,113</td>
<td align="right">3,115,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,875,744</td>
<td align="right">26,876,004</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,648,036</td>
<td align="right">11,648,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,615,999</td>
<td align="right">133,614,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,014,630</td>
<td align="right">95,015,218</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,090,164</td>
<td align="right">2,090,174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">25,934,933</td>
<td align="right">25,935,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,546,571</td>
<td align="right">20,546,667</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,877,111</td>
<td align="right">20,877,207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,877,132</td>
<td align="right">20,877,228</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,135,473</td>
<td align="right">70,135,786</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">58,535,236</td>
<td align="right">58,535,494</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">116,016,990</td>
<td align="right">116,016,536</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">49,179,570</td>
<td align="right">49,179,701</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,885</td>
<td align="right">6,169,901</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">393,176,375</td>
<td align="right">393,177,235</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">24,727,426</td>
<td align="right">24,727,382</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,785,460</td>
<td align="right">1,071,787,301</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">189,409,366</td>
<td align="right">189,409,043</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">157,622,796</td>
<td align="right">157,623,053</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,258</td>
<td align="right">14,760,276</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">289,434,235</td>
<td align="right">289,433,912</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">79,437,631</td>
<td align="right">79,437,707</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,347,251</td>
<td align="right">97,347,171</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">112,046,059</td>
<td align="right">112,046,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,335,404</td>
<td align="right">242,335,598</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">329,106,270</td>
<td align="right">329,106,487</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">69,841,125</td>
<td align="right">69,841,171</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">58,843,615</td>
<td align="right">58,843,577</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">208,903,506</td>
<td align="right">208,903,637</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">169,249,680</td>
<td align="right">169,249,590</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">206,464,020</td>
<td align="right">206,464,123</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">266,550,891</td>
<td align="right">266,550,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">54,468,015</td>
<td align="right">54,467,991</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">453,979,271</td>
<td align="right">453,979,104</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">776,892,388</td>
<td align="right">776,892,570</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">79,752,516</td>
<td align="right">79,752,501</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">114,701,661</td>
<td align="right">114,701,648</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">139,896,338</td>
<td align="right">139,896,352</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,814,106</td>
<td align="right">100,814,099</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">90,861,268</td>
<td align="right">90,861,264</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,369</td>
<td align="right">302,607,369</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">177,225,660</td>
<td align="right">177,225,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">170,068,018</td>
<td align="right">170,068,018</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,581</td>
<td align="right">128,850,581</td>
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
<td align="right">41,964,789</td>
<td align="right">41,964,789</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">34,315,050</td>
<td align="right">34,315,050</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">33,292,776</td>
<td align="right">33,292,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">31,650,499</td>
<td align="right">31,650,499</td>
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
<td align="left">CALL_STR_1</td>
<td align="right">23,563,771</td>
<td align="right">23,563,771</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">21,773,913</td>
<td align="right">21,773,913</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,976,841</td>
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
<td align="right">4,866,933</td>
<td align="right">4,866,933</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,957,709</td>
<td align="right">3,957,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,902,682</td>
<td align="right">3,902,682</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,573,080</td>
<td align="right">2,573,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,920</td>
<td align="right">1,645,920</td>
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
<td align="right">236,915</td>
<td align="right">236,915</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,885</td>
<td align="right">120,885</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,718</td>
<td align="right">98,718</td>
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
<td align="right">57,166</td>
<td align="right">57,166</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,670</td>
<td align="right">56,670</td>
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
<td align="right">3,624</td>
<td align="right">3,624</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,708</td>
<td align="right">2,708</td>
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
<td align="right">152</td>
<td align="right">152</td>
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
<td align="right">42</td>
<td align="right">42</td>
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
<td align="right">321,491,008</td>
<td align="right">4.2%</td>
<td align="right">322,750,273</td>
<td align="right">4.2%</td>
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
<td align="right">22,797,943</td>
<td align="right">0.3%</td>
<td align="right">22,806,643</td>
<td align="right">0.3%</td>
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
<td align="right">7,373,777,436</td>
<td align="right">95.5%</td>
<td align="right">7,373,997,565</td>
<td align="right">95.5%</td>
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
<td align="right">790,120</td>
<td align="right">64.4%</td>
<td align="right">791,020</td>
<td align="right">64.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">437,168</td>
<td align="right">35.6%</td>
<td align="right">437,331</td>
<td align="right">35.6%</td>
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
<td align="left">and int</td>
<td align="right">10,099</td>
<td align="right">1.3%</td>
<td align="right">10,348</td>
<td align="right">1.3%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">6,407</td>
<td align="right">0.8%</td>
<td align="right">6,544</td>
<td align="right">0.8%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">56,248</td>
<td align="right">7.1%</td>
<td align="right">56,776</td>
<td align="right">7.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">492</td>
<td align="right">0.1%</td>
<td align="right">493</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,851</td>
<td align="right">2.5%</td>
<td align="right">19,829</td>
<td align="right">2.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,478</td>
<td align="right">0.4%</td>
<td align="right">3,479</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">13,451</td>
<td align="right">1.7%</td>
<td align="right">13,453</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,538</td>
<td align="right">3.0%</td>
<td align="right">23,537</td>
<td align="right">3.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">49,854</td>
<td align="right">6.3%</td>
<td align="right">49,856</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">583,386</td>
<td align="right">73.8%</td>
<td align="right">583,389</td>
<td align="right">73.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,412</td>
<td align="right">0.7%</td>
<td align="right">5,412</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">5,273</td>
<td align="right">0.7%</td>
<td align="right">5,273</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">3,331</td>
<td align="right">0.4%</td>
<td align="right">3,331</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">3,267</td>
<td align="right">0.4%</td>
<td align="right">3,267</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.3%</td>
<td align="right">2,343</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1,387</td>
<td align="right">0.2%</td>
<td align="right">1,387</td>
<td align="right">0.2%</td>
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
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">836</td>
<td align="right">0.1%</td>
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
<td align="right">97,347,251</td>
<td align="right">100.0%</td>
<td align="right">97,347,171</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,824,989</td>
<td align="right">0.1%</td>
<td align="right">5,822,823</td>
<td align="right">0.1%</td>
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
<td align="right">482,321,333</td>
<td align="right">8.1%</td>
<td align="right">482,382,938</td>
<td align="right">8.1%</td>
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
<td align="right">5,470,713,801</td>
<td align="right">91.8%</td>
<td align="right">5,470,817,127</td>
<td align="right">91.8%</td>
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
<td align="right">118,912</td>
<td align="right">44.3%</td>
<td align="right">118,872</td>
<td align="right">44.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">149,516</td>
<td align="right">55.7%</td>
<td align="right">149,524</td>
<td align="right">55.7%</td>
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
<td align="right">3,681</td>
<td align="right">2.5%</td>
<td align="right">3,679</td>
<td align="right">2.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,443</td>
<td align="right">8.3%</td>
<td align="right">12,446</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">59,691</td>
<td align="right">39.9%</td>
<td align="right">59,698</td>
<td align="right">39.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">35,115</td>
<td align="right">23.5%</td>
<td align="right">35,115</td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">24,073</td>
<td align="right">16.1%</td>
<td align="right">24,073</td>
<td align="right">16.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">7,101</td>
<td align="right">4.7%</td>
<td align="right">7,101</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,609</td>
<td align="right">2.4%</td>
<td align="right">3,609</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.0%</td>
<td align="right">2,941</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">769</td>
<td align="right">0.5%</td>
<td align="right">769</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">72</td>
<td align="right">0.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,053,992,658</td>
<td align="right">98.8%</td>
<td align="right">11,058,499,636</td>
<td align="right">98.9%</td>
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
<td align="right">230,056</td>
<td align="right">0.0%</td>
<td align="right">230,070</td>
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
<td align="right">128,248,425</td>
<td align="right">1.1%</td>
<td align="right">128,241,598</td>
<td align="right">1.1%</td>
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
<td align="right">2,593,712</td>
<td align="right">100.0%</td>
<td align="right">2,593,632</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">446</td>
<td align="right">0.0%</td>
<td align="right">446</td>
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
<td align="right">752</td>
<td align="right">168.6%</td>
<td align="right">752</td>
<td align="right">168.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">287</td>
<td align="right">64.3%</td>
<td align="right">287</td>
<td align="right">64.3%</td>
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
<td align="right">111,575</td>
<td align="right">15.8%</td>
<td align="right">111,575</td>
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
<td align="right">584,005</td>
<td align="right">82.9%</td>
<td align="right">584,005</td>
<td align="right">82.9%</td>
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
<td align="right">20,190</td>
<td align="right">99.4%</td>
<td align="right">20,190</td>
<td align="right">99.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">0.6%</td>
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
<td align="right">1,291,622</td>
<td align="right">0.0%</td>
<td align="right">1,306,644</td>
<td align="right">0.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">86,095,499</td>
<td align="right">1.9%</td>
<td align="right">86,235,901</td>
<td align="right">1.9%</td>
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
<td align="right">4,516,921,922</td>
<td align="right">98.1%</td>
<td align="right">4,517,479,586</td>
<td align="right">98.1%</td>
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
<td align="right">42,309</td>
<td align="right">28.7%</td>
<td align="right">42,594</td>
<td align="right">28.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">105,108</td>
<td align="right">71.3%</td>
<td align="right">105,469</td>
<td align="right">71.2%</td>
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
<td align="left">float long</td>
<td align="right">8,095</td>
<td align="right">7.7%</td>
<td align="right">8,433</td>
<td align="right">8.0%</td>
<td align="right">4.2%</td>
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
<td align="left">bool</td>
<td align="right">927</td>
<td align="right">0.9%</td>
<td align="right">932</td>
<td align="right">0.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,735</td>
<td align="right">7.4%</td>
<td align="right">7,756</td>
<td align="right">7.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,544</td>
<td align="right">4.3%</td>
<td align="right">4,540</td>
<td align="right">4.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,186</td>
<td align="right">22.1%</td>
<td align="right">23,192</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">43,653</td>
<td align="right">41.5%</td>
<td align="right">43,646</td>
<td align="right">41.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.3%</td>
<td align="right">7,639</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,430</td>
<td align="right">6.1%</td>
<td align="right">6,430</td>
<td align="right">6.1%</td>
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
<td align="right">983</td>
<td align="right">0.9%</td>
<td align="right">983</td>
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
<td align="right">51,782,027</td>
<td align="right">2.3%</td>
<td align="right">51,861,058</td>
<td align="right">2.3%</td>
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
<td align="right">2,189,211,811</td>
<td align="right">97.6%</td>
<td align="right">2,189,529,193</td>
<td align="right">97.6%</td>
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
<td align="right">33,953</td>
<td align="right">46.9%</td>
<td align="right">33,977</td>
<td align="right">46.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,435</td>
<td align="right">53.1%</td>
<td align="right">38,435</td>
<td align="right">53.1%</td>
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
<td align="right">7,830</td>
<td align="right">23.1%</td>
<td align="right">7,856</td>
<td align="right">23.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,739</td>
<td align="right">16.9%</td>
<td align="right">5,737</td>
<td align="right">16.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,178</td>
<td align="right">32.9%</td>
<td align="right">11,178</td>
<td align="right">32.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,206</td>
<td align="right">27.1%</td>
<td align="right">9,206</td>
<td align="right">27.1%</td>
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
<td align="right">32,000,045</td>
<td align="right">4.3%</td>
<td align="right">31,861,656</td>
<td align="right">4.3%</td>
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
<td align="right">118,977,892</td>
<td align="right">15.9%</td>
<td align="right">119,029,566</td>
<td align="right">15.9%</td>
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
<td align="right">597,599,104</td>
<td align="right">79.8%</td>
<td align="right">597,807,490</td>
<td align="right">79.8%</td>
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
<td align="right">95,503</td>
<td align="right">13.6%</td>
<td align="right">90,456</td>
<td align="right">13.0%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">608,705</td>
<td align="right">86.4%</td>
<td align="right">606,116</td>
<td align="right">87.0%</td>
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
<td align="left">dict items</td>
<td align="right">54,326</td>
<td align="right">56.9%</td>
<td align="right">49,275</td>
<td align="right">54.5%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,898</td>
<td align="right">6.2%</td>
<td align="right">5,901</td>
<td align="right">6.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,739</td>
<td align="right">11.2%</td>
<td align="right">10,740</td>
<td align="right">11.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,546</td>
<td align="right">4.8%</td>
<td align="right">4,546</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,495</td>
<td align="right">4.7%</td>
<td align="right">4,495</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4,183</td>
<td align="right">4.4%</td>
<td align="right">4,183</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,015</td>
<td align="right">3.2%</td>
<td align="right">3,015</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,867</td>
<td align="right">3.0%</td>
<td align="right">2,867</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,247</td>
<td align="right">2.4%</td>
<td align="right">2,247</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,587</td>
<td align="right">1.7%</td>
<td align="right">1,587</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">965</td>
<td align="right">1.0%</td>
<td align="right">965</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">327</td>
<td align="right">0.4%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">537,271,633</td>
<td align="right">4.1%</td>
<td align="right">538,820,298</td>
<td align="right">4.1%</td>
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
<td align="right">12,022,518,650</td>
<td align="right">91.0%</td>
<td align="right">12,028,907,662</td>
<td align="right">91.0%</td>
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
<td align="right">645,123,740</td>
<td align="right">4.9%</td>
<td align="right">645,335,092</td>
<td align="right">4.9%</td>
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
<td align="right">1,404,473</td>
<td align="right">0.0%</td>
<td align="right">1,404,473</td>
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
<td align="right">356,204</td>
<td align="right">2.8%</td>
<td align="right">356,803</td>
<td align="right">2.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,258,758</td>
<td align="right">97.2%</td>
<td align="right">12,262,572</td>
<td align="right">97.2%</td>
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
<td align="right">4,912</td>
<td align="right">1.4%</td>
<td align="right">5,006</td>
<td align="right">1.4%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">38,531</td>
<td align="right">10.8%</td>
<td align="right">38,788</td>
<td align="right">10.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">858</td>
<td align="right">0.2%</td>
<td align="right">859</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,144</td>
<td align="right">6.8%</td>
<td align="right">24,168</td>
<td align="right">6.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">41,448</td>
<td align="right">11.6%</td>
<td align="right">41,480</td>
<td align="right">11.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60,080</td>
<td align="right">16.9%</td>
<td align="right">60,105</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,407</td>
<td align="right">0.7%</td>
<td align="right">2,408</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,528</td>
<td align="right">4.1%</td>
<td align="right">14,533</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,942</td>
<td align="right">2.2%</td>
<td align="right">7,943</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.8%</td>
<td align="right">6,405</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,951</td>
<td align="right">1.4%</td>
<td align="right">4,951</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,626</td>
<td align="right">0.5%</td>
<td align="right">1,626</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,578</td>
<td align="right">0.4%</td>
<td align="right">1,578</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.3%</td>
<td align="right">1,092</td>
<td align="right">0.3%</td>
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
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">163</td>
<td align="right">0.0%</td>
<td align="right">163</td>
<td align="right">0.0%</td>
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
<td align="right">3,711,063,434</td>
<td align="right">99.6%</td>
<td align="right">3,714,977,319</td>
<td align="right">99.6%</td>
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
<td align="right">14,622,678</td>
<td align="right">0.4%</td>
<td align="right">14,622,679</td>
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
<td align="right">52,726</td>
<td align="right">0.0%</td>
<td align="right">52,726</td>
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
<td align="right">138,366</td>
<td align="right">100.0%</td>
<td align="right">138,383</td>
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
<td align="right">64,606,852</td>
<td align="right">100.0%</td>
<td align="right">65,105,920</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
</tr>
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
<td align="right">253</td>
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
<td align="right">593,288,688</td>
<td align="right">82.2%</td>
<td align="right">593,288,791</td>
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
<td align="right">128,815,789</td>
<td align="right">17.8%</td>
<td align="right">128,815,789</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">115,875,524</td>
<td align="right">5.7%</td>
<td align="right">115,757,516</td>
<td align="right">5.7%</td>
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
<td align="right">1,844,770,515</td>
<td align="right">90.9%</td>
<td align="right">1,845,794,147</td>
<td align="right">90.9%</td>
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
<td align="right">69,747,998</td>
<td align="right">3.4%</td>
<td align="right">69,748,039</td>
<td align="right">3.4%</td>
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
<td align="right">2,227,736</td>
<td align="right">97.8%</td>
<td align="right">2,225,530</td>
<td align="right">97.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">50,973</td>
<td align="right">2.2%</td>
<td align="right">50,979</td>
<td align="right">2.2%</td>
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
<td align="left">not managed dict</td>
<td align="right">3,352</td>
<td align="right">6.6%</td>
<td align="right">3,358</td>
<td align="right">6.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">135,551</td>
<td align="right">265.9%</td>
<td align="right">135,659</td>
<td align="right">266.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,077</td>
<td align="right">47.2%</td>
<td align="right">24,077</td>
<td align="right">47.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">15.0%</td>
<td align="right">7,666</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,098</td>
<td align="right">10.0%</td>
<td align="right">5,098</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,954</td>
<td align="right">9.7%</td>
<td align="right">4,954</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.2%</td>
<td align="right">1,619</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">810</td>
<td align="right">1.6%</td>
<td align="right">810</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.4%</td>
<td align="right">699</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">361</td>
<td align="right">0.7%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">920,108,076</td>
<td align="right">87.3%</td>
<td align="right">920,426,123</td>
<td align="right">87.3%</td>
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
<td align="right">133,570,061</td>
<td align="right">12.7%</td>
<td align="right">133,568,905</td>
<td align="right">12.7%</td>
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
<td align="left">Success</td>
<td align="right">2,197</td>
<td align="right">4.8%</td>
<td align="right">2,196</td>
<td align="right">4.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43,781</td>
<td align="right">95.2%</td>
<td align="right">43,779</td>
<td align="right">95.2%</td>
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
<td align="right">14,759</td>
<td align="right">33.7%</td>
<td align="right">14,757</td>
<td align="right">33.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,703</td>
<td align="right">38.2%</td>
<td align="right">16,703</td>
<td align="right">38.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">8,143</td>
<td align="right">18.6%</td>
<td align="right">8,143</td>
<td align="right">18.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,032</td>
<td align="right">6.9%</td>
<td align="right">3,032</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">499</td>
<td align="right">1.1%</td>
<td align="right">499</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.8%</td>
<td align="right">341</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">236</td>
<td align="right">0.5%</td>
<td align="right">236</td>
<td align="right">0.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,598,529,170</td>
<td align="right">97.0%</td>
<td align="right">4,601,036,809</td>
<td align="right">97.0%</td>
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
<td align="right">102,436,039</td>
<td align="right">2.2%</td>
<td align="right">102,447,905</td>
<td align="right">2.2%</td>
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
<td align="right">41,017,176</td>
<td align="right">0.9%</td>
<td align="right">41,017,376</td>
<td align="right">0.9%</td>
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
<td align="right">417,637</td>
<td align="right">33.7%</td>
<td align="right">417,663</td>
<td align="right">33.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">822,562</td>
<td align="right">66.3%</td>
<td align="right">822,594</td>
<td align="right">66.3%</td>
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
<td align="left">mapping</td>
<td align="right">8,612</td>
<td align="right">2.1%</td>
<td align="right">8,628</td>
<td align="right">2.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">19,829</td>
<td align="right">4.7%</td>
<td align="right">19,864</td>
<td align="right">4.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">5,687</td>
<td align="right">1.4%</td>
<td align="right">5,690</td>
<td align="right">1.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">93,843</td>
<td align="right">22.5%</td>
<td align="right">93,812</td>
<td align="right">22.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,359</td>
<td align="right">3.0%</td>
<td align="right">12,360</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">13,474</td>
<td align="right">3.2%</td>
<td align="right">13,475</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,451</td>
<td align="right">61.6%</td>
<td align="right">257,452</td>
<td align="right">61.6%</td>
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
<td align="right">1,233,404,250</td>
<td align="right">99.9%</td>
<td align="right">1,233,501,476</td>
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
<td align="right">1,427,480</td>
<td align="right">0.1%</td>
<td align="right">1,427,521</td>
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
<td align="right">868</td>
<td align="right">7.0%</td>
<td align="right">872</td>
<td align="right">7.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,601</td>
<td align="right">93.0%</td>
<td align="right">11,601</td>
<td align="right">93.0%</td>
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
<td align="right">641</td>
<td align="right">73.8%</td>
<td align="right">645</td>
<td align="right">74.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.7%</td>
<td align="right">136</td>
<td align="right">15.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">10.5%</td>
<td align="right">91</td>
<td align="right">10.4%</td>
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
<td align="right">2,151,263,067</td>
<td align="right">2.7%</td>
<td align="right">2,154,411,403</td>
<td align="right">2.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">29,460,985,320</td>
<td align="right">37.5%</td>
<td align="right">29,483,168,195</td>
<td align="right">37.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">45,959,391,162</td>
<td align="right">58.5%</td>
<td align="right">45,990,683,116</td>
<td align="right">58.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">994,910,865</td>
<td align="right">1.3%</td>
<td align="right">994,880,797</td>
<td align="right">1.3%</td>
<td align="right">-0.0%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">321,491,008</td>
<td align="right">15.0%</td>
<td align="right">322,750,273</td>
<td align="right">15.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">537,271,633</td>
<td align="right">25.0%</td>
<td align="right">538,820,298</td>
<td align="right">25.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">86,095,499</td>
<td align="right">4.0%</td>
<td align="right">86,235,901</td>
<td align="right">4.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">118,977,892</td>
<td align="right">5.5%</td>
<td align="right">119,029,566</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">482,321,333</td>
<td align="right">22.5%</td>
<td align="right">482,382,938</td>
<td align="right">22.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">102,436,039</td>
<td align="right">4.8%</td>
<td align="right">102,447,905</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,570,061</td>
<td align="right">6.2%</td>
<td align="right">133,568,905</td>
<td align="right">6.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,347,251</td>
<td align="right">4.5%</td>
<td align="right">97,347,171</td>
<td align="right">4.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">69,747,998</td>
<td align="right">3.2%</td>
<td align="right">69,748,039</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,789</td>
<td align="right">6.0%</td>
<td align="right">128,815,789</td>
<td align="right">6.0%</td>
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
<td align="right">183,525,322</td>
<td align="right">18.4%</td>
<td align="right">183,758,589</td>
<td align="right">18.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,273,101</td>
<td align="right">9.5%</td>
<td align="right">94,156,101</td>
<td align="right">9.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,239,308</td>
<td align="right">2.1%</td>
<td align="right">21,251,099</td>
<td align="right">2.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">69,120,020</td>
<td align="right">6.9%</td>
<td align="right">69,111,303</td>
<td align="right">6.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">77,082,625</td>
<td align="right">7.7%</td>
<td align="right">77,091,207</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">21,566,888</td>
<td align="right">2.2%</td>
<td align="right">21,565,880</td>
<td align="right">2.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">75,809,785</td>
<td align="right">7.6%</td>
<td align="right">75,811,434</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">19,325,956</td>
<td align="right">1.9%</td>
<td align="right">19,326,207</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,872,726</td>
<td align="right">2.1%</td>
<td align="right">20,872,941</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">255,494,590</td>
<td align="right">25.7%</td>
<td align="right">255,494,765</td>
<td align="right">25.7%</td>
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
<td align="left">Frames pushed</td>
<td align="right">5,460,440,036</td>
<td align="right">81.6%</td>
<td align="right">5,465,000,498</td>
<td align="right">81.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">951,783,765</td>
<td align="right">14.2%</td>
<td align="right">952,566,022</td>
<td align="right">14.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">953,915,910</td>
<td align="right">14.3%</td>
<td align="right">954,698,167</td>
<td align="right">14.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,066,762,102</td>
<td align="right">75.7%</td>
<td align="right">5,070,540,203</td>
<td align="right">75.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,624,323,319</td>
<td align="right">24.3%</td>
<td align="right">1,625,107,579</td>
<td align="right">24.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,624,323,319</td>
<td align="right">24.3%</td>
<td align="right">1,625,107,579</td>
<td align="right">24.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,294,905</td>
<td align="right">4.2%</td>
<td align="right">279,397,938</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,407,328</td>
<td align="right">3.9%</td>
<td align="right">261,405,852</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,289</td>
<td align="right">0.4%</td>
<td align="right">24,922,393</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,407,409</td>
<td align="right">10.0%</td>
<td align="right">670,409,412</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,639,786</td>
<td align="right">1.1%</td>
<td align="right">71,639,842</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,249</td>
<td align="right">0.0%</td>
<td align="right">2,128,249</td>
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
<td align="left">Immortal decrefs</td>
<td align="right">55,130,875,659</td>
<td align="right">27.4%</td>
<td align="right">50,169,157,908</td>
<td align="right">25.5%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">8,907,505</td>
<td align="right"></td>
<td align="right">8,163,715</td>
<td align="right"></td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">7,179,666,452</td>
<td align="right">39.2%</td>
<td align="right">7,479,721,932</td>
<td align="right">40.8%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">7,257,607,593</td>
<td align="right">39.6%</td>
<td align="right">7,557,657,562</td>
<td align="right">41.3%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">7,848,447,931</td>
<td align="right"></td>
<td align="right">8,148,922,800</td>
<td align="right"></td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,050,483,487</td>
<td align="right">60.4%</td>
<td align="right">10,756,693,619</td>
<td align="right">58.7%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,050,559,872</td>
<td align="right"></td>
<td align="right">10,756,779,295</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">46,656,859,222</td>
<td align="right">23.2%</td>
<td align="right">47,385,466,605</td>
<td align="right">24.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">77,753,776,549</td>
<td align="right">48.1%</td>
<td align="right">78,671,188,817</td>
<td align="right">48.3%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">40,053,716,841</td>
<td align="right">24.8%</td>
<td align="right">40,363,157,153</td>
<td align="right">24.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">57,750,038</td>
<td align="right"></td>
<td align="right">58,151,003</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">65,848,793</td>
<td align="right"></td>
<td align="right">65,504,966</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">83,203,041,429</td>
<td align="right">41.4%</td>
<td align="right">83,419,107,730</td>
<td align="right">42.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,637,538</td>
<td align="right"></td>
<td align="right">180,000,656</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">8,717,267,933</td>
<td align="right">5.4%</td>
<td align="right">8,727,777,416</td>
<td align="right">5.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,899,592,889</td>
<td align="right"></td>
<td align="right">2,902,189,220</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">16,110,064,730</td>
<td align="right">8.0%</td>
<td align="right">16,123,928,701</td>
<td align="right">8.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,181,952,294</td>
<td align="right"></td>
<td align="right">2,183,481,241</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">35,104,368,355</td>
<td align="right">21.7%</td>
<td align="right">35,125,940,965</td>
<td align="right">21.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,520,653</td>
<td align="right">0.4%</td>
<td align="right">71,515,046</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,420,488</td>
<td align="right">0.0%</td>
<td align="right">6,420,584</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,166</td>
<td align="right">2.5%</td>
<td align="right">4,444,166</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">476,016</td>
<td align="right">0.3%</td>
<td align="right">476,016</td>
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
<td align="right">363,603</td>
<td align="right">103,077,426</td>
<td align="right">9,321,028,135</td>
<td align="right">731,630,541</td>
<td align="right">762,861,577</td>
<td align="right">363,623</td>
<td align="right">103,082,726</td>
<td align="right">9,321,554,470</td>
<td align="right">731,736,544</td>
<td align="right">762,851,712</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,605,576,484</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,605,575,980</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">267,069,711,492</td>
<td align="right">3,835.1%</td>
<td align="right">281,051,234,999</td>
<td align="right">4,035.5%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">290</td>
<td align="right">0.1%</td>
<td align="right">305</td>
<td align="right">0.1%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">2,624</td>
<td align="right">0.5%</td>
<td align="right">2,664</td>
<td align="right">0.5%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">972</td>
<td align="right">0.2%</td>
<td align="right">963</td>
<td align="right">0.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">900</td>
<td align="right">0.2%</td>
<td align="right">901</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">67,724</td>
<td align="right">13.6%</td>
<td align="right">67,787</td>
<td align="right">13.6%</td>
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
<td align="right">497,567</td>
<td align="right"></td>
<td align="right">497,619</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,963,761,158</td>
<td align="right"></td>
<td align="right">6,964,398,690</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">429,553</td>
<td align="right">86.3%</td>
<td align="right">429,527</td>
<td align="right">86.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">386,643</td>
<td align="right">77.7%</td>
<td align="right">386,654</td>
<td align="right">77.7%</td>
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
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">522</td>
<td align="right">0.8%</td>
<td align="right">522</td>
<td align="right">0.8%</td>
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
<td align="right">61,425</td>
<td align="right">90.7%</td>
<td align="right">61,528</td>
<td align="right">90.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">67,724</td>
<td align="right"></td>
<td align="right">67,787</td>
<td align="right"></td>
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
<td align="right">5,872</td>
<td align="right">8.7%</td>
<td align="right">5,877</td>
<td align="right">8.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,342</td>
<td align="right">12.3%</td>
<td align="right">8,361</td>
<td align="right">12.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">22,110</td>
<td align="right">32.6%</td>
<td align="right">21,943</td>
<td align="right">32.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">16,539</td>
<td align="right">24.4%</td>
<td align="right">16,535</td>
<td align="right">24.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">9,208</td>
<td align="right">13.6%</td>
<td align="right">9,321</td>
<td align="right">13.8%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,913</td>
<td align="right">7.3%</td>
<td align="right">5,001</td>
<td align="right">7.4%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">660</td>
<td align="right">1.0%</td>
<td align="right">669</td>
<td align="right">1.0%</td>
<td align="right">1.4%</td>
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
<td align="right">1,974</td>
<td align="right">2.9%</td>
<td align="right">1,972</td>
<td align="right">2.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">8,601</td>
<td align="right">12.7%</td>
<td align="right">8,631</td>
<td align="right">12.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">9,213</td>
<td align="right">13.6%</td>
<td align="right">8,925</td>
<td align="right">13.2%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">24,557</td>
<td align="right">36.3%</td>
<td align="right">24,461</td>
<td align="right">36.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">11,648</td>
<td align="right">17.2%</td>
<td align="right">11,722</td>
<td align="right">17.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,912</td>
<td align="right">5.8%</td>
<td align="right">3,991</td>
<td align="right">5.9%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,254</td>
<td align="right">1.9%</td>
<td align="right">1,560</td>
<td align="right">2.3%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">266</td>
<td align="right">0.4%</td>
<td align="right">266</td>
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
<td align="left">_POP_TOP</td>
<td align="right">1,887,935,525</td>
<td align="right">1,497,481,547</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">868,418</td>
<td align="right">1,000,617</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">4,592,042</td>
<td align="right">4,704,064</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">8,293,116</td>
<td align="right">8,491,538</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,628,886</td>
<td align="right">1,663,606</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">1,693,842</td>
<td align="right">1,728,562</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,652,969</td>
<td align="right">6,687,048</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">25,877,980</td>
<td align="right">26,005,860</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">21,262,401</td>
<td align="right">21,348,420</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,867,257,929</td>
<td align="right">8,892,290,529</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">92,196,399</td>
<td align="right">92,456,263</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">168,060,330</td>
<td align="right">168,469,960</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">56,569,579</td>
<td align="right">56,701,778</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">192,449,400</td>
<td align="right">192,868,193</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">71,997,379</td>
<td align="right">72,138,313</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">409,951,757</td>
<td align="right">410,573,436</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">166,955,752</td>
<td align="right">167,201,519</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">244,146,814</td>
<td align="right">244,505,651</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">150,792,369</td>
<td align="right">151,005,441</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,522,382</td>
<td align="right">117,684,102</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">383,604,780</td>
<td align="right">384,129,382</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">81,481,164</td>
<td align="right">81,591,453</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">137,892,764</td>
<td align="right">138,054,484</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">35,073</td>
<td align="right">35,113</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">484,477,496</td>
<td align="right">484,996,423</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">485,427,848</td>
<td align="right">485,946,775</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,175,898,098</td>
<td align="right">1,177,128,041</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">598,095,789</td>
<td align="right">598,720,544</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">305,855,586</td>
<td align="right">306,163,378</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">419,654,905</td>
<td align="right">419,253,357</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">170,696,494</td>
<td align="right">170,858,212</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">664,637,295</td>
<td align="right">665,246,291</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,240,854,268</td>
<td align="right">1,241,912,220</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,239,964,635</td>
<td align="right">1,241,017,707</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,154,093,921</td>
<td align="right">1,155,036,744</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">571,708,127</td>
<td align="right">572,166,699</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">786,477,602</td>
<td align="right">787,030,611</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">114,090,504</td>
<td align="right">114,167,111</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">4,972,941,298</td>
<td align="right">4,976,121,045</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,623,689,504</td>
<td align="right">1,624,654,501</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">790,589,466</td>
<td align="right">791,059,267</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">647,135,700</td>
<td align="right">647,478,851</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,427,883,343</td>
<td align="right">3,429,697,933</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">25,743,953,602</td>
<td align="right">25,756,815,371</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,866,104,927</td>
<td align="right">2,867,496,768</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">5,750,700,221</td>
<td align="right">5,753,481,039</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,469,738,923</td>
<td align="right">1,470,417,779</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">298,432,392</td>
<td align="right">298,569,814</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,180,898,517</td>
<td align="right">2,181,863,934</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">30,912,981,333</td>
<td align="right">30,926,622,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,834,988,812</td>
<td align="right">2,836,211,263</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">510,536,714</td>
<td align="right">510,753,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,558,644,275</td>
<td align="right">1,559,284,787</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">12,862,610</td>
<td align="right">12,867,768</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">618,234,670</td>
<td align="right">618,473,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">23,432,159</td>
<td align="right">23,441,215</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">361,210,601</td>
<td align="right">361,344,636</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">361,210,601</td>
<td align="right">361,344,636</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,430,055,172</td>
<td align="right">2,430,933,202</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,190,440,539</td>
<td align="right">1,190,858,950</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">103,394,036</td>
<td align="right">103,429,222</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">701,755,487</td>
<td align="right">701,992,291</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,932,206,579</td>
<td align="right">1,932,849,896</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">37,333,494</td>
<td align="right">37,345,463</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,588,409,209</td>
<td align="right">4,589,876,427</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">711,189,522</td>
<td align="right">711,410,953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,025,224,990</td>
<td align="right">1,025,541,074</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,404,084,801</td>
<td align="right">2,404,808,897</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,461,284,539</td>
<td align="right">2,462,008,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">494,554,145</td>
<td align="right">494,696,849</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,305,882,779</td>
<td align="right">8,308,272,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,355,632,431</td>
<td align="right">1,356,013,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,775,136,465</td>
<td align="right">2,775,900,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">309,286,498</td>
<td align="right">309,369,601</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,175,275,650</td>
<td align="right">3,176,076,086</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">208,965,257</td>
<td align="right">209,017,891</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,849,994,403</td>
<td align="right">1,850,435,894</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,838,000,269</td>
<td align="right">5,839,384,421</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">94,739,233</td>
<td align="right">94,761,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,074,294,647</td>
<td align="right">2,074,769,242</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">758,012,897</td>
<td align="right">758,185,349</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">155,438,711</td>
<td align="right">155,472,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,879,211,139</td>
<td align="right">1,879,608,712</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">961,323,019</td>
<td align="right">961,521,436</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">393,203,125</td>
<td align="right">393,282,807</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,174,101</td>
<td align="right">6,172,884</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">578,803,454</td>
<td align="right">578,915,881</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">578,803,454</td>
<td align="right">578,915,881</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,500,521</td>
<td align="right">47,509,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">173,778,606</td>
<td align="right">173,811,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">433,462,847</td>
<td align="right">433,380,979</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">557,454,166</td>
<td align="right">557,558,891</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,822,915,412</td>
<td align="right">1,823,251,412</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">246,810,670</td>
<td align="right">246,854,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,047,936,266</td>
<td align="right">1,048,111,899</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,393,816,330</td>
<td align="right">9,395,331,892</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,388,232,214</td>
<td align="right">1,388,444,583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,977,146,728</td>
<td align="right">4,976,400,488</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,034,078,960</td>
<td align="right">1,034,221,310</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">896,821,078</td>
<td align="right">896,944,497</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">545,483,668</td>
<td align="right">545,557,099</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">1,260,486</td>
<td align="right">1,260,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,949,449,147</td>
<td align="right">1,949,685,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,692,227,700</td>
<td align="right">1,692,427,429</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,185,958,549</td>
<td align="right">1,186,074,928</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,963,761,158</td>
<td align="right">6,964,398,690</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">801,985,298</td>
<td align="right">802,057,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,126,429,250</td>
<td align="right">2,126,620,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">513,118,474</td>
<td align="right">513,160,908</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,935,006,915</td>
<td align="right">1,935,161,315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,614,815,606</td>
<td align="right">4,615,181,826</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">361,316,861</td>
<td align="right">361,344,636</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">43,597,249</td>
<td align="right">43,600,589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">5,988,315,043</td>
<td align="right">5,988,748,846</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">654,421,387</td>
<td align="right">654,462,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">78,198,994</td>
<td align="right">78,203,834</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,817,116,374</td>
<td align="right">3,817,350,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">79,472,278</td>
<td align="right">79,477,118</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,926,651,095</td>
<td align="right">2,926,826,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">20,532,473</td>
<td align="right">20,531,257</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,137,996,512</td>
<td align="right">4,138,225,571</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">753,785,711</td>
<td align="right">753,824,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">724,975,946</td>
<td align="right">725,010,074</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">431,209,390</td>
<td align="right">431,224,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,521,705,010</td>
<td align="right">2,521,790,366</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,333,063,003</td>
<td align="right">9,333,341,608</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">97,914,429</td>
<td align="right">97,911,516</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">97,914,429</td>
<td align="right">97,911,516</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,220,544,979</td>
<td align="right">1,220,579,058</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,352,104,890</td>
<td align="right">1,352,139,018</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">312,322,543</td>
<td align="right">312,330,314</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,871,573,380</td>
<td align="right">1,871,527,095</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">722,115,888</td>
<td align="right">722,100,501</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,219,363,050</td>
<td align="right">4,219,444,842</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,087,178,608</td>
<td align="right">1,087,193,263</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">293,916,475</td>
<td align="right">293,913,026</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">297,240,445</td>
<td align="right">297,236,996</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">40,380,044</td>
<td align="right">40,380,464</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">791,184,893</td>
<td align="right">791,190,818</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">87,850,849</td>
<td align="right">87,851,233</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,662,756</td>
<td align="right">91,663,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">671,347,023</td>
<td align="right">671,344,414</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,422,360</td>
<td align="right">40,422,456</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">25,585,269</td>
<td align="right">25,585,329</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">25,585,269</td>
<td align="right">25,585,329</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">567,310,141</td>
<td align="right">567,311,449</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">31,512,200</td>
<td align="right">31,512,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">29,953,171</td>
<td align="right">29,953,211</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">29,953,171</td>
<td align="right">29,953,211</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">18,020,013</td>
<td align="right">18,019,990</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">84,011,221</td>
<td align="right">84,011,301</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,202,669</td>
<td align="right">3,202,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">48,341,155</td>
<td align="right">48,341,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,037,314,183</td>
<td align="right">3,037,314,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">991,855,948</td>
<td align="right">991,856,068</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">57,107,331</td>
<td align="right">57,107,337</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,278,330,588</td>
<td align="right">4,278,331,030</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,562,624,634</td>
<td align="right">1,562,624,491</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,371,390,207</td>
<td align="right">1,371,390,267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">71,268,747</td>
<td align="right">71,268,745</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">71,268,747</td>
<td align="right">71,268,745</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">285,437,870</td>
<td align="right">285,437,877</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">215,056,044</td>
<td align="right">215,056,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">221,231,549</td>
<td align="right">221,231,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">862,055,348</td>
<td align="right">862,055,348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">504,193,484</td>
<td align="right">504,193,484</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">500,430,593</td>
<td align="right">500,430,593</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">446,210,616</td>
<td align="right">446,210,616</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">386,839,379</td>
<td align="right">386,839,379</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">335,843,151</td>
<td align="right">335,843,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">273,054,037</td>
<td align="right">273,054,037</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">217,385,693</td>
<td align="right">217,385,693</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">195,739,285</td>
<td align="right">195,739,285</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">194,370,682</td>
<td align="right">194,370,682</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">178,299,174</td>
<td align="right">178,299,174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">123,515,060</td>
<td align="right">123,515,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">114,400,018</td>
<td align="right">114,400,018</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,492,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">97,102,470</td>
<td align="right">97,102,470</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">94,611,486</td>
<td align="right">94,611,486</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">78,389,206</td>
<td align="right">78,389,206</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">62,848,645</td>
<td align="right">62,848,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,278,080</td>
<td align="right">60,278,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">53,743,510</td>
<td align="right">53,743,510</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">52,084,740</td>
<td align="right">52,084,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">50,223,440</td>
<td align="right">50,223,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">50,223,440</td>
<td align="right">50,223,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">48,638,840</td>
<td align="right">48,638,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,062,820</td>
<td align="right">47,062,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">40,381,144</td>
<td align="right">40,381,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,304,301</td>
<td align="right">40,304,301</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">40,020,812</td>
<td align="right">40,020,812</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">38,540,043</td>
<td align="right">38,540,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">36,489,101</td>
<td align="right">36,489,101</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">35,389,641</td>
<td align="right">35,389,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">31,155,920</td>
<td align="right">31,155,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">30,183,358</td>
<td align="right">30,183,358</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">29,419,325</td>
<td align="right">29,419,325</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,262,336</td>
<td align="right">24,262,336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">15,564,716</td>
<td align="right">15,564,716</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">13,165,084</td>
<td align="right">13,165,084</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">10,763,905</td>
<td align="right">10,763,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">10,763,905</td>
<td align="right">10,763,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,818,343</td>
<td align="right">6,818,343</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,532,837</td>
<td align="right">6,532,837</td>
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
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right">3,840,960</td>
<td align="right">3,840,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,579,420</td>
<td align="right">3,579,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">3,106,020</td>
<td align="right">3,106,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,093,927</td>
<td align="right">3,093,927</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">2,615,370</td>
<td align="right">2,615,370</td>
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
<td align="left">_MAKE_CELL</td>
<td align="right">493,053</td>
<td align="right">493,053</td>
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
<tr>
<td align="left">_POP_UNDER_INT</td>
<td align="right"></td>
<td align="right">5,125,556,393</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_UNDER_IMMORTAL</td>
<td align="right"></td>
<td align="right">4,602,525,665</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_UNDER_FLOAT</td>
<td align="right"></td>
<td align="right">3,169,999,504</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_UNDER</td>
<td align="right"></td>
<td align="right">929,046,501</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_IMMORTAL</td>
<td align="right"></td>
<td align="right">374,411,569</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_UNDER_UNICODE</td>
<td align="right"></td>
<td align="right">54,805,641</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_INT</td>
<td align="right"></td>
<td align="right">17,152,421</td>
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
<td align="left">CALL</td>
<td align="right">7,307</td>
<td align="right">7,292</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">24,576</td>
<td align="right">24,599</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,425</td>
<td align="right">23,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">84</td>
<td align="right">84</td>
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
Stats gathered on: 2025-01-15
