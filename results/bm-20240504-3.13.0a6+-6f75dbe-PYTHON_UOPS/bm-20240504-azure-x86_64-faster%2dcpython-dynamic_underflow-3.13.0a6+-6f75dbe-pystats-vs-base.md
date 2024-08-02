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
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">239,774,164</td>
<td align="right">5,721,193</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">98,864,672</td>
<td align="right">2,858,540</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">33,197,040</td>
<td align="right">1,698,760</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,780,968</td>
<td align="right">3,385,115</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">105,827,712</td>
<td align="right">6,818,330</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">34,141,997</td>
<td align="right">2,453,360</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">326,755,302</td>
<td align="right">27,298,299</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">277,075,445</td>
<td align="right">55,577,081</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">113,272,642</td>
<td align="right">28,533,489</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">89,680</td>
<td align="right">25,520</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">69,092,821</td>
<td align="right">21,275,841</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">123,090,119</td>
<td align="right">39,058,859</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">481,973</td>
<td align="right">153,645</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">807,420</td>
<td align="right">258,020</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">280,066,663</td>
<td align="right">92,675,801</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">50,450,511</td>
<td align="right">16,802,621</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,694,629</td>
<td align="right">17,168,667</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,296,430</td>
<td align="right">2,885,693</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">86,566,348</td>
<td align="right">34,453,224</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">365,803,068</td>
<td align="right">152,359,948</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">646,654,924</td>
<td align="right">278,070,313</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">908,128,558</td>
<td align="right">391,311,119</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">102,921,059</td>
<td align="right">44,487,871</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">60,522,876</td>
<td align="right">26,863,952</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,224,718</td>
<td align="right">88,388,463</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">65,948,286</td>
<td align="right">31,162,410</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">193,944,776</td>
<td align="right">92,742,051</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">287,123,766</td>
<td align="right">137,767,862</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">991,719</td>
<td align="right">484,046</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">73,426,663</td>
<td align="right">38,568,148</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,856,247</td>
<td align="right">5,202,898</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,656,801</td>
<td align="right">4,197,522</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">116,948,126</td>
<td align="right">64,468,160</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,899,230,966</td>
<td align="right">2,715,870,673</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">376,336,170</td>
<td align="right">209,228,683</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">447,881,293</td>
<td align="right">251,190,860</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">346,067,670</td>
<td align="right">194,650,262</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">73,533,496</td>
<td align="right">42,871,581</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,599,429,988</td>
<td align="right">2,105,585,936</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,445,178</td>
<td align="right">45,911,950</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,342,254,485</td>
<td align="right">788,342,701</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,206,188</td>
<td align="right">62,484,749</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">396,622,455</td>
<td align="right">238,936,933</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">88,886,319</td>
<td align="right">53,940,757</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">292,504,920</td>
<td align="right">178,613,116</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,300,196,878</td>
<td align="right">1,418,379,717</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">92,069,208</td>
<td align="right">56,777,995</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">300,743,727</td>
<td align="right">191,048,682</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,934,121,452</td>
<td align="right">2,516,379,116</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">225,719,816</td>
<td align="right">149,415,330</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">207,464,418</td>
<td align="right">139,647,078</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">325,604,435</td>
<td align="right">223,443,555</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,724,740</td>
<td align="right">2,263,284</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,804,533,735</td>
<td align="right">1,952,491,772</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">199,784,054</td>
<td align="right">140,463,601</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,180,137,966</td>
<td align="right">1,542,061,498</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">395,546,519</td>
<td align="right">283,143,751</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">154,168,295</td>
<td align="right">110,568,603</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">201,508,282</td>
<td align="right">145,735,336</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">134,502,791</td>
<td align="right">97,559,572</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">342,296,678</td>
<td align="right">248,521,252</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">482,482,584</td>
<td align="right">350,629,397</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,377,217,299</td>
<td align="right">12,679,411,371</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,690,545,088</td>
<td align="right">3,441,281,356</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,232,399,279</td>
<td align="right">911,763,324</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,971,459,638</td>
<td align="right">1,459,694,882</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">987,379,724</td>
<td align="right">736,329,701</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,164,573,625</td>
<td align="right">3,132,345,237</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">85,327,631</td>
<td align="right">64,197,780</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">45,298,196</td>
<td align="right">34,117,284</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,637,768</td>
<td align="right">35,187,640</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,313,539,723</td>
<td align="right">2,500,848,324</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">358,231,542</td>
<td align="right">273,430,618</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">523,834,117</td>
<td align="right">404,099,284</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">44,507,398</td>
<td align="right">34,503,157</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">24,148,676</td>
<td align="right">18,749,642</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">36,416,958</td>
<td align="right">28,436,330</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,097,050,805</td>
<td align="right">2,419,399,542</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">293,857,625</td>
<td align="right">230,422,003</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">597,384,942</td>
<td align="right">469,274,482</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">785,068,121</td>
<td align="right">616,883,109</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">294,408,887</td>
<td align="right">231,418,870</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">42,271,921</td>
<td align="right">33,349,762</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,613,312,463</td>
<td align="right">1,285,740,919</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,887,894</td>
<td align="right">2,269,128</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">16,029,218</td>
<td align="right">12,798,013</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,212,681</td>
<td align="right">7,358,189</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,319,536,165</td>
<td align="right">1,859,375,767</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">171,298,019</td>
<td align="right">137,450,697</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">84,403,303</td>
<td align="right">67,804,897</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">852,826,667</td>
<td align="right">685,391,683</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">305,787,461</td>
<td align="right">246,831,984</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">141,396,121</td>
<td align="right">115,661,862</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">448,289,341</td>
<td align="right">369,224,427</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">30,383,775</td>
<td align="right">25,089,844</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,074,790,439</td>
<td align="right">890,547,363</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">230,797,733</td>
<td align="right">191,868,655</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">354,872,911</td>
<td align="right">296,484,241</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">532,922,036</td>
<td align="right">446,100,692</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">106,431,106</td>
<td align="right">89,482,276</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">351,407,302</td>
<td align="right">301,496,004</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">118,117,635</td>
<td align="right">101,538,676</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">28,303,486</td>
<td align="right">24,440,558</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,488,845,742</td>
<td align="right">4,764,819,592</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">494,940</td>
<td align="right">434,020</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">172,516,771</td>
<td align="right">154,023,635</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">71,816,533</td>
<td align="right">64,945,279</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">218,227,247</td>
<td align="right">200,348,044</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">7,508,554</td>
<td align="right">6,901,723</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">271,579,208</td>
<td align="right">250,449,071</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">2,795,753</td>
<td align="right">2,581,986</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">82,090,117</td>
<td align="right">75,937,219</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">693,596</td>
<td align="right">642,586</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,574,651</td>
<td align="right">375,108,668</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">45,855,342</td>
<td align="right">42,766,778</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,852,002</td>
<td align="right">140,367,788</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">200,776,382</td>
<td align="right">188,850,351</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,459,748</td>
<td align="right">18,369,077</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">55,597,133</td>
<td align="right">52,707,051</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">42,739,808</td>
<td align="right">40,526,177</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,128,182</td>
<td align="right">2,032,964</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">161,458,836</td>
<td align="right">154,248,557</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,560,644</td>
<td align="right">78,138,021</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">253,232,734</td>
<td align="right">242,773,463</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">486,124,544</td>
<td align="right">466,296,281</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">66,031,891</td>
<td align="right">63,433,984</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">70,894</td>
<td align="right">73,617</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">150,014,524</td>
<td align="right">144,865,101</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">602,229,581</td>
<td align="right">582,006,266</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,096,881,503</td>
<td align="right">1,061,888,010</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">91,695,502</td>
<td align="right">88,781,794</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">8,426,660</td>
<td align="right">8,652,645</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">34,081,671</td>
<td align="right">33,224,654</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">44,844,906</td>
<td align="right">43,790,042</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">364,472,211</td>
<td align="right">355,945,350</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">14,634,301</td>
<td align="right">14,300,455</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">49,596,929</td>
<td align="right">48,682,743</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">11,645,174</td>
<td align="right">11,495,072</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">38,087,106</td>
<td align="right">37,811,247</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,075,646,341</td>
<td align="right">1,068,366,853</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,192,241,205</td>
<td align="right">2,205,780,232</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">229,144,963</td>
<td align="right">227,743,331</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">7,183,871</td>
<td align="right">7,218,733</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">14,642,068</td>
<td align="right">14,679,100</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">14,600,519</td>
<td align="right">14,637,435</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">238,173</td>
<td align="right">238,579</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">53,599,104</td>
<td align="right">53,535,035</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">278,540</td>
<td align="right">278,767</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">199,192,622</td>
<td align="right">199,339,184</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,832,724</td>
<td align="right">11,839,984</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">11,378,447</td>
<td align="right">11,385,419</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">228,598,881</td>
<td align="right">228,717,573</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,111,874</td>
<td align="right">2,112,799</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">276,154,120</td>
<td align="right">276,256,267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">127,354,365</td>
<td align="right">127,400,632</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,469,974</td>
<td align="right">4,470,864</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1,337,635</td>
<td align="right">1,337,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">19,005</td>
<td align="right">19,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">556,269,910</td>
<td align="right">556,311,842</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,462,968</td>
<td align="right">20,464,032</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,839,830</td>
<td align="right">173,848,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">3,005,926</td>
<td align="right">3,006,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">152,063</td>
<td align="right">152,057</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,865,010</td>
<td align="right">786,895,053</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">91,112,808</td>
<td align="right">91,116,204</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">91,119,068</td>
<td align="right">91,122,464</td>
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
<td align="right">8,095,340</td>
<td align="right">8,095,340</td>
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
<td align="right">3,465,180</td>
<td align="right">3,465,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">541,780</td>
<td align="right">541,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">241,040</td>
<td align="right">241,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">202,660</td>
<td align="right">202,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">24,020</td>
<td align="right">24,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,020</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,000</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">320</td>
<td align="right">320</td>
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
<td align="right">29,506,665</td>
<td align="right">1.7%</td>
<td align="right">20,051,694</td>
<td align="right">1.6%</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">423,343,723</td>
<td align="right">23.9%</td>
<td align="right">301,795,829</td>
<td align="right">23.5%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,344,032,938</td>
<td align="right">76.0%</td>
<td align="right">983,082,211</td>
<td align="right">76.4%</td>
<td align="right">-26.9%</td>
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
<td align="right">598,445</td>
<td align="right">35.0%</td>
<td align="right">420,216</td>
<td align="right">30.0%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,111,016</td>
<td align="right">65.0%</td>
<td align="right">979,400</td>
<td align="right">70.0%</td>
<td align="right">-11.8%</td>
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
<td align="right">39,241</td>
<td align="right">3.5%</td>
<td align="right">12,963</td>
<td align="right">1.3%</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,826</td>
<td align="right">0.5%</td>
<td align="right">3,349</td>
<td align="right">0.3%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">83,709</td>
<td align="right">7.5%</td>
<td align="right">55,696</td>
<td align="right">5.7%</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,714</td>
<td align="right">0.5%</td>
<td align="right">3,904</td>
<td align="right">0.4%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">39,862</td>
<td align="right">3.6%</td>
<td align="right">28,114</td>
<td align="right">2.9%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,842</td>
<td align="right">0.8%</td>
<td align="right">6,885</td>
<td align="right">0.7%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,709</td>
<td align="right">1.3%</td>
<td align="right">11,886</td>
<td align="right">1.2%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,780</td>
<td align="right">1.0%</td>
<td align="right">8,937</td>
<td align="right">0.9%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">3,401</td>
<td align="right">0.3%</td>
<td align="right">2,960</td>
<td align="right">0.3%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">5,122</td>
<td align="right">0.5%</td>
<td align="right">4,505</td>
<td align="right">0.5%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">35,061</td>
<td align="right">3.2%</td>
<td align="right">31,605</td>
<td align="right">3.2%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">782,344</td>
<td align="right">70.4%</td>
<td align="right">734,751</td>
<td align="right">75.0%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,708</td>
<td align="right">2.9%</td>
<td align="right">30,817</td>
<td align="right">3.1%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,993</td>
<td align="right">0.8%</td>
<td align="right">8,739</td>
<td align="right">0.9%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">12,377</td>
<td align="right">1.1%</td>
<td align="right">12,063</td>
<td align="right">1.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,656</td>
<td align="right">0.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">17,254</td>
<td align="right">1.6%</td>
<td align="right">17,173</td>
<td align="right">1.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,973</td>
<td align="right">0.2%</td>
<td align="right">1,977</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,187,809,236</td>
<td align="right">79.7%</td>
<td align="right">645,928,587</td>
<td align="right">77.0%</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">302,334,348</td>
<td align="right">20.3%</td>
<td align="right">192,588,183</td>
<td align="right">23.0%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,837,691</td>
<td align="right">0.1%</td>
<td align="right">1,755,255</td>
<td align="right">0.2%</td>
<td align="right">-4.5%</td>
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
<td align="right">126,058</td>
<td align="right">51.0%</td>
<td align="right">96,165</td>
<td align="right">44.6%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">121,012</td>
<td align="right">49.0%</td>
<td align="right">119,589</td>
<td align="right">55.4%</td>
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
<td align="left">buffer int</td>
<td align="right">21,760</td>
<td align="right">17.3%</td>
<td align="right">10,300</td>
<td align="right">10.7%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">45,200</td>
<td align="right">35.9%</td>
<td align="right">30,440</td>
<td align="right">31.7%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">12.9%</td>
<td align="right">13,220</td>
<td align="right">13.7%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,320</td>
<td align="right">1.0%</td>
<td align="right">1,280</td>
<td align="right">1.3%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">123</td>
<td align="right">0.1%</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">34,655</td>
<td align="right">27.5%</td>
<td align="right">33,999</td>
<td align="right">35.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">3.4%</td>
<td align="right">4,300</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">1,640</td>
<td align="right">1.3%</td>
<td align="right">1,640</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">760</td>
<td align="right">0.6%</td>
<td align="right">760</td>
<td align="right">0.8%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">20,080</td>
<td align="right">0.0%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,243,720,928</td>
<td align="right">94.2%</td>
<td align="right">3,915,441,083</td>
<td align="right">93.2%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">196,888,009</td>
<td align="right">3.5%</td>
<td align="right">160,181,917</td>
<td align="right">3.8%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">319,861,343</td>
<td align="right">5.7%</td>
<td align="right">283,892,907</td>
<td align="right">6.8%</td>
<td align="right">-11.2%</td>
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
<td align="right">4,285,801</td>
<td align="right">97.8%</td>
<td align="right">3,594,074</td>
<td align="right">97.4%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">95,230</td>
<td align="right">2.2%</td>
<td align="right">95,568</td>
<td align="right">2.6%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">82,350</td>
<td align="right">86.5%</td>
<td align="right">82,648</td>
<td align="right">86.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">11,820</td>
<td align="right">12.4%</td>
<td align="right">11,860</td>
<td align="right">12.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,480</td>
<td align="right">3.7%</td>
<td align="right">3,480</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">1,060</td>
<td align="right">1.1%</td>
<td align="right">1,060</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">680</td>
<td align="right">0.7%</td>
<td align="right">680</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">200</td>
<td align="right">0.2%</td>
<td align="right">200</td>
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
<td align="right">104,751,399</td>
<td align="right">6.5%</td>
<td align="right">63,036,130</td>
<td align="right">5.3%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,503,944,186</td>
<td align="right">93.5%</td>
<td align="right">1,122,834,614</td>
<td align="right">94.7%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">764,918</td>
<td align="right">0.0%</td>
<td align="right">756,338</td>
<td align="right">0.1%</td>
<td align="right">-1.1%</td>
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
<td align="right">144,558</td>
<td align="right">65.8%</td>
<td align="right">129,981</td>
<td align="right">63.4%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">75,149</td>
<td align="right">34.2%</td>
<td align="right">74,976</td>
<td align="right">36.6%</td>
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
<td align="left">float long</td>
<td align="right">16,094</td>
<td align="right">11.1%</td>
<td align="right">10,456</td>
<td align="right">8.0%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,000</td>
<td align="right">2.8%</td>
<td align="right">2,740</td>
<td align="right">2.1%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,980</td>
<td align="right">1.4%</td>
<td align="right">1,660</td>
<td align="right">1.3%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,766</td>
<td align="right">8.1%</td>
<td align="right">10,251</td>
<td align="right">7.9%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,790</td>
<td align="right">11.6%</td>
<td align="right">14,865</td>
<td align="right">11.4%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,634</td>
<td align="right">13.6%</td>
<td align="right">18,410</td>
<td align="right">14.2%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">30,285</td>
<td align="right">21.0%</td>
<td align="right">28,494</td>
<td align="right">21.9%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">1,533</td>
<td align="right">1.1%</td>
<td align="right">1,480</td>
<td align="right">1.1%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,912</td>
<td align="right">19.3%</td>
<td align="right">27,099</td>
<td align="right">20.8%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,824</td>
<td align="right">1.3%</td>
<td align="right">1,786</td>
<td align="right">1.4%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.4%</td>
<td align="right">10,680</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,060</td>
<td align="right">1.4%</td>
<td align="right">2,060</td>
<td align="right">1.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">387,830,827</td>
<td align="right">88.9%</td>
<td align="right">81,593,310</td>
<td align="right">64.3%</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">48,229,180</td>
<td align="right">11.1%</td>
<td align="right">45,144,483</td>
<td align="right">35.6%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,517,260</td>
<td align="right">0.6%</td>
<td align="right">2,517,260</td>
<td align="right">2.0%</td>
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
<td align="right">81,868</td>
<td align="right">57.1%</td>
<td align="right">77,995</td>
<td align="right">55.9%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,554</td>
<td align="right">42.9%</td>
<td align="right">61,560</td>
<td align="right">44.1%</td>
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
<td align="right">9,700</td>
<td align="right">11.8%</td>
<td align="right">8,880</td>
<td align="right">11.4%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">19,748</td>
<td align="right">24.1%</td>
<td align="right">18,203</td>
<td align="right">23.3%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">30,060</td>
<td align="right">36.7%</td>
<td align="right">29,032</td>
<td align="right">37.2%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">22,360</td>
<td align="right">27.3%</td>
<td align="right">21,880</td>
<td align="right">28.1%</td>
<td align="right">-2.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">356,895,432</td>
<td align="right">81.3%</td>
<td align="right">217,805,170</td>
<td align="right">73.5%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">379,024</td>
<td align="right">0.1%</td>
<td align="right">328,363</td>
<td align="right">0.1%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">81,753,758</td>
<td align="right">18.6%</td>
<td align="right">78,283,937</td>
<td align="right">26.4%</td>
<td align="right">-4.2%</td>
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
<td align="right">128,397</td>
<td align="right">69.1%</td>
<td align="right">125,846</td>
<td align="right">69.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">57,513</td>
<td align="right">30.9%</td>
<td align="right">56,601</td>
<td align="right">31.0%</td>
<td align="right">-1.6%</td>
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
<td align="left">set</td>
<td align="right">19,322</td>
<td align="right">15.0%</td>
<td align="right">18,343</td>
<td align="right">14.6%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,723</td>
<td align="right">9.1%</td>
<td align="right">11,407</td>
<td align="right">9.1%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">42,415</td>
<td align="right">33.0%</td>
<td align="right">41,467</td>
<td align="right">33.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">13,300</td>
<td align="right">10.4%</td>
<td align="right">13,160</td>
<td align="right">10.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,980</td>
<td align="right">1.5%</td>
<td align="right">1,960</td>
<td align="right">1.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,020</td>
<td align="right">3.1%</td>
<td align="right">3,980</td>
<td align="right">3.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,739</td>
<td align="right">9.1%</td>
<td align="right">11,639</td>
<td align="right">9.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">5,520</td>
<td align="right">4.3%</td>
<td align="right">5,480</td>
<td align="right">4.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,880</td>
<td align="right">5.4%</td>
<td align="right">6,914</td>
<td align="right">5.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">518</td>
<td align="right">0.4%</td>
<td align="right">516</td>
<td align="right">0.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">8,580</td>
<td align="right">6.7%</td>
<td align="right">8,580</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,560</td>
<td align="right">1.2%</td>
<td align="right">1,560</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">560</td>
<td align="right">0.4%</td>
<td align="right">560</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.2%</td>
<td align="right">280</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">253,058,286</td>
<td align="right">3.1%</td>
<td align="right">154,513,897</td>
<td align="right">2.3%</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">678,462</td>
<td align="right">0.0%</td>
<td align="right">488,353</td>
<td align="right">0.0%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">779,774,300</td>
<td align="right">9.5%</td>
<td align="right">596,312,673</td>
<td align="right">9.0%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,406,018,653</td>
<td align="right">90.4%</td>
<td align="right">5,995,016,848</td>
<td align="right">90.9%</td>
<td align="right">-19.1%</td>
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
<td align="right">5,428,722</td>
<td align="right">87.5%</td>
<td align="right">3,571,182</td>
<td align="right">83.0%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">777,300</td>
<td align="right">12.5%</td>
<td align="right">730,734</td>
<td align="right">17.0%</td>
<td align="right">-6.0%</td>
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
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">46,563</td>
<td align="right">6.0%</td>
<td align="right">41,317</td>
<td align="right">5.7%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">57,142</td>
<td align="right">7.4%</td>
<td align="right">51,065</td>
<td align="right">7.0%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">211,914</td>
<td align="right">27.3%</td>
<td align="right">189,929</td>
<td align="right">26.0%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,800</td>
<td align="right">2.0%</td>
<td align="right">14,610</td>
<td align="right">2.0%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,958</td>
<td align="right">2.1%</td>
<td align="right">14,920</td>
<td align="right">2.0%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,980</td>
<td align="right">0.4%</td>
<td align="right">2,820</td>
<td align="right">0.4%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">7,491</td>
<td align="right">1.0%</td>
<td align="right">7,138</td>
<td align="right">1.0%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">99,697</td>
<td align="right">12.8%</td>
<td align="right">95,746</td>
<td align="right">13.1%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">29,480</td>
<td align="right">3.8%</td>
<td align="right">28,400</td>
<td align="right">3.9%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">74,677</td>
<td align="right">9.6%</td>
<td align="right">72,431</td>
<td align="right">9.9%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">1,080</td>
<td align="right">0.1%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">160,205</td>
<td align="right">20.6%</td>
<td align="right">157,343</td>
<td align="right">21.5%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3,342</td>
<td align="right">0.4%</td>
<td align="right">3,397</td>
<td align="right">0.5%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,128</td>
<td align="right">2.6%</td>
<td align="right">19,898</td>
<td align="right">2.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">14,843</td>
<td align="right">1.9%</td>
<td align="right">14,780</td>
<td align="right">2.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">15,280</td>
<td align="right">2.0%</td>
<td align="right">15,280</td>
<td align="right">2.1%</td>
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
<td align="left">property</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">4,775,567,641</td>
<td align="right">99.6%</td>
<td align="right">3,411,758,129</td>
<td align="right">99.4%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">425,732</td>
<td align="right">0.0%</td>
<td align="right">428,525</td>
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
<td align="right">20,365,516</td>
<td align="right">0.4%</td>
<td align="right">20,368,874</td>
<td align="right">0.6%</td>
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
<td align="right">11,760</td>
<td align="right">0.0%</td>
<td align="right">11,760</td>
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
<td align="right">523,184</td>
<td align="right">100.0%</td>
<td align="right">523,683</td>
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
<td align="right">89,273,988</td>
<td align="right">100.0%</td>
<td align="right">83,155,952</td>
<td align="right">100.0%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,584</td>
<td align="right">0.0%</td>
<td align="right">9,587</td>
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
<td align="right">9,421</td>
<td align="right">100.0%</td>
<td align="right">9,421</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,801,953</td>
<td align="right">18.1%</td>
<td align="right">173,810,075</td>
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
<td align="right">786,834,110</td>
<td align="right">81.9%</td>
<td align="right">786,864,153</td>
<td align="right">81.9%</td>
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
<td align="right">30,900</td>
<td align="right">0.0%</td>
<td align="right">30,900</td>
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
<td align="right">7,050</td>
<td align="right">10.3%</td>
<td align="right">7,127</td>
<td align="right">10.4%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,727</td>
<td align="right">89.7%</td>
<td align="right">61,727</td>
<td align="right">89.6%</td>
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
<td align="right">53.8%</td>
<td align="right">33,180</td>
<td align="right">53.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,127</td>
<td align="right">26.1%</td>
<td align="right">16,127</td>
<td align="right">26.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,960</td>
<td align="right">16.1%</td>
<td align="right">9,960</td>
<td align="right">16.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,220</td>
<td align="right">3.6%</td>
<td align="right">2,220</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">240</td>
<td align="right">0.4%</td>
<td align="right">240</td>
<td align="right">0.4%</td>
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
<td align="right">69,496,139</td>
<td align="right">3.4%</td>
<td align="right">41,917,013</td>
<td align="right">2.3%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">102,044,075</td>
<td align="right">5.1%</td>
<td align="right">74,129,608</td>
<td align="right">4.0%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,912,575,973</td>
<td align="right">94.9%</td>
<td align="right">1,765,376,558</td>
<td align="right">95.9%</td>
<td align="right">-7.7%</td>
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
<td align="right">1,433,291</td>
<td align="right">93.5%</td>
<td align="right">913,193</td>
<td align="right">90.2%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">100,444</td>
<td align="right">6.5%</td>
<td align="right">98,866</td>
<td align="right">9.8%</td>
<td align="right">-1.6%</td>
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
<td align="left">no dict</td>
<td align="right">5,000</td>
<td align="right">5.0%</td>
<td align="right">4,746</td>
<td align="right">4.8%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,720</td>
<td align="right">8.7%</td>
<td align="right">8,400</td>
<td align="right">8.5%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,680</td>
<td align="right">14.6%</td>
<td align="right">14,188</td>
<td align="right">14.4%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">11,580</td>
<td align="right">11.5%</td>
<td align="right">11,342</td>
<td align="right">11.5%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">5,240</td>
<td align="right">5.2%</td>
<td align="right">5,340</td>
<td align="right">5.4%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">35,464</td>
<td align="right">35.3%</td>
<td align="right">35,090</td>
<td align="right">35.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,780</td>
<td align="right">7.7%</td>
<td align="right">7,780</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">6,080</td>
<td align="right">6.1%</td>
<td align="right">6,080</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">4,360</td>
<td align="right">4.3%</td>
<td align="right">4,360</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
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
<td align="right">167,331,497</td>
<td align="right">71.7%</td>
<td align="right">99,852,707</td>
<td align="right">61.2%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">65,959,745</td>
<td align="right">28.3%</td>
<td align="right">63,363,502</td>
<td align="right">38.8%</td>
<td align="right">-3.9%</td>
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
<td align="right">57,004</td>
<td align="right">79.0%</td>
<td align="right">55,338</td>
<td align="right">78.5%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,142</td>
<td align="right">21.0%</td>
<td align="right">15,144</td>
<td align="right">21.5%</td>
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
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">11.4%</td>
<td align="right">6,120</td>
<td align="right">11.1%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">35,217</td>
<td align="right">61.8%</td>
<td align="right">34,039</td>
<td align="right">61.5%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">11,307</td>
<td align="right">19.8%</td>
<td align="right">11,159</td>
<td align="right">20.2%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,300</td>
<td align="right">4.0%</td>
<td align="right">2,320</td>
<td align="right">4.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">900</td>
<td align="right">1.6%</td>
<td align="right">900</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">800</td>
<td align="right">1.4%</td>
<td align="right">800</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,812,255,571</td>
<td align="right">91.9%</td>
<td align="right">1,893,493,513</td>
<td align="right">91.2%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">247,675,717</td>
<td align="right">8.1%</td>
<td align="right">182,386,430</td>
<td align="right">8.8%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,229,871</td>
<td align="right">1.6%</td>
<td align="right">43,129,987</td>
<td align="right">2.1%</td>
<td align="right">-12.4%</td>
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
<td align="right">1,144,186</td>
<td align="right">85.5%</td>
<td align="right">1,029,650</td>
<td align="right">85.3%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">194,022</td>
<td align="right">14.5%</td>
<td align="right">177,508</td>
<td align="right">14.7%</td>
<td align="right">-8.5%</td>
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
<td align="right">20,160</td>
<td align="right">10.4%</td>
<td align="right">13,435</td>
<td align="right">7.6%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">30,683</td>
<td align="right">15.8%</td>
<td align="right">22,739</td>
<td align="right">12.8%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2,321</td>
<td align="right">1.2%</td>
<td align="right">2,028</td>
<td align="right">1.1%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">17,801</td>
<td align="right">9.2%</td>
<td align="right">17,378</td>
<td align="right">9.8%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">4,743</td>
<td align="right">2.4%</td>
<td align="right">4,677</td>
<td align="right">2.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">49,400</td>
<td align="right">25.5%</td>
<td align="right">48,875</td>
<td align="right">27.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">23,181</td>
<td align="right">11.9%</td>
<td align="right">22,943</td>
<td align="right">12.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,169</td>
<td align="right">2.7%</td>
<td align="right">5,123</td>
<td align="right">2.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">38,904</td>
<td align="right">20.1%</td>
<td align="right">38,650</td>
<td align="right">21.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,240</td>
<td align="right">0.6%</td>
<td align="right">1,240</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">420</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">447,416</td>
<td align="right">0.1%</td>
<td align="right">119,449</td>
<td align="right">0.1%</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">533,270,803</td>
<td align="right">99.9%</td>
<td align="right">184,818,355</td>
<td align="right">99.9%</td>
<td align="right">-65.3%</td>
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
<td align="right">3,073</td>
<td align="right">8.9%</td>
<td align="right">2,657</td>
<td align="right">7.8%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">31,484</td>
<td align="right">91.1%</td>
<td align="right">31,539</td>
<td align="right">92.2%</td>
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
<td align="right">380</td>
<td align="right">12.4%</td>
<td align="right">300</td>
<td align="right">11.3%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">2,193</td>
<td align="right">71.4%</td>
<td align="right">1,857</td>
<td align="right">69.9%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">500</td>
<td align="right">16.3%</td>
<td align="right">500</td>
<td align="right">18.8%</td>
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
<td align="right">604,319,282</td>
<td align="right">0.6%</td>
<td align="right">425,796,072</td>
<td align="right">0.6%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">53,742,161,858</td>
<td align="right">55.3%</td>
<td align="right">38,253,804,231</td>
<td align="right">53.7%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,098,980,568</td>
<td align="right">8.3%</td>
<td align="right">5,881,620,788</td>
<td align="right">8.3%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">34,741,349,234</td>
<td align="right">35.7%</td>
<td align="right">26,632,975,816</td>
<td align="right">37.4%</td>
<td align="right">-23.3%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">104,751,399</td>
<td align="right">3.9%</td>
<td align="right">63,036,130</td>
<td align="right">3.0%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">302,334,348</td>
<td align="right">11.3%</td>
<td align="right">192,588,183</td>
<td align="right">9.3%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">423,343,723</td>
<td align="right">15.9%</td>
<td align="right">301,795,829</td>
<td align="right">14.5%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">102,044,075</td>
<td align="right">3.8%</td>
<td align="right">74,129,608</td>
<td align="right">3.6%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">247,675,717</td>
<td align="right">9.3%</td>
<td align="right">182,386,430</td>
<td align="right">8.8%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">779,774,300</td>
<td align="right">29.2%</td>
<td align="right">596,312,673</td>
<td align="right">28.7%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">319,861,343</td>
<td align="right">12.0%</td>
<td align="right">283,892,907</td>
<td align="right">13.7%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">81,753,758</td>
<td align="right">3.1%</td>
<td align="right">78,283,937</td>
<td align="right">3.8%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">65,959,745</td>
<td align="right">2.5%</td>
<td align="right">63,363,502</td>
<td align="right">3.1%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,801,953</td>
<td align="right">6.5%</td>
<td align="right">173,810,075</td>
<td align="right">8.4%</td>
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
<td align="right">73,373,495</td>
<td align="right">12.1%</td>
<td align="right">19,159,107</td>
<td align="right">4.5%</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">90,557,899</td>
<td align="right">15.0%</td>
<td align="right">58,202,838</td>
<td align="right">13.7%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">105,110,388</td>
<td align="right">17.4%</td>
<td align="right">72,301,562</td>
<td align="right">17.0%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">23,642,971</td>
<td align="right">3.9%</td>
<td align="right">20,357,361</td>
<td align="right">4.8%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">41,715,523</td>
<td align="right">6.9%</td>
<td align="right">39,267,102</td>
<td align="right">9.2%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">23,629,299</td>
<td align="right">3.9%</td>
<td align="right">23,102,105</td>
<td align="right">5.4%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">26,125,470</td>
<td align="right">4.3%</td>
<td align="right">25,946,518</td>
<td align="right">6.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">39,418,666</td>
<td align="right">6.5%</td>
<td align="right">39,376,427</td>
<td align="right">9.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,825,627</td>
<td align="right">4.6%</td>
<td align="right">27,831,441</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,345,903</td>
<td align="right">7.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20,980,092</td>
<td align="right">4.9%</td>
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
<td align="right">233,855,666</td>
<td align="right">3.0%</td>
<td align="right">245,345,856</td>
<td align="right">3.1%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,337,815,746</td>
<td align="right">17.2%</td>
<td align="right">1,351,682,542</td>
<td align="right">17.3%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,340,491,966</td>
<td align="right">17.2%</td>
<td align="right">1,354,358,762</td>
<td align="right">17.3%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,194,856,268</td>
<td align="right">28.1%</td>
<td align="right">2,208,744,708</td>
<td align="right">28.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,194,856,268</td>
<td align="right">28.1%</td>
<td align="right">2,208,744,708</td>
<td align="right">28.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">454,031,968</td>
<td align="right">5.8%</td>
<td align="right">455,022,272</td>
<td align="right">5.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">34,575,456</td>
<td align="right">0.4%</td>
<td align="right">34,623,171</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,604,099,047</td>
<td align="right">71.9%</td>
<td align="right">5,597,548,079</td>
<td align="right">71.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,115,297,119</td>
<td align="right">78.4%</td>
<td align="right">6,122,230,960</td>
<td align="right">78.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">73,895,965</td>
<td align="right">0.9%</td>
<td align="right">73,946,567</td>
<td align="right">0.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">213,167,294</td>
<td align="right">2.7%</td>
<td align="right">213,221,899</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">854,364,302</td>
<td align="right">11.0%</td>
<td align="right">854,385,946</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,652,200</td>
<td align="right">0.0%</td>
<td align="right">2,652,200</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">24,020</td>
<td align="right">0.0%</td>
<td align="right">24,020</td>
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
<td align="right">6,422,554</td>
<td align="right"></td>
<td align="right">7,479,540</td>
<td align="right"></td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,239,352,322</td>
<td align="right"></td>
<td align="right">2,326,935,849</td>
<td align="right"></td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">22,633,804,070</td>
<td align="right">21.1%</td>
<td align="right">23,452,415,952</td>
<td align="right">21.4%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,353,393,349</td>
<td align="right">61.9%</td>
<td align="right">10,673,694,148</td>
<td align="right">62.5%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,478,987,633</td>
<td align="right">62.6%</td>
<td align="right">10,799,434,370</td>
<td align="right">63.3%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,804,157,192</td>
<td align="right"></td>
<td align="right">11,124,958,459</td>
<td align="right"></td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">97,424,122,619</td>
<td align="right">78.9%</td>
<td align="right">99,739,000,366</td>
<td align="right">79.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">37,470,967</td>
<td align="right"></td>
<td align="right">38,141,858</td>
<td align="right"></td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">84,712,357,612</td>
<td align="right">78.9%</td>
<td align="right">86,203,373,782</td>
<td align="right">78.6%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">25,992,793,367</td>
<td align="right">21.1%</td>
<td align="right">26,329,284,939</td>
<td align="right">20.9%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">31,270,681</td>
<td align="right"></td>
<td align="right">30,873,929</td>
<td align="right"></td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,541,445</td>
<td align="right">0.1%</td>
<td align="right">20,617,070</td>
<td align="right">0.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,251,271,576</td>
<td align="right">37.4%</td>
<td align="right">6,273,715,883</td>
<td align="right">36.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,253,143,385</td>
<td align="right"></td>
<td align="right">6,275,588,328</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,229,082</td>
<td align="right"></td>
<td align="right">162,546,110</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,088,331,981</td>
<td align="right"></td>
<td align="right">3,090,848,181</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">105,052,839</td>
<td align="right">0.6%</td>
<td align="right">105,123,152</td>
<td align="right">0.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">6,547,460</td>
<td align="right">4.0%</td>
<td align="right">6,547,460</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">64,160</td>
<td align="right">0.0%</td>
<td align="right">64,160</td>
<td align="right">0.0%</td>
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
<td align="right">19,449,935</td>
<td align="right">14,619,176,001</td>
<td align="right">0</td>
<td align="right">19,533,998</td>
<td align="right">14,657,845,618</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">7,051,830,980</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">7,052,275,830</td>
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">380</td>
<td align="right">0.1%</td>
<td align="right">216.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">46,463</td>
<td align="right">6.2%</td>
<td align="right">96,866</td>
<td align="right">18.1%</td>
<td align="right">108.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">443,074</td>
<td align="right">58.8%</td>
<td align="right">50,677</td>
<td align="right">9.5%</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">110,823</td>
<td align="right">14.7%</td>
<td align="right">182,900</td>
<td align="right">34.2%</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,435</td>
<td align="right">0.9%</td>
<td align="right">10,011</td>
<td align="right">1.9%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">642,864</td>
<td align="right">85.3%</td>
<td align="right">351,303</td>
<td align="right">65.8%</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">753,687</td>
<td align="right"></td>
<td align="right">534,203</td>
<td align="right"></td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">1,660</td>
<td align="right">0.3%</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">693</td>
<td align="right">0.1%</td>
<td align="right">867</td>
<td align="right">0.2%</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">195,953,165,138</td>
<td align="right">2,806.2%</td>
<td align="right">243,812,821,294</td>
<td align="right">3,163.4%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,982,862,232</td>
<td align="right"></td>
<td align="right">7,707,416,115</td>
<td align="right"></td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,281</td>
<td align="right">5.7%</td>
<td align="right">6,773</td>
<td align="right">3.7%</td>
<td align="right">7.8%</td>
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
<td align="right">107,263</td>
<td align="right">96.8%</td>
<td align="right">179,080</td>
<td align="right">97.9%</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">110,823</td>
<td align="right"></td>
<td align="right">182,900</td>
<td align="right"></td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,340</td>
<td align="right">2.1%</td>
<td align="right">2,354</td>
<td align="right">1.3%</td>
<td align="right">0.6%</td>
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
<td align="right">5,097</td>
<td align="right">4.6%</td>
<td align="right">14,854</td>
<td align="right">8.1%</td>
<td align="right">191.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,016</td>
<td align="right">19.0%</td>
<td align="right">41,120</td>
<td align="right">22.5%</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,981</td>
<td align="right">32.5%</td>
<td align="right">54,517</td>
<td align="right">29.8%</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">27,242</td>
<td align="right">24.6%</td>
<td align="right">39,241</td>
<td align="right">21.5%</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,987</td>
<td align="right">12.6%</td>
<td align="right">20,955</td>
<td align="right">11.5%</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,100</td>
<td align="right">5.5%</td>
<td align="right">9,657</td>
<td align="right">5.3%</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,260</td>
<td align="right">1.1%</td>
<td align="right">2,136</td>
<td align="right">1.2%</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">200.0%</td>
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
<td align="right">4,117</td>
<td align="right">3.7%</td>
<td align="right">2,992</td>
<td align="right">1.6%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">14,618</td>
<td align="right">13.2%</td>
<td align="right">36,078</td>
<td align="right">19.7%</td>
<td align="right">146.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">23,895</td>
<td align="right">21.6%</td>
<td align="right">40,334</td>
<td align="right">22.1%</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,894</td>
<td align="right">32.4%</td>
<td align="right">54,103</td>
<td align="right">29.6%</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">17,562</td>
<td align="right">15.8%</td>
<td align="right">27,291</td>
<td align="right">14.9%</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,257</td>
<td align="right">7.5%</td>
<td align="right">13,330</td>
<td align="right">7.3%</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,580</td>
<td align="right">2.3%</td>
<td align="right">4,272</td>
<td align="right">2.3%</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">340</td>
<td align="right">0.3%</td>
<td align="right">680</td>
<td align="right">0.4%</td>
<td align="right">100.0%</td>
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
<tr>
<td align="left"><= 2</td>
<td align="right">27,717,760</td>
<td align="right">0.4%</td>
<td align="right">28,222,400</td>
<td align="right">0.4%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">373,460,738</td>
<td align="right">5.3%</td>
<td align="right">190,273,294</td>
<td align="right">2.5%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">905,006,398</td>
<td align="right">13.0%</td>
<td align="right">1,031,368,449</td>
<td align="right">13.4%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,052,813,549</td>
<td align="right">15.1%</td>
<td align="right">850,947,895</td>
<td align="right">11.0%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,110,391,450</td>
<td align="right">15.9%</td>
<td align="right">890,846,364</td>
<td align="right">11.6%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">693,116,859</td>
<td align="right">9.9%</td>
<td align="right">779,478,569</td>
<td align="right">10.1%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">339,829,871</td>
<td align="right">4.9%</td>
<td align="right">433,393,339</td>
<td align="right">5.6%</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">183,003,639</td>
<td align="right">2.6%</td>
<td align="right">212,852,313</td>
<td align="right">2.8%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">26,125,060</td>
<td align="right">0.4%</td>
<td align="right">26,941,643</td>
<td align="right">0.3%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">7,342,778</td>
<td align="right">0.1%</td>
<td align="right">7,342,898</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 2,048</td>
<td align="right">18,394,000</td>
<td align="right">0.3%</td>
<td align="right">18,394,013</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4,096</td>
<td align="right">685,824</td>
<td align="right">0.0%</td>
<td align="right">685,827</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="right">740,467</td>
<td align="right">0.0%</td>
<td align="right">740,528</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="right">246,840</td>
<td align="right">0.0%</td>
<td align="right">246,820</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="right">43,760</td>
<td align="right">0.0%</td>
<td align="right">43,780</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="right">13,150</td>
<td align="right">0.0%</td>
<td align="right">13,160</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="right">1,010</td>
<td align="right">0.0%</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left"><= 262,144</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
<td align="right">2,001</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 524,288</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">479</td>
<td align="right">0.0%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left"><= 1,048,576</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 2,097,152</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">399</td>
<td align="right">0.0%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left"><= 4,194,304</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">241</td>
<td align="right">0.0%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left"><= 8,388,608</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16,777,216</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="left">_CONVERT_VALUE</td>
<td align="right">71,420</td>
<td align="right">96,082,420</td>
<td align="right">134,431.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">6,729,622</td>
<td align="right">22,392.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,551,735</td>
<td align="right">316,236,152</td>
<td align="right">20,279.5%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">2,007,330</td>
<td align="right">101,032,941</td>
<td align="right">4,933.2%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">378,499</td>
<td align="right">4,867.2%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,953,610</td>
<td align="right">51,360,321</td>
<td align="right">2,529.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,160</td>
<td align="right">12,271,336</td>
<td align="right">1,394.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">174,004,615</td>
<td align="right">2,374,091,377</td>
<td align="right">1,264.4%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,610,840</td>
<td align="right">38,937,994</td>
<td align="right">978.4%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,168,875</td>
<td align="right">58,384,619</td>
<td align="right">846.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">13,550,480</td>
<td align="right">97,629,965</td>
<td align="right">620.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">448,573</td>
<td align="right">2,416,549</td>
<td align="right">438.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">61,625,420</td>
<td align="right">224,559,660</td>
<td align="right">264.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,123,104</td>
<td align="right">35,827,972</td>
<td align="right">253.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">34,050,600</td>
<td align="right">118,131,528</td>
<td align="right">246.9%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">836,100,176</td>
<td align="right">2,664,455,634</td>
<td align="right">218.7%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">651,310</td>
<td align="right">2,072,415</td>
<td align="right">218.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">871,420</td>
<td align="right">170.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">22,421,720</td>
<td align="right">55,122,382</td>
<td align="right">145.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">140,298,221</td>
<td align="right">342,037,940</td>
<td align="right">143.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">55,151,895</td>
<td align="right">117,246,901</td>
<td align="right">112.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,337,772</td>
<td align="right">72,281,312</td>
<td align="right">104.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">93,518,647</td>
<td align="right">178,338,063</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">16,604,268</td>
<td align="right">30,891,300</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">121,066,596</td>
<td align="right">222,291,948</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,782,169</td>
<td align="right">10,095,895</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">710,997,045</td>
<td align="right">1,231,842,667</td>
<td align="right">73.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">73,395,423</td>
<td align="right">126,388,043</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,635,720</td>
<td align="right">9,429,529</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">97,472,022</td>
<td align="right">157,928,634</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">108,946,575</td>
<td align="right">175,580,021</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">263,645,615</td>
<td align="right">418,697,877</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,285,795,517</td>
<td align="right">2,040,702,771</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">264,872,435</td>
<td align="right">419,890,666</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">2,069,920,744</td>
<td align="right">861,528,686</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">324,415,782</td>
<td align="right">512,895,843</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,226,305</td>
<td align="right">12,914,864</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,843,820</td>
<td align="right">96,592,850</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">113,698,869</td>
<td align="right">170,794,175</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">112,576,229</td>
<td align="right">165,880,424</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">278,282,861</td>
<td align="right">406,896,280</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">79,346,703</td>
<td align="right">116,017,023</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">87,586,581</td>
<td align="right">127,150,885</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">129,527,425</td>
<td align="right">187,873,023</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,312,959,597</td>
<td align="right">1,903,347,184</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">339,609,115</td>
<td align="right">491,562,064</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,623,776,874</td>
<td align="right">2,323,956,463</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,412,610</td>
<td align="right">112,112,092</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">199,474,425</td>
<td align="right">284,840,782</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">948,501,041</td>
<td align="right">1,329,351,021</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,772,475,314</td>
<td align="right">2,480,406,008</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,825,173,057</td>
<td align="right">2,552,554,149</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,924,820,601</td>
<td align="right">2,684,245,594</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,912,941,488</td>
<td align="right">6,845,887,429</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">384,961,390</td>
<td align="right">534,277,081</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">13,743,341,056</td>
<td align="right">19,044,434,970</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">153,025,357</td>
<td align="right">211,972,400</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">564,586,027</td>
<td align="right">778,678,833</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,543,472,922</td>
<td align="right">2,110,187,678</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">115,449,772</td>
<td align="right">157,049,370</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,619,488</td>
<td align="right">127,327,359</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,069,378,457</td>
<td align="right">2,804,654,107</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">217,534,602</td>
<td align="right">294,125,769</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,868,052,088</td>
<td align="right">2,514,046,018</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,918,923</td>
<td align="right">136,785,734</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">727,114,245</td>
<td align="right">970,094,696</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">411,157,503</td>
<td align="right">547,162,353</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">62,368,668</td>
<td align="right">82,670,624</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">62,254,768</td>
<td align="right">82,443,101</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">99,762,244</td>
<td align="right">131,806,145</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,222,485,346</td>
<td align="right">2,903,514,817</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,399,009,928</td>
<td align="right">1,824,598,800</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">845,848,240</td>
<td align="right">1,098,161,306</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">551,515,722</td>
<td align="right">715,462,649</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,199,058,586</td>
<td align="right">2,847,466,815</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,008,955,006</td>
<td align="right">1,294,857,860</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">97,045,246</td>
<td align="right">123,370,372</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">96,801,126</td>
<td align="right">122,841,272</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,109,261,947</td>
<td align="right">1,406,961,783</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,167,410,311</td>
<td align="right">4,009,292,160</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,429,696,692</td>
<td align="right">4,337,559,792</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,433,067,361</td>
<td align="right">8,134,865,193</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">688,100,377</td>
<td align="right">868,044,132</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">331,264,604</td>
<td align="right">416,428,944</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,209,387,301</td>
<td align="right">1,516,944,737</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,228,579,698</td>
<td align="right">1,540,115,940</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,826,414,100</td>
<td align="right">3,534,625,499</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,236,157,279</td>
<td align="right">4,046,061,848</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">789,423,670</td>
<td align="right">986,138,826</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">413,976,715</td>
<td align="right">516,046,241</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">144,484,275</td>
<td align="right">179,841,576</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,941,160</td>
<td align="right">179,732,340</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">233,242,154</td>
<td align="right">289,030,234</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,600,851,125</td>
<td align="right">8,146,737,228</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">484,289,810</td>
<td align="right">597,196,017</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">4,482,988</td>
<td align="right">5,500,976</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,264,755</td>
<td align="right">1,634,737,910</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,389,236,307</td>
<td align="right">7,805,829,745</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">153,994,236</td>
<td align="right">187,893,129</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,061,508,102</td>
<td align="right">8,615,272,594</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,149,312,426</td>
<td align="right">2,620,060,115</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">758,213,727</td>
<td align="right">918,608,652</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,696,947,294</td>
<td align="right">14,114,639,559</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">336,628,220</td>
<td align="right">405,536,727</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">595,988,882</td>
<td align="right">716,321,107</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">960,588,627</td>
<td align="right">1,134,596,094</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,039,921,236</td>
<td align="right">1,225,362,832</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,973,479,293</td>
<td align="right">2,323,288,641</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">557,119,100</td>
<td align="right">652,736,239</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,205,620,838</td>
<td align="right">2,580,419,174</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,133,180</td>
<td align="right">2,489,080</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,426,420</td>
<td align="right">232,463,146</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">364,489,778</td>
<td align="right">422,564,317</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,587,179,192</td>
<td align="right">11,102,364,931</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,059,081,218</td>
<td align="right">1,220,153,494</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,958,197,444</td>
<td align="right">3,406,398,269</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,393,560,766</td>
<td align="right">1,603,031,398</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,681,753,520</td>
<td align="right">6,517,785,507</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">686,391,932</td>
<td align="right">786,192,940</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">404,534,338</td>
<td align="right">462,626,161</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">22,768,182</td>
<td align="right">25,923,935</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">314,421,877</td>
<td align="right">357,987,407</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,042,489,674</td>
<td align="right">1,186,545,243</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,653,969,848</td>
<td align="right">1,875,482,541</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">212,390,965</td>
<td align="right">238,329,802</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">58,672,404</td>
<td align="right">65,697,421</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">184,675,145</td>
<td align="right">206,736,564</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">187,014,436</td>
<td align="right">209,322,327</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">133,732,295</td>
<td align="right">149,620,165</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">133,732,295</td>
<td align="right">149,620,165</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,367,710,853</td>
<td align="right">1,526,510,178</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">226,004,300</td>
<td align="right">251,757,815</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">877,798,999</td>
<td align="right">975,555,017</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,565,631</td>
<td align="right">50,278,645</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">484,834,312</td>
<td align="right">534,880,755</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">29,592,879</td>
<td align="right">32,644,030</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,821,191,289</td>
<td align="right">2,008,850,318</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,112,566,854</td>
<td align="right">1,220,664,125</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">172,041,249</td>
<td align="right">188,707,329</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,292,268</td>
<td align="right">110,823,884</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">99,814,900</td>
<td align="right">109,199,614</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">531,150,840</td>
<td align="right">579,435,810</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,242,237,871</td>
<td align="right">1,352,729,927</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">92,087,855</td>
<td align="right">100,148,083</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">228,606,315</td>
<td align="right">248,347,692</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">70,416,220</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">223,042,225</td>
<td align="right">204,106,312</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,903,010</td>
<td align="right">137,614,660</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,680</td>
<td align="right">58,333,120</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">64,594,900</td>
<td align="right">69,919,780</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,673,616</td>
<td align="right">413,357,472</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">245,488,189</td>
<td align="right">262,574,789</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">935,679,620</td>
<td align="right">999,272,386</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,722,160</td>
<td align="right">542,268,067</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,539,403,882</td>
<td align="right">2,700,380,524</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,337,652</td>
<td align="right">57,767,637</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,532,398,662</td>
<td align="right">4,255,471,258</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">613,731,428</td>
<td align="right">650,067,212</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">99,792,471</td>
<td align="right">105,441,334</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">227,618,685</td>
<td align="right">240,106,433</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">98,833,831</td>
<td align="right">104,075,420</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,114,509,436</td>
<td align="right">1,173,085,257</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,399,850</td>
<td align="right">11,998,778</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,239,262,242</td>
<td align="right">1,304,102,553</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">556,466,020</td>
<td align="right">585,341,217</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,399,850</td>
<td align="right">11,978,598</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,273,419,689</td>
<td align="right">1,332,915,316</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">4,823,420</td>
<td align="right">5,046,751</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,647,063,439</td>
<td align="right">2,767,971,794</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,059,100</td>
<td align="right">23,051,496</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">202,055,223</td>
<td align="right">210,823,778</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">747,101,843</td>
<td align="right">777,993,130</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">746,564,523</td>
<td align="right">777,390,430</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,808,233</td>
<td align="right">10,147,189</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,893,078</td>
<td align="right">237,027,248</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">974,058,812</td>
<td align="right">1,003,339,161</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,868,340</td>
<td align="right">154,281,720</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,865,500</td>
<td align="right">2,946,700</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">149,739,059</td>
<td align="right">153,619,818</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,604,086,617</td>
<td align="right">3,694,727,775</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,270,066</td>
<td align="right">207,668,457</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">134,222,543</td>
<td align="right">137,088,106</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">188,411,476</td>
<td align="right">192,025,711</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,312,982,062</td>
<td align="right">1,333,354,563</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,369,753,282</td>
<td align="right">1,390,575,456</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,101,974,182</td>
<td align="right">1,117,535,571</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">620,646,895</td>
<td align="right">628,780,943</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,913,275</td>
<td align="right">69,597,513</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">700,996,533</td>
<td align="right">706,397,789</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">381,764,120</td>
<td align="right">384,363,673</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,405,920</td>
<td align="right">81,913,617</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">543,620,171</td>
<td align="right">546,664,784</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,500,884</td>
<td align="right">32,652,300</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,683,574,699</td>
<td align="right">4,694,560,798</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,155,109,872</td>
<td align="right">2,160,058,825</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">46,374,040</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">20,499,060</td>
<td align="right">20,500,503</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,693,500</td>
<td align="right">12,693,120</td>
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
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">543,640</td>
<td align="right">543,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">41,100</td>
<td align="right">41,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_OFFSET</td>
<td align="right"></td>
<td align="right">1,580,645,353</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">554,293,148</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_OFFSET</td>
<td align="right"></td>
<td align="right">554,293,148</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">27,485,438</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">113,183</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right"></td>
<td align="right">57,582</td>
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
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">260</td>
<td align="right">3,065</td>
<td align="right">1,078.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">400</td>
<td align="right">1,080</td>
<td align="right">170.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,574</td>
<td align="right">5,705</td>
<td align="right">121.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">880</td>
<td align="right">1,599</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">84,334</td>
<td align="right">148,207</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,751</td>
<td align="right">10,522</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">30,362</td>
<td align="right">44,622</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,380</td>
<td align="right">1,980</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,612</td>
<td align="right">7,858</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">440</td>
<td align="right">600</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">1,910</td>
<td align="right">2,298</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">32,250</td>
<td align="right">38,683</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,340</td>
<td align="right">2,700</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">539</td>
<td align="right">620</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">41,851</td>
<td align="right">46,483</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,660</td>
<td align="right">1,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right"></td>
<td align="right">68</td>
<td align="right"></td>
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
<td align="right">1,081</td>
<td align="right">1,086</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,081</td>
<td align="right">1,086</td>
<td align="right">0.5%</td>
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
<td align="right">1,980</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-05-04
