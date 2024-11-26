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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,434,751</td>
<td align="right">9,343,963</td>
<td align="right">551.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,456</td>
<td align="right">9,075</td>
<td align="right">523.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">4</td>
<td align="right">8</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">225,004</td>
<td align="right">4</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">108,000</td>
<td align="right">2</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">153,180</td>
<td align="right">3</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">245,160</td>
<td align="right">5</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">45,120</td>
<td align="right">120</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">45,120</td>
<td align="right">120</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">402,520</td>
<td align="right">1,153</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">271,737</td>
<td align="right">880</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">18,060</td>
<td align="right">60</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9,240</td>
<td align="right">200</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">236,927</td>
<td align="right">9,802</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">12,659,026</td>
<td align="right">528,864</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">257,959</td>
<td align="right">11,011</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">568,653</td>
<td align="right">27,192</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,239,372</td>
<td align="right">116,648</td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">542,138</td>
<td align="right">54,573</td>
<td align="right">-89.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,475,031</td>
<td align="right">163,518</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">223,837</td>
<td align="right">36,301</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">504,900</td>
<td align="right">90,548</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">138,206</td>
<td align="right">28,217</td>
<td align="right">-79.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,836,926</td>
<td align="right">998,232</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">423,372</td>
<td align="right">89,794</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,891,416</td>
<td align="right">425,572</td>
<td align="right">-77.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,695,342</td>
<td align="right">606,679</td>
<td align="right">-77.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,889,269</td>
<td align="right">688,605</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">559,320</td>
<td align="right">135,965</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">390,184</td>
<td align="right">95,768</td>
<td align="right">-75.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">36,000</td>
<td align="right">9,000</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">591,565</td>
<td align="right">155,072</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,490,796</td>
<td align="right">928,221</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">694,307</td>
<td align="right">190,506</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,092,088</td>
<td align="right">587,259</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">37,878</td>
<td align="right">10,806</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">221,387</td>
<td align="right">64,502</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">90,064</td>
<td align="right">26,468</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,906,361</td>
<td align="right">572,381</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">90,060</td>
<td align="right">27,061</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">29,404</td>
<td align="right">9,001</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">143,700</td>
<td align="right">45,181</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">16,944,409</td>
<td align="right">5,503,416</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">82,328</td>
<td align="right">27,436</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">54,060</td>
<td align="right">18,060</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,673,802</td>
<td align="right">895,122</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">39,949</td>
<td align="right">13,553</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,675,189</td>
<td align="right">571,505</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,480,579</td>
<td align="right">2,216,514</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,275,286</td>
<td align="right">783,758</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">631,275</td>
<td align="right">225,187</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,192,631</td>
<td align="right">429,931</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,004,812</td>
<td align="right">17,521,545</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">391,543</td>
<td align="right">144,597</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">72,008</td>
<td align="right">27,017</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">596,134</td>
<td align="right">227,444</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,339,732</td>
<td align="right">2,803,880</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">115,710</td>
<td align="right">44,463</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">160,594</td>
<td align="right">62,349</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">585,170</td>
<td align="right">233,352</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">45,180</td>
<td align="right">18,162</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">579,283</td>
<td align="right">238,227</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">486,218</td>
<td align="right">205,141</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">64,080</td>
<td align="right">27,180</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,266,566</td>
<td align="right">977,381</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">63,360</td>
<td align="right">27,360</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">146,922</td>
<td align="right">64,142</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,372,402</td>
<td align="right">621,473</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">353,084</td>
<td align="right">162,304</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">687,933</td>
<td align="right">330,924</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">568,582</td>
<td align="right">273,676</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">593,588</td>
<td align="right">288,187</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">9,258,487</td>
<td align="right">4,555,904</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,561,224</td>
<td align="right">3,293,041</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">7,407,314</td>
<td align="right">3,744,555</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,761,096</td>
<td align="right">2,410,341</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">534,372</td>
<td align="right">270,958</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,136,253</td>
<td align="right">1,088,507</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,690,684</td>
<td align="right">2,919,556</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,424,164</td>
<td align="right">5,470,174</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,295,460</td>
<td align="right">691,602</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,112,108</td>
<td align="right">3,916,344</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">442,272</td>
<td align="right">243,658</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">875,673</td>
<td align="right">500,162</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">45,120</td>
<td align="right">27,060</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">350,224</td>
<td align="right">215,776</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">193,384</td>
<td align="right">119,850</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">994,525</td>
<td align="right">630,725</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">800,607</td>
<td align="right">511,479</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">223,564</td>
<td align="right">143,102</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">207,420</td>
<td align="right">135,364</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">162,406</td>
<td align="right">106,202</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,006,203</td>
<td align="right">1,337,496</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">243,312</td>
<td align="right">162,326</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">81,360</td>
<td align="right">54,360</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">199,325</td>
<td align="right">138,300</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">115,842</td>
<td align="right">80,543</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">478,701</td>
<td align="right">338,367</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">214,564</td>
<td align="right">152,102</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">128,547</td>
<td align="right">91,509</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">126,180</td>
<td align="right">90,180</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">289,840</td>
<td align="right">208,761</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">189,180</td>
<td align="right">153,180</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,421</td>
<td align="right">13,493</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">270,061</td>
<td align="right">225,062</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63,957</td>
<td align="right">54,225</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">252,060</td>
<td align="right">216,060</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">63,464</td>
<td align="right">54,428</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">660,395</td>
<td align="right">566,567</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">135,061</td>
<td align="right">153,060</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">298,817</td>
<td align="right">259,262</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,683,524</td>
<td align="right">6,231,477</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">21,904</td>
<td align="right">20,430</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">146,223</td>
<td align="right">137,551</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,622,696</td>
<td align="right">5,779,886</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,491,886</td>
<td align="right">8,552,190</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">142,530</td>
<td align="right">143,279</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">336,124</td>
<td align="right">337,465</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">343,653</td>
<td align="right">344,797</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">343,649</td>
<td align="right">344,789</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,350</td>
<td align="right">2,344</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">813,049</td>
<td align="right">814,589</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">3,905,350</td>
<td align="right">3,909,450</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">12,090</td>
<td align="right">12,084</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">90,440</td>
<td align="right">90,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">9,045</td>
<td align="right">9,044</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">91,056</td>
<td align="right">91,050</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">252,312</td>
<td align="right">252,324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">432,000</td>
<td align="right">432,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">342,000</td>
<td align="right">342,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">333,000</td>
<td align="right">333,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">252,400</td>
<td align="right">252,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">216,000</td>
<td align="right">216,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">171,060</td>
<td align="right">171,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">54,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">54,000</td>
<td align="right">54,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">45,000</td>
<td align="right">45,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">45,000</td>
<td align="right">45,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">26,460</td>
<td align="right">26,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">18,000</td>
<td align="right">18,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">18,000</td>
<td align="right">18,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">9,000</td>
<td align="right">9,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">9,000</td>
<td align="right">9,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">9,000</td>
<td align="right">9,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">9,000</td>
<td align="right">9,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">9,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">60</td>
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
<td align="right">658,731</td>
<td align="right">26.7%</td>
<td align="right">565,258</td>
<td align="right">23.8%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,810,031</td>
<td align="right">73.3%</td>
<td align="right">1,810,539</td>
<td align="right">76.2%</td>
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
<td align="right">1,544</td>
<td align="right">92.8%</td>
<td align="right">1,189</td>
<td align="right">90.8%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">7.2%</td>
<td align="right">120</td>
<td align="right">9.2%</td>
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
<td align="left">remainder</td>
<td align="right">200</td>
<td align="right">13.0%</td>
<td align="right">40</td>
<td align="right">3.4%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">131</td>
<td align="right">8.5%</td>
<td align="right">71</td>
<td align="right">6.0%</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">259</td>
<td align="right">16.8%</td>
<td align="right">200</td>
<td align="right">16.8%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">180</td>
<td align="right">11.7%</td>
<td align="right">220</td>
<td align="right">18.5%</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">712</td>
<td align="right">46.1%</td>
<td align="right">596</td>
<td align="right">50.1%</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">40</td>
<td align="right">2.6%</td>
<td align="right">40</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">22</td>
<td align="right">1.4%</td>
<td align="right">22</td>
<td align="right">1.9%</td>
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
<td align="right">223,837</td>
<td align="right">100.0%</td>
<td align="right">36,301</td>
<td align="right">100.0%</td>
<td align="right">-83.8%</td>
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
<td align="right">235,850</td>
<td align="right">15.3%</td>
<td align="right">9,322</td>
<td align="right">0.7%</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,306,284</td>
<td align="right">84.6%</td>
<td align="right">1,306,422</td>
<td align="right">99.3%</td>
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
<td align="right">737</td>
<td align="right">68.4%</td>
<td align="right">140</td>
<td align="right">29.2%</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">340</td>
<td align="right">31.6%</td>
<td align="right">340</td>
<td align="right">70.8%</td>
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
<td align="right">557</td>
<td align="right">75.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">60</td>
<td align="right">8.1%</td>
<td align="right">60</td>
<td align="right">42.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">5.4%</td>
<td align="right">40</td>
<td align="right">28.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">40</td>
<td align="right">5.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">40</td>
<td align="right">5.4%</td>
<td align="right">40</td>
<td align="right">28.6%</td>
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
<td align="right">191,177</td>
<td align="right">1.1%</td>
<td align="right">139,871</td>
<td align="right">0.8%</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,653,223</td>
<td align="right">98.9%</td>
<td align="right">17,721,819</td>
<td align="right">99.1%</td>
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
<td align="right">9,030</td>
<td align="right">0.1%</td>
<td align="right">9,024</td>
<td align="right">0.1%</td>
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
<td align="right">6,796</td>
<td align="right">99.4%</td>
<td align="right">5,823</td>
<td align="right">99.3%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.7%</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">20</td>
<td align="right">50.0%</td>
<td align="right">20</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">20</td>
<td align="right">50.0%</td>
<td align="right">20</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW

<details>
<summary> specialization stats for CALL_KW family </summary>


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
<td align="right">127,872</td>
<td align="right">3.9%</td>
<td align="right">91,014</td>
<td align="right">2.8%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">116</td>
<td align="right">0.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,116,482</td>
<td align="right">96.0%</td>
<td align="right">3,116,782</td>
<td align="right">97.1%</td>
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
<td align="right">495</td>
<td align="right">73.3%</td>
<td align="right">315</td>
<td align="right">63.6%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">180</td>
<td align="right">26.7%</td>
<td align="right">180</td>
<td align="right">36.4%</td>
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
<td align="right">100</td>
<td align="right">20.2%</td>
<td align="right">20</td>
<td align="right">6.3%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">120</td>
<td align="right">24.2%</td>
<td align="right">80</td>
<td align="right">25.4%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">95</td>
<td align="right">19.2%</td>
<td align="right">75</td>
<td align="right">23.8%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">80</td>
<td align="right">16.2%</td>
<td align="right">80</td>
<td align="right">25.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">40</td>
<td align="right">8.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">40</td>
<td align="right">8.1%</td>
<td align="right">40</td>
<td align="right">12.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">20</td>
<td align="right">4.0%</td>
<td align="right">20</td>
<td align="right">6.3%</td>
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
<td align="right">288,780</td>
<td align="right">58.1%</td>
<td align="right">207,781</td>
<td align="right">49.9%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">207,540</td>
<td align="right">41.7%</td>
<td align="right">207,540</td>
<td align="right">49.9%</td>
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
<td align="right">1,020</td>
<td align="right">96.2%</td>
<td align="right">940</td>
<td align="right">95.9%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">40</td>
<td align="right">3.8%</td>
<td align="right">40</td>
<td align="right">4.1%</td>
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
<td align="right">220</td>
<td align="right">21.6%</td>
<td align="right">180</td>
<td align="right">19.1%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">600</td>
<td align="right">58.8%</td>
<td align="right">560</td>
<td align="right">59.6%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">200</td>
<td align="right">19.6%</td>
<td align="right">200</td>
<td align="right">21.3%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">146,351</td>
<td align="right">22.8%</td>
<td align="right">63,822</td>
<td align="right">17.1%</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">495,471</td>
<td align="right">77.1%</td>
<td align="right">310,094</td>
<td align="right">82.9%</td>
<td align="right">-37.4%</td>
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
<td align="right">571</td>
<td align="right">100.0%</td>
<td align="right">320</td>
<td align="right">100.0%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">320</td>
<td align="right">56.0%</td>
<td align="right">260</td>
<td align="right">81.2%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">60</td>
<td align="right">10.5%</td>
<td align="right">60</td>
<td align="right">18.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">7.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">40</td>
<td align="right">7.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">40</td>
<td align="right">7.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">40</td>
<td align="right">7.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">31</td>
<td align="right">5.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">344,398</td>
<td align="right">0.8%</td>
<td align="right">28,476</td>
<td align="right">0.1%</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,988,794</td>
<td align="right">4.8%</td>
<td align="right">1,324,136</td>
<td align="right">3.3%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">39,454,040</td>
<td align="right">94.4%</td>
<td align="right">38,518,167</td>
<td align="right">96.6%</td>
<td align="right">-2.4%</td>
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
<td align="right">18,986</td>
<td align="right">79.5%</td>
<td align="right">10,066</td>
<td align="right">72.5%</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,909</td>
<td align="right">20.5%</td>
<td align="right">3,820</td>
<td align="right">27.5%</td>
<td align="right">-22.2%</td>
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
<td align="left">module attr not found</td>
<td align="right">320</td>
<td align="right">6.5%</td>
<td align="right">160</td>
<td align="right">4.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">360</td>
<td align="right">7.3%</td>
<td align="right">200</td>
<td align="right">5.2%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">140</td>
<td align="right">2.9%</td>
<td align="right">100</td>
<td align="right">2.6%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,938</td>
<td align="right">39.5%</td>
<td align="right">1,480</td>
<td align="right">38.7%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,671</td>
<td align="right">34.0%</td>
<td align="right">1,460</td>
<td align="right">38.2%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">220</td>
<td align="right">4.5%</td>
<td align="right">220</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">60</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">60</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">20</td>
<td align="right">0.4%</td>
<td align="right">20</td>
<td align="right">0.5%</td>
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
<td align="right">12,175,818</td>
<td align="right">100.0%</td>
<td align="right">3,864,331</td>
<td align="right">99.9%</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">840</td>
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
<td align="right">2,320</td>
<td align="right">100.0%</td>
<td align="right">2,320</td>
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
<td align="right">233,760</td>
<td align="right">100.0%</td>
<td align="right">233,760</td>
<td align="right">100.0%</td>
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
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">60</td>
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
<td align="right">252,000</td>
<td align="right">53.8%</td>
<td align="right">252,000</td>
<td align="right">53.8%</td>
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
<td align="right">216,000</td>
<td align="right">46.1%</td>
<td align="right">216,000</td>
<td align="right">46.1%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">400</td>
<td align="right">100.0%</td>
<td align="right">400</td>
<td align="right">100.0%</td>
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
<td align="right">400</td>
<td align="right">100.0%</td>
<td align="right">400</td>
<td align="right">100.0%</td>
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
<td align="right">387,424</td>
<td align="right">4.2%</td>
<td align="right">94,248</td>
<td align="right">1.1%</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">515,370</td>
<td align="right">5.6%</td>
<td align="right">125,395</td>
<td align="right">1.4%</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,216,758</td>
<td align="right">90.1%</td>
<td align="right">8,604,199</td>
<td align="right">97.5%</td>
<td align="right">4.7%</td>
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
<td align="right">10,653</td>
<td align="right">85.4%</td>
<td align="right">3,314</td>
<td align="right">85.1%</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,820</td>
<td align="right">14.6%</td>
<td align="right">580</td>
<td align="right">14.9%</td>
<td align="right">-68.1%</td>
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
<td align="right">1,000</td>
<td align="right">54.9%</td>
<td align="right">80</td>
<td align="right">13.8%</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">120</td>
<td align="right">6.6%</td>
<td align="right">40</td>
<td align="right">6.9%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">80</td>
<td align="right">4.4%</td>
<td align="right">40</td>
<td align="right">6.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">420</td>
<td align="right">23.1%</td>
<td align="right">260</td>
<td align="right">44.8%</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">120</td>
<td align="right">6.6%</td>
<td align="right">120</td>
<td align="right">20.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">40</td>
<td align="right">2.2%</td>
<td align="right">40</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">40</td>
<td align="right">2.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">63,064</td>
<td align="right">13.0%</td>
<td align="right">54,068</td>
<td align="right">11.3%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">423,492</td>
<td align="right">87.0%</td>
<td align="right">423,504</td>
<td align="right">88.6%</td>
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
<td align="right">300</td>
<td align="right">75.0%</td>
<td align="right">260</td>
<td align="right">72.2%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">100</td>
<td align="right">25.0%</td>
<td align="right">100</td>
<td align="right">27.8%</td>
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
<td align="left">py simple</td>
<td align="right">220</td>
<td align="right">73.3%</td>
<td align="right">180</td>
<td align="right">69.2%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">80</td>
<td align="right">26.7%</td>
<td align="right">80</td>
<td align="right">30.8%</td>
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
<td align="right">8,767</td>
<td align="right">0.1%</td>
<td align="right">16,704</td>
<td align="right">0.2%</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">577,477</td>
<td align="right">5.8%</td>
<td align="right">236,370</td>
<td align="right">2.5%</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,351,333</td>
<td align="right">94.1%</td>
<td align="right">9,212,282</td>
<td align="right">97.3%</td>
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
<td align="left">Success</td>
<td align="right">1,066</td>
<td align="right">54.1%</td>
<td align="right">1,215</td>
<td align="right">55.5%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">906</td>
<td align="right">45.9%</td>
<td align="right">976</td>
<td align="right">44.5%</td>
<td align="right">7.7%</td>
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
<td align="right">83</td>
<td align="right">9.2%</td>
<td align="right">518</td>
<td align="right">53.1%</td>
<td align="right">524.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">140</td>
<td align="right">15.5%</td>
<td align="right">60</td>
<td align="right">6.1%</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">244</td>
<td align="right">26.9%</td>
<td align="right">118</td>
<td align="right">12.1%</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">80</td>
<td align="right">8.8%</td>
<td align="right">40</td>
<td align="right">4.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">240</td>
<td align="right">26.5%</td>
<td align="right">240</td>
<td align="right">24.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">79</td>
<td align="right">8.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">40</td>
<td align="right">4.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">884,545</td>
<td align="right">99.0%</td>
<td align="right">885,912</td>
<td align="right">100.0%</td>
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
<td align="right">9,000</td>
<td align="right">1.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">40</td>
<td align="right">16.7%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">200</td>
<td align="right">83.3%</td>
<td align="right">200</td>
<td align="right">100.0%</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">1,060,767</td>
<td align="right">0.5%</td>
<td align="right">311,594</td>
<td align="right">0.3%</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">95,206,703</td>
<td align="right">40.5%</td>
<td align="right">31,972,009</td>
<td align="right">27.7%</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">5,001,882</td>
<td align="right">2.1%</td>
<td align="right">2,970,229</td>
<td align="right">2.6%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">133,852,965</td>
<td align="right">56.9%</td>
<td align="right">80,224,184</td>
<td align="right">69.5%</td>
<td align="right">-40.1%</td>
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
<td align="left">BINARY_SLICE</td>
<td align="right">223,837</td>
<td align="right">4.5%</td>
<td align="right">36,301</td>
<td align="right">1.2%</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">387,424</td>
<td align="right">7.8%</td>
<td align="right">94,248</td>
<td align="right">3.2%</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">577,477</td>
<td align="right">11.6%</td>
<td align="right">236,370</td>
<td align="right">8.0%</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">146,351</td>
<td align="right">2.9%</td>
<td align="right">63,822</td>
<td align="right">2.2%</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,988,794</td>
<td align="right">40.0%</td>
<td align="right">1,324,136</td>
<td align="right">45.0%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">127,872</td>
<td align="right">2.6%</td>
<td align="right">91,014</td>
<td align="right">3.1%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">288,780</td>
<td align="right">5.8%</td>
<td align="right">207,781</td>
<td align="right">7.1%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">658,731</td>
<td align="right">13.3%</td>
<td align="right">565,258</td>
<td align="right">19.2%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">252,000</td>
<td align="right">5.1%</td>
<td align="right">252,000</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">235,850</td>
<td align="right">4.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">54,068</td>
<td align="right">1.8%</td>
<td align="right"></td>
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
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">17,791</td>
<td align="right">1.7%</td>
<td align="right">917</td>
<td align="right">0.3%</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">515,370</td>
<td align="right">48.6%</td>
<td align="right">125,395</td>
<td align="right">40.2%</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">47,758</td>
<td align="right">4.5%</td>
<td align="right">17,369</td>
<td align="right">5.6%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">31,065</td>
<td align="right">2.9%</td>
<td align="right">17,415</td>
<td align="right">5.6%</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,189</td>
<td align="right">1.1%</td>
<td align="right">10,695</td>
<td align="right">3.4%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">93,727</td>
<td align="right">8.8%</td>
<td align="right">93,925</td>
<td align="right">30.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">182,529</td>
<td align="right">17.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">95,400</td>
<td align="right">9.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">27,660</td>
<td align="right">2.6%</td>
<td align="right">27,660</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">22,855</td>
<td align="right">2.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">12,215</td>
<td align="right">3.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">4,429</td>
<td align="right">1.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">480</td>
<td align="right">0.2%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">814,067</td>
<td align="right">5.3%</td>
<td align="right">815,852</td>
<td align="right">5.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">3,653,354</td>
<td align="right">23.9%</td>
<td align="right">3,657,458</td>
<td align="right">23.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">3,653,354</td>
<td align="right">23.9%</td>
<td align="right">3,657,458</td>
<td align="right">23.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">3,914,414</td>
<td align="right">25.6%</td>
<td align="right">3,918,518</td>
<td align="right">25.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">3,914,414</td>
<td align="right">25.6%</td>
<td align="right">3,918,518</td>
<td align="right">25.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">562,591</td>
<td align="right">3.7%</td>
<td align="right">563,180</td>
<td align="right">3.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">659,764</td>
<td align="right">4.3%</td>
<td align="right">660,148</td>
<td align="right">4.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">14,847,307</td>
<td align="right">97.2%</td>
<td align="right">14,855,827</td>
<td align="right">97.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">11,364,641</td>
<td align="right">74.4%</td>
<td align="right">11,369,045</td>
<td align="right">74.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">99,184</td>
<td align="right">0.6%</td>
<td align="right">99,188</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">261,060</td>
<td align="right">1.7%</td>
<td align="right">261,060</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">126,360</td>
<td align="right">0.8%</td>
<td align="right">126,360</td>
<td align="right">0.8%</td>
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
<td align="left">Mortal increfs</td>
<td align="right">63,969,426</td>
<td align="right">25.2%</td>
<td align="right">137,602,699</td>
<td align="right">51.5%</td>
<td align="right">115.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">68,723,420</td>
<td align="right">25.5%</td>
<td align="right">126,293,846</td>
<td align="right">42.6%</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">34,431,386</td>
<td align="right">12.8%</td>
<td align="right">52,264,173</td>
<td align="right">17.6%</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">38,834,726</td>
<td align="right">15.3%</td>
<td align="right">20,363,878</td>
<td align="right">7.6%</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">118,180,680</td>
<td align="right">46.5%</td>
<td align="right">64,722,326</td>
<td align="right">24.2%</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">397,747</td>
<td align="right"></td>
<td align="right">243,938</td>
<td align="right"></td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">414,460</td>
<td align="right"></td>
<td align="right">254,243</td>
<td align="right"></td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">17,379</td>
<td align="right"></td>
<td align="right">10,990</td>
<td align="right"></td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">33,038,973</td>
<td align="right">13.0%</td>
<td align="right">44,532,872</td>
<td align="right">16.7%</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">33,376,143</td>
<td align="right">12.4%</td>
<td align="right">22,662,933</td>
<td align="right">7.6%</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">132,681,423</td>
<td align="right">49.3%</td>
<td align="right">95,295,376</td>
<td align="right">32.1%</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">5,606,644</td>
<td align="right"></td>
<td align="right">5,101,866</td>
<td align="right"></td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,928,054</td>
<td align="right"></td>
<td align="right">4,785,981</td>
<td align="right"></td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">57,467</td>
<td align="right">0.3%</td>
<td align="right">58,106</td>
<td align="right">0.3%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,768,366</td>
<td align="right">42.0%</td>
<td align="right">8,785,873</td>
<td align="right">42.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,786,375</td>
<td align="right"></td>
<td align="right">8,803,832</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">174,640</td>
<td align="right">0.8%</td>
<td align="right">174,966</td>
<td align="right">0.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,854,189</td>
<td align="right">56.8%</td>
<td align="right">11,849,256</td>
<td align="right">56.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">12,329,866</td>
<td align="right"></td>
<td align="right">12,324,778</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,086,296</td>
<td align="right">58.0%</td>
<td align="right">12,082,328</td>
<td align="right">57.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">792,856</td>
<td align="right"></td>
<td align="right">792,872</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">9,000</td>
<td align="right">1.1%</td>
<td align="right">9,000</td>
<td align="right">1.1%</td>
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
<td align="right">120</td>
<td align="right">0</td>
<td align="right">2,873,620</td>
<td align="right">120</td>
<td align="right">0</td>
<td align="right">2,820,328</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
<td align="right">3,367,521</td>
<td align="right"></td>
<td align="right">18,208,945</td>
<td align="right"></td>
<td align="right">440.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,521</td>
<td align="right">78.7%</td>
<td align="right">7,884</td>
<td align="right">85.4%</td>
<td align="right">418.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,544</td>
<td align="right">79.9%</td>
<td align="right">7,626</td>
<td align="right">82.6%</td>
<td align="right">393.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,933</td>
<td align="right"></td>
<td align="right">9,237</td>
<td align="right"></td>
<td align="right">377.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">107,691,236</td>
<td align="right">3,197.9%</td>
<td align="right">380,677,896</td>
<td align="right">2,090.6%</td>
<td align="right">253.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">412</td>
<td align="right">21.3%</td>
<td align="right">1,353</td>
<td align="right">14.6%</td>
<td align="right">228.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">10</td>
<td align="right">0.5%</td>
<td align="right">6</td>
<td align="right">0.1%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">41</td>
<td align="right">0.4%</td>
<td align="right">41 / 0 !!</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
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
<td align="right">412</td>
<td align="right"></td>
<td align="right">1,353</td>
<td align="right"></td>
<td align="right">228.4%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">412</td>
<td align="right">100.0%</td>
<td align="right">1,333</td>
<td align="right">98.5%</td>
<td align="right">223.5%</td>
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
<td align="right">20</td>
<td align="right">1.5%</td>
<td align="right">20 / 0 !!</td>
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
<td align="right">80</td>
<td align="right">19.4%</td>
<td align="right">78</td>
<td align="right">5.8%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">31</td>
<td align="right">7.5%</td>
<td align="right">162</td>
<td align="right">12.0%</td>
<td align="right">422.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">131</td>
<td align="right">31.8%</td>
<td align="right">610</td>
<td align="right">45.1%</td>
<td align="right">365.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">146</td>
<td align="right">35.4%</td>
<td align="right">308</td>
<td align="right">22.8%</td>
<td align="right">111.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4</td>
<td align="right">1.0%</td>
<td align="right">134</td>
<td align="right">9.9%</td>
<td align="right">3,250.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">20</td>
<td align="right">4.9%</td>
<td align="right">61</td>
<td align="right">4.5%</td>
<td align="right">205.0%</td>
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
<td align="right">40</td>
<td align="right">9.7%</td>
<td align="right">59</td>
<td align="right">4.4%</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">60</td>
<td align="right">14.6%</td>
<td align="right">161</td>
<td align="right">11.9%</td>
<td align="right">168.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">63</td>
<td align="right">15.3%</td>
<td align="right">366</td>
<td align="right">27.1%</td>
<td align="right">481.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">192</td>
<td align="right">46.6%</td>
<td align="right">422</td>
<td align="right">31.2%</td>
<td align="right">119.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">36</td>
<td align="right">8.7%</td>
<td align="right">204</td>
<td align="right">15.1%</td>
<td align="right">466.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21</td>
<td align="right">5.1%</td>
<td align="right">60</td>
<td align="right">4.4%</td>
<td align="right">185.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">61</td>
<td align="right">4.5%</td>
<td align="right"></td>
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
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">18</td>
<td align="right">257,723</td>
<td align="right">1,431,694.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">60</td>
<td align="right">293,240</td>
<td align="right">488,633.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">18</td>
<td align="right">36,119</td>
<td align="right">200,561.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">18</td>
<td align="right">18,117</td>
<td align="right">100,550.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">18</td>
<td align="right">9,000</td>
<td align="right">49,900.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">9,000</td>
<td align="right">884,871</td>
<td align="right">9,731.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">9,000</td>
<td align="right">558,532</td>
<td align="right">6,105.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">42,839</td>
<td align="right">2,126,851</td>
<td align="right">4,864.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">4,256</td>
<td align="right">196,574</td>
<td align="right">4,518.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">6,703</td>
<td align="right">255,449</td>
<td align="right">3,711.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">9,060</td>
<td align="right">314,469</td>
<td align="right">3,371.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">36,720</td>
<td align="right">1,159,456</td>
<td align="right">3,057.6%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">18,022</td>
<td align="right">307,127</td>
<td align="right">1,604.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,000</td>
<td align="right">143,452</td>
<td align="right">1,493.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,232,333</td>
<td align="right">14,344,787</td>
<td align="right">1,064.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">9,000</td>
<td align="right">89,998</td>
<td align="right">900.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">9,000</td>
<td align="right">89,998</td>
<td align="right">900.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">221,687</td>
<td align="right">2,098,851</td>
<td align="right">846.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">9,060</td>
<td align="right">82,782</td>
<td align="right">813.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">322,775</td>
<td align="right">2,610,246</td>
<td align="right">708.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">188,996</td>
<td align="right">1,502,674</td>
<td align="right">695.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">548,286</td>
<td align="right">3,602,681</td>
<td align="right">557.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">348,529</td>
<td align="right">2,286,681</td>
<td align="right">556.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">51,575</td>
<td align="right">323,604</td>
<td align="right">527.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,114,223</td>
<td align="right">6,711,790</td>
<td align="right">502.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">108,059</td>
<td align="right">649,718</td>
<td align="right">501.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,498,351</td>
<td align="right">14,625,856</td>
<td align="right">485.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">106,703</td>
<td align="right">594,780</td>
<td align="right">457.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">165,956</td>
<td align="right">920,083</td>
<td align="right">454.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">8,160</td>
<td align="right">45,060</td>
<td align="right">452.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">80,999</td>
<td align="right">444,146</td>
<td align="right">448.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,367,521</td>
<td align="right">18,208,945</td>
<td align="right">440.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">964,390</td>
<td align="right">5,208,454</td>
<td align="right">440.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">346,490</td>
<td align="right">1,799,979</td>
<td align="right">419.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">3,656,732</td>
<td align="right">18,435,530</td>
<td align="right">404.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">894,813</td>
<td align="right">4,259,912</td>
<td align="right">376.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">2,284,854</td>
<td align="right">10,829,929</td>
<td align="right">374.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">402,412</td>
<td align="right">1,897,336</td>
<td align="right">371.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">413,133</td>
<td align="right">1,820,900</td>
<td align="right">340.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">87,533</td>
<td align="right">378,179</td>
<td align="right">332.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">133,305</td>
<td align="right">573,284</td>
<td align="right">330.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">91,383</td>
<td align="right">386,534</td>
<td align="right">323.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">346,450</td>
<td align="right">1,452,944</td>
<td align="right">319.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,595,577</td>
<td align="right">15,048,315</td>
<td align="right">318.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">3,595,577</td>
<td align="right">15,018,558</td>
<td align="right">317.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,517,385</td>
<td align="right">29,991,518</td>
<td align="right">299.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">403,754</td>
<td align="right">1,607,322</td>
<td align="right">298.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">64,463</td>
<td align="right">251,999</td>
<td align="right">290.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">159,831</td>
<td align="right">623,015</td>
<td align="right">289.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">4,890,926</td>
<td align="right">19,047,272</td>
<td align="right">289.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">851,130</td>
<td align="right">3,257,845</td>
<td align="right">282.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">786,728</td>
<td align="right">2,985,963</td>
<td align="right">279.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">786,728</td>
<td align="right">2,985,963</td>
<td align="right">279.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">552,432</td>
<td align="right">2,055,759</td>
<td align="right">272.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">709,705</td>
<td align="right">2,589,016</td>
<td align="right">264.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,570,287</td>
<td align="right">5,707,892</td>
<td align="right">263.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">664,541</td>
<td align="right">2,411,673</td>
<td align="right">262.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,482,754</td>
<td align="right">5,257,715</td>
<td align="right">254.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">269,006</td>
<td align="right">952,731</td>
<td align="right">254.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,633,287</td>
<td align="right">5,779,893</td>
<td align="right">253.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">132,749</td>
<td align="right">467,998</td>
<td align="right">252.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">17,999</td>
<td align="right">62,998</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">18,000</td>
<td align="right">62,999</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">90,056</td>
<td align="right">315,056</td>
<td align="right">249.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">90,056</td>
<td align="right">315,056</td>
<td align="right">249.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">491,922</td>
<td align="right">1,695,996</td>
<td align="right">244.8%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">16,649</td>
<td align="right">56,611</td>
<td align="right">240.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,894,343</td>
<td align="right">6,346,947</td>
<td align="right">235.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,299,421</td>
<td align="right">7,474,702</td>
<td align="right">225.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">143,943</td>
<td align="right">467,757</td>
<td align="right">225.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">305,554</td>
<td align="right">990,959</td>
<td align="right">224.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">180,120</td>
<td align="right">582,453</td>
<td align="right">223.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">281,127</td>
<td align="right">901,247</td>
<td align="right">220.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">297,112</td>
<td align="right">904,834</td>
<td align="right">204.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">187,936</td>
<td align="right">563,869</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">1,232,851</td>
<td align="right">3,585,723</td>
<td align="right">190.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,232,851</td>
<td align="right">3,585,723</td>
<td align="right">190.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,292,700</td>
<td align="right">3,712,984</td>
<td align="right">187.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">176,182</td>
<td align="right">505,618</td>
<td align="right">187.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">8,270,486</td>
<td align="right">23,716,398</td>
<td align="right">186.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">271,872</td>
<td align="right">776,064</td>
<td align="right">185.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">390,267</td>
<td align="right">1,087,203</td>
<td align="right">178.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,888,457</td>
<td align="right">5,213,925</td>
<td align="right">176.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,888,457</td>
<td align="right">5,213,925</td>
<td align="right">176.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,870,458</td>
<td align="right">5,141,927</td>
<td align="right">174.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">142,373</td>
<td align="right">389,313</td>
<td align="right">173.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">260,937</td>
<td align="right">696,667</td>
<td align="right">167.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,645,010</td>
<td align="right">4,293,460</td>
<td align="right">161.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">6,334,798</td>
<td align="right">16,493,118</td>
<td align="right">160.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">428,934</td>
<td align="right">1,096,679</td>
<td align="right">155.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">231,824</td>
<td align="right">584,395</td>
<td align="right">152.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">1,921,123</td>
<td align="right">4,803,739</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">18,954</td>
<td align="right">45,784</td>
<td align="right">141.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">294,144</td>
<td align="right">701,001</td>
<td align="right">138.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">987,190</td>
<td align="right">2,334,469</td>
<td align="right">136.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">44,999</td>
<td align="right">106,408</td>
<td align="right">136.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,336,463</td>
<td align="right">3,115,825</td>
<td align="right">133.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,879,625</td>
<td align="right">8,849,042</td>
<td align="right">128.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">178,529</td>
<td align="right">405,058</td>
<td align="right">126.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,340,975</td>
<td align="right">2,812,257</td>
<td align="right">109.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">1,905,624</td>
<td align="right">3,653,446</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">65,136</td>
<td align="right">123,668</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,135,654</td>
<td align="right">162,000</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">167,045</td>
<td align="right">307,917</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">244,191</td>
<td align="right">442,882</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,272,883</td>
<td align="right">2,294,753</td>
<td align="right">80.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">135,000</td>
<td align="right">27,000</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">45,000</td>
<td align="right">81,000</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">45,000</td>
<td align="right">81,000</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">426,439</td>
<td align="right">761,447</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">901,589</td>
<td align="right">1,550,687</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">280,033</td>
<td align="right">480,014</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">40,023</td>
<td align="right">66,359</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">45,480</td>
<td align="right">72,498</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">45,480</td>
<td align="right">72,498</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">195,808</td>
<td align="right">304,024</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">229,008</td>
<td align="right">352,806</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,080,461</td>
<td align="right">1,605,792</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">42,596</td>
<td align="right">62,999</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">213,110</td>
<td align="right">308,197</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">189,000</td>
<td align="right">269,999</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">488,241</td>
<td align="right">279,057</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">199,138</td>
<td align="right">281,736</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">134,160</td>
<td align="right">189,060</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">90,060</td>
<td align="right">126,060</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">535,799</td>
<td align="right">693,985</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">535,799</td>
<td align="right">693,985</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">284,519</td>
<td align="right">365,756</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">73,031</td>
<td align="right">93,334</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">284,519</td>
<td align="right">347,756</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">289,211</td>
<td align="right">226,585</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">364,388</td>
<td align="right">437,069</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">47,159</td>
<td align="right">56,512</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">411,241</td>
<td align="right">468,990</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,000</td>
<td align="right">90,000</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">117,000</td>
<td align="right">126,000</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">31,263</td>
<td align="right">28,937</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">327,207</td>
<td align="right">329,650</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">347,523</td>
<td align="right">349,960</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">347,523</td>
<td align="right">349,960</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">6,703</td>
<td align="right">6,726</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">36,360</td>
<td align="right">36,380</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">162,000</td>
<td align="right">162,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">81,000</td>
<td align="right">81,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">12,835</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">414,352</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">333,590</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">153,177</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">135,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">127,653</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">125,991</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right"></td>
<td align="right">117,178</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">107,998</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">107,998</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">98,998</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">98,519</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right">72,056</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right"></td>
<td align="right">72,056</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">63,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">63,059</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">63,059</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">62,999</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">56,611</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right"></td>
<td align="right">54,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">45,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">45,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right"></td>
<td align="right">44,399</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">36,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">36,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right"></td>
<td align="right">36,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">36,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">36,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right"></td>
<td align="right">29,757</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right"></td>
<td align="right">27,057</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right"></td>
<td align="right">27,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">27,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">27,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right"></td>
<td align="right">27,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">20,848</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right"></td>
<td align="right">18,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">18,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">18,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">9,000</td>
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
<td align="right">100</td>
<td align="right">620</td>
<td align="right">520.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">220</td>
<td align="right">450.0%</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-23
