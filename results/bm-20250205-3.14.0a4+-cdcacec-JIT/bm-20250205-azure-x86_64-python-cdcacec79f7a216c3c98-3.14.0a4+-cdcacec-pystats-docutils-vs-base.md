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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">207,820,080</td>
<td align="right">41,280</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">17,481,960</td>
<td align="right">3,313,660</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">16,979,260</td>
<td align="right">5,695,620</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">54,288,660</td>
<td align="right">18,604,320</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">14,345,700</td>
<td align="right">5,230,980</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">20,213,100</td>
<td align="right">7,865,920</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">165,799,300</td>
<td align="right">75,933,860</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">18,028,420</td>
<td align="right">8,467,800</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">45,320,200</td>
<td align="right">23,497,300</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">69,462,800</td>
<td align="right">36,291,960</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">48,258,120</td>
<td align="right">26,479,800</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">28,877,420</td>
<td align="right">16,203,980</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">30,160,320</td>
<td align="right">17,972,380</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">41,723,820</td>
<td align="right">27,569,660</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">14,048,100</td>
<td align="right">9,654,900</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">135,576,840</td>
<td align="right">93,499,520</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">34,017,420</td>
<td align="right">24,205,580</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">12,204,760</td>
<td align="right">8,739,020</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">68,757,240</td>
<td align="right">50,230,920</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">441,064,440</td>
<td align="right">325,630,480</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">50,369,160</td>
<td align="right">37,647,280</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">3,467,820</td>
<td align="right">2,626,600</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">118,686,060</td>
<td align="right">90,173,480</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">15,345,720</td>
<td align="right">12,006,200</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">58,019,820</td>
<td align="right">45,630,400</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">296,151,840</td>
<td align="right">234,904,740</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">22,014,720</td>
<td align="right">17,951,780</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">147,614,400</td>
<td align="right">121,409,040</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">380,939,380</td>
<td align="right">314,931,780</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">12,758,740</td>
<td align="right">10,591,460</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">251,712,240</td>
<td align="right">209,281,500</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">93,314,960</td>
<td align="right">77,632,020</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">94,549,320</td>
<td align="right">78,767,900</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">59,118,900</td>
<td align="right">49,314,820</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">8,364,240</td>
<td align="right">7,035,220</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">24,100,980</td>
<td align="right">20,433,400</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,600,827,600</td>
<td align="right">1,374,215,100</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">6,734,080</td>
<td align="right">5,801,620</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">22,288,280</td>
<td align="right">19,308,860</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">65,011,020</td>
<td align="right">56,383,320</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">104,980</td>
<td align="right">91,560</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">223,772,120</td>
<td align="right">196,909,760</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">225,990,500</td>
<td align="right">199,208,740</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">15,179,580</td>
<td align="right">13,393,660</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">195,401,800</td>
<td align="right">172,837,360</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">169,002,140</td>
<td align="right">149,921,700</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,104,700</td>
<td align="right">10,789,500</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">37,464,360</td>
<td align="right">33,429,160</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">328,424,880</td>
<td align="right">294,183,740</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">822,420</td>
<td align="right">740,040</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">22,797,240</td>
<td align="right">20,563,820</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">936,120</td>
<td align="right">853,740</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">17,160,720</td>
<td align="right">15,709,760</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">130,778,280</td>
<td align="right">120,034,700</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">823,320</td>
<td align="right">759,480</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">41,478,100</td>
<td align="right">38,274,020</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">53,006,580</td>
<td align="right">48,952,000</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">51,359,920</td>
<td align="right">47,440,120</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">19,137,660</td>
<td align="right">17,706,580</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">22,105,440</td>
<td align="right">20,491,480</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,126,000</td>
<td align="right">1,205,540</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">67,752,240</td>
<td align="right">62,969,140</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">29,646,180</td>
<td align="right">27,579,860</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">110,128,660</td>
<td align="right">102,619,220</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">28,096,320</td>
<td align="right">26,525,940</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">41,699,820</td>
<td align="right">39,630,920</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">5,146,200</td>
<td align="right">4,906,240</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">8,105,400</td>
<td align="right">7,742,940</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">40,151,340</td>
<td align="right">38,531,300</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">317,301,900</td>
<td align="right">304,867,140</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">71,196,700</td>
<td align="right">68,804,960</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,831,780</td>
<td align="right">2,760,020</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">125,325,840</td>
<td align="right">122,785,240</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">52,458,180</td>
<td align="right">51,541,820</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,446,120</td>
<td align="right">1,423,400</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,335,600</td>
<td align="right">91,944,460</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">309,918,100</td>
<td align="right">306,594,240</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,461,880</td>
<td align="right">3,425,140</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">175,819,840</td>
<td align="right">174,043,980</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">67,154,280</td>
<td align="right">66,690,580</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,655,060</td>
<td align="right">8,607,300</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,516,240</td>
<td align="right">10,458,460</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">30,207,900</td>
<td align="right">30,073,340</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">30,209,280</td>
<td align="right">30,074,720</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,589,220</td>
<td align="right">16,539,060</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">61,740</td>
<td align="right">61,560</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,783,840</td>
<td align="right">5,767,920</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,652,860</td>
<td align="right">38,573,320</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,917,000</td>
<td align="right">9,898,840</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">22,925,500</td>
<td align="right">22,885,340</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21,017,760</td>
<td align="right">21,001,660</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,947,380</td>
<td align="right">3,944,720</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,926,600</td>
<td align="right">1,925,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,365,660</td>
<td align="right">11,362,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,220,440</td>
<td align="right">3,220,200</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,440,860</td>
<td align="right">5,440,660</td>
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
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">19,401,480</td>
<td align="right">19,401,480</td>
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
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,918,100</td>
<td align="right">2,918,100</td>
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
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">840,600</td>
<td align="right">840,600</td>
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
<td align="left">MAP_ADD</td>
<td align="right">49,980</td>
<td align="right">49,980</td>
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
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">104,201,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">54,819,620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">5,454,100</td>
<td align="right"></td>
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
<td align="right">21,005,760</td>
<td align="right">30.2%</td>
<td align="right">20,989,680</td>
<td align="right">30.2%</td>
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
<td align="left">Failure</td>
<td align="right">11,800</td>
<td align="right">98.3%</td>
<td align="right">11,780</td>
<td align="right">98.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">200</td>
<td align="right">1.7%</td>
<td align="right">200</td>
<td align="right">1.7%</td>
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
<td align="left">add other</td>
<td align="right">3,220</td>
<td align="right">27.3%</td>
<td align="right">3,200</td>
<td align="right">27.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">4,980</td>
<td align="right">42.2%</td>
<td align="right">4,980</td>
<td align="right">42.3%</td>
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
<td align="right">12,104,700</td>
<td align="right">100.0%</td>
<td align="right">10,789,500</td>
<td align="right">100.0%</td>
<td align="right">-10.9%</td>
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
<td align="right">10,504,680</td>
<td align="right">9.8%</td>
<td align="right">10,446,700</td>
<td align="right">9.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,166,940</td>
<td align="right">2.0%</td>
<td align="right">2,164,100</td>
<td align="right">2.0%</td>
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
<td align="right">93,970,320</td>
<td align="right">88.1%</td>
<td align="right">93,971,400</td>
<td align="right">88.2%</td>
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
<td align="right">10,940</td>
<td align="right">20.9%</td>
<td align="right">11,140</td>
<td align="right">21.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,460</td>
<td align="right">79.1%</td>
<td align="right">41,400</td>
<td align="right">78.8%</td>
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
<td align="left">out of range</td>
<td align="right">7,600</td>
<td align="right">69.5%</td>
<td align="right">7,820</td>
<td align="right">70.2%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,760</td>
<td align="right">16.1%</td>
<td align="right">1,740</td>
<td align="right">15.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">720</td>
<td align="right">6.6%</td>
<td align="right">720</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">680</td>
<td align="right">6.2%</td>
<td align="right">680</td>
<td align="right">6.1%</td>
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
<td align="right">17,832,960</td>
<td align="right">3.1%</td>
<td align="right">17,620,680</td>
<td align="right">3.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,496,660</td>
<td align="right">3.1%</td>
<td align="right">17,288,400</td>
<td align="right">3.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">553,138,740</td>
<td align="right">96.9%</td>
<td align="right">553,361,880</td>
<td align="right">96.9%</td>
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
<td align="right">340,260</td>
<td align="right">100.0%</td>
<td align="right">336,240</td>
<td align="right">100.0%</td>
<td align="right">-1.2%</td>
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
<td align="right">12,199,080</td>
<td align="right">18.3%</td>
<td align="right">8,734,180</td>
<td align="right">13.8%</td>
<td align="right">-28.4%</td>
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
<td align="right">81.7%</td>
<td align="right">54,350,400</td>
<td align="right">86.1%</td>
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
<td align="right">5,560</td>
<td align="right">97.9%</td>
<td align="right">4,720</td>
<td align="right">97.5%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">2.1%</td>
<td align="right">120</td>
<td align="right">2.5%</td>
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
<td align="right">1,260</td>
<td align="right">22.7%</td>
<td align="right">860</td>
<td align="right">18.2%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,240</td>
<td align="right">40.3%</td>
<td align="right">1,880</td>
<td align="right">39.8%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,260</td>
<td align="right">22.7%</td>
<td align="right">1,180</td>
<td align="right">25.0%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">14.4%</td>
<td align="right">800</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45,308,280</td>
<td align="right">13.9%</td>
<td align="right">23,490,760</td>
<td align="right">13.0%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">242,653,180</td>
<td align="right">74.5%</td>
<td align="right">130,117,100</td>
<td align="right">72.3%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">37,776,560</td>
<td align="right">11.6%</td>
<td align="right">26,435,140</td>
<td align="right">14.7%</td>
<td align="right">-30.0%</td>
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
<td align="right">11,920</td>
<td align="right">1.6%</td>
<td align="right">6,540</td>
<td align="right">1.3%</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">712,740</td>
<td align="right">98.4%</td>
<td align="right">498,760</td>
<td align="right">98.7%</td>
<td align="right">-30.0%</td>
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
<td align="left">enumerate</td>
<td align="right">4,280</td>
<td align="right">35.9%</td>
<td align="right">1,460</td>
<td align="right">22.3%</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,600</td>
<td align="right">13.4%</td>
<td align="right">560</td>
<td align="right">8.6%</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">780</td>
<td align="right">6.5%</td>
<td align="right">400</td>
<td align="right">6.1%</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,840</td>
<td align="right">15.4%</td>
<td align="right">1,020</td>
<td align="right">15.6%</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,480</td>
<td align="right">20.8%</td>
<td align="right">2,160</td>
<td align="right">33.0%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">560</td>
<td align="right">4.7%</td>
<td align="right">560</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">220</td>
<td align="right">1.8%</td>
<td align="right">220</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">331,811,080</td>
<td align="right">30.1%</td>
<td align="right">278,871,540</td>
<td align="right">26.8%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">109,454,380</td>
<td align="right">9.9%</td>
<td align="right">101,961,320</td>
<td align="right">9.8%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">658,666,980</td>
<td align="right">59.8%</td>
<td align="right">660,365,900</td>
<td align="right">63.4%</td>
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
<td align="left">Success</td>
<td align="right">6,201,760</td>
<td align="right">99.6%</td>
<td align="right">5,203,120</td>
<td align="right">99.6%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">22,780</td>
<td align="right">0.4%</td>
<td align="right">21,140</td>
<td align="right">0.4%</td>
<td align="right">-7.2%</td>
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
<td align="right">11,000</td>
<td align="right">48.3%</td>
<td align="right">9,820</td>
<td align="right">46.5%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,600</td>
<td align="right">24.6%</td>
<td align="right">5,140</td>
<td align="right">24.3%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2,840</td>
<td align="right">12.5%</td>
<td align="right">2,840</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">640</td>
<td align="right">2.8%</td>
<td align="right">640</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">1.8%</td>
<td align="right">420</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">1.8%</td>
<td align="right">400</td>
<td align="right">1.9%</td>
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
<td align="right">0.8%</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">0.5%</td>
<td align="right">120</td>
<td align="right">0.6%</td>
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
<td align="right">319,303,320</td>
<td align="right">100.0%</td>
<td align="right">276,838,620</td>
<td align="right">100.0%</td>
<td align="right">-13.3%</td>
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
<td align="right">22,092,060</td>
<td align="right">18.0%</td>
<td align="right">20,478,500</td>
<td align="right">16.9%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,915,340</td>
<td align="right">43.8%</td>
<td align="right">53,915,360</td>
<td align="right">44.4%</td>
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
<td align="right">47,039,540</td>
<td align="right">38.2%</td>
<td align="right">47,039,540</td>
<td align="right">38.7%</td>
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
<td align="right">12,980</td>
<td align="right">1.3%</td>
<td align="right">12,580</td>
<td align="right">1.2%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,017,780</td>
<td align="right">98.7%</td>
<td align="right">1,017,800</td>
<td align="right">98.8%</td>
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
<td align="right">10,340</td>
<td align="right">79.7%</td>
<td align="right">9,940</td>
<td align="right">79.0%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">15.7%</td>
<td align="right">2,040</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,000</td>
<td align="right">7.7%</td>
<td align="right">1,000</td>
<td align="right">7.9%</td>
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
<td align="right">1.5%</td>
<td align="right">200</td>
<td align="right">1.6%</td>
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
<td align="right">11,378,560</td>
<td align="right">4.0%</td>
<td align="right">10,174,720</td>
<td align="right">3.6%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">269,386,040</td>
<td align="right">94.6%</td>
<td align="right">269,120,240</td>
<td align="right">95.0%</td>
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
<td align="right">3,779,500</td>
<td align="right">1.3%</td>
<td align="right">3,776,840</td>
<td align="right">1.3%</td>
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
<td align="right">215,520</td>
<td align="right">56.3%</td>
<td align="right">192,820</td>
<td align="right">53.6%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">167,000</td>
<td align="right">43.7%</td>
<td align="right">167,000</td>
<td align="right">46.4%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">3,415,423,700</td>
<td align="right">40.9%</td>
<td align="right">2,743,512,220</td>
<td align="right">38.8%</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">243,900,060</td>
<td align="right">2.9%</td>
<td align="right">208,096,280</td>
<td align="right">2.9%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">455,155,200</td>
<td align="right">5.4%</td>
<td align="right">389,455,720</td>
<td align="right">5.5%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">4,244,735,480</td>
<td align="right">50.8%</td>
<td align="right">3,726,311,860</td>
<td align="right">52.7%</td>
<td align="right">-12.2%</td>
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
<td align="right">45,308,280</td>
<td align="right">17.4%</td>
<td align="right">23,490,760</td>
<td align="right">10.5%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">12,199,080</td>
<td align="right">4.7%</td>
<td align="right">8,734,180</td>
<td align="right">3.9%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">12,104,700</td>
<td align="right">4.6%</td>
<td align="right">10,789,500</td>
<td align="right">4.8%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">22,092,060</td>
<td align="right">8.5%</td>
<td align="right">20,478,500</td>
<td align="right">9.1%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">109,454,380</td>
<td align="right">42.0%</td>
<td align="right">101,961,320</td>
<td align="right">45.4%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">17,496,660</td>
<td align="right">6.7%</td>
<td align="right">17,288,400</td>
<td align="right">7.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,504,680</td>
<td align="right">4.0%</td>
<td align="right">10,446,700</td>
<td align="right">4.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21,005,760</td>
<td align="right">8.1%</td>
<td align="right">20,989,680</td>
<td align="right">9.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,779,500</td>
<td align="right">1.5%</td>
<td align="right">3,776,840</td>
<td align="right">1.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,583,860</td>
<td align="right">1.8%</td>
<td align="right">4,583,860</td>
<td align="right">2.0%</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">18,888,680</td>
<td align="right">4.1%</td>
<td align="right">13,217,800</td>
<td align="right">3.4%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">18,887,880</td>
<td align="right">4.1%</td>
<td align="right">13,217,340</td>
<td align="right">3.4%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">132,973,760</td>
<td align="right">29.2%</td>
<td align="right">103,334,140</td>
<td align="right">26.5%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">100,609,520</td>
<td align="right">22.1%</td>
<td align="right">83,536,360</td>
<td align="right">21.4%</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">6,154,400</td>
<td align="right">1.4%</td>
<td align="right">5,547,560</td>
<td align="right">1.4%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,301,900</td>
<td align="right">7.8%</td>
<td align="right">31,957,560</td>
<td align="right">8.2%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">51,720,400</td>
<td align="right">11.4%</td>
<td align="right">49,825,900</td>
<td align="right">12.8%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,697,820</td>
<td align="right">2.1%</td>
<td align="right">9,582,520</td>
<td align="right">2.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,912,160</td>
<td align="right">11.8%</td>
<td align="right">53,912,180</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,565,220</td>
<td align="right">1.7%</td>
<td align="right">7,565,220</td>
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
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,383,960</td>
<td align="right">11.1%</td>
<td align="right">39,304,420</td>
<td align="right">11.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,387,440</td>
<td align="right">11.1%</td>
<td align="right">39,307,900</td>
<td align="right">11.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,695,300</td>
<td align="right">11.2%</td>
<td align="right">39,615,760</td>
<td align="right">11.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,695,300</td>
<td align="right">11.2%</td>
<td align="right">39,615,760</td>
<td align="right">11.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,530,880</td>
<td align="right">88.5%</td>
<td align="right">313,610,420</td>
<td align="right">88.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">314,724,520</td>
<td align="right">88.8%</td>
<td align="right">314,804,060</td>
<td align="right">88.8%</td>
<td align="right">0.0%</td>
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
<td align="left">Mortal decrefs</td>
<td align="right">1,757,202,220</td>
<td align="right">20.7%</td>
<td align="right">2,474,567,760</td>
<td align="right">27.5%</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,004,792,293</td>
<td align="right">26.3%</td>
<td align="right">2,696,420,948</td>
<td align="right">33.7%</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">970,373,640</td>
<td align="right">12.7%</td>
<td align="right">715,885,900</td>
<td align="right">9.0%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,356,433,304</td>
<td align="right">16.0%</td>
<td align="right">1,695,725,534</td>
<td align="right">18.9%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,331,861,400</td>
<td align="right">15.7%</td>
<td align="right">1,092,094,660</td>
<td align="right">12.1%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,431,351,089</td>
<td align="right">18.8%</td>
<td align="right">1,668,195,178</td>
<td align="right">20.9%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,939,083</td>
<td align="right"></td>
<td align="right">2,485,406</td>
<td align="right"></td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">3,210,638,500</td>
<td align="right">42.2%</td>
<td align="right">2,914,672,460</td>
<td align="right">36.5%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">4,048,663,800</td>
<td align="right">47.7%</td>
<td align="right">3,726,971,320</td>
<td align="right">41.5%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">44,001,839</td>
<td align="right"></td>
<td align="right">41,471,406</td>
<td align="right"></td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">41,823,897</td>
<td align="right"></td>
<td align="right">39,747,433</td>
<td align="right"></td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">487,440</td>
<td align="right">0.1%</td>
<td align="right">500,140</td>
<td align="right">0.1%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">462,719,643</td>
<td align="right"></td>
<td align="right">451,373,967</td>
<td align="right"></td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">197,788,337</td>
<td align="right"></td>
<td align="right">196,100,354</td>
<td align="right"></td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">344,040</td>
<td align="right">0.1%</td>
<td align="right">344,680</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">316,943,520</td>
<td align="right">47.0%</td>
<td align="right">316,784,220</td>
<td align="right">47.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">317,775,000</td>
<td align="right">47.1%</td>
<td align="right">317,629,040</td>
<td align="right">47.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">354,023,448</td>
<td align="right"></td>
<td align="right">353,912,504</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">356,567,660</td>
<td align="right">52.9%</td>
<td align="right">356,652,720</td>
<td align="right">52.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">356,575,640</td>
<td align="right"></td>
<td align="right">356,656,380</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
<td align="right">26,020</td>
<td align="right">73,050,040</td>
<td align="right">1,152,207,149</td>
<td align="right">45,336,140</td>
<td align="right">99,588,260</td>
<td align="right">25,940</td>
<td align="right">73,080,840</td>
<td align="right">1,149,961,967</td>
<td align="right">44,663,460</td>
<td align="right">100,213,160</td>
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
