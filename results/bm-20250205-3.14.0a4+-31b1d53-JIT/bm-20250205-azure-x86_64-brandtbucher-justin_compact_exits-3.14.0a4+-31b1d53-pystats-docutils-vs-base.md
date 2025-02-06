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
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">18,604,320</td>
<td align="right">47,096,620</td>
<td align="right">153.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,313,660</td>
<td align="right">6,698,220</td>
<td align="right">102.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">54,819,620</td>
<td align="right">92,679,940</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">5,454,100</td>
<td align="right">2,978,460</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">27,569,660</td>
<td align="right">38,639,220</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">8,467,800</td>
<td align="right">11,673,180</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">23,497,300</td>
<td align="right">31,419,740</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">36,291,960</td>
<td align="right">48,362,600</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,695,620</td>
<td align="right">7,408,800</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">7,865,920</td>
<td align="right">9,983,260</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,006,200</td>
<td align="right">14,966,500</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">75,933,860</td>
<td align="right">94,207,840</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">93,499,520</td>
<td align="right">114,806,580</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">9,654,900</td>
<td align="right">11,839,300</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">26,479,800</td>
<td align="right">32,265,300</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,951,780</td>
<td align="right">21,655,060</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">104,201,880</td>
<td align="right">84,594,640</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">90,173,480</td>
<td align="right">106,188,600</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">8,739,020</td>
<td align="right">10,250,340</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">16,203,980</td>
<td align="right">18,739,700</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">37,647,280</td>
<td align="right">43,109,420</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">91,560</td>
<td align="right">104,600</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">17,972,380</td>
<td align="right">20,525,180</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,230,980</td>
<td align="right">5,967,920</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">7,035,220</td>
<td align="right">8,013,200</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">24,205,580</td>
<td align="right">27,555,260</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">234,904,740</td>
<td align="right">267,227,320</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">209,281,500</td>
<td align="right">236,990,180</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">314,931,780</td>
<td align="right">356,253,640</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,591,460</td>
<td align="right">11,963,520</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">50,230,920</td>
<td align="right">56,233,080</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">325,630,480</td>
<td align="right">364,291,700</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">78,767,900</td>
<td align="right">87,930,520</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">5,801,620</td>
<td align="right">6,422,460</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">121,409,040</td>
<td align="right">134,328,480</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">45,630,400</td>
<td align="right">50,159,760</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">20,433,400</td>
<td align="right">22,395,500</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">196,909,760</td>
<td align="right">215,579,780</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,626,600</td>
<td align="right">2,872,300</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33,429,160</td>
<td align="right">36,532,480</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,393,660</td>
<td align="right">14,593,840</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">172,837,360</td>
<td align="right">188,085,940</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">199,208,740</td>
<td align="right">216,135,420</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,374,215,100</td>
<td align="right">1,486,339,460</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">20,491,480</td>
<td align="right">22,105,440</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">48,952,000</td>
<td align="right">52,653,800</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">149,921,700</td>
<td align="right">160,626,880</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,789,500</td>
<td align="right">11,554,560</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,709,760</td>
<td align="right">16,748,260</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">47,440,120</td>
<td align="right">50,472,600</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">19,308,860</td>
<td align="right">20,508,700</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">120,034,700</td>
<td align="right">127,337,840</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">20,563,820</td>
<td align="right">21,787,480</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">294,183,740</td>
<td align="right">311,329,160</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">62,969,140</td>
<td align="right">66,514,760</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">77,632,020</td>
<td align="right">81,927,200</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">38,274,020</td>
<td align="right">40,346,680</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">102,619,220</td>
<td align="right">108,115,840</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">56,383,320</td>
<td align="right">59,142,860</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">17,706,580</td>
<td align="right">18,557,800</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,205,540</td>
<td align="right">1,149,200</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,906,240</td>
<td align="right">5,094,060</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">49,314,820</td>
<td align="right">51,149,160</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">7,742,940</td>
<td align="right">8,005,500</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">68,804,960</td>
<td align="right">70,756,220</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">304,867,140</td>
<td align="right">313,311,600</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">26,525,940</td>
<td align="right">27,205,140</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">38,531,300</td>
<td align="right">39,424,600</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">122,785,240</td>
<td align="right">125,262,280</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,630,920</td>
<td align="right">40,379,460</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,760,020</td>
<td align="right">2,810,720</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,423,400</td>
<td align="right">1,444,440</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,944,460</td>
<td align="right">92,923,160</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">27,579,860</td>
<td align="right">27,825,520</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,425,140</td>
<td align="right">3,454,720</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">174,043,980</td>
<td align="right">175,253,760</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">51,541,820</td>
<td align="right">51,850,680</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,458,460</td>
<td align="right">10,511,220</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">306,594,240</td>
<td align="right">307,745,140</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,539,060</td>
<td align="right">16,581,680</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">66,690,580</td>
<td align="right">66,813,980</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,898,840</td>
<td align="right">9,917,000</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,573,320</td>
<td align="right">38,629,660</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">19,401,480</td>
<td align="right">19,384,540</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">30,073,340</td>
<td align="right">30,047,600</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">30,074,720</td>
<td align="right">30,048,980</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,918,100</td>
<td align="right">2,916,180</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">22,885,340</td>
<td align="right">22,894,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,440,660</td>
<td align="right">5,438,720</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21,001,660</td>
<td align="right">20,998,880</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,362,640</td>
<td align="right">11,363,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,220,200</td>
<td align="right">3,220,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,114,500</td>
<td align="right">37,114,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">36,886,980</td>
<td align="right">36,886,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">15,100,320</td>
<td align="right">15,100,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">11,627,520</td>
<td align="right">11,627,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,619,980</td>
<td align="right">9,619,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,607,300</td>
<td align="right">8,607,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">7,613,400</td>
<td align="right">7,613,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,146,540</td>
<td align="right">7,146,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">6,143,580</td>
<td align="right">6,143,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">6,143,580</td>
<td align="right">6,143,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">5,787,480</td>
<td align="right">5,787,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,767,920</td>
<td align="right">5,767,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,325,060</td>
<td align="right">5,325,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,951,860</td>
<td align="right">4,951,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,587,740</td>
<td align="right">4,587,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,193,640</td>
<td align="right">4,193,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,944,720</td>
<td align="right">3,944,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,731,500</td>
<td align="right">2,731,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,728,440</td>
<td align="right">2,728,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,480,940</td>
<td align="right">2,480,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,925,660</td>
<td align="right">1,925,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,885,920</td>
<td align="right">1,885,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,693,560</td>
<td align="right">1,693,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,413,900</td>
<td align="right">1,413,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,175,460</td>
<td align="right">1,175,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">853,740</td>
<td align="right">853,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">840,600</td>
<td align="right">840,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">759,480</td>
<td align="right">759,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">740,040</td>
<td align="right">740,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">672,120</td>
<td align="right">672,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">440,340</td>
<td align="right">440,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">361,260</td>
<td align="right">361,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">332,160</td>
<td align="right">332,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">267,120</td>
<td align="right">267,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">230,880</td>
<td align="right">230,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">228,720</td>
<td align="right">228,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">176,880</td>
<td align="right">176,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">156,900</td>
<td align="right">156,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">145,320</td>
<td align="right">145,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">82,320</td>
<td align="right">82,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">75,960</td>
<td align="right">75,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">73,620</td>
<td align="right">73,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">61,740</td>
<td align="right">61,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">61,560</td>
<td align="right">61,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">49,980</td>
<td align="right">49,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">41,280</td>
<td align="right">41,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">27,480</td>
<td align="right">27,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">16,860</td>
<td align="right">16,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">14,700</td>
<td align="right">14,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">14,640</td>
<td align="right">14,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,400</td>
<td align="right">11,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">7,260</td>
<td align="right">7,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">4,740</td>
<td align="right">4,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,960</td>
<td align="right">3,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,420</td>
<td align="right">3,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">3,360</td>
<td align="right">3,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,940</td>
<td align="right">1,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">780</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
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
<td align="right">20,989,680</td>
<td align="right">30.2%</td>
<td align="right">20,986,900</td>
<td align="right">30.2%</td>
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
<td align="right">48,555,780</td>
<td align="right">69.8%</td>
<td align="right">48,555,780</td>
<td align="right">69.8%</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">200</td>
<td align="right">1.7%</td>
<td align="right">200</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">11,780</td>
<td align="right">98.3%</td>
<td align="right">11,780</td>
<td align="right">98.3%</td>
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
<td align="right">4,980</td>
<td align="right">42.3%</td>
<td align="right">4,980</td>
<td align="right">42.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,200</td>
<td align="right">27.2%</td>
<td align="right">3,200</td>
<td align="right">27.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">26.8%</td>
<td align="right">3,160</td>
<td align="right">26.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">240</td>
<td align="right">2.0%</td>
<td align="right">240</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">180</td>
<td align="right">1.5%</td>
<td align="right">180</td>
<td align="right">1.5%</td>
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
<td align="right">10,789,500</td>
<td align="right">100.0%</td>
<td align="right">11,554,560</td>
<td align="right">100.0%</td>
<td align="right">7.1%</td>
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
<td align="right">10,446,700</td>
<td align="right">9.8%</td>
<td align="right">10,499,660</td>
<td align="right">9.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,164,100</td>
<td align="right">2.0%</td>
<td align="right">2,166,940</td>
<td align="right">2.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">93,971,400</td>
<td align="right">88.2%</td>
<td align="right">93,970,320</td>
<td align="right">88.1%</td>
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
<td align="right">11,140</td>
<td align="right">21.2%</td>
<td align="right">10,940</td>
<td align="right">20.9%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,400</td>
<td align="right">78.8%</td>
<td align="right">41,460</td>
<td align="right">79.1%</td>
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
<td align="left">out of range</td>
<td align="right">7,820</td>
<td align="right">70.2%</td>
<td align="right">7,600</td>
<td align="right">69.5%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,740</td>
<td align="right">15.6%</td>
<td align="right">1,760</td>
<td align="right">16.1%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">720</td>
<td align="right">6.5%</td>
<td align="right">720</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">680</td>
<td align="right">6.1%</td>
<td align="right">680</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">1.6%</td>
<td align="right">180</td>
<td align="right">1.6%</td>
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
<td align="right">17,620,680</td>
<td align="right">3.1%</td>
<td align="right">17,768,800</td>
<td align="right">3.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,288,400</td>
<td align="right">3.0%</td>
<td align="right">17,433,700</td>
<td align="right">3.1%</td>
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
<td align="right">553,361,880</td>
<td align="right">96.9%</td>
<td align="right">553,201,900</td>
<td align="right">96.9%</td>
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
<td align="right">336,240</td>
<td align="right">100.0%</td>
<td align="right">339,060</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
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
<td align="right">160</td>
<td align="right">160 / 0 !!</td>
<td align="right">160</td>
<td align="right">160 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
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
<td align="right">300</td>
<td align="right">100.0%</td>
<td align="right">300</td>
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
<td align="right">1,680,260</td>
<td align="right">4.6%</td>
<td align="right">1,680,260</td>
<td align="right">4.6%</td>
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
<td align="right">34,787,600</td>
<td align="right">94.7%</td>
<td align="right">34,787,600</td>
<td align="right">94.7%</td>
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
<td align="right">259,420</td>
<td align="right">0.7%</td>
<td align="right">259,420</td>
<td align="right">0.7%</td>
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
<td align="right">5,220</td>
<td align="right">28.7%</td>
<td align="right">5,220</td>
<td align="right">28.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">12,960</td>
<td align="right">71.3%</td>
<td align="right">12,960</td>
<td align="right">71.3%</td>
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
<td align="left">different types</td>
<td align="right">12,500</td>
<td align="right">96.5%</td>
<td align="right">12,500</td>
<td align="right">96.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
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
<td align="right">8,734,180</td>
<td align="right">13.8%</td>
<td align="right">10,245,140</td>
<td align="right">15.9%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">54,350,400</td>
<td align="right">86.1%</td>
<td align="right">54,350,400</td>
<td align="right">84.1%</td>
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
<td align="right">4,720</td>
<td align="right">97.5%</td>
<td align="right">5,080</td>
<td align="right">97.7%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">2.5%</td>
<td align="right">120</td>
<td align="right">2.3%</td>
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
<td align="left">str</td>
<td align="right">860</td>
<td align="right">18.2%</td>
<td align="right">1,080</td>
<td align="right">21.3%</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,180</td>
<td align="right">25.0%</td>
<td align="right">1,260</td>
<td align="right">24.8%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,880</td>
<td align="right">39.8%</td>
<td align="right">1,940</td>
<td align="right">38.2%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">16.9%</td>
<td align="right">800</td>
<td align="right">15.7%</td>
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
<td align="right">23,490,760</td>
<td align="right">13.0%</td>
<td align="right">31,411,260</td>
<td align="right">14.4%</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">130,117,100</td>
<td align="right">72.3%</td>
<td align="right">157,751,380</td>
<td align="right">72.2%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">26,435,140</td>
<td align="right">14.7%</td>
<td align="right">29,391,180</td>
<td align="right">13.4%</td>
<td align="right">11.2%</td>
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
<td align="right">6,540</td>
<td align="right">1.3%</td>
<td align="right">8,480</td>
<td align="right">1.5%</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">498,760</td>
<td align="right">98.7%</td>
<td align="right">554,540</td>
<td align="right">98.5%</td>
<td align="right">11.2%</td>
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
<td align="right">560</td>
<td align="right">8.6%</td>
<td align="right">1,020</td>
<td align="right">12.0%</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,020</td>
<td align="right">15.6%</td>
<td align="right">1,740</td>
<td align="right">20.5%</td>
<td align="right">70.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,460</td>
<td align="right">22.3%</td>
<td align="right">1,980</td>
<td align="right">23.3%</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">400</td>
<td align="right">6.1%</td>
<td align="right">460</td>
<td align="right">5.4%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,160</td>
<td align="right">33.0%</td>
<td align="right">2,340</td>
<td align="right">27.6%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">560</td>
<td align="right">8.6%</td>
<td align="right">560</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">220</td>
<td align="right">3.4%</td>
<td align="right">220</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
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
<td align="right">278,871,540</td>
<td align="right">26.8%</td>
<td align="right">320,383,040</td>
<td align="right">29.4%</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">101,961,320</td>
<td align="right">9.8%</td>
<td align="right">107,451,940</td>
<td align="right">9.9%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">660,365,900</td>
<td align="right">63.4%</td>
<td align="right">659,741,880</td>
<td align="right">60.6%</td>
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
<td align="right">5,203,120</td>
<td align="right">99.6%</td>
<td align="right">5,986,080</td>
<td align="right">99.6%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">21,140</td>
<td align="right">0.4%</td>
<td align="right">22,420</td>
<td align="right">0.4%</td>
<td align="right">6.1%</td>
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
<td align="right">9,820</td>
<td align="right">46.5%</td>
<td align="right">10,840</td>
<td align="right">48.3%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,140</td>
<td align="right">24.3%</td>
<td align="right">5,400</td>
<td align="right">24.1%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2,840</td>
<td align="right">13.4%</td>
<td align="right">2,840</td>
<td align="right">12.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">640</td>
<td align="right">3.0%</td>
<td align="right">640</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">2.0%</td>
<td align="right">420</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">1.9%</td>
<td align="right">400</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">240</td>
<td align="right">1.1%</td>
<td align="right">240</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">180</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
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
<td align="right">276,838,620</td>
<td align="right">100.0%</td>
<td align="right">298,060,480</td>
<td align="right">100.0%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,140</td>
<td align="right">0.0%</td>
<td align="right">2,140</td>
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
<td align="right">1,980</td>
<td align="right">100.0%</td>
<td align="right">1,980</td>
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
<td align="right">75,960</td>
<td align="right">100.0%</td>
<td align="right">75,960</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">7,260</td>
<td align="right">100.0%</td>
<td align="right">7,260</td>
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
<td align="right">20,478,500</td>
<td align="right">16.9%</td>
<td align="right">22,092,060</td>
<td align="right">18.0%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,039,540</td>
<td align="right">38.7%</td>
<td align="right">47,039,540</td>
<td align="right">38.2%</td>
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
<td align="right">53,915,360</td>
<td align="right">44.4%</td>
<td align="right">53,915,360</td>
<td align="right">43.8%</td>
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
<td align="right">12,580</td>
<td align="right">1.2%</td>
<td align="right">12,980</td>
<td align="right">1.3%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,017,800</td>
<td align="right">98.8%</td>
<td align="right">1,017,800</td>
<td align="right">98.7%</td>
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
<td align="left">class attr simple</td>
<td align="right">9,940</td>
<td align="right">79.0%</td>
<td align="right">10,340</td>
<td align="right">79.7%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">16.2%</td>
<td align="right">2,040</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,000</td>
<td align="right">7.9%</td>
<td align="right">1,000</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">320</td>
<td align="right">2.5%</td>
<td align="right">320</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
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
<td align="right">267,120</td>
<td align="right">100.0%</td>
<td align="right">267,120</td>
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
<td align="right">4,583,860</td>
<td align="right">9.7%</td>
<td align="right">4,583,860</td>
<td align="right">9.7%</td>
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
<td align="right">42,562,200</td>
<td align="right">90.3%</td>
<td align="right">42,562,200</td>
<td align="right">90.3%</td>
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
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,760</td>
<td align="right">95.9%</td>
<td align="right">3,760</td>
<td align="right">95.9%</td>
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
<td align="right">2,440</td>
<td align="right">64.9%</td>
<td align="right">2,440</td>
<td align="right">64.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">220</td>
<td align="right">5.9%</td>
<td align="right">220</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right">40</td>
<td align="right">1.1%</td>
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
<td align="right">10,174,720</td>
<td align="right">3.6%</td>
<td align="right">10,670,060</td>
<td align="right">3.8%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">269,120,240</td>
<td align="right">95.0%</td>
<td align="right">268,880,100</td>
<td align="right">94.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,776,840</td>
<td align="right">1.3%</td>
<td align="right">3,776,840</td>
<td align="right">1.3%</td>
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
<td align="right">192,820</td>
<td align="right">53.6%</td>
<td align="right">202,140</td>
<td align="right">54.8%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">167,000</td>
<td align="right">46.4%</td>
<td align="right">167,000</td>
<td align="right">45.2%</td>
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
<td align="left">number</td>
<td align="right">121,740</td>
<td align="right">72.9%</td>
<td align="right">121,740</td>
<td align="right">72.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">41,540</td>
<td align="right">24.9%</td>
<td align="right">41,540</td>
<td align="right">24.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,360</td>
<td align="right">1.4%</td>
<td align="right">2,360</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,200</td>
<td align="right">0.7%</td>
<td align="right">1,200</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">48,290,020</td>
<td align="right">100.0%</td>
<td align="right">48,290,020</td>
<td align="right">100.0%</td>
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
<td align="left">Success</td>
<td align="right">380</td>
<td align="right">100.0%</td>
<td align="right">380</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">389,455,720</td>
<td align="right">5.5%</td>
<td align="right">434,570,660</td>
<td align="right">5.7%</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">2,743,512,220</td>
<td align="right">38.8%</td>
<td align="right">3,021,285,060</td>
<td align="right">39.4%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">208,096,280</td>
<td align="right">2.9%</td>
<td align="right">225,455,660</td>
<td align="right">2.9%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,726,311,860</td>
<td align="right">52.7%</td>
<td align="right">3,991,684,120</td>
<td align="right">52.0%</td>
<td align="right">7.1%</td>
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
<td align="right">23,490,760</td>
<td align="right">10.5%</td>
<td align="right">31,411,260</td>
<td align="right">13.0%</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">8,734,180</td>
<td align="right">3.9%</td>
<td align="right">10,245,140</td>
<td align="right">4.2%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">20,478,500</td>
<td align="right">9.1%</td>
<td align="right">22,092,060</td>
<td align="right">9.1%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,789,500</td>
<td align="right">4.8%</td>
<td align="right">11,554,560</td>
<td align="right">4.8%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">101,961,320</td>
<td align="right">45.4%</td>
<td align="right">107,451,940</td>
<td align="right">44.4%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,288,400</td>
<td align="right">7.7%</td>
<td align="right">17,433,700</td>
<td align="right">7.2%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,446,700</td>
<td align="right">4.7%</td>
<td align="right">10,499,660</td>
<td align="right">4.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20,989,680</td>
<td align="right">9.4%</td>
<td align="right">20,986,900</td>
<td align="right">8.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,583,860</td>
<td align="right">2.0%</td>
<td align="right">4,583,860</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,776,840</td>
<td align="right">1.7%</td>
<td align="right">3,776,840</td>
<td align="right">1.6%</td>
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
<td align="right">103,334,140</td>
<td align="right">26.5%</td>
<td align="right">125,990,400</td>
<td align="right">29.0%</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">83,536,360</td>
<td align="right">21.4%</td>
<td align="right">97,294,940</td>
<td align="right">22.4%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">13,217,800</td>
<td align="right">3.4%</td>
<td align="right">14,696,200</td>
<td align="right">3.4%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,217,340</td>
<td align="right">3.4%</td>
<td align="right">14,694,980</td>
<td align="right">3.4%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">31,957,560</td>
<td align="right">8.2%</td>
<td align="right">34,942,320</td>
<td align="right">8.0%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,547,560</td>
<td align="right">1.4%</td>
<td align="right">5,795,920</td>
<td align="right">1.3%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">49,825,900</td>
<td align="right">12.8%</td>
<td align="right">51,377,060</td>
<td align="right">11.8%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,582,520</td>
<td align="right">2.5%</td>
<td align="right">9,657,320</td>
<td align="right">2.2%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,912,180</td>
<td align="right">13.8%</td>
<td align="right">53,912,180</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,565,220</td>
<td align="right">1.9%</td>
<td align="right">7,565,220</td>
<td align="right">1.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,304,420</td>
<td align="right">11.1%</td>
<td align="right">39,360,760</td>
<td align="right">11.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,307,900</td>
<td align="right">11.1%</td>
<td align="right">39,364,240</td>
<td align="right">11.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,615,760</td>
<td align="right">11.2%</td>
<td align="right">39,672,100</td>
<td align="right">11.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,615,760</td>
<td align="right">11.2%</td>
<td align="right">39,672,100</td>
<td align="right">11.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,610,420</td>
<td align="right">88.5%</td>
<td align="right">313,554,080</td>
<td align="right">88.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">314,804,060</td>
<td align="right">88.8%</td>
<td align="right">314,747,720</td>
<td align="right">88.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">307,860</td>
<td align="right">0.1%</td>
<td align="right">307,860</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,420</td>
<td align="right">0.0%</td>
<td align="right">3,420</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">13,631,100</td>
<td align="right">3.8%</td>
<td align="right">13,631,100</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,826,760</td>
<td align="right">0.5%</td>
<td align="right">1,826,760</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">8,426,280</td>
<td align="right">2.4%</td>
<td align="right">8,426,280</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">9,607,200</td>
<td align="right">2.7%</td>
<td align="right">9,607,200</td>
<td align="right">2.7%</td>
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
<td align="right">2,485,406</td>
<td align="right"></td>
<td align="right">3,135,282</td>
<td align="right"></td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,474,567,760</td>
<td align="right">27.5%</td>
<td align="right">2,043,898,471</td>
<td align="right">23.4%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,696,420,948</td>
<td align="right">33.7%</td>
<td align="right">2,289,088,467</td>
<td align="right">29.5%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">715,885,900</td>
<td align="right">9.0%</td>
<td align="right">818,741,440</td>
<td align="right">10.5%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,092,094,660</td>
<td align="right">12.1%</td>
<td align="right">1,197,530,440</td>
<td align="right">13.7%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,695,725,534</td>
<td align="right">18.9%</td>
<td align="right">1,571,730,717</td>
<td align="right">18.0%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,914,672,460</td>
<td align="right">36.5%</td>
<td align="right">3,087,354,080</td>
<td align="right">39.7%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,668,195,178</td>
<td align="right">20.9%</td>
<td align="right">1,573,352,632</td>
<td align="right">20.3%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,726,971,320</td>
<td align="right">41.5%</td>
<td align="right">3,922,993,580</td>
<td align="right">44.9%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">500,140</td>
<td align="right">0.1%</td>
<td align="right">513,360</td>
<td align="right">0.1%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">41,471,406</td>
<td align="right"></td>
<td align="right">42,104,309</td>
<td align="right"></td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">344,680</td>
<td align="right">0.1%</td>
<td align="right">346,700</td>
<td align="right">0.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">196,100,354</td>
<td align="right"></td>
<td align="right">197,201,958</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">451,373,967</td>
<td align="right"></td>
<td align="right">453,702,717</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">39,747,433</td>
<td align="right"></td>
<td align="right">39,730,363</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">317,629,040</td>
<td align="right">47.1%</td>
<td align="right">317,724,640</td>
<td align="right">47.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">316,784,220</td>
<td align="right">47.0%</td>
<td align="right">316,864,580</td>
<td align="right">47.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">353,912,504</td>
<td align="right"></td>
<td align="right">353,973,963</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">356,652,720</td>
<td align="right">52.9%</td>
<td align="right">356,663,880</td>
<td align="right">52.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">356,656,380</td>
<td align="right"></td>
<td align="right">356,654,340</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">10,534,200</td>
<td align="right"></td>
<td align="right">10,534,200</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">26,460</td>
<td align="right">0.3%</td>
<td align="right">26,460</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">119,040</td>
<td align="right">1.1%</td>
<td align="right">119,040</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
<td align="right">2,940</td>
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
<td align="right">25,940</td>
<td align="right">73,080,840</td>
<td align="right">1,149,961,967</td>
<td align="right">44,663,460</td>
<td align="right">100,213,160</td>
<td align="right">25,980</td>
<td align="right">73,056,780</td>
<td align="right">1,157,515,585</td>
<td align="right">44,554,840</td>
<td align="right">100,508,600</td>
</tr>
<tr>
<td align="right">2</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">10,720</td>
<td align="right">33.3%</td>
<td align="right">1,820</td>
<td align="right">5.8%</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">340</td>
<td align="right">1.1%</td>
<td align="right">600</td>
<td align="right">1.9%</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">12,660</td>
<td align="right">39.3%</td>
<td align="right">2,980</td>
<td align="right">9.4%</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">309,297,640</td>
<td align="right"></td>
<td align="right">88,921,720</td>
<td align="right"></td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">200</td>
<td align="right">0.6%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">2,540</td>
<td align="right">7.9%</td>
<td align="right">3,740</td>
<td align="right">11.8%</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,377,042,880</td>
<td align="right">1,415.2%</td>
<td align="right">2,310,236,100</td>
<td align="right">2,598.1%</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">21,260</td>
<td align="right">66.1%</td>
<td align="right">29,600</td>
<td align="right">93.6%</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">200</td>
<td align="right">0.6%</td>
<td align="right">220</td>
<td align="right">0.7%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">32,180</td>
<td align="right"></td>
<td align="right">31,640</td>
<td align="right"></td>
<td align="right">-1.7%</td>
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
<td align="right">15,320</td>
<td align="right">72.1%</td>
<td align="right">24,520</td>
<td align="right">82.8%</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">21,260</td>
<td align="right"></td>
<td align="right">29,600</td>
<td align="right"></td>
<td align="right">39.2%</td>
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

### JIT memory stats

<details>
<summary> JIT memory stats </summary>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Base Size (bytes)</th>
<th align="right">Base Ratio</th>
<th align="right">Head Size (bytes)</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">18,301,120</td>
<td align="right">11.5%</td>
<td align="right">45,012,480</td>
<td align="right">12.1%</td>
<td align="right">146.0%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">108,410,220</td>
<td align="right">67.9%</td>
<td align="right">264,530,500</td>
<td align="right">71.2%</td>
<td align="right">144.0%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">158,105,600</td>
<td align="right">99.1%</td>
<td align="right">371,589,120</td>
<td align="right">100.0%</td>
<td align="right">135.0%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">159,580,160</td>
<td align="right"></td>
<td align="right">371,425,280</td>
<td align="right"></td>
<td align="right">132.8%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">32,868,820</td>
<td align="right">20.6%</td>
<td align="right">61,882,300</td>
<td align="right">16.7%</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">
Trampoline size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the trampolines of the JIT traces
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


</details>

### JIT trace total memory histogram

<details>
<summary> JIT trace total memory histogram </summary>

<table>
<thead>
<tr>
<th align="left">Size (bytes)</th>
<th align="left">Base Count</th>
<th align="right">Base Ratio</th>
<th align="left">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 4,096</td>
<td align="left">2,840</td>
<td align="right">18.5%</td>
<td align="left">3,600</td>
<td align="right">11.7%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">7,700</td>
<td align="right">50.3%</td>
<td align="left">14,680</td>
<td align="right">47.8%</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">3,540</td>
<td align="right">23.1%</td>
<td align="left">8,060</td>
<td align="right">26.2%</td>
<td align="right">127.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">820</td>
<td align="right">5.4%</td>
<td align="left">3,540</td>
<td align="right">11.5%</td>
<td align="right">331.7%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">380</td>
<td align="right">2.5%</td>
<td align="left">820</td>
<td align="right">2.7%</td>
<td align="right">115.8%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">40</td>
<td align="right">0.3%</td>
<td align="left">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

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
<td align="left"><= 8</td>
<td align="right">940</td>
<td align="right">4.4%</td>
<td align="right">1,180</td>
<td align="right">4.0%</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,440</td>
<td align="right">6.8%</td>
<td align="right">2,020</td>
<td align="right">6.8%</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,100</td>
<td align="right">33.4%</td>
<td align="right">12,280</td>
<td align="right">41.5%</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">4,860</td>
<td align="right">22.9%</td>
<td align="right">6,320</td>
<td align="right">21.4%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,660</td>
<td align="right">17.2%</td>
<td align="right">3,580</td>
<td align="right">12.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,960</td>
<td align="right">13.9%</td>
<td align="right">3,960</td>
<td align="right">13.4%</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">280</td>
<td align="right">1.3%</td>
<td align="right">240</td>
<td align="right">0.8%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
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
<td align="left"><= 4</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,960</td>
<td align="right">9.2%</td>
<td align="right">2,160</td>
<td align="right">7.3%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,540</td>
<td align="right">11.9%</td>
<td align="right">3,140</td>
<td align="right">10.6%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">6,600</td>
<td align="right">31.0%</td>
<td align="right">13,160</td>
<td align="right">44.5%</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">3,160</td>
<td align="right">14.9%</td>
<td align="right">4,680</td>
<td align="right">15.8%</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">860</td>
<td align="right">4.0%</td>
<td align="right">1,220</td>
<td align="right">4.1%</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">140</td>
<td align="right">0.7%</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>


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
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">200</td>
<td align="right">2,140</td>
<td align="right">970.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">36,060</td>
<td align="right">220</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,540,600</td>
<td align="right">63,560</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">13,420</td>
<td align="right">380</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,559,060</td>
<td align="right">130,540</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">45,061,560</td>
<td align="right">2,002,440</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">22,720</td>
<td align="right">1,680</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">22,720</td>
<td align="right">1,680</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,784,420</td>
<td align="right">359,660</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">59,680</td>
<td align="right">5,020</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,365,280</td>
<td align="right">399,420</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,339,520</td>
<td align="right">379,220</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">2,643,400</td>
<td align="right">346,000</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">50,160</td>
<td align="right">7,540</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,348,320</td>
<td align="right">508,380</td>
<td align="right">-84.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">36,740</td>
<td align="right">7,160</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,246,680</td>
<td align="right">449,040</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">35,684,340</td>
<td align="right">7,192,040</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">14,154,160</td>
<td align="right">3,084,600</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">3,919,600</td>
<td align="right">887,120</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">4,035,200</td>
<td align="right">931,880</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">18,624,740</td>
<td align="right">4,343,300</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">23,724,840</td>
<td align="right">5,701,980</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">4,200</td>
<td align="right">1,080</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">4,783,100</td>
<td align="right">1,237,480</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">1,184,400</td>
<td align="right">310,080</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">1,329,980</td>
<td align="right">351,280</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">1,329,020</td>
<td align="right">351,040</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,450,960</td>
<td align="right">412,460</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">302,232,240</td>
<td align="right">86,338,260</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">309,297,640</td>
<td align="right">88,921,720</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">44,101,160</td>
<td align="right">12,761,480</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">21,350,540</td>
<td align="right">6,205,160</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">70,220</td>
<td align="right">20,600</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">1,391,160</td>
<td align="right">412,460</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,391,160</td>
<td align="right">412,460</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">1,506,200</td>
<td align="right">446,800</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">26,500,160</td>
<td align="right">8,202,700</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">27,029,260</td>
<td align="right">8,433,520</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,606,060</td>
<td align="right">818,500</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">364,340</td>
<td align="right">114,880</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">22,562,640</td>
<td align="right">7,298,920</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,786,220</td>
<td align="right">586,040</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">29,968,300</td>
<td align="right">9,894,700</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">932,520</td>
<td align="right">311,620</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,204,080</td>
<td align="right">1,131,420</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,167,280</td>
<td align="right">795,220</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">65,785,120</td>
<td align="right">24,529,580</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">2,231,120</td>
<td align="right">876,000</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,431,080</td>
<td align="right">579,860</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">18,344,780</td>
<td align="right">7,641,800</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,315,200</td>
<td align="right">550,140</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">15,781,420</td>
<td align="right">6,618,800</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">38,392,980</td>
<td align="right">17,275,600</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,233,420</td>
<td align="right">1,009,760</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">3,970,840</td>
<td align="right">1,820,920</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,667,580</td>
<td align="right">1,705,480</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">3,626,280</td>
<td align="right">1,687,320</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">39,277,600</td>
<td align="right">19,110,200</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,251,500</td>
<td align="right">610,780</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">7,875,780</td>
<td align="right">3,859,800</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,945,380</td>
<td align="right">973,200</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,393,200</td>
<td align="right">2,208,800</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">9,733,780</td>
<td align="right">4,916,080</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">113,812,800</td>
<td align="right">57,531,600</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">34,183,280</td>
<td align="right">17,290,360</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">26,176,960</td>
<td align="right">13,274,100</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">42,778,420</td>
<td align="right">22,893,220</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">85,011,460</td>
<td align="right">45,637,080</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">38,776,160</td>
<td align="right">21,402,820</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">347,873,600</td>
<td align="right">192,060,860</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">15,466,040</td>
<td align="right">8,583,160</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">43,968,240</td>
<td align="right">24,536,800</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">43,968,240</td>
<td align="right">24,536,800</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">3,716,880</td>
<td align="right">2,074,860</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">229,195,980</td>
<td align="right">128,365,480</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,673,780</td>
<td align="right">8,800,420</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">3,020</td>
<td align="right">1,700</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">3,464,900</td>
<td align="right">1,953,940</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,570,380</td>
<td align="right">891,180</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">12,721,880</td>
<td align="right">7,259,740</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">79,554,900</td>
<td align="right">45,600,340</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">35,068,360</td>
<td align="right">20,126,080</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">64,187,700</td>
<td align="right">37,098,660</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">576,954,200</td>
<td align="right">333,838,300</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">433,571,860</td>
<td align="right">257,546,440</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,979,420</td>
<td align="right">1,779,580</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">23,120,000</td>
<td align="right">13,897,020</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">14,436,780</td>
<td align="right">8,834,800</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">27,135,700</td>
<td align="right">17,015,240</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">16,166,060</td>
<td align="right">10,211,880</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">2,068,900</td>
<td align="right">1,320,360</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">3,403,400</td>
<td align="right">2,196,160</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">32,565,220</td>
<td align="right">21,020,660</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,495,720</td>
<td align="right">8,134,120</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">21,151,260</td>
<td align="right">13,819,020</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">9,811,840</td>
<td align="right">6,462,160</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">9,811,840</td>
<td align="right">6,462,160</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">9,788,780</td>
<td align="right">6,464,320</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">24,652,420</td>
<td align="right">16,308,740</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">918,600</td>
<td align="right">609,740</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">918,600</td>
<td align="right">609,740</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">9,560,620</td>
<td align="right">6,355,240</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">10,365,100</td>
<td align="right">6,919,700</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">9,404,640</td>
<td align="right">6,282,120</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">10,415,240</td>
<td align="right">6,971,760</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">814,560</td>
<td align="right">569,100</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">841,220</td>
<td align="right">595,520</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">841,220</td>
<td align="right">595,520</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">194,775,220</td>
<td align="right">138,877,860</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">33,540,880</td>
<td align="right">24,557,320</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">41,912,580</td>
<td align="right">30,964,500</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">14,168,300</td>
<td align="right">10,783,740</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">13,881,400</td>
<td align="right">10,670,240</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">39,560</td>
<td align="right">30,800</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">38,575,960</td>
<td align="right">30,330,480</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">12,187,940</td>
<td align="right">9,635,140</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">32,449,860</td>
<td align="right">25,791,120</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">94,062,280</td>
<td align="right">75,504,680</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">88,954,600</td>
<td align="right">71,512,800</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">134,560</td>
<td align="right">160,300</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">134,560</td>
<td align="right">160,300</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">59,399,640</td>
<td align="right">48,103,160</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">9,804,080</td>
<td align="right">7,969,740</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">16,080</td>
<td align="right">18,860</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">12,347,180</td>
<td align="right">10,229,840</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">11,285,800</td>
<td align="right">9,570,460</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,066,320</td>
<td align="right">1,820,660</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">1,000</td>
<td align="right">1,100</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">400</td>
<td align="right">440</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">400</td>
<td align="right">440</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">200</td>
<td align="right">220</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">200</td>
<td align="right">220</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">200</td>
<td align="right">220</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">8,386,600</td>
<td align="right">7,560,540</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">240</td>
<td align="right">260</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">240</td>
<td align="right">260</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,103,680</td>
<td align="right">1,024,920</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">17,720</td>
<td align="right">16,460</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">90,040</td>
<td align="right">85,020</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">651,440</td>
<td align="right">623,660</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">255,620</td>
<td align="right">246,860</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">262,940</td>
<td align="right">265,200</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,613,560</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">116,700</td>
<td align="right">116,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">82,380</td>
<td align="right">82,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">82,380</td>
<td align="right">82,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">63,840</td>
<td align="right">63,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">47,760</td>
<td align="right">47,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">15,920</td>
<td align="right">15,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,660</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">16,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">1,920</td>
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
<td align="right">1,220</td>
<td align="right">1,660</td>
<td align="right">36.1%</td>
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
Stats gathered on: 2025-02-06
