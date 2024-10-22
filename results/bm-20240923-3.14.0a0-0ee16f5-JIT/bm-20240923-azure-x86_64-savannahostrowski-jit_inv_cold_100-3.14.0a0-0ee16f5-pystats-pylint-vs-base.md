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
<td align="right">296,789</td>
<td align="right">41,062,556</td>
<td align="right">13,735.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,972,804</td>
<td align="right">20,971,441</td>
<td align="right">963.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,019,384</td>
<td align="right">21,174,685</td>
<td align="right">948.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">5,591,429</td>
<td align="right">36,679,247</td>
<td align="right">556.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">71,000</td>
<td align="right">447,020</td>
<td align="right">529.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,070,300</td>
<td align="right">29,795,140</td>
<td align="right">487.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">3,941,660</td>
<td align="right">20,866,629</td>
<td align="right">429.4%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">45,420</td>
<td align="right">224,846</td>
<td align="right">395.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">104,820</td>
<td align="right">499,028</td>
<td align="right">376.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,117,240</td>
<td align="right">4,704,186</td>
<td align="right">321.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,126,000</td>
<td align="right">11,804,483</td>
<td align="right">277.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">9,004,863</td>
<td align="right">32,553,891</td>
<td align="right">261.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">536,840</td>
<td align="right">1,421,765</td>
<td align="right">164.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,100,840</td>
<td align="right">5,344,751</td>
<td align="right">154.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">344,180</td>
<td align="right">864,388</td>
<td align="right">151.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,212,860</td>
<td align="right">8,019,742</td>
<td align="right">149.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,438,180</td>
<td align="right">3,419,852</td>
<td align="right">137.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">47,413</td>
<td align="right">108,908</td>
<td align="right">129.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,943,920</td>
<td align="right">13,631,086</td>
<td align="right">129.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,976,240</td>
<td align="right">4,438,270</td>
<td align="right">124.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,154,780</td>
<td align="right">14,683,929</td>
<td align="right">105.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">76,620</td>
<td align="right">153,586</td>
<td align="right">100.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">171,460</td>
<td align="right">342,924</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">24,659,437</td>
<td align="right">49,094,493</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,837,780</td>
<td align="right">9,252,436</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">7,067,480</td>
<td align="right">13,179,421</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,733,920</td>
<td align="right">3,043,105</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,949,761</td>
<td align="right">4,986,786</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">50,050,259</td>
<td align="right">16,390,932</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,442,360</td>
<td align="right">2,394,168</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">742,960</td>
<td align="right">1,223,965</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,617,060</td>
<td align="right">4,284,253</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">429,540</td>
<td align="right">696,910</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">44,427,543</td>
<td align="right">71,100,963</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">425,700</td>
<td align="right">673,079</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">18,461,980</td>
<td align="right">29,162,064</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">299,854,179</td>
<td align="right">470,387,020</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">60,566,021</td>
<td align="right">93,107,416</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">4,076,560</td>
<td align="right">6,257,738</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,008,493</td>
<td align="right">4,605,618</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,656,200</td>
<td align="right">3,971,721</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">58,660,471</td>
<td align="right">87,424,040</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,739,359</td>
<td align="right">5,524,873</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">11,226,600</td>
<td align="right">16,583,411</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">33,322,573</td>
<td align="right">48,846,015</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">363,040</td>
<td align="right">531,264</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,466,700</td>
<td align="right">9,443,269</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">57,020</td>
<td align="right">82,855</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">26,621,700</td>
<td align="right">38,681,736</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">3,375,805</td>
<td align="right">4,890,298</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,752,494</td>
<td align="right">2,537,458</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,428,920</td>
<td align="right">3,516,109</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">891,320</td>
<td align="right">499,256</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">16,968,320</td>
<td align="right">24,411,734</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,880</td>
<td align="right">16,844</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,499,240</td>
<td align="right">7,745,192</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">23,540</td>
<td align="right">33,060</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">89,063,134</td>
<td align="right">124,806,623</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">123,060</td>
<td align="right">171,064</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,632,924</td>
<td align="right">2,251,547</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,680,521</td>
<td align="right">3,675,279</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,447,575</td>
<td align="right">3,344,271</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,100,444</td>
<td align="right">16,442,913</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">369,880</td>
<td align="right">497,220</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">78,597,624</td>
<td align="right">104,841,349</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">64,863,413</td>
<td align="right">85,470,449</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">5,092,161</td>
<td align="right">6,514,311</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">14,731,179</td>
<td align="right">18,670,484</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2,785,580</td>
<td align="right">3,526,939</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">43,864,562</td>
<td align="right">55,419,042</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,562,880</td>
<td align="right">1,170,036</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">8,872,840</td>
<td align="right">11,035,060</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">25,453,720</td>
<td align="right">31,203,984</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,859,400</td>
<td align="right">3,487,975</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">52,017,828</td>
<td align="right">62,996,603</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">6,764,440</td>
<td align="right">8,159,911</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">573,220</td>
<td align="right">688,413</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,931,141</td>
<td align="right">5,884,936</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">5,472,560</td>
<td align="right">6,507,531</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60,404,584</td>
<td align="right">71,007,477</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,096,049</td>
<td align="right">4,810,581</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,500</td>
<td align="right">5,280</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">5,909,540</td>
<td align="right">6,832,858</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,581,550</td>
<td align="right">1,827,700</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">58,961,885</td>
<td align="right">68,013,328</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,523,122</td>
<td align="right">2,869,246</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">75,656,464</td>
<td align="right">85,267,798</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,762,031</td>
<td align="right">9,845,962</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,386,920</td>
<td align="right">3,779,802</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">25,250,540</td>
<td align="right">28,093,817</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">479,160</td>
<td align="right">429,184</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,148,280</td>
<td align="right">2,366,700</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">6,488,400</td>
<td align="right">7,115,825</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">32,878,730</td>
<td align="right">35,999,708</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,753,000</td>
<td align="right">1,915,774</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,393,300</td>
<td align="right">1,515,415</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,574,460</td>
<td align="right">2,779,000</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">123,020</td>
<td align="right">132,095</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">32,724,860</td>
<td align="right">35,079,106</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">9,280</td>
<td align="right">9,935</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">5,257,989</td>
<td align="right">5,599,014</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">10,297,280</td>
<td align="right">10,816,761</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">3,310,300</td>
<td align="right">3,461,442</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">85,910</td>
<td align="right">89,620</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,803,080</td>
<td align="right">1,880,006</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">101,340</td>
<td align="right">105,420</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,016,201</td>
<td align="right">1,055,948</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,768,180</td>
<td align="right">2,867,475</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">544,580</td>
<td align="right">563,380</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">545,540</td>
<td align="right">564,340</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">5,629,980</td>
<td align="right">5,822,412</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">29,417,761</td>
<td align="right">30,395,422</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">931,260</td>
<td align="right">953,259</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,209,740</td>
<td align="right">3,285,374</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">26,777,060</td>
<td align="right">27,366,569</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">7,599,640</td>
<td align="right">7,763,142</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,656,840</td>
<td align="right">1,688,408</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">564,660</td>
<td align="right">575,376</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">5,055,160</td>
<td align="right">5,145,466</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">73,986,936</td>
<td align="right">75,249,377</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">759,780</td>
<td align="right">772,445</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">3,201,380</td>
<td align="right">3,250,376</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,052,109</td>
<td align="right">1,063,064</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,050,200</td>
<td align="right">1,059,887</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">750,120</td>
<td align="right">756,816</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">15,691,220</td>
<td align="right">15,793,972</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">39,403,831</td>
<td align="right">39,647,420</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,405,740</td>
<td align="right">1,413,940</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">23,260</td>
<td align="right">23,370</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">13,500</td>
<td align="right">13,540</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">341,940</td>
<td align="right">342,840</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">6,368,120</td>
<td align="right">6,366,029</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">675,940</td>
<td align="right">676,052</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">37,509,193</td>
<td align="right">37,513,309</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,055,460</td>
<td align="right">1,055,490</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">16,821,380</td>
<td align="right">16,821,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">10,680,080</td>
<td align="right">10,680,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">8,588,980</td>
<td align="right">8,588,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,543,340</td>
<td align="right">3,543,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,947,160</td>
<td align="right">1,947,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,590,040</td>
<td align="right">1,590,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,413,940</td>
<td align="right">1,413,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">608,540</td>
<td align="right">608,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">475,480</td>
<td align="right">475,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">270,640</td>
<td align="right">270,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">265,920</td>
<td align="right">265,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">241,280</td>
<td align="right">241,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">199,520</td>
<td align="right">199,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">195,560</td>
<td align="right">195,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">179,300</td>
<td align="right">179,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">157,060</td>
<td align="right">157,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">108,240</td>
<td align="right">108,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">91,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,340</td>
<td align="right">91,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">73,400</td>
<td align="right">73,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">66,720</td>
<td align="right">66,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">60,520</td>
<td align="right">60,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">36,060</td>
<td align="right">36,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">25,800</td>
<td align="right">25,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20,540</td>
<td align="right">20,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">13,540</td>
<td align="right">13,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">10,720</td>
<td align="right">10,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">10,200</td>
<td align="right">10,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,980</td>
<td align="right">6,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">4,720</td>
<td align="right">4,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">4,580</td>
<td align="right">4,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">4,220</td>
<td align="right">4,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,440</td>
<td align="right">3,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,100</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">940</td>
<td align="right">940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">100</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
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
<td align="right">918,880</td>
<td align="right">9.8%</td>
<td align="right">940,679</td>
<td align="right">10.0%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,460,220</td>
<td align="right">90.1%</td>
<td align="right">8,460,220</td>
<td align="right">89.9%</td>
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
<td align="right">9,140</td>
<td align="right">73.8%</td>
<td align="right">9,340</td>
<td align="right">74.2%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,240</td>
<td align="right">26.2%</td>
<td align="right">3,240</td>
<td align="right">25.8%</td>
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
<td align="left">floor divide</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">80</td>
<td align="right">0.9%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,440</td>
<td align="right">15.8%</td>
<td align="right">1,560</td>
<td align="right">16.7%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">540</td>
<td align="right">5.9%</td>
<td align="right">580</td>
<td align="right">6.2%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">660</td>
<td align="right">7.2%</td>
<td align="right">620</td>
<td align="right">6.6%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,380</td>
<td align="right">37.0%</td>
<td align="right">3,420</td>
<td align="right">36.6%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">900</td>
<td align="right">9.8%</td>
<td align="right">900</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">720</td>
<td align="right">7.9%</td>
<td align="right">720</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">400</td>
<td align="right">4.4%</td>
<td align="right">400</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">340</td>
<td align="right">3.7%</td>
<td align="right">340</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">260</td>
<td align="right">2.8%</td>
<td align="right">260</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">200</td>
<td align="right">2.2%</td>
<td align="right">200</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">120</td>
<td align="right">1.3%</td>
<td align="right">120</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">60</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">742,960</td>
<td align="right">100.0%</td>
<td align="right">1,223,965</td>
<td align="right">100.0%</td>
<td align="right">64.7%</td>
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
<td align="right">1,420,400</td>
<td align="right">6.6%</td>
<td align="right">3,401,532</td>
<td align="right">15.4%</td>
<td align="right">139.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">20,110,206</td>
<td align="right">93.1%</td>
<td align="right">18,614,166</td>
<td align="right">84.3%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">44,840</td>
<td align="right">0.2%</td>
<td align="right">44,840</td>
<td align="right">0.2%</td>
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
<td align="right">8,820</td>
<td align="right">47.6%</td>
<td align="right">9,360</td>
<td align="right">49.1%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,720</td>
<td align="right">52.4%</td>
<td align="right">9,720</td>
<td align="right">50.9%</td>
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
<td align="left">list slice</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">180</td>
<td align="right">1.9%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,660</td>
<td align="right">30.2%</td>
<td align="right">3,180</td>
<td align="right">34.0%</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">1,880</td>
<td align="right">21.3%</td>
<td align="right">1,940</td>
<td align="right">20.7%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,740</td>
<td align="right">42.4%</td>
<td align="right">3,660</td>
<td align="right">39.1%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">260</td>
<td align="right">2.9%</td>
<td align="right">260</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">11,904,360</td>
<td align="right">7.9%</td>
<td align="right">16,937,471</td>
<td align="right">11.1%</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">139,283,574</td>
<td align="right">92.0%</td>
<td align="right">135,197,665</td>
<td align="right">88.7%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">140,120</td>
<td align="right">0.1%</td>
<td align="right">140,120</td>
<td align="right">0.1%</td>
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
<td align="right">10,260</td>
<td align="right">0.0%</td>
<td align="right">10,260</td>
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
<td align="right">341,640</td>
<td align="right">100.0%</td>
<td align="right">443,503</td>
<td align="right">100.0%</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">480</td>
<td align="right">2,400.0%</td>
<td align="right">480</td>
<td align="right">2,400.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">300</td>
<td align="right">1,500.0%</td>
<td align="right">300</td>
<td align="right">1,500.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
<td align="right">100.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">431,660</td>
<td align="right">95.5%</td>
<td align="right">799,220</td>
<td align="right">97.5%</td>
<td align="right">85.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">10,780</td>
<td align="right">2.4%</td>
<td align="right">10,780</td>
<td align="right">1.3%</td>
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
<td align="right">6,280</td>
<td align="right">0.0%</td>
<td align="right">12,660</td>
<td align="right">0.0%</td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,236,269</td>
<td align="right">10.6%</td>
<td align="right">5,576,430</td>
<td align="right">11.2%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">44,193,484</td>
<td align="right">89.4%</td>
<td align="right">44,190,087</td>
<td align="right">88.7%</td>
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
<td align="right">10,300</td>
<td align="right">47.2%</td>
<td align="right">11,145</td>
<td align="right">48.8%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,540</td>
<td align="right">52.8%</td>
<td align="right">11,683</td>
<td align="right">51.2%</td>
<td align="right">1.2%</td>
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
<td align="right">3,020</td>
<td align="right">29.3%</td>
<td align="right">3,665</td>
<td align="right">32.9%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">4,160</td>
<td align="right">40.4%</td>
<td align="right">4,360</td>
<td align="right">39.1%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">980</td>
<td align="right">9.5%</td>
<td align="right">980</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">860</td>
<td align="right">8.3%</td>
<td align="right">860</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">340</td>
<td align="right">3.3%</td>
<td align="right">340</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">340</td>
<td align="right">3.3%</td>
<td align="right">340</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">220</td>
<td align="right">2.1%</td>
<td align="right">220</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">200</td>
<td align="right">1.9%</td>
<td align="right">200</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">160</td>
<td align="right">1.6%</td>
<td align="right">160</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
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
<td align="right">2,425,835</td>
<td align="right">21.1%</td>
<td align="right">3,321,827</td>
<td align="right">26.8%</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">31,300</td>
<td align="right">0.3%</td>
<td align="right">32,604</td>
<td align="right">0.3%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,002,320</td>
<td align="right">78.4%</td>
<td align="right">9,001,265</td>
<td align="right">72.7%</td>
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
<td align="right">17,540</td>
<td align="right">78.6%</td>
<td align="right">18,244</td>
<td align="right">79.1%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,780</td>
<td align="right">21.4%</td>
<td align="right">4,806</td>
<td align="right">20.9%</td>
<td align="right">0.5%</td>
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
<td align="right">3,360</td>
<td align="right">19.2%</td>
<td align="right">3,700</td>
<td align="right">20.3%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">3,740</td>
<td align="right">21.3%</td>
<td align="right">3,930</td>
<td align="right">21.5%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,180</td>
<td align="right">46.6%</td>
<td align="right">8,354</td>
<td align="right">45.8%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,260</td>
<td align="right">12.9%</td>
<td align="right">2,260</td>
<td align="right">12.4%</td>
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
<td align="right">101,540</td>
<td align="right">0.4%</td>
<td align="right">282,821</td>
<td align="right">0.5%</td>
<td align="right">178.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,389,849</td>
<td align="right">90.2%</td>
<td align="right">57,727,141</td>
<td align="right">93.8%</td>
<td align="right">146.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,400,800</td>
<td align="right">9.3%</td>
<td align="right">3,483,326</td>
<td align="right">5.7%</td>
<td align="right">45.1%</td>
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
<td align="right">15,020</td>
<td align="right">50.1%</td>
<td align="right">19,686</td>
<td align="right">51.7%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">14,940</td>
<td align="right">49.9%</td>
<td align="right">18,370</td>
<td align="right">48.3%</td>
<td align="right">23.0%</td>
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
<td align="left">seq iter</td>
<td align="right">60</td>
<td align="right">0.4%</td>
<td align="right">320</td>
<td align="right">1.6%</td>
<td align="right">433.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,680</td>
<td align="right">17.8%</td>
<td align="right">6,566</td>
<td align="right">33.4%</td>
<td align="right">145.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">400</td>
<td align="right">2.7%</td>
<td align="right">520</td>
<td align="right">2.6%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,040</td>
<td align="right">20.2%</td>
<td align="right">3,300</td>
<td align="right">16.8%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">1,000</td>
<td align="right">6.7%</td>
<td align="right">1,060</td>
<td align="right">5.4%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">680</td>
<td align="right">4.5%</td>
<td align="right">700</td>
<td align="right">3.6%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">4,000</td>
<td align="right">26.6%</td>
<td align="right">4,060</td>
<td align="right">20.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,700</td>
<td align="right">11.3%</td>
<td align="right">1,700</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">620</td>
<td align="right">4.1%</td>
<td align="right">620</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">460</td>
<td align="right">3.1%</td>
<td align="right">460</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">140</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">140</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">100</td>
<td align="right">0.7%</td>
<td align="right">100</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">30,678,170</td>
<td align="right">12.5%</td>
<td align="right">61,299,270</td>
<td align="right">21.7%</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">25,086,260</td>
<td align="right">10.2%</td>
<td align="right">30,792,820</td>
<td align="right">10.9%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">190,187,652</td>
<td align="right">77.2%</td>
<td align="right">189,827,653</td>
<td align="right">67.2%</td>
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
<td align="right">427,360</td>
<td align="right">0.2%</td>
<td align="right">427,360</td>
<td align="right">0.2%</td>
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
<td align="right">856,700</td>
<td align="right">91.9%</td>
<td align="right">1,475,689</td>
<td align="right">95.0%</td>
<td align="right">72.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">75,580</td>
<td align="right">8.1%</td>
<td align="right">77,817</td>
<td align="right">5.0%</td>
<td align="right">3.0%</td>
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
<td align="right">840</td>
<td align="right">1.1%</td>
<td align="right">920</td>
<td align="right">1.2%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">1,640</td>
<td align="right">2.2%</td>
<td align="right">1,780</td>
<td align="right">2.3%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">4,300</td>
<td align="right">5.7%</td>
<td align="right">4,521</td>
<td align="right">5.8%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">20,240</td>
<td align="right">26.8%</td>
<td align="right">21,020</td>
<td align="right">27.0%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,080</td>
<td align="right">5.4%</td>
<td align="right">4,200</td>
<td align="right">5.4%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">14,980</td>
<td align="right">19.8%</td>
<td align="right">15,358</td>
<td align="right">19.7%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">19,500</td>
<td align="right">25.8%</td>
<td align="right">19,858</td>
<td align="right">25.5%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,120</td>
<td align="right">1.5%</td>
<td align="right">1,140</td>
<td align="right">1.5%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,420</td>
<td align="right">1.9%</td>
<td align="right">1,440</td>
<td align="right">1.9%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">2,000</td>
<td align="right">2.6%</td>
<td align="right">2,000</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">920</td>
<td align="right">1.2%</td>
<td align="right">920</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">380</td>
<td align="right">0.5%</td>
<td align="right">380</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
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
<td align="right">96,367,631</td>
<td align="right">99.7%</td>
<td align="right">134,015,696</td>
<td align="right">99.8%</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">102,200</td>
<td align="right">0.1%</td>
<td align="right">102,200</td>
<td align="right">0.1%</td>
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
<td align="right">1,500</td>
<td align="right">0.0%</td>
<td align="right">1,500</td>
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
<td align="right">81,940</td>
<td align="right">0.1%</td>
<td align="right">81,940</td>
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
<td align="left">Success</td>
<td align="right">98,120</td>
<td align="right">100.0%</td>
<td align="right">98,120</td>
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
<td align="right">2,140</td>
<td align="right">0.1%</td>
<td align="right">2,140</td>
<td align="right">0.1%</td>
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
<td align="right">3,809,260</td>
<td align="right">99.9%</td>
<td align="right">3,809,260</td>
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
<td align="right">2,080</td>
<td align="right">100.0%</td>
<td align="right">2,080</td>
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
<td align="right">8,578,840</td>
<td align="right">55.4%</td>
<td align="right">8,578,840</td>
<td align="right">55.4%</td>
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
<td align="right">6,899,920</td>
<td align="right">44.5%</td>
<td align="right">6,899,920</td>
<td align="right">44.5%</td>
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
<td align="right">880</td>
<td align="right">8.7%</td>
<td align="right">880</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,260</td>
<td align="right">91.3%</td>
<td align="right">9,260</td>
<td align="right">91.3%</td>
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
<td align="right">6,780</td>
<td align="right">73.2%</td>
<td align="right">6,780</td>
<td align="right">73.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">24.4%</td>
<td align="right">2,260</td>
<td align="right">24.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">2.4%</td>
<td align="right">220</td>
<td align="right">2.4%</td>
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
<td align="right">3,182,700</td>
<td align="right">6.3%</td>
<td align="right">3,258,214</td>
<td align="right">6.5%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">15,000,900</td>
<td align="right">29.8%</td>
<td align="right">15,032,840</td>
<td align="right">29.9%</td>
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
<td align="right">32,052,460</td>
<td align="right">63.8%</td>
<td align="right">32,025,360</td>
<td align="right">63.6%</td>
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
<td align="right">13,960</td>
<td align="right">4.5%</td>
<td align="right">14,080</td>
<td align="right">4.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">295,480</td>
<td align="right">95.5%</td>
<td align="right">296,080</td>
<td align="right">95.5%</td>
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
<td align="left">overridden</td>
<td align="right">1,320</td>
<td align="right">9.5%</td>
<td align="right">1,380</td>
<td align="right">9.8%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">3,020</td>
<td align="right">21.6%</td>
<td align="right">3,080</td>
<td align="right">21.9%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">7,240</td>
<td align="right">51.9%</td>
<td align="right">7,240</td>
<td align="right">51.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">600</td>
<td align="right">4.3%</td>
<td align="right">600</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">600</td>
<td align="right">4.3%</td>
<td align="right">600</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">420</td>
<td align="right">3.0%</td>
<td align="right">420</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">320</td>
<td align="right">2.3%</td>
<td align="right">320</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">200</td>
<td align="right">1.4%</td>
<td align="right">200</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">160</td>
<td align="right">1.1%</td>
<td align="right">160</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
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
<td align="right">4,720</td>
<td align="right">100.0%</td>
<td align="right">4,720</td>
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
<td align="right">119,500</td>
<td align="right">2.6%</td>
<td align="right">128,495</td>
<td align="right">2.8%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,394,560</td>
<td align="right">97.3%</td>
<td align="right">4,394,560</td>
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
<td align="right">1,460</td>
<td align="right">41.5%</td>
<td align="right">1,540</td>
<td align="right">42.8%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,060</td>
<td align="right">58.5%</td>
<td align="right">2,060</td>
<td align="right">57.2%</td>
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
<td align="right">260</td>
<td align="right">17.8%</td>
<td align="right">340</td>
<td align="right">22.1%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">800</td>
<td align="right">54.8%</td>
<td align="right">800</td>
<td align="right">51.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">160</td>
<td align="right">11.0%</td>
<td align="right">160</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">8.2%</td>
<td align="right">120</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">120</td>
<td align="right">8.2%</td>
<td align="right">120</td>
<td align="right">7.8%</td>
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
<td align="right">2,283,340</td>
<td align="right">2.0%</td>
<td align="right">10,061,195</td>
<td align="right">8.2%</td>
<td align="right">340.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">985,549</td>
<td align="right">0.9%</td>
<td align="right">996,124</td>
<td align="right">0.8%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">110,841,610</td>
<td align="right">97.1%</td>
<td align="right">110,893,119</td>
<td align="right">90.9%</td>
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
<td align="right">88,320</td>
<td align="right">81.5%</td>
<td align="right">235,039</td>
<td align="right">92.0%</td>
<td align="right">166.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20,000</td>
<td align="right">18.5%</td>
<td align="right">20,360</td>
<td align="right">8.0%</td>
<td align="right">1.8%</td>
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
<td align="right">780</td>
<td align="right">3.9%</td>
<td align="right">1,080</td>
<td align="right">5.3%</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,380</td>
<td align="right">6.9%</td>
<td align="right">1,420</td>
<td align="right">7.0%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,460</td>
<td align="right">67.3%</td>
<td align="right">13,480</td>
<td align="right">66.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,760</td>
<td align="right">8.8%</td>
<td align="right">1,760</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">1,300</td>
<td align="right">6.5%</td>
<td align="right">1,300</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,000</td>
<td align="right">5.0%</td>
<td align="right">1,000</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">200</td>
<td align="right">1.0%</td>
<td align="right">200</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">0.6%</td>
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
<td align="right">7,300</td>
<td align="right">0.0%</td>
<td align="right">12,204</td>
<td align="right">0.0%</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,670,340</td>
<td align="right">100.0%</td>
<td align="right">29,672,971</td>
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
<td align="left">Failure</td>
<td align="right">320</td>
<td align="right">7.0%</td>
<td align="right">380</td>
<td align="right">8.2%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,260</td>
<td align="right">93.0%</td>
<td align="right">4,260</td>
<td align="right">91.8%</td>
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
<td align="right">240</td>
<td align="right">75.0%</td>
<td align="right">300</td>
<td align="right">78.9%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">80</td>
<td align="right">25.0%</td>
<td align="right">80</td>
<td align="right">21.1%</td>
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
<td align="right">60,567,873</td>
<td align="right">3.3%</td>
<td align="right">104,724,772</td>
<td align="right">4.1%</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">615,515,104</td>
<td align="right">33.3%</td>
<td align="right">883,314,585</td>
<td align="right">34.3%</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,120,186,818</td>
<td align="right">60.6%</td>
<td align="right">1,526,208,859</td>
<td align="right">59.2%</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">52,156,613</td>
<td align="right">2.8%</td>
<td align="right">62,817,091</td>
<td align="right">2.4%</td>
<td align="right">20.4%</td>
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
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,420,400</td>
<td align="right">2.8%</td>
<td align="right">3,401,532</td>
<td align="right">5.5%</td>
<td align="right">139.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">742,960</td>
<td align="right">1.4%</td>
<td align="right">1,223,965</td>
<td align="right">2.0%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,400,800</td>
<td align="right">4.7%</td>
<td align="right">3,483,326</td>
<td align="right">5.6%</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,425,835</td>
<td align="right">4.7%</td>
<td align="right">3,321,827</td>
<td align="right">5.4%</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">25,086,260</td>
<td align="right">48.8%</td>
<td align="right">30,792,820</td>
<td align="right">49.7%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">5,236,269</td>
<td align="right">10.2%</td>
<td align="right">5,576,430</td>
<td align="right">9.0%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,182,700</td>
<td align="right">6.2%</td>
<td align="right">3,258,214</td>
<td align="right">5.3%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">918,880</td>
<td align="right">1.8%</td>
<td align="right">940,679</td>
<td align="right">1.5%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">985,549</td>
<td align="right">1.9%</td>
<td align="right">996,124</td>
<td align="right">1.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">8,578,840</td>
<td align="right">16.7%</td>
<td align="right">8,578,840</td>
<td align="right">13.8%</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,628,000</td>
<td align="right">2.7%</td>
<td align="right">8,347,572</td>
<td align="right">8.0%</td>
<td align="right">412.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">756,240</td>
<td align="right">1.2%</td>
<td align="right">3,466,144</td>
<td align="right">3.3%</td>
<td align="right">358.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,217,100</td>
<td align="right">3.7%</td>
<td align="right">6,445,049</td>
<td align="right">6.1%</td>
<td align="right">190.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">4,817,320</td>
<td align="right">8.0%</td>
<td align="right">11,552,832</td>
<td align="right">11.0%</td>
<td align="right">139.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,909,740</td>
<td align="right">13.1%</td>
<td align="right">16,600,615</td>
<td align="right">15.8%</td>
<td align="right">109.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,509,960</td>
<td align="right">2.5%</td>
<td align="right">2,703,376</td>
<td align="right">2.6%</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">14,851,000</td>
<td align="right">24.5%</td>
<td align="right">23,108,817</td>
<td align="right">22.0%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,991,920</td>
<td align="right">14.8%</td>
<td align="right">10,511,366</td>
<td align="right">10.0%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">15,000,840</td>
<td align="right">24.8%</td>
<td align="right">15,032,674</td>
<td align="right">14.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">610,880</td>
<td align="right">1.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2,364,171</td>
<td align="right">2.3%</td>
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
<td align="left">Frame objects created</td>
<td align="right">2,621,120</td>
<td align="right">1.8%</td>
<td align="right">1,987,055</td>
<td align="right">1.3%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">9,119,780</td>
<td align="right">6.2%</td>
<td align="right">8,731,496</td>
<td align="right">5.9%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">38,383,473</td>
<td align="right">25.9%</td>
<td align="right">37,995,159</td>
<td align="right">25.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">38,383,473</td>
<td align="right">25.9%</td>
<td align="right">37,995,159</td>
<td align="right">25.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">109,590,253</td>
<td align="right">74.1%</td>
<td align="right">109,585,723</td>
<td align="right">74.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">29,249,293</td>
<td align="right">19.8%</td>
<td align="right">29,249,263</td>
<td align="right">19.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">29,263,693</td>
<td align="right">19.8%</td>
<td align="right">29,263,663</td>
<td align="right">19.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">117,397,466</td>
<td align="right">79.3%</td>
<td align="right">117,397,496</td>
<td align="right">79.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,680</td>
<td align="right">0.0%</td>
<td align="right">3,680</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">10,720</td>
<td align="right">0.0%</td>
<td align="right">10,720</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">780,253</td>
<td align="right">0.5%</td>
<td align="right">780,253</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">890,860</td>
<td align="right">0.6%</td>
<td align="right">890,860</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">5,112,700</td>
<td align="right">3.5%</td>
<td align="right">5,112,700</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">480</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">622,580</td>
<td align="right">0.3%</td>
<td align="right">1,332,081</td>
<td align="right">0.6%</td>
<td align="right">114.0%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">1,197,121,224</td>
<td align="right">1,197,121,224 / 0 !!</td>
<td align="right">697,154,451</td>
<td align="right">697,154,451 / 0 !!</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">1,125,789,598</td>
<td align="right">1,125,789,598 / 0 !!</td>
<td align="right">656,821,181</td>
<td align="right">656,821,181 / 0 !!</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">809,084,118</td>
<td align="right">809,084,118 / 0 !!</td>
<td align="right">1,104,441,525</td>
<td align="right">1,104,441,525 / 0 !!</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">1,041,422,629</td>
<td align="right">1,041,422,629 / 0 !!</td>
<td align="right">1,305,549,967</td>
<td align="right">1,305,549,967 / 0 !!</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">687,015</td>
<td align="right"></td>
<td align="right">765,777</td>
<td align="right"></td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">125,520,399</td>
<td align="right"></td>
<td align="right">129,490,710</td>
<td align="right"></td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">5,116,804</td>
<td align="right"></td>
<td align="right">5,242,624</td>
<td align="right"></td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">63,328,371</td>
<td align="right"></td>
<td align="right">62,655,814</td>
<td align="right"></td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">4,459,621</td>
<td align="right"></td>
<td align="right">4,506,046</td>
<td align="right"></td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">153,317,321</td>
<td align="right">68.6%</td>
<td align="right">151,925,622</td>
<td align="right">68.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">69,415,544</td>
<td align="right">31.0%</td>
<td align="right">69,825,375</td>
<td align="right">31.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">69,454,764</td>
<td align="right"></td>
<td align="right">69,864,595</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">154,191,301</td>
<td align="right">69.0%</td>
<td align="right">153,509,851</td>
<td align="right">68.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">141,568,942</td>
<td align="right"></td>
<td align="right">141,082,750</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">251,400</td>
<td align="right">0.1%</td>
<td align="right">252,148</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">4,405,040</td>
<td align="right"></td>
<td align="right">4,405,040</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">436,500</td>
<td align="right">9.9%</td>
<td align="right">436,500</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">39,240</td>
<td align="right">0.9%</td>
<td align="right">39,240</td>
<td align="right">0.9%</td>
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
<td align="right">5,380</td>
<td align="right">80,580</td>
<td align="right">483,984,010</td>
<td align="right">5,338</td>
<td align="right">82,660</td>
<td align="right">483,359,037</td>
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
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">17,750</td>
<td align="right">1.9%</td>
<td align="right">8,775.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">32,900</td>
<td align="right">49.4%</td>
<td align="right">937,591</td>
<td align="right">97.8%</td>
<td align="right">2,749.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">66,620</td>
<td align="right"></td>
<td align="right">958,940</td>
<td align="right"></td>
<td align="right">1,339.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">940</td>
<td align="right">1.4%</td>
<td align="right">11,166</td>
<td align="right">1.2%</td>
<td align="right">1,087.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">32,700</td>
<td align="right">49.1%</td>
<td align="right">109,720</td>
<td align="right">11.4%</td>
<td align="right">235.5%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">211,924,195</td>
<td align="right"></td>
<td align="right">36,195,455</td>
<td align="right"></td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,472,684,684</td>
<td align="right">1,166.8%</td>
<td align="right">671,667,394</td>
<td align="right">1,855.7%</td>
<td align="right">-72.8%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">520</td>
<td align="right">1.6%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">33,720</td>
<td align="right">50.6%</td>
<td align="right">21,349</td>
<td align="right">2.2%</td>
<td align="right">-36.7%</td>
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
<td align="right">32,220</td>
<td align="right">97.9%</td>
<td align="right">934,012</td>
<td align="right">99.6%</td>
<td align="right">2,798.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">32,900</td>
<td align="right"></td>
<td align="right">937,591</td>
<td align="right"></td>
<td align="right">2,749.8%</td>
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
<td align="right">220</td>
<td align="right">0.7%</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">720</td>
<td align="right">2.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">6,660</td>
<td align="right">20.2%</td>
<td align="right">12,389</td>
<td align="right">1.3%</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">3,960</td>
<td align="right">12.0%</td>
<td align="right">194,441</td>
<td align="right">20.7%</td>
<td align="right">4,810.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">10,760</td>
<td align="right">32.7%</td>
<td align="right">406,218</td>
<td align="right">43.3%</td>
<td align="right">3,675.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,240</td>
<td align="right">25.0%</td>
<td align="right">274,352</td>
<td align="right">29.3%</td>
<td align="right">3,229.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,300</td>
<td align="right">7.0%</td>
<td align="right">46,281</td>
<td align="right">4.9%</td>
<td align="right">1,912.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">240</td>
<td align="right">0.7%</td>
<td align="right">3,130</td>
<td align="right">0.3%</td>
<td align="right">1,204.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">780</td>
<td align="right">0.1%</td>
<td align="right">3,800.0%</td>
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
<td align="right">4,460</td>
<td align="right">13.6%</td>
<td align="right">6,877</td>
<td align="right">0.7%</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">4,240</td>
<td align="right">12.9%</td>
<td align="right">171,570</td>
<td align="right">18.3%</td>
<td align="right">3,946.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">6,280</td>
<td align="right">19.1%</td>
<td align="right">83,328</td>
<td align="right">8.9%</td>
<td align="right">1,226.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">12,020</td>
<td align="right">36.5%</td>
<td align="right">516,814</td>
<td align="right">55.1%</td>
<td align="right">4,199.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">4,520</td>
<td align="right">13.7%</td>
<td align="right">145,738</td>
<td align="right">15.5%</td>
<td align="right">3,124.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">660</td>
<td align="right">2.0%</td>
<td align="right">8,656</td>
<td align="right">0.9%</td>
<td align="right">1,211.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">1,029</td>
<td align="right">0.1%</td>
<td align="right">2,472.5%</td>
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
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">2,162,540</td>
<td align="right">320</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">1,390,620</td>
<td align="right">1,871</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">9,660</td>
<td align="right">20</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">2,100</td>
<td align="right">7</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,431,980</td>
<td align="right">17,324</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">396,580</td>
<td align="right">2,372</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">181,780</td>
<td align="right">2,354</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">4,200</td>
<td align="right">70</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">3,099,380</td>
<td align="right">65,260</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">197,240</td>
<td align="right">4,808</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">6,452,980</td>
<td align="right">178,525</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">92,880</td>
<td align="right">2,574</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">79,260</td>
<td align="right">2,334</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">995,260</td>
<td align="right">29,555</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">2,100</td>
<td align="right">63</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">2,100</td>
<td align="right">63</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,353,920</td>
<td align="right">44,375</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">94,280</td>
<td align="right">3,194</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">79,900</td>
<td align="right">2,934</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,106,940</td>
<td align="right">161,703</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">5,063,956</td>
<td align="right">223,258</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,576,880</td>
<td align="right">114,850</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">50,380</td>
<td align="right">2,376</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">8,117,980</td>
<td align="right">430,814</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">755,091</td>
<td align="right">40,559</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">34,641,640</td>
<td align="right">1,878,571</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">9,980</td>
<td align="right">553</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">551,600</td>
<td align="right">32,119</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">1,399,940</td>
<td align="right">87,713</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">7,968,800</td>
<td align="right">525,386</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">990,380</td>
<td align="right">67,062</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">1,122,440</td>
<td align="right">87,713</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">969,060</td>
<td align="right">84,135</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">7,122,616</td>
<td align="right">619,092</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">376,280</td>
<td align="right">33,260</td>
<td align="right">-91.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,253,000</td>
<td align="right">403,785</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">6,280,436</td>
<td align="right">599,991</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">136,732,943</td>
<td align="right">14,886,023</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">13,563,593</td>
<td align="right">1,503,557</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">4,971,500</td>
<td align="right">587,805</td>
<td align="right">-88.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,649,540</td>
<td align="right">200,805</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">5,597,439</td>
<td align="right">691,244</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">3,414,700</td>
<td align="right">438,131</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">8,525,319</td>
<td align="right">1,121,582</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">21,196,373</td>
<td align="right">3,113,087</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,767,359</td>
<td align="right">261,359</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">9,160</td>
<td align="right">1,360</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">38,278,753</td>
<td align="right">6,063,687</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,410</td>
<td align="right">700</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">181,143,106</td>
<td align="right">28,915,180</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">33,656,593</td>
<td align="right">5,379,698</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,155,659</td>
<td align="right">689,658</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">211,924,195</td>
<td align="right">36,195,455</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">44,774,044</td>
<td align="right">7,901,997</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">30,470,610</td>
<td align="right">5,655,817</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">39,180</td>
<td align="right">7,612</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">60,940</td>
<td align="right">11,944</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">10,226,047</td>
<td align="right">2,012,479</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">27,603,436</td>
<td align="right">5,461,929</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">29,383,957</td>
<td align="right">5,834,929</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">97,915,291</td>
<td align="right">19,466,489</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">7,453,426</td>
<td align="right">1,519,586</td>
<td align="right">-79.6%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">24,963,457</td>
<td align="right">5,155,783</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">12,758,987</td>
<td align="right">2,647,360</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">6,778,460</td>
<td align="right">1,421,649</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">21,368,656</td>
<td align="right">4,680,028</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,651,647</td>
<td align="right">1,902,752</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">20,288,768</td>
<td align="right">4,619,617</td>
<td align="right">-77.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">664,980</td>
<td align="right">151,783</td>
<td align="right">-77.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">13,878,118</td>
<td align="right">3,186,317</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">322,460</td>
<td align="right">74,186</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">158,820</td>
<td align="right">36,705</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">55,393,743</td>
<td align="right">12,881,500</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">366,440</td>
<td align="right">85,611</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,960,380</td>
<td align="right">1,160,075</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">25,697,109</td>
<td align="right">6,026,254</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">972,320</td>
<td align="right">230,961</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">972,320</td>
<td align="right">230,961</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">18,101,437</td>
<td align="right">4,313,578</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">332,360</td>
<td align="right">79,280</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">130,720</td>
<td align="right">31,425</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">29,975,108</td>
<td align="right">7,215,156</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">20,015,033</td>
<td align="right">4,969,168</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">18,513,533</td>
<td align="right">4,628,231</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">2,021,079</td>
<td align="right">506,589</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">8,783,670</td>
<td align="right">2,213,506</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">30,998,336</td>
<td align="right">7,871,567</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,060,583</td>
<td align="right">275,622</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,878,876</td>
<td align="right">1,539,038</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">24,136,358</td>
<td align="right">6,471,159</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">42,726,960</td>
<td align="right">11,678,243</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">300,580</td>
<td align="right">82,160</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">13,380</td>
<td align="right">3,660</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">42,649,220</td>
<td align="right">11,675,170</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">44,888,689</td>
<td align="right">12,478,346</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">214,688,123</td>
<td align="right">60,129,726</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">3,959,459</td>
<td align="right">1,109,602</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">3,270,300</td>
<td align="right">920,344</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,269,860</td>
<td align="right">920,344</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">33,994,239</td>
<td align="right">9,594,507</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">875,400</td>
<td align="right">247,975</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">8,582,680</td>
<td align="right">2,466,946</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">161,860,235</td>
<td align="right">46,724,170</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">32,443,920</td>
<td align="right">9,400,464</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">499,838</td>
<td align="right">149,454</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">293,260</td>
<td align="right">88,720</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">27,534,396</td>
<td align="right">8,538,390</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,272,540</td>
<td align="right">1,026,588</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">20,597,450</td>
<td align="right">6,479,035</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">30,893,660</td>
<td align="right">9,812,084</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">25,873,858</td>
<td align="right">8,241,369</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">28,563,317</td>
<td align="right">9,124,821</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">16,219,624</td>
<td align="right">5,241,744</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">12,653,920</td>
<td align="right">4,204,957</td>
<td align="right">-66.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">927,840</td>
<td align="right">309,220</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,952,753</td>
<td align="right">1,710,617</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">98,452,114</td>
<td align="right">34,130,912</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">26,150,065</td>
<td align="right">9,074,871</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,526,079</td>
<td align="right">530,281</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">258,320</td>
<td align="right">90,096</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">807,640</td>
<td align="right">287,432</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">641,300</td>
<td align="right">248,418</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">2,171,340</td>
<td align="right">855,819</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">2,313,640</td>
<td align="right">918,169</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">6,143,111</td>
<td align="right">2,553,328</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">269,600</td>
<td align="right">118,458</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">187,400</td>
<td align="right">84,648</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">371,000</td>
<td align="right">179,696</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">4,043,196</td>
<td align="right">1,983,421</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,644,216</td>
<td align="right">2,781,575</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">34,216,890</td>
<td align="right">16,881,743</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">348,180</td>
<td align="right">176,716</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">348,180</td>
<td align="right">176,716</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">12,625,043</td>
<td align="right">6,425,040</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">127,260</td>
<td align="right">64,945</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">125,800</td>
<td align="right">64,305</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">5,980</td>
<td align="right">3,080</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">2,243,573</td>
<td align="right">1,159,645</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">4,551,040</td>
<td align="right">2,366,922</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,346,680</td>
<td align="right">718,354</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">19,220,756</td>
<td align="right">10,505,523</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,085,120</td>
<td align="right">604,115</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">7,472,580</td>
<td align="right">4,312,926</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">7,517,280</td>
<td align="right">4,380,218</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,354,920</td>
<td align="right">796,951</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">4,242,520</td>
<td align="right">2,521,808</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">241,880</td>
<td align="right">144,733</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">4,640</td>
<td align="right">2,826</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">589,640</td>
<td align="right">368,174</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">589,640</td>
<td align="right">368,174</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">2,120</td>
<td align="right">1,340</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">2,280</td>
<td align="right">1,500</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">9,534,872</td>
<td align="right">6,320,092</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">4,105,029</td>
<td align="right">2,769,297</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">602,180</td>
<td align="right">423,598</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">86,920</td>
<td align="right">61,763</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">33,440</td>
<td align="right">24,158</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">3,523,619</td>
<td align="right">2,548,938</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">3,323,175</td>
<td align="right">2,429,579</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">711,900</td>
<td align="right">521,967</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">123,600</td>
<td align="right">93,946</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">6,104,780</td>
<td align="right">4,680,365</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">425,280</td>
<td align="right">327,051</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">3,100</td>
<td align="right">2,445</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">6,158,260</td>
<td align="right">4,868,390</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">392,180</td>
<td align="right">312,426</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">3,983,540</td>
<td align="right">3,174,113</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">53,520</td>
<td align="right">42,804</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,382,120</td>
<td align="right">1,114,750</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">8,685,260</td>
<td align="right">7,159,273</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">2,773,440</td>
<td align="right">2,288,348</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">5,360</td>
<td align="right">4,460</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">3,085,380</td>
<td align="right">2,618,826</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">6,320,263</td>
<td align="right">5,366,471</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">6,458,963</td>
<td align="right">5,841,847</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,693,890</td>
<td align="right">2,447,740</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,420</td>
<td align="right">1,308</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">126,500</td>
<td align="right">117,505</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,016,500</td>
<td align="right">1,066,476</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,665,359</td>
<td align="right">1,625,612</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,314,440</td>
<td align="right">1,292,641</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,169,140</td>
<td align="right">2,156,475</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,538,936</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">529,580</td>
<td align="right">531,065</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">376,020</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">127,340</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">41,600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">26,480</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">18,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">18,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">10,240</td>
<td align="right">10,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">9,960</td>
<td align="right">9,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">9,520</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">4,080</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">2,560</td>
<td align="right">2,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">40</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right"></td>
<td align="right">41,351,238</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right"></td>
<td align="right">80</td>
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
<td align="right">1,080</td>
<td align="right">10,740</td>
<td align="right">894.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">480</td>
<td align="right">1,140</td>
<td align="right">137.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">3,340</td>
<td align="right">7,354</td>
<td align="right">120.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">40</td>
<td align="right"></td>
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
<td align="right">240</td>
<td align="right">240</td>
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
<td align="right">320</td>
<td align="right">320</td>
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
<td align="right">320</td>
<td align="right">320</td>
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
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
