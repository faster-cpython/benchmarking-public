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
<td align="right">22,877,101</td>
<td align="right">61,918,015</td>
<td align="right">170.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">70,050,613</td>
<td align="right">145,515,669</td>
<td align="right">107.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,972,544</td>
<td align="right">10,255,524</td>
<td align="right">106.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,516,744</td>
<td align="right">921,933</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,500,349</td>
<td align="right">1,881,401</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">28,560,388</td>
<td align="right">5,445,851</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,976,070</td>
<td align="right">2,296,656</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">17,309,155</td>
<td align="right">5,207,065</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,644</td>
<td align="right">418,821</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">47,707,221</td>
<td align="right">14,683,529</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">97,868,835</td>
<td align="right">34,120,780</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">156,216,697</td>
<td align="right">56,251,313</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">12,186,249</td>
<td align="right">4,457,770</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">11,814,809</td>
<td align="right">4,560,351</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">22,681,893</td>
<td align="right">8,993,662</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">17,730,690</td>
<td align="right">8,560,697</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,067,786</td>
<td align="right">1,995,432</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,161,376</td>
<td align="right">1,136,448</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,035,324</td>
<td align="right">3,310,814</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">18,860,087</td>
<td align="right">10,464,766</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">58,733,609</td>
<td align="right">32,671,029</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,591</td>
<td align="right">526,729</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,085</td>
<td align="right">745,531</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,622,261</td>
<td align="right">3,777,782</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,028,349</td>
<td align="right">612,486</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,028,954</td>
<td align="right">613,091</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">19,742,169</td>
<td align="right">11,764,704</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">6,143,725</td>
<td align="right">3,740,875</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">4,519,630</td>
<td align="right">2,775,528</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">154,352,161</td>
<td align="right">96,745,041</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">22,415,923</td>
<td align="right">14,085,937</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">39,662,122</td>
<td align="right">25,552,914</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">561,066,923</td>
<td align="right">365,293,025</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">19,400,772</td>
<td align="right">12,637,941</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">31,727,363</td>
<td align="right">20,748,187</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,337</td>
<td align="right">4,469,346</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">642,602</td>
<td align="right">430,278</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">163,055,401</td>
<td align="right">112,666,210</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">83,152,728</td>
<td align="right">57,746,161</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">38,569,266</td>
<td align="right">27,166,780</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">32,859,297</td>
<td align="right">23,423,476</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,165,639</td>
<td align="right">3,714,993</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">190,145,374</td>
<td align="right">137,068,782</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,002,103</td>
<td align="right">4,337,716</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">43,592,592</td>
<td align="right">31,560,252</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">22,435,224</td>
<td align="right">16,571,803</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,056</td>
<td align="right">1,713,078</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,909,932</td>
<td align="right">2,941,410</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,242,787</td>
<td align="right">2,440,433</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">111,160,177</td>
<td align="right">84,437,566</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">41,351,577</td>
<td align="right">31,470,120</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">13,810,389</td>
<td align="right">10,547,151</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">128,899,595</td>
<td align="right">98,492,733</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">13,994,113</td>
<td align="right">10,760,024</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,233,206</td>
<td align="right">1,727,101</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,571,228</td>
<td align="right">5,103,930</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">14,719,868</td>
<td align="right">11,457,103</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">37,762,104</td>
<td align="right">29,876,275</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">133,724</td>
<td align="right">106,319</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">338,565</td>
<td align="right">274,851</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,209</td>
<td align="right">190,056</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">711,020</td>
<td align="right">831,257</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">14,201,224</td>
<td align="right">11,827,932</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">46,985,670</td>
<td align="right">39,213,967</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">384,641</td>
<td align="right">321,473</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,066,786</td>
<td align="right">13,433,542</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,605,480</td>
<td align="right">2,194,422</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,959,833</td>
<td align="right">1,665,929</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,001,348</td>
<td align="right">1,702,197</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,989,759</td>
<td align="right">2,549,891</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,599,276</td>
<td align="right">1,371,259</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,537</td>
<td align="right">368,189</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,634,522</td>
<td align="right">3,187,096</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,095,397</td>
<td align="right">5,411,789</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,191,958</td>
<td align="right">1,064,094</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,113,075</td>
<td align="right">11,834,627</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">27,843,185</td>
<td align="right">25,180,653</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">26,029,645</td>
<td align="right">23,685,047</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,470,978</td>
<td align="right">3,197,766</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,012,162</td>
<td align="right">4,644,644</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">20,519,963</td>
<td align="right">19,087,441</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,451,098</td>
<td align="right">16,289,618</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,521,987</td>
<td align="right">35,727,998</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">9,876,558</td>
<td align="right">9,267,422</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">56,119,825</td>
<td align="right">52,998,874</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">17,406,712</td>
<td align="right">18,373,111</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">456,408</td>
<td align="right">432,870</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,740,538</td>
<td align="right">4,502,253</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,469,472</td>
<td align="right">2,351,850</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">53,883,526</td>
<td align="right">51,437,275</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">41,626,040</td>
<td align="right">43,445,468</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">16,842,082</td>
<td align="right">17,519,287</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">43,467,312</td>
<td align="right">45,182,975</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,150,087</td>
<td align="right">3,030,605</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">12,697,942</td>
<td align="right">13,127,239</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">413,753</td>
<td align="right">425,306</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,344,696</td>
<td align="right">1,378,246</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">493,504</td>
<td align="right">483,206</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">93,769</td>
<td align="right">95,708</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,100,312</td>
<td align="right">3,163,237</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,642,470</td>
<td align="right">17,988,302</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">45,357,510</td>
<td align="right">44,553,782</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">14,140,081</td>
<td align="right">14,387,468</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,753,184</td>
<td align="right">11,944,774</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,485,867</td>
<td align="right">4,426,710</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,650,725</td>
<td align="right">17,834,586</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,326</td>
<td align="right">4,424,559</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,824,720</td>
<td align="right">96,940,851</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,965,820</td>
<td align="right">1,958,237</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">29,319,056</td>
<td align="right">29,416,416</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,074</td>
<td align="right">18,022</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,441</td>
<td align="right">1,445</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">8,940</td>
<td align="right">8,952</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,186</td>
<td align="right">24,157</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,287,898</td>
<td align="right">1,286,853</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">17,021</td>
<td align="right">17,008</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,965</td>
<td align="right">2,963</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,048</td>
<td align="right">655,243</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,048</td>
<td align="right">655,243</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,048</td>
<td align="right">655,243</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">147,595</td>
<td align="right">147,557</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,216</td>
<td align="right">40,226</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,617</td>
<td align="right">165,655</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">182,062,723</td>
<td align="right">182,101,210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,878</td>
<td align="right">389,950</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">642,586</td>
<td align="right">642,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">20,680</td>
<td align="right">20,678</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,295</td>
<td align="right">746,367</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">174,919</td>
<td align="right">174,934</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,704,226</td>
<td align="right">15,702,977</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,728,096</td>
<td align="right">3,728,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">172,046</td>
<td align="right">172,039</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,461,662</td>
<td align="right">4,461,798</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,885</td>
<td align="right">745,864</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,089</td>
<td align="right">83,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,720,589</td>
<td align="right">1,720,595</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,519</td>
<td align="right">1,244,521</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,976,741</td>
<td align="right">21,976,720</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">372,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">270,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">178,536</td>
<td align="right">178,536</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">178,534</td>
<td align="right">178,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">89,010</td>
<td align="right">89,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">78,653</td>
<td align="right">78,653</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">13,963</td>
<td align="right">13,963</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">9,212</td>
<td align="right">9,212</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,941</td>
<td align="right">8,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">8,778</td>
<td align="right">8,778</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,742</td>
<td align="right">3,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,645</td>
<td align="right">2,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,679</td>
<td align="right">1,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,455</td>
<td align="right">1,455</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,055</td>
<td align="right">1,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">591</td>
<td align="right">591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">447</td>
<td align="right">447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">394</td>
<td align="right">394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">255</td>
<td align="right">255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">133</td>
<td align="right">133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">102</td>
<td align="right">102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">92</td>
<td align="right">92</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">1</td>
<td align="right">1</td>
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
<td align="right">26,009,187</td>
<td align="right">64.4%</td>
<td align="right">23,665,257</td>
<td align="right">62.2%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,385,626</td>
<td align="right">35.6%</td>
<td align="right">14,385,233</td>
<td align="right">37.8%</td>
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
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">126</td>
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
<td align="right">19,189</td>
<td align="right">100.0%</td>
<td align="right">18,519</td>
<td align="right">100.0%</td>
<td align="right">-3.5%</td>
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
<td align="left">subtract other</td>
<td align="right">2,944</td>
<td align="right">15.3%</td>
<td align="right">2,430</td>
<td align="right">13.1%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,289</td>
<td align="right">6.7%</td>
<td align="right">1,158</td>
<td align="right">6.3%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,210</td>
<td align="right">6.3%</td>
<td align="right">1,136</td>
<td align="right">6.1%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">706</td>
<td align="right">3.7%</td>
<td align="right">737</td>
<td align="right">4.0%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">189</td>
<td align="right">1.0%</td>
<td align="right">190</td>
<td align="right">1.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">210</td>
<td align="right">1.1%</td>
<td align="right">209</td>
<td align="right">1.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,008</td>
<td align="right">5.3%</td>
<td align="right">1,012</td>
<td align="right">5.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,891</td>
<td align="right">15.1%</td>
<td align="right">2,898</td>
<td align="right">15.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">565</td>
<td align="right">2.9%</td>
<td align="right">566</td>
<td align="right">3.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,575</td>
<td align="right">13.4%</td>
<td align="right">2,579</td>
<td align="right">13.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">700</td>
<td align="right">3.6%</td>
<td align="right">701</td>
<td align="right">3.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">5.1%</td>
<td align="right">983</td>
<td align="right">5.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">11.6%</td>
<td align="right">2,225</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">5.7%</td>
<td align="right">1,086</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.9%</td>
<td align="right">363</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.8%</td>
<td align="right">155</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.5%</td>
<td align="right">91</td>
<td align="right">0.5%</td>
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
<td align="right">8,778</td>
<td align="right">100.0%</td>
<td align="right">8,778</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,138,208</td>
<td align="right">15.8%</td>
<td align="right">3,736,005</td>
<td align="right">10.2%</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,746</td>
<td align="right">0.0%</td>
<td align="right">10,730</td>
<td align="right">0.0%</td>
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
<td align="right">32,750,052</td>
<td align="right">84.2%</td>
<td align="right">32,753,390</td>
<td align="right">89.7%</td>
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
<td align="right">4,735</td>
<td align="right">82.8%</td>
<td align="right">4,088</td>
<td align="right">80.6%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">982</td>
<td align="right">17.2%</td>
<td align="right">982</td>
<td align="right">19.4%</td>
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
<td align="right">3,204</td>
<td align="right">67.7%</td>
<td align="right">2,551</td>
<td align="right">62.4%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">270</td>
<td align="right">5.7%</td>
<td align="right">276</td>
<td align="right">6.8%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">690</td>
<td align="right">14.6%</td>
<td align="right">690</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">8.9%</td>
<td align="right">422</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">148</td>
<td align="right">3.1%</td>
<td align="right">148</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">24,435,436</td>
<td align="right">7.6%</td>
<td align="right">23,439,955</td>
<td align="right">7.3%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">296,268,200</td>
<td align="right">92.4%</td>
<td align="right">297,585,105</td>
<td align="right">92.7%</td>
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
<td align="right">8,439</td>
<td align="right">0.0%</td>
<td align="right">8,433</td>
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
<td align="right">13,673</td>
<td align="right">0.0%</td>
<td align="right">13,673</td>
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
<td align="right">477,695</td>
<td align="right">100.0%</td>
<td align="right">458,889</td>
<td align="right">100.0%</td>
<td align="right">-3.9%</td>
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
<td align="left">init not inline values</td>
<td align="right">13</td>
<td align="right">13 / 0 !!</td>
<td align="right">13</td>
<td align="right">13 / 0 !!</td>
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
<td align="right">399</td>
<td align="right">9.4%</td>
<td align="right">399</td>
<td align="right">9.4%</td>
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
<td align="right">2,805</td>
<td align="right">66.1%</td>
<td align="right">2,805</td>
<td align="right">66.0%</td>
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
<td align="right">22,398,531</td>
<td align="right">30.3%</td>
<td align="right">16,537,566</td>
<td align="right">24.4%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">409,691</td>
<td align="right">0.6%</td>
<td align="right">377,550</td>
<td align="right">0.6%</td>
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
<td align="right">51,030,827</td>
<td align="right">69.1%</td>
<td align="right">50,900,097</td>
<td align="right">75.0%</td>
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
<td align="right">35,527</td>
<td align="right">80.1%</td>
<td align="right">33,073</td>
<td align="right">80.1%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,839</td>
<td align="right">19.9%</td>
<td align="right">8,238</td>
<td align="right">19.9%</td>
<td align="right">-6.8%</td>
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
<td align="right">5,702</td>
<td align="right">16.0%</td>
<td align="right">4,356</td>
<td align="right">13.2%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">307</td>
<td align="right">0.9%</td>
<td align="right">261</td>
<td align="right">0.8%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,095</td>
<td align="right">39.7%</td>
<td align="right">13,047</td>
<td align="right">39.4%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,155</td>
<td align="right">8.9%</td>
<td align="right">3,149</td>
<td align="right">9.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,261</td>
<td align="right">12.0%</td>
<td align="right">4,253</td>
<td align="right">12.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">21.1%</td>
<td align="right">7,480</td>
<td align="right">22.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">137</td>
<td align="right">0.4%</td>
<td align="right">137</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">117</td>
<td align="right">0.3%</td>
<td align="right">117</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">44</td>
<td align="right">0.1%</td>
<td align="right">44</td>
<td align="right">0.1%</td>
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
<td align="right">3,630,827</td>
<td align="right">13.4%</td>
<td align="right">3,183,456</td>
<td align="right">11.9%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,204</td>
<td align="right">86.6%</td>
<td align="right">23,499,003</td>
<td align="right">88.1%</td>
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
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">1,020</td>
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
<td align="right">3,573</td>
<td align="right">100.0%</td>
<td align="right">3,518</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="left">other</td>
<td align="right">1,667</td>
<td align="right">46.7%</td>
<td align="right">1,611</td>
<td align="right">45.8%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,470</td>
<td align="right">41.1%</td>
<td align="right">1,471</td>
<td align="right">41.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">8.4%</td>
<td align="right">299</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">137</td>
<td align="right">3.8%</td>
<td align="right">137</td>
<td align="right">3.9%</td>
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
<td align="right">212,756</td>
<td align="right">0.3%</td>
<td align="right">251,226</td>
<td align="right">0.4%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">33,499,736</td>
<td align="right">51.1%</td>
<td align="right">35,704,400</td>
<td align="right">53.4%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">31,849,829</td>
<td align="right">48.6%</td>
<td align="right">30,916,174</td>
<td align="right">46.2%</td>
<td align="right">-2.9%</td>
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
<td align="right">4,642</td>
<td align="right">17.7%</td>
<td align="right">5,367</td>
<td align="right">19.0%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">21,552</td>
<td align="right">82.3%</td>
<td align="right">22,903</td>
<td align="right">81.0%</td>
<td align="right">6.3%</td>
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
<td align="right">12,758</td>
<td align="right">59.2%</td>
<td align="right">13,939</td>
<td align="right">60.9%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,776</td>
<td align="right">12.9%</td>
<td align="right">2,885</td>
<td align="right">12.6%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,693</td>
<td align="right">12.5%</td>
<td align="right">2,751</td>
<td align="right">12.0%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,332</td>
<td align="right">6.2%</td>
<td align="right">1,335</td>
<td align="right">5.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">3.5%</td>
<td align="right">758</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">557</td>
<td align="right">2.6%</td>
<td align="right">557</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">1.8%</td>
<td align="right">382</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">1.1%</td>
<td align="right">243</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.1%</td>
<td align="right">24</td>
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
<td align="right">35,364,301</td>
<td align="right">11.0%</td>
<td align="right">18,042,091</td>
<td align="right">6.2%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">58,673,806</td>
<td align="right">18.3%</td>
<td align="right">32,617,342</td>
<td align="right">11.2%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">226,715,821</td>
<td align="right">70.7%</td>
<td align="right">240,336,206</td>
<td align="right">82.6%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,588</td>
<td align="right">0.0%</td>
<td align="right">18,588</td>
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
<td align="right">680,095</td>
<td align="right">93.8%</td>
<td align="right">353,294</td>
<td align="right">90.2%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">44,632</td>
<td align="right">6.2%</td>
<td align="right">38,490</td>
<td align="right">9.8%</td>
<td align="right">-13.8%</td>
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
<td align="left">builtin class method</td>
<td align="right">308</td>
<td align="right">0.7%</td>
<td align="right">568</td>
<td align="right">1.5%</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,424</td>
<td align="right">5.4%</td>
<td align="right">826</td>
<td align="right">2.1%</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,707</td>
<td align="right">15.0%</td>
<td align="right">2,685</td>
<td align="right">7.0%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,101</td>
<td align="right">6.9%</td>
<td align="right">2,786</td>
<td align="right">7.2%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">20,908</td>
<td align="right">46.8%</td>
<td align="right">20,473</td>
<td align="right">53.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,892</td>
<td align="right">6.5%</td>
<td align="right">2,860</td>
<td align="right">7.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,153</td>
<td align="right">7.1%</td>
<td align="right">3,165</td>
<td align="right">8.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">3,961</td>
<td align="right">8.9%</td>
<td align="right">3,969</td>
<td align="right">10.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">148</td>
<td align="right">0.3%</td>
<td align="right">148</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">238,572,500</td>
<td align="right">100.0%</td>
<td align="right">154,981,671</td>
<td align="right">100.0%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,532</td>
<td align="right">0.0%</td>
<td align="right">4,522</td>
<td align="right">0.0%</td>
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
<td align="right">1,294</td>
<td align="right">0.0%</td>
<td align="right">1,294</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">2,265,756</td>
<td align="right">100.0%</td>
<td align="right">2,265,761</td>
<td align="right">100.0%</td>
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
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">30</td>
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
<td align="right">30</td>
<td align="right">100.0%</td>
<td align="right">30</td>
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
<td align="right">731,584</td>
<td align="right">72.0%</td>
<td align="right">731,656</td>
<td align="right">72.0%</td>
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
<td align="right">268,986</td>
<td align="right">26.5%</td>
<td align="right">268,986</td>
<td align="right">26.5%</td>
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
<td align="right">1.4%</td>
<td align="right">14,711</td>
<td align="right">1.4%</td>
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
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
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
<td align="right">1,108</td>
<td align="right">100.0%</td>
<td align="right">1,108</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,573,954</td>
<td align="right">17.3%</td>
<td align="right">543,990</td>
<td align="right">6.2%</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,329,363</td>
<td align="right">80.7%</td>
<td align="right">8,029,471</td>
<td align="right">91.8%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,614</td>
<td align="right">1.9%</td>
<td align="right">173,621</td>
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
<td align="left">Success</td>
<td align="right">29,942</td>
<td align="right">96.9%</td>
<td align="right">10,488</td>
<td align="right">91.5%</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">970</td>
<td align="right">3.1%</td>
<td align="right">978</td>
<td align="right">8.5%</td>
<td align="right">0.8%</td>
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
<td align="right">155</td>
<td align="right">16.0%</td>
<td align="right">159</td>
<td align="right">16.3%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">294</td>
<td align="right">30.3%</td>
<td align="right">298</td>
<td align="right">30.5%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.4%</td>
<td align="right">518</td>
<td align="right">53.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3</td>
<td align="right">0.3%</td>
<td align="right">3</td>
<td align="right">0.3%</td>
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
<td align="right">591</td>
<td align="right">100.0%</td>
<td align="right">591</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">230,640</td>
<td align="right">1.3%</td>
<td align="right">188,482</td>
<td align="right">1.1%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,738,672</td>
<td align="right">98.7%</td>
<td align="right">17,737,429</td>
<td align="right">98.9%</td>
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
<td align="right">993</td>
<td align="right">63.3%</td>
<td align="right">998</td>
<td align="right">63.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">576</td>
<td align="right">36.7%</td>
<td align="right">576</td>
<td align="right">36.6%</td>
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
<td align="right">993</td>
<td align="right">100.0%</td>
<td align="right">998</td>
<td align="right">100.0%</td>
<td align="right">0.5%</td>
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
<td align="right">9,956,859</td>
<td align="right">6.1%</td>
<td align="right">2,278,974</td>
<td align="right">1.5%</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">394,189</td>
<td align="right">0.2%</td>
<td align="right">392,285</td>
<td align="right">0.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">153,416,665</td>
<td align="right">93.7%</td>
<td align="right">153,405,491</td>
<td align="right">98.3%</td>
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
<td align="right">11,602</td>
<td align="right">100.0%</td>
<td align="right">10,039</td>
<td align="right">100.0%</td>
<td align="right">-13.5%</td>
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
<td align="left">tuple</td>
<td align="right">6,108</td>
<td align="right">52.6%</td>
<td align="right">4,413</td>
<td align="right">44.0%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,824</td>
<td align="right">15.7%</td>
<td align="right">1,951</td>
<td align="right">19.4%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">714</td>
<td align="right">6.2%</td>
<td align="right">728</td>
<td align="right">7.3%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,262</td>
<td align="right">10.9%</td>
<td align="right">1,256</td>
<td align="right">12.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">725</td>
<td align="right">6.2%</td>
<td align="right">722</td>
<td align="right">7.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">7.6%</td>
<td align="right">883</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.7%</td>
<td align="right">84</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">83,627,887</td>
<td align="right">100.0%</td>
<td align="right">84,006,056</td>
<td align="right">100.0%</td>
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
<td align="right">6,249</td>
<td align="right">0.0%</td>
<td align="right">6,250</td>
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
<td align="right">299</td>
<td align="right">11.1%</td>
<td align="right">310</td>
<td align="right">11.5%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,392</td>
<td align="right">88.9%</td>
<td align="right">2,392</td>
<td align="right">88.5%</td>
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
<td align="right">256</td>
<td align="right">85.6%</td>
<td align="right">267</td>
<td align="right">86.1%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.4%</td>
<td align="right">43</td>
<td align="right">13.9%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,193,812,343</td>
<td align="right">34.4%</td>
<td align="right">790,402,218</td>
<td align="right">29.7%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">62,421,631</td>
<td align="right">1.8%</td>
<td align="right">43,079,753</td>
<td align="right">1.6%</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">161,214,076</td>
<td align="right">4.6%</td>
<td align="right">118,577,595</td>
<td align="right">4.5%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,054,132,506</td>
<td align="right">59.2%</td>
<td align="right">1,708,014,760</td>
<td align="right">64.2%</td>
<td align="right">-16.8%</td>
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
<td align="right">9,956,859</td>
<td align="right">6.2%</td>
<td align="right">2,278,974</td>
<td align="right">1.9%</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">58,673,806</td>
<td align="right">36.4%</td>
<td align="right">32,617,342</td>
<td align="right">27.6%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">6,138,208</td>
<td align="right">3.8%</td>
<td align="right">3,736,005</td>
<td align="right">3.2%</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">22,398,531</td>
<td align="right">13.9%</td>
<td align="right">16,537,566</td>
<td align="right">14.0%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">230,640</td>
<td align="right">0.1%</td>
<td align="right">188,482</td>
<td align="right">0.2%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,630,827</td>
<td align="right">2.3%</td>
<td align="right">3,183,456</td>
<td align="right">2.7%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">26,009,187</td>
<td align="right">16.2%</td>
<td align="right">23,665,257</td>
<td align="right">20.0%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,499,736</td>
<td align="right">20.8%</td>
<td align="right">35,704,400</td>
<td align="right">30.2%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">173,614</td>
<td align="right">0.1%</td>
<td align="right">173,621</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.2%</td>
<td align="right">268,986</td>
<td align="right">0.2%</td>
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
<td align="right">15,048,605</td>
<td align="right">24.1%</td>
<td align="right">3,462,362</td>
<td align="right">8.0%</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,573,175</td>
<td align="right">2.5%</td>
<td align="right">543,211</td>
<td align="right">1.3%</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,159,100</td>
<td align="right">5.1%</td>
<td align="right">1,903,307</td>
<td align="right">4.4%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,757,292</td>
<td align="right">17.2%</td>
<td align="right">7,373,416</td>
<td align="right">17.1%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,830,295</td>
<td align="right">9.3%</td>
<td align="right">4,539,091</td>
<td align="right">10.5%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,008,879</td>
<td align="right">9.6%</td>
<td align="right">4,913,878</td>
<td align="right">11.4%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">408,671</td>
<td align="right">0.7%</td>
<td align="right">376,530</td>
<td align="right">0.9%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,291,604</td>
<td align="right">18.1%</td>
<td align="right">11,643,487</td>
<td align="right">27.0%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,517</td>
<td align="right">8.2%</td>
<td align="right">5,102,661</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,562</td>
<td align="right">3.4%</td>
<td align="right">2,103,558</td>
<td align="right">4.9%</td>
<td align="right">-0.0%</td>
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
<td align="right">41,317,854</td>
<td align="right">19.6%</td>
<td align="right">40,088,218</td>
<td align="right">19.0%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,613,163</td>
<td align="right">35.9%</td>
<td align="right">74,383,749</td>
<td align="right">35.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,613,948</td>
<td align="right">35.9%</td>
<td align="right">74,384,534</td>
<td align="right">35.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,365,186</td>
<td align="right">10.6%</td>
<td align="right">22,710,731</td>
<td align="right">10.8%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,506,328</td>
<td align="right">53.5%</td>
<td align="right">113,779,422</td>
<td align="right">54.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">97,979,134</td>
<td align="right">46.5%</td>
<td align="right">97,095,265</td>
<td align="right">46.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">97,979,134</td>
<td align="right">46.5%</td>
<td align="right">97,095,265</td>
<td align="right">46.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,875,330</td>
<td align="right">89.3%</td>
<td align="right">187,919,046</td>
<td align="right">89.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,135</td>
<td align="right">0.5%</td>
<td align="right">950,325</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,631</td>
<td align="right">8.8%</td>
<td align="right">18,490,900</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,331,920</td>
<td align="right">4.4%</td>
<td align="right">9,331,922</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">348</td>
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
<td align="right">1,774,120,931</td>
<td align="right">35.7%</td>
<td align="right">2,307,129,411</td>
<td align="right">44.6%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,857,642,751</td>
<td align="right">32.1%</td>
<td align="right">2,232,200,552</td>
<td align="right">36.7%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,576,194,697</td>
<td align="right">31.8%</td>
<td align="right">1,268,496,453</td>
<td align="right">24.5%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">426,875,896</td>
<td align="right">8.6%</td>
<td align="right">348,762,059</td>
<td align="right">6.7%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">687,008,565</td>
<td align="right">11.9%</td>
<td align="right">574,021,318</td>
<td align="right">9.4%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,293,137,037</td>
<td align="right">22.4%</td>
<td align="right">1,470,244,078</td>
<td align="right">24.2%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">143,908,886</td>
<td align="right"></td>
<td align="right">131,977,541</td>
<td align="right"></td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,947,156,680</td>
<td align="right">33.7%</td>
<td align="right">1,797,960,773</td>
<td align="right">29.6%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,187,048,138</td>
<td align="right">23.9%</td>
<td align="right">1,243,285,994</td>
<td align="right">24.1%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,151,806</td>
<td align="right"></td>
<td align="right">1,188,581</td>
<td align="right"></td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,835</td>
<td align="right">0.0%</td>
<td align="right">9,007</td>
<td align="right">0.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">773,332</td>
<td align="right">0.2%</td>
<td align="right">787,764</td>
<td align="right">0.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">263,520,575</td>
<td align="right"></td>
<td align="right">261,196,910</td>
<td align="right"></td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,761,463</td>
<td align="right"></td>
<td align="right">3,789,332</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,611,068</td>
<td align="right"></td>
<td align="right">2,602,376</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">232,915,141</td>
<td align="right">45.3%</td>
<td align="right">232,956,239</td>
<td align="right">45.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">245,562,785</td>
<td align="right"></td>
<td align="right">245,602,498</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">232,132,974</td>
<td align="right">45.1%</td>
<td align="right">232,159,468</td>
<td align="right">45.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,131</td>
<td align="right"></td>
<td align="right">866,203</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">281,716,482</td>
<td align="right">54.7%</td>
<td align="right">281,732,920</td>
<td align="right">54.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">281,747,874</td>
<td align="right"></td>
<td align="right">281,764,313</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">38,586</td>
<td align="right">61.8%</td>
<td align="right">87,715</td>
<td align="right">71.4%</td>
<td align="right">127.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">41,309</td>
<td align="right">66.1%</td>
<td align="right">86,054</td>
<td align="right">70.1%</td>
<td align="right">108.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">62,458</td>
<td align="right"></td>
<td align="right">122,835</td>
<td align="right"></td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">178,138,414</td>
<td align="right"></td>
<td align="right">337,372,326</td>
<td align="right"></td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">21,149</td>
<td align="right">33.9%</td>
<td align="right">36,781</td>
<td align="right">29.9%</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">3,109,675,878</td>
<td align="right">1,745.7%</td>
<td align="right">5,120,264,430</td>
<td align="right">1,517.7%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">688</td>
<td align="right">1.1%</td>
<td align="right">961</td>
<td align="right">0.8%</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">669</td>
<td align="right">1.1%</td>
<td align="right">499</td>
<td align="right">0.4%</td>
<td align="right">-25.4%</td>
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
<td align="right">100</td>
<td align="right">0.3%</td>
<td align="right">100 / 0 !!</td>
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
<td align="right">20,285</td>
<td align="right">95.9%</td>
<td align="right">35,784</td>
<td align="right">97.3%</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">21,149</td>
<td align="right"></td>
<td align="right">36,781</td>
<td align="right"></td>
<td align="right">73.9%</td>
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
<td align="right">276</td>
<td align="right">0.8%</td>
<td align="right">276 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">3,100</td>
<td align="right">14.7%</td>
<td align="right">4,489</td>
<td align="right">12.2%</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">3,423</td>
<td align="right">16.2%</td>
<td align="right">7,290</td>
<td align="right">19.8%</td>
<td align="right">113.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">6,834</td>
<td align="right">32.3%</td>
<td align="right">11,845</td>
<td align="right">32.2%</td>
<td align="right">73.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">4,702</td>
<td align="right">22.2%</td>
<td align="right">8,750</td>
<td align="right">23.8%</td>
<td align="right">86.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,696</td>
<td align="right">12.7%</td>
<td align="right">3,371</td>
<td align="right">9.2%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">394</td>
<td align="right">1.9%</td>
<td align="right">760</td>
<td align="right">2.1%</td>
<td align="right">92.9%</td>
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
<td align="right">612</td>
<td align="right">2.9%</td>
<td align="right">1,370</td>
<td align="right">3.7%</td>
<td align="right">123.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">3,380</td>
<td align="right">16.0%</td>
<td align="right">4,810</td>
<td align="right">13.1%</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">4,399</td>
<td align="right">20.8%</td>
<td align="right">10,184</td>
<td align="right">27.7%</td>
<td align="right">131.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,433</td>
<td align="right">35.1%</td>
<td align="right">12,050</td>
<td align="right">32.8%</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">3,922</td>
<td align="right">18.5%</td>
<td align="right">6,458</td>
<td align="right">17.6%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">445</td>
<td align="right">2.1%</td>
<td align="right">716</td>
<td align="right">1.9%</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">94</td>
<td align="right">0.4%</td>
<td align="right">196</td>
<td align="right">0.5%</td>
<td align="right">108.5%</td>
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
<td align="right">80</td>
<td align="right">577,637</td>
<td align="right">721,946.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">331</td>
<td align="right">311,097</td>
<td align="right">93,887.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">24,402</td>
<td align="right">6,619,448</td>
<td align="right">27,026.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">24,402</td>
<td align="right">6,619,448</td>
<td align="right">27,026.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">744</td>
<td align="right">64,458</td>
<td align="right">8,563.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">131,799</td>
<td align="right">7,810,434</td>
<td align="right">5,826.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,771,912</td>
<td align="right">143,516,005</td>
<td align="right">5,077.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">791</td>
<td align="right">40,496</td>
<td align="right">5,019.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">33,737</td>
<td align="right">1,058,680</td>
<td align="right">3,038.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">416,217</td>
<td align="right">9,035,126</td>
<td align="right">2,070.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">420,858</td>
<td align="right">9,102,935</td>
<td align="right">2,062.9%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">113,820</td>
<td align="right">2,186,175</td>
<td align="right">1,820.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">4,641</td>
<td align="right">67,809</td>
<td align="right">1,361.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">494,069</td>
<td align="right">3,881,257</td>
<td align="right">685.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">40,482</td>
<td align="right">278,995</td>
<td align="right">589.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">40,482</td>
<td align="right">278,995</td>
<td align="right">589.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">40,482</td>
<td align="right">278,995</td>
<td align="right">589.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">259,396</td>
<td align="right">1,726,958</td>
<td align="right">565.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,936,240</td>
<td align="right">12,828,016</td>
<td align="right">562.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">23,962</td>
<td align="right">153,549</td>
<td align="right">540.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">4,585,318</td>
<td align="right">27,700,380</td>
<td align="right">504.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,166</td>
<td align="right">28,791</td>
<td align="right">457.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">19,083,096</td>
<td align="right">87,537,236</td>
<td align="right">358.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">2,328,863</td>
<td align="right">9,065,791</td>
<td align="right">289.3%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">587,136</td>
<td align="right">2,251,773</td>
<td align="right">283.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">21,218,733</td>
<td align="right">80,785,497</td>
<td align="right">280.7%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">587,136</td>
<td align="right">2,037,952</td>
<td align="right">247.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">4,108,586</td>
<td align="right">13,888,052</td>
<td align="right">238.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">4,304,237</td>
<td align="right">14,085,981</td>
<td align="right">227.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">128,502</td>
<td align="right">413,310</td>
<td align="right">221.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,394,015</td>
<td align="right">4,089,102</td>
<td align="right">193.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,394,015</td>
<td align="right">4,025,718</td>
<td align="right">188.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">71,786,033</td>
<td align="right">200,161,378</td>
<td align="right">178.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">587,150</td>
<td align="right">1,555,967</td>
<td align="right">165.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">7,434,378</td>
<td align="right">19,541,264</td>
<td align="right">162.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">18,487,995</td>
<td align="right">47,216,750</td>
<td align="right">155.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,540,395</td>
<td align="right">3,906,557</td>
<td align="right">153.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">3,312,075</td>
<td align="right">8,316,884</td>
<td align="right">151.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">192,811</td>
<td align="right">483,947</td>
<td align="right">151.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">24,937,138</td>
<td align="right">61,585,831</td>
<td align="right">147.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">8,521,248</td>
<td align="right">20,554,107</td>
<td align="right">141.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">22,105,624</td>
<td align="right">51,913,257</td>
<td align="right">134.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">383,729</td>
<td align="right">889,812</td>
<td align="right">131.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">8,251,671</td>
<td align="right">18,699,673</td>
<td align="right">126.6%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,127,644</td>
<td align="right">13,856,088</td>
<td align="right">126.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">41,799,871</td>
<td align="right">93,704,787</td>
<td align="right">124.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,901,827</td>
<td align="right">4,246,039</td>
<td align="right">123.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">22,807</td>
<td align="right">49,710</td>
<td align="right">118.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">24,759,479</td>
<td align="right">53,736,358</td>
<td align="right">117.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">22,870,751</td>
<td align="right">49,598,177</td>
<td align="right">116.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">24,759,479</td>
<td align="right">53,523,964</td>
<td align="right">116.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">9,515,149</td>
<td align="right">20,558,457</td>
<td align="right">116.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">6,987,930</td>
<td align="right">14,965,522</td>
<td align="right">114.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">211,940</td>
<td align="right">440,099</td>
<td align="right">107.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,865,475</td>
<td align="right">3,872,221</td>
<td align="right">107.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,875,505</td>
<td align="right">3,875,594</td>
<td align="right">106.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,818,343</td>
<td align="right">14,072,127</td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,818,343</td>
<td align="right">14,072,127</td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">27,225,049</td>
<td align="right">56,161,445</td>
<td align="right">106.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">8,155,980</td>
<td align="right">16,704,056</td>
<td align="right">104.8%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">3,131,535</td>
<td align="right">6,394,723</td>
<td align="right">104.2%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">691,635</td>
<td align="right">1,375,386</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,465,707</td>
<td align="right">2,898,191</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">15,604,072</td>
<td align="right">30,596,351</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">9,764,489</td>
<td align="right">19,104,521</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">74,439,473</td>
<td align="right">145,171,257</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">98,654,239</td>
<td align="right">186,841,268</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">178,138,414</td>
<td align="right">337,372,326</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">6,128,440</td>
<td align="right">850,432</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">13,751,142</td>
<td align="right">25,492,463</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">13,111,167</td>
<td align="right">24,102,968</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">9,337,639</td>
<td align="right">17,090,613</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">159,521,126</td>
<td align="right">289,701,770</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">14,631,700</td>
<td align="right">26,417,903</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,028,423</td>
<td align="right">212,768</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,028,423</td>
<td align="right">212,768</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">8,000,712</td>
<td align="right">14,060,028</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">220,986,564</td>
<td align="right">375,999,407</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">34,459,932</td>
<td align="right">57,194,446</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">700,853</td>
<td align="right">1,111,887</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,670,728</td>
<td align="right">704,089</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">21,383,439</td>
<td align="right">33,283,846</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">7,107,753</td>
<td align="right">10,778,553</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">22,668,263</td>
<td align="right">34,344,227</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">530,814</td>
<td align="right">804,136</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">302,987,616</td>
<td align="right">450,972,119</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">21,807,542</td>
<td align="right">32,402,431</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">243,036,109</td>
<td align="right">354,150,805</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">7,405,695</td>
<td align="right">10,528,239</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">54,626,816</td>
<td align="right">76,192,628</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">35,760,199</td>
<td align="right">49,767,147</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">64,728,400</td>
<td align="right">89,542,705</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">10,119,056</td>
<td align="right">13,866,356</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">10,119,056</td>
<td align="right">13,866,356</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">325,023</td>
<td align="right">204,786</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,095,094</td>
<td align="right">13,712,807</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">24,519,356</td>
<td align="right">32,846,837</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">31,384,077</td>
<td align="right">41,897,475</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">15,834</td>
<td align="right">20,231</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">41,398,332</td>
<td align="right">52,512,039</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">10,408,075</td>
<td align="right">12,867,981</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">14,597,943</td>
<td align="right">17,856,970</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">544,169</td>
<td align="right">663,691</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">134,437,724</td>
<td align="right">163,440,275</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">2,832,425</td>
<td align="right">3,441,850</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">293,568</td>
<td align="right">355,395</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">12,253,230</td>
<td align="right">14,791,283</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">12,380,973</td>
<td align="right">14,865,447</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">42,415,637</td>
<td align="right">50,762,190</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,293,947</td>
<td align="right">9,621,205</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,664,159</td>
<td align="right">18,061,453</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">16,422,436</td>
<td align="right">18,879,163</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">71,564,221</td>
<td align="right">81,914,746</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">6,515,976</td>
<td align="right">7,456,247</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,409,301</td>
<td align="right">1,218,018</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,684,304</td>
<td align="right">11,972,211</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,746,547</td>
<td align="right">7,548,351</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">327,309</td>
<td align="right">293,240</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">42,848,150</td>
<td align="right">38,627,081</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">13,494,781</td>
<td align="right">14,767,348</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">14,171,181</td>
<td align="right">15,443,534</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">5,099,005</td>
<td align="right">5,543,809</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">14,928,384</td>
<td align="right">16,159,677</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,558,831</td>
<td align="right">1,676,487</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">12,916,613</td>
<td align="right">13,824,509</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">183,858</td>
<td align="right">172,307</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">183,858</td>
<td align="right">172,307</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">10,202,693</td>
<td align="right">10,666,194</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">31,832,792</td>
<td align="right">30,432,352</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">6,584,157</td>
<td align="right">6,863,433</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,760,208</td>
<td align="right">2,875,948</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">7,017,805</td>
<td align="right">7,311,047</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">7,017,805</td>
<td align="right">7,311,047</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">47,619</td>
<td align="right">45,678</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">6,271,404</td>
<td align="right">6,514,581</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">32,715,170</td>
<td align="right">31,534,825</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">49,164,961</td>
<td align="right">47,393,811</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40,572,561</td>
<td align="right">39,131,154</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">19,816,481</td>
<td align="right">19,112,813</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">13,728,041</td>
<td align="right">14,212,860</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">5,726,666</td>
<td align="right">5,546,469</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">32,147,346</td>
<td align="right">31,379,432</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">31,147,547</td>
<td align="right">30,425,240</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">12,916,283</td>
<td align="right">12,630,838</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">22,397,162</td>
<td align="right">22,871,523</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">25,924,234</td>
<td align="right">25,395,060</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">18,409,577</td>
<td align="right">18,777,062</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">2,352,337</td>
<td align="right">2,394,471</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">6,116,871</td>
<td align="right">6,019,544</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">6,231,002</td>
<td align="right">6,159,511</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,513,544</td>
<td align="right">2,513,448</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">40,393,371</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">280,003</td>
<td align="right">280,003</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">152,677</td>
<td align="right">152,677</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">33,854</td>
<td align="right">33,854</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">666</td>
<td align="right">666</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right"></td>
<td align="right">2,724,713</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right"></td>
<td align="right">2,724,713</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">2,514,474</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">2,274,673</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right"></td>
<td align="right">1,193,380</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">568,127</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">568,127</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">415,864</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">415,864</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">415,864</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">212,394</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">212,394</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">90,336</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right"></td>
<td align="right">70,566</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right"></td>
<td align="right">59,337</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right"></td>
<td align="right">59,337</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">44,900</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right"></td>
<td align="right">33,074</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">29,550</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">27,405</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">18,165</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right"></td>
<td align="right">1,195</td>
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
<td align="right">5,773</td>
<td align="right">9,397</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,226</td>
<td align="right">5,143</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">142</td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-23
