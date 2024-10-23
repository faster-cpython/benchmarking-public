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
<td align="right">12,827,588</td>
<td align="right">3,166.0%</td>
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
<td align="right">2,295</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,750</td>
<td align="right">825</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,387</td>
<td align="right">109</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,288,654</td>
<td align="right">64,268</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">472,377</td>
<td align="right">6,291</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">158,428</td>
<td align="right">4,858</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">741,530</td>
<td align="right">24,059</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">117,056</td>
<td align="right">6,780</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,539,508</td>
<td align="right">2,972,432</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,282,990</td>
<td align="right">102,034</td>
<td align="right">-92.0%</td>
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
<td align="left">CONVERT_VALUE</td>
<td align="right">5,646,553</td>
<td align="right">1,164,030</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,907,776</td>
<td align="right">618,895</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">12,121,067</td>
<td align="right">2,636,422</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">11,749,455</td>
<td align="right">2,570,248</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">10,825,600</td>
<td align="right">2,370,607</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,882,978</td>
<td align="right">1,299,052</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">750,621</td>
<td align="right">182,568</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">610,258</td>
<td align="right">154,957</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">4,617,446</td>
<td align="right">1,174,135</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,905</td>
<td align="right">6,666</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,886,353</td>
<td align="right">486,120</td>
<td align="right">-74.2%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">13,750,183</td>
<td align="right">4,559,735</td>
<td align="right">-66.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">38,269,374</td>
<td align="right">12,759,783</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,265,634</td>
<td align="right">426,790</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,495,681</td>
<td align="right">506,607</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,656,702</td>
<td align="right">2,787,835</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,465,187</td>
<td align="right">1,679,033</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">128,285,735</td>
<td align="right">48,271,018</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,736,002</td>
<td align="right">3,336,850</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">14,297,470</td>
<td align="right">5,619,167</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,201,772</td>
<td align="right">480,262</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">9,370,287</td>
<td align="right">3,851,158</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,397,470</td>
<td align="right">12,535,173</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,821,620</td>
<td align="right">1,194,240</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">266,244</td>
<td align="right">113,870</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,538,716</td>
<td align="right">695,498</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">61,973,000</td>
<td align="right">28,083,607</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">84,414</td>
<td align="right">38,373</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,513,653</td>
<td align="right">2,121,150</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">162,479</td>
<td align="right">77,782</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">671,823</td>
<td align="right">325,833</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">544,894</td>
<td align="right">266,267</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,909,374</td>
<td align="right">1,423,696</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80,946,510</td>
<td align="right">40,669,553</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">117,009,131</td>
<td align="right">173,695,315</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">341,232</td>
<td align="right">181,116</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">142,252</td>
<td align="right">77,217</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,334,191</td>
<td align="right">4,632,857</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,152,822</td>
<td align="right">1,757,063</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">814,256</td>
<td align="right">455,333</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,495,209</td>
<td align="right">1,401,799</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,486,108</td>
<td align="right">846,076</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,063,222</td>
<td align="right">1,190,701</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">42,821,670</td>
<td align="right">24,852,872</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">191,216</td>
<td align="right">111,302</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,131,253</td>
<td align="right">664,980</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,610,044</td>
<td align="right">2,725,081</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">243,448</td>
<td align="right">146,718</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">10,999,964</td>
<td align="right">6,779,058</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">34,490,063</td>
<td align="right">21,257,683</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,912,311</td>
<td align="right">3,087,390</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">96,395,802</td>
<td align="right">61,531,697</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,019,670</td>
<td align="right">1,297,588</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">28,038,124</td>
<td align="right">18,360,165</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">106,826,087</td>
<td align="right">70,143,615</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">448,599,866</td>
<td align="right">296,296,666</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,088,912</td>
<td align="right">724,820</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,877,226</td>
<td align="right">6,596,207</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">3,289,107</td>
<td align="right">2,267,222</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,383,960</td>
<td align="right">955,391</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">134,434</td>
<td align="right">93,062</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">1,211,866</td>
<td align="right">841,844</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,484,194</td>
<td align="right">2,422,422</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">13,621,630</td>
<td align="right">9,537,057</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,776,311</td>
<td align="right">14,589,266</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">15,460,756</td>
<td align="right">10,881,418</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,448,101</td>
<td align="right">3,142,457</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">14,597,140</td>
<td align="right">10,430,503</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,623,279</td>
<td align="right">6,264,046</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">31,327,813</td>
<td align="right">22,833,598</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">68,323,614</td>
<td align="right">50,689,027</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">5,936,531</td>
<td align="right">4,428,754</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,707,266</td>
<td align="right">2,772,433</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">91,331,015</td>
<td align="right">68,805,050</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">131,242,264</td>
<td align="right">99,685,289</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,666,398</td>
<td align="right">4,316,911</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">78,657,567</td>
<td align="right">59,978,104</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">4,141,260</td>
<td align="right">3,208,117</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,647,343</td>
<td align="right">4,405,412</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,660,294</td>
<td align="right">14,641,109</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">24,359,318</td>
<td align="right">19,326,599</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,351,877</td>
<td align="right">4,029,601</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,176,912</td>
<td align="right">956,437</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">14,275,368</td>
<td align="right">11,634,967</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">112,671,651</td>
<td align="right">93,226,517</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">960,944</td>
<td align="right">798,299</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">482,495</td>
<td align="right">401,372</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">70,578</td>
<td align="right">59,559</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">323,870</td>
<td align="right">280,310</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,948,083</td>
<td align="right">6,054,320</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,251,711</td>
<td align="right">43,941,927</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">630,419</td>
<td align="right">559,051</td>
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
<td align="right">3,002,747</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,324,812</td>
<td align="right">2,096,403</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,481,453</td>
<td align="right">1,340,137</td>
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
<td align="right">958,208</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">55,787,355</td>
<td align="right">51,274,527</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,440,533</td>
<td align="right">5,933,316</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">549,114</td>
<td align="right">505,876</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">12,201</td>
<td align="right">11,241</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">774,162</td>
<td align="right">713,824</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">115,389</td>
<td align="right">123,485</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,192,702</td>
<td align="right">1,262,812</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,994,117</td>
<td align="right">2,835,272</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,976,955</td>
<td align="right">5,674,308</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">24,225</td>
<td align="right">25,138</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">5,337,621</td>
<td align="right">5,136,651</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,694</td>
<td align="right">34,385</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,222,783</td>
<td align="right">4,092,872</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,314</td>
<td align="right">9,040</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,720,759</td>
<td align="right">1,678,550</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">37,974,066</td>
<td align="right">37,245,491</td>
<td align="right">-1.9%</td>
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
<td align="left">RERAISE</td>
<td align="right">452,456</td>
<td align="right">446,817</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">3,229</td>
<td align="right">3,208</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">543,124</td>
<td align="right">545,800</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">116,582,458</td>
<td align="right">116,135,440</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">75,888,466</td>
<td align="right">75,770,827</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">14,762</td>
<td align="right">14,750</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">79,173,752</td>
<td align="right">79,145,516</td>
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
<td align="right">38,626</td>
<td align="right">38,632</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">219,361</td>
<td align="right">219,334</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">22,093</td>
<td align="right">22,095</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,526,554</td>
<td align="right">39,527,053</td>
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
<td align="right">6,431,256</td>
<td align="right">37.3%</td>
<td align="right">5,924,643</td>
<td align="right">35.4%</td>
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
<td align="right">10,824,479</td>
<td align="right">62.7%</td>
<td align="right">10,824,479</td>
<td align="right">64.6%</td>
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
<td align="right">8,664</td>
<td align="right">93.4%</td>
<td align="right">8,060</td>
<td align="right">92.9%</td>
<td align="right">-7.0%</td>
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
<td align="right">2,569</td>
<td align="right">31.9%</td>
<td align="right">-14.4%</td>
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
<td align="left">floor divide</td>
<td align="right">119</td>
<td align="right">1.4%</td>
<td align="right">127</td>
<td align="right">1.6%</td>
<td align="right">6.7%</td>
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
<td align="left">and int</td>
<td align="right">187</td>
<td align="right">2.2%</td>
<td align="right">185</td>
<td align="right">2.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,376</td>
<td align="right">27.4%</td>
<td align="right">2,354</td>
<td align="right">29.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">846</td>
<td align="right">9.8%</td>
<td align="right">843</td>
<td align="right">10.5%</td>
<td align="right">-0.4%</td>
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
<td align="right">0.8%</td>
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
<td align="right">1,190,701</td>
<td align="right">100.0%</td>
<td align="right">-42.3%</td>
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
<td align="right">2,996,634</td>
<td align="right">7.9%</td>
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
<td align="right">4,871</td>
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
<td align="right">939</td>
<td align="right">19.3%</td>
<td align="right">-26.1%</td>
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
<td align="right">1,763,569</td>
<td align="right">0.7%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,387</td>
<td align="right">0.0%</td>
<td align="right">14,389</td>
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
<td align="right">239,378,080</td>
<td align="right">99.2%</td>
<td align="right">239,401,821</td>
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
<td align="left">Success</td>
<td align="right">60,022</td>
<td align="right">100.0%</td>
<td align="right">59,027</td>
<td align="right">100.0%</td>
<td align="right">-1.7%</td>
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
<td align="right">626,494</td>
<td align="right">5.4%</td>
<td align="right">555,435</td>
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
<td align="right">2,684</td>
<td align="right">66.2%</td>
<td align="right">2,378</td>
<td align="right">64.3%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,370</td>
<td align="right">33.8%</td>
<td align="right">1,323</td>
<td align="right">35.7%</td>
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
<td align="right">68.7%</td>
<td align="right">1,533</td>
<td align="right">64.5%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">98</td>
<td align="right">3.7%</td>
<td align="right">105</td>
<td align="right">4.4%</td>
<td align="right">7.1%</td>
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
<td align="right">9.5%</td>
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
<td align="right">2,418,651</td>
<td align="right">17.1%</td>
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
<td align="right">11,730,761</td>
<td align="right">77.1%</td>
<td align="right">11,730,732</td>
<td align="right">82.9%</td>
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
<td align="right">3,243</td>
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
<td align="right">1,277</td>
<td align="right">39.4%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,456</td>
<td align="right">30.7%</td>
<td align="right">1,114</td>
<td align="right">34.4%</td>
<td align="right">-23.5%</td>
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
<td align="right">2,968,648</td>
<td align="right">3.9%</td>
<td align="right">26.6%</td>
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
<td align="right">4,026,035</td>
<td align="right">5.3%</td>
<td align="right">20.3%</td>
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
<td align="right">68,514,709</td>
<td align="right">90.7%</td>
<td align="right">-4.1%</td>
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
<td align="right">56,643</td>
<td align="right">95.1%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,220</td>
<td align="right">6.7%</td>
<td align="right">2,917</td>
<td align="right">4.9%</td>
<td align="right">-9.4%</td>
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
<td align="right">0.3%</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">185</td>
<td align="right">5.7%</td>
<td align="right">95</td>
<td align="right">3.3%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">818</td>
<td align="right">25.4%</td>
<td align="right">1,079</td>
<td align="right">37.0%</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">315</td>
<td align="right">9.8%</td>
<td align="right">225</td>
<td align="right">7.7%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">275</td>
<td align="right">8.5%</td>
<td align="right">204</td>
<td align="right">7.0%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,075</td>
<td align="right">33.4%</td>
<td align="right">811</td>
<td align="right">27.8%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">240</td>
<td align="right">7.5%</td>
<td align="right">236</td>
<td align="right">8.1%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">142</td>
<td align="right">4.4%</td>
<td align="right">142</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">76</td>
<td align="right">2.4%</td>
<td align="right">76</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">25</td>
<td align="right">0.8%</td>
<td align="right">25</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15</td>
<td align="right">0.5%</td>
<td align="right">15</td>
<td align="right">0.5%</td>
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
<td align="right">30,080,755</td>
<td align="right">9.9%</td>
<td align="right">12,351,359</td>
<td align="right">4.6%</td>
<td align="right">-58.9%</td>
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
<td align="right">43,930</td>
<td align="right">0.0%</td>
<td align="right">-31.8%</td>
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
<td align="right">44,824,446</td>
<td align="right">16.7%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">209,005,047</td>
<td align="right">68.8%</td>
<td align="right">210,659,651</td>
<td align="right">78.6%</td>
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
<td align="right">9,431</td>
<td align="right">0.6%</td>
<td align="right">4,992</td>
<td align="right">0.5%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,516,990</td>
<td align="right">99.4%</td>
<td align="right">1,023,037</td>
<td align="right">99.5%</td>
<td align="right">-32.6%</td>
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
<td align="right">131</td>
<td align="right">2.6%</td>
<td align="right">-79.7%</td>
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
<td align="right">869</td>
<td align="right">17.4%</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,086</td>
<td align="right">11.5%</td>
<td align="right">596</td>
<td align="right">11.9%</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">994</td>
<td align="right">10.5%</td>
<td align="right">557</td>
<td align="right">11.2%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,965</td>
<td align="right">31.4%</td>
<td align="right">1,723</td>
<td align="right">34.5%</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">530</td>
<td align="right">5.6%</td>
<td align="right">310</td>
<td align="right">6.2%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">112</td>
<td align="right">1.2%</td>
<td align="right">67</td>
<td align="right">1.3%</td>
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
<td align="right">168,787,547</td>
<td align="right">100.0%</td>
<td align="right">98,280,359</td>
<td align="right">100.0%</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,067</td>
<td align="right">0.0%</td>
<td align="right">3,067</td>
<td align="right">0.0%</td>
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
<td align="right">19,445</td>
<td align="right">100.0%</td>
<td align="right">19,447</td>
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
<td align="right">6,250,569</td>
<td align="right">21.6%</td>
<td align="right">-27.4%</td>
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
<td align="right">8,509,934</td>
<td align="right">29.4%</td>
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
<td align="right">14,104,450</td>
<td align="right">43.7%</td>
<td align="right">14,187,794</td>
<td align="right">49.0%</td>
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
<td align="right">9,462</td>
<td align="right">4.9%</td>
<td align="right">8,327</td>
<td align="right">4.8%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">184,604</td>
<td align="right">95.1%</td>
<td align="right">165,353</td>
<td align="right">95.2%</td>
<td align="right">-10.4%</td>
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
<td align="right">643</td>
<td align="right">6.8%</td>
<td align="right">509</td>
<td align="right">6.1%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">308</td>
<td align="right">3.3%</td>
<td align="right">245</td>
<td align="right">2.9%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">4,737</td>
<td align="right">50.1%</td>
<td align="right">3,887</td>
<td align="right">46.7%</td>
<td align="right">-17.9%</td>
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
<td align="right">31.5%</td>
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
<td align="right">123,485</td>
<td align="right">100.0%</td>
<td align="right">7.0%</td>
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
<td align="right">1,336,421</td>
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
<td align="right">2,539,151</td>
<td align="right">1.5%</td>
<td align="right">-78.2%</td>
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
<td align="right">1,438,342</td>
<td align="right">0.8%</td>
<td align="right">-59.0%</td>
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
<td align="right">168,090,309</td>
<td align="right">97.7%</td>
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
<td align="right">93,164</td>
<td align="right">57.0%</td>
<td align="right">27,134</td>
<td align="right">46.6%</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">70,254</td>
<td align="right">43.0%</td>
<td align="right">31,049</td>
<td align="right">53.4%</td>
<td align="right">-55.8%</td>
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
<td align="right">16,118</td>
<td align="right">59.4%</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,074</td>
<td align="right">1.2%</td>
<td align="right">618</td>
<td align="right">2.3%</td>
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
<td align="right">8,005</td>
<td align="right">29.5%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">213</td>
<td align="right">0.2%</td>
<td align="right">190</td>
<td align="right">0.7%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,160</td>
<td align="right">2.3%</td>
<td align="right">2,026</td>
<td align="right">7.5%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">107</td>
<td align="right">0.1%</td>
<td align="right">107</td>
<td align="right">0.4%</td>
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
<td align="right">72,057,435</td>
<td align="right">2.7%</td>
<td align="right">40,039,371</td>
<td align="right">2.0%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">874,765,026</td>
<td align="right">32.8%</td>
<td align="right">538,165,087</td>
<td align="right">27.1%</td>
<td align="right">-38.5%</td>
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
<td align="right">61,890,938</td>
<td align="right">3.1%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,635,197,719</td>
<td align="right">61.3%</td>
<td align="right">1,343,068,385</td>
<td align="right">67.7%</td>
<td align="right">-17.9%</td>
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
<td align="right">2,539,151</td>
<td align="right">6.4%</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,080,755</td>
<td align="right">42.0%</td>
<td align="right">12,351,359</td>
<td align="right">31.1%</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,063,222</td>
<td align="right">2.9%</td>
<td align="right">1,190,701</td>
<td align="right">3.0%</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,478,919</td>
<td align="right">4.9%</td>
<td align="right">2,418,651</td>
<td align="right">6.1%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,608,663</td>
<td align="right">12.0%</td>
<td align="right">6,250,569</td>
<td align="right">15.7%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,348,008</td>
<td align="right">4.7%</td>
<td align="right">4,026,035</td>
<td align="right">10.1%</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">626,494</td>
<td align="right">0.9%</td>
<td align="right">555,435</td>
<td align="right">1.4%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,348,600</td>
<td align="right">4.7%</td>
<td align="right">2,996,634</td>
<td align="right">7.5%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,477,503</td>
<td align="right">2.1%</td>
<td align="right">1,336,421</td>
<td align="right">3.4%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,431,256</td>
<td align="right">9.0%</td>
<td align="right">5,924,643</td>
<td align="right">14.9%</td>
<td align="right">-7.9%</td>
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
<td align="right">2,048,034</td>
<td align="right">3.3%</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,941,581</td>
<td align="right">9.5%</td>
<td align="right">4,872,248</td>
<td align="right">7.9%</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">30,651,138</td>
<td align="right">36.6%</td>
<td align="right">20,333,640</td>
<td align="right">32.9%</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">10,474,119</td>
<td align="right">12.5%</td>
<td align="right">7,084,568</td>
<td align="right">11.4%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,172,977</td>
<td align="right">1.4%</td>
<td align="right">1,485,112</td>
<td align="right">2.4%</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,172,795</td>
<td align="right">1.4%</td>
<td align="right">1,483,536</td>
<td align="right">2.4%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,497,824</td>
<td align="right">11.3%</td>
<td align="right">8,471,745</td>
<td align="right">13.7%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,508,102</td>
<td align="right">11.3%</td>
<td align="right">10,067,990</td>
<td align="right">16.3%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,338,573</td>
<td align="right">2.8%</td>
<td align="right">2,338,563</td>
<td align="right">3.8%</td>
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
<td align="right">772,560</td>
<td align="right">1.2%</td>
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
<td align="right">18,436,951</td>
<td align="right">8.4%</td>
<td align="right">17,711,052</td>
<td align="right">8.1%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,508,781</td>
<td align="right">18.0%</td>
<td align="right">38,780,206</td>
<td align="right">17.7%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,510,455</td>
<td align="right">18.0%</td>
<td align="right">38,781,880</td>
<td align="right">17.7%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,380,362</td>
<td align="right">18.4%</td>
<td align="right">39,646,148</td>
<td align="right">18.1%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,380,362</td>
<td align="right">18.4%</td>
<td align="right">39,646,148</td>
<td align="right">18.1%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">869,907</td>
<td align="right">0.4%</td>
<td align="right">864,268</td>
<td align="right">0.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">179,020,704</td>
<td align="right">81.6%</td>
<td align="right">179,749,279</td>
<td align="right">81.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">7,050,327</td>
<td align="right">3.2%</td>
<td align="right">7,043,171</td>
<td align="right">3.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,044,439</td>
<td align="right">72.0%</td>
<td align="right">158,047,115</td>
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
<td align="right">1,645,550,070</td>
<td align="right">40.4%</td>
<td align="right">2,145,514,900</td>
<td align="right">50.3%</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,499,057,118</td>
<td align="right">34.3%</td>
<td align="right">1,915,442,220</td>
<td align="right">41.1%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,556,165</td>
<td align="right">0.5%</td>
<td align="right">1,973,423</td>
<td align="right">0.6%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">423,767,994</td>
<td align="right">10.4%</td>
<td align="right">323,998,506</td>
<td align="right">7.6%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,190,989,258</td>
<td align="right">29.2%</td>
<td align="right">922,494,399</td>
<td align="right">21.6%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">440,904,361</td>
<td align="right">10.1%</td>
<td align="right">370,574,072</td>
<td align="right">8.0%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">837,218,872</td>
<td align="right">19.2%</td>
<td align="right">966,927,856</td>
<td align="right">20.8%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,588,530,943</td>
<td align="right">36.4%</td>
<td align="right">1,404,077,159</td>
<td align="right">30.1%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">811,714,517</td>
<td align="right">19.9%</td>
<td align="right">876,249,372</td>
<td align="right">20.5%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">7,310,708</td>
<td align="right"></td>
<td align="right">7,778,283</td>
<td align="right"></td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">9,141,669</td>
<td align="right"></td>
<td align="right">9,606,366</td>
<td align="right"></td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">61,674</td>
<td align="right">0.0%</td>
<td align="right">64,409</td>
<td align="right">0.0%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">200,890,758</td>
<td align="right"></td>
<td align="right">194,645,006</td>
<td align="right"></td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">155,205,350</td>
<td align="right"></td>
<td align="right">153,755,537</td>
<td align="right"></td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">242,476,164</td>
<td align="right">74.3%</td>
<td align="right">242,963,854</td>
<td align="right">74.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">252,027,602</td>
<td align="right"></td>
<td align="right">252,463,558</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,832,891</td>
<td align="right"></td>
<td align="right">1,830,141</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">83,784,492</td>
<td align="right"></td>
<td align="right">83,866,401</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">83,799,046</td>
<td align="right">25.7%</td>
<td align="right">83,867,836</td>
<td align="right">25.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">240,858,325</td>
<td align="right">73.8%</td>
<td align="right">240,926,022</td>
<td align="right">73.7%</td>
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
<td align="right">6,261</td>
<td align="right">12,378,927</td>
<td align="right">367,160,727</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">3,322</td>
<td align="right">1.0%</td>
<td align="right">22,494</td>
<td align="right">2.2%</td>
<td align="right">577.1%</td>
</tr>
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
<td align="right">196</td>
<td align="right">0.0%</td>
<td align="right">444.4%</td>
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
<td align="right">6,164</td>
<td align="right">0.6%</td>
<td align="right">324.8%</td>
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
<td align="right">800,968</td>
<td align="right">79.1%</td>
<td align="right">249.9%</td>
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
<td align="right">455,452</td>
<td align="right">45.0%</td>
<td align="right">239.0%</td>
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
<td align="right">1,012,213</td>
<td align="right"></td>
<td align="right">206.9%</td>
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
<td align="right">211,161</td>
<td align="right">20.9%</td>
<td align="right">109.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">3,837,815,070</td>
<td align="right">963.5%</td>
<td align="right">5,728,841,078</td>
<td align="right">990.5%</td>
<td align="right">49.3%</td>
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
<td align="right">578,350,241</td>
<td align="right"></td>
<td align="right">45.2%</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">220,159</td>
<td align="right">96.2%</td>
<td align="right">790,879</td>
<td align="right">98.7%</td>
<td align="right">259.2%</td>
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
<td align="right">800,968</td>
<td align="right"></td>
<td align="right">249.9%</td>
</tr>
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
<td align="right">507</td>
<td align="right">0.1%</td>
<td align="right">507 / 0 !!</td>
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
<td align="right">11,494</td>
<td align="right">1.4%</td>
<td align="right">11,494 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,237</td>
<td align="right">7.1%</td>
<td align="right">33,905</td>
<td align="right">4.2%</td>
<td align="right">108.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">59,359</td>
<td align="right">25.9%</td>
<td align="right">137,580</td>
<td align="right">17.2%</td>
<td align="right">131.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">85,957</td>
<td align="right">37.5%</td>
<td align="right">339,539</td>
<td align="right">42.4%</td>
<td align="right">295.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">50,927</td>
<td align="right">22.2%</td>
<td align="right">198,049</td>
<td align="right">24.7%</td>
<td align="right">288.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">16,119</td>
<td align="right">7.0%</td>
<td align="right">71,001</td>
<td align="right">8.9%</td>
<td align="right">340.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">344</td>
<td align="right">0.2%</td>
<td align="right">7,960</td>
<td align="right">1.0%</td>
<td align="right">2,214.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,440</td>
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
<td align="right">29,874</td>
<td align="right">3.7%</td>
<td align="right">340.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">43,207</td>
<td align="right">18.9%</td>
<td align="right">67,163</td>
<td align="right">8.4%</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">48,620</td>
<td align="right">21.2%</td>
<td align="right">205,945</td>
<td align="right">25.7%</td>
<td align="right">323.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">90,974</td>
<td align="right">39.7%</td>
<td align="right">348,469</td>
<td align="right">43.5%</td>
<td align="right">283.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">28,141</td>
<td align="right">12.3%</td>
<td align="right">113,467</td>
<td align="right">14.2%</td>
<td align="right">303.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,388</td>
<td align="right">1.0%</td>
<td align="right">23,182</td>
<td align="right">2.9%</td>
<td align="right">870.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">44</td>
<td align="right">0.0%</td>
<td align="right">2,611</td>
<td align="right">0.3%</td>
<td align="right">5,834.1%</td>
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
<td align="right">146,068</td>
<td align="right">356,163.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">83,035</td>
<td align="right">115,433,367</td>
<td align="right">138,917.7%</td>
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
<td align="right">719,198</td>
<td align="right">41,544.4%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">19,971</td>
<td align="right">7,244,357</td>
<td align="right">36,174.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">9,026</td>
<td align="right">2,707,041</td>
<td align="right">29,891.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1</td>
<td align="right">275</td>
<td align="right">27,400.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">1,886</td>
<td align="right">468,159</td>
<td align="right">24,722.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">892</td>
<td align="right">128,211</td>
<td align="right">14,273.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,571</td>
<td align="right">366,663</td>
<td align="right">14,161.5%</td>
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
<td align="right">4,518,827</td>
<td align="right">12,347.2%</td>
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
<td align="right">4,648,866</td>
<td align="right">7,058.7%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">32,984</td>
<td align="right">2,321,865</td>
<td align="right">6,939.4%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">14,961</td>
<td align="right">853,805</td>
<td align="right">5,606.9%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">14,961</td>
<td align="right">852,540</td>
<td align="right">5,598.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">18,718</td>
<td align="right">1,007,792</td>
<td align="right">5,284.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">3,718</td>
<td align="right">163,834</td>
<td align="right">4,306.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">43,909</td>
<td align="right">1,868,830</td>
<td align="right">4,156.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">63,316</td>
<td align="right">2,455,819</td>
<td align="right">3,778.7%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">74,993</td>
<td align="right">2,861,147</td>
<td align="right">3,715.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">242,201</td>
<td align="right">8,540,077</td>
<td align="right">3,426.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">11,507</td>
<td align="right">376,119</td>
<td align="right">3,168.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">333,665</td>
<td align="right">7,535,113</td>
<td align="right">2,158.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">58,486</td>
<td align="right">1,239,482</td>
<td align="right">2,019.3%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">29,298</td>
<td align="right">495,384</td>
<td align="right">1,590.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">65,559</td>
<td align="right">787,069</td>
<td align="right">1,100.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">102,848</td>
<td align="right">996,076</td>
<td align="right">868.5%</td>
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
<td align="right">23,814</td>
<td align="right">779.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">690,436</td>
<td align="right">5,933,732</td>
<td align="right">759.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">690,436</td>
<td align="right">5,933,732</td>
<td align="right">759.4%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">47,421</td>
<td align="right">406,287</td>
<td align="right">756.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">38,250</td>
<td align="right">315,250</td>
<td align="right">724.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">82,636</td>
<td align="right">650,646</td>
<td align="right">687.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">1,077,411</td>
<td align="right">7,222,743</td>
<td align="right">570.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">28,553</td>
<td align="right">177,104</td>
<td align="right">520.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,223</td>
<td align="right">88,042</td>
<td align="right">383.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">937,690</td>
<td align="right">4,368,371</td>
<td align="right">365.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,447,650</td>
<td align="right">9,528,682</td>
<td align="right">289.3%</td>
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
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">173,014</td>
<td align="right">632,948</td>
<td align="right">265.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">11,131,750</td>
<td align="right">39,502,121</td>
<td align="right">254.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">3,472,409</td>
<td align="right">12,150,712</td>
<td align="right">249.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,992,433</td>
<td align="right">6,863,830</td>
<td align="right">244.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,447,316</td>
<td align="right">4,729,915</td>
<td align="right">226.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,577,644</td>
<td align="right">4,810,854</td>
<td align="right">204.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">5,209,455</td>
<td align="right">15,608,729</td>
<td align="right">199.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">812,695</td>
<td align="right">2,320,472</td>
<td align="right">185.5%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,286</td>
<td align="right">3,547</td>
<td align="right">175.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">5,448,385</td>
<td align="right">14,933,030</td>
<td align="right">174.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,045,128</td>
<td align="right">2,786,271</td>
<td align="right">166.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">70,330,900</td>
<td align="right">179,162,565</td>
<td align="right">154.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">3,577,024</td>
<td align="right">9,096,845</td>
<td align="right">154.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,724</td>
<td align="right">263,810</td>
<td align="right">144.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,724</td>
<td align="right">263,810</td>
<td align="right">144.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">26,700,039</td>
<td align="right">64,799,027</td>
<td align="right">142.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">6,112,823</td>
<td align="right">14,567,816</td>
<td align="right">138.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">7,043,598</td>
<td align="right">16,570,180</td>
<td align="right">135.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,739,445</td>
<td align="right">6,440,779</td>
<td align="right">135.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,065,560</td>
<td align="right">2,499,354</td>
<td align="right">134.6%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">303,521</td>
<td align="right">700,524</td>
<td align="right">130.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">25,559,490</td>
<td align="right">58,114,893</td>
<td align="right">127.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">225,813</td>
<td align="right">504,447</td>
<td align="right">123.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">760,635</td>
<td align="right">1,695,468</td>
<td align="right">122.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">27,643,734</td>
<td align="right">61,511,477</td>
<td align="right">122.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">352,962</td>
<td align="right">781,531</td>
<td align="right">121.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">182,808</td>
<td align="right">404,559</td>
<td align="right">121.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">724,077</td>
<td align="right">1,596,598</td>
<td align="right">120.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">9,256</td>
<td align="right">20,275</td>
<td align="right">119.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">27,593,706</td>
<td align="right">60,109,312</td>
<td align="right">117.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,116,003</td>
<td align="right">4,564,252</td>
<td align="right">115.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,442,113</td>
<td align="right">3,069,493</td>
<td align="right">112.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">996,150</td>
<td align="right">2,056,447</td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">18,709,809</td>
<td align="right">36,344,396</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,488,050</td>
<td align="right">2,825,118</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,271,919</td>
<td align="right">28,136,392</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">14,863,575</td>
<td align="right">27,207,666</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">24,780,665</td>
<td align="right">45,096,967</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,907,541</td>
<td align="right">21,582,834</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">79,399,911</td>
<td align="right">143,403,295</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">5,115,903</td>
<td align="right">9,135,088</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,724,311</td>
<td align="right">22,633,254</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,488,778</td>
<td align="right">9,709,388</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">188,293</td>
<td align="right">329,375</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">414,993</td>
<td align="right">722,388</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">187,474,111</td>
<td align="right">325,086,035</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,938,195</td>
<td align="right">3,333,954</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,735,906</td>
<td align="right">6,376,307</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,735,906</td>
<td align="right">6,376,307</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">430,912</td>
<td align="right">728,286</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">51,218,643</td>
<td align="right">15,884,673</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">28,167,384</td>
<td align="right">47,529,487</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">550,598</td>
<td align="right">902,939</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">5,629,477</td>
<td align="right">9,230,641</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,965,799</td>
<td align="right">6,431,371</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,502,158</td>
<td align="right">2,419,724</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,555,609</td>
<td align="right">2,472,609</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">13,694,443</td>
<td align="right">21,672,585</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,256,418</td>
<td align="right">1,979,164</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">27,423,235</td>
<td align="right">43,038,516</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">74,188</td>
<td align="right">116,397</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">809,213</td>
<td align="right">1,265,252</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">37,246,934</td>
<td align="right">57,217,999</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">576,380</td>
<td align="right">879,027</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">2,001,348</td>
<td align="right">3,047,905</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">21,337,913</td>
<td align="right">32,159,878</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">320,441,041</td>
<td align="right">479,410,088</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">370,931</td>
<td align="right">554,136</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,772,736</td>
<td align="right">7,111,196</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">46,994,028</td>
<td align="right">69,449,933</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">3,103,542</td>
<td align="right">1,670,618</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">3,103,542</td>
<td align="right">1,670,618</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">809,010</td>
<td align="right">1,182,476</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">808,441</td>
<td align="right">1,178,463</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">398,307,903</td>
<td align="right">578,350,241</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">50,922,067</td>
<td align="right">73,577,889</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">5,113,977</td>
<td align="right">7,360,413</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">41,288,552</td>
<td align="right">59,417,862</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">17,997,936</td>
<td align="right">25,899,470</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">409,722,135</td>
<td align="right">589,530,870</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">41,231,578</td>
<td align="right">58,974,152</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">226,678,233</td>
<td align="right">322,811,948</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">13,847,321</td>
<td align="right">19,537,305</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">54,756,671</td>
<td align="right">76,392,617</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">311,178,832</td>
<td align="right">432,267,095</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">4,924,376</td>
<td align="right">6,677,214</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,485</td>
<td align="right">986</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">95,509,997</td>
<td align="right">125,699,809</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,895,526</td>
<td align="right">3,807,416</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,321,489</td>
<td align="right">9,618,344</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">157,329</td>
<td align="right">200,889</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">157,329</td>
<td align="right">200,889</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">12,817,852</td>
<td align="right">16,278,333</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">73,545,429</td>
<td align="right">92,239,776</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">73,486,070</td>
<td align="right">91,786,394</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">179,594</td>
<td align="right">222,832</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">38,357,894</td>
<td align="right">47,543,785</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">5,521,438</td>
<td align="right">6,813,252</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">49,589,988</td>
<td align="right">38,510,911</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">21,767,353</td>
<td align="right">17,077,137</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,542,886</td>
<td align="right">7,848,530</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">7,421,319</td>
<td align="right">8,898,578</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">39,059,543</td>
<td align="right">46,482,782</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">10,699,600</td>
<td align="right">12,732,603</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,476,059</td>
<td align="right">2,936,772</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,809,235</td>
<td align="right">3,315,857</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">78,774,603</td>
<td align="right">91,488,804</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">508,524</td>
<td align="right">588,438</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">3,113,921</td>
<td align="right">3,579,774</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">3,687,738</td>
<td align="right">4,216,674</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">458,859</td>
<td align="right">523,894</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">34,127,580</td>
<td align="right">38,640,408</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,688,780</td>
<td align="right">3,035,555</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">8,535,812</td>
<td align="right">9,629,193</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">974,886</td>
<td align="right">1,093,576</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">3,393,991</td>
<td align="right">3,772,773</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">70,962,958</td>
<td align="right">78,877,371</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">80,851</td>
<td align="right">72,755</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">120,649,517</td>
<td align="right">132,132,623</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,444,899</td>
<td align="right">1,576,366</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">11,397</td>
<td align="right">12,357</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">3,089,917</td>
<td align="right">3,290,887</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,025,840</td>
<td align="right">9,602,000</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">75,339,097</td>
<td align="right">79,876,235</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">5,240</td>
<td align="right">5,515</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">29,956,806</td>
<td align="right">31,317,943</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">2,287,482</td>
<td align="right">2,384,212</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">10,332,252</td>
<td align="right">9,903,149</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">3,058,329</td>
<td align="right">3,155,013</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,337,066</td>
<td align="right">2,266,956</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">1,482,913</td>
<td align="right">1,524,985</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,570,370</td>
<td align="right">8,789,160</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,696,667</td>
<td align="right">1,738,039</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,696,667</td>
<td align="right">1,738,039</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">11,414,232</td>
<td align="right">11,180,629</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">44,289,512</td>
<td align="right">44,977,220</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">61,002</td>
<td align="right">60,089</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">66,864,938</td>
<td align="right">67,509,866</td>
<td align="right">1.0%</td>
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
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">17,007</td>
<td align="right">17,034</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">8,745</td>
<td align="right">8,757</td>
<td align="right">0.1%</td>
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
<td align="right">1,284,915</td>
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
<td align="right">153,570</td>
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
<td align="right">64,742</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">64,677</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">46,041</td>
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
<td align="right">1,309</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">1,024</td>
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
<td align="right">12,043</td>
<td align="right">852.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">4,476</td>
<td align="right">27,893</td>
<td align="right">523.2%</td>
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
Stats gathered on: 2024-10-23
