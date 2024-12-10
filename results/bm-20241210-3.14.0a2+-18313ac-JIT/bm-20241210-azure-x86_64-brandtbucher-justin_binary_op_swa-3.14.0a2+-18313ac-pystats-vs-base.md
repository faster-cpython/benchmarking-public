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
<td align="right">4,118,016</td>
<td align="right">4,009,038</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">14,693,784</td>
<td align="right">14,482,360</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">5,591,717</td>
<td align="right">5,512,499</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">142,026,921</td>
<td align="right">143,550,187</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">259,590,912</td>
<td align="right">262,279,010</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">60,078,233</td>
<td align="right">59,488,812</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">234,347,188</td>
<td align="right">236,595,186</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">131,642,846</td>
<td align="right">132,836,876</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,091,682</td>
<td align="right">3,117,417</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,827,379</td>
<td align="right">3,800,964</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">38,694,018</td>
<td align="right">38,450,481</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">400,066,370</td>
<td align="right">402,271,698</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">140,126,842</td>
<td align="right">140,817,504</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">349,282,087</td>
<td align="right">350,744,241</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">683,786,485</td>
<td align="right">686,500,139</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">66,108,900</td>
<td align="right">65,868,175</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">408,671,912</td>
<td align="right">410,149,405</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,239,486</td>
<td align="right">47,081,150</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">290,775,451</td>
<td align="right">289,937,301</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,643,689</td>
<td align="right">18,591,177</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">211,183,644</td>
<td align="right">210,593,379</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,008,166</td>
<td align="right">9,982,228</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,914,002</td>
<td align="right">9,888,350</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">68,984,513</td>
<td align="right">68,808,962</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">138,308,656</td>
<td align="right">137,978,366</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">102,322,505</td>
<td align="right">102,108,148</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,704,389,249</td>
<td align="right">1,707,807,919</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">352,568,619</td>
<td align="right">351,871,450</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">632,420,377</td>
<td align="right">633,556,740</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">312,322,028</td>
<td align="right">311,779,683</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">335,277,427</td>
<td align="right">334,705,450</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">868,989,298</td>
<td align="right">870,433,302</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">500,405,811</td>
<td align="right">501,231,269</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">60,549,890</td>
<td align="right">60,452,729</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,120,068,106</td>
<td align="right">1,121,845,072</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">165,554,652</td>
<td align="right">165,298,463</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">54,755,250</td>
<td align="right">54,832,273</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">304,349,498</td>
<td align="right">303,930,043</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">19,933,156</td>
<td align="right">19,906,890</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">115,405,609</td>
<td align="right">115,262,327</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">199,584,318</td>
<td align="right">199,830,544</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,934,542,978</td>
<td align="right">1,936,883,545</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,334,483,022</td>
<td align="right">3,338,474,449</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">169,934,985</td>
<td align="right">170,134,558</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">78,665,225</td>
<td align="right">78,754,975</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">160,883,553</td>
<td align="right">160,710,442</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,989,363,640</td>
<td align="right">3,993,603,670</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">24,707,835</td>
<td align="right">24,733,283</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,862,080,537</td>
<td align="right">1,860,270,518</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">91,180,563</td>
<td align="right">91,093,085</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">114,594,474</td>
<td align="right">114,484,609</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">83,301,035</td>
<td align="right">83,221,955</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">295,379,086</td>
<td align="right">295,100,530</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,277,780,111</td>
<td align="right">1,278,924,317</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">208,586,343</td>
<td align="right">208,772,927</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">172,062,268</td>
<td align="right">171,924,718</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">321,311,873</td>
<td align="right">321,062,103</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,374,586,537</td>
<td align="right">2,372,756,339</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">189,429,242</td>
<td align="right">189,283,590</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">31,609,699</td>
<td align="right">31,633,385</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">88,462,615</td>
<td align="right">88,528,776</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,710</td>
<td align="right">2,708</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">21,726,124</td>
<td align="right">21,712,042</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">660,663,334</td>
<td align="right">660,252,498</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">14,538,862,214</td>
<td align="right">14,547,886,892</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">401,317,916</td>
<td align="right">401,078,483</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">63,764,816</td>
<td align="right">63,732,974</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">108,836,861</td>
<td align="right">108,785,277</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">36,614,382</td>
<td align="right">36,597,182</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">195,782,561</td>
<td align="right">195,871,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">119,201,694</td>
<td align="right">119,149,891</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">232,770,151</td>
<td align="right">232,672,048</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">64,353,995</td>
<td align="right">64,379,626</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">43,875,975</td>
<td align="right">43,858,775</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">98,585,839</td>
<td align="right">98,549,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">629,894,834</td>
<td align="right">629,664,579</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">155,435,174</td>
<td align="right">155,379,187</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">783,635,588</td>
<td align="right">783,362,628</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">76,976,508</td>
<td align="right">76,950,879</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,735,160,452</td>
<td align="right">4,733,586,352</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">311,687,027</td>
<td align="right">311,788,768</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">593,687,030</td>
<td align="right">593,494,978</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">181,321,628</td>
<td align="right">181,377,967</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,078,119,915</td>
<td align="right">1,078,444,954</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">431,749,016</td>
<td align="right">431,624,108</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,486,437,806</td>
<td align="right">2,485,743,569</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,150,303,608</td>
<td align="right">4,151,462,068</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">85,465,047</td>
<td align="right">85,443,830</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">471,891,306</td>
<td align="right">471,774,794</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">52,389,292</td>
<td align="right">52,377,432</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">680,255,657</td>
<td align="right">680,125,230</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,641,597,784</td>
<td align="right">1,641,334,916</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">99,246,412</td>
<td align="right">99,261,076</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,968,446,340</td>
<td align="right">1,968,696,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1,829,580</td>
<td align="right">1,829,807</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">254,104,398</td>
<td align="right">254,073,462</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">619,263,412</td>
<td align="right">619,195,885</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,918,025</td>
<td align="right">58,923,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">345,031,319</td>
<td align="right">345,064,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,321,207,400</td>
<td align="right">3,321,517,965</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,486,378</td>
<td align="right">1,486,509</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,128,946,489</td>
<td align="right">3,129,191,555</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">61,686,442</td>
<td align="right">61,690,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">41,172,495</td>
<td align="right">41,174,677</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,573,689</td>
<td align="right">93,578,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">352,971,127</td>
<td align="right">352,959,153</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,882</td>
<td align="right">120,878</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,718</td>
<td align="right">33,717</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">58,574,203</td>
<td align="right">58,575,811</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,482,140</td>
<td align="right">21,482,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,812,740</td>
<td align="right">21,813,321</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,812,761</td>
<td align="right">21,813,341</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">111,266,555</td>
<td align="right">111,269,422</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">76,076,919</td>
<td align="right">76,078,602</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">216,925,339</td>
<td align="right">216,929,895</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">56,009,482</td>
<td align="right">56,008,475</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">77,993,487</td>
<td align="right">77,994,415</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,183,499</td>
<td align="right">6,183,569</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,846,977,703</td>
<td align="right">1,846,995,845</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">19,646,406</td>
<td align="right">19,646,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">3,590,936</td>
<td align="right">3,590,961</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,459</td>
<td align="right">14,760,358</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,370,958,966</td>
<td align="right">2,370,974,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">114,553,967</td>
<td align="right">114,553,236</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">206,703,820</td>
<td align="right">206,705,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">202,012,547</td>
<td align="right">202,011,309</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">72,199,386</td>
<td align="right">72,199,779</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">111,261,644</td>
<td align="right">111,261,074</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">38,718,202</td>
<td align="right">38,718,382</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">48,988,802</td>
<td align="right">48,989,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">112,137,973</td>
<td align="right">112,138,317</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">30,613,321</td>
<td align="right">30,613,412</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">116,145,824</td>
<td align="right">116,145,496</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">35,061,307</td>
<td align="right">35,061,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">42,797,599</td>
<td align="right">42,797,493</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">159,634,656</td>
<td align="right">159,635,045</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">70,060,242</td>
<td align="right">70,060,352</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,122,663,754</td>
<td align="right">1,122,665,401</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">197,498,006</td>
<td align="right">197,497,790</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">299,085,681</td>
<td align="right">299,085,995</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">459,196,086</td>
<td align="right">459,196,558</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">5,919,255</td>
<td align="right">5,919,258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,643,042</td>
<td align="right">11,643,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">183,508,551</td>
<td align="right">183,508,481</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">97,145,371</td>
<td align="right">97,145,349</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,838,134</td>
<td align="right">100,838,156</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">117,240,181</td>
<td align="right">117,240,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">34,257,200</td>
<td align="right">34,257,203</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">33,222,635</td>
<td align="right">33,222,636</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,764,958</td>
<td align="right">97,764,959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,662,576</td>
<td align="right">302,662,576</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">267,014,843</td>
<td align="right">267,014,843</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">188,039,054</td>
<td align="right">188,039,054</td>
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
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">35,669,420</td>
<td align="right">35,669,420</td>
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
<td align="right">23,579,734</td>
<td align="right">23,579,734</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">22,609,725</td>
<td align="right">22,609,725</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">9,778,144</td>
<td align="right">9,778,144</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,103,989</td>
<td align="right">4,103,989</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">4,033,523</td>
<td align="right">4,033,523</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,140</td>
<td align="right">2,597,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">1,282,633</td>
<td align="right">1,282,633</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,200,677</td>
<td align="right">1,200,677</td>
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
<td align="right">793,140</td>
<td align="right">793,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">236,064</td>
<td align="right">236,064</td>
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
<td align="right">84,673</td>
<td align="right">84,673</td>
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
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">3,832</td>
<td align="right">3,832</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,642</td>
<td align="right">3,642</td>
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
<td align="right">351,774,315</td>
<td align="right">4.5%</td>
<td align="right">351,077,454</td>
<td align="right">4.5%</td>
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
<td align="right">22,227,335</td>
<td align="right">0.3%</td>
<td align="right">22,226,819</td>
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
<td align="right">7,384,757,337</td>
<td align="right">95.2%</td>
<td align="right">7,384,688,856</td>
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
<td align="right">787,195</td>
<td align="right">64.9%</td>
<td align="right">786,929</td>
<td align="right">64.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">426,497</td>
<td align="right">35.1%</td>
<td align="right">426,445</td>
<td align="right">35.1%</td>
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
<td align="left">and int</td>
<td align="right">10,526</td>
<td align="right">1.3%</td>
<td align="right">10,390</td>
<td align="right">1.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">6,745</td>
<td align="right">0.9%</td>
<td align="right">6,665</td>
<td align="right">0.8%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,350</td>
<td align="right">0.3%</td>
<td align="right">2,343</td>
<td align="right">0.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,779</td>
<td align="right">0.5%</td>
<td align="right">3,776</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1,628</td>
<td align="right">0.2%</td>
<td align="right">1,627</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,841</td>
<td align="right">2.5%</td>
<td align="right">19,829</td>
<td align="right">2.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">6,215</td>
<td align="right">0.8%</td>
<td align="right">6,212</td>
<td align="right">0.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">58,832</td>
<td align="right">7.5%</td>
<td align="right">58,805</td>
<td align="right">7.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">6,088</td>
<td align="right">0.8%</td>
<td align="right">6,086</td>
<td align="right">0.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">24,963</td>
<td align="right">3.2%</td>
<td align="right">24,959</td>
<td align="right">3.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">37,896</td>
<td align="right">4.8%</td>
<td align="right">37,899</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">583,405</td>
<td align="right">74.1%</td>
<td align="right">583,411</td>
<td align="right">74.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">13,737</td>
<td align="right">1.7%</td>
<td align="right">13,737</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">5,528</td>
<td align="right">0.7%</td>
<td align="right">5,528</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">2,651</td>
<td align="right">0.3%</td>
<td align="right">2,651</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,403</td>
<td align="right">0.2%</td>
<td align="right">1,403</td>
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
<td align="left">and other</td>
<td align="right">649</td>
<td align="right">0.1%</td>
<td align="right">649</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">123</td>
<td align="right">0.0%</td>
<td align="right">123</td>
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
<td align="right">97,764,958</td>
<td align="right">100.0%</td>
<td align="right">97,764,959</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">5,825,178</td>
<td align="right">0.1%</td>
<td align="right">5,823,285</td>
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
<td align="right">431,597,718</td>
<td align="right">7.2%</td>
<td align="right">431,472,833</td>
<td align="right">7.2%</td>
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
<td align="right">5,560,772,415</td>
<td align="right">92.7%</td>
<td align="right">5,560,747,829</td>
<td align="right">92.7%</td>
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
<td align="right">118,921</td>
<td align="right">45.6%</td>
<td align="right">118,875</td>
<td align="right">45.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">142,050</td>
<td align="right">54.4%</td>
<td align="right">142,033</td>
<td align="right">54.4%</td>
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
<td align="left">buffer int</td>
<td align="right">3,872</td>
<td align="right">2.7%</td>
<td align="right">3,883</td>
<td align="right">2.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">8,731</td>
<td align="right">6.1%</td>
<td align="right">8,710</td>
<td align="right">6.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">50,110</td>
<td align="right">35.3%</td>
<td align="right">50,102</td>
<td align="right">35.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,485</td>
<td align="right">8.8%</td>
<td align="right">12,486</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">40,666</td>
<td align="right">28.6%</td>
<td align="right">40,666</td>
<td align="right">28.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">18,318</td>
<td align="right">12.9%</td>
<td align="right">18,318</td>
<td align="right">12.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,789</td>
<td align="right">2.7%</td>
<td align="right">3,789</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.1%</td>
<td align="right">2,941</td>
<td align="right">2.1%</td>
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
<td align="right">348</td>
<td align="right">0.2%</td>
<td align="right">348</td>
<td align="right">0.2%</td>
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
<td align="right">150,852,492</td>
<td align="right">1.3%</td>
<td align="right">151,184,408</td>
<td align="right">1.3%</td>
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
<td align="right">11,373,716,916</td>
<td align="right">97.1%</td>
<td align="right">11,371,588,875</td>
<td align="right">97.1%</td>
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
<td align="right">183,278,403</td>
<td align="right">1.6%</td>
<td align="right">183,278,386</td>
<td align="right">1.6%</td>
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
<td align="right">3,038,799</td>
<td align="right">98.2%</td>
<td align="right">3,045,018</td>
<td align="right">98.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">55,141</td>
<td align="right">1.8%</td>
<td align="right">55,141</td>
<td align="right">1.8%</td>
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
<td align="right">55,141</td>
<td align="right">100.0%</td>
<td align="right">55,141</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">54,575</td>
<td align="right">99.0%</td>
<td align="right">54,575</td>
<td align="right">99.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">752</td>
<td align="right">1.4%</td>
<td align="right">752</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">287</td>
<td align="right">0.5%</td>
<td align="right">287</td>
<td align="right">0.5%</td>
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
<td align="right">111,572</td>
<td align="right">15.8%</td>
<td align="right">111,570</td>
<td align="right">15.8%</td>
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
<td align="right">1,556,968</td>
<td align="right">0.0%</td>
<td align="right">1,573,550</td>
<td align="right">0.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">114,441,307</td>
<td align="right">2.4%</td>
<td align="right">114,330,251</td>
<td align="right">2.4%</td>
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
<td align="right">4,570,175,627</td>
<td align="right">97.5%</td>
<td align="right">4,569,892,501</td>
<td align="right">97.5%</td>
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
<td align="right">134,882</td>
<td align="right">74.0%</td>
<td align="right">136,072</td>
<td align="right">74.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">47,350</td>
<td align="right">26.0%</td>
<td align="right">47,665</td>
<td align="right">25.9%</td>
<td align="right">0.7%</td>
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
<td align="right">39,073</td>
<td align="right">29.0%</td>
<td align="right">40,362</td>
<td align="right">29.7%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">401</td>
<td align="right">0.3%</td>
<td align="right">399</td>
<td align="right">0.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">9,238</td>
<td align="right">6.8%</td>
<td align="right">9,203</td>
<td align="right">6.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,052</td>
<td align="right">0.8%</td>
<td align="right">1,054</td>
<td align="right">0.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">49,388</td>
<td align="right">36.6%</td>
<td align="right">49,318</td>
<td align="right">36.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">5,097</td>
<td align="right">3.8%</td>
<td align="right">5,100</td>
<td align="right">3.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,010</td>
<td align="right">7.4%</td>
<td align="right">10,013</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">9,679</td>
<td align="right">7.2%</td>
<td align="right">9,679</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">5.7%</td>
<td align="right">7,639</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,750</td>
<td align="right">1.3%</td>
<td align="right">1,750</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,221</td>
<td align="right">0.9%</td>
<td align="right">1,221</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.2%</td>
<td align="right">334</td>
<td align="right">0.2%</td>
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
<td align="right">66,063,520</td>
<td align="right">2.9%</td>
<td align="right">65,822,871</td>
<td align="right">2.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,206,465,748</td>
<td align="right">97.0%</td>
<td align="right">2,206,281,288</td>
<td align="right">97.0%</td>
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
<td align="right">43,118</td>
<td align="right">52.9%</td>
<td align="right">43,042</td>
<td align="right">52.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,436</td>
<td align="right">47.1%</td>
<td align="right">38,436</td>
<td align="right">47.2%</td>
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
<td align="left">tuple</td>
<td align="right">15,487</td>
<td align="right">35.9%</td>
<td align="right">15,446</td>
<td align="right">35.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">10,844</td>
<td align="right">25.1%</td>
<td align="right">10,824</td>
<td align="right">25.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,517</td>
<td align="right">22.1%</td>
<td align="right">9,502</td>
<td align="right">22.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">7,270</td>
<td align="right">16.9%</td>
<td align="right">7,270</td>
<td align="right">16.9%</td>
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
<td align="right">33,653,870</td>
<td align="right">4.0%</td>
<td align="right">33,806,555</td>
<td align="right">4.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">138,196,407</td>
<td align="right">16.5%</td>
<td align="right">137,865,915</td>
<td align="right">16.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">664,715,627</td>
<td align="right">79.4%</td>
<td align="right">665,247,129</td>
<td align="right">79.5%</td>
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
<td align="right">639,936</td>
<td align="right">85.7%</td>
<td align="right">642,801</td>
<td align="right">85.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">107,158</td>
<td align="right">14.3%</td>
<td align="right">107,379</td>
<td align="right">14.3%</td>
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
<td align="left">ascii string</td>
<td align="right">1,587</td>
<td align="right">1.5%</td>
<td align="right">1,547</td>
<td align="right">1.4%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">53,049</td>
<td align="right">49.5%</td>
<td align="right">53,418</td>
<td align="right">49.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">15,629</td>
<td align="right">14.6%</td>
<td align="right">15,536</td>
<td align="right">14.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">8,505</td>
<td align="right">7.9%</td>
<td align="right">8,490</td>
<td align="right">7.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">6,497</td>
<td align="right">6.1%</td>
<td align="right">6,497</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">5,143</td>
<td align="right">4.8%</td>
<td align="right">5,143</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4,163</td>
<td align="right">3.9%</td>
<td align="right">4,163</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,585</td>
<td align="right">3.3%</td>
<td align="right">3,585</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,584</td>
<td align="right">3.3%</td>
<td align="right">3,584</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">2,494</td>
<td align="right">2.3%</td>
<td align="right">2,494</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,287</td>
<td align="right">2.1%</td>
<td align="right">2,287</td>
<td align="right">2.1%</td>
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
<td align="right">634,798,608</td>
<td align="right">4.6%</td>
<td align="right">639,529,249</td>
<td align="right">4.6%</td>
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
<td align="right">498,705,094</td>
<td align="right">3.6%</td>
<td align="right">499,530,423</td>
<td align="right">3.6%</td>
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
<td align="right">12,733,375,048</td>
<td align="right">91.8%</td>
<td align="right">12,729,115,273</td>
<td align="right">91.8%</td>
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
<td align="right">1,406,846</td>
<td align="right">0.0%</td>
<td align="right">1,406,846</td>
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
<td align="right">13,430,661</td>
<td align="right">98.3%</td>
<td align="right">13,519,766</td>
<td align="right">98.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">234,851</td>
<td align="right">1.7%</td>
<td align="right">235,017</td>
<td align="right">1.7%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">23,757</td>
<td align="right">10.1%</td>
<td align="right">24,179</td>
<td align="right">10.3%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,095</td>
<td align="right">2.6%</td>
<td align="right">6,059</td>
<td align="right">2.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">859</td>
<td align="right">0.4%</td>
<td align="right">854</td>
<td align="right">0.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">41,484</td>
<td align="right">17.7%</td>
<td align="right">41,335</td>
<td align="right">17.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,408</td>
<td align="right">1.0%</td>
<td align="right">2,403</td>
<td align="right">1.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">43,934</td>
<td align="right">18.7%</td>
<td align="right">43,893</td>
<td align="right">18.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,885</td>
<td align="right">7.2%</td>
<td align="right">16,891</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,132</td>
<td align="right">3.5%</td>
<td align="right">8,133</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">62,278</td>
<td align="right">26.5%</td>
<td align="right">62,283</td>
<td align="right">26.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,625</td>
<td align="right">3.2%</td>
<td align="right">7,625</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">5,005</td>
<td align="right">2.1%</td>
<td align="right">5,005</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">2,486</td>
<td align="right">1.1%</td>
<td align="right">2,486</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,786</td>
<td align="right">0.8%</td>
<td align="right">1,786</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,229</td>
<td align="right">0.5%</td>
<td align="right">1,229</td>
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
<td align="right">4,212,405,655</td>
<td align="right">99.6%</td>
<td align="right">4,214,008,641</td>
<td align="right">99.6%</td>
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
<td align="right">14,622,731</td>
<td align="right">0.3%</td>
<td align="right">14,622,696</td>
<td align="right">0.3%</td>
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
<td align="right">1,854</td>
<td align="right">0.0%</td>
<td align="right">1,854</td>
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
<td align="right">53,234</td>
<td align="right">0.0%</td>
<td align="right">53,234</td>
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
<td align="right">138,536</td>
<td align="right">100.0%</td>
<td align="right">138,470</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">255</td>
<td align="right">0.0%</td>
<td align="right">253</td>
<td align="right">0.0%</td>
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
<td align="right">109,882,633</td>
<td align="right">100.0%</td>
<td align="right">109,617,819</td>
<td align="right">100.0%</td>
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
<td align="right">593,528,463</td>
<td align="right">82.2%</td>
<td align="right">593,529,734</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">198,095,846</td>
<td align="right">8.2%</td>
<td align="right">198,113,215</td>
<td align="right">8.2%</td>
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
<td align="right">2,157,391,016</td>
<td align="right">88.9%</td>
<td align="right">2,157,384,777</td>
<td align="right">88.9%</td>
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
<td align="right">69,961,093</td>
<td align="right">2.9%</td>
<td align="right">69,961,200</td>
<td align="right">2.9%</td>
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
<td align="right">3,779,494</td>
<td align="right">98.5%</td>
<td align="right">3,779,834</td>
<td align="right">98.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">56,371</td>
<td align="right">1.5%</td>
<td align="right">56,375</td>
<td align="right">1.5%</td>
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
<td align="right">3,344</td>
<td align="right">5.9%</td>
<td align="right">3,348</td>
<td align="right">5.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">27,514</td>
<td align="right">48.8%</td>
<td align="right">27,514</td>
<td align="right">48.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">11,722</td>
<td align="right">20.8%</td>
<td align="right">11,722</td>
<td align="right">20.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,954</td>
<td align="right">8.8%</td>
<td align="right">4,954</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">2,848</td>
<td align="right">5.1%</td>
<td align="right">2,848</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,932</td>
<td align="right">3.4%</td>
<td align="right">1,932</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">1,061</td>
<td align="right">1.9%</td>
<td align="right">1,061</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">992</td>
<td align="right">1.8%</td>
<td align="right">992</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.3%</td>
<td align="right">730</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.2%</td>
<td align="right">699</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">365</td>
<td align="right">0.6%</td>
<td align="right">365</td>
<td align="right">0.6%</td>
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
<td align="right">922,771,123</td>
<td align="right">90.8%</td>
<td align="right">922,589,691</td>
<td align="right">90.8%</td>
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
<td align="right">93,537,027</td>
<td align="right">9.2%</td>
<td align="right">93,541,885</td>
<td align="right">9.2%</td>
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
<td align="right">2,202</td>
<td align="right">6.0%</td>
<td align="right">2,199</td>
<td align="right">6.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,500</td>
<td align="right">94.0%</td>
<td align="right">34,502</td>
<td align="right">94.0%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">4,307</td>
<td align="right">12.5%</td>
<td align="right">4,309</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,703</td>
<td align="right">48.4%</td>
<td align="right">16,703</td>
<td align="right">48.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">9,040</td>
<td align="right">26.2%</td>
<td align="right">9,040</td>
<td align="right">26.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,070</td>
<td align="right">8.9%</td>
<td align="right">3,070</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">735</td>
<td align="right">2.1%</td>
<td align="right">735</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">1.0%</td>
<td align="right">341</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">236</td>
<td align="right">0.7%</td>
<td align="right">236</td>
<td align="right">0.7%</td>
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
<td align="right">44,034,648</td>
<td align="right">0.9%</td>
<td align="right">44,116,559</td>
<td align="right">0.9%</td>
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
<td align="right">4,812,344,086</td>
<td align="right">96.9%</td>
<td align="right">4,810,976,344</td>
<td align="right">96.9%</td>
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
<td align="right">110,775,244</td>
<td align="right">2.2%</td>
<td align="right">110,778,118</td>
<td align="right">2.2%</td>
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
<td align="right">879,297</td>
<td align="right">66.6%</td>
<td align="right">880,823</td>
<td align="right">66.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">441,063</td>
<td align="right">33.4%</td>
<td align="right">441,068</td>
<td align="right">33.4%</td>
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
<td align="right">5,702</td>
<td align="right">1.3%</td>
<td align="right">5,714</td>
<td align="right">1.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">9,560</td>
<td align="right">2.2%</td>
<td align="right">9,553</td>
<td align="right">2.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">24,286</td>
<td align="right">5.5%</td>
<td align="right">24,270</td>
<td align="right">5.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,333</td>
<td align="right">3.0%</td>
<td align="right">13,335</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">14,940</td>
<td align="right">3.4%</td>
<td align="right">14,942</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">100,854</td>
<td align="right">22.9%</td>
<td align="right">100,866</td>
<td align="right">22.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">266,006</td>
<td align="right">60.3%</td>
<td align="right">266,006</td>
<td align="right">60.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,540</td>
<td align="right">1.0%</td>
<td align="right">4,540</td>
<td align="right">1.0%</td>
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
<td align="right">1,254,672,325</td>
<td align="right">99.9%</td>
<td align="right">1,255,026,176</td>
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
<td align="right">1,473,667</td>
<td align="right">0.1%</td>
<td align="right">1,473,813</td>
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
<td align="right">1,138</td>
<td align="right">8.9%</td>
<td align="right">1,135</td>
<td align="right">8.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,653</td>
<td align="right">91.1%</td>
<td align="right">11,641</td>
<td align="right">91.1%</td>
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
<td align="right">753</td>
<td align="right">66.2%</td>
<td align="right">750</td>
<td align="right">66.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">255</td>
<td align="right">22.4%</td>
<td align="right">255</td>
<td align="right">22.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">130</td>
<td align="right">11.4%</td>
<td align="right">130</td>
<td align="right">11.5%</td>
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
<td align="right">1,093,777,009</td>
<td align="right">1.3%</td>
<td align="right">1,099,105,666</td>
<td align="right">1.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">48,390,258,294</td>
<td align="right">58.1%</td>
<td align="right">48,410,156,425</td>
<td align="right">58.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,306,324,562</td>
<td align="right">2.8%</td>
<td align="right">2,305,654,852</td>
<td align="right">2.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">31,431,085,758</td>
<td align="right">37.8%</td>
<td align="right">31,439,331,670</td>
<td align="right">37.8%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">138,196,407</td>
<td align="right">6.0%</td>
<td align="right">137,865,915</td>
<td align="right">6.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">351,774,315</td>
<td align="right">15.3%</td>
<td align="right">351,077,454</td>
<td align="right">15.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">498,705,094</td>
<td align="right">21.7%</td>
<td align="right">499,530,423</td>
<td align="right">21.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">114,441,307</td>
<td align="right">5.0%</td>
<td align="right">114,330,251</td>
<td align="right">5.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">431,597,718</td>
<td align="right">18.7%</td>
<td align="right">431,472,833</td>
<td align="right">18.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,537,027</td>
<td align="right">4.1%</td>
<td align="right">93,541,885</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">110,775,244</td>
<td align="right">4.8%</td>
<td align="right">110,778,118</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">183,278,403</td>
<td align="right">8.0%</td>
<td align="right">183,278,386</td>
<td align="right">8.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,764,958</td>
<td align="right">4.2%</td>
<td align="right">97,764,959</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,796</td>
<td align="right">5.6%</td>
<td align="right">128,815,796</td>
<td align="right">5.6%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">77,951,690</td>
<td align="right">7.1%</td>
<td align="right">79,614,419</td>
<td align="right">7.2%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">74,279,712</td>
<td align="right">6.8%</td>
<td align="right">75,496,062</td>
<td align="right">6.9%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">183,930,410</td>
<td align="right">16.8%</td>
<td align="right">185,352,679</td>
<td align="right">16.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">233,440,738</td>
<td align="right">21.3%</td>
<td align="right">233,915,890</td>
<td align="right">21.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">20,446,112</td>
<td align="right">1.9%</td>
<td align="right">20,487,101</td>
<td align="right">1.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,793,395</td>
<td align="right">2.1%</td>
<td align="right">22,806,868</td>
<td align="right">2.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">106,500,104</td>
<td align="right">9.7%</td>
<td align="right">106,516,519</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">86,856,831</td>
<td align="right">7.9%</td>
<td align="right">86,859,432</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,546,345</td>
<td align="right">8.4%</td>
<td align="right">91,547,299</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">21,063,257</td>
<td align="right">1.9%</td>
<td align="right">21,063,278</td>
<td align="right">1.9%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">681,167,417</td>
<td align="right">9.7%</td>
<td align="right">681,491,463</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,630,956,594</td>
<td align="right">80.0%</td>
<td align="right">5,628,828,965</td>
<td align="right">80.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,184,831,396</td>
<td align="right">73.7%</td>
<td align="right">5,182,922,295</td>
<td align="right">73.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,168,395,693</td>
<td align="right">16.6%</td>
<td align="right">1,168,088,764</td>
<td align="right">16.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,170,527,839</td>
<td align="right">16.6%</td>
<td align="right">1,170,220,910</td>
<td align="right">16.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">25,738,042</td>
<td align="right">0.4%</td>
<td align="right">25,738,410</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,851,695,256</td>
<td align="right">26.3%</td>
<td align="right">1,851,712,373</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,851,695,256</td>
<td align="right">26.3%</td>
<td align="right">1,851,712,373</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">295,806,209</td>
<td align="right">4.2%</td>
<td align="right">295,804,438</td>
<td align="right">4.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">72,681,193</td>
<td align="right">1.0%</td>
<td align="right">72,681,590</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">265,393,901</td>
<td align="right">3.8%</td>
<td align="right">265,394,652</td>
<td align="right">3.8%</td>
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
<td align="right">1.9%</td>
<td align="right">132,513,139</td>
<td align="right">1.9%</td>
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
<td align="right">9,911,167</td>
<td align="right"></td>
<td align="right">11,155,635</td>
<td align="right"></td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,585,107,206</td>
<td align="right">45.2%</td>
<td align="right">9,479,817,312</td>
<td align="right">47.7%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,585,334,851</td>
<td align="right"></td>
<td align="right">9,480,049,361</td>
<td align="right"></td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">56,286,166,366</td>
<td align="right">26.9%</td>
<td align="right">51,308,554,631</td>
<td align="right">25.0%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">67,795,645</td>
<td align="right"></td>
<td align="right">69,753,342</td>
<td align="right"></td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">49,930,066,528</td>
<td align="right">23.9%</td>
<td align="right">50,662,572,580</td>
<td align="right">24.7%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">69,875,321</td>
<td align="right"></td>
<td align="right">70,593,119</td>
<td align="right"></td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">86,090,049,333</td>
<td align="right">41.1%</td>
<td align="right">86,218,212,595</td>
<td align="right">42.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">9,414,550,379</td>
<td align="right">5.5%</td>
<td align="right">9,423,726,935</td>
<td align="right">5.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">80,572,853,179</td>
<td align="right">46.9%</td>
<td align="right">80,535,670,216</td>
<td align="right">46.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,234,479,172</td>
<td align="right"></td>
<td align="right">3,233,198,772</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,210,837,816</td>
<td align="right"></td>
<td align="right">2,210,073,962</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">44,059,618,838</td>
<td align="right">25.6%</td>
<td align="right">44,045,772,814</td>
<td align="right">25.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">186,783,040</td>
<td align="right"></td>
<td align="right">186,725,538</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">17,004,637,360</td>
<td align="right">8.1%</td>
<td align="right">17,008,621,759</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,967,993,119</td>
<td align="right"></td>
<td align="right">10,966,013,510</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">37,852,464,963</td>
<td align="right">22.0%</td>
<td align="right">37,857,710,377</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,324,645,127</td>
<td align="right">54.4%</td>
<td align="right">10,323,840,909</td>
<td align="right">51.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,403,282,878</td>
<td align="right">54.8%</td>
<td align="right">10,402,483,439</td>
<td align="right">52.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">72,087,884</td>
<td align="right">0.4%</td>
<td align="right">72,092,596</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,549,867</td>
<td align="right">0.0%</td>
<td align="right">6,549,934</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,379</td>
<td align="right">2.4%</td>
<td align="right">4,444,379</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">476,374</td>
<td align="right">0.3%</td>
<td align="right">476,374</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,884</td>
<td align="right">0.0%</td>
<td align="right">4,884</td>
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
<td align="right">364,282</td>
<td align="right">103,756,792</td>
<td align="right">9,980,378,652</td>
<td align="right">787,454,792</td>
<td align="right">784,355,013</td>
<td align="right">364,259</td>
<td align="right">103,294,032</td>
<td align="right">9,966,349,578</td>
<td align="right">786,027,083</td>
<td align="right">784,188,814</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,605,396,290</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,605,396,674</td>
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
<td align="right">250,147,708,646</td>
<td align="right">3,696.0%</td>
<td align="right">270,594,598,841</td>
<td align="right">4,008.9%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">251</td>
<td align="right">0.1%</td>
<td align="right">238</td>
<td align="right">0.0%</td>
<td align="right">-5.2%</td>
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
<td align="right">2,664</td>
<td align="right">0.5%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,221</td>
<td align="right">0.2%</td>
<td align="right">1,174</td>
<td align="right">0.2%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,319</td>
<td align="right">0.3%</td>
<td align="right">1,339</td>
<td align="right">0.3%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,768,001,895</td>
<td align="right"></td>
<td align="right">6,749,813,498</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">80,051</td>
<td align="right">16.2%</td>
<td align="right">79,872</td>
<td align="right">16.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">371,675</td>
<td align="right">75.0%</td>
<td align="right">371,366</td>
<td align="right">75.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">415,187</td>
<td align="right">83.8%</td>
<td align="right">415,282</td>
<td align="right">83.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">495,489</td>
<td align="right"></td>
<td align="right">495,392</td>
<td align="right"></td>
<td align="right">-0.0%</td>
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
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">601</td>
<td align="right">0.8%</td>
<td align="right">601</td>
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
<td align="right">71,391</td>
<td align="right">89.2%</td>
<td align="right">70,712</td>
<td align="right">88.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">80,051</td>
<td align="right"></td>
<td align="right">79,872</td>
<td align="right"></td>
<td align="right">-0.2%</td>
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
<td align="right">5,699</td>
<td align="right">7.1%</td>
<td align="right">5,585</td>
<td align="right">7.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">9,418</td>
<td align="right">11.8%</td>
<td align="right">9,401</td>
<td align="right">11.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">27,371</td>
<td align="right">34.2%</td>
<td align="right">26,625</td>
<td align="right">33.3%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">19,292</td>
<td align="right">24.1%</td>
<td align="right">19,000</td>
<td align="right">23.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">11,251</td>
<td align="right">14.1%</td>
<td align="right">11,939</td>
<td align="right">14.9%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,129</td>
<td align="right">7.7%</td>
<td align="right">6,429</td>
<td align="right">8.0%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">811</td>
<td align="right">1.0%</td>
<td align="right">813</td>
<td align="right">1.0%</td>
<td align="right">0.2%</td>
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
<td align="right">1,003</td>
<td align="right">1.3%</td>
<td align="right">978</td>
<td align="right">1.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">10,001</td>
<td align="right">12.5%</td>
<td align="right">9,530</td>
<td align="right">11.9%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">12,306</td>
<td align="right">15.4%</td>
<td align="right">12,301</td>
<td align="right">15.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">30,315</td>
<td align="right">37.9%</td>
<td align="right">29,709</td>
<td align="right">37.2%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">12,144</td>
<td align="right">15.2%</td>
<td align="right">11,944</td>
<td align="right">15.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,317</td>
<td align="right">5.4%</td>
<td align="right">4,436</td>
<td align="right">5.6%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,223</td>
<td align="right">1.5%</td>
<td align="right">1,732</td>
<td align="right">2.2%</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">82</td>
<td align="right">0.1%</td>
<td align="right">82</td>
<td align="right">0.1%</td>
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
<td align="right">1,794,202,893</td>
<td align="right">2,288,280,137</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">96,661,423</td>
<td align="right">94,027,425</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,599,338</td>
<td align="right">1,637,018</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">1,689,747</td>
<td align="right">1,727,427</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">121,418,603</td>
<td align="right">118,887,625</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">6,962,083</td>
<td align="right">6,833,249</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">4,468,446</td>
<td align="right">4,392,254</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">425,032,266</td>
<td align="right">418,343,294</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">76,319,882</td>
<td align="right">75,206,788</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">5,539,672</td>
<td align="right">5,461,935</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">413,302,716</td>
<td align="right">408,326,240</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">246,262,286</td>
<td align="right">244,113,307</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">390,945,874</td>
<td align="right">388,322,609</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">221,763,860</td>
<td align="right">222,759,047</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">326,837,123</td>
<td align="right">325,559,089</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,567,118</td>
<td align="right">6,542,658</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">282,831,310</td>
<td align="right">283,827,544</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">805,449,565</td>
<td align="right">802,710,027</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,304,148,671</td>
<td align="right">5,287,501,972</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">5,935,624,575</td>
<td align="right">5,917,369,832</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">22,506,497</td>
<td align="right">22,441,994</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">314,469,951</td>
<td align="right">313,595,055</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">608,569,492</td>
<td align="right">606,924,958</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,768,001,895</td>
<td align="right">6,749,813,498</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,420,634,862</td>
<td align="right">1,417,395,044</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">779,355,330</td>
<td align="right">777,705,909</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,095,035</td>
<td align="right">117,338,573</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,818,283,048</td>
<td align="right">2,812,577,291</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">688,995,508</td>
<td align="right">687,623,106</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,207,825,261</td>
<td align="right">9,190,318,359</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">117,026,654</td>
<td align="right">117,242,808</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">793,107,743</td>
<td align="right">791,645,693</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">152,197,256</td>
<td align="right">152,440,834</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">171,704,078</td>
<td align="right">171,973,608</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">68,543,519</td>
<td align="right">68,438,592</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">94,152,630</td>
<td align="right">94,295,990</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,805,476,153</td>
<td align="right">2,801,208,533</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,943,664,463</td>
<td align="right">1,940,921,358</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">5,944,099,878</td>
<td align="right">5,935,735,890</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">56,353,887</td>
<td align="right">56,277,687</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,771,148,200</td>
<td align="right">1,768,795,083</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">907,334,317</td>
<td align="right">906,174,368</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,698,480,045</td>
<td align="right">1,696,334,186</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">541,056,465</td>
<td align="right">541,724,583</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,244,014,158</td>
<td align="right">3,240,159,813</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">486,790,884</td>
<td align="right">486,230,240</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">487,507,822</td>
<td align="right">486,947,178</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,203,272,538</td>
<td align="right">1,201,918,975</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,909,475,322</td>
<td align="right">2,906,360,952</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,315,666,432</td>
<td align="right">1,314,320,647</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,316,567,170</td>
<td align="right">1,315,243,725</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">15,454,238</td>
<td align="right">15,469,659</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">778,365,726</td>
<td align="right">777,605,617</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,143,488,995</td>
<td align="right">4,139,525,548</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,318,421,701</td>
<td align="right">2,316,224,916</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">221,373,261</td>
<td align="right">221,173,881</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">197,246,783</td>
<td align="right">197,069,969</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,105,146,985</td>
<td align="right">2,106,971,423</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,392,126,506</td>
<td align="right">1,393,321,889</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">153,558,957</td>
<td align="right">153,430,340</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">186,955,904</td>
<td align="right">186,802,440</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">560,671,439</td>
<td align="right">561,123,182</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">838,207,925</td>
<td align="right">837,632,308</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">19,330,087,901</td>
<td align="right">19,317,620,758</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">504,446,575</td>
<td align="right">504,129,968</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">169,731,865</td>
<td align="right">169,625,964</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">632,982,399</td>
<td align="right">633,363,968</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">755,104,234</td>
<td align="right">754,684,566</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,113,827,332</td>
<td align="right">5,110,996,624</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">248,001,379</td>
<td align="right">247,867,344</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">769,711,198</td>
<td align="right">769,305,870</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">68,945,178</td>
<td align="right">68,979,464</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">25,901,689</td>
<td align="right">25,914,361</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">70,252,058</td>
<td align="right">70,286,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">134,218,918</td>
<td align="right">134,153,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">395,045,884</td>
<td align="right">394,855,375</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">173,817,648</td>
<td align="right">173,900,739</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">27,015,089</td>
<td align="right">27,027,761</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">22,700,281,999</td>
<td align="right">22,689,805,835</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">787,341,542</td>
<td align="right">787,002,307</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">715,416,826</td>
<td align="right">715,713,712</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,153,438</td>
<td align="right">6,155,883</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,884,533,990</td>
<td align="right">5,882,199,590</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,480,800,894</td>
<td align="right">2,479,861,046</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,647,472,820</td>
<td align="right">4,645,748,209</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,538,287,197</td>
<td align="right">2,537,347,353</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,677,243,088</td>
<td align="right">4,675,587,956</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">853,436,670</td>
<td align="right">853,720,109</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">59,970,161</td>
<td align="right">59,989,933</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,482,127,074</td>
<td align="right">1,482,615,216</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,071,996,068</td>
<td align="right">1,071,645,967</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">517,871,042</td>
<td align="right">517,709,273</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,956,698,400</td>
<td align="right">1,957,305,347</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">704,810,750</td>
<td align="right">704,594,246</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,042,309,061</td>
<td align="right">1,041,994,306</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,439,823,366</td>
<td align="right">2,440,504,861</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,705,564,671</td>
<td align="right">1,706,015,129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,378,340,674</td>
<td align="right">8,376,152,527</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,569,197,462</td>
<td align="right">3,568,294,711</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,004,640,183</td>
<td align="right">1,004,404,891</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">78,196,998</td>
<td align="right">78,214,198</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">79,536,222</td>
<td align="right">79,553,422</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">407,099,878</td>
<td align="right">407,176,903</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,234,957,100</td>
<td align="right">1,234,724,409</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">409,761,118</td>
<td align="right">409,838,143</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">159,923,922</td>
<td align="right">159,896,056</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">219,097,084</td>
<td align="right">219,059,607</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,014,128,632</td>
<td align="right">1,014,295,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">309,306,693</td>
<td align="right">309,256,695</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,871,982,463</td>
<td align="right">1,871,698,194</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,013,379,600</td>
<td align="right">2,013,672,962</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">99,666,781</td>
<td align="right">99,681,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">99,666,781</td>
<td align="right">99,681,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">126,880,557</td>
<td align="right">126,862,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,946,462,647</td>
<td align="right">1,946,718,729</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">20,516,773</td>
<td align="right">20,519,217</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">75,250,850</td>
<td align="right">75,259,647</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">579,324,367</td>
<td align="right">579,261,405</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">579,324,367</td>
<td align="right">579,261,405</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,093,376,131</td>
<td align="right">1,093,260,927</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">427,689,510</td>
<td align="right">427,729,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">981,286</td>
<td align="right">981,367</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,942,102,364</td>
<td align="right">2,941,889,346</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,537,740,892</td>
<td align="right">3,537,497,108</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">545,780,263</td>
<td align="right">545,743,701</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,096,856,634</td>
<td align="right">2,096,720,301</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">815,941,796</td>
<td align="right">815,992,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,950,022,018</td>
<td align="right">1,949,918,441</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,246,468,407</td>
<td align="right">4,246,249,483</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">293,917,236</td>
<td align="right">293,931,750</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">294,135,186</td>
<td align="right">294,149,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">725,037,009</td>
<td align="right">725,068,149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,811,182,633</td>
<td align="right">3,811,024,995</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">598,793,601</td>
<td align="right">598,818,317</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,476,338,491</td>
<td align="right">1,476,288,937</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,878,164,222</td>
<td align="right">1,878,106,544</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,351,976,525</td>
<td align="right">1,352,007,665</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">88,349,500</td>
<td align="right">88,351,456</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,713,870</td>
<td align="right">91,715,826</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">391,641,138</td>
<td align="right">391,649,374</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,220,812,764</td>
<td align="right">1,220,788,264</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,517,781,646</td>
<td align="right">2,517,750,146</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,516,479,785</td>
<td align="right">9,516,368,920</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">40,380,424</td>
<td align="right">40,380,724</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">674,678,102</td>
<td align="right">674,673,124</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">608,984,394</td>
<td align="right">608,980,025</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">7,234,843</td>
<td align="right">7,234,883</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,584,057</td>
<td align="right">40,584,233</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">44,909,934</td>
<td align="right">44,909,754</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">61,699,829</td>
<td align="right">61,699,997</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">16,092,406</td>
<td align="right">16,092,392</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,202,669</td>
<td align="right">3,202,667</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,035,086,240</td>
<td align="right">3,035,088,054</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,277,770,171</td>
<td align="right">4,277,771,936</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">41,848,780</td>
<td align="right">41,848,766</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">42,612,813</td>
<td align="right">42,612,799</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">43,232,866</td>
<td align="right">43,232,852</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">35,857,106</td>
<td align="right">35,857,099</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">35,857,106</td>
<td align="right">35,857,099</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">37,693,973</td>
<td align="right">37,693,966</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">50,654,205</td>
<td align="right">50,654,198</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">66,335,253</td>
<td align="right">66,335,246</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">196,681,674</td>
<td align="right">196,681,659</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">57,255,980</td>
<td align="right">57,255,984</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">18,019,991</td>
<td align="right">18,019,990</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">71,268,684</td>
<td align="right">71,268,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">71,268,684</td>
<td align="right">71,268,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">71,299,200</td>
<td align="right">71,299,199</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">290,647,027</td>
<td align="right">290,647,025</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,556,431,336</td>
<td align="right">1,556,431,326</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,363,984,039</td>
<td align="right">1,363,984,039</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">991,820,999</td>
<td align="right">991,820,999</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">851,688,594</td>
<td align="right">851,688,594</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">504,248,661</td>
<td align="right">504,248,661</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">500,433,261</td>
<td align="right">500,433,261</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">468,665,076</td>
<td align="right">468,665,076</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">386,839,354</td>
<td align="right">386,839,354</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">305,220,594</td>
<td align="right">305,220,594</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">269,489,697</td>
<td align="right">269,489,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">216,978,477</td>
<td align="right">216,978,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">183,193,551</td>
<td align="right">183,193,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">172,166,413</td>
<td align="right">172,166,413</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">123,597,560</td>
<td align="right">123,597,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">116,319,398</td>
<td align="right">116,319,398</td>
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
<td align="right">97,200,649</td>
<td align="right">97,200,649</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">85,877,082</td>
<td align="right">85,877,082</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">84,164,950</td>
<td align="right">84,164,950</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">78,651,966</td>
<td align="right">78,651,966</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">60,725,105</td>
<td align="right">60,725,105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">58,103,990</td>
<td align="right">58,103,990</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">52,060,760</td>
<td align="right">52,060,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">50,239,620</td>
<td align="right">50,239,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">50,239,620</td>
<td align="right">50,239,620</td>
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
<td align="right">40,381,384</td>
<td align="right">40,381,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,370,263</td>
<td align="right">40,370,263</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">38,739,851</td>
<td align="right">38,739,851</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">33,816,322</td>
<td align="right">33,816,322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">33,816,322</td>
<td align="right">33,816,322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">25,679,371</td>
<td align="right">25,679,371</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">25,679,371</td>
<td align="right">25,679,371</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,322,630</td>
<td align="right">24,322,630</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,758,327</td>
<td align="right">6,758,327</td>
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
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right">3,555,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,094,097</td>
<td align="right">3,094,097</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">2,615,370</td>
<td align="right">2,615,370</td>
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
<td align="left">_MAKE_CELL</td>
<td align="right">410,042</td>
<td align="right">410,042</td>
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
<td align="left">_SET_ADD</td>
<td align="right">153,675</td>
<td align="right">153,675</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">123,711</td>
<td align="right">123,711</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">98,482</td>
<td align="right">98,482</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">42,221</td>
<td align="right">42,221</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right"></td>
<td align="right">6,877,490,588</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_INT</td>
<td align="right"></td>
<td align="right">5,114,746,770</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_IMMORTAL</td>
<td align="right"></td>
<td align="right">4,966,150,615</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_FLOAT</td>
<td align="right"></td>
<td align="right">3,124,501,446</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_UNICODE</td>
<td align="right"></td>
<td align="right">55,160,060</td>
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
<td align="right">10,661</td>
<td align="right">10,734</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">24,541</td>
<td align="right">24,525</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,489</td>
<td align="right">23,489</td>
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
<td align="right">2,496</td>
<td align="right">2,496</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-12-10
