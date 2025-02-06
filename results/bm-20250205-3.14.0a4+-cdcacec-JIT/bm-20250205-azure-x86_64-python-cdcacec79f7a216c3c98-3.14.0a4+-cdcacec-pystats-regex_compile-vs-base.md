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
<td align="left">STORE_SUBSCR</td>
<td align="right">21,222,120</td>
<td align="right">704,780</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">24,411,060</td>
<td align="right">1,634,400</td>
<td align="right">-93.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">8,037,480</td>
<td align="right">1,768,220</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">9,163,140</td>
<td align="right">2,022,440</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,703,140</td>
<td align="right">857,860</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">8,465,160</td>
<td align="right">2,412,500</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,369,900</td>
<td align="right">5,511,540</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">44,887,800</td>
<td align="right">16,062,400</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">9,477,480</td>
<td align="right">3,436,360</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">46,043,400</td>
<td align="right">17,332,080</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">10,714,980</td>
<td align="right">4,228,300</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">11,415,840</td>
<td align="right">4,640,980</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">12,708,360</td>
<td align="right">5,190,400</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">83,454,720</td>
<td align="right">35,071,540</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,083,420</td>
<td align="right">463,080</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">4,087,560</td>
<td align="right">1,945,020</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">33,183,360</td>
<td align="right">16,045,380</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">10,367,520</td>
<td align="right">5,072,920</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">14,294,340</td>
<td align="right">7,014,700</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">210,240</td>
<td align="right">105,000</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">37,589,220</td>
<td align="right">18,915,000</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">4,732,680</td>
<td align="right">2,391,460</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">31,269,960</td>
<td align="right">16,267,240</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,093,840</td>
<td align="right">3,228,340</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">5,816,340</td>
<td align="right">3,101,620</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">409,920</td>
<td align="right">220,200</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">4,339,200</td>
<td align="right">2,374,180</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">219,626,160</td>
<td align="right">123,126,100</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">695,760</td>
<td align="right">392,920</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">63,490,080</td>
<td align="right">35,983,300</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">7,406,280</td>
<td align="right">4,263,880</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">11,783,100</td>
<td align="right">6,787,440</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">16,895,760</td>
<td align="right">10,005,560</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,459,260</td>
<td align="right">870,260</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">7,052,260</td>
<td align="right">4,222,140</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">1,677,840</td>
<td align="right">1,011,120</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">54,357,900</td>
<td align="right">33,575,100</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">29,511,120</td>
<td align="right">19,100,840</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">4,677,360</td>
<td align="right">3,089,560</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,129,840</td>
<td align="right">8,081,400</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">518,880</td>
<td align="right">347,040</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">2,072,520</td>
<td align="right">1,390,260</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">10,566,960</td>
<td align="right">7,091,200</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">6,395,680</td>
<td align="right">4,330,800</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">14,891,400</td>
<td align="right">10,144,720</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,681,180</td>
<td align="right">2,513,020</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,859,180</td>
<td align="right">1,271,900</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">26,332,500</td>
<td align="right">18,272,720</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,314,660</td>
<td align="right">932,560</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">219,240</td>
<td align="right">157,500</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">9,898,800</td>
<td align="right">7,130,420</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,750,420</td>
<td align="right">7,324,380</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">3,397,200</td>
<td align="right">2,607,880</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,742,800</td>
<td align="right">2,895,080</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,917,100</td>
<td align="right">5,403,460</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,905,020</td>
<td align="right">2,272,720</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,281,680</td>
<td align="right">1,004,220</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,740,420</td>
<td align="right">1,367,580</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,681,080</td>
<td align="right">1,347,720</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">26,009,820</td>
<td align="right">20,876,980</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,875,860</td>
<td align="right">2,325,040</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,986,340</td>
<td align="right">5,788,840</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">9,503,160</td>
<td align="right">7,923,940</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">933,480</td>
<td align="right">779,340</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,248,740</td>
<td align="right">1,907,260</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,207,220</td>
<td align="right">1,906,400</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">936,720</td>
<td align="right">821,880</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">754,880</td>
<td align="right">670,540</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,004,040</td>
<td align="right">901,900</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">6,396,420</td>
<td align="right">5,780,240</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,345,380</td>
<td align="right">1,225,200</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,046,060</td>
<td align="right">4,783,260</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">3,186,660</td>
<td align="right">3,154,560</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">339,600</td>
<td align="right">337,720</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,866,060</td>
<td align="right">1,863,900</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">36,954,240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">31,790,160</td>
<td align="right">31,790,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,866,420</td>
<td align="right">4,866,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,459,260</td>
<td align="right">1,459,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">875,000</td>
<td align="right">875,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">679,860</td>
<td align="right">679,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">671,280</td>
<td align="right">671,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">598,680</td>
<td align="right">598,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">531,000</td>
<td align="right">531,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">503,460</td>
<td align="right">503,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">448,800</td>
<td align="right">448,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">424,620</td>
<td align="right">424,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">424,620</td>
<td align="right">424,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">424,620</td>
<td align="right">424,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">338,280</td>
<td align="right">338,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">336,420</td>
<td align="right">336,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">333,360</td>
<td align="right">333,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">300,720</td>
<td align="right">300,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">220,020</td>
<td align="right">220,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">167,820</td>
<td align="right">167,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">122,040</td>
<td align="right">122,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">79,920</td>
<td align="right">79,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">59,880</td>
<td align="right">59,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">38,940</td>
<td align="right">38,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">33,840</td>
<td align="right">33,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">25,200</td>
<td align="right">25,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">24,420</td>
<td align="right">24,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">24,420</td>
<td align="right">24,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">4,080</td>
<td align="right">4,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">15,604,620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">4,131,220</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">1,092,680</td>
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
<td align="right">754,380</td>
<td align="right">3.3%</td>
<td align="right">670,060</td>
<td align="right">2.9%</td>
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
<td align="right">22,071,120</td>
<td align="right">96.7%</td>
<td align="right">22,071,120</td>
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
<td align="right">480</td>
<td align="right">96.0%</td>
<td align="right">460</td>
<td align="right">95.8%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">4.0%</td>
<td align="right">20</td>
<td align="right">4.2%</td>
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
<td align="right">60</td>
<td align="right">12.5%</td>
<td align="right">40</td>
<td align="right">8.7%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">200</td>
<td align="right">41.7%</td>
<td align="right">200</td>
<td align="right">43.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">120</td>
<td align="right">25.0%</td>
<td align="right">120</td>
<td align="right">26.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">60</td>
<td align="right">12.5%</td>
<td align="right">60</td>
<td align="right">13.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">40</td>
<td align="right">8.3%</td>
<td align="right">40</td>
<td align="right">8.7%</td>
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
<td align="right">409,920</td>
<td align="right">100.0%</td>
<td align="right">220,200</td>
<td align="right">100.0%</td>
<td align="right">-46.3%</td>
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
<td align="right">1,281,180</td>
<td align="right">5.5%</td>
<td align="right">1,003,800</td>
<td align="right">4.4%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">20,916,180</td>
<td align="right">89.7%</td>
<td align="right">20,916,180</td>
<td align="right">90.7%</td>
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
<td align="right">1,131,220</td>
<td align="right">4.8%</td>
<td align="right">1,131,220</td>
<td align="right">4.9%</td>
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
<td align="right">480</td>
<td align="right">2.2%</td>
<td align="right">400</td>
<td align="right">1.8%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">21,360</td>
<td align="right">97.8%</td>
<td align="right">21,360</td>
<td align="right">98.2%</td>
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
<td align="right">240</td>
<td align="right">50.0%</td>
<td align="right">160</td>
<td align="right">40.0%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">120</td>
<td align="right">25.0%</td>
<td align="right">120</td>
<td align="right">30.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">40</td>
<td align="right">8.3%</td>
<td align="right">40</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">40</td>
<td align="right">8.3%</td>
<td align="right">40</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">40</td>
<td align="right">8.3%</td>
<td align="right">40</td>
<td align="right">10.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">38,220</td>
<td align="right">0.1%</td>
<td align="right">38,220</td>
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
<td align="right">72,126,600</td>
<td align="right">99.9%</td>
<td align="right">72,126,600</td>
<td align="right">99.9%</td>
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
<td align="right">38,940</td>
<td align="right">0.1%</td>
<td align="right">38,940</td>
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
<td align="right">980</td>
<td align="right">100.0%</td>
<td align="right">980</td>
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
<td align="right">869,820</td>
<td align="right">6.7%</td>
<td align="right">869,820</td>
<td align="right">6.7%</td>
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
<td align="right">12,023,580</td>
<td align="right">92.3%</td>
<td align="right">12,023,580</td>
<td align="right">92.3%</td>
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
<td align="right">123,960</td>
<td align="right">1.0%</td>
<td align="right">123,960</td>
<td align="right">1.0%</td>
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
<td align="right">2,340</td>
<td align="right">31.1%</td>
<td align="right">2,340</td>
<td align="right">31.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,180</td>
<td align="right">68.9%</td>
<td align="right">5,180</td>
<td align="right">68.9%</td>
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
<td align="right">4,900</td>
<td align="right">94.6%</td>
<td align="right">4,900</td>
<td align="right">94.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">80</td>
<td align="right">1.5%</td>
<td align="right">80</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">80</td>
<td align="right">1.5%</td>
<td align="right">80</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">80</td>
<td align="right">1.5%</td>
<td align="right">80</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
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
<td align="right">6,394,020</td>
<td align="right">41.1%</td>
<td align="right">4,329,660</td>
<td align="right">32.1%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,160,920</td>
<td align="right">58.9%</td>
<td align="right">9,160,920</td>
<td align="right">67.9%</td>
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
<td align="right">1,660</td>
<td align="right">100.0%</td>
<td align="right">1,140</td>
<td align="right">100.0%</td>
<td align="right">-31.3%</td>
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
<td align="left">str</td>
<td align="right">1,640</td>
<td align="right">98.8%</td>
<td align="right">1,120</td>
<td align="right">98.2%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">20</td>
<td align="right">1.2%</td>
<td align="right">20</td>
<td align="right">1.8%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,254,820</td>
<td align="right">89.9%</td>
<td align="right">5,360,560</td>
<td align="right">85.4%</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,691,740</td>
<td align="right">9.7%</td>
<td align="right">853,940</td>
<td align="right">13.6%</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">152,600</td>
<td align="right">0.4%</td>
<td align="right">57,240</td>
<td align="right">0.9%</td>
<td align="right">-62.5%</td>
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
<td align="right">11,400</td>
<td align="right">79.8%</td>
<td align="right">3,920</td>
<td align="right">78.4%</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,880</td>
<td align="right">20.2%</td>
<td align="right">1,080</td>
<td align="right">21.6%</td>
<td align="right">-62.5%</td>
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
<td align="right">11,280</td>
<td align="right">98.9%</td>
<td align="right">3,800</td>
<td align="right">96.9%</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">1.0%</td>
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
<td align="right">6,977,220</td>
<td align="right">11.9%</td>
<td align="right">5,780,020</td>
<td align="right">10.1%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,780,240</td>
<td align="right">88.1%</td>
<td align="right">51,660,060</td>
<td align="right">89.9%</td>
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
<td align="left">Failure</td>
<td align="right">1,920</td>
<td align="right">89.7%</td>
<td align="right">1,620</td>
<td align="right">88.0%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">220</td>
<td align="right">10.3%</td>
<td align="right">220</td>
<td align="right">12.0%</td>
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
<td align="right">180</td>
<td align="right">9.4%</td>
<td align="right">140</td>
<td align="right">8.6%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,420</td>
<td align="right">74.0%</td>
<td align="right">1,160</td>
<td align="right">71.6%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">160</td>
<td align="right">8.3%</td>
<td align="right">160</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">80</td>
<td align="right">4.2%</td>
<td align="right">80</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">2.1%</td>
<td align="right">40</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">20</td>
<td align="right">1.0%</td>
<td align="right">20</td>
<td align="right">1.2%</td>
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
<td align="right">87,541,260</td>
<td align="right">100.0%</td>
<td align="right">49,620,480</td>
<td align="right">100.0%</td>
<td align="right">-43.3%</td>
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
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">120</td>
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
<td align="right">14,294,340</td>
<td align="right">100.0%</td>
<td align="right">14,294,340</td>
<td align="right">100.0%</td>
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
<td align="right">33,840</td>
<td align="right">100.0%</td>
<td align="right">33,840</td>
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
<td align="right">21,216,780</td>
<td align="right">89.8%</td>
<td align="right">704,440</td>
<td align="right">22.6%</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,410,800</td>
<td align="right">10.2%</td>
<td align="right">2,410,800</td>
<td align="right">77.4%</td>
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
<td align="right">5,340</td>
<td align="right">100.0%</td>
<td align="right">340</td>
<td align="right">100.0%</td>
<td align="right">-93.6%</td>
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
<td align="left">bytearray int</td>
<td align="right">5,200</td>
<td align="right">97.4%</td>
<td align="right">200</td>
<td align="right">58.8%</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">60</td>
<td align="right">1.1%</td>
<td align="right">60</td>
<td align="right">17.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">40</td>
<td align="right">0.7%</td>
<td align="right">40</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">40</td>
<td align="right">0.7%</td>
<td align="right">40</td>
<td align="right">11.8%</td>
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
<td align="right">1,734,940</td>
<td align="right">6.0%</td>
<td align="right">1,362,160</td>
<td align="right">4.7%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">137,360</td>
<td align="right">0.5%</td>
<td align="right">135,980</td>
<td align="right">0.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">27,276,900</td>
<td align="right">93.6%</td>
<td align="right">27,260,040</td>
<td align="right">94.8%</td>
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
<td align="right">2,620</td>
<td align="right">32.5%</td>
<td align="right">2,580</td>
<td align="right">32.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,440</td>
<td align="right">67.5%</td>
<td align="right">5,400</td>
<td align="right">67.7%</td>
<td align="right">-0.7%</td>
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
<td align="left">mapping</td>
<td align="right">300</td>
<td align="right">5.5%</td>
<td align="right">220</td>
<td align="right">4.1%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,120</td>
<td align="right">20.6%</td>
<td align="right">1,160</td>
<td align="right">21.5%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,780</td>
<td align="right">69.5%</td>
<td align="right">3,780</td>
<td align="right">70.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">180</td>
<td align="right">3.3%</td>
<td align="right">180</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">40</td>
<td align="right">0.7%</td>
<td align="right">40</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">0.4%</td>
<td align="right">20</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,231,900</td>
<td align="right">100.0%</td>
<td align="right">12,231,900</td>
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
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
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
<td align="right">43,403,420</td>
<td align="right">3.7%</td>
<td align="right">15,854,060</td>
<td align="right">2.5%</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">462,279,880</td>
<td align="right">39.9%</td>
<td align="right">235,331,600</td>
<td align="right">37.1%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">652,617,180</td>
<td align="right">56.3%</td>
<td align="right">381,343,380</td>
<td align="right">60.1%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,584,080</td>
<td align="right">0.1%</td>
<td align="right">1,487,480</td>
<td align="right">0.2%</td>
<td align="right">-6.1%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">21,216,780</td>
<td align="right">48.9%</td>
<td align="right">704,440</td>
<td align="right">4.4%</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,691,740</td>
<td align="right">8.5%</td>
<td align="right">853,940</td>
<td align="right">5.4%</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">409,920</td>
<td align="right">0.9%</td>
<td align="right">220,200</td>
<td align="right">1.4%</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">6,394,020</td>
<td align="right">14.7%</td>
<td align="right">4,329,660</td>
<td align="right">27.3%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,281,180</td>
<td align="right">3.0%</td>
<td align="right">1,003,800</td>
<td align="right">6.3%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,734,940</td>
<td align="right">4.0%</td>
<td align="right">1,362,160</td>
<td align="right">8.6%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,977,220</td>
<td align="right">16.1%</td>
<td align="right">5,780,020</td>
<td align="right">36.4%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">754,380</td>
<td align="right">1.7%</td>
<td align="right">670,060</td>
<td align="right">4.2%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">869,820</td>
<td align="right">2.0%</td>
<td align="right">869,820</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">38,220</td>
<td align="right">0.1%</td>
<td align="right">38,220</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">152,600</td>
<td align="right">9.6%</td>
<td align="right">57,240</td>
<td align="right">3.8%</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">112,100</td>
<td align="right">7.1%</td>
<td align="right">110,720</td>
<td align="right">7.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">957,120</td>
<td align="right">60.4%</td>
<td align="right">957,120</td>
<td align="right">64.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">174,100</td>
<td align="right">11.0%</td>
<td align="right">174,100</td>
<td align="right">11.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">123,960</td>
<td align="right">7.8%</td>
<td align="right">123,960</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">38,940</td>
<td align="right">2.5%</td>
<td align="right">38,940</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">19,080</td>
<td align="right">1.2%</td>
<td align="right">19,080</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">6,180</td>
<td align="right">0.4%</td>
<td align="right">6,180</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">140</td>
<td align="right">0.0%</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">5,805,540</td>
<td align="right">18.6%</td>
<td align="right">5,805,540</td>
<td align="right">18.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">25,464,420</td>
<td align="right">81.4%</td>
<td align="right">25,464,420</td>
<td align="right">81.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">5,805,540</td>
<td align="right">18.6%</td>
<td align="right">5,805,540</td>
<td align="right">18.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">5,805,540</td>
<td align="right">18.6%</td>
<td align="right">5,805,540</td>
<td align="right">18.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">5,805,540</td>
<td align="right">18.6%</td>
<td align="right">5,805,540</td>
<td align="right">18.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">5,610,060</td>
<td align="right">17.9%</td>
<td align="right">5,610,060</td>
<td align="right">17.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">2,302,740</td>
<td align="right">7.4%</td>
<td align="right">2,302,740</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">32,729,220</td>
<td align="right">104.7%</td>
<td align="right">32,729,220</td>
<td align="right">104.7%</td>
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
<td align="right">74,214,118</td>
<td align="right">10.3%</td>
<td align="right">282,175,560</td>
<td align="right">37.4%</td>
<td align="right">280.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">93,346,183</td>
<td align="right">10.4%</td>
<td align="right">285,032,209</td>
<td align="right">29.9%</td>
<td align="right">205.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">84,190,791</td>
<td align="right">9.4%</td>
<td align="right">206,358,953</td>
<td align="right">21.6%</td>
<td align="right">145.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">72,592,296</td>
<td align="right">10.1%</td>
<td align="right">133,485,082</td>
<td align="right">17.7%</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">160,370,340</td>
<td align="right">22.2%</td>
<td align="right">88,918,780</td>
<td align="right">11.8%</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">414,989,960</td>
<td align="right">57.5%</td>
<td align="right">248,905,800</td>
<td align="right">33.0%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">269,198,460</td>
<td align="right">30.0%</td>
<td align="right">163,320,020</td>
<td align="right">17.1%</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">449,246,460</td>
<td align="right">50.1%</td>
<td align="right">299,439,540</td>
<td align="right">31.4%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">44</td>
<td align="right"></td>
<td align="right">34</td>
<td align="right"></td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">43</td>
<td align="right"></td>
<td align="right">47</td>
<td align="right"></td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">79</td>
<td align="right"></td>
<td align="right">72</td>
<td align="right"></td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">29,940</td>
<td align="right">0.1%</td>
<td align="right">31,260</td>
<td align="right">0.1%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
<td align="right">1,620</td>
<td align="right">0.0%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,860,480</td>
<td align="right">30.7%</td>
<td align="right">16,861,900</td>
<td align="right">30.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">18,916,465</td>
<td align="right"></td>
<td align="right">18,917,969</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,024,477</td>
<td align="right"></td>
<td align="right">7,024,173</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">38,075,340</td>
<td align="right"></td>
<td align="right">38,075,860</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">38,075,400</td>
<td align="right">69.3%</td>
<td align="right">38,075,920</td>
<td align="right">69.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">14,153,456</td>
<td align="right"></td>
<td align="right">14,153,386</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">16,828,980</td>
<td align="right">30.6%</td>
<td align="right">16,829,020</td>
<td align="right">30.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,459,260</td>
<td align="right"></td>
<td align="right">1,459,260</td>
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
