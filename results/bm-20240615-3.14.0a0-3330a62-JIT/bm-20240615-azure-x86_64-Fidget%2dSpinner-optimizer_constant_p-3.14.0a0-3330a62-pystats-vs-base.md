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
<td align="right">1,541,408</td>
<td align="right">2,424,433</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">1,449,934</td>
<td align="right">2,205,906</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,337,565</td>
<td align="right">2,969,200</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,454,019</td>
<td align="right">10,304,874</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">6,114,432</td>
<td align="right">6,603,190</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">39,881,782</td>
<td align="right">42,342,882</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">6,574,134</td>
<td align="right">6,899,336</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">37,815,864</td>
<td align="right">39,557,960</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">80,519,169</td>
<td align="right">83,550,540</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">363,815,195</td>
<td align="right">373,495,147</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">104,020,745</td>
<td align="right">106,489,068</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">87,341,819</td>
<td align="right">89,411,001</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">31,387,289</td>
<td align="right">32,112,452</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">39,413,972</td>
<td align="right">40,303,333</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,774,376</td>
<td align="right">1,809,034</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">70,583,164</td>
<td align="right">71,745,053</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">151,960</td>
<td align="right">154,440</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,100,933</td>
<td align="right">8,227,955</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">355,238,853</td>
<td align="right">360,617,090</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,308,197</td>
<td align="right">17,560,471</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">105,275,084</td>
<td align="right">106,743,799</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">97,048,771</td>
<td align="right">98,209,283</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">169,857,155</td>
<td align="right">171,836,774</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">110,344,274</td>
<td align="right">111,592,541</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">80,943,986</td>
<td align="right">81,828,964</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">291,538,269</td>
<td align="right">294,597,198</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">110,464,857</td>
<td align="right">111,607,747</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">195,955,037</td>
<td align="right">197,934,977</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">474,823</td>
<td align="right">479,620</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">207,298</td>
<td align="right">209,373</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">389,643,682</td>
<td align="right">393,433,844</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,186,614,893</td>
<td align="right">4,227,120,970</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">622,067,490</td>
<td align="right">627,874,929</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">180,265,730</td>
<td align="right">181,895,766</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">326,500,582</td>
<td align="right">329,247,771</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,265,416,213</td>
<td align="right">1,275,264,002</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">859,422,759</td>
<td align="right">866,032,440</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,147,517,249</td>
<td align="right">1,156,295,947</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">980,569,755</td>
<td align="right">987,565,402</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,536,053</td>
<td align="right">53,900,372</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">321,477,260</td>
<td align="right">323,586,841</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">946,322,469</td>
<td align="right">952,317,102</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">412,931,856</td>
<td align="right">415,520,959</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,544,965,058</td>
<td align="right">1,554,565,823</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,238,133,406</td>
<td align="right">2,251,551,142</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,347,241,736</td>
<td align="right">5,378,864,524</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,561,089,900</td>
<td align="right">20,681,594,319</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,460,868,036</td>
<td align="right">5,491,865,478</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,727,594,487</td>
<td align="right">1,737,313,507</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,160,737</td>
<td align="right">78,596,517</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">65,829,510</td>
<td align="right">66,191,278</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">571,555,655</td>
<td align="right">574,681,202</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,959,744,844</td>
<td align="right">5,991,925,105</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">705,322,800</td>
<td align="right">709,005,151</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">752,577,160</td>
<td align="right">756,351,475</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">362,550,816</td>
<td align="right">364,353,726</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">735,363,169</td>
<td align="right">738,790,257</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">389,868,666</td>
<td align="right">391,668,918</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">98,868,820</td>
<td align="right">99,318,420</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,233,558,081</td>
<td align="right">3,248,240,197</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">132,692,687</td>
<td align="right">133,293,587</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">641,068,673</td>
<td align="right">643,908,945</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">282,639,579</td>
<td align="right">283,876,237</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,491,981</td>
<td align="right">52,717,741</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">105,647,062</td>
<td align="right">106,097,622</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">185,031,270</td>
<td align="right">185,800,145</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">273,529,965</td>
<td align="right">274,665,901</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,774,866,580</td>
<td align="right">5,796,782,517</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">225,091,261</td>
<td align="right">225,932,131</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">365,987,796</td>
<td align="right">367,289,884</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">288,466,195</td>
<td align="right">289,467,729</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,574,516</td>
<td align="right">9,607,748</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,916,641,631</td>
<td align="right">3,929,835,171</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,665,826,042</td>
<td align="right">2,674,799,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">472,794,671</td>
<td align="right">474,334,560</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">209,407,528</td>
<td align="right">210,086,827</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,270,028,914</td>
<td align="right">2,277,222,141</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,931,801,940</td>
<td align="right">3,944,259,530</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,260,730,667</td>
<td align="right">3,270,661,486</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,251,078,289</td>
<td align="right">1,254,818,262</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">658,741,509</td>
<td align="right">660,689,395</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">727,092,659</td>
<td align="right">729,208,987</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">429,843,935</td>
<td align="right">431,084,148</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">586,179,836</td>
<td align="right">587,803,736</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">193,746,031</td>
<td align="right">194,278,592</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">195,444,600</td>
<td align="right">195,958,519</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,126,744,927</td>
<td align="right">1,129,617,880</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">90,629,262</td>
<td align="right">90,856,220</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">90,634,082</td>
<td align="right">90,861,040</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">141,800</td>
<td align="right">142,120</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,928,960</td>
<td align="right">49,026,413</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67,880,384</td>
<td align="right">68,007,131</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">221,425,498</td>
<td align="right">221,814,685</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,685,496</td>
<td align="right">72,811,163</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,691,261</td>
<td align="right">58,791,451</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">147,674,289</td>
<td align="right">147,920,664</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">936,801,232</td>
<td align="right">938,335,171</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">474,758,492</td>
<td align="right">475,502,329</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">357,423,541</td>
<td align="right">357,968,620</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,629,886</td>
<td align="right">13,650,660</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">899,858,916</td>
<td align="right">901,145,720</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,021,169</td>
<td align="right">216,293,954</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">33,114,412</td>
<td align="right">33,155,053</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,091,058,068</td>
<td align="right">4,095,977,923</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">12,945,890</td>
<td align="right">12,960,711</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">12,953,650</td>
<td align="right">12,968,471</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">12,962,706</td>
<td align="right">12,977,364</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,672,439,189</td>
<td align="right">2,675,352,787</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,546,820,516</td>
<td align="right">1,548,079,183</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,363,558,326</td>
<td align="right">1,364,627,031</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">128,883,810</td>
<td align="right">128,970,106</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">397,081,492</td>
<td align="right">397,336,477</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,169,987</td>
<td align="right">19,181,067</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">89,876,839</td>
<td align="right">89,825,573</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,641,144</td>
<td align="right">9,645,805</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">785,082,266</td>
<td align="right">785,461,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,207,058</td>
<td align="right">9,211,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">520,187,016</td>
<td align="right">520,376,789</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,872,459</td>
<td align="right">1,873,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,752,650</td>
<td align="right">1,753,218</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">94,567,149</td>
<td align="right">94,595,894</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">356,400,563</td>
<td align="right">356,498,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">381,519,866</td>
<td align="right">381,621,170</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">22,136,390</td>
<td align="right">22,141,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">278,723,112</td>
<td align="right">278,788,868</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,486</td>
<td align="right">15,489</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,868,131</td>
<td align="right">10,869,982</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">47,905,473</td>
<td align="right">47,913,167</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">214,648</td>
<td align="right">214,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">258,637,920</td>
<td align="right">258,671,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">133,049,141</td>
<td align="right">133,033,407</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,666,305</td>
<td align="right">47,670,308</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,382,110</td>
<td align="right">4,382,430</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,066,065</td>
<td align="right">83,071,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,816,135</td>
<td align="right">40,813,421</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,330,364</td>
<td align="right">1,047,390,871</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,117,499</td>
<td align="right">91,122,328</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">65,812,337</td>
<td align="right">65,815,462</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">104,361,028</td>
<td align="right">104,364,570</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">22,310,002</td>
<td align="right">22,310,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">187,850,906</td>
<td align="right">187,855,958</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,692,579</td>
<td align="right">555,706,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">32,498,477</td>
<td align="right">32,499,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">231,070,800</td>
<td align="right">231,075,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">148,273,666</td>
<td align="right">148,276,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">33,217,534</td>
<td align="right">33,218,146</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,475</td>
<td align="right">687,466</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,037,447</td>
<td align="right">190,039,370</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,280,833</td>
<td align="right">20,281,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">143,282,751</td>
<td align="right">143,282,395</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,554,112</td>
<td align="right">158,554,258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,610,660</td>
<td align="right">46,610,676</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">172,973,216</td>
<td align="right">172,973,242</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,306,504</td>
<td align="right">233,306,525</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,211,060</td>
<td align="right">786,211,076</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">49,527,058</td>
<td align="right">49,527,059</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">257,956,294</td>
<td align="right">257,956,297</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,022,120</td>
<td align="right">402,022,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">228,622,200</td>
<td align="right">228,622,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,640</td>
<td align="right">173,318,640</td>
<td align="right">0.0%</td>
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
<td align="right">12,056,520</td>
<td align="right">12,056,520</td>
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
<td align="left">STORE_SLICE</td>
<td align="right">7,254,160</td>
<td align="right">7,254,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,464,760</td>
<td align="right">3,464,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">2,995,200</td>
<td align="right">2,995,200</td>
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
<td align="right">560,300</td>
<td align="right">560,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">150,560</td>
<td align="right">150,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,600</td>
<td align="right">91,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">90,000</td>
<td align="right">90,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">46,620</td>
<td align="right">46,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">25,780</td>
<td align="right">25,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">22,580</td>
<td align="right">22,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">17,540</td>
<td align="right">17,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,960</td>
<td align="right">1,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">700</td>
<td align="right">700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">600</td>
<td align="right">600</td>
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
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">417,464,136</td>
<td align="right">4.3%</td>
<td align="right">421,253,141</td>
<td align="right">4.3%</td>
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
<td align="right">9,368,380,053</td>
<td align="right">95.7%</td>
<td align="right">9,374,339,276</td>
<td align="right">95.7%</td>
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
<td align="right">29,500,860</td>
<td align="right">0.3%</td>
<td align="right">29,500,860</td>
<td align="right">0.3%</td>
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
<td align="right">1,089,616</td>
<td align="right">64.8%</td>
<td align="right">1,090,721</td>
<td align="right">64.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">590,790</td>
<td align="right">35.2%</td>
<td align="right">590,842</td>
<td align="right">35.1%</td>
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
<td align="left">or</td>
<td align="right">12,155</td>
<td align="right">1.1%</td>
<td align="right">12,492</td>
<td align="right">1.1%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,189</td>
<td align="right">2.7%</td>
<td align="right">29,734</td>
<td align="right">2.7%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">14,160</td>
<td align="right">1.3%</td>
<td align="right">14,248</td>
<td align="right">1.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,899</td>
<td align="right">0.2%</td>
<td align="right">1,893</td>
<td align="right">0.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,844</td>
<td align="right">0.8%</td>
<td align="right">8,865</td>
<td align="right">0.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,528</td>
<td align="right">0.5%</td>
<td align="right">5,535</td>
<td align="right">0.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">39,287</td>
<td align="right">3.6%</td>
<td align="right">39,331</td>
<td align="right">3.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,028</td>
<td align="right">0.5%</td>
<td align="right">5,033</td>
<td align="right">0.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,705</td>
<td align="right">7.5%</td>
<td align="right">81,748</td>
<td align="right">7.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">37,918</td>
<td align="right">3.5%</td>
<td align="right">37,933</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,608</td>
<td align="right">0.8%</td>
<td align="right">8,610</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">4,725</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,096</td>
<td align="right">2.9%</td>
<td align="right">32,100</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,611</td>
<td align="right">71.7%</td>
<td align="right">781,610</td>
<td align="right">71.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,504</td>
<td align="right">1.0%</td>
<td align="right">10,504</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">736,765,714</td>
<td align="right">10.9%</td>
<td align="right">740,191,656</td>
<td align="right">10.9%</td>
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
<td align="right">6,014,291,628</td>
<td align="right">89.1%</td>
<td align="right">6,028,534,654</td>
<td align="right">89.1%</td>
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
<td align="right">1,741,466</td>
<td align="right">0.0%</td>
<td align="right">1,741,606</td>
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
<td align="right">226,439</td>
<td align="right">66.8%</td>
<td align="right">227,718</td>
<td align="right">66.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">112,482</td>
<td align="right">33.2%</td>
<td align="right">112,489</td>
<td align="right">33.1%</td>
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
<td align="left">buffer slice</td>
<td align="right">760</td>
<td align="right">0.3%</td>
<td align="right">840</td>
<td align="right">0.4%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,060</td>
<td align="right">0.5%</td>
<td align="right">1,100</td>
<td align="right">0.5%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">43,880</td>
<td align="right">19.4%</td>
<td align="right">44,760</td>
<td align="right">19.7%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">125</td>
<td align="right">0.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,217</td>
<td align="right">13.3%</td>
<td align="right">30,440</td>
<td align="right">13.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">109,258</td>
<td align="right">48.3%</td>
<td align="right">109,313</td>
<td align="right">48.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,500</td>
<td align="right">8.6%</td>
<td align="right">19,500</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">7.2%</td>
<td align="right">16,200</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.4%</td>
<td align="right">5,340</td>
<td align="right">2.3%</td>
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
<td align="right">164,018,982</td>
<td align="right">1.2%</td>
<td align="right">167,010,833</td>
<td align="right">1.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">680,475,465</td>
<td align="right">5.0%</td>
<td align="right">683,600,156</td>
<td align="right">5.0%</td>
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
<td align="right">12,988,320,178</td>
<td align="right">95.0%</td>
<td align="right">13,018,972,061</td>
<td align="right">95.0%</td>
<td align="right">0.2%</td>
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
<td align="right">28,860</td>
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
<td align="right">3,556,871</td>
<td align="right">95.3%</td>
<td align="right">3,613,430</td>
<td align="right">95.4%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">173,662</td>
<td align="right">4.7%</td>
<td align="right">174,036</td>
<td align="right">4.6%</td>
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
<td align="left">wrong number arguments</td>
<td align="right">8,000</td>
<td align="right">4.6%</td>
<td align="right">8,040</td>
<td align="right">4.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">165,322</td>
<td align="right">95.2%</td>
<td align="right">165,656</td>
<td align="right">95.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,920</td>
<td align="right">1.7%</td>
<td align="right">2,920</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">560</td>
<td align="right">0.3%</td>
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
<tr>
<td align="left">init not python</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">200</td>
<td align="right">0.1%</td>
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
<td align="right">733,844</td>
<td align="right">0.0%</td>
<td align="right">745,418</td>
<td align="right">0.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">97,589,619</td>
<td align="right">1.6%</td>
<td align="right">98,760,676</td>
<td align="right">1.6%</td>
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
<td align="right">6,066,101,520</td>
<td align="right">98.4%</td>
<td align="right">6,084,150,467</td>
<td align="right">98.4%</td>
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
<td align="right">128,898</td>
<td align="right">66.8%</td>
<td align="right">129,706</td>
<td align="right">66.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">64,098</td>
<td align="right">33.2%</td>
<td align="right">64,319</td>
<td align="right">33.1%</td>
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
<td align="left">bytes</td>
<td align="right">800</td>
<td align="right">0.6%</td>
<td align="right">920</td>
<td align="right">0.7%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">500</td>
<td align="right">0.4%</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">24,928</td>
<td align="right">19.3%</td>
<td align="right">25,365</td>
<td align="right">19.6%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,706</td>
<td align="right">9.1%</td>
<td align="right">11,802</td>
<td align="right">9.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,680</td>
<td align="right">14.5%</td>
<td align="right">18,740</td>
<td align="right">14.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,333</td>
<td align="right">11.1%</td>
<td align="right">14,374</td>
<td align="right">11.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,378</td>
<td align="right">12.7%</td>
<td align="right">16,339</td>
<td align="right">12.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">26,268</td>
<td align="right">20.4%</td>
<td align="right">26,320</td>
<td align="right">20.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,425</td>
<td align="right">1.1%</td>
<td align="right">1,426</td>
<td align="right">1.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">8.3%</td>
<td align="right">10,680</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,620</td>
<td align="right">1.3%</td>
<td align="right">1,620</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,580</td>
<td align="right">1.2%</td>
<td align="right">1,580</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">197,806,741</td>
<td align="right">7.6%</td>
<td align="right">198,320,269</td>
<td align="right">7.6%</td>
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
<td align="right">2,411,944,528</td>
<td align="right">92.4%</td>
<td align="right">2,416,859,170</td>
<td align="right">92.4%</td>
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
<td align="right">2,517,260</td>
<td align="right">0.1%</td>
<td align="right">2,517,260</td>
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
<td align="right">96,321</td>
<td align="right">62.1%</td>
<td align="right">96,710</td>
<td align="right">62.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">58,798</td>
<td align="right">37.9%</td>
<td align="right">58,800</td>
<td align="right">37.8%</td>
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
<td align="right">8,340</td>
<td align="right">8.7%</td>
<td align="right">8,460</td>
<td align="right">8.7%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">21,838</td>
<td align="right">22.7%</td>
<td align="right">22,078</td>
<td align="right">22.8%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,783</td>
<td align="right">13.3%</td>
<td align="right">12,812</td>
<td align="right">13.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">53,360</td>
<td align="right">55.4%</td>
<td align="right">53,360</td>
<td align="right">55.2%</td>
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
<td align="right">134,853</td>
<td align="right">0.0%</td>
<td align="right">153,923</td>
<td align="right">0.0%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">459,698,836</td>
<td align="right">49.2%</td>
<td align="right">462,736,274</td>
<td align="right">49.3%</td>
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
<td align="right">474,659,136</td>
<td align="right">50.8%</td>
<td align="right">475,420,928</td>
<td align="right">50.7%</td>
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
<td align="right">45,949</td>
<td align="right">19.6%</td>
<td align="right">46,346</td>
<td align="right">19.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">188,260</td>
<td align="right">80.4%</td>
<td align="right">188,978</td>
<td align="right">80.3%</td>
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
<td align="left">reversed list</td>
<td align="right">3,760</td>
<td align="right">2.0%</td>
<td align="right">3,860</td>
<td align="right">2.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">34,879</td>
<td align="right">18.5%</td>
<td align="right">35,371</td>
<td align="right">18.7%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">9,979</td>
<td align="right">5.3%</td>
<td align="right">10,081</td>
<td align="right">5.3%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">476</td>
<td align="right">0.3%</td>
<td align="right">479</td>
<td align="right">0.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,480</td>
<td align="right">3.4%</td>
<td align="right">6,500</td>
<td align="right">3.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,766</td>
<td align="right">5.2%</td>
<td align="right">9,767</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,840</td>
<td align="right">55.7%</td>
<td align="right">104,840</td>
<td align="right">55.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,240</td>
<td align="right">3.3%</td>
<td align="right">6,240</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">4,240</td>
<td align="right">2.3%</td>
<td align="right">4,240</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,580</td>
<td align="right">1.9%</td>
<td align="right">3,580</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">2,020</td>
<td align="right">1.1%</td>
<td align="right">2,020</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,220</td>
<td align="right">0.6%</td>
<td align="right">1,220</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">560</td>
<td align="right">0.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,449,466,995</td>
<td align="right">92.5%</td>
<td align="right">15,538,484,487</td>
<td align="right">92.5%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,240,158,212</td>
<td align="right">7.4%</td>
<td align="right">1,247,153,535</td>
<td align="right">7.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">265,894,410</td>
<td align="right">1.6%</td>
<td align="right">265,898,144</td>
<td align="right">1.6%</td>
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
<td align="right">319,640</td>
<td align="right">0.0%</td>
<td align="right">319,640</td>
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
<td align="right">763,602</td>
<td align="right">12.1%</td>
<td align="right">767,617</td>
<td align="right">12.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,542,351</td>
<td align="right">87.9%</td>
<td align="right">5,542,394</td>
<td align="right">87.8%</td>
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
<td align="right">5,438</td>
<td align="right">0.7%</td>
<td align="right">5,564</td>
<td align="right">0.7%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">75,169</td>
<td align="right">9.8%</td>
<td align="right">76,749</td>
<td align="right">10.0%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">19,740</td>
<td align="right">2.6%</td>
<td align="right">19,880</td>
<td align="right">2.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">45,151</td>
<td align="right">5.9%</td>
<td align="right">45,469</td>
<td align="right">5.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">54,897</td>
<td align="right">7.2%</td>
<td align="right">55,260</td>
<td align="right">7.2%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">13,860</td>
<td align="right">1.8%</td>
<td align="right">13,940</td>
<td align="right">1.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">13,416</td>
<td align="right">1.8%</td>
<td align="right">13,468</td>
<td align="right">1.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">250,280</td>
<td align="right">32.8%</td>
<td align="right">251,249</td>
<td align="right">32.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">25,860</td>
<td align="right">3.4%</td>
<td align="right">25,960</td>
<td align="right">3.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,200</td>
<td align="right">1.6%</td>
<td align="right">12,240</td>
<td align="right">1.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">73,231</td>
<td align="right">9.6%</td>
<td align="right">73,336</td>
<td align="right">9.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">148,860</td>
<td align="right">19.5%</td>
<td align="right">149,002</td>
<td align="right">19.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,840</td>
<td align="right">2.1%</td>
<td align="right">15,840</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,120</td>
<td align="right">0.7%</td>
<td align="right">5,120</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,780</td>
<td align="right">0.4%</td>
<td align="right">2,780</td>
<td align="right">0.4%</td>
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
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
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
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">403,924</td>
<td align="right">0.0%</td>
<td align="right">407,752</td>
<td align="right">0.0%</td>
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
<td align="right">5,604,949,801</td>
<td align="right">99.6%</td>
<td align="right">5,626,821,300</td>
<td align="right">99.6%</td>
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
<td align="right">20,254,358</td>
<td align="right">0.4%</td>
<td align="right">20,258,228</td>
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
<td align="right">10,780</td>
<td align="right">0.0%</td>
<td align="right">10,780</td>
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
<td align="right">430,399</td>
<td align="right">100.0%</td>
<td align="right">430,544</td>
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
<td align="right">82,748,282</td>
<td align="right">100.0%</td>
<td align="right">83,667,918</td>
<td align="right">100.0%</td>
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
<td align="right">7,886</td>
<td align="right">0.0%</td>
<td align="right">7,889</td>
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
<td align="right">7,600</td>
<td align="right">100.0%</td>
<td align="right">7,600</td>
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
<td align="right">786,180,400</td>
<td align="right">81.9%</td>
<td align="right">786,180,416</td>
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
<td align="right">173,284,300</td>
<td align="right">18.1%</td>
<td align="right">173,284,300</td>
<td align="right">18.1%</td>
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
<td align="right">5,400</td>
<td align="right">8.3%</td>
<td align="right">5,400</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
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
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">9,960</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">98,795,000</td>
<td align="right">3.6%</td>
<td align="right">99,542,826</td>
<td align="right">3.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,661,489,310</td>
<td align="right">96.4%</td>
<td align="right">2,671,442,063</td>
<td align="right">96.4%</td>
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
<td align="right">68,854,445</td>
<td align="right">2.5%</td>
<td align="right">68,878,091</td>
<td align="right">2.5%</td>
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
<td align="right">61,808</td>
<td align="right">4.3%</td>
<td align="right">62,370</td>
<td align="right">4.3%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,384,926</td>
<td align="right">95.7%</td>
<td align="right">1,385,347</td>
<td align="right">95.7%</td>
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
<td align="left">property</td>
<td align="right">2,480</td>
<td align="right">4.0%</td>
<td align="right">2,720</td>
<td align="right">4.4%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,580</td>
<td align="right">13.9%</td>
<td align="right">8,740</td>
<td align="right">14.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,700</td>
<td align="right">7.6%</td>
<td align="right">4,740</td>
<td align="right">7.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">12,920</td>
<td align="right">20.9%</td>
<td align="right">13,000</td>
<td align="right">20.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">9,800</td>
<td align="right">15.9%</td>
<td align="right">9,840</td>
<td align="right">15.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,768</td>
<td align="right">15.8%</td>
<td align="right">9,770</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,480</td>
<td align="right">7.2%</td>
<td align="right">4,480</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,360</td>
<td align="right">7.1%</td>
<td align="right">4,360</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3,800</td>
<td align="right">6.1%</td>
<td align="right">3,800</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">800</td>
<td align="right">1.3%</td>
<td align="right">800</td>
<td align="right">1.3%</td>
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
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
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
<td align="right">817,816,676</td>
<td align="right">78.0%</td>
<td align="right">820,323,718</td>
<td align="right">78.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">230,968,725</td>
<td align="right">22.0%</td>
<td align="right">230,973,080</td>
<td align="right">22.0%</td>
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
<td align="right">10,662</td>
<td align="right">10.4%</td>
<td align="right">10,668</td>
<td align="right">10.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">91,413</td>
<td align="right">89.6%</td>
<td align="right">91,457</td>
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
<td align="left">dict subclass no override</td>
<td align="right">7,512</td>
<td align="right">8.2%</td>
<td align="right">7,517</td>
<td align="right">8.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">32,521</td>
<td align="right">35.6%</td>
<td align="right">32,540</td>
<td align="right">35.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,180</td>
<td align="right">47.2%</td>
<td align="right">43,200</td>
<td align="right">47.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">7.1%</td>
<td align="right">6,480</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">920</td>
<td align="right">1.0%</td>
<td align="right">920</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">800</td>
<td align="right">0.9%</td>
<td align="right">800</td>
<td align="right">0.9%</td>
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
<td align="right">273,126,583</td>
<td align="right">4.5%</td>
<td align="right">273,998,842</td>
<td align="right">4.5%</td>
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
<td align="right">5,764,446,405</td>
<td align="right">95.5%</td>
<td align="right">5,782,407,489</td>
<td align="right">95.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,314,393</td>
<td align="right">0.8%</td>
<td align="right">49,346,919</td>
<td align="right">0.8%</td>
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
<td align="right">171,991</td>
<td align="right">13.4%</td>
<td align="right">172,499</td>
<td align="right">13.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,107,080</td>
<td align="right">86.6%</td>
<td align="right">1,107,709</td>
<td align="right">86.5%</td>
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
<td align="left">dict</td>
<td align="right">12,780</td>
<td align="right">7.4%</td>
<td align="right">12,900</td>
<td align="right">7.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,430</td>
<td align="right">2.6%</td>
<td align="right">4,465</td>
<td align="right">2.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">47,919</td>
<td align="right">27.9%</td>
<td align="right">48,104</td>
<td align="right">27.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,202</td>
<td align="right">7.7%</td>
<td align="right">13,245</td>
<td align="right">7.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,118</td>
<td align="right">7.6%</td>
<td align="right">13,160</td>
<td align="right">7.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">26,805</td>
<td align="right">15.6%</td>
<td align="right">26,855</td>
<td align="right">15.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">4,821</td>
<td align="right">2.8%</td>
<td align="right">4,826</td>
<td align="right">2.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">45,996</td>
<td align="right">26.7%</td>
<td align="right">46,024</td>
<td align="right">26.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,498,137,057</td>
<td align="right">100.0%</td>
<td align="right">1,499,370,755</td>
<td align="right">100.0%</td>
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
<td align="right">186,469</td>
<td align="right">0.0%</td>
<td align="right">186,490</td>
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
<td align="right">1,779</td>
<td align="right">6.3%</td>
<td align="right">1,773</td>
<td align="right">6.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">26,400</td>
<td align="right">93.7%</td>
<td align="right">26,416</td>
<td align="right">93.7%</td>
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
<td align="right">1,139</td>
<td align="right">64.0%</td>
<td align="right">1,133</td>
<td align="right">63.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">21.4%</td>
<td align="right">380</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.6%</td>
<td align="right">260</td>
<td align="right">14.7%</td>
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
<td align="right">11,344,441,510</td>
<td align="right">9.7%</td>
<td align="right">11,405,375,102</td>
<td align="right">9.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">41,048,297,282</td>
<td align="right">35.1%</td>
<td align="right">41,254,887,315</td>
<td align="right">35.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">661,019,607</td>
<td align="right">0.6%</td>
<td align="right">664,106,150</td>
<td align="right">0.6%</td>
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
<td align="right">63,809,824,403</td>
<td align="right">54.6%</td>
<td align="right">64,083,870,781</td>
<td align="right">54.6%</td>
<td align="right">0.4%</td>
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
<td align="right">417,464,136</td>
<td align="right">9.0%</td>
<td align="right">421,253,141</td>
<td align="right">9.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">98,795,000</td>
<td align="right">2.1%</td>
<td align="right">99,542,826</td>
<td align="right">2.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,240,158,212</td>
<td align="right">26.7%</td>
<td align="right">1,247,153,535</td>
<td align="right">26.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">736,765,714</td>
<td align="right">15.9%</td>
<td align="right">740,191,656</td>
<td align="right">15.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">680,475,465</td>
<td align="right">14.7%</td>
<td align="right">683,600,156</td>
<td align="right">14.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">273,126,583</td>
<td align="right">5.9%</td>
<td align="right">273,998,842</td>
<td align="right">5.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">197,806,741</td>
<td align="right">4.3%</td>
<td align="right">198,320,269</td>
<td align="right">4.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">474,659,136</td>
<td align="right">10.2%</td>
<td align="right">475,420,928</td>
<td align="right">10.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">230,968,725</td>
<td align="right">5.0%</td>
<td align="right">230,973,080</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,300</td>
<td align="right">3.7%</td>
<td align="right">173,284,300</td>
<td align="right">3.7%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">85,150,764</td>
<td align="right">11.5%</td>
<td align="right">87,465,063</td>
<td align="right">11.8%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">24,518,736</td>
<td align="right">3.3%</td>
<td align="right">24,698,254</td>
<td align="right">3.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,191,442</td>
<td align="right">3.4%</td>
<td align="right">25,213,170</td>
<td align="right">3.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,983,144</td>
<td align="right">5.5%</td>
<td align="right">40,978,508</td>
<td align="right">5.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,643,583</td>
<td align="right">5.9%</td>
<td align="right">43,645,501</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">70,356,802</td>
<td align="right">9.5%</td>
<td align="right">70,359,241</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,481,213</td>
<td align="right">3.7%</td>
<td align="right">27,481,390</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,874,510</td>
<td align="right">10.5%</td>
<td align="right">77,874,684</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,874,510</td>
<td align="right">10.5%</td>
<td align="right">77,874,684</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">121,603,789</td>
<td align="right">16.5%</td>
<td align="right">121,604,001</td>
<td align="right">16.4%</td>
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
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,617,280,163</td>
<td align="right">67.7%</td>
<td align="right">5,639,481,485</td>
<td align="right">67.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,588,569,901</td>
<td align="right">79.5%</td>
<td align="right">6,612,841,163</td>
<td align="right">79.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">369,527,150</td>
<td align="right">4.5%</td>
<td align="right">370,517,019</td>
<td align="right">4.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,810,146,456</td>
<td align="right">21.8%</td>
<td align="right">1,813,033,595</td>
<td align="right">21.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,814,580,676</td>
<td align="right">21.9%</td>
<td align="right">1,817,467,815</td>
<td align="right">21.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,674,882,595</td>
<td align="right">32.3%</td>
<td align="right">2,677,796,117</td>
<td align="right">32.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,674,882,595</td>
<td align="right">32.3%</td>
<td align="right">2,677,796,117</td>
<td align="right">32.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,548,618</td>
<td align="right">0.9%</td>
<td align="right">71,562,207</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">526,870,403</td>
<td align="right">6.4%</td>
<td align="right">526,918,941</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">28,576,467</td>
<td align="right">0.3%</td>
<td align="right">28,577,871</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,301,919</td>
<td align="right">10.4%</td>
<td align="right">860,328,302</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,357,653</td>
<td align="right">2.5%</td>
<td align="right">211,357,843</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,411,640</td>
<td align="right">0.1%</td>
<td align="right">4,411,640</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">22,580</td>
<td align="right">0.0%</td>
<td align="right">22,580</td>
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
<td align="right">9,388,159</td>
<td align="right"></td>
<td align="right">7,633,387</td>
<td align="right"></td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">26,819,408</td>
<td align="right"></td>
<td align="right">25,693,138</td>
<td align="right"></td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">19,836,740</td>
<td align="right"></td>
<td align="right">20,573,461</td>
<td align="right"></td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">149,532,349</td>
<td align="right"></td>
<td align="right">150,280,364</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">50,649,857,054</td>
<td align="right">37.0%</td>
<td align="right">50,877,736,700</td>
<td align="right">37.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">68,091,429,351</td>
<td align="right">42.8%</td>
<td align="right">68,360,428,113</td>
<td align="right">42.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,625,392,034</td>
<td align="right"></td>
<td align="right">2,635,259,283</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,044,746</td>
<td align="right">0.1%</td>
<td align="right">20,118,962</td>
<td align="right">0.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,120,893,598</td>
<td align="right"></td>
<td align="right">13,144,842,459</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,392,640,874</td>
<td align="right">55.1%</td>
<td align="right">12,415,225,351</td>
<td align="right">55.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,268,740,616</td>
<td align="right">54.5%</td>
<td align="right">12,291,070,352</td>
<td align="right">54.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,855,512</td>
<td align="right">0.5%</td>
<td align="right">104,036,037</td>
<td align="right">0.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">86,123,497,229</td>
<td align="right">63.0%</td>
<td align="right">86,256,900,461</td>
<td align="right">62.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,280,915,915</td>
<td align="right"></td>
<td align="right">4,287,314,900</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">91,129,753,432</td>
<td align="right">57.2%</td>
<td align="right">91,253,749,794</td>
<td align="right">57.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,102,233,271</td>
<td align="right"></td>
<td align="right">10,115,065,095</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,100,427,191</td>
<td align="right">44.9%</td>
<td align="right">10,113,227,537</td>
<td align="right">44.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,270,980</td>
<td align="right">2.2%</td>
<td align="right">3,270,980</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">63,660</td>
<td align="right">0.0%</td>
<td align="right">63,660</td>
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
<td align="right">18,576,020</td>
<td align="right">18,536,744,893</td>
<td align="right">0</td>
<td align="right">19,252,320</td>
<td align="right">18,529,941,071</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,985,376,904</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,985,314,880</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">636</td>
<td align="right">0.1%</td>
<td align="right">790</td>
<td align="right">0.1%</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">11,954</td>
<td align="right">1.1%</td>
<td align="right">12,007</td>
<td align="right">1.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">108,203</td>
<td align="right">9.6%</td>
<td align="right">108,445</td>
<td align="right">9.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">45,090</td>
<td align="right">4.0%</td>
<td align="right">45,159</td>
<td align="right">4.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,129,265</td>
<td align="right"></td>
<td align="right">1,130,985</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,021,062</td>
<td align="right">90.4%</td>
<td align="right">1,022,540</td>
<td align="right">90.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">10,640,722,497</td>
<td align="right"></td>
<td align="right">10,654,043,706</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">428,604</td>
<td align="right">38.0%</td>
<td align="right">429,123</td>
<td align="right">37.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,323</td>
<td align="right">5.8%</td>
<td align="right">6,329</td>
<td align="right">5.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">242,903,335,676</td>
<td align="right">2,282.8%</td>
<td align="right">243,106,112,647</td>
<td align="right">2,281.8%</td>
<td align="right">0.1%</td>
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
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,360</td>
<td align="right">0.1%</td>
<td align="right">1,360</td>
<td align="right">0.1%</td>
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
<td align="right">96,109</td>
<td align="right">88.8%</td>
<td align="right">96,360</td>
<td align="right">88.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">108,203</td>
<td align="right"></td>
<td align="right">108,445</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,300</td>
<td align="right">2.1%</td>
<td align="right">2,303</td>
<td align="right">2.1%</td>
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
<td align="right">4,394</td>
<td align="right">4.1%</td>
<td align="right">4,395</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">18,663</td>
<td align="right">17.2%</td>
<td align="right">18,695</td>
<td align="right">17.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">31,953</td>
<td align="right">29.5%</td>
<td align="right">32,000</td>
<td align="right">29.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">26,416</td>
<td align="right">24.4%</td>
<td align="right">26,470</td>
<td align="right">24.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">18,991</td>
<td align="right">17.6%</td>
<td align="right">19,022</td>
<td align="right">17.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,146</td>
<td align="right">5.7%</td>
<td align="right">6,223</td>
<td align="right">5.7%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,480</td>
<td align="right">1.4%</td>
<td align="right">1,480</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">160</td>
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
<td align="right">3,514</td>
<td align="right">3.2%</td>
<td align="right">3,515</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">13,180</td>
<td align="right">12.2%</td>
<td align="right">13,185</td>
<td align="right">12.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,504</td>
<td align="right">19.9%</td>
<td align="right">21,574</td>
<td align="right">19.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">31,856</td>
<td align="right">29.4%</td>
<td align="right">31,894</td>
<td align="right">29.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">15,751</td>
<td align="right">14.6%</td>
<td align="right">15,831</td>
<td align="right">14.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,464</td>
<td align="right">6.9%</td>
<td align="right">7,501</td>
<td align="right">6.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,480</td>
<td align="right">2.3%</td>
<td align="right">2,500</td>
<td align="right">2.3%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">360</td>
<td align="right">0.3%</td>
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
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">17,200</td>
<td align="right">36,000</td>
<td align="right">109.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,919,540</td>
<td align="right">140</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">7,891,700</td>
<td align="right">6,405,680</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">7,908,960</td>
<td align="right">6,441,740</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">22,284,220</td>
<td align="right">25,717,580</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">59,827,758</td>
<td align="right">63,261,031</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">88,407,874</td>
<td align="right">91,867,730</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">88,650,494</td>
<td align="right">92,110,350</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,768,415</td>
<td align="right">5,894,996</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">324,839,935</td>
<td align="right">328,965,083</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,109,418</td>
<td align="right">10,234,897</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,236,192,274</td>
<td align="right">2,257,680,239</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">114,548,726</td>
<td align="right">115,592,255</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,213,311,814</td>
<td align="right">2,231,366,419</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">178,687,694</td>
<td align="right">179,623,096</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">253,498,076</td>
<td align="right">254,635,583</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">254,725,336</td>
<td align="right">255,862,843</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">375,524,373</td>
<td align="right">376,959,638</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">445,247</td>
<td align="right">446,897</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">71,144,829</td>
<td align="right">71,397,678</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,386,263,433</td>
<td align="right">6,405,699,784</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">227,005,207</td>
<td align="right">227,691,004</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,354,590</td>
<td align="right">11,387,093</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,354,590</td>
<td align="right">11,387,093</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">123,129,323</td>
<td align="right">123,470,471</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,851,912,604</td>
<td align="right">1,856,621,877</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,134,010</td>
<td align="right">31,076,668</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">177,906,792</td>
<td align="right">178,231,915</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,108,131,685</td>
<td align="right">6,119,182,449</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">543,275,260</td>
<td align="right">544,187,285</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">135,789,923</td>
<td align="right">136,008,090</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">757,387,576</td>
<td align="right">758,590,725</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,914,132,039</td>
<td align="right">1,917,142,526</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">173,285,499</td>
<td align="right">173,551,092</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">878,601,657</td>
<td align="right">879,913,735</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,607,741,825</td>
<td align="right">1,609,866,793</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">552,928,422</td>
<td align="right">553,651,306</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">3,688,566,409</td>
<td align="right">3,693,246,568</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,612,885,790</td>
<td align="right">5,605,775,619</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,952,156,088</td>
<td align="right">6,960,797,138</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,225,464,606</td>
<td align="right">6,233,120,710</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">977,919,159</td>
<td align="right">979,106,066</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,414,308,119</td>
<td align="right">6,421,770,426</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">27,682,381</td>
<td align="right">27,714,128</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,799,606,493</td>
<td align="right">1,801,573,451</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,326,219</td>
<td align="right">126,462,445</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">185,436,027</td>
<td align="right">185,631,299</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,663,838,614</td>
<td align="right">1,665,587,311</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">187,961,143</td>
<td align="right">188,156,535</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">958,952,529</td>
<td align="right">959,902,293</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">908,175,165</td>
<td align="right">909,072,721</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">285,021,570</td>
<td align="right">285,295,394</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,137,397,482</td>
<td align="right">1,138,488,372</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,362,687,353</td>
<td align="right">1,363,992,402</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,063,540,836</td>
<td align="right">17,079,357,589</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,066,997</td>
<td align="right">134,188,576</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,066,997</td>
<td align="right">134,188,576</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,818,527,855</td>
<td align="right">1,820,166,106</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,237,452,202</td>
<td align="right">1,238,543,092</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">232,150,714</td>
<td align="right">231,948,096</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,256,110,102</td>
<td align="right">1,257,200,992</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">402,727,070</td>
<td align="right">403,068,067</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">995,992,460</td>
<td align="right">996,807,720</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">360,163,964</td>
<td align="right">359,872,580</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">681,991,895</td>
<td align="right">681,450,748</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">118,328,757</td>
<td align="right">118,422,531</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">1,911,074</td>
<td align="right">1,912,493</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">400,208,524</td>
<td align="right">399,917,140</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,251,755,171</td>
<td align="right">2,253,386,345</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,010,006,393</td>
<td align="right">7,014,987,562</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,974,209,292</td>
<td align="right">1,975,599,197</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">715,333,673</td>
<td align="right">715,826,919</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">357,249,201</td>
<td align="right">357,491,123</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">14,907,351,746</td>
<td align="right">14,917,278,258</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">394,350,373</td>
<td align="right">394,605,995</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,524,746,089</td>
<td align="right">1,525,716,621</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,479,406</td>
<td align="right">78,429,702</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">22,030,287</td>
<td align="right">22,016,450</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">151,007,797</td>
<td align="right">150,915,401</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,290,915</td>
<td align="right">89,241,084</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,831,888,070</td>
<td align="right">1,832,899,341</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,672,873,185</td>
<td align="right">3,674,882,201</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,899,860,239</td>
<td align="right">2,901,445,574</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,464,300,743</td>
<td align="right">3,466,165,147</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,088,615,651</td>
<td align="right">2,089,731,106</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,151,678</td>
<td align="right">1,335,864,489</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">93,445,268</td>
<td align="right">93,395,544</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,431,819</td>
<td align="right">93,382,103</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,259,757,045</td>
<td align="right">4,261,990,800</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,947,814</td>
<td align="right">779,320,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">779,485,134</td>
<td align="right">779,857,525</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,046,144,038</td>
<td align="right">1,046,637,304</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,682,070,196</td>
<td align="right">1,682,817,910</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">133,706,469</td>
<td align="right">133,765,431</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,104,831,709</td>
<td align="right">2,105,582,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,005,568</td>
<td align="right">733,252,143</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,056,813,542</td>
<td align="right">13,061,036,569</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,308,749,411</td>
<td align="right">1,309,160,939</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">112,293,496</td>
<td align="right">112,325,970</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,062,164,457</td>
<td align="right">3,062,994,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">342,892,848</td>
<td align="right">342,800,741</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">915,688,409</td>
<td align="right">915,927,562</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,236,116,825</td>
<td align="right">1,236,436,311</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,008,888,437</td>
<td align="right">1,009,114,699</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,165,457,875</td>
<td align="right">2,165,924,492</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,353,247,312</td>
<td align="right">3,353,940,578</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">968,226,367</td>
<td align="right">968,405,484</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">320,718,226</td>
<td align="right">320,660,855</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,294,260</td>
<td align="right">91,309,632</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">563,356,422</td>
<td align="right">563,450,695</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,011,476,044</td>
<td align="right">1,011,645,056</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,894,024,284</td>
<td align="right">1,894,302,595</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">930,152,560</td>
<td align="right">930,283,270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,940,320</td>
<td align="right">144,959,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">811,005,726</td>
<td align="right">811,106,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">646,876,253</td>
<td align="right">646,952,994</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,631,184,394</td>
<td align="right">9,632,289,938</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">625,558,908</td>
<td align="right">625,487,557</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,734,346,373</td>
<td align="right">4,734,882,869</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,612,651,765</td>
<td align="right">3,613,041,688</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,811,091,519</td>
<td align="right">1,811,284,936</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">330,420,806</td>
<td align="right">330,385,915</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">48,459,097</td>
<td align="right">48,454,075</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,458,595,701</td>
<td align="right">2,458,849,379</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,606,076,558</td>
<td align="right">1,606,215,869</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">860,388,302</td>
<td align="right">860,319,954</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,627,595,218</td>
<td align="right">4,627,939,061</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,831,267,170</td>
<td align="right">2,831,471,936</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">893,669,459</td>
<td align="right">893,733,117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,635,720</td>
<td align="right">5,636,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">768,171,894</td>
<td align="right">768,129,742</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">6,583,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,359,912,040</td>
<td align="right">4,360,121,868</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,314,652,493</td>
<td align="right">1,314,712,469</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">93,665,820</td>
<td align="right">93,669,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,170,175,624</td>
<td align="right">3,170,288,693</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,890,421</td>
<td align="right">4,890,253</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,628,796,198</td>
<td align="right">2,628,869,208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">236,348,767</td>
<td align="right">236,343,310</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,077,365,895</td>
<td align="right">1,077,387,608</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,101,561,022</td>
<td align="right">1,101,579,169</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,692,856</td>
<td align="right">909,706,128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">142,596,140</td>
<td align="right">142,598,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">280,346,197</td>
<td align="right">280,349,853</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,549,860</td>
<td align="right">1,144,563,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,401,090</td>
<td align="right">32,400,784</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,571,420</td>
<td align="right">80,571,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,202,031</td>
<td align="right">10,202,092</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,365,270</td>
<td align="right">203,366,463</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,213,747</td>
<td align="right">97,214,293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,171,087</td>
<td align="right">98,171,633</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">227,820,926</td>
<td align="right">227,821,955</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">643,367,939</td>
<td align="right">643,365,517</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,022,516</td>
<td align="right">22,022,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,816,300</td>
<td align="right">61,816,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,881,743,432</td>
<td align="right">1,881,746,957</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,029,000</td>
<td align="right">199,029,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,756,268</td>
<td align="right">229,755,954</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">163,692,799</td>
<td align="right">163,692,585</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,278,464,953</td>
<td align="right">1,278,466,484</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">213,613,460</td>
<td align="right">213,613,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,193,564</td>
<td align="right">101,193,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">148,671,469</td>
<td align="right">148,671,382</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,638,156</td>
<td align="right">384,637,988</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,198,145</td>
<td align="right">101,198,181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">47,971,810</td>
<td align="right">47,971,794</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,281,657</td>
<td align="right">54,281,641</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">101,766,730</td>
<td align="right">101,766,714</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,070,105</td>
<td align="right">35,070,102</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,165</td>
<td align="right">645,067,201</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,257,045</td>
<td align="right">68,257,042</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">588,457,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,073,140</td>
<td align="right">533,073,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,717,980</td>
<td align="right">509,717,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">230,436,740</td>
<td align="right">230,436,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,548,560</td>
<td align="right">187,548,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,868,340</td>
<td align="right">149,868,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">99,651,520</td>
<td align="right">99,651,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">66,196,660</td>
<td align="right">66,196,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">64,886,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">63,424,460</td>
<td align="right">63,424,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">58,060,100</td>
<td align="right">58,060,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">57,950,460</td>
<td align="right">57,950,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">53,794,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">46,348,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,693,140</td>
<td align="right">12,693,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,134,220</td>
<td align="right">8,134,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,625,240</td>
<td align="right">4,625,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,671,180</td>
<td align="right">3,671,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">2,714,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,935,140</td>
<td align="right">1,935,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,881,420</td>
<td align="right">1,881,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,543,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,160</td>
<td align="right">821,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">647,420</td>
<td align="right">647,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">543,380</td>
<td align="right">543,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">71,600</td>
<td align="right">71,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">34,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">29,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">7,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right"></td>
<td align="right">1,486,020</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">480</td>
<td align="right">500</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,488</td>
<td align="right">6,521</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">1,402</td>
<td align="right">1,406</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">478,878</td>
<td align="right">479,710</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40,699</td>
<td align="right">40,674</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">32,220</td>
<td align="right">32,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">29,100</td>
<td align="right">29,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,341</td>
<td align="right">5,341</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,398</td>
<td align="right">2,398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,360</td>
<td align="right">2,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,620</td>
<td align="right">1,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,340</td>
<td align="right">1,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">540</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">360</td>
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
<td align="right">1,082</td>
<td align="right">1,083</td>
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
<td align="right">1,082</td>
<td align="right">1,083</td>
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
<td align="right">360</td>
<td align="right">360</td>
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
<td align="right">1,880</td>
<td align="right">1,880</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-06-19
