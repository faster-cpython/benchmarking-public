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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">417,492</td>
<td align="right">610,590</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">853,546</td>
<td align="right">1,240,301</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">855,951</td>
<td align="right">1,242,156</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,885,645</td>
<td align="right">4,172,810</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">289,270</td>
<td align="right">417,986</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,162,304</td>
<td align="right">1,677,234</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">438,573</td>
<td align="right">631,684</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">881,840</td>
<td align="right">1,268,122</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,835,440</td>
<td align="right">5,509,032</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,190,541</td>
<td align="right">1,705,471</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">596,202</td>
<td align="right">853,667</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">458,659</td>
<td align="right">651,731</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,228,354</td>
<td align="right">1,743,284</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">307,942</td>
<td align="right">436,682</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">308,004</td>
<td align="right">436,744</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">923,978</td>
<td align="right">1,309,975</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">616,544</td>
<td align="right">873,826</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">467,798</td>
<td align="right">660,890</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">940,387</td>
<td align="right">1,326,370</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">786,608</td>
<td align="right">1,109,034</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">954,344</td>
<td align="right">1,340,370</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">161,528</td>
<td align="right">225,895</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">970,802</td>
<td align="right">1,356,800</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">668,116</td>
<td align="right">925,581</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">170,701</td>
<td align="right">235,059</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,900,931</td>
<td align="right">2,609,070</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,995,627</td>
<td align="right">6,799,605</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">180,767</td>
<td align="right">245,134</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,815,918</td>
<td align="right">5,167,916</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">9,839,154</td>
<td align="right">13,315,129</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,117,300</td>
<td align="right">9,626,863</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,473,927</td>
<td align="right">8,727,736</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,635,100</td>
<td align="right">4,858,776</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,733,309</td>
<td align="right">2,312,621</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,554,087</td>
<td align="right">2,069,925</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,856,582</td>
<td align="right">6,465,912</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,333,738</td>
<td align="right">7,072,892</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">201,344</td>
<td align="right">265,710</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,718,882</td>
<td align="right">11,488,656</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,847,609</td>
<td align="right">5,006,700</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,125,644</td>
<td align="right">5,348,839</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,335,612</td>
<td align="right">1,721,289</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">50,562,898</td>
<td align="right">64,604,102</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,661,202</td>
<td align="right">3,370,700</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,277,538</td>
<td align="right">2,860,170</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,544,024</td>
<td align="right">3,188,155</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">10,741,898</td>
<td align="right">13,383,826</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">17,208,937</td>
<td align="right">21,329,630</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,941,743</td>
<td align="right">2,392,232</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">15,313,896</td>
<td align="right">18,854,380</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">852,295</td>
<td align="right">1,045,402</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">2,337,136</td>
<td align="right">2,852,084</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,363,937</td>
<td align="right">4,072,300</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">11,064,607</td>
<td align="right">13,388,190</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,987,720</td>
<td align="right">2,374,385</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">999,454</td>
<td align="right">1,193,198</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">15,569,472</td>
<td align="right">18,402,771</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,616,716</td>
<td align="right">11,356,873</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,948,242</td>
<td align="right">6,978,743</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">773,043</td>
<td align="right">901,752</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,743,545</td>
<td align="right">8,837,800</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">462,262</td>
<td align="right">526,555</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,614,406</td>
<td align="right">9,580,986</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">618,328</td>
<td align="right">682,604</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,139,414</td>
<td align="right">3,461,196</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">109</td>
<td align="right">103</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,788</td>
<td align="right">5,020</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,483,571</td>
<td align="right">1,547,847</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,188</td>
<td align="right">13,419</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,411</td>
<td align="right">17,642</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,411</td>
<td align="right">17,642</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">184,987</td>
<td align="right">186,267</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">67,142</td>
<td align="right">67,602</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,563</td>
<td align="right">36,797</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,489</td>
<td align="right">4,469</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">30,020</td>
<td align="right">29,928</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">94,374</td>
<td align="right">94,624</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">452</td>
<td align="right">451</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,130</td>
<td align="right">3,124</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">443,904</td>
<td align="right">444,701</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">44,022</td>
<td align="right">44,057</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">89,288</td>
<td align="right">89,326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">20,701</td>
<td align="right">20,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">37,953</td>
<td align="right">37,962</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">57,470</td>
<td align="right">57,481</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">22,092</td>
<td align="right">22,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,046</td>
<td align="right">34,040</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">28,686</td>
<td align="right">28,681</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">149,256</td>
<td align="right">149,276</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,471</td>
<td align="right">21,473</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">26,019</td>
<td align="right">26,021</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">146,985</td>
<td align="right">146,975</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">300,240</td>
<td align="right">300,227</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">61,373</td>
<td align="right">61,375</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">892,569</td>
<td align="right">892,598</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">489,418</td>
<td align="right">489,414</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,643</td>
<td align="right">1,818,652</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,067,766</td>
<td align="right">5,067,766</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,137</td>
<td align="right">105,137</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,107</td>
<td align="right">105,107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">84,693</td>
<td align="right">84,693</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,098</td>
<td align="right">77,098</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,585</td>
<td align="right">67,585</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,468</td>
<td align="right">55,468</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,466</td>
<td align="right">55,466</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">50,952</td>
<td align="right">50,952</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">43,864</td>
<td align="right">43,864</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,873</td>
<td align="right">42,873</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">39,010</td>
<td align="right">39,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">38,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,547</td>
<td align="right">29,547</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,763</td>
<td align="right">28,763</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">28,680</td>
<td align="right">28,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">26,276</td>
<td align="right">26,276</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">21,676</td>
<td align="right">21,676</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">20,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">17,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,855</td>
<td align="right">12,855</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,831</td>
<td align="right">12,831</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,728</td>
<td align="right">12,728</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">9,142</td>
<td align="right">9,142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">8,731</td>
<td align="right">8,731</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">8,731</td>
<td align="right">8,731</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">8,502</td>
<td align="right">8,502</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,485</td>
<td align="right">8,485</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">8,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,396</td>
<td align="right">4,396</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,227</td>
<td align="right">4,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">4,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">742</td>
<td align="right">742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">368</td>
<td align="right">368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">195</td>
<td align="right">195</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">179</td>
<td align="right">179</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">152</td>
<td align="right">152</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">148</td>
<td align="right">148</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">139</td>
<td align="right">139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">93</td>
<td align="right">93</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">68</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">37</td>
<td align="right">37</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
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
<td align="right">3,833,340</td>
<td align="right">72.0%</td>
<td align="right">5,506,525</td>
<td align="right">76.6%</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,485,367</td>
<td align="right">27.9%</td>
<td align="right">1,678,709</td>
<td align="right">23.4%</td>
<td align="right">13.0%</td>
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
<td align="right">1,982</td>
<td align="right">94.4%</td>
<td align="right">2,388</td>
<td align="right">95.3%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118</td>
<td align="right">5.6%</td>
<td align="right">119</td>
<td align="right">4.7%</td>
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
<td align="left">or</td>
<td align="right">551</td>
<td align="right">27.8%</td>
<td align="right">709</td>
<td align="right">29.7%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">940</td>
<td align="right">47.4%</td>
<td align="right">1,192</td>
<td align="right">49.9%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">213</td>
<td align="right">10.7%</td>
<td align="right">209</td>
<td align="right">8.8%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">191</td>
<td align="right">9.6%</td>
<td align="right">191</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">87</td>
<td align="right">4.4%</td>
<td align="right">87</td>
<td align="right">3.6%</td>
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
<td align="right">12,855</td>
<td align="right">100.0%</td>
<td align="right">12,855</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">495,790</td>
<td align="right">93.1%</td>
<td align="right">624,506</td>
<td align="right">94.4%</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,262</td>
<td align="right">6.8%</td>
<td align="right">36,494</td>
<td align="right">5.5%</td>
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
<td align="right">184</td>
<td align="right">61.1%</td>
<td align="right">186</td>
<td align="right">61.4%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">117</td>
<td align="right">38.9%</td>
<td align="right">117</td>
<td align="right">38.6%</td>
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
<td align="right">183</td>
<td align="right">99.5%</td>
<td align="right">185</td>
<td align="right">99.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">0.5%</td>
<td align="right">1</td>
<td align="right">0.5%</td>
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
<td align="right">19,549,145</td>
<td align="right">100.0%</td>
<td align="right">25,473,057</td>
<td align="right">100.0%</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,134</td>
<td align="right">0.0%</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">517</td>
<td align="right">0.0%</td>
<td align="right">517</td>
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
<td align="right">3,495</td>
<td align="right">100.0%</td>
<td align="right">3,489</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">41</td>
<td align="right">22.9%</td>
<td align="right">41</td>
<td align="right">22.9%</td>
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
<td align="right">457,937</td>
<td align="right">10.8%</td>
<td align="right">650,969</td>
<td align="right">12.5%</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,769,688</td>
<td align="right">89.1%</td>
<td align="right">4,542,636</td>
<td align="right">87.4%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,313</td>
<td align="right">0.1%</td>
<td align="right">4,277</td>
<td align="right">0.1%</td>
<td align="right">-0.8%</td>
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
<td align="right">455</td>
<td align="right">57.5%</td>
<td align="right">494</td>
<td align="right">59.6%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">336</td>
<td align="right">42.5%</td>
<td align="right">335</td>
<td align="right">40.4%</td>
<td align="right">-0.3%</td>
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
<td align="right">249</td>
<td align="right">54.7%</td>
<td align="right">292</td>
<td align="right">59.1%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">111</td>
<td align="right">24.4%</td>
<td align="right">107</td>
<td align="right">21.7%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">20.9%</td>
<td align="right">95</td>
<td align="right">19.2%</td>
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
<td align="right">1,405,908</td>
<td align="right">100.0%</td>
<td align="right">1,856,489</td>
<td align="right">100.0%</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
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
<td align="right">7</td>
<td align="right">100.0%</td>
<td align="right">7</td>
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
<td align="right">5,624,947</td>
<td align="right">99.6%</td>
<td align="right">6,010,930</td>
<td align="right">99.6%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,788</td>
<td align="right">0.4%</td>
<td align="right">21,788</td>
<td align="right">0.4%</td>
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
<td align="right">48</td>
<td align="right">15.8%</td>
<td align="right">52</td>
<td align="right">16.9%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">256</td>
<td align="right">84.2%</td>
<td align="right">256</td>
<td align="right">83.1%</td>
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
<td align="left">itertools</td>
<td align="right">72</td>
<td align="right">28.1%</td>
<td align="right">72</td>
<td align="right">28.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">69</td>
<td align="right">27.0%</td>
<td align="right">69</td>
<td align="right">27.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">50</td>
<td align="right">19.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">2.7%</td>
<td align="right">7</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">1.2%</td>
<td align="right">3</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.4%</td>
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
<td align="right">4,847,034</td>
<td align="right">12.3%</td>
<td align="right">6,455,931</td>
<td align="right">12.9%</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,251,439</td>
<td align="right">86.8%</td>
<td align="right">43,203,194</td>
<td align="right">86.4%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">334,047</td>
<td align="right">0.8%</td>
<td align="right">335,321</td>
<td align="right">0.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
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
<td align="right">4,793</td>
<td align="right">30.8%</td>
<td align="right">5,216</td>
<td align="right">32.6%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,761</td>
<td align="right">69.2%</td>
<td align="right">10,799</td>
<td align="right">67.4%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">1,269</td>
<td align="right">26.5%</td>
<td align="right">1,581</td>
<td align="right">30.3%</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">697</td>
<td align="right">14.5%</td>
<td align="right">747</td>
<td align="right">14.3%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,349</td>
<td align="right">28.1%</td>
<td align="right">1,347</td>
<td align="right">25.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">9.6%</td>
<td align="right">460</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">189</td>
<td align="right">3.9%</td>
<td align="right">189</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.5%</td>
<td align="right">71</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.9%</td>
<td align="right">45</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">23</td>
<td align="right">0.5%</td>
<td align="right">23</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.5%</td>
<td align="right">23</td>
<td align="right">0.4%</td>
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
<td align="right">13,964,524</td>
<td align="right">100.0%</td>
<td align="right">18,663,694</td>
<td align="right">100.0%</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">780</td>
<td align="right">0.0%</td>
<td align="right">776</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
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
<td align="right">274</td>
<td align="right">0.0%</td>
<td align="right">274</td>
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
<td align="right">2,359</td>
<td align="right">100.0%</td>
<td align="right">2,357</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">1,594,926</td>
<td align="right">100.0%</td>
<td align="right">2,302,972</td>
<td align="right">100.0%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13</td>
<td align="right">0.0%</td>
<td align="right">13</td>
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
<td align="right">55</td>
<td align="right">100.0%</td>
<td align="right">55</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,091,568</td>
<td align="right">95.3%</td>
<td align="right">5,378,892</td>
<td align="right">96.4%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">59,829</td>
<td align="right">1.4%</td>
<td align="right">59,830</td>
<td align="right">1.1%</td>
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
<td align="right">140,654</td>
<td align="right">3.3%</td>
<td align="right">140,654</td>
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
<td align="left">Success</td>
<td align="right">3,619</td>
<td align="right">86.6%</td>
<td align="right">3,620</td>
<td align="right">86.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">561</td>
<td align="right">13.4%</td>
<td align="right">561</td>
<td align="right">13.4%</td>
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
<td align="right">344</td>
<td align="right">61.3%</td>
<td align="right">344</td>
<td align="right">61.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">163</td>
<td align="right">29.1%</td>
<td align="right">163</td>
<td align="right">29.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">44</td>
<td align="right">7.8%</td>
<td align="right">44</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.8%</td>
<td align="right">10</td>
<td align="right">1.8%</td>
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
<td align="right">1,471,886</td>
<td align="right">98.6%</td>
<td align="right">1,921,935</td>
<td align="right">98.9%</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,264</td>
<td align="right">1.4%</td>
<td align="right">21,265</td>
<td align="right">1.1%</td>
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
<td align="right">20</td>
<td align="right">9.7%</td>
<td align="right">21</td>
<td align="right">10.1%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">90.3%</td>
<td align="right">187</td>
<td align="right">89.9%</td>
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
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
<td align="right">68</td>
<td align="right">36.4%</td>
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
<td align="right">9,103,233</td>
<td align="right">99.3%</td>
<td align="right">12,645,091</td>
<td align="right">99.5%</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">66,152</td>
<td align="right">0.7%</td>
<td align="right">66,604</td>
<td align="right">0.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">28</td>
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
<td align="right">450</td>
<td align="right">45.4%</td>
<td align="right">454</td>
<td align="right">45.4%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">542</td>
<td align="right">54.6%</td>
<td align="right">546</td>
<td align="right">54.6%</td>
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
<td align="left">sequence</td>
<td align="right">137</td>
<td align="right">25.3%</td>
<td align="right">142</td>
<td align="right">26.0%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">176</td>
<td align="right">32.5%</td>
<td align="right">175</td>
<td align="right">32.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">118</td>
<td align="right">21.8%</td>
<td align="right">118</td>
<td align="right">21.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">12.5%</td>
<td align="right">68</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">43</td>
<td align="right">7.9%</td>
<td align="right">43</td>
<td align="right">7.9%</td>
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
<td align="right">2,030,017</td>
<td align="right">100.0%</td>
<td align="right">2,158,760</td>
<td align="right">100.0%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">38</td>
<td align="right">0.0%</td>
<td align="right">38</td>
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
<td align="right">110</td>
<td align="right">100.0%</td>
<td align="right">110</td>
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
<td align="right">9,380,205</td>
<td align="right">3.3%</td>
<td align="right">12,856,875</td>
<td align="right">3.6%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">89,349,549</td>
<td align="right">31.8%</td>
<td align="right">115,243,467</td>
<td align="right">32.6%</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">182,052,845</td>
<td align="right">64.7%</td>
<td align="right">225,072,522</td>
<td align="right">63.6%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">479,913</td>
<td align="right">0.2%</td>
<td align="right">481,151</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
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
<td align="right">3,833,340</td>
<td align="right">41.0%</td>
<td align="right">5,506,525</td>
<td align="right">42.9%</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">457,937</td>
<td align="right">4.9%</td>
<td align="right">650,969</td>
<td align="right">5.1%</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,847,034</td>
<td align="right">51.8%</td>
<td align="right">6,455,931</td>
<td align="right">50.3%</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,134</td>
<td align="right">0.0%</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">66,152</td>
<td align="right">0.7%</td>
<td align="right">66,604</td>
<td align="right">0.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,262</td>
<td align="right">0.4%</td>
<td align="right">36,494</td>
<td align="right">0.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,264</td>
<td align="right">0.2%</td>
<td align="right">21,265</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">59,829</td>
<td align="right">0.6%</td>
<td align="right">59,830</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,788</td>
<td align="right">0.2%</td>
<td align="right">21,788</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,855</td>
<td align="right">0.1%</td>
<td align="right">12,855</td>
<td align="right">0.1%</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,312</td>
<td align="right">0.9%</td>
<td align="right">4,276</td>
<td align="right">0.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">274,509</td>
<td align="right">57.2%</td>
<td align="right">275,762</td>
<td align="right">57.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,488</td>
<td align="right">10.3%</td>
<td align="right">49,509</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,654</td>
<td align="right">29.3%</td>
<td align="right">140,654</td>
<td align="right">29.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">2.1%</td>
<td align="right">9,895</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">269</td>
<td align="right">0.1%</td>
<td align="right">269</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">144</td>
<td align="right">0.0%</td>
<td align="right">144</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">143</td>
<td align="right">0.0%</td>
<td align="right">143</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">86</td>
<td align="right">0.0%</td>
<td align="right">86</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">415,247</td>
<td align="right">1.5%</td>
<td align="right">543,991</td>
<td align="right">1.6%</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">22,689,973</td>
<td align="right">81.9%</td>
<td align="right">28,871,220</td>
<td align="right">85.2%</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">19,967,203</td>
<td align="right">72.0%</td>
<td align="right">25,054,195</td>
<td align="right">73.9%</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,320,990</td>
<td align="right">26.4%</td>
<td align="right">8,415,245</td>
<td align="right">24.8%</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,321,046</td>
<td align="right">26.4%</td>
<td align="right">8,415,301</td>
<td align="right">24.8%</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,747,903</td>
<td align="right">28.0%</td>
<td align="right">8,842,158</td>
<td align="right">26.1%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,747,903</td>
<td align="right">28.0%</td>
<td align="right">8,842,158</td>
<td align="right">26.1%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,422</td>
<td align="right">0.1%</td>
<td align="right">17,653</td>
<td align="right">0.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">426,857</td>
<td align="right">1.5%</td>
<td align="right">426,857</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">15</td>
<td align="right">0.0%</td>
<td align="right">15</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">41</td>
<td align="right">0.0%</td>
<td align="right">41</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<td align="right">1.6%</td>
<td align="right">456,471</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,507</td>
<td align="right">1.6%</td>
<td align="right">441,507</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="left">Method cache misses</td>
<td align="right">65,470</td>
<td align="right"></td>
<td align="right">28,667</td>
<td align="right"></td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">94,942</td>
<td align="right"></td>
<td align="right">51,343</td>
<td align="right"></td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,292,708</td>
<td align="right"></td>
<td align="right">1,807,638</td>
<td align="right"></td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,675,741</td>
<td align="right"></td>
<td align="right">10,610,771</td>
<td align="right"></td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">59,353,264</td>
<td align="right">14.3%</td>
<td align="right">77,835,965</td>
<td align="right">15.1%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">59,621,799</td>
<td align="right">16.7%</td>
<td align="right">76,684,799</td>
<td align="right">17.2%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">15,995,480</td>
<td align="right">49.8%</td>
<td align="right">20,438,024</td>
<td align="right">51.4%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">15,998,177</td>
<td align="right"></td>
<td align="right">20,440,731</td>
<td align="right"></td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">55,554,783</td>
<td align="right">15.5%</td>
<td align="right">70,630,513</td>
<td align="right">15.8%</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">152,238,792</td>
<td align="right">36.8%</td>
<td align="right">191,846,760</td>
<td align="right">37.1%</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">115,729,653</td>
<td align="right">32.4%</td>
<td align="right">144,455,581</td>
<td align="right">32.3%</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">82,838,113</td>
<td align="right">20.0%</td>
<td align="right">103,319,344</td>
<td align="right">20.0%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">10,338,261</td>
<td align="right"></td>
<td align="right">12,791,037</td>
<td align="right"></td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">29,720</td>
<td align="right"></td>
<td align="right">22,930</td>
<td align="right"></td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">126,720,386</td>
<td align="right">35.4%</td>
<td align="right">155,200,762</td>
<td align="right">34.7%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">17,216,406</td>
<td align="right"></td>
<td align="right">20,822,140</td>
<td align="right"></td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">119,523,572</td>
<td align="right">28.9%</td>
<td align="right">143,882,841</td>
<td align="right">27.8%</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">16,016,000</td>
<td align="right">49.8%</td>
<td align="right">19,171,044</td>
<td align="right">48.3%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,137,372</td>
<td align="right">50.2%</td>
<td align="right">19,292,397</td>
<td align="right">48.6%</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,832</td>
<td align="right">0.2%</td>
<td align="right">77,818</td>
<td align="right">0.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,540</td>
<td align="right">0.1%</td>
<td align="right">43,535</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">228</td>
<td align="right">5.9%</td>
<td align="right">275</td>
<td align="right">6.6%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">384,478,212</td>
<td align="right">1,775.7%</td>
<td align="right">461,713,098</td>
<td align="right">1,947.1%</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">21,652,591</td>
<td align="right"></td>
<td align="right">23,713,169</td>
<td align="right"></td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">3,212</td>
<td align="right">83.8%</td>
<td align="right">3,495</td>
<td align="right">83.9%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,834</td>
<td align="right"></td>
<td align="right">4,166</td>
<td align="right"></td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">3,251</td>
<td align="right">84.8%</td>
<td align="right">3,522</td>
<td align="right">84.5%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">394</td>
<td align="right">10.3%</td>
<td align="right">396</td>
<td align="right">9.5%</td>
<td align="right">0.5%</td>
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
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">390</td>
<td align="right">99.0%</td>
<td align="right">392</td>
<td align="right">99.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">394</td>
<td align="right"></td>
<td align="right">396</td>
<td align="right"></td>
<td align="right">0.5%</td>
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
<td align="right">4</td>
<td align="right">1.0%</td>
<td align="right">4</td>
<td align="right">1.0%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">109</td>
<td align="right">27.7%</td>
<td align="right">106</td>
<td align="right">26.8%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">34</td>
<td align="right">8.6%</td>
<td align="right">34</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">69</td>
<td align="right">17.5%</td>
<td align="right">70</td>
<td align="right">17.7%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">121</td>
<td align="right">30.7%</td>
<td align="right">127</td>
<td align="right">32.1%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">27</td>
<td align="right">6.9%</td>
<td align="right">26</td>
<td align="right">6.6%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">33</td>
<td align="right">8.4%</td>
<td align="right">32</td>
<td align="right">8.1%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1</td>
<td align="right">0.3%</td>
<td align="right">1</td>
<td align="right">0.3%</td>
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
<td align="right">50</td>
<td align="right">12.7%</td>
<td align="right">53</td>
<td align="right">13.4%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">81</td>
<td align="right">20.6%</td>
<td align="right">74</td>
<td align="right">18.7%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">35</td>
<td align="right">8.9%</td>
<td align="right">36</td>
<td align="right">9.1%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">100</td>
<td align="right">25.4%</td>
<td align="right">105</td>
<td align="right">26.5%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">83</td>
<td align="right">21.1%</td>
<td align="right">83</td>
<td align="right">21.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">38</td>
<td align="right">9.6%</td>
<td align="right">37</td>
<td align="right">9.3%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3</td>
<td align="right">0.8%</td>
<td align="right">4</td>
<td align="right">1.0%</td>
<td align="right">33.3%</td>
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
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">136,225</td>
<td align="right">200,684</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">136,284</td>
<td align="right">200,744</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">408,834</td>
<td align="right">602,123</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">681,382</td>
<td align="right">1,003,415</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">545,243</td>
<td align="right">802,901</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,362,752</td>
<td align="right">2,006,645</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">408,822</td>
<td align="right">601,938</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">408,822</td>
<td align="right">601,938</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">136,274</td>
<td align="right">200,646</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">408,824</td>
<td align="right">601,940</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">408,824</td>
<td align="right">601,940</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">408,828</td>
<td align="right">601,944</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,503,332</td>
<td align="right">2,211,494</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,188,974</td>
<td align="right">3,219,275</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,370,861</td>
<td align="right">2,014,810</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">553,094</td>
<td align="right">810,565</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,532,485</td>
<td align="right">2,240,553</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">140,312</td>
<td align="right">204,670</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">421,122</td>
<td align="right">614,210</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">284,854</td>
<td align="right">413,570</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,038,106</td>
<td align="right">2,939,715</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">291,355</td>
<td align="right">420,173</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">732,332</td>
<td align="right">1,054,223</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">297,233</td>
<td align="right">425,949</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,190,396</td>
<td align="right">1,705,503</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">450,147</td>
<td align="right">643,221</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">450,147</td>
<td align="right">643,221</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">150,811</td>
<td align="right">215,171</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">626,781</td>
<td align="right">884,358</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">4,389,388</td>
<td align="right">6,192,259</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">3,492,429</td>
<td align="right">4,909,206</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">3,492,429</td>
<td align="right">4,909,206</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,083,595</td>
<td align="right">4,307,083</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,502,936</td>
<td align="right">3,468,926</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">5,226,395</td>
<td align="right">7,222,367</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,214,458</td>
<td align="right">3,051,676</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">4,801,122</td>
<td align="right">6,604,006</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">7,425,516</td>
<td align="right">10,193,704</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">173,405</td>
<td align="right">237,823</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">4,174,341</td>
<td align="right">5,719,648</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,348,959</td>
<td align="right">5,958,309</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,646,430</td>
<td align="right">10,414,825</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,801,449</td>
<td align="right">2,445,377</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,675,821</td>
<td align="right">2,255,311</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,710,145</td>
<td align="right">2,289,816</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,899,983</td>
<td align="right">3,801,008</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,280,231</td>
<td align="right">1,665,696</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,093,103</td>
<td align="right">1,414,335</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,107,407</td>
<td align="right">1,429,422</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">11,404,347</td>
<td align="right">14,684,450</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,385,285</td>
<td align="right">4,350,938</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,061,270</td>
<td align="right">2,640,625</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,067,298</td>
<td align="right">2,646,818</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">9,784,074</td>
<td align="right">12,486,553</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">975,368</td>
<td align="right">1,232,839</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,080,983</td>
<td align="right">1,338,467</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">896,055</td>
<td align="right">1,089,330</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">7,735,173</td>
<td align="right">9,341,057</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">7,751,965</td>
<td align="right">9,357,842</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">9,871,635</td>
<td align="right">11,867,607</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">23,304,776</td>
<td align="right">27,874,072</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">32,570,908</td>
<td align="right">38,878,612</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,762,276</td>
<td align="right">3,277,322</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,384,766</td>
<td align="right">1,641,601</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">711,436</td>
<td align="right">840,338</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">711,442</td>
<td align="right">840,344</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,454,540</td>
<td align="right">1,712,274</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">9,509,998</td>
<td align="right">11,183,442</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">9,059,266</td>
<td align="right">10,604,184</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,707,780</td>
<td align="right">3,157,094</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,057,858</td>
<td align="right">3,508,465</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,756,380</td>
<td align="right">7,722,083</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,756,380</td>
<td align="right">7,722,083</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,364,941</td>
<td align="right">1,558,147</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,858,770</td>
<td align="right">2,115,732</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">552,004</td>
<td align="right">616,456</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">554,443</td>
<td align="right">618,901</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">16,153,476</td>
<td align="right">18,020,959</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">552,265</td>
<td align="right">616,091</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,115,211</td>
<td align="right">1,244,041</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">564,512</td>
<td align="right">628,872</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">564,571</td>
<td align="right">628,931</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">568,442</td>
<td align="right">632,090</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">568,442</td>
<td align="right">632,090</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">592,122</td>
<td align="right">656,800</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,412,527</td>
<td align="right">2,670,107</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,193,657</td>
<td align="right">9,030,711</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">629,082</td>
<td align="right">692,809</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">19,346,676</td>
<td align="right">21,276,120</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">22,281,673</td>
<td align="right">24,405,978</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">21,652,591</td>
<td align="right">23,713,169</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,752,644</td>
<td align="right">3,010,137</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,752,644</td>
<td align="right">3,010,137</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,460,219</td>
<td align="right">5,845,794</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">4,916,485</td>
<td align="right">5,238,416</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,394,521</td>
<td align="right">1,458,980</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,103,572</td>
<td align="right">6,361,256</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,482,245</td>
<td align="right">5,675,346</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,677,715</td>
<td align="right">2,742,174</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">411,458</td>
<td align="right">410,660</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">417,951</td>
<td align="right">417,153</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">16,421</td>
<td align="right">16,393</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">16,792</td>
<td align="right">16,785</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">16,870</td>
<td align="right">16,864</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">44,037</td>
<td align="right">44,041</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,645,240</td>
<td align="right">4,645,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">918,323</td>
<td align="right">918,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">829,765</td>
<td align="right">829,765</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">823,550</td>
<td align="right">823,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">819,293</td>
<td align="right">819,293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">422,270</td>
<td align="right">422,270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">411,776</td>
<td align="right">411,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">411,730</td>
<td align="right">411,730</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">411,726</td>
<td align="right">411,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">411,718</td>
<td align="right">411,718</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">61,094</td>
<td align="right">61,094</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">60,911</td>
<td align="right">60,911</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">60,907</td>
<td align="right">60,907</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">60,907</td>
<td align="right">60,907</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">60,907</td>
<td align="right">60,907</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">14,341</td>
<td align="right">14,341</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">11,921</td>
<td align="right">11,921</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">8,564</td>
<td align="right">8,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">8,564</td>
<td align="right">8,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">8,302</td>
<td align="right">8,302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,391</td>
<td align="right">6,391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,391</td>
<td align="right">6,391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">6,385</td>
<td align="right">6,385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,385</td>
<td align="right">6,385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,385</td>
<td align="right">6,385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">4,151</td>
<td align="right">4,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">4,151</td>
<td align="right">4,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">4,151</td>
<td align="right">4,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">4,151</td>
<td align="right">4,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,077</td>
<td align="right">4,077</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">191</td>
<td align="right">191</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">59</td>
<td align="right">59</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">59</td>
<td align="right">59</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">156</td>
<td align="right">156</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-18
