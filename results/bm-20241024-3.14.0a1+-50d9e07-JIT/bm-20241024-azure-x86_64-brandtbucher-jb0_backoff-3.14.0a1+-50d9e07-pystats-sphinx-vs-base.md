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
<td align="right">13,569,063</td>
<td align="right">3,354.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,686,999</td>
<td align="right">2,296</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">76,798</td>
<td align="right">124</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,750</td>
<td align="right">1,031</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,288,654</td>
<td align="right">55,383</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,387</td>
<td align="right">157</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">472,377</td>
<td align="right">9,146</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">158,428</td>
<td align="right">6,039</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">741,530</td>
<td align="right">30,724</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">117,056</td>
<td align="right">6,844</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,282,990</td>
<td align="right">101,916</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">136,473</td>
<td align="right">14,960</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,646,553</td>
<td align="right">1,164,324</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,907,776</td>
<td align="right">620,944</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">11,749,455</td>
<td align="right">2,579,907</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,882,978</td>
<td align="right">1,303,297</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">10,825,600</td>
<td align="right">2,450,762</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">32,048</td>
<td align="right">7,581</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">750,621</td>
<td align="right">183,312</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">4,617,446</td>
<td align="right">1,168,566</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">610,258</td>
<td align="right">155,431</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,886,353</td>
<td align="right">483,631</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">12,121,067</td>
<td align="right">3,151,869</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">151,245</td>
<td align="right">42,901</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">253,749</td>
<td align="right">73,834</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,905</td>
<td align="right">8,272</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">13,750,183</td>
<td align="right">4,550,841</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,539,508</td>
<td align="right">2,560,517</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,265,634</td>
<td align="right">430,066</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,495,681</td>
<td align="right">515,339</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,656,702</td>
<td align="right">2,659,715</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">38,269,374</td>
<td align="right">14,541,863</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">128,285,735</td>
<td align="right">49,447,313</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,821,620</td>
<td align="right">1,121,215</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,201,772</td>
<td align="right">482,769</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">671,823</td>
<td align="right">272,983</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,736,002</td>
<td align="right">3,699,353</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,397,476</td>
<td align="right">12,901,244</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">14,297,470</td>
<td align="right">6,170,123</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">266,244</td>
<td align="right">116,060</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">61,973,000</td>
<td align="right">27,907,201</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,538,716</td>
<td align="right">698,076</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,465,187</td>
<td align="right">2,030,965</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,513,653</td>
<td align="right">2,118,446</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,909,374</td>
<td align="right">1,370,709</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">162,479</td>
<td align="right">78,315</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">84,414</td>
<td align="right">40,984</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">544,923</td>
<td align="right">264,664</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80,946,542</td>
<td align="right">40,970,772</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">117,009,131</td>
<td align="right">174,105,349</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,063,222</td>
<td align="right">1,076,450</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">9,370,287</td>
<td align="right">4,946,622</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">341,232</td>
<td align="right">182,676</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">814,256</td>
<td align="right">439,765</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,152,822</td>
<td align="right">1,717,267</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,495,209</td>
<td align="right">1,380,797</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,486,108</td>
<td align="right">863,961</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">42,821,670</td>
<td align="right">25,105,431</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,610,044</td>
<td align="right">2,710,368</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">142,252</td>
<td align="right">83,962</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,334,191</td>
<td align="right">4,953,278</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,131,253</td>
<td align="right">674,947</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">243,448</td>
<td align="right">147,170</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">10,999,964</td>
<td align="right">6,724,358</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">191,216</td>
<td align="right">118,371</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">34,490,063</td>
<td align="right">21,613,016</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,912,311</td>
<td align="right">3,086,681</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,019,670</td>
<td align="right">1,291,207</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">28,038,124</td>
<td align="right">18,129,640</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">96,395,805</td>
<td align="right">62,447,675</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">106,826,116</td>
<td align="right">71,013,790</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">448,599,928</td>
<td align="right">299,510,504</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,877,226</td>
<td align="right">6,598,645</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">134,434</td>
<td align="right">89,883</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,088,912</td>
<td align="right">736,095</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">3,289,107</td>
<td align="right">2,248,407</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,383,960</td>
<td align="right">948,444</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,484,194</td>
<td align="right">2,421,571</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,448,101</td>
<td align="right">3,111,048</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">31,327,813</td>
<td align="right">22,672,616</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,623,279</td>
<td align="right">6,258,326</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">1,211,866</td>
<td align="right">883,965</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,776,311</td>
<td align="right">15,262,809</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">68,323,614</td>
<td align="right">50,507,066</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">78,657,598</td>
<td align="right">58,168,352</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">15,460,756</td>
<td align="right">11,477,482</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">5,936,531</td>
<td align="right">4,428,342</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">13,621,633</td>
<td align="right">10,237,593</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,707,266</td>
<td align="right">2,792,123</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">131,242,295</td>
<td align="right">99,295,659</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">14,597,140</td>
<td align="right">11,145,420</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">91,331,018</td>
<td align="right">69,957,976</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">774,162</td>
<td align="right">599,209</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,647,343</td>
<td align="right">4,372,613</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">960,944</td>
<td align="right">751,651</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,666,398</td>
<td align="right">4,437,809</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,660,294</td>
<td align="right">14,634,691</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">4,141,260</td>
<td align="right">3,260,659</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">24,359,318</td>
<td align="right">19,197,377</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">14,275,368</td>
<td align="right">11,570,330</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,176,912</td>
<td align="right">957,303</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">482,495</td>
<td align="right">398,532</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">112,671,651</td>
<td align="right">93,290,320</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">323,870</td>
<td align="right">278,708</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">70,578</td>
<td align="right">60,853</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,251,711</td>
<td align="right">43,857,040</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,948,083</td>
<td align="right">6,140,450</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,324,812</td>
<td align="right">2,059,527</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,355,783</td>
<td align="right">2,980,404</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">630,461</td>
<td align="right">560,208</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20,175</td>
<td align="right">18,152</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,481,453</td>
<td align="right">1,340,248</td>
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
<td align="right">958,524</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,351,877</td>
<td align="right">3,646,934</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">12,201</td>
<td align="right">11,243</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,440,575</td>
<td align="right">5,939,390</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">549,114</td>
<td align="right">506,885</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">55,787,355</td>
<td align="right">51,503,448</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">115,389</td>
<td align="right">123,019</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,994,117</td>
<td align="right">2,812,261</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,192,702</td>
<td align="right">1,262,090</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,976,955</td>
<td align="right">5,675,397</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,222,783</td>
<td align="right">4,055,918</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">24,225</td>
<td align="right">25,166</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">5,337,621</td>
<td align="right">5,143,008</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,694</td>
<td align="right">34,591</td>
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
<td align="right">1,679,599</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">37,974,066</td>
<td align="right">37,343,048</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">452,456</td>
<td align="right">446,355</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">543,124</td>
<td align="right">545,924</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">116,582,461</td>
<td align="right">116,138,817</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">3,229</td>
<td align="right">3,224</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">75,888,466</td>
<td align="right">75,773,378</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">79,173,752</td>
<td align="right">79,122,530</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">22,099</td>
<td align="right">22,087</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">38,632</td>
<td align="right">38,622</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">219,361</td>
<td align="right">219,346</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,526,554</td>
<td align="right">39,526,887</td>
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
<td align="left">STORE_NAME</td>
<td align="right">20,645</td>
<td align="right">20,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">14,762</td>
<td align="right">14,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,663</td>
<td align="right">10,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,706</td>
<td align="right">8,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,559</td>
<td align="right">8,559</td>
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
<td align="right">5,930,509</td>
<td align="right">35.4%</td>
<td align="right">-7.8%</td>
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
<td align="right">8,675</td>
<td align="right">93.4%</td>
<td align="right">8,268</td>
<td align="right">93.1%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">613</td>
<td align="right">6.6%</td>
<td align="right">613</td>
<td align="right">6.9%</td>
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
<td align="right">45</td>
<td align="right">0.5%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,002</td>
<td align="right">34.6%</td>
<td align="right">2,698</td>
<td align="right">32.6%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">130</td>
<td align="right">1.5%</td>
<td align="right">123</td>
<td align="right">1.5%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,508</td>
<td align="right">17.4%</td>
<td align="right">1,441</td>
<td align="right">17.4%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">187</td>
<td align="right">2.2%</td>
<td align="right">185</td>
<td align="right">2.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">2.6%</td>
<td align="right">228</td>
<td align="right">2.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">846</td>
<td align="right">9.8%</td>
<td align="right">843</td>
<td align="right">10.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,376</td>
<td align="right">27.4%</td>
<td align="right">2,374</td>
<td align="right">28.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">251</td>
<td align="right">2.9%</td>
<td align="right">251</td>
<td align="right">3.0%</td>
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
<td align="right">1,076,450</td>
<td align="right">100.0%</td>
<td align="right">-47.8%</td>
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
<td align="right">2,974,306</td>
<td align="right">7.9%</td>
<td align="right">-11.2%</td>
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
<td align="right">85.9%</td>
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
<td align="right">4,856</td>
<td align="right">9.6%</td>
<td align="right">-18.2%</td>
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
<td align="left">buffer int</td>
<td align="right">238</td>
<td align="right">4.0%</td>
<td align="right">148</td>
<td align="right">3.0%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">1,271</td>
<td align="right">21.4%</td>
<td align="right">873</td>
<td align="right">18.0%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">113</td>
<td align="right">1.9%</td>
<td align="right">88</td>
<td align="right">1.8%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">780</td>
<td align="right">13.1%</td>
<td align="right">651</td>
<td align="right">13.4%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">304</td>
<td align="right">5.1%</td>
<td align="right">261</td>
<td align="right">5.4%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,989</td>
<td align="right">50.3%</td>
<td align="right">2,590</td>
<td align="right">53.3%</td>
<td align="right">-13.3%</td>
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
<td align="right">1,756,519</td>
<td align="right">0.7%</td>
<td align="right">-3.2%</td>
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
<td align="right">14,384</td>
<td align="right">0.0%</td>
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
<td align="right">239,378,109</td>
<td align="right">99.2%</td>
<td align="right">239,419,089</td>
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
<td align="right">60,026</td>
<td align="right">100.0%</td>
<td align="right">58,883</td>
<td align="right">100.0%</td>
<td align="right">-1.9%</td>
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
<td align="right">556,550</td>
<td align="right">4.8%</td>
<td align="right">-11.2%</td>
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
<td align="right">2,420</td>
<td align="right">64.7%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,370</td>
<td align="right">33.7%</td>
<td align="right">1,323</td>
<td align="right">35.3%</td>
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
<td align="right">1,579</td>
<td align="right">65.2%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">109</td>
<td align="right">4.0%</td>
<td align="right">101</td>
<td align="right">4.2%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">259</td>
<td align="right">9.6%</td>
<td align="right">259</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">254</td>
<td align="right">9.4%</td>
<td align="right">254</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">157</td>
<td align="right">5.8%</td>
<td align="right">157</td>
<td align="right">6.5%</td>
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
<td align="right">2,417,505</td>
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
<td align="right">3,538</td>
<td align="right">87.0%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">528</td>
<td align="right">10.0%</td>
<td align="right">528</td>
<td align="right">13.0%</td>
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
<td align="right">466</td>
<td align="right">13.2%</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,992</td>
<td align="right">42.0%</td>
<td align="right">1,472</td>
<td align="right">41.6%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,456</td>
<td align="right">30.7%</td>
<td align="right">1,142</td>
<td align="right">32.3%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">565</td>
<td align="right">11.9%</td>
<td align="right">458</td>
<td align="right">12.9%</td>
<td align="right">-18.9%</td>
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
<td align="right">3,081,735</td>
<td align="right">4.1%</td>
<td align="right">31.4%</td>
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
<td align="right">3,643,459</td>
<td align="right">4.8%</td>
<td align="right">8.8%</td>
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
<td align="right">68,605,471</td>
<td align="right">91.1%</td>
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
<td align="left">Success</td>
<td align="right">44,904</td>
<td align="right">93.3%</td>
<td align="right">58,779</td>
<td align="right">95.4%</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,220</td>
<td align="right">6.7%</td>
<td align="right">2,826</td>
<td align="right">4.6%</td>
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
<td align="right">3.4%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">275</td>
<td align="right">8.5%</td>
<td align="right">184</td>
<td align="right">6.5%</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">315</td>
<td align="right">9.8%</td>
<td align="right">225</td>
<td align="right">8.0%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">818</td>
<td align="right">25.4%</td>
<td align="right">1,004</td>
<td align="right">35.5%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,075</td>
<td align="right">33.4%</td>
<td align="right">834</td>
<td align="right">29.5%</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">240</td>
<td align="right">7.5%</td>
<td align="right">217</td>
<td align="right">7.7%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">142</td>
<td align="right">4.4%</td>
<td align="right">142</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">76</td>
<td align="right">2.4%</td>
<td align="right">76</td>
<td align="right">2.7%</td>
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
<td align="right">30,080,757</td>
<td align="right">9.9%</td>
<td align="right">12,716,919</td>
<td align="right">4.7%</td>
<td align="right">-57.7%</td>
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
<td align="right">46,432,616</td>
<td align="right">17.2%</td>
<td align="right">-27.7%</td>
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
<td align="right">210,059,164</td>
<td align="right">78.0%</td>
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
<td align="left">Failure</td>
<td align="right">9,431</td>
<td align="right">0.6%</td>
<td align="right">5,243</td>
<td align="right">0.5%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,516,994</td>
<td align="right">99.4%</td>
<td align="right">1,053,510</td>
<td align="right">99.5%</td>
<td align="right">-30.6%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">644</td>
<td align="right">6.8%</td>
<td align="right">131</td>
<td align="right">2.5%</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">259</td>
<td align="right">2.7%</td>
<td align="right">65</td>
<td align="right">1.2%</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,116</td>
<td align="right">22.4%</td>
<td align="right">987</td>
<td align="right">18.8%</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">994</td>
<td align="right">10.5%</td>
<td align="right">539</td>
<td align="right">10.3%</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">530</td>
<td align="right">5.6%</td>
<td align="right">310</td>
<td align="right">5.9%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,086</td>
<td align="right">11.5%</td>
<td align="right">646</td>
<td align="right">12.3%</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">112</td>
<td align="right">1.2%</td>
<td align="right">68</td>
<td align="right">1.3%</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,965</td>
<td align="right">31.4%</td>
<td align="right">1,818</td>
<td align="right">34.7%</td>
<td align="right">-38.7%</td>
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
<td align="right">1.2%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">72</td>
<td align="right">0.8%</td>
<td align="right">72</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
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
<td align="right">98,973,441</td>
<td align="right">100.0%</td>
<td align="right">-41.4%</td>
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
<td align="right">3,064</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">19,442</td>
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
<td align="right">6,244,691</td>
<td align="right">21.1%</td>
<td align="right">-27.5%</td>
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
<td align="right">9,124,992</td>
<td align="right">30.8%</td>
<td align="right">-4.3%</td>
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
<td align="right">14,238,548</td>
<td align="right">48.1%</td>
<td align="right">1.0%</td>
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
<td align="right">8,483</td>
<td align="right">4.6%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">184,604</td>
<td align="right">95.1%</td>
<td align="right">176,909</td>
<td align="right">95.4%</td>
<td align="right">-4.2%</td>
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
<td align="right">246</td>
<td align="right">2.9%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">643</td>
<td align="right">6.8%</td>
<td align="right">532</td>
<td align="right">6.3%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">4,737</td>
<td align="right">50.1%</td>
<td align="right">3,976</td>
<td align="right">46.9%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">984</td>
<td align="right">10.4%</td>
<td align="right">940</td>
<td align="right">11.1%</td>
<td align="right">-4.5%</td>
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
<td align="right">31.0%</td>
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
<td align="right">123,019</td>
<td align="right">100.0%</td>
<td align="right">6.6%</td>
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
<td align="right">1,336,527</td>
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
<td align="right">3,242</td>
<td align="right">87.1%</td>
<td align="right">-6.6%</td>
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
<td align="right">2,734</td>
<td align="right">84.3%</td>
<td align="right">-7.6%</td>
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
<td align="right">11,652,267</td>
<td align="right">6.4%</td>
<td align="right">2,548,171</td>
<td align="right">1.5%</td>
<td align="right">-78.1%</td>
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
<td align="right">1,403,505</td>
<td align="right">0.8%</td>
<td align="right">-60.0%</td>
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
<td align="right">166,609,281</td>
<td align="right">97.7%</td>
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
<td align="right">93,164</td>
<td align="right">57.0%</td>
<td align="right">27,735</td>
<td align="right">47.7%</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">70,254</td>
<td align="right">43.0%</td>
<td align="right">30,420</td>
<td align="right">52.3%</td>
<td align="right">-56.7%</td>
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
<td align="right">16,638</td>
<td align="right">60.0%</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,074</td>
<td align="right">1.2%</td>
<td align="right">659</td>
<td align="right">2.4%</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">93</td>
<td align="right">0.1%</td>
<td align="right">71</td>
<td align="right">0.3%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,948</td>
<td align="right">10.7%</td>
<td align="right">8,024</td>
<td align="right">28.9%</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">213</td>
<td align="right">0.2%</td>
<td align="right">188</td>
<td align="right">0.7%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,160</td>
<td align="right">2.3%</td>
<td align="right">2,048</td>
<td align="right">7.4%</td>
<td align="right">-5.2%</td>
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
<td align="right">621</td>
<td align="right">0.0%</td>
<td align="right">-99.8%</td>
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
<td align="right">27</td>
<td align="right">6.6%</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">383</td>
<td align="right">79.8%</td>
<td align="right">383</td>
<td align="right">93.4%</td>
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
<td align="right">4</td>
<td align="right">14.8%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">23</td>
<td align="right">23.7%</td>
<td align="right">23</td>
<td align="right">85.2%</td>
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
<td align="right">39,896,333</td>
<td align="right">2.0%</td>
<td align="right">-44.6%</td>
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
<td align="right">540,733,936</td>
<td align="right">27.1%</td>
<td align="right">-38.2%</td>
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
<td align="right">64,185,314</td>
<td align="right">3.2%</td>
<td align="right">-23.4%</td>
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
<td align="right">1,351,647,175</td>
<td align="right">67.7%</td>
<td align="right">-17.3%</td>
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
<td align="right">2,548,171</td>
<td align="right">6.4%</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,080,757</td>
<td align="right">42.0%</td>
<td align="right">12,716,919</td>
<td align="right">32.1%</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,063,222</td>
<td align="right">2.9%</td>
<td align="right">1,076,450</td>
<td align="right">2.7%</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,478,919</td>
<td align="right">4.9%</td>
<td align="right">2,417,505</td>
<td align="right">6.1%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,608,663</td>
<td align="right">12.0%</td>
<td align="right">6,244,691</td>
<td align="right">15.8%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,348,600</td>
<td align="right">4.7%</td>
<td align="right">2,974,306</td>
<td align="right">7.5%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">626,525</td>
<td align="right">0.9%</td>
<td align="right">556,550</td>
<td align="right">1.4%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,477,503</td>
<td align="right">2.1%</td>
<td align="right">1,336,527</td>
<td align="right">3.4%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,348,008</td>
<td align="right">4.7%</td>
<td align="right">3,643,459</td>
<td align="right">9.2%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,431,287</td>
<td align="right">9.0%</td>
<td align="right">5,930,509</td>
<td align="right">15.0%</td>
<td align="right">-7.8%</td>
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
<td align="right">2,429,787</td>
<td align="right">3.8%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">30,651,138</td>
<td align="right">36.6%</td>
<td align="right">20,564,248</td>
<td align="right">32.0%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,172,977</td>
<td align="right">1.4%</td>
<td align="right">1,541,615</td>
<td align="right">2.4%</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,172,795</td>
<td align="right">1.4%</td>
<td align="right">1,540,120</td>
<td align="right">2.4%</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,941,581</td>
<td align="right">9.5%</td>
<td align="right">5,467,340</td>
<td align="right">8.5%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">10,474,119</td>
<td align="right">12.5%</td>
<td align="right">7,590,612</td>
<td align="right">11.8%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,508,102</td>
<td align="right">11.3%</td>
<td align="right">9,948,787</td>
<td align="right">15.5%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,497,824</td>
<td align="right">11.3%</td>
<td align="right">9,086,803</td>
<td align="right">14.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,338,573</td>
<td align="right">2.8%</td>
<td align="right">2,338,563</td>
<td align="right">3.6%</td>
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
<td align="right">780,767</td>
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
<td align="right">17,808,733</td>
<td align="right">8.1%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,508,781</td>
<td align="right">18.0%</td>
<td align="right">38,877,763</td>
<td align="right">17.7%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,510,455</td>
<td align="right">18.0%</td>
<td align="right">38,879,437</td>
<td align="right">17.7%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,380,362</td>
<td align="right">18.4%</td>
<td align="right">39,743,243</td>
<td align="right">18.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,380,362</td>
<td align="right">18.4%</td>
<td align="right">39,743,243</td>
<td align="right">18.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">869,907</td>
<td align="right">0.4%</td>
<td align="right">863,806</td>
<td align="right">0.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">179,020,704</td>
<td align="right">81.6%</td>
<td align="right">179,651,722</td>
<td align="right">81.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">7,050,327</td>
<td align="right">3.2%</td>
<td align="right">7,042,620</td>
<td align="right">3.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,044,439</td>
<td align="right">72.0%</td>
<td align="right">158,047,239</td>
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
<td align="right">2,147,616,824</td>
<td align="right">50.2%</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,499,404,565</td>
<td align="right">34.3%</td>
<td align="right">1,917,924,344</td>
<td align="right">41.1%</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,556,163</td>
<td align="right">0.5%</td>
<td align="right">1,941,311</td>
<td align="right">0.6%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">423,768,053</td>
<td align="right">10.4%</td>
<td align="right">324,184,214</td>
<td align="right">7.6%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,190,989,365</td>
<td align="right">29.2%</td>
<td align="right">927,088,971</td>
<td align="right">21.7%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">440,901,141</td>
<td align="right">10.1%</td>
<td align="right">372,240,252</td>
<td align="right">8.0%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">837,389,195</td>
<td align="right">19.2%</td>
<td align="right">965,122,898</td>
<td align="right">20.7%</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,588,534,414</td>
<td align="right">36.4%</td>
<td align="right">1,408,166,727</td>
<td align="right">30.2%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">811,888,416</td>
<td align="right">19.9%</td>
<td align="right">875,949,092</td>
<td align="right">20.5%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">61,674</td>
<td align="right">0.0%</td>
<td align="right">63,913</td>
<td align="right">0.0%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">200,680,030</td>
<td align="right"></td>
<td align="right">195,426,473</td>
<td align="right"></td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">7,521,442</td>
<td align="right"></td>
<td align="right">7,407,456</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,881,084</td>
<td align="right"></td>
<td align="right">1,908,863</td>
<td align="right"></td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">9,400,457</td>
<td align="right"></td>
<td align="right">9,314,165</td>
<td align="right"></td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">155,157,157</td>
<td align="right"></td>
<td align="right">153,735,685</td>
<td align="right"></td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">242,479,562</td>
<td align="right">74.3%</td>
<td align="right">242,900,784</td>
<td align="right">74.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">83,784,492</td>
<td align="right"></td>
<td align="right">83,885,402</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">252,031,110</td>
<td align="right"></td>
<td align="right">252,269,870</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">83,799,046</td>
<td align="right">25.7%</td>
<td align="right">83,863,805</td>
<td align="right">25.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">240,861,725</td>
<td align="right">73.8%</td>
<td align="right">240,895,560</td>
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
<td align="right">6,278</td>
<td align="right">12,292,130</td>
<td align="right">366,918,934</td>
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
<td align="right">21,028</td>
<td align="right">2.2%</td>
<td align="right">533.0%</td>
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
<td align="right">190</td>
<td align="right">0.0%</td>
<td align="right">427.8%</td>
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
<td align="right">5,842</td>
<td align="right">0.6%</td>
<td align="right">302.6%</td>
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
<td align="right">758,199</td>
<td align="right">78.6%</td>
<td align="right">231.2%</td>
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
<td align="right">437,927</td>
<td align="right">45.4%</td>
<td align="right">226.0%</td>
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
<td align="right">964,929</td>
<td align="right"></td>
<td align="right">192.6%</td>
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
<td align="right">206,730</td>
<td align="right">21.4%</td>
<td align="right">104.9%</td>
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
<td align="right">5,738,439,329</td>
<td align="right">980.8%</td>
<td align="right">49.5%</td>
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
<td align="right">585,086,471</td>
<td align="right"></td>
<td align="right">46.9%</td>
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
<td align="right">744,781</td>
<td align="right">98.2%</td>
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
<td align="right">228,943</td>
<td align="right"></td>
<td align="right">758,199</td>
<td align="right"></td>
<td align="right">231.2%</td>
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
<td align="right">112</td>
<td align="right">0.0%</td>
<td align="right">103.6%</td>
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
<td align="right">422</td>
<td align="right">0.1%</td>
<td align="right">422 / 0 !!</td>
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
<td align="right">10,545</td>
<td align="right">1.4%</td>
<td align="right">10,545 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,237</td>
<td align="right">7.1%</td>
<td align="right">32,246</td>
<td align="right">4.3%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">59,359</td>
<td align="right">25.9%</td>
<td align="right">129,310</td>
<td align="right">17.1%</td>
<td align="right">117.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">85,957</td>
<td align="right">37.5%</td>
<td align="right">322,468</td>
<td align="right">42.5%</td>
<td align="right">275.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">50,927</td>
<td align="right">22.2%</td>
<td align="right">182,863</td>
<td align="right">24.1%</td>
<td align="right">259.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">16,119</td>
<td align="right">7.0%</td>
<td align="right">69,768</td>
<td align="right">9.2%</td>
<td align="right">332.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">344</td>
<td align="right">0.2%</td>
<td align="right">9,904</td>
<td align="right">1.3%</td>
<td align="right">2,779.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,095</td>
<td align="right">0.1%</td>
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
<td align="right">27,358</td>
<td align="right">3.6%</td>
<td align="right">303.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">43,207</td>
<td align="right">18.9%</td>
<td align="right">66,517</td>
<td align="right">8.8%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">48,620</td>
<td align="right">21.2%</td>
<td align="right">192,958</td>
<td align="right">25.4%</td>
<td align="right">296.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">90,974</td>
<td align="right">39.7%</td>
<td align="right">324,380</td>
<td align="right">42.8%</td>
<td align="right">256.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">28,141</td>
<td align="right">12.3%</td>
<td align="right">110,701</td>
<td align="right">14.6%</td>
<td align="right">293.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,388</td>
<td align="right">1.0%</td>
<td align="right">19,796</td>
<td align="right">2.6%</td>
<td align="right">729.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">44</td>
<td align="right">0.0%</td>
<td align="right">3,029</td>
<td align="right">0.4%</td>
<td align="right">6,784.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">42</td>
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
<td align="right">148,733</td>
<td align="right">362,663.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">83,035</td>
<td align="right">114,177,966</td>
<td align="right">137,405.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">184</td>
<td align="right">76,858</td>
<td align="right">41,670.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,727</td>
<td align="right">712,533</td>
<td align="right">41,158.4%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">19,971</td>
<td align="right">7,253,242</td>
<td align="right">36,218.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">9,026</td>
<td align="right">2,707,596</td>
<td align="right">29,897.7%</td>
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
<td align="right">458,192</td>
<td align="right">24,194.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">892</td>
<td align="right">126,212</td>
<td align="right">14,049.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">892</td>
<td align="right">125,073</td>
<td align="right">13,921.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,571</td>
<td align="right">355,388</td>
<td align="right">13,722.9%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">1,338</td>
<td align="right">181,253</td>
<td align="right">13,446.6%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">36,304</td>
<td align="right">4,518,533</td>
<td align="right">12,346.4%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,286</td>
<td align="right">109,630</td>
<td align="right">8,424.9%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">64,940</td>
<td align="right">4,644,621</td>
<td align="right">7,052.2%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">32,984</td>
<td align="right">2,319,816</td>
<td align="right">6,933.2%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">14,961</td>
<td align="right">850,529</td>
<td align="right">5,585.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">14,961</td>
<td align="right">849,500</td>
<td align="right">5,578.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">18,718</td>
<td align="right">999,060</td>
<td align="right">5,237.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">3,718</td>
<td align="right">162,274</td>
<td align="right">4,264.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">43,909</td>
<td align="right">1,869,539</td>
<td align="right">4,157.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">63,316</td>
<td align="right">2,458,523</td>
<td align="right">3,782.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">242,201</td>
<td align="right">8,538,070</td>
<td align="right">3,425.2%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">74,993</td>
<td align="right">2,509,215</td>
<td align="right">3,245.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">11,507</td>
<td align="right">376,731</td>
<td align="right">3,173.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">333,665</td>
<td align="right">7,548,849</td>
<td align="right">2,162.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">58,486</td>
<td align="right">1,239,600</td>
<td align="right">2,019.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">29,298</td>
<td align="right">492,529</td>
<td align="right">1,581.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">65,559</td>
<td align="right">784,562</td>
<td align="right">1,096.7%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">13,156</td>
<td align="right">134,669</td>
<td align="right">923.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">102,848</td>
<td align="right">988,175</td>
<td align="right">860.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">10,293</td>
<td align="right">96,365</td>
<td align="right">836.2%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">47,421</td>
<td align="right">421,854</td>
<td align="right">789.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,709</td>
<td align="right">24,095</td>
<td align="right">789.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">690,436</td>
<td align="right">5,926,001</td>
<td align="right">758.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">690,436</td>
<td align="right">5,926,001</td>
<td align="right">758.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">38,250</td>
<td align="right">312,579</td>
<td align="right">717.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">82,636</td>
<td align="right">649,902</td>
<td align="right">686.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">28,553</td>
<td align="right">197,663</td>
<td align="right">592.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">1,077,411</td>
<td align="right">7,216,255</td>
<td align="right">569.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,223</td>
<td align="right">87,080</td>
<td align="right">377.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">937,690</td>
<td align="right">4,374,397</td>
<td align="right">366.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,507</td>
<td align="right">113,671</td>
<td align="right">285.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,507</td>
<td align="right">113,671</td>
<td align="right">285.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">11,131,750</td>
<td align="right">40,033,005</td>
<td align="right">259.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">173,014</td>
<td align="right">614,999</td>
<td align="right">255.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,992,433</td>
<td align="right">6,991,478</td>
<td align="right">250.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">3,472,409</td>
<td align="right">11,599,756</td>
<td align="right">234.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,577,644</td>
<td align="right">4,783,446</td>
<td align="right">203.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,447,650</td>
<td align="right">7,258,811</td>
<td align="right">196.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">812,695</td>
<td align="right">2,320,884</td>
<td align="right">185.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,724</td>
<td align="right">307,333</td>
<td align="right">185.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,724</td>
<td align="right">307,333</td>
<td align="right">185.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,447,316</td>
<td align="right">4,081,535</td>
<td align="right">182.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">5,209,455</td>
<td align="right">13,934,689</td>
<td align="right">167.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">430,912</td>
<td align="right">1,149,396</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">5,448,385</td>
<td align="right">14,417,583</td>
<td align="right">164.6%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,286</td>
<td align="right">3,309</td>
<td align="right">157.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">7,043,598</td>
<td align="right">18,047,494</td>
<td align="right">156.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">26,700,039</td>
<td align="right">67,034,639</td>
<td align="right">151.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">70,330,897</td>
<td align="right">176,396,511</td>
<td align="right">150.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,045,125</td>
<td align="right">2,583,102</td>
<td align="right">147.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">6,112,823</td>
<td align="right">14,487,661</td>
<td align="right">137.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">724,077</td>
<td align="right">1,710,849</td>
<td align="right">136.3%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">303,521</td>
<td align="right">717,023</td>
<td align="right">136.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,065,560</td>
<td align="right">2,501,557</td>
<td align="right">134.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">225,813</td>
<td align="right">506,075</td>
<td align="right">124.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">25,559,490</td>
<td align="right">57,243,093</td>
<td align="right">124.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">3,577,024</td>
<td align="right">8,001,381</td>
<td align="right">123.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,739,445</td>
<td align="right">6,120,358</td>
<td align="right">123.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">352,962</td>
<td align="right">788,478</td>
<td align="right">123.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">27,643,731</td>
<td align="right">61,567,292</td>
<td align="right">122.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">182,808</td>
<td align="right">403,191</td>
<td align="right">120.6%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">760,635</td>
<td align="right">1,675,778</td>
<td align="right">120.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">27,593,703</td>
<td align="right">60,168,997</td>
<td align="right">118.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,442,113</td>
<td align="right">3,142,518</td>
<td align="right">117.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">24,780,665</td>
<td align="right">51,209,976</td>
<td align="right">106.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">996,150</td>
<td align="right">2,057,593</td>
<td align="right">106.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">9,256</td>
<td align="right">18,981</td>
<td align="right">105.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">18,709,809</td>
<td align="right">36,526,357</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,488,050</td>
<td align="right">2,895,604</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,724,311</td>
<td align="right">23,557,396</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,271,919</td>
<td align="right">28,150,938</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">14,863,575</td>
<td align="right">27,326,999</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,907,541</td>
<td align="right">21,814,664</td>
<td align="right">83.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">79,399,911</td>
<td align="right">142,786,244</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">5,115,903</td>
<td align="right">9,141,506</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,488,778</td>
<td align="right">9,764,001</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,116,003</td>
<td align="right">3,758,679</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">187,474,108</td>
<td align="right">329,184,941</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,965,799</td>
<td align="right">6,941,536</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">188,293</td>
<td align="right">329,269</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,938,195</td>
<td align="right">3,373,750</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,735,906</td>
<td align="right">6,440,944</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,735,906</td>
<td align="right">6,440,944</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">51,218,643</td>
<td align="right">15,963,515</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">28,167,384</td>
<td align="right">47,468,039</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">550,598</td>
<td align="right">925,267</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">370,931</td>
<td align="right">608,643</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">5,629,477</td>
<td align="right">9,204,435</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,502,158</td>
<td align="right">2,437,391</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,256,418</td>
<td align="right">1,985,524</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">37,246,934</td>
<td align="right">58,703,120</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">3,393,991</td>
<td align="right">5,307,600</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">809,213</td>
<td align="right">1,264,778</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">2,001,348</td>
<td align="right">3,114,485</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,555,609</td>
<td align="right">2,420,067</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">74,188</td>
<td align="right">115,348</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">13,694,443</td>
<td align="right">21,138,387</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">576,380</td>
<td align="right">877,938</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">320,441,044</td>
<td align="right">485,773,215</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">46,994,028</td>
<td align="right">69,249,205</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">398,307,903</td>
<td align="right">585,086,471</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">21,337,913</td>
<td align="right">31,104,517</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">409,722,135</td>
<td align="right">595,612,938</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">50,922,064</td>
<td align="right">73,611,693</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">5,113,977</td>
<td align="right">7,361,517</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">17,997,936</td>
<td align="right">25,822,514</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">41,288,552</td>
<td align="right">59,187,836</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">41,231,578</td>
<td align="right">58,750,525</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">13,847,321</td>
<td align="right">19,727,898</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">226,678,230</td>
<td align="right">320,983,648</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,772,736</td>
<td align="right">6,755,994</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">809,010</td>
<td align="right">1,140,098</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">808,441</td>
<td align="right">1,136,342</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">27,423,235</td>
<td align="right">38,443,265</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">311,178,829</td>
<td align="right">429,957,165</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">4,924,373</td>
<td align="right">6,787,375</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">54,756,671</td>
<td align="right">75,068,366</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">3,103,542</td>
<td align="right">2,082,533</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">3,103,542</td>
<td align="right">2,082,533</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,895,526</td>
<td align="right">3,819,453</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,321,489</td>
<td align="right">9,637,360</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">95,509,997</td>
<td align="right">124,226,373</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">157,329</td>
<td align="right">202,491</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">157,329</td>
<td align="right">202,491</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">73,545,426</td>
<td align="right">92,332,060</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">49,589,988</td>
<td align="right">36,950,101</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">73,486,067</td>
<td align="right">91,884,692</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">38,357,894</td>
<td align="right">47,495,676</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">5,521,438</td>
<td align="right">6,822,188</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">179,594</td>
<td align="right">221,823</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">12,817,852</td>
<td align="right">15,826,817</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,485</td>
<td align="right">1,152</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">21,767,353</td>
<td align="right">17,162,024</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,542,886</td>
<td align="right">7,879,939</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">7,421,319</td>
<td align="right">8,921,226</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">10,699,600</td>
<td align="right">12,713,867</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,809,235</td>
<td align="right">3,310,011</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">39,059,543</td>
<td align="right">45,970,960</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">414,993</td>
<td align="right">487,028</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">78,774,603</td>
<td align="right">91,831,035</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">3,113,921</td>
<td align="right">3,584,082</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">3,687,735</td>
<td align="right">4,243,608</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,688,780</td>
<td align="right">3,088,394</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">508,524</td>
<td align="right">581,369</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">8,535,812</td>
<td align="right">9,650,195</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">458,859</td>
<td align="right">517,149</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">34,127,580</td>
<td align="right">38,411,487</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">974,886</td>
<td align="right">1,095,852</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,444,899</td>
<td align="right">1,613,303</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,025,840</td>
<td align="right">10,068,779</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,476,059</td>
<td align="right">2,748,554</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">80,851</td>
<td align="right">73,221</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">70,962,958</td>
<td align="right">77,470,656</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">120,649,517</td>
<td align="right">131,659,906</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">11,397</td>
<td align="right">12,355</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">11,414,232</td>
<td align="right">10,526,467</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">75,339,097</td>
<td align="right">80,742,865</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,570,370</td>
<td align="right">9,138,278</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">3,089,917</td>
<td align="right">3,284,530</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">5,240</td>
<td align="right">5,515</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">2,287,482</td>
<td align="right">2,383,760</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">29,956,806</td>
<td align="right">31,200,475</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">3,058,329</td>
<td align="right">3,154,697</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,337,066</td>
<td align="right">2,267,678</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">1,482,913</td>
<td align="right">1,524,258</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,696,667</td>
<td align="right">1,741,218</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,696,667</td>
<td align="right">1,741,218</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">61,002</td>
<td align="right">60,061</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">44,289,512</td>
<td align="right">44,904,214</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">66,864,938</td>
<td align="right">67,413,790</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">10,332,252</td>
<td align="right">10,294,377</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">17,007</td>
<td align="right">17,022</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">7,195</td>
<td align="right">7,200</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">8,745</td>
<td align="right">8,745</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_WITH_SPEC</td>
<td align="right">2,417</td>
<td align="right">2,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">2,265</td>
<td align="right">2,265</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">147</td>
<td align="right">147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">147</td>
<td align="right">147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right"></td>
<td align="right">1,284,198</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">295,649</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">152,389</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">150,184</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right"></td>
<td align="right">110,212</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">63,990</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">63,990</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">43,430</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right"></td>
<td align="right">24,467</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right"></td>
<td align="right">17,633</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right"></td>
<td align="right">16,230</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right"></td>
<td align="right">15,804</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">1,532</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">1,103</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">1,022</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">567</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right"></td>
<td align="right">567</td>
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
<td align="right">10,805</td>
<td align="right">754.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">4,476</td>
<td align="right">26,656</td>
<td align="right">495.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">127</td>
<td align="right">150</td>
<td align="right">18.1%</td>
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
<td align="right">148</td>
<td align="right">1,750.0%</td>
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
<td align="right">148</td>
<td align="right">1,750.0%</td>
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
