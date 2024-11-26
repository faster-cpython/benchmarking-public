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
<td align="right">392,756</td>
<td align="right">2,534,085</td>
<td align="right">545.2%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">76,798</td>
<td align="right">60</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,686,999</td>
<td align="right">2,315</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,750</td>
<td align="right">825</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,288,654</td>
<td align="right">42,113</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,387</td>
<td align="right">109</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">472,377</td>
<td align="right">6,294</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">158,428</td>
<td align="right">4,859</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">741,530</td>
<td align="right">25,195</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">117,056</td>
<td align="right">6,780</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,282,990</td>
<td align="right">84,681</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">10,825,600</td>
<td align="right">1,685,255</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,646,553</td>
<td align="right">950,358</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,907,776</td>
<td align="right">502,180</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">12,121,067</td>
<td align="right">2,123,675</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,882,978</td>
<td align="right">1,065,622</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">136,473</td>
<td align="right">25,184</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">32,048</td>
<td align="right">5,975</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">11,749,455</td>
<td align="right">2,494,526</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,886,353</td>
<td align="right">404,967</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">610,258</td>
<td align="right">141,456</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">750,621</td>
<td align="right">182,545</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">4,617,446</td>
<td align="right">1,152,580</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,905</td>
<td align="right">6,666</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">13,750,183</td>
<td align="right">3,709,921</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">151,245</td>
<td align="right">41,828</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">253,749</td>
<td align="right">71,259</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,736,002</td>
<td align="right">2,590,625</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,495,681</td>
<td align="right">449,360</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">38,269,374</td>
<td align="right">11,517,094</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,265,634</td>
<td align="right">411,468</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">128,285,735</td>
<td align="right">41,975,890</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,656,702</td>
<td align="right">2,516,033</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">84,414</td>
<td align="right">28,473</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">9,370,287</td>
<td align="right">3,244,038</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">14,297,470</td>
<td align="right">5,262,541</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,465,187</td>
<td align="right">1,645,168</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,821,620</td>
<td align="right">1,047,759</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,201,772</td>
<td align="right">450,472</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,397,476</td>
<td align="right">11,544,935</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">671,823</td>
<td align="right">279,684</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">266,244</td>
<td align="right">113,870</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,495,209</td>
<td align="right">1,078,706</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,513,653</td>
<td align="right">2,013,372</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">61,973,000</td>
<td align="right">27,796,138</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80,946,542</td>
<td align="right">36,399,405</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">544,923</td>
<td align="right">248,602</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,538,716</td>
<td align="right">710,738</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,909,374</td>
<td align="right">1,360,909</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">162,479</td>
<td align="right">77,782</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">117,009,131</td>
<td align="right">176,096,391</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,152,822</td>
<td align="right">1,615,519</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,948,083</td>
<td align="right">3,657,823</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,486,108</td>
<td align="right">786,699</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">341,232</td>
<td align="right">181,154</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,063,222</td>
<td align="right">1,111,967</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,334,191</td>
<td align="right">4,507,180</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">42,821,670</td>
<td align="right">23,275,162</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,666,398</td>
<td align="right">3,100,058</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">34,490,063</td>
<td align="right">19,094,958</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">814,256</td>
<td align="right">454,888</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">134,434</td>
<td align="right">75,342</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,131,253</td>
<td align="right">647,958</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,610,044</td>
<td align="right">2,652,312</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">15,460,756</td>
<td align="right">9,049,082</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">142,252</td>
<td align="right">83,436</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">10,999,964</td>
<td align="right">6,482,914</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">243,448</td>
<td align="right">146,543</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">191,216</td>
<td align="right">117,355</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">31,327,813</td>
<td align="right">19,334,965</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">96,395,805</td>
<td align="right">60,197,074</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,019,670</td>
<td align="right">1,264,778</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,912,311</td>
<td align="right">3,086,337</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">448,599,928</td>
<td align="right">282,494,435</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">28,038,124</td>
<td align="right">17,798,536</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,383,960</td>
<td align="right">890,771</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">78,657,598</td>
<td align="right">50,655,167</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">106,826,116</td>
<td align="right">69,158,310</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,088,912</td>
<td align="right">724,369</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,877,226</td>
<td align="right">6,577,165</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,484,194</td>
<td align="right">2,322,556</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,448,101</td>
<td align="right">3,006,744</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">3,289,107</td>
<td align="right">2,227,366</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,776,311</td>
<td align="right">14,325,630</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">1,211,866</td>
<td align="right">836,086</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,351,877</td>
<td align="right">2,329,765</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">91,331,018</td>
<td align="right">64,189,043</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">14,597,140</td>
<td align="right">10,358,786</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,623,279</td>
<td align="right">6,162,475</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">960,944</td>
<td align="right">687,776</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,707,266</td>
<td align="right">2,705,097</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">774,162</td>
<td align="right">564,957</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">70,578</td>
<td align="right">51,775</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,647,343</td>
<td align="right">4,144,356</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">5,936,531</td>
<td align="right">4,367,502</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">68,323,614</td>
<td align="right">50,492,381</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">131,242,295</td>
<td align="right">98,245,471</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">4,141,260</td>
<td align="right">3,205,481</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,660,294</td>
<td align="right">14,446,327</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">323,870</td>
<td align="right">252,073</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">24,359,318</td>
<td align="right">19,146,977</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">14,275,368</td>
<td align="right">11,412,541</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">482,495</td>
<td align="right">386,400</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">112,671,651</td>
<td align="right">91,115,312</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,176,912</td>
<td align="right">955,184</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">13,621,633</td>
<td align="right">11,372,027</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">55,787,355</td>
<td align="right">48,675,166</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,539,508</td>
<td align="right">1,348,525</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,324,812</td>
<td align="right">2,058,873</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">630,461</td>
<td align="right">559,061</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20,175</td>
<td align="right">17,914</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,355,783</td>
<td align="right">2,993,517</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,440,575</td>
<td align="right">5,805,346</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,481,453</td>
<td align="right">1,340,134</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,923</td>
<td align="right">2,648</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,054,892</td>
<td align="right">958,124</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">549,114</td>
<td align="right">503,876</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">12,201</td>
<td align="right">11,241</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">5,337,621</td>
<td align="right">4,933,039</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,994,117</td>
<td align="right">2,803,666</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">116,582,461</td>
<td align="right">109,512,056</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">452,456</td>
<td align="right">477,379</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,976,955</td>
<td align="right">5,673,264</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,694</td>
<td align="right">34,365</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,222,783</td>
<td align="right">4,065,737</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,192,702</td>
<td align="right">1,150,770</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,314</td>
<td align="right">9,038</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,720,759</td>
<td align="right">1,677,395</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,559</td>
<td align="right">8,706</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,663</td>
<td align="right">10,810</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">115,389</td>
<td align="right">114,225</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">543,124</td>
<td align="right">546,710</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">3,229</td>
<td align="right">3,208</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">24,225</td>
<td align="right">24,322</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">75,888,466</td>
<td align="right">75,771,769</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">37,974,066</td>
<td align="right">38,024,280</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">14,762</td>
<td align="right">14,750</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">22,099</td>
<td align="right">22,090</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">79,173,752</td>
<td align="right">79,145,516</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">219,361</td>
<td align="right">219,292</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">20,645</td>
<td align="right">20,641</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">38,632</td>
<td align="right">38,627</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,251,711</td>
<td align="right">39,248,985</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,526,554</td>
<td align="right">39,526,583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,864,496</td>
<td align="right">38,864,496</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,677,409</td>
<td align="right">22,677,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,973,635</td>
<td align="right">2,973,635</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,522,501</td>
<td align="right">1,522,501</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,522,501</td>
<td align="right">1,522,501</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,477,299</td>
<td align="right">1,477,299</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">146,429</td>
<td align="right">146,429</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">129,082</td>
<td align="right">129,082</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">28,752</td>
<td align="right">28,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,706</td>
<td align="right">8,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4,541</td>
<td align="right">4,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,085</td>
<td align="right">3,085</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,240</td>
<td align="right">2,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,087</td>
<td align="right">2,087</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1,324</td>
<td align="right">1,324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">474</td>
<td align="right">474</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">323</td>
<td align="right">323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">264</td>
<td align="right">264</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">143</td>
<td align="right">143</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">95</td>
<td align="right">95</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">19</td>
<td align="right">19</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">6</td>
<td align="right">6</td>
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
<td align="right">6,431,287</td>
<td align="right">37.3%</td>
<td align="right">5,796,680</td>
<td align="right">34.9%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,824,479</td>
<td align="right">62.7%</td>
<td align="right">10,824,479</td>
<td align="right">65.1%</td>
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
<td align="right">8,675</td>
<td align="right">93.4%</td>
<td align="right">8,053</td>
<td align="right">92.9%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">613</td>
<td align="right">6.6%</td>
<td align="right">613</td>
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
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.8%</td>
<td align="right">24</td>
<td align="right">0.3%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,002</td>
<td align="right">34.6%</td>
<td align="right">2,546</td>
<td align="right">31.6%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">2.6%</td>
<td align="right">207</td>
<td align="right">2.6%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,508</td>
<td align="right">17.4%</td>
<td align="right">1,420</td>
<td align="right">17.6%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">130</td>
<td align="right">1.5%</td>
<td align="right">125</td>
<td align="right">1.6%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">187</td>
<td align="right">2.2%</td>
<td align="right">185</td>
<td align="right">2.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">846</td>
<td align="right">9.8%</td>
<td align="right">842</td>
<td align="right">10.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,376</td>
<td align="right">27.4%</td>
<td align="right">2,373</td>
<td align="right">29.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">251</td>
<td align="right">2.9%</td>
<td align="right">251</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">65</td>
<td align="right">0.7%</td>
<td align="right">65</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">9</td>
<td align="right">0.1%</td>
<td align="right">9</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">2,063,222</td>
<td align="right">100.0%</td>
<td align="right">1,111,967</td>
<td align="right">100.0%</td>
<td align="right">-46.1%</td>
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
<td align="right">3,348,600</td>
<td align="right">8.8%</td>
<td align="right">2,987,405</td>
<td align="right">7.9%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,467,373</td>
<td align="right">85.0%</td>
<td align="right">32,467,009</td>
<td align="right">85.8%</td>
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
<td align="right">2,363,133</td>
<td align="right">6.2%</td>
<td align="right">2,363,123</td>
<td align="right">6.2%</td>
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
<td align="right">5,940</td>
<td align="right">11.5%</td>
<td align="right">4,870</td>
<td align="right">9.6%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">45,685</td>
<td align="right">88.5%</td>
<td align="right">45,685</td>
<td align="right">90.4%</td>
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
<td align="right">113</td>
<td align="right">1.9%</td>
<td align="right">67</td>
<td align="right">1.4%</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">238</td>
<td align="right">4.0%</td>
<td align="right">146</td>
<td align="right">3.0%</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">1,271</td>
<td align="right">21.4%</td>
<td align="right">938</td>
<td align="right">19.3%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">780</td>
<td align="right">13.1%</td>
<td align="right">626</td>
<td align="right">12.9%</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">304</td>
<td align="right">5.1%</td>
<td align="right">260</td>
<td align="right">5.3%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,989</td>
<td align="right">50.3%</td>
<td align="right">2,588</td>
<td align="right">53.1%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">245</td>
<td align="right">4.1%</td>
<td align="right">245</td>
<td align="right">5.0%</td>
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
<td align="right">1,814,588</td>
<td align="right">0.8%</td>
<td align="right">1,757,599</td>
<td align="right">0.7%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">239,378,109</td>
<td align="right">99.2%</td>
<td align="right">239,430,622</td>
<td align="right">99.3%</td>
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
<td align="right">14,389</td>
<td align="right">0.0%</td>
<td align="right">14,387</td>
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
<td align="right">60,026</td>
<td align="right">100.0%</td>
<td align="right">58,939</td>
<td align="right">100.0%</td>
<td align="right">-1.8%</td>
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
<td align="right">424</td>
<td align="right">424 / 0 !!</td>
<td align="right">424</td>
<td align="right">424 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">24</td>
<td align="right">24 / 0 !!</td>
<td align="right">24</td>
<td align="right">24 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3</td>
<td align="right">3 / 0 !!</td>
<td align="right">3</td>
<td align="right">3 / 0 !!</td>
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
<td align="right">334</td>
<td align="right">15.5%</td>
<td align="right">334</td>
<td align="right">15.5%</td>
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
<td align="right">64</td>
<td align="right">3.0%</td>
<td align="right">64</td>
<td align="right">3.0%</td>
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
<td align="right">7,962</td>
<td align="right">0.1%</td>
<td align="right">5,368</td>
<td align="right">0.0%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">626,525</td>
<td align="right">5.4%</td>
<td align="right">555,447</td>
<td align="right">4.8%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,926,353</td>
<td align="right">94.5%</td>
<td align="right">10,912,804</td>
<td align="right">95.1%</td>
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
<td align="right">2,695</td>
<td align="right">66.3%</td>
<td align="right">2,376</td>
<td align="right">64.2%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,370</td>
<td align="right">33.7%</td>
<td align="right">1,323</td>
<td align="right">35.8%</td>
<td align="right">-3.4%</td>
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
<td align="right">1,845</td>
<td align="right">68.5%</td>
<td align="right">1,533</td>
<td align="right">64.5%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">109</td>
<td align="right">4.0%</td>
<td align="right">103</td>
<td align="right">4.3%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">259</td>
<td align="right">9.6%</td>
<td align="right">259</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">254</td>
<td align="right">9.4%</td>
<td align="right">254</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">157</td>
<td align="right">5.8%</td>
<td align="right">157</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">27</td>
<td align="right">1.0%</td>
<td align="right">27</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">3,478,919</td>
<td align="right">22.9%</td>
<td align="right">2,318,788</td>
<td align="right">16.5%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,730,761</td>
<td align="right">77.1%</td>
<td align="right">11,730,732</td>
<td align="right">83.5%</td>
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
<td align="right">4,747</td>
<td align="right">90.0%</td>
<td align="right">3,240</td>
<td align="right">86.0%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">528</td>
<td align="right">10.0%</td>
<td align="right">528</td>
<td align="right">14.0%</td>
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
<td align="right">734</td>
<td align="right">15.5%</td>
<td align="right">417</td>
<td align="right">12.9%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,992</td>
<td align="right">42.0%</td>
<td align="right">1,297</td>
<td align="right">40.0%</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,456</td>
<td align="right">30.7%</td>
<td align="right">1,091</td>
<td align="right">33.7%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">565</td>
<td align="right">11.9%</td>
<td align="right">435</td>
<td align="right">13.4%</td>
<td align="right">-23.0%</td>
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
<td align="right">2,345,772</td>
<td align="right">3.0%</td>
<td align="right">1,517,537</td>
<td align="right">2.2%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,348,008</td>
<td align="right">4.3%</td>
<td align="right">2,326,572</td>
<td align="right">3.3%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">71,422,207</td>
<td align="right">92.6%</td>
<td align="right">66,334,750</td>
<td align="right">94.5%</td>
<td align="right">-7.1%</td>
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
<td align="right">44,904</td>
<td align="right">93.3%</td>
<td align="right">29,284</td>
<td align="right">92.0%</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,220</td>
<td align="right">6.7%</td>
<td align="right">2,544</td>
<td align="right">8.0%</td>
<td align="right">-21.0%</td>
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
<td align="right">54</td>
<td align="right">1.7%</td>
<td align="right">9</td>
<td align="right">0.4%</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">185</td>
<td align="right">5.7%</td>
<td align="right">95</td>
<td align="right">3.7%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">315</td>
<td align="right">9.8%</td>
<td align="right">225</td>
<td align="right">8.8%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">275</td>
<td align="right">8.5%</td>
<td align="right">204</td>
<td align="right">8.0%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,075</td>
<td align="right">33.4%</td>
<td align="right">830</td>
<td align="right">32.6%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">240</td>
<td align="right">7.5%</td>
<td align="right">197</td>
<td align="right">7.7%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">818</td>
<td align="right">25.4%</td>
<td align="right">726</td>
<td align="right">28.5%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">142</td>
<td align="right">4.4%</td>
<td align="right">142</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">76</td>
<td align="right">2.4%</td>
<td align="right">76</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">25</td>
<td align="right">0.8%</td>
<td align="right">25</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15</td>
<td align="right">0.5%</td>
<td align="right">15</td>
<td align="right">0.6%</td>
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
<td align="right">30,080,757</td>
<td align="right">9.9%</td>
<td align="right">11,364,835</td>
<td align="right">4.4%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">64,392</td>
<td align="right">0.0%</td>
<td align="right">30,432</td>
<td align="right">0.0%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">64,212,278</td>
<td align="right">21.1%</td>
<td align="right">39,204,857</td>
<td align="right">15.3%</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">209,005,076</td>
<td align="right">68.8%</td>
<td align="right">206,317,217</td>
<td align="right">80.3%</td>
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
<td align="right">9,431</td>
<td align="right">0.6%</td>
<td align="right">4,937</td>
<td align="right">0.5%</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,516,994</td>
<td align="right">99.4%</td>
<td align="right">913,140</td>
<td align="right">99.5%</td>
<td align="right">-39.8%</td>
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
<td align="left">overridden</td>
<td align="right">644</td>
<td align="right">6.8%</td>
<td align="right">129</td>
<td align="right">2.6%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">259</td>
<td align="right">2.7%</td>
<td align="right">65</td>
<td align="right">1.3%</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,116</td>
<td align="right">22.4%</td>
<td align="right">738</td>
<td align="right">14.9%</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">994</td>
<td align="right">10.5%</td>
<td align="right">556</td>
<td align="right">11.3%</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">530</td>
<td align="right">5.6%</td>
<td align="right">310</td>
<td align="right">6.3%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,086</td>
<td align="right">11.5%</td>
<td align="right">637</td>
<td align="right">12.9%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,965</td>
<td align="right">31.4%</td>
<td align="right">1,761</td>
<td align="right">35.7%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">112</td>
<td align="right">1.2%</td>
<td align="right">67</td>
<td align="right">1.4%</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6</td>
<td align="right">0.1%</td>
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">68</td>
<td align="right">0.7%</td>
<td align="right">65</td>
<td align="right">1.3%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">72</td>
<td align="right">0.8%</td>
<td align="right">70</td>
<td align="right">1.4%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">168,787,576</td>
<td align="right">100.0%</td>
<td align="right">97,007,595</td>
<td align="right">100.0%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,069</td>
<td align="right">0.0%</td>
<td align="right">3,065</td>
<td align="right">0.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">59</td>
<td align="right">0.0%</td>
<td align="right">59</td>
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
<td align="right">11,540</td>
<td align="right">0.0%</td>
<td align="right">11,540</td>
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
<td align="right">19,449</td>
<td align="right">100.0%</td>
<td align="right">19,444</td>
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
<td align="right">53</td>
<td align="right">0.0%</td>
<td align="right">53</td>
<td align="right">0.0%</td>
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
<td align="right">424,672</td>
<td align="right">99.9%</td>
<td align="right">424,672</td>
<td align="right">99.9%</td>
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
<td align="right">211</td>
<td align="right">100.0%</td>
<td align="right">211</td>
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
<td align="right">4,490</td>
<td align="right">29.2%</td>
<td align="right">4,490</td>
<td align="right">29.2%</td>
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
<td align="right">10,810</td>
<td align="right">70.4%</td>
<td align="right">10,810</td>
<td align="right">70.4%</td>
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
<td align="right">4</td>
<td align="right">7.8%</td>
<td align="right">4</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">47</td>
<td align="right">92.2%</td>
<td align="right">47</td>
<td align="right">92.2%</td>
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
<td align="right">47</td>
<td align="right">100.0%</td>
<td align="right">47</td>
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
<td align="right">8,608,663</td>
<td align="right">26.7%</td>
<td align="right">6,149,022</td>
<td align="right">21.4%</td>
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
<td align="right">9,537,030</td>
<td align="right">29.6%</td>
<td align="right">8,328,793</td>
<td align="right">29.0%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,104,450</td>
<td align="right">43.7%</td>
<td align="right">14,224,985</td>
<td align="right">49.5%</td>
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
<td align="left">Success</td>
<td align="right">184,604</td>
<td align="right">95.1%</td>
<td align="right">161,922</td>
<td align="right">95.1%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,462</td>
<td align="right">4.9%</td>
<td align="right">8,303</td>
<td align="right">4.9%</td>
<td align="right">-12.2%</td>
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
<td align="left">not in keys</td>
<td align="right">308</td>
<td align="right">3.3%</td>
<td align="right">243</td>
<td align="right">2.9%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">643</td>
<td align="right">6.8%</td>
<td align="right">509</td>
<td align="right">6.1%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">4,737</td>
<td align="right">50.1%</td>
<td align="right">3,865</td>
<td align="right">46.5%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">984</td>
<td align="right">10.4%</td>
<td align="right">897</td>
<td align="right">10.8%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">1.0%</td>
<td align="right">93</td>
<td align="right">1.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,626</td>
<td align="right">27.8%</td>
<td align="right">2,626</td>
<td align="right">31.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">53</td>
<td align="right">0.6%</td>
<td align="right">53</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">6</td>
<td align="right">0.1%</td>
<td align="right">6</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">115,389</td>
<td align="right">100.0%</td>
<td align="right">114,225</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">1,477,503</td>
<td align="right">13.9%</td>
<td align="right">1,336,418</td>
<td align="right">12.7%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,156,246</td>
<td align="right">86.1%</td>
<td align="right">9,156,246</td>
<td align="right">87.2%</td>
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
<td align="right">3,471</td>
<td align="right">87.9%</td>
<td align="right">3,237</td>
<td align="right">87.1%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">479</td>
<td align="right">12.1%</td>
<td align="right">479</td>
<td align="right">12.9%</td>
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
<td align="right">10</td>
<td align="right">0.3%</td>
<td align="right">9</td>
<td align="right">0.3%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,960</td>
<td align="right">85.3%</td>
<td align="right">2,729</td>
<td align="right">84.3%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">113</td>
<td align="right">3.3%</td>
<td align="right">111</td>
<td align="right">3.4%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">341</td>
<td align="right">9.8%</td>
<td align="right">341</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">47</td>
<td align="right">1.4%</td>
<td align="right">47</td>
<td align="right">1.5%</td>
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
<td align="right">11,652,267</td>
<td align="right">6.4%</td>
<td align="right">2,468,856</td>
<td align="right">1.4%</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,512,212</td>
<td align="right">1.9%</td>
<td align="right">1,147,169</td>
<td align="right">0.7%</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">166,691,594</td>
<td align="right">91.6%</td>
<td align="right">168,654,327</td>
<td align="right">97.9%</td>
<td align="right">1.2%</td>
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
<td align="right">93,164</td>
<td align="right">57.0%</td>
<td align="right">21,687</td>
<td align="right">45.9%</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">70,254</td>
<td align="right">43.0%</td>
<td align="right">25,539</td>
<td align="right">54.1%</td>
<td align="right">-63.6%</td>
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
<td align="right">79,569</td>
<td align="right">85.4%</td>
<td align="right">10,649</td>
<td align="right">49.1%</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,074</td>
<td align="right">1.2%</td>
<td align="right">618</td>
<td align="right">2.8%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">93</td>
<td align="right">0.1%</td>
<td align="right">70</td>
<td align="right">0.3%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,948</td>
<td align="right">10.7%</td>
<td align="right">8,007</td>
<td align="right">36.9%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">213</td>
<td align="right">0.2%</td>
<td align="right">190</td>
<td align="right">0.9%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,160</td>
<td align="right">2.3%</td>
<td align="right">2,046</td>
<td align="right">9.4%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">107</td>
<td align="right">0.1%</td>
<td align="right">107</td>
<td align="right">0.5%</td>
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
<td align="right">296,270</td>
<td align="right">2.0%</td>
<td align="right">416</td>
<td align="right">0.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,605,169</td>
<td align="right">98.0%</td>
<td align="right">14,605,169</td>
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
<td align="left">Failure</td>
<td align="right">97</td>
<td align="right">20.2%</td>
<td align="right">26</td>
<td align="right">6.4%</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">383</td>
<td align="right">79.8%</td>
<td align="right">383</td>
<td align="right">93.6%</td>
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
<td align="right">74</td>
<td align="right">76.3%</td>
<td align="right">3</td>
<td align="right">11.5%</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">23</td>
<td align="right">23.7%</td>
<td align="right">23</td>
<td align="right">88.5%</td>
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
<td align="right">72,057,537</td>
<td align="right">2.7%</td>
<td align="right">36,846,941</td>
<td align="right">1.9%</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">874,765,119</td>
<td align="right">32.8%</td>
<td align="right">510,020,697</td>
<td align="right">27.0%</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">83,808,740</td>
<td align="right">3.1%</td>
<td align="right">54,340,467</td>
<td align="right">2.9%</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,635,197,852</td>
<td align="right">61.3%</td>
<td align="right">1,290,172,366</td>
<td align="right">68.2%</td>
<td align="right">-21.1%</td>
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
<td align="right">11,652,267</td>
<td align="right">16.3%</td>
<td align="right">2,468,856</td>
<td align="right">6.8%</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,080,757</td>
<td align="right">42.0%</td>
<td align="right">11,364,835</td>
<td align="right">31.1%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,063,222</td>
<td align="right">2.9%</td>
<td align="right">1,111,967</td>
<td align="right">3.0%</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,478,919</td>
<td align="right">4.9%</td>
<td align="right">2,318,788</td>
<td align="right">6.3%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,348,008</td>
<td align="right">4.7%</td>
<td align="right">2,326,572</td>
<td align="right">6.4%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,608,663</td>
<td align="right">12.0%</td>
<td align="right">6,149,022</td>
<td align="right">16.8%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">626,525</td>
<td align="right">0.9%</td>
<td align="right">555,447</td>
<td align="right">1.5%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,348,600</td>
<td align="right">4.7%</td>
<td align="right">2,987,405</td>
<td align="right">8.2%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,431,287</td>
<td align="right">9.0%</td>
<td align="right">5,796,680</td>
<td align="right">15.9%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,477,503</td>
<td align="right">2.1%</td>
<td align="right">1,336,418</td>
<td align="right">3.7%</td>
<td align="right">-9.5%</td>
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
<td align="right">5,101,616</td>
<td align="right">6.1%</td>
<td align="right">1,552,841</td>
<td align="right">2.9%</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">10,474,119</td>
<td align="right">12.5%</td>
<td align="right">5,917,488</td>
<td align="right">10.9%</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">30,651,138</td>
<td align="right">36.6%</td>
<td align="right">17,441,515</td>
<td align="right">32.1%</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,172,977</td>
<td align="right">1.4%</td>
<td align="right">758,481</td>
<td align="right">1.4%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,172,795</td>
<td align="right">1.4%</td>
<td align="right">759,056</td>
<td align="right">1.4%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,941,581</td>
<td align="right">9.5%</td>
<td align="right">6,276,694</td>
<td align="right">11.5%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,508,102</td>
<td align="right">11.3%</td>
<td align="right">7,632,454</td>
<td align="right">14.0%</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,497,824</td>
<td align="right">11.3%</td>
<td align="right">8,296,519</td>
<td align="right">15.3%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,338,573</td>
<td align="right">2.8%</td>
<td align="right">2,338,563</td>
<td align="right">4.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,802,306</td>
<td align="right">3.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">776,436</td>
<td align="right">1.4%</td>
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
<td align="right">869,907</td>
<td align="right">0.4%</td>
<td align="right">894,830</td>
<td align="right">0.4%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">7,050,327</td>
<td align="right">3.2%</td>
<td align="right">7,076,923</td>
<td align="right">3.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">18,436,951</td>
<td align="right">8.4%</td>
<td align="right">18,490,751</td>
<td align="right">8.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,380,362</td>
<td align="right">18.4%</td>
<td align="right">40,455,499</td>
<td align="right">18.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,380,362</td>
<td align="right">18.4%</td>
<td align="right">40,455,499</td>
<td align="right">18.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,508,781</td>
<td align="right">18.0%</td>
<td align="right">39,558,995</td>
<td align="right">18.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,510,455</td>
<td align="right">18.0%</td>
<td align="right">39,560,669</td>
<td align="right">18.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">179,020,704</td>
<td align="right">81.6%</td>
<td align="right">178,970,490</td>
<td align="right">81.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,044,439</td>
<td align="right">72.0%</td>
<td align="right">158,048,025</td>
<td align="right">72.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">350</td>
<td align="right">0.0%</td>
<td align="right">350</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">1,324</td>
<td align="right">0.0%</td>
<td align="right">1,324</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">10,483,505</td>
<td align="right">4.8%</td>
<td align="right">10,483,505</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">502,480</td>
<td align="right">0.2%</td>
<td align="right">502,480</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">94</td>
<td align="right">0.0%</td>
<td align="right">94</td>
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
<td align="left">Mortal increfs</td>
<td align="right">1,645,897,237</td>
<td align="right">40.4%</td>
<td align="right">2,210,055,438</td>
<td align="right">51.2%</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,499,404,565</td>
<td align="right">34.3%</td>
<td align="right">1,983,607,958</td>
<td align="right">42.1%</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">423,768,053</td>
<td align="right">10.4%</td>
<td align="right">310,470,449</td>
<td align="right">7.2%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,190,989,365</td>
<td align="right">29.2%</td>
<td align="right">906,038,654</td>
<td align="right">21.0%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">440,901,141</td>
<td align="right">10.1%</td>
<td align="right">358,515,938</td>
<td align="right">7.6%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">837,389,195</td>
<td align="right">19.2%</td>
<td align="right">987,001,925</td>
<td align="right">20.9%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,556,163</td>
<td align="right">0.5%</td>
<td align="right">1,814,004</td>
<td align="right">0.6%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,588,534,414</td>
<td align="right">36.4%</td>
<td align="right">1,383,908,327</td>
<td align="right">29.4%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">811,888,416</td>
<td align="right">19.9%</td>
<td align="right">887,515,524</td>
<td align="right">20.6%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">7,521,442</td>
<td align="right"></td>
<td align="right">6,939,938</td>
<td align="right"></td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">9,400,457</td>
<td align="right"></td>
<td align="right">8,844,087</td>
<td align="right"></td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">61,674</td>
<td align="right">0.0%</td>
<td align="right">63,678</td>
<td align="right">0.0%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,881,084</td>
<td align="right"></td>
<td align="right">1,906,069</td>
<td align="right"></td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">155,157,157</td>
<td align="right"></td>
<td align="right">153,874,024</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">200,680,030</td>
<td align="right"></td>
<td align="right">199,289,381</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">252,031,110</td>
<td align="right"></td>
<td align="right">252,477,224</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">242,479,562</td>
<td align="right">74.3%</td>
<td align="right">242,890,619</td>
<td align="right">74.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">240,861,725</td>
<td align="right">73.8%</td>
<td align="right">241,012,937</td>
<td align="right">73.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">83,784,492</td>
<td align="right"></td>
<td align="right">83,795,426</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">83,799,046</td>
<td align="right">25.7%</td>
<td align="right">83,806,229</td>
<td align="right">25.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,079,566</td>
<td align="right"></td>
<td align="right">3,079,566</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">997,125</td>
<td align="right">32.4%</td>
<td align="right">997,125</td>
<td align="right">32.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">98,881</td>
<td align="right">3.2%</td>
<td align="right">98,881</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
<td align="right">1,344</td>
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
<td align="right">6,259</td>
<td align="right">12,462,340</td>
<td align="right">368,039,687</td>
<td align="right">6,257</td>
<td align="right">12,392,186</td>
<td align="right">369,726,162</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">36</td>
<td align="right">0.0%</td>
<td align="right">392</td>
<td align="right">0.1%</td>
<td align="right">988.9%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">3,322</td>
<td align="right">1.0%</td>
<td align="right">15,337</td>
<td align="right">2.1%</td>
<td align="right">361.7%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,451</td>
<td align="right">0.4%</td>
<td align="right">5,233</td>
<td align="right">0.7%</td>
<td align="right">260.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">134,332</td>
<td align="right">40.7%</td>
<td align="right">339,656</td>
<td align="right">45.6%</td>
<td align="right">152.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">228,943</td>
<td align="right">69.4%</td>
<td align="right">571,151</td>
<td align="right">76.7%</td>
<td align="right">149.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">329,814</td>
<td align="right"></td>
<td align="right">744,429</td>
<td align="right"></td>
<td align="right">125.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">100,871</td>
<td align="right">30.6%</td>
<td align="right">173,194</td>
<td align="right">23.3%</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">3,837,815,037</td>
<td align="right">963.5%</td>
<td align="right">6,056,789,834</td>
<td align="right">970.5%</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">398,307,903</td>
<td align="right"></td>
<td align="right">624,116,395</td>
<td align="right"></td>
<td align="right">56.7%</td>
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
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">84 / 0 !!</td>
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">149</td>
<td align="right">0.0%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">55</td>
<td align="right">0.0%</td>
<td align="right">173</td>
<td align="right">0.0%</td>
<td align="right">214.5%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">220,159</td>
<td align="right">96.2%</td>
<td align="right">562,816</td>
<td align="right">98.5%</td>
<td align="right">155.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">228,943</td>
<td align="right"></td>
<td align="right">571,151</td>
<td align="right"></td>
<td align="right">149.5%</td>
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
<td align="right">338</td>
<td align="right">0.1%</td>
<td align="right">338 / 0 !!</td>
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
<td align="right">7,982</td>
<td align="right">1.4%</td>
<td align="right">7,982 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,237</td>
<td align="right">7.1%</td>
<td align="right">24,852</td>
<td align="right">4.4%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">59,359</td>
<td align="right">25.9%</td>
<td align="right">97,680</td>
<td align="right">17.1%</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">85,957</td>
<td align="right">37.5%</td>
<td align="right">239,603</td>
<td align="right">42.0%</td>
<td align="right">178.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">50,927</td>
<td align="right">22.2%</td>
<td align="right">143,841</td>
<td align="right">25.2%</td>
<td align="right">182.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">16,119</td>
<td align="right">7.0%</td>
<td align="right">50,454</td>
<td align="right">8.8%</td>
<td align="right">213.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">344</td>
<td align="right">0.2%</td>
<td align="right">5,644</td>
<td align="right">1.0%</td>
<td align="right">1,540.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,095</td>
<td align="right">0.2%</td>
<td align="right"></td>
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
<td align="right">6,785</td>
<td align="right">3.0%</td>
<td align="right">22,189</td>
<td align="right">3.9%</td>
<td align="right">227.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">43,207</td>
<td align="right">18.9%</td>
<td align="right">47,778</td>
<td align="right">8.4%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">48,620</td>
<td align="right">21.2%</td>
<td align="right">143,531</td>
<td align="right">25.1%</td>
<td align="right">195.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">90,974</td>
<td align="right">39.7%</td>
<td align="right">248,366</td>
<td align="right">43.5%</td>
<td align="right">173.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">28,141</td>
<td align="right">12.3%</td>
<td align="right">82,408</td>
<td align="right">14.4%</td>
<td align="right">192.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,388</td>
<td align="right">1.0%</td>
<td align="right">16,497</td>
<td align="right">2.9%</td>
<td align="right">590.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">44</td>
<td align="right">0.0%</td>
<td align="right">1,879</td>
<td align="right">0.3%</td>
<td align="right">4,170.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">168</td>
<td align="right">0.0%</td>
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
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">41</td>
<td align="right">146,005</td>
<td align="right">356,009.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">83,035</td>
<td align="right">116,083,973</td>
<td align="right">139,701.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">184</td>
<td align="right">76,922</td>
<td align="right">41,705.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,727</td>
<td align="right">718,062</td>
<td align="right">41,478.6%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">19,971</td>
<td align="right">7,266,512</td>
<td align="right">36,285.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">9,026</td>
<td align="right">2,708,315</td>
<td align="right">29,905.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1</td>
<td align="right">277</td>
<td align="right">27,600.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">1,886</td>
<td align="right">485,181</td>
<td align="right">25,625.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">892</td>
<td align="right">128,264</td>
<td align="right">14,279.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,571</td>
<td align="right">367,114</td>
<td align="right">14,179.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">892</td>
<td align="right">126,277</td>
<td align="right">14,056.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">1,338</td>
<td align="right">183,828</td>
<td align="right">13,639.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">36,304</td>
<td align="right">4,732,499</td>
<td align="right">12,935.8%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,286</td>
<td align="right">110,703</td>
<td align="right">8,508.3%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">64,940</td>
<td align="right">4,882,296</td>
<td align="right">7,418.2%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">32,984</td>
<td align="right">2,438,580</td>
<td align="right">7,293.2%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">14,961</td>
<td align="right">869,127</td>
<td align="right">5,709.3%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">14,961</td>
<td align="right">867,862</td>
<td align="right">5,700.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">18,718</td>
<td align="right">1,065,039</td>
<td align="right">5,589.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">3,718</td>
<td align="right">163,796</td>
<td align="right">4,305.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">43,909</td>
<td align="right">1,869,883</td>
<td align="right">4,158.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">63,316</td>
<td align="right">2,563,597</td>
<td align="right">3,948.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">74,993</td>
<td align="right">2,895,012</td>
<td align="right">3,760.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">242,201</td>
<td align="right">8,596,954</td>
<td align="right">3,449.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">11,507</td>
<td align="right">379,142</td>
<td align="right">3,194.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">333,665</td>
<td align="right">7,607,473</td>
<td align="right">2,180.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">58,486</td>
<td align="right">1,256,728</td>
<td align="right">2,048.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">29,298</td>
<td align="right">495,381</td>
<td align="right">1,590.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">65,559</td>
<td align="right">816,859</td>
<td align="right">1,146.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">102,848</td>
<td align="right">983,014</td>
<td align="right">855.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">10,293</td>
<td align="right">97,460</td>
<td align="right">846.9%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">13,156</td>
<td align="right">124,445</td>
<td align="right">845.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,709</td>
<td align="right">24,618</td>
<td align="right">808.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">690,436</td>
<td align="right">6,053,525</td>
<td align="right">776.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">690,436</td>
<td align="right">6,053,525</td>
<td align="right">776.8%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">47,421</td>
<td align="right">406,726</td>
<td align="right">757.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">38,250</td>
<td align="right">315,958</td>
<td align="right">726.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">82,636</td>
<td align="right">650,669</td>
<td align="right">687.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">1,077,411</td>
<td align="right">7,273,913</td>
<td align="right">575.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">28,553</td>
<td align="right">177,072</td>
<td align="right">520.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,223</td>
<td align="right">91,197</td>
<td align="right">400.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">173,014</td>
<td align="right">816,907</td>
<td align="right">372.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">937,690</td>
<td align="right">4,384,543</td>
<td align="right">367.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,507</td>
<td align="right">114,204</td>
<td align="right">287.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,507</td>
<td align="right">114,204</td>
<td align="right">287.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,447,650</td>
<td align="right">9,246,225</td>
<td align="right">277.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">11,131,750</td>
<td align="right">41,622,737</td>
<td align="right">273.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">430,912</td>
<td align="right">1,552,538</td>
<td align="right">260.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">3,472,409</td>
<td align="right">12,507,338</td>
<td align="right">260.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,992,433</td>
<td align="right">7,135,632</td>
<td align="right">258.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">5,209,455</td>
<td align="right">18,353,794</td>
<td align="right">252.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,447,316</td>
<td align="right">4,971,981</td>
<td align="right">243.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,577,644</td>
<td align="right">4,931,078</td>
<td align="right">212.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">9,256</td>
<td align="right">28,059</td>
<td align="right">203.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,724</td>
<td align="right">325,448</td>
<td align="right">202.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,724</td>
<td align="right">325,448</td>
<td align="right">202.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">812,695</td>
<td align="right">2,381,724</td>
<td align="right">193.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">5,448,385</td>
<td align="right">15,445,777</td>
<td align="right">183.5%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,286</td>
<td align="right">3,547</td>
<td align="right">175.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,116,003</td>
<td align="right">5,789,838</td>
<td align="right">173.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">3,577,024</td>
<td align="right">9,703,965</td>
<td align="right">171.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">70,330,897</td>
<td align="right">183,713,063</td>
<td align="right">161.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">6,112,823</td>
<td align="right">15,253,168</td>
<td align="right">149.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">26,700,039</td>
<td align="right">65,547,538</td>
<td align="right">145.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,065,560</td>
<td align="right">2,582,291</td>
<td align="right">142.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">352,962</td>
<td align="right">846,151</td>
<td align="right">139.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,739,445</td>
<td align="right">6,566,456</td>
<td align="right">139.7%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">303,521</td>
<td align="right">706,902</td>
<td align="right">132.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">760,635</td>
<td align="right">1,762,804</td>
<td align="right">131.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">7,043,598</td>
<td align="right">16,310,663</td>
<td align="right">131.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">724,077</td>
<td align="right">1,675,332</td>
<td align="right">131.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">225,813</td>
<td align="right">522,126</td>
<td align="right">131.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">25,559,490</td>
<td align="right">59,054,229</td>
<td align="right">131.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,442,113</td>
<td align="right">3,215,974</td>
<td align="right">123.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">182,808</td>
<td align="right">405,644</td>
<td align="right">121.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">996,150</td>
<td align="right">2,156,310</td>
<td align="right">116.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">27,643,731</td>
<td align="right">58,940,726</td>
<td align="right">113.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">27,593,703</td>
<td align="right">57,543,623</td>
<td align="right">108.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,488,050</td>
<td align="right">3,036,203</td>
<td align="right">104.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">18,709,809</td>
<td align="right">36,541,042</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,271,919</td>
<td align="right">29,820,046</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">14,863,575</td>
<td align="right">28,931,699</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">24,780,665</td>
<td align="right">47,343,995</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,907,541</td>
<td align="right">22,146,508</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">79,399,911</td>
<td align="right">147,662,082</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">5,115,903</td>
<td align="right">9,329,870</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,488,778</td>
<td align="right">10,004,842</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,724,311</td>
<td align="right">23,101,812</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">187,474,108</td>
<td align="right">337,744,579</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,938,195</td>
<td align="right">3,475,498</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">370,931</td>
<td align="right">655,507</td>
<td align="right">76.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">28,167,384</td>
<td align="right">49,756,671</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,735,906</td>
<td align="right">6,598,733</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,735,906</td>
<td align="right">6,598,733</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">188,293</td>
<td align="right">329,378</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">37,246,934</td>
<td align="right">64,696,839</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">550,598</td>
<td align="right">912,168</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">5,629,477</td>
<td align="right">9,228,737</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,502,158</td>
<td align="right">2,451,213</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">13,694,443</td>
<td align="right">22,252,765</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">320,441,044</td>
<td align="right">519,027,727</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">5,113,977</td>
<td align="right">8,244,861</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,256,418</td>
<td align="right">2,012,181</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,555,609</td>
<td align="right">2,475,245</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">2,001,348</td>
<td align="right">3,177,523</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">74,188</td>
<td align="right">117,552</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">809,213</td>
<td align="right">1,278,753</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">51,218,643</td>
<td align="right">21,528,546</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">27,423,235</td>
<td align="right">43,210,363</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,476,059</td>
<td align="right">3,897,756</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">398,307,903</td>
<td align="right">624,116,395</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">21,337,913</td>
<td align="right">33,297,450</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">409,722,135</td>
<td align="right">635,470,010</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">17,997,936</td>
<td align="right">27,566,812</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">576,380</td>
<td align="right">880,071</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">46,994,028</td>
<td align="right">71,447,810</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,772,736</td>
<td align="right">7,198,979</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,045,125</td>
<td align="right">1,576,113</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">13,847,321</td>
<td align="right">20,705,298</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">50,922,064</td>
<td align="right">75,896,954</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">41,288,552</td>
<td align="right">61,028,197</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">226,678,230</td>
<td align="right">334,257,114</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">41,231,578</td>
<td align="right">60,583,827</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">809,010</td>
<td align="right">1,188,314</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">808,441</td>
<td align="right">1,184,221</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,965,799</td>
<td align="right">5,799,157</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">311,178,829</td>
<td align="right">453,538,423</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">157,329</td>
<td align="right">229,126</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">157,329</td>
<td align="right">229,126</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">54,756,671</td>
<td align="right">78,604,047</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">95,509,997</td>
<td align="right">136,362,508</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">4,924,373</td>
<td align="right">6,944,771</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,895,526</td>
<td align="right">3,921,150</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">73,545,426</td>
<td align="right">99,257,980</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">73,486,067</td>
<td align="right">98,802,471</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">78,774,603</td>
<td align="right">104,999,470</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,321,489</td>
<td align="right">9,721,401</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">12,817,852</td>
<td align="right">16,901,523</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">5,521,438</td>
<td align="right">6,964,192</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">70,962,958</td>
<td align="right">89,306,197</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">38,357,894</td>
<td align="right">48,129,603</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">179,594</td>
<td align="right">224,832</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,809,235</td>
<td align="right">3,443,832</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">39,059,543</td>
<td align="right">47,864,136</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">3,393,991</td>
<td align="right">4,145,989</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">7,421,319</td>
<td align="right">9,061,727</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,542,886</td>
<td align="right">7,984,243</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">34,127,580</td>
<td align="right">41,239,769</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">10,699,600</td>
<td align="right">12,786,275</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">3,687,735</td>
<td align="right">4,395,560</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">3,113,921</td>
<td align="right">3,707,948</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,025,840</td>
<td align="right">10,713,560</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">414,993</td>
<td align="right">487,040</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">120,649,517</td>
<td align="right">140,804,840</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">8,535,812</td>
<td align="right">9,952,286</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">974,886</td>
<td align="right">1,131,834</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,570,370</td>
<td align="right">9,851,930</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,688,780</td>
<td align="right">3,081,704</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">508,524</td>
<td align="right">582,385</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">3,089,917</td>
<td align="right">3,494,499</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">458,859</td>
<td align="right">517,675</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">49,589,988</td>
<td align="right">55,061,528</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,444,899</td>
<td align="right">1,603,965</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">10,332,252</td>
<td align="right">11,329,766</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">29,956,806</td>
<td align="right">32,520,802</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">11,397</td>
<td align="right">12,357</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">44,289,512</td>
<td align="right">47,032,783</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">3,103,542</td>
<td align="right">3,294,525</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">3,103,542</td>
<td align="right">3,294,525</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">5,240</td>
<td align="right">5,515</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">66,864,938</td>
<td align="right">70,165,844</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">2,287,482</td>
<td align="right">2,384,414</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,696,667</td>
<td align="right">1,755,759</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,696,667</td>
<td align="right">1,755,759</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">3,058,329</td>
<td align="right">3,155,097</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">1,482,913</td>
<td align="right">1,525,170</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,485</td>
<td align="right">1,456</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,337,066</td>
<td align="right">2,378,998</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">80,851</td>
<td align="right">82,015</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">75,339,097</td>
<td align="right">76,050,450</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">11,414,232</td>
<td align="right">11,353,615</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">17,007</td>
<td align="right">17,076</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">7,195</td>
<td align="right">7,216</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">2,265</td>
<td align="right">2,269</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">61,002</td>
<td align="right">60,905</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">8,745</td>
<td align="right">8,757</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">21,767,353</td>
<td align="right">21,770,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_WITH_SPEC</td>
<td align="right">2,417</td>
<td align="right">2,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">147</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">147</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right"></td>
<td align="right">1,290,848</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">295,854</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">153,569</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">152,374</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right"></td>
<td align="right">110,276</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">64,753</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">64,687</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">55,941</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right"></td>
<td align="right">26,073</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right"></td>
<td align="right">19,239</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">16,466</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right"></td>
<td align="right">16,278</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">2,145</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right"></td>
<td align="right">2,145</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">1,742</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">1,329</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">1,082</td>
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
<td align="right">1,264</td>
<td align="right">9,200</td>
<td align="right">627.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">4,476</td>
<td align="right">20,072</td>
<td align="right">348.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">127</td>
<td align="right">215</td>
<td align="right">69.3%</td>
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
<td align="right">8</td>
<td align="right">149</td>
<td align="right">1,762.5%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">8</td>
<td align="right">149</td>
<td align="right">1,762.5%</td>
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
<td align="right">17</td>
<td align="right">17</td>
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
<td align="right">17</td>
<td align="right">17</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-25
